# Chapter 4: Relational Algebra & Relational Calculus

---

## 🎯 What is Relational Algebra?

**Relational Algebra** is a **procedural** query language that:
- Specifies **HOW** to get the result
- Uses operators on relations
- Produces relations as output (closure property)

### 🔑 Key Insight
> Think of it as **assembly language** for databases — you specify step-by-step operations.

---

## 📊 Types of Operations

```
                  Relational Algebra Operations
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
      Unary               Binary              Extended
          │                   │                   │
    ┌─────┴─────┐     ┌───────┴───────┐     ┌────┴────┐
    │           │     │               │     │         │
 Select(σ)  Project(π)  Union(∪)   Join(⋈)  Aggregate  Division
 Rename(ρ)          Intersect(∩)   × (Cross)  Group by
                    Difference(−)
```

---

## 🔍 SELECT Operation (σ)

### Syntax
```
σ_condition(Relation)
```

### Purpose
Filter **rows** based on a condition (horizontal subset).

### Example
```
Student:
┌──────┬────────┬──────┬──────┐
│ Roll │  Name  │ Dept │ CGPA │
├──────┼────────┼──────┼──────┤
│  1   │ Alice  │  CS  │ 9.2  │
│  2   │ Bob    │  EE  │ 8.5  │
│  3   │ Carol  │  CS  │ 9.0  │
│  4   │ Dave   │  ME  │ 7.5  │
└──────┴────────┴──────┴──────┘

σ_Dept='CS'(Student):
┌──────┬────────┬──────┬──────┐
│ Roll │  Name  │ Dept │ CGPA │
├──────┼────────┼──────┼──────┤
│  1   │ Alice  │  CS  │ 9.2  │
│  3   │ Carol  │  CS  │ 9.0  │
└──────┴────────┴──────┴──────┘
```

### Complex Conditions
```
σ_Dept='CS' ∧ CGPA>9.0(Student)  -- AND
σ_Dept='CS' ∨ CGPA>9.0(Student)  -- OR
σ_¬(Dept='CS')(Student)          -- NOT
```

### Properties
- **Commutative**: σ_p(σ_q(R)) = σ_q(σ_p(R))
- **Cascading**: σ_p∧q(R) = σ_p(σ_q(R))
- **Degree**: Same as input
- **Cardinality**: ≤ Input (removes rows)

---

## 📋 PROJECT Operation (π)

### Syntax
```
π_attribute_list(Relation)
```

### Purpose
Select **columns** (vertical subset) and remove duplicates.

### Example
```
Student:
┌──────┬────────┬──────┬──────┐
│ Roll │  Name  │ Dept │ CGPA │
├──────┼────────┼──────┼──────┤
│  1   │ Alice  │  CS  │ 9.2  │
│  2   │ Bob    │  EE  │ 8.5  │
│  3   │ Carol  │  CS  │ 9.0  │
└──────┴────────┴──────┴──────┘

π_Name,Dept(Student):
┌────────┬──────┐
│  Name  │ Dept │
├────────┼──────┤
│ Alice  │  CS  │
│ Bob    │  EE  │
│ Carol  │  CS  │
└────────┴──────┘

π_Dept(Student):      ← Duplicates removed!
┌──────┐
│ Dept │
├──────┤
│  CS  │
│  EE  │
└──────┘
```

### Properties
- **NOT Commutative**: π_a(π_b(R)) ≠ π_b(π_a(R)) in general
- **Degree**: ≤ Input (selects columns)
- **Cardinality**: ≤ Input (removes duplicates)

### ⚠️ GATE Trap
```
π removes duplicates by default in Relational Algebra!
(SQL SELECT does NOT remove duplicates unless DISTINCT)
```

---

## 🏷️ RENAME Operation (ρ)

### Syntax
```
ρ_new_name(Relation)                    -- Rename relation
ρ_new_name(A1,A2,...)(Relation)         -- Rename relation and attributes
ρ_(A1,A2,...)(Relation)                 -- Rename only attributes
```

### Purpose
Rename relation and/or attributes.

### Example
```
ρ_S(Roll→ID, Name→StudentName)(Student):

Before: Student(Roll, Name, Dept, CGPA)
After:  S(ID, StudentName, Dept, CGPA)
```

