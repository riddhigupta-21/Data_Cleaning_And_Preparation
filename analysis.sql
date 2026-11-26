-- DecodeLabs | Project 3: SQL Data Analysis
-- Dataset table: orders
-- Focus: SELECT, WHERE, ORDER BY, GROUP BY, COUNT, SUM, AVG

-- 1. View the dataset
SELECT * FROM orders LIMIT 10;

-- 2. Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- 3. Total revenue
SELECT ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM orders;

-- 4. Average order value
SELECT ROUND(AVG(TotalPrice), 2) AS average_order_value
FROM orders;

-- 5. Orders above ₹2,000
SELECT OrderID, Date, Product, TotalPrice
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;

-- 6. Orders by status
SELECT OrderStatus, COUNT(*) AS order_count
FROM orders
GROUP BY OrderStatus
ORDER BY order_count DESC;

-- 7. Revenue by product
SELECT Product,
       COUNT(*) AS order_count,
       SUM(Quantity) AS units_sold,
       ROUND(SUM(TotalPrice), 2) AS revenue
FROM orders
GROUP BY Product
ORDER BY revenue DESC;

-- 8. Average order value by product
SELECT Product,
       COUNT(*) AS order_count,
       ROUND(AVG(TotalPrice), 2) AS average_order_value
FROM orders
GROUP BY Product
ORDER BY average_order_value DESC;

-- 9. Payment method analysis
SELECT PaymentMethod,
       COUNT(*) AS order_count,
       ROUND(SUM(TotalPrice), 2) AS revenue
FROM orders
GROUP BY PaymentMethod
ORDER BY revenue DESC;

-- 10. Referral source performance
SELECT ReferralSource,
       COUNT(*) AS orders,
       ROUND(SUM(TotalPrice), 2) AS revenue,
       ROUND(AVG(TotalPrice), 2) AS average_order_value
FROM orders
GROUP BY ReferralSource
ORDER BY revenue DESC;

-- 11. Coupon code performance
SELECT CouponCode,
       COUNT(*) AS orders,
       ROUND(SUM(TotalPrice), 2) AS revenue
FROM orders
GROUP BY CouponCode
ORDER BY revenue DESC;

-- 12. Monthly revenue
SELECT substr(Date, 1, 7) AS month,
       COUNT(*) AS orders,
       ROUND(SUM(TotalPrice), 2) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- 13. Top 10 customers by revenue
SELECT CustomerID,
       COUNT(*) AS orders,
       ROUND(SUM(TotalPrice), 2) AS total_spend
FROM orders
GROUP BY CustomerID
ORDER BY total_spend DESC
LIMIT 10;

-- 14. Delivered orders only
SELECT Product,
       COUNT(*) AS delivered_orders,
       ROUND(SUM(TotalPrice), 2) AS delivered_revenue
FROM orders
WHERE OrderStatus = 'Delivered'
GROUP BY Product
ORDER BY delivered_revenue DESC;

-- 15. Products with revenue above ₹100,000
SELECT Product,
       ROUND(SUM(TotalPrice), 2) AS revenue
FROM orders
GROUP BY Product
HAVING SUM(TotalPrice) > 100000
ORDER BY revenue DESC;
