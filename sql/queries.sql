-- 1. Top 5 funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per month

SELECT
    substr(date,1,7) AS month,
    AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 3. SIP YoY Growth

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip
FROM investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio < 1%

SELECT
    amfi_code,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- 6. Top 10 Funds by 5-Year Return

SELECT
    amfi_code,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Average Transaction Amount

SELECT
    AVG(amount_inr) AS avg_transaction
FROM investor_transactions;


-- 8. Total Investment by State

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC;


-- 9. Fund House Wise AUM

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;


-- 10. Benchmark Average Close Value

SELECT
    benchmark_name,
    AVG(close_value) AS avg_close
FROM benchmark_indices
GROUP BY benchmark_name;
