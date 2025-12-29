# Database Design & Normalization — Teaching Notes

> *For the intellectually curious. We don't just learn what—we understand why.*

---

## The Big Picture: What Are We Really Doing?

**Core insight:** Normalization eliminates redundancy by ensuring each fact is stored exactly once.

When a fact appears in multiple places, three problems emerge:
- **Update Anomaly:** Change it in one place, forget another — database lies
- **Insertion Anomaly:** Can't add new fact without inventing unrelated data
- **Deletion Anomaly:** Remove one thing, accidentally destroy unrelated knowledge

**The entire field exists because redundancy = potential inconsistency.**

*Example to internalize:* Table (StudentID, StudentName, CourseID, CourseName, Instructor). The fact "CS101 taught by Dr. Smith" repeats in every row where someone takes CS101. That's the disease. Normal forms are the cure.

---

## Functional Dependencies: The Language of Constraints

### The Core Idea

**X → Y** states: *"Knowing X uniquely determines Y."*

This isn't about current data—it's about **what's logically possible**. If EmpID → Salary, the database will *never* allow two different salaries for the same EmpID.

**Why this matters:** FDs are the mathematical language for "what depends on what." Every normal form is defined in terms of which FDs are allowed or forbidden.

### Schema vs Instance (Critical!)

```
WRONG: "I looked at my data, every city maps to one state, so City → State"
RIGHT: "Springfield exists in Illinois AND Massachusetts, so City → State is FALSE"
```

FDs must hold for **all possible valid data**, not just today's snapshot. This is the #1 GATE trap.

### Types That Actually Matter

| Type | What It Really Means | Why You Care |
|------|---------------------|--------------|
| **Partial FD** | A *proper subset* of the key determines something | Violates 2NF |
| **Transitive FD** | Non-key → Non-key chain | Violates 3NF |
| **Trivial FD** | Y ⊆ X (always true) | Ignore in analysis |

**Partial FD intuition:** (StudentID, CourseID) is your key but StudentID alone → StudentName. You've embedded Student info where it doesn't belong.

**Transitive FD intuition:** EmpID → DeptID → DeptName. DeptName is "reachable" from EmpID indirectly through DeptID. That intermediary creates the redundancy.

---

## Closure: The Computational Engine

### Why Closure Exists

Given FDs, we ask: "Does X determine Y?" Computing X⁺ (closure of X) answers this—if Y ⊆ X⁺, then yes.

**The algorithm** is elegant—keep adding what you can determine until nothing new appears:

```
X⁺ = X
while (change occurs):
    for each A → B in F:
        if A ⊆ X⁺: X⁺ = X⁺ ∪ B
```

**Trace example:**

R(A, B, C, D, E), FDs: {A → B, BC → D, E → C, D → A}

Finding (AE)⁺:
```
Start: {A, E}
A → B: {A, E, B}
E → C: {A, E, B, C}
BC → D: {A, E, B, C, D}
D → A: (already present)
Done: {A, B, C, D, E}
```

Since (AE)⁺ = all attributes, **AE is a superkey**.

### Three Uses of Closure

1. **Check if X → Y:** Is Y ⊆ X⁺?
2. **Check if X is superkey:** Is X⁺ = all attributes?
3. **Find candidate keys:** Find minimal X where X⁺ = all attributes

---

## Armstrong's Axioms: The Logical Foundation

### Why Three Rules Are Enough

Armstrong proved: three simple rules can derive **every valid FD**. Nothing more is needed.

| Axiom | The Rule | The Intuition |
|-------|----------|---------------|
| **Reflexivity** | If Y ⊆ X, then X → Y | Trivial—if you know AB, you know A |
| **Augmentation** | X → Y ⟹ XZ → YZ | Adding same info to both sides preserves dependency |
| **Transitivity** | X → Y, Y → Z ⟹ X → Z | Chaining works |

**Memory: RAT**

### Derived Rules (Shortcuts)

- **Union:** X → Y, X → Z ⟹ X → YZ
- **Decomposition:** X → YZ ⟹ X → Y, X → Z
- **Pseudo-transitivity:** X → Y, WY → Z ⟹ WX → Z

### Why This Matters

- **Sound:** Never produce false FDs
- **Complete:** Every valid FD can be derived

Closure computation is just systematic application of Armstrong's axioms.

---

## Keys: Understanding the Hierarchy

### The Stack

```
SUPERKEY → any set that uniquely identifies a row
    ↓ minimize
CANDIDATE KEY → minimal superkey (remove anything, it breaks)
    ↓ choose one
PRIMARY KEY → the designated identifier
```

**Prime attribute:** In *any* candidate key
**Non-prime attribute:** Not in *any* candidate key

**Why this matters:** Normal forms are defined by which FDs involve non-prime attributes.

### Finding Candidate Keys: The Smart Way

**The insight:** 
- Attributes *never on RHS* → MUST be in every CK (nothing derives them)
- Attributes *only on RHS* → NEVER in any CK (always derived)

