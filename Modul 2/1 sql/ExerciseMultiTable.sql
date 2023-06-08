USE Sakila;
SELECT * FROM film f, language l;
SELECT f.title, f.length, f.language_id, l.name
FROM film f, language l
WHERE title LIKE '%k' and f.language_id = l.language_id;

SELECT * FROM film;
SELECT f.title, a.first_name, a.last_name
FROM film f, film_actor fa, actor a
WHERE f.film_id = fa.film_id AND fa.actor_id = 14 AND fa.actor_id = a.actor_id;

-- 1
SELECT f.title, c.name, f.length
FROM film f
LEFT JOIN film_category fc
on f.film_id = fc.film_id
LEFT JOIN category c
on fc.category_id = c.category_id
WHERE c.name = 'Comedy'
ORDER BY f.length
LIMIT 10;

-- 2
SELECT c.name AS kategori, COUNT(fc.film_id) AS jumlahMovie, AVG(rental_rate) AS rataHargaSewa
FROM CATEGORY c
LEFT JOIN film_category fc
on
c.category_id = fc.category_id
LEFT JOIN FILM f
on
fc.film_id = f.film_id
GROUP BY c.name
ORDER BY COUNT(fc.film_id) DESC;

-- 3
SELECT a.actor_id, a.first_name, a.last_name, count(fa.film_id) as jumlah_movie
FROM ACTOR a
LEFT JOIN film_actor fa
on
a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY count(fa.film_id) DESC
LIMIT 10;

-- 4
SELECT c.name AS kategori, COUNT(fa.film_id) AS jumlahMovie
FROM CATEGORY c
LEFT JOIN film_category fc
on
c.category_id = fc.category_id
LEFT JOIN film_actor fa
on
fc.film_id = fa.film_id
WHERE actor_id = (SELECT actor_id FROM (
SELECT a.actor_id, a.first_name, a.last_name, count(fa.film_id) as jumlah_movie
FROM ACTOR a
LEFT JOIN film_actor fa
on
a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY count(fa.film_id) DESC
LIMIT 1) x)
GROUP BY c.name;


-- 5
SELECT f.title, c.name
FROM CATEGORY c
LEFT JOIN film_category fc
on
c.category_id = fc.category_id
LEFT JOIN film_actor fa
on
fc.film_id = fa.film_id
LEFT JOIN FILM f
on
fc.film_id = f.film_id
WHERE
fa.actor_id = (SELECT actor_id FROM (
SELECT a.actor_id, a.first_name, a.last_name, count(fa.film_id) as jumlah_movie
FROM ACTOR a
LEFT JOIN film_actor fa
on
a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY count(fa.film_id) DESC
LIMIT 1) x)
AND c.name = (SELECT kategori FROM (
SELECT c.name AS kategori, COUNT(fa.film_id) AS jumlahMovie
FROM CATEGORY c
LEFT JOIN film_category fc
on
c.category_id = fc.category_id
LEFT JOIN film_actor fa
on
fc.film_id = fa.film_id
WHERE actor_id = (SELECT actor_id FROM (
SELECT a.actor_id, a.first_name, a.last_name, count(fa.film_id) as jumlah_movie
FROM ACTOR a
LEFT JOIN film_actor fa
on
a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY count(fa.film_id) DESC
LIMIT 1) x)
GROUP BY c.name
ORDER BY count(fa.film_id) DESC
LIMIT 1)y);



