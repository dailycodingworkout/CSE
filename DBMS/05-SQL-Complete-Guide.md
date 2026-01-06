# Chapter 5: SQL - Complete Guide

---

## 🎯 What is SQL?

**SQL (Structured Query Language)** is the standard language for relational databases.

### Key Characteristics
- **Declarative**: Specify WHAT, not HOW
- **Set-based**: Operates on sets of rows
- **Non-procedural**: No loops or conditionals in basic SQL

### 🔑 SQL vs Relational Algebra
| Aspect | SQL | Relational Algebra |
|--------|-----|-------------------|
| Nature | Declarative | Procedural |
| Duplicates | Allowed (bags) | Not allowed (sets) |
| NULL handling | Three-valued logic | Limited |
| Aggregation | Built-in | Extended RA |

---

## 📊 SQL Components

```
                        SQL
                         │
    ┌────────┬───────────┼───────────┬────────┐
    │        │           │           │        │
   DDL      DML         DCL        TCL      DQL
    │        │           │           │        │
 CREATE   SELECT      GRANT      COMMIT   SELECT
 ALTER    INSERT      REVOKE    ROLLBACK  (Often part
 DROP     UPDATE                SAVEPOINT  of DML)
 TRUNCATE DELETE
```

---

## 🔨 DDL - Data Definition Language

### CREATE TABLE

```sql
CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    DOB DATE,
    CGPA DECIMAL(3,2) CHECK (CGPA >= 0 AND CGPA <= 10),
    Dept_ID INT DEFAULT NULL,
    FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

### Data Types

| Category | Types | Usage |
|----------|-------|-------|
| **Numeric** | INT, BIGINT, DECIMAL(p,s), FLOAT | Numbers |
| **String** | CHAR(n), VARCHAR(n), TEXT | Text |
| **Date/Time** | DATE, TIME, DATETIME, TIMESTAMP | Temporal |
| **Boolean** | BOOLEAN, BIT | True/False |
| **Binary** | BLOB, BINARY | Files, images |

### CHAR vs VARCHAR

| Aspect | CHAR(n) | VARCHAR(n) |
|--------|---------|------------|
| Storage | Fixed n bytes | Variable (actual + 1-2 bytes) |
| Padding | Right-padded with spaces | No padding |
| Best for | Fixed-length data (state codes) | Variable-length (names) |

### ALTER TABLE

```sql
-- Add column
ALTER TABLE Student ADD Phone VARCHAR(15);

-- Drop column
ALTER TABLE Student DROP COLUMN Phone;

-- Modify column
ALTER TABLE Student MODIFY Name VARCHAR(100);

-- Add constraint
ALTER TABLE Student ADD CONSTRAINT chk_cgpa CHECK (CGPA <= 10);

-- Drop constraint
ALTER TABLE Student DROP CONSTRAINT chk_cgpa;

-- Rename column
ALTER TABLE Student RENAME COLUMN Name TO Full_Name;
```

### DROP vs TRUNCATE vs DELETE

| Aspect | DROP | TRUNCATE | DELETE |
|--------|------|----------|--------|
| **Type** | DDL | DDL | DML |
| **Removes** | Table + Data | Data only | Data only |
| **WHERE** | N/A | Not allowed | Allowed |
| **Rollback** | Usually No | Usually No | Yes |
| **Speed** | Fastest | Fast | Slowest |
| **Triggers** | No | No | Yes |
| **Identity** | Reset | Reset | Not reset |
| **Space** | Freed | Freed | Not freed |

### ⚠️ GATE Trap
```sql
TRUNCATE TABLE Student;  -- Cannot rollback (DDL)
DELETE FROM Student;      -- Can rollback (DML)
```

---

## 📝 DML - Data Manipulation Language

### INSERT

```sql
-- Single row
INSERT INTO Student VALUES (1, 'Alice', 'alice@email.com', '2000-01-15', 9.2, 10);

-- Specific columns
INSERT INTO Student (Roll, Name, Dept_ID) VALUES (2, 'Bob', 20);

