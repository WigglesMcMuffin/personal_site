from .test_base import BaseTestCase
from flask_app.models.base import db, User

class TestUsers(BaseTestCase):
  def test_hashed(self):
    user = User('test', 'test', 'hashed', 'test')
    u_id = str(user.id)
    db.session.add(user)
    db.session.commit()
    new_user = User.query.get(u_id)
    self.assertNotEqual('hashed', new_user.password)

  def test_credentials(self):
    user = User('test', 'test', 'correct', 'test')
    u_id = str(user.id)
    db.session.add(user)
    db.session.commit()
    new_user = User.query.get(u_id)
    self.assertFalse(new_user.check_password('not correct'))
    self.assertTrue(new_user.check_password('correct'))

  def test_credentials_different_user(self):
    u1_pass = 'test1'
    u2_pass = 'test2'
    u1 = User('test1', 'test1', u1_pass, 'test1')
    u1_id = str(u1.id)
    u2 = User('test2', 'test2', u2_pass, 'test2')
    u2_id = str(u2.id)
    db.session.add_all([u1, u2])
    db.session.commit()
    new_u1 = User.query.get(u1_id)
    new_u2 = User.query.get(u2_id)
    self.assertFalse(new_u1.check_password(u2_pass))
    self.assertFalse(new_u2.check_password(u1_pass))

class TestStore(BaseTestCase):
  pass

class TestItem(BaseTestCase):
  pass
