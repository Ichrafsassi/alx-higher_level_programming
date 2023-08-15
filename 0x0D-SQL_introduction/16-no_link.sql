--  score average of all records as "average"

SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC
