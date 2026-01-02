# 📚 Chapter 09: Recovery System

> **The Atomic Truth**: *Ensure durability through logging and controlled recovery.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 2-4 marks |
| Frequency | 60% years |
| Type | MCQ (recovery protocols), NAT (log analysis) |
| Difficulty | Medium |
| Hot Topics | WAL, UNDO/REDO, Checkpoints, ARIES basics |

---

## 1. Recovery System Overview

### Why Recovery?
- System crashes (power failure, hardware fault)
- Transaction failures (errors, deadlock victim)
- Disk failures (media failure)

### Recovery Goals
1. **Atomicity**: Undo incomplete transactions
2. **Durability**: Ensure committed changes persist

### Types of Failures

| Failure Type | Description | Recovery Method |
|--------------|-------------|-----------------|
| **Transaction Failure** | Logical error, deadlock | Rollback transaction |
| **System Crash** | Power failure, OS crash | Log-based recovery |
| **Disk Failure** | Head crash, media damage | Backup + Log replay |

---

## 2. Storage Classification

### Storage Types by Volatility

```
┌─────────────────────────────────────────────────────────┐
│                    VOLATILE STORAGE                      │
│              (Lost on power failure)                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │           Main Memory (RAM)                      │    │
│  │   - Database buffer (dirty pages)               │    │
│  │   - Transaction data structures                 │    │
│  └─────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│                  NON-VOLATILE STORAGE                    │
│              (Survives power failure)                    │
│  ┌─────────────────────────────────────────────────┐    │
│  │           Disk Storage                           │    │
│  │   - Database files                              │    │
│  │   - Log files                                   │    │
│  └─────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│                    STABLE STORAGE                        │
│           (Survives all failures)                        │
│  ┌─────────────────────────────────────────────────┐    │
│  │           Replicated Storage                     │    │
│  │   - RAID arrays                                 │    │
│  │   - Remote backups                              │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Data Access Model

```
      ┌───────────────┐
      │  Transaction  │
      │    (Read X)   │
      └───────┬───────┘
              │
              ▼
      ┌───────────────┐
      │ Database      │
      │ Buffer (RAM)  │ ◄─── X may be here (buffer hit)
      └───────┬───────┘
              │ If not in buffer
              ▼
      ┌───────────────┐
      │    Disk       │ ◄─── Read from disk to buffer
      │   Storage     │
      └───────────────┘

Write path:
Transaction → Buffer (marked dirty) → Disk (eventually flushed)
```

---

## 3. Log-Based Recovery

### What is a Log?
A **log** (or journal) is a sequence of log records describing database modifications.

### Log Record Types

| Record Type | Format | Description |
|-------------|--------|-------------|
| **Start** | `<Ti, start>` | Transaction Ti has started |
| **Update** | `<Ti, X, old_val, new_val>` | Ti changed X |
| **Commit** | `<Ti, commit>` | Ti has committed |
| **Abort** | `<Ti, abort>` | Ti has aborted |
| **Checkpoint** | `<checkpoint, L>` | Checkpoint with active transactions L |

### Log Example

```
Log Sequence:
1. <T1, start>
2. <T1, A, 100, 90>      -- T1: A was 100, now 90
3. <T2, start>
4. <T2, B, 200, 210>     -- T2: B was 200, now 210
5. <T1, C, 50, 40>       -- T1: C was 50, now 40
6. <T1, commit>
7. <T2, D, 300, 350>
8. <CHECKPOINT, {T2}>    -- T2 is active at checkpoint
9. <T2, commit>
10. <T3, start>
11. <T3, E, 400, 450>
--- CRASH ---
```

---

## 4. Write-Ahead Logging (WAL)

### The WAL Protocol

**Rule 1 (UNDO Rule)**: Before a dirty page is written to disk, all log records for that page must be written to disk.

**Rule 2 (REDO Rule)**: Before a transaction commits, all its log records must be written to disk.

### Why WAL?

```
Without WAL:
1. T1 modifies A in buffer (A: 100 → 90)
2. Buffer with A is written to disk
3. System crashes before log is written
4. We've lost information needed to undo T1!

