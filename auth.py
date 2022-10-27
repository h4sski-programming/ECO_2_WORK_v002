from flask import Blueprint, render_template, redirect, url_for

# from models import User, Activity

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('auth.login'))
