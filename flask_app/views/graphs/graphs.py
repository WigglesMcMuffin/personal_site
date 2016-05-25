from flask import Blueprint, render_template, redirect, url_for, request, current_app

graphs_pages = Blueprint('graphs', __name__,
                        template_folder='templates',
                        static_folder='static',
                        url_prefix='/d3')

@graphs_pages.route('/')
def d3():
  lines = ''
  #with open('/code/flask_app/static/assets/2008.abridged.csv', 'r') as fh:
  #  lines = ';'.join([x[:-1].strip() for x in fh.readlines()])
  return render_template('d3.jade', pageTitle='D3', lines=lines)
