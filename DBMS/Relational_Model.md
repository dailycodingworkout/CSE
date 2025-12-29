# 🎯 Relational Model - Complete GATE & ESE Teaching Notes

> **Master the Concepts** - Deep understanding through intuition, examples, and first-principles thinking.

---

## 📚 Table of Contents

1. [Introduction & Foundations](#1-introduction--foundations)
2. [Relation Schema & Instance](#2-relation-schema--instance)
3. [Keys - The Heart of Relational Model](#3-keys---the-heart-of-relational-model)
4. [Integrity Constraints](#4-integrity-constraints)
5. [Relational Algebra](#5-relational-algebra)
6. [Tuple Relational Calculus (TRC)](#6-tuple-relational-calculus-trc)
7. [Domain Relational Calculus (DRC)](#7-domain-relational-calculus-drc)
8. [Normalization](#8-normalization)
9. [Functional Dependencies](#9-functional-dependencies)
10. [Decomposition](#10-decomposition)
11. [GATE PYQ Patterns & Tricks](#11-gate-pyq-patterns--tricks)

---

## 1. Introduction & Foundations

### 💡 What is the Relational Model and Why Does It Exist?

**The Problem Before Relational Model:**

In the 1960s, databases were a mess. We had hierarchical models (data stored like folder trees) and network models (data connected like a spider web). Both had serious issues:
- Programmers needed to know EXACTLY how data was physically stored
- Changing the storage structure meant rewriting all programs
- Queries were procedural nightmares - you had to tell the computer HOW to find data step by step

**The Breakthrough:**

In 1970, E.F. Codd at IBM asked a brilliant question: *"What if we separated the logical structure of data from its physical storage?"*

His answer was the **Relational Model** - data organized into simple **tables** (relations) based on mathematical set theory. This was revolutionary because:

1. **Data Independence**: Change how data is stored without changing programs
2. **Declarative Queries**: Tell the database WHAT you want, not HOW to get it
3. **Mathematical Foundation**: Operations are well-defined and predictable

**Think of it this way:** Before Codd, using a database was like giving someone turn-by-turn directions. After Codd, it's like giving them a destination and letting GPS figure out the route.

### 🔑 Core Terminology - Understanding Each Term Deeply

| Term | Formal Meaning | Intuitive Understanding | Why It Matters |
|------|----------------|------------------------|----------------|
| **Relation** | A 2D table | Think of an Excel sheet with named columns | This is your fundamental data container |
| **Tuple** | A row (an ordered list of values) | One complete record - e.g., one student's info | Each tuple represents one "thing" you're tracking |
| **Attribute** | A column header | A property every tuple has - e.g., "Age" | Defines what information you store |
| **Domain** | Set of allowed values | Like a data type + validation - e.g., Age: integers 0-150 | Prevents garbage data from entering |
| **Degree** | Count of attributes | How many columns? | Tells you the "width" of your table |
| **Cardinality** | Count of tuples | How many rows? | Tells you the "height" - how much data |
| **Schema** | Structure definition | The blueprint: column names and their types | Stays stable while data changes |
| **Instance** | The actual data | A snapshot of all rows at this moment | Changes constantly with INSERT/UPDATE/DELETE |

### 🎓 Why is a Relation a "SET" of Tuples?

This is crucial to understand. In mathematics, a **set** has two properties:
1. **No duplicates** - Each element appears exactly once
2. **No ordering** - {A, B, C} = {C, A, B}

**Why does this matter for databases?**

**No Duplicates**: If you could have identical rows, how would you refer to a specific one? "Get me the row that's exactly like this other row but is different" makes no sense. The no-duplicates rule forces uniqueness.

**No Ordering**: If row order mattered, you'd need to track positions. But what happens when you insert a row in the middle? All positions after it change! By ignoring order, we make insertions and deletions simpler.

**Edge Case to Remember**: In practice, SQL allows duplicate rows (tables, not true relations). This is a deviation from pure relational theory that causes real problems - another reason to understand keys deeply.

### 🧠 The Maximum Tuples Question - Why m^n?

> **Q**: Max tuples in a relation with `n` attributes where each attribute's domain has `m` values?

**Let's reason through this:**

Imagine a table with 2 attributes:
- **Color**: {Red, Blue} → 2 values
- **Size**: {Small, Medium, Large} → 3 values

How many possible UNIQUE rows can exist?
```
(Red, Small), (Red, Medium), (Red, Large),
(Blue, Small), (Blue, Medium), (Blue, Large)
```
That's 2 × 3 = 6 rows. This is the **Cartesian product** of the domains.

**General Formula**: With n attributes, each having m values:
- Attribute 1: m choices
- Attribute 2: m choices
- ...
- Attribute n: m choices

Total combinations = m × m × ... × m (n times) = **m^n**

**GATE Trap**: This is the MAXIMUM. Actual tables usually have far fewer rows because:
1. Not all combinations make real-world sense
2. Business rules eliminate many combinations
3. We only store data we actually have

---

## 2. Relation Schema & Instance

### Understanding Schema vs Instance - The Blueprint Analogy

**Think of building a house:**
- The **architect's blueprint** defines rooms, dimensions, where doors go = **SCHEMA**
- The **actual house** with furniture, people, decorations = **INSTANCE**

You can have many houses built from the same blueprint. Similarly, a schema can have many instances over time (as data changes).

### Schema (Intension) - The Structure

```
R(A₁, A₂, ..., Aₙ)
```

**What it tells you:**
- Relation name (R)
- Attribute names (A₁, A₂, etc.)
- Domain of each attribute (implicit or explicit)

**Example**: `Student(Roll_No: INTEGER, Name: VARCHAR(50), Age: INTEGER, Department: VARCHAR(20))`

**Key Insight**: Schema changes are EXPENSIVE. Adding a column to a billion-row table is a major operation. This is why schema design matters so much.

### Instance (Extension) - The Actual Data

The set of tuples at any given point in time.

**Example Instance**:
| Roll_No | Name | Age | Department |
|---------|------|-----|------------|
| 101 | Alice | 20 | CS |
| 102 | Bob | 21 | EE |
| 103 | Carol | 19 | CS |

This instance has cardinality 3 and degree 4.

### 📐 The Mathematical Foundation - Why It Matters

```
If D₁, D₂, ..., Dₙ are domains of attributes A₁, A₂, ..., Aₙ
Then relation r ⊆ D₁ × D₂ × ... × Dₙ
```

**Breaking this down:**

D₁ × D₂ × ... × Dₙ is the Cartesian product - ALL possible combinations of values.

A relation r is a SUBSET of this. Why subset and not equal?
- Because not all combinations exist in reality
- We only store actual data, not every theoretical possibility

**Example:**
- D₁ (Roll_No) = {101, 102, 103, ...} (all possible IDs)
- D₂ (Department) = {CS, EE, ME, CE}

The Cartesian product includes (101, CS), (101, EE), (101, ME), ... but a student only belongs to ONE department. The actual relation is a small subset.

### 🎓 Why This Mathematical View Matters for GATE

GATE loves asking:
1. "What's the maximum number of tuples?" → Size of Cartesian product
2. "Is this a valid relation?" → Check if it's a subset of the Cartesian product
3. "What's the degree after operation X?" → Track how attributes change

---

## 3. Keys - The Heart of Relational Model

### 🔐 Why Do We Need Keys?

Imagine a classroom where everyone is called "Student." How do you call on a specific person? You can't! You need a way to uniquely identify each individual.

Keys solve the **identity problem** in databases:
- How do we refer to a specific tuple?
- How do we prevent duplicate entries?
- How do we link tables together?

### The Key Hierarchy - Building Up From First Principles

Let's build understanding step by step:

#### Step 1: Super Key - "Anything That Works"

**Definition**: Any set of attributes that can uniquely identify tuples.

**Intuition**: It's like asking "What information guarantees I'm talking about exactly one person?"

For a Student table:
- {Roll_No} → Works! Each student has unique roll number
- {Roll_No, Name} → Also works! (Adding more info doesn't hurt uniqueness)
- {Roll_No, Name, Age, Phone} → Still works!

**Key Insight**: Adding attributes to a super key ALWAYS gives another super key. You can never "break" uniqueness by adding more information.

#### Step 2: Candidate Key - "The Minimal Super Keys"

**Definition**: A super key with no unnecessary attributes - remove ANY attribute and it stops being a super key.

**Intuition**: What's the MINIMUM information needed to identify someone uniquely?

From our examples:
- {Roll_No} → Minimal! Remove Roll_No and you have nothing
- {Roll_No, Name} → NOT minimal! Name is unnecessary since Roll_No alone works

**Why "Candidate"?** A table can have multiple minimal options. Each is a "candidate" for being the primary key.

**Example**: `Student(Roll_No, Email, Name, Phone)`
- {Roll_No} is a candidate key (unique ID)
- {Email} is also a candidate key (emails are unique)
- Both are minimal; both uniquely identify students

#### Step 3: Primary Key - "The Chosen One"

**Definition**: The candidate key we CHOOSE as the official identifier.

**Why choose just one?**
- Other tables need to reference this table - they need ONE consistent way
- Indexes are built on the primary key
- It becomes the "official" identity

**Convention**: Usually pick the candidate key that is:
- Shorter (less storage)
- Immutable (won't change)
- Not null (always has a value)

#### Step 4: Alternate Key - "The Runners Up"

**Definition**: Candidate keys that weren't chosen as primary.

If {Roll_No} is primary, then {Email} is an alternate key.

**Practical Use**: Alternate keys often get UNIQUE constraints to maintain their uniqueness guarantee.

### 🔗 Foreign Key - The Bridge Between Tables

**The Relationship Problem:**

Suppose we have:
- Student(Roll_No, Name, DeptID)
- Department(DeptID, DeptName, HOD)

How does DeptID in Student relate to DeptID in Department?

**Foreign Key**: An attribute in one table that references the primary key of another table.

```
Student.DeptID → Department.DeptID
```

**Why "Foreign"?** The key value comes from a "foreign" table - it's borrowed, not owned.

**Critical Properties:**
1. Must reference a PRIMARY KEY or UNIQUE key (not just any column)
2. Values must exist in the referenced table (or be NULL)
3. Can have a different name (Student.Dept could reference Department.DeptID)
4. Can reference the SAME table (self-referential: Employee.ManagerID → Employee.EmpID)

### 🧮 Counting Super Keys - GATE Favorite!

This is a classic GATE problem type. Let's understand the math.

**The Formula:**
```
Super keys containing a candidate key of size k in a relation with n attributes = 2^(n-k)
```

**Why does this work?**

If CK = {A, B} is a candidate key in R(A, B, C, D, E):
- The candidate key attributes (A, B) MUST be present
- The remaining attributes (C, D, E) can be present or absent
- Each of the (n-k) remaining attributes has 2 choices: include or exclude
- Total combinations = 2^(n-k)

**Visual Example:**
```
CK = {A, B}, Remaining = {C, D, E}

Super keys:
{A,B}           - C:no,  D:no,  E:no
{A,B,C}         - C:yes, D:no,  E:no
{A,B,D}         - C:no,  D:yes, E:no
{A,B,E}         - C:no,  D:no,  E:yes
{A,B,C,D}       - C:yes, D:yes, E:no
{A,B,C,E}       - C:yes, D:no,  E:yes
{A,B,D,E}       - C:no,  D:yes, E:yes
{A,B,C,D,E}     - C:yes, D:yes, E:yes

Total = 2³ = 8 super keys
```

### 🎯 Multiple Candidate Keys - Inclusion-Exclusion

**Problem**: R(A, B, C, D, E) with candidate keys {AB} and {CD}. Find total super keys.

**Naive Approach**:
- Super keys containing AB = 2^3 = 8
- Super keys containing CD = 2^3 = 8
- Total = 16? **WRONG!**

**The Problem**: Some super keys contain BOTH AB and CD. We're counting them twice!

**Inclusion-Exclusion Principle:**
```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

Applied here:
- Super keys with AB = 8
- Super keys with CD = 8
- Super keys with BOTH AB AND CD = 2^(5-4) = 2^1 = 2
  (Only E is free to vary)

**Total = 8 + 8 - 2 = 14**

**Extension to 3+ Candidate Keys:**
```
|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |B∩C| - |A∩C| + |A∩B∩C|
```

### ⚠️ Common Misconceptions That Cost Marks

**Misconception 1**: "Primary key must be a single attribute"
**Truth**: Primary key can be composite. In (StudentID, CourseID) → Grade table, the primary key is {StudentID, CourseID}.

**Misconception 2**: "Primary key can have NULL"
**Truth**: NEVER. NULL means "unknown" - how can you identify something with unknown identity?

**Misconception 3**: "Foreign key cannot be NULL"
**Truth**: Foreign key CAN be NULL (unless you add NOT NULL constraint). NULL means "relationship doesn't exist" - e.g., an employee with no manager.

**Misconception 4**: "Foreign key must have same name as primary key"
**Truth**: Names can differ. `Student.AdvisorID → Professor.ProfID` is valid.

---

## 4. Integrity Constraints

### Why Constraints Exist - Keeping Data Honest

Databases would be chaos without rules. Imagine:
- An employee assigned to department "XYZ" that doesn't exist
- A person with age -50
- Two students with the same ID but different names

Constraints are the **rules that maintain data sanity**.

### The Constraint Hierarchy - From Simple to Complex

#### 1. Domain Constraint - "Stay in Your Lane"

**What it does**: Ensures each attribute value comes from its defined domain.

**Examples**:
- Age must be an integer between 0 and 150
- Gender must be 'M', 'F', or 'Other'
- Email must match a valid email format

**Why it matters**: Prevents garbage data at the most fundamental level.

**SQL Implementation**: Data types, CHECK constraints
```sql
Age INT CHECK (Age >= 0 AND Age <= 150)
```

#### 2. Key Constraint - "Be Unique"

**What it does**: Ensures no two tuples have the same values for key attributes.

**Why it matters**: Without uniqueness, you can't reliably identify tuples.

**Example Violation**:
| StudentID | Name |
|-----------|------|
| 101 | Alice |
| 101 | Bob | ← VIOLATION! Same ID, different person

#### 3. Entity Integrity - "Know Thyself"

**What it does**: Primary key cannot be NULL.

**The Logic**: If the primary key is how we identify a tuple, and NULL means "unknown," then a NULL primary key means "we don't know what this is." That's existential crisis for a row!

**Important Distinction**:
- Primary key → No NULLs allowed (ever)
- Candidate key → NULLs allowed (unless it's the primary key)
- Foreign key → NULLs allowed (means "no relationship")

#### 4. Referential Integrity - "No Broken Links"

**What it does**: Foreign key values must exist in the referenced table (or be NULL).

**The Problem It Solves:**
```
Employee(EmpID, Name, DeptID)
Department(DeptID, DeptName)

If Employee has DeptID = "D99" but Department has no "D99"...
Where does this employee work? Nowhere that exists!
```

**The Rule**: Every non-NULL foreign key value must match a primary key value in the referenced table.

### 🔄 Referential Integrity Actions - What Happens When References Break?

The interesting case: What if you DELETE or UPDATE a row that other rows reference?

| Action | What Happens | When to Use |
|--------|--------------|-------------|
| **RESTRICT** | Reject the operation | Default. Safe. "Don't break anything." |
| **CASCADE** | Propagate the change | When child rows should follow parent |
| **SET NULL** | Set FK to NULL | When relationship can become "none" |
| **SET DEFAULT** | Set FK to default value | When there's a meaningful default |

**Deep Dive with Example:**

```
Department(DeptID PK, Name)
Employee(EmpID PK, Name, DeptID FK → Department)
```

**Scenario**: Delete Department "D1" (Engineering) which has 50 employees.

**RESTRICT**: "No! 50 employees reference D1. Delete them first or reassign them."
- Use when: Accidental deletion could cause data loss

**CASCADE**: "Delete D1 AND all 50 employees automatically."
- Use when: Child data is meaningless without parent (delete an order → delete order items)

**SET NULL**: "Delete D1, set all 50 employees' DeptID to NULL."
- Use when: Employees can temporarily be without a department

**SET DEFAULT**: "Delete D1, reassign all 50 employees to the default department."
- Use when: There's a fallback option (e.g., "Unassigned" department)

#### 5. Semantic Constraints - "Business Rules"

These are application-specific rules that go beyond structure:
- "Salary must be positive"
- "End date must be after start date"
- "A manager cannot manage more than 10 employees"

These typically require CHECK constraints or triggers.

### 🎓 GATE Edge Cases

**Q**: Can a foreign key reference a non-primary key?
**A**: Yes! It can reference any UNIQUE key (candidate key with unique constraint).

**Q**: Can a foreign key be part of the primary key?
**A**: Yes! In Enrollment(StudentID, CourseID, Grade), both StudentID and CourseID are foreign keys AND together form the primary key.

**Q**: Can a table have a foreign key to itself?
**A**: Yes! This is called a **self-referential relationship**.
```
Employee(EmpID PK, Name, ManagerID FK → Employee.EmpID)
```

---

## 5. Relational Algebra

### 🎯 What is Relational Algebra and Why Learn It?

**The Problem**: How do you precisely describe database operations?

Before relational algebra, queries were ambiguous. Different systems interpreted requests differently.

**The Solution**: A formal language with well-defined operators. Each operator:
1. Takes one or more relations as input
2. Produces exactly one relation as output
3. Has precise semantics - no ambiguity

**Why It Matters for GATE**:
1. It's the theoretical foundation of SQL
2. Query optimization uses algebraic transformations
3. Understanding operators = understanding database queries at a fundamental level

### 🧰 The Minimal Set - Why These Six?

These six operators can express ANY relational query:

| Operator | Symbol | Input | Output |
|----------|--------|-------|--------|
| Selection | σ | 1 relation | Subset of rows |
| Projection | π | 1 relation | Subset of columns |
| Union | ∪ | 2 relations | Combined rows |
| Set Difference | − | 2 relations | Rows in first but not second |
| Cartesian Product | × | 2 relations | All row combinations |
| Rename | ρ | 1 relation | Same relation, different names |

**Why these specific six?**
- They're **independent** - none can be derived from others
- They're **complete** - together they can express any query
- Every other operator is just a shortcut built from these

### 📝 Deep Dive: Each Operator

#### σ (Selection) - Horizontal Filtering

**What it does**: Keeps rows that satisfy a condition.

**Syntax**: σ_condition(R)

**Visual Understanding**:
```
Original Table:               After σ_Salary>50000:
| Name  | Salary |            | Name  | Salary |
|-------|--------|            |-------|--------|
| Alice | 50000  |            | Bob   | 70000  |
| Bob   | 70000  |            | Carol | 60000  |
| Carol | 60000  |
```

**Properties Explained**:

1. **Commutative**: σ_c1(σ_c2(R)) = σ_c2(σ_c1(R))
   - *Why?* Both give rows satisfying c1 AND c2. Order doesn't matter.

2. **Cascading**: σ_c1(σ_c2(R)) = σ_(c1 ∧ c2)(R)
   - *Why?* Filtering twice is the same as filtering once with combined condition.
   - *Used for optimization*: Combine multiple filters into one.

3. **Cardinality**: 0 ≤ |σ(R)| ≤ |R|
   - *Best case*: All rows match → same cardinality
   - *Worst case*: No rows match → 0

4. **Degree unchanged**: Selection doesn't add or remove columns.

#### π (Projection) - Vertical Filtering

**What it does**: Keeps only specified columns AND removes duplicates.

**Syntax**: π_A1,A2,...(R)

**The Duplicate Removal Trap**:
```
Original:                    π_Department:
| Name  | Department |       | Department |
|-------|------------|       |------------|
| Alice | CS         |       | CS         |
| Bob   | CS         |       | EE         |
| Carol | EE         |       
                              ↑ Only 2 rows! Duplicate "CS" removed
```

**Why remove duplicates?** Relations are SETS. Projection outputs a relation, which can't have duplicates.

**Properties**:

1. **NOT commutative**: π_A(π_B(R)) ≠ π_B(π_A(R)) in general
   - Only works if A ⊆ B (can't project columns you've already removed)

2. **Cardinality**: 1 ≤ |π(R)| ≤ |R| (assuming R is non-empty)
   - *Can decrease*: Due to duplicate removal
   - *Minimum 1*: Even if all rows become identical, you get one row

3. **Degree changes**: Output degree = number of projected attributes

#### ∪ (Union) - Combining Rows

**What it does**: Combines tuples from two relations, removing duplicates.

**Requirement - Union Compatibility**:
- Same number of attributes
- Corresponding attributes have compatible domains

**Why this requirement?** Union combines rows. If tables have different structures, how would you combine a (Name, Age) row with a (ProductID, Price, Stock) row? You can't.

**Properties**:
- Commutative: R ∪ S = S ∪ R
- Associative: (R ∪ S) ∪ T = R ∪ (S ∪ T)
- Removes duplicates (it's set union)

**Cardinality**: max(|R|, |S|) ≤ |R ∪ S| ≤ |R| + |S|
- *Min*: When R ⊆ S or S ⊆ R
- *Max*: When R and S have no common tuples

#### − (Set Difference) - What's in R but not S?

**What it does**: Returns tuples in R that are NOT in S.

**Requirement**: Union compatible (same reason as union)

**Crucial Property - NOT Commutative**:
- R − S: Employees who are NOT managers
- S − R: Managers who are NOT (regular) employees

These are completely different!

**Example Application**: Finding students who haven't enrolled in any course
```
AllStudents − StudentsWithEnrollments
```

**Cardinality**: max(0, |R| - |S|) ≤ |R − S| ≤ |R|
- *Min 0*: When R ⊆ S
- *Max |R|*: When R and S have no common tuples

#### × (Cartesian Product) - Every Possible Combination

**What it does**: Pairs every tuple of R with every tuple of S.

**Visual Understanding**:
```
R:                S:               R × S:
| A |             | X |            | A | X |
|---|             |---|            |---|---|
| 1 |             | a |            | 1 | a |
| 2 |             | b |            | 1 | b |
                                   | 2 | a |
                                   | 2 | b |
```

**Cardinality**: |R × S| = |R| × |S| (always exactly this)

**Degree**: degree(R × S) = degree(R) + degree(S)

**Why is it useful?** By itself, it's usually not. But combined with selection, it becomes JOIN:
```
R ⋈_condition S = σ_condition(R × S)
```

#### ρ (Rename) - Identity Crisis Solver

**What it does**: Changes the name of a relation or its attributes.

**Syntax**: ρ_NewName(A1→B1, A2→B2)(R)

**Why do we need it?**

**Use Case 1: Self-Join**
Find employees who earn more than their manager:
```
Without rename, how do you join Employee with Employee?
ρ_E1(Employee) ⋈ ρ_E2(Employee)
Now you have E1.Salary and E2.Salary - distinguishable!
```

**Use Case 2: Resolving Ambiguity**
After Cartesian product, if both relations have column "Name":
```
ρ(StudentName/Name)(Student) × ρ(ProfName/Name)(Professor)
```

### 🔗 Join Operations - The Workhorses of Queries

Joins are the most important derived operators. They combine related data from multiple tables.

#### Why Multiple Types of Joins?

Different situations need different combinations:
- Sometimes you want only matching rows (inner join)
- Sometimes you want all rows from one side (outer join)
- Sometimes you want to match on specific conditions (theta join)
- Sometimes you want to match on all common columns (natural join)

#### 1. Theta Join (θ-Join) - Any Condition

**Definition**: R ⋈_θ S = σ_θ(R × S)

Combine rows where condition θ is true. θ can be ANY condition.

**Example**: Find products more expensive than their category average
```
Product ⋈_(Product.Price > CategoryAvg.AvgPrice) CategoryAvg
```

#### 2. Equi Join - Equality Only

A theta join where θ uses only equality (=).

**Example**: R ⋈_(R.A = S.B) S

**Why special name?** Equi joins are extremely common and can be optimized heavily.

#### 3. Natural Join (⋈) - The Smart Join

**Definition**: Equi-join on ALL common attribute names, then remove duplicate columns.

**The Magic:**
```
Student(SID, Name, DeptID)
Department(DeptID, DeptName)

Student ⋈ Department
= σ_(Student.DeptID = Department.DeptID)(Student × Department)
  then remove one copy of DeptID

Result: (SID, Name, DeptID, DeptName)
```

**⚠️ GATE TRAP: No Common Attributes = Cartesian Product!**

If Student and Product share no column names:
```
Student ⋈ Product = Student × Product
```

This is usually NOT what you want!

**Cardinality Range**: 0 ≤ |R ⋈ S| ≤ |R| × |S|
- *Min 0*: No matching values in common columns
- *Max |R| × |S|*: Every pair matches (rarely happens)

**Special Case - Foreign Key Join**:
If R.FK → S.PK and every R tuple has a matching S tuple:
|R ⋈ S| = |R|

#### 4. Outer Joins - Keep the Lonely Rows

Regular join discards non-matching rows. Outer joins preserve them with NULLs.

**Left Outer Join (R ⟕ S)**: Keep all R rows
```
Student ⟕ Enrollment
Students without any enrollments appear with NULL enrollment data
```

**Right Outer Join (R ⟖ S)**: Keep all S rows

**Full Outer Join (R ⟗ S)**: Keep all rows from both

**When to use**:
- "Find all students and their enrollments (if any)" → Left outer
- "Find all courses and their enrollments (if any)" → Right outer
- "Find all students and all courses with any relationships" → Full outer

#### 5. Semi Join (⋉) - Just Check Existence

**R ⋉ S** = π_R.*(R ⋈ S)

Returns R's attributes for tuples that have a match in S.

**Use Case**: Distributed databases - instead of shipping entire S, ship just the matching keys, do local join.

#### 6. Anti Join (▷) - Non-Matches Only

**R ▷ S** = R − (R ⋉ S)

Returns R's tuples that have NO match in S.

**Example**: Students not enrolled in any course
```
Student ▷ Enrollment
```

### ➗ Division (÷) - The "FOR ALL" Operator

This is the most conceptually difficult operator. Master it!

**The Question It Answers**: "Find X that is related to ALL Y"

**Definition**: R(A, B) ÷ S(B) = {a | for every b in S, (a, b) is in R}

**Intuitive Example:**

```
Enrollment:          Courses:        Enrollment ÷ Courses:
| Student | Course | | Course |      | Student |
|---------|--------|  |--------|      |---------|
| Alice   | Math   |  | Math   |      | Alice   |  ← Alice took ALL courses
| Alice   | Physics|  | Physics|      
| Bob     | Math   |                  
| Carol   | Math   |                  ← Bob only took Math (not all)
| Carol   | Physics|                  ← Carol took both = ALL
```

Wait, Carol is missing! Let me recalculate... Carol took Math and Physics = ALL courses required. So Carol should appear.

**The Formula** (how to compute without a division operator):
```
R ÷ S = π_A(R) − π_A((π_A(R) × S) − R)
```

**Breaking it down**:
1. π_A(R): All A values that appear in R (all students who took something)
2. π_A(R) × S: All possible (A, B) pairs (if every student took every course)
3. (π_A(R) × S) − R: Missing pairs (courses a student DIDN'T take)
4. π_A(...): Students who have missing courses
5. π_A(R) − ...: Students with NO missing courses = students who took ALL

**GATE Keywords**: "all", "every", "each", "must have completed all"

### 🎯 Cardinality Bounds Summary

Understanding bounds helps verify query correctness:

| Operation | Minimum | Maximum |
|-----------|---------|---------|
| R ∪ S | max(|R|, |S|) | |R| + |S| |
| R ∩ S | 0 | min(|R|, |S|) |
| R − S | 0 | |R| |
| R × S | |R| × |S| | |R| × |S| |
| R ⋈ S | 0 | |R| × |S| |
| σ(R) | 0 | |R| |
| π(R) | 1 (if R ≠ ∅) | |R| |

### 🧠 Operator Precedence

When reading expressions without parentheses:

**High to Low**:
1. σ, π, ρ (Unary - apply first)
2. ×, ⋈
3. ∩
4. ∪, −

**Best Practice**: Always use parentheses to be explicit!

---

## 6. Tuple Relational Calculus (TRC)

### 📝 What is TRC and Why Does It Exist?

**The Paradigm Shift:**

Relational Algebra is **procedural** - you describe HOW to get the answer:
```
"Take table A, join with B, filter by condition, project these columns"
```

TRC is **declarative** - you describe WHAT you want:
```
"Give me tuples where this condition is true"
```

**The Analogy:**
- Relational Algebra = Giving turn-by-turn directions
- TRC = Giving a destination and letting GPS figure it out

**Why both?** Different perspectives on the same thing help understanding. Also, SQL is based on TRC's declarative approach!

### 📝 The Syntax

```
{ t | P(t) }
```

**Reading this**: "The set of all tuples t such that predicate P(t) is true"

- **t** is a tuple variable (represents an entire row)
- **P(t)** is a predicate (condition that evaluates to true/false)

### Understanding Through Examples

**Example 1: Simple Selection**
```
Find all employees in IT department
{ t | t ∈ Employee ∧ t.Dept = 'IT' }
```

**Translation**: "Give me all tuples t from Employee where department is IT"

**Example 2: Using Existential Quantifier**
```
Find employees who earn more than SOMEONE in IT
{ t | t ∈ Employee ∧ ∃s ∈ Employee (s.Dept = 'IT' ∧ t.Salary > s.Salary) }
```

**Translation**: "Give me employee t if there EXISTS some s in Employee who is in IT and t's salary beats s's salary"

**Key insight**: "Someone" = "There exists" = ∃

**Example 3: Using Universal Quantifier**
```
Find employees who earn more than EVERYONE in IT
{ t | t ∈ Employee ∧ ∀s ∈ Employee (s.Dept ≠ 'IT' ∨ t.Salary > s.Salary) }
```

Wait, why the weird condition?

**The Logic Trick**: "t beats everyone in IT" means:
- For ALL employees s: IF s is in IT, THEN t.Salary > s.Salary
- In logic: p → q ≡ ¬p ∨ q
- So: s.Dept = 'IT' → t.Salary > s.Salary ≡ s.Dept ≠ 'IT' ∨ t.Salary > s.Salary

**Key insight**: "Everyone" = "For all" = ∀

### Quantifiers - The Heart of TRC

| Symbol | Name | Meaning | Keywords to recognize |
|--------|------|---------|----------------------|
| ∃ | Existential | "There exists at least one" | some, any, at least one |
| ∀ | Universal | "For all" | all, every, each, none (∀ with negation) |

### ⚡ Conversion Between Quantifiers

These equivalences are CRITICAL for GATE:

```
∀x P(x) ≡ ¬∃x ¬P(x)
"All X satisfy P" = "There doesn't exist an X that fails P"

∃x P(x) ≡ ¬∀x ¬P(x)  
"Some X satisfies P" = "Not all X fail P"
```

**Why useful?** Sometimes one form is easier to express than the other.

### ⚠️ Safe Expressions - A Crucial Concept

**The Problem:**
```
{ t | ¬(t ∈ Employee) }
```

What is this query asking for? "All tuples NOT in Employee table."

How many such tuples exist? **INFINITE!** Every possible combination of values that isn't in Employee.

**Definition**: A TRC expression is **safe** if it guarantees a **finite result**.

**The Rule**: Every variable must be limited to tuples from the database. You can't ask for "all tuples that aren't employees" because that's infinite.

**Safe version:**
```
{ t | t ∈ Person ∧ ¬(t ∈ Employee) }
```
Now t is limited to Person table - finite result!

### 🎓 TRC to Relational Algebra Mapping

| TRC Pattern | Relational Algebra |
|-------------|-------------------|
| t ∈ R ∧ condition(t) | σ_condition(R) |
| ∃s ∈ S (t.A = s.A ∧ ...) | R ⋈ S |
| {t.A, t.B \| ...} | π_A,B(...) |
| ∃s ∈ S (t.A = s.A) | R ⋉ S |
| ¬∃s ∈ S (t.A = s.A) | R ▷ S |

---

## 7. Domain Relational Calculus (DRC)

### 📝 How DRC Differs from TRC

**TRC**: Variables represent **entire tuples**
```
{ t | t ∈ Employee ∧ t.Salary > 50000 }
```

**DRC**: Variables represent **individual domain values** (column values)
```
{ <name, salary> | ∃empid ∃dept (Employee(empid, name, salary, dept) ∧ salary > 50000) }
```

**Analogy:**
- TRC: "I want this entire row"
- DRC: "I want these specific values from columns"

### The Syntax

```
{ <x₁, x₂, ..., xₙ> | P(x₁, x₂, ..., xₙ) }
```

**Reading this**: "Give me tuples formed by values x₁, x₂, ... where predicate P is true"

### 🎯 Understanding Through Examples

**Example 1: Find names and salaries of employees in IT**

**TRC version:**
```
{ <t.Name, t.Salary> | t ∈ Employee ∧ t.Dept = 'IT' }
```

**DRC version:**
```
{ <n, s> | ∃e ∃d (Employee(e, n, s, d) ∧ d = 'IT') }
```

**Breaking down the DRC:**
- We want name (n) and salary (s)
- There must exist empid (e) and dept (d) such that...
- (e, n, s, d) is a valid Employee tuple AND d is 'IT'

**Why existential quantifiers?** We don't want e and d in our output, but they must exist for n and s to be valid values from Employee.

**Example 2: Find employees earning more than everyone in IT**

```
{ <e, n, s, d> | Employee(e, n, s, d) ∧ 
                ∀e2 ∀n2 ∀s2 ∀d2 (
                    ¬Employee(e2, n2, s2, d2) ∨ 
                    d2 ≠ 'IT' ∨ 
                    s > s2
                ) 
}
```

This is more verbose than TRC because we must explicitly quantify each column!

### TRC vs DRC vs Relational Algebra - The Complete Picture

| Aspect | Relational Algebra | TRC | DRC |
|--------|-------------------|-----|-----|
| **Nature** | Procedural | Declarative | Declarative |
| **Variables** | None | Tuple variables | Domain variables |
| **Specifies** | HOW to compute | WHAT tuples we want | WHAT values we want |
| **Closer to** | Query optimization | SQL (conceptually) | SQL SELECT clause |

### 🎓 Codd's Theorem - The Fundamental Equivalence

**Theorem**: Relational Algebra, TRC (safe), and DRC (safe) have **exactly the same expressive power**.

**What this means:**
- Any query in RA can be written in TRC and DRC
- Any query in TRC can be written in RA and DRC
- Any query in DRC can be written in RA and TRC

**Why it matters:**
1. You can choose whichever is most convenient for a problem
2. SQL (based on TRC/DRC) is as powerful as RA
3. Query optimizers can translate between them

**The Limitation**: None of these can express:
- Recursive queries (e.g., find all ancestors)
- Aggregation (COUNT, SUM, AVG)
- Sorting (ORDER BY)

These require extensions beyond basic relational model.

---

## 8. Normalization

### 🎯 What is Normalization and Why Do We Need It?

**The Problem: Redundancy**

Consider this table:

| StudentID | StudentName | CourseID | CourseName | InstructorID | InstructorName |
|-----------|-------------|----------|------------|--------------|----------------|
| 1 | Alice | C1 | Database | I1 | Prof. Smith |
| 2 | Bob | C1 | Database | I1 | Prof. Smith |
| 3 | Carol | C2 | Networks | I2 | Prof. Jones |
| 1 | Alice | C2 | Networks | I2 | Prof. Jones |

**What's wrong?**
1. "Database" and "Prof. Smith" appear twice
2. If we change Prof. Smith's name, we must update multiple rows
3. If Carol drops the Networks course, we lose information about Prof. Jones!

**Normalization** is the process of organizing tables to:
1. **Minimize redundancy** - Store each fact once
2. **Prevent anomalies** - Avoid update/insert/delete problems
3. **Preserve data integrity** - Keep data consistent

### 🔥 The Three Types of Anomalies

#### 1. Update Anomaly
**Problem**: Same fact stored in multiple places → Must update all or get inconsistency.

**Example**: Changing "Database" to "Database Systems" - must update every row with that course.

#### 2. Insertion Anomaly
**Problem**: Can't insert some data without inserting other data.

**Example**: Can't add a new instructor until they teach a course (because CourseID might be required).

#### 3. Deletion Anomaly
**Problem**: Deleting data removes more than intended.

**Example**: If Carol drops Networks and she's the only student, we lose Prof. Jones's information entirely.

### 📊 The Normal Form Hierarchy

```
1NF ⊂ 2NF ⊂ 3NF ⊂ BCNF ⊂ 4NF ⊂ 5NF
```

**Reading**: Every 3NF table is also in 2NF and 1NF. But not every 2NF table is in 3NF.

**Practical Reality**: Most real databases aim for 3NF or BCNF.

### 1NF (First Normal Form) - "Make It a Proper Table"

**Rule**: All attributes must be **ATOMIC** (indivisible).

**What violates 1NF?**

1. **Multi-valued attributes:**
   ```
   ❌ Student(ID, Name, Phones)  where Phones = "123, 456, 789"
   ✓ Student(ID, Name) + StudentPhone(ID, Phone)
   ```

2. **Composite attributes:**
   ```
   ❌ Person(ID, FullName)  where FullName = {FirstName, LastName}
   ✓ Person(ID, FirstName, LastName)
   ```

3. **Repeating groups:**
   ```
   ❌ Order(OrderID, Product1, Qty1, Product2, Qty2, Product3, Qty3)
   ✓ Order(OrderID) + OrderItem(OrderID, Product, Qty)
   ```

**The Atomicity Question**: Is "Address" atomic? It depends on how you USE it. If you never query by City separately, "123 Main St, NYC" could be atomic. If you need to query by City, it's not.

### 2NF (Second Normal Form) - "Eliminate Partial Dependencies"

**Rule**: 1NF + No partial dependencies.

**Partial Dependency**: A non-prime attribute depends on PART of a candidate key.

**Only applies when**: You have a composite candidate key! If all candidate keys are single-attribute, you're automatically in 2NF.

**Example Violation:**
```
OrderItem(OrderID, ProductID, ProductName, Quantity, Price)
Candidate Key: {OrderID, ProductID}
```

ProductName depends on ProductID alone, not the full key!
- {OrderID, ProductID} → ProductName ✗
- {ProductID} → ProductName ✓ (partial dependency!)

**Fix**: Split into:
```
OrderItem(OrderID, ProductID, Quantity, Price)
Product(ProductID, ProductName)
```

**The Intuition**: In 2NF, every non-key attribute must need the WHOLE key to be determined.

### 3NF (Third Normal Form) - "Eliminate Transitive Dependencies"

**Rule**: 2NF + No transitive dependencies.

**Transitive Dependency**: A → B → C, where B is non-prime.

**Example Violation:**
```
Employee(EmpID, DeptID, DeptName, DeptLocation)
Candidate Key: {EmpID}

EmpID → DeptID → DeptName
EmpID → DeptID → DeptLocation
```

DeptName and DeptLocation are transitively dependent on EmpID through DeptID.

**Fix**: Split into:
```
Employee(EmpID, DeptID)
Department(DeptID, DeptName, DeptLocation)
```

**Formal Definition (Important for GATE):**

A relation is in 3NF if for every non-trivial FD X → A:
- **X is a superkey**, OR
- **A is a prime attribute**

### BCNF (Boyce-Codd Normal Form) - "The Strictest Practical Form"

**Rule**: For every non-trivial FD X → Y, X must be a **superkey**.

**Difference from 3NF**: No exception for prime attributes!

**Example: 3NF but NOT BCNF**
```
Teaches(Student, Subject, Professor)

FDs:
- {Student, Subject} → Professor  (a student takes a subject with one professor)
- Professor → Subject             (a professor teaches only one subject)

Candidate Key: {Student, Subject}
```

**3NF Check:**
- {Student, Subject} → Professor: {Student, Subject} is superkey ✓
- Professor → Subject: Professor is not superkey, but Subject IS prime ✓ (part of CK)

**BCNF Check:**
- {Student, Subject} → Professor: ✓
- Professor → Subject: Professor is NOT a superkey ✗

**Why this matters**: Professor → Subject means if we know the professor, we know the subject. But different student-professor pairs can have the same professor, causing redundancy!

**BCNF Decomposition:**
```
ProfessorSubject(Professor, Subject)  -- Professor is key
StudentProfessor(Student, Professor)  -- {Student, Professor} is key
```

### The BCNF vs 3NF Trade-off

| Property | 3NF | BCNF |
|----------|-----|------|
| Eliminates all redundancy from FDs? | No | Yes |
| Lossless decomposition always possible? | Yes | Yes |
| Dependency preservation always possible? | Yes | **NO** |

**Key Insight**: BCNF might require breaking a table in a way that you can't verify some FDs without joining tables back together!

### 4NF (Fourth Normal Form) - "Eliminate Multi-Valued Dependencies"

**The Problem 4NF Solves:**
```
Employee(EmpID, Skill, Language)

EmpID | Skill      | Language
------|------------|----------
1     | Python     | English
1     | Python     | French
1     | Java       | English
1     | Java       | French
```

Skills and languages are INDEPENDENT! An employee's skills have nothing to do with their languages. But this table creates 2×2 = 4 rows for 2 skills and 2 languages.

**Multi-Valued Dependency (MVD)**: X ↠ Y means for each X value, there's a set of Y values independent of other attributes.

Here: EmpID ↠ Skill and EmpID ↠ Language

**4NF Rule**: For every non-trivial MVD X ↠ Y, X must be a superkey.

**Fix:**
```
EmpSkill(EmpID, Skill)
EmpLanguage(EmpID, Language)
```

### 5NF (Fifth Normal Form / Project-Join Normal Form)

**Rule**: 4NF + No join dependencies except those implied by candidate keys.

**Practical Impact**: Very rare. A table violates 5NF only if:
- It can be decomposed into 3+ smaller tables
- These tables join back to give the original
- But 2-table decomposition isn't lossless

Most databases don't worry about 5NF. For GATE, just know it exists.

### 🎯 Quick Decision Table

| Normal Form | What to Check | Quick Test |
|-------------|---------------|------------|
| 1NF | Atomic values? | Any lists, arrays, or nested structures? |
| 2NF | Partial dependencies? | Composite key + non-prime depends on part? |
| 3NF | Transitive dependencies? | Non-prime → non-prime chain? |
| BCNF | Every LHS is superkey? | Any FD with non-superkey LHS? |
| 4NF | Multi-valued dependencies? | Independent multi-valued attributes? |

### 🧠 Speed Trick for Normal Form Identification

1. **Find all candidate keys first** (this is crucial!)
2. Check each FD: Is LHS a superkey?
   - If ALL yes → BCNF
   - If some no → check if RHS is prime
     - If RHS prime → 3NF (not BCNF)
     - If RHS non-prime → check if LHS is proper subset of some CK
       - If yes → not 2NF
       - If no → 2NF (not 3NF)

---

## 9. Functional Dependencies

### 📝 What is a Functional Dependency, Really?

**Definition**: X → Y means "if two tuples agree on X, they MUST agree on Y."

**Intuition**: Knowing X tells you Y. X "determines" Y.

**Real-world Examples:**
- SSN → Person's Name (knowing SSN tells you the name)
- {StudentID, CourseID} → Grade (a student has one grade per course)
- ZipCode → City (knowing ZIP tells you the city)

**Non-Examples:**
- Name → Age ✗ (many people share names but have different ages)
- City → ZipCode ✗ (cities have multiple ZIPs)

### Trivial vs Non-Trivial FDs

**Trivial FD**: X → Y where Y ⊆ X

Examples:
- {A, B} → A (trivial - always true)
- {A, B} → {A, B} (trivial)

**Non-Trivial FD**: X → Y where Y ⊄ X

Only non-trivial FDs are interesting for normalization!

### Armstrong's Axioms - The Foundation

These three rules let you derive ALL valid FDs from a given set:

#### 1. Reflexivity: If Y ⊆ X, then X → Y

**Translation**: Any set of attributes determines any of its subsets.

**Why it's true**: If two tuples have the same values for {A, B, C}, they certainly have the same values for {A, B} (a subset).

**Examples**:
- {A, B, C} → {A, B}
- {A} → {A}

#### 2. Augmentation: If X → Y, then XZ → YZ

**Translation**: You can add the same attributes to both sides.

**Why it's true**: If X determines Y, then knowing X and Z certainly determines Y and Z.

**Example**: If A → B, then AC → BC

#### 3. Transitivity: If X → Y and Y → Z, then X → Z

**Translation**: Dependencies chain together.

**Why it's true**: If X determines Y, and Y determines Z, then X determines Z through Y.

**Example**: If EmpID → DeptID and DeptID → DeptName, then EmpID → DeptName

### Why Are These Axioms Important?

**Soundness**: They only produce VALID FDs (no false conclusions)

**Completeness**: They can produce ALL valid FDs (nothing is missed)

Together, these mean Armstrong's Axioms are a complete system for reasoning about functional dependencies.

### Derived Rules (For Speed)

These are proven using the axioms but are faster to apply directly:

| Rule | Statement | Proof Sketch |
|------|-----------|--------------|
| **Union** | X → Y, X → Z ⟹ X → YZ | Augment both, combine |
| **Decomposition** | X → YZ ⟹ X → Y, X → Z | Reflexivity on YZ |
| **Pseudo-transitivity** | X → Y, WY → Z ⟹ WX → Z | Augment first, apply transitivity |

### 🔑 Attribute Closure (X⁺) - The Most Important Algorithm

**Definition**: X⁺ is the set of ALL attributes functionally determined by X.

**Why it matters**: This single algorithm solves:
1. Finding if X is a superkey (X⁺ = all attributes?)
2. Checking if FD X → Y holds (Y ⊆ X⁺?)
3. Finding candidate keys (minimal X where X⁺ = all attributes)

**Algorithm:**
```
X⁺ = X  // Start with X itself

repeat
    for each FD Y → Z in F:
        if Y ⊆ X⁺:
            X⁺ = X⁺ ∪ Z  // Add Z to closure
until X⁺ doesn't change
```

**Example:**
```
R(A, B, C, D, E)
FDs: A → B, BC → D, D → E, E → A

Compute (BC)⁺:

Initial: (BC)⁺ = {B, C}

Iteration 1:
- A → B: A ⊆ {B,C}? No
- BC → D: BC ⊆ {B,C}? Yes! Add D → {B,C,D}
- D → E: D ⊆ {B,C,D}? Yes! Add E → {B,C,D,E}
- E → A: E ⊆ {B,C,D,E}? Yes! Add A → {A,B,C,D,E}

Iteration 2:
- A → B: A ⊆ {A,B,C,D,E}? Yes, but B already in closure

No more changes. (BC)⁺ = {A, B, C, D, E} = All attributes

Therefore, BC is a superkey!
```

### 🎯 Finding Candidate Keys - Systematic Approach

**Step 1**: Categorize attributes

- **LHS only**: Only appear on left side of FDs → MUST be in every key
- **RHS only**: Only appear on right side → NEVER in any key  
- **Both sides**: May or may not be in key
- **Neither side**: MUST be in every key (no FD determines them)

**Step 2**: Start with (LHS only ∪ Neither side), compute closure

**Step 3**: If not superkey, try adding attributes from "Both sides" one at a time

**Example:**
```
R(A, B, C, D, E)
FDs: A → B, BC → E, ED → A

Categorize:
- LHS: A, B, C, E, D
- RHS: B, E, A
- LHS only: C, D (appear on left, never on right)
- RHS only: none
- Both: A, B, E
- Neither: none

(CD)⁺ = {C, D} - Not superkey (missing A, B, E)

Try ACD:
(ACD)⁺ = {A, C, D} → A→B → {A, B, C, D} → BC→E → {A, B, C, D, E} ✓

Try BCD:
(BCD)⁺ = {B, C, D} → BC→E → {B, C, D, E} → ED→A → {A, B, C, D, E} ✓

Candidate Keys: {ACD, BCD}
```

### Canonical Cover (Fc) - Minimizing FDs

**Goal**: Find an equivalent set of FDs that is minimal.

**Properties of Canonical Cover:**
1. Single attribute on RHS (decomposed form)
2. No extraneous attributes on LHS
3. No redundant FDs
4. Equivalent to original set (same closure)

**Algorithm:**
1. Apply decomposition: X → AB becomes X → A, X → B
2. For each FD X → A, check if any attribute in X is extraneous
   - b is extraneous in X if (X - b)⁺ under remaining FDs still contains A
3. Remove redundant FDs
   - FD is redundant if removing it doesn't change closure

### Prime vs Non-Prime Attributes

**Prime Attribute**: Part of at least one candidate key
**Non-Prime Attribute**: Not part of any candidate key

**Why it matters**: This distinction is key for 2NF and 3NF definitions!

**Example:**
```
R(A, B, C, D)
Candidate Keys: {AB}

Prime: A, B (in the key)
Non-Prime: C, D (not in any key)
```

---

## 10. Decomposition

### 🎯 Why Decompose? What Are We Trying to Achieve?

When we normalize a table, we break it into smaller tables. But not any decomposition works!

**Two Critical Properties:**

1. **Lossless Join** - Can we get back the original table by joining?
2. **Dependency Preserving** - Can we verify all FDs without joining?

### Lossless Join Decomposition - "No Data Loss"

**The Problem:**

Original: R(A, B, C) with data:
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 2 | 5 |

Decompose into R1(A, B) and R2(B, C):

R1:          R2:
| A | B |    | B | C |
|---|---|    |---|---|
| 1 | 2 |    | 2 | 3 |
| 4 | 2 |    | 2 | 5 |

Join R1 ⋈ R2 (on B=2):
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 1 | 2 | 5 |  ← SPURIOUS! Didn't exist originally!
| 4 | 2 | 3 |  ← SPURIOUS!
| 4 | 2 | 5 |

**This is a LOSSY decomposition** - we get fake data when we join back!

### The Lossless Join Test (Binary Decomposition)

**Theorem**: Decomposition of R into R1 and R2 is lossless iff:

```
R1 ∩ R2 → R1  OR  R1 ∩ R2 → R2
```

**In English**: The common attributes must be a superkey of at least one decomposed relation.

**Why does this work?**

If R1 ∩ R2 is a key in R1, then each R2 tuple matches at most ONE R1 tuple, preventing the multiplication of spurious tuples.

### 🎯 Example: Checking Losslessness

**R(A, B, C)** with FD: A → B

**Decomposition 1**: R1(A, B) and R2(A, C)
- Common: {A}
- In R1: A → B, so A → AB, meaning A is a superkey of R1 ✓
- **Lossless!**

**Decomposition 2**: R1(A, B) and R2(B, C)
- Common: {B}
- Does B → A? No (not given)
- Does B → C? No (not given)
- **Lossy!**

### Dependency Preserving Decomposition - "Keep FDs Checkable"

**The Problem:**

Original: R(A, B, C) with FD: AC → B

Decompose into: R1(A, B) and R2(A, C)

Can we verify AC → B using only R1 or R2?
- R1 has A and B but not C
- R2 has A and C but not B
- To check AC → B, we'd need to JOIN first!

**This is NOT dependency preserving** - the FD AC → B is lost in decomposition.

### The Dependency Preserving Test

Compute the closure of the union of projections:

```
F' = F projected onto R1 ∪ F projected onto R2 ∪ ...

If F'⁺ = F⁺, decomposition is dependency preserving.
```

**Projecting F onto Ri**: Keep only FDs where all attributes are in Ri.

### The Trade-off: 3NF vs BCNF

| Goal | 3NF | BCNF |
|------|-----|------|
| Lossless decomposition | ✓ Always possible | ✓ Always possible |
| Dependency preserving | ✓ Always possible | ✗ Not always possible |
| Eliminates all FD-based redundancy | ✗ May have some | ✓ Complete |

**The Dilemma**: Sometimes you can't have both BCNF AND dependency preservation. You must choose!

### 🔧 BCNF Decomposition Algorithm

```
Input: Relation R, Set of FDs F

Algorithm:
1. Compute candidate keys of R
2. Find an FD X → Y that violates BCNF (X is not superkey)
3. If no such FD exists, R is already in BCNF. Done.
4. Decompose R into:
   - R1 = X ∪ Y (the FD's attributes)
   - R2 = R - (Y - X) (everything except Y's non-key attributes)
5. Recursively apply to R1 and R2

This is guaranteed lossless because X → Y means X is superkey of R1.
```

**Example:**
```
R(A, B, C, D)
FDs: A → B, C → D
Keys: AC

Check BCNF:
- A → B: Is A superkey? No (A⁺ = {A, B} ≠ ABCD)

Decompose:
- R1 = {A, B} (FD's attributes)
- R2 = {A, C, D} (ABCD - {B} = ACD)

Now check R2:
- C → D: Is C superkey of R2? C⁺ in R2 = {C, D} ≠ {A, C, D}

Decompose R2:
- R3 = {C, D}
- R4 = {A, C}

Final: R1(A,B), R3(C,D), R4(A,C) - all in BCNF
```

### 🔧 3NF Synthesis Algorithm

Unlike BCNF, 3NF uses **synthesis** (building up) rather than decomposition.

```
Input: Relation R, Set of FDs F

Algorithm:
1. Compute canonical cover Fc of F
2. For each FD X → Y in Fc, create relation XY
3. If no relation contains a candidate key of R, add a relation with a candidate key
4. Remove redundant relations (those whose attributes are subset of another)
```

**Why this works:**
- Step 2 ensures each FD is within one relation (dependency preserving)
- Step 3 ensures we can reconstruct R (lossless)
- Canonical cover minimizes the number of relations

### 🎯 Key Insight for GATE

**Question Pattern**: "Is this decomposition lossless/dependency-preserving?"

**Strategy**:
1. For lossless: Find common attributes, check if they're a superkey of either part
2. For dependency preserving: Check if each FD's attributes are entirely within some part

---

## 11. GATE PYQ Patterns & Tricks

### 🎯 Most Frequently Asked Topics (By Marks Weight)

1. **Candidate Keys & Super Keys** (Very High) - Counting, finding, inclusion-exclusion
2. **Normal Form Identification** (Very High) - Given FDs, determine highest NF
3. **Relational Algebra** (High) - Writing queries, understanding operators
4. **Lossless Decomposition** (High) - Test for losslessness
5. **Attribute Closure** (Medium-High) - Foundation for keys and FD verification

### ⚡ Speed Tricks That Save Time

#### Trick 1: Finding Candidate Keys Fast

**Step 1**: Categorize attributes
```
LHS-only: MUST be in every key
RHS-only: NEVER in any key
Both/Neither: Compute closures
```

**Step 2**: Start minimal, expand if needed
```
(LHS-only + Neither)⁺ = All attributes? 
If yes → candidate key found
If no → Add one attribute at a time from "Both" category
```

**Example Walkthrough:**
```
R(A, B, C, D, E), FDs: {A→B, BC→D, D→E}

LHS: {A, B, C, D}
RHS: {B, D, E}
LHS-only: {A, C}
Neither: none

(AC)⁺ = {A,C} → A→B → {A,B,C} → BC→D → {A,B,C,D} → D→E → {A,B,C,D,E} ✓

AC is a candidate key!
Check for others by trying BC, AD, etc.
```

#### Trick 2: Super Key Counting with Inclusion-Exclusion

**Formula per candidate key of size k in relation of size n:**
```
Super keys containing this CK = 2^(n-k)
```

**For multiple candidate keys:**
```
|SuperKeys| = Σ|containing CKi| - Σ|containing CKi ∩ CKj| + Σ|containing CKi ∩ CKj ∩ CKk| - ...
```

**Example:**
```
R(A,B,C,D,E), CKs: {AB}, {CD}, {AE}

|with AB| = 2^(5-2) = 8
|with CD| = 2^(5-2) = 8  
|with AE| = 2^(5-2) = 8

|with AB ∩ CD| = |with ABCD| = 2^(5-4) = 2
|with AB ∩ AE| = |with ABE| = 2^(5-3) = 4
|with CD ∩ AE| = |with ACDE| = 2^(5-4) = 2

|with AB ∩ CD ∩ AE| = |with ABCDE| = 2^(5-5) = 1

Total = 8+8+8 - 2-4-2 + 1 = 17
```

#### Trick 3: Quick Normal Form Determination

```
Step 1: Find ALL candidate keys
Step 2: For each FD X → Y:
        - Is X a superkey? 
          Yes → OK for BCNF
          No  → Is Y prime?
                Yes → OK for 3NF (but not BCNF)
                No  → Is X proper subset of some CK?
                      Yes → Not even 2NF
                      No  → 2NF but not 3NF
```

#### Trick 4: Recognizing Division Problems

**Keywords in question**: "all", "every", "each", "must have completed all"

**Pattern**: "Find X that is related to ALL Y"

**Template Answer**: R(X, Y) ÷ S(Y)

**Examples:**
- "Students enrolled in all courses" → Enrollment ÷ Course
- "Suppliers who supply all parts" → Supplies ÷ Parts
- "Employees who work on all projects" → WorksOn ÷ Project

#### Trick 5: Natural Join Cardinality Bounds

**Foreign Key Case**: If R.FK references S.PK:
- |R ⋈ S| = |R| (every R tuple has exactly one match)

**No Common Values**: |R ⋈ S| = 0

**All Values Match**: |R ⋈ S| can be up to |R| × |S|

### 📝 Common GATE Traps - Don't Fall For These!

#### Trap 1: Confusing 3NF and BCNF

**Difference**: 3NF allows X → A when A is prime (part of some key), even if X isn't a superkey.

**Example That's 3NF but not BCNF:**
```
R(A, B, C), FDs: AB → C, C → B
CK: {AB}

AB → C: AB is superkey ✓
C → B: C is not superkey, but B is prime ✓

Result: 3NF but not BCNF!
```

#### Trap 2: Assuming Lossless ⟺ Dependency Preserving

**These are INDEPENDENT properties!**

- A decomposition can be lossless but not dependency preserving
- A decomposition can be dependency preserving but lossy
- They're separate tests!

#### Trap 3: Natural Join with No Common Attributes

```
R(A, B) ⋈ S(C, D) = R × S
```

Natural join on disjoint schemas = Cartesian product!

**This is usually NOT what the query intends** - it's often a sign of incorrect table design or wrong query.

#### Trap 4: Forgetting Self-Referential Foreign Keys

```
Employee(EmpID, Name, ManagerID)
```

ManagerID is a FK to the SAME table (ManagerID → EmpID).

This is valid and common for hierarchical data!

#### Trap 5: Prime Attribute Confusion

**Prime** = Part of SOME candidate key (not just THE primary key)

If CKs are {AB} and {CD}, then prime attributes are {A, B, C, D}.

### 🧮 Formula Quick Reference

| Concept | Formula/Rule |
|---------|--------------|
| Max tuples in relation | Product of all domain sizes |
| Super keys from CK(k) in R(n) | 2^(n-k) |
| Cartesian product size | \|R\| × \|S\| |
| Selection result | 0 to \|R\| |
| Projection result | 1 to \|R\| |
| Natural join result | 0 to \|R\| × \|S\| |
| Union result | max(\|R\|,\|S\|) to \|R\|+\|S\| |
| Difference result | 0 to \|R\| |

### 📊 Decision Flowchart for Normal Forms

```
Given: Relation R with FDs F

1. Find ALL candidate keys of R

2. For EACH non-trivial FD X → A:

   Is X a superkey of R?
   │
   ├─ YES → This FD is fine for BCNF
   │
   └─ NO → Is A a prime attribute?
           │
           ├─ YES → FD is fine for 3NF (not BCNF)
           │
           └─ NO → Is X a proper subset of some candidate key?
                   │
                   ├─ YES → Violates 2NF (partial dependency)
                   │
                   └─ NO → Violates 3NF (transitive dependency)

3. Final determination:
   - ALL FDs pass BCNF test → R is in BCNF
   - All pass 3NF but some fail BCNF → R is in 3NF (not BCNF)
   - All pass 2NF but some fail 3NF → R is in 2NF (not 3NF)
   - Some fail 2NF → R is only in 1NF
```

---

## 🎓 Final Mastery Checklist

Before your exam, verify you can:

### Keys & Dependencies
- [ ] Compute attribute closure X⁺ efficiently
- [ ] Find ALL candidate keys for any relation
- [ ] Count super keys using inclusion-exclusion
- [ ] Identify prime vs non-prime attributes
- [ ] Recognize trivial vs non-trivial FDs

### Relational Algebra
- [ ] Write queries using σ, π, ∪, −, ×, ρ
- [ ] Understand and apply all join types
- [ ] Use division for "for all" queries
- [ ] Calculate cardinality bounds for operations

### Calculus
- [ ] Write TRC expressions with ∃ and ∀
- [ ] Convert between quantifiers
- [ ] Identify safe vs unsafe expressions

### Normalization
- [ ] Identify normal form of any relation (1NF through BCNF)
- [ ] Recognize partial, transitive, and multi-valued dependencies
- [ ] Understand the 3NF vs BCNF trade-off

### Decomposition
- [ ] Test if decomposition is lossless
- [ ] Test if decomposition is dependency preserving
- [ ] Apply BCNF decomposition algorithm
- [ ] Apply 3NF synthesis algorithm

---

## 📚 Quick Reference Card (For Last-Minute Revision)

### Keys
```
Super Key ⊇ Candidate Key ⊇ Primary Key
Count per CK(k) in R(n): 2^(n-k)
Use inclusion-exclusion for multiple CKs
```

### Armstrong's Axioms
```
Reflexivity:   Y ⊆ X  →  X → Y
Augmentation:  X → Y  →  XZ → YZ
Transitivity:  X → Y, Y → Z  →  X → Z
```

### Operators (Minimal Set)
```
σ (select)  π (project)  ∪ (union)
− (diff)    × (product)  ρ (rename)
```

### Normal Forms
```
1NF: Atomic values only
2NF: No partial dependencies
3NF: X → A means X superkey OR A prime
BCNF: X → A means X superkey (no exceptions!)
```

### Decomposition
```
Lossless: R1 ∩ R2 is superkey of R1 or R2
DP: Each FD's attributes in same decomposed relation
3NF: Both always achievable
BCNF: Lossless always, DP not always
```

### TRC Quantifiers
```
∃ = "there exists" (some, any)
∀ = "for all" (every, each)
∀x P(x) ≡ ¬∃x ¬P(x)
```

---

**The Golden Rule**: When stuck on any FD/Key question, COMPUTE THE CLOSURE. X⁺ is the answer to most questions.

**Pro Tip**: Practice 5 closure computations daily for a week before your exam. Speed and accuracy will improve dramatically.

---

*These notes cover the complete Relational Model syllabus for GATE CSE and ESE. Master these concepts through understanding, not memorization.*
