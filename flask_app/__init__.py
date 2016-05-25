from flask import Flask
from flask.ext.principal import Principal
from flask_wtf.csrf import CsrfProtect
from flask.ext.uploads import configure_uploads

from flask_app import config
from flask_app.middleware.reverse_proxy import ReverseProxied
from flask_app.sockets import socketio
from flask_app.models import db
from flask_app.users import login_manager, principals
from flask_app.stores import item_images, storefronts

import pyjade

csrf = CsrfProtect()

def create_app(debug=False):
  app = Flask(__name__, static_folder=None)
  app.config['SECRET_KEY'] = 'dev_secret'
  app.debug =  debug
  app.config['SQLALCHEMY_DATABASE_URI'] = config.get_database_uri()
  app.config['SQLALCHEMY_BINDS'] = config.get_datastore_uri()
  app.config['UPLOADS_DEFAULT_DEST'] = '/uploads'
  app.wsgi_app = ReverseProxied(app.wsgi_app)
  app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

  # Turn on all the features
  db.init_app(app)
  csrf.init_app(app)
  socketio.init_app(app)
  login_manager.init_app(app)
  principals.init_app(app)

  # Add flask uploads
  configure_uploads(app, (item_images, storefronts))

  #TODO: Work on useful logging
  """
  import logging
  from logging import FileHandler
  file_handler = FileHandler('/code/logs.log')
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)
  """

  # Plugin in the socket support
  import flask_app.sockets

  from flask_app.users import login_processor
  app.context_processor(login_processor)

  # Register the blueprints to display the pages
  from flask_app.views.main import main_site
  from flask_app.views.users import user_pages
  from flask_app.views.games import games_pages
  from flask_app.views.sockets import socket_pages
  from flask_app.views.graphs import graphs_pages
  from flask_app.views.stores import store_pages
  app.register_blueprint(main_site)
  app.register_blueprint(user_pages)
  app.register_blueprint(games_pages)
  app.register_blueprint(socket_pages)
  app.register_blueprint(graphs_pages)
  app.register_blueprint(store_pages)

  return app
