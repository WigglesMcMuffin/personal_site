from flask import Blueprint, render_template, redirect, url_for, request
from flask.ext.login import login_required

socket_pages = Blueprint('sockets', __name__,
                        template_folder='templates', url_prefix='/sockets')

@socket_pages.route('/')
@login_required
def sockets():
  return render_template('sockets.jade', pageTitle='Sockets')
