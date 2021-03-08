from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)  # From which point to start the flask application
Swagger(app)
# Load the pickle file
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route("/")
def welcome():
    return "Welcome ALL"


@app.route("/predict")
def predict_note_autentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skweness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = request.args.get("variance")
    skweness = request.args.get("skweness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")

    prediction = classifier.predict([[variance, skweness, curtosis, entropy]])
    return "The predicted value is :" + str(prediction)


@app.route("/predict_file", methods=["POST"])
def predict_note_autentication_using_csv_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: files
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df = pd.read_csv(request.files.get("files"))
    prediction = classifier.predict(df)
    return "The predicted value is :" + str(list(prediction))


if __name__ == "__main__":
    app.run(debug=True)
