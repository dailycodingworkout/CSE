# Chapter 8: Concurrency Control

---

## 🎯 Why Concurrency Control?

**Concurrency Control** ensures:
1. **Isolation** in ACID properties
2. **Correct results** with multiple concurrent transactions
3. **Maximum throughput** without sacrificing correctness

### 🎭 Analogy
> Concurrency control = **Traffic signals at an intersection**
> 
> Without signals: Chaos, collisions
> With signals: Safe, orderly movement

---

## ⚠️ Concurrency Problems

### 1. Lost Update (Write-Write Conflict)
```
T1: Read(A) = 100        T2:
T1: A = A - 10                   
                         T2: Read(A) = 100
T1: Write(A) = 90       
                         T2: A = A + 20
                         T2: Write(A) = 120

Final: A = 120 (T1's update lost!)
Expected: A = 110 (100 - 10 + 20)
```

### 2. Dirty Read (Write-Read Conflict)
```
T1: Read(A) = 100        T2:
T1: A = A - 50
T1: Write(A) = 50
                         T2: Read(A) = 50 (dirty read!)
T1: ABORT (rollback)
                         T2: Uses A = 50 (invalid value!)

T2 read uncommitted (dirty) data that was rolled back.
```

### 3. Non-Repeatable Read
```
T1: Read(A) = 100        T2:
                         T2: Read(A) = 100
                         T2: A = A + 50
                         T2: Write(A) = 150
                         T2: COMMIT
T1: Read(A) = 150 (different value!)

T1 read same item twice, got different values.
```

### 4. Phantom Read
```
T1: SELECT * WHERE Dept='CS'  
    → Returns {Alice, Bob}
                              T2: INSERT (Carol, CS)
                              T2: COMMIT
T1: SELECT * WHERE Dept='CS'
    → Returns {Alice, Bob, Carol}

New row appeared (phantom) between two reads.
```

---

## 🔒 Lock-Based Protocols

### Types of Locks

| Lock Type | Notation | Allows |
|-----------|----------|--------|
| **Shared (S)** | S(X), LS(X) | Read only, multiple holders |
| **Exclusive (X)** | X(X), LX(X) | Read & Write, single holder |

### Lock Compatibility Matrix

| Request \ Hold | S (Shared) | X (Exclusive) |
|----------------|------------|---------------|
| S (Shared) | ✓ Compatible | ✗ Conflict |
| X (Exclusive) | ✗ Conflict | ✗ Conflict |

### 🧠 Memory Trick
> Shared locks **share** with each other
> Exclusive locks are **selfish** (no sharing)

---

## 🔄 Basic Lock Protocol

### Rules
1. Transaction must acquire **S-lock** before reading
2. Transaction must acquire **X-lock** before writing
3. Transaction releases lock when done

### Problem: Does NOT Guarantee Serializability!

```
T1: S(A), R(A), U(A), S(B), R(B), U(B)
T2: X(A), W(A), U(A), X(B), W(B), U(B)

Interleaved:
T1: S(A), R(A), U(A)
T2: X(A), W(A), U(A), X(B), W(B), U(B)
T1: S(B), R(B), U(B)

Not serializable! (T1 sees old A, new B)
```

---

## 📋 Two-Phase Locking (2PL)

### The Protocol
All locks acquired **before** any lock is released.

```
    GROWING PHASE          SHRINKING PHASE
    ──────────────►       ◄──────────────
    
    Acquire locks         Release locks
    (No releases)         (No acquisitions)
         │                     │
         │     Lock Point      │
         └─────────┬───────────┘
                   │
```

### Rules
1. **Growing Phase**: Can only acquire locks
2. **Shrinking Phase**: Can only release locks
3. Once any lock is released → No new locks

### 🎯 Key Theorem
> 2PL guarantees **Conflict Serializability**

