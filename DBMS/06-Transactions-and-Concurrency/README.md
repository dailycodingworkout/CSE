# 📚 Chapter 06: Transactions & Concurrency Control

> **The Atomic Truth**: *Serialize concurrent operations while maintaining ACID properties.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 6-10 marks (HIGHEST alongside Normalization!) |
| Frequency | Every year, multiple questions |
| Type | MCQ + NAT (schedule analysis, lock compatibility) |
| Difficulty | Hard |
| Hot Topics | Serializability, 2PL, Deadlock, Timestamp ordering |

---

## 1. Transaction Fundamentals

### What is a Transaction?
A **transaction** is a logical unit of work that comprises one or more database operations, treated as a single indivisible unit.

### Transaction States

```
                    ┌──────────────────────────────────┐
                    ▼                                  │
┌────────┐    ┌──────────┐    ┌──────────┐    ┌───────┴───────┐
│ Active │───►│ Partially│───►│Committed │    │   Aborted     │
│        │    │ Committed│    │          │    │               │
└────────┘    └──────────┘    └──────────┘    └───────────────┘
     │              │                                  ▲
     │              └──────────────────────────────────┤
     └─────────────────────────────────────────────────┘
                     (Failure at any point)
```

| State | Description |
|-------|-------------|
| **Active** | Transaction is executing |
| **Partially Committed** | Final statement executed, awaiting commit |
| **Committed** | Changes made permanent |
| **Failed** | Normal execution cannot proceed |
| **Aborted** | Rolled back, DB restored to pre-transaction state |

---

## 2. ACID Properties

### The Foundation of Transaction Processing

| Property | Definition | Mechanism |
|----------|------------|-----------|
| **Atomicity** | All or nothing - complete or rollback entirely | Logging, undo operations |
| **Consistency** | Valid state to valid state | Integrity constraints, application logic |
| **Isolation** | Concurrent transactions don't interfere | Concurrency control (locks, timestamps) |
| **Durability** | Committed changes survive failures | Logging, write-ahead log |

### ACID Illustrated

```
Bank Transfer: $100 from A to B

ATOMICITY:
  T: Read(A), A = A - 100, Write(A), Read(B), B = B + 100, Write(B)
  Either ALL operations happen or NONE.
  If crash after Write(A): Must undo A's debit.

CONSISTENCY:
  Before: A = 500, B = 300, Total = 800
  After:  A = 400, B = 400, Total = 800
  Conservation of money is maintained.

ISOLATION:
  T1: Transfer $100 from A to B
  T2: Calculate total balance
  T2 must see either (500, 300) or (400, 400), never (400, 300).

DURABILITY:
  Once "Transfer Complete" shown, even power failure won't reverse it.
```

---

## 3. Transaction Operations

### Basic Operations

| Operation | Notation | Description |
|-----------|----------|-------------|
| **Read** | R(X) or read(X) | Read data item X into local buffer |
| **Write** | W(X) or write(X) | Write local buffer value to X |
| **Commit** | C or commit | Make all changes permanent |
| **Abort** | A or abort | Undo all changes |

### Example Transaction

```
T1: Bank transfer of $50 from account A to account B

read(A)
A := A - 50
write(A)
read(B)
B := B + 50
write(B)
commit
```

---

## 4. Schedules

### What is a Schedule?
A **schedule** (or history) is a sequence of operations from one or more transactions, preserving the order within each transaction.

### Types of Schedules

```
                         SCHEDULES
                             │
              ┌──────────────┴──────────────┐
              ▼                              ▼
          SERIAL                        CONCURRENT
      (One after another)            (Interleaved)
              │                              │
              │                    ┌─────────┴─────────┐
              │                    ▼                   ▼
              │               SERIALIZABLE        NON-SERIALIZABLE
              │                    │
              │         ┌──────────┴──────────┐
              │         ▼                      ▼
              │    CONFLICT               VIEW
              │  SERIALIZABLE         SERIALIZABLE
              │         │
              │         ▼
              └────► SERIAL ◄────────────────┘
```

### Serial Schedule
Transactions execute one after another, no interleaving.

```
Serial Schedule (T1 before T2):
T1: R(A) W(A) R(B) W(B) C
T2:                       R(A) W(A) R(B) W(B) C

Serial Schedule (T2 before T1):
T2: R(A) W(A) R(B) W(B) C
T1:                       R(A) W(A) R(B) W(B) C
```

**Property**: Serial schedules are always correct but have poor concurrency.

### Concurrent Schedule
Operations from multiple transactions are interleaved.

