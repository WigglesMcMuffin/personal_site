from functools import wraps

from flask import abort
from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.login import login_required, login_user, logout_user, current_user, LoginManager, AnonymousUserMixin

from flask_app.forms import LoginForm

login_manager = LoginManager()
principals = Principal()

class AnonymousUser(object):
  def __init__(self, *args, **kwargs):
    super(AnonymousUser, self).__init__(*args, **kwargs)

  def is_verified(self):
    return False

  def is_authenticated(self):
    return False

  def is_anonymous(self):
    return True

  def is_active(self):
    return False

  def get_id(self):
    return None

login_manager.login_view = 'users.login_users'
login_manager.anonymous_user = AnonymousUser

def verified_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not current_user.is_verified():
      return abort(403)
    return f(*args, **kwargs)
  return decorated_function

def login_processor():
  return dict(login_form=LoginForm())
