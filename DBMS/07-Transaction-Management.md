# Chapter 7: Transaction Management

---

## 🎯 What is a Transaction?

A **transaction** is a **logical unit of work** that:
- Contains one or more database operations
- Maintains database consistency
- Either completes entirely or not at all

### 🎭 Analogy
> Transaction = **Bank transfer**
> - Debit from Account A
> - Credit to Account B
> Both must happen, or neither should!

### Transaction States

```
              ┌─────────┐
              │  ACTIVE │◄─── Transaction starts
              └────┬────┘
                   │
          ┌────────┼────────┐
          ▼        │        ▼
    ┌──────────┐   │   ┌──────────┐
    │PARTIALLY │   │   │  FAILED  │
    │COMMITTED │   │   │          │
    └────┬─────┘   │   └────┬─────┘
         │         │        │
         ▼         │        ▼
    ┌──────────┐   │   ┌──────────┐
    │COMMITTED │   │   │ ABORTED  │
    └──────────┘   │   └──────────┘
                   │
              Success/Failure
```

---

## 🔐 ACID Properties

### A - Atomicity
**All or Nothing**: Either all operations complete or none do.

```
Transaction: Transfer $100 from A to B
  1. Debit A by $100
  2. Credit B by $100
  
If crash after step 1: ROLLBACK (undo step 1)
Both succeed or both fail!
```

**Responsibility**: Transaction Manager / Recovery System

### C - Consistency
**Valid States Only**: Database moves from one consistent state to another.

```
Constraint: Total balance must remain constant
Before: A=$500, B=$500, Total=$1000
After:  A=$400, B=$600, Total=$1000 ✓
```

**Responsibility**: Application logic + Integrity constraints

### I - Isolation
**Independent Execution**: Concurrent transactions appear serial.

```
T1: Read A, Write A
T2: Read A, Write A

Isolation ensures T1 and T2 don't interfere
Result should be same as T1;T2 or T2;T1
```

**Responsibility**: Concurrency Control

### D - Durability
**Permanent Changes**: Committed changes survive failures.

```
After COMMIT: Data persists even if power fails
Achieved through: Write-Ahead Logging (WAL)
```

**Responsibility**: Recovery System

### 🧠 Memory Trick: "ACID"
> **A**ll-or-nothing, **C**onsistent states, **I**ndependent execution, **D**urable commits

---

## 📊 Transaction Operations

| Operation | Notation | Description |
|-----------|----------|-------------|
| **Read** | R(X) or r(X) | Read item X from database |
| **Write** | W(X) or w(X) | Write item X to database |
| **Commit** | C or COMMIT | Make changes permanent |
| **Abort** | A or ABORT | Undo all changes |

### Example Transaction
```
T1: BEGIN
    R(A)      -- Read balance of A
    A = A - 100
    W(A)      -- Write new balance of A
    R(B)      -- Read balance of B
    B = B + 100
    W(B)      -- Write new balance of B
    COMMIT
```

---

## 📅 Schedules

### What is a Schedule?
A **schedule** is a sequence of operations from multiple transactions that preserves the order within each transaction.

### Types of Schedules

```
                    Schedules
                        │
        ┌───────────────┴───────────────┐
        │                               │
    Serial                         Non-Serial
   Schedules                        Schedules
                                        │
                        ┌───────────────┼───────────────┐
                        │               │               │
                 Serializable    Non-Serializable
                        │
            ┌───────────┴───────────┐
            │                       │
     Conflict              View
    Serializable        Serializable
```

### Serial Schedule
Transactions execute one after another, no interleaving.

```
T1: R(A), W(A), R(B), W(B)
T2: R(A), W(A)

Serial Schedule 1 (T1 → T2):
R1(A), W1(A), R1(B), W1(B), R2(A), W2(A)

Serial Schedule 2 (T2 → T1):
R2(A), W2(A), R1(A), W1(A), R1(B), W1(B)
```

### Non-Serial Schedule
Operations of different transactions are interleaved.

```
R1(A), R2(A), W1(A), W2(A), R1(B), W1(B)
```

---

## ⚔️ Conflicting Operations

### Definition
Two operations **conflict** if:
1. They belong to **different transactions**
2. They access the **same data item**
3. At least one is a **write** operation

### Conflict Types

| Operation Pair | Conflict? | Reason |
|----------------|-----------|--------|
| R1(A), R2(A) | No | Both reads |
| R1(A), W2(A) | Yes | Read-Write |
| W1(A), R2(A) | Yes | Write-Read |
| W1(A), W2(A) | Yes | Write-Write |
| R1(A), R2(B) | No | Different items |
| W1(A), W2(B) | No | Different items |

