-- Cannabis Retail Intelligence Platform
-- Business Analysis Queries

-- 1. Revenue by Store
SELECT
    store_id,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue,
    COUNT(*) AS transactions
FROM sales_transactions
GROUP BY store_id
ORDER BY revenue DESC;

-- 2. Average Sale by Store
SELECT
    store_id,
    ROUND(AVG(net_revenue)::numeric, 2) AS average_sale,
    COUNT(*) AS transactions
FROM sales_transactions
GROUP BY store_id
ORDER BY average_sale DESC;

-- 3. Revenue by Category
SELECT
    p.category,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue,
    SUM(s.quantity_sold) AS units_sold
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 4. Top Brands by Revenue
SELECT
    p.brand,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue,
    SUM(s.quantity_sold) AS units_sold
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.brand
ORDER BY revenue DESC
LIMIT 10;

-- 5. Estimated Profit by Brand
SELECT
    p.brand,
    ROUND(SUM((p.retail_price - p.unit_cost) * s.quantity_sold)::numeric, 2) AS estimated_profit,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.brand
ORDER BY estimated_profit DESC
LIMIT 10;

-- 6. Monthly Revenue Trend
SELECT
    DATE_TRUNC('month', transaction_date::date) AS month,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue
FROM sales_transactions
WHERE transaction_date IS NOT NULL
GROUP BY month
ORDER BY month;