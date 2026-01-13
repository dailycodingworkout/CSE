# 📚 Chapter 04: Structured Query Language (SQL)

> **The Atomic Truth**: *Declarative language to query and manipulate relational databases.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 4-6 marks |
| Frequency | Every year |
| Type | MCQ (output prediction), NAT (count rows) |
| Difficulty | Easy to Medium |
| Hot Topics | NULL handling, GROUP BY/HAVING, Nested queries, Joins |

---

## 1. SQL Overview

### What is SQL?
**SQL (Structured Query Language)** is the standard language for relational database management systems.

### SQL Sublanguages

| Category | Commands | Purpose |
|----------|----------|---------|
| **DDL** (Data Definition) | CREATE, ALTER, DROP, TRUNCATE | Define structure |
| **DML** (Data Manipulation) | SELECT, INSERT, UPDATE, DELETE | Manipulate data |
| **DCL** (Data Control) | GRANT, REVOKE | Control access |
| **TCL** (Transaction Control) | COMMIT, ROLLBACK, SAVEPOINT | Manage transactions |

### SQL vs Relational Algebra

| Aspect | Relational Algebra | SQL |
|--------|-------------------|-----|
| Type | Procedural | Declarative |
| Duplicates | Always eliminates | Keeps by default |
| NULL | Not supported | Supported |
| Aggregation | Extended RA only | Built-in |

---

## 2. DDL - Data Definition Language

### CREATE TABLE

```sql
CREATE TABLE Student (
    roll_no     INT             PRIMARY KEY,
    name        VARCHAR(100)    NOT NULL,
    age         INT             CHECK (age > 0 AND age < 150),
    email       VARCHAR(255)    UNIQUE,
    dept_id     INT,
    created_at  TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

### Data Types

| Category | Types | Example |
|----------|-------|---------|
| **Numeric** | INT, BIGINT, DECIMAL(p,s), FLOAT | DECIMAL(10,2) for money |
| **String** | CHAR(n), VARCHAR(n), TEXT | VARCHAR(100) for names |
| **Date/Time** | DATE, TIME, DATETIME, TIMESTAMP | DATE for birthdate |
| **Binary** | BLOB, BINARY | BLOB for images |
| **Boolean** | BOOLEAN, BIT | BOOLEAN for flags |

### CHAR vs VARCHAR

| CHAR(n) | VARCHAR(n) |
|---------|------------|
| Fixed-length | Variable-length |
| Pads with spaces | No padding |
| Faster for fixed data | Saves space for variable data |
| 'AB' = 'AB  ' (sometimes) | 'AB' ≠ 'AB  ' |

### ALTER TABLE

```sql
-- Add column
ALTER TABLE Student ADD phone VARCHAR(15);

-- Drop column
ALTER TABLE Student DROP COLUMN phone;

-- Modify column
ALTER TABLE Student MODIFY name VARCHAR(200);

-- Add constraint
ALTER TABLE Student ADD CONSTRAINT chk_age CHECK (age >= 18);

-- Drop constraint
ALTER TABLE Student DROP CONSTRAINT chk_age;

-- Rename table
ALTER TABLE Student RENAME TO Pupils;
```

### DROP vs TRUNCATE vs DELETE

| Operation | Removes | Rollback | Speed | Resets Auto-Increment | WHERE Clause |
|-----------|---------|----------|-------|----------------------|--------------|
| DROP | Table + Data | No | Fast | Yes | No |
| TRUNCATE | All Data | No* | Fast | Yes | No |
| DELETE | Specific Rows | Yes | Slow | No | Yes |

*Some RDBMS allow TRUNCATE rollback within transaction

---

## 3. DML - Data Manipulation Language

### INSERT

```sql
-- Insert single row
INSERT INTO Student (roll_no, name, age) 
VALUES (101, 'Alice', 20);

-- Insert multiple rows
INSERT INTO Student (roll_no, name, age) VALUES
    (102, 'Bob', 21),
    (103, 'Charlie', 22),
    (104, 'David', 23);

-- Insert from SELECT
INSERT INTO Archive_Student 
SELECT * FROM Student WHERE graduated = true;
```

### UPDATE

```sql
-- Update specific rows
UPDATE Student 
SET age = age + 1 
WHERE dept_id = 1;

-- Update with subquery
UPDATE Student 
SET dept_id = (SELECT dept_id FROM Department WHERE name = 'CS')
WHERE roll_no = 101;

