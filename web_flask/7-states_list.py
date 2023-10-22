#!/usr/bin/python3
"""Flask Application Module"""

from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays list of states in an HTML page"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
