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
app.secret_key = "key"

@app.get("/")
def index():
    return render_template(
        "index.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "en"))]["index"]
    )

@app.get("/book-holiday-home")
def book_holiday_home():
    return render_template(
        "book-holiday-home.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "en"))]["book-holiday-home"]
    )

@app.get("/city-tax-payment")
def city_tax_payment():
    return render_template(
        "city-tax-payment.html",
        lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "en"))]["city-tax-payment"]
    )

@app.post("/")
@app.post("/book-holiday-home")
@app.post("/city-tax-payment")
def _():
    session["lang"] = request.form.get("lang")

@app.route("/robots.txt")
def robots():
    return send_file("robots.txt")

@app.route("/sitemap.xml")
def sitemaps():
    return send_file("sitemap.txt")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_):
    return redirect("/")

if __name__ == "__main__": app.run(debug = True)