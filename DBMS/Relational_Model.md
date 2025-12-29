# 🎯 Relational Model - Complete GATE & ESE Study Notes

> **The Ultimate A-Z Guide** - No fluff, no redundancy, pure concepts for acing your exam.

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

### 💡 What is Relational Model?

**Definition**: A data model where data is organized into **relations** (tables) consisting of **tuples** (rows) and **attributes** (columns).

**Proposed by**: E.F. Codd (1970) - IBM Research

### 🔑 Core Terminology

| Term | Meaning | Analogy |
|------|---------|---------|
| **Relation** | A table | Excel spreadsheet |
| **Tuple** | A row in the table | A single record |
| **Attribute** | A column header | A property/field |
| **Domain** | Set of allowed values for an attribute | Data type + constraints |
| **Degree** | Number of attributes | Number of columns |
| **Cardinality** | Number of tuples | Number of rows |
| **Schema** | Structure (column names + types) | Template |
| **Instance** | Actual data at a point in time | Snapshot |

### ⚡ Quick Facts

- **Relation is a SET of tuples** → No duplicate tuples allowed
- **Tuples are UNORDERED** → Order doesn't matter
- **Attributes are ATOMIC** → No composite/multivalued (1NF)
- **Each cell contains exactly ONE value**

### 🧠 GATE Trick

> **Q**: Max tuples in a relation with `n` attributes where domain of each attribute has `m` values?
> 
> **A**: m^n (Cartesian product of all domains)

---

## 2. Relation Schema & Instance

### Schema (Intension)

```
R(A₁, A₂, ..., Aₙ)
```

- **Static** - Doesn't change frequently
- Defines structure, not data
- Example: `Student(Roll_No, Name, Age, Department)`

### Instance (Extension)

- **Dynamic** - Changes with INSERT/UPDATE/DELETE
- Actual tuples at a given time
- Subset of Cartesian product of attribute domains

### 📐 Mathematical Definition

```
If D₁, D₂, ..., Dₙ are domains of attributes A₁, A₂, ..., Aₙ
Then relation r ⊆ D₁ × D₂ × ... × Dₙ
```

### 🎯 Example

**Schema**: `Employee(EmpID, Name, Salary, DeptID)`

**Instance**:
| EmpID | Name | Salary | DeptID |
|-------|------|--------|--------|
| 101 | Alice | 50000 | D1 |
| 102 | Bob | 60000 | D2 |

---

## 3. Keys - The Heart of Relational Model

### 🔐 Types of Keys (Hierarchy)

```
Super Key ⊇ Candidate Key ⊇ Primary Key
                ↓
           Alternate Key (remaining candidate keys)
```

### Definitions with Examples

**Relation**: `Student(Roll_No, Email, Name, Phone, Department)`

| Key Type | Definition | Example |
|----------|------------|---------|
| **Super Key** | Any set of attributes that uniquely identifies tuples | {Roll_No}, {Email}, {Roll_No, Name}, {Roll_No, Email, Phone} |
| **Candidate Key** | Minimal super key (no proper subset is a super key) | {Roll_No}, {Email} |
| **Primary Key** | Chosen candidate key for the table | {Roll_No} |
| **Alternate Key** | Candidate keys not chosen as primary | {Email} |
| **Foreign Key** | Attribute referencing primary key of another table | DeptID in Student referencing Dept(DeptID) |
| **Composite Key** | Key with more than one attribute | {Course_ID, Student_ID} in Enrollment |

### 🧮 Counting Keys - GATE Favorite!

**Formula for number of super keys**:

If a relation has:
- Candidate key of size `k`
- Total `n` attributes

Then, **Number of super keys containing this candidate key** = 2^(n-k)

### 🎯 GATE Example

**Q**: R(A, B, C, D, E) with candidate keys {AB} and {CD}. Find total super keys.

**Solution**:
- Super keys containing AB = 2^(5-2) = 2³ = 8
- Super keys containing CD = 2^(5-2) = 2³ = 8
- Super keys containing BOTH AB and CD = 2^(5-4) = 2¹ = 2

**Using Inclusion-Exclusion**:
Total = 8 + 8 - 2 = **14**

### ⚠️ Common Mistakes

1. **Primary Key ≠ Always Single Attribute** - Can be composite
2. **NULL not allowed in Primary Key**
3. **Foreign Key CAN be NULL** (unless specified NOT NULL)
4. **Foreign Key CAN reference same table** (Self-referential)

