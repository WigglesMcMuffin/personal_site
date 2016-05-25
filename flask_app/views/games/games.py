from flask import Blueprint, render_template, redirect, url_for, request

games_pages = Blueprint('games', __name__,
                        template_folder='templates', url_prefix='/games', static_folder='static')

@games_pages.route('/')
def canvas():
	return render_template('canvas.jade', pageTitle='Canvas')
