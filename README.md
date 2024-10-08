# UK E-Commerce Sales Analysis with Tableau BI

## Project Overview

This project analyzes a dataset of online sales for a UK-based e-commerce company from December 1, 2010, to December 9, 2011. The dataset includes client ID, unit price, invoice number, stock code, product description, quantity, invoice date, and country.

## Data Source

The dataset used in this project was collected from [Kaggle](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-data).

## Objective

Utilize Tableau BI dashboards to derive data-driven insights into UK e-commerce sales, aiming to enhance business strategies.

## Business Analysis

- **Evaluate Company Performance**
  - Analyze KPIs such as total revenue, total transactions, and average order value (AOV).
  
- **Increase Sales and Optimize Operations**
  - Identify sales patterns to uncover growth opportunities.
  
- **Personalize Marketing**
  - Conduct RFM (Recency, Frequency, Monetary) analysis to segment customers.
  
- **Reduce Customer Churn**
  - Identify at-risk customers and develop retention strategies.
  
- **Analyzing Customer Behavior and Enhancing CLV**
  - Calculate Customer Lifetime Value (CLV) based on historical transaction data.
  
- **Optimize Inventory and Product Offerings**
  - Utilize market basket analysis to enhance product mix and cross-selling opportunities.

## Key Findings

### Evaluate Company Performance
- Throughout the year, transactions and revenue increased, with significant spikes from Q3 onwards. AOV remained consistently high, reflecting substantial customer spending.
- Operations span 37 countries, predominantly with 90% of customers in the UK, and notable presences in Germany and France.

### Personalize Marketing
- "Champions" (7% of customers) generate 40% of total revenue, while "loyal customers" contribute 28% of overall revenue.

### Reduce Customer Churn
- Customer segments labeled "promising" and "at risk" show churn rates of 41% and 100%, respectively.

### Analyzing Customer Behavior and Enhancing CLV
- Customers with higher CLVs are identified as "Champions".

### Optimize Inventory and Product Offerings
- Product association analysis suggests strategic opportunities for cross-selling and product placement.

---

## Dashboard 

You can view the live visualization on Tableau Public [here](https://public.tableau.com/views/RETAILSHOPANALYSIS/SALESDASHBOARD?%3Aembed=yes&%3AshowVizHome=no&%3Atoolbar=no&%3Atabs=no&%3Anoheader=yes#1). 

---

## File Structure

- `notebooks/e-commerce_analysis.ipynb`: Jupyter notebook containing the main script for analyzing the data.
- `data/`: Directory containing the dataset.
- `images/`: Directory containing charts in `.png` format.
- `slides/`: Directory containing information about the presentation.
- `tableau/`: Directory containing information about Tableau dashboards.

## Technologies Used

- Python
- Tableau
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn and others (Refer to requirements-dev.txt for detailed library requirements)

## Installation

To set up the project environment, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
