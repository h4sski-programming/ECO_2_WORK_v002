from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from os import path

import models
from models import DB_NAME

app = Flask(__name__)


# db = SQLAlchemy()
# # db = declarative_base()
# DB_NAME = 'database.db'
# engine = create_engine(f'sqlite:///{DB_NAME}', echo=True, future=True)
# session = Session(engine)


def initiate_app():
    app.config['SECRET_KEY'] = 'h4sski'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


def create_db():
    app.run(debug=True)
    # db.init_app(app)
    models.create_db(app)


def main():
    initiate_app()

    from views import views
    app.register_blueprint(views, url_prefix='/')
    from auth import auth
    app.register_blueprint(auth, url_prefix='/')

    create_db()


if __name__ == '__main__':
    main()
