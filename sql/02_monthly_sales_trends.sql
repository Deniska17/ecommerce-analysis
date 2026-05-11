SELECT
	STRFTIME('%Y-%m',order_date) AS month,
	COUNT(*) AS orders_count,
	SUM(total_amount) AS global_spend,
	ROUND(AVG(total_amount),2) AS med_price
	FROM orders
	GROUP BY month
	ORDER BY month DESC