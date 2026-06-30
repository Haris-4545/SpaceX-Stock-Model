import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Which columns are model inputs.
FEATURE_COLS = [
    "sma_5", "sma_10", "sma_20", "sma_50", "ema_12", "ema_26", "macd", "macd_signal", "macd_hist", "rsi_14", "bb_width", "bb_pct", "atr_14", "vol_ratio", "obv", "ret_1d", "ret_3d", "ret_5d", "ret_10d", "ret_21d",
]

class XGBoostPredictor:
    def __init__(self, params: dict | None = None):
        defaults = dict(n_estimators=300, max_depth=4, leaning_rate=0.05, subsample=0.8, colsample_bytree=0.8, random_state=42, n_jobs=-1, objective="reg:squarederror")
        self.model = XGBRegressor(**{**defaults, **(params or {})})
        self._features: list[str] = []

    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        self._features = X.columns.tolist()
        self.model.fit(X, y, verbose=False)
        print(f"Trained on {len(X)} rows x {len(self._features)} features")

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X)
    
    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> dict:
        p = self.predict(X)
        return {"MAE": mean_absolute_error(y, p), "R2": r2_score(y, p), "RMSE": float(np.sqrt(np.mean((y-p) ** 2)))}
    
    def feature_importance(self) -> pd.Series:
        return pd.Series(self.model.feature_importances_, index=self._features).sort_values(ascending=False)
    
    def save(self, path: str | Path) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self, path)
    
    @classmethod
    def load(cls, path: str | Path) -> "XGBoostPredictor":
        return joblib.load(path)