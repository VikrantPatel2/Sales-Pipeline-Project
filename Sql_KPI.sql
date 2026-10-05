
--- sales record

select * from sales

--- data type change of the columns
ALTER TABLE sales
ALTER COLUMN "Order_Date" TYPE DATE
USING "Order_Date"::DATE;

--- record coulmns

SELECT column_name
FROM information_schema.columns
WHERE table_name = 'sales'
ORDER BY ordinal_position;

--- total rows
select count(*) from sales

----  total revenue
select 
	sum("Net_Revenue") as revenue
	from sales

---total orders
select 
		count( Distinct "Order_ID") as total_Orders
	from sales

--- total Unit Sold
select 
		sum("Quantity")as Unit_Sold
	from sales

--- Average Order Value

select 
	sum("Net_Revenue")/count( Distinct "Order_ID") as Average_Order_Value
	from sales

---- Analyze revenue by city
SELECT
    "City",
    SUM("Net_Revenue") AS total_revenue
FROM sales
GROUP BY "City"
ORDER BY total_revenue DESC;

---Analyze products
SELECT
    "Product",
    SUM("Quantity") AS units_sold,
    SUM("Net_Revenue") AS total_revenue
FROM sales
GROUP BY "Product"
ORDER BY total_revenue DESC;



--- Monthly Revenue
SELECT
    DATE_TRUNC('month', "Order_Date") AS month,
    SUM("Net_Revenue") AS revenue
FROM sales
GROUP BY month
ORDER BY month;

---- Top Product

SELECT
    "Product",
    SUM("Net_Revenue") AS revenue,
    SUM("Quantity") AS units_sold
FROM sales
GROUP BY "Product"
ORDER BY revenue DESC
LIMIT 10;

----Create a KPI table
CREATE TABLE sales_kpis AS
SELECT
    COUNT(DISTINCT "Order_ID") AS total_orders,
    SUM("Quantity") AS total_units,
    SUM("Net_Revenue") AS total_revenue,
    AVG("Net_Revenue") AS average_transaction_value
FROM sales;

SELECT *
FROM sales_kpis;


----Create a daily KPI table
CREATE TABLE daily_sales_kpi AS
SELECT
    "Order_Date"::date AS order_date,
    COUNT(DISTINCT "Order_ID") AS orders,
    SUM("Quantity") AS units_sold,
    SUM("Net_Revenue") AS revenue
FROM sales
GROUP BY "Order_Date"::date
ORDER BY order_date;