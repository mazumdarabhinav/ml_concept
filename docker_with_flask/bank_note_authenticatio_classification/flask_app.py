from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)  # From which point to start the flask application
# Load the pickle file
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route("/")
def welcome():
    return "Welcome ALL"


@app.route("/predict")
def predict_note_autentication():
    variance = request.args.get("variance")
    skweness = request.args.get("skweness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")

    prediction = classifier.predict([[variance, skweness, curtosis, entropy]])
    return "The predicted value is :" + str(prediction)


@app.route("/predict_file", methods=["POST"])
def predict_note_autentication_using_csv_file():
    df = pd.read_csv(request.files.get("files"))
    prediction = classifier.predict(df)
    return "The predicted value is :" + str(list(prediction))


if __name__ == "__main__":
    app.run(debug=True)
