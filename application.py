import cs50

from flask import Flask, flash, jsonify, redirect, render_template, request
from helpers import error

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.template_filter('usd')
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


# Get index page for splits, accept spot submissions
@app.route("/", methods=["GET", "POST"])
def index():

    # generate index template with form
    if request.method == "GET":
        return render_template("/index.html")

    # collect user input in the form
    if request.method == "POST":

        # check that arguments entered
        if not request.form.get("total") or not request.form.get("splits") or not request.form.get("tip"):
            return error("Form incomplete please retry.")

        # store form data into variables
        total = request.form.get("total")
        splits = request.form.get("splits")
        tip = request.form.get("tip")

        # check valid usage of the splitter
        if not total.replace('.', '', 1).isdigit():
            return error("Please enter a valid bill amount without dollar sign")
        if not splits.isdigit():
            return error("Please enter a valid number of splits")
        if not tip.isdigit():
            return error("Please enter a valid tip amount")

        # cast variables
        splits = int(splits)
        tip = int(tip)
        bill = float(total)
        total = round((float(total) * 100) * (1 + (tip / 100)))
        rem = total % splits
        splitdict = {}

        for i in range(splits):
            splitdict[i] = (total // splits) / 100

        for i in range(rem):
            splitdict[i] = splitdict[i] + .01

        total = total / 100
        tip = bill * (tip / 100)

        return render_template("/splits.html", splitdict=splitdict, splits=splits, tip=tip, total=total)