# Chapter 5: Deadlocks

> **"Deadlock is like two cars meeting on a narrow bridge - neither can move until the other backs up, but neither will"**

---

## 🎯 What is Deadlock?

**Definition:** A set of processes is deadlocked when every process in the set is waiting for an event that can only be caused by another process in the set.

```
     ┌──────────────┐
     │  Process P1  │
     │  (holds R1,  │
     │   wants R2)  │
     └───────┬──────┘
             │ waiting
             ▼
     ┌──────────────┐
     │  Resource R2 │
     │  (held by P2)│
     └───────┬──────┘
             │ held by
             ▼
     ┌──────────────┐
     │  Process P2  │
     │  (holds R2,  │
     │   wants R1)  │
     └───────┬──────┘
             │ waiting
             ▼
     ┌──────────────┐
     │  Resource R1 │
     │  (held by P1)│ ← CIRCULAR WAIT!
     └──────────────┘
```

---

## 🔐 Four Necessary Conditions (Coffman Conditions)

**All FOUR must hold simultaneously for deadlock:**

| Condition | Definition | Example |
|-----------|------------|---------|
| **Mutual Exclusion** | At least one resource held in non-sharable mode | Printer can only be used by one process |
| **Hold and Wait** | Process holds resource while waiting for others | Process has file open, waiting for printer |
| **No Preemption** | Resources cannot be forcibly taken | Can't take CPU register from running process |
| **Circular Wait** | Circular chain of processes waiting for resources | P1→R1→P2→R2→P1 |

**💡 Memory Trick: MHNC** = "Must Have No Circular wait"

**⚠️ GATE Insight:** 
- These are NECESSARY conditions, not sufficient
- All 4 must be present for deadlock to occur
- Breaking ANY ONE prevents/resolves deadlock

---

## 📊 Resource Allocation Graph (RAG)

### Notation

```
Process:    ○ or [Pi]    (circle)
Resource:   □ or [Rj]    (rectangle with dots for instances)
Request:    Pi ──────→ Rj    (process to resource)
Assignment: Rj ──────→ Pi    (resource to process)
```

### Single Instance Resources

**Deadlock ⟺ Cycle exists**

```
Example with cycle (DEADLOCK):
    P1 → R1 → P2 → R2 → P1
         ↓         ↓
    (P1 holds R1, wants R2)
    (P2 holds R2, wants R1)
```

### Multiple Instance Resources

**Cycle → Possible deadlock (not guaranteed)**
**No Cycle → Definitely no deadlock**

```
Example with cycle but NO deadlock:
    R1 has 2 instances
    P1 holds R1(1), wants R2
    P2 holds R2, wants R1
    P3 holds R1(2)
    
    P3 can finish → releases R1
    Now P2 can get R1, finish → releases R2
    P1 can get R2, finish
    → No deadlock despite cycle!
```

---

## 🛡️ Deadlock Handling Strategies

| Strategy | Approach | Overhead | When to Use |
|----------|----------|----------|-------------|
| **Prevention** | Ensure at least one condition never holds | High | Critical systems |
| **Avoidance** | Carefully allocate resources | Medium | Known resource needs |
| **Detection + Recovery** | Allow deadlock, detect and fix | Low until deadlock | General systems |
| **Ignorance** | Pretend it won't happen | None | Most OS (Ostrich Algorithm) |

---

## 🚫 Deadlock Prevention

### 1. Mutual Exclusion
**Approach:** Make resources sharable

**Practical?** Often NO
- Some resources inherently non-sharable (printer, tape drive)
- Read-only files CAN be shared

---

### 2. Hold and Wait
**Approach:** Process must request all resources at once

**Methods:**
1. Request all before execution starts
2. Request only when holding none

```c
// Method 1: Request all upfront
wait(all_resources);
    // Execute
signal(all_resources);

// Method 2: Release before new request
signal(current_resources);
wait(new_resources);
```

**Problems:**
- Low resource utilization
- Possible starvation

---

