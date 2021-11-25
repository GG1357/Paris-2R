"""
docstring
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    home page
    """
    return render_template('Newscreen09.html')

@app.route('/map')
def geomap():
    return render_template('map.html')

@app.route('/geofencing')
def geofencing():
    return render_template('figure_116.html')


if __name__ == "__main__":
    app.run(debug=True)