```
L = only LHS → MUST be in every CK
R = only RHS → NEVER in any CK
LR = both sides → maybe
N = neither → MUST be in every CK
```

Start with L ∪ N, compute closure. If covers everything, that's the only CK. Otherwise, try adding LR attributes.

**Example:** R(A, B, C, D, E), FDs: {A → BC, CD → E, B → D, E → A}

All appear on both sides (LR). Try each: A⁺ = all ✓, E⁺ = all ✓, others fail.

**Candidate Keys: {A}, {E}**

### Counting Superkeys

CK of size k in relation of n attributes: **Superkeys = 2^(n-k)**

*Why:* Each of (n-k) non-key attributes can be in or out.

**Multiple CKs:** Use inclusion-exclusion to avoid double-counting.

---

## Canonical Cover: Minimal Equivalent FD Set

### The Goal

Reduce FD set to minimal equivalent form:
1. Single attribute on RHS
2. No extraneous LHS attributes
3. No redundant FDs
4. Same closure as original

### The Algorithm

```
1. DECOMPOSE: A → BC becomes A → B, A → C
2. SIMPLIFY LHS: For XY → A, check if X⁺ contains A. If yes, Y is extraneous.
3. REMOVE REDUNDANT: For X → A, check if X⁺ (using other FDs) contains A. If yes, redundant.
```

**Example:** F = {A → BC, B → C, AB → D}

1. Decompose: {A → B, A → C, B → C, AB → D}
2. In AB → D: B⁺ = {B,C}, no D. A⁺ = {A,B,C}, no D. Neither extraneous.
3. A → C redundant? A⁺ with {A→B, B→C, AB→D} = {A,B,C}. Yes! Remove.
4. AB → D redundant? (AB)⁺ with {A→B, B→C} = {A,B,C}. No D. Keep.

**Canonical Cover: {A → B, B → C, AB → D}**

---

## Normal Forms: The Progression

### The Core Insight

Each normal form prohibits a specific type of "bad" FD:

| NF | What's Prohibited | Intuition |
|----|-------------------|-----------|
| **1NF** | Multi-valued attributes | One value per cell |
| **2NF** | Partial dependency | Non-prime depends on *part* of key |
| **3NF** | Transitive dependency | Non-prime → Non-prime chain |
| **BCNF** | Any non-superkey determinant | Every determinant is a superkey |

### 1NF: Atomic Values

No arrays, no comma-separated lists. Each cell holds one value.

*Violation:* Phone = "9876, 1234"
*Fix:* Separate rows or separate table

### 2NF: No Partial Dependencies

**Only matters when CK is composite.** If single-attribute CK → automatically 2NF.

*Violation:* (StudentID, CourseID) → Grade, but StudentID → StudentName
*Problem:* StudentName depends on *part* of key
*Fix:* Separate Student table

### 3NF: No Transitive Dependencies

For every non-trivial X → A:
- X is superkey, OR
- A is prime attribute

*Violation:* EmpID → DeptID → DeptName (DeptID not superkey, DeptName not prime)
*Problem:* Chain through non-key
*Fix:* Separate Department table

**Memory:** "The key, the whole key, and nothing but the key, so help me Codd" (Edgar F. Codd invented the relational model)

### BCNF: No Exceptions

For every non-trivial X → A: **X must be superkey. Period.**

*Difference from 3NF:* No exception for prime attributes on RHS.

*When 3NF ≠ BCNF:* Prime attribute depends on non-superkey.

Example: R(Student, Subject, Teacher)
- FDs: (Student, Subject) → Teacher, Teacher → Subject
- CKs: (Student, Subject), (Student, Teacher)
- All attributes are prime
- Teacher → Subject: Teacher not superkey, but Subject is prime → 3NF OK, BCNF violated

### 4NF: Multi-Valued Dependencies

**MVD X ↠ Y:** Given X, the Y values are independent of other attributes.

*Violation:* (EmpID, Skill, Hobby) where skills and hobbies are independent
*Problem:* Forced to create all combinations
*Fix:* Separate tables: (EmpID, Skill), (EmpID, Hobby)

**Memory:** "Independent facts in independent tables"

### Quick Identification

1. Find all CKs
2. Identify prime/non-prime attributes
3. For each FD X → A:
   - X is superkey? → BCNF OK
   - A is prime? → 3NF OK
   - X proper subset of CK and A non-prime? → Not even 2NF
   - X non-prime, A non-prime? → Not 3NF

---

## Decomposition: Splitting Tables

### Two Properties to Check

1. **Lossless Join:** Can we reconstruct original by joining?
2. **Dependency Preserving:** Can we check all FDs locally?

### Lossless Join Test (Binary)

R split into R1, R2 is lossless iff:

**(R1 ∩ R2) → (R1 - R2)** OR **(R1 ∩ R2) → (R2 - R1)**

**Translation:** The common attributes must be a key in at least one piece.

