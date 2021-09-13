#!/usr/bin/python3
""" List of cities from HTML Query """
from models.state import State
from models.city import City
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Return HTML with states and cities """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """ Returns HTML Query of state with the cities """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('9-states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Close session """
    storage.close()


if __name__ == '__main__':
    """ Run the port 5000 and listen in 0.0.0.0 """
    app.run(debug=True, host='0.0.0.0', port=5000)
