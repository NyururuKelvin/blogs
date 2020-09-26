import os
from flask import render_template,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User

@main.route('/')
def index():

    title = 'Blogs Site'
  
    return render_template('index.html', title = title)