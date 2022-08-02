from flask import render_template, Blueprint
from valleybookreviews.reviews.classes import UserReviews

home = Blueprint("home", __name__)


@home.route('/')
def index():

    random_review = UserReviews.get_random_review()
    return render_template("index.html", random_review=random_review)
