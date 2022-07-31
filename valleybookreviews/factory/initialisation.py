"""
Initialisation - Factory Sub-Module

Initialise flask Application Factory with MongoDB.

Functions:
    create_app()

"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa

# Creates an instance of MongoDB
mongo_db = PyMongo()

# Creates an instance of SQLAlchemy
postgresql_db = SQLAlchemy()

# Creates an instance of Bcrypt
bcrypt = Bcrypt()


def create_app():
    """
        Flask Application Factory


    """

    app = Flask(__name__)

    # Config
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DB_URL")  # local
    else:
        uri = os.environ.get("DATABASE_URL")
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
            app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

    app.template_folder = os.path.abspath("valleybookreviews/templates")
    app.secret_key = os.environ.get("SECRET_KEY")
    app.static_folder = os.path.abspath("valleybookreviews/static")

    # Initialise SQL Alchemy, mongodb and bcrypt for password hashing.
    mongo_db = PyMongo(app)
    postgresql_db = SQLAlchemy(app)
    bcrypt = Bcrypt(app)

    return app