### Use Case: Self-Join
```
-- Find pairs of students in same department
-- Need two copies of Student table

ρ_S1(Student) × ρ_S2(Student)
σ_S1.Dept=S2.Dept ∧ S1.Roll<S2.Roll(ρ_S1(Student) × ρ_S2(Student))
```

---

## ∪ UNION Operation

### Syntax
```
R ∪ S
```

### Prerequisites (Union Compatibility)
1. Same number of attributes (degree)
2. Corresponding attributes have same domain

### Example
```
CS_Students:              EE_Students:
┌──────┬────────┐         ┌──────┬────────┐
│ Roll │  Name  │         │ Roll │  Name  │
├──────┼────────┤         ├──────┼────────┤
│  1   │ Alice  │         │  2   │ Bob    │
│  3   │ Carol  │         │  5   │ Eve    │
└──────┴────────┘         └──────┴────────┘

CS_Students ∪ EE_Students:
┌──────┬────────┐
│ Roll │  Name  │
├──────┼────────┤
│  1   │ Alice  │
│  2   │ Bob    │
│  3   │ Carol  │
│  5   │ Eve    │
└──────┴────────┘
```

### Properties
- **Commutative**: R ∪ S = S ∪ R
- **Associative**: (R ∪ S) ∪ T = R ∪ (S ∪ T)
- **Removes duplicates**

---

## ∩ INTERSECTION Operation

### Syntax
```
R ∩ S
```

### Example
```
Freshers:                 TopScorers:
┌──────┬────────┐         ┌──────┬────────┐
│ Roll │  Name  │         │ Roll │  Name  │
├──────┼────────┤         ├──────┼────────┤
│  1   │ Alice  │         │  1   │ Alice  │
│  2   │ Bob    │         │  3   │ Carol  │
│  3   │ Carol  │         │  5   │ Eve    │
└──────┴────────┘         └──────┴────────┘

Freshers ∩ TopScorers:
┌──────┬────────┐
│ Roll │  Name  │
├──────┼────────┤
│  1   │ Alice  │
│  3   │ Carol  │
└──────┴────────┘
```

### Can be Derived
```
R ∩ S = R - (R - S)
      = S - (S - R)
```

### Properties
- **Commutative**: R ∩ S = S ∩ R
- **Associative**: (R ∩ S) ∩ T = R ∩ (S ∩ T)

---

## − SET DIFFERENCE Operation

### Syntax
```
R - S
```

### Example
```
AllStudents:              Graduates:
┌──────┬────────┐         ┌──────┬────────┐
│ Roll │  Name  │         │ Roll │  Name  │
├──────┼────────┤         ├──────┼────────┤
│  1   │ Alice  │         │  1   │ Alice  │
│  2   │ Bob    │         │  3   │ Carol  │
│  3   │ Carol  │         
└──────┴────────┘         └──────┴────────┘

AllStudents - Graduates (Current students):
┌──────┬────────┐
│ Roll │  Name  │
├──────┼────────┤
│  2   │ Bob    │
└──────┴────────┘
```

### Properties
- **NOT Commutative**: R - S ≠ S - R
- **NOT Associative**: (R - S) - T ≠ R - (S - T)

---

## × CARTESIAN PRODUCT

### Syntax
```
R × S
```

### Purpose
Every tuple in R paired with every tuple in S.

### Example
```
A:                  B:
┌─────┬─────┐      ┌─────┬─────┐
│  X  │  Y  │      │  P  │  Q  │
├─────┼─────┤      ├─────┼─────┤
│  1  │  a  │      │ 10  │  x  │
│  2  │  b  │      │ 20  │  y  │
└─────┴─────┘      └─────┴─────┘

A × B:
┌─────┬─────┬─────┬─────┐
│  X  │  Y  │  P  │  Q  │
├─────┼─────┼─────┼─────┤
│  1  │  a  │ 10  │  x  │
│  1  │  a  │ 20  │  y  │
│  2  │  b  │ 10  │  x  │
│  2  │  b  │ 20  │  y  │
└─────┴─────┴─────┴─────┘
```

### Properties
- **Degree**: deg(R) + deg(S)
- **Cardinality**: |R| × |S|
- **Commutative**: R × S = S × R (in terms of information, not column order)
- **Associative**: (R × S) × T = R × (S × T)

