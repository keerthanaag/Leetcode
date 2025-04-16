# Write your MySQL query statement below
select max(num) as num from (select num,count(num) as counts from MyNumbers group by num) as tb1 where tb1.counts = 1; 