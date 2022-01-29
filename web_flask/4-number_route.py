#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """returns a parameter by url as string"""
    txt = text.replace('_', ' ')
    return "C {}".format(escape(txt))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Py_is_fun(text):
    """Set a parameter by or return passed value"""
    txt = text.replace('_', ' ')
    return "Python {}".format(escape(txt))


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_num(n):
    """Check if a parameter is integer type and return"""
    if isinstance(n, int):
        return "{} is a number".format(escape(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
