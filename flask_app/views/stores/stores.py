from flask import Blueprint, render_template, redirect, url_for, request
from flask_app.forms import LoginForm

from flask import render_template, request

store_pages = Blueprint('stores', __name__, static_folder='static', url_prefix='/stores')

@store_pages.route('/')
def main_page():
  return render_template('main.jade', pageTitle='Home Page')
