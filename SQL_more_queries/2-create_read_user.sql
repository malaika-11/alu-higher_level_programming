-- Create database hbtn_0d_2 and user_0d_2 with read privilege only.
-- Create database hbtn_0d_2 if missing.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user_0d_2 if missing.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
