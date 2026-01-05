# Chapter 3: CPU Scheduling Algorithms

## 🎯 The Atomic Truth
> **Scheduling = Maximize CPU Use + Minimize Wait**

---

## 🧠 Why CPU Scheduling?

### The Problem
- Multiple processes compete for ONE CPU
- CPU is idle during I/O operations
- Some processes are urgent, some aren't

### The Solution
**CPU Scheduler**: Decides WHICH process runs WHEN and for HOW LONG.

```
READY QUEUE:  [P1] → [P2] → [P3] → [P4]
                              ↓
                      ┌──────────────┐
                      │  SCHEDULER   │
                      │  (Algorithm) │
                      └──────┬───────┘
                             ↓
                      ┌──────────────┐
                      │     CPU      │
                      └──────────────┘
```

---

## 📊 Scheduling Criteria Recap

| Criterion | Goal | Formula |
|-----------|------|---------|
| **Turnaround Time (TAT)** | Minimize | Completion - Arrival |
| **Waiting Time (WT)** | Minimize | TAT - Burst Time |
| **Response Time (RT)** | Minimize | First CPU - Arrival |
| **Throughput** | Maximize | Processes / Time |
| **CPU Utilization** | Maximize | (Busy Time / Total Time) × 100 |

---

## 🔑 Preemptive vs Non-Preemptive

| Aspect | Non-Preemptive | Preemptive |
|--------|----------------|------------|
| **Definition** | Process runs until completion/blocking | Process can be interrupted |
| **When stops** | Finishes, I/O request, or voluntarily yields | All above + scheduler forces switch |
| **Overhead** | Lower (fewer context switches) | Higher (more context switches) |
| **Response** | Poor | Better |
| **Starvation** | Possible | Less likely |
| **Example** | FCFS, SJF | SRTF, RR, Priority |

---

## 📚 Scheduling Algorithms

---

## 1️⃣ First-Come, First-Served (FCFS)

### The Idea
> Queue at bank: First person in line gets served first.

**Type**: Non-preemptive

### Algorithm
1. Processes arrive in ready queue
2. Execute in order of arrival
3. No preemption

### Example

| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 24 |
| P2 | 1 | 3 |
| P3 | 2 | 3 |

**Gantt Chart**:
```
|    P1 (0-24)    | P2 (24-27) | P3 (27-30) |
0                 24           27           30
```

**Calculations**:

| Process | Completion | TAT | WT |
|---------|------------|-----|-----|
| P1 | 24 | 24-0=24 | 24-24=0 |
| P2 | 27 | 27-1=26 | 26-3=23 |
| P3 | 30 | 30-2=28 | 28-3=25 |

$$\text{Avg TAT} = \frac{24+26+28}{3} = 26 \text{ ms}$$

$$\text{Avg WT} = \frac{0+23+25}{3} = 16 \text{ ms}$$

### The Convoy Effect 🚗🚚

**Problem**: Short processes wait behind long process.

```
CONVOY EFFECT:
                    Long Process P1
Small P2 ─────────→ ████████████████████████████
Small P3 ─────────→ Waiting... Waiting... Waiting...
Small P4 ─────────→ Still waiting...
```

**Like being stuck behind a truck on a single-lane road.**

### FCFS Summary

| Pros | Cons |
|------|------|
| Simple to implement | Convoy effect |
| Fair (first come = first serve) | High average waiting time |
| No starvation | Poor for interactive systems |

---

## 2️⃣ Shortest Job First (SJF)

### The Idea
> Express checkout: Customers with fewer items go first.

**Type**: Non-preemptive

### Algorithm
1. Select process with shortest burst time
2. Execute to completion
3. Repeat

### Example

| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**At t=0**: Only P1 available → P1 runs (0-7)
**At t=7**: P2, P3, P4 available → P3 shortest (1) → P3 runs (7-8)
**At t=8**: P2, P4 available → Both have 4 → P2 arrived first → P2 runs (8-12)
**At t=12**: Only P4 → P4 runs (12-16)

**Gantt Chart**:
```
| P1 (0-7) | P3 (7-8) | P2 (8-12) | P4 (12-16) |
0          7          8           12           16
```

**Calculations**:

| Process | Completion | TAT | WT |
|---------|------------|-----|-----|
| P1 | 7 | 7 | 0 |
| P2 | 12 | 10 | 6 |
| P3 | 8 | 4 | 3 |
| P4 | 16 | 11 | 7 |

