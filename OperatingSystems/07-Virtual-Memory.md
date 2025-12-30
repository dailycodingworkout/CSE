# Chapter 7: Virtual Memory

> **"Virtual memory is like a magician's trick - showing the audience (process) a larger space than actually exists on stage (RAM)"**

---

## 🎯 What is Virtual Memory?

**Definition:** Separation of logical memory (what process sees) from physical memory (actual RAM)

**Key Concept:** Only part of program needs to be in memory for execution

### Benefits

| Benefit | Description |
|---------|-------------|
| **Large Address Space** | Programs can be larger than physical memory |
| **More Processes** | Each uses less physical memory |
| **Less I/O** | Don't load entire program at start |
| **Efficient Use** | Pages loaded only when needed |
| **Simplified Loading** | OS handles memory allocation |

```
Process View:                    Physical Reality:
┌────────────────────┐          ┌────────────────────┐
│    Very Large      │          │   Limited RAM      │
│    Virtual         │          │                    │
│    Address Space   │   →      │   + Disk Storage   │
│    (e.g., 4GB)     │          │   (swap space)     │
└────────────────────┘          └────────────────────┘
```

---

## 📄 Demand Paging

### Concept

**Load pages only when needed (on demand)**

```
Page Table with Valid/Invalid Bit:
┌─────────┬───────┬───────────────┐
│ Page #  │ Valid │ Frame/Disk    │
├─────────┼───────┼───────────────┤
│    0    │   1   │   Frame 4     │ ← In memory
│    1    │   0   │   Disk loc    │ ← On disk
│    2    │   1   │   Frame 7     │ ← In memory
│    3    │   0   │   Disk loc    │ ← On disk
│    4    │   0   │   Disk loc    │ ← On disk
│    5    │   1   │   Frame 2     │ ← In memory
└─────────┴───────┴───────────────┘
```

**Valid = 1:** Page in memory
**Valid = 0:** Page fault (not in memory)

---

### Page Fault Handling

```
1. Check internal table (in PCB) - is reference valid?
2. If invalid reference → terminate process
3. If valid but not in memory → page fault
4. Find free frame
5. Read page from disk into frame
6. Update page table (set valid bit)
7. Restart instruction that caused fault
```

```
┌─────────┐     page     ┌────────────┐
│   CPU   │────fault────►│    OS      │
└────┬────┘              └─────┬──────┘
     │                         │
     │ restart                 │ 1. Find free frame
     │                         │ 2. Disk I/O
     │                         │ 3. Update page table
     │                         ▼
┌────┴────┐              ┌────────────┐
│ Memory  │◄─────────────│   Disk     │
└─────────┘    load page └────────────┘
```

---

### Pure Demand Paging

**Start with NO pages in memory**

- First instruction causes page fault
- Page loaded, instruction restarts
- Next instruction may cause another fault
- Eventually, working set loaded

**Locality of Reference:** Programs tend to access nearby locations → reasonable performance

---

### Performance of Demand Paging

**Effective Access Time (EAT):**

```
EAT = (1 - p) × memory_access_time + p × page_fault_time

where p = page fault rate (0 ≤ p ≤ 1)
```

**Page Fault Service Time Components:**
1. Service interrupt: ~1-100 μs
2. Read page from disk: ~3-8 ms (dominant)
3. Restart process: ~1-100 μs

**Example:**
```
Memory access = 100 ns
Page fault time = 8 ms = 8,000,000 ns
Acceptable slowdown = 10% (EAT ≤ 110 ns)

110 ≥ (1-p) × 100 + p × 8,000,000
110 ≥ 100 - 100p + 8,000,000p
10 ≥ 7,999,900p
p ≤ 0.00000125

→ Less than 1 page fault per 800,000 accesses!
```

**💡 GATE Insight:** Page faults are VERY expensive; must be minimized

---

## 🔄 Copy-on-Write (COW)

**Problem:** fork() copies entire address space (slow)

**Solution:** Share pages initially, copy only when written

```
After fork():
Parent:           Child:
┌─────────┐      ┌─────────┐
│ Page 0  │─────►│ Page 0  │──────►  Shared Frame A
├─────────┤      ├─────────┤          (marked read-only)
│ Page 1  │─────►│ Page 1  │──────►  Shared Frame B
└─────────┘      └─────────┘          (marked read-only)

On write by child:
Parent:           Child:
┌─────────┐      ┌─────────┐
│ Page 0  │──────►Frame A   │ Page 0  │──────►Frame A (unchanged)
├─────────┤               ├─────────┤
│ Page 1  │──────►Frame B   │ Page 1  │──────►Frame C (copied!)
└─────────┘               └─────────┘
```

