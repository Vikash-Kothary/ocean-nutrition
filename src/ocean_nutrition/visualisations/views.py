
from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__,
	static_folder='static', 
	static_url_path='', 
	template_folder='templates')

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/search')
def search():
    return render_template('search.html')

@views.route('/diary')
def diary():
    return render_template('diary.html')
