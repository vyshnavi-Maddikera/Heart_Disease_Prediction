from flask import Flask, render_template, request
import pickle
import pandas as pd
from pathlib import Path

app = Flask(__name__)

# --------------------------------------------------
# LOAD THE TRAINED MODEL
# --------------------------------------------------

MODEL_PATH = Path(__file__).parent / "heart_disease_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# FEATURES USED BY THE MODEL
# --------------------------------------------------

FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get values from HTML form

        age = float(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])


        # Create patient dataframe

        patient = pd.DataFrame(
            [[
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal
            ]],
            columns=FEATURES
        )


        # Make prediction

        prediction = model.predict(patient)[0]


        # Get probability

        probability = model.predict_proba(patient)[0][1] * 100


        # --------------------------------------------------
        # RESULT
        # --------------------------------------------------

        if prediction == 1:

            result = "Heart Disease Detected"

            result_type = "risk"

            message = (
                "The model detected a pattern associated "
                "with the positive class in the dataset."
            )

        else:

            result = "No Heart Disease Detected"

            result_type = "safe"

            message = (
                "The model detected a pattern associated "
                "with the negative class in the dataset."
            )


        # Send result to HTML

        return render_template(
            "index.html",
            result=result,
            result_type=result_type,
            message=message,
            probability=round(probability, 2)
        )


    except Exception as e:

        return render_template(
            "index.html",
            error="Please enter valid values in all fields."
        )


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)