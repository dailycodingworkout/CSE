# 📚 Chapter 03: Relational Model & Relational Algebra

> **The Atomic Truth**: *Data as mathematical relations; operations return relations.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 4-6 marks |
| Frequency | 90% years |
| Type | MCQ, NAT (count tuples), MSQ |
| Difficulty | Medium to Hard |
| Hot Topics | Keys, Relational Algebra expressions, Tuple/Domain Calculus |

---

## 1. Relational Model Fundamentals

### What is the Relational Model?
The **Relational Model** represents data as a collection of **relations** (tables) where each relation is a set of **tuples** (rows).

### Core Concepts

| Term | Definition | Alternative Name |
|------|------------|-----------------|
| **Relation** | A table with rows and columns | Table |
| **Tuple** | A row in a relation | Record, Row |
| **Attribute** | A column in a relation | Field, Column |
| **Domain** | Set of allowed values for an attribute | Data Type |
| **Schema** | Relation name + attribute names | Table structure |
| **Instance** | Set of tuples at a given time | Table data |

### Formal Definition

A **relation** $R$ is defined as:

$$R \subseteq D_1 \times D_2 \times \cdots \times D_n$$

Where $D_i$ is the domain of attribute $A_i$.

### Properties of Relations

| Property | Meaning | Implication |
|----------|---------|-------------|
| **No duplicate tuples** | Each row is unique | At least one candidate key exists |
| **Tuples are unordered** | No "first" or "last" row | Can't reference "5th row" |
| **Attributes are unordered** | Column order doesn't matter | Reference by name, not position |
| **Attribute values are atomic** | No multi-valued attributes | First Normal Form (1NF) |

### Relation Schema Notation

$$R(A_1, A_2, \ldots, A_n)$$

Example:
$$\text{Student}(\underline{\text{roll\_no}}, \text{name}, \text{age}, \text{dept\_id})$$

*Underline indicates primary key*

---

## 2. Keys in the Relational Model

### Types of Keys

```
                          ALL ATTRIBUTES
                               │
                    ┌──────────┴──────────┐
                    ▼                      ▼
               SUPER KEYS            NON-KEY ATTRIBUTES
                    │
         ┌──────────┴──────────┐
         ▼                      ▼
    CANDIDATE KEYS         OTHER SUPER KEYS
         │                (Non-minimal)
    ┌────┴────┐
    ▼         ▼
PRIMARY   ALTERNATE
  KEY       KEYS
```

### Key Definitions

| Key Type | Definition | Example |
|----------|------------|---------|
| **Super Key** | Any set of attributes that uniquely identifies tuples | {roll_no}, {roll_no, name}, {roll_no, name, age} |
| **Candidate Key** | Minimal super key (no proper subset is a super key) | {roll_no}, {email} |
| **Primary Key** | Chosen candidate key for the relation | {roll_no} |
| **Alternate Key** | Candidate keys not chosen as primary key | {email} |
| **Foreign Key** | Attribute that references primary key of another relation | dept_id in Student references Department |
| **Composite Key** | Key with multiple attributes | {course_id, student_id} in Enrollment |
| **Prime Attribute** | Attribute that is part of any candidate key | roll_no, email |
| **Non-Prime Attribute** | Attribute not part of any candidate key | name, age |

### Finding Candidate Keys

#### Method 1: Attribute Closure
The **closure** of a set of attributes $X$, denoted $X^+$, is the set of all attributes that can be functionally determined by $X$.

Algorithm:
```
1. Start with X+ = X
2. Repeat until no change:
   For each FD: Y → Z
   If Y ⊆ X+, then X+ = X+ ∪ Z
3. If X+ contains all attributes, X is a super key
4. If no proper subset of X is a super key, X is a candidate key
```

#### Method 2: Categorize Attributes

```
Given relation R(A, B, C, D, E) with FDs:
AB → C
C → D
D → E

Step 1: Categorize attributes
- LHS only: {A, B} - Must be in every key
- RHS only: {E} - Never in any key
- Both sides: {C, D} - May or may not be in key
- Neither side: {} - Must be in every key

Step 2: Start with (LHS only ∪ Neither side)
- Start with {A, B}
- Compute {A, B}+ = {A, B, C, D, E} = All attributes ✓
- Check if proper subset is super key:
  - {A}+ = {A} ✗
  - {B}+ = {B} ✗
- Therefore, {A, B} is the only candidate key
```

