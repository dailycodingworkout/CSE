# 📖 Chapter 4: CPU Scheduling

> **The Atomic Truth:** CPU Scheduling = Choose which process runs next

---

## 🎯 GATE Syllabus Coverage
- Scheduling Criteria
- Scheduling Algorithms (FCFS, SJF, SRTF, Priority, Round Robin)
- Multi-level Queue Scheduling
- Multi-level Feedback Queue
- Numerical Problems

---

## 4.1 CPU Scheduling Basics

### Why CPU Scheduling?
- Multiprogramming requires selection of next process
- Maximize CPU utilization
- Minimize waiting time for users

### CPU-I/O Burst Cycle

```
┌───────────────────────────────────────────────────┐
│                                                   │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐       │
│  │CPU Burst│───→│I/O Burst│───→│CPU Burst│───→...│
│  │(compute)│    │ (wait)  │    │(compute)│       │
│  └─────────┘    └─────────┘    └─────────┘       │
│                                                   │
└───────────────────────────────────────────────────┘
```

### Process Types

| Type | CPU Burst | I/O Burst | Example |
|------|-----------|-----------|---------|
| **CPU-bound** | Long | Short | Scientific computation |
| **I/O-bound** | Short | Long | Text editor, web browser |

---

## 4.2 Scheduling Criteria

| Criterion | Goal | Optimize |
|-----------|------|----------|
| **CPU Utilization** | Keep CPU busy | Maximize |
| **Throughput** | Processes completed per unit time | Maximize |
| **Turnaround Time** | Total time from submission to completion | Minimize |
| **Waiting Time** | Time spent in ready queue | Minimize |
| **Response Time** | Time from submission to first response | Minimize |

### Key Formulas

$$\boxed{\text{Turnaround Time (TAT)} = \text{Completion Time (CT)} - \text{Arrival Time (AT)}}$$

$$\boxed{\text{Waiting Time (WT)} = \text{Turnaround Time} - \text{Burst Time (BT)}}$$

$$\boxed{\text{Response Time (RT)} = \text{First Response Time} - \text{Arrival Time}}$$

$$\boxed{\text{Throughput} = \frac{\text{Number of Processes}}{\text{Total Time}}}$$

---

## 4.3 Preemptive vs Non-Preemptive Scheduling

| Feature | Non-Preemptive | Preemptive |
|---------|----------------|------------|
| Definition | Process runs until completion or blocks | Process can be interrupted |
| Control | Process controls CPU | Scheduler controls CPU |
| Response Time | Higher | Lower |
| Overhead | Lower | Higher (context switches) |
| Implementation | Simpler | Complex |

**Preemption Points:**
- New process arrives with higher priority
- Running process time quantum expires
- Running process priority drops

---

## 4.4 Scheduling Algorithms

### 4.4.1 First-Come, First-Served (FCFS)

**Concept:** Process that arrives first is served first.

**Properties:**
- Non-preemptive
- Simple to implement
- Convoy Effect (short processes wait for long)

**Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 24 |
| P2 | 0 | 3 |
| P3 | 0 | 3 |

**Gantt Chart:**
```
│    P1      │ P2 │ P3 │
0           24   27   30
```

**Calculations:**

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 24 | 24 | 0 |
| P2 | 27 | 27 | 24 |
| P3 | 30 | 30 | 27 |

$$\text{Average TAT} = \frac{24 + 27 + 30}{3} = 27$$

$$\text{Average WT} = \frac{0 + 24 + 27}{3} = 17$$

**Convoy Effect:** If P2 and P3 came first:
```
│P2│P3│    P1      │
0  3  6           30
```
Average WT = (0 + 3 + 6)/3 = 3 (Much better!)

---

### 4.4.2 Shortest Job First (SJF)

**Concept:** Select process with smallest burst time.

**Properties:**
- Can be preemptive (SRTF) or non-preemptive
- Optimal for minimum average waiting time
- Starvation possible for long processes

#### Non-Preemptive SJF

**Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**Gantt Chart:**
```
│   P1   │P3│  P2  │  P4  │
0        7  8     12     16
```

