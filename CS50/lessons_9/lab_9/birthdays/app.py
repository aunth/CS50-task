from importlib.metadata import requires
import os

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


db = sqlite3.connect("./birthdays.db", check_same_thread=False)
cursor = db.cursor()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        if valid_month(month) and valid_day(day):
            cursor.execute("INSERT INTO birthdays(name, month, day) values(?, ?, ?)", (name, int(month), int(day)))
            db.commit()
        else:
            return render_template("failed.html")
        return redirect("/")

    else:
        user_info = cursor.execute("SELECT name, month, day FROM birthdays")
        db.commit()
        return render_template("index.html", user_info=user_info)

def valid_month(month):
    try:
        a = int(month)
        if not (1 <= a <= 12):
            raise TypeError
        return True
    except TypeError:
        return False


def valid_day(day):
    try:
        day = int(day)
        if not(1 <= day <= 31):
            raise TypeError
        return True
    except TypeError:
        return False
    


