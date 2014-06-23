from flask import Flask
#Create a flask application called app
app = Flask(__name__)
#Import configuration data from config.py
app.config.from_object('config')
#import views module
from application import views