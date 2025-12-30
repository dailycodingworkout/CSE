# Chapter 3: CPU Scheduling

> **"CPU Scheduling is like a traffic controller deciding which car (process) gets the green light (CPU) next"**

---

## 🎯 Why CPU Scheduling?

**Goal:** Maximize CPU utilization by keeping CPU busy at all times

### CPU-I/O Burst Cycle
```
Process Execution Pattern:
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│CPU Burst│→│I/O Burst│→│CPU Burst│→│I/O Burst│→ ...
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

- **CPU-bound process:** Long CPU bursts, short I/O bursts
- **I/O-bound process:** Short CPU bursts, long I/O bursts

---

## 📊 Scheduling Criteria

| Criterion | Definition | Optimize |
|-----------|------------|----------|
| **CPU Utilization** | % time CPU is busy | Maximize |
| **Throughput** | Processes completed per unit time | Maximize |
| **Turnaround Time** | Total time from submission to completion | Minimize |
| **Waiting Time** | Time spent in ready queue | Minimize |
| **Response Time** | Time from submission to first response | Minimize |

### ⚡ Key Formulas

```
Turnaround Time (TAT) = Completion Time - Arrival Time
                      = Burst Time + Waiting Time

Waiting Time (WT) = Turnaround Time - Burst Time
                  = Completion Time - Arrival Time - Burst Time

Response Time (RT) = First Response Time - Arrival Time

Throughput = Number of processes / Total time

CPU Utilization = (Total Burst Time / Total Time) × 100%
```

---

## 🔄 Preemptive vs Non-Preemptive

| Aspect | Non-Preemptive | Preemptive |
|--------|----------------|------------|
| **Definition** | Process runs until completion/block | CPU can be taken away |
| **Control** | Process holds CPU voluntarily | OS forces context switch |
| **Response Time** | Poor | Better |
| **Overhead** | Less | More (context switches) |
| **Starvation** | Possible | Less likely |
| **Race Conditions** | Rare | Common |
| **Examples** | FCFS, SJF | SRTF, Round Robin |

**💡 GATE Trick:** 
- Non-preemptive = "Polite" (process gives up voluntarily)
- Preemptive = "Aggressive" (OS takes control)

---

## 📚 Scheduling Algorithms

### 1️⃣ First-Come, First-Served (FCFS)

**Rule:** Process that arrives first gets CPU first

**Characteristics:**
- Non-preemptive
- Simple to implement (FIFO queue)
- No starvation
- Poor performance with varying burst times

**🧠 Analogy:** Queue at a bank counter

---

#### FCFS Example

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 24 |
| P2 | 1 | 3 |
| P3 | 2 | 3 |

**Gantt Chart:**
```
| P1 (0-24) | P2 (24-27) | P3 (27-30) |
```

**Calculations:**
```
P1: TAT = 24-0 = 24, WT = 24-24 = 0
P2: TAT = 27-1 = 26, WT = 26-3 = 23
P3: TAT = 30-2 = 28, WT = 28-3 = 25

Avg TAT = (24+26+28)/3 = 26
Avg WT = (0+23+25)/3 = 16
```

---

#### Convoy Effect (FCFS Problem)

```
Long CPU-bound process arrives first:
┌──────────────────────────────────┐
│           P1 (CPU-bound)         │
└──────────────────────────────────┘
                                    ↑
    Short I/O-bound processes wait behind
    P2, P3, P4 (all waiting)
```

**Result:** Short processes wait behind long process → Poor average waiting time

**💡 Solution:** Use SJF or Round Robin

---

### 2️⃣ Shortest Job First (SJF)

**Rule:** Process with shortest burst time gets CPU first

**Characteristics:**
- Can be preemptive or non-preemptive
- Optimal for minimizing average waiting time
- May cause starvation of long processes
- Requires knowing burst time in advance

---

#### SJF (Non-Preemptive) Example

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**Gantt Chart:**
```
| P1 (0-7) | P3 (7-8) | P2 (8-12) | P4 (12-16) |
```

At t=0: Only P1 available, starts P1
At t=7: P2, P3, P4 available. P3 has shortest burst (1), run P3
At t=8: P2, P4 available. P2 chosen (tie-break or equal), run P2
At t=12: Run P4

**Calculations:**
```
P1: TAT = 7-0 = 7,   WT = 0
P2: TAT = 12-2 = 10, WT = 10-4 = 6
P3: TAT = 8-4 = 4,   WT = 4-1 = 3
P4: TAT = 16-5 = 11, WT = 11-4 = 7

