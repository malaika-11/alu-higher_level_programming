-- Create database hbtn_0d_usa and table cities with foreign key.
-- Create database hbtn_0d_usa if missing.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database hbtn_0d_usa.
USE hbtn_0d_usa;
-- Create cities table if missing.
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
