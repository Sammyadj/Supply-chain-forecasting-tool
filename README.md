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

This project uses a publicly available [**retail store inventory dataset**](https://www.kaggle.com/datasets/anirudhchauhan/retail-store-inventory-forecasting-dataset) which contains daily inventory and sales records across multiple stores and product categories.

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

\`\`\`bash
supply_chain_tool/
├── data/
│ ├── retail_store_inventory_data.xlsx # Raw inventory data
│ └── output_forecast.xlsx # Forecast and alert output
├── notebooks/
│ └── demand_forecasting.ipynb # Jupyter notebook for analysis
├── src/
│ ├── data_loader.py # Data ingestion and cleaning
│ ├── forecaster.py # Time series model with Prophet
│ ├── alert_generator.py # Low-stock alert engine
├── app.py # CLI to trigger alerts
└── requirements.txt # Python dependencies
\`\`\`

---

## 🚀 How It Works

1. **Data Ingestion**  
   Inventory data is loaded from Excel (`data_loader.py`) and preprocessed for analysis.

2. **Forecasting**  
   For each selected product-store pair, the system:

   - Trains a [Prophet](https://facebook.github.io/prophet/) model on past `Units Sold`
   - Generates a 14-day forecast with `yhat`, `yhat_lower`, and `yhat_upper`

3. **Alert Generation**  
   The tool flags products where `Inventory Level < Demand Forecast` — triggering a **restock alert**.

4. **Excel Dashboard**
   - Forecasts and alerts are saved to `output_forecast.xlsx`
   - Managers use line charts and conditional formatting in Excel/Google Sheets to monitor performance
   - Charts include confidence bands for demand forecasting (`yhat_lower`, `yhat_upper`)

---

## 📈 Sample Analysis

- 📉 **Line Charts**: Forecasted demand with confidence intervals
- 🚨 **Alerts**: Products expected to fall below reorder thresholds
- 🌍 **Region-wise Trends**: Pivot tables for comparative inventory risk across regions
- 📆 **Time-based Trends**: Seasonal variations and promotion impacts on sales

---

## ✅ Results

- **Improved visibility** into real-time stock levels and future demand
- **Faster decision-making** via Excel-integrated dashboards
- **Reduction in stockouts** by preemptively alerting for reorder points
- Modular structure ready for expansion into:
  - Supplier performance tracking
  - Price optimization
  - Weather and promotion impact modeling

---

## 🛠️ Technologies Used

- Python 3.10+
- `pandas`, `openpyxl` – Data handling & Excel I/O
- `prophet` – Time series forecasting
- `jupyter` – Exploratory notebooks
- Google Sheets or Excel – Final visualisation layer

---

## 📂 Installation & Usage

\`\`\`bash

# Clone the repo

git clone https://github.com/yourusername/supply-chain-forecasting-tool.git
cd supply-chain-forecasting-tool

# Install dependencies

pip install -r requirements.txt

# Run alert generator

python app.py
\`\`\`

To generate new forecasts and charts, open the notebook:
\`\`\`bash
notebooks/demand_forecasting.ipynb
\`\`\`

---

## 📎 Use Cases

- Inventory optimization in retail chains
- Demand planning in FMCG/logistics
- Sales forecasting dashboards for non-technical teams

---

## 🙋‍♂️ Author

**[Your Name]**  
MSc Computer Science, University of Sussex  
🔗 [LinkedIn Profile](https://linkedin.com/in/yourusername)  
📫 Reach me via [Email](mailto:your.email@example.com)

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## ⭐ Star This Repo

If you found this project useful, feel free to ⭐ star it and share!