### 3. No Preemption
**Approach:** If request fails, release all held resources

```c
if (request(R) fails) {
    release(all_held_resources);
    wait(all_resources);  // Try again
}
```

**Alternative:** OS preempts resources from waiting processes

**Practical?** Only for certain resources (CPU, memory)
- Can't preempt printer mid-job!

---

### 4. Circular Wait
**Approach:** Impose total ordering on resource types

**Method:** Number all resources, request in increasing order only

```
Resource ordering: R1 < R2 < R3 < R4

Process must request: R1 → R2 → R3  (increasing order)
Cannot request: R3 → R1  (would violate ordering)
```

**Why it works:**
```
For cycle P1→R1→P2→R2→P1:
- P1 has R1, wants R2 → implies R1 < R2
- P2 has R2, wants R1 → implies R2 < R1
- CONTRADICTION! So cycle impossible.
```

**💡 GATE Fact:** This is the most practical prevention method

---

## ⚠️ Deadlock Avoidance

### Concept: Safe State

**Safe State:** There exists a sequence of processes such that all can complete

```
Safe State Check:
Available resources = V
For each process Pi:
    If Pi's needs ≤ V:
        V = V + Pi's allocation (simulate completion)
        Mark Pi as finished
    Repeat until all finished or stuck
    
All finished → SAFE
Stuck → UNSAFE
```

**Key Insight:**
```
Safe → No deadlock (guaranteed)
Unsafe → Deadlock possible (not guaranteed)
Deadlock → Unsafe (definitely)
```

```
        ┌─────────────────────┐
        │     All States      │
        │  ┌───────────────┐  │
        │  │  Safe States  │  │
        │  │               │  │
        │  │               │  │
        │  └───────────────┘  │
        │  ┌───────────────┐  │
        │  │ Unsafe States │  │
        │  │  ┌─────────┐  │  │
        │  │  │Deadlock │  │  │
        │  │  └─────────┘  │  │
        │  └───────────────┘  │
        └─────────────────────┘
```

---

### Banker's Algorithm

**Prerequisites:**
1. Number of processes (n) and resources (m) known
2. Maximum needs declared in advance
3. Processes must return resources in finite time

**Data Structures:**

| Variable | Size | Description |
|----------|------|-------------|
| `Available` | m | Available resources of each type |
| `Max` | n × m | Maximum demand of each process |
| `Allocation` | n × m | Currently allocated to each process |
| `Need` | n × m | Remaining need = Max - Allocation |

---

### Safety Algorithm

```
1. Initialize:
   Work = Available (copy)
   Finish[i] = false for all i

2. Find process Pi where:
   Finish[i] = false AND Need[i] ≤ Work
   
   If found: Go to step 3
   If not found: Go to step 4

3. Execute Pi (simulate):
   Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. Check:
   If all Finish[i] = true → SAFE
   Else → UNSAFE
```

---

### Resource Request Algorithm

When process Pi requests Request[i]:

```
1. Check validity:
   If Request[i] > Need[i] → ERROR (exceeded max claim)

2. Check availability:
   If Request[i] > Available → Pi must WAIT

3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm:
   If SAFE → Grant request
   If UNSAFE → Deny request, restore old state
```

---

### Banker's Algorithm Example

**System:**
- 5 processes: P0, P1, P2, P3, P4
- 3 resource types: A (10), B (5), C (7)

| Process | Allocation (A B C) | Max (A B C) | Need (A B C) |
|---------|-------------------|-------------|--------------|
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |

**Total Allocated:** 7 + 2 + 7 = (7, 2, 5)
**Available:** (10, 5, 7) - (7, 2, 5) = **(3, 3, 2)**

---

**Finding Safe Sequence:**

