-- Creates the MySQL server user user_0d_1
-- and assigns password and grants all privileges to it
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
