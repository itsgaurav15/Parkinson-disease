import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("best_model.pkl", "rb"))

@app.route("/")
def home():
    prediction_text=""
    return render_template("index.html",prediction_text=prediction_text)  # Load HTML form

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input features from the form
        features = [float(x) for x in request.form.values()]
        features_array = np.array(features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features_array)
        output = "Parkinson’s Detected" if prediction[0] == 1 else "No Parkinson’s"

        return render_template("index.html", prediction_text=f"Prediction: {output}")

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
