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

app = Flask(__name__, template_folder = "app/templates", static_folder = "app/static")
app.config.update(
    SECRET_KEY = token_hex(16),
    SESSION_COOKIE_NAME = "lang",
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = "Strict",
    SESSION_COOKIE_DOMAIN = ".garbatella-elegant-apartment.com"
)

@app.get("/")
def index():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("index.html", lang = lang[user_lang]["index"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/more/<tab>")
def more(tab):
    if tab == "home" or tab == "neighborhood":
        user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
        response = make_response(render_template("more.html", lang = lang[user_lang]["more"], tab = tab))
        response.set_cookie("lang", user_lang, timedelta(weeks = 52))
        return response
    else:
        return redirect("/")

@app.get("/book-holiday-home")
def book_holiday_home():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("book-holiday-home.html", lang = lang[user_lang]["book-holiday-home"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("tourist-tax-payment.html", lang = lang[user_lang]["tourist-tax-payment"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/thanks")
def thanks():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("thanks.html", lang = lang[user_lang]["thanks"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.post("/disable_days")
def disable_days():
    days = []
    only_checkout = None
    for month in Api(randomize = True).get_calendar("1103438586972971737")["calendar_months"]:
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
@app.post("/more/home")
@app.post("/more/neighborhood")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def change_language():
    response = make_response(redirect(request.referrer))
    response.set_cookie("lang", request.form.get("lang"))
    return response

@app.get("/robots.txt")
@app.get("/sitemap.xml")
def serve_file(): return send_file(f"./{request.path}")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_): return redirect("/")

if __name__ == "__main__": app.run()