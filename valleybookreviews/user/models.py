from valleybookreviews.factory.initialisation import postgresql_db
from flask_login import UserMixin


class Users(postgresql_db.Model, UserMixin):
    # schema for User Details
    id = postgresql_db.Column(postgresql_db.Integer, primary_key=True)
    user_name = postgresql_db.Column(
        postgresql_db.String(25), unique=True, nullable=False)
    first_name = postgresql_db.Column(postgresql_db.String(50), nullable=False)
    last_name = postgresql_db.Column(postgresql_db.String(150), nullable=False)
    email = postgresql_db.Column(
        postgresql_db.String(320), unique=True, nullable=False)
    password = postgresql_db.Column(postgresql_db.String(80), nullable=False)

    def __repr__(self):
        return self.user_name
