from valleybookreviews import db


class User(db.Model):
    # schema for User Details
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    modified_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return self.user_name
