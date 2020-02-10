

--Questions using the NOT operator
--We can pull all of the rows that  were excluded from the queries in the previous two concepts with our new operator.
    --1. Use the accounts table to find the account name, primary poc, and sales rep id for all stores except 
    --Walmart, Target, and Nordstrom.
    SELECT name, primary_poc, sales_rep_id
    FROM accounts
    WHERE name NOT IN ('Walmart', 'Target', 'Nordstrom');

    --2. Use the web_events table to find all information regarding individuals who were contacted via any 
    --method except using organic or adwords methods.
    SELECT *
    FROM web_events
    WHERE channel NOT IN ('organic', 'adwords');

--Use the accounts table to find:
    --1. All the companies whose names do not start with 'C'.
    SELECT name
    FROM accounts
    WHERE name NOT LIKE 'C%';

    --2. All companies whose names do not contain the string 'one' somewhere in the name.
    SELECT name
    FROM accounts
    WHERE name NOT LIKE '%one%';

    --3. All companies whose names do not end with 's'.
    SELECT name
    FROM accounts
    WHERE name NOT LIKE '%s';

--Quiz: IN
--Questions using IN operator
--Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name IN ('Walmart', 'Target', 'Nordstrom');

--Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords.
SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords')


--Quiz: LIKE
--Questions using the LIKE operator

--Use the accounts table to find
--1. All the companies whose names start with 'C'.
SELECT name
FROM accounts
WHERE name LIKE 'C%';

--2. All companies whose names contain the string 'one' somewhere in the name.
SELECT name
FROM accounts
WHERE name LIKE '%one%';

--3. All companies whose names end with 's'.
SELECT name
FROM accounts
WHERE name LIKE '%s';

--Quiz: Arithmetic Operators
--Questions using Arithmetic Operations

--Using the orders table:
--1. Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for 
--standard paper for each order. Limit the results to the first 10 orders, and include the id and account_id fields.
SELECT id, account_id, standard_amt_usd/standard_qty AS unit_price_std_paper
FROM orders
LIMIT 10;

--2. Write a query that finds the percentage of revenue that comes from poster paper for each order. You will need to use 
--only the columns that end with _usd. (Try to do this without using the total column.) Display the id and account_id fields also. 
--NOTE - you will receive an error with the correct solution to this question. This occurs because at least one of the values in 
--the data creates a division by zero in your formula. You will learn later in the course how to fully handle this issue. For now, 
--you can just limit your calculations to the first 10 orders, as we did in question #1, and you'll avoid that set of 
--data that causes the problem.
SELECT id, account_id, (poster_amt_usd/total_amt_usd)*100 AS revenue_only_poster
FROM orders
LIMIT 10;

--Notice, the above operators combine information across columns for the same row. If you want to combine values of a 
--particular column, across multiple rows, we will do this with aggregations. We will get to that before the end of the course!

--Quiz: WHERE
--Write a query that:
--1. Pulls the first 5 rows and all columns from the orders table that have a dollar amount of 
--gloss_amt_usd greater than or equal to 1000.
SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5;

--2. Pulls the first 10 rows and all columns from the orders table that have a total_amt_usd less than 500.
SELECT *
FROM orders
WHERE total_amt_usd < 500
LIMIT 10;

--You will notice when using these WHERE statements, we do not need to ORDER BY 
--unless we want to actually order our data. Our condition will work without having to do any sorting of the data.

--Practice Question Using WHERE with Non-Numeric Data
--Filter the accounts table to include the company name, website, and the primary 
--point of contact (primary_poc) just for the Exxon Mobil company in the accounts table.
SELECT name, website, primary_poc
FROM accounts
WHERE name = 'Exxon Mobil';

--ORDER BY Part II
--1. Write a query that displays the order ID, account ID, and total dollar amount for all the orders, 
--sorted first by the account ID (in ascending order), and then by the total dollar amount (in descending order).
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY account_id ASC, total_amt_usd DESC;

--2. Now write a query that again displays order ID, account ID, and total dollar amount for each order, 
--but this time sorted first by total dollar amount (in descending order), and then by account ID (in ascending order).
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC, account_id ASC;

--3. Compare the results of these two queries above. How are the results different when you 
--switch the column you sort on first?
    -- ANSWER: Listing by account_id its possible to group because there are multiple of the same, grouping by 
    --         total_amt_usd the numbers are very specific so no way you can have a pattern and group by it

-- ORDER BY
--1. Write a query to return the 10 earliest orders in the orders table. 
--Include the id, occurred_at, and total_amt_usd.
SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at
LIMIT 10;

--2. Write a query to return the top 5 orders in terms of largest total_amt_usd. 
--Include the id, account_id, and total_amt_usd.
SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC
LIMIT 5;

--3. Write a query to return the lowest 20 orders in terms of smallest total_amt_usd. 
--Include the id, account_id, and total_amt_usd.
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd
LIMIT 20;

--Can You Use LIMIT?
--Try using LIMIT yourself below by writing a query that displays all the data in the occurred_at, account_id, 
--and channel columns of the web_events table, and limits the output to only the first 15 rows.
SELECT occurred_at, account_id, channel
 FROM web_events
LIMIT 15;