$$\text{Avg WT} = \frac{0+6+3+7}{4} = 4 \text{ ms}$$

### The Optimality Theorem

> **SJF gives minimum average waiting time among all non-preemptive algorithms.**

**Proof Intuition**: Short jobs waiting behind long jobs add more to total waiting time than vice versa.

### The Problem: Prediction

**We don't know burst time in advance!**

**Solution**: Predict using exponential averaging:

$$\tau_{n+1} = \alpha \cdot t_n + (1-\alpha) \cdot \tau_n$$

Where:
- $\tau_{n+1}$ = predicted next burst
- $t_n$ = actual last burst
- $\tau_n$ = previous prediction
- $\alpha$ = weight factor (typically 0.5)

**Example**: If $\alpha = 0.5$, $t_n = 6$, $\tau_n = 10$:
$$\tau_{n+1} = 0.5 \times 6 + 0.5 \times 10 = 8$$

### SJF Summary

| Pros | Cons |
|------|------|
| Optimal average WT | Starvation of long processes |
| Better throughput | Need to predict burst time |
| | Non-preemptive |

---

## 3️⃣ Shortest Remaining Time First (SRTF)

### The Idea
> Preemptive version of SJF. Always run process with least remaining time.

**Type**: Preemptive SJF

### Algorithm
1. At each time unit (or arrival), compare remaining times
2. Switch to process with shortest remaining time
3. Preempt if necessary

### Example

| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**Step-by-step**:

| Time | Event | Running | Ready Queue (Remaining) |
|------|-------|---------|------------------------|
| 0 | P1 arrives | P1 (8) | - |
| 1 | P2 arrives, P2 < P1 | P2 (4) | P1(7) |
| 2 | P3 arrives, P2 still shortest | P2 (3) | P1(7), P3(9) |
| 3 | P4 arrives, P2 still shortest | P2 (2) | P1(7), P3(9), P4(5) |
| 5 | P2 completes | P4 (5) | P1(7), P3(9) |
| 10 | P4 completes | P1 (7) | P3(9) |
| 17 | P1 completes | P3 (9) | - |
| 26 | P3 completes | - | - |

**Gantt Chart**:
```
|P1| P2 (1-5) | P4 (5-10) | P1 (10-17) | P3 (17-26) |
0  1          5           10           17           26
```

**Calculations**:

| Process | Completion | TAT | WT |
|---------|------------|-----|-----|
| P1 | 17 | 17 | 17-8=9 |
| P2 | 5 | 4 | 4-4=0 |
| P3 | 26 | 24 | 24-9=15 |
| P4 | 10 | 7 | 7-5=2 |

$$\text{Avg WT} = \frac{9+0+15+2}{4} = 6.5 \text{ ms}$$

### SRTF Summary

| Pros | Cons |
|------|------|
| Optimal among all algorithms | High context switch overhead |
| Best average WT | Still has starvation |
| Good response time | Need burst time prediction |

---

## 4️⃣ Priority Scheduling

### The Idea
> VIP lounge: Important people go first regardless of arrival time.

**Type**: Can be Preemptive or Non-Preemptive

### Convention
- **Lower number = Higher priority** (usually in GATE)
- Unless stated otherwise!

### Example (Non-Preemptive)

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1 | 0 | 10 | 3 |
| P2 | 0 | 1 | 1 |
| P3 | 0 | 2 | 4 |
| P4 | 0 | 1 | 5 |
| P5 | 0 | 5 | 2 |

**Order**: P2 (1) → P5 (2) → P1 (3) → P3 (4) → P4 (5)

**Gantt Chart**:
```
| P2 | P5 (1-6) | P1 (6-16) | P3 (16-18) | P4 (18-19) |
0    1          6           16           18           19
```

### The Starvation Problem

**Low priority process may NEVER execute** (infinite waiting).

```
STARVATION SCENARIO:
                           High Priority
Low Priority P1 ────────→  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (keeps coming)
(Waiting forever...)       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                           P1: "When is my turn?!"
```

### The Solution: Aging

**Gradually increase priority of waiting processes.**

$$\text{New Priority} = \text{Original Priority} - \text{(Wait Time / Aging Factor)}$$

**Example**: Priority decreases by 1 for every 10 minutes of waiting.

---

## 5️⃣ Round Robin (RR)

### The Idea
> Carousel: Everyone gets equal turn, then goes to back of line.

**Type**: Preemptive

### Algorithm
1. Fixed time quantum (q)
2. Each process runs for at most q time units
3. After q, goes to back of queue
4. FCFS within the queue

