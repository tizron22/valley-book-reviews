
import re

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


# from valleybookreviews import sql_db
from valleybookreviews.user.models import Users


class UserDetails(UserMixin):

    def __init__(self, user_name):
        self.user_name

    def __repr__(self):
        return self.user_name

    def register_form(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(
            min=4, max=25)], render_kw={"placeholder": "Username"})
        firstname = StringField(validators=[InputRequired(), Length(
            min=1, max=50)], render_kw={"placeholder": "First Name"})
        lastname = StringField(validators=[InputRequired(), Length(
            min=1, max=100)], render_kw={"placeholder": "Last Name"})
        emailaddress = StringField(validators=[InputRequired(), Length(
            min=1, max=150)], render_kw={"placeholder": "Email Address"})
        newpassword = PasswordField(validators=[InputRequired(), Length(
            min=1, max=20)], render_kw={"placeholder": "Password"})

        submit = SubmitField("Register")

    def validate_new_user(self, username):
        existing_user = Users.query.filter_by(user_name=username.data).first()
        if existing_user:
            raise ValidationError(
                "Sorry, that Username has already been taken. Please try a different one!")

    def login_form(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(
            min=4, max=25)], render_kw={"placeholder": "Username"})
        currentpassword = PasswordField(validators=[InputRequired(), Length(
            min=1, max=20)], render_kw={"placeholder": "Password"})

        submit = SubmitField("Login")

        return
