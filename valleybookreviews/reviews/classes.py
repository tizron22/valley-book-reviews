import re

from valleybookreviews.factory.initialisation import mongo_db
from bson.objectid import ObjectId


class UserReviews():

    def __init__(self, user_id, book_name, author_name, image_link, review_text, _id=None, review_likes_users=None, review_likes_count=None, review_dislikes_users=None, review_dislikes_count=None):

        self._id = _id
        self.user_id = user_id
        self.book_name = book_name
        self.author_name = author_name
        self.image_link = image_link
        self.review_text = review_text
        self.review_likes_users = review_likes_users if review_likes_users else []
        self.review_likes_count = review_likes_count if review_likes_count else 0
        self.review_dislikes_users = review_dislikes_users if review_dislikes_users else []
        self.review_dislikes_count = review_dislikes_count if review_dislikes_count else 0

    def get_review_id(self):
        return self._id

    def get_db_info(self):

        review = {
            "user_id": self.user_id,
            "book_name": self.book_name,
            "author_name": self.author_name,
            "image_link": self.image_link,
            "review_text": self.review_text,
            "review_likes_users": self.review_likes_users,
            "review_likes_count": self.review_likes_count,
            "review_dislikes_users": self.review_dislikes_users,
            "review_dislikes_count": self.review_dislikes_count
        }
        return review

    def add_user_review(self):
        mongo_db.db.reviews.insert_one(self.get_db_info())

    def delete_user_review(_id):
        if ObjectId.is_valid(_id):
            mongo_db.db.reviews.delete_one({"_id": ObjectId(_id)})

    def edit_user_review(self, book_name, author_name, image_link, review_text):

        self.book_name = book_name
        self.author_name = author_name
        self.image_link = image_link
        self.review_text = review_text

        mongo_db.db.reviews.update_one({"_id": ObjectId(self._id)}, {
                                       "$set": self.get_db_info()})

    @classmethod
    def get_user_reviews(cls, user_name):
        reviews = list(mongo_db.db.reviews.find({"user_id": user_name}))

        returned_reviews = []

        if reviews is not None:

            for review in reviews:
                returned_reviews.append(cls(**review))

        return returned_reviews

    @classmethod
    def get_all_reviews(cls):
        reviews = list(mongo_db.db.reviews.aggregate(
            [{"$sort": {"review_likes_count": -1}}]))

        returned_reviews = []

        if reviews is not None:

            for review in reviews:
                returned_reviews.append(cls(**review))

        return returned_reviews