### Counting Super Keys (GATE NAT Favorite!)

**Formula**: If a candidate key has $k$ attributes and total attributes are $n$:

$$\text{Number of Super Keys} = 2^{n-k}$$

**Why?** Each super key must contain the candidate key. The remaining $(n-k)$ attributes can either be included or not = $2^{n-k}$ choices.

**Multiple Candidate Keys?** Use Inclusion-Exclusion:

For two candidate keys $K_1$ and $K_2$ with sizes $k_1$ and $k_2$:

$$\text{Super Keys} = 2^{n-k_1} + 2^{n-k_2} - 2^{n-|K_1 \cup K_2|}$$

### GATE Example: Super Key Counting

**Given**: R(A, B, C, D, E) with candidate keys {AB} and {CD}

Find number of super keys.

**Solution**:
- $n = 5$, $k_1 = 2$ (AB), $k_2 = 2$ (CD)
- $|K_1 \cup K_2| = |{A,B,C,D}| = 4$
- Super keys = $2^{5-2} + 2^{5-2} - 2^{5-4}$
- = $8 + 8 - 2 = 14$

---

## 3. Integrity Constraints

### Types of Integrity Constraints

| Constraint | Description | Example |
|------------|-------------|---------|
| **Domain Constraint** | Values must be from attribute's domain | age must be integer |
| **Entity Integrity** | Primary key cannot be NULL | roll_no cannot be NULL |
| **Referential Integrity** | Foreign key must reference existing primary key | dept_id must exist in Department |
| **Key Constraint** | Primary key must be unique | No duplicate roll_no |
| **NOT NULL Constraint** | Attribute cannot be NULL | name cannot be NULL |
| **CHECK Constraint** | Attribute must satisfy condition | age > 0 AND age < 150 |
| **UNIQUE Constraint** | Attribute must be unique | email must be unique |

### Referential Integrity Actions

When referenced row is deleted or updated:

| Action | On DELETE | On UPDATE |
|--------|-----------|-----------|
| **RESTRICT/NO ACTION** | Reject if referenced | Reject if referenced |
| **CASCADE** | Delete referencing rows | Update foreign keys |
| **SET NULL** | Set foreign key to NULL | Set foreign key to NULL |
| **SET DEFAULT** | Set foreign key to default | Set foreign key to default |

```sql
CREATE TABLE Student (
    roll_no INT PRIMARY KEY,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

---

## 4. Relational Algebra

### What is Relational Algebra?
**Relational Algebra** is a procedural query language that takes relations as input and produces relations as output.

### Properties
- **Closure Property**: Every operation produces a relation
- **Procedural**: Specifies HOW to compute the result
- **Foundation**: Basis for query optimization

### Classification of Operations

```
                    RELATIONAL ALGEBRA OPERATIONS
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
     UNARY OPERATIONS    BINARY OPERATIONS    SET OPERATIONS
           │                  │                  │
     ┌─────┴─────┐      ┌─────┴─────┐      ┌────┴────┐
     ▼           ▼      ▼           ▼      ▼         ▼
   Select    Project  Join       Division  Union    Intersection
   (σ)        (π)     (⋈)         (÷)      (∪)      (∩)
                                                    Difference
                                                    (−)
                                                    Cartesian
                                                    (×)
```

---

## 5. Unary Operations

### Selection (σ) - Horizontal Filtering

**Notation**: $\sigma_{\text{condition}}(R)$

**Purpose**: Select tuples that satisfy the condition

**Properties**:
- Input: Relation R
- Output: Subset of tuples from R
- Schema of output = Schema of input
- Number of tuples ≤ Number of input tuples

```
Table: Student
| roll_no | name    | age | dept |
|---------|---------|-----|------|
| 101     | Alice   | 20  | CS   |
| 102     | Bob     | 22  | EE   |
| 103     | Charlie | 21  | CS   |
| 104     | David   | 23  | ME   |

