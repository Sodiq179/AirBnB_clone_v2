#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
    routes /hbnb: displays "HBNB"
    routes /c/<text>: diaplays C text
    routes /python/(<text>): displays Python text
"""

from flask import Flask, render_template
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

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
	"""Check number"""
	return "{%d} is a number".format(n)

@app.route("/number_template/<int:n>",strict_slashes=False)
def number_template(n):
	"""Number template"""
	return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>",strict_slashes=False)
def number_odd_or_even(n):
        """Number template"""
	if n % 2 == 0:
		state = "even"
	else:
		state = "odd"
        return render_template("6-number_odd_or_even.html", number=n, even_or_odd = state)


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=5000, debug = True)