### 🧠 Memory Formula
```
|R × S| = |R| × |S|
degree(R × S) = degree(R) + degree(S)
```

---

## ⋈ JOIN Operations

### 1. Theta Join (θ-Join)
```
R ⋈_θ S = σ_θ(R × S)
```
Cartesian product followed by selection on condition θ.

### 2. Equi-Join
Theta join where θ contains only **equality** comparisons.

```
R ⋈_R.A=S.B S

Employee:                Department:
┌────┬────────┬────────┐ ┌────────┬─────────┐
│ ID │  Name  │ DeptID │ │ DeptID │  DName  │
├────┼────────┼────────┤ ├────────┼─────────┤
│ 1  │ Alice  │   10   │ │   10   │   CS    │
│ 2  │ Bob    │   20   │ │   20   │   EE    │
│ 3  │ Carol  │   10   │ │   30   │   ME    │
└────┴────────┴────────┘ └────────┴─────────┘

Employee ⋈_Employee.DeptID=Department.DeptID Department:
┌────┬────────┬────────┬────────┬─────────┐
│ ID │  Name  │ DeptID │ DeptID │  DName  │
├────┼────────┼────────┼────────┼─────────┤
│ 1  │ Alice  │   10   │   10   │   CS    │
│ 2  │ Bob    │   20   │   20   │   EE    │
│ 3  │ Carol  │   10   │   10   │   CS    │
└────┴────────┴────────┴────────┴─────────┘
Note: DeptID appears twice (redundant)
```

### 3. Natural Join (⋈)
Equi-join on **all common attributes** + remove duplicate columns.

```
Employee ⋈ Department:  (join on common attribute DeptID)
┌────┬────────┬────────┬─────────┐
│ ID │  Name  │ DeptID │  DName  │
├────┼────────┼────────┼─────────┤
│ 1  │ Alice  │   10   │   CS    │
│ 2  │ Bob    │   20   │   EE    │
│ 3  │ Carol  │   10   │   CS    │
└────┴────────┴────────┴─────────┘
Note: Only one DeptID column
```

### Natural Join Properties
- If no common attributes: Natural Join = Cartesian Product
- If all attributes common: Natural Join = Intersection

### 4. Left Outer Join (⟕)
Keep all tuples from **left** relation; NULL for non-matching right.

```
Employee ⟕ Department:
┌────┬────────┬────────┬─────────┐
│ ID │  Name  │ DeptID │  DName  │
├────┼────────┼────────┼─────────┤
│ 1  │ Alice  │   10   │   CS    │
│ 2  │ Bob    │   20   │   EE    │
│ 3  │ Carol  │   10   │   CS    │
│ 4  │ Dave   │   40   │  NULL   │ ← No matching dept
└────┴────────┴────────┴─────────┘
```

### 5. Right Outer Join (⟖)
Keep all tuples from **right** relation; NULL for non-matching left.

### 6. Full Outer Join (⟗)
Keep all tuples from **both**; NULL for non-matches on either side.

```
Employee ⟗ Department:
┌────┬────────┬────────┬─────────┐
│ ID │  Name  │ DeptID │  DName  │
├────┼────────┼────────┼─────────┤
│ 1  │ Alice  │   10   │   CS    │
│ 2  │ Bob    │   20   │   EE    │
│ 3  │ Carol  │   10   │   CS    │
│ 4  │ Dave   │   40   │  NULL   │
│NULL│  NULL  │   30   │   ME    │
└────┴────────┴────────┴─────────┘
```

---

## ➗ DIVISION Operation

### Syntax
```
R ÷ S
```

### Purpose
Find tuples in R associated with **ALL** tuples in S.

### 🎭 Analogy
> "Which students have taken **ALL** required courses?"

### Example
```
Takes(Student, Course):           Required(Course):
┌─────────┬────────┐              ┌────────┐
│ Student │ Course │              │ Course │
├─────────┼────────┤              ├────────┤
│  Alice  │  DBMS  │              │  DBMS  │
│  Alice  │   OS   │              │   OS   │
│  Alice  │   CN   │              └────────┘
│   Bob   │  DBMS  │
│   Bob   │   OS   │
│  Carol  │  DBMS  │
└─────────┴────────┘

Takes ÷ Required:
┌─────────┐
│ Student │
├─────────┤
│  Alice  │  ← Alice has both DBMS and OS
│   Bob   │  ← Bob has both DBMS and OS
└─────────┘
Carol doesn't appear (only has DBMS, not OS)
```