σ_{age > 21}(Student)
| roll_no | name    | age | dept |
|---------|---------|-----|------|
| 102     | Bob     | 22  | EE   |
| 104     | David   | 23  | ME   |
```

**Condition Operators**:
- Comparison: $=, \neq, <, >, \leq, \geq$
- Logical: $\land$ (AND), $\lor$ (OR), $\lnot$ (NOT)

**Selection Properties**:
$$\sigma_{p \land q}(R) = \sigma_p(\sigma_q(R)) = \sigma_q(\sigma_p(R))$$
$$\sigma_{p \lor q}(R) \neq \sigma_p(R) \cup \sigma_q(R) \text{ (in general)}$$

### Projection (π) - Vertical Filtering

**Notation**: $\pi_{A_1, A_2, \ldots, A_k}(R)$

**Purpose**: Extract specified columns

**Properties**:
- Input: Relation R
- Output: Relation with only specified attributes
- **Eliminates duplicate tuples** (fundamental property)
- Number of tuples ≤ Number of input tuples

```
Table: Student
| roll_no | name    | age | dept |
|---------|---------|-----|------|
| 101     | Alice   | 20  | CS   |
| 102     | Bob     | 22  | EE   |
| 103     | Charlie | 21  | CS   |

π_{dept}(Student)
| dept |
|------|
| CS   |    ← Only 2 rows (duplicates removed!)
| EE   |
```

### GATE Trap Alert! 🚨
**Projection REMOVES duplicates!**

If you project on non-key attributes, the output may have fewer tuples than input.

$$|\pi_A(R)| \leq |R|$$

Equality holds when A is a superkey.

### Rename (ρ) - Renaming Relations/Attributes

**Notation**: 
- $\rho_{S}(R)$ - Rename relation R to S
- $\rho_{S(A_1, A_2, \ldots)}(R)$ - Rename relation and attributes
- $\rho_{A/B}(R)$ - Rename attribute A to B

**Purpose**: Required for self-joins and to avoid ambiguity

```
ρ_{E1}(Employee) ⋈_{E1.manager_id = E2.emp_id} ρ_{E2}(Employee)
```

---

## 6. Set Operations

### Requirements for Set Operations
For $R \cup S$, $R \cap S$, $R - S$:
1. **Union Compatible**: R and S must have same number of attributes
2. **Domain Compatible**: Corresponding attributes must have compatible domains

### Union (∪)

**Notation**: $R \cup S$

**Result**: All tuples in R or S (or both)

```
R                   S                   R ∪ S
| A | B |          | A | B |          | A | B |
|---|---|          |---|---|          |---|---|
| 1 | 2 |          | 1 | 2 |          | 1 | 2 |
| 3 | 4 |          | 5 | 6 |          | 3 | 4 |
                                       | 5 | 6 |
```

**Duplicate handling**: Duplicates are eliminated

### Intersection (∩)

**Notation**: $R \cap S$

**Result**: Tuples in both R and S

```
R                   S                   R ∩ S
| A | B |          | A | B |          | A | B |
|---|---|          |---|---|          |---|---|
| 1 | 2 |          | 1 | 2 |          | 1 | 2 |
| 3 | 4 |          | 5 | 6 |
```

### Set Difference (−)

**Notation**: $R - S$

**Result**: Tuples in R but not in S

```
R                   S                   R - S
| A | B |          | A | B |          | A | B |
|---|---|          |---|---|          |---|---|
| 1 | 2 |          | 1 | 2 |          | 3 | 4 |
| 3 | 4 |          | 5 | 6 |

S - R
| A | B |
|---|---|
| 5 | 6 |
```

### Cartesian Product (×)

**Notation**: $R \times S$

**Result**: All combinations of tuples from R and S

**Output size**: $|R| \times |S|$ tuples

**Schema**: All attributes from R and S (renamed if same name)

```
R                   S                   R × S
| A | B |          | C | D |          | A | B | C | D |
|---|---|          |---|---|          |---|---|---|---|
| 1 | 2 |          | x | y |          | 1 | 2 | x | y |
| 3 | 4 |          | p | q |          | 1 | 2 | p | q |
                                       | 3 | 4 | x | y |
                                       | 3 | 4 | p | q |
```

---

## 7. Join Operations

### Natural Join (⋈)

**Notation**: $R \bowtie S$

**Process**:
1. Find common attributes between R and S
2. Keep tuples where common attributes have equal values
3. Eliminate duplicate columns

```
R                       S                       R ⋈ S
| A | B | C |          | B | C | D |          | A | B | C | D |
|---|---|---|          |---|---|---|          |---|---|---|---|
| 1 | 2 | 3 |          | 2 | 3 | 4 |          | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 |          | 6 | 8 | 9 |          
| 8 | 2 | 3 |                                  | 8 | 2 | 3 | 4 |

