# Chapter 3: Relational Model

---

## 🎯 What is the Relational Model?

The **Relational Model** organizes data into **relations (tables)** where:
- Data is stored in rows and columns
- Relationships are represented through **values** (not pointers)
- All operations produce new relations (closure property)

### 🔑 Key Insight
> Developed by **E.F. Codd at IBM (1970)**
> 
> Codd's paper: "A Relational Model of Data for Large Shared Data Banks"

---

## 📊 Formal Definitions

### Relation
A relation R is a subset of the Cartesian product of n domains:
```
R ⊆ D₁ × D₂ × D₃ × ... × Dₙ
```

### Example:
```
Domain D₁ = {1, 2, 3}           (Roll numbers)
Domain D₂ = {Alice, Bob, Carol} (Names)
Domain D₃ = {CS, EE, ME}        (Departments)

Relation Student ⊆ D₁ × D₂ × D₃

Student = {(1, Alice, CS), (2, Bob, EE), (3, Carol, CS)}
```

### Terminology Mapping

| Formal Term | Informal Term | File System Term |
|-------------|---------------|------------------|
| Relation | Table | File |
| Tuple | Row | Record |
| Attribute | Column | Field |
| Domain | Data Type | Field Type |
| Relation Schema | Table Definition | File Structure |
| Relation Instance | Table Data | File Content |

---

## 📐 Relational Schema vs Instance

### Schema (Intension)
- **Structure** of the relation
- Rarely changes
- Notation: R(A₁, A₂, ..., Aₙ)

```
Student(Roll: INT, Name: VARCHAR, Dept: VARCHAR, CGPA: FLOAT)
```

### Instance (Extension)
- **Data** in the relation at a given time
- Changes frequently
- A set of tuples

```
Current Instance:
┌──────┬────────┬──────┬──────┐
│ Roll │  Name  │ Dept │ CGPA │
├──────┼────────┼──────┼──────┤
│  1   │ Alice  │  CS  │ 9.2  │
│  2   │ Bob    │  EE  │ 8.5  │
│  3   │ Carol  │  CS  │ 9.0  │
└──────┴────────┴──────┴──────┘
```

### 🎭 Analogy
> - **Schema** = Recipe (ingredients list, structure)
> - **Instance** = Actual dish made (can make multiple times)

---

## 🔑 Keys in Relational Model

### Super Key
Any set of attributes that **uniquely identifies** tuples.

```
For Student(Roll, Name, Email, Dept):
Super Keys: {Roll}, {Email}, {Roll, Name}, {Roll, Email}, 
           {Roll, Name, Email}, {Roll, Name, Dept}, ...
```

### Candidate Key
**Minimal** super key (no proper subset is a super key).

```
Candidate Keys: {Roll}, {Email}

{Roll, Name} is NOT a candidate key because {Roll} alone suffices
```

### Primary Key
One **chosen** candidate key for main identification.

```
PRIMARY KEY: Roll (chosen by designer)
```

### Alternate Key
Candidate keys that are **not chosen** as primary key.

```
Alternate Key: Email (since Roll is PK)
```

### Foreign Key
Attribute(s) that **reference** primary key of another relation.

```
Student(Roll, Name, Dept_ID)
Department(Dept_ID, Dept_Name)

Dept_ID in Student is FOREIGN KEY referencing Department(Dept_ID)
```

### Composite Key
Primary key made of **multiple attributes**.

```
Enrollment(Student_Roll, Course_ID, Grade)
Composite PK: (Student_Roll, Course_ID)
```

### 📊 Key Hierarchy

```
                    All Attributes
                          │
                    ┌─────┴─────┐
                    ▼           ▼
              Super Keys    Non-Key Attrs
                    │
            ┌───────┴───────┐
            ▼               ▼
      Candidate Keys   Non-Minimal Super Keys
            │
      ┌─────┴─────┐
      ▼           ▼
Primary Key   Alternate Keys
```

---

## 🔢 Counting Keys (GATE Favorite!)

### Number of Super Keys

**Given**: Relation with n attributes, candidate key of size k

**Formula**: Number of Super Keys = 2^(n-k)

### Why?
- Candidate key attributes MUST be included
- Remaining (n-k) attributes can be included or not → 2^(n-k) choices

