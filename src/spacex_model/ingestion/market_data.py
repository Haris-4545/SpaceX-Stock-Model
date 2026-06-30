import pandas as pd
from pathlib import Path

from spacex_model.ingestion.validation import validate_market_df

def load_raw_market_data(file_path: str) -> pd.DataFrame:
    """Load raw market data CSV & sort by dated."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No CSV found at {path.absolute()}")
    
    df = pd.read_csv(path, parse_dates=['Date'])

    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.tz_convert(None)

    df = df.sort_values('Date').reset_index(drop=True)

    validate_market_df(df, name=path.name)
    
    return df