-- Update multiple columns
UPDATE Student 
SET name = 'Alice Smith', age = 21 
WHERE roll_no = 101;
```

### DELETE

```sql
-- Delete specific rows
DELETE FROM Student WHERE age < 18;

-- Delete all rows (use TRUNCATE instead for performance)
DELETE FROM Student;

-- Delete with subquery
DELETE FROM Student 
WHERE dept_id IN (SELECT dept_id FROM Department WHERE name = 'Obsolete');
```

---

## 4. SELECT - The Core Query

### Basic Syntax

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE condition]
[GROUP BY column_list]
[HAVING condition]
[ORDER BY column_list [ASC|DESC]]
[LIMIT n [OFFSET m]];
```

### Execution Order (CRITICAL for GATE!)

```
FROM        → 1. Determine source tables
WHERE       → 2. Filter rows (before grouping)
GROUP BY    → 3. Group rows
HAVING      → 4. Filter groups
SELECT      → 5. Compute select list
DISTINCT    → 6. Remove duplicates
ORDER BY    → 7. Sort results
LIMIT       → 8. Limit output rows
```

### GATE Trap Alert! 🚨
**Execution order ≠ Written order!**

You CANNOT use column alias from SELECT in WHERE because WHERE executes before SELECT.

```sql
-- WRONG
SELECT salary * 12 AS annual FROM Employee WHERE annual > 100000;

-- CORRECT
SELECT salary * 12 AS annual FROM Employee WHERE salary * 12 > 100000;
```

### SELECT Clause Features

```sql
-- Select all columns
SELECT * FROM Student;

-- Select specific columns
SELECT name, age FROM Student;

-- Column alias
SELECT name AS student_name, age AS student_age FROM Student;

-- Computed columns
SELECT name, salary, salary * 12 AS annual_salary FROM Employee;

-- DISTINCT
SELECT DISTINCT dept_id FROM Employee;

-- ALL (default, keeps duplicates)
SELECT ALL dept_id FROM Employee;
```

---

## 5. WHERE Clause & Operators

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| = | Equal | `age = 20` |
| <> or != | Not equal | `age <> 20` |
| < | Less than | `age < 20` |
| > | Greater than | `age > 20` |
| <= | Less than or equal | `age <= 20` |
| >= | Greater than or equal | `age >= 20` |

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| AND | Both true | `age > 18 AND dept = 'CS'` |
| OR | Either true | `age < 18 OR age > 60` |
| NOT | Negation | `NOT (age < 18)` |

### Precedence: NOT > AND > OR

```sql
-- These are different!
WHERE A OR B AND C    -- Same as: A OR (B AND C)
WHERE (A OR B) AND C  -- Different!
```

### Special Operators

```sql
-- BETWEEN (inclusive)
SELECT * FROM Student WHERE age BETWEEN 18 AND 25;
-- Same as: age >= 18 AND age <= 25

-- IN
SELECT * FROM Student WHERE dept IN ('CS', 'IT', 'ECE');
-- Same as: dept = 'CS' OR dept = 'IT' OR dept = 'ECE'

-- LIKE (pattern matching)
SELECT * FROM Student WHERE name LIKE 'A%';     -- Starts with A
SELECT * FROM Student WHERE name LIKE '%son';   -- Ends with son
SELECT * FROM Student WHERE name LIKE '_a%';    -- Second char is 'a'
SELECT * FROM Student WHERE name LIKE '%[aeiou]%'; -- Contains vowel

-- Pattern characters:
-- % = Any sequence of characters (including empty)
-- _ = Exactly one character
-- [] = Character class (SQL Server)
-- ESCAPE for literal % or _

-- IS NULL (NOT = NULL!)
SELECT * FROM Student WHERE phone IS NULL;
SELECT * FROM Student WHERE phone IS NOT NULL;
```

### GATE Trap Alert! 🚨
**NULL comparisons with = always return UNKNOWN!**

```sql
-- WRONG: Returns no rows even if phone is NULL
SELECT * FROM Student WHERE phone = NULL;

-- CORRECT:
SELECT * FROM Student WHERE phone IS NULL;
```

---

## 6. NULL Handling (GATE Favorite!)

### Three-Valued Logic

SQL uses **three-valued logic**: TRUE, FALSE, UNKNOWN

