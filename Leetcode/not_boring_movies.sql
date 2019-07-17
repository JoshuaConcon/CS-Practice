SELECT *
FROM cinema
WHERE id % 2 = 1 AND description <> "boring"
GROUP BY rating DESC
