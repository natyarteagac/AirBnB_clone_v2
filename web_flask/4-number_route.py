#!/usr/bin/python3
""" Creating the first Flask Application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Returning the string Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returning the string HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_the_string_in_c(text):
    """Returning the string sent by shell"""
    return 'C %s' % escape(text).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_the_string_in_python(text="is cool"):
    """ Returning the string sent by shell """
    return 'Python %s' % escape(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def show_the_number(n):
    """ Returning the variable n if is int"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