### 🔄 Foreign Key Properties

- Must reference a **primary key or unique key**
- Can have **different name** than referenced attribute
- Must have **compatible domain**
- Creates **referential integrity constraint**

---

## 4. Integrity Constraints

### Types of Constraints

| Constraint | Scope | Description |
|------------|-------|-------------|
| **Domain Constraint** | Single attribute | Values must belong to attribute's domain |
| **Key Constraint** | Single relation | No duplicate tuples, key must be unique |
| **Entity Integrity** | Single relation | Primary key cannot be NULL |
| **Referential Integrity** | Multiple relations | Foreign key must reference existing tuple or be NULL |
| **Semantic Constraint** | Application-level | Business rules (e.g., Age > 0) |

### 🎯 Referential Integrity Actions

When referenced tuple is DELETED or UPDATED:

| Action | Effect |
|--------|--------|
| **CASCADE** | Delete/Update all referencing tuples |
| **SET NULL** | Set foreign key to NULL |
| **SET DEFAULT** | Set foreign key to default value |
| **RESTRICT/NO ACTION** | Reject the operation |

### 💡 Example Scenario

```
Employee(EmpID PK, Name, DeptID FK → Dept)
Dept(DeptID PK, DeptName)
```

If we delete Dept 'D1':
- CASCADE → Delete all employees in D1
- SET NULL → Set DeptID = NULL for employees in D1
- RESTRICT → Don't allow deletion if employees exist

---

## 5. Relational Algebra

### 🧰 Complete Set of Operators

**Minimal/Fundamental Operators** (Can derive all others):
1. **σ** (Selection) - Select rows
2. **π** (Projection) - Select columns
3. **∪** (Union)
4. **−** (Set Difference)
5. **×** (Cartesian Product)
6. **ρ** (Rename)

**Derived Operators**:
- **⋈** (Join) = σ(×)
- **∩** (Intersection) = R − (R − S)
- **÷** (Division)

### 📝 Detailed Operators

#### σ (Selection/Restrict)

**Syntax**: σ_condition(R)

**Output**: Subset of tuples satisfying condition

**Properties**:
- Commutative: σ_c1(σ_c2(R)) = σ_c2(σ_c1(R))
- Cascade: σ_c1(σ_c2(R)) = σ_(c1 ∧ c2)(R)
- Output cardinality ≤ Input cardinality
- Output degree = Input degree

**Example**: σ_Salary>50000(Employee) → All employees with salary > 50000

#### π (Projection)

**Syntax**: π_A1,A2,...(R)

**Output**: Selected attributes only (removes duplicates!)

**Properties**:
- NOT commutative
- π_A(π_B(R)) = π_A(R) if A ⊆ B
- Output cardinality ≤ Input cardinality (due to duplicate removal)
- Output degree = Number of projected attributes

**Example**: π_Name,Salary(Employee) → Only Name and Salary columns

#### ∪ (Union)

**Requirement**: **Union Compatible** - Same degree, corresponding domains compatible

**Properties**:
- Commutative: R ∪ S = S ∪ R
- Associative: (R ∪ S) ∪ T = R ∪ (S ∪ T)
- Removes duplicates

#### − (Set Difference)

**Requirement**: Union Compatible

**Properties**:
- NOT commutative: R − S ≠ S − R
- NOT associative

**Example**: Students_CS − Students_Failed → CS students who haven't failed

#### × (Cartesian Product)

**Output**: Every tuple of R paired with every tuple of S

**Cardinality**: |R × S| = |R| × |S|

**Degree**: degree(R) + degree(S)

**Example**: 
- R has 5 tuples, S has 3 tuples
- R × S has 15 tuples

#### ρ (Rename)

**Syntax**: ρ_S(A1,A2,...)(R) - Rename relation to S with attributes A1, A2, ...

**Use Case**: Avoid ambiguity in self-joins

### 🔗 Join Operations

#### 1. Theta Join (θ-Join)

**Syntax**: R ⋈_θ S = σ_θ(R × S)

Any condition θ can be used.

#### 2. Equi Join

Special case of θ-join where condition uses only **equality (=)**.

#### 3. Natural Join (⋈)

**Definition**: Equi-join on **all common attributes** + **remove duplicate columns**

**Properties**:
- Commutative: R ⋈ S = S ⋈ R
- Associative: (R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)

**Cardinality**: 0 ≤ |R ⋈ S| ≤ |R| × |S|

