#!/usr/bin/python3
""" Creating the first Flask Application
"""
from flask import Flask, escape, render_template
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


@app.route('/number_template/<int:n>')
def display_html(n):
    """ Returns a HTLM if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
