from datetime import timedelta
from secrets import token_hex
from config import lang
from airbnb import Api
from flask import (
    Flask,
    jsonify,
    request,
    redirect,
    send_file,
    make_response,
    render_template
)

app = Flask(__name__)
app.config.update(
    SECRET_KEY = token_hex(16),
    SESSION_COOKIE_NAME = "lang",
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = "Strict",
    SESSION_COOKIE_DOMAIN = ".garbatella-elegant-aparment.com"
)
app.template_folder = "templates/min"

@app.get("/")
def index():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("index.min.html", lang = lang[user_lang]["index"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/more-info")
def more_info():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("more-info.min.html", lang = lang[user_lang]["more-info"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/book-holiday-home")
def book_holiday_home():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("book-holiday-home.min.html", lang = lang[user_lang]["book-holiday-home"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("tourist-tax-payment.min.html", lang = lang[user_lang]["tourist-tax-payment"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/thanks")
def thanks():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("thanks.min.html", lang = lang[user_lang]["thanks"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

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

@app.post("/")
@app.post("/more-info")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def change_language():
    response = make_response(redirect(request.referrer))
    response.set_cookie("lang", request.form.get("lang"))
    return response

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