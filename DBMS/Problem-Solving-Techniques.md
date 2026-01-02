# 🎯 DBMS Problem-Solving Techniques for GATE & ESE

> **Master the Art of Solving DBMS Questions in Under 2 Minutes**

---

## 📐 Mathematical Notation Guide

| Symbol | Meaning | Example |
|--------|---------|---------|
| ⌊x⌋ | Floor function (round down) | ⌊3.7⌋ = 3 |
| ⌈x⌉ | Ceiling function (round up) | ⌈3.2⌉ = 4 |
| \|R\| | Cardinality (number of tuples) | \|Student\| = 100 |
| 2^n | 2 to the power n | 2^3 = 8 |
| log_p(x) | Logarithm base p of x | log_2(8) = 3 |
| ⊆ | Subset | {A} ⊆ {A, B} |
| ∪ | Union | {A} ∪ {B} = {A, B} |
| ∩ | Intersection | {A, B} ∩ {B, C} = {B} |

---

## 📋 Table of Contents

1. [General GATE Problem-Solving Framework](#1-general-gate-problem-solving-framework)
2. [ER Model Techniques](#2-er-model-techniques)
3. [Candidate Key Finding Techniques](#3-candidate-key-finding-techniques)
4. [Super Key Counting Techniques](#4-super-key-counting-techniques)
5. [Relational Algebra Techniques](#5-relational-algebra-techniques)
6. [SQL Query Analysis Techniques](#6-sql-query-analysis-techniques)
7. [Normalization Techniques](#7-normalization-techniques)
8. [Serializability Checking Techniques](#8-serializability-checking-techniques)
9. [B+ Tree Calculation Techniques](#9-b-tree-calculation-techniques)
10. [Recovery Analysis Techniques](#10-recovery-analysis-techniques)

---

## 1. General GATE Problem-Solving Framework

### The 4-Step GATE Method

```
Step 1: CLASSIFY the question type
        ↓
Step 2: RECALL the relevant formula/algorithm
        ↓
Step 3: EXECUTE with care for edge cases
        ↓
Step 4: VERIFY with sanity checks
```

### Time Management per Question Type

| Question Type | Recommended Time | Strategy |
|---------------|------------------|----------|
| 1-mark MCQ | 1 minute | Quick formula application |
| 2-mark MCQ | 2-3 minutes | Methodical solving |
| NAT (Numerical) | 2-3 minutes | Double-check calculations |
| MSQ (Multi-Select) | 3-4 minutes | Eliminate, then verify each |

### Common Mistake Prevention

1. **Read EVERY word** - "minimum" vs "maximum", "at least" vs "at most"
2. **Check units** - bytes vs bits, blocks vs records
3. **Watch for NULL** - SQL questions often trap with NULL behavior
4. **Draw diagrams** - Especially for schedules and ER models

---

## 2. ER Model Techniques

### Technique 2.1: Minimum Tables Count

**Problem Type**: "What is the minimum number of tables required?"

**Step-by-Step Algorithm**:

```
1. Count Strong Entities: +1 table each
2. Count Weak Entities: +1 table each (includes identifying relationship)
3. Count M:N Relationships: +1 table each
4. Count Multi-valued Attributes: +1 table each
5. 1:1 and 1:N relationships: +0 tables (use FK approach)

Formula:
Tables = Strong + Weak + M:N + Multi-valued
```

**Worked Example**:
```
Given:
- 4 entities (3 strong, 1 weak)
- 3 relationships (one M:N, two 1:N)
- 2 multi-valued attributes

Solution:
Tables = 3 (strong) + 1 (weak) + 1 (M:N) + 2 (multi-valued)
       = 7 tables

Note: Weak entity absorbs its identifying relationship
      1:N relationships use FK (no extra table)
```

### Technique 2.2: Cardinality Determination

**Problem Type**: "Identify the cardinality of relationship"

**Decision Tree**:
```
Does Entity A map to multiple Entity B?
├── Yes → Is it also B maps to multiple A?
│         ├── Yes → M:N
│         └── No  → 1:N (from B to A)
└── No  → Does B map to multiple A?
          ├── Yes → N:1 (which is 1:N from A to B)
          └── No  → 1:1
```

### Technique 2.3: Identifying Weak Entities

**Checklist**:
- [ ] No attribute can uniquely identify the entity alone
- [ ] Depends on another entity for existence
- [ ] Has a partial key (discriminator)
- [ ] Has identifying relationship with owner

---

## 3. Candidate Key Finding Techniques

### Technique 3.1: Attribute Classification Method (FASTEST!)

**Problem Type**: "Find all candidate keys"

**Step-by-Step Algorithm**:

```
Step 1: Classify all attributes into 4 categories

| Category | Rule | Must be in Key? |
|----------|------|-----------------|
| L (Left only) | Only on LHS of FDs | YES - Always |
| R (Right only) | Only on RHS of FDs | NEVER |
| LR (Both sides) | On both LHS and RHS | MAYBE |
| N (Neither) | Not in any FD | YES - Always |

Step 2: Start with (L ∪ N) as base

Step 3: Compute closure of base
        - If closure = all attributes → Done, this is key
        - If not → Add attributes from LR one by one

Step 4: Check minimality (no proper subset is key)
```

**Worked Example**:
```
R(A, B, C, D, E)
FDs: {A → B, BC → D, D → E}

Step 1: Classify
- LHS attributes: A, B, C, D
- RHS attributes: B, D, E

| Attr | LHS? | RHS? | Category |
|------|------|------|----------|
| A    | Yes  | No   | L        |
| B    | Yes  | Yes  | LR       |
| C    | Yes  | No   | L        |
| D    | Yes  | Yes  | LR       |
| E    | No   | Yes  | R        |

L = {A, C}, R = {E}, LR = {B, D}, N = {}

Step 2: Base = L ∪ N = {A, C}

Step 3: Compute (AC)+
AC → (A→B) → ABC → (BC→D) → ABCD → (D→E) → ABCDE ✓

Step 4: Check minimality
- A+ = AB ≠ all (not a key alone)
- C+ = C ≠ all (not a key alone)
- So AC is minimal

Answer: Candidate Key = {A, C}
```

### Technique 3.2: Closure Computation (For Verification)

**Algorithm**:
```python
def compute_closure(X, FDs):
    closure = set(X)
    changed = True
    while changed:
        changed = False
        for lhs, rhs in FDs:
            if lhs.issubset(closure) and not rhs.issubset(closure):
                closure = closure.union(rhs)
                changed = True
    return closure
```

**Quick Mental Computation**:
```
Start with X
For each FD α → β:
    If α ⊆ current closure:
        Add β to closure
Repeat until no change
```

---

## 4. Super Key Counting Techniques

### Technique 4.1: Single Candidate Key

**Formula**:
$$\text{Super Keys} = 2^{n-k}$$

Where:
- n = total attributes
- k = size of candidate key

**Quick Reasoning**: 
- Key attributes MUST be present
- Remaining (n-k) attributes CAN be present or not
- 2 choices for each → 2^(n-k) combinations

**Worked Example**:
```
R(A, B, C, D, E) with candidate key {A, B}

n = 5, k = 2
Super Keys = 2^(5-2) = 2³ = 8

Verification:
{AB}, {ABC}, {ABD}, {ABE}, {ABCD}, {ABCE}, {ABDE}, {ABCDE}
Count = 8 ✓
```

### Technique 4.2: Multiple Candidate Keys (Inclusion-Exclusion)

**Formula for 2 Keys**:
$$\text{Super Keys} = 2^{n-|K_1|} + 2^{n-|K_2|} - 2^{n-|K_1 \cup K_2|}$$

**Formula for 3 Keys**:
$$= 2^{n-|K_1|} + 2^{n-|K_2|} + 2^{n-|K_3|}$$
$$- 2^{n-|K_1 \cup K_2|} - 2^{n-|K_2 \cup K_3|} - 2^{n-|K_1 \cup K_3|}$$
$$+ 2^{n-|K_1 \cup K_2 \cup K_3|}$$

**Worked Example**:
```
R(A, B, C, D, E) with candidate keys {AB} and {CD}

n = 5
|K1| = 2, |K2| = 2
|K1 ∪ K2| = |{A,B,C,D}| = 4

Super Keys = 2^(5-2) + 2^(5-2) - 2^(5-4)
           = 8 + 8 - 2
           = 14
```

---

## 5. Relational Algebra Techniques

### Technique 5.1: Query Translation

**English to Algebra Pattern Matching**:

| English Phrase | Relational Algebra |
|----------------|-------------------|
| "Find all X where condition" | σ_condition(R) |
| "Show only columns A, B" | π_{A,B}(R) |
| "From both tables" | R × S or R ⋈ S |
| "Not in" | R - S or R ▷ S |
| "All X that have every Y" | R ÷ S (Division) |

### Technique 5.2: Division Problems (Most Difficult!)

**Problem Pattern**: "Find X associated with ALL Y"

**Algorithm**:
```
R ÷ S = π_A(R) - π_A((π_A(R) × S) - R)

Step-by-step:
1. π_A(R): Get all X values
2. π_A(R) × S: All possible (X, Y) combinations
3. (Step 2) - R: Missing combinations
4. π_A(Step 3): X values missing some Y
5. π_A(R) - Step 4: X values with ALL Y
```

**Worked Example**:
```
Question: Find students enrolled in ALL required courses

Enrolled(sid, cid):        Required(cid):
| sid | cid |              | cid |
|-----|-----|              |-----|
| S1  | C1  |              | C1  |
| S1  | C2  |              | C2  |
| S2  | C1  |

Solution:
1. π_sid(Enrolled) = {S1, S2}
2. {S1, S2} × {C1, C2} = {(S1,C1), (S1,C2), (S2,C1), (S2,C2)}
3. Step2 - Enrolled = {(S2, C2)}  ← S2 missing C2
4. π_sid(Step3) = {S2}
5. {S1, S2} - {S2} = {S1}

Answer: S1 is enrolled in all required courses
```

### Technique 5.3: Counting Tuples

**Quick Bounds**:

| Operation | Min | Max |
|-----------|-----|-----|
| σ_p(R) | 0 | \|R\| |
| π_A(R) | 1 (if R≠∅) | \|R\| |
| R ∪ S | max(\|R\|,\|S\|) | \|R\|+\|S\| |
| R ∩ S | 0 | min(\|R\|,\|S\|) |
| R - S | 0 | \|R\| |
| R × S | \|R\|×\|S\| | \|R\|×\|S\| |
| R ⋈ S | 0 | \|R\|×\|S\| |

---

## 6. SQL Query Analysis Techniques

### Technique 6.1: Execution Order Tracing

**Always Remember This Order**:
```
FROM    → 1. Identify tables
WHERE   → 2. Filter rows
GROUP BY→ 3. Create groups
HAVING  → 4. Filter groups
SELECT  → 5. Compute columns
ORDER BY→ 6. Sort results
LIMIT   → 7. Limit output

Mnemonic: "From Where Grandpa Had Selected Oranges Lately"
```

### Technique 6.2: NULL Handling (Critical!)

**Decision Table for Comparisons**:
```
NULL = NULL     → UNKNOWN (not TRUE!)
NULL <> NULL    → UNKNOWN
NULL = anything → UNKNOWN
NULL AND TRUE   → UNKNOWN
NULL AND FALSE  → FALSE
NULL OR TRUE    → TRUE
NULL OR FALSE   → UNKNOWN
```

**NOT IN Trap Detection**:
```
If subquery can return NULL:
  - NOT IN with NULL → Returns EMPTY (no rows!)
  
Fix: Use NOT EXISTS or filter NULL
```

**Worked Example**:
```sql
-- TRAP: This returns EMPTY if any Y is NULL
SELECT * FROM T1 WHERE X NOT IN (SELECT Y FROM T2);

-- SOLUTION 1: Filter NULLs
SELECT * FROM T1 WHERE X NOT IN (SELECT Y FROM T2 WHERE Y IS NOT NULL);

-- SOLUTION 2: Use NOT EXISTS
SELECT * FROM T1 t1 WHERE NOT EXISTS (SELECT 1 FROM T2 t2 WHERE t2.Y = t1.X);
```

### Technique 6.3: Aggregate Function Behavior

| Scenario | COUNT(*) | COUNT(col) | SUM/AVG |
|----------|----------|------------|---------|
| All NULL | Row count | 0 | NULL |
| Some NULL | Row count | Non-NULL count | Ignores NULL |
| Empty table | 0 | 0 | NULL |

**GATE Trap**: AVG ignores NULL, doesn't treat as 0!
```
Values: 100, NULL, 200
AVG = (100 + 200) / 2 = 150  (NOT 100!)
```

---

## 7. Normalization Techniques

### Technique 7.1: Quick Normal Form Check

**Decision Flowchart**:
```
Start
  │
  ▼
All atomic values?
  │ No → NOT 1NF
  │ Yes
  ▼
Any partial dependency?
(Part of key → Non-prime)
  │ Yes → 1NF only
  │ No
  ▼
Any transitive dependency?
(Non-prime → Non-prime)
  │ Yes → 2NF only
  │ No
  ▼
For all FDs X→A:
Is X superkey OR A prime?
  │ No → NOT 3NF (but check for 2NF first)
  │ Yes
  ▼
For all FDs X→A:
Is X superkey?
  │ No → 3NF only
  │ Yes → BCNF ✓
```

### Technique 7.2: Canonical Cover Computation

**Algorithm**:
```
1. Make RHS single attribute (decompose A→BC to A→B, A→C)

2. Remove extraneous LHS attributes:
   For each FD X→A, for each B in X:
     If A ∈ (X-B)+ then remove B from X

3. Remove redundant FDs:
   For each FD X→A:
     If A ∈ X+ (computed without this FD) then remove FD

4. Combine same LHS (X→A, X→B becomes X→AB)
```

### Technique 7.3: Lossless Decomposition Check

**Rule for 2 Relations**:
```
Decomposition of R into R1 and R2 is lossless iff:

(R1 ∩ R2) → R1   OR   (R1 ∩ R2) → R2

In other words: Common attributes must be key of at least one relation
```

**Quick Check Method**:
```
1. Find R1 ∩ R2 (common attributes)
2. Compute (R1 ∩ R2)+
3. If closure contains all of R1 OR all of R2 → Lossless
4. Otherwise → Lossy
```

---

## 8. Serializability Checking Techniques

### Technique 8.1: Precedence Graph Method

**Algorithm**:
```
1. Create node for each transaction

2. For each pair of conflicting operations:
   - R_i(X) ... W_j(X): Add edge Ti → Tj
   - W_i(X) ... R_j(X): Add edge Ti → Tj
   - W_i(X) ... W_j(X): Add edge Ti → Tj
   
   (Note: R_i ... R_j is NOT a conflict!)

3. Check for cycles:
   - No cycle → Conflict Serializable
   - Cycle exists → NOT Conflict Serializable
```

**Conflict Detection Shortcut**:
```
Only these are conflicts:
- Read-Write on same item (different transactions)
- Write-Read on same item (different transactions)
- Write-Write on same item (different transactions)

NOT a conflict:
- Read-Read (both just reading)
- Same transaction operations
```

**Worked Example**:
```
Schedule: R1(A) R2(A) W1(A) W2(A) R1(B) W2(B)

Identify conflicts:
1. R2(A) before W1(A): T2 → T1
2. W1(A) before W2(A): T1 → T2
3. R1(B) before W2(B): T1 → T2

Draw graph:
T1 ⟷ T2 (edges in both directions)

Cycle found! → NOT Conflict Serializable
```

### Technique 8.2: 2PL Verification

**Check Rule**:
```
For each transaction:
- All Lock operations must come before all Unlock operations
- No Lock after any Unlock

If TRUE for all transactions → Valid 2PL → Conflict Serializable
```

### Technique 8.3: Timestamp Protocol Analysis

**Rules to Check**:
```
For Read(X) by Ti:
  If TS(Ti) < W-TS(X): REJECT
  Else: Execute, R-TS(X) = max(R-TS(X), TS(Ti))

For Write(X) by Ti:
  If TS(Ti) < R-TS(X): REJECT
  If TS(Ti) < W-TS(X): REJECT (or ignore with Thomas Write Rule)
  Else: Execute, W-TS(X) = TS(Ti)
```

---

## 9. B+ Tree Calculation Techniques

### Technique 9.1: Order Calculation

**Internal Node Order (p)**:
```
Each internal node has: (p-1) keys, p pointers

Space equation: (p-1)×K + p×P ≤ B

Solving: p ≤ (B + K) / (K + P)

Formula: p = ⌊(B + K) / (K + P)⌋
```

**Leaf Node Order (p_L)**:
```
Each leaf has: (p_L-1) key-pointer pairs, 1 sibling pointer

Space equation: (p_L-1)×(K + Pr) + P ≤ B

Formula: p_L = ⌊(B - P) / (K + Pr)⌋ + 1
```

### Technique 9.2: Height/Level Calculation

**Number of Leaf Nodes**:
```
Leaves = ⌈n / (p_L - 1)⌉

where n = number of records
```

**Height Calculation**:
```
Height h = ⌈log_p(Leaves)⌉

Quick estimate: h ≈ ⌈log_p(n)⌉
```

### Technique 9.3: Search Cost

```
Block accesses = Height + 1
               = ⌈log_p(n)⌉ + 1

(Height levels of tree traversal + 1 data block access)
```

**Worked Example**:
```
Given:
- Block size B = 512 bytes
- Key size K = 10 bytes
- Tree pointer P = 6 bytes
- Data pointer Pr = 6 bytes
- Records n = 100,000

Step 1: Internal order
p = ⌊(512 + 10)/(10 + 6)⌋ = ⌊522/16⌋ = 32

Step 2: Leaf order
p_L = ⌊(512 - 6)/(10 + 6)⌋ + 1 = ⌊506/16⌋ + 1 = 31 + 1 = 32

Step 3: Leaves
Leaves = ⌈100,000/31⌉ = 3,226

Step 4: Height
h = ⌈log_32(3226)⌉ = ⌈2.3⌉ = 3

Step 5: Search cost = 3 + 1 = 4 block accesses
```

---

## 10. Recovery Analysis Techniques

### Technique 10.1: UNDO/REDO Determination

**Decision Matrix**:
```
After crash, for each transaction:

| Committed? | Action |
|------------|--------|
| Yes (commit in log) | REDO (ensure changes persist) |
| No (no commit) | UNDO (rollback changes) |
```

### Technique 10.2: Checkpoint Analysis

**Recovery Scope**:
```
1. Find last checkpoint
2. Get active transaction list from checkpoint
3. Scan forward from checkpoint:
   - New start → Add to undo-list
   - Commit → Remove from undo-list
4. Final undo-list = Transactions to UNDO
5. All committed since checkpoint = REDO
```

**Worked Example**:
```
Log:
<T1, start>
<T1, A, 100, 90>
<CHECKPOINT, {T1}>
<T2, start>
<T2, B, 200, 210>
<T1, commit>
<T3, start>
<T3, C, 300, 350>
--- CRASH ---

Analysis:
1. Checkpoint has {T1}
2. undo-list = {T1}
3. Forward scan:
   - T2 starts: undo-list = {T1, T2}
   - T1 commits: undo-list = {T2}
   - T3 starts: undo-list = {T2, T3}
4. Final: UNDO T2, T3; REDO T1
```

### Technique 10.3: WAL Rule Verification

**Two Rules to Check**:
```
1. UNDO Rule: Log record written before data page flush
2. REDO Rule: All log records written before commit

Violation Detection:
- If data written before log → UNDO rule violated
- If commit before log flush → REDO rule violated
```

---

## 🏆 Quick Reference: Formula Sheet

### Keys
```
Super Keys (single CK): 2^(n-k)
Super Keys (multiple CK): Use Inclusion-Exclusion
```

### Indexing
```
Blocking Factor: bfr = ⌊B/R⌋
Number of Blocks: b = ⌈r/bfr⌉
B+ Tree Order: p = ⌊(B+K)/(K+P)⌋
B+ Tree Height: h = ⌈log_p(n)⌉
Search Cost: h + 1 block accesses
```

### File Organization
```
Linear Search: b/2 average, b worst
Binary Search: ⌈log_2(b)⌉
Primary Index Search: ⌈log_2(b_i)⌉ + 1
```

### Joins
```
Nested Loop: b_R + n_R × b_S
Block Nested Loop: b_R + b_R × b_S
Hash Join: 3(b_R + b_S)
```

---

## 📌 Final Tips for Exam Day

1. **Start with classification**: What type of problem is this?
2. **Write down the formula first**: Before plugging numbers
3. **Draw diagrams**: For schedules, ER, precedence graphs
4. **Check edge cases**: NULL, empty sets, single elements
5. **Verify with sanity check**: Does the answer make sense?
6. **Manage time**: Don't spend >3 min on any question
7. **Mark and move**: If stuck, mark and return later

---

> **Master these techniques, and DBMS becomes your scoring subject!**

---

[← Back to DBMS Home](./README.md)
