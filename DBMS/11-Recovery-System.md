# Chapter 11: Recovery System

---

## 🎯 Why Recovery?

**Recovery** ensures database returns to a consistent state after failure.

### Failure Types

| Type | Cause | Recovery Method |
|------|-------|-----------------|
| **Transaction Failure** | Logic error, deadlock, user abort | Undo transaction |
| **System Failure** | Power outage, OS crash, software bug | Redo + Undo from logs |
| **Disk Failure** | Head crash, bad sectors | Restore from backup |
| **Media Failure** | Fire, flood, theft | Offsite backup |

### 🎭 Analogy
> Recovery = **Auto-save in Word**
> - Crash? Recover to last saved state
> - Log = Auto-save history

---

## 📊 ACID and Recovery

| Property | Recovery Responsibility |
|----------|------------------------|
| **Atomicity** | Undo incomplete transactions |
| **Durability** | Redo committed transactions |
| **Consistency** | Restore valid state |
| **Isolation** | Handled by concurrency control |

---

## 📝 Log-Based Recovery

### What is a Log?

A **log** is a sequential record of all database modifications.

```
Log Structure:
┌───────────────────────────────────────────────────────┐
│ <T1, START>                                           │
│ <T1, A, old_val, new_val>                             │
│ <T2, START>                                           │
│ <T1, B, old_val, new_val>                             │
│ <T1, COMMIT>                                          │
│ <T2, C, old_val, new_val>                             │
│ <T2, ABORT>                                           │
└───────────────────────────────────────────────────────┘
```

### Log Record Types

| Record | Format | Meaning |
|--------|--------|---------|
| Start | `<Ti, START>` | Transaction Ti began |
| Update | `<Ti, X, V_old, V_new>` | Ti changed X from V_old to V_new |
| Commit | `<Ti, COMMIT>` | Ti completed successfully |
| Abort | `<Ti, ABORT>` | Ti was rolled back |
| Checkpoint | `<CHECKPOINT, L>` | Checkpoint with active transactions L |

---

## 🔄 Write-Ahead Logging (WAL)

### The Protocol
> **Before** any data modification is written to disk, the **log record** must be written to stable storage.

### Two Rules

#### 1. Undo Rule
```
Log record with OLD value must be written before 
data page is written to disk.

Why: If crash before commit, need old value to undo
```

#### 2. Redo Rule (Commit Rule)
```
ALL log records must be written to stable storage 
before transaction commits.

Why: If crash after commit, need new values to redo
```

### 🧠 Memory Trick
> **"Log before data"** = WAL principle

---

## 📊 Recovery Techniques

### 1. Deferred Database Modification
- Don't write to disk until commit
- Only REDO needed (no UNDO)
- Also called **No-Steal, Force**

```
Log:                      Database:
<T1, START>               (no changes yet)
<T1, A, -, 100>           (no changes yet)
<T1, B, -, 200>           (no changes yet)
<T1, COMMIT>              Now write A=100, B=200
```

**Recovery**: Only REDO committed transactions

### 2. Immediate Database Modification
- Write to disk anytime (before or after commit)
- Both REDO and UNDO needed
- Also called **Steal, No-Force**

```
Log:                      Database:
<T1, START>               
<T1, A, 50, 100>          A = 100 (may be written)
<T1, B, 150, 200>         B = 200 (may be written)
<T1, COMMIT>              
```

**Recovery**: REDO committed, UNDO uncommitted

---

## 🔀 Steal vs No-Steal, Force vs No-Force

### Definitions

| Policy | Meaning |
|--------|---------|
| **Steal** | Uncommitted data CAN be written to disk |
| **No-Steal** | Uncommitted data CANNOT be written to disk |
| **Force** | Committed data MUST be written to disk at commit |
| **No-Force** | Committed data can remain in buffer after commit |

### Combinations

| Policy | UNDO Needed | REDO Needed | Used In |
|--------|-------------|-------------|---------|
| No-Steal + Force | No | No | Simple, poor performance |
| Steal + Force | Yes | No | |
| No-Steal + No-Force | No | Yes | Shadow paging |
| **Steal + No-Force** | Yes | Yes | ARIES (most practical) |

