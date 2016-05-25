from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.login import login_required, login_user, logout_user, current_user, LoginManager

from flask_app.forms import LoginForm

login_manager = LoginManager()
principals = Principal()

login_manager.login_view = 'users.login_users'

def login_processor():
  return dict(login_form=LoginForm())
