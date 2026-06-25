# Data Quality Report

## Initial Audit Summary

| File | Rows | Duplicate Rows | Missing Value Issues |
|---|---:|---:|---|
| products.csv | 500 | 0 | brand: 10, cbd_percent: 15 |
| purchase_orders.csv | 15,075 | 75 | total_cost: 226 |
| inventory_snapshots.csv | 419,254 | 1,254 | quantity_on_hand: 4,193 |
| customer_loyalty.csv | 20,080 | 80 | total_lifetime_spend: 400 |
| vendors.csv | 50 | 0 | lead_time_days: 1 |
| sales_transactions.csv | 251,000 | 1,000 | discount_amount: 5,011 |
| employees.csv | 76 | 1 | hourly_rate: 1 |
| stores.csv | 4 | 0 | None |

## Key Findings

The largest data quality issue appears in `sales_transactions.csv`, which contains 1,000 duplicate rows and 5,011 missing discount values.

The largest table, `inventory_snapshots.csv`, contains 419,254 records, 1,254 duplicate rows, and 4,193 missing inventory quantity values.

The `stores.csv` dimension table appears clean, with no duplicate rows or missing values.

## Next Cleaning Steps

1. Remove duplicate rows from all tables.
2. Fill missing `discount_amount` values with 0.
3. Investigate missing `quantity_on_hand` values before deciding whether to fill with 0 or flag as unknown.
4. Fill missing `total_lifetime_spend` values using customer transaction history if possible.
5. Fill missing vendor `lead_time_days` using the median lead time.
6. Review missing product `brand` and `cbd_percent` values.