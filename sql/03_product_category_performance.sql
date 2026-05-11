SELECT p.name, SUM(oi.subtotal ) AS total,SUM(oi.quantity) AS total_sell, ct.name FROM products p 
INNER JOIN categories ct ON p.category_id = ct.category_id
INNER JOIN order_items oi  ON p.product_id = oi.product_id
GROUP BY p.name, ct.name 
ORDER BY total DESC LIMIT 10 