### Division Formula
```
R ÷ S = π_X(R) - π_X((π_X(R) × S) - R)

Where:
- X = attributes of R not in S
- π_X(R) = all possible values from R's unique attributes
- π_X(R) × S = all possible combinations
- (π_X(R) × S) - R = combinations that DON'T exist
- Final subtraction removes disqualified tuples
```

### 📊 Division Cardinality
If R has m tuples and S has n tuples:
- Minimum result: 0 (no one has all S values)
- Maximum result: m/n (if perfectly divided)

---

## 📊 Extended Relational Algebra

### 1. Aggregate Functions

| Function | Purpose |
|----------|---------|
| COUNT(*) | Count all tuples |
| COUNT(A) | Count non-NULL values of A |
| SUM(A) | Sum of attribute A |
| AVG(A) | Average of attribute A |
| MAX(A) | Maximum value of A |
| MIN(A) | Minimum value of A |

### Notation
```
ℱ_function_list(Relation)
```

### Example
```
ℱ_COUNT(*), AVG(CGPA)(Student)

Result: (4, 8.55)  -- 4 students, average CGPA 8.55
```

### 2. Grouping (𝒢 or γ)
```
_group_by_attributes ℱ_agg_functions(Relation)
```

### Example
```
_Dept ℱ_COUNT(*), AVG(CGPA)(Student)

Result:
┌──────┬─────────┬──────────┐
│ Dept │  COUNT  │ AVG_CGPA │
├──────┼─────────┼──────────┤
│  CS  │    2    │   9.1    │
│  EE  │    1    │   8.5    │
│  ME  │    1    │   7.5    │
└──────┴─────────┴──────────┘
```

---

## 🧮 Relational Calculus

### Two Types
1. **Tuple Relational Calculus (TRC)** - Variables represent tuples
2. **Domain Relational Calculus (DRC)** - Variables represent domain values

---

## 📝 Tuple Relational Calculus (TRC)

### Syntax
```
{ t | P(t) }
```
Where:
- t is a tuple variable
- P(t) is a formula (predicate)

### Example Queries

#### Query 1: Select all CS students
```
{ t | t ∈ Student ∧ t.Dept = 'CS' }
```

#### Query 2: Get names of CS students
```
{ t.Name | t ∈ Student ∧ t.Dept = 'CS' }
```

#### Query 3: Students with CGPA > 8
```
{ t | t ∈ Student ∧ t.CGPA > 8 }
```

### Quantifiers

| Symbol | Meaning | Usage |
|--------|---------|-------|
| ∃ | Existential (there exists) | ∃t(P(t)) |
| ∀ | Universal (for all) | ∀t(P(t)) |

### Example with Quantifiers

#### Query: Names of students who have taken at least one course
```
{ s.Name | s ∈ Student ∧ ∃e(e ∈ Enrollment ∧ e.Roll = s.Roll) }
```

#### Query: Students who have taken ALL courses
```
{ s | s ∈ Student ∧ ∀c(c ∈ Course → ∃e(e ∈ Enrollment ∧ 
      e.Roll = s.Roll ∧ e.CourseID = c.CourseID)) }
```

### Safe Queries
A query is **safe** if it produces a **finite** result.

#### Unsafe Example:
```
{ t | ¬(t ∈ Student) }
-- Returns all tuples NOT in Student → infinite!
```

---

## 📝 Domain Relational Calculus (DRC)

### Syntax
```
{ <x₁, x₂, ..., xₙ> | P(x₁, x₂, ..., xₙ) }
```
Variables represent domain values, not tuples.

### Example Queries

#### Query 1: Roll and Name of CS students
```
{ <r, n> | ∃d∃c(Student(r, n, d, c) ∧ d = 'CS') }
```

#### Query 2: All student names
```
{ <n> | ∃r∃d∃c(Student(r, n, d, c)) }
```

---

## ⚖️ Equivalence of Query Languages

```
┌───────────────────────────────────────────────┐
│                                               │
│    Relational     ≡     Tuple      ≡   Domain │
│    Algebra              Calculus       Calculus│
│                                               │
└───────────────────────────────────────────────┘
            (Expressively Equivalent)
```

