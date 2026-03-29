-- List all cities with their state name.
-- Show cities.id, cities.name, states.name sorted by cities.id.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
