KPI_QUERY = """
SELECT
    ROUND(SUM(s.net_revenue)::numeric, 2) AS total_revenue,
    ROUND(SUM((p.retail_price - p.unit_cost) * s.quantity_sold)::numeric, 2) AS estimated_profit,
    ROUND(
        (
            SUM((p.retail_price - p.unit_cost) * s.quantity_sold)
            / NULLIF(SUM(s.net_revenue), 0)
        )::numeric * 100,
        2
    ) AS profit_margin,
    ROUND(AVG(s.net_revenue)::numeric, 2) AS average_sale,
    COUNT(*) AS transactions,
    SUM(s.quantity_sold) AS units_sold
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
{store_filter_with_alias};
"""


CATEGORY_QUERY = """
SELECT
    p.category,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
{store_filter_with_alias}
GROUP BY p.category
ORDER BY revenue DESC;
"""


BRAND_QUERY = """
SELECT
    p.brand,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
{store_filter_with_alias}
GROUP BY p.brand
ORDER BY revenue DESC
LIMIT 10;
"""


STORE_QUERY = """
SELECT
    store_id,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue,
    COUNT(*) AS transactions
FROM sales_transactions
GROUP BY store_id
ORDER BY revenue DESC;
"""


MONTHLY_QUERY = """
SELECT
    DATE_TRUNC('month', transaction_date::date) AS month,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue
FROM sales_transactions
WHERE transaction_date IS NOT NULL
{monthly_store_filter}
GROUP BY month
ORDER BY month;
"""