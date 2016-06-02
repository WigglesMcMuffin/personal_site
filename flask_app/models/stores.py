import uuid

from .base import db

class Store(db.Model):
  __tablename__ = 'stores'
  __bind_key__ = None
  id = db.Column(db.String(36, convert_unicode=True), primary_key=True)
  store_name = db.Column(db.String(100), unique=True, nullable=False)
  owner_id = db.Column(db.String(36, convert_unicode=True), db.ForeignKey('users.id'), nullable=False)
  owner = db.relationship("User", foreign_keys=[owner_id], single_parent=True, cascade='all, delete-orphan')

  def __init__(self, store_name=None, owner_id=None):
      self.id = uuid.uuid4()
      self.store_name = store_name
      self.owner_id = owner_id

class Item(db.Model):
  __tablename__ = 'items'
  __bind_key__ = None
  id = db.Column(db.String(36, convert_unicode=True), primary_key=True)
  store_id = db.Column(db.String(36, convert_unicode=True), db.ForeignKey('stores.id'), nullable=False)
  store = db.relationship("Store", foreign_keys=[store_id], single_parent=True, cascade='all, delete-orphan')
  item_name = db.Column(db.String(50), unique=False, nullable=False)
  item_description = db.Column(db.String(2000), unique=False, nullable=True)
  item_cost = db.Column(db.Integer, unique=False, nullable=True)
  item_image = db.Column(db.String(200), unique=False, nullable=False)
