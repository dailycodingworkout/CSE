# 📖 Chapter 6: Deadlocks

> **The Atomic Truth:** Deadlock = Circular wait for resources

---

## 🎯 GATE Syllabus Coverage
- Deadlock Characterization
- Resource Allocation Graph
- Deadlock Prevention
- Deadlock Avoidance (Banker's Algorithm)
- Deadlock Detection and Recovery

---

## 6.1 What is Deadlock?

### Definition
A **Deadlock** is a situation where a set of processes are blocked, each holding a resource and waiting to acquire a resource held by another process in the set.

### Real-World Analogy
**Traffic Gridlock:**
```
        ↑ Car B (wants →)
        │
  ──────┼────────
        │
←───────┼─────── Car C (wants ↑)
        │
        ↓ Car A (wants ←)
```
All cars waiting for each other. None can move!

### System Model
- **Resources:** R₁, R₂, ..., Rₘ (e.g., CPU, memory, printers)
- **Instances:** Each resource type has W instances
- **Process operations:** Request → Use → Release

---

## 6.2 Necessary Conditions for Deadlock

**All four conditions must hold simultaneously:**

| Condition | Description | Example |
|-----------|-------------|---------|
| **Mutual Exclusion** | Only one process can use resource at a time | Printer |
| **Hold and Wait** | Process holds resource while waiting for another | Process has file, wants printer |
| **No Preemption** | Resources can't be forcibly taken | Can't interrupt mid-print |
| **Circular Wait** | Circular chain of waiting | P₁→P₂→P₃→P₁ |

### Mnemonic: "MH-NC" = "Must Have No Circular"
- **M**utual exclusion
- **H**old and wait
- **N**o preemption
- **C**ircular wait

---

## 6.3 Resource Allocation Graph (RAG)

### Components
- **Process nodes:** Circles (P₁, P₂, ...)
- **Resource nodes:** Rectangles with dots for instances
- **Request edge:** P → R (process requests resource)
- **Assignment edge:** R → P (resource assigned to process)

### RAG Example

```
┌─────────────────────────────────────────┐
│                                         │
│    ┌───┐         ┌─────────┐           │
│    │ P₁│◄────────│R₁ [●][●]│           │
│    └─┬─┘         └────┬────┘           │
│      │                │                 │
│      │    Request     │ Assignment     │
│      ↓                ↓                 │
│    ┌─────────┐     ┌───┐               │
│    │R₂ [●]  │────→│ P₂│               │
│    └─────────┘     └───┘               │
│                                         │
└─────────────────────────────────────────┘
```

### Deadlock Detection via RAG

**Single Instance Resources:**
- Cycle in RAG = Deadlock

**Multiple Instance Resources:**
- Cycle is necessary but NOT sufficient for deadlock
- Need more complex detection

### Example: Cycle but No Deadlock

```
      ┌───┐
      │ P₁│◄──────┐
      └─┬─┘       │
        │         │
        ↓         │
    ┌───────┐     │
    │R₁[●][●]│────┘
    └───┬───┘
        │
        ↓
      ┌───┐
      │ P₃│ ←── P₃ holds R₁, can release
      └───┘
```

If P₃ releases R₁, the cycle breaks. No deadlock!

---

## 6.4 Handling Deadlocks

### Approaches

| Approach | Method | Overhead | Safety |
|----------|--------|----------|--------|
| **Prevention** | Ensure one condition never holds | High | Safe |
| **Avoidance** | Careful resource allocation | Medium | Safe |
| **Detection + Recovery** | Allow deadlock, then fix | Low | Reactive |
| **Ignore** | Pretend it doesn't happen | None | Risky |

---

## 6.5 Deadlock Prevention

### 6.5.1 Prevent Mutual Exclusion
- Not always possible (some resources inherently exclusive)
- Can use spooling for printers

### 6.5.2 Prevent Hold and Wait

**Method 1:** Request all resources at start
- Process must request all resources before execution
- Holds resources even when not needed

**Method 2:** Request only when holding none
- Release all before requesting new set

**Problems:** Low utilization, starvation possible

### 6.5.3 Prevent No Preemption

**Method:** If process can't get resource, release all held resources

```
if (resource not available) {
    release all held resources;
    wait for all needed resources;
}
```

**Works for:** CPU registers, memory
**Doesn't work for:** Printers, tapes

### 6.5.4 Prevent Circular Wait

**Method:** Impose total ordering on resources. Request in order only.

$$R_1 < R_2 < R_3 < ... < R_m$$

**Rule:** If process holds $R_i$, can only request $R_j$ where $j > i$

**Example:**
- Resources: Scanner (1) < Printer (2) < Disk (3)
- Process must request Scanner before Printer
- If needs Printer first, must release Scanner first

**Proof:** Cannot have cycle because edges go only in increasing order.

---

## 6.6 Deadlock Avoidance

### Concept
System makes decisions that ensure deadlock never occurs.

### Safe State
A state is **safe** if system can allocate resources to each process in some order and avoid deadlock.

**Safe State → No Deadlock**
**Unsafe State → Deadlock possible (not guaranteed)**

```
┌────────────────────────────────────────┐
│              ALL STATES                │
│  ┌──────────────────────────────────┐  │
│  │         SAFE STATES              │  │
│  │  (Can complete all processes)    │  │
│  │                                  │  │
│  └──────────────────────────────────┘  │
│  ┌──────────────────────────────────┐  │
│  │        UNSAFE STATES             │  │
│  │  ┌────────────────────────────┐  │  │
│  │  │     DEADLOCK STATES       │  │  │
│  │  └────────────────────────────┘  │  │
│  └──────────────────────────────────┘  │
└────────────────────────────────────────┘
```

### Safe Sequence
A sequence $\langle P_1, P_2, ..., P_n \rangle$ is safe if:
- For each $P_i$, its needs can be satisfied by currently available resources + resources held by all $P_j$ where $j < i$

---

## 6.7 Banker's Algorithm

### Overview
- Used for multiple instance resources
- Before allocation, check if resulting state is safe
- If safe, allocate. If unsafe, process must wait.

### Data Structures

| Structure | Size | Description |
|-----------|------|-------------|
| **Available** | m | Available[j] = instances of resource Rⱼ available |
| **Max** | n × m | Max[i][j] = max demand of Pᵢ for Rⱼ |
| **Allocation** | n × m | Allocation[i][j] = instances of Rⱼ held by Pᵢ |
| **Need** | n × m | Need[i][j] = Max[i][j] - Allocation[i][j] |

### Safety Algorithm

```
1. Work = Available;  Finish[i] = false for all i

2. Find process i such that:
   - Finish[i] == false
   - Need[i] ≤ Work

3. If found:
   Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If all Finish[i] == true:
   System is in SAFE state
   Else:
   System is in UNSAFE state
```

### Resource Request Algorithm

When process Pᵢ requests resources Request[i]:

```
1. If Request[i] > Need[i]:
   Error! (Exceeds maximum claim)

2. If Request[i] > Available:
   Process must wait (resources not available)

3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm:
   If safe: Grant request
   If unsafe: Restore old state, process waits
```

---

## 6.8 Banker's Algorithm Example

### Given Data

**Resources:** A=10, B=5, C=7

| Process | Allocation (A B C) | Max (A B C) | Need (A B C) |
|---------|-------------------|-------------|--------------|
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |

**Available:** Total - Allocated = (10,5,7) - (7,2,5) = (3,3,2)

### Finding Safe Sequence

**Step 1:** Work = (3, 3, 2)

| Check | Need ≤ Work? | Action |
|-------|--------------|--------|
| P0 | (7,4,3) ≤ (3,3,2)? NO | Skip |
| P1 | (1,2,2) ≤ (3,3,2)? YES | Execute P1 |

Work = (3,3,2) + (2,0,0) = (5,3,2), Finish[1] = true

**Step 2:** Work = (5, 3, 2)

| Check | Need ≤ Work? | Action |
|-------|--------------|--------|
| P0 | (7,4,3) ≤ (5,3,2)? NO | Skip |
| P2 | (6,0,0) ≤ (5,3,2)? NO | Skip |
| P3 | (0,1,1) ≤ (5,3,2)? YES | Execute P3 |

Work = (5,3,2) + (2,1,1) = (7,4,3), Finish[3] = true

**Step 3:** Work = (7, 4, 3)

| Check | Need ≤ Work? | Action |
|-------|--------------|--------|
| P0 | (7,4,3) ≤ (7,4,3)? YES | Execute P0 |

Work = (7,4,3) + (0,1,0) = (7,5,3), Finish[0] = true

**Step 4:** Work = (7, 5, 3)

| Check | Need ≤ Work? | Action |
|-------|--------------|--------|
| P2 | (6,0,0) ≤ (7,5,3)? YES | Execute P2 |

Work = (7,5,3) + (3,0,2) = (10,5,5), Finish[2] = true

**Step 5:** Work = (10, 5, 5)

| Check | Need ≤ Work? | Action |
|-------|--------------|--------|
| P4 | (4,3,1) ≤ (10,5,5)? YES | Execute P4 |

Work = (10,5,5) + (0,0,2) = (10,5,7), Finish[4] = true

**Safe Sequence:** ⟨P1, P3, P0, P2, P4⟩

**Note:** Multiple safe sequences may exist!

---

## 6.9 Deadlock Detection

### Single Instance Resources

Use **Wait-For Graph:**
- Remove resource nodes from RAG
- Edge Pᵢ → Pⱼ if Pᵢ waiting for resource held by Pⱼ
- Cycle in WFG = Deadlock

**Detection Algorithm:** O(n²) DFS

### Multiple Instance Resources

Similar to Safety Algorithm, but uses current allocation instead of maximum.

```
1. Work = Available
   For all i: Finish[i] = (Allocation[i] == 0)

2. Find i such that:
   - Finish[i] == false
   - Request[i] ≤ Work

3. If found:
   Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If any Finish[i] == false:
   Pᵢ is deadlocked
```

### When to Detect?
- On every resource request (high overhead)
- Periodically (e.g., every 5 minutes)
- When CPU utilization drops below threshold

---

## 6.10 Deadlock Recovery

### Process Termination

| Method | Description | Drawback |
|--------|-------------|----------|
| Abort all | Kill all deadlocked processes | High cost |
| Abort one by one | Kill until cycle breaks | Repeated detection |

**Selection criteria:**
- Priority
- CPU time used
- Resources held
- Remaining time
- Interactive vs batch

### Resource Preemption

1. **Select victim:** Choose process to preempt
2. **Rollback:** Return to safe state (checkpoint)
3. **Starvation prevention:** Limit preemptions per process

---

## 6.11 Numerical Problems

### Problem Type 1: RAG Analysis

**Question:** Is there a deadlock?

```
P1 holds R1, requests R2
P2 holds R2, requests R3
P3 holds R3, requests R1
```

**Solution:** 
- P1 → R2 → P2 → R3 → P3 → R1 → P1
- Cycle exists! Deadlock if single instance each.

### Problem Type 2: Minimum Resources for No Deadlock

**Question:** n processes, each needs k resources. Minimum resources to prevent deadlock?

**Formula:**
$$\text{Min resources} = n(k-1) + 1$$

**Example:** 5 processes, each needs 3 resources
- Min = 5(3-1) + 1 = 5(2) + 1 = 11 resources

**Proof:** In worst case, each process holds (k-1) resources. One more resource lets any process complete.

### Problem Type 3: Safe State Check

Given allocation, find if safe and give safe sequence.

(Solved in Banker's Algorithm example above)

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2018)
**Q:** In a system with 3 processes and 2 resource types, P holds R1 and needs R2. Q holds R2 and needs R1. Which is true?
(a) System is in safe state
(b) Deadlock exists
(c) No deadlock possible
(d) Need more information

**Answer:** (b) Deadlock exists

**Explanation:** Circular wait: P→R2→Q→R1→P

---

### Question 2 (GATE 2019)
**Q:** 4 processes need maximum 4, 3, 4, 4 units of resource R. Total R = 12. Is system safe if current allocation is 2, 1, 2, 1?

**Solution:**
- Available = 12 - (2+1+2+1) = 6
- Need: P0=2, P1=2, P2=2, P3=3
- All needs ≤ Available(6)
- Can execute in order: P0, P1, P2, P3

**Answer:** Yes, system is safe.

---

### Question 3 (GATE 2020)
**Q:** 5 processes, each needs 3 resources. Minimum resources to avoid deadlock?

**Solution:** n(k-1) + 1 = 5(3-1) + 1 = 11

**Answer:** 11 resources

---

## 🧠 Memory Tricks

### Mnemonic: Four Conditions "MH-NC"
- **M**utual exclusion
- **H**old and wait  
- **N**o preemption
- **C**ircular wait

All must be TRUE for deadlock.

### Banker's Algorithm Memory Hook
Think of a **bank**:
- **Max:** Credit limit
- **Allocation:** Money borrowed
- **Need:** Remaining credit
- **Available:** Cash in vault
- Bank only lends if it can recover (safe state)

### The Mental Slider: Safe vs Unsafe
Imagine a **tightrope**:
- Safe state = On the rope (can reach end)
- Unsafe state = Wobbling (might fall)
- Deadlock = Fallen (stuck)

---

## ⚠️ Common GATE Traps

### Trap 1: Cycle = Deadlock
**Wrong:** Any cycle means deadlock
**Right:** For multiple instances, cycle is necessary but not sufficient

### Trap 2: Unsafe = Deadlock
**Wrong:** Unsafe state means deadlock
**Right:** Unsafe state means deadlock is *possible*, not certain

### Trap 3: Banker's Comparison
**Wrong:** Using > instead of ≤ in Need comparison
**Right:** Need[i] ≤ Work means process CAN run

### Trap 4: Safe Sequence Uniqueness
**Wrong:** There's only one safe sequence
**Right:** Multiple safe sequences usually exist

---

## 🛠️ Problem-Solving Techniques

### Technique 1: Deadlock Detection via RAG

**Step-by-step approach:**

```
Step 1: Draw all processes as circles, resources as rectangles
Step 2: Draw dots inside rectangles for instances
Step 3: Draw edges:
        - Request: P → R (process wants resource)
        - Assignment: R → P (resource given to process)
Step 4: Check for cycle
        - Single instance: Cycle = Deadlock
        - Multiple instance: Cycle = Possible deadlock (need reduction)
```

**RAG Reduction Algorithm (Multiple Instances):**
```
1. Find a process whose requests can be satisfied
2. Remove all its edges (pretend it completes)
3. Repeat until no more reductions possible
4. If edges remain → Deadlock
```

### Technique 2: Banker's Algorithm - Systematic Approach

**The "Greedy Safe Sequence" Method:**

```
Step 1: Setup Tables
        ┌─────────┬────────────┬─────┬──────┐
        │ Process │ Allocation │ Max │ Need │
        ├─────────┼────────────┼─────┼──────┤
        │  P0     │  (A,B,C)   │     │      │
        └─────────┴────────────┴─────┴──────┘
        
Step 2: Calculate Need = Max - Allocation

Step 3: Calculate Available = Total - ΣAllocation

Step 4: Create Work = Available (copy)

Step 5: Find process where Need ≤ Work
        (Compare element-wise: ALL must satisfy)

Step 6: If found:
        - Work = Work + Allocation[process]
        - Mark process as finished
        - Add to safe sequence
        - Go to Step 5

Step 7: If all finished → Safe
        If stuck with unfinished → Unsafe
```

### Technique 3: Minimum Resources Formula

**For n processes, each needing maximum k resources:**

$$\text{Minimum resources for deadlock-free} = n(k-1) + 1$$

**Proof strategy:** In worst case, each process holds (k-1) resources. One more resource allows any process to complete.

**Variations:**
- Different max for each process: $\sum(max_i - 1) + 1$
- At least one must complete: $\sum(max_i) - n + 1$

### Technique 4: Quick Deadlock Condition Check

**Use "MHNC" checklist:**

| Condition | Quick Test |
|-----------|------------|
| **M**utual Exclusion | Is resource shareable? If yes, can't deadlock on it |
| **H**old and Wait | Does process hold while requesting? |
| **N**o Preemption | Can we forcibly take resource? |
| **C**ircular Wait | Draw dependency, check cycle |

**If ANY condition is FALSE → No deadlock possible**

### Technique 5: Request Handling in Banker's

**When process Pᵢ requests Request[i]:**

```
Step 1: Check Request[i] ≤ Need[i]?
        NO → Error (exceeded claim)
        
Step 2: Check Request[i] ≤ Available?
        NO → Wait (resources unavailable)
        
Step 3: Tentatively allocate:
        Available -= Request[i]
        Allocation[i] += Request[i]
        Need[i] -= Request[i]
        
Step 4: Run Safety Algorithm
        Safe → Grant request
        Unsafe → Rollback, make process wait
```

### Technique 6: Finding ALL Safe Sequences

**Systematic exploration:**
```
At each step, list ALL processes that CAN run (Need ≤ Work)
Create branches for each choice
Continue until all complete
Each complete path = one safe sequence
```

**Counting formula:** If at each step there are $c_1, c_2, ..., c_n$ choices:
$$\text{Total safe sequences} = c_1 \times c_2 \times ... \times c_n$$

### Technique 7: Resource Allocation Graph Construction

**Drawing tips:**
```
1. Use squares for resource types
2. Put dots inside for instances
3. Arrow TO process = allocated
4. Arrow FROM process = requested
5. Check cycles by tracing arrows
```

**Quick cycle detection:**
- Start from any edge
- Follow the direction
- If you return to start → Cycle exists

### Technique 8: Prevention Strategy Selection

| Goal | Break Which Condition | How |
|------|----------------------|-----|
| Simple, always works | Circular Wait | Resource ordering |
| Maximize utilization | Hold and Wait | Request all upfront |
| For preemptible resources | No Preemption | Allow preemption |

**Decision flowchart:**
```
Is resource preemptible (e.g., CPU)?
├── Yes → Allow preemption
└── No → Can we order resources?
    ├── Yes → Circular wait prevention
    └── No → Request all at once
```

---

## 📝 Practice Problems

### Problem 1
| Process | Allocation (A B) | Max (A B) |
|---------|-----------------|-----------|
| P0 | 2 1 | 4 2 |
| P1 | 3 2 | 5 4 |
| P2 | 1 0 | 2 1 |

Available: A=2, B=1. Find safe sequence.

### Problem 2
Draw RAG and determine if deadlock:
- P1 holds R1, R2, requests R3
- P2 holds R3, requests R1
- R1, R2, R3 have 1 instance each

### Problem 3
n=10 processes, each needs max 5 resources. Minimum resources for deadlock-free?

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| Deadlock | Circular wait for resources |
| 4 Conditions | Mutual Excl, Hold&Wait, No Preempt, Circular Wait |
| RAG Cycle | Single instance: Deadlock. Multiple: Maybe. |
| Safe State | Can complete all processes |
| Banker's | Check safety before allocation |
| Min Resources | n(k-1) + 1 for n processes needing k each |

### Banker's Algorithm Steps
1. Calculate Need = Max - Allocation
2. Calculate Available = Total - ΣAllocation
3. Find process with Need ≤ Work
4. Add its Allocation to Work
5. Repeat until all done (safe) or stuck (unsafe)

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 7 - Memory Management](../07-Memory-Management/README.md)*
