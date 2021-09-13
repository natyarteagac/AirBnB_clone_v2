#!/usr/bin/python3
""" List of cities """

from models.state import State
from models.city import City
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Return HTML with states and cities """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Close session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)
