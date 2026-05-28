-- 1. Top 5 χρήστες με τα περισσότερα έσοδα τους τελευταίους 3 μήνες
SELECT u.id, u.name, SUM(o.total_amount) as total_revenue
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at >= NOW() - INTERVAL '3 months'
GROUP BY u.id, u.name
ORDER BY total_revenue DESC
LIMIT 5;

-- 2. Προϊόντα που δεν έχουν αγοραστεί ποτέ
SELECT p.id, p.name, p.category
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;

-- 3. Μηνιαίο revenue ανά κατηγορία (τελευταίοι 6 μήνες) με window function
SELECT
    p.category,
    DATE_TRUNC('month', o.created_at) as month,
    SUM(oi.quantity * oi.unit_price) as monthly_revenue,
    SUM(SUM(oi.quantity * oi.unit_price)) OVER (
        PARTITION BY p.category
        ORDER BY DATE_TRUNC('month', o.created_at)
    ) as cumulative_revenue
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.created_at >= NOW() - INTERVAL '6 months'
GROUP BY p.category, DATE_TRUNC('month', o.created_at);

-- 4. Χρήστες που έκαναν order τον Ιανουάριο αλλά όχι τον Φεβρουάριο
SELECT DISTINCT u.id, u.name
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE DATE_TRUNC('month', o.created_at) = '2024-01-01'
AND u.id NOT IN (
    SELECT DISTINCT user_id FROM orders
    WHERE DATE_TRUNC('month', created_at) = '2024-02-01'
);