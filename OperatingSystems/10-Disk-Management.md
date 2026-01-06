# Chapter 10: Disk Management

> **"Disk scheduling is like an elevator algorithm - picking up passengers (requests) in the most efficient order"**

---

## 🎯 Disk Structure

### Physical Structure

```
        ┌──────────────────────────────────────────┐
        │           Platters (spinning disks)      │
        │    ┌─────────────────────────────────┐   │
        │    │    ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○       │   │
        │    │    Track 0 (outermost)          │   │
        │    │      ○ ○ ○ ○ ○ ○ ○ ○ ○          │   │
        │    │      Track 1                    │   │
        │    │        ○ ○ ○ ○ ○ ○ ○            │   │
        │    │        Track 2                  │   │
        │    │          ...                    │   │
        │    │            ○ ○ ○ (innermost)   │   │
        │    └─────────────────────────────────┘   │
        │                   │                       │
        │                   │ Spindle              │
        │                   ●                       │
        │                                          │
        │    ◄──── Read/Write Head ────►           │
        │         (moves radially)                 │
        └──────────────────────────────────────────┘
```

### Disk Geometry

| Term | Definition |
|------|------------|
| **Platter** | Circular magnetic disk |
| **Surface** | Top and bottom of platter |
| **Track** | Concentric circle on surface |
| **Sector** | Pie-shaped division of track (smallest unit) |
| **Cylinder** | Same track number across all surfaces |
| **Head** | Read/write component |
| **Arm** | Holds head, moves radially |

```
Cylinder 0:    Cylinder 1:    Cylinder 2:
Track 0, Surf 0   Track 1, Surf 0   Track 2, Surf 0
Track 0, Surf 1   Track 1, Surf 1   Track 2, Surf 1
Track 0, Surf 2   Track 1, Surf 2   Track 2, Surf 2
...              ...              ...
```

---

### Disk Addressing

**CHS (Cylinder-Head-Sector):**
```
Sector Address = (Cylinder, Head, Sector)
Example: (100, 2, 15) = Cylinder 100, Head 2, Sector 15
```

**LBA (Logical Block Addressing):**
```
Linear addressing: 0, 1, 2, 3, ...
Simpler for OS, controller translates to CHS
```

---

## ⏱️ Disk Access Time

### Components

```
Total Access Time = Seek Time + Rotational Latency + Transfer Time

┌────────────────────────────────────────────────────────────┐
│                                                            │
│  Seek Time        Rotational Latency    Transfer Time      │
│  ───────────      ─────────────────     ──────────────     │
│  Move head        Wait for sector       Read/write data    │
│  to cylinder      to rotate under       from sector(s)     │
│                   head                                     │
│                                                            │
│  Dominant!        = 1/2 × Rotation      = Bytes / Rate     │
│  (mechanical)       Time (avg)                             │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Formulas

```
Average Rotational Latency = (1/2) × (60/RPM) seconds

Transfer Time = (Bytes to transfer) / (Transfer rate)

Transfer Rate = (Bytes per track) × (RPM / 60)
             or = (Bytes per sector) × (Sectors per track) × (RPM / 60)
```

### Example Calculation

```
Disk: 7200 RPM, 500 sectors/track, 512 bytes/sector
Seek time: 8 ms (average)
Read 1 sector

Rotational latency = (1/2) × (60/7200) = 4.17 ms
Transfer time = 512 / (500 × 512 × 7200/60) = 0.0167 ms
Total = 8 + 4.17 + 0.0167 ≈ 12.2 ms
```

---

## 🔄 Disk Scheduling Algorithms

### Why Scheduling?

**Goal:** Minimize total seek time

```
Without scheduling:
Request order: 98, 183, 37, 122, 14, 124, 65, 67
Head at: 53

With scheduling:
Reorder for minimal head movement
```

---

### 1️⃣ FCFS (First-Come, First-Served)

**Rule:** Service requests in arrival order

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head starts at: 53

Path: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67

Seek distance:
|53-98| = 45
|98-183| = 85
|183-37| = 146
|37-122| = 85
|122-14| = 108
|14-124| = 110
|124-65| = 59
|65-67| = 2
─────────────
Total: 640 tracks
```

**Pros:** Fair, simple
**Cons:** Large seek times, wild swings

---

### 2️⃣ SSTF (Shortest Seek Time First)

**Rule:** Service nearest request next

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head starts at: 53

Step 1: Nearest to 53 → 65 (distance 12)
Step 2: Nearest to 65 → 67 (distance 2)
Step 3: Nearest to 67 → 37 (distance 30)
Step 4: Nearest to 37 → 14 (distance 23)
Step 5: Nearest to 14 → 98 (distance 84)
Step 6: Nearest to 98 → 122 (distance 24)
Step 7: Nearest to 122 → 124 (distance 2)
Step 8: Nearest to 124 → 183 (distance 59)