### Example:
```
R(A, B, C, D, E) where {A, B} is the only candidate key

n = 5, k = 2
Super Keys = 2^(5-2) = 2³ = 8

They are: {AB}, {ABC}, {ABD}, {ABE}, {ABCD}, {ABCE}, {ABDE}, {ABCDE}
```

### Multiple Candidate Keys

**Formula**: Apply Inclusion-Exclusion Principle

If CK₁ and CK₂ are two candidate keys:
```
Total Super Keys = SK(CK₁) + SK(CK₂) - SK(CK₁ ∪ CK₂)
```

### Example:
```
R(A, B, C, D) with candidate keys {A} and {B}

SK containing A = 2^(4-1) = 8
SK containing B = 2^(4-1) = 8
SK containing both A and B = 2^(4-2) = 4

Total = 8 + 8 - 4 = 12 super keys
```

---

## 🔒 Integrity Constraints

### 1. Domain Constraint
Each attribute value must be from its defined domain.

```sql
CREATE TABLE Student (
    Roll INT,              -- Domain: integers
    Name VARCHAR(50),      -- Domain: strings up to 50 chars
    Age INT CHECK (Age > 0 AND Age < 120)  -- Domain: positive integers < 120
);
```

### 2. Key Constraint (Entity Integrity)
- Primary key must be **UNIQUE**
- Primary key cannot be **NULL**

```sql
CREATE TABLE Student (
    Roll INT PRIMARY KEY,  -- Unique + NOT NULL
    Name VARCHAR(50)
);
```

### 3. Referential Integrity (Foreign Key Constraint)
Foreign key value must either:
- Match a primary key value in referenced table, OR
- Be NULL (if allowed)

```sql
CREATE TABLE Enrollment (
    Roll INT,
    CourseID INT,
    FOREIGN KEY (Roll) REFERENCES Student(Roll),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);
```

### Referential Integrity Actions

| Action | ON DELETE | ON UPDATE |
|--------|-----------|-----------|
| **CASCADE** | Delete referencing rows | Update FK values |
| **SET NULL** | Set FK to NULL | Set FK to NULL |
| **SET DEFAULT** | Set FK to default | Set FK to default |
| **RESTRICT** | Prevent deletion | Prevent update |
| **NO ACTION** | Prevent (checked at end) | Prevent (checked at end) |

### Example:
```sql
CREATE TABLE Enrollment (
    Roll INT,
    CourseID INT,
    FOREIGN KEY (Roll) REFERENCES Student(Roll)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- If Student(Roll=1) deleted → All Enrollment rows with Roll=1 deleted
```

### 4. NOT NULL Constraint
Attribute cannot have NULL value.

```sql
CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL  -- Must have a value
);
```

### 5. UNIQUE Constraint
All values in column(s) must be distinct (NULLs allowed).

```sql
CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE  -- No duplicate emails
);
```

### 6. CHECK Constraint
Custom condition on attribute values.

```sql
CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Age INT CHECK (Age >= 18),
    Grade CHAR(1) CHECK (Grade IN ('A', 'B', 'C', 'D', 'F'))
);
```

---

## 📏 Codd's 12 Rules (13 Rules: 0-12)

### Rule 0: Foundation Rule
A system that claims to be a RDBMS must manage data entirely through relational capabilities.

### Rule 1: Information Rule
All information must be represented as data values in tables.

### Rule 2: Guaranteed Access Rule
Every value must be accessible via table name + primary key + column name.

### Rule 3: Systematic NULL Treatment
NULLs must be handled systematically (distinct from empty string or zero).

### Rule 4: Active Online Catalog
Database structure must be stored in system tables (data dictionary) accessible via same language.

### Rule 5: Comprehensive Data Sublanguage
At least one language must support:
- Data definition (DDL)
- Data manipulation (DML)
- Security/Authorization (DCL)
- Integrity constraints

### Rule 6: View Updating Rule
All theoretically updateable views must be updateable by the system.

### Rule 7: High-Level Insert, Update, Delete
Operations must work on sets of rows, not just single rows.

### Rule 8: Physical Data Independence
Changing physical storage must not require application changes.

### Rule 9: Logical Data Independence
Changing logical schema must not require application changes (where possible).

### Rule 10: Integrity Independence
Integrity constraints must be defined in catalog, not in application code.

