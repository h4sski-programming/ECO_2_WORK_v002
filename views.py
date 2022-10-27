from flask import Blueprint, render_template

# from models import User, Activity

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@views.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html')


@views.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')