```
Work = (3, 3, 2)

Step 1: Find process with Need ≤ Work
   P0: (7,4,3) > (3,3,2) ✗
   P1: (1,2,2) ≤ (3,3,2) ✓  → Execute P1
   
   Work = (3,3,2) + (2,0,0) = (5,3,2)
   Finish[P1] = true

Step 2: Continue
   P0: (7,4,3) > (5,3,2) ✗
   P3: (0,1,1) ≤ (5,3,2) ✓  → Execute P3
   
   Work = (5,3,2) + (2,1,1) = (7,4,3)
   Finish[P3] = true

Step 3: Continue
   P0: (7,4,3) ≤ (7,4,3) ✓  → Execute P0
   
   Work = (7,4,3) + (0,1,0) = (7,5,3)
   Finish[P0] = true

Step 4: Continue
   P2: (6,0,0) ≤ (7,5,3) ✓  → Execute P2
   
   Work = (7,5,3) + (3,0,2) = (10,5,5)
   Finish[P2] = true

Step 5: Continue
   P4: (4,3,1) ≤ (10,5,5) ✓  → Execute P4
   
   Finish[P4] = true

All finished → SAFE!
Safe Sequence: <P1, P3, P0, P2, P4>
```

---

**Request Example:**

P1 requests (1, 0, 2)

```
Check 1: Request ≤ Need?
   (1,0,2) ≤ (1,2,2) ✓

Check 2: Request ≤ Available?
   (1,0,2) ≤ (3,3,2) ✓

Pretend allocation:
   Available = (3,3,2) - (1,0,2) = (2,3,0)
   Allocation[P1] = (2,0,0) + (1,0,2) = (3,0,2)
   Need[P1] = (1,2,2) - (1,0,2) = (0,2,0)

Run Safety Algorithm with new state...
(Work through to find safe sequence)

If safe → Grant
If unsafe → Deny, rollback
```

---

## 🔍 Deadlock Detection

### Single Instance of Each Resource Type

**Method:** Build Wait-For Graph (WFG)

```
Resource Allocation Graph → Wait-For Graph
Remove resource nodes, draw direct edges between processes

Pi → Rj → Pk  becomes  Pi → Pk
```

**Detection:** Run cycle detection algorithm

**Time Complexity:** O(n²) where n = number of processes

---

### Multiple Instance Resources

**Detection Algorithm (similar to Safety Algorithm):**

```
1. Initialize:
   Work = Available
   For each Pi: Finish[i] = (Allocation[i] == 0)

2. Find Pi where:
   Finish[i] = false AND Request[i] ≤ Work

   If found: Work = Work + Allocation[i]
             Finish[i] = true
             Go to step 2
   If not found: Go to step 3

3. Result:
   If any Finish[i] = false → Process Pi is DEADLOCKED
```

**Difference from Banker's:**
- Uses Request (current) not Need (maximum)
- More optimistic - assumes processes might release resources

---

### When to Run Detection?

| Frequency | Trade-off |
|-----------|-----------|
| Every request | High overhead, fast detection |
| Periodically | Medium overhead, medium delay |
| CPU utilization drop | Low overhead, relies on symptom |

**💡 GATE Insight:** Run when CPU utilization drops below threshold

---

## 🔧 Deadlock Recovery

### 1. Process Termination

| Method | Approach | Cost |
|--------|----------|------|
| **Abort All** | Kill all deadlocked processes | High (lost work) |
| **Abort One by One** | Kill until deadlock resolves | Medium |

**Selection Criteria (which to kill?):**
1. Priority of process
2. How long it has run
3. Resources used
4. Resources needed to complete
5. Interactive vs batch
6. How many processes to terminate

---

### 2. Resource Preemption

**Steps:**
1. **Select victim:** Which resources to preempt
2. **Rollback:** Return to safe state (checkpoint)
3. **Prevent starvation:** Don't always pick same victim

**Rollback Options:**
- Total rollback (abort and restart)
- Partial rollback (checkpoint-based)

---

## 📐 Combined Approach

**Real systems use combination:**

