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

    # Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop("species", axis=1)
        y = self.df["species"]
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model

    # Make a prediction based on the user-entered data
    # Returns the predicted species with its respective probability
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probabilty = self.model.predict_proba(data_in).max()
        return prediction[0], probabilty