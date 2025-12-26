We have two tables fund_investment and participant, please write a query and get the result as you seen in output table:
 
Table-fund_investment
 
+--------------------------------------------------+
 
| Fundid | Allocation type | Allocation Percentage |
 
|--------|-----------------|-----------------------|
 
| 2342   | BOND            | 0.2
 
| 2342   | CASH            | 0.7                   |
 
| 2342   | CTSK            | 0.1                   |
 
+--------------------------------------------------+
 
Table-participant
 
+------------------------------+
 
| Part_id  | Fundid | Balanace |
 
|----------|--------|----------|
 
| 34546778 | 2342   | 5000     |
 
| 11254678 | 2342   | 50000    |
 
+------------------------------+
 Table-output
 
+---------------------------------------------------------------------------+
 
| Part_id  | Fundid | Balance | Bond Balance | Cash Balance | Stock Balance |
 
|----------|--------|---------|--------------|--------------|---------------|
 
| 34546778 | 2342   | 5000    | 1000         | 3500         | 500           |
 
| 11254678 | 2342   | 50000   | 10000        | 35000        | 5000          |
 
+---------------------------------------------------------------------------+

with cte as (
	select fund_id, case when allocation_type = 'BOND' then Allocation_percentage else 0 end as bond_allocation_percentage,
	case when allocation_type = 'CASH' then Allocation_percentage else 0 end as cash_allocation_percentage,
	case when allocation_type = 'CSTK' then Allocation_percentage else 0 end as stock_allocation_percentage
	from fund_investment
)


select part_id, p.fund_id, balance, balance*bond_allocation_percentage as Bond_balance,
balance*cash_allocation_percentage as cash_balance,
balance*stock_allocation_percentage as stock_balance
from participant p left join cte f on p.fund_id = f.fund_id
