# Sales-Pipeline-Project
# Automated Sales Analytics Pipeline

An end-to-end data analytics pipeline that automates **sales data cleaning, transformation, database loading, SQL analysis, and Power BI reporting**.

The project demonstrates how raw sales data can be transformed into reliable business insights using **Python, Pandas, PostgreSQL, SQL, Jupyter Notebook, and Power BI**.

---



## 📌 Project Overview

Businesses often receive sales data in raw and inconsistent formats containing:

* Duplicate records
* Missing values
* Inconsistent city names
* Incorrect or missing prices
* Uncalculated revenue fields
* Data quality issues

This project builds a repeatable pipeline to clean and transform raw sales data before loading it into PostgreSQL for analysis and visualization.

### Pipeline

```text
Raw Sales Data
      │
      ▼
Python Data Cleaning
      │
      ▼
Cleaned Sales Data
      │
      ▼
PostgreSQL Database
      │
      ├───────────────┐
      ▼               ▼
Jupyter Analysis   Power BI Dashboard
      │               │
      └───────┬───────┘
              ▼
        Business Insights
```

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Clean and validate raw sales data using Python.
2. Remove duplicate records.
3. Handle missing values.
4. Standardize inconsistent city names.
5. Recalculate revenue-related metrics.
6. Load cleaned data into PostgreSQL.
7. Perform SQL-based business analysis.
8. Create an interactive Power BI dashboard.
9. Build a reusable automated pipeline.
10. Demonstrate an end-to-end analytics workflow suitable for real-world business environments.

---

# 🛠️ Technologies Used

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| Python           | Data processing and automation   |
| Pandas           | Data cleaning and transformation |
| NumPy            | Data manipulation                |
| PostgreSQL       | Data storage and SQL analysis    |
| SQL              | Business analysis                |
| SQLAlchemy       | Python–PostgreSQL connection     |
| Psycopg2         | PostgreSQL database driver       |
| Jupyter Notebook | Exploratory data analysis        |
| Power BI         | Interactive dashboard            |
| Excel/CSV        | Raw and intermediate data        |
| Git & GitHub     | Version control                  |

---

# 📂 Project Structure

```text
Pipeline Project/
│
├── data/
│   ├── sales.xls
│   └── cleaned_sales.xlsx
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_postgresql_loading.ipynb
│   └── 03_data_analysis.ipynb
│
├── scripts/
│   ├── clean_data.py
│   ├── load_postgresql.py
│   └── run_pipeline.py
│
├── logs/
│
├── powerbi/
│   └── Sales_Analytics_Dashboard.pbix
│
├── .gitignore
│
└── README.md
```

> **Note:** The raw `sales.xls` file used in the local project contains CSV-formatted data despite the `.xls` extension. For a production implementation, it is recommended to use the `.csv` extension consistently.

---

# 📊 Dataset

The dataset contains approximately **10,000 sales transactions** after cleaning.

### Main Columns

| Column            | Description             |
| ----------------- | ----------------------- |
| `Order_ID`        | Unique order identifier |
| `Order_Date`      | Date of order           |
| `Customer_ID`     | Customer identifier     |
| `City`            | Customer/order city     |
| `Product`         | Product purchased       |
| `Category`        | Product category        |
| `Quantity`        | Quantity purchased      |
| `Unit_Price`      | Price per unit          |
| `Discount_Pct`    | Discount percentage     |
| `Discount_Amount` | Calculated discount     |
| `Revenue`         | Gross revenue           |
| `Net_Revenue`     | Revenue after discount  |
| `Payment_Method`  | Payment method          |
| `Order_Status`    | Order status            |

---

# 🧹 Data Cleaning

The `clean_data.py` script performs the following operations:

### 1. Duplicate Removal

The raw dataset contains duplicate records.

```python
df = df.drop_duplicates()
```

The pipeline removes duplicate rows before loading the data into PostgreSQL.

### 2. Date Conversion

The `Order_Date` column is converted into a proper datetime format.

### 3. City Standardization

Inconsistent city names are standardized:

```text
delhi      → Delhi
MUMBAI     → Mumbai
Bangalore  → Bengaluru
hyderabad  → Hyderabad
```

