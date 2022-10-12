from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, \
    ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship
from os import path
from app import app, db

# db = declarative_base()
# db = SQLAlchemy()
DB_NAME = 'database.db'


class User(db, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    email = Column(String(200), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    role = Column(String(50), default='member')
    time_create = Column(DateTime(timezone=True), server_default=func.now())
    activity = relationship('Activity')


class Activity(db):
    __tablename__ = 'activity'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    date = Column(Date(), unique=True)
    distance = Column(Integer())
    type = Column(Integer())
    time_create = Column(DateTime(timezone=True), server_default=unc.now())
    time_update = Column(DateTime(timezone=True), onupdate=func.now())


# def initiate_db():
#     app.config['SECRET_KEY'] = 'h4sski'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     app.run(debug=True)
#     db.init_app(app)
#
#
# def create_db(app_create):
#     if not path.exists(f'/{DB_NAME}'):
#         db.create_all(app_create)