-- Multiple rows
INSERT INTO Student (Roll, Name) VALUES 
    (3, 'Carol'),
    (4, 'Dave'),
    (5, 'Eve');

-- From another table
INSERT INTO Archive_Students
SELECT * FROM Student WHERE Graduated = TRUE;
```

### UPDATE

```sql
-- Simple update
UPDATE Student SET CGPA = 9.5 WHERE Roll = 1;

-- Multiple columns
UPDATE Student SET CGPA = CGPA + 0.1, Dept_ID = 20 WHERE Dept_ID = 10;

-- Update with subquery
UPDATE Student 
SET Dept_ID = (SELECT Dept_ID FROM Department WHERE Dept_Name = 'CS')
WHERE Roll = 1;

-- Update all rows (dangerous!)
UPDATE Student SET CGPA = CGPA * 1.1;  -- 10% increase for all
```

### DELETE

```sql
-- Delete specific rows
DELETE FROM Student WHERE CGPA < 5.0;

-- Delete with subquery
DELETE FROM Enrollment 
WHERE Roll IN (SELECT Roll FROM Student WHERE Graduated = TRUE);

-- Delete all rows
DELETE FROM Student;  -- Keeps table structure
```

---

## 🔍 SELECT - The Heart of SQL

### Basic Syntax
```sql
SELECT [DISTINCT] column_list
FROM table_name
[WHERE condition]
[GROUP BY columns]
[HAVING condition]
[ORDER BY columns [ASC|DESC]]
[LIMIT n [OFFSET m]];
```

### Execution Order (Logical)
```
1. FROM      - Identify tables
2. WHERE     - Filter rows
3. GROUP BY  - Group rows
4. HAVING    - Filter groups
5. SELECT    - Choose columns
6. DISTINCT  - Remove duplicates
7. ORDER BY  - Sort results
8. LIMIT     - Limit rows
```

### 🧠 Memory Trick: "From Where Groups Having Selected Distinct Orders Limit"
> **F**rom **W**here **G**roups **H**aving **S**elected **D**istinct **O**rders **L**imit

---

## 📊 SELECT Clause Variations

### Basic Selection
```sql
-- All columns
SELECT * FROM Student;

-- Specific columns
SELECT Roll, Name FROM Student;

-- With aliases
SELECT Roll AS ID, Name AS Student_Name FROM Student;

-- With expressions
SELECT Name, CGPA * 10 AS Percentage FROM Student;

-- DISTINCT
SELECT DISTINCT Dept_ID FROM Student;
```

### ⚠️ COUNT(*) vs COUNT(column)

| Expression | Counts |
|------------|--------|
| COUNT(*) | All rows (including NULLs) |
| COUNT(column) | Non-NULL values in column |
| COUNT(DISTINCT column) | Unique non-NULL values |

```sql
-- Table: Student(Roll, Name, Email)
-- (1, 'Alice', 'a@x.com')
-- (2, 'Bob', NULL)
-- (3, 'Carol', 'c@x.com')

SELECT COUNT(*) FROM Student;         -- 3
SELECT COUNT(Email) FROM Student;     -- 2 (NULL excluded)
SELECT COUNT(DISTINCT Email) FROM Student; -- 2
```

---

## 🎯 WHERE Clause

### Comparison Operators
```sql
= , <> , != , < , > , <= , >=

SELECT * FROM Student WHERE CGPA > 8.0;
SELECT * FROM Student WHERE Dept_ID <> 10;
```

### Logical Operators
```sql
AND, OR, NOT

SELECT * FROM Student WHERE Dept_ID = 10 AND CGPA > 9.0;
SELECT * FROM Student WHERE Dept_ID = 10 OR Dept_ID = 20;
SELECT * FROM Student WHERE NOT (Dept_ID = 10);
```

### Special Operators

#### BETWEEN
```sql
SELECT * FROM Student WHERE CGPA BETWEEN 8.0 AND 9.0;
-- Equivalent to: CGPA >= 8.0 AND CGPA <= 9.0 (inclusive)
```

#### IN
```sql
SELECT * FROM Student WHERE Dept_ID IN (10, 20, 30);
-- Equivalent to: Dept_ID = 10 OR Dept_ID = 20 OR Dept_ID = 30
```

#### LIKE (Pattern Matching)
```sql
-- % = any sequence of characters
-- _ = single character

