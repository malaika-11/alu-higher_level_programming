-- List records from second_table with non-null and non-empty names.
-- Show score and name ordered by score descending.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
