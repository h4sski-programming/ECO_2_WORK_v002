from flask import Flask
from flask_login import LoginManager

from models import create_db
from models import DB_NAME
from auth import auth, initiate_login_manager
from views import views

app = Flask(__name__)


def initiate_app():
    app.config['SECRET_KEY'] = 'h4sski'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


def main():
    initiate_app()

    app.register_blueprint(views, url_prefix='/')

    app.register_blueprint(auth, url_prefix='/')
    # initiate_login_manager(app)

    create_db(app)

    app.run(debug=True)


if __name__ == '__main__':
    main()
