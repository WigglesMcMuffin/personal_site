from flask import Blueprint, render_template, redirect, url_for, request
from flask_app.forms import LoginForm
from flask_app.models import db

from flask import render_template, request

main_site = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main_site.route('/')
def main_page():
  return render_template('main.jade', pageTitle='Home Page')

@main_site.route('/about')
def about_page():
  return render_template('about.jade', pageTitle='About Page')
