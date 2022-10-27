from flask import Blueprint, render_template
from models import User, Activity

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