| A | B | A AND B | A OR B | NOT A |
|---|---|---------|--------|-------|
| T | T | T | T | F |
| T | F | F | T | F |
| T | U | U | T | F |
| F | T | F | T | T |
| F | F | F | F | T |
| F | U | F | U | T |
| U | T | U | T | U |
| U | F | F | U | U |
| U | U | U | U | U |

### NULL Comparison Rules

| Expression | Result |
|------------|--------|
| NULL = NULL | UNKNOWN |
| NULL <> NULL | UNKNOWN |
| NULL > 5 | UNKNOWN |
| 5 = NULL | UNKNOWN |
| NULL IS NULL | TRUE |
| NULL IS NOT NULL | FALSE |

### NULL in Aggregate Functions

| Function | Behavior with NULL |
|----------|-------------------|
| COUNT(*) | Counts all rows including NULL |
| COUNT(column) | Ignores NULL values |
| SUM, AVG | Ignores NULL values |
| MIN, MAX | Ignores NULL values |

### GATE Example: NULL Counting

```sql
Table: Employee
| id | name  | salary |
|----|-------|--------|
| 1  | Alice | 50000  |
| 2  | Bob   | NULL   |
| 3  | Carol | 60000  |
| 4  | David | NULL   |

SELECT COUNT(*) FROM Employee;         -- Result: 4
SELECT COUNT(salary) FROM Employee;    -- Result: 2
SELECT AVG(salary) FROM Employee;      -- Result: 55000 (not 27500!)
SELECT SUM(salary) FROM Employee;      -- Result: 110000
```

### COALESCE and IFNULL

```sql
-- Return first non-NULL value
SELECT COALESCE(phone, email, 'No contact') FROM Customer;

-- Replace NULL with default
SELECT IFNULL(salary, 0) FROM Employee;  -- MySQL
SELECT ISNULL(salary, 0) FROM Employee;  -- SQL Server
SELECT NVL(salary, 0) FROM Employee;     -- Oracle
```

---

## 7. Aggregate Functions

### Standard Aggregate Functions

| Function | Purpose | NULL Handling |
|----------|---------|---------------|
| COUNT(*) | Count rows | Includes NULL |
| COUNT(col) | Count non-NULL values | Excludes NULL |
| SUM(col) | Sum of values | Excludes NULL |
| AVG(col) | Average of values | Excludes NULL |
| MIN(col) | Minimum value | Excludes NULL |
| MAX(col) | Maximum value | Excludes NULL |

### COUNT Variations

```sql
-- Count all rows
SELECT COUNT(*) FROM Employee;

-- Count non-NULL values in column
SELECT COUNT(salary) FROM Employee;

-- Count distinct values
SELECT COUNT(DISTINCT dept_id) FROM Employee;
```

### GATE Trap Alert! 🚨
**AVG ignores NULL, doesn't treat as 0!**

```sql
-- If salaries are: 100, NULL, 200
SELECT AVG(salary);  -- Returns 150, not 100!
```

---

## 8. GROUP BY and HAVING

### GROUP BY

Groups rows with same values in specified columns.

```sql
-- Count employees per department
SELECT dept_id, COUNT(*) AS emp_count
FROM Employee
GROUP BY dept_id;

-- Multiple grouping columns
SELECT dept_id, job_title, AVG(salary)
FROM Employee
GROUP BY dept_id, job_title;
```

### GROUP BY Rules

1. **Every non-aggregated column in SELECT must be in GROUP BY**
2. **Aggregates operate on groups, not individual rows**

```sql
-- WRONG: name is not in GROUP BY
SELECT dept_id, name, COUNT(*)
FROM Employee
GROUP BY dept_id;

-- CORRECT:
SELECT dept_id, COUNT(*)
FROM Employee
GROUP BY dept_id;
```

### HAVING vs WHERE

| WHERE | HAVING |
|-------|--------|
| Filters rows BEFORE grouping | Filters groups AFTER grouping |
| Cannot use aggregates | Can use aggregates |
| Works on individual rows | Works on groups |

```sql
-- Find departments with more than 5 employees
-- and only consider employees earning > 30000

SELECT dept_id, COUNT(*) AS emp_count
FROM Employee
WHERE salary > 30000        -- Filter rows first
GROUP BY dept_id
HAVING COUNT(*) > 5;        -- Filter groups after
```

### Execution Order Reminder

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

---

## 9. Joins in SQL

### Types of Joins

