-- nomor 3
USE sakila;
SELECT	rental_duration AS Durasi_Rental, COUNT(*) AS Banyak_Film, ROUND(AVG(LENGTH),2)
FROM film
GROUP BY rental_duration
ORDER BY rental_duration;

-- nomor 4
SELECT TITLE, LENGTH, RATING FROM FILM
WHERE LENGTH > (SELECT AVG(LENGTH) as lengthAverage FROM FILM)
GROUP BY TITLE, LENGTH, RATING
ORDER BY LENGTH DESC
LIMIT 25;

-- nomor 5
SELECT rating,max(replacement_cost), min(rental_rate), AVG(length)
FROM film
GROUP BY rating;

-- nomor 8
SELECT city, country_id
FROM city
WHERE city LIKE '%d%a'
LIMIT 15;

-- nomor 10
SELECT title, description, length, rating
FROM film
WHERE length > (SELECT AVG(LENGTH) FROM FILM) AND title LIKE '%h'
LIMIT 10;

-- Exercise from Achmad
USE world;

-- 1. 5 Departemen mana yang memiliki gaji yang paling besar?
SELECT * FROM country;

SELECT name, concat(round((population/1000000),2),' juta') AS 'population (mio)'
FROM country
ORDER BY population DESC
LIMIT 10;

SELECT continent, AVG(GNP/population)
FROM country
GROUP BY continent;

SELECT Name, SurfaceArea FROM country
WHERE continent LIKE '%America%'
ORDER BY SurfaceArea DESC;

