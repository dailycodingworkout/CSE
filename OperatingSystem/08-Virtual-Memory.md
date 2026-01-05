# Chapter 8: Virtual Memory

## 🎯 The Atomic Truth
> **Virtual Memory = Run Programs Larger Than Physical Memory**

---

## 🧠 The WHY of Virtual Memory

### The Problem
- Programs can be larger than physical memory
- Not all code/data needed at once
- Multiple programs compete for memory

### The Solution
```
VIRTUAL MEMORY INSIGHT:

"Load only what's needed, when it's needed"

┌─────────────────────────────────────────────────────────────┐
│  ENTIRE PROGRAM (100 GB game)                                │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────────────┐  │
│  │ P0  │ P1  │ P2  │ P3  │ P4  │ ... │ Pn  │   Huge!     │  │
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────────────┘  │
│                                                              │
│  WHAT'S IN RAM (8 GB):                                       │
│  ┌─────┬─────┬─────┬─────┐                                   │
│  │ P0  │ P3  │ P7  │ P12 │ ← Only active pages               │
│  └─────┴─────┴─────┴─────┘                                   │
│                                                              │
│  REST ON DISK (Swap Space):                                  │
│  ┌─────┬─────┬─────┬─────┬─────────────────────────────────┐│
│  │ P1  │ P2  │ P4  │ P5  │ ... (loaded when needed)        ││
│  └─────┴─────┴─────┴─────┴─────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## 📄 Demand Paging

### The Idea
> **Load page only when accessed (demanded)**

**Lazy Loading**: Don't load everything at start. Load on first access.

### How It Works

```
DEMAND PAGING FLOW:

1. CPU generates address for page P
         ↓
2. Check page table: Is valid bit = 1?
         ↓
    ┌────┴────┐
    ↓         ↓
  YES        NO
    ↓         ↓
  Access   PAGE FAULT!
  Memory      ↓
           3. Trap to OS
              ↓
           4. Find page on disk
              ↓
           5. Load into free frame
              ↓
           6. Update page table (valid=1)
              ↓
           7. Restart instruction
```

### Page Fault Handling (Detailed)

```
PAGE FAULT SEQUENCE:

