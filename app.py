from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/iris_model.pkl")

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
