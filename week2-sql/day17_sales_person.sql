-- Problem: Sales Person
-- Pattern: Multi-table anti-join (NOT IN + NULL trap awareness)
-- Solved: 2026-07-22

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id FROM Orders o
    INNER JOIN Company c ON c.com_id = o.com_id
    WHERE c.name = 'RED'
);
