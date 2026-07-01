import pandas as pd

# Load processed performance data
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

print("=" * 50)
print(" MUTUAL FUND RECOMMENDATION SYSTEM ")
print("=" * 50)

risk = input("Enter your risk appetite (Low/Medium/High): ").strip().capitalize()

# Map user input to dataset values
risk_map = {
    "Low": ["Low"],
    "Medium": ["Moderate", "Medium"],
    "High": ["High", "Very High"]
}

if risk not in risk_map:
    print("\nInvalid input! Please enter Low, Medium, or High.")
    exit()

# Filter by risk grade
recommended = performance[
    performance["risk_grade"].isin(risk_map[risk])
].copy()

# Sort by Sharpe Ratio (higher is better)
recommended = recommended.sort_values(
    by="sharpe_ratio",
    ascending=False
)

print(f"\nTop Recommended Funds for {risk} Risk Investors:\n")

print(
    recommended[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ].head(5).to_string(index=False)
)