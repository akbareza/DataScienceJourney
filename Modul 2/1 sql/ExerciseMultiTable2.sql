USE SAKILA;
SELECT COUNT(*) FROM
( SELECT DISTINCT actor_id from actor
	where last_name is not null
) a;

SELECT concat(first_name, ' ',last_name) as NamaLengkap
FROM ACTOR a
LEFT JOIN film_actor fa
on a.actor_id = fa.actor_id
LEFT JOIN film f
on fa.film_id = f.film_id
WHERE title = 'Alone Trip'
ORDER BY concat(first_name, ' ',last_name) ASC
LIMIT 10;

USE WORLD;
SELECT DISTINCT LANGUAGE, c.name FROM countrylanguage cl
LEFT JOIN country c
on c.code = cl.countryCode
WHERE c.name = 'Indonesia';

SELECT DISTINCT c.name AS namaNegara, ci.name AS ibuKota
FROM country c
LEFT JOIN CITY ci
on c.capital = ci.id
WHERE c.name IN ('Indonesia', 'Italy', 'Spain');

-- namalengk, tgl lahir, jumlah penghasilan selama bekerja di kantor, divisi
-- 10 orang total penghasilan terbanyaka
USE employees;
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT * FROM departments;



WITH total_sal AS(
SELECT emp_no, SUM(salary) as total_salary
FROM salaries
GROUP BY emp_no
-- ORDER BY total_salary desc
)
SELECT e.EMP_NO, concat(first_name,' ', last_name) AS full_name, birth_date, dept_name,
total_salary
FROM employees e	

LEFT JOIN dept_emp de
on
e.emp_no = de.emp_no

LEFT JOIN total_sal ts
on
e.emp_no = ts.emp_no

LEFT JOIN departments d
on
de.dept_no = d.dept_no

ORDER by total_salary desc
LIMIT 10;

SELECT s.emp_no, first_name, SUM(s.salary) as total_salary
FROM salaries s

INNER JOIN employees e
on
s.emp_no = e.emp_no

GROUP BY s.emp_no
ORDER BY total_salary desc
LIMIT 10;

USE employees;
SELECT emp_no, count(dept_no)
FROM dept_emp
GROUP BY emp_no;
-- WHERE EMP_NO  IN (109334)

select * FROM dept_emp;

