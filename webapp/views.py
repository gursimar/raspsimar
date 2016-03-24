from datetime import datetime

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

class Alarm(db.Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(256))
    message = Column(db.String(512))
    status = Column(db.Boolean)
    severity = Column(db.Integer)
    days = Column (db.String)
    time = Column (db.DateTime)
    deadline = Column (db.DateTime)
db.create_all()


# Insert a alarm manually
al = Alarm(id=101, name = "pompu", message= "pompu is great", status=1, severity = 1, days="monday", time=datetime.now(), deadline=datetime.now())

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Video, methods = ['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Alarm, methods = ['GET', 'POST', 'DELETE', 'PUT'])


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

