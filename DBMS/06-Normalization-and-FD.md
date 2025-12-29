# Chapter 6: Normalization & Functional Dependencies

---

## 🎯 Why Normalization?

**Normalization** is the process of organizing data to:
1. **Minimize redundancy** (duplicate data)
2. **Avoid anomalies** (update, insert, delete problems)
3. **Ensure data integrity**

### 🎭 Analogy
> Normalization is like **organizing your closet** — you don't store the same shirt in 5 different drawers. You store it once and reference its location.

---

## ⚠️ Problems Without Normalization

### Example: Unnormalized Table
```
StudentCourse:
┌──────┬────────┬─────────────┬──────────┬────────────┬──────────┐
│ Roll │  Name  │    Email    │ CourseID │ CourseName │ Faculty  │
├──────┼────────┼─────────────┼──────────┼────────────┼──────────┤
│  1   │ Alice  │ a@mail.com  │   C101   │   DBMS     │  Prof.X  │
│  1   │ Alice  │ a@mail.com  │   C102   │   OS       │  Prof.Y  │
│  2   │ Bob    │ b@mail.com  │   C101   │   DBMS     │  Prof.X  │
└──────┴────────┴─────────────┴──────────┴────────────┴──────────┘
```

### Three Types of Anomalies

#### 1. Update Anomaly
> Change Alice's email? Must update **multiple rows** — risk of inconsistency!

#### 2. Insert Anomaly
> Add a new course with no enrolled students? **Cannot insert** (Roll would be NULL)!

#### 3. Delete Anomaly
> Delete Bob's enrollment? **Lose course info** (C101 data disappears if Bob was the only one)!

---

## 🔗 Functional Dependencies (FD)

### Definition
If X → Y, then for any two tuples t₁ and t₂:
```
if t₁[X] = t₂[X], then t₁[Y] = t₂[Y]
```

### 🎭 Analogy
> X → Y means "X **determines** Y" or "knowing X, you know Y"
> 
> **Roll → Name**: If you know Roll number, you know the Name.

### Types of FDs

| Type | Description | Example |
|------|-------------|---------|
| **Trivial** | Y ⊆ X | AB → A, AB → B |
| **Non-trivial** | Y ⊄ X | Roll → Name |
| **Completely Non-trivial** | X ∩ Y = ∅ | Roll → Name (if Roll ≠ Name) |

### Partial vs Full Dependency

#### Full Dependency
Y depends on the **entire** key X.
```
{Roll, CourseID} → Grade
Grade depends on BOTH Roll and CourseID together
```

#### Partial Dependency
Y depends on **part of** the key X.
```
Key: {Roll, CourseID}
Roll → Name  ← Name depends only on Roll, not CourseID
This is PARTIAL dependency
```

### Transitive Dependency
X → Y and Y → Z, but Y ↛ X
```
Roll → DeptID → DeptName
Roll doesn't directly determine DeptName, it's via DeptID
```

---

## 📐 Armstrong's Axioms

### Primary Rules (Sound & Complete)

| Axiom | Name | Rule |
|-------|------|------|
| **A1** | Reflexivity | If Y ⊆ X, then X → Y |
| **A2** | Augmentation | If X → Y, then XZ → YZ |
| **A3** | Transitivity | If X → Y and Y → Z, then X → Z |

### Derived Rules

| Rule | Name | Derivation |
|------|------|------------|
| **Union** | If X → Y and X → Z, then X → YZ | From augmentation + transitivity |
| **Decomposition** | If X → YZ, then X → Y and X → Z | From reflexivity + transitivity |
| **Pseudo-transitivity** | If X → Y and WY → Z, then WX → Z | From augmentation + transitivity |

### 🧠 Memory Trick: "RAT"
> **R**eflexivity, **A**ugmentation, **T**ransitivity = Armstrong's Axioms

---

## 🔑 Closure of Attributes (X⁺)

### Definition
Set of all attributes functionally determined by X.

