import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total codes in Fund Master:", len(master_codes))
print("Total codes in NAV History:", len(nav_codes))
print("Missing codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
else:
    print("\n✅ All AMFI codes from Fund Master exist in NAV History")
    