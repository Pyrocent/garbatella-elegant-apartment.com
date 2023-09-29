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
    make_response,
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
    response = make_response(render_template("index.min.html"))
    response.set_cookie("lang", lang[request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["index"])
    return response

@app.get("/more-info")
def more_info():
    response = make_response(render_template("more-info.min.html"))
    response.set_cookie("lang", lang[request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["more-info"])
    return response

@app.get("/book-holiday-home")
def book_holiday_home():
    response = make_response(render_template("book-holiday-home.min.html"))
    response.set_cookie("lang", lang[request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["book-holiday-home"])
    return response

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    response = make_response(render_template("tourist-tax-payment.min.html"))
    response.set_cookie("lang", lang[request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["tourist-tax-payment"])
    return response

@app.get("/thanks")
def thanks():
    response = make_response(render_template("thanks.min.html"))
    response.set_cookie("lang", lang[request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["thanks"])
    return response

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