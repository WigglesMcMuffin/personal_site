from flask.ext.testing import TestCase

from flask_app import create_app as c_a
from flask_app.models import db

class BaseTestCase(TestCase):
  def create_app(self):
    return c_a(True, True)

  def setUp(self):
    db.create_all(bind=None)

  def tearDown(self):
    db.session.remove()
    db.drop_all(bind=None)