SELECT * FROM Student WHERE Name LIKE 'A%';     -- Starts with A
SELECT * FROM Student WHERE Name LIKE '%son';   -- Ends with son
SELECT * FROM Student WHERE Name LIKE '%an%';   -- Contains an
SELECT * FROM Student WHERE Name LIKE '_o_';    -- 3 chars, o in middle
```

#### IS NULL
```sql
SELECT * FROM Student WHERE Email IS NULL;
SELECT * FROM Student WHERE Email IS NOT NULL;

-- WRONG: WHERE Email = NULL (never matches!)
```

---

## 🔗 JOINs in SQL

### INNER JOIN
```sql
SELECT S.Name, D.Dept_Name
FROM Student S
INNER JOIN Department D ON S.Dept_ID = D.Dept_ID;
```

### LEFT OUTER JOIN
```sql
SELECT S.Name, D.Dept_Name
FROM Student S
LEFT JOIN Department D ON S.Dept_ID = D.Dept_ID;
-- All students, NULL for dept if no match
```

### RIGHT OUTER JOIN
```sql
SELECT S.Name, D.Dept_Name
FROM Student S
RIGHT JOIN Department D ON S.Dept_ID = D.Dept_ID;
-- All departments, NULL for student if no match
```

### FULL OUTER JOIN
```sql
SELECT S.Name, D.Dept_Name
FROM Student S
FULL OUTER JOIN Department D ON S.Dept_ID = D.Dept_ID;
-- All from both, NULL where no match
```

### CROSS JOIN
```sql
SELECT S.Name, C.Course_Name
FROM Student S
CROSS JOIN Course C;
-- Cartesian product
```

### SELF JOIN
```sql
-- Find employees and their managers
SELECT E.Name AS Employee, M.Name AS Manager
FROM Employee E
LEFT JOIN Employee M ON E.Manager_ID = M.Emp_ID;
```

### NATURAL JOIN
```sql
SELECT * FROM Student NATURAL JOIN Department;
-- Automatically joins on columns with same name
-- ⚠️ Dangerous if unintended columns match!
```

### 📊 JOIN Result Sizes

| Join Type | Max Result Size |
|-----------|-----------------|
| INNER JOIN | min(m, n) to m×n |
| LEFT JOIN | m to m×n |
| RIGHT JOIN | n to m×n |
| FULL OUTER | max(m,n) to m+n |
| CROSS JOIN | exactly m×n |

---

## 📊 Aggregate Functions

| Function | Description |
|----------|-------------|
| COUNT() | Number of rows/values |
| SUM() | Total of numeric values |
| AVG() | Average of numeric values |
| MAX() | Maximum value |
| MIN() | Minimum value |

### Usage
```sql
SELECT 
    COUNT(*) AS Total_Students,
    AVG(CGPA) AS Average_CGPA,
    MAX(CGPA) AS Highest_CGPA,
    MIN(CGPA) AS Lowest_CGPA,
    SUM(Credits) AS Total_Credits
FROM Student;
```

### NULL Handling in Aggregates
- All aggregates **ignore NULLs** (except COUNT(*))
- AVG(column) = SUM(column) / COUNT(column)

---

## 📦 GROUP BY Clause

### Syntax
```sql
SELECT Dept_ID, COUNT(*), AVG(CGPA)
FROM Student
GROUP BY Dept_ID;
```

### Rule
> Every column in SELECT must be either:
> 1. In GROUP BY, OR
> 2. In an aggregate function

### Example
```sql
-- Valid
SELECT Dept_ID, COUNT(*), AVG(CGPA)
FROM Student
GROUP BY Dept_ID;