### Example
```
T1 (2PL): S(A), S(B), R(A), R(B), U(A), U(B)
          ←───Growing──────→ ←─Shrinking─→

T2 (Not 2PL): S(A), R(A), U(A), S(B), R(B), U(B)
                        ↑         ↑
                     Release   Acquire → Violates 2PL!
```

---

## 🔐 Variations of 2PL

### 1. Basic 2PL
- Guarantees conflict serializability
- May cause **deadlock**
- May cause **cascading rollback**

### 2. Strict 2PL
- Hold all **exclusive locks** until commit/abort
- Prevents cascading rollback
- Most commonly used in practice

```
T1: S(A), X(B), R(A), W(B), COMMIT, U(A), U(B)
                                   ↑
                              X-locks released only at end
```

### 3. Rigorous 2PL
- Hold **ALL locks** (S and X) until commit/abort
- Even stricter than Strict 2PL
- Guarantees serializable order = commit order

```
T1: S(A), X(B), R(A), W(B), COMMIT, U(A), U(B)
                                    ↑
                              All locks released at end
```

### Comparison

| Variant | Serializability | Cascading Rollback | Deadlock |
|---------|----------------|-------------------|----------|
| Basic 2PL | ✓ | Possible | Possible |
| Strict 2PL | ✓ | Prevented | Possible |
| Rigorous 2PL | ✓ | Prevented | Possible |

---

## ⚡ Deadlock

### Definition
Two or more transactions waiting for each other's locks.

### Example
```
T1: X(A), waits for X(B)
T2: X(B), waits for X(A)

T1 → waiting → T2
T2 → waiting → T1
Cycle = Deadlock!
```

### Wait-For Graph
```
T1 ──────► T2
 ▲          │
 │          │
 └──────────┘
    Cycle!
```

---

## 🔄 Deadlock Handling

### 1. Deadlock Prevention

#### Wait-Die (Non-preemptive)
- **Older** transaction waits
- **Younger** transaction dies (rollback)

```
If Ti requests lock held by Tj:
  If TS(Ti) < TS(Tj): Ti waits (older waits for younger)
  Else: Ti dies/aborts (younger dies)
```

#### Wound-Wait (Preemptive)
- **Older** transaction wounds (forces abort) younger
- **Younger** transaction waits

```
If Ti requests lock held by Tj:
  If TS(Ti) < TS(Tj): Ti wounds Tj (older kills younger)
  Else: Ti waits (younger waits for older)
```

### 🧠 Memory Trick
| Scheme | Older (Ti < Tj) | Younger (Ti > Tj) |
|--------|-----------------|-------------------|
| Wait-Die | Ti **waits** | Ti **dies** |
| Wound-Wait | Ti **wounds** Tj | Ti **waits** |

> "**Wait-Die**: Old waits, Young dies"
> "**Wound-Wait**: Old wounds, Young waits"

### 2. Deadlock Detection

- Build wait-for graph periodically
- Detect cycles
- Choose victim and rollback

### 3. Deadlock Timeout

- If transaction waits too long, abort it
- Simple but may abort non-deadlocked transactions

---

## 🌳 Lock Granularity

### Levels of Locking

```
            DATABASE
                │
        ┌───────┼───────┐
        │       │       │
      TABLE   TABLE   TABLE
        │
    ┌───┼───┐
    │   │   │
   PAGE PAGE PAGE
    │
  ┌─┼─┐
  │ │ │
ROW ROW ROW
```

### Trade-offs

| Granularity | Concurrency | Overhead |
|-------------|-------------|----------|
| Coarse (Table) | Low | Low |
| Fine (Row) | High | High |

---

## 🔓 Multiple Granularity Locking

### Intention Locks

| Lock | Meaning |
|------|---------|
| **IS** (Intention Shared) | Intent to get S lock on descendant |
| **IX** (Intention Exclusive) | Intent to get X lock on descendant |
| **SIX** (Shared + IX) | S on node, IX on descendants |

### Compatibility Matrix

