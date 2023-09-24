from secrets import token_hex
from config import lang
from airbnb import Api
from flask import (
    g,
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

@app.before_request
def before_request():
    g.lang = lang[session.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))]

@app.get("/")
def index():
    return render_template("index.min.html", lang = g.lang["index"])

@app.get("/book-holiday-home")
def book_holiday_home():
    return render_template("book-holiday-home.min.html", lang = g.lang["book-holiday-home"])

@app.get("/tourist-tax-payment")
def tourist_tax_payment():
    return render_template("tourist-tax-payment.min.html", lang = g.lang["tourist-tax-payment"])

@app.post("/")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def change_language():
    session["lang"] = request.form.get("lang")
    return redirect(request.referrer)

@app.post("/disable_days")
def disable_days():
    days = []
    for month in Api(randomize = True).get_calendar("940534339344086732")["calendar_months"]:
        for day in month["days"]:
            if day["available"] == False:
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

# from requests import get
# from bs4 import BeautifulSoup
# from datetime import datetime, timedelta

# today = datetime.now()
# one_year_from_today = today + timedelta(days = 365)

# while today <= one_year_from_today:
#     page_content = get(f"https://www.airbnb.it/s/Roma/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-09-24&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=1&channel=EXPLORE&date_picker_type=calendar&checkout={today.strftime('%Y-%m-%d')}&source=structured_search_input_header&search_type=user_map_move&query=Roma%2C%20RM&place_id=ChIJu46S-ZZhLxMROG5lkwZ3D7k&ne_lat=41.865437039685204&ne_lng=12.495719843478298&sw_lat=41.86453384175038&sw_lng=12.494547739682048&zoom=18.869290362301008&zoom_level=18.869290362301008&search_by_map=true").content
#     soup = BeautifulSoup(page_content, "html.parser")

#     if soup.find(class_ = "t6mzqp7 dir dir-ltr").get_text() == "Garbatella Elegant Apartament":
#         print(today.strftime("%Y-%m-%d"), "OKAY")
#     else:
#         print(soup.find(class_ = "t6mzqp7 dir dir-ltr").get_text())

#     today += timedelta(days = 1)