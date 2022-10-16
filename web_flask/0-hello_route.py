#!/usr/bin/python3
from flask import Flask

# Creating an app instance
app = Flask(__name__)

# Creating the root of the web application
@app.route("/")#, strict_slashes=False)
def root():
	# This returns Hello HBNB message at the root 
	# of the web app
	return "Hello HBNB!"