Path: 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Total: 12+2+30+23+84+24+2+59 = 236 tracks
```

**Pros:** Better than FCFS
**Cons:** **Starvation** of distant requests

---

### 3️⃣ SCAN (Elevator Algorithm)

**Rule:** Move head in one direction, servicing all requests, then reverse

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head at 53, moving toward 0

Phase 1 (toward 0):
53 → 37 → 14 → 0 (end)

Phase 2 (toward 199):
0 → 65 → 67 → 98 → 122 → 124 → 183

Path: 53 → 37 → 14 → 0 → 65 → 67 → 98 → 122 → 124 → 183

Seek: 53-37=16, 37-14=23, 14-0=14, 0-65=65, 65-67=2, 
      67-98=31, 98-122=24, 122-124=2, 124-183=59
Total: 236 tracks
```

**💡 Analogy:** Elevator going down, picking up all, then going up

**Pros:** No starvation, uniform wait
**Cons:** Unnecessary trip to end (0 or 199)

---

### 4️⃣ C-SCAN (Circular SCAN)

**Rule:** Move in one direction only, jump back to start after reaching end

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head at 53, moving toward 199

Phase 1 (toward 199):
53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 (end)

Jump to 0 (not counted as seek? depends on implementation)

Phase 2 (continue toward 199):
0 → 14 → 37

Path: 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
```

**Pros:** More uniform wait time than SCAN
**Cons:** Still goes to end

---

### 5️⃣ LOOK

**Rule:** Like SCAN but reverses at last request, not disk end

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head at 53, moving toward 0

Phase 1 (toward 0):
53 → 37 → 14 (last request in this direction, reverse here)

Phase 2 (toward 199):
14 → 65 → 67 → 98 → 122 → 124 → 183

Path: 53 → 37 → 14 → 65 → 67 → 98 → 122 → 124 → 183
Total: 16 + 23 + 51 + 2 + 31 + 24 + 2 + 59 = 208 tracks
```

**Better than SCAN:** Doesn't go to 0 unnecessarily

---

### 6️⃣ C-LOOK (Circular LOOK)

**Rule:** Like C-SCAN but reverses at last request in current direction

```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head at 53, moving toward 199

Phase 1:
53 → 65 → 67 → 98 → 122 → 124 → 183 (last in this direction)

Jump to first request (14)

Phase 2:
14 → 37

Path: 53 → 65 → 67 → 98 → 122 → 124 → 183 → 14 → 37
```

---

### Algorithm Comparison

| Algorithm | Total Seek (example) | Starvation? | Notes |
|-----------|---------------------|-------------|-------|
| FCFS | 640 | No | Simple, fair |
| SSTF | 236 | Yes | Greedy, fast |
| SCAN | 236 | No | Elevator |
| C-SCAN | ~300 | No | Uniform wait |
| LOOK | 208 | No | Practical SCAN |
| C-LOOK | ~250 | No | Practical C-SCAN |

---

## 💽 Disk Formatting

### Low-Level (Physical) Formatting

**Divides disk into sectors:**
```
┌──────────────────────────────────────────┐
│ Header │         Data          │ Trailer │
│  (ID)  │      (512 bytes)     │  (ECC)  │
└──────────────────────────────────────────┘
         Sector format
```

**Header:** Sector number, error codes
**Trailer:** Error Correcting Code (ECC)

---

### High-Level (Logical) Formatting

**Creates file system:**
1. Partition the disk
2. Write file system structures
   - Boot sector
   - Superblock
   - Free block list
   - Root directory

---

## 🔄 RAID (Redundant Array of Independent Disks)

### Goals
1. **Performance:** Parallel access
2. **Reliability:** Redundancy

---

### RAID Levels

#### RAID 0 (Striping)

```
┌─────────┐ ┌─────────┐
│ Disk 0  │ │ Disk 1  │
├─────────┤ ├─────────┤
│ Block 0 │ │ Block 1 │
│ Block 2 │ │ Block 3 │
│ Block 4 │ │ Block 5 │
└─────────┘ └─────────┘
```

**Pros:** Maximum performance, full capacity
**Cons:** NO redundancy - any disk fails = all data lost

**Use:** Speed over safety

---

#### RAID 1 (Mirroring)

```
┌─────────┐ ┌─────────┐
│ Disk 0  │ │ Disk 1  │
├─────────┤ ├─────────┤
│ Block 0 │ │ Block 0 │ ← Same data
│ Block 1 │ │ Block 1 │ ← Same data
│ Block 2 │ │ Block 2 │ ← Same data
└─────────┘ └─────────┘
```

**Pros:** Full redundancy, fast reads
**Cons:** 50% capacity, slow writes (write both)

**Use:** Critical data, boot drives

---

#### RAID 2 (Bit-level striping with Hamming code)

```
Data bits striped + Hamming ECC disks
Rarely used in practice
```

---

#### RAID 3 (Byte-level striping with dedicated parity)