```
                    JOIN TYPES
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     INNER           OUTER           CROSS
      JOIN           JOINS            JOIN
        │               │
        │       ┌───────┼───────┐
        │       ▼       ▼       ▼
        │     LEFT    RIGHT    FULL
        │     OUTER   OUTER   OUTER
        │
    ┌───┴───┐
    ▼       ▼
 EQUI    NON-EQUI
 JOIN     JOIN
    │
    ▼
 NATURAL
  JOIN
```

### INNER JOIN

Returns only matching rows from both tables.

```sql
-- Explicit JOIN syntax (preferred)
SELECT E.name, D.dept_name
FROM Employee E
INNER JOIN Department D ON E.dept_id = D.dept_id;

-- Implicit (WHERE) syntax
SELECT E.name, D.dept_name
FROM Employee E, Department D
WHERE E.dept_id = D.dept_id;
```

### LEFT OUTER JOIN

Returns all rows from left table, matched with right table or NULL.

```sql
SELECT E.name, D.dept_name
FROM Employee E
LEFT JOIN Department D ON E.dept_id = D.dept_id;
```

### RIGHT OUTER JOIN

Returns all rows from right table, matched with left table or NULL.

```sql
SELECT E.name, D.dept_name
FROM Employee E
RIGHT JOIN Department D ON E.dept_id = D.dept_id;
```

### FULL OUTER JOIN

Returns all rows from both tables, NULL for non-matches.

```sql
SELECT E.name, D.dept_name
FROM Employee E
FULL OUTER JOIN Department D ON E.dept_id = D.dept_id;
```

### CROSS JOIN (Cartesian Product)

```sql
SELECT E.name, P.product_name
FROM Employee E
CROSS JOIN Product P;

-- Same as:
SELECT E.name, P.product_name
FROM Employee E, Product P;
```

### NATURAL JOIN

Automatically joins on common column names.

```sql
SELECT E.name, D.dept_name
FROM Employee E
NATURAL JOIN Department D;
-- Joins on columns with same name (e.g., dept_id)
```

### Self-Join

```sql
-- Find employees and their managers
SELECT E.name AS employee, M.name AS manager
FROM Employee E
LEFT JOIN Employee M ON E.manager_id = M.emp_id;
```

### Join Output Row Count

| Join Type | Min Rows | Max Rows |
|-----------|----------|----------|
| INNER | 0 | min(m×n, match count) |
| LEFT | \|Left table\| | m×n |
| RIGHT | \|Right table\| | m×n |
| FULL | max(\|L\|, \|R\|) | \|L\| + \|R\| |
| CROSS | m×n | m×n |

---

## 10. Subqueries (Nested Queries)

### Types of Subqueries

| Type | Returns | Example Use |
|------|---------|-------------|
| Scalar | Single value | In SELECT, WHERE with = |
| Row | Single row | With row comparisons |
| Table | Multiple rows/columns | With IN, EXISTS |
| Correlated | Depends on outer query | Row-by-row evaluation |

### Scalar Subquery

```sql
-- Find employees earning above average
SELECT name, salary
FROM Employee
WHERE salary > (SELECT AVG(salary) FROM Employee);

-- Subquery in SELECT
SELECT name, salary, 
       (SELECT AVG(salary) FROM Employee) AS avg_salary
FROM Employee;
```

### IN / NOT IN

```sql
-- Find employees in departments located in 'NYC'
SELECT name
FROM Employee
WHERE dept_id IN (
    SELECT dept_id FROM Department WHERE location = 'NYC'
);
```

### GATE Trap Alert! 🚨
**NOT IN with NULL returns empty!**

```sql
-- If subquery contains NULL, NOT IN returns no rows!
-- Subquery returns: (1, 2, NULL)
SELECT * FROM A WHERE x NOT IN (SELECT y FROM B);
-- Returns empty even if x = 3 exists!

-- Because: 3 NOT IN (1, 2, NULL)
--        = 3 <> 1 AND 3 <> 2 AND 3 <> NULL
--        = TRUE AND TRUE AND UNKNOWN
--        = UNKNOWN (not TRUE, so not returned)

-- Solution: Use NOT EXISTS or filter NULLs
SELECT * FROM A WHERE x NOT IN (SELECT y FROM B WHERE y IS NOT NULL);
```

### EXISTS / NOT EXISTS

