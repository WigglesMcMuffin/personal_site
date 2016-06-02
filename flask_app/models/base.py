from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  __bind_key__ = None
  id = db.Column(db.String(36, convert_unicode=True), primary_key=True)
  name = db.Column(db.String(50), unique=False, nullable=False)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(300), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  admin = db.Column(db.Boolean(), unique=False, nullable=False)
  active = db.Column(db.Boolean(), unique=False, nullable=False)
  verified = db.Column(db.Boolean(), unique=False, nullable=False)

  def __init__(self, name=None, username=None, password=None, email=None, admin=False):
    self.id = uuid.uuid4()
    self.name = name
    self.username = username
    self.password = self.hash_password(password)
    self.email = email
    self.admin = admin
    self.active = True
    self.verified = False

  def is_authenticated(self):
    return True

  def is_anonymous(self):
    return False

  def is_active(self):
    return self.active

  def is_verified(self):
    return self.verified

  def verify(self):
    self.verified = True

  def hash_password(self, password):
    return generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def get_id(self):
    return self.id

  def __repr__(self):
    return '<User %r -- %r>' % (self.username, self.name)