```
Concurrent Schedule:
T1: R(A) W(A)      R(B)      W(B) C
T2:           R(A)      W(A)         R(B) W(B) C
```

---

## 5. Conflict Serializability

### Conflicting Operations
Two operations **conflict** if:
1. They belong to **different transactions**
2. They access the **same data item**
3. **At least one is a write**

### Types of Conflicts

| Conflict | Operations | Symbol |
|----------|------------|--------|
| Read-Write (RW) | R₁(X) ... W₂(X) | T₁ → T₂ |
| Write-Read (WR) | W₁(X) ... R₂(X) | T₁ → T₂ |
| Write-Write (WW) | W₁(X) ... W₂(X) | T₁ → T₂ |

**Note**: R-R (Read-Read) is NOT a conflict!

### Conflict Equivalence
Two schedules are **conflict equivalent** if one can be transformed into the other by swapping non-conflicting operations.

### Conflict Serializable
A schedule is **conflict serializable** if it is conflict equivalent to some serial schedule.

### Precedence Graph (Conflict Graph)

**Algorithm**:
1. Create a node for each transaction
2. Add edge Tᵢ → Tⱼ if:
   - Tᵢ has an operation O₁
   - Tⱼ has an operation O₂
   - O₁ and O₂ conflict
   - O₁ appears before O₂ in schedule

**Test**: Schedule is conflict serializable ⟺ Precedence graph is **acyclic**

### Example: Precedence Graph

```
Schedule S:
R₁(A) R₂(A) W₁(A) R₁(B) W₂(A) R₂(B) W₁(B) W₂(B)

Conflicts:
- R₂(A) before W₁(A): T₂ → T₁
- W₁(A) before W₂(A): T₁ → T₂
- R₁(B) before W₂(B): T₁ → T₂
- W₁(B) before W₂(B): T₁ → T₂
- W₂(A) before nothing
- R₂(B) before W₁(B): T₂ → T₁

Edges: T₂ → T₁, T₁ → T₂

Precedence Graph:
    T₁ ←→ T₂ (Cycle!)
    
CYCLE EXISTS → NOT Conflict Serializable
```

### Example: Acyclic Graph

```
Schedule S:
R₁(A) W₁(A) R₂(A) W₂(A) R₁(B) W₁(B) R₂(B) W₂(B)

Conflicts:
- W₁(A) before R₂(A): T₁ → T₂
- W₁(A) before W₂(A): T₁ → T₂
- W₁(B) before R₂(B): T₁ → T₂
- W₁(B) before W₂(B): T₁ → T₂

Edges: T₁ → T₂ (only direction)

Precedence Graph:
    T₁ → T₂ (No cycle)
    
NO CYCLE → Conflict Serializable
Equivalent serial schedule: T₁, T₂
```

---

## 6. View Serializability

### View Equivalence
Two schedules S and S' are **view equivalent** if:
1. **Initial Read**: If Tᵢ reads initial value of X in S, it does so in S'
2. **Read From**: If Tᵢ reads value written by Tⱼ in S, it does so in S'
3. **Final Write**: If Tᵢ performs final write on X in S, it does so in S'

### View Serializable
A schedule is **view serializable** if it is view equivalent to some serial schedule.

### Relationship

$$\text{Conflict Serializable} \subset \text{View Serializable} \subset \text{Serializable}$$

### Blind Writes and View Serializability

**Blind Write**: Writing without reading first.

```
Schedule with blind writes:
T₁: W(A)
T₂: W(A)
T₃: W(A)

Any order of T₁, T₂, T₃ is view equivalent!
This is VIEW serializable but may not be CONFLICT serializable.
```

### Checking View Serializability
- Testing view serializability is **NP-Complete**
- Not practical for real systems
- GATE usually tests conflict serializability

### GATE Trap Alert! 🚨
**Conflict Serializable ⟹ View Serializable (but not vice versa)**

If precedence graph has no cycle → Both conflict and view serializable.
If precedence graph has cycle → May still be view serializable (check manually).

---

## 7. Recoverability