**Special Cases**:
- If no common attributes: R ⋈ S = R × S
- If all attributes common and R = S: R ⋈ S = R

**GATE Trap**: Natural join on no common attributes → Cartesian product!

#### 4. Outer Joins

| Type | Preserves | NULL padding |
|------|-----------|--------------|
| **Left Outer (⟕)** | All tuples from LEFT | Right side |
| **Right Outer (⟖)** | All tuples from RIGHT | Left side |
| **Full Outer (⟗)** | ALL tuples from BOTH | Both sides |

#### 5. Semi Join (⋉)

**R ⋉ S** = π_R.*(R ⋈ S)

Returns only R's attributes for matching tuples.

**Use Case**: Distributed databases - reduce data transfer

#### 6. Anti Join (▷)

**R ▷ S** = R − (R ⋉ S)

Returns tuples from R that DON'T match with S.

### ➗ Division Operator (÷)

**The "FOR ALL" Operator** - Used for queries with "all", "every"

**Definition**: R(A, B) ÷ S(B) gives tuples in π_A(R) that are associated with **ALL** tuples in S.

**Formula**: R ÷ S = π_A(R) − π_A((π_A(R) × S) − R)

**Example Query**: "Find students who have taken ALL courses"
```
Enrollment(StudentID, CourseID) ÷ Course(CourseID)
```

### 🎯 GATE Cardinality Formulas

| Operation | Min Cardinality | Max Cardinality |
|-----------|----------------|-----------------|
| R ∪ S | max(|R|, |S|) | |R| + |S| |
| R ∩ S | 0 | min(|R|, |S|) |
| R − S | |R| − |S| (or 0) | |R| |
| R × S | |R| × |S| | |R| × |S| |
| R ⋈ S | 0 | |R| × |S| |
| σ(R) | 0 | |R| |
| π(R) | 1 (if R non-empty) | |R| |

### 🧠 Operator Precedence (High to Low)

1. σ, π, ρ (Unary)
2. ×, ⋈
3. ∩
4. ∪, −

---

## 6. Tuple Relational Calculus (TRC)

### 📝 Syntax

```
{ t | P(t) }
```
- t = tuple variable
- P(t) = predicate/condition

### Quantifiers

| Symbol | Meaning | Example |
|--------|---------|---------|
| ∃ (Existential) | "There exists" | ∃t ∈ R(condition) |
| ∀ (Universal) | "For all" | ∀t ∈ R(condition) |

### ⚡ Conversion Rules

- ∀x P(x) ≡ ¬∃x ¬P(x)
- ∃x P(x) ≡ ¬∀x ¬P(x)

### 🎯 Examples

**1. Find all employees in IT department**
```
{ t | t ∈ Employee ∧ t.Dept = 'IT' }
```

**2. Find employees earning more than someone in IT**
```
{ t | t ∈ Employee ∧ ∃s ∈ Employee (s.Dept = 'IT' ∧ t.Salary > s.Salary) }
```

**3. Find employees earning more than ALL employees in IT**
```
{ t | t ∈ Employee ∧ ∀s ∈ Employee (s.Dept ≠ 'IT' ∨ t.Salary > s.Salary) }
```

### ⚠️ Safe Expressions

A TRC expression is **safe** if it guarantees a **finite result**.

**Unsafe Example**: { t | ¬(t ∈ Employee) } → Infinite result!

**Rule**: Limit tuple variables to tuples appearing in relations.

---

## 7. Domain Relational Calculus (DRC)

### 📝 Syntax

```
{ <x₁, x₂, ..., xₙ> | P(x₁, x₂, ..., xₙ) }
```
- Variables represent domain values (not entire tuples)

### 🎯 Example

**Find names and salaries of employees in IT**
```
{ <n, s> | ∃e ∃d (Employee(e, n, s, d) ∧ d = 'IT') }
```

### TRC vs DRC vs Relational Algebra

| Feature | Relational Algebra | TRC | DRC |
|---------|-------------------|-----|-----|
| Nature | Procedural | Declarative | Declarative |
| Variables | - | Tuple | Domain |
| Specifies | HOW | WHAT | WHAT |
| Power | Equivalent | Equivalent | Equivalent |

**Codd's Theorem**: All three have **equivalent expressive power**.

---

## 8. Normalization

### 🎯 Purpose

- Eliminate **Redundancy**
- Prevent **Update Anomalies**
- Preserve **Data Integrity**

