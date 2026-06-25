-- Revenue by Store

SELECT
    store_id,
    ROUND(SUM(total_amount), 2) AS revenue,
    COUNT(*) AS transactions
FROM sales_transactions
GROUP BY store_id
ORDER BY revenue DESC;