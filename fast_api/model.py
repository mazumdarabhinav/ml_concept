# Classifier which classifies iris flower dataset

# Necessary imports
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib

# Class which describes singel flower measurement
class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Class for training the model and making predictions
class IrisModel:
    # Class constructor, loads the dataset and loads the model
    # if exists. If not, calls the _train_model method and
    # saves the model

    def __init__(self):
        self.df = pd.read_csv("iris.csv")
        self.model_fname_ = "iris_model.pkl"

        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