At t=0: Only P1 available → Run P1
At t=7: P2, P3, P4 available → Shortest is P3 (BT=1)
At t=8: P2, P4 available → Shortest is P2 (BT=4)
At t=12: Only P4 → Run P4

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 7 | 7 | 0 |
| P2 | 12 | 10 | 6 |
| P3 | 8 | 4 | 3 |
| P4 | 16 | 11 | 7 |

Average WT = (0 + 6 + 3 + 7)/4 = 4

---

#### Preemptive SJF (Shortest Remaining Time First - SRTF)

**Concept:** If new process has shorter remaining time, preempt current.

**Same Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**Gantt Chart:**
```
│P1│ P2 │P3│P2│  P4  │   P1   │
0  2   4  5  7     11       16
```

**Step-by-step:**
- t=0: Only P1 available (RT=7). Run P1.
- t=2: P2 arrives (BT=4). P1 remaining=5. 4<5, preempt P1. Run P2.
- t=4: P3 arrives (BT=1). P2 remaining=2. 1<2, preempt P2. Run P3.
- t=5: P3 completes. P4 arrives (BT=4). P1 remaining=5, P2 remaining=2. Run P2 (smallest=2).
- t=7: P2 completes. P1 remaining=5, P4 remaining=4. Run P4 (4<5).
- t=11: P4 completes. Run P1.
- t=16: P1 completes.

**Correct Gantt Chart:**
```
│P1│P2│P3│P2│  P4  │   P1   │
0  2  4  5  7     11       16
```

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 16 | 16 | 9 |
| P2 | 7 | 5 | 1 |
| P3 | 5 | 1 | 0 |
| P4 | 11 | 6 | 2 |

Average WT = (9 + 1 + 0 + 2)/4 = 3

**Note:** SRTF gives better average WT than non-preemptive SJF!

---

### 4.4.3 Priority Scheduling

**Concept:** Each process assigned a priority; highest priority runs first.

**Properties:**
- Can be preemptive or non-preemptive
- Priority can be static or dynamic
- Starvation possible (low priority never runs)
- Solution: **Aging** (increase priority over time)

**Convention:**
- Lower number = Higher priority (usually)
- GATE always specifies which convention

**Example (Non-Preemptive, Lower number = Higher priority):**

| Process | AT | BT | Priority |
|---------|----|----|----------|
| P1 | 0 | 10 | 3 |
| P2 | 0 | 1 | 1 |
| P3 | 0 | 2 | 4 |
| P4 | 0 | 1 | 5 |
| P5 | 0 | 5 | 2 |

**Gantt Chart:**
```
│P2│    P5   │    P1     │P3│P4│
0  1        6          16 18 19
```

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 16 | 16 | 6 |
| P2 | 1 | 1 | 0 |
| P3 | 18 | 18 | 16 |
| P4 | 19 | 19 | 18 |
| P5 | 6 | 6 | 1 |

---

### 4.4.4 Round Robin (RR)

**Concept:** Each process gets a fixed time quantum; after which it's preempted.

**Properties:**
- Preemptive
- Fair allocation
- Performance depends on time quantum
- No starvation

**Time Quantum Selection:**
- Too large → FCFS behavior
- Too small → Too many context switches

**Rule of Thumb:** 80% of CPU bursts should be smaller than quantum

**Example (Time Quantum = 4):**

| Process | AT | BT |
|---------|----|----|
| P1 | 0 | 24 |
| P2 | 0 | 3 |
| P3 | 0 | 3 |

**Gantt Chart:**
```
│P1│P2│P3│P1│P1│P1│P1│P1│
0  4  7 10 14 18 22 26 30
```

**Step-by-step:**
- t=0-4: P1 runs (remaining=20)
- t=4-7: P2 runs, completes (3<4)
- t=7-10: P3 runs, completes (3<4)
- t=10-30: P1 runs 5 more quantums (20/4=5)

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 30 | 30 | 6 |
| P2 | 7 | 7 | 4 |
| P3 | 10 | 10 | 7 |

Average WT = (6 + 4 + 7)/3 = 5.67

**Context Switches:** At t=4, 7, 10, 14, 18, 22, 26 = 7 switches

---

### 4.4.5 Algorithm Comparison

