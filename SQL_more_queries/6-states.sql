-- Create database hbtn_0d_usa and table states.
-- Create database hbtn_0d_usa if missing.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database hbtn_0d_usa.
USE hbtn_0d_usa;
-- Create states table if missing.
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