```sql
-- Find departments with at least one employee
SELECT dept_name
FROM Department D
WHERE EXISTS (
    SELECT 1 FROM Employee E WHERE E.dept_id = D.dept_id
);

-- Find departments with no employees
SELECT dept_name
FROM Department D
WHERE NOT EXISTS (
    SELECT 1 FROM Employee E WHERE E.dept_id = D.dept_id
);
```

### ALL / ANY / SOME

```sql
-- Find employees earning more than ALL managers
SELECT name FROM Employee
WHERE salary > ALL (SELECT salary FROM Employee WHERE job = 'Manager');

-- Find employees earning more than SOME(ANY) manager
SELECT name FROM Employee
WHERE salary > ANY (SELECT salary FROM Employee WHERE job = 'Manager');
```

### Correlated Subquery

Subquery depends on outer query - evaluated once per outer row.

```sql
-- Find employees earning more than department average
SELECT E1.name, E1.salary
FROM Employee E1
WHERE E1.salary > (
    SELECT AVG(E2.salary)
    FROM Employee E2
    WHERE E2.dept_id = E1.dept_id  -- References outer query
);
```

---

## 11. Set Operations in SQL

### UNION / UNION ALL

```sql
-- Remove duplicates (like ∪ in RA)
SELECT name FROM Student
UNION
SELECT name FROM Teacher;

-- Keep duplicates
SELECT name FROM Student
UNION ALL
SELECT name FROM Teacher;
```

### INTERSECT

```sql
-- Common rows (like ∩ in RA)
SELECT name FROM Student
INTERSECT
SELECT name FROM Alumni;
```

### EXCEPT / MINUS

```sql
-- Difference (like − in RA)
SELECT name FROM Student
EXCEPT
SELECT name FROM Graduated;
```

### Compatibility Requirements
- Same number of columns
- Compatible data types

---

## 12. Views

### Creating Views

```sql
CREATE VIEW HighEarners AS
SELECT emp_id, name, salary
FROM Employee
WHERE salary > 100000;

-- Query the view like a table
SELECT * FROM HighEarners WHERE name LIKE 'A%';
```

### Updatable Views

A view is updatable if:
1. Based on single table
2. No aggregates, DISTINCT, GROUP BY
3. No computed columns
4. Includes primary key
5. No subqueries in SELECT

```sql
-- Updatable view
CREATE VIEW CSEmployees AS
SELECT emp_id, name, salary FROM Employee WHERE dept = 'CS';

-- Can do:
INSERT INTO CSEmployees VALUES (100, 'New', 50000);
UPDATE CSEmployees SET salary = 60000 WHERE emp_id = 100;
DELETE FROM CSEmployees WHERE emp_id = 100;
```

### WITH CHECK OPTION

```sql
CREATE VIEW CSEmployees AS
SELECT * FROM Employee WHERE dept = 'CS'
WITH CHECK OPTION;

-- This will FAIL because dept is not 'CS':
INSERT INTO CSEmployees VALUES (100, 'New', 50000, 'IT');
```

### Materialized Views

```sql
-- Pre-computed and stored (not in standard SQL)
CREATE MATERIALIZED VIEW MonthlySales AS
SELECT month, SUM(amount) as total
FROM Sales
GROUP BY month;
```

---

## 13. Advanced SQL Features

### CASE Expression

```sql
SELECT name, salary,
    CASE 
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_grade
FROM Employee;

-- Simple CASE
SELECT name,
    CASE dept_id
        WHEN 1 THEN 'Engineering'
        WHEN 2 THEN 'Marketing'
        ELSE 'Other'
    END AS department
FROM Employee;
```

### Common Table Expressions (CTE)

```sql
WITH DeptStats AS (
    SELECT dept_id, AVG(salary) as avg_salary, COUNT(*) as emp_count
    FROM Employee
    GROUP BY dept_id
)
SELECT D.dept_name, DS.avg_salary, DS.emp_count
FROM Department D
JOIN DeptStats DS ON D.dept_id = DS.dept_id;
```

### Window Functions

```sql
-- Row number within department
SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank
FROM Employee;

-- Running total
SELECT name, salary,
    SUM(salary) OVER (ORDER BY emp_id) as running_total
FROM Employee;

-- Common window functions:
-- ROW_NUMBER(), RANK(), DENSE_RANK()
-- LEAD(), LAG()
-- FIRST_VALUE(), LAST_VALUE()
-- SUM(), AVG(), COUNT() OVER (...)
```