Avg TAT = (7+10+4+11)/4 = 8
Avg WT = (0+6+3+7)/4 = 4
```

---

### 3️⃣ Shortest Remaining Time First (SRTF)

**Rule:** Preemptive version of SJF - process with shortest **remaining** time runs

**Characteristics:**
- Preemptive
- Optimal for minimizing average waiting time
- High context switch overhead
- May cause starvation

---

#### SRTF Example

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**Gantt Chart:**
```
| P1 | P2 | P2 | P2 | P2 | P1 | P1 | P1 | P1 | P1 | P1 | P1 | P4 | P4 | P4 | P4 | P4 | P3...
  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
```

**Detailed trace:**
```
t=0: P1 starts (remaining=8)
t=1: P2 arrives (rem=4), P1 (rem=7). 4<7 → preempt P1, run P2
t=2: P3 arrives (rem=9), P2 (rem=3). 3<9 → continue P2
t=3: P4 arrives (rem=5), P2 (rem=2). 2<5 → continue P2
t=5: P2 done. Ready: P1(7), P3(9), P4(5) → run P4? 
     Wait, P1 has 7, P4 has 5. Run P4? No!
     Actually: P1(7), P4(5). 5<7<9 → run P4
     
Let me recalculate:
t=0: P1(8)
t=1: P2(4) arrives. 4<7 → run P2
t=2: P3(9) arrives. P2(3). 3<9 → P2 continues  
t=3: P4(5) arrives. P2(2). 2<5 → P2 continues
t=5: P2 done. P1(7), P3(9), P4(5). 5 shortest → run P4
t=10: P4 done. P1(7), P3(9). 7 shortest → run P1
t=17: P1 done. Run P3
t=26: P3 done
```

**Correct Gantt Chart:**
```
|P1|  P2  |   P4   |    P1    |    P3    |
0  1     5       10        17          26
```

---

### 4️⃣ Round Robin (RR)

**Rule:** Each process gets a fixed time quantum, then preempted

**Characteristics:**
- Preemptive (always after time quantum)
- Fair - no starvation
- Good response time
- Performance depends on time quantum

---

#### Time Quantum Selection

| Time Quantum | Effect |
|--------------|--------|
| Very small | Too many context switches (overhead) |
| Very large | Degenerates to FCFS |
| Optimal | 80% of CPU bursts should be < quantum |

**Rule of thumb:** Context switch time should be < 10% of quantum

---

#### Round Robin Example

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 10 |
| P2 | 1 | 4 |
| P3 | 2 | 5 |

**Time Quantum = 3**

**Gantt Chart:**
```
| P1 | P2 | P3 | P1 | P2 | P3 | P1 | P1 |
0    3    6    9   12   13   15   18   19
```

**Trace:**
```
t=0:  Ready: P1(10). Run P1 for 3 units
t=3:  Ready: P2(4), P3(5), P1(7). Run P2 for 3 units
t=6:  Ready: P3(5), P1(7), P2(1). Run P3 for 3 units
t=9:  Ready: P1(7), P2(1), P3(2). Run P1 for 3 units
t=12: Ready: P2(1), P3(2), P1(4). Run P2 for 1 unit (done)
t=13: Ready: P3(2), P1(4). Run P3 for 2 units (done)
t=15: Ready: P1(4). Run P1 for 3 units
t=18: Ready: P1(1). Run P1 for 1 unit (done)
```

**Calculations:**
```
P1: Completion=19, TAT=19-0=19, WT=19-10=9
P2: Completion=13, TAT=13-1=12, WT=12-4=8
P3: Completion=15, TAT=15-2=13, WT=13-5=8

Avg TAT = (19+12+13)/3 = 14.67
Avg WT = (9+8+8)/3 = 8.33
```

---

### 5️⃣ Priority Scheduling

**Rule:** Process with highest priority runs first

**Characteristics:**
- Can be preemptive or non-preemptive
- Priority can be internal or external
- May cause starvation (low priority processes)

**Priority Assignment:**
- Internal: Based on time limits, memory requirements
- External: Assigned by user/admin

---

#### Priority Scheduling Example

| Process | Arrival Time | Burst Time | Priority |
|---------|--------------|------------|----------|
| P1 | 0 | 10 | 3 |
| P2 | 0 | 1 | 1 |
| P3 | 0 | 2 | 4 |
| P4 | 0 | 1 | 5 |
| P5 | 0 | 5 | 2 |

*(Lower number = Higher priority)*

**Gantt Chart (Non-preemptive):**
```
| P2 | P5 | P1 | P3 | P4 |
0    1    6   16   18   19
```

---

#### Starvation & Aging

**Problem:** Low-priority processes may never execute (indefinite blocking)

**Solution: Aging**
- Gradually increase priority of waiting processes
- Example: Increase priority by 1 every 15 minutes

```
Time 0:   P1(priority=10), P2(priority=1)
Time 15:  P1(priority=9),  P2(priority=1)
Time 30:  P1(priority=8),  P2(priority=1)
...
Time 120: P1(priority=1),  P2(priority=1) → Both equal priority
```

---

### 6️⃣ Multilevel Queue Scheduling

**Rule:** Multiple ready queues with different priorities and algorithms

```
┌─────────────────────────────────────────────────────────┐
│  Highest Priority                                       │
│  ┌────────────────────────────────────────────────┐    │
│  │ Queue 1: System Processes (Priority)           │    │
│  └───────────────────────┬────────────────────────┘    │
│  ┌───────────────────────┴────────────────────────┐    │
│  │ Queue 2: Interactive Processes (RR)            │    │
│  └───────────────────────┬────────────────────────┘    │
│  ┌───────────────────────┴────────────────────────┐    │
│  │ Queue 3: Batch Processes (FCFS)                │    │
│  └────────────────────────────────────────────────┘    │
│  Lowest Priority                                        │
└─────────────────────────────────────────────────────────┘
```

**Characteristics:**
- Process permanently assigned to queue
- Each queue has its own scheduling algorithm
- Must schedule among queues (fixed priority or time-slice)

---

### 7️⃣ Multilevel Feedback Queue (MLFQ)

**Rule:** Processes can move between queues based on behavior

```
Queue 0 (Highest, RR q=8):  ───→ New processes enter here
           │
           ▼ (used full quantum)
Queue 1 (Medium, RR q=16): 
           │
           ▼ (used full quantum)
Queue 2 (Lowest, FCFS):    ───→ CPU-bound processes end here
```

**Movement Rules:**
1. New process → Highest priority queue
2. Process uses full quantum → Move down
3. Process gives up CPU (I/O) → Stay or move up
4. Aging: Move long-waiting processes up

**💡 GATE Insight:** MLFQ separates CPU-bound (sink down) from I/O-bound (stay up) automatically

---

#### MLFQ Example

```
Three queues: Q0 (q=4), Q1 (q=8), Q2 (FCFS)

Process P with burst time 22:
1. P enters Q0, runs for 4 (remaining=18), moves to Q1
2. P runs from Q1 for 8 (remaining=10), moves to Q2
3. P runs from Q2 for 10 (done)

Total time in each queue:
Q0: 4 time units
Q1: 8 time units
Q2: 10 time units
```

---

## 🔄 Algorithm Comparison

| Algorithm | Preemptive? | Starvation? | Optimal Avg WT? |
|-----------|-------------|-------------|-----------------|
| FCFS | No | No | No |
| SJF | No | Yes (long jobs) | Yes (non-preemptive) |
| SRTF | Yes | Yes (long jobs) | Yes (overall) |
| RR | Yes | No | No |
| Priority | Both | Yes | No |
| MLFQ | Yes | No (with aging) | Adaptive |

---

## 🖥️ Multi-Processor Scheduling

### Types of Multiprocessing

| Type | Description |
|------|-------------|
| **Asymmetric (AMP)** | Master CPU schedules, slaves execute |
| **Symmetric (SMP)** | All CPUs self-schedule from common queue |

### Processor Affinity

**Definition:** Keep process on same CPU to use cached data

| Type | Description |
|------|-------------|
| **Soft Affinity** | OS tries but may migrate |
| **Hard Affinity** | Process bound to specific CPU(s) |

### Load Balancing

**Push Migration:** Overloaded CPU pushes tasks to idle CPUs
**Pull Migration:** Idle CPU pulls tasks from busy CPUs

---

## ⏱️ Real-Time Scheduling

### Types of Real-Time Systems

| Type | Deadline | Consequence |
|------|----------|-------------|
| **Hard Real-Time** | Must meet | System failure |
| **Soft Real-Time** | Should meet | Degraded performance |

---

### Rate Monotonic Scheduling (RMS)

**Rule:** Shorter period = Higher priority (static)

**Schedulability Test:**
```
U = Σ(Ci/Ti) ≤ n(2^(1/n) - 1)

where:
  Ci = Execution time of process i
  Ti = Period of process i
  n  = Number of processes
```

**n → ∞:** Upper bound approaches ln(2) ≈ 0.693 ≈ 69.3%

| n | Bound |
|---|-------|
| 1 | 1.000 |
| 2 | 0.828 |
| 3 | 0.779 |
| ∞ | 0.693 |

---

#### RMS Example

| Process | Period (Ti) | Execution (Ci) |
|---------|-------------|----------------|
| P1 | 50 | 20 |
| P2 | 100 | 35 |

**Step 1:** Assign priorities
- P1: T1=50 (shorter) → Higher priority
- P2: T2=100 (longer) → Lower priority

**Step 2:** Check schedulability
```
U = 20/50 + 35/100 = 0.4 + 0.35 = 0.75
Bound for n=2: 2(2^0.5 - 1) = 0.828

0.75 < 0.828 ✓ Schedulable
```

---

### Earliest Deadline First (EDF)

**Rule:** Process closest to deadline gets highest priority (dynamic)

**Schedulability Test:**
```
U = Σ(Ci/Ti) ≤ 1.0
```

**Advantage:** Optimal - if system is schedulable, EDF will schedule it

---

#### EDF Example

| Process | Period | Execution | Deadline |
|---------|--------|-----------|----------|
| P1 | 50 | 25 | 50 |
| P2 | 80 | 35 | 80 |

```
U = 25/50 + 35/80 = 0.5 + 0.4375 = 0.9375 < 1.0 ✓
```

**Timeline:**
```
t=0:  Deadlines: P1@50, P2@80. Run P1 (closer deadline)
t=25: P1 done. Run P2
t=50: P1 arrives (deadline=100), P2 remaining=10 (deadline=80)
      P2 deadline closer → continue P2
t=60: P2 done. Run P1
t=75: P1 done.
t=80: P2 arrives (deadline=160). Run P2
...
```

---

### RMS vs EDF Comparison

| Aspect | RMS | EDF |
|--------|-----|-----|
| Priority | Static | Dynamic |
| Complexity | Simpler | More complex |
| CPU Bound | ~69% max | 100% max |
| Implementation | Easier | Harder |
| Predictability | High | Lower |

---

## ⚙️ Dispatcher

**Dispatcher:** Module that gives control of CPU to selected process

### Dispatcher Functions:
1. Context switch
2. Switch to user mode
3. Jump to proper location in program

### Dispatch Latency
Time between stopping one process and starting another

```
Dispatch Latency = Context switch time + 
                   Scheduler decision time +
                   Process start time
```

---

## 🎯 GATE Numerical Problem Patterns

### Pattern 1: Basic Scheduling
Given arrival times and burst times, calculate:
- Gantt chart
- Average waiting time
- Average turnaround time

### Pattern 2: Quantum Impact
How does changing time quantum affect:
- Number of context switches
- Average response time
- Algorithm behavior

### Pattern 3: Starvation Analysis
Given priority levels, identify:
- Which process starves
- Effect of aging

### Pattern 4: Real-Time Feasibility
Given periods and execution times:
- RMS schedulability check
- EDF schedulability check

---

## ⚠️ Edge Cases & Traps

1. **FCFS with different arrival times:** Sort by arrival, then process
2. **SJF tie-breaking:** Use FCFS among equal burst times
3. **RR remaining time < quantum:** Process completes, doesn't wait for quantum
4. **Priority with same priority:** Use FCFS or round-robin among them
5. **SRTF continuous preemption:** Check at every arrival, not just quantum boundaries
6. **Empty ready queue:** CPU idle time counts in utilization

---

## 🎯 Quick Revision Points

```
✓ TAT = Completion - Arrival
✓ WT = TAT - Burst
✓ FCFS: Simple but convoy effect
✓ SJF/SRTF: Optimal waiting time but starvation
✓ RR: Fair, good response, quantum-dependent
✓ Priority: May starve, use aging
✓ MLFQ: Adaptive, favors I/O-bound
✓ RMS: Static priority, ~69% CPU bound
✓ EDF: Dynamic priority, 100% CPU bound
```

---

## 📚 Master Formula Sheet

```
Turnaround Time = Completion Time - Arrival Time
Waiting Time = Turnaround Time - Burst Time
Response Time = First CPU Time - Arrival Time

CPU Utilization = Σ(Burst Time) / Total Time × 100%
Throughput = Number of processes / Total time

RMS Bound: n(2^(1/n) - 1)
EDF Bound: Σ(Ci/Ti) ≤ 1.0

Context Switches in RR = ceil(Σ Burst Times / Quantum) - Number of complete quantums
```

---

[← Previous: Process Management](./02-Process-Management.md) | [Next: Process Synchronization →](./04-Process-Synchronization.md)
