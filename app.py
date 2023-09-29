from secrets import token_hex
from config import lang
from airbnb import Api
from flask import (
    Flask,
    jsonify,
    session,
    request,
    redirect,
    send_file,
    render_template
)

app = Flask(__name__)
app.config.update(
    SECRET_KEY = token_hex(16),
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = "Strict",
)
app.template_folder = "templates/min"

@app.get("/")
def index():
    return render_template("index.min.html", lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["index"])

@app.get("/more-info")
def more_info():
    return render_template("more-info.min.html", lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["more-info"])

@app.get("/book-holiday-home")
def book_holiday_home():
    return render_template("book-holiday-home.min.html", lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["book-holiday-home"])

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    return render_template("tourist-tax-payment.min.html", lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["tourist-tax-payment"])

@app.get("/thanks")
def thanks():
    return render_template("thanks.min.html", lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["thanks"])

@app.post("/")
@app.post("/more-info")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def change_language():
    session["lang"] = request.form.get("lang")
    return redirect(request.referrer)

@app.post("/disable_days")
def disable_days():
    days = []
    only_checkout = None
    for month in Api(randomize = True).get_calendar("940534339344086732")["calendar_months"]:
        for day in month["days"]:
            if day["available"] == True:
                only_checkout = True
            else:
                if only_checkout == True:
                    only_checkout = False
                else:
                    days.append(day["date"])

    return jsonify(days)

@app.get("/robots.txt")
def robots():
    return send_file("robots.txt")

@app.get("/sitemap.xml")
def sitemap():
    return send_file("sitemap.xml")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_):
    return redirect("/")

if __name__ == "__main__": app.run(debug = True)