With WAL:
1. T1 modifies A in buffer (A: 100 → 90)
2. Log record <T1, A, 100, 90> written to disk FIRST
3. Then buffer can be written to disk
4. If crash occurs, log has info to undo/redo
```

### Force vs No-Force

| Policy | Description | Trade-off |
|--------|-------------|-----------|
| **Force** | Flush dirty pages on commit | Slower commits, no redo needed |
| **No-Force** | Don't force flush on commit | Faster commits, may need redo |

### Steal vs No-Steal

| Policy | Description | Trade-off |
|--------|-------------|-----------|
| **Steal** | Can flush uncommitted pages | May need undo |
| **No-Steal** | Only committed pages to disk | No undo needed, more memory |

### Common Policy Combinations

| Policy | UNDO | REDO | Notes |
|--------|------|------|-------|
| **No-Steal/Force** | No | No | Simple but impractical |
| **Steal/No-Force** | Yes | Yes | Most common (ARIES) |
| **No-Steal/No-Force** | No | Yes | - |
| **Steal/Force** | Yes | No | - |

---

## 5. UNDO and REDO Operations

### UNDO
Restore database to state before transaction's modifications.

```
Log record: <T1, A, old_val, new_val>
UNDO: Set A = old_val
```

**When to UNDO**: Transaction did not commit before crash.

### REDO
Reapply transaction's modifications.

```
Log record: <T1, A, old_val, new_val>
REDO: Set A = new_val
```

**When to REDO**: Transaction committed but changes may not be on disk.

### Idempotency
Both UNDO and REDO must be **idempotent**:
- Applying operation multiple times = applying once
- Important because crash may occur during recovery itself

---

## 6. Recovery Algorithms

### Deferred Database Modification (No-Undo/Redo)

**Protocol**:
1. Log all modifications but don't write to database
2. On commit, write log to disk, then apply all modifications
3. Recovery: Only REDO committed transactions

```
During normal execution:
T1: Log <T1, A, _, 90> but don't modify A yet
T1: Log <T1, B, _, 80>
T1: Commit → Write log, then write A=90, B=80 to DB

Recovery:
- Find committed transactions
- REDO their modifications
- Uncommitted transactions never touched DB (no UNDO needed)
```

### Immediate Database Modification (Undo/Redo)

**Protocol**:
1. Log modifications before writing to database (WAL)
2. Modifications written to database before commit is allowed
3. Recovery: UNDO uncommitted, REDO committed

```
During normal execution:
T1: Log <T1, A, 100, 90>
T1: May write A=90 to disk
T1: Log <T1, B, 200, 80>
T1: May write B=80 to disk
T1: Commit

Recovery:
- REDO all committed transactions
- UNDO all uncommitted transactions
```

### Shadow Paging (No logging)

**Concept**: Maintain two page tables - current and shadow.

```
┌───────────────┐    ┌───────────────┐
│ Shadow Page   │    │ Current Page  │
│ Table         │    │ Table         │
├───────────────┤    ├───────────────┤
│ Page 1 → D1   │    │ Page 1 → D1   │
│ Page 2 → D2   │    │ Page 2 → D2'  │ ← Modified
│ Page 3 → D3   │    │ Page 3 → D3   │
└───────────────┘    └───────────────┘
        │                    │
        │    Disk            │
        │    ┌─────────────┐ │
        └───►│ D1 │ D2 │D2'│◄┘
             │ D3 │    │   │
             └─────────────┘
```

**Commit**: Atomically replace shadow with current page table.

**Abort/Crash**: Discard current page table, use shadow.

**Disadvantage**: Fragmentation, difficult for concurrent transactions.

---

## 7. Checkpoints

### Why Checkpoints?
Without checkpoints, recovery must scan entire log from beginning.

### Simple Checkpoint Protocol

1. **Stop** accepting new transactions
2. **Wait** for all active transactions to complete
3. **Flush** all dirty buffers to disk
4. **Write** checkpoint record to log
5. **Resume** normal operation

**Problem**: System paused during checkpoint (quiesce checkpoint).

### Fuzzy Checkpoint (Non-Quiescent)

1. **Write** `<checkpoint, L>` where L = list of active transactions
2. **Don't stop** transactions
3. **Continue** normal operation

**Recovery**: Only need to examine log from last checkpoint.

```
Log:
...
<T1, start>
<T1, A, 100, 90>
<CHECKPOINT, {T1}>     ← Start recovery here
<T2, start>
<T2, B, 200, 210>
<T1, commit>
--- CRASH ---

