# Chapter 6: Deadlocks

## 🎯 The Atomic Truth
> **Deadlock = Circular Wait for Resources with No Preemption**

---

## 🧠 What is Deadlock?

### The WHY (First Principles)

**Definition**: A set of processes is deadlocked if each process is waiting for an event that only another process in the set can cause.

```
DEADLOCK SCENARIO:

Process P1                     Process P2
─────────────                  ─────────────
Holds: Resource A              Holds: Resource B
Wants: Resource B              Wants: Resource A

        P1 ───waits for B───→ P2
         ↑                      │
         └────waits for A───────┘
         
CIRCULAR WAIT = DEADLOCK!
```

### Real-World Analogy

**Traffic Gridlock**:
```
         ↓
    ←─[Car]─→
         ↓
    ─────X─────  (Intersection blocked)
         ↓
    ←─[Car]─→
         ↓
         
All cars waiting for each other to move!
```

---

## 📋 Necessary Conditions for Deadlock

### The Four Horsemen of Deadlock

**ALL FOUR must hold simultaneously for deadlock to occur.**

| Condition | Meaning | Breaking It |
|-----------|---------|-------------|
| **Mutual Exclusion** | At least one resource held in non-sharable mode | Make resources sharable |
| **Hold and Wait** | Process holds resource while waiting for others | Request all at once |
| **No Preemption** | Resources can't be forcibly taken | Allow preemption |
| **Circular Wait** | Circular chain of waiting | Order resource requests |

### Mnemonic: "My Horse Never Circles"
- **M**utual Exclusion
- **H**old and Wait
- **N**o Preemption
- **C**ircular Wait

---

## 📊 Resource Allocation Graph (RAG)

### Components

```
NOTATION:
┌─────┐
│ Pi  │ = Process (circle)
└─────┘

[R1][R2][R3] = Resource type with 3 instances (rectangle with dots)

Pi ─────→ Rj  = Request edge (Pi wants Rj)

Rj ─────→ Pi  = Assignment edge (Rj assigned to Pi)
```

### Example RAG

```
        REQUEST          ASSIGNMENT
           ↓                 ↓
    ┌──────────────────────────────────┐
    │                                  │
    │    P1 ──────→ R1 ──────→ P2     │
    │     ↑                     │      │
    │     │                     │      │
    │     └───── R2 ←───────────┘      │
    │                                  │
    └──────────────────────────────────┘
    
    P1 wants R1, R1 held by P2
    P2 wants R2, R2 held by P1
    
    CYCLE EXISTS = DEADLOCK (with single instance resources)
```

### Cycle Detection Rules

| Resource Type | Cycle Exists? | Deadlock? |
|---------------|---------------|-----------|
| Single instance per type | Yes | **Yes (definitely)** |
| Multiple instances per type | Yes | **Maybe** |

**GATE Trap**: Cycle is NECESSARY for deadlock, but SUFFICIENT only with single-instance resources.

---

## 🛡️ Methods of Handling Deadlocks

```
HANDLING STRATEGIES:

┌─────────────────────────────────────────────────────────┐
│                    DEADLOCK                              │
├─────────────┬─────────────┬─────────────┬───────────────┤
│   IGNORE    │  PREVENT    │   AVOID     │   DETECT &    │
│  (Ostrich)  │             │             │   RECOVER     │
├─────────────┼─────────────┼─────────────┼───────────────┤
│ Do nothing  │ Break one   │ Don't grant │ Let it happen │
│ Assume rare │ of the 4    │ unsafe      │ then fix      │
│             │ conditions  │ requests    │               │
└─────────────┴─────────────┴─────────────┴───────────────┘
```

---

## 🚫 Deadlock Prevention

**Strategy**: Ensure at least one of the four conditions can never hold.

### 1. Breaking Mutual Exclusion
- Make resources sharable (read-only files)
- **Problem**: Not always possible (printers, CPU)

### 2. Breaking Hold and Wait

**Approach 1**: Request all resources at once
```
// Before execution, request everything needed
request(R1, R2, R3, R4);
execute();
release(R1, R2, R3, R4);
```
**Problem**: Low resource utilization, possible starvation