### Codd's Theorem
> Any query expressible in safe TRC/DRC can be expressed in Relational Algebra and vice versa.

### What RA Cannot Express (Not Relationally Complete)
1. Transitive closure (recursive queries)
2. Some aggregate operations in basic RA

---

## 🔄 Converting Between Notations

### Relational Algebra to SQL

| RA Operation | SQL Equivalent |
|--------------|----------------|
| σ_condition(R) | SELECT * FROM R WHERE condition |
| π_A,B(R) | SELECT DISTINCT A, B FROM R |
| R ∪ S | SELECT * FROM R UNION SELECT * FROM S |
| R ∩ S | SELECT * FROM R INTERSECT SELECT * FROM S |
| R - S | SELECT * FROM R EXCEPT SELECT * FROM S |
| R × S | SELECT * FROM R, S |
| R ⋈ S | SELECT * FROM R NATURAL JOIN S |

### Example Conversion
```
RA: π_Name(σ_Dept='CS' ∧ CGPA>9.0(Student))

SQL:
SELECT DISTINCT Name
FROM Student
WHERE Dept = 'CS' AND CGPA > 9.0;

TRC: { t.Name | t ∈ Student ∧ t.Dept = 'CS' ∧ t.CGPA > 9.0 }
```

---

## 📊 Operation Properties Summary

| Operation | Commutative | Associative | Degree Change | Cardinality |
|-----------|-------------|-------------|---------------|-------------|
| σ (Select) | Yes | Yes | Same | ≤ Original |
| π (Project) | No | - | ≤ Original | ≤ Original |
| ∪ (Union) | Yes | Yes | Same | ≤ Sum |
| ∩ (Intersect) | Yes | Yes | Same | ≤ Min |
| − (Difference) | No | No | Same | ≤ First |
| × (Cross) | Yes | Yes | Sum | Product |
| ⋈ (Natural Join) | Yes | Yes | ≤ Sum | ≤ Product |

---

## ⚠️ Common GATE Traps

### Trap 1: Project Removes Duplicates
```
π_Dept(Student) with 100 students in 3 depts → Result has 3 rows
```

### Trap 2: Natural Join with No Common Attributes
```
R(A, B) ⋈ S(C, D) = R × S  (Cartesian product!)
```

### Trap 3: Division Result Size
```
R ÷ S where R has 10 tuples, S has 5 tuples
Result: Not necessarily 2! Could be 0 to any number.
```

### Trap 4: Outer Join NULL Handling
```
Left Outer Join: Right side gets NULL
Right Outer Join: Left side gets NULL
```

---

## 🧪 Practice Problems

### Q1: Expression Equivalence
> Is σ_A>5(σ_B<10(R)) = σ_B<10(σ_A>5(R))?

**Answer**: YES - Select is commutative.

### Q2: Natural Join Result
> R(A, B, C) has 5 tuples, S(C, D, E) has 4 tuples. 
> If all values of C in R match with all in S, max result tuples?

**Answer**: 5 × 4 = 20 (if every C matches every other C)
**Actually**: Max = 20 if C has 1 unique value in both.

### Q3: Division
> Students who have taken ALL courses offered by 'CS' department?

```
π_Roll,CourseID(Enrollment) ÷ π_CourseID(σ_Dept='CS'(Course))
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Select (σ)** | Filter rows, commutative |
| **Project (π)** | Select columns, removes duplicates |
| **Join (⋈)** | Natural removes duplicates, Theta keeps all columns |
| **Division (÷)** | "For all" queries |
| **TRC** | { t \| P(t) } - tuple variables |
| **DRC** | { <x,y> \| P(x,y) } - domain variables |
| **Equivalence** | RA ≡ TRC ≡ DRC (Codd's Theorem) |

---

## 🎓 Quick Revision Points

1. ✅ σ is commutative and cascading
2. ✅ π removes duplicates (unlike SQL SELECT)
3. ✅ Natural join on no common attrs = Cross product
4. ✅ Division = "for all" semantics
5. ✅ RA ≡ Safe TRC ≡ Safe DRC
6. ✅ ∃ = at least one, ∀ = every
7. ✅ Unsafe queries → infinite results

---

*Previous: [Relational Model](./03-Relational-Model.md) | Next: [SQL Complete Guide](./05-SQL-Complete-Guide.md)*
