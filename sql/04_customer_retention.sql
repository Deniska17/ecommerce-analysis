
WITH monthly_customers AS (
    SELECT 
        STRFTIME('%Y-%m', order_date) AS month,
        customer_id
    FROM orders
    GROUP BY month, customer_id
)
SELECT 
    m1.month,
    COUNT(DISTINCT m1.customer_id) AS active_customers,
    COUNT(DISTINCT m2.customer_id) AS retained_customers,
    ROUND(COUNT(DISTINCT m2.customer_id) * 100.0 / COUNT(DISTINCT m1.customer_id), 1) AS retention_rate_pct
FROM monthly_customers m1
LEFT JOIN monthly_customers m2 
    ON m2.customer_id = m1.customer_id
    AND m2.month = STRFTIME('%Y-%m', date(m1.month || '-01', '+1 month'))
GROUP BY m1.month
ORDER BY m1.month