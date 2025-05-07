import pandas as pd
from prophet import Prophet

def forecast_product_demand(df: pd.DataFrame, product_id: str, store_id: str, periods: int = 14) -> pd.DataFrame:
    """Forecast demand for a specific product at a specific store using Prophet."""
    filtered = df[(df["Product ID"] == product_id) & (df["Store ID"] == store_id)]

    # Prepare data for Prophet
    prophet_df = filtered[["Date", "Units Sold"]].rename(columns={"Date": "ds", "Units Sold": "y"})
    
    # Train model
    model = Prophet()
    model.fit(prophet_df)

    # Create future dataframe
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]