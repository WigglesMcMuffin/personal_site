from flask import Blueprint, render_template, redirect, url_for, request
from flask_app.forms import LoginForm
from flask_app.users import verified_required

from flask import render_template, request

stream_pages = Blueprint('streams', __name__, static_folder='static', template_folder='templates', url_prefix='/streams')

@stream_pages.route('/')
@verified_required
def main_page():
  return render_template('stream.jade', pageTitle='Stream Page')
