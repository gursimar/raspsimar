from flask import Flask
app = Flask(__name__, static_url_path='')
from webapp import views
