-- Create table unique_id with unique default id value.
-- Create unique_id table if missing.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
