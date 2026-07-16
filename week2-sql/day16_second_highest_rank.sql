-- Day 16 (July 16) — Post-finals restart
-- Topics: Second Highest Salary, DENSE_RANK, Level 1 practice

-- =============================================
-- PROBLEM 1: Second Highest Salary
-- =============================================
-- Return second highest distinct salary. NULL if doesn't exist.

-- Step 1: Basic approach (empty if only 1 salary)
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Step 2: Handles NULL case (correct answer)
SELECT (
  SELECT DISTINCT salary
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

-- =============================================
-- PROBLEM 2: Rank Scores (window functions)
-- =============================================
-- DENSE_RANK = no gaps (1,1,2)
-- RANK = gaps (1,1,3)

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;

-- =============================================
-- LEVEL 1 PRACTICE (using sample_data.sql)
-- =============================================

-- #1: Employees hired after 2023-01-01
SELECT id, name, department_id, salary, hire_date
FROM employees
WHERE hire_date > '2023-01-01';

-- #2: Products under $20
SELECT id, name, category, price
FROM products
WHERE price < 20;

-- #3: Engineering dept sorted by salary desc
SELECT name, salary
FROM employees
WHERE department_id = 1
ORDER BY salary DESC;