### Rule 11: Distribution Independence
Applications should work regardless of data distribution (single or distributed).

### Rule 12: Non-Subversion Rule
Low-level access must not bypass integrity constraints.

### 🧠 Memory Trick (GIFT PLAN CHIND)
```
G - Guaranteed access
I - Information rule
F - Foundation
T - Treatement of NULL

P - Physical independence
L - Logical independence
A - Active catalog
N - Non-subversion

C - Comprehensive sublanguage
H - High-level operations
I - Integrity independence
N - Non-distribution dependence
D - View updating (Derived relations)
```

### 📊 GATE Focus
Most commonly asked:
1. Information Rule (Rule 1)
2. Guaranteed Access (Rule 2)
3. Physical/Logical Independence (Rules 8, 9)
4. Integrity Independence (Rule 10)

---

## 📊 Degree and Cardinality

### Degree (Arity)
Number of **attributes (columns)** in a relation.

### Cardinality
Number of **tuples (rows)** in a relation.

```
Student:
┌──────┬────────┬──────┐
│ Roll │  Name  │ Dept │  ← Degree = 3
├──────┼────────┼──────┤
│  1   │ Alice  │  CS  │
│  2   │ Bob    │  EE  │
│  3   │ Carol  │  CS  │  ← Cardinality = 3
└──────┴────────┴──────┘
```

### After Operations

| Operation | Effect on Degree | Effect on Cardinality |
|-----------|------------------|----------------------|
| SELECT (σ) | Same | ≤ Original |
| PROJECT (π) | ≤ Original | ≤ Original |
| UNION (∪) | Same | ≤ Sum |
| INTERSECT (∩) | Same | ≤ Min |
| DIFFERENCE (-) | Same | ≤ First relation |
| CROSS PRODUCT (×) | Sum | Product |
| JOIN (⋈) | ≤ Sum | ≤ Product |

---

## ⚠️ NULL Values

### What is NULL?
- **Unknown** value
- **Not applicable** value
- **Missing** value

### NULL in Comparisons

| Expression | Result |
|------------|--------|
| NULL = NULL | UNKNOWN |
| NULL < 5 | UNKNOWN |
| NULL AND TRUE | UNKNOWN |
| NULL AND FALSE | FALSE |
| NULL OR TRUE | TRUE |
| NULL OR FALSE | UNKNOWN |
| NOT NULL | UNKNOWN |

### Three-Valued Logic Table

**AND**:
| | TRUE | FALSE | UNKNOWN |
|---|------|-------|---------|
| TRUE | T | F | U |
| FALSE | F | F | F |
| UNKNOWN | U | F | U |

**OR**:
| | TRUE | FALSE | UNKNOWN |
|---|------|-------|---------|
| TRUE | T | T | T |
| FALSE | T | F | U |
| UNKNOWN | T | U | U |

### 🎯 GATE Trap
```sql
SELECT * FROM Student WHERE Age = NULL;  -- Returns NO rows!
SELECT * FROM Student WHERE Age IS NULL; -- Correct way
```

---

## 🔀 Tuple Relational Calculus Preview

### Declarative vs Procedural

| Relational Algebra | Relational Calculus |
|--------------------|---------------------|
| Procedural (HOW) | Declarative (WHAT) |
| Specifies operations | Specifies conditions |
| Step-by-step | Result specification |

### Example:
```
Find students in CS department:

Relational Algebra: σ_Dept='CS'(Student)

Tuple Calculus: {t | t ∈ Student ∧ t.Dept = 'CS'}
```

---

## 🧮 Operations on Relations (Preview)

### Unary Operations
- **SELECT (σ)**: Filter rows
- **PROJECT (π)**: Choose columns
- **RENAME (ρ)**: Rename relation/attributes

### Binary Operations
- **UNION (∪)**: Combine rows from two relations
- **INTERSECTION (∩)**: Common rows
- **DIFFERENCE (-)**: Rows in first but not second
- **CARTESIAN PRODUCT (×)**: All combinations
- **JOIN (⋈)**: Combine related rows

*Detailed coverage in [Chapter 4: Relational Algebra](./04-Relational-Algebra-and-Calculus.md)*

---

## 🎯 Schema Diagrams