**vfork():** Even faster - child shares address space, parent blocks until child exits/execs

---

## 🔁 Page Replacement

### When All Frames Are Full

```
1. Page fault occurs
2. Find victim page (using replacement algorithm)
3. If victim is modified, write to disk
4. Load new page into victim's frame
5. Update page tables
6. Continue process
```

**Modify (Dirty) Bit:** Reduces disk writes
- If page unchanged, no need to write back
- Only modified pages need disk write

---

### Page Replacement Algorithms

#### 1️⃣ FIFO (First-In, First-Out)

**Rule:** Replace the oldest page in memory

```
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames = 3

Step-by-step:
7: [7, -, -] PF
0: [7, 0, -] PF
1: [7, 0, 1] PF
2: [2, 0, 1] PF (7 out - oldest)
0: [2, 0, 1] Hit
3: [2, 3, 1] PF (0 out)
0: [2, 3, 0] PF (1 out)
4: [4, 3, 0] PF (2 out)
2: [4, 2, 0] PF (3 out)
3: [4, 2, 3] PF (0 out)
0: [0, 2, 3] PF (4 out)
3: [0, 2, 3] Hit
2: [0, 2, 3] Hit

Page Faults = 10
```

**Belady's Anomaly:** More frames can cause MORE page faults!

```
Reference: 1 2 3 4 1 2 5 1 2 3 4 5

3 frames: 9 page faults
4 frames: 10 page faults  ← WORSE!
```

---

#### 2️⃣ Optimal (OPT / MIN)

**Rule:** Replace page that won't be used for longest time in future

```
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames = 3

7: [7, -, -] PF
0: [7, 0, -] PF
1: [7, 0, 1] PF
2: [2, 0, 1] PF (7 not used again until... never, replace it)
0: [2, 0, 1] Hit
3: [2, 0, 3] PF (1 used last, replace it)
0: [2, 0, 3] Hit
4: [2, 4, 3] PF (0 used later, 2 used later, replace 0... wait)
   Looking ahead: 0 at position 10, 2 at position 8, 3 at position 9
   Replace 0 (furthest future use)
4: [2, 4, 3] PF (replace 0)
...

Page Faults = 6 (minimum possible)
```

**💡 GATE Fact:** Optimal is theoretical - we don't know future. Use as benchmark.

---

#### 3️⃣ LRU (Least Recently Used)

**Rule:** Replace page that hasn't been used for longest time

```
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames = 3

7: [7, -, -] PF
0: [7, 0, -] PF
1: [7, 0, 1] PF
2: [2, 0, 1] PF (7 LRU)
0: [2, 0, 1] Hit
3: [2, 0, 3] PF (1 LRU)
0: [2, 0, 3] Hit
4: [4, 0, 3] PF (2 LRU)
2: [4, 0, 2] PF (3 LRU)
3: [3, 0, 2] PF (4 LRU)
0: [3, 0, 2] Hit
3: [3, 0, 2] Hit
2: [3, 0, 2] Hit

Page Faults = 8
```

**Implementation Methods:**

**Counter-based:**
```
Each page entry has "time of last use"
Replace page with smallest time value
Overhead: Update counter on EVERY memory access
```

**Stack-based:**
```
Maintain stack of page numbers
On access: Move page to top
Replace: Bottom of stack (LRU)
Overhead: Stack operations
```