| Algorithm | Preemptive | Optimal? | Starvation | Overhead |
|-----------|------------|----------|------------|----------|
| FCFS | No | No | No | Low |
| SJF | No | Yes (for NP) | Yes | Low |
| SRTF | Yes | Yes | Yes | Medium |
| Priority | Both | No | Yes | Low |
| RR | Yes | No | No | High |

---

## 4.5 Multi-Level Queue Scheduling

**Concept:** Ready queue partitioned into separate queues with different priorities.

```
                           ┌───────────────────┐
                           │   System Queue    │ Priority 0
                           │  (Highest Prio)   │
                           └────────┬──────────┘
                                    │
                           ┌────────┴──────────┐
                           │ Interactive Queue │ Priority 1
                           └────────┬──────────┘
                                    │
                           ┌────────┴──────────┐
                           │   Batch Queue     │ Priority 2
                           └────────┬──────────┘
                                    │
                           ┌────────┴──────────┐
                           │  Student Queue    │ Priority 3
                           │ (Lowest Priority) │
                           └────────┬──────────┘
                                    │
                                    ↓
                                  [CPU]
```

**Characteristics:**
- Processes permanently assigned to queue
- Each queue can have its own scheduling algorithm
- Inter-queue scheduling typically preemptive priority

---

## 4.6 Multi-Level Feedback Queue (MLFQ)

**Concept:** Processes can move between queues based on behavior.

```
Queue 0 (RR, TQ=8)    ┌────┬────┬────┐
   Highest Priority   │ P1 │ P2 │    │──→ If not finished, move down
                      └────┴────┴────┘
                            ↓
Queue 1 (RR, TQ=16)   ┌────┬────┬────┐
   Medium Priority    │ P3 │ P4 │    │──→ If not finished, move down
                      └────┴────┴────┘
                            ↓
Queue 2 (FCFS)        ┌────┬────┬────┐
   Lowest Priority    │ P5 │ P6 │ P7 │──→ Run to completion
                      └────┴────┴────┘
```

**Rules:**
1. New process enters highest priority queue
2. If process uses entire time quantum, move to lower queue
3. If process gives up CPU (I/O), stay in same queue or move up
4. If process waits too long in lower queue, move up (aging)

**Parameters to Define MLFQ:**
- Number of queues
- Scheduling algorithm for each queue
- Method to upgrade/demote processes
- Method to determine initial queue

**Advantage:** Separates I/O-bound (stay up) from CPU-bound (move down)

---

## 4.7 Advanced Topics

### 4.7.1 Completely Fair Scheduler (CFS) - Linux

**Concept:** Based on virtual runtime (vruntime); process with smallest vruntime runs.

$$\text{vruntime} += \text{actual runtime} \times \frac{\text{nice 0 weight}}{\text{process weight}}$$

### 4.7.2 Real-Time Scheduling

**Hard Real-Time:** Must meet deadlines
**Soft Real-Time:** Preferably meet deadlines

**Rate Monotonic Scheduling (RMS):**
- Fixed priority
- Shorter period = Higher priority
- Schedulability: $\sum_{i=1}^{n} \frac{C_i}{T_i} \leq n(2^{1/n} - 1)$

**Earliest Deadline First (EDF):**
- Dynamic priority
- Earlier deadline = Higher priority
- Schedulability: $\sum_{i=1}^{n} \frac{C_i}{T_i} \leq 1$

---

## 4.8 Numerical Problem Solving Strategies

### Strategy 1: Create Timeline
Always draw Gantt chart for visual clarity.

### Strategy 2: Track Remaining Time
For preemptive algorithms, track remaining burst time.

### Strategy 3: Table Method

| Process | AT | BT | CT | TAT | WT | RT |
|---------|----|----|----|----|----|----|
| ... | ... | ... | ... | ... | ... | ... |

### Strategy 4: Formula Verification
- TAT = CT - AT (always positive)
- WT = TAT - BT (always ≥ 0)
- RT ≤ WT (response time ≤ waiting time)

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2018)
**Q:** Consider the following processes:

| Process | AT | BT |
|---------|----|----|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 3 |

Using SRTF, what is the average waiting time?

**Solution:**

