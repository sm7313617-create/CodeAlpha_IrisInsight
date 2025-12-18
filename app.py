from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

import os
import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---- SAFE ABSOLUTE PATHS ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "iris_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    pred = model.predict(features)[0]

    species = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(np.max(model.predict_proba(features)))

    return jsonify({
        "species": species[pred],
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# -------------------------------
# Safe absolute paths (Render fix)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "iris_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[ 
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    prediction = model.predict(features)[0]
    species = label_encoder.inverse_transform([prediction])[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(np.max(model.predict_proba(features)))

    return jsonify({
        "species": species,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run()
