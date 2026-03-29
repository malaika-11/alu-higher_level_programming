-- Count records per score in second_table.
-- Show score and number of rows for each score ordered by count desc.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
