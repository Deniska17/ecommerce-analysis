WITH rfm AS (
	SELECT 
		customer_id,
		MAX(order_date) AS last_order_date,
		COUNT(order_id) AS order_count,
		ROUND(SUM(total_amount),2) AS total_spend
	FROM orders
	GROUP BY customer_id)
SELECT c.first_name || ' '|| c.last_name AS customer_name,
	r.last_order_date,
	CAST(julianday('now') - julianday(r.last_order_date) AS INTEGER) AS days_since_last_order,
    r.last_order_date ,
	r.order_count, 
	r.total_spend,
	CASE 
	WHEN r.order_count  >= 5 AND r.total_spend >= 1000 THEN 'VIP'
    WHEN r.order_count >= 3 AND r.total_spend >= 500  THEN 'Loyal'
    WHEN CAST(julianday('now') - julianday(r.last_order_date) AS INTEGER) <= 60                  THEN 'Recent'
    ELSE 'At Risk'
END AS segment 
FROM rfm r 
INNER JOIN customers c ON c.customer_id = r.customer_id 
ORDER BY days_since_last_order DESC
---

