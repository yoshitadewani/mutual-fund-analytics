# Data Quality Summary

## Dataset Validation

* Successfully loaded all 10 mutual fund datasets.
* Verified dataset structure, columns, and data types.
* Successfully fetched live NAV data from MFAPI.
* Fund houses, categories, sub-categories, and risk categories were explored.

## AMFI Code Validation

* Total AMFI codes in fund_master: 40
* Total AMFI codes in nav_history: 40
* Missing AMFI codes: 0

Result: All AMFI codes present in fund_master exist in nav_history. No missing or invalid AMFI codes were found.

## Conclusion

The datasets passed initial ingestion and validation checks and are ready for further analysis.
