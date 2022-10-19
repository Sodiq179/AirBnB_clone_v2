#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
    routes /hbnb: displays "HBNB"
    routes /c/<text>: diaplays C text
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


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=5000, debug = True)