### Algorithm
```
X⁺ = X
repeat
    for each FD α → β in F:
        if α ⊆ X⁺:
            X⁺ = X⁺ ∪ β
until no change in X⁺
```

### Example
```
R(A, B, C, D, E)
F = {A → B, BC → D, D → E}

Find (AC)⁺:

Step 1: (AC)⁺ = {A, C}
Step 2: A → B, A ⊆ {A,C}, add B → {A, B, C}
Step 3: BC → D, BC ⊆ {A,B,C}, add D → {A, B, C, D}
Step 4: D → E, D ⊆ {A,B,C,D}, add E → {A, B, C, D, E}

(AC)⁺ = {A, B, C, D, E} = All attributes!
∴ AC is a candidate key
```

---

## 🔑 Finding Candidate Keys

### Algorithm
1. Find attributes that appear **only on LHS** of FDs → Must be in every key
2. Find attributes that appear **only on RHS** → Cannot be in any key
3. Find attributes on **both sides** → May or may not be in key
4. Start with LHS-only attributes, compute closure
5. Add other attributes if closure ≠ all attributes

### Example
```
R(A, B, C, D, E, F)
F = {AB → C, C → D, D → E, E → A}

LHS only: B, F (never on RHS)
RHS only: None
Both: A, C, D, E

Start: {B, F}
(BF)⁺ = {B, F} ≠ All attributes

Add A: (ABF)⁺:
  A is in ABF
  AB → C: {A, B, C, F}
  C → D: {A, B, C, D, F}
  D → E: {A, B, C, D, E, F} ✓

Candidate Key: {A, B, F}

Try other combinations...
(CBF)⁺ = {B, C, D, E, F, A} ✓ → {B, C, F} is also a CK
(DBF)⁺ = {B, D, E, F, A, C} ✓ → {B, D, F} is also a CK
(EBF)⁺ = {B, E, F, A, C, D} ✓ → {B, E, F} is also a CK

All Candidate Keys: {ABF}, {BCF}, {BDF}, {BEF}
```

---

## 📊 Normal Forms Hierarchy

```
┌─────────────────────────────────────────────┐
│               5NF (PJNF)                    │
│  ┌─────────────────────────────────────┐   │
│  │            4NF                       │   │
│  │  ┌─────────────────────────────┐    │   │
│  │  │          BCNF                │    │   │
│  │  │  ┌─────────────────────┐    │    │   │
│  │  │  │        3NF           │    │    │   │
│  │  │  │  ┌─────────────┐    │    │    │   │
│  │  │  │  │    2NF      │    │    │    │   │
│  │  │  │  │  ┌─────┐   │    │    │    │   │
│  │  │  │  │  │ 1NF │   │    │    │    │   │
│  │  │  │  │  └─────┘   │    │    │    │   │
│  │  │  │  └─────────────┘    │    │    │   │
│  │  │  └─────────────────────┘    │    │   │
│  │  └─────────────────────────────┘    │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘

Every higher NF is a subset of lower NF:
5NF ⊂ 4NF ⊂ BCNF ⊂ 3NF ⊂ 2NF ⊂ 1NF
```

---

## 1️⃣ First Normal Form (1NF)

### Requirements
1. Each attribute contains **atomic** (indivisible) values
2. No **repeating groups** or arrays
3. Each row is **unique**

### Violation Example
```
❌ Not in 1NF:
┌──────┬────────┬─────────────────────┐
│ Roll │  Name  │      Phones         │
├──────┼────────┼─────────────────────┤
│  1   │ Alice  │ 123456, 789012      │  ← Multi-valued!
└──────┴────────┴─────────────────────┘

✅ Convert to 1NF:
┌──────┬────────┬──────────┐
│ Roll │  Name  │  Phone   │
├──────┼────────┼──────────┤
│  1   │ Alice  │ 123456   │
│  1   │ Alice  │ 789012   │
└──────┴────────┴──────────┘
```