### Example (Time Quantum = 4)

| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 24 |
| P2 | 0 | 3 |
| P3 | 0 | 3 |

**Execution**:

| Time | Process | Remaining |
|------|---------|-----------|
| 0-4 | P1 | 20 |
| 4-7 | P2 | 0 (done) |
| 7-10 | P3 | 0 (done) |
| 10-14 | P1 | 16 |
| 14-18 | P1 | 12 |
| 18-22 | P1 | 8 |
| 22-26 | P1 | 4 |
| 26-30 | P1 | 0 (done) |

**Gantt Chart**:
```
| P1 | P2 | P3 | P1 | P1 | P1 | P1 | P1 |
0    4    7   10   14   18   22   26   30
```

**Calculations**:

| Process | Completion | TAT | WT |
|---------|------------|-----|-----|
| P1 | 30 | 30 | 30-24=6 |
| P2 | 7 | 7 | 7-3=4 |
| P3 | 10 | 10 | 10-3=7 |

$$\text{Avg WT} = \frac{6+4+7}{3} = 5.67 \text{ ms}$$

### Time Quantum Selection

```
QUANTUM SIZE EFFECT:

q → ∞:   Round Robin becomes FCFS
q → 0:   Maximum context switches (processor sharing)

OPTIMAL QUANTUM:
┌────────────────────────────────────────────────────────┐
│ Too Small        │      Optimal      │   Too Large    │
│ High overhead    │    Good balance   │   FCFS-like    │
│ More switches    │                   │   Poor response│
└────────────────────────────────────────────────────────┘
                         ↑
              Typically 10-100 ms
              Rule: 80% of bursts should complete in one quantum
```

### RR Formula: Number of Context Switches

For process with burst time B and quantum q:

$$\text{Context Switches for Process} = \lceil B/q \rceil - 1$$

**Total Context Switches**:
$$\sum_{i=1}^{n} \lceil B_i/q \rceil - 1 + \text{(inter-process switches)}$$

### RR Summary

| Pros | Cons |
|------|------|
| Fair | Performance depends on q |
| No starvation | Higher avg TAT than SJF |
| Good for time-sharing | More context switches |
| Predictable response time | |

---

## 6️⃣ Multilevel Queue Scheduling

### The Idea
> Different queues for different types of processes.

```
┌─────────────────────────────────────────────────────────┐
│  HIGHEST PRIORITY                                        │
│  ┌────────────────────────────────────────────────────┐ │
│  │ System Processes (Priority 0)      [RR, q=8]       │ │
│  └────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Interactive Processes (Priority 1) [RR, q=16]      │ │
│  └────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Batch Processes (Priority 2)       [FCFS]          │ │
│  └────────────────────────────────────────────────────┘ │
│  LOWEST PRIORITY                                        │
└─────────────────────────────────────────────────────────┘
                         ↓
                  ┌──────────────┐
                  │     CPU      │
                  └──────────────┘
```

### Key Features
1. Multiple ready queues based on process type
2. Each queue has its own scheduling algorithm
3. Higher queue has priority over lower queues
4. Processes don't move between queues (fixed assignment)

---

## 7️⃣ Multilevel Feedback Queue (MLFQ)

### The Idea
> Processes can move between queues based on behavior.

**The Most Sophisticated Scheduler!**

```
┌─────────────────────────────────────────────────────────┐
│  Queue 0: [RR, q=8]   ← New processes enter here        │
│  ├─ If uses full quantum → Demote to Queue 1            │
│  └─ If blocks for I/O → Stay or Promote                 │
├─────────────────────────────────────────────────────────┤
│  Queue 1: [RR, q=16]  ← Demoted processes               │
│  ├─ If uses full quantum → Demote to Queue 2            │
│  └─ If blocks for I/O → Promote to Queue 0              │
├─────────────────────────────────────────────────────────┤
│  Queue 2: [FCFS]      ← CPU-bound processes end here    │
│  └─ May get promoted if waiting too long (aging)        │
└─────────────────────────────────────────────────────────┘
```

### Example

**Process P1**: CPU-bound (needs 100ms)
**Process P2**: I/O-bound (needs 5ms CPU, then I/O)

```
TIME PROGRESSION:

t=0:  P1, P2 enter Queue 0
      P1 runs for 8ms → Demoted to Queue 1
      P2 runs for 5ms → I/O → Returns to Queue 0

t=13: P2 runs for 3ms → I/O
      P1 runs for 16ms from Queue 1 → Demoted to Queue 2

      P2: Happy in Queue 0 (good response time)
      P1: Stuck in Queue 2 (but doesn't need fast response)
```

