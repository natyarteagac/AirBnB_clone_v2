from flask import Flask
""" Creating the first Flask Application
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """ Returning the string Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
