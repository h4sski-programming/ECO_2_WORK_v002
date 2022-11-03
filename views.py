from flask import Blueprint, render_template
from flask_login import login_required

from models import User, Activity
from models import session

views = Blueprint('views', __name__)

user = session.query(User).filter_by(id=1).first()

@views.route('/')
# @ login_required
def home():
    return render_template('home.html')


@views.route('/edit', methods=['GET', 'POST'])
# @ login_required
def edit():
    return render_template('edit.html')


@views.route('/profile')
# @ login_required
def profile():
    return render_template('profile.html', user=user)
