-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server

-- Database creation 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Database usage
USE hbtn_0d_usa;

-- Table creation
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
