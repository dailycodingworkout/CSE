# DBMS Quick Revision Sheet for GATE & ESE

> 🎯 **Purpose**: Last-minute revision covering all critical formulas, tricks, and concepts

---

## 📌 Chapter 1: Introduction

| Concept | Key Point |
|---------|-----------|
| Three-Schema | External → Conceptual → Internal |
| Physical Independence | Easier (storage changes) |
| Logical Independence | Harder (schema changes) |
| DDL | CREATE, ALTER, DROP, TRUNCATE |
| DML | SELECT, INSERT, UPDATE, DELETE |
| DCL | GRANT, REVOKE |
| TCL | COMMIT, ROLLBACK, SAVEPOINT |

**TRUNCATE vs DELETE**: TRUNCATE = DDL (no rollback), DELETE = DML (rollback possible)

---

## 📌 Chapter 2: ER Model

| Symbol | Meaning |
|--------|---------|
| Rectangle | Strong Entity |
| Double Rectangle | Weak Entity |
| Diamond | Relationship |
| Double Diamond | Identifying Relationship |
| Ellipse | Attribute |
| Double Ellipse | Multi-valued Attribute |
| Dashed Ellipse | Derived Attribute |
| Double Line | Total Participation |

### Minimum Tables Formula
| Relationship | Min Tables |
|--------------|------------|
| 1:1 (both total) | 1 |
| 1:1 (partial) | 2 |
| 1:N | 2 |
| M:N | 3 |

**Weak Entity PK** = Owner's PK + Partial Key

---

## 📌 Chapter 3: Relational Model

### Super Key Formula
```
Given n attributes, candidate key of size k:
Number of Super Keys = 2^(n-k)

Multiple CKs: Use inclusion-exclusion principle
```

### NULL Logic
```
NULL = NULL → UNKNOWN (not TRUE!)
NULL AND FALSE = FALSE
NULL OR TRUE = TRUE
NULL AND TRUE = UNKNOWN
```

---

## 📌 Chapter 4: Relational Algebra

| Operation | Cardinality Change | Degree Change |
|-----------|-------------------|---------------|
| σ (Select) | ≤ original | Same |
| π (Project) | ≤ original | ≤ original |
| × (Cross) | Product | Sum |
| ⋈ (Natural) | ≤ product | ≤ sum |
| ∪ (Union) | ≤ sum | Same |
| − (Difference) | ≤ first | Same |

**Key Facts**:
- π removes duplicates (unlike SQL SELECT)
- Natural join on no common attrs = Cross product
- Division = "for all" semantics

---

## 📌 Chapter 5: SQL

### Execution Order
```
FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT
```

### COUNT Variations
| Expression | Counts |
|------------|--------|
| COUNT(*) | All rows (including NULL) |
| COUNT(col) | Non-NULL values |
| COUNT(DISTINCT col) | Unique non-NULL values |

### Key Rules
- WHERE filters rows, HAVING filters groups
- SELECT columns must be in GROUP BY or aggregate
- UNION removes duplicates, UNION ALL keeps them

---

## 📌 Chapter 6: Normalization

### Normal Forms Quick Check
| NF | Requirement |
|----|-------------|
| 1NF | Atomic values |
| 2NF | 1NF + No partial dependency |
| 3NF | 2NF + No transitive dependency |
| BCNF | Every determinant is superkey |

### Closure Algorithm
```
X⁺ = X
repeat:
    for each FD α → β:
        if α ⊆ X⁺: X⁺ = X⁺ ∪ β
until no change
```

### Armstrong's Axioms (RAT)
- **R**eflexivity: Y ⊆ X → X → Y
- **A**ugmentation: X → Y → XZ → YZ
- **T**ransitivity: X → Y ∧ Y → Z → X → Z

### Lossless Decomposition Test
```
R1 ∩ R2 → R1  OR  R1 ∩ R2 → R2
(Common attributes must be key of one side)
```

---

## 📌 Chapter 7: Transactions

### ACID
- **A**tomicity: All or nothing
- **C**onsistency: Valid states only
- **I**solation: Concurrent = Serial
- **D**urability: Committed = Permanent

### Conflict Conditions
```
Different transactions + Same item + At least one Write
```

### Precedence Graph
- No cycle → Conflict Serializable
- Has cycle → NOT Conflict Serializable

### Hierarchy
```
Conflict Serializable ⊂ View Serializable
Strict ⊂ Cascadeless ⊂ Recoverable
```

---

## 📌 Chapter 8: Concurrency Control

### 2PL Phases
```
Growing Phase (acquire) → Lock Point → Shrinking Phase (release)
```

### 2PL Variants
| Variant | Holds X-locks until | Prevents Cascading |
|---------|---------------------|-------------------|
| Basic 2PL | After operation | No |
| Strict 2PL | Commit | Yes |
| Rigorous 2PL | Commit (all locks) | Yes |

