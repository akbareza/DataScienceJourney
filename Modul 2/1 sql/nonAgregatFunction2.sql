-- number 2
USE Sakila;
SELECT f.* FROM FILM f;

WITH
bestCat AS (SELECT f. category_id, SUM(f.film_id) totalFilm
FROM film_category f
GROUP BY f.category_id
ORDER BY 2 DESC
LIMIT 3)

SELECT f.rating, AVG(f.rental_duration) AS avg_rental_duration-- , fc.category_id, bc.totalFilm
-- SELECT f.rating, f.rental_duration , fc.category_id, bc.totalFilm
FROM film f
LEFT JOIN film_category fc
on
f.film_id = fc.film_id
INNER JOIN (SELECT * FROM bestCat) bc
on
fc.category_id = bc.category_id
GROUP BY f.rating
ORDER BY 2 DESC;



-- number 3