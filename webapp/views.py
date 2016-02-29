from webapp import app
from flask import render_template

@app.route('/')
def index():
    name = 'simar'
    return render_template('index.html', name=name)
    
@app.route('/cakes')
def cakes():
    return 'cakes'