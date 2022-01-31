#!/usr/bin/python3

"""
Fetch data by Flask
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def fetch_all_states():
    """Get states from DBStorage"""
    fetch_states = storage.all("State").values()
    return render_template("7-states_list.html", states=fetch_states)


@app.teardown_appcontext
def teardown_db(self):
    """close session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
