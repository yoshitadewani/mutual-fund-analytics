import pandas as pd
import os

nav = pd.read_csv("data/raw/02_nav_history.csv")

print(nav.head())
print(nav.shape)
print(nav.columns)
nav['date'] = pd.to_datetime(nav['date'])
print(nav.dtypes)
nav = nav.sort_values(
    ['amfi_code', 'date']
)
print(nav.head(10))
print(nav.isnull().sum())
nav['nav'] = (
    nav.groupby('amfi_code')['nav']
       .ffill()
)
nav = nav.drop_duplicates()
print(nav['nav'].isnull().sum())
print("Duplicates:", nav.duplicated().sum())
print("Invalid NAV:", (nav['nav'] <= 0).sum())
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("nav_history_clean.csv saved successfully")

# Load investor transactions

tx = pd.read_csv("data/raw/08_investor_transactions.csv")

print(tx.head())

print(tx.shape)

print(tx.columns)
tx['transaction_date'] = pd.to_datetime(
    tx['transaction_date']
)

print(tx.dtypes)
print(tx['transaction_date'].dtype)
print(tx['transaction_type'].unique())
tx['transaction_type'] = (
    tx['transaction_type']
    .str.strip()
    .str.lower()
)

tx['transaction_type'] = tx['transaction_type'].replace({
    'sip': 'SIP',
    'lumpsum': 'Lumpsum',
    'redemption': 'Redemption'
})

print(tx['transaction_type'].unique())
valid_types = ['SIP', 'Lumpsum', 'Redemption']

invalid_types = tx[
    ~tx['transaction_type'].isin(valid_types)
]

print("Invalid transaction types:", len(invalid_types))
print("Invalid Amounts:", (tx['amount_inr'] <= 0).sum())
# Check KYC status values

print(tx['kyc_status'].unique())

valid_kyc = [
    'Verified',
    'Pending',
    'Rejected'
]

invalid_kyc = tx[
    ~tx['kyc_status'].isin(valid_kyc)
]

print("Invalid KYC:", len(invalid_kyc))
tx.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("investor_transactions_clean.csv saved")

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(perf.shape)
print(perf.columns)
# =========================
# SCHEME PERFORMANCE CLEANING
# =========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Return columns ko numeric banao
return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

# Expense ratio numeric
perf['expense_ratio_pct'] = pd.to_numeric(
    perf['expense_ratio_pct'],
    errors='coerce'
)

# Missing return values (anomalies)
anomalies = perf[
    perf[return_cols]
    .isnull()
    .any(axis=1)
]

print("Anomalies:", len(anomalies))

# Expense ratio range check
expense_issues = perf[
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
]

print("Expense Ratio Issues:",
      len(expense_issues))

# Save cleaned file
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(
    "scheme_performance_clean.csv saved"
)
# Remaining datasets

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}")

    # Remove duplicates
    df = df.drop_duplicates()

    output_name = file.replace(".csv", "_clean.csv")

    df.to_csv(
        f"data/processed/{output_name}",
        index=False
    )

    print(f"{output_name} saved")