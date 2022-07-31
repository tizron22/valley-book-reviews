"""


"""
# from crypt import methods
# import re

from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from valleybookreviews.user.classes import UserDetails

from valleybookreviews.factory.initialisation import postgresql_db
from valleybookreviews.user.models import Users


user_accounts = Blueprint('user_accounts', __name__)


login_manager = LoginManager()


@login_manager.user_loader
def load_user(username):
    return Users.query.get(int(username))


# The registered user route sheet
@user_accounts.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        user_id = request.form.get("userID").lower()
        first_name = request.form.get("firstName").title()
        last_name = request.form.get("lastName").title()
        email_address = request.form.get("emailAddress").lower()
        submited_password = request.form.get("userPassword")

        user_account_exist = UserDetails.query_user(user_id)
        if user_account_exist:
            print(
                "Sorry, that Username has already been taken. Please try a different one!")
        else:
            hash_submited_password = UserDetails.hash_password(
                submited_password)
            UserDetails.register_user_account(
                user_id, first_name, last_name, email_address, hash_submited_password)
            return redirect("login")

    return render_template("register.html")


@user_accounts.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user_name = request.form.get("userLogin").lower()
        submited_password = request.form.get("userpassword")

        registered_user_account = UserDetails.query_user(user_name)
        if registered_user_account:
            UserDetails.login_user_account(
                registered_user_account, submited_password)
            return redirect("myreviews")

    return render_template("login.html")


@user_accounts.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("login")
