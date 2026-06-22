#Basic linear regression

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

class BaselineRegressor:
    def __init__(self):
        self.model = LinearRegression()
    def train(self, X: pd.DataFrame, y: pd.Series):
        self.model.fit(X, y)
        print("Baseline model trained.")
    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> dict:
        predictions = self.model.predict(X)
        mae = mean_absolute_error(y, predictions)
        r2 = r2_score(y, predictions)

        return {"Mean Absolute Error": mae, "R2 Score": r2}