-- Problem: Product Sales Analysis I
-- Pattern: Basic JOIN
-- Solved: 2026-07-22

SELECT p.product_name, s.year, s.price
FROM Product p
INNER JOIN Sales s ON p.product_id = s.product_id;