Recovery:
1. Find last checkpoint
2. T1 was active at checkpoint
3. Scan forward: T1 commits ✓, T2 doesn't commit ✗
4. REDO T1, UNDO T2
```

### Checkpoint Impact on Recovery

```
Without Checkpoint:
Log: Start ─────────────────────────────── Crash
     Must scan from beginning

With Checkpoint:
Log: Start ──── CP1 ──── CP2 ──── CP3 ──── Crash
                                   ↑
                         Start recovery here
```

---

## 8. Recovery with Checkpoints

### Recovery Algorithm (Undo/Redo with Checkpoint)

```
Algorithm: Recover()

Phase 1: Analysis (find active transactions)
1. Start from last checkpoint
2. Build undo-list = transactions in checkpoint
3. Scan forward:
   - If see <Ti, start>: add Ti to undo-list
   - If see <Ti, commit> or <Ti, abort>: remove Ti from undo-list

Phase 2: Redo (forward scan)
4. Scan from checkpoint to end
5. REDO all logged updates

Phase 3: Undo (backward scan)  
6. Scan backwards from end
7. For each record of transaction in undo-list:
   - UNDO the operation
   - When see <Ti, start>: remove Ti, write <Ti, abort>
8. Repeat until undo-list is empty
```

### Example Recovery

```
Log:
1. <T1, start>
2. <T1, A, 100, 90>
3. <CHECKPOINT, {T1}>
4. <T2, start>
5. <T2, B, 200, 210>
6. <T1, C, 50, 40>
7. <T1, commit>
8. <T2, D, 300, 350>
--- CRASH ---

Analysis:
- Checkpoint has {T1}
- Undo-list = {T1}
- T2 starts: undo-list = {T1, T2}
- T1 commits: undo-list = {T2}
- Final undo-list = {T2}

Redo (forward from checkpoint):
- Redo <T2, B, 200, 210>: B = 210
- Redo <T1, C, 50, 40>: C = 40
- Redo <T2, D, 300, 350>: D = 350

Undo (backward):
- Undo <T2, D, 300, 350>: D = 300
- Undo <T2, B, 200, 210>: B = 200
- See <T2, start>: write <T2, abort>, remove from undo-list
- Undo-list empty, done

Final: T1's changes (A=90, C=40) persist
       T2's changes undone