### 4. Missing City Values

Missing city values are replaced with:

```text
Unknown
```

### 5. Missing Unit Prices

Missing `Unit_Price` values are replaced using the median price.

### 6. Revenue Calculation

```text
Revenue = Quantity × Unit_Price
```

### 7. Discount Calculation

```text
Discount Amount =
Revenue × Discount Percentage / 100
```

### 8. Net Revenue Calculation

```text
Net Revenue =
Revenue − Discount Amount
```

---

# 🗄️ PostgreSQL Database

After cleaning, the data is loaded into PostgreSQL.

### Database

```text
sales_automation
```

### Table

```text
sales
```

The `load_postgresql.py` script uses:

* SQLAlchemy
* Psycopg2
* Pandas

to load the cleaned dataset into PostgreSQL.

---

# 🔎 SQL Analysis

The PostgreSQL database can be used to answer important business questions.

### Total Revenue

```sql
SELECT
    SUM("Revenue") AS total_revenue
FROM sales;
```

### Total Net Revenue

```sql
SELECT
    SUM("Net_Revenue") AS total_net_revenue
FROM sales;
```

### Revenue by City

```sql
SELECT
    "City",
    SUM("Net_Revenue") AS total_revenue
FROM sales
GROUP BY "City"
ORDER BY total_revenue DESC;
```

### Revenue by Product

```sql
SELECT
    "Product",
    SUM("Net_Revenue") AS total_revenue
FROM sales
GROUP BY "Product"
ORDER BY total_revenue DESC;
```

### Monthly Revenue

```sql
SELECT
    DATE_TRUNC('month', "Order_Date") AS month,
    SUM("Net_Revenue") AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
```

---

# 📈 Power BI Dashboard

The cleaned PostgreSQL data is connected to Power BI to create an interactive sales analytics dashboard.

### Dashboard Analysis

The dashboard focuses on:

* Total Revenue
* Total Net Revenue
* Total Orders
* Total Units Sold
* Average Order Value
* Revenue by City
* Revenue by Product
* Revenue by Category
* Monthly Revenue Trends
* Payment Method Analysis
* Order Status Analysis
* Discount Analysis

### Dashboard Workflow

```text
PostgreSQL
     ↓
Power BI
     ↓
Data Model
     ↓
DAX Measures
     ↓
Interactive Dashboard
```

---

# 🔄 Automation Pipeline

The `run_pipeline.py` script combines the cleaning and PostgreSQL loading processes.

Run:

```powershell
python ".\scripts\run_pipeline.py"
```

This executes:

```text
Raw Sales Data
      ↓
clean_data.py
      ↓
Cleaned Sales Data
      ↓
load_postgresql.py
      ↓
PostgreSQL
      ↓
sales table
```

The complete data pipeline can therefore be executed with a **single command**.

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```bash
cd Pipeline-Project
```

## 2. Install Required Libraries

```bash
pip install pandas openpyxl sqlalchemy psycopg2-binary
```

## 3. Configure PostgreSQL

Create the database:

```sql
CREATE DATABASE sales_automation;
```

Make sure PostgreSQL is running on:

```text
Host: localhost
Port: 5432
```

## 4. Configure Database Credentials

Open:

```text
scripts/load_postgresql.py
```

Update:

```python
DB_USER = "postgres"
DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sales_automation"
```

**Never upload your actual PostgreSQL password to GitHub.**

## 5. Run Data Cleaning

```bash
python ".\scripts\clean_data.py"
```

This creates:

```text
data/cleaned_sales.xlsx
```

## 6. Load Data into PostgreSQL

```bash
python ".\scripts\load_postgresql.py"
```

The data will be loaded into:

```text
sales_automation → public → sales
```

## 7. Run the Complete Pipeline

```bash
python ".\scripts\run_pipeline.py"
```

---

# 🔁 Updating the Dataset

When the raw sales data changes:

```text
Update sales.xls
       ↓
Run run_pipeline.py
       ↓
Data Cleaning
       ↓
PostgreSQL Updated
       ↓
Refresh Power BI
       ↓
Updated Dashboard
```

