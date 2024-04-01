SELECT CONCAT(MAX(months * salary), ' ', COUNT(*))
FROM employee
WHERE months * salary = (
    SELECT MAX(months * salary)
    FROM employee
);