```
┌─────────────────────────────────────────────────────┐
│            Resource Classification                   │
├────────────────┬────────────────┬───────────────────┤
│ Internal       │ Swappable      │ Non-preemptable   │
│ Resources      │ Space          │ Resources         │
├────────────────┼────────────────┼───────────────────┤
│ Prevention     │ Prevention     │ Avoidance         │
│ (ordering)     │ (hold & wait)  │ (Banker's)        │
└────────────────┴────────────────┴───────────────────┘
```

---

## 🎯 Comparison of Methods

| Method | Overhead | Restrictions | Speed |
|--------|----------|--------------|-------|
| **Prevention** | Low (runtime) | High | Fast |
| **Avoidance** | Medium | Max needs known | Medium |
| **Detection** | High (periodic) | None | Slow |
| **Ignorance** | None | None | N/A |

---

## 🧮 Important Formulas & Calculations

### Minimum Resources to Avoid Deadlock

**For n processes, each needing max R resources of same type:**

```
Minimum = n × (R - 1) + 1
```

**Explanation:** 
- Worst case: Each process has (R-1) resources (one short of completing)
- Need 1 more for any process to complete
- n(R-1) + 1 guarantees at least one can finish

**Example:**
- 5 processes, each needs max 3 resources
- Minimum = 5 × (3-1) + 1 = 11 resources

---

### Multiple Resource Types

**For m resource types, ni processes needing resource type i:**

```
For each resource type i:
Minimum[i] = (Sum of (Max[j,i] - 1) for all processes j) + 1
           = (Sum of Max[j,i]) - n + 1
```

---

### Maximum Processes Without Deadlock

Given R resources of one type, each process needs max M:

```
Maximum processes = floor((R - 1) / (M - 1))
```

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **Banker's Algorithm:** Given state, find safe sequence
2. **Minimum resources:** Calculate for deadlock prevention
3. **RAG analysis:** Identify deadlock from graph
4. **Coffman conditions:** Which condition violated
5. **Safe/Unsafe determination:** Is given state safe?

### ⚠️ Edge Cases & Traps:

1. **Safe sequence may not be unique** - Multiple valid orders
2. **Cycle with multi-instance** - NOT always deadlock
3. **Banker's requires max claims** - Often unrealistic assumption
4. **Need = Max - Allocation** - Don't confuse with Request
5. **Detection uses Request, Avoidance uses Max**

---

## 🔢 Quick Problems

### Problem 1: Minimum Resources
**Q:** 4 processes each need max 5 instances of resource R. Minimum R instances to guarantee no deadlock?

**A:** n(R-1) + 1 = 4(5-1) + 1 = **17 instances**

---

### Problem 2: Maximum Processes  
**Q:** System has 10 instances of resource. Each process needs max 4. Maximum processes without deadlock?

**A:** floor((10-1)/(4-1)) = floor(9/3) = **3 processes**

---

### Problem 3: Safe State
**Q:** Available = 2, Processes: P1 (Alloc=2, Max=5), P2 (Alloc=3, Max=6). Is it safe?

**A:** 
- Need: P1=3, P2=3
- Available=2 < Need of both
- **UNSAFE!**

---

## 🎯 Quick Revision Points

```
✓ Deadlock needs ALL 4 conditions (MHNC)
✓ Prevention: Break any one condition
✓ Circular Wait prevention most practical (ordering)
✓ Safe state: sequence exists for all to complete
✓ Banker's: Avoidance using Need matrix
✓ RAG: Cycle = Deadlock (single instance)
✓ WFG: Collapse RAG, find cycles
✓ Minimum resources = n(R-1) + 1
✓ Detection: Uses Request, not Need
✓ Recovery: Terminate or Preempt
```

---

## 📚 Algorithm Complexity

```
Safety Algorithm: O(m × n²)
  - m resource types, n processes
  - May need n passes, each checking n processes

Detection Algorithm: O(m × n²)
  - Similar to safety algorithm

Cycle Detection (WFG): O(n²)
  - DFS on wait-for graph
```

---

[← Previous: Process Synchronization](./04-Process-Synchronization.md) | [Next: Memory Management →](./06-Memory-Management.md)