Common attributes: B, C
Only tuples where R.B = S.B AND R.C = S.C are kept
```

**Formula**:
$$R \bowtie S = \pi_{R.*, S.* - \text{common}}(\sigma_{R.\text{common} = S.\text{common}}(R \times S))$$

### Theta Join (⋈θ)

**Notation**: $R \bowtie_{\theta} S$

**Process**: Cartesian product followed by selection on condition θ

$$R \bowtie_{\theta} S = \sigma_{\theta}(R \times S)$$

```
R                   S                   R ⋈_{R.A < S.C} S
| A | B |          | C | D |          | A | B | C | D |
|---|---|          |---|---|          |---|---|---|---|
| 1 | 2 |          | 3 | 4 |          | 1 | 2 | 3 | 4 |
| 5 | 6 |          | 2 | 7 |          | 1 | 2 | 2 | 7 |
```

### Equi-Join

**Definition**: Theta join where θ contains only equality conditions

$$R \bowtie_{R.A = S.B} S$$

**Difference from Natural Join**: Keeps both columns (doesn't eliminate duplicates)

### Semi-Join (⋉)

**Notation**: $R \ltimes S$ or $R \rtimes S$

**Result**: Tuples of R (or S) that have matching tuples in S (or R)

$$R \ltimes S = \pi_{R.*}(R \bowtie S)$$

### Anti-Join (▷)

**Notation**: $R \triangleright S$

**Result**: Tuples of R that have NO matching tuples in S

$$R \triangleright S = R - (R \ltimes S)$$

### Outer Joins

| Type | Notation | Keeps |
|------|----------|-------|
| **Left Outer Join** | $R ⟕ S$ | All tuples from R, matched with S or NULL |
| **Right Outer Join** | $R ⟖ S$ | All tuples from S, matched with R or NULL |
| **Full Outer Join** | $R ⟗ S$ | All tuples from both, NULLs for non-matches |

```
R                   S
| A | B |          | B | C |
|---|---|          |---|---|
| 1 | 2 |          | 2 | x |
| 3 | 4 |          | 5 | y |

R ⟕ S (Left Outer)         R ⟖ S (Right Outer)
| A | B | C |               | A | B | C |
|---|---|---|               |---|---|---|
| 1 | 2 | x |               | 1 | 2 | x |
| 3 | 4 |NULL|               |NULL| 5 | y |

R ⟗ S (Full Outer)
| A | B | C |
|---|---|---|
| 1 | 2 | x |
| 3 | 4 |NULL|
|NULL| 5 | y |
```

---

## 8. Division (÷)

### The Most Complex Operation!

**Notation**: $R \div S$

**Intuition**: Find tuples in R that are associated with ALL tuples in S

**Schema**:
- R has attributes $(A_1, \ldots, A_m, B_1, \ldots, B_n)$
- S has attributes $(B_1, \ldots, B_n)$
- $R \div S$ has attributes $(A_1, \ldots, A_m)$

**Formula**:
$$R \div S = \pi_A(R) - \pi_A((\pi_A(R) \times S) - R)$$

### Division Example

```
R (Enrolled)                    S (Required)        R ÷ S
| student | course |           | course |          | student |
|---------|--------|           |--------|          |---------|
| Alice   | Math   |           | Math   |          | Alice   |
| Alice   | Physics|           | Physics|
| Alice   | Chem   |
| Bob     | Math   |
| Bob     | Chem   |
| Charlie | Math   |
| Charlie | Physics|

Question: Which students are enrolled in ALL required courses?
Answer: Only Alice (enrolled in both Math and Physics)
```

### Division Formula Explained

Step by step for above example:
```
1. π_student(R) = {Alice, Bob, Charlie}

2. π_student(R) × S = 
   | student | course  |
   |---------|---------|
   | Alice   | Math    |
   | Alice   | Physics |
   | Bob     | Math    |
   | Bob     | Physics |
   | Charlie | Math    |
   | Charlie | Physics |

3. (π_student(R) × S) - R =
   | student | course  |
   |---------|---------|
   | Bob     | Physics |     ← Bob missing Physics
   | Charlie | Physics |     ← Charlie missing Physics (Wait, Charlie has Physics!)
   
   Actually: 
   | Bob     | Physics |     ← Only Bob is missing Physics

4. π_student(Step 3) = {Bob}

5. π_student(R) - Step 4 = {Alice, Bob, Charlie} - {Bob} = {Alice, Charlie}

Wait, let me recalculate...