The existing Power BI report can then use the updated PostgreSQL data without rebuilding the dashboard.

---

# 📓 Jupyter Notebook Analysis

### `01_data_cleaning.ipynb`

* Data inspection
* Missing-value analysis
* Duplicate detection
* Data type conversion
* Data cleaning
* Feature calculations

### `02_postgresql_loading.ipynb`

* PostgreSQL connection
* Database loading
* Table verification
* SQL queries

### `03_data_analysis.ipynb`

* Exploratory Data Analysis
* Revenue analysis
* Product analysis
* City analysis
* Category analysis
* Monthly trends
* Payment analysis
* Order status analysis

---

# 💡 Business Questions Answered

### Sales Performance

* What is the total revenue?
* What is the total net revenue?
* How many orders were placed?
* How many units were sold?
* What is the average order value?

### Geographic Performance

* Which city generates the highest revenue?
* Which cities have the highest order volume?
* Which cities contribute most to overall sales?

### Product Performance

* Which products generate the most revenue?
* Which categories perform best?
* Which products have the highest sales volume?

### Time-Based Analysis

* How does revenue change month over month?
* Which months have the highest sales?
* Are there noticeable sales trends?

### Payment & Order Analysis

* Which payment methods are most commonly used?
* What is the distribution of order statuses?
* How do discounts affect revenue?

---

# 🔐 Security

Never commit sensitive information to GitHub.

Add the following to `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environment
venv/
.venv/

# Environment variables
.env

# Jupyter
.ipynb_checkpoints/

# Logs
*.log

# Local/processed data
data/cleaned_sales.xlsx

# Credentials
secrets/
*.key
```

For a production implementation, database credentials should be stored using environment variables rather than directly inside Python scripts.

---

# 🚀 Future Improvements

Planned improvements include:

* Automated scheduled pipeline execution
* Incremental database loading
* Data quality validation
* Pipeline logging
* Error monitoring
* Automated email alerts
* Power BI scheduled refresh
* Sales anomaly detection
* AI-generated sales summaries
* Sales forecasting
* Customer segmentation
* Demand forecasting
* Machine learning integration

---

# 🏗️ Future Architecture

```text
                    RAW SALES DATA
                          │
                          ▼
                 ┌─────────────────┐
                 │ Python Pipeline │
                 │ Cleaning + ETL  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   PostgreSQL    │
                 │   Data Storage  │
                 └────────┬────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       ┌─────────────┐         ┌─────────────┐
       │   Jupyter   │         │   Power BI  │
       │  Analytics  │         │  Dashboard  │
       └─────────────┘         └──────┬──────┘
                                      │
                                      ▼
                              Business Insights
                                      │
                                      ▼
                                  AI Layer
```

---

# 📌 Skills Demonstrated

* Python
* Pandas
* NumPy
* Data Cleaning
* Data Transformation
* ETL Pipelines
* SQL
* PostgreSQL
* SQLAlchemy
* Psycopg2
* Exploratory Data Analysis
* Business Intelligence
* Power BI
* DAX
* Data Visualization
* Pipeline Automation
* Git & GitHub

---

# 👨‍💻 Connect With Me

**Vikrant Patel**

* GitHub: [VikrantPatel2](https://github.com/VikrantPatel2)
* LinkedIn: [Vikrant Patel](https://www.linkedin.com/in/vikrant-patel-8a5032286/)

---

# ⭐ Project Summary

**Automated Sales Analytics Pipeline** demonstrates an end-to-end analytics workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Transformation
   ↓
PostgreSQL
   ↓
SQL Analysis
   ↓
Jupyter
   ↓
Power BI
   ↓
Business Insights
```

This project showcases how **Python, SQL, PostgreSQL, Jupyter, and Power BI** can work together to create a reusable data analytics and business intelligence solution.

---

## 👨‍💻 Author

**Vikrant Patel**

B.Tech Biotechnology | NIT Jalandhar
Data Analyst | BI | Python | SQL | Power BI

**GitHub:** [VikrantPatel2](https://github.com/VikrantPatel2)
**LinkedIn:** [Vikrant Patel](https://www.linkedin.com/in/vikrant-patel-8a5032286/)

---
