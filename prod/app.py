"""
docstring
"""
from backend import run
from flask import Flask, render_template, request

## APP
app = Flask(__name__)

@app.route('/') #, methods=['POST']
def home():
    """
    home page
    """
    return render_template('index.html')


@app.route('/map', methods=['GET','POST'])
def geomap():

    if request.method == 'POST':
        address_from = request.form.get('from')
        address_to = request.form.get('to')
        print(f"ADDRESS : {address_from}")
        print(f"ADDRESS : {address_to}")
        run(address_from, address_to, log=False)
        return render_template('map.html')
    # address_from = "55 Rue du Faubourg Saint-Honoré, 75008 Paris"
    # address_to = "12 Rue Olivier Métra, 75020 Paris"
    # run(address_from, address_to, log=False)
    return render_template('index.html')

@app.route('/geofencing')
def geofencing():
    return render_template('geofencing.html')


if __name__ == "__main__":
    app.run(debug=True)