### Recoverable Schedule
A schedule is **recoverable** if for each transaction Tⱼ that reads from Tᵢ:
- Tᵢ commits before Tⱼ commits (or Tⱼ doesn't commit)

```
Non-Recoverable Schedule:
T₁: W(A) ...           ... (crash before commit)
T₂:       R(A) ... C

T₂ committed using T₁'s value, but T₁ never committed!
Cannot recover to consistent state.

Recoverable Schedule:
T₁: W(A) ...           C
T₂:       R(A) ...       C

T₂ commits after T₁ commits. Safe!
```

### Cascadeless Schedule
A schedule is **cascadeless** (avoids cascading rollbacks) if:
- Each transaction reads only values written by committed transactions

```
Cascading Rollback:
T₁: W(A) ... Abort
T₂:       R(A) W(B)
T₃:               R(B) W(C)

T₁ aborts → T₂ must abort (read from T₁)
         → T₃ must abort (read from T₂)

Cascadeless:
Only read committed values → No cascading rollbacks.
```

### Strict Schedule
A schedule is **strict** if:
- No transaction reads or writes X until the last transaction that wrote X has committed or aborted

### Hierarchy

$$\text{Strict} \subset \text{Cascadeless} \subset \text{Recoverable}$$

All strict schedules are cascadeless.
All cascadeless schedules are recoverable.

---

## 8. Lock-Based Concurrency Control

### Binary Locks
Simple lock/unlock mechanism.

| Operation | Description |
|-----------|-------------|
| Lock(X) | Acquire exclusive lock on X |
| Unlock(X) | Release lock on X |

### Shared/Exclusive Locks

| Lock Mode | Also Called | Purpose | Compatibility |
|-----------|-------------|---------|---------------|
| **Shared (S)** | Read lock | Allow reading | Compatible with S |
| **Exclusive (X)** | Write lock | Allow reading and writing | Not compatible with any |

### Lock Compatibility Matrix

|  | S | X |
|--|---|---|
| **S** | ✓ | ✗ |
| **X** | ✗ | ✗ |

### Lock-Based Protocol Rules
1. A transaction must acquire appropriate lock before access
2. A transaction cannot acquire conflicting lock held by another
3. A transaction must release locks (eventually)

---

## 9. Two-Phase Locking (2PL)

### The 2PL Protocol
A transaction follows **2PL** if all locking operations precede all unlocking operations.

```
      Locks
        ▲
        │    Growing      Shrinking
        │    Phase        Phase
        │      ◄──────┬───────►
        │             │
        │    ┌───────►│
        │   ╱         │╲
        │  ╱          │ ╲
        │ ╱           │  ╲
        │╱            │   ╲
        └─────────────┼─────────────► Time
                   Lock
                   Point
```

### Two Phases
1. **Growing Phase**: Transaction may acquire locks, but not release any
2. **Shrinking Phase**: Transaction may release locks, but not acquire any

### 2PL Guarantees Conflict Serializability

**Theorem**: Any schedule of transactions following 2PL is conflict serializable.

### Variants of 2PL

| Variant | Description | Guarantees |
|---------|-------------|------------|
| **Basic 2PL** | Standard growing/shrinking phases | Conflict serializability |
| **Strict 2PL** | Hold all X locks until commit/abort | Conflict serializable + Strict |
| **Rigorous 2PL** | Hold ALL locks until commit/abort | Conflict serializable + Strict |

```
Basic 2PL:
T: Lock(A) Lock(B) Unlock(A) Unlock(B) Commit
   ←─ Growing ─→  ←─ Shrinking ─→

Strict 2PL:
T: Lock-X(A) Lock-X(B) ........ Commit; Unlock(A) Unlock(B)
   X-locks held until commit

Rigorous 2PL:
T: Lock-S(A) Lock-X(B) ........ Commit; Unlock(A) Unlock(B)
   ALL locks held until commit
```

### GATE Trap Alert! 🚨
**2PL prevents cascading rollback only if STRICT or RIGOROUS!**

Basic 2PL allows releases before commit, enabling dirty reads.

---

## 10. Deadlock

### What is Deadlock?
**Deadlock** occurs when two or more transactions are waiting for each other to release locks.

```
T₁ holds Lock(A), waiting for Lock(B)
T₂ holds Lock(B), waiting for Lock(A)

     T₁ ─waits─► T₂
      ▲          │
      │          │
      └───waits──┘

CIRCULAR WAIT = DEADLOCK
```

### Deadlock Handling

| Method | Description | Action |
|--------|-------------|--------|
| **Prevention** | Ensure deadlock can never occur | Order resources, timestamps |
| **Detection** | Allow deadlocks, detect and resolve | Wait-for graph |
| **Avoidance** | Don't enter unsafe states | Banker's algorithm (rare in DBMS) |
| **Timeout** | Abort after waiting too long | Simple but imprecise |

### Wait-Die and Wound-Wait (Prevention)

Assign timestamps (older = lower number):

| Scheme | Older → Younger | Younger → Older |
|--------|-----------------|-----------------|
| **Wait-Die** | Wait | Die (abort younger) |
| **Wound-Wait** | Wound (abort younger) | Wait |

```
Wait-Die (Non-preemptive):
If Tᵢ (older) wants lock held by Tⱼ (younger): Tᵢ WAITS
If Tᵢ (younger) wants lock held by Tⱼ (older): Tᵢ DIES (aborts)

Wound-Wait (Preemptive):
If Tᵢ (older) wants lock held by Tⱼ (younger): Tⱼ WOUNDED (aborts)
If Tᵢ (younger) wants lock held by Tⱼ (older): Tᵢ WAITS
```

### Wait-For Graph (Detection)

- Nodes: Transactions
- Edge Tᵢ → Tⱼ: Tᵢ is waiting for Tⱼ
- **Cycle = Deadlock**

```
T₁ → T₂ → T₃ → T₁ (Cycle! Deadlock detected)

Resolution: Abort one transaction (victim selection)
```

---

## 11. Timestamp-Based Protocols

### Timestamp Ordering (TO)

Each transaction Tᵢ gets timestamp TS(Tᵢ) when it starts.

For each data item X, maintain:
- **W-timestamp(X)**: Largest timestamp of transaction that wrote X
- **R-timestamp(X)**: Largest timestamp of transaction that read X

### TO Protocol Rules

**For Read(X) by Tᵢ**:
- If TS(Tᵢ) < W-timestamp(X): **Reject** (reading too-new value)
- Else: Execute, update R-timestamp(X) = max(R-timestamp(X), TS(Tᵢ))

**For Write(X) by Tᵢ**:
- If TS(Tᵢ) < R-timestamp(X): **Reject** (overwriting already-read value)
- If TS(Tᵢ) < W-timestamp(X): **Reject** (overwriting newer write)
- Else: Execute, update W-timestamp(X) = TS(Tᵢ)

### Thomas Write Rule (Optimization)

When TS(Tᵢ) < W-timestamp(X) for a write:
- **Basic TO**: Reject and rollback
- **Thomas Write Rule**: Ignore the write (don't rollback)

The obsolete write can be safely ignored as a newer value already exists.

### TO Properties
- **Guarantees**: Conflict serializability, no deadlocks
- **Disadvantage**: May have more aborts than 2PL

---

## 12. Multi-Version Concurrency Control (MVCC)

### Concept
Maintain multiple versions of each data item. Readers see older version while writers create new version.

### Benefits
- Readers never block writers
- Writers never block readers
- Higher concurrency

### Multi-Version Timestamp Ordering

For each write, create new version with writer's timestamp.

For read by Tᵢ:
- Find version with largest timestamp ≤ TS(Tᵢ)
- Read that version

### MVCC in Practice
Used in PostgreSQL, MySQL InnoDB, Oracle, etc.

---

## 13. Isolation Levels

### SQL Standard Isolation Levels

| Level | Dirty Read | Non-Repeatable Read | Phantom |
|-------|------------|---------------------|---------|
| **Read Uncommitted** | ✓ | ✓ | ✓ |
| **Read Committed** | ✗ | ✓ | ✓ |
| **Repeatable Read** | ✗ | ✗ | ✓ |
| **Serializable** | ✗ | ✗ | ✗ |

### Phenomena Explained

**Dirty Read**: Reading uncommitted data
```
T₁: W(A) ....... Abort
T₂:     R(A)
T₂ read value that was never committed!
```

**Non-Repeatable Read**: Same query, different results
```
T₁: R(A)          R(A)
T₂:      W(A) C
T₁ reads A twice, gets different values!
```

**Phantom Read**: New rows appear in repeated query
```
T₁: SELECT * WHERE age > 20 .... SELECT * WHERE age > 20
T₂:                         INSERT (id, age=25) C
T₁'s second query returns an extra row!
```

---

## 14. Granularity of Locking

### Lock Hierarchy

```
        Database
           │
     ┌─────┴─────┐
   Table       Table
     │           │
  ┌──┴──┐     ┌──┴──┐
 Page  Page  Page  Page
  │     │     │     │
Tuple Tuple Tuple Tuple
```

### Intention Locks

| Lock | Name | Meaning |
|------|------|---------|
| IS | Intention Shared | Will acquire S lock on descendant |
| IX | Intention Exclusive | Will acquire X lock on descendant |
| SIX | Shared + Intention Exclusive | S on node, IX on descendants |

### Lock Compatibility Matrix (with Intention Locks)

|  | IS | IX | S | SIX | X |
|--|----|----|---|-----|---|
| **IS** | ✓ | ✓ | ✓ | ✓ | ✗ |
| **IX** | ✓ | ✓ | ✗ | ✗ | ✗ |
| **S** | ✓ | ✗ | ✓ | ✗ | ✗ |
| **SIX** | ✓ | ✗ | ✗ | ✗ | ✗ |
| **X** | ✗ | ✗ | ✗ | ✗ | ✗ |

### Multiple Granularity Locking Protocol

1. Must acquire locks root to leaf (top-down)
2. To get S or IS on node, must hold IS or IX on parent
3. To get X, IX, or SIX on node, must hold IX or SIX on parent
4. Must release locks leaf to root (bottom-up)

---

## 15. Serializability Examples (GATE Practice)

### Example 1: Check Conflict Serializability

```
Schedule: R₁(X) R₂(Y) W₃(X) R₁(Y) W₂(Y) R₃(X) W₁(X)

Identify conflicts:
- R₁(X) vs W₃(X): R before W, same X → T₁ → T₃
- W₃(X) vs R₃(X): Same transaction, no edge
- W₃(X) vs W₁(X): W before W, same X → T₃ → T₁
- R₂(Y) vs W₂(Y): Same transaction, no edge
- R₁(Y) vs W₂(Y): R before W, same Y → T₁ → T₂

Edges: T₁ → T₃, T₃ → T₁, T₁ → T₂

Graph:
T₁ ⟷ T₃, T₁ → T₂

Cycle: T₁ ⟷ T₃
NOT Conflict Serializable!
```

### Example 2: 2PL Verification

```
T₁: L(A) R(A) L(B) U(A) W(B) U(B)
T₂: L(B) R(B) L(A) W(A) U(A) U(B)

T₁: L(A) L(B) are before U(A) U(B)? 
    Growing: L(A), L(B)
    Shrinking: U(A), U(B)
    Lock point: After L(B), before U(A)
    ✓ Valid 2PL

T₂: L(B) L(A) are before U(A) U(B)?
    Growing: L(B), L(A)
    Shrinking: U(A), U(B)
    Lock point: After L(A), before U(A)
    ✓ Valid 2PL

Both follow 2PL → Schedule is conflict serializable!
```

### Example 3: Timestamp Ordering

```
TS(T₁) = 10, TS(T₂) = 15
Initially: R-TS(A) = 0, W-TS(A) = 0

Operations: W₁(A), R₂(A), W₂(A), R₁(A)

W₁(A): TS(T₁)=10 ≥ R-TS(A)=0, TS(T₁)=10 ≥ W-TS(A)=0
       Execute. W-TS(A) = 10.

R₂(A): TS(T₂)=15 ≥ W-TS(A)=10
       Execute. R-TS(A) = 15.

W₂(A): TS(T₂)=15 ≥ R-TS(A)=15, TS(T₂)=15 ≥ W-TS(A)=10
       Execute. W-TS(A) = 15.

R₁(A): TS(T₁)=10 < W-TS(A)=15
       REJECT! T₁ must rollback.
```

---

## 16. Common GATE Patterns

### Pattern 1: Precedence Graph
Draw graph, check for cycles, find equivalent serial order.

### Pattern 2: 2PL Compliance
Check if locks before unlocks for each transaction.

### Pattern 3: Deadlock Detection
Draw wait-for graph, find cycles.

### Pattern 4: Timestamp Protocol
Trace R-TS and W-TS, determine accepts/rejects.

### Pattern 5: Isolation Levels
Identify which phenomena are possible.

---

## 🧠 Memory Techniques

### 2PL Phases: "Grow then Glow (away)"
- **Grow**: Acquire locks
- **Glow (away)**: Release locks

### Deadlock Prevention: "Wait-Die = Old Waits, Wound-Wait = Old Wounds"
- Wait-Die: Older waits, younger dies
- Wound-Wait: Older wounds (kills younger), younger waits

### Isolation Levels: "RRRS" (Read, Read, Repeat, Serialize)
- Read Uncommitted
- Read Committed
- Repeatable Read
- Serializable

### Conflict Detection: "RW, WR, WW - No RR"
Only R-W, W-R, W-W are conflicts. Never R-R!

---

## 🔑 Key Takeaways for GATE

1. **Precedence Graph**: Cycle = Not conflict serializable
2. **2PL guarantees serializability**: But not strict without variants
3. **Strict 2PL prevents cascading rollback**: X-locks held until commit
4. **Wait-Die vs Wound-Wait**: Know which aborts in each case
5. **Timestamp Ordering**: Compare TS with R-TS and W-TS
6. **View serializable ⊃ Conflict serializable**: View is more general

---

## 📚 Related Chapters
- [← Previous: Chapter 05 - Normalization](../05-Normalization/README.md)
- [Next: Chapter 07 - Indexing & File Organization →](../07-Indexing-and-File-Organization/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
