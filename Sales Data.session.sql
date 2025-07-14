SELECT * FROM sales LIMIT 10;

SELECT ProductCategory, SUM(TotalAmount) AS TotalSales
FROM sales 
GROUP BY ProductCategory
ORDER BY TotalSales DESC;

SELECT COUNT(DISTINCT CUSTOMERID) FROM Sales;