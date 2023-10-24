#!/usr/bin/python3
"""a script that starts a Flask web application:"""

from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """list of cities by states in an HTML page is displayed"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """current SQLAlchemy Session is removed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