```
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ Disk 0  │ │ Disk 1  │ │ Disk 2  │ │ Parity  │
├─────────┤ ├─────────┤ ├─────────┤ ├─────────┤
│ Byte 0  │ │ Byte 1  │ │ Byte 2  │ │ P(0,1,2)│
│ Byte 3  │ │ Byte 4  │ │ Byte 5  │ │ P(3,4,5)│
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

**Dedicated parity disk = bottleneck**

---

#### RAID 4 (Block-level striping with dedicated parity)

```
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ Disk 0  │ │ Disk 1  │ │ Disk 2  │ │ Parity  │
├─────────┤ ├─────────┤ ├─────────┤ ├─────────┤
│ Block 0 │ │ Block 1 │ │ Block 2 │ │ P(0,1,2)│
│ Block 3 │ │ Block 4 │ │ Block 5 │ │ P(3,4,5)│
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

**Same bottleneck as RAID 3**

---

#### RAID 5 (Block-level striping with distributed parity) ⭐

```
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ Disk 0  │ │ Disk 1  │ │ Disk 2  │ │ Disk 3  │
├─────────┤ ├─────────┤ ├─────────┤ ├─────────┤
│ Block 0 │ │ Block 1 │ │ Block 2 │ │ P(0,1,2)│
│ Block 3 │ │ Block 4 │ │ P(3,4,5)│ │ Block 5 │
│ Block 6 │ │ P(6,7,8)│ │ Block 7 │ │ Block 8 │
│P(9,10,11)│ │ Block 9 │ │ Block 10│ │ Block 11│
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

**Parity distributed across all disks - no bottleneck**

**Capacity:** (n-1) disks worth
**Fault tolerance:** 1 disk failure

**Most common in practice**

---

#### RAID 6 (Double distributed parity)

```
Like RAID 5 but with 2 parity blocks per stripe
Survives 2 disk failures
Capacity: (n-2) disks
```

---

### RAID Comparison

| Level | Capacity | Fault Tolerance | Read | Write | Min Disks |
|-------|----------|-----------------|------|-------|-----------|
| 0 | n | 0 | Fast | Fast | 2 |
| 1 | n/2 | 1 | Fast | Slow | 2 |
| 5 | n-1 | 1 | Fast | Medium | 3 |
| 6 | n-2 | 2 | Fast | Slow | 4 |
| 10 | n/2 | 1 per pair | Fast | Medium | 4 |

---

#### RAID 10 (1+0) - Stripe of Mirrors

```
      Stripe
   ┌────┴────┐
   │         │
┌──┴──┐   ┌──┴──┐
│Mirror│   │Mirror│
│ 0-1 │   │ 2-3  │
└──┬──┘   └──┬──┘
  ┌┴┐       ┌┴┐
  │0│1│     │2│3│
  └─┘       └─┘
```

**Best performance + redundancy (expensive)**

---

## 🔧 Disk Management Operations

### Bad Block Handling

**Sector sparing:** Map bad sector to spare
**Sector slipping:** Shift sectors to skip bad one

```
Before: [1][2][BAD][4][5]
After (sparing): [1][2][→Spare][4][5]
After (slipping): [1][2][3][4][5] (BAD skipped, others shifted)
```

---

### Swap Space

**Used for:**
- Virtual memory (page swap)
- Hibernation

**Location:**
- Separate partition (faster)
- Swap file (flexible)

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **Calculate seek distance:** Apply algorithms
2. **Disk access time:** Sum components
3. **RAID capacity/redundancy:** Given n disks
4. **Compare algorithms:** Which is best for scenario

### ⚠️ Edge Cases:
1. **LOOK vs SCAN:** LOOK doesn't go to disk end
2. **Head direction matters:** Especially for SCAN/LOOK
3. **SSTF can starve:** Not fair
4. **RAID 5 min disks:** 3 (not 2)

---

## 🎯 Quick Revision Points

```
✓ Access Time = Seek + Rotational Latency + Transfer
✓ Avg Rotational Latency = (1/2) × (60/RPM)
✓ FCFS: Fair but slow
✓ SSTF: Fast but starves
✓ SCAN: Elevator, goes to end
✓ LOOK: Elevator, reverses at last request
✓ C-SCAN/C-LOOK: One direction only
✓ RAID 0: Speed, no redundancy
✓ RAID 1: Mirroring, 50% capacity
✓ RAID 5: Distributed parity, n-1 capacity
✓ RAID 6: Double parity, n-2 capacity
```

---

## 📚 Key Formulas

```
Disk Access Time = Seek Time + Rotational Latency + Transfer Time

Average Rotational Latency = (60 / RPM) / 2 seconds
                          = (60000 / RPM) / 2 ms

Transfer Rate = Bytes per sector × Sectors per track × (RPM / 60)

Transfer Time = Data Size / Transfer Rate

RAID 5 Usable Capacity = (N - 1) × Disk Size
RAID 6 Usable Capacity = (N - 2) × Disk Size
RAID 1 Usable Capacity = N / 2 × Disk Size
RAID 0 Usable Capacity = N × Disk Size
```

---

[← Previous: I/O Systems](./09-IO-Systems.md) | [Next: Protection & Security →](./11-Protection-Security.md)