---

## 14. Query Output Prediction (GATE Skill)

### Step-by-Step Approach

1. **Identify tables and their content**
2. **Trace execution order**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
3. **Handle NULL carefully**
4. **Count final rows**

### Example 1: Aggregate with NULL

```sql
Table: T
| A | B  |
|---|------|
| 1 | 10   |
| 2 | NULL |
| 3 | 20   |
| 1 | 30   |

Query: SELECT A, SUM(B) FROM T GROUP BY A;

Step 1: Group by A
  Group A=1: rows (1,10), (1,30) → SUM = 40
  Group A=2: rows (2,NULL) → SUM = NULL
  Group A=3: rows (3,20) → SUM = 20

Result:
| A | SUM(B) |
|---|--------|
| 1 | 40     |
| 2 | NULL   |
| 3 | 20     |
```

### Example 2: Join with NULL

```sql
R                   S
| A | B |          | B | C |
|---|---|          |---|---|
| 1 | 2 |          | 2 | X |
| 3 | NULL|        | NULL | Y |

Query: SELECT * FROM R NATURAL JOIN S;

Join condition: R.B = S.B
- (1,2) matches (2,X) → (1, 2, X)
- (3,NULL) vs (NULL,Y): NULL = NULL is UNKNOWN → No match

Result:
| A | B | C |
|---|---|---|
| 1 | 2 | X |
```

### Example 3: NOT IN with NULL

```sql
T1: | X |     T2: | Y |
    |---|         |---|
    | 1 |         | 1 |
    | 2 |         | NULL |
    | 3 |

Query: SELECT * FROM T1 WHERE X NOT IN (SELECT Y FROM T2);

For X = 1: 1 NOT IN (1, NULL) = FALSE
For X = 2: 2 NOT IN (1, NULL) = 2<>1 AND 2<>NULL = TRUE AND UNKNOWN = UNKNOWN
For X = 3: 3 NOT IN (1, NULL) = 3<>1 AND 3<>NULL = TRUE AND UNKNOWN = UNKNOWN

Result: EMPTY! (Nothing returned because of NULL in subquery)
```

---

## 15. Common GATE Patterns

### Pattern 1: NULL Handling
Predict output with NULL values in aggregates, joins, comparisons.

### Pattern 2: Nested Query Evaluation
Trace correlated vs non-correlated subqueries.

### Pattern 3: GROUP BY Output Rows
Count groups and apply HAVING filter.

### Pattern 4: Join Output Count
Calculate min/max possible rows.

### Pattern 5: Equivalent Queries
Identify queries that produce same output.

---

## 16. Edge Cases Summary

| Scenario | Behavior |
|----------|----------|
| AVG of NULLs only | NULL |
| COUNT(*) with all NULLs | Count of rows (not 0) |
| GROUP BY with NULL values | NULL forms its own group |
| ORDER BY with NULLs | DB-specific (first or last) |
| UNION of NULLs | Duplicates removed (NULL = NULL for UNION) |
| JOIN on NULL = NULL | Does not match (UNKNOWN) |
| DISTINCT on NULLs | Keeps one NULL |

---

## 🧠 Memory Techniques

### Execution Order: "From Where Grandpa Had Selected Oranges Later"
- **F**ROM
- **W**HERE
- **G**ROUP BY
- **H**AVING
- **S**ELECT
- **O**RDER BY
- **L**IMIT

### NULL Comparison: "NULL is Unknowable"
- NULL = anything → UNKNOWN
- NULL <> anything → UNKNOWN
- Use IS NULL / IS NOT NULL

### Join Types: "LEFT keeps Left, RIGHT keeps Right, FULL keeps All"

---

## 🔑 Key Takeaways for GATE

1. **Execution Order**: Critical for understanding aliases and aggregates
2. **NULL = NULL is UNKNOWN**: Not TRUE!
3. **NOT IN with NULL**: Returns empty result
4. **COUNT(*) vs COUNT(col)**: Former includes NULL rows
5. **AVG ignores NULL**: Doesn't treat as 0
6. **GROUP BY rules**: All non-aggregate columns must be in GROUP BY

---

## 📚 Related Chapters
- [← Previous: Chapter 03 - Relational Model](../03-Relational-Model/README.md)
- [Next: Chapter 05 - Normalization →](../05-Normalization/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