### 🎭 Analogy
> 1NF = **One value per cell** (like Excel, not like Word with paragraphs in cells)

---

## 2️⃣ Second Normal Form (2NF)

### Requirements
1. Must be in **1NF**
2. No **partial dependency** (non-prime attribute on part of candidate key)

### Partial Dependency
Non-prime attribute depends on **subset** of candidate key.

### Violation Example
```
StudentCourse(Roll, CourseID, Name, CourseName, Grade)
PK: (Roll, CourseID)

FDs:
  Roll → Name               ← Partial (Name depends on part of key)
  CourseID → CourseName     ← Partial
  Roll, CourseID → Grade    ← Full (OK)

❌ Not in 2NF due to partial dependencies
```

### Conversion to 2NF
```
Split into:
- Student(Roll, Name)           ← Roll → Name
- Course(CourseID, CourseName)  ← CourseID → CourseName
- Enrollment(Roll, CourseID, Grade)  ← Full dependency
```

### 🔑 Key Point
> 2NF only applies when **composite primary key** exists.
> If PK is single attribute → already in 2NF (no partial dependency possible)

---

## 3️⃣ Third Normal Form (3NF)

### Requirements
1. Must be in **2NF**
2. No **transitive dependency** (non-prime attribute on another non-prime)

### Definition (Formal)
For every FD X → Y:
- X is a superkey, OR
- Y is a prime attribute (part of some candidate key)

### Transitive Dependency
A → B → C where B is not a superkey

### Violation Example
```
Student(Roll, Name, DeptID, DeptName, HOD)
CK: {Roll}

FDs:
  Roll → DeptID         ← OK
  DeptID → DeptName     ← Transitive! (DeptID not superkey)
  DeptID → HOD          ← Transitive!

Roll → DeptID → DeptName (transitive chain)
```

### Conversion to 3NF
```
Split into:
- Student(Roll, Name, DeptID)
- Department(DeptID, DeptName, HOD)
```

### 🧠 Memory Trick for 3NF
> **"Every non-key attribute must depend on the key, the whole key, and nothing but the key."**
> 
> - Whole key → No partial (2NF)
> - Nothing but the key → No transitive (3NF)

---

## 🅱️ Boyce-Codd Normal Form (BCNF)

### Requirements
For every FD X → Y:
- X must be a **superkey**

### BCNF vs 3NF
| Condition | 3NF | BCNF |
|-----------|-----|------|
| X is superkey | ✓ | ✓ |
| Y is prime attribute | ✓ | ✗ |

> BCNF is stricter than 3NF!

### Violation Example
```
Teaches(Student, Subject, Professor)

FDs:
  (Student, Subject) → Professor
  Professor → Subject

CK: {Student, Subject}
Prime attributes: Student, Subject
Non-prime: Professor

Check Professor → Subject:
- Professor is NOT a superkey
- Subject IS a prime attribute

∴ In 3NF (because Subject is prime)
∴ NOT in BCNF (because Professor not superkey)
```

### Conversion to BCNF
```
Split on violating FD: Professor → Subject

- TeachesWith(Student, Professor)  ← Key determines everything
- ProfSubject(Professor, Subject)  ← Professor → Subject
```

### ⚠️ BCNF Trade-off
BCNF decomposition may **lose dependency preservation**!

```
Original: Professor → Subject was enforced
After split: Cannot be enforced with FK (need join to check)
```

---

## 📊 3NF vs BCNF Comparison

| Aspect | 3NF | BCNF |
|--------|-----|------|
| Redundancy | Slightly more | Minimal |
| Dependency Preservation | Always | Not always |
| Lossless Join | Always | Always |
| When same? | When no overlapping CKs | When no overlapping CKs |

### When are 3NF and BCNF same?
- When there's only one candidate key
- When all candidate keys are single attributes
- When no candidate keys overlap

---

## 4️⃣ Fourth Normal Form (4NF)

