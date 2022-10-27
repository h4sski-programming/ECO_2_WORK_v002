from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = 'database.db'


def initiate_app():
    app.config['SECRET_KEY'] = 'h4sski'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


def create_db(app_create):
    app.run(debug=True)
    db.init_app(app)
    if not path.exists(f'/{DB_NAME}'):
        db.metadata.create_all(app_create)


def main():
    initiate_app()

    from views import views
    from auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import User, Activity
    create_db(app)


if __name__ == '__main__':
    main()