-- Invalid (Name not in GROUP BY or aggregate)
SELECT Dept_ID, Name, COUNT(*)  -- ❌ Error!
FROM Student
GROUP BY Dept_ID;
```

---

## 🎛️ HAVING Clause

### Purpose
Filter **groups** (not rows) based on aggregate conditions.

### WHERE vs HAVING

| Aspect | WHERE | HAVING |
|--------|-------|--------|
| Filters | Individual rows | Groups |
| Timing | Before grouping | After grouping |
| Aggregates | Cannot use | Can use |

### Example
```sql
SELECT Dept_ID, AVG(CGPA) AS Avg_CGPA
FROM Student
WHERE CGPA > 5.0           -- Filter rows before grouping
GROUP BY Dept_ID
HAVING COUNT(*) >= 5;      -- Filter groups after
```

---

## 📱 Subqueries

### Types by Location

#### 1. Scalar Subquery (Returns single value)
```sql
SELECT Name, CGPA,
    (SELECT AVG(CGPA) FROM Student) AS Overall_Avg
FROM Student;
```

#### 2. Row Subquery (Returns single row)
```sql
SELECT * FROM Student
WHERE (Dept_ID, CGPA) = (SELECT Dept_ID, MAX(CGPA) 
                          FROM Student 
                          GROUP BY Dept_ID 
                          LIMIT 1);
```

#### 3. Table Subquery (Returns table)
```sql
SELECT * FROM 
    (SELECT Dept_ID, AVG(CGPA) AS Avg
     FROM Student GROUP BY Dept_ID) AS DeptAvg
WHERE Avg > 8.0;
```

### Subquery Operators

#### IN / NOT IN
```sql
SELECT * FROM Student
WHERE Dept_ID IN (SELECT Dept_ID FROM Department WHERE Building = 'Main');
```

#### EXISTS / NOT EXISTS
```sql
-- Students who have enrolled in at least one course
SELECT * FROM Student S
WHERE EXISTS (SELECT 1 FROM Enrollment E WHERE E.Roll = S.Roll);
```

#### ANY / SOME
```sql
-- Students with CGPA greater than ANY student in CS
SELECT * FROM Student
WHERE CGPA > ANY (SELECT CGPA FROM Student WHERE Dept_ID = 10);
```

#### ALL
```sql
-- Student with highest CGPA (greater than ALL others)
SELECT * FROM Student
WHERE CGPA >= ALL (SELECT CGPA FROM Student);
```

### Correlated Subquery
Inner query depends on outer query (executed for each outer row).

```sql
-- Students with above-average CGPA for their department
SELECT * FROM Student S1
WHERE CGPA > (SELECT AVG(CGPA) 
              FROM Student S2 
              WHERE S2.Dept_ID = S1.Dept_ID);  -- Correlated!
```

---

## 🔢 Set Operations

### UNION (Distinct) / UNION ALL (Duplicates)
```sql
SELECT Name FROM Student WHERE Dept_ID = 10
UNION
SELECT Name FROM Student WHERE CGPA > 9.0;
-- Removes duplicates

SELECT Name FROM Student WHERE Dept_ID = 10
UNION ALL
SELECT Name FROM Student WHERE CGPA > 9.0;
-- Keeps duplicates
```

### INTERSECT
```sql
SELECT Roll FROM Student
INTERSECT
SELECT Roll FROM Enrollment;
```

### EXCEPT / MINUS
```sql
SELECT Roll FROM Student
EXCEPT
SELECT Roll FROM Graduated;  -- Students who haven't graduated
```

---

## 📋 ORDER BY Clause

```sql
SELECT * FROM Student
ORDER BY CGPA DESC, Name ASC;

-- NULL handling
ORDER BY CGPA NULLS FIRST;  -- PostgreSQL
ORDER BY CGPA NULLS LAST;
```

---

## 🔢 LIMIT and OFFSET

```sql
-- First 10 rows
SELECT * FROM Student ORDER BY CGPA DESC LIMIT 10;

-- Rows 11-20 (pagination)
SELECT * FROM Student ORDER BY CGPA DESC LIMIT 10 OFFSET 10;
```

---

## 🔐 DCL - Data Control Language

### GRANT
```sql
-- Grant specific privileges
GRANT SELECT, INSERT ON Student TO user1;

