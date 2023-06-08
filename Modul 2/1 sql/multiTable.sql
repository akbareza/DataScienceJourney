USE employees;

-- subqueries to combine data from 2 tables, couldn't show the second or third table. just gathering the data only.
select * from employees
WHERE emp_no in (SELECT emp_no FROM titles WHERE title = 'Senior Engineer')
and
emp_no in (SELECT emp_no FROM salaries WHERE salary > 70000);


-- implicit join, Proses lebih lama karena 'mungkin' di-joinkan dengan keseluruhan table.
SELECT E.first_name, E.last_name, T.title, S.Salary
FROM employees E, Titles T, Salaries S
where (E.emp_no = T.emp_no) AND (E.emp_no = S.emp_no) and T.title = 'Senior Engineer'
order by S.Salary;