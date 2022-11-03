from os import path

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, \
    ForeignKey, Date, DateTime, func, create_engine
from sqlalchemy.orm import relationship, declarative_base, Session

db = SQLAlchemy()
# db = declarative_base()
DB_NAME = 'database.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True, future=True)
session = Session(engine)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    role = db.Column(db.String(50), default='member')
    time_create = db.Column(db.DateTime(timezone=True), server_default=func.now())
    activity = relationship('Activity')


class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), ForeignKey('user.id'))
    date = db.Column(db.Date(), unique=True)
    distance = db.Column(db.Integer())
    type = db.Column(db.Integer())
    time_create = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())


def create_db(app):
    if not path.exists(f'/{DB_NAME}'):
        db.metadata.create_all(engine)
