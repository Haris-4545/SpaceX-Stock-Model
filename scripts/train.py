import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from spacex_model.ingestion.market_data import load_raw_market_data
from spacex_model.features.technical import compute_technical_features, build_target
from spacex_model.models.baseline import BaselineRegressor

def main():
    raw_data_path = "data/raw/spcx/teslaaa_stock_max_daily.csv"

    raw_df = load_raw_market_data(raw_data_path)
    feature_df = compute_technical_features(raw_df)
    final_df = build_target(feature_df)

    X = final_df[['sma_5']]
    y = final_df['target']

    split_index = int(len(final_df) * 0.8)
    X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
    y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

    #Run model
    baseline = BaselineRegressor()
    baseline.train(X_train, y_train)

    #Show Performance
    metrics  = baseline.evaluate(X_test, y_test)
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")

if __name__ == "__main__":
    main()