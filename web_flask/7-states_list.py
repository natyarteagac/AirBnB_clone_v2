#!/usr/bin/python3
""" List of cities """

from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)
elements = storage.all()


@app.route('/states_list', strict_slashes=False)
def states_list(elements):
    """ Returns HTML with query """
    return render_template('7-states_list.html', elements=elements)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
