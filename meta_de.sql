-- copies, checkouts, members
--copies: copy_id(PK), book_id, reserved_by_member_id(FK), condition
--checkouts: copy_id(FK), due_date, checkout_date, returned_date
--members: member_id(PK), invited_by_member_id

--1. Get the count of book copies that are in good condition and yet to be returned. 
--Of the book copies above, get the percentage of book copies that are past due.
-- expected: num_of_book_copies_in_good_condition (INT), pct_past_due (FLOAT)
select sum(case when condition='good' and returned_date is null then 1 else 0 end) num_of_book_copies_in_good_condition,
((sum(case when condition='good' and returned_date is null and past_due is not null then 1 else 0 end)*100.00)/sum(case when condition='good' and returned_date is null then 1 else 0 end)) pct_past_due
from copies c join checkouts ch on c.copy_id=ch.copy_id

--2. calculate the total lifetime value of all copies of a book and display the top 3 rows with the highest LTV. the book should have atleast 10 copies
select book_id, lifetime_value
from (
select book_id, count(c.copy_id) copy_count, sum(abs(returned_date-checkout_date)) lifetime_value
from copies c left join checkouts ch on c.copy_id=ch.copy_id
where returned_date is not null
group by 1) t
where copy_count > 10
order by 2 desc
limit 3

--3. calculate the largest differnce between the number of book copies reserved by a member and the member who invited them
select member_id, invited_by_member_id, sum(abs(count(c.copy_id) - count(c2.copy_id))) difference_in_books_reserved
from members m left join copies c on m.member_id = c.reserved_by_member_id
left join copies c2 on m.member_id = c2.reserved_by_member_id
group by 1,2
order by 3 desc
limit 1