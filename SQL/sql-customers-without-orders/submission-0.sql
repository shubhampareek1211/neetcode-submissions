-- Write your query below
select name
from(
select c.id, c.name, o.id, o.customer_id
from customers c 
left join orders o 
on c.id = o.customer_id 
) as t 
where customer_id IS NULL