```
│P1│  P2  │  P3  │  P1   │
0  1     4      7      11
```

- t=0: P1 runs (RT=5)
- t=1: P2 arrives (BT=3), P1 RT=4. 3<4, preempt.
- t=4: P2 done. P3 RT=1 (arrived at 2, waited), P1 RT=4. 1<4. Run P3? Wait, let me recalculate.
  
Actually:
- t=1: P2 arrives (BT=3<4). Run P2.
- t=2: P3 arrives (BT=3). P2 RT=2. 3>2. Continue P2.
- t=4: P2 done. P3 BT=3, P1 RT=4. 3<4. Run P3.
- t=7: P3 done. Run P1.
- t=11: P1 done.

```
│P1│  P2  │  P3  │   P1   │
0  1     4      7       11
```

| Process | CT | TAT | WT |
|---------|----|----|-----|
| P1 | 11 | 11 | 6 |
| P2 | 4 | 3 | 0 |
| P3 | 7 | 5 | 2 |

Average WT = (6 + 0 + 2)/3 = **8/3 = 2.67**

---

### Question 2 (GATE 2017)
**Q:** Round Robin with TQ=2. What is the order of completion?

| Process | AT | BT |
|---------|----|----|
| P1 | 0 | 4 |
| P2 | 1 | 3 |
| P3 | 2 | 1 |

**Solution:**

```
│P1│P2│P3│P1│P2│
0  2  4  5  7  8
```

- t=0-2: P1 (RT=2)
- t=2-4: P2 (RT=1)
- t=4-5: P3 (RT=0, done)
- t=5-7: P1 (RT=0, done)
- t=7-8: P2 (RT=0, done)

**Completion Order:** P3, P1, P2

---

### Question 3 (GATE 2019)
**Q:** Which scheduling algorithm can result in starvation?
(a) FCFS
(b) Round Robin
(c) Priority (without aging)
(d) None

**Answer:** (c) Priority without aging

---

## 🧠 Memory Tricks

### Mnemonic: "FCFS SJF Priority RR" = "Fat Cats Sleep Peacefully, Rest Running"
- **F**at = FCFS (First Come)
- **C**ats = Convoy effect
- **S**leep = SJF (Shortest)
- **P**eacefully = Priority
- **R**est = Round Robin

### The Mental Slider: Time Quantum
Imagine a **water tap**:
- Wide open (large TQ) = Water flows continuously = FCFS-like
- Partially open (optimal TQ) = Balanced flow
- Barely open (tiny TQ) = Droplets = Context switch overhead

### Quick Comparison Trick
- Need **optimal** average WT? → SJF/SRTF
- Need **fairness**? → Round Robin
- Need **priority**? → Priority Scheduling
- Need **simple**? → FCFS

---

## ⚠️ Common GATE Traps

### Trap 1: Arrival Time = 0
**Wrong:** Forgetting to consider AT in calculations
**Right:** Always use TAT = CT - AT, not just CT

### Trap 2: SRTF Preemption
**Wrong:** Preempting only when new process arrives
**Right:** Check remaining time of current vs new process

### Trap 3: RR with I/O
**Wrong:** Process returning from I/O goes to end of queue
**Right:** Check problem statement (usually goes to end, but verify)

### Trap 4: Priority Convention
**Wrong:** Assuming lower number = higher priority
**Right:** Always check problem statement for convention

---

## 🛠️ Problem-Solving Techniques

### Technique 1: The Table Method (Universal Approach)

**Step-by-step framework for ANY scheduling problem:**

```
Step 1: Create a master table
┌─────────┬────┬────┬────┬─────┬────┬────┐
│ Process │ AT │ BT │ CT │ TAT │ WT │ RT │
├─────────┼────┼────┼────┼─────┼────┼────┤
│   P1    │    │    │    │     │    │    │
│   P2    │    │    │    │     │    │    │
└─────────┴────┴────┴────┴─────┴────┴────┘

Step 2: Draw Gantt chart based on algorithm
Step 3: Fill CT from Gantt chart
Step 4: Calculate TAT = CT - AT
Step 5: Calculate WT = TAT - BT
Step 6: Calculate RT = First Response - AT
Step 7: Compute averages
```

