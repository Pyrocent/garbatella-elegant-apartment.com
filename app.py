from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book")
def play():
    return render_template("book.html")

if __name__ == "__main__": app.run(debug = True)