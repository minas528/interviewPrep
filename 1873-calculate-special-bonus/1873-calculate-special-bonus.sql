# Write your MySQL query statement below
select employee_id,
case when employee_id%2=0 or Left(name,1)="M" Then 0
else salary
end as bonus
from Employees  ;