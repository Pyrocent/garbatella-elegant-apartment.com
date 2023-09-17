from flask import (
    Flask,
    request,
    redirect,
    send_file,
    render_template
)

app = Flask(__name__)

@app.get("/")
def index():
    request.accept_languages.best_match(["de_DE", "en_GB", "en_US", "es_ES", "fr_FR", "it_IT"], default = "en_US")
    
    return render_template("index.min.html")

@app.get("/book-holiday-home")
def book_holiday_home():
    return render_template("book-holiday-home.min.html")

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    return render_template("tourist-tax-payment.min.html")

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