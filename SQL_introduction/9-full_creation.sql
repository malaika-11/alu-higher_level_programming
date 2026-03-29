-- Create second_table and add required rows.
-- Create second_table if it does not exist.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Insert the row for John.
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
-- Insert the row for Alex.
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
-- Insert the row for Bob.
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
-- Insert the row for George.
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
