import pandas as pd

def load_inventory_data(filepath: str) -> pd.DataFrame:
    """Load inventory data from Excel file."""
    df = pd.read_excel(filepath)
    df["Date"] = pd.to_datetime(df["Date"])  # ensure datetime format
    return df

def get_latest_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return the latest snapshot of inventory for each product at each store."""
    return df.sort_values("Date").groupby(["Store ID", "Product ID"]).tail(1)