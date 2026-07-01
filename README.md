# Mutual Fund Analytics Platform

## Project Overview

This project focuses on building a Mutual Fund Analytics Platform using Python, Pandas, SQLite, SQLAlchemy, SQL, and Power BI. The objective is to ingest, clean, validate, store, analyze, and visualize mutual fund data to support business reporting and investment analytics.

The project follows a structured workflow covering data engineering, database development, exploratory analysis, performance evaluation, and dashboard development.

---

# Objectives

* Perform data ingestion and validation
* Clean and standardize financial datasets
* Create a structured SQLite database
* Design an analytics-ready schema
* Execute analytical SQL queries
* Perform Exploratory Data Analysis (EDA)
* Analyze mutual fund performance using financial metrics
* Build an interactive Power BI dashboard
* Generate project documentation and reports

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* SQLite
* SQLAlchemy
* SQL
* Power BI
* Git & GitHub
* VS Code

---

# Day 1: Data Ingestion & Validation

## Tasks Completed

* Created project folder structure
* Initialized Git repository
* Installed required dependencies
* Loaded source datasets
* Performed data exploration
* Conducted validation checks
* Identified missing values and duplicates
* Generated data quality documentation

## Deliverables

* Data ingestion script
* Validation script
* Data quality report

---

# Day 2: Data Cleaning & Database Creation

## Data Cleaning

* Standardized date formats
* Removed duplicate records
* Validated numerical fields
* Handled missing values
* Standardized categorical values
* Performed consistency checks

## Database Development

* Created SQLite database
* Loaded processed datasets using SQLAlchemy
* Verified successful data loading
* Prepared analytics-ready tables

## SQL Analytics

Developed analytical SQL queries covering:

* Asset growth analysis
* Monthly trend analysis
* Transaction analysis
* Geographic analysis
* Expense ratio analysis
* Performance comparison

## Documentation

Created:

* Database schema
* SQL query documentation
* Data dictionary
* Data quality summary

---

# Day 3: Exploratory Data Analysis (EDA)

## Data Analysis

Performed exploratory analysis on processed mutual fund datasets.

### Activities

* NAV trend analysis
* Category-wise analysis
* Geographic analysis
* Investor analysis
* Correlation analysis
* Portfolio allocation analysis
* Business insights generation

## Visualizations

Created visualizations for:

* NAV Trends
* AUM Analysis
* SIP Trends
* Category Distribution
* Investor Demographics
* Geographic Distribution
* Folio Growth
* Correlation Matrix
* Sector Allocation

## Deliverables

* EDA Notebook
* Visualization Reports
* Business Insights Summary

---

# Day 4: Performance Analytics

## Performance Metrics

Calculated key mutual fund performance metrics including:

* Daily Returns
* CAGR (1-Year, 3-Year and 5-Year)
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown

## Fund Evaluation

Developed a weighted Fund Scorecard using:

* 3-Year CAGR
* Sharpe Ratio
* Alpha
* Expense Ratio
* Maximum Drawdown

## Benchmark Comparison

Performed comparative analysis of mutual fund performance against benchmark indices.

## Reports Generated

* CAGR Comparison
* Sharpe Ratio Report
* Sortino Ratio Report
* Alpha & Beta Report
* Maximum Drawdown Report
* Fund Scorecard
* Benchmark Comparison Summary

---

# Day 5: Interactive Dashboard Development

## Dashboard Development

Built an interactive Power BI dashboard using the processed analytical dataset.

### Dashboard Features

* Industry overview and KPI summary
* Fund performance analysis
* Investor analytics
* SIP and market trend analysis
* Interactive filtering and navigation
* Drill-through navigation
* Report tooltips
* Consistent dashboard theme and branding

## Deliverables

* Power BI Dashboard (.pbix)
* Dashboard PDF Report
* Dashboard Page Exports (PNG)

---
## Project Structure

```text
Mutual_Fund_Analytics/
│
├── Bluestock_MF_Dashboard/
│   ├── bluestock_mf_dashboard.pbix        
│   ├── Dashboard.pdf                      
│   ├── Page1_Industry_Overview.png
│   ├── Page2_Fund_Performance.png
│   ├── Page3_Investor_Analytics.png
│   └── Page4_SIP_Market_Trends.png
│
├── data/
│   ├── raw/
│   │   └── (not included)
│   │
│   └── processed/
│       └── (not included)
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── reports/
│   ├── charts/
│   ├── data_dictionary.md
│   └── data_quality_summary.md
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── amfi_validation.py
├── clean_data.py
├── data_ingestion.py
├── fund_analysis.py
├── live_nav_fetch.py
├── load_db.py
├── bluestock_mf.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Current Status

* ✅ Data Ingestion Completed
* ✅ Data Validation Completed
* ✅ Data Cleaning Completed
* ✅ SQLite Database Created
* ✅ SQL Analytics Completed
* ✅ Exploratory Data Analysis Completed
* ✅ Performance Analytics Completed
* ✅ Interactive Power BI Dashboard Completed
* ✅ Documentation Completed

---

# Key Outcomes

* Built a complete analytics pipeline for mutual fund analysis
* Improved data quality through validation and preprocessing
* Created an analytics-ready SQLite database
* Performed SQL-based business analysis
* Generated comprehensive exploratory analysis
* Calculated industry-standard performance metrics
* Developed an interactive Power BI dashboard for business reporting
* Produced reusable documentation and analytical reports

---

# Future Enhancements

* Automated ETL Pipeline
* Real-Time Mutual Fund Data Integration
* Portfolio Recommendation Engine
* Risk Prediction Models
* Predictive Investment Analytics
* Dashboard Automation and Scheduled Refresh

