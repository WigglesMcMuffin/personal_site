from flask_app.forms import LoginForm, RegisterForm, ChangePasswordForm
from flask_app.users import login_manager, principals
from flask_app.models.base import User, db

from flask import Blueprint, render_template, redirect, url_for, request, abort, flash
from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.login import login_required, login_user, logout_user, current_user, LoginManager

import redis

user_pages = Blueprint('users', __name__,
                        template_folder='templates')

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@user_pages.route('/register', methods=('GET', 'POST'))
def register_user():
  form = RegisterForm()
  if form.validate_on_submit():
    username = form.username.data
    name     = form.name.data
    password = form.password.data
    email    = form.email.data
    user = User(name, username, password, email)
    u_id = str(user.id)
    db.session.add(user)
    db.session.commit()
    user = User.query.get(u_id)
    login_user(user)
    next = request.args.get('next')
    return redirect(next or url_for('main.main_page'))
  return render_template('register.jade', pageTitle='Register New User Account', form=form)

@user_pages.route('/login', methods=('GET', 'POST'))
def login_users():
  form = LoginForm()
  if form.validate_on_submit():
    user = form.user
    login_user(user)
    next = request.args.get('next')
    return redirect(next or url_for('main.main_page'))
  else:
    return render_template('login.jade')

@user_pages.route('/verify', methods=['GET'])
@login_required
def quick_verify():
  user = current_user
  user.verify()
  db.session.add(user)
  db.session.commit()
  return redirect(url_for('main.main_page'))

@user_pages.route('/logout', methods=['GET'])
@login_required
def logout_users():
  logout_user()
  return redirect(url_for('main.main_page'))

@user_pages.route('/user/<user_id>')
@login_required
def user_page(user_id):
  user = User.query.get(user_id)
  if user == current_user:
    return render_template('user.jade', pageTitle='%s info' % (current_user.username))
  else:
    abort(403)