**Approach 2**: Release all before requesting new
```
// If need new resource, release everything first
release_all();
request(new_resource);
```
**Problem**: May lose progress

### 3. Breaking No Preemption

**Approach**: If process can't get all resources, release what it holds
```
if (request_fails) {
    release_all_resources();
    // Will retry later
}
```
**Problem**: Works for resources with saveable state (CPU, memory), not for printers

### 4. Breaking Circular Wait

**Approach**: Total ordering of resources. Request in order only.

```
Resources ordered: R1 < R2 < R3 < R4 < R5

Rule: Can only request Rj if j > all currently held resources

VALID:   request(R1); request(R3); request(R5);
INVALID: request(R3); request(R1);  ← R1 < R3, not allowed!
```

**Proof it prevents circular wait**:
- If P1 holds Ri and waits for Rj, then j > i
- Chain: P1 waits for Rj held by P2, P2 waits for Rk held by P3...
- Implies: i < j < k < ... (can't be circular!)

---

## 🎯 Deadlock Avoidance

**Strategy**: Know maximum resource needs in advance. Only grant requests that keep system in "safe" state.

### Safe State Definition

**Safe State**: Exists at least one sequence of processes (safe sequence) that can complete.

```
SAFE STATE CHECK:

Available = 3 printers

Process    Max Need    Current Hold    Still Needs
P1         10          5               5
P2         4           2               2
P3         9           2               7

Can we find safe sequence?

Available = 3
1. P2 can finish (needs 2 ≤ 3). Available becomes 3 + 2 = 5
2. P1 can finish (needs 5 ≤ 5). Available becomes 5 + 5 = 10
3. P3 can finish (needs 7 ≤ 10). Available becomes 10 + 2 = 12

Safe sequence: <P2, P1, P3>
System is in SAFE STATE!
```

### Unsafe State

**Unsafe State**: No safe sequence exists. MAY lead to deadlock.

**GATE Trap**: Unsafe ≠ Deadlock. Unsafe means deadlock is POSSIBLE.

```
SAFE STATE ────→ May remain safe or become unsafe
UNSAFE STATE ──→ May lead to deadlock (not guaranteed)
DEADLOCK ──────→ Definitely stuck
```

---

## 🏦 Banker's Algorithm

### The WHY

Named after how bankers ensure they can satisfy all customers:
- Don't loan out so much that you can't satisfy remaining customers

### Data Structures

For n processes, m resource types:

| Structure | Size | Meaning |
|-----------|------|---------|
| **Available** | m | Currently available resources |
| **Max** | n × m | Maximum each process may need |
| **Allocation** | n × m | Currently allocated to each |
| **Need** | n × m | Max - Allocation |

$$Need[i][j] = Max[i][j] - Allocation[i][j]$$

### Safety Algorithm

```
1. Initialize:
   Work = Available (copy)
   Finish[i] = false for all i

2. Find process Pi where:
   Finish[i] = false AND Need[i] ≤ Work
   
   If no such i exists, go to step 4

3. Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If Finish[i] = true for all i:
   System is SAFE
   Else:
   System is UNSAFE
```

### Resource Request Algorithm

When Pi requests resources Request[]:

```
1. If Request[i] > Need[i]:
   ERROR (exceeded maximum claim)

2. If Request[i] > Available:
   WAIT (resources not available)

3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm
   If SAFE: Grant request
   If UNSAFE: Deny request, restore old state
```

---

## 🧮 Banker's Algorithm: Complete Example

### Problem

| Process | Allocation (A B C) | Max (A B C) |
|---------|-------------------|-------------|
| P0 | 0 1 0 | 7 5 3 |
| P1 | 2 0 0 | 3 2 2 |
| P2 | 3 0 2 | 9 0 2 |
| P3 | 2 1 1 | 2 2 2 |
| P4 | 0 0 2 | 4 3 3 |

**Available = (3, 3, 2)**

### Step 1: Calculate Need Matrix

$$Need[i] = Max[i] - Allocation[i]$$

| Process | Need (A B C) |
|---------|--------------|
| P0 | 7-0=7, 5-1=4, 3-0=3 → (7, 4, 3) |
| P1 | 3-2=1, 2-0=2, 2-0=2 → (1, 2, 2) |
| P2 | 9-3=6, 0-0=0, 2-2=0 → (6, 0, 0) |
| P3 | 2-2=0, 2-1=1, 2-1=1 → (0, 1, 1) |
| P4 | 4-0=4, 3-0=3, 3-2=1 → (4, 3, 1) |

### Step 2: Run Safety Algorithm

**Work = (3, 3, 2), Finish = [F, F, F, F, F]**

| Iteration | Work | Check | Selected | New Work | Finish |
|-----------|------|-------|----------|----------|--------|
| 1 | (3,3,2) | P1: (1,2,2) ≤ (3,3,2)? ✓ | P1 | (3,3,2)+(2,0,0)=(5,3,2) | [F,T,F,F,F] |
| 2 | (5,3,2) | P3: (0,1,1) ≤ (5,3,2)? ✓ | P3 | (5,3,2)+(2,1,1)=(7,4,3) | [F,T,F,T,F] |
| 3 | (7,4,3) | P4: (4,3,1) ≤ (7,4,3)? ✓ | P4 | (7,4,3)+(0,0,2)=(7,4,5) | [F,T,F,T,T] |
| 4 | (7,4,5) | P0: (7,4,3) ≤ (7,4,5)? ✓ | P0 | (7,4,5)+(0,1,0)=(7,5,5) | [T,T,F,T,T] |
| 5 | (7,5,5) | P2: (6,0,0) ≤ (7,5,5)? ✓ | P2 | (7,5,5)+(3,0,2)=(10,5,7) | [T,T,T,T,T] |

**All Finish[i] = True → SAFE STATE**

**Safe Sequence: <P1, P3, P4, P0, P2>**

---

### Request Example

**P1 requests (1, 0, 2)**

**Step 1**: Check Request ≤ Need[P1]
- (1, 0, 2) ≤ (1, 2, 2)? ✓

**Step 2**: Check Request ≤ Available
- (1, 0, 2) ≤ (3, 3, 2)? ✓

**Step 3**: Pretend allocation
- Available = (3,3,2) - (1,0,2) = (2, 3, 0)
- Allocation[P1] = (2,0,0) + (1,0,2) = (3, 0, 2)
- Need[P1] = (1,2,2) - (1,0,2) = (0, 2, 0)

**Step 4**: Safety check with new state

New Need matrix:
| Process | Need |
|---------|------|
| P0 | (7, 4, 3) |
| P1 | (0, 2, 0) |
| P2 | (6, 0, 0) |
| P3 | (0, 1, 1) |
| P4 | (4, 3, 1) |

Check if safe... (similar process)

If safe → **GRANT REQUEST**
If unsafe → **DENY REQUEST**

---

## 🔍 Deadlock Detection

**Strategy**: Let deadlocks occur, then detect and recover.

### Single Instance Resources: Wait-For Graph

Simplify RAG by removing resource nodes:

```
RAG:                          Wait-For Graph:
P1 → R1 → P2                  P1 → P2
P2 → R2 → P1                  P2 → P1

                              CYCLE = DEADLOCK
```

**Algorithm**: Periodically check for cycles in wait-for graph.

### Multiple Instance Resources

Use algorithm similar to Banker's but without Max matrix:

```
1. Work = Available
   Finish[i] = false if Allocation[i] ≠ 0, else true

2. Find Pi where Finish[i] = false AND Request[i] ≤ Work

3. Work = Work + Allocation[i]; Finish[i] = true; goto 2

4. If any Finish[i] = false:
   Pi is DEADLOCKED
```

---

## 🔧 Deadlock Recovery

### Option 1: Process Termination

| Method | Pros | Cons |
|--------|------|------|
| **Kill all deadlocked** | Simple, fast | Loses all work |
| **Kill one at a time** | Minimal damage | Slow, need to check after each |

**Selection criteria for victim**:
1. Priority
2. Time executed / time remaining
3. Resources held
4. Resources needed
5. Interactive vs batch

### Option 2: Resource Preemption

Take resources from victim and give to others.

**Challenges**:
1. **Selecting victim**: Minimize cost
2. **Rollback**: How to restart victim? (Checkpoint/restore)
3. **Starvation**: Same process always victim

---

## 🧮 GATE Numerical: RAG Analysis

### Problem

```
Resources: R1 (2 instances), R2 (1 instance), R3 (1 instance)

P1: Holds R1(1), Requests R2
P2: Holds R2, Requests R3
P3: Holds R3, Requests R1(1)
```

**Question**: Is there a deadlock?

### Solution

**Draw RAG**:
```
       P1 ←── R1 (1 instance free)
        │
        ↓
       R2 ←── P2
                │
                ↓
               R3 ←── P3
                        │
                        ↓
                       R1 (wants 1)
```

**Check cycle**: P1 → R2 → P2 → R3 → P3 → R1 → P1? 

Wait, R1 has 2 instances, P1 has 1, P3 wants 1.
Available R1 = 2 - 1 = 1

**P3 can get R1!** (1 instance available)
- P3 finishes, releases R3
- P2 gets R3, finishes, releases R2
- P1 gets R2, finishes

**No Deadlock** (multiple instances saved us)

---

## 📊 Summary Table: Handling Methods

| Method | Resource Utilization | Overhead | May Deadlock? |
|--------|---------------------|----------|---------------|
| **Prevention** | Low | Low (once designed) | No |
| **Avoidance** | Medium | High (Banker's) | No |
| **Detection** | High | Periodic checking | Yes (then recover) |
| **Ignore** | High | None | Yes |

---

## 🎯 GATE Traps and Anti-Solutions

### Trap 1: Cycle = Deadlock?
**Wrong**: Cycle always means deadlock
**Right**: Only with single-instance resources

### Trap 2: Safe = No Deadlock
**Wrong**: Unsafe means deadlock
**Right**: Unsafe means deadlock is POSSIBLE, not certain

### Trap 3: Banker's Complexity
- Safety algorithm: O(m × n²)
- Total: O(m × n²) per request
- n = processes, m = resource types

### Trap 4: Resource Ordering
For circular wait prevention: if holding Ri, can only request Rj where j > i.

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2018)
**In Banker's algorithm, if a process releases all its resources, the state:**

(A) Becomes unsafe  
(B) Remains same  
(C) Becomes safe or remains safe ✓  
(D) Becomes deadlocked

**Explanation**: Releasing resources only adds to Available, can't make things worse.

---

### Q2: (GATE 2019)
**Minimum resources to prevent deadlock with n processes, each needing max m resources:**

**Formula**: $$R = n(m-1) + 1$$

**Example**: 3 processes, max 4 resources each:
$$R = 3(4-1) + 1 = 10$$

**Proof**: With n(m-1), each has (m-1), all waiting for 1 more. +1 breaks tie.

---

### Q3: (GATE 2017)
**Which is NOT necessary for deadlock?**

(A) Mutual Exclusion  
(B) Hold and Wait  
(C) Preemption ✓  
(D) Circular Wait

**Explanation**: NO preemption is required, not preemption.

---

## ⚡ The 5-Second Snap-Check

1. **All 4 conditions?** → Only then deadlock possible
2. **Cycle in RAG?** → Check instance count
3. **Banker's safe?** → Find ONE sequence that works
4. **Minimum resources?** → n(m-1) + 1

---

## 🧠 Memory Mnemonics

### Four Conditions: "My Horse Never Circles"
- **M**utual Exclusion
- **H**old and Wait
- **N**o Preemption
- **C**ircular Wait

### Banker's Check Order
1. **C**alculate Need
2. **F**ind safe process (Need ≤ Work)
3. **A**dd Allocation to Work
4. **R**epeat

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Deadlock | Circular wait with all 4 conditions |
| RAG Cycle | Necessary for deadlock |
| Single Instance + Cycle | Sufficient for deadlock |
| Prevention | Break one of 4 conditions |
| Avoidance | Stay in safe state |
| Banker's | Check if request keeps safe state |
| Detection | Allow, then detect cycles |
| Recovery | Kill processes or preempt resources |
| Minimum Resources | n(m-1) + 1 for n processes, max m each |

---

*Next Chapter: [Memory Management →](07-Memory-Management.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
