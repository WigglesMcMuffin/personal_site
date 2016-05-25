from flask import flash
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_app.models.base import User

class LoginForm(Form):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])

  def validate(self):
    rv = Form.validate(self)
    error_message = 'The Username or Password you entered is incorrect'
    if not rv:
      return False

    flag = False

    user = User.query.filter_by(username=self.username.data).first()
    if user is None:
      flag = True

    if not flag and not user.check_password(self.password.data):
      flag = True

    if flag:
      #self.errors['general'] = error_message
      flash(error_message, 'list-group-item-danger')
      return False
    else:
      self.user = user
      return True
