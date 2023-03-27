# importing required libraries

from features import getFeatures
from flask import Flask, request, render_template
import numpy as np
import warnings
import pickle


gbc = pickle.load(open("pickle_model/phishing_model.pkl", "rb"))

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = getFeatures(url)
        x = np.array(obj.featuresArray()).reshape(1, 30)
        predictions = gbc.predict_proba(x)[0, 1]
        print(predictions)
        return render_template('index.html', score=round(predictions, 2), url=url)
    return render_template('index.html', score=42)


if __name__ == "__main__":
    app.run(debug=True)
