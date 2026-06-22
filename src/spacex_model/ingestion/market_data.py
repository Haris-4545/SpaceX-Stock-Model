import pandas as pd
from pathlib import Path

def load_raw_market_data(file_path: str) -> pd.DataFrame:
    """Load raw market data CSV & sort by dated."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No CSV found at {path.absolute()}")
    
    df = pd.read_csv(path, parse_dates=['Date'])

    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.tz_localize(None)

    df = df.sort_values('Date').reset_index(drop=True)

    print(col_count := len(df), f"rows loaded from {path.name}")
    return df