-- Create table force_name with a NOT NULL name column.
-- Create force_name table if missing.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
