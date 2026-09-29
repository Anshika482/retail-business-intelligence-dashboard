-- Retail Sales Analytics SQL Analysis
-- Compatible with SQLite / MySQL with minor date-function changes.

-- 1. Overall KPIs
SELECT
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) * 100.0 / NULLIF(SUM(Revenue),0), 2) AS profit_margin
FROM retail_sales;

-- 2. Monthly revenue trend
SELECT
    strftime('%Y-%m', Order_Date) AS month,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY month
ORDER BY month;

-- 3. Region performance
SELECT
    Region,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit,
    COUNT(DISTINCT Order_ID) AS orders
FROM retail_sales
GROUP BY Region
ORDER BY revenue DESC;

-- 4. Category performance
SELECT
    Category,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit,
    ROUND(SUM(Profit)*100.0/NULLIF(SUM(Revenue),0),2) AS margin_pct
FROM retail_sales
GROUP BY Category
ORDER BY revenue DESC;

-- 5. Top 10 products
SELECT
    Product,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY Product
ORDER BY revenue DESC
LIMIT 10;

-- 6. Customer segment contribution
SELECT
    Customer_Segment,
    COUNT(DISTINCT Order_ID) AS orders,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit
FROM retail_sales
GROUP BY Customer_Segment
ORDER BY revenue DESC;

-- 7. Low-margin products for investigation
SELECT
    Product,
    ROUND(SUM(Revenue),2) AS revenue,
    ROUND(SUM(Profit),2) AS profit,
    ROUND(SUM(Profit)*100.0/NULLIF(SUM(Revenue),0),2) AS margin_pct
FROM retail_sales
GROUP BY Product
HAVING SUM(Revenue) > 0
ORDER BY margin_pct ASC
LIMIT 10;
