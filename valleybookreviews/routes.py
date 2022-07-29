from crypt import methods
import re
from flask import render_template, request, redirect, url_for
from valleybookreviews import app, db, bcrypt, login_user, LoginManager, login_required, logout_user, current_user
from valleybookreviews.models import Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class register_form(FlaskForm):
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

    def validate_user(self, user_name):
        existing_user = Users.query.filter_by(user_name=user_name.data).first()
        if existing_user:
            raise ValidationError(
                "Sorry, that Username has already been taken. Please try a different one!")


class login_form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=25)], render_kw={"placeholder": "Username"})
    currentpassword = PasswordField(validators=[InputRequired(), Length(
        min=1, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = register_form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.newpassword.data).decode("utf-8", "ignore")
        new_account = Users(user_name=form.username.data,
                            first_name=form.firstname.data,
                            last_name=form.lastname.data,
                            email=form.emailaddress.data,
                            password=hashed_password
                            )
        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = login_form()
    if form.validate_on_submit():
        user_account = Users.query.filter_by(
            user_name=form.username.data).first()
        if user_account:
            if bcrypt.check_password_hash(user_account.password, form.currentpassword.data):
                login_user(user_account)
                return redirect(url_for("myreviews"))
    return render_template("login.html", form=form)


@app.route("/myreviews", methods=["GET", "POST"])
@login_required
def myreviews():
    return render_template("myreviews.html")


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