### MLFQ Rules

1. Higher priority queue always runs first
2. New process starts in highest priority queue
3. If process uses entire time quantum → Demote
4. If process blocks before quantum → Stay or Promote
5. Periodically boost all processes to prevent starvation

### MLFQ Summary

| Pros | Cons |
|------|------|
| Adapts to process behavior | Complex to implement |
| Good for mixed workloads | Many parameters to tune |
| Separates I/O-bound and CPU-bound | Overhead of queue management |
| Prevents starvation (with aging) | |

---

## 🧮 GATE Numerical: Complete Example

### Problem

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1 | 0 | 5 | 3 |
| P2 | 1 | 3 | 1 |
| P3 | 2 | 8 | 2 |
| P4 | 3 | 6 | 4 |

Calculate average TAT and WT for:
a) FCFS
b) SJF (Non-preemptive)
c) SRTF
d) Priority (Preemptive, lower number = higher priority)
e) Round Robin (q=2)

---

### Solution (a): FCFS

**Order**: P1 → P2 → P3 → P4

```
| P1 (0-5) | P2 (5-8) | P3 (8-16) | P4 (16-22) |
0          5          8           16           22
```

| Process | CT | TAT | WT |
|---------|-----|-----|-----|
| P1 | 5 | 5 | 0 |
| P2 | 8 | 7 | 4 |
| P3 | 16 | 14 | 6 |
| P4 | 22 | 19 | 13 |

**Avg TAT = 11.25, Avg WT = 5.75**

---

### Solution (b): SJF (Non-Preemptive)

**At t=0**: Only P1 → Run P1 (0-5)
**At t=5**: P2(3), P3(8), P4(6) → Shortest = P2 → Run P2 (5-8)
**At t=8**: P3(8), P4(6) → Shortest = P4 → Run P4 (8-14)
**At t=14**: Only P3 → Run P3 (14-22)

```
| P1 (0-5) | P2 (5-8) | P4 (8-14) | P3 (14-22) |
0          5          8           14           22
```

| Process | CT | TAT | WT |
|---------|-----|-----|-----|
| P1 | 5 | 5 | 0 |
| P2 | 8 | 7 | 4 |
| P3 | 22 | 20 | 12 |
| P4 | 14 | 11 | 5 |

**Avg TAT = 10.75, Avg WT = 5.25**

---

### Solution (c): SRTF

| Time | Event | Running | Remaining |
|------|-------|---------|-----------|
| 0 | P1 arrives | P1 | P1(5) |
| 1 | P2 arrives (3<4) | P2 | P1(4), P2(3) |
| 2 | P3 arrives | P2 | P1(4), P2(2), P3(8) |
| 3 | P4 arrives | P2 | P1(4), P2(1), P3(8), P4(6) |
| 4 | P2 done, P1 shortest | P1 | P1(4), P3(8), P4(6) |
| 8 | P1 done | P4 | P3(8), P4(6) |
| 14 | P4 done | P3 | P3(8) |
| 22 | P3 done | - | - |

```
|P1| P2 (1-4) | P1 (4-8) | P4 (8-14) | P3 (14-22) |
0  1          4          8           14           22
```

| Process | CT | TAT | WT |
|---------|-----|-----|-----|
| P1 | 8 | 8 | 3 |
| P2 | 4 | 3 | 0 |
| P3 | 22 | 20 | 12 |
| P4 | 14 | 11 | 5 |

**Avg TAT = 10.5, Avg WT = 5**

---

### Solution (d): Priority (Preemptive)

Priority: P2(1) > P3(2) > P1(3) > P4(4)

| Time | Event | Running | Ready |
|------|-------|---------|-------|
| 0 | P1(3) arrives | P1 | - |
| 1 | P2(1) arrives, preempts | P2 | P1 |
| 2 | P3(2) arrives | P2 | P1, P3 |
| 3 | P4(4) arrives | P2 | P1, P3, P4 |
| 4 | P2 done | P3 (highest) | P1, P4 |
| 12 | P3 done | P1 | P4 |
| 16 | P1 done | P4 | - |
| 22 | P4 done | - | - |

```
|P1| P2 (1-4) | P3 (4-12) | P1 (12-16) | P4 (16-22) |
0  1          4           12           16           22
```