### Multi-Valued Dependency (MVD)
X →→ Y means: For any value of X, Y values are independent of other attributes.

### Notation
```
X →→ Y (X multi-determines Y)
```

### Requirements
1. Must be in **BCNF**
2. No non-trivial **multi-valued dependencies** (unless X is superkey)

### Violation Example
```
Employee(EmpID, Skill, Hobby)

EmpID →→ Skill (skills independent of hobbies)
EmpID →→ Hobby (hobbies independent of skills)

┌───────┬────────┬────────┐
│ EmpID │ Skill  │ Hobby  │
├───────┼────────┼────────┤
│  101  │ Java   │ Chess  │
│  101  │ Java   │ Music  │
│  101  │ Python │ Chess  │
│  101  │ Python │ Music  │
└───────┴────────┴────────┘
All combinations! (redundancy)
```

### Conversion to 4NF
```
- EmpSkill(EmpID, Skill)
- EmpHobby(EmpID, Hobby)
```

---

## 5️⃣ Fifth Normal Form (5NF / PJNF)

### Join Dependency (JD)
Relation R satisfies JD ⋈(R₁, R₂, ..., Rₙ) if R can be reconstructed by joining R₁, R₂, ..., Rₙ.

### Requirements
1. Must be in **4NF**
2. Every join dependency implied by candidate keys

### Rarely Asked in GATE
Focus on 1NF through BCNF for exam preparation.

---

## 🔄 Decomposition Properties

### 1. Lossless Join Property
No information lost when decomposed and rejoined.

### Test for Lossless Join (Binary Decomposition)
Decomposition of R into R₁ and R₂ is lossless iff:
```
(R₁ ∩ R₂) → R₁  OR  (R₁ ∩ R₂) → R₂
```
Common attributes must be a key of at least one decomposed relation.

### Example
```
R(A, B, C) with A → B

Decomposition: R₁(A, B), R₂(A, C)
Common: A
A → B means A → R₁(A,B)
∴ Lossless!
```

### 2. Dependency Preservation
All FDs can be enforced in decomposed relations without joins.

### Test for Dependency Preservation
For each FD X → Y in F:
- X and Y should both be in **same decomposed relation**

### Example
```
R(A, B, C) with FDs: A → B, B → C

Decomposition: R₁(A, B), R₂(B, C)
- A → B: A, B both in R₁ ✓
- B → C: B, C both in R₂ ✓
∴ Dependency preserving!
```

---

## 📐 Canonical Cover (Minimal Cover)

### Definition
Minimal set of FDs equivalent to original set F.

### Properties
1. No redundant FDs
2. Each FD has single attribute on RHS
3. No extraneous attributes on LHS

### Algorithm
```
1. Decompose RHS: A → BC becomes A → B, A → C
2. Remove extraneous LHS attributes:
   For each FD XY → A, check if X → A without Y
3. Remove redundant FDs:
   For each FD X → Y, check if F - {X → Y} still implies X → Y
```

### Example
```
F = {A → BC, B → C, AB → D}

Step 1: Decompose
{A → B, A → C, B → C, AB → D}

Step 2: Check LHS extraneous
AB → D: Check A → D without B
  A⁺ = {A, B, C} doesn't contain D
Check B → D without A
  B⁺ = {B, C} doesn't contain D
AB → D cannot be reduced

Step 3: Remove redundant
A → C: Check if A → C from {A → B, B → C, AB → D}
  A → B, B → C gives A → C (transitive)
  ∴ A → C is redundant, remove it!

Canonical Cover: {A → B, B → C, AB → D}
```

---

## 🧮 Number of FDs Calculation

### Maximum Possible FDs
For relation with n attributes:
- LHS options: 2ⁿ - 1 (non-empty subsets)
- RHS options: 2ⁿ - 1 (non-empty subsets)
- But trivial FDs excluded...

### Simpler Calculation
For each pair of attribute sets:
```
Max non-trivial FDs ≈ (2ⁿ - 1) × (2ⁿ - 1)
```

