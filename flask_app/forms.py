from flask import flash
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Required, EqualTo
from flask_app.models.base import User

class LoginForm(Form):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])

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

class RegisterPasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
        [
            Length(min=8),
            Required(),
            EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Confirm Password')

class ChangePasswordForm(Form):
    old_password = PasswordField('Old Password')
    new_password = PasswordField('New Password',
        [
            Length(min=8),
            Required(),
            EqualTo('confirm', message='New Password must match')
    ])
    confirm = PasswordField('Confirm New Password')


class ItemForm(Form):
    item_name = StringField('item_name', validators=[DataRequired()])
    item_description = StringField('item_description')