### Technique 2: Timeline Tracking (For Preemptive Algorithms)

**For SRTF/Preemptive Priority:**

```
Create a timeline with events:
Time │ Event           │ Ready Queue (Remaining BT) │ Running
─────┼─────────────────┼───────────────────────────┼─────────
  0  │ P1 arrives      │ P1(7)                      │ P1
  2  │ P2 arrives      │ P1(5), P2(4)               │ P2 ← P2 has less RT
  4  │ P3 arrives      │ P1(5), P2(2), P3(1)        │ P3 ← P3 has least RT
  5  │ P3 completes    │ P1(5), P2(2)               │ P2
  ...
```

**Key:** At each arrival/completion, re-evaluate who runs.

### Technique 3: Round Robin Quick Method

**Shortcut for RR problems:**

1. **List all processes with remaining burst times**
2. **Cycle through queue, subtract TQ (or remaining BT if < TQ)**
3. **Track when each process finishes**

**Quick formula for number of context switches:**
$$\text{Context Switches} = \sum_{i} \lceil \frac{BT_i}{TQ} \rceil - 1 + \text{new arrivals during execution}$$

### Technique 4: FCFS Convoy Effect Detection

**Quick check:** If a long burst time process arrives first, followed by short ones → Convoy effect → High average WT.

**Comparison trick:** Calculate WT for original order vs sorted order (shortest first).

### Technique 5: Gantt Chart Construction Rules

| Algorithm | Gantt Chart Rule |
|-----------|------------------|
| FCFS | Order of arrival |
| SJF | At decision point, pick shortest BT among arrived |
| SRTF | At each arrival, compare remaining times |
| Priority | At decision point, pick highest priority among arrived |
| RR | Cyclic, each gets TQ or remaining (whichever is less) |

### Technique 6: The "Decision Point" Method

**For non-preemptive algorithms:**
1. Decision points occur when a process **completes**
2. At each decision point, look at ready queue
3. Apply algorithm rule to select next process

**For preemptive algorithms:**
1. Decision points occur at **arrivals** AND **completions**
2. At each point, compare with currently running process
3. Preempt if necessary

### Technique 7: Verification Checklist

After solving, verify:
- [ ] TAT is always positive (CT > AT)
- [ ] WT ≥ 0 for all processes
- [ ] RT ≤ WT (response comes before completion)
- [ ] Sum of all time in Gantt = last completion time
- [ ] No idle time unless no process is ready

### Technique 8: MLFQ Solving Strategy

```
Track for each process:
1. Current queue level
2. Remaining burst time
3. Time spent in current quantum

Rules to apply:
- New process → Queue 0
- Uses full TQ without completing → Demote
- Gives up CPU (I/O or done) → Stay or promote
```

---

## 📝 Practice Problems

### Problem 1
| Process | AT | BT |
|---------|----|----|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 2 |
| P4 | 3 | 1 |

Calculate average waiting time for: FCFS, SJF (non-preemptive), SRTF

### Problem 2
RR with TQ=3:
| Process | AT | BT |
|---------|----|----|
| P1 | 0 | 10 |
| P2 | 3 | 6 |
| P3 | 7 | 2 |

Calculate: Average TAT, Average WT, Number of context switches

### Problem 3
MLFQ with:
- Q0: RR, TQ=4
- Q1: RR, TQ=8
- Q2: FCFS

Process P1 has BT=20. Show queue transitions and total time.

---

## 🔗 Quick Reference

| Algorithm | Key Property | Formula/Note |
|-----------|--------------|--------------|
| FCFS | First arrived | Convoy effect |
| SJF | Shortest burst | Optimal avg WT (NP) |
| SRTF | Shortest remaining | Preemptive SJF |
| Priority | Based on priority | Aging prevents starvation |
| RR | Time quantum | Fair, context switch overhead |
| MLFQ | Dynamic queues | Separates I/O and CPU bound |

### Key Formulas
$$\text{TAT} = \text{CT} - \text{AT}$$
$$\text{WT} = \text{TAT} - \text{BT}$$
$$\text{RT} = \text{First Response} - \text{AT}$$

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 5 - Process Synchronization](../05-Process-Synchronization/README.md)*
