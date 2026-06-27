# Mutual Fund Analytics Platform

## Project Overview

This project focuses on building a Mutual Fund Analytics Platform using Python, Pandas, SQLite, SQLAlchemy, and SQL. The objective is to ingest, clean, validate, store, and analyze mutual fund data to support business reporting and investment analytics.

---

## Objectives

* Perform data ingestion and validation
* Clean and standardize financial datasets
* Create a structured SQLite database
* Design an analytics-ready schema
* Execute analytical SQL queries
* Generate project documentation

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* SQL
* Git & GitHub
* VS Code

---

## Day 1: Data Ingestion & Validation

### Tasks Completed

* Created project folder structure
* Initialized Git repository
* Installed required dependencies
* Loaded source datasets for analysis
* Performed data exploration and profiling
* Conducted validation checks
* Identified missing values and duplicates
* Generated data quality documentation

### Deliverables

* Data ingestion script
* Validation script
* Data quality report

---

## Day 2: Data Cleaning & Database Creation

### Data Cleaning

* Standardized date formats
* Removed duplicate records
* Validated numerical fields
* Handled missing values
* Standardized categorical values
* Performed consistency checks across datasets

### Database Development

* Created SQLite database
* Loaded processed datasets using SQLAlchemy
* Verified successful data loading
* Prepared analytics-ready tables

### SQL Analytics

Developed analytical SQL queries covering:

* Asset growth analysis
* Monthly trend analysis
* Transaction analysis
* Geographic analysis
* Expense ratio analysis
* Performance comparisons

### Documentation

Created:

* Database schema documentation
* SQL query documentation
* Data dictionary
* Data quality summary

---
## Day 3: Exploratory Data Analysis (EDA)

### Data Analysis

Performed exploratory analysis on the processed mutual fund datasets.

Activities included:

- Created analytical visualizations
- Analyzed time-series trends
- Performed category-wise analysis
- Explored investor demographics
- Conducted geographic analysis
- Evaluated portfolio allocation
- Generated correlation analysis
- Documented analytical observations

### Visualization Development

Created multiple visualizations covering:

- NAV trend analysis
- AUM analysis
- SIP trend analysis
- Category distribution
- Investor demographics
- Geographic distribution
- Folio growth
- Correlation analysis
- Sector allocation

### Documentation

Created:

- EDA notebook
- Visualization reports
- Business insights summary

### Deliverables

- EDA analysis notebook
- Visualization reports
- Summary documentation
- 
## Project Structure

```text
mutual-fund-analytics/
│
├── data/
│   ├── raw/                 # Raw source datasets
│   └── processed/           # Cleaned datasets
│
├── notebooks/
│   └── EDA_Analysis.ipynb   # Exploratory Data Analysis
│
├── reports/
│   ├── charts/              # Exported visualizations
│   ├── data_dictionary.md
│   └── data_quality_summary.md
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── clean_data.py
├── data_ingestion.py
├── amfi_validation.py
├── load_db.py
├── fund_analysis.py
│
├── bluestock_mf.db          # SQLite database
├── requirements.txt
├── README.md
└── .gitignore
```
---

##Current Status

✅ Data Ingestion Complete

✅ Data Validation Complete

✅ Data Cleaning Complete

✅ SQLite Database Created

✅ SQL Analytics Completed

✅ Exploratory Data Analysis Completed

✅ Documentation Completed
---

## Key Outcomes

* Built a structured data pipeline
* Improved data quality through validation and cleaning
* Created a centralized SQLite database
* Enabled analytical reporting through SQL queries
* Documented the complete workflow for reproducibility
* Generated analytical visualizations for business reporting

Produced documentation supporting exploratory data analysis

---

## Future Enhancements

* Advanced Exploratory Data Analysis (EDA)
* Interactive Dashboards
* Automated ETL Pipeline
* Real-Time Data Integration
* Performance Monitoring & Reporting
