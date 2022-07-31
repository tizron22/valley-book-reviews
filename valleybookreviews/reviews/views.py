from flask import render_template, Blueprint
from flask_login import current_user, login_required

user_reviews = Blueprint('user_reviews', __name__)


@user_reviews.route("/myreviews", methods=["GET", "POST"])
@login_required
def myreviews():

    return render_template("myreviews.html")
