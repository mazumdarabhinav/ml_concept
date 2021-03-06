# Make an API to predict the species of iris flower based on user input
# Necesaary Imports

import uvicorn
from fastapi import FastAPI
from model import IrisModel, IrisSpecies

# Create an App and Iris Model Object

app = FastAPI()
model = IrisModel()

# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted flower species with the confidence


@app.post("/predict")
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    )
    return {"prediction": prediction, "probability": probability}


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
