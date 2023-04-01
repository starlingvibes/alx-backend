#!/usr/bin/env python3

"""
Using Flask-Babel to demonstrate internationalization
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """Return a string"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
