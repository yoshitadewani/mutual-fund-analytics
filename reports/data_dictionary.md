# Data Dictionary

## 01_fund_master

| Column       | Data Type | Description                   |
| ------------ | --------- | ----------------------------- |
| amfi_code    | INTEGER   | Unique AMFI scheme identifier |
| fund_house   | TEXT      | Mutual fund company           |
| scheme_name  | TEXT      | Name of scheme                |
| category     | TEXT      | Fund category                 |
| sub_category | TEXT      | Fund sub-category             |

Source: 01_fund_master.csv

---

## 02_nav_history

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | INTEGER   | Scheme identifier |
| date      | DATE      | NAV date          |
| nav       | REAL      | Net Asset Value   |

Source: 02_nav_history.csv

---

## 03_aum_by_fund_house

| Column     | Data Type | Description              |
| ---------- | --------- | ------------------------ |
| fund_house | TEXT      | Asset management company |
| aum_crore  | REAL      | Assets under management  |

Source: 03_aum_by_fund_house.csv

---

## 04_monthly_sip_inflows

| Column     | Data Type | Description        |
| ---------- | --------- | ------------------ |
| month      | DATE      | Reporting month    |
| sip_amount | REAL      | Monthly SIP inflow |

Source: 04_monthly_sip_inflows.csv

---

## 05_category_inflows

| Column        | Data Type | Description            |
| ------------- | --------- | ---------------------- |
| category      | TEXT      | Fund category          |
| inflow_amount | REAL      | Category inflow amount |

Source: 05_category_inflows.csv

---

## 06_industry_folio_count

| Column      | Data Type | Description           |
| ----------- | --------- | --------------------- |
| month       | DATE      | Reporting month       |
| folio_count | INTEGER   | Total investor folios |

Source: 06_industry_folio_count.csv

---

## 07_scheme_performance

| Column            | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| amfi_code         | INTEGER   | Scheme identifier       |
| return_1yr_pct    | REAL      | One-year return         |
| return_3yr_pct    | REAL      | Three-year return       |
| return_5yr_pct    | REAL      | Five-year return        |
| expense_ratio_pct | REAL      | Expense ratio           |
| aum_crore         | REAL      | Assets under management |

Source: 07_scheme_performance.csv

---

## 08_investor_transactions

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | TEXT      | Investor identifier        |
| transaction_date | DATE      | Transaction date           |
| amfi_code        | INTEGER   | Scheme identifier          |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr       | REAL      | Transaction amount         |
| state            | TEXT      | Investor state             |
| city             | TEXT      | Investor city              |
| kyc_status       | TEXT      | KYC verification status    |

Source: 08_investor_transactions.csv

---

## 09_portfolio_holdings

| Column        | Data Type | Description           |
| ------------- | --------- | --------------------- |
| amfi_code     | INTEGER   | Scheme identifier     |
| security_name | TEXT      | Holding name          |
| sector        | TEXT      | Sector classification |
| weight_pct    | REAL      | Portfolio weight      |

Source: 09_portfolio_holdings.csv

---

## 10_benchmark_indices

| Column         | Data Type | Description         |
| -------------- | --------- | ------------------- |
| benchmark_name | TEXT      | Benchmark index     |
| date           | DATE      | Observation date    |
| close_value    | REAL      | Closing index value |

Source: 10_benchmark_indices.csv
