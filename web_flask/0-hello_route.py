#!/usr/bin/python3
"""This script runs an app with Flask framework"""
from flask import Flask


# Creating an app instance
app = Flask(__name__)


# Creating the root of the web application
@app.route("/", strict_slashes=False)
def root():
	"""This returns Hello HBNB message at the root"""
	return "Hello HBNB!"

if __name__ == "__main__":
	app.run(host='0.0.0.0'. port:5000)