**💡 LRU doesn't suffer from Belady's Anomaly** (it's a stack algorithm)

---

#### 4️⃣ LRU Approximations

##### Reference Bit Algorithm

```
Each page has reference bit (set by hardware on access)
Initially: All bits = 0
On access: Hardware sets bit = 1
Periodically: OS clears all bits

Replace: Any page with reference bit = 0
```

---

##### Second Chance (Clock) Algorithm

```
Pages in circular queue with pointer
┌─────────────────────────────────────┐
│    ┌───┐                            │
│    │ 0 │ ←────── pointer            │
│    └─┬─┘                            │
│  ┌───┴───┐                          │
│  │ 1 │ 1 │ (page 1, ref bit = 1)    │
│  └───┬───┘                          │
│  ┌───┴───┐                          │
│  │ 2 │ 0 │ (page 2, ref bit = 0)    │
│  └───┬───┘                          │
│  ┌───┴───┐                          │
│  │ 3 │ 1 │                          │
│  └───────┘                          │
└─────────────────────────────────────┘

On page fault:
1. Check page at pointer
2. If ref bit = 0: Replace this page
3. If ref bit = 1: Clear bit, advance pointer, repeat
```

**Worst case:** All bits = 1 → degenerates to FIFO

---

##### Enhanced Second Chance

**Use both reference (R) and modify (M) bits:**

| Class | (R, M) | Description |
|-------|--------|-------------|
| 0 | (0, 0) | Not recently used, not modified |
| 1 | (0, 1) | Not recently used, modified |
| 2 | (1, 0) | Recently used, not modified |
| 3 | (1, 1) | Recently used, modified |

**Replace:** Lowest class first (prioritize clean pages)

---

#### 5️⃣ Not Recently Used (NRU)

```
1. Periodically clear R bit
2. On page fault, classify pages by (R, M)
3. Pick random page from lowest non-empty class
```

---

#### 6️⃣ Counting-Based Algorithms

**LFU (Least Frequently Used):**
- Keep count of accesses
- Replace page with smallest count
- Problem: Old pages have high counts

**MFU (Most Frequently Used):**
- Replace page with highest count
- Assumption: Low count = just loaded, will be used more

---

### Algorithm Comparison

| Algorithm | Overhead | Performance | Anomaly? |
|-----------|----------|-------------|----------|
| FIFO | Low | Poor | Yes |
| Optimal | N/A | Best | No |
| LRU | High | Good | No |
| Second Chance | Low | Good | No |
| LFU | Medium | Medium | Possible |

---

## 📊 Frame Allocation

### Allocation Strategies

**Equal Allocation:**
```
m frames, n processes
Each gets m/n frames
```

**Proportional Allocation:**
```
Process Pi gets: ai = (si / Σsj) × m
where si = size of Pi, m = total frames
```

**Priority-based Allocation:**
Higher priority → more frames

---

### Global vs Local Replacement

| Type | Scope | Behavior |
|------|-------|----------|
| **Global** | All frames in system | Can steal from other processes |
| **Local** | Only own frames | Limited to allocated frames |

**Global:** Better throughput, unpredictable performance
**Local:** More predictable, possible underutilization

---

## 📈 Thrashing

### Definition

**Thrashing:** System spends more time paging than executing

```
                    ▲ CPU Utilization
                    │
                    │         Thrashing point
                    │              │
                    │    ┌─────────┼──┐
                    │   /          │   \
                    │  /           │    \
                    │ /            │     \
                    │/             │      \
                    ├──────────────┼───────┼───────►
                                   │       │    Degree of
                              Optimal   Overload  Multiprogramming
```

### Cause

```
1. Too many processes → not enough frames each
2. Process needs more frames than allocated
3. High page fault rate → much I/O
4. CPU utilization drops
5. OS thinks CPU underutilized
6. OS adds more processes → worse!
```

---

### Solutions

#### 1. Working Set Model

**Working Set:** Set of pages referenced in last Δ time units

```
Working Set Window Δ = 10

Reference: ...1 2 3 4 2 3 4 4 3 1 | 2 3 4 5
                              └───┘
                              Window at time t
                              
WS(t, Δ) = {1, 2, 3, 4} (size = 4)
```

**Working Set Size (WSS):** Number of pages in working set

**Policy:**
```
If Σ WSSi > total frames → thrashing likely
Solution: Suspend a process
```

---

#### 2. Page Fault Frequency (PFF)

```
               ▲ Page Fault Rate
               │
               │─────────────────── Upper bound
               │                        (add frames)
               │       xxxxxx
               │      x      x
               │     x        x
               │─────────────────── Lower bound
               │                        (remove frames)
               ├─────────────────────────────────────►
                           Frames allocated

If PFF > upper → allocate more frames
If PFF < lower → take frames away
```

---

## 🖥️ Memory-Mapped Files

**Concept:** Map file directly into virtual address space

```
Virtual Address Space:          File on Disk:
┌──────────────────┐           ┌──────────────────┐
│                  │           │                  │
├──────────────────┤           │                  │
│ Memory-mapped    │◄─────────►│    File          │
│ file region      │           │    contents      │
├──────────────────┤           │                  │
│                  │           │                  │
└──────────────────┘           └──────────────────┘
```

**Benefits:**
- File I/O through memory operations
- Efficient sharing between processes
- Simplifies programming

**Implementation:**
```c
void *ptr = mmap(NULL, length, PROT_READ | PROT_WRITE, 
                 MAP_SHARED, fd, 0);
// Access file through ptr
munmap(ptr, length);
```

---

## 🔐 Kernel Memory Allocation

### Why Different from User Memory?

1. Some kernel memory must be contiguous (DMA)
2. No page replacement for kernel pages
3. Must be fast and efficient

---

### Buddy System

**Allocate memory in power-of-2 sizes:**

```
Request: 21 KB (rounded to 32 KB = 2^5)

Start: 256 KB block
Split: 128 | 128
Split: 64 | 64 | 128
Split: 32 | 32 | 64 | 128
Allocate: [32 used] | 32 | 64 | 128

On free: Merge with "buddy" if both free
```

**Advantage:** Fast coalescing
**Disadvantage:** Internal fragmentation

---

### Slab Allocation

**Idea:** Pre-allocate objects of same type

```
Cache for Process Descriptors:
┌─────────────────────────────────────────────┐
│ Slab 1 (full)    │ Slab 2 (partial) │ Slab 3 (empty)
│ [used][used][used]│[used][free][free]│[free][free][free]
└─────────────────────────────────────────────┘
```

**Benefits:**
- No fragmentation (objects same size)
- Fast allocation (grab from free list)
- Objects pre-initialized

---

## 🔢 Page Size Considerations

| Small Pages | Large Pages |
|-------------|-------------|
| Less internal fragmentation | Less page faults |
| More page table entries | Fewer page table entries |
| Better resolution | Less I/O overhead |
| More TLB misses | Better TLB hit rate |

**Modern Systems:** Support multiple page sizes (4KB, 2MB, 1GB)

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **Page fault calculation:** Given reference string
2. **EAT calculation:** With page fault rate
3. **Page replacement trace:** FIFO, LRU, Optimal
4. **Belady's Anomaly:** When it occurs
5. **Working set:** Calculate from reference string

### ⚠️ Edge Cases & Traps:

1. **First access to page = page fault** (demand paging)
2. **Hit doesn't reset FIFO order** (only LRU)
3. **Optimal looks FORWARD, LRU looks BACKWARD**
4. **Modify bit only matters for write-back, not hit/miss**
5. **Working set size changes dynamically**

---

## 🔢 Numerical Shortcuts

### Page Faults by Reference String

**Quick method for small examples:**
```
1. Draw frame table
2. On each reference:
   - If present → Hit (no page fault)
   - If not present → Page Fault, apply algorithm
```

### Minimum Frames for No Page Fault

**Optimal = number of distinct pages in reference string**

```
Reference: 1 2 3 1 2 4 1 2 3
Distinct pages: {1, 2, 3, 4} = 4
With 4 frames using Optimal: 4 page faults (initial loads only)
```

---

## 🎯 Quick Revision Points

```
✓ Virtual memory = Logical memory > Physical memory
✓ Demand paging = Load pages only when needed
✓ Page fault = Page not in memory
✓ EAT = (1-p)×mem + p×fault_time
✓ FIFO: Oldest page out (Belady's Anomaly possible)
✓ Optimal: Furthest future use (theoretical best)
✓ LRU: Longest since last use (practical best)
✓ Second Chance: FIFO + reference bit
✓ Thrashing: Too much paging, CPU underutilized
✓ Working Set: Pages used in time window Δ
✓ COW: Share until write, then copy
```

---

## 📚 Key Formulas

```
EAT = (1 - p) × m + p × (m + page_fault_time)
    = m + p × page_fault_time

Page Fault Rate = Page Faults / Total References

Working Set Size = |WS(t, Δ)|

Thrashing Prevention:
If Σ WSSi > total_frames → suspend process

Memory Required (100% in memory):
= Number of frames × Page size
```

---

[← Previous: Memory Management](./06-Memory-Management.md) | [Next: File Systems →](./08-File-Systems.md)