---

## 🔢 Counting Candidate Keys

### From Given FDs
1. Identify attributes only on LHS → must be in every CK
2. Identify attributes only on RHS → cannot be in any CK
3. Build closure from LHS-only, add others if needed

### Example
```
R(A, B, C, D) with FDs: A → B, B → C

Only LHS: A, D
Only RHS: C
Both: B

Must have: A, D
(AD)⁺ = {A, D, B, C} = All ✓

Candidate Keys: {AD}
```

---

## ⚠️ Common GATE Traps

### Trap 1: Single-Attribute Key
> If primary key is single attribute, relation is automatically in 2NF
> (No partial dependency possible)

### Trap 2: All Attributes Prime
> If all attributes are part of some candidate key, relation is in 3NF
> (No non-prime attributes for transitive dependency)

### Trap 3: BCNF Always Lossless
> BCNF decomposition is always lossless
> But may NOT preserve dependencies

### Trap 4: 3NF Allows Some Redundancy
> 3NF allows X → Y where Y is prime (part of CK)
> This can cause some redundancy

### Trap 5: Closure Computation
> Don't forget to iterate until no change
> One pass may not catch all derived FDs

---

## 🧪 Practice Problems

### Q1: Find Candidate Keys
```
R(A, B, C, D, E)
FDs: A → BC, CD → E, B → D, E → A

Only LHS: None (all appear on RHS)
Check each attribute:
A⁺ = {A, B, C, D, E} ✓ → A is CK
B⁺ = {B, D} ✗
C⁺ = {C} ✗
D⁺ = {D} ✗
E⁺ = {E, A, B, C, D} ✓ → E is CK

Since CD → E and E → A:
(CD)⁺ = {C, D, E, A, B} ✓ → CD is CK
(BC)⁺ = {B, C, D, E, A} ✓ → BC is CK

Candidate Keys: {A}, {E}, {BC}, {CD}
```

### Q2: Highest Normal Form
```
R(A, B, C, D)
FDs: AB → CD, C → A

CKs: Find first
(AB)⁺ = {A, B, C, D} ✓
(BC)⁺ = {B, C, A, D} ✓ (C → A, then AB → CD)

Check C → A:
- C is NOT superkey
- A IS prime (part of CK)
∴ 3NF satisfied

Check for BCNF:
- C → A, C is not superkey
∴ NOT in BCNF

Highest NF: 3NF
```

### Q3: Lossless Decomposition
```
R(A, B, C) decomposed to R₁(A, B) and R₂(B, C)
FDs: A → B, B → C

Common: B
Check: B → B ✓ (trivial) but need B → R₁ or B → R₂
B → B alone doesn't help

Check: Does B → A? No
Does B → C? Yes!
B → C means B determines R₂(B, C)

∴ Lossless decomposition!
```

---

## 📌 Chapter Summary

| Normal Form | Requirement | Removes |
|-------------|-------------|---------|
| **1NF** | Atomic values | Multi-valued attributes |
| **2NF** | 1NF + No partial dependency | Partial dependencies |
| **3NF** | 2NF + No transitive dependency | Transitive dependencies |
| **BCNF** | Every determinant is superkey | All anomalies |
| **4NF** | BCNF + No MVD | Multi-valued dependencies |

---

## 🎓 Quick Revision Points

1. ✅ 2NF issues only with composite keys
2. ✅ 3NF: "Nothing but the key" (no transitive)
3. ✅ BCNF stricter than 3NF (may lose dependency preservation)
4. ✅ Lossless test: Common attrs → one side
5. ✅ Canonical cover: Single RHS, no redundancy
6. ✅ Closure: Iterate until no change
7. ✅ Prime attribute can be on RHS in 3NF (not in BCNF)

---

*Previous: [SQL Complete Guide](./05-SQL-Complete-Guide.md) | Next: [Transaction Management](./07-Transaction-Management.md)*
