#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
    routes: /hbnb: display “HBNB”
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""This returns Hello HBNB message at the root"""
	return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
	"""This page displays HBNB"""
	return "HBNB"


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
