/* Given transactions table with transaction_time and transaction_amount for January 2021, write SQL query to display the rolling 3 day average transaction amount for each day in January 2021 */

with daily_transactiosn as (
    select date(transaction_time) transaction_date, sum(transaction_amount) as amount
    from transactions
    group by 1
    ),
with lag_transactions as (
    select transaction_date, amount, coalesce(lag(amount, 1) over (order by transaction_date), 0) as amount_lag_1,
    coalesce(lag(amount, 2) over (order by transaction_date), 0) as amount_lag_2
    from daily_transactions
    )
select transaction_date, round(cast((amount+amount_lag_1+amount_lag_2)/3 as numeric), 2) as rolling_3_day_average
from lag_transactions

/* 
select transaction_date, cast((amount+amount_lag_1+amount_lag_2)/3 as numeric(10,2)) as rolling_3_day_average
from lag_transactions
*/
/* Rolling 30 day average transaction amount per customer */
SELECT
  customer_id,
  transaction_date,
  transaction_amount,
  AVG(transaction_amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_date
    RANGE BETWEEN INTERVAL '30' DAY PRECEDING AND CURRENT ROW
  ) AS rolling_30_day_avg
FROM
  your_transactions_table
ORDER BY
  customer_id,
  transaction_date;