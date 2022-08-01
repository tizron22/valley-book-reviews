from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import current_user, login_required
from valleybookreviews.reviews.classes import UserReviews

user_reviews = Blueprint('user_reviews', __name__)


@user_reviews.route("/myreviews", methods=["GET", "POST"])
@login_required
def myreviews():

    if request.method == "POST":

        new_review = UserReviews(
            user_id=current_user.user_name,
            book_name=request.form.get("bookName"),
            author_name=request.form.get("authorName"),
            image_link=request.form.get("imageLink"),
            review_text=request.form.get("reviewText")
        )
        new_review.add_user_review()
        return redirect(url_for("user_reviews.myreviews"))

    return render_template("myreviews.html")