*Example:* R(A,B,C) with A → B, split into R1(A,B), R2(A,C)
- R1 ∩ R2 = {A}
- A → B? Yes! Lossless ✓

### Dependency Preservation Test

For each original FD, check if it can be verified within a single decomposed relation.

*Example:* R(A,B,C) with {A → B, B → C}, split into R1(A,B), R2(B,C)
- A → B in R1 ✓
- B → C in R2 ✓
- All preserved ✓

### The Critical Trade-off

| Property | 3NF | BCNF |
|----------|-----|------|
| Lossless | Always achievable | Always achievable |
| Dependency Preserving | Always achievable | **Not always possible** |

**This is why 3NF exists:** Sometimes you can't get BCNF without losing dependency preservation.

### 3NF Synthesis Algorithm (Guarantees Both)

1. Find canonical cover
2. For each FD X → A, create relation (X, A)
3. If no relation contains a CK, add one
4. Remove relations contained in others

---

## Exam Patterns

### Pattern 1: Find Candidate Keys

1. Categorize attributes (L, R, LR, N)
2. Start with L ∪ N
3. Compute closure, add LR if needed
4. Verify minimality

### Pattern 2: Identify Normal Form

1. Find all CKs
2. Classify prime/non-prime
3. Check each FD against NF definitions
4. Report lowest violated

### Pattern 3: Canonical Cover

1. Decompose RHS
2. Remove extraneous LHS (closure test)
3. Remove redundant FDs (closure without that FD)

### Pattern 4: Check Decomposition

1. Lossless: Is intersection a key somewhere?
2. DP: Are all FD attributes together somewhere?

### Pattern 5: Count Superkeys

Single CK of size k, n total: **2^(n-k)**
*Reasoning:* Each of the (n-k) non-key attributes can be included or excluded independently.

Multiple CKs: Inclusion-exclusion

---

## Practice Problems

### Problem 1: Candidate Keys

R(A, B, C, D, E), FDs: {AB → C, C → D, D → E, E → A}

**Solve:** 
- B only on LHS → in every CK
- B⁺ = {B} (not enough)
- (AB)⁺: AB→C→D→E→A = {A,B,C,D,E} ✓
- (BC)⁺: C→D→E→A, BC = {A,B,C,D,E} ✓
- (BD)⁺: D→E→A, AB→C = {A,B,C,D,E} ✓
- (BE)⁺: E→A, AB→C→D = {A,B,C,D,E} ✓

**Answer: {AB, BC, BD, BE}** — four candidate keys

### Problem 2: Normal Form

R(A, B, C, D), FDs: {A → B, B → C, C → D, D → A}

**Solve:**
- A⁺ = B⁺ = C⁺ = D⁺ = all attributes
- CKs: {A}, {B}, {C}, {D}
- All attributes prime
- Every FD: determinant is superkey

**Answer: BCNF**

### Problem 3: Canonical Cover

F = {A → BC, B → C, A → B, AB → C}

**Solve:**
1. Decompose: {A→B, A→C, B→C, AB→C}
2. AB→C: B extraneous (A⁺ covers C)? A→B→C, yes. Remove B.
3. Now have {A→B, A→C, B→C, A→C}
4. A→C redundant (A→B→C)? Yes. Remove.
5. Remove duplicate.

**Answer: {A → B, B → C}**

### Problem 4: Decomposition Check

R(A,B,C,D), FDs: {A→B, B→C, C→D}, split into R1(A,B), R2(B,C), R3(C,D)

**DP:** A→B in R1 ✓, B→C in R2 ✓, C→D in R3 ✓ → **Preserved**

**LJ:** 
- R1 ∩ R2 = {B}, B→C ✓
- (R1⋈R2) ∩ R3 = {C}, C→D ✓ → **Lossless**

### Problem 5: GATE-Style

R(A,B,C,D,E), FDs: {A→B, BC→D, D→E}. Number of candidate keys?

**Solve:**
- A only LHS, C only LHS → {A,C} must be in every CK
- (AC)⁺: A→B, BC→D, D→E = {A,B,C,D,E} ✓

**Answer: 1 candidate key {A,C}**
**Superkeys: 2^(5-2) = 8**

---

## Quick Reference

### Closure Algorithm
```
X⁺ = X; repeat: if A ⊆ X⁺ for A→B, then X⁺ ∪= B
```

### Superkey Count
Single CK size k, n attrs: **2^(n-k)**

### Lossless Test
(R1 ∩ R2) → (R1 - R2) or (R1 ∩ R2) → (R2 - R1)

### Normal Form Tests
- **3NF:** X superkey OR A prime
- **BCNF:** X superkey

### Memory Anchors
- **RAT:** Reflexive, Augmentation, Transitivity
- **2NF:** Whole key
- **3NF:** Nothing but the key
- **BCNF:** Every determinant is superkey
- **Lossless:** Intersection is key

---

*Master closure computation and candidate key finding first—everything else builds on these. Practice 5-10 problems of each type.*
