from flask import Flask,render_template,flash,redirect,url_for

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='653e33351c6f4a262c1bceda061a6cb3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)
from flask_1 import routes