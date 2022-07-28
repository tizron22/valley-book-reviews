from flask import render_template
from valleybookreviews import app, db
from valleybookreviews.models import User


@app.route("/")
def home():
    return render_template("base.html")
