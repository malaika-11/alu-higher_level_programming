-- List all cities of California using a subquery.
-- Show city id and name for California sorted by city id.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
