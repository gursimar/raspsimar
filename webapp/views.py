from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import INTEGER, Text

from webapp import app
from flask import render_template

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///system.db'
db = SQLAlchemy(app)

class Video(db.Model):
    id= Column(INTEGER, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)
db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Video, methods = ['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def index():
    return app.send_static_file('index.html')

# this is jinja example
@app.route('/jinja')
def jinja():
    name = 'simar'
    return render_template('jinja.html', name=name)

# just a basic page
@app.route('/cakes')
def cakes():
    return 'cakes'

#bootstrap example
@app.route('/bootstrap')
def welcome():
	return render_template('bootstrap.html')