| Process | CT | TAT | WT |
|---------|-----|-----|-----|
| P1 | 16 | 16 | 11 |
| P2 | 4 | 3 | 0 |
| P3 | 12 | 10 | 2 |
| P4 | 22 | 19 | 13 |

**Avg TAT = 12, Avg WT = 6.5**

---

### Solution (e): Round Robin (q=2)

Queue order: P1 → P2 → P3 → P4 (as they arrive)

| Time | Running | Queue (after execution) |
|------|---------|------------------------|
| 0-2 | P1(5→3) | P2(3) |
| 2-4 | P2(3→1) | P3(8), P1(3) |
| 4-6 | P3(8→6) | P1(3), P4(6), P2(1) |
| 6-8 | P1(3→1) | P4(6), P2(1), P3(6) |
| 8-10 | P4(6→4) | P2(1), P3(6), P1(1) |
| 10-11 | P2(1→0) ✓ | P3(6), P1(1), P4(4) |
| 11-13 | P3(6→4) | P1(1), P4(4), P3(4) |
| 13-14 | P1(1→0) ✓ | P4(4), P3(4) |
| 14-16 | P4(4→2) | P3(4), P4(2) |
| 16-18 | P3(4→2) | P4(2), P3(2) |
| 18-20 | P4(2→0) ✓ | P3(2) |
| 20-22 | P3(2→0) ✓ | - |

```
|P1|P2|P3|P1|P4|P2|P3|P1|P4|P3|P4|P3|
0  2  4  6  8 10 11 13 14 16 18 20 22
```

| Process | CT | TAT | WT |
|---------|-----|-----|-----|
| P1 | 14 | 14 | 9 |
| P2 | 11 | 10 | 7 |
| P3 | 22 | 20 | 12 |
| P4 | 20 | 17 | 11 |

**Avg TAT = 15.25, Avg WT = 9.75**

---

## 📊 Algorithm Comparison

| Algorithm | Avg WT | TAT | Best For |
|-----------|--------|-----|----------|
| FCFS | 5.75 | 11.25 | Simple batch |
| SJF | 5.25 | 10.75 | Non-preemptive optimal |
| SRTF | 5.0 | 10.5 | Preemptive optimal |
| Priority | 6.5 | 12 | Urgent tasks |
| RR (q=2) | 9.75 | 15.25 | Interactive systems |

---

## 🎯 GATE Traps and Anti-Solutions

### Trap 1: Preemption at Arrival
**Wrong**: Only check at quantum end (for RR)
**Right**: SRTF/Priority preempt at EVERY arrival

### Trap 2: Same Priority/Burst
**Wrong**: Random selection
**Right**: FCFS (first arrived gets CPU)

### Trap 3: Response Time in RR
**Wrong**: Response Time = Waiting Time
**Right**: Response Time = Time to FIRST CPU

### Trap 4: Context Switch in RR
**Wrong**: Counting switch after last process
**Right**: No switch needed after completion

### Trap 5: Quantum Boundary
**Wrong**: Process A finishes at t=10, Process B (q=4) runs 10-14
**Right**: Check if new arrivals should preempt (for priority-based)

---

## 🧠 Quick Reference Formulas

### Average Waiting Time
$$\text{Avg WT} = \frac{\sum_{i=1}^{n} WT_i}{n}$$

### CPU Efficiency
$$\text{Efficiency} = \frac{\sum \text{Burst Times}}{\text{Total Time}} \times 100\%$$

### RR Time for n Processes
Worst case for process with burst B:
$$\text{Time} = (n-1) \times q \times \lceil B/q \rceil + B$$

### Throughput
$$\text{Throughput} = \frac{\text{Number of Processes}}{\text{Total Time}}$$

---

## ⚡ The 5-Second Snap-Check

1. **FCFS question?** → Just sum bursts in order
2. **SJF question?** → Pick shortest at decision point
3. **SRTF question?** → Recalculate at EVERY arrival
4. **Priority question?** → Check convention (lower = higher?)
5. **RR question?** → Draw timeline, mark each quantum

---

## 🏆 Chapter Summary

| Algorithm | Type | Optimal? | Starvation? |
|-----------|------|----------|-------------|
| FCFS | Non-preemptive | No | No |
| SJF | Non-preemptive | Yes (non-preemptive) | Yes |
| SRTF | Preemptive | Yes (all algorithms) | Yes |
| Priority | Both | No | Yes |
| RR | Preemptive | No | No |
| MLFQ | Preemptive | No | No (with aging) |

---

*Next Chapter: [Threads →](04-Threads.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