-- Grant all privileges
GRANT ALL PRIVILEGES ON Student TO admin;

-- Grant with ability to grant others
GRANT SELECT ON Student TO user1 WITH GRANT OPTION;

-- Grant to all users
GRANT SELECT ON Student TO PUBLIC;
```

### REVOKE
```sql
-- Revoke specific privileges
REVOKE INSERT ON Student FROM user1;

-- Cascade revoke (revoke from grantees too)
REVOKE SELECT ON Student FROM user1 CASCADE;
```

---

## 🔄 TCL - Transaction Control Language

### COMMIT
```sql
BEGIN TRANSACTION;
UPDATE Account SET Balance = Balance - 100 WHERE ID = 1;
UPDATE Account SET Balance = Balance + 100 WHERE ID = 2;
COMMIT;  -- Make changes permanent
```

### ROLLBACK
```sql
BEGIN TRANSACTION;
DELETE FROM Student WHERE Roll = 1;
-- Oops, wrong delete!
ROLLBACK;  -- Undo changes
```

### SAVEPOINT
```sql
BEGIN TRANSACTION;
UPDATE Student SET CGPA = 9.0 WHERE Roll = 1;
SAVEPOINT sp1;
DELETE FROM Enrollment WHERE Roll = 1;
-- Realize mistake
ROLLBACK TO sp1;  -- Undo only after sp1
COMMIT;  -- Commit the UPDATE
```

---

## 👁️ Views

### What is a View?
A **virtual table** based on a query (doesn't store data).

### Create View
```sql
CREATE VIEW CS_Students AS
SELECT Roll, Name, CGPA
FROM Student
WHERE Dept_ID = 10;
```

### Updateable Views
Views can be updated if they:
1. Based on single table
2. Include primary key
3. No aggregates, DISTINCT, GROUP BY
4. No subqueries in SELECT

### Materialized View
Actually stores the result (for performance).

```sql
CREATE MATERIALIZED VIEW StudentStats AS
SELECT Dept_ID, COUNT(*), AVG(CGPA)
FROM Student
GROUP BY Dept_ID;

-- Refresh manually
REFRESH MATERIALIZED VIEW StudentStats;
```

---

## 🔄 Common Table Expressions (CTE)

### WITH Clause
```sql
WITH DeptStats AS (
    SELECT Dept_ID, AVG(CGPA) AS Avg_CGPA
    FROM Student
    GROUP BY Dept_ID
)
SELECT S.Name, D.Avg_CGPA
FROM Student S
JOIN DeptStats D ON S.Dept_ID = D.Dept_ID
WHERE S.CGPA > D.Avg_CGPA;
```

### Recursive CTE
```sql
-- Employee hierarchy
WITH RECURSIVE EmpHierarchy AS (
    -- Base case
    SELECT Emp_ID, Name, Manager_ID, 1 AS Level
    FROM Employee
    WHERE Manager_ID IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT E.Emp_ID, E.Name, E.Manager_ID, H.Level + 1
    FROM Employee E
    JOIN EmpHierarchy H ON E.Manager_ID = H.Emp_ID
)
SELECT * FROM EmpHierarchy;
```

---

## 🎯 CASE Expression

```sql
SELECT Name, CGPA,
    CASE
        WHEN CGPA >= 9.0 THEN 'Outstanding'
        WHEN CGPA >= 8.0 THEN 'Excellent'
        WHEN CGPA >= 7.0 THEN 'Good'
        WHEN CGPA >= 6.0 THEN 'Average'
        ELSE 'Below Average'
    END AS Performance
FROM Student;
```

---

## 📊 Window Functions

### Syntax
```sql
function() OVER (
    [PARTITION BY columns]
    [ORDER BY columns]
    [frame_clause]
)
```

### Examples

#### ROW_NUMBER
```sql
SELECT Name, Dept_ID, CGPA,
    ROW_NUMBER() OVER (PARTITION BY Dept_ID ORDER BY CGPA DESC) AS Rank
