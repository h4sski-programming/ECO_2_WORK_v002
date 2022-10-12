from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

import views
import auth

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = 'database.db'


def initiate_db():
    app.config['SECRET_KEY'] = 'h4sski'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.run(debug=True)
    db.init_app(app)


def create_db(app_create):
    print('create')
    if not path.exists(f'/{DB_NAME}'):
        print('created')
        db.create_all(app_create)


def main():
    initiate_db()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_db(app)


if __name__ == '__main__':
    main()
