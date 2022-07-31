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