### 🧠 Quick Rule
> Conflict = Different transactions + Same item + At least one Write

---

## 🔄 Conflict Serializability

### Definition
A schedule is **conflict serializable** if it can be transformed into a serial schedule by **swapping non-conflicting adjacent operations**.

### Precedence Graph Method

#### Building the Graph
1. Create a node for each transaction
2. Add edge Ti → Tj if:
   - Ti executes R(X) before Tj executes W(X), OR
   - Ti executes W(X) before Tj executes R(X), OR
   - Ti executes W(X) before Tj executes W(X)

#### Check for Serializability
- **No cycle** → Conflict Serializable
- **Has cycle** → NOT Conflict Serializable

### Example 1: Conflict Serializable
```
Schedule S: R1(A), R2(A), W1(A), W2(A)

Conflicts:
- R1(A) before W2(A): T1 → T2
- W1(A) before W2(A): T1 → T2

Precedence Graph:
T1 → T2

No cycle! ✓ Conflict Serializable
Equivalent to: T1 → T2 (serial)
```

### Example 2: NOT Conflict Serializable
```
Schedule S: R1(A), W2(A), W1(A), R2(B), W1(B)

Conflicts:
- R1(A) before W2(A): T1 → T2
- W2(A) before W1(A): T2 → T1
- W1(B) after R2(B): T2 → T1

Precedence Graph:
T1 → T2
T2 → T1

Cycle exists! ✗ NOT Conflict Serializable
```

---

## 👁️ View Serializability

### Definition
A schedule is **view serializable** if it is **view equivalent** to some serial schedule.

### View Equivalence Conditions
Two schedules S and S' are view equivalent if:
1. **Initial Read**: If Ti reads initial value of X in S, Ti reads initial value of X in S'
2. **Updated Read**: If Ti reads value of X written by Tj in S, same in S'
3. **Final Write**: If Ti performs final write on X in S, same in S'

### Relationship
```
Conflict Serializable ⊂ View Serializable

All conflict serializable schedules are view serializable.
NOT all view serializable are conflict serializable.
```

### Blind Write Example
```
Schedule S: W1(A), W2(A), W1(B), W2(B), C1, C2

This is NOT conflict serializable (cycle in precedence graph)
But IS view serializable (equivalent to T2;T1 for final writes)

W2(A) is "blind write" - overwrites without reading
```

### 📊 Comparison

| Property | Conflict Serializable | View Serializable |
|----------|----------------------|-------------------|
| Test | Precedence graph | Complex (NP-complete) |
| Restrictive | More | Less |
| Practical | Yes (used in practice) | Theoretical only |
| Blind writes | Not allowed | Allowed |

---

## 📱 Recoverable Schedules

### Definition
A schedule is **recoverable** if a transaction commits only after all transactions whose data it read have committed.

```
If Tj reads data written by Ti, then:
Commit(Ti) must happen before Commit(Tj)
```

### Non-Recoverable Example
```
Schedule: W1(A), R2(A), C2, A1

T2 commits after reading T1's data
T1 aborts after T2 commits
Problem: T2 has committed with invalid data! ✗
```

### Recoverable Version
```
Schedule: W1(A), R2(A), C1, C2

T1 commits before T2 ✓
If T1 aborts, T2 can also be aborted
```

---

## 🔄 Cascading Rollback

### Definition
When one transaction aborts, other dependent transactions must also abort.

### Example
```
Schedule: W1(A), R2(A), W2(B), R3(B), A1

T1 aborts:
- T2 read T1's data → T2 must abort
- T3 read T2's data → T3 must abort

Cascade: T1 abort → T2 abort → T3 abort
```

### Problem
Cascading rollback is expensive!

### Cascadeless Schedule
A schedule is **cascadeless** (avoids cascading rollback) if transactions only read **committed** data.

```
If Tj reads data written by Ti, then:
Commit(Ti) must happen before Read_j(X)
```

---

## 🔒 Strict Schedule

### Definition
A schedule is **strict** if:
- No read of uncommitted data
- No write of uncommitted data

```
If Tj reads or writes X written by Ti, then:
Commit(Ti) or Abort(Ti) must happen before operation_j(X)
```

### Hierarchy
```
Strict ⊂ Cascadeless ⊂ Recoverable

Every strict schedule is cascadeless.
Every cascadeless schedule is recoverable.
```

---

## 📊 Schedule Hierarchy Summary