### Types of Anomalies

| Anomaly | Description | Example |
|---------|-------------|---------|
| **Insertion** | Can't insert without other data | Can't add course without enrolled student |
| **Deletion** | Unintended data loss | Deleting last student deletes course info |
| **Update** | Inconsistent modifications | Updating course name in one row, not others |

### 📊 Normal Forms Hierarchy

```
1NF ⊂ 2NF ⊂ 3NF ⊂ BCNF ⊂ 4NF ⊂ 5NF
```

### 1NF (First Normal Form)

**Rule**: All attributes must be **ATOMIC** (single-valued)

**Violation**: Multi-valued or composite attributes

**Example**:
```
❌ Student(ID, Name, Phones[])
✓ Student(ID, Name) + StudentPhone(ID, Phone)
```

### 2NF (Second Normal Form)

**Rule**: 1NF + No **Partial Dependency**

**Partial Dependency**: Non-prime attribute depends on PART of a candidate key

**Applies to**: Tables with composite candidate keys

**Example**:
```
❌ OrderItem(OrderID, ProductID, ProductName, Qty)
   ProductName depends only on ProductID (partial dependency)

✓ OrderItem(OrderID, ProductID, Qty)
   Product(ProductID, ProductName)
```

**Trick**: If all candidate keys are single-attribute → Already in 2NF!

### 3NF (Third Normal Form)

**Rule**: 2NF + No **Transitive Dependency**

**Transitive Dependency**: A → B → C where B is non-prime

**Definition (Formal)**: For every FD X → A:
- X is a superkey, OR
- A is a prime attribute (part of some candidate key)

**Example**:
```
❌ Employee(EmpID, DeptID, DeptName)
   EmpID → DeptID → DeptName (transitive)

✓ Employee(EmpID, DeptID)
   Department(DeptID, DeptName)
```

### BCNF (Boyce-Codd Normal Form)

**Rule**: For every FD X → Y, X must be a **superkey**

**Difference from 3NF**: No exception for prime attributes!

**Example where 3NF ≠ BCNF**:
```
R(Student, Subject, Teacher)
FDs: {Student, Subject} → Teacher
     Teacher → Subject

Candidate Key: {Student, Subject}

3NF? Yes (Teacher → Subject has Subject as prime attribute)
BCNF? No (Teacher is not a superkey)

Decompose to BCNF:
R1(Teacher, Subject)
R2(Student, Teacher)
```

### 4NF (Fourth Normal Form)

**Rule**: BCNF + No **Multi-valued Dependencies** (except those implied by superkeys)

**Multi-valued Dependency (MVD)**: X ↠ Y means for each X value, there's a fixed set of Y values independent of other attributes.

**Example**:
```
❌ Employee(EmpID, Skill, Hobby)
   EmpID ↠ Skill (skills independent of hobbies)
   EmpID ↠ Hobby

✓ EmpSkill(EmpID, Skill)
   EmpHobby(EmpID, Hobby)
```

### 5NF (Fifth Normal Form / PJNF)

**Rule**: 4NF + No **Join Dependencies** (except those implied by candidate keys)

**Join Dependency**: R can be losslessly decomposed into R1, R2, ... Rn

**Rare in practice** - Mostly theoretical.

### 🎯 Quick Comparison Table

| NF | Eliminates | Key Test |
|----|------------|----------|
| 1NF | Non-atomic values | All values atomic? |
| 2NF | Partial dependencies | Non-prime fully depends on entire key? |
| 3NF | Transitive dependencies | X→A: X superkey OR A prime? |
| BCNF | All non-trivial FD violations | X→Y: X superkey? |
| 4NF | Multi-valued dependencies | X↠Y: X superkey? |

### 🧠 GATE Shortcut

**To check BCNF quickly**:
1. Find all candidate keys
2. For each FD X → Y, check if X is a superkey
3. If ANY X is not a superkey → Not in BCNF

---

## 9. Functional Dependencies

### 📝 Definition

**X → Y**: Value of X uniquely determines value of Y

**Trivial FD**: X → Y where Y ⊆ X (Always true!)

### Armstrong's Axioms (RAT)

| Axiom | Name | Rule |
|-------|------|------|
| **Reflexivity** | - | If Y ⊆ X, then X → Y |
| **Augmentation** | - | If X → Y, then XZ → YZ |
| **Transitivity** | - | If X → Y and Y → Z, then X → Z |

