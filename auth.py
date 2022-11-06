from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager

from models import session, db
from models import User, Activity

auth = Blueprint('auth', __name__)
# login_manager = LoginManager()


# @login_manager.user_loader
# def load_user(user):
#     return User.get(user)

# @login_manager.user_loader
# def load_user(user_id):
#     return session.query(User).filter_by(id=user_id).first()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = session.query(User).filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f'Logged, welcome {user.first_name}!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = session.query(User).filter_by(email=email).first()
        if user:
            flash('User already exist.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 characters.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match.', category='error')
        else:
            # new_user = user_table(email=email, first_name=first_name, last_name=last_name,
            #                       password=generate_password_hash(password1, method='sha256'))
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            password=generate_password_hash(password1, method='sha256'))
            session.add(new_user)
            session.commit()
            login_user(new_user, remember=True)
            flash('Account created.', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
