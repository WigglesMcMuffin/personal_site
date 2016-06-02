from flask.ext.login import current_user

from flask_app.models.base import db, User

from .test_base import BaseTestCase

class TestUsers(BaseTestCase):

  render_templates = False

  def test_login_page_template(self):
    response = self.client.get("/login")
    self.assert_template_used('login.jade')

  def test_wrong_user_pass_not_logged_in(self):
    self.assertTrue(current_user.is_anonymous)
    u1_pass = 'test1'
    u2_pass = 'test2'
    u1 = User('test1', 'test1', u1_pass, 'test1')
    u1_id = str(u1.id)
    u2 = User('test2', 'test2', u2_pass, 'test2')
    db.session.add_all([u1, u2])
    db.session.commit()
    new_user = User.query.get(u1_id)
    response = self.client.post('/login', data=dict(
      username = new_user.username,
      password = u2_pass
    ))
    self.assertTrue(current_user.is_anonymous)
    response = self.client.post('/login', data=dict(
      username = new_user.username,
      password = u1_pass
    ))
    #TODO: THIS NEEDS TO BE FIXED
    self.assertFalse(current_user)