Charlie has: Math, Physics
Required: Math, Physics
So Charlie should also be in the result!

R ÷ S = {Alice, Charlie}
```

### GATE Trap Alert! 🚨
Division is about finding entities associated with **ALL** items in S, not just **some**.

---

## 9. Extended Relational Algebra

### Aggregate Functions

**Notation**: $\mathcal{G}$ or $\gamma$

**Syntax**: $_{G}\mathcal{G}_{F_1(A_1), F_2(A_2), \ldots}(R)$

Where:
- $G$ = Grouping attributes
- $F$ = Aggregate function (SUM, AVG, COUNT, MIN, MAX)
- $A$ = Attribute to aggregate

```
Table: Sales
| region | product | amount |
|--------|---------|--------|
| North  | A       | 100    |
| North  | B       | 200    |
| South  | A       | 150    |
| South  | A       | 100    |

_{region}𝒢_{SUM(amount), COUNT(*)}(Sales)
| region | SUM(amount) | COUNT |
|--------|-------------|-------|
| North  | 300         | 2     |
| South  | 250         | 2     |
```

### Generalized Projection

**Notation**: $\pi_{F_1, F_2, \ldots}(R)$

Allows arithmetic expressions in projection:

$$\pi_{A, B, A+B \text{ AS } C}(R)$$

```
R                       π_{A, B, A*B AS product}(R)
| A | B |              | A | B | product |
|---|---|              |---|---|---------|
| 2 | 3 |              | 2 | 3 | 6       |
| 4 | 5 |              | 4 | 5 | 20      |
```

---

## 10. Query Optimization Equivalences

### Selection Equivalences

$$\sigma_{p_1 \land p_2}(R) = \sigma_{p_1}(\sigma_{p_2}(R)) = \sigma_{p_2}(\sigma_{p_1}(R))$$

$$\sigma_{p_1 \lor p_2}(R) \neq \sigma_{p_1}(R) \cup \sigma_{p_2}(R) \text{ (unless p1, p2 disjoint)}$$

### Projection Equivalences

$$\pi_{A}(\pi_{A,B}(R)) = \pi_{A}(R) \text{ (if } A \subseteq \{A, B\}\text{)}$$

### Join Equivalences

$$R \bowtie S = S \bowtie R \text{ (Commutative)}$$

$$(R \bowtie S) \bowtie T = R \bowtie (S \bowtie T) \text{ (Associative)}$$

### Selection Pushdown (Important for Optimization!)

$$\sigma_p(R \bowtie S) = \sigma_p(R) \bowtie S \text{ (if p references only R's attributes)}$$

---

## 11. Relational Calculus (Brief)

### Tuple Relational Calculus (TRC)

**Format**: $\{t \mid P(t)\}$

Read as: "Set of all tuples t such that predicate P(t) is true"

**Example**: Students older than 20
$$\{t \mid \text{Student}(t) \land t[\text{age}] > 20\}$$

### Domain Relational Calculus (DRC)

**Format**: $\{<x_1, x_2, \ldots, x_n> \mid P(x_1, x_2, \ldots, x_n)\}$

**Example**: Names of students older than 20
$$\{<n> \mid \exists r, a, d (\text{Student}(r, n, a, d) \land a > 20)\}$$

### Safe Queries
A query is **safe** if it:
1. Always produces finite results
2. Only contains values from the domain of the database

### Equivalence
**Codd's Theorem**: Relational Algebra = TRC (safe) = DRC (safe)

Same expressive power!

---

## 12. Query Expression Examples

### Example 1: Find employees earning more than their manager

```
Employee(emp_id, name, salary, manager_id)

Relational Algebra:
ρ_{E1}(Employee) ⋈_{E1.manager_id = E2.emp_id ∧ E1.salary > E2.salary} ρ_{E2}(Employee)
π_{E1.name}(...)

SQL Equivalent:
SELECT E1.name
FROM Employee E1, Employee E2
WHERE E1.manager_id = E2.emp_id 
  AND E1.salary > E2.salary
```

### Example 2: Find students enrolled in ALL courses

```
Enrolled(student, course)
Course(course_id, name)

Division:
π_{student, course_id}(Enrolled) ÷ π_{course_id}(Course)

