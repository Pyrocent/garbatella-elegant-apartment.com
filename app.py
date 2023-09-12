from secrets import token_hex
from config import lang
from flask import (
    Flask,
    session,
    request,
    redirect,
    send_file,
    render_template
)

app = Flask(__name__)
app.secret_key = token_hex(16)

@app.get("/")
def index():
    return render_template(
        "min/index.min.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["index"]
    )

@app.get("/book-holiday-home")
def book_holiday_home():
    return render_template(
        "min/book-holiday-home.min.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["book-holiday-home"]
    )

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    return render_template(
        "min/tourist-tax-payment.min.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]["tourist-tax-payment"]
    )

@app.post("/")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def _():
    session["lang"] = request.form.get("lang")
    return "", 200

@app.get("/robots.txt")
def robots():
    return send_file("robots.txt")

@app.get("/sitemap.xml")
def sitemaps():
    return send_file("sitemap.xml")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_):
    return redirect("/")

if __name__ == "__main__": app.run(debug = True)