### Deadlock Prevention
| Scheme | Older Ti | Younger Ti |
|--------|----------|------------|
| Wait-Die | Waits | Dies |
| Wound-Wait | Wounds | Waits |

### Timestamp Rules
```
Read X:  If TS(Ti) < W-TS(X): Abort
Write X: If TS(Ti) < R-TS(X): Abort
         If TS(Ti) < W-TS(X): Ignore (Thomas) or Abort
```

---

## 📌 Chapter 9: Indexing

### B+ Tree Formulas
```
Order n:
- Internal: max (n-1) keys, n children
- Internal (non-root) min: ⌈n/2⌉ children
- Leaf: max (n-1) records
- Leaf min: ⌈(n-1)/2⌉ records

Order calculation:
n = ⌊(Block - Pointer) / (Key + Pointer)⌋ + 1
```

### Index Types
| Type | Dense/Sparse | File Requirement |
|------|--------------|------------------|
| Primary | Sparse | Sorted on key |
| Secondary | Dense | Any |

### Access Costs
| Method | Blocks |
|--------|--------|
| Linear Scan | b_r |
| Binary Search | ⌈log₂(b_r)⌉ |
| B+ Tree | h + 1 |

---

## 📌 Chapter 10: Query Optimization

### Join Costs
| Algorithm | Cost |
|-----------|------|
| Simple NL | n_r × b_s + b_r |
| Block NL | b_r × b_s + b_r |
| Index NL | b_r + n_r × (h+1) |
| Hash | 3 × (b_r + b_s) |

### Optimization Rule Priority
1. Push selections down (most important!)
2. Push projections down
3. Avoid Cartesian products
4. Use indexes

---

## 📌 Chapter 11: Recovery

### WAL Rules
- UNDO: Log with old value before page to disk
- REDO: All logs before commit

### Steal/Force Combinations
| Policy | UNDO | REDO |
|--------|------|------|
| No-Steal + Force | No | No |
| Steal + No-Force | Yes | Yes |

### ARIES Phases
```
Analysis → REDO (forward) → UNDO (backward)
```

### Recovery Actions
| Transaction State | Action |
|-------------------|--------|
| Committed after checkpoint | REDO |
| Uncommitted | UNDO |
| Committed before checkpoint | Already on disk |

---

## 📌 Chapter 12: Distributed DB

### Fragmentation
| Type | Operation | Reconstruction |
|------|-----------|----------------|
| Horizontal | Selection | Union |
| Vertical | Projection | Natural Join |

### 2PC
```
All Yes → COMMIT
Any No → ABORT
```

### CAP Theorem
```
Can only guarantee 2 of 3:
- Consistency
- Availability  
- Partition Tolerance

In practice: P is required, choose C or A
```

---

## 🔢 Critical Formulas

### Blocking Factor
```
bfr = ⌊Block Size / Record Size⌋
```

### Number of Blocks
```
Blocks = ⌈Records / bfr⌉
```

### Super Keys
```
2^(n-k) where k = size of candidate key
```

### B+ Tree Height
```
h = ⌈log_{⌈n/2⌉}(Records)⌉
```

### Join Result Size
```
|R ⋈ S| = (n_r × n_s) / max(V(A,r), V(A,s))
```

---

## ⚡ Top 20 GATE Traps

1. TRUNCATE is DDL (not DML)
2. NULL = NULL returns UNKNOWN (not TRUE)
3. π removes duplicates (unlike SQL SELECT)
4. 2NF applies only with composite key
5. BCNF may lose dependency preservation
6. 2PL can cause deadlock
7. Primary index = Sparse
8. Secondary index = Dense
9. Conflict Serializable ⊂ View Serializable
10. Recoverable ≠ Serializable
11. Wait-Die: Young dies, Wound-Wait: Young waits
12. B+ Tree: Data only in leaves
13. Hash: O(1) equality, O(n) range
14. Natural join on no common attrs = Cross product
15. Weak entity PK = Owner PK + Partial key
16. Derived attributes are NOT stored
17. REDO = forward, UNDO = backward
18. CAP: Can't have all 3 during partition
19. 2PC is blocking (coordinator failure)
20. Vertical fragmentation must include key

---

## 🎯 Last-Minute Memory Aids

### Schema Architecture
> **ECI** = External, Conceptual, Internal

### Armstrong's Axioms
> **RAT** = Reflexivity, Augmentation, Transitivity

### SQL Execution Order
> **FWGHSD OL** = From Where Group Having Select Distinct Order Limit

### Deadlock Schemes
> **Wait-Die**: Young dies | **Wound-Wait**: Young waits

### Recovery Phases
> **ARU** = Analysis, Redo, Undo

### CAP Theorem
> **Pick 2**: In distributed systems, P is required, choose C or A

---

*Good luck with your GATE/ESE exam!* 🎓