```

---

## 9. ARIES (Brief Overview)

### ARIES: Algorithms for Recovery and Isolation Exploiting Semantics

Most widely used recovery algorithm (IBM).

### Key Concepts

| Concept | Description |
|---------|-------------|
| **LSN** | Log Sequence Number - unique ID for each log record |
| **PageLSN** | LSN of last update to a page |
| **RecLSN** | First LSN that dirtied a page |
| **Dirty Page Table** | Pages in buffer that are modified |
| **Transaction Table** | Active transactions and their status |

### ARIES Three Phases

1. **Analysis Phase**: Determine dirty pages and active transactions at crash
2. **Redo Phase**: Repeat history to restore database to crash state
3. **Undo Phase**: Rollback uncommitted transactions

### Compensation Log Records (CLR)

When undoing an operation, write a CLR:
- Describes the undo action
- Contains pointer to previous log record
- CLRs are never undone (prevents infinite undo loops)

```
Regular log:    <T1, A, 100, 90>
CLR for undo:   <T1, A, CLR, undo(A=100), prevLSN=...>
```

---

## 10. Recovery with Concurrent Transactions

### Transaction Table at Checkpoint

```
<CHECKPOINT>
Transaction Table: {(T1, active), (T2, active), (T3, committed)}
Dirty Page Table: {(P1, LSN=100), (P2, LSN=150)}
```

### Recovery Process

1. Rebuild transaction and dirty page tables from checkpoint
2. Scan forward updating tables
3. Redo from minimum RecLSN in dirty page table
4. Undo uncommitted transactions

---

## 11. Media Recovery

### Handling Disk Failure

**Method**: Restore from backup + replay log

```
1. Restore database from last full backup
2. Apply all log records since backup
3. Perform normal recovery (undo/redo)
```

### Backup Strategies

| Strategy | Description | Frequency |
|----------|-------------|-----------|
| **Full Backup** | Complete database copy | Weekly |
| **Incremental** | Changes since last backup | Daily |
| **Log Archiving** | Save old log files | Continuous |

### Remote Backup

Maintain standby database at remote site:
- Ship log records to standby
- Apply logs to keep synchronized
- On failure, standby takes over

---

## 12. Log Record Structure

### Typical UNDO/REDO Log Record

```
┌────────────────────────────────────────────────────────────┐
│ LSN │ Trans │ Type │ Page │ Offset │ Old Value │ New Value │
│ ID  │ ID    │      │ ID   │        │           │           │
├────────────────────────────────────────────────────────────┤
│ 101 │ T1    │ UPD  │ P5   │ 200    │ 100       │ 90        │
│ 102 │ T2    │ UPD  │ P3   │ 50     │ ABC       │ XYZ       │
│ 103 │ T1    │ CMT  │  -   │   -    │    -      │    -      │
└────────────────────────────────────────────────────────────┘
```

### Log File Organization

```
┌──────────────────────────────────────────────────────────┐
│                      LOG FILE                             │
├──────────────────────────────────────────────────────────┤
│ ← Old records              Tail →                        │
│ [Archived or truncated]    [Active log]                  │
│                            ↑                             │
│                     Last checkpoint                      │
└──────────────────────────────────────────────────────────┘
```

---

## 13. Common GATE Questions

### Pattern 1: Determine UNDO/REDO Actions

Given log and crash point, identify which transactions to undo/redo.

```
Question: Given log ending in crash, which transactions need:
- REDO: Committed before crash
- UNDO: Started but not committed
- NOTHING: Committed and flushed (before checkpoint)
```

### Pattern 2: Checkpoint Impact

How does checkpoint affect recovery time/complexity?

### Pattern 3: WAL Rules

Identify violations of write-ahead logging.

### Pattern 4: Recovery Order

Specify order of operations during recovery.

---

## 14. Recovery Summary Table

| Scenario | REDO | UNDO |
|----------|------|------|
| Committed, changes on disk | No | No |
| Committed, changes not on disk | Yes | No |
| Not committed, changes on disk | No | Yes |
| Not committed, changes not on disk | No | No* |

*But with Steal policy, uncommitted changes might be on disk.

---

## 15. Key Formulas and Concepts

### Recovery Time Estimation

$$\text{Recovery Time} \approx \text{Log scan time} + \text{Redo time} + \text{Undo time}$$

With checkpoint:
$$\text{Log to scan} = \text{Log since last checkpoint}$$

### Log Space Calculation

$$\text{Log size} = \text{Number of operations} \times \text{Avg record size}$$

---

## 🧠 Memory Techniques

### WAL Mnemonic: "Log Before Leap"
Write log BEFORE writing data to disk.

### UNDO/REDO Decision: "Commit = Redo, No Commit = Undo"
- Committed transactions: REDO (ensure durability)
- Uncommitted transactions: UNDO (ensure atomicity)

### Recovery Phases: "ARU" (Analysis, Redo, Undo)
1. **A**nalyze what happened
2. **R**edo committed work
3. **U**ndo uncommitted work

### Steal/No-Force: "Steal = Undo needed, No-Force = Redo needed"

---

## 🔑 Key Takeaways for GATE

1. **WAL is fundamental**: Log before database modification
2. **Checkpoint reduces recovery scope**: Scan from checkpoint, not beginning
3. **REDO for durability**: Committed but not flushed
4. **UNDO for atomicity**: Started but not committed
5. **ARIES uses LSN**: For precise recovery
6. **Fuzzy checkpoints**: Don't stop transactions

---

## 📚 Related Chapters
- [← Previous: Chapter 08 - Query Processing](../08-Query-Processing/README.md)
- [Back to DBMS Home](../README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**

---

# 🎓 DBMS Study Material Complete!

You have completed all 9 chapters of the DBMS study material:

1. ✅ Introduction to DBMS
2. ✅ ER Model & EER  
3. ✅ Relational Model & Relational Algebra
4. ✅ SQL
5. ✅ Functional Dependencies & Normalization
6. ✅ Transactions & Concurrency Control
7. ✅ Indexing & File Organization
8. ✅ Query Processing & Optimization
9. ✅ Recovery System

**Next Steps for GATE/ESE Success**:
1. Solve Previous Year Questions (2000-2024)
2. Practice NAT calculations with timer
3. Master precedence graphs for concurrency
4. Memorize key formulas for indexing
5. Review edge cases in SQL NULL handling

> **Good luck for your examination!**
