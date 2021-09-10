from flask import Flask, escape
""" Creating the first Flask Application
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """ Returning the string Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returning the string HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def show_the_string(text):
    """Returning the string sent by shell"""
    return 'C %s' % escape(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
