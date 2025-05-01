select p.product_name, sum(o.unit) as unit 
from orders o 
join 
products p 
on p.product_id = o.product_id
where month(o.order_date) = 2 and year(o.order_date) = 2020
group by o.product_id 
having sum(o.unit) >=100;