# 📦 Supply Chain Data Visualisation & Forecasting Tool

An internal analytics tool designed to track product availability trends, forecast demand using time series models, and alert managers to low-stock products — all powered by Python and Excel dashboards.

---

## 📌 Project Objective

Retail operations often suffer from stockouts or overstocking due to inaccurate demand forecasting and lack of real-time inventory insights. This project solves that problem by:

- Forecasting future product demand using historical sales data.
- Identifying low-stock items and generating reorder alerts.
- Visualising trends and forecasts in a user-friendly Excel dashboard for decision-making.

---

## 📊 Dataset Description

This project uses a publicly available **retail store inventory dataset** which contains daily inventory and sales records across multiple stores and product categories.

### Key Columns:

| Feature             | Description                                   |
| ------------------- | --------------------------------------------- |
| `Date`              | Daily record timestamp                        |
| `Store ID`          | Unique store identifier                       |
| `Product ID`        | Unique product identifier                     |
| `Category`          | Product category (e.g., Toys, Electronics)    |
| `Region`            | Store region (e.g., East, West)               |
| `Inventory Level`   | Stock available at the start of the day       |
| `Units Sold`        | Total units sold on the day                   |
| `Demand Forecast`   | Forecasted units for that day                 |
| `Holiday/Promotion` | Flag for promotions/holidays affecting demand |
| `Weather Condition` | (Optional) External factor affecting sales    |

---

## 🧱 Project Structure

```bash
supply_chain_tool/
├── data/
│   ├── retail_store_inventory_data.xlsx       # Raw inventory data
│   └── output_forecast.xlsx                   # Forecast and alert output
├── notebooks/
│   └── demand_forecasting.ipynb               # Jupyter notebook for analysis
├── src/
│   ├── data_loader.py                         # Data ingestion and cleaning
│   ├── forecaster.py                          # Time series model with Prophet
│   ├── alert_generator.py                     # Low-stock alert engine
├── app.py                                     # CLI to trigger alerts
└── requirements.txt                           # Python dependencies
```
