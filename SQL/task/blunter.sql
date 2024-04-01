/*
Enter your query here.
*/
select ceil(avg(salary) - avg(cast(replace(salary,'0','')as decimal) ))
from employees;