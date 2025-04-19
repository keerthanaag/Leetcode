# Write your MySQL query statement below
select distinct b.employee_id, 
case 
when b.counts > 1 then (select department_id from employee where primary_flag ='Y' and employee_id = b.employee_id)
else (select department_id from employee where employee_id = b.employee_id)
end as department_id 
from employee a
join 
(select employee_id , count(employee_id) as counts from employee group by employee_id) as b
on a.employee_id = b.employee_id;