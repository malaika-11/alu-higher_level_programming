-- Create table id_not_null with default id value.
-- Create id_not_null table if missing.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