| | IS | IX | S | SIX | X |
|---|:---:|:---:|:---:|:---:|:---:|
| **IS** | ✓ | ✓ | ✓ | ✓ | ✗ |
| **IX** | ✓ | ✓ | ✗ | ✗ | ✗ |
| **S** | ✓ | ✗ | ✓ | ✗ | ✗ |
| **SIX** | ✓ | ✗ | ✗ | ✗ | ✗ |
| **X** | ✗ | ✗ | ✗ | ✗ | ✗ |

### Locking Rules
1. Lock root first
2. Lock node only if parent is locked with appropriate intention lock
3. For S/IS on node: Parent must be IS or IX
4. For X/SIX/IX on node: Parent must be IX or SIX

---

## 📊 Timestamp-Based Protocols

### Concept
Each transaction gets a **timestamp** when it starts.
Older timestamp = Higher priority.

### Timestamp Ordering (TO) Protocol

For each data item X, maintain:
- **R-TS(X)**: Largest timestamp of transaction that read X
- **W-TS(X)**: Largest timestamp of transaction that wrote X

### Rules

#### For Ti reading X:
```
If TS(Ti) < W-TS(X):
    Ti trying to read value written by future transaction
    ABORT Ti (rollback and restart with new timestamp)
Else:
    Allow read
    R-TS(X) = max(R-TS(X), TS(Ti))
```

#### For Ti writing X:
```
If TS(Ti) < R-TS(X):
    Ti trying to write value that future transaction already read
    ABORT Ti

If TS(Ti) < W-TS(X):
    Ti trying to write but future transaction already wrote
    Two options:
    a) ABORT Ti
    b) Ignore write (Thomas Write Rule)
    
Else:
    Allow write
    W-TS(X) = TS(Ti)
```

### Thomas Write Rule (Optimization)
If Ti's write is outdated (TS(Ti) < W-TS(X)):
- Instead of aborting, just **ignore the write**
- Write is obsolete anyway

---

## 📋 Timestamp vs 2PL Comparison

| Aspect | 2PL | Timestamp |
|--------|-----|-----------|
| Serializability | Conflict serializable | View serializable (with TWR) |
| Deadlock | Possible | Not possible |
| Starvation | Less likely | Possible |
| Overhead | Lock management | Timestamp tracking |
| Abort rate | Lower | Higher |

---

## 🌊 Optimistic Concurrency Control (OCC)

### Phases

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   READ PHASE    │───►│VALIDATION PHASE │───►│  WRITE PHASE    │
│                 │    │                 │    │                 │
│ Read from DB    │    │ Check for       │    │ Write to DB     │
│ Write to local  │    │ conflicts       │    │ (if validated)  │
│ workspace       │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Validation
For Ti completing validation:
Check all Tj that committed after Ti started:

1. Tj completed before Ti started → OK
2. Tj writes don't intersect Ti reads → OK
3. Otherwise → Abort Ti

### When to Use
- Best for **read-heavy** workloads
- Low conflict scenarios
- High abort rate in write-heavy scenarios

---

## 📱 Multi-Version Concurrency Control (MVCC)

### Concept
Maintain **multiple versions** of each data item.
Readers don't block writers, writers don't block readers.

### How It Works
```
X versions: X₁(ts=10), X₂(ts=25), X₃(ts=40)

Ti with TS=30 reads X:
    Returns X₂ (largest version ≤ 30)

Tj with TS=50 reads X:
    Returns X₃ (largest version ≤ 50)
```

### MVCC Advantages
- Readers never wait
- High concurrency for read-heavy workloads
- Used by PostgreSQL, Oracle, MySQL InnoDB

### MVCC Disadvantages
- Storage overhead (multiple versions)
- Garbage collection needed
- Write-write conflicts still need handling

---

## 🔒 SQL Isolation Levels

### Standard Levels (SQL-92)

