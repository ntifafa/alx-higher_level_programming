-- Creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
-- Second_table description: id INT, name VARCHAR(256), score INT
-- The database name will be passed as an argument to the mysql command
-- If the table second_table already exists, your script should not fail
-- You are not allowed to use the SELECT and SHOW statements
-- Your script should create these records:
--      id = 1, name = “John”, score = 10
--      id = 2, name = “Alex”, score = 3
--      id = 3, name = “Bob”, score = 14
--      id = 4, name = “George”, score = 8

SELECT score, name FROM second_table ORDER BY score DESC;
