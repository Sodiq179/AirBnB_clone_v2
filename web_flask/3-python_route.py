#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
    routes /hbnb: displays "HBNB"
    routes /c/<text>: diaplays C text
    routes /python/(<text>): displays Python text
"""

from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""return Hello HBNB"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
	"""return HBNB"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
	"""C is fun"""
	text = " ".join(text.split("_"))
	return "C {}".format(text)

@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text = "is cool"):
	"Python is cool"
	if text != "is cool":
		text = " ".join(text.split("_"))
	return "Python {}".format(text)


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=5000, debug = True)