**These are SOUND and COMPLETE** (derive all valid FDs, only valid FDs)

### Derived Rules

| Rule | Derivation |
|------|------------|
| **Union** | X → Y, X → Z ⟹ X → YZ |
| **Decomposition** | X → YZ ⟹ X → Y, X → Z |
| **Pseudo-transitivity** | X → Y, WY → Z ⟹ WX → Z |

### 🔑 Closure of Attributes (X⁺)

**Definition**: Set of ALL attributes functionally determined by X

**Algorithm**:
```
X⁺ = X
repeat
    for each FD Y → Z in F
        if Y ⊆ X⁺ then X⁺ = X⁺ ∪ Z
until no change
```

**Use Cases**:
1. **Find candidate keys**: X⁺ = all attributes → X is superkey
2. **Check if FD holds**: X → Y holds iff Y ⊆ X⁺

### 🎯 GATE Example: Finding Candidate Keys

**R(A, B, C, D, E)** with FDs: {A → B, BC → E, ED → A}

**Step 1**: Find attributes that NEVER appear on RHS → Must be in every key
- RHS: {B, E, A}
- Never on RHS: {C, D}
- CD must be in every candidate key

**Step 2**: Compute (CD)⁺
- CD⁺ = {C, D} (initially)
- No FD has C or D alone on LHS
- CD⁺ = {C, D} → Not a superkey

**Step 3**: Try adding one attribute
- ACD⁺: A → B, so {A,C,D,B}, BC → E, so {A,B,C,D,E} ✓
- BCD⁺: BC → E, so {B,C,D,E}, ED → A, so {A,B,C,D,E} ✓

**Candidate Keys**: {ACD, BCD}

### Canonical Cover (Minimal Cover)

**Properties**:
1. No extraneous attributes on LHS
2. No redundant FDs
3. Equivalent to original set

**Algorithm**:
1. Apply decomposition rule (single attribute on RHS)
2. Remove extraneous attributes from LHS
3. Remove redundant FDs

### Prime vs Non-Prime Attributes

- **Prime Attribute**: Appears in SOME candidate key
- **Non-Prime Attribute**: Doesn't appear in ANY candidate key

---

## 10. Decomposition

### 🎯 Goals of Decomposition

1. **Lossless Join** (MUST have)
2. **Dependency Preserving** (Desirable)
3. **Achieve desired normal form**

### Lossless Join Decomposition

**Definition**: R decomposed into R1, R2 is lossless iff:
```
R = R1 ⋈ R2 (natural join recovers original)
```

**Test (Binary Decomposition)**:
R1 ∩ R2 → R1 or R1 ∩ R2 → R2 must hold

**In other words**: Common attributes must be a superkey in at least one decomposition.

### 🎯 GATE Example

**R(A, B, C)** with FD: A → B

Decompose into:
- R1(A, B)
- R2(A, C)

**Test**: R1 ∩ R2 = {A}
- Does A → R1(A,B)? A → B means A → AB ✓
- **Lossless!**

Alternative decomposition:
- R1(A, B)
- R2(B, C)

**Test**: R1 ∩ R2 = {B}
- Does B → A or B → C? Neither given!
- **Lossy!**

### Dependency Preserving Decomposition

**Definition**: All original FDs can be verified using decomposed relations.

**Test**: F⁺ = (F1 ∪ F2 ∪ ... ∪ Fn)⁺

**BCNF Trade-off**: BCNF decomposition may NOT be dependency preserving!

### 🎯 Key Theorems

| Normal Form | Lossless | Dependency Preserving |
|-------------|----------|----------------------|
| 3NF | Always achievable | Always achievable |
| BCNF | Always achievable | NOT always achievable |

### Decomposition Algorithm for BCNF

```
while (R is not in BCNF):
    Find FD X → Y that violates BCNF
    Decompose R into:
        R1 = X ∪ Y
        R2 = R - (Y - X)  // R minus Y's non-key attributes
```

### Decomposition Algorithm for 3NF

**Synthesis Algorithm**:
1. Find canonical cover Fc
2. For each FD X → Y in Fc, create relation XY
3. If no relation contains a candidate key, add one
4. Remove redundant relations

---

## 11. GATE PYQ Patterns & Tricks

### 🎯 Most Asked Topics (Priority Order)

1. **Candidate Keys & Super Keys Counting**
2. **Normal Form Identification**
3. **Relational Algebra Queries**
4. **Lossless Decomposition Check**
5. **FD Closure Computation**

