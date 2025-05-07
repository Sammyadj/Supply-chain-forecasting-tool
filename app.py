from src.data_loader import load_inventory_data
from src.alert_generator import generate_stock_alerts

def main():
    filepath = "data/retail_store_inventory_data.xlsx"
    df = load_inventory_data(filepath)
    
    print("✅ Data Loaded.")

    alerts = generate_stock_alerts(df)
    if not alerts.empty:
        print("\n⚠️ Low Stock Alerts:")
        print(alerts.to_string(index=False))
    else:
        print("\n✅ All products are sufficiently stocked.")

if __name__ == "__main__":
    main()