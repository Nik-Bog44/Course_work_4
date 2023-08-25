from marshmallow import Schema, fields
from model.basemodel import BaseModelId

from setup_db import db


class User(BaseModelId, db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favorite_genre = db.Column(db.String(150))


class UserSchema(Schema):
    username = fields.Str(required=True)
    name = fields.Str(required=True)
    surname = fields.Str

