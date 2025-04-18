# Write your MySQL query statement below 
SELECT 
    e.employee_id,
    e.name,
    tb1.reports_count,
    tb1.average_age
FROM 
    employees e
JOIN (
    SELECT 
        reports_to AS employee_id,
        COUNT(employee_id) AS reports_count,
        round(avg(age))as average_age
    FROM 
        employees
    WHERE 
        reports_to IS NOT NULL
    GROUP BY 
        reports_to
) AS tb1
ON 
    tb1.employee_id = e.employee_id
order by e.employee_id;
