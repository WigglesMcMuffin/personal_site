from flask_app.forms import LoginForm
from flask_app.users import login_manager, principals
from flask_app.models.base import User

from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.login import login_required, login_user, logout_user, current_user, LoginManager

user_pages = Blueprint('users', __name__,
                        template_folder='templates')

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@user_pages.route('/login', methods=('GET', 'POST'))
def login_users():
  form = LoginForm()
  if form.validate_on_submit():
    user = form.user
    login_user(user)
    next = flask.request.args.get('next')
    return redirect(next or url_for('main.main_page'))
  else:
    return render_template('login.jade')

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
