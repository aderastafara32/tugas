
import os, random, string

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import json


app = Flask(__name__)


# curl -i -X POST http://127.0.0.1:5000/api/v2/getBMI -H 'Content-Type: application/json' -d '{"bb":40, "tb":1.6}'
@app.route("/api/v2/getBMI",  methods=["POST"])
def getBMI():
    req = request.json
    bb = req['bb']
    tb = req['tb']

    bmi = float(bb)/float(tb)


    if bmi < 18.5 :
        return jsonify({'bmi' : bmi, "kesimpulan": "Kurus"}), 200
    elif bmi >= 18.5 or bmi <= 25 :
        return jsonify({'bmi' : bmi, "kesimpulan": "Normal"}), 200
    elif bmi >= 25 or bmi <= 40 :
        return jsonify({'bmi' : bmi, "kesimpulan": "Berlebih"}), 200
    elif bmi > 40 :
        return jsonify({'bmi' : bmi, "kesimpulan": "Bahaya"}), 200
    else :
        return jsonify({'bmi' : bmi, "kesimpulan": "Tidak terdefinisi"}), 200

if __name__ == "__main__":
    app.run(debug=True)

