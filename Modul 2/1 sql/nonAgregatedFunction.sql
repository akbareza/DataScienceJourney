USE sakila;

-- Window

-- 1. Over Partition
-- must after agegated/non-agregat function
-- make an agregat function from specific coloumn without grouped the value.
-- AVG field OVER() -> agregat entire one field
-- AVG field OVER(PARTITION BY  another field) -> AGREAGTED based on another field.

-- 2. ROW_NUMBER()
-- make numbering for each row. Could be combined with OVER(PARTITION BY _).

-- 3. RANK() and DENSE_RANK()
-- RANK() OVER(ORDER BY __ DESC/ASC

-- 4. NTILE() dividing based on coloumn value
-- NTILE(2) OVER(PARTITION BY field) --> grouped by value

-- NTILE(2) OVER(ORDER BY field) --> all row

-- 5 moving window

USE sakila;

WITH
rentalDurationMean AS (
SELECT AVG(rental_duration) FROM film)

SELECT a.*,
SUM(total_rental_duration) OVER (ORDER BY total_rental_duration DESC
								ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_sum,
ROUND(AVG(total_rental_duration) OVER (ORDER BY total_rental_duration DESC
								ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),2) AS moving_avg
FROM(
SELECT c. name, SUM(f.rental_duration) as total_rental_duration

FROM category c
LEFT JOIN film_category fc
on
c.category_id = fc.category_id
LEFT JOIN film f
on
fc.film_id = f.film_id
WHERE rental_duration <= (select * From rentalDurationMean)
GROUP BY c.name
ORDER BY SUM(f.rental_duration) desc
LIMIT 5) a