┌─────────────────────────────────────────────────────────────┐
│ 1. Reference to page not in memory                          │
│         ↓                                                   │
│ 2. Trap to OS (page fault exception)                        │
│         ↓                                                   │
│ 3. Save process state                                       │
│         ↓                                                   │
│ 4. Is reference valid? (within address space?)              │
│         ↓                                                   │
│    ┌────┴────┐                                              │
│  INVALID    VALID                                           │
│    ↓          ↓                                             │
│  Terminate  5. Find free frame                              │
│  Process       ↓                                            │
│             6. Schedule disk read                           │
│                ↓                                            │
│             7. Wait for I/O (process blocked)               │
│                ↓                                            │
│             8. Update page table (frame#, valid=1)          │
│                ↓                                            │
│             9. Move process to ready queue                  │
│                ↓                                            │
│            10. Restart faulting instruction                 │
└─────────────────────────────────────────────────────────────┘
```

### Page Table with Valid Bit

```
PAGE TABLE:
┌─────────────┬───────────────┬───────────────┐
│ Page Number │ Frame Number  │ Valid/Invalid │
├─────────────┼───────────────┼───────────────┤
│     0       │      5        │      1        │ ← In memory
│     1       │      -        │      0        │ ← On disk
│     2       │      3        │      1        │ ← In memory
│     3       │      -        │      0        │ ← On disk
│     4       │      7        │      1        │ ← In memory
└─────────────┴───────────────┴───────────────┘

Valid = 1: Page in memory
Valid = 0: Page fault will occur
```

---

## ⏱️ Performance of Demand Paging

### Effective Access Time

Let:
- $p$ = Page fault rate (0 ≤ p ≤ 1)
- $ma$ = Memory access time
- $pft$ = Page fault time (disk I/O)

$$EAT = (1-p) \times ma + p \times pft$$

### Page Fault Time Components

| Component | Time |
|-----------|------|
| Trap to OS | ~1 μs |
| Save state | ~1 μs |
| Determine fault | ~1 μs |
| Disk seek + read | ~8-10 ms |
| Restart process | ~1 μs |
| **Total** | **~8-10 ms** |

**GATE Insight**: Disk I/O dominates. Page fault is ~10,000× slower than memory access!

### Example Calculation

**Given**:
- Memory access: 100 ns
- Page fault: 10 ms = 10,000,000 ns
- Desired slowdown: < 10%

**Find**: Required page fault rate

**Solution**:
$$EAT < 1.1 \times 100 = 110 \text{ ns}$$
$$100 \times (1-p) + 10,000,000 \times p < 110$$
$$100 + 9,999,900 \times p < 110$$
$$p < \frac{10}{9,999,900} \approx 10^{-6}$$

**One page fault per million accesses!**

---

## 🔄 Page Replacement

### The Problem
All frames occupied. Need to bring in new page.

### Solution
Remove (replace) an existing page.

### Page Replacement Algorithm

```
PAGE REPLACEMENT:

1. Page fault occurs
2. Find victim page
3. If dirty (modified): Write to disk
4. Load new page into frame
5. Update page tables
6. Restart instruction
```

### Victim Selection: The Key Question

> **Which page to replace?**

Goal: Minimize future page faults.

---

## 📊 Page Replacement Algorithms

### Reference String

A sequence of page references used to test algorithms.

**Example**: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

---

## 1️⃣ FIFO (First-In, First-Out)

### The Idea
> **Replace the oldest page**

### Example (3 frames)
Reference: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

```
Page  | Frames        | Fault?
──────┼───────────────┼────────
  7   | 7 - -         | F
  0   | 7 0 -         | F
  1   | 7 0 1         | F
  2   | 2 0 1         | F (replace 7, oldest)
  0   | 2 0 1         | 
  3   | 2 3 1         | F (replace 0)
  0   | 2 3 0         | F (replace 1)
  4   | 4 3 0         | F (replace 2)
  2   | 4 2 0         | F (replace 3)
  3   | 4 2 3         | F (replace 0)
  0   | 0 2 3         | F (replace 4)
  3   | 0 2 3         | 
  2   | 0 2 3         | 
  1   | 1 2 3         | F (replace 0)
  2   | 1 2 3         | 
  0   | 0 2 3         | F (replace 1)
  1   | 0 1 3         | F (replace 2)
  7   | 0 1 7         | F (replace 3)
  0   | 0 1 7         | 
  1   | 0 1 7         | 

Total Page Faults = 15
```

### Belady's Anomaly

**FIFO ONLY**: More frames can cause MORE page faults!

**Example**: Reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

| Frames | Page Faults |
|--------|-------------|
| 3 | 9 |
| 4 | 10 ← More faults! |

**GATE Trap**: Only FIFO has Belady's anomaly. LRU and Optimal don't.

---

## 2️⃣ Optimal (OPT/MIN)

### The Idea
> **Replace the page that won't be used for longest time**

### Example (3 frames)
Reference: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

```
Page  | Frames        | Fault?
──────┼───────────────┼────────
  7   | 7 - -         | F
  0   | 7 0 -         | F
  1   | 7 0 1         | F
  2   | 2 0 1         | F (replace 7, used farthest at position 18)
  0   | 2 0 1         | 
  3   | 2 0 3         | F (replace 1, used at 14 vs 2 at 9, 0 at 6)
  0   | 2 0 3         | 
  4   | 2 4 3         | F (replace 0, look ahead...)
  2   | 2 4 3         | 
  3   | 2 4 3         | 
  0   | 2 0 3         | F
  3   | 2 0 3         | 
  2   | 2 0 3         | 
  1   | 2 0 1         | F (replace 3)
  2   | 2 0 1         | 
  0   | 2 0 1         | 
  1   | 2 0 1         | 
  7   | 7 0 1         | F (replace 2)
  0   | 7 0 1         | 
  1   | 7 0 1         | 

Total Page Faults = 9
```

### Why It's Called "Optimal"
- **Provably minimum** page faults
- **Impossible to implement** (requires future knowledge)
- Used as **benchmark** for other algorithms

---

## 3️⃣ LRU (Least Recently Used)

### The Idea
> **Replace the page not used for longest time (past)**

**Approximation of Optimal using past as predictor of future.**

### Example (3 frames)
Reference: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

```
Page  | Frames (recent→old) | Fault?
──────┼─────────────────────┼────────
  7   | 7 - -               | F
  0   | 0 7 -               | F
  1   | 1 0 7               | F
  2   | 2 1 0               | F (replace 7, LRU)
  0   | 0 2 1               | 
  3   | 3 0 2               | F (replace 1)
  0   | 0 3 2               | 
  4   | 4 0 3               | F (replace 2)
  2   | 2 4 0               | F (replace 3)
  3   | 3 2 4               | F (replace 0)
  0   | 0 3 2               | F (replace 4)
  3   | 3 0 2               | 
  2   | 2 3 0               | 
  1   | 1 2 3               | F (replace 0)
  2   | 2 1 3               | 
  0   | 0 2 1               | F (replace 3)
  1   | 1 0 2               | 
  7   | 7 1 0               | F (replace 2)
  0   | 0 7 1               | 
  1   | 1 0 7               | 

Total Page Faults = 12
```

### LRU Implementation

#### Method 1: Counter
- Each PTE has timestamp
- On access, update timestamp
- Replace smallest timestamp
- **Problem**: Search overhead

#### Method 2: Stack
- Keep pages in access-order stack
- On access, move to top
- Replace from bottom
- **Problem**: Stack manipulation overhead

#### Method 3: Reference Bits (Approximation)
- Hardware sets reference bit on access
- Periodically clear bits
- Replace page with bit = 0

---

## 4️⃣ LRU Approximations

### Second Chance (Clock) Algorithm

**Circular queue with reference bits.**

```
CLOCK ALGORITHM:

        ┌───┐
    ┌───│ 0 │───┐
    │   └───┘   │         Reference Bit = 0: Replace
   ┌┴──┐     ┌──┴┐        Reference Bit = 1: Clear to 0, move on
   │ 1 │     │ 1 │
   └┬──┘     └──┬┘
    │   ┌───┐   │
    └───│ 0 │───┘
        └───┘
          ↑
        Clock
         Hand

If frame's ref bit = 1: Set to 0, advance
If frame's ref bit = 0: Replace this frame
```

### Enhanced Second Chance

Use (reference bit, modify bit) pair:

| (R, M) | Priority | Action |
|--------|----------|--------|
| (0, 0) | 1 (best) | Not used, not modified |
| (0, 1) | 2 | Not used, modified (need write) |
| (1, 0) | 3 | Used, not modified |
| (1, 1) | 4 (worst) | Used, modified |

---

## 5️⃣ Counting-Based Algorithms

### LFU (Least Frequently Used)
Replace page with smallest access count.

**Problem**: Old pages accumulate high counts.

### MFU (Most Frequently Used)
Replace page with highest count.

**Logic**: High count = already used extensively.

---

## 📊 Algorithm Comparison

| Algorithm | Page Faults | Complexity | Belady's Anomaly? |
|-----------|-------------|------------|-------------------|
| **FIFO** | 15 | O(1) | Yes |
| **Optimal** | 9 | - (impractical) | No |
| **LRU** | 12 | O(n) or special hardware | No |
| **Clock** | ~LRU | O(1) | No |

**GATE Key**: LRU ≤ Optimal always. FIFO can be worse than LRU.

---

## 📦 Frame Allocation

### How Many Frames Per Process?

**Minimum**: Enough to hold any single instruction's references

**Maximum**: All available frames

### Allocation Strategies

#### 1. Equal Allocation
$$frames_i = \frac{total\_frames}{number\_of\_processes}$$

#### 2. Proportional Allocation
$$frames_i = \frac{size_i}{\sum size_j} \times total\_frames$$

**Example**: 
- Total frames = 64
- Process A = 10KB, Process B = 127KB
- A gets: (10/137) × 64 ≈ 5 frames
- B gets: (127/137) × 64 ≈ 59 frames

### Global vs Local Replacement

| Type | Victim Selection | Effect |
|------|------------------|--------|
| **Global** | Any process's frame | One process can steal from another |
| **Local** | Own frames only | Isolated, predictable |

---

## 💀 Thrashing

### The Problem

**When process doesn't have enough frames:**

```
THRASHING SPIRAL:

Low Frames → More Page Faults → More Disk I/O
     ↑                                  ↓
     └──── CPU Idle ←── Waiting for I/O
     
OS sees low CPU → Adds more processes → Even fewer frames per process!
```

### Thrashing Definition

> **Thrashing**: Process spends more time paging than executing.

### Thrashing Graph

```
CPU Utilization
     │
     │        ┌──── Peak
     │       /│\
     │      / │ \
     │     /  │  \
     │    /   │   \_________ Thrashing
     │   /    │
     │  /     │
     │_/______|________________ Degree of Multiprogramming
              │
         Optimal point
```

### Solution: Working Set Model

**Working Set**: Set of pages referenced in last Δ time units.

$$WS_i(t, \Delta) = \text{pages referenced in } [t - \Delta, t]$$

**Total Demand**: $D = \sum WS_i$

**If D > Available Frames**: Thrashing will occur.

**Solution**: 
- If D > m: Suspend some process
- Allocate frames ≈ working set size

---

## 🧮 GATE Numerical Examples

### Example 1: Page Fault Rate

**Given**:
- Reference: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
- 3 frames, FIFO

**Find**: Page faults

| Ref | Frames | Fault |
|-----|--------|-------|
| 1 | 1 - - | F |
| 2 | 1 2 - | F |
| 3 | 1 2 3 | F |
| 4 | 4 2 3 | F |
| 1 | 4 1 3 | F |
| 2 | 4 1 2 | F |
| 5 | 5 1 2 | F |
| 1 | 5 1 2 | |
| 2 | 5 1 2 | |
| 3 | 3 1 2 | F |
| 4 | 3 4 2 | F |
| 5 | 3 4 5 | F |

**Page Faults = 9**

---

### Example 2: EAT Calculation

**Given**:
- Memory access: 200 ns
- Page fault: 8 ms
- Page fault rate: 0.001

**Find**: EAT

$$EAT = (1 - 0.001) \times 200 + 0.001 \times 8,000,000$$
$$= 0.999 \times 200 + 8000$$
$$= 199.8 + 8000 = 8199.8 \text{ ns}$$

**Slowdown**: 8199.8 / 200 ≈ 41× slower!

---

### Example 3: Working Set

**Given**:
- Reference: 1, 2, 3, 2, 1, 4, 5, 4, 3, 2
- Δ = 4

**Find**: Working set at time 6

Last 4 references at time 6: 2, 1, 4, 5

**WS(6, 4) = {1, 2, 4, 5}**

Size = 4 pages needed

---

## 🎯 GATE Traps and Anti-Solutions

### Trap 1: Belady's Anomaly
- ONLY affects FIFO
- LRU, Optimal, Clock don't have it

### Trap 2: Optimal is Always Best
- Yes, but only when you know future
- LRU is best practical algorithm

### Trap 3: Page Fault Time
- Dominated by disk I/O (~10 ms)
- Don't forget: includes disk seek + transfer

### Trap 4: Clock vs LRU
- Clock approximates LRU
- Not identical results!

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2018)
**Which algorithm suffers from Belady's anomaly?**

(A) LRU  
(B) FIFO ✓  
(C) Optimal  
(D) Clock

---

### Q2: (GATE 2019)
**Minimum frames for process executing `MOV [X], [Y]`?**

Need: 1 for instruction, 1 for X, 1 for Y = **3 frames minimum**

(If instruction spans pages: could be more)

---

### Q3: (GATE 2017)
**What is thrashing?**

(A) High CPU utilization  
(B) High disk utilization  
(C) High paging activity with low CPU utilization ✓  
(D) Memory overflow

---

## ⚡ The 5-Second Snap-Check

1. **FIFO?** → Replace oldest (watch for Belady's)
2. **Optimal?** → Replace farthest future use
3. **LRU?** → Replace longest past unused
4. **Thrashing?** → Too many processes, not enough frames

---

## 🧠 Memory Mnemonics

### Page Replacement: "FOL"
- **F**IFO: First page in
- **O**ptimal: Future farthest
- **L**RU: Least recently used

### Thrashing Sign: "Fast Disk, Slow CPU"
- High disk I/O
- Low CPU utilization
- = Thrashing!

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Demand Paging | Load pages only when needed |
| Page Fault | Page not in memory, trap to OS |
| FIFO | Simple but Belady's anomaly |
| Optimal | Best but needs future knowledge |
| LRU | Best practical algorithm |
| Clock | LRU approximation, O(1) |
| Thrashing | More paging than executing |
| Working Set | Pages needed in time window |

---

*Next Chapter: [File Systems →](09-File-Systems.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
