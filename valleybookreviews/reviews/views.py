from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import current_user, login_required
from valleybookreviews.reviews.classes import UserReviews

user_reviews = Blueprint('user_reviews', __name__)


@user_reviews.route("/allreviews", methods=["GET", "POST"])
def allreviews():

    all_submited_reviews = UserReviews.get_all_reviews()

    return render_template("allreviews.html", all_submited_reviews=all_submited_reviews)


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

    submited_user_reviews = UserReviews.get_user_reviews(
        current_user.user_name)

    return render_template("myreviews.html", submited_user_reviews=submited_user_reviews)


@user_reviews.route("/delete_review/<review_id>", methods=["GET", "POST"])
@login_required
def delete_review(review_id):

    if request.method == "POST":
        UserReviews.delete_user_review(review_id)
        return redirect(url_for("user_reviews.myreviews"))


@user_reviews.route("/add_like/<review_id>")
@login_required
def add_like(review_id):

    liked_review = UserReviews.get_reviews_id(review_id)

    if current_user.is_authenticated:

        if current_user.user_name in liked_review.get_db_info()['review_likes_users']:
            print("You already liked the Review")
        elif current_user.user_name in liked_review.get_db_info()["review_dislikes_users"]:
            dislike_index = liked_review.get_db_info(
            )["review_dislikes_users"].index(current_user.user_name)
            liked_review.remove_review_dislike(dislike_index)
            liked_review.add_review_like(current_user.user_name)
            return redirect(url_for("user_reviews.allreviews"))
        else:
            liked_review.add_review_like(current_user.user_name)
            return redirect(url_for("user_reviews.allreviews"))

    return redirect(url_for("user_reviews.allreviews", review_id=liked_review.get_review_id))


@user_reviews.route("/add_dislike/<review_id>")
@login_required
def add_dislike(review_id):

    disliked_review = UserReviews.get_reviews_id(review_id)

    if current_user.user_name in disliked_review.get_db_info()["review_dislikes_users"]:
        print("You already disliked the Review")
    elif current_user.user_name in disliked_review.get_db_info()["review_likes_users"]:
        like_index = disliked_review.get_db_info(
        )["review_likes_users"].index(current_user.user_name)
        disliked_review.remove_review_like(like_index)
        disliked_review.add_review_dislike(current_user.user_name)
        return redirect(url_for("user_reviews.allreviews"))

    else:
        disliked_review.add_review_dislike(current_user.user_name)
        return redirect(url_for("user_reviews.allreviews"))

    return redirect(url_for("user_reviews.allreviews", review_id=disliked_review.get_review_id))
