from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf.csrf import CsrfProtect
from flask.ext.uploads import configure_uploads
from flask.ext.login import current_user

from flask_app import config
from flask_app.middleware.reverse_proxy import ReverseProxied
from flask_app.sockets import socketio
from flask_app.models import db
from flask_app.users import login_manager, principals
from flask_app.stores import item_images, storefronts

import pyjade

csrf = CsrfProtect()

def create_app(debug=False, testing=False):
  app = Flask(__name__, static_folder=None)
  app.config['SECRET_KEY'] = 'dev_secret'
  app.debug =  debug
  app.config['TESTING'] = testing
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SQLALCHEMY_DATABASE_URI'] = config.get_database_uri(testing)
  app.config['SQLALCHEMY_BINDS'] = config.get_datastore_uri(testing)
  app.config['UPLOADS_DEFAULT_DEST'] = '/uploads'
  app.wsgi_app = ReverseProxied(app.wsgi_app)
  app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

  # Turn on all the features
  db.init_app(app)
  if not testing:
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
  from flask_app.views.streams import stream_pages
  app.register_blueprint(main_site)
  app.register_blueprint(user_pages)
  app.register_blueprint(games_pages)
  app.register_blueprint(socket_pages)
  app.register_blueprint(graphs_pages)
  app.register_blueprint(store_pages)
  app.register_blueprint(stream_pages)

  @app.errorhandler(404)
  def page_not_found(e):
      return render_template('not_found.jade')

  @app.errorhandler(500)
  def major_error(e):
      db.session.rollback()
      return render_template('broken.jade')

  @app.errorhandler(502)
  def major_error(e):
      db.session.rollback()
      return render_template('broken.jade')

  @app.errorhandler(403)
  def unauthorized(e):
    from flask import request
    if current_user.is_authenticated():
      if current_user.is_verified():
        status = 'verified'
      else:
        status = 'authenticated'
    else:
      flash('Please log in to access this page.')
      return redirect(url_for('users.login_users', next=request.full_path))
    return render_template('unauthorized.jade', pageTitle='Unauthorized Access', status=status)

  return app