### Notation
```
┌─────────────────────────────────┐
│           STUDENT               │
├─────────────────────────────────┤
│ Roll (PK)                       │
│ Name                            │
│ Email (UNIQUE)                  │
│ Dept_ID (FK → Department)       │
└─────────────────────────────────┘
         │
         │ references
         ▼
┌─────────────────────────────────┐
│         DEPARTMENT              │
├─────────────────────────────────┤
│ Dept_ID (PK)                    │
│ Dept_Name                       │
│ HOD_ID (FK → Faculty)           │
└─────────────────────────────────┘
```

---

## 📝 Example: University Database Schema

```sql
-- Complete Schema Definition

CREATE TABLE Department (
    Dept_ID INT PRIMARY KEY,
    Dept_Name VARCHAR(50) NOT NULL UNIQUE,
    Building VARCHAR(20)
);

CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    DOB DATE,
    Dept_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
        ON DELETE SET NULL
);

CREATE TABLE Course (
    Course_ID VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Credits INT CHECK (Credits > 0 AND Credits <= 6),
    Dept_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);

CREATE TABLE Enrollment (
    Roll INT,
    Course_ID VARCHAR(10),
    Semester VARCHAR(10),
    Grade CHAR(2),
    PRIMARY KEY (Roll, Course_ID, Semester),
    FOREIGN KEY (Roll) REFERENCES Student(Roll)
        ON DELETE CASCADE,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);
```

---

## ⚠️ Common GATE Traps

### Trap 1: NULL Comparisons
```sql
-- Q: How many rows returned if some students have NULL age?
SELECT * FROM Student WHERE Age <> 25;
-- Answer: Rows with Age NOT 25 AND Age NOT NULL
-- NULL rows are excluded!
```

### Trap 2: Super Key Count
```
R(A, B, C) with CK = {A, B}
Q: Number of super keys?

Wrong: 2³ = 8 (treating A,B as separate)
Right: 2^(3-2) = 2 (A,B fixed, C optional)
       {AB}, {ABC}
```

### Trap 3: Foreign Key Can Be NULL
```sql
-- FK can be NULL (unless explicitly NOT NULL)
Student(Roll, Name, Dept_ID)
-- Dept_ID can be NULL if student not assigned to department
```

### Trap 4: Primary Key vs UNIQUE
| Aspect | PRIMARY KEY | UNIQUE |
|--------|-------------|--------|
| NULL allowed | No | Yes (one NULL typically) |
| Number per table | One | Multiple |
| Implicit index | Yes | Usually yes |

---

## 🧪 Practice Problems

### Q1: Super Keys
> R(A, B, C, D) with candidate keys {A} and {BC}. Count super keys.

**Solution**:
```
SK containing A = 2³ = 8
SK containing BC = 2² = 4
SK containing A and BC = 2¹ = 2

Total = 8 + 4 - 2 = 10
```

### Q2: Referential Integrity
> What happens when we delete a row referenced by foreign key with ON DELETE CASCADE?

**Answer**: All referencing rows are automatically deleted.

### Q3: NULL Logic
> Evaluate: (NULL OR TRUE) AND (NULL AND FALSE)

**Solution**:
```
NULL OR TRUE = TRUE
NULL AND FALSE = FALSE
TRUE AND FALSE = FALSE
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Keys** | Super ⊃ Candidate ⊃ Primary |
| **Super Key Count** | 2^(n-k) for single CK |
| **Constraints** | Domain, Key, Referential, NOT NULL, UNIQUE, CHECK |
| **NULL** | Unknown value, three-valued logic |
| **Codd's Rules** | 12 rules (0-12) for true RDBMS |
| **FK Actions** | CASCADE, SET NULL, RESTRICT, NO ACTION |

---

## 🎓 Quick Revision Points

1. ✅ E.F. Codd → Relational Model (1970)
2. ✅ Primary Key = Unique + NOT NULL
3. ✅ Super Key Count = 2^(n-k)
4. ✅ NULL = NULL gives UNKNOWN, not TRUE
5. ✅ FK can be NULL (if not explicitly restricted)
6. ✅ Codd's 12 rules (actually 0-12 = 13 rules)
7. ✅ Referential integrity: Foreign key → Primary key reference

---

*Previous: [Data Models & ER Diagrams](./02-Data-Models-and-ER-Diagrams.md) | Next: [Relational Algebra & Calculus](./04-Relational-Algebra-and-Calculus.md)*
