#This calculates a 5-day Simple Moving Avg & sets up target var(tmr close price)
import pandas as pd
def compute_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['sma_5'] = df['Close'].rolling(window=5).mean()
    return df
def build_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['target'] = df['Close'].shift(-1)
    df = df.dropna().reset_index(drop=True)
    return df