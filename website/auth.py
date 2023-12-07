from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login(method = 'GET'):
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully',category='success')
                login_user(user, remember=True)
            else:
                flash('password incorrect',category='error')
        else:
            flash('Invalid username',category='error') 

            

    return render_template("login.html",user=current_user)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            flash('User already exists')
        else:
            first_name = request.form.get('firstName')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')


            if len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            
            else:
                new_user = User(email=email,first_name = first_name, password = generate_password_hash(password1,method='pbkdf2:sha1'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created!', category='success')
                login_user(new_user, remember=True)

                return redirect(url_for('views.home'))



    return render_template("sign_up.html",user=current_user)
