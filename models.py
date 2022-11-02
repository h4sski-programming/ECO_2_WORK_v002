from os import path

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session
from sqlalchemy import Column, Integer, String, \
    ForeignKey, Date, DateTime, func, create_engine
from sqlalchemy.orm import relationship
# from app import db


db = SQLAlchemy()
DB_NAME = 'database.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True, future=True)
session = Session(engine)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    email = Column(String(200), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    role = Column(String(50), default='member')
    time_create = Column(DateTime(timezone=True), server_default=func.now())
    activity = relationship('Activity')


class Activity(db.Model):
    __tablename__ = 'activity'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    date = Column(Date(), unique=True)
    distance = Column(Integer())
    type = Column(Integer())
    time_create = Column(DateTime(timezone=True), server_default=func.now())
    time_update = Column(DateTime(timezone=True), onupdate=func.now())

def create_db():
    if not path.exist(f'/{DB_NAME}'):
        db.metadata.create_all(engine)