from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year

    # Check if the birthday has occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        try:
            year = int(request.form["year"])
            month = int(request.form["month"])
            day = int(request.form["day"])

            birthdate = datetime(year, month, day)
            age = calculate_age(birthdate)
        except ValueError:
            age = "Invalid date! Please enter a valid date."

    return render_template("index.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)