### ⚡ Speed Tricks

#### Trick 1: Finding Candidate Keys Fast

1. Find attributes ONLY on LHS → Must be in every key
2. Find attributes ONLY on RHS → Never in any key
3. Find attributes on BOTH sides → May or may not be in key
4. Start with LHS-only, compute closure, add others if needed

#### Trick 2: Super Key Counting

**Formula**: If CK has k attributes in n-attribute relation:
- Super keys containing this CK = 2^(n-k)

**Multiple CKs**: Use inclusion-exclusion!

#### Trick 3: Quick Normal Form Check

1. **BCNF Check**: Every LHS of FD is superkey? → BCNF
2. **3NF but not BCNF**: RHS has prime attribute, LHS not superkey
3. **2NF but not 3NF**: Transitive dependency exists
4. **1NF but not 2NF**: Partial dependency exists

#### Trick 4: Natural Join Cardinality

- **Foreign Key Join**: |R ⋈ S| = |R| (if R has FK to S)
- **No matching values**: |R ⋈ S| = 0
- **All values match (1:1)**: |R ⋈ S| = |R| = |S|

#### Trick 5: Division Query Recognition

**Keywords**: "all", "every", "must have all"

Example: "Find students enrolled in ALL courses" → Division!

### 📝 Common GATE Traps

1. **Confusing 3NF and BCNF**
   - 3NF allows prime attributes on RHS
   - BCNF doesn't!

2. **Assuming Lossless = Dependency Preserving**
   - They're independent properties!

3. **Natural Join with No Common Attributes**
   - Result = Cartesian Product (not empty!)

4. **Forgetting to Check ALL Candidate Keys**
   - Must check ALL FDs against ALL candidate keys for BCNF

5. **Missing Self-Referential Foreign Keys**
   - Employee(EmpID, ManagerID) where ManagerID → EmpID

### 🧮 Important Formulas Summary

| Concept | Formula |
|---------|---------|
| Max tuples | Product of domain sizes |
| Super keys from CK(k) in R(n) | 2^(n-k) |
| Cartesian product cardinality | \|R\| × \|S\| |
| Projection cardinality | ≤ \|R\| |
| Selection cardinality | ≤ \|R\| |
| Natural join cardinality | 0 to \|R\| × \|S\| |

### 📊 Decision Flowchart

```
Is R in BCNF?
│
├─ For each FD X → Y:
│  └─ Is X a superkey?
│     ├─ Yes → Continue
│     └─ No → NOT BCNF
│              │
│              ├─ Is Y prime? 
│              │  ├─ Yes → 3NF (not BCNF)
│              │  └─ No → Check 2NF
│              │          │
│              │          ├─ Is X proper subset of CK?
│              │          │  ├─ Yes → NOT 2NF
│              │          │  └─ No → 2NF (not 3NF)
```

---

## 🎓 Final Revision Checklist

- [ ] Can identify all types of keys
- [ ] Can compute attribute closure
- [ ] Can find all candidate keys
- [ ] Can count super keys using formula
- [ ] Know all relational algebra operators
- [ ] Can write TRC/DRC expressions
- [ ] Can identify normal form (1NF through BCNF)
- [ ] Can check lossless decomposition
- [ ] Can check dependency preservation
- [ ] Know the synthesis algorithm for 3NF
- [ ] Know the decomposition algorithm for BCNF

---

## 📚 Quick Reference Card

### Keys
```
Super Key ⊇ Candidate Key ⊇ Primary Key
Super Key Count = 2^(n-k) per candidate key
```

### Operators (Minimal Set)
```
σ π ∪ − × ρ
```

### Normal Forms
```
1NF: Atomic values
2NF: No partial dependency
3NF: No transitive dependency (or RHS is prime)
BCNF: LHS is always superkey
```

### Decomposition Tests
```
Lossless: R1 ∩ R2 is superkey of R1 or R2
Dependency Preserving: F⁺ = (F1 ∪ F2)⁺
```

### Armstrong's Axioms
```
Reflexivity: Y ⊆ X → X → Y
Augmentation: X → Y → XZ → YZ
Transitivity: X → Y, Y → Z → X → Z
```

---

**Pro Tip**: Practice closure computation daily - it's the foundation for a significant portion of GATE questions on this topic!

**Remember**: When in doubt, compute the closure! X⁺ solves most problems.

---

*Last Updated: 2024 | For GATE CSE & ESE*
