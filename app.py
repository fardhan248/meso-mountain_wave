from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt

omega = 7.292e-5
lat = np.pi/2
f = 2*omega*np.sin(lat)

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    """Return the main page"""
    return render_template("index.html")
"""
@app.route("/update_wspd", methods=["GET", "POST"])
def update_wspd():
   data = request.json
    #wind = float(data["wspd_value"])
    update_rossby(float(data["wspd_value"]))

@app.route("/update_hlfwdt", methods=["GET", "POST"])
def update_hlfwdt():
    data = request.json
    #wind = float(data["wspd_value"])
    update_rossby(float(data["hlfwdt_value"]))
"""

@app.route("/update_rossby", methods=["GET", "POST"])
def update_rossby():
    data = request.json
    wspd = float(data.get("wspd_value"))
    hlfwdt = float(data.get("hlfwdt_value"))
    U = wspd
    a = 1000*hlfwdt
    rossby = U/(f*a)
    rossby = "{0:.4f}".format(rossby)
    return str(rossby)

@app.route("/update_scorer", methods=["GET", "POST"])
def update_scorer():
    data = request.json
    intht = float(data.get("intht_value"))
    llower = float(data.get("llower_value"))
    lupper = float(data.get("lupper_value"))
    H = 1000*intht
    Llower = 0.0001*llower
    Lupper = 0.0001*lupper
    scorer = 4*H*H*(Llower*Llower-Lupper*Lupper)/(np.pi*np.pi)
    scorer = "{0:.4f}".format(scorer)
    return str(scorer)

if __name__ == '__main__':
    app.run(debug=True)
