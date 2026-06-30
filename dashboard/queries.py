KPI_QUERY = """
SELECT
    ROUND(SUM(net_revenue)::numeric, 2) AS total_revenue,
    ROUND(AVG(net_revenue)::numeric, 2) AS average_sale,
    COUNT(*) AS transactions,
    SUM(quantity_sold) AS units_sold
FROM sales_transactions
{store_filter};
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