| Level | Dirty Read | Non-Repeatable | Phantom |
|-------|:----------:|:--------------:|:-------:|
| **Read Uncommitted** | ✓ Possible | ✓ Possible | ✓ Possible |
| **Read Committed** | ✗ Prevented | ✓ Possible | ✓ Possible |
| **Repeatable Read** | ✗ Prevented | ✗ Prevented | ✓ Possible |
| **Serializable** | ✗ Prevented | ✗ Prevented | ✗ Prevented |

### SQL Syntax
```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

> **Note**: Syntax may vary slightly between database systems (MySQL, PostgreSQL, SQL Server). The above is ANSI SQL standard.

### Implementation Mapping

| Level | Typical Implementation |
|-------|----------------------|
| Read Uncommitted | No read locks |
| Read Committed | Short-duration S-locks |
| Repeatable Read | Long-duration S-locks (2PL) |
| Serializable | 2PL + Range/Predicate locks |

---

## ⚠️ Common GATE Traps

### Trap 1: 2PL and Deadlock
```
2PL guarantees serializability BUT
2PL can cause deadlock
Only Strict/Rigorous 2PL prevents cascading rollback
```

### Trap 2: Wait-Die vs Wound-Wait
```
Wait-Die: Old waits, Young aborts
Wound-Wait: Old kills young, Young waits

Common mistake: Mixing up which one aborts
```

### Trap 3: Timestamp Ordering
```
TS(Ti) < W-TS(X) for READ: Abort (reading from future)
TS(Ti) < R-TS(X) for WRITE: Abort (future already read)
TS(Ti) < W-TS(X) for WRITE: Ignore or Abort (Thomas Write Rule)
```

### Trap 4: Lock Compatibility
```
S-S: Compatible
S-X: NOT compatible
X-X: NOT compatible
```

### Trap 5: MVCC vs 2PL
```
MVCC: Readers don't block writers
2PL: Readers DO block writers (shared lock blocks exclusive)
```

---

## 🧪 Practice Problems

### Q1: Is this 2PL?
```
T1: L(A), L(B), R(A), R(B), U(A), L(C), R(C), U(B), U(C)
                          ↑     ↑
                       Unlock  Lock → Violates 2PL!
Answer: NOT 2PL
```

### Q2: Deadlock Detection
```
T1 waits for T2 (T1 → T2)
T2 waits for T3 (T2 → T3)
T3 waits for T1 (T3 → T1)

Graph: T1 → T2 → T3 → T1 (cycle)
Answer: Deadlock exists
```

### Q3: Wait-Die Decision
```
T1 (ts=5) requests lock held by T2 (ts=10)
T1 is older (5 < 10)
Wait-Die: Old waits → T1 waits
Answer: T1 waits for T2
```

### Q4: Timestamp Protocol
```
X: R-TS = 20, W-TS = 15
T1 (ts=25) wants to read X

Check: TS(T1) = 25 ≥ W-TS(X) = 15 ✓
Action: Allow read, R-TS(X) = max(20, 25) = 25
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Lock Types** | S (shared), X (exclusive) |
| **2PL** | Grow then shrink, guarantees CS |
| **Strict 2PL** | X-locks until commit |
| **Deadlock** | Cycle in wait-for graph |
| **Wait-Die** | Old waits, Young dies |
| **Wound-Wait** | Old wounds, Young waits |
| **Timestamp** | Compare TS with R-TS, W-TS |
| **MVCC** | Multiple versions, readers don't block |

---

## 🎓 Quick Revision Points

1. ✅ 2PL = Growing + Shrinking phases
2. ✅ 2PL guarantees conflict serializability
3. ✅ Strict 2PL prevents cascading rollback
4. ✅ Wait-Die: Old waits, Young dies (aborts)
5. ✅ Wound-Wait: Old wounds (kills), Young waits
6. ✅ Timestamp: Compare TS with R-TS/W-TS
7. ✅ MVCC: Multiple versions, high concurrency

---

*Previous: [Transaction Management](./07-Transaction-Management.md) | Next: [File Organization & Indexing](./09-File-Organization-and-Indexing.md)*
