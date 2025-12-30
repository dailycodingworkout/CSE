# 🚀 Operating Systems Quick Reference (Cheat Sheet)

> **One-page summary for last-minute revision before GATE/ESE exam**

---

## 📋 Process Management

```
PROCESS STATES: New → Ready → Running → Waiting → Terminated
CONTEXT SWITCH: Save PCB(P1) → Load PCB(P2)

fork() returns:
  • 0 to child
  • Child PID to parent  
  • -1 on error

n fork() calls = 2^n processes
```

---

## ⏱️ CPU Scheduling Formulas

```
TAT = Completion Time - Arrival Time
WT = TAT - Burst Time = Completion - Arrival - Burst
Response Time = First CPU Time - Arrival Time

| Algorithm | Preemptive? | Starvation? |
|-----------|-------------|-------------|
| FCFS      | No          | No          |
| SJF       | No          | Yes         |
| SRTF      | Yes         | Yes         |
| RR        | Yes         | No          |
| Priority  | Both        | Yes         |
```

---

## 🔒 Synchronization

```
Peterson's: flag[i] = true; turn = j; while(flag[j] && turn==j);

Semaphore Operations:
  wait(S) / P(S) / down(S): S--; if S<0 → block
  signal(S) / V(S) / up(S): S++; if S≤0 → wakeup

Producer-Consumer:
  mutex=1, empty=n, full=0
  Producer: wait(empty) → wait(mutex) → produce → signal(mutex) → signal(full)
  Consumer: wait(full) → wait(mutex) → consume → signal(mutex) → signal(empty)
```

---

## 💀 Deadlock

```
4 Conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait

Banker's Algorithm:
  Need = Max - Allocation
  Safe if: ∃ sequence where each process can complete

Minimum resources to prevent deadlock: n(R-1) + 1
  where n = processes, R = max need per process
```

---

## 📦 Memory Management

```
Logical Address → MMU → Physical Address

Page Table Entry: Valid | Ref | Modify | Protection | Frame#

Address Translation:
  Page# = LogicalAddr / PageSize
  Offset = LogicalAddr % PageSize
  PhysicalAddr = (FrameNumber × PageSize) + Offset

EAT = α(TLB + Mem) + (1-α)(TLB + 2×Mem)
    ≈ m(2-α) when TLB time ≈ 0
```

---

## 🔄 Virtual Memory

```
EAT = (1-p)×m + p×(page_fault_time)

Page Replacement Algorithms:
| FIFO    | Oldest page out          | Belady's anomaly possible |
| OPT     | Furthest future use      | Theoretical best          |
| LRU     | Longest since last use   | Practical best            |

FIFO: Simple queue, doesn't consider usage
LRU: Looks BACKWARD in time
OPT: Looks FORWARD in time (impossible to implement)
```

---

## 📁 File Systems

```
UNIX inode: 12 direct + 1 single + 1 double + 1 triple indirect

Max file size (B=block size, P=pointer size):
  Direct: 12 × B
  Single: (B/P) × B
  Double: (B/P)² × B
  Triple: (B/P)³ × B

Allocation Methods:
  Contiguous: Fast but external fragmentation
  Linked: No fragmentation but slow random access
  Indexed: Good random access but overhead
```

---

## 💽 Disk Scheduling

```
Access Time = Seek + Rotational Latency + Transfer
Avg Rotational Latency = (60/RPM)/2 seconds

| FCFS   | Arrival order        | Fair, slow           |
| SSTF   | Nearest request      | Fast, starves        |
| SCAN   | Elevator, go to end  | No starvation        |
| LOOK   | Elevator, last req   | Better than SCAN     |
| C-SCAN | One direction only   | Uniform wait         |

RAID:
  0 = Striping (fast, no redundancy)
  1 = Mirroring (50% capacity)
  5 = Distributed parity (n-1 capacity)
  6 = Double parity (n-2 capacity)
```

---

## 🔐 Protection & Security

```
Access Matrix: Rows = Domains, Columns = Objects, Cells = Rights

ACL: Stored with object (who can access this?)
Capability: Stored with subject (what can I access?)

CIA Triad: Confidentiality, Integrity, Availability

Password: Store as hash(password + salt)

Bell-LaPadula: No read up, No write down (confidentiality)
Biba: No read down, No write up (integrity)
```

---

## 🔢 Important Numbers

```
Context switch overhead: ~1-1000 μs
Disk access time: ~5-15 ms
Page fault penalty: ~3-8 ms
TLB hit: ~10-100 ns
Memory access: ~100 ns
Cache access: ~1-10 ns
Register access: <1 ns

RAID 5 min disks: 3
RAID 6 min disks: 4
RMS CPU bound (n→∞): 69.3%
```

---

## ⚠️ Common GATE Traps

```
1. fork() in loop: 2^n processes for n iterations
2. fork() || fork(): 3 processes (short-circuit)
3. fork() && fork(): 3 processes (short-circuit)
4. Semaphore signal() always increments (unlike condition variable)
5. LRU ≠ FIFO: LRU updates on access, FIFO doesn't
6. Safe ≠ Deadlock-free: Safe guarantees no deadlock; unsafe means might deadlock
7. Cycle in RAG with multi-instance: Not necessarily deadlock
8. Page table size: Include all entries, not just valid ones
9. LOOK vs SCAN: LOOK doesn't go to disk end
10. inode doesn't contain filename (directory does)
```

---

## 📊 Quick Decision Chart

```
Scheduling algorithm for...
  - Fairness: RR or FCFS
  - Min avg wait: SJF/SRTF
  - Real-time: RMS or EDF
  - Interactive: MLFQ

Memory allocation for...
  - Simple: First Fit
  - Min fragmentation: Best Fit
  - Fast: First Fit

Page replacement for...
  - Simplicity: FIFO
  - Performance: LRU approximation
  - Benchmark: Optimal
```

---

*Good luck on your exam! 🎯*
