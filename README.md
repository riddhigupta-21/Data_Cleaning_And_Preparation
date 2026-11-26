#  Project SQL Data Analysis

  
**Project: Project 3 — SQL Data Analysis

## Objective
Use SQL queries to extract actionable insights from an order dataset.

The project demonstrates:
- `SELECT`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `HAVING`
- `COUNT()`
- `SUM()`
- `AVG()`

## Dataset
The dataset contains order-level e-commerce information such as:
Order ID, date, customer, product, quantity, unit price, order status,
payment method, coupon code, referral source and total price.

## Files
- `dataset.csv` — project dataset
- `decodeLabs_project3.db` — ready-to-run SQLite database
- `schema.sql` — table definition
- `analysis.sql` — SQL analysis queries
- `query_results.md` — key results/insights

## How to run
### Option 1 — DB Browser for SQLite
1. Open `decodeLabs_project3.db`.
2. Open the **Execute SQL** tab.
3. Copy queries from `analysis.sql`.
4. Run them and show the result grid.

### Option 2 — SQLite command line
```sql
.open decodeLabs_project3.db
.read analysis.sql
```

## Key business questions
1. How many orders are present?
2. What is the total revenue?
3. What is the average order value?
4. Which orders have a value above ₹2,000?
5. Which order status occurs most often?
6. Which product generates the highest revenue?
7. Which payment method contributes the most revenue?
8. Which referral source performs best?
9. Which coupon code generates the most revenue?
10. What are the monthly revenue trends?
11. Which customers have the highest total spend?
12. Which products have revenue above ₹100,000?

## Portfolio outcome
This project demonstrates practical SQL querying, filtering, aggregation,
grouping and business-oriented data interpretation as part of the DecodeLabs internship.
