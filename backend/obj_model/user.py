import random

from backend import db


def generate_nonce(length=8):
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_address = db.Column(db.String(80), nullable=False, unique=True)
    nonce = db.Column(db.Integer(), nullable=False, default=generate_nonce, )


def get_user(public_address):
    user: User = User.query.filter_by(public_address=public_address).first()
    return user
