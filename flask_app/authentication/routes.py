from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from .. import bcrypt
from werkzeug.utils import secure_filename
from ..forms import RegistrationForm, LoginForm, UpdatePasswordForm
from ..models import User

authentication = Blueprint("authentication", __name__)

""" ************ User Management views ************ """

@authentication.route("/register", methods=["GET", "POST"])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data, password=hashed, burger_counter=0, calorie_counter=0)
        user.save()
        return redirect(url_for('authentication.login'))
    
    return render_template('register.html', title='Register', form=form)

@authentication.route("/login", methods=["GET", "POST"])
def login():
    user = None
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        print(user)

        if (user is not None and  bcrypt.check_password_hash(user.password, form.password.data)):
                login_user(user)
                return redirect(url_for('users.index'))
        else:
            flash('Not successfully authenticated. Authenticate again')
            return redirect(url_for('authentication.login'))

    return render_template('login.html', title='Login', form=form)

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.index'))

@authentication.route("/account", methods=["GET", "POST"])
@login_required
def account():
    update_password_form = UpdatePasswordForm()

    if request.method == "POST":

        if update_password_form.submit_password.data and update_password_form.validate_on_submit():
            
                # Update the password
                user = User.objects(id=current_user.id).first()
                print('here')
                print(user.password)
                
                if(bcrypt.check_password_hash(user.password, update_password_form.curr_password.data)):
                    print("here")
                    hashed = bcrypt.generate_password_hash(update_password_form.new_password.data).decode('utf-8')
                    user.modify(password=hashed)

                    user.save()
                    flash('Your password has been updated!', 'success')
                    return redirect(url_for('authentication.account'))
                else:
                    flash('Your password has NOT been updated!', 'failure')
                    return redirect(url_for('authentication.account'))


    # Render the account page with forms
    return render_template('account.html', update_password_form=update_password_form)