```
                        All Schedules
                              │
                    ┌─────────┴─────────┐
                    │                   │
              Serializable         Non-Serializable
                    │
         ┌──────────┴──────────┐
         │                     │
   Conflict            View (only)
  Serializable        Serializable
         │
         │
    Recoverable ──────── Not Recoverable
         │
    Cascadeless
         │
      Strict
```

---

## 🧮 Testing Serializability

### Algorithm for Conflict Serializability

```
1. For each transaction, create a node
2. For each pair of conflicting operations:
   - If Ti's operation is before Tj's operation
   - Add edge Ti → Tj
3. If graph has cycle → NOT conflict serializable
4. If no cycle → Conflict serializable
   Topological order gives equivalent serial schedule
```

### Time Complexity
- Building graph: O(n²) where n = number of operations
- Cycle detection: O(V + E) using DFS

---

## 📝 Notation Quick Reference

| Symbol | Meaning |
|--------|---------|
| R(X) / r(X) | Read item X |
| W(X) / w(X) | Write item X |
| Ri(X) | Transaction i reads X |
| Wi(X) | Transaction i writes X |
| Ci | Transaction i commits |
| Ai | Transaction i aborts |

---

## ⚠️ Common GATE Traps

### Trap 1: Serial ≠ Serializable
```
Serial: Transactions run one after another
Serializable: Can be reordered to equivalent serial schedule

All serial schedules are serializable.
NOT all serializable schedules are serial!
```

### Trap 2: Precedence Graph Direction
```
Ti → Tj means Ti must come BEFORE Tj in equivalent serial schedule
If conflict: Earlier operation's transaction → Later operation's transaction
```

### Trap 3: View vs Conflict
```
Conflict Serializable → View Serializable ✓
View Serializable → Conflict Serializable ✗ (not always)
```

### Trap 4: Recoverability
```
Serializable does NOT imply recoverable!
A schedule can be conflict serializable but not recoverable.
```

### Trap 5: Commit Order in Recovery
```
Recoverable: Ti commits before Tj commits (if Tj reads Ti's data)
Cascadeless: Ti commits before Tj reads Ti's data
Strict: Ti commits/aborts before Tj reads OR writes Ti's data
```

---

## 🧪 Practice Problems

### Q1: Check Conflict Serializability
```
Schedule: R1(A), R2(B), W1(B), W2(A)

Conflicts:
- R2(B) before W1(B): T2 → T1
- R1(A) before W2(A): T1 → T2

Precedence Graph: T1 ↔ T2 (cycle!)
Answer: NOT Conflict Serializable
```

### Q2: Check Recoverability
```
Schedule: R1(A), W1(A), R2(A), W2(B), C2, C1

T2 reads A written by T1
C2 happens before C1

Answer: NOT Recoverable (T2 commits before T1)
```

### Q3: Find Equivalent Serial Schedule
```
Schedule: R1(X), R2(Y), W2(X), W1(Y)

Conflicts:
- R1(X) before W2(X): T1 → T2
- R2(Y) before W1(Y): T2 → T1

Cycle: T1 → T2 → T1
Answer: No equivalent serial schedule (NOT conflict serializable)
```

### Q4: Cascadeless Check
```
Schedule: W1(A), C1, R2(A), W2(B), C2

T2 reads A after T1 commits
Answer: Cascadeless ✓
```

---

## 📐 Counting Serial Schedules

### Formula
For n transactions: **n!** serial schedules

```
3 transactions: 3! = 6 serial schedules
T1;T2;T3, T1;T3;T2, T2;T1;T3, T2;T3;T1, T3;T1;T2, T3;T2;T1
```

### Serializable Schedules
More than n! (includes non-serial but equivalent schedules)

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **Conflict** | Different T, Same item, ≥1 Write |
| **Precedence Graph** | Cycle → Not CS, No cycle → CS |
| **CS ⊂ VS** | Conflict ⊂ View Serializable |
| **Strict ⊂ CL ⊂ R** | Strict ⊂ Cascadeless ⊂ Recoverable |

---

## 🎓 Quick Revision Points

1. ✅ ACID = Atomicity, Consistency, Isolation, Durability
2. ✅ Conflict: Different T + Same item + One is Write
3. ✅ Precedence graph cycle → NOT conflict serializable
4. ✅ Conflict Serializable ⊂ View Serializable
5. ✅ Strict ⊂ Cascadeless ⊂ Recoverable
6. ✅ Recoverable: Read's source commits first
7. ✅ n transactions → n! serial schedules

---

*Previous: [Normalization & FD](./06-Normalization-and-FD.md) | Next: [Concurrency Control](./08-Concurrency-Control.md)*
