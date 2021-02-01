from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')






@bp.route('/map')
def map():
    return render_template('map.html')
  

@bp.route('/analytics')
def analytics():
    return render_template('analytics.html')





    




#export FLASK_ENV=development

#export FLASK_APP=flaskr
#flask run