# Database Design and Normalization - Complete GATE & ESE Guide

> **Master Document for GATE CSE & ESE** | Database Design, Functional Dependencies, Normal Forms, Decomposition

---

## Table of Contents

1. [Why Database Design Matters](#1-why-database-design-matters)
2. [Functional Dependencies (FD)](#2-functional-dependencies-fd)
3. [Closure of Attributes (X⁺)](#3-closure-of-attributes-x)
4. [Armstrong's Axioms](#4-armstrongs-axioms)
5. [Keys - The Foundation](#5-keys---the-foundation)
6. [Canonical Cover (Minimal Cover)](#6-canonical-cover-minimal-cover)
7. [Normal Forms - The Heart of Normalization](#7-normal-forms---the-heart-of-normalization)
8. [Decomposition](#8-decomposition)
9. [Denormalization](#9-denormalization)
10. [GATE Shortcuts & Tricks](#10-gate-shortcuts--tricks)
11. [Practice Problems with Solutions](#11-practice-problems-with-solutions)
12. [Quick Revision Checklist](#12-quick-revision-checklist)

---

## 1. Why Database Design Matters

### The Problem: Data Anomalies

Consider a table `StudentCourse`:

| StudentID | StudentName | CourseID | CourseName | Instructor |
|-----------|-------------|----------|------------|------------|
| 101 | Alice | CS101 | DBMS | Dr. Smith |
| 101 | Alice | CS102 | OS | Dr. Jones |
| 102 | Bob | CS101 | DBMS | Dr. Smith |

**Three deadly anomalies arise:**

| Anomaly | What Happens | Example |
|---------|--------------|---------|
| **Insertion Anomaly** | Can't insert data without unrelated data | Can't add new course without a student enrolled |
| **Deletion Anomaly** | Deleting one fact removes unrelated facts | Deleting Bob removes CS101-Dr.Smith link |
| **Update Anomaly** | Must update same fact in multiple places | Changing "Dr. Smith" requires updating all rows |

> **🎯 Analogy:** Think of a messy room where your books, clothes, and food are all in one pile. Finding or changing anything becomes a nightmare. Normalization is like organizing into separate drawers.

### The Solution: Normalization

**Normalization** = Decomposing a relation into smaller, well-structured relations to eliminate redundancy and anomalies.

---

## 2. Functional Dependencies (FD)

### Definition

A **Functional Dependency** X → Y means: *If two tuples have the same value for X, they MUST have the same value for Y.*

> **🎯 Analogy:** Roll_Number → Student_Name is like saying "If you know someone's Aadhaar number, you can determine their name." The Aadhaar number *functionally determines* the name.

### Types of FDs

| Type | Definition | Example |
|------|------------|---------|
| **Trivial FD** | Y ⊆ X | AB → A, AB → B, AB → AB |
| **Non-trivial FD** | Y ⊄ X | AB → C (C is not in AB) |
| **Completely Non-trivial** | X ∩ Y = ∅ | AB → CD (no overlap) |
| **Partial FD** | X → Y where proper subset of X can determine Y | If AB → C and A → C, then AB → C is partial |
| **Full FD** | X → Y where no proper subset of X can determine Y | AB → C where neither A → C nor B → C |
| **Transitive FD** | X → Y → Z (Y is not a key, Y ↛ X) | Roll → Dept, Dept → HOD implies Roll → HOD transitively |

### Identifying FDs from Real-World Scenarios

**Universal Rule:** An FD X → Y holds if and only if X is a **determinant** for Y in all possible instances.

| Scenario | FD | Reasoning |
|----------|-----|-----------|
| Employee table | EmpID → Name, Salary, DeptID | EmpID uniquely identifies employee |
| Order system | OrderID → OrderDate, CustomerID | Each order has one date and customer |
| Student enrollment | (StudentID, CourseID) → Grade | A student has one grade per course |

### ⚠️ GATE Trap: FDs vs Data

FDs are **schema-level constraints**, not just observations from current data!

```
Current data might show: City → State (all cities in data belong to unique states)
But FDs must hold for ALL possible data: 
Springfield exists in Illinois AND Massachusetts → City ↛ State
```

---

## 3. Closure of Attributes (X⁺)

### Definition

**Closure of X (X⁺)** = Set of all attributes that can be functionally determined from X using given FDs.

### Algorithm to Find X⁺

```
INPUT: Set of FDs F, attribute set X
OUTPUT: X⁺

1. Initialize: X⁺ = X
2. REPEAT:
   For each FD (A → B) in F:
     If A ⊆ X⁺ then X⁺ = X⁺ ∪ B
3. UNTIL: X⁺ doesn't change
4. RETURN X⁺
```

### Worked Example

**Given:** R(A, B, C, D, E) with FDs: A → B, BC → D, E → C, D → A

**Find:** (AE)⁺

| Step | X⁺ | FD Applied | Reason |
|------|-----|------------|--------|
| Init | {A, E} | - | Start with AE |
| 1 | {A, E, B} | A → B | A ⊆ {A,E} |
| 2 | {A, E, B, C} | E → C | E ⊆ {A,E,B} |
| 3 | {A, E, B, C, D} | BC → D | BC ⊆ {A,E,B,C} |
| Final | {A, B, C, D, E} | - | Contains all attributes |

**(AE)⁺ = {A, B, C, D, E}** → AE is a **superkey** (determines all attributes)

### Key Applications of Closure

| Purpose | How to Use Closure |
|---------|-------------------|
| Check if X → Y | Y ⊆ X⁺ ? |
| Check if X is superkey | X⁺ = R (all attributes)? |
| Find candidate key | Minimal X where X⁺ = R |

---

## 4. Armstrong's Axioms

### The Three Core Axioms (RAT)

These are **sound** (never produce wrong FDs) and **complete** (can derive all valid FDs).

| Axiom | Rule | Example |
|-------|------|---------|
| **Reflexivity** | If Y ⊆ X, then X → Y | AB → A, AB → B |
| **Augmentation** | If X → Y, then XZ → YZ | A → B implies AC → BC |
| **Transitivity** | If X → Y and Y → Z, then X → Z | A → B, B → C implies A → C |

### Derived Rules (Time-Savers)

| Rule | Formula | Derivation |
|------|---------|------------|
| **Union** | X → Y, X → Z ⟹ X → YZ | Augment + Transitivity |
| **Decomposition** | X → YZ ⟹ X → Y, X → Z | Reflexivity + Transitivity |
| **Pseudo-transitivity** | X → Y, WY → Z ⟹ WX → Z | Augment + Transitivity |

> **🎯 Memory Trick:** RAT for core (Reflexive, Augmentation, Transitivity), then U-D-P for derived (Union, Decomposition, Pseudo-transitivity)

### Why Armstrong's Axioms Matter for GATE

1. **Proving FDs:** Show if an FD can be derived from given FDs
2. **Finding Closure of FD Set (F⁺):** All FDs derivable from F
3. **Equivalence of FD Sets:** Two sets F and G are equivalent if F⁺ = G⁺

---

## 5. Keys - The Foundation

### Key Hierarchy

```
┌─────────────────────────────────────────────────────┐
│                    SUPER KEY                        │
│   (Any set of attributes that uniquely identifies)  │
│                                                     │
│    ┌───────────────────────────────────────────┐   │
│    │           CANDIDATE KEY                    │   │
│    │   (Minimal superkey - no proper subset    │   │
│    │    is also a superkey)                    │   │
│    │                                           │   │
│    │    ┌─────────────────────────────────┐   │   │
│    │    │       PRIMARY KEY                │   │   │
│    │    │   (Chosen candidate key)         │   │   │
│    │    └─────────────────────────────────┘   │   │
│    └───────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Definitions

| Key Type | Definition | Example |
|----------|------------|---------|
| **Super Key** | Any attribute set whose closure = all attributes | {AB, ABC, ABCD...} if AB is key |
| **Candidate Key** | Minimal superkey (remove any attribute, no longer superkey) | {AB} if neither A nor B alone is key |
| **Primary Key** | Chosen candidate key for the table | One of the candidate keys |
| **Prime Attribute** | Attribute that is part of ANY candidate key | If CKs are {AB, CD}, prime attrs = {A,B,C,D} |
| **Non-Prime Attribute** | Attribute NOT part of any candidate key | All others |

### Algorithm to Find Candidate Keys

**Step 1:** Categorize attributes
- **L (Left only):** Appear only on LHS of FDs - MUST be in every CK
- **R (Right only):** Appear only on RHS of FDs - NEVER in any CK
- **LR (Both sides):** May or may not be in CK
- **N (Neither side):** MUST be in every CK

**Step 2:** Start with L ∪ N (mandatory attributes)

**Step 3:** If (L ∪ N)⁺ = R, then L ∪ N is the only CK

**Step 4:** If not, try adding LR attributes one by one

### Worked Example: Finding Candidate Keys

**Given:** R(A, B, C, D, E) with FDs: A → BC, CD → E, B → D, E → A

**Step 1: Categorize**
| Position | Attributes |
|----------|------------|
| L (left only) | None (all that appear left also appear right) |
| R (right only) | None |
| LR (both) | A, B, C, D, E |
| N (neither) | None |

**Step 2:** L ∪ N = {} → Need to check each attribute

**Step 3: Find closures**
- A⁺: A → BC → D (B→D) → E (CD→E) = {A,B,C,D,E} ✓ A is superkey
- B⁺: B → D = {B,D} ✗ 
- C⁺: {C} ✗
- D⁺: {D} ✗
- E⁺: E → A → BC → D = {A,B,C,D,E} ✓ E is superkey

**Candidate Keys:** {A} and {E} (both minimal)

### Formula: Number of Super Keys

If candidate key has k attributes and relation has n total attributes:

**Number of superkeys = 2^(n-k)**

*Reason:* Any superset of CK is a superkey. There are (n-k) non-key attributes, each can be included or not.

**If multiple candidate keys exist:**
Use **Inclusion-Exclusion Principle**:

If CK1 has k₁ attrs, CK2 has k₂ attrs, their intersection has c attrs:
- Superkeys from CK1 = 2^(n-k₁)
- Superkeys from CK2 = 2^(n-k₂)
- Common superkeys (containing both) = 2^(n-k₁-k₂+c)

**Total = 2^(n-k₁) + 2^(n-k₂) - 2^(n-k₁-k₂+c)**

---

## 6. Canonical Cover (Minimal Cover)

### Definition

**Canonical Cover (Fc)** of FD set F is a minimal equivalent FD set where:
1. Every FD has a **single attribute** on RHS
2. No **extraneous attributes** on LHS
3. No **redundant FDs**
4. Fc⁺ = F⁺ (equivalent to original)

### Algorithm

```
STEP 1: Decompose RHS (make all FDs have single RHS)
        A → BC becomes A → B, A → C

STEP 2: Remove extraneous LHS attributes
        For each FD X → A, for each attribute B in X:
        Check if (X - B)⁺ contains A
        If yes, B is extraneous → remove it

STEP 3: Remove redundant FDs
        For each FD X → A:
        Check if X⁺ (using remaining FDs) contains A
        If yes, FD is redundant → remove it
```

### Worked Example

**Given:** F = {A → BC, B → C, AB → D}

**Step 1: Decompose RHS**
- A → B
- A → C
- B → C
- AB → D

**Step 2: Check extraneous LHS attributes**
- In AB → D: Is A extraneous? Check B⁺ = {B, C} ✗ (D not in B⁺)
- Is B extraneous? Check A⁺ = {A, B, C} ✗ (D not in A⁺)
- Neither extraneous, keep AB → D

**Step 3: Remove redundant FDs**
- A → B: Remove temporarily. A⁺ = {A, C} (using remaining). B ∉ A⁺. NOT redundant.
- A → C: Remove temporarily. A⁺ = {A, B, C} (A→B, B→C). C ∈ A⁺. **REDUNDANT - REMOVE**
- B → C: Keep
- AB → D: Keep

**Canonical Cover: {A → B, B → C, AB → D}**

> **🎯 Trick:** Always process in order: Decompose → Simplify LHS → Remove Redundant

---

## 7. Normal Forms - The Heart of Normalization

### Overview Map

```
┌─────────────────────────────────────────────────────────────────┐
│  1NF: Atomic values, no repeating groups                       │
│    ↓                                                            │
│  2NF: 1NF + No partial dependency on candidate key              │
│    ↓                                                            │
│  3NF: 2NF + No transitive dependency                            │
│    ↓                                                            │
│  BCNF: For every X → Y, X is superkey                           │
│    ↓                                                            │
│  4NF: BCNF + No multi-valued dependencies                       │
│    ↓                                                            │
│  5NF: 4NF + No join dependencies                                │
└─────────────────────────────────────────────────────────────────┘
```

---

### 7.1 First Normal Form (1NF)

#### Definition
A relation is in **1NF** if:
- All attributes have **atomic (indivisible) values**
- No **repeating groups** or arrays

#### Violation Example

| EmpID | Name | Phone |
|-------|------|-------|
| 101 | Alice | 9876, 1234 |  ← Violates 1NF (multi-valued)

#### Fix: Separate rows or separate table

| EmpID | Name | Phone |
|-------|------|-------|
| 101 | Alice | 9876 |
| 101 | Alice | 1234 |

**OR** create EmpPhone(EmpID, Phone) table.

> **🎯 1NF Memory:** "One value per cell"

---

### 7.2 Second Normal Form (2NF)

#### Definition
A relation is in **2NF** if:
- It is in 1NF
- **No partial dependency**: No non-prime attribute depends on a proper subset of any candidate key

> **Key Insight:** 2NF only matters when candidate key is **composite** (multiple attributes)

#### Violation Example

**StudentCourse**(StudentID, CourseID, StudentName, CourseName)
- CK: (StudentID, CourseID)
- StudentID → StudentName ← **Partial dependency!** (StudentName depends on part of key)
- CourseID → CourseName ← **Partial dependency!**

#### Fix: Decompose

```
Student(StudentID, StudentName)
Course(CourseID, CourseName)  
Enrollment(StudentID, CourseID)
```

> **🎯 2NF Memory:** "Whole key, nothing but the key" (for non-prime attributes)

#### Quick Test for 2NF
1. Find all candidate keys
2. If ALL candidate keys are single-attribute → Automatically 2NF
3. Else, check if any non-prime attribute depends on part of any candidate key

---

### 7.3 Third Normal Form (3NF)

#### Definition
A relation is in **3NF** if for every non-trivial FD X → A:
- **X is a superkey**, OR
- **A is a prime attribute** (part of some candidate key)

> **🎯 Alternative Definition:** No non-prime attribute transitively depends on any candidate key

#### Violation Example

**Employee**(EmpID, DeptID, DeptName)
- CK: EmpID
- EmpID → DeptID (OK - EmpID is superkey)
- DeptID → DeptName ← **3NF violation!** (DeptID not superkey, DeptName not prime)

This is a **transitive dependency**: EmpID → DeptID → DeptName

#### Fix: Decompose

```
Employee(EmpID, DeptID)
Department(DeptID, DeptName)
```

> **🎯 3NF Memory:** "Nothing but the key, so help me Codd" (Edgar F. Codd invented the relational model) - non-prime attributes depend ONLY on keys, not on other non-prime attributes

#### 3NF vs 2NF Relationship

| Property | 2NF | 3NF |
|----------|-----|-----|
| Partial dependency of non-prime on CK | ✗ Not allowed | ✗ Not allowed |
| Transitive dependency | Allowed | ✗ Not allowed |
| Subset relationship | - | 3NF ⊂ 2NF (every 3NF is 2NF) |

---

### 7.4 Boyce-Codd Normal Form (BCNF)

#### Definition
A relation is in **BCNF** if for every non-trivial FD X → Y:
- **X is a superkey**

> **🎯 BCNF = Stronger 3NF** (no exception for prime attributes)

#### Difference from 3NF

| Normal Form | For X → A (non-trivial) | Exception |
|-------------|-------------------------|-----------|
| 3NF | X is superkey OR A is prime | Yes - prime attr exception |
| BCNF | X is superkey | No exceptions |

#### When 3NF ≠ BCNF

This happens when a **prime attribute** depends on a **non-superkey**.

**Example:**
R(Student, Subject, Teacher) with FDs:
- (Student, Subject) → Teacher (Each student has one teacher per subject)
- Teacher → Subject (Each teacher teaches only one subject)

CK: (Student, Subject) and (Student, Teacher)
Prime attributes: {Student, Subject, Teacher}

Check Teacher → Subject:
- 3NF: Teacher not superkey, but Subject IS prime → **3NF satisfied**
- BCNF: Teacher not superkey → **BCNF violated**

#### BCNF Decomposition Algorithm

```
while (some Ri is not in BCNF):
    Find X → Y that violates BCNF in Ri
    Decompose Ri into:
        R1 = X ∪ Y (the violating FD's attributes)
        R2 = Ri - Y (remaining attributes with X)
```

**For above example:**
- Violating FD: Teacher → Subject
- Decompose: 
  - R1(Teacher, Subject)
  - R2(Student, Teacher)

---

### 7.5 Fourth Normal Form (4NF)

#### Multi-Valued Dependencies (MVD)

**MVD X ↠ Y** means: For a given X, the set of Y values is independent of other attributes.

**Definition:** X ↠ Y holds if whenever two tuples agree on X, we can swap their Y values and get valid tuples.

#### Formal Definition of 4NF
A relation is in **4NF** if for every non-trivial MVD X ↠ Y:
- **X is a superkey**

#### Example of 4NF Violation

**EmpSkillHobby**(EmpID, Skill, Hobby)

| EmpID | Skill | Hobby |
|-------|-------|-------|
| 101 | Java | Chess |
| 101 | Java | Music |
| 101 | Python | Chess |
| 101 | Python | Music |

Here: EmpID ↠ Skill and EmpID ↠ Hobby (skills and hobbies are independent)

But EmpID is not a superkey → **4NF violated**

#### Fix: Decompose

```
EmpSkill(EmpID, Skill)
EmpHobby(EmpID, Hobby)
```

> **🎯 4NF Memory:** "Independent facts in independent tables"

---

### 7.6 Fifth Normal Form (5NF) / PJNF

#### Join Dependencies

A relation R satisfies **join dependency** JD*(R1, R2, ..., Rn) if R can be reconstructed by joining R1, R2, ..., Rn.

#### Definition of 5NF
A relation is in **5NF** if every non-trivial join dependency is implied by candidate keys.

> **🎯 GATE Reality:** 5NF is rarely tested. Focus on 1NF-BCNF.

---

### Normal Forms Comparison Table

| NF | Condition | Violation Pattern |
|----|-----------|-------------------|
| 1NF | Atomic values | Multi-valued attributes |
| 2NF | 1NF + No partial deps | Part of CK → Non-prime |
| 3NF | 2NF + No transitive deps | Non-prime → Non-prime |
| BCNF | For all X→Y, X is superkey | Non-superkey → Anything |
| 4NF | BCNF + No MVD violations | X ↠ Y where X not superkey |
| 5NF | 4NF + No JD violations | Rare in exams |

---

## 8. Decomposition

### Two Critical Properties

Any decomposition must be evaluated for:

1. **Lossless Join Property** - Can we reconstruct original data?
2. **Dependency Preservation** - Can we check all FDs on decomposed tables?

---

### 8.1 Lossless Join (LJ) Decomposition

#### Definition
Decomposition of R into R1 and R2 is **lossless** if:

**R1 ⋈ R2 = R** (joining back gives exactly original, no extra tuples)

#### Test for Lossless Join (Binary Decomposition)

Decomposition of R into R1 and R2 is lossless if and only if:

**(R1 ∩ R2) → (R1 - R2)** OR **(R1 ∩ R2) → (R2 - R1)**

> **🎯 In simple terms:** The common attributes must be a key in at least one of the decomposed relations.

#### Example

R(A, B, C) with FD: A → B

Decompose into: R1(A, B), R2(A, C)

Check: R1 ∩ R2 = {A}
- A → B? Yes (given)
- A → (R1 - R2)? A → B? **Yes!**

**Lossless: ✓**

#### Chase Algorithm (For n-way decomposition)

For decompositions into more than 2 relations, use the **Chase Algorithm**:

```
1. Create a table with one row per Ri, columns = attributes of R
2. Initialize: for row i, if attribute A ∈ Ri, put 'a' (subscript i optional)
               else put 'b' with subscript i
3. Apply FDs: If X → Y, and two rows agree on X, make their Y values same 
   (prefer 'a' over 'b')
4. If any row becomes all 'a's → Lossless
5. If no changes possible and no all-'a' row → Lossy
```

---

### 8.2 Dependency Preserving (DP) Decomposition

#### Definition
A decomposition **preserves dependencies** if all original FDs can be checked using only the decomposed relations (without joining).

#### Test for DP

1. For each decomposed relation Ri, find FDs whose attributes are all in Ri
2. Let F' = union of all such FDs
3. Decomposition is DP if F'⁺ = F⁺

> **🎯 Simpler Test:** For each FD X → Y in F, check if it can be derived from F'

#### Example: DP Check

R(A, B, C) with F = {A → B, B → C}

Decompose into: R1(A, B), R2(B, C)

FDs in R1: {A → B}
FDs in R2: {B → C}
F' = {A → B, B → C}

Is F'⁺ = F⁺? Yes, we have all original FDs!

**Dependency Preserving: ✓**

---

### 8.3 BCNF vs 3NF Decomposition Trade-off

| Property | 3NF Decomposition | BCNF Decomposition |
|----------|-------------------|-------------------|
| Lossless | ✓ Always achievable | ✓ Always achievable |
| Dependency Preserving | ✓ Always achievable | ✗ Not always possible |

> **🎯 Key GATE Fact:** You can ALWAYS get lossless + dependency preserving in 3NF, but NOT always in BCNF.

#### 3NF Synthesis Algorithm (Guarantees LJ + DP)

```
1. Find canonical cover Fc of F
2. For each FD X → A in Fc, create relation X ∪ A
3. If no relation contains a candidate key, add one
4. Remove redundant relations (those contained in others)
```

---

## 9. Denormalization

### When to Denormalize

Normalization reduces redundancy but increases **join operations**. Sometimes, for performance:

| Scenario | Action |
|----------|--------|
| Frequent read, rare write | Consider denormalization |
| Complex joins hurting performance | Selective denormalization |
| Real-time analytics | Pre-computed summaries |

### Common Denormalization Techniques

1. **Adding redundant columns** to avoid joins
2. **Pre-joined tables** for common query patterns
3. **Materialized views** for complex aggregations

> **⚠️ GATE Focus:** Normalization is tested far more than denormalization. Know the concept but focus on normalization.

---

## 10. GATE Shortcuts & Tricks

### Trick 1: Quick Normal Form Identification

```
Given FDs and Relation:
1. Find all candidate keys (CKs)
2. Identify prime and non-prime attributes
3. For each FD X → Y:
   - Check if X is superkey → OK for BCNF
   - If not superkey:
     - Y is prime? → OK for 3NF only
     - Y is non-prime, X is proper subset of CK? → Not even 2NF
     - Y is non-prime, X is non-prime? → Not 3NF
```

### Trick 2: Minimum Number of Tables in BCNF Decomposition

**Often = Number of FDs in Canonical Cover + 1** (for remaining attributes if needed)

### Trick 3: Counting Candidate Keys

1. Attributes only on LHS → MUST be in all CKs
2. Attributes only on RHS → NEVER in any CK
3. Attributes on both sides → May or may not be in CK
4. Attributes on neither side → MUST be in all CKs

### Trick 4: Super Key Count Formula

If there are k candidate keys with sizes s₁, s₂, ..., sₖ and total n attributes:

Use inclusion-exclusion carefully. For single CK of size s:
**Super keys = 2^(n-s)**

### Trick 5: FD Closure vs Attribute Closure

| Term | Notation | Meaning |
|------|----------|---------|
| Attribute Closure | X⁺ | All attributes determined by X |
| FD Closure | F⁺ | All FDs derivable from F |

### Trick 6: Recognizing MVD in Questions

Keywords: "independent of", "doesn't affect", "regardless of"
Example: "An employee's skills are independent of their projects" → EmpID ↠ Skill, EmpID ↠ Project

### Trick 7: Quick Lossless Join Check

**R1 ∩ R2 must be a key in R1 or R2**

### Trick 8: Properties Always True

- **1NF ⊃ 2NF ⊃ 3NF ⊃ BCNF ⊃ 4NF ⊃ 5NF** (higher NF relations are subsets of lower NF; every 3NF relation is also in 2NF and 1NF)
- Every relation has at least one candidate key
- Single-attribute candidate key → Automatically in 2NF
- No non-prime attributes → Automatically in 3NF and BCNF

---

## 11. Practice Problems with Solutions

### Problem 1: Finding Candidate Keys

**Given:** R(A, B, C, D, E) with FDs: AB → C, C → D, D → E, E → A

**Solution:**

Step 1: Categorize attributes
- Only on LHS: B (appears in AB but not on any RHS)
- Only on RHS: None
- Both sides: A, C, D, E

Step 2: B must be in every candidate key (only LHS)

Step 3: Find B⁺
- B⁺ = {B} (B doesn't determine anything alone)

Step 4: Try adding LR attributes to B
- (AB)⁺: AB → C → D → E → A = {A,B,C,D,E} ✓ (AB is superkey, is it minimal?)
- (BC)⁺: C → D → E → A, so BC⁺ = {A,B,C,D,E} ✓ 
- (BD)⁺: D → E → A → (with B, AB) → C, so BD⁺ = {A,B,C,D,E} ✓
- (BE)⁺: E → A → (with B, AB) → C → D, so BE⁺ = {A,B,C,D,E} ✓

Step 5: Check minimality - all have B plus one attribute, all determine everything

**Candidate Keys: {AB, BC, BD, BE}**

---

### Problem 2: Normal Form Identification

**Given:** R(A, B, C, D) with FDs: A → B, B → C, C → D, D → A

**Find the highest normal form.**

**Solution:**

Step 1: Find candidate keys
- A⁺ = {A,B,C,D} ✓
- B⁺ = {B,C,D,A} ✓
- C⁺ = {C,D,A,B} ✓
- D⁺ = {D,A,B,C} ✓

CKs: {A}, {B}, {C}, {D} - All single attributes are candidate keys!

Step 2: Prime attributes = {A, B, C, D} (all are prime)

Step 3: Non-prime attributes = {} (none)

Step 4: Check normal forms
- 1NF: Assumed ✓
- 2NF: No partial dependency (all CKs are single-attribute) ✓
- 3NF: All FDs X → Y where X is superkey OR Y is prime
  - A → B: A is superkey ✓
  - B → C: B is superkey ✓
  - C → D: C is superkey ✓
  - D → A: D is superkey ✓
  All satisfy 3NF ✓
- BCNF: All FDs X → Y where X is superkey (same check as above) ✓

**Highest NF: BCNF** (since all determinants are superkeys)

---

### Problem 3: Canonical Cover

**Given:** F = {A → BC, B → C, A → B, AB → C}

**Find canonical cover.**

**Solution:**

Step 1: Decompose RHS
- A → B
- A → C
- B → C
- A → B (duplicate)
- AB → C

Remove duplicate A → B:
{A → B, A → C, B → C, AB → C}

Step 2: Remove extraneous LHS
- AB → C: Check if A⁺ contains C: A → B → C. Yes! A → C
- So B is extraneous in AB → C. But wait, we already have A → C!

Step 3: Remove redundant FDs
- A → C: Remove and check if A⁺ still contains C
  - Remaining: {A → B, B → C, AB → C}
  - A⁺ = A → B → C. Yes! A → C is redundant.
- AB → C: Remove and check if (AB)⁺ contains C
  - Remaining: {A → B, B → C}
  - (AB)⁺ = AB → C (via B → C). Yes! AB → C is redundant.

**Canonical Cover: {A → B, B → C}**

---

### Problem 4: Decomposition Analysis

**Given:** R(A, B, C, D) with FDs: A → B, B → C, C → D

**Decomposition:** R1(A, B), R2(B, C), R3(C, D)

**Check if lossless and dependency preserving.**

**Solution:**

**Dependency Preserving:**
- FDs in R1: A → B ✓
- FDs in R2: B → C ✓
- FDs in R3: C → D ✓
- All FDs preserved! **DP: Yes**

**Lossless Join:**
Use chase algorithm or check pairwise:
- R1 ∩ R2 = {B}. Is B → (A)? No. Is B → (C)? Yes! ✓
- (R1 ⋈ R2) ∩ R3 = {C}. Is C → (AB)? No. Is C → (D)? Yes! ✓

**Lossless: Yes**

---

### Problem 5: GATE-Style MCQ

**Question:** R(A, B, C, D, E) with FDs: {A → B, BC → D, D → E}. How many candidate keys does R have?

**Solution:**

Step 1: Categorize attributes
- Only LHS: A, C (appear on LHS, not on RHS)
- Only RHS: E (appears only on RHS)
- Both: B, D

Step 2: Attributes only on LHS must be in all CKs: {A, C}

Step 3: Check (AC)⁺:
- Start: {A, C}
- A → B: {A, B, C}
- BC → D: {A, B, C, D}
- D → E: {A, B, C, D, E} = All attributes ✓

**Single Candidate Key: {A, C}**

**Number of Super Keys = 2^(5-2) = 2^3 = 8**

---

## 12. Quick Revision Checklist

### Before Exam, Verify You Know:

#### Functional Dependencies
- [ ] Definition and how to identify FDs
- [ ] Trivial vs Non-trivial FDs
- [ ] Partial vs Full FDs
- [ ] Transitive FDs
- [ ] Closure computation algorithm

#### Armstrong's Axioms
- [ ] Three core axioms (RAT)
- [ ] Three derived rules (Union, Decomposition, Pseudo-transitivity)

#### Keys
- [ ] Super key, Candidate key, Primary key definitions
- [ ] Prime vs Non-prime attributes
- [ ] Algorithm to find candidate keys
- [ ] Formula to count super keys

#### Canonical Cover
- [ ] Three-step algorithm
- [ ] How to identify extraneous attributes
- [ ] How to identify redundant FDs

#### Normal Forms
- [ ] 1NF: Atomic values
- [ ] 2NF: No partial dependencies
- [ ] 3NF: No transitive dependencies OR prime attribute exception
- [ ] BCNF: Every determinant is a superkey
- [ ] 4NF: No multi-valued dependency violations
- [ ] Quick identification algorithm

#### Decomposition
- [ ] Lossless join condition (intersection is key)
- [ ] Dependency preservation test
- [ ] 3NF synthesis algorithm
- [ ] BCNF decomposition algorithm
- [ ] Trade-off between 3NF and BCNF

### Memory Anchors

| Concept | Memory Anchor |
|---------|---------------|
| Armstrong's Axioms | **RAT** - Reflexive, Augmentation, Transitivity |
| 2NF | "**W**hole key" |
| 3NF | "**N**othing but the key, so help me Codd" |
| BCNF | "**E**very determinant is superkey" |
| Lossless Join | "**I**ntersection is **K**ey" |

### Common GATE Patterns

1. **Find candidate keys** → Categorize attributes, compute closures
2. **Highest normal form** → Find CKs, check each FD against NF definitions
3. **Canonical cover** → Decompose RHS, remove extraneous, remove redundant
4. **Check decomposition** → Test LJ (intersection is key) and DP (FDs covered)
5. **Count super keys** → Use 2^(n-k) formula with inclusion-exclusion

---

## Appendix: Formula Sheet

### Closure Computation
```
X⁺ = X
repeat until no change:
  for each A → B in F:
    if A ⊆ X⁺: X⁺ = X⁺ ∪ B
```

### Number of Super Keys
- Single CK of size k in relation of size n: **2^(n-k)**
- Multiple CKs: Use **inclusion-exclusion**

### Lossless Join Test (Binary)
R1 ⋈ R2 is lossless iff:
**(R1 ∩ R2) → (R1 - R2)** OR **(R1 ∩ R2) → (R2 - R1)**

### 3NF Test
For each X → A (non-trivial):
- X is superkey, OR
- A is prime attribute

### BCNF Test
For each X → A (non-trivial):
- X is superkey

### 4NF Test
For each X ↠ Y (non-trivial):
- X is superkey

---

> **Final Note:** Master the closure algorithm and candidate key finding first—they're the foundation for everything else. Practice 5-10 problems of each type before exam. Good luck! 🎯