FROM Student;
```

#### RANK vs DENSE_RANK
```sql
-- CGPA: 9.5, 9.5, 9.0
-- RANK: 1, 1, 3 (skips 2)
-- DENSE_RANK: 1, 1, 2 (no skip)
```

#### Running Total
```sql
SELECT Name, Amount,
    SUM(Amount) OVER (ORDER BY Date) AS Running_Total
FROM Transactions;
```

---

## ⚠️ GATE-Specific SQL Traps

### Trap 1: NULL in WHERE
```sql
SELECT * FROM T WHERE A = NULL;   -- Returns 0 rows!
SELECT * FROM T WHERE A IS NULL;  -- Correct
```

### Trap 2: GROUP BY with SELECT
```sql
SELECT Dept_ID, Name, COUNT(*)  -- ❌ Error
FROM Student GROUP BY Dept_ID;
-- Name must be in GROUP BY or aggregate
```

### Trap 3: HAVING without GROUP BY
```sql
SELECT * FROM Student HAVING CGPA > 8;  -- ❌ Usually error
-- Use WHERE instead
```

### Trap 4: COUNT(*) vs COUNT(column)
```sql
-- If column has NULL, COUNT(column) < COUNT(*)
```

### Trap 5: UNION vs UNION ALL
```sql
-- UNION removes duplicates (slower)
-- UNION ALL keeps duplicates (faster)
```

### Trap 6: Nested Aggregates
```sql
SELECT MAX(AVG(CGPA)) FROM Student GROUP BY Dept_ID;  -- ❌ Invalid
-- Need subquery:
SELECT MAX(Avg_CGPA) FROM (SELECT AVG(CGPA) AS Avg_CGPA FROM Student GROUP BY Dept_ID) T;
```

---

## 🧪 Practice Questions

### Q1: Second Highest CGPA
```sql
SELECT MAX(CGPA) FROM Student
WHERE CGPA < (SELECT MAX(CGPA) FROM Student);

-- Or using LIMIT
SELECT CGPA FROM Student ORDER BY CGPA DESC LIMIT 1 OFFSET 1;
```

### Q2: Departments with no Students
```sql
SELECT * FROM Department D
WHERE NOT EXISTS (SELECT 1 FROM Student S WHERE S.Dept_ID = D.Dept_ID);

-- Or
SELECT * FROM Department
WHERE Dept_ID NOT IN (SELECT DISTINCT Dept_ID FROM Student WHERE Dept_ID IS NOT NULL);
```

### Q3: Duplicate Names
```sql
SELECT Name, COUNT(*)
FROM Student
GROUP BY Name
HAVING COUNT(*) > 1;
```

### Q4: Running Total
```sql
SELECT Roll, Amount,
    SUM(Amount) OVER (ORDER BY Roll) AS Running_Total
FROM Payments;
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **DDL** | CREATE, ALTER, DROP, TRUNCATE |
| **DML** | SELECT, INSERT, UPDATE, DELETE |
| **DCL** | GRANT, REVOKE |
| **TCL** | COMMIT, ROLLBACK, SAVEPOINT |
| **Execution Order** | FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY |
| **Aggregates** | Ignore NULL except COUNT(*) |
| **Subqueries** | IN, EXISTS, ANY, ALL |

---

## 🎓 Quick Revision Points

1. ✅ TRUNCATE is DDL, DELETE is DML
2. ✅ NULL comparisons use IS NULL, not = NULL
3. ✅ SELECT columns must be in GROUP BY or aggregate
4. ✅ WHERE filters rows, HAVING filters groups
5. ✅ UNION removes duplicates, UNION ALL keeps them
6. ✅ COUNT(*) includes NULL rows, COUNT(col) doesn't
7. ✅ Correlated subquery runs once per outer row

---

*Previous: [Relational Algebra & Calculus](./04-Relational-Algebra-and-Calculus.md) | Next: [Normalization & FD](./06-Normalization-and-FD.md)*
