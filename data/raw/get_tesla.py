import yfinance as yf
from pathlib import Path
ticker_symbol = "TSLA"
tsla = yf.Ticker(ticker_symbol)

target_dir = Path(__file__).resolve().parents[2] / "data" / "raw" / "spcx"
target_dir.mkdir(parents=True, exist_ok=True)

output_path = target_dir / "teslaaa_stock_max_daily.csv"

df = tsla.history(period="max", interval="1d")
df.to_csv(output_path)
print(f"File saved as '{output_path}'")