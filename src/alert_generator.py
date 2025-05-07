import pandas as pd

def generate_stock_alerts(df: pd.DataFrame) -> pd.DataFrame:
    """Return a list of low-stock items based on Inventory Level < Demand Forecast."""
    latest_df = df.sort_values("Date").groupby(["Store ID", "Product ID"]).tail(1)
    alerts = latest_df[latest_df["Inventory Level"] < latest_df["Demand Forecast"]]
    return alerts[["Store ID", "Product ID", "Inventory Level", "Demand Forecast"]]