
import re

from flask import redirect, session, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


# from valleybookreviews import sql_db
from valleybookreviews.user.models import Users
from valleybookreviews.factory.initialisation import postgresql_db, bcrypt


class UserDetails(UserMixin):

    def __init__(self, user_name):
        self.user_name

    def get_user(self):
        return self.user_name

    def query_user(user_name):
        return Users.query.filter_by(user_name=user_name).first()

    def hash_password(password):
        """
            This function will Hash any password that is provided.
        """
        return bcrypt.generate_password_hash(password).decode("utf-8", "ignore")

    def register_user_account(username, firstname, lastname, emailaddress, hashed_password):
        new_account = Users(user_name=username.data,
                            first_name=firstname.data,
                            last_name=lastname.data,
                            email=emailaddress.data,
                            password=hashed_password.data
                            )
        postgresql_db.session.add(new_account)
        postgresql_db.session.commit()

    def validate_new_user(self, username):
        existing_user = Users.query.filter_by(user_name=username.data).first()
        if existing_user:
            print(
                "Sorry, that Username has already been taken. Please try a different one!")

    def login_user_account(username, submited_password):
        if bcrypt.check_password_hash(username.password, submited_password):
            login_user(username)
