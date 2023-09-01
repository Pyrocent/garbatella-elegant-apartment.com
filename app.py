from flask import (
    Flask,
    redirect,
    send_file,
    render_template
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book")
def play():
    return render_template("book.html")

@app.route("/robots")
def robots():
    return send_file("robots.txt")

@app.route("/sitemap")
def sitemaps():
    return send_file("sitemap.txt")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_):
    return redirect("/")

if __name__ == "__main__": app.run(debug = True)