from flask import Blueprint
import register

auth = Blueprint('auth', __name__)

@auth.route('/auth')
def auth():
    # return render_template('home.html')
    return 'Auth'