### 🎯 Most Common
> **Steal + No-Force** requires both UNDO and REDO but offers best performance.

---

## ✅ Checkpoints

### Purpose
- Reduce recovery time
- Don't need to scan entire log
- Establish known consistent state

### Checkpoint Process

1. Suspend all transactions temporarily
2. Force all modified buffers to disk
3. Write checkpoint record to log
4. Resume transactions

### Checkpoint Record
```
<CHECKPOINT, {T1, T2, T3}>

Lists all active (uncommitted) transactions at checkpoint time
```

### Recovery with Checkpoint

```
                  Checkpoint
                      │
    T1 ─────────────────────────────────── (committed before checkpoint)
    T2 ────────────────────────────────────────────── (committed after)
    T3 ──────────────────────────────────────────X (active at crash)
    T4           ─────────────────────────────────── (started after)
                                               │
                                             Crash

Recovery:
- T1: Already on disk (no action)
- T2: REDO (committed but may not be on disk)
- T3: UNDO (not committed)
- T4: REDO if committed, else UNDO
```

---

## 🔄 Recovery Algorithm (UNDO/REDO)

### Phase 1: Analysis (Scan Forward)
```
1. Find last checkpoint
2. Identify:
   - Committed transactions (REDO list)
   - Uncommitted transactions (UNDO list)
```

### Phase 2: REDO (Scan Forward)
```
For each log record of committed transaction:
    If update record:
        Redo the operation (apply new value)
```

### Phase 3: UNDO (Scan Backward)
```
For each log record of uncommitted transaction (reverse order):
    If update record:
        Undo the operation (apply old value)
```

### Order Matters!
```
REDO: Forward order (oldest first)
UNDO: Backward order (newest first)
```

---

## 🔄 ARIES Recovery Algorithm

### Advanced Recovery Technique

**ARIES** = **A**lgorithms for **R**ecovery and **I**solation **E**xploiting **S**emantics

### Three Phases

```
1. ANALYSIS PHASE
   └── Scan log to determine:
       - Dirty pages (might need redo)
       - Active transactions (need undo)

2. REDO PHASE
   └── Repeat history
       - Redo ALL actions (even aborted!)
       - Brings database to crash state

3. UNDO PHASE
   └── Undo incomplete transactions
       - Scan backward
       - Write CLRs (Compensation Log Records)
```

### Key Concepts in ARIES

| Concept | Description |
|---------|-------------|
| **LSN** (Log Sequence Number) | Unique ID for each log record |
| **PageLSN** | LSN of last update to a page |
| **RecLSN** | LSN of first update to page since written to disk |
| **CLR** | Compensation Log Record (for undone operations) |
| **Dirty Page Table** | Pages modified but not written to disk |
| **Transaction Table** | Active transactions and their last LSN |

### ARIES Properties
1. **Steal + No-Force** policy
2. **Repeating history** during redo
3. **Logical undo** possible
4. **Compensation Log Records (CLRs)** prevent repeated undo on re-crash

---

## 📊 Log Sequence Number (LSN)

### Purpose
- Unique identifier for each log record
- Monotonically increasing
- Used to track recovery progress

### Usage in Pages

```
Page Header:
┌─────────────────────────────────────┐
│ PageLSN: 12345                      │ ← Last log record that modified this page
│ ...data...                          │
└─────────────────────────────────────┘

During REDO:
If Log_Record.LSN ≤ PageLSN:
    Skip (already applied)
Else:
    Apply the update
```

---

## 💾 Shadow Paging

### Alternative to Logging

### Concept
Maintain two page tables:
- **Current Page Table**: Points to current pages
- **Shadow Page Table**: Points to old pages (stable)

```
           Shadow PT             Current PT
           ┌───────┐             ┌───────┐
        0  │   ●───┼─────────►   │   ●───┼──► Page 0'
           ├───────┤             ├───────┤
        1  │   ●───┼──► Page 1   │   ●───┼──► Page 1
           ├───────┤             ├───────┤
        2  │   ●───┼──► Page 2   │   ●───┼──► Page 2'
           └───────┘             └───────┘
                                 (Modified pages)
```

### On Commit
1. Force modified pages to disk
2. Copy current page table to shadow
3. Write shadow PT to known location

### On Abort/Crash
- Discard current page table
- Use shadow page table

### Advantages
- No UNDO needed
- Simple recovery

### Disadvantages
- Fragmentation
- Garbage collection needed
- Hard to extend to concurrent transactions

---

## 🔐 Remote Backup

### For Disaster Recovery

```
┌──────────────────┐                    ┌──────────────────┐
│   Primary Site   │───── Network ─────►│   Backup Site    │
│    (Active)      │      Log Ship      │    (Standby)     │
└──────────────────┘                    └──────────────────┘
```

### Hot Standby
- Backup continuously applies logs
- Can take over immediately

### Warm Standby
- Backup receives logs
- Needs time to apply on failover

### Cold Standby
- Periodic backup copy
- Significant data loss on failure

---

## 📐 Important Concepts Summary

### Compensation Log Records (CLR)
```
When undoing T1's update:
Write: <T1_CLR, X, old_value, next_undo_LSN>

CLR is NEVER undone (redo-only)
Prevents infinite undo loop on repeated crashes
```

### Fuzzy Checkpoint
```
Don't block all transactions
Record:
- Active transactions
- Dirty pages
Continue running during checkpoint I/O
```

### Nested Transaction Recovery
```
Sub-transaction abort: Undo sub-transaction only
Parent abort: Undo all nested transactions
```

---

## ⚠️ Common GATE Traps

### Trap 1: REDO vs UNDO Order
```
REDO: Forward (oldest to newest)
UNDO: Backward (newest to oldest)
```

### Trap 2: Checkpoint Scope
```
Transactions committed BEFORE checkpoint: Already on disk
Transactions active AT checkpoint: Need recovery
Transactions started AFTER checkpoint: Need recovery
```

### Trap 3: WAL Rules
```
UNDO rule: Log with old value before page to disk
REDO rule: All logs before commit

Not: "All operations logged before commit"
```

### Trap 4: Shadow Paging
```
No UNDO needed (use shadow)
No REDO needed (force at commit)
BUT: Hard with concurrent transactions
```

### Trap 5: Steal + No-Force
```
Steal: UNDO needed (uncommitted data may be on disk)
No-Force: REDO needed (committed data may not be on disk)
```

---

## 🧪 Practice Problems

### Q1: Identify Recovery Actions
```
Log:
<T1, START>
<T1, A, 100, 200>
<T2, START>
<T2, B, 50, 75>
<CHECKPOINT, {T1, T2}>
<T1, COMMIT>
<T3, START>
<T3, C, 30, 60>
CRASH

Analysis:
- T1: REDO (committed after checkpoint)
- T2: UNDO (never committed)
- T3: UNDO (never committed)
```

### Q2: WAL Scenario
```
T1 modifies A from 100 to 200
Which must happen before A=200 is written to disk?

Answer: Log record <T1, A, 100, 200> must be on stable storage
(UNDO rule of WAL)
```

### Q3: ARIES Phase Order
```
Correct order: Analysis → REDO → UNDO
Not: REDO → UNDO → Analysis
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **WAL** | Log before data, enables undo/redo |
| **UNDO** | Restore old values for uncommitted |
| **REDO** | Apply new values for committed |
| **Checkpoint** | Reduces recovery scope |
| **Steal/Force** | Determines UNDO/REDO need |
| **ARIES** | Analysis → REDO → UNDO |
| **Shadow Paging** | No logging, uses page table copies |

---

## 🎓 Quick Revision Points

1. ✅ WAL: Log record before data to disk
2. ✅ REDO = committed but maybe not on disk
3. ✅ UNDO = uncommitted but maybe on disk
4. ✅ Checkpoint reduces recovery scope
5. ✅ Steal + No-Force: Both UNDO and REDO needed
6. ✅ ARIES: Analysis → REDO → UNDO
7. ✅ CLR prevents repeated undo

---

*Previous: [Query Processing & Optimization](./10-Query-Processing-and-Optimization.md) | Next: [Distributed Databases](./12-Distributed-Databases.md)*