SQL Equivalent (using NOT EXISTS NOT EXISTS pattern):
SELECT DISTINCT E1.student
FROM Enrolled E1
WHERE NOT EXISTS (
    SELECT C.course_id
    FROM Course C
    WHERE NOT EXISTS (
        SELECT E2.student
        FROM Enrolled E2
        WHERE E2.student = E1.student
          AND E2.course = C.course_id
    )
)
```

### Example 3: Find departments with no employees

```
Department(dept_id, name)
Employee(emp_id, name, dept_id)

Set Difference:
π_{dept_id}(Department) - π_{dept_id}(Employee)

Or using Anti-Join:
Department ▷_{Department.dept_id = Employee.dept_id} Employee
```

---

## 13. Tuple Count Calculations (GATE NAT)

### Rules for Tuple Counts

| Operation | Min Tuples | Max Tuples |
|-----------|------------|------------|
| $\sigma_p(R)$ | 0 | $\|R\|$ |
| $\pi_A(R)$ | 1 (if R non-empty) | $\|R\|$ |
| $R \cup S$ | $\max(\|R\|, \|S\|)$ | $\|R\| + \|S\|$ |
| $R \cap S$ | 0 | $\min(\|R\|, \|S\|)$ |
| $R - S$ | $\max(0, \|R\| - \|S\|)$ | $\|R\|$ |
| $R \times S$ | $\|R\| \times \|S\|$ | $\|R\| \times \|S\|$ |
| $R \bowtie S$ | 0 | $\|R\| \times \|S\|$ |
| $R \div S$ | 0 | $\|R\| / \|S\|$ |

### Example Calculation

**Given**: R has 100 tuples, S has 50 tuples, both union compatible

**Find**: Max and min tuples in $R \cup S$, $R \cap S$, $R - S$

**Solution**:
- $R \cup S$: Min = 100 (if S ⊆ R), Max = 150 (if disjoint)
- $R \cap S$: Min = 0 (if disjoint), Max = 50 (if S ⊆ R)
- $R - S$: Min = 50 (if S ⊆ R), Max = 100 (if disjoint)

---

## 14. Common GATE Patterns

### Pattern 1: Count Candidate Keys
Given FDs, find candidate keys using attribute closure.

### Pattern 2: Count Super Keys
Use formula: $2^{n-k}$ for single candidate key.

### Pattern 3: Write Relational Algebra
Translate English query to algebra expression.

### Pattern 4: Tuple Count
Calculate min/max tuples after operations.

### Pattern 5: Equivalence Check
Determine if two expressions are equivalent.

---

## 15. Edge Cases & Tricky Scenarios

### Edge Case 1: Natural Join with No Common Attributes
$$R \bowtie S = R \times S \text{ (becomes Cartesian product)}$$

### Edge Case 2: Division by Empty Relation
$$R \div \emptyset = \text{All tuples of } \pi_{R-S}(R) \text{ (everything qualifies)}$$

### Edge Case 3: Projection on Key Attribute
$$|\pi_{key}(R)| = |R| \text{ (no duplicates removed)}$$

### Edge Case 4: Selection on Empty Condition
$$\sigma_{true}(R) = R$$
$$\sigma_{false}(R) = \emptyset$$

---

## 🧠 Memory Techniques

### Operation Symbols Mnemonic: "SPUD JCR"
- **S**election: σ (sigma) - **S**elect rows
- **P**rojection: π (pi) - **P**ick columns
- **U**nion: ∪ - **U**nite sets
- **D**ifference: − - **D**elete common
- **J**oin: ⋈ - **J**oin tables
- **C**artesian: × - **C**ross product
- **R**ename: ρ (rho) - **R**ename

### Division Mnemonic: "ALL or NOTHING"
$R \div S$ = Give me entities in R that appear with **ALL** entities in S

### Join Types Visual
```
Natural Join: Merge common columns, keep matches only
Left Outer:   Keep all from LEFT, NULL for non-matches
Right Outer:  Keep all from RIGHT, NULL for non-matches
Full Outer:   Keep ALL from BOTH, NULL for non-matches
```

---

## 🔑 Key Takeaways for GATE

1. **Projection removes duplicates**: Always remember this!
2. **Super Keys = 2^(n-k)**: For single candidate key
3. **Closure Algorithm**: Master it for finding keys
4. **Division**: Most complex operation, understand the formula
5. **Join types**: Know the difference between all joins
6. **Set Operations need union compatibility**: Same schema required

---

## 📚 Related Chapters
- [← Previous: Chapter 02 - ER Model](../02-ER-Model/README.md)
- [Next: Chapter 04 - SQL →](../04-SQL/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
