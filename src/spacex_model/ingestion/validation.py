import pandas as pd

REQUIRED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]

def validate_market_df(df: pd.DataFrame, name: str = "dataset") -> None:
    errors = []

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        errors.append(f"Missing columns: {missing}")

    if df.empty:
        errors.append("DataFrame is empty")

    if "Close" in df.columns:
        null_pct = df["Close"].isnull().mean()
        if null_pct > 0.05:
            errors.append(f"'Close' has {null_pct:.1%} nulls (threshold 5%)")

    if "Date" in df.columns:
        if not df["Date"].is_monotonic_increasing:
            errors.append("Dates are not in ascending order.")
        dupes = df["Date"].duplicated().sum()
        if dupes:
            errors.append(f"{dupes} duplicate dates found.")

    for col in ["Open", "High", "Low", "Close"]:
        if col in df.columns and (df[col] <= 0).any():
            errors.append(f"'{col}' contains non-positive values.")

    if errors:
        raise ValueError(f"[{name}] Validation failed:\n  " + "\n  ".join(errors))
    
    print(f"[{name}] {len(df)} rows | {df['Date'].min().date()} → {df['Date'].max().date()}")