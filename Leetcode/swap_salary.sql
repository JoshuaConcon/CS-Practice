# Use CASE as an IF statement to swap the values
UPDATE salary
SET sex = CASE WHEN sex = 'm' THEN 'f'
               WHEN sex = 'f' THEN 'm' END
WHERE sex IN ('m','f');
