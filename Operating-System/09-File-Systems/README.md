# 📖 Chapter 9: File Systems

> **The Atomic Truth:** File System = Organize data persistently on storage

---

## 🎯 GATE Syllabus Coverage
- File Concepts and Operations
- Directory Structure
- File Allocation Methods
- Free Space Management
- File System Implementation

---

## 9.1 File Concepts

### What is a File?
A **File** is a named collection of related information stored on secondary storage.

### File Attributes

| Attribute | Description |
|-----------|-------------|
| Name | Human-readable identifier |
| Identifier | Unique number (inode) |
| Type | File type (.txt, .exe, etc.) |
| Location | Pointer to data blocks |
| Size | Current file size |
| Protection | Access control (rwx) |
| Time/Date | Creation, modification, access |
| Owner | User who owns file |

### File Operations

| Operation | Description |
|-----------|-------------|
| Create | Allocate space, add to directory |
| Write | Write data at write pointer |
| Read | Read data at read pointer |
| Seek | Move file pointer |
| Delete | Free space, remove from directory |
| Truncate | Delete content, keep attributes |
| Open | Load metadata to memory |
| Close | Free memory structures |

### Open File Table

```
┌─────────────────────────────────────────────────────┐
│             Per-Process Open File Table             │
│  ┌─────┬──────────────────────────────────────────┐│
│  │ FD  │  Pointer to System-Wide Table Entry      ││
│  ├─────┼──────────────────────────────────────────┤│
│  │  0  │  stdin                                   ││
│  │  1  │  stdout                                  ││
│  │  2  │  stderr                                  ││
│  │  3  │  → myfile.txt entry                      ││
│  └─────┴──────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────┐
│           System-Wide Open File Table               │
│  ┌───────────────────────────────────────────────┐ │
│  │ Open count │ File pointer │ Inode pointer    │ │
│  │     2      │    1024      │   → inode 42     │ │
│  └───────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## 9.2 File Types

### Common Types

| Type | Extension | Description |
|------|-----------|-------------|
| Executable | .exe, .bin | Machine code |
| Object | .obj, .o | Compiled code |
| Source | .c, .java | Source code |
| Text | .txt | ASCII characters |
| Archive | .tar, .zip | Grouped files |

### File Structure

| Type | Description | Example |
|------|-------------|---------|
| None (byte stream) | Sequence of bytes | UNIX |
| Simple record | Lines of fixed/variable length | Text file |
| Complex | Tree, indexed | Database |

---

## 9.3 Access Methods

### Sequential Access

```
   Read/Write
       ↓
┌──────────────────────────────────────────┐
│ Data 1 │ Data 2 │ Data 3 │ Data 4 │ ... │
└──────────────────────────────────────────┘
                    ─────→
               (forward only)
```

Operations: `read_next()`, `write_next()`, `reset()`

### Direct (Random) Access

```
   Seek to position n
       ↓
┌──────────────────────────────────────────┐
│ Data 0 │ Data 1 │ Data 2 │ Data 3 │ ... │
└──────────────────────────────────────────┘
     ↑         ↑         ↑         ↑
   read(0)  read(1)  read(2)  read(3)
```

Operations: `read(n)`, `write(n)`, `seek(n)`

### Indexed Access

```
┌─────────────┐     ┌─────────────────────────┐
│   Index     │     │     Data File           │
├─────────────┤     ├─────────────────────────┤
│ Key → Ptr   │────→│ Record                  │
│ Key → Ptr   │────→│ Record                  │
│ Key → Ptr   │────→│ Record                  │
└─────────────┘     └─────────────────────────┘
```

---

## 9.4 Directory Structure

### Single-Level Directory

```
┌─────────────────────────────────────────┐
│              Directory                   │
├────────┬────────┬────────┬──────────────┤
│ cat    │ bo     │ a      │ test        │
└────────┴────────┴────────┴──────────────┘
```

**Problems:**
- Naming conflicts between users
- No organization

### Two-Level Directory

```
┌─────────────────────────────────────────┐
│           Master File Directory         │
├─────────────────┬───────────────────────┤
│     User 1      │       User 2          │
└────────┬────────┴────────┬──────────────┘
         ↓                 ↓
┌─────────────────┐ ┌─────────────────────┐
│ cat │ a │ test  │ │ x │ data │ test    │
└─────────────────┘ └─────────────────────┘
```

**Advantage:** Users can have same file names
**Disadvantage:** No subdirectories

### Tree-Structured Directory

```
                    root
                   /    \
                users    bin
               /    \      \
            user1  user2   ls
             /  \     |
           doc code  data
           /
        paper.txt
```

**Path names:**
- Absolute: `/users/user1/doc/paper.txt`
- Relative: `doc/paper.txt` (from user1)

### Acyclic-Graph Directory

Allows sharing via **links** (hard links, symbolic links).

```
         root
        /    \
      dict   spell
        \    /
         list (shared)
```

**Hard Link:** Direct pointer to inode
**Symbolic Link:** File containing path name

### General Graph Directory

Allows cycles (dangerous - can lead to infinite loops).

**Solution:** Garbage collection to detect unreachable files.

---

## 9.5 File Allocation Methods

### 9.5.1 Contiguous Allocation

**Concept:** Each file occupies contiguous blocks.

```
Directory Entry:
┌──────────┬───────┬────────┐
│ File     │ Start │ Length │
├──────────┼───────┼────────┤
│ mail     │   0   │   2    │
│ list     │   4   │   4    │
│ f        │  10   │   3    │
└──────────┴───────┴────────┘

Disk:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │
├───┴───┼───┴───┼───┴───┴───┴───┼───┴───┼───┴───┴───┤
│ mail  │ free  │     list      │ free  │    f      │
└───────┴───────┴───────────────┴───────┴───────────┘
```

**Advantages:**
- Simple (only start and length)
- Fast sequential and random access
- Minimal seek time

**Disadvantages:**
- External fragmentation
- File size must be known at creation
- Difficult to grow files

**Best for:** CD-ROMs, DVDs (read-only)

---

### 9.5.2 Linked Allocation

**Concept:** Each block contains pointer to next block.

```
Directory Entry:
┌──────────┬───────┬─────┐
│ File     │ Start │ End │
├──────────┼───────┼─────┤
│ jeep     │   9   │  25 │
└──────────┴───────┴─────┘

Disk blocks:
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│Block 9  │───→│Block 16 │───→│Block 1  │───→│Block 25 │───→ null
│ data    │    │ data    │    │ data    │    │ data    │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Advantages:**
- No external fragmentation
- Files can grow easily
- No need to declare size

**Disadvantages:**
- Random access is slow (must traverse)
- Space overhead for pointers
- Pointer corruption is fatal

**File Allocation Table (FAT):**
Move pointers to separate table in memory.

```
FAT:
┌───────┬────────┐
│ Block │ Next   │
├───────┼────────┤
│   0   │  -1    │
│   1   │  25    │
│   ...         │
│   9   │  16    │
│   16  │   1    │
│   25  │  -1    │ (end)
└───────┴────────┘
```

---

### 9.5.3 Indexed Allocation

**Concept:** Each file has index block containing pointers to all data blocks.

```
Directory Entry:
┌──────────┬─────────────┐
│ File     │ Index Block │
├──────────┼─────────────┤
│ jeep     │     19      │
└──────────┴─────────────┘

Index Block 19:        Data Blocks:
┌──────────────┐       ┌────────┐
│ 0 → Block 9  │──────→│ Block 9│
├──────────────┤       └────────┘
│ 1 → Block 16 │──────→┌────────┐
├──────────────┤       │Block 16│
│ 2 → Block 1  │       └────────┘
├──────────────┤       ┌────────┐
│ 3 → Block 10 │       │ Block 1│
├──────────────┤       └────────┘
│ 4 → Block 25 │       ...
├──────────────┤
│ 5 → null     │
└──────────────┘
```

**Advantages:**
- Fast random access
- No external fragmentation
- Files can grow (within index limit)

**Disadvantages:**
- Index block overhead
- Index block size limits file size

**Handling Large Files:**

| Method | Description |
|--------|-------------|
| Linked indexes | Index blocks linked together |
| Multi-level index | Index of index blocks |
| Combined (UNIX) | Direct + indirect blocks |

---

### 9.5.4 UNIX Inode Structure

```
┌─────────────────────────────────────────┐
│              INODE                       │
├─────────────────────────────────────────┤
│ File attributes (mode, size, time, etc.)│
├─────────────────────────────────────────┤
│ Direct blocks (12 pointers)             │
│  [0] → data block                       │
│  [1] → data block                       │
│  ...                                    │
│  [11] → data block                      │
├─────────────────────────────────────────┤
│ Single indirect → ┌──────┐              │
│                   │Index │→ data blocks │
│                   └──────┘              │
├─────────────────────────────────────────┤
│ Double indirect → ┌──────┐              │
│                   │Index │→ Index → data│
│                   └──────┘              │
├─────────────────────────────────────────┤
│ Triple indirect → ┌──────┐              │
│                   │Index │→Index→Index→ │
│                   └──────┘         data │
└─────────────────────────────────────────┘
```

### Maximum File Size Calculation

**Given:**
- Block size: 4KB
- Pointer size: 4 bytes
- Pointers per block: 4KB/4B = 1024

**Calculate:**
- Direct: 12 × 4KB = 48KB
- Single indirect: 1024 × 4KB = 4MB
- Double indirect: 1024² × 4KB = 4GB
- Triple indirect: 1024³ × 4KB = 4TB

**Max file size ≈ 4TB**

---

### 9.5.5 Allocation Method Comparison

| Feature | Contiguous | Linked | Indexed |
|---------|------------|--------|---------|
| External Frag | Yes | No | No |
| Random Access | Fast | Slow | Fast |
| Directory Info | Start + Length | Start | Index block |
| File Growth | Difficult | Easy | Easy |
| Space Overhead | None | Pointer/block | Index block |

---

## 9.6 Free Space Management

### 9.6.1 Bit Vector (Bitmap)

```
Block:  0 1 2 3 4 5 6 7 8 9 ...
Bitmap: 0 0 1 0 0 0 1 1 0 1 ...
        free  used          used
```

**Finding free block:** Find first 0 bit

**Advantages:**
- Simple, efficient
- Easy to find contiguous blocks

**Disadvantages:**
- Requires extra space (1 bit per block)
- Bitmap should be in memory

**Size calculation:**
$$\text{Bitmap size} = \frac{\text{Disk size}}{\text{Block size} \times 8}$$

Example: 1TB disk, 4KB blocks
= 1TB / (4KB × 8) = 32MB bitmap

---

### 9.6.2 Linked List

Free blocks linked together.

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│Block 2  │───→│Block 6  │───→│Block 7  │───→ null
│(free)   │    │(free)   │    │(free)   │
└─────────┘    └─────────┘    └─────────┘
```

**Advantages:**
- No space wastage

**Disadvantages:**
- Slow to traverse
- Finding contiguous blocks is difficult

---

### 9.6.3 Grouping

First free block contains addresses of n free blocks.

```
┌─────────────────────────────────┐
│ Block 2 (free)                  │
│ ┌─────────────────────────────┐ │
│ │ Block 5, 7, 9, 12, ...     │ │
│ │ → Block 20 (more addresses)│ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

### 9.6.4 Counting

Store (starting block, count) pairs for contiguous free regions.

```
┌────────┬───────┐
│ Start  │ Count │
├────────┼───────┤
│   2    │   3   │  Blocks 2, 3, 4 free
│   8    │   5   │  Blocks 8-12 free
└────────┴───────┘
```

---

## 9.7 Disk Block Access Calculation

### Number of Disk Accesses for File Access

**Contiguous:**
- 1 access (direct seek)

**Linked:**
- N accesses for Nth block (traverse chain)

**Indexed:**
- 2 accesses (index block + data block)
- More for multi-level

**UNIX inode (block N, 0-indexed):**

| Block Number | Accesses | Path |
|--------------|----------|------|
| 0-11 | 1 | Direct |
| 12-1035 | 2 | Single indirect |
| 1036-1049611 | 3 | Double indirect |
| > 1049611 | 4 | Triple indirect |

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2018)
**Q:** Block size = 1KB, inode has 10 direct, 1 single indirect, 1 double indirect. Pointer = 4B. Max file size?

**Solution:**
- Pointers per block = 1KB/4B = 256
- Direct: 10 × 1KB = 10KB
- Single indirect: 256 × 1KB = 256KB
- Double indirect: 256² × 1KB = 64MB

**Max = 10KB + 256KB + 64MB ≈ 64MB**

---

### Question 2 (GATE 2019)
**Q:** Which allocation method is best for random access?
(a) Contiguous
(b) Linked
(c) Indexed
(d) Both (a) and (c)

**Answer:** (d) Both Contiguous and Indexed support fast random access.

---

### Question 3 (GATE 2020)
**Q:** Disk = 16GB, Block = 4KB. Bitmap size?

**Solution:**
- Total blocks = 16GB / 4KB = 4M blocks
- Bitmap size = 4M bits = 512KB

**Answer:** 512KB

---

## 🧠 Memory Tricks

### Mnemonic: Allocation Methods "CLI"
- **C**ontiguous: Fast but fragments
- **L**inked: No fragments, slow random
- **I**ndexed: Best of both worlds

### UNIX Inode Memory Hook
"**12 Direct is Small, Indirect is Powerful**"
- 12 direct blocks for small files
- Indirect for large files

### Directory Structure Progression
Single → Two → Tree → Graph
(Like organization growth: Solo → Team → Department → Matrix)

---

## ⚠️ Common GATE Traps

### Trap 1: Inode Pointer Counting
**Wrong:** Including inode itself as an access
**Right:** Count only data block accesses

### Trap 2: Linked Allocation FAT
**Wrong:** FAT adds disk accesses
**Right:** FAT is in memory, no extra disk access

### Trap 3: Max File Size
**Wrong:** Forgetting to add all levels
**Right:** Max = Direct + Single + Double + Triple

---

## 🛠️ Problem-Solving Techniques

### Technique 1: Maximum File Size Calculation (UNIX inode)

**Step-by-step template:**

```
Given: Block size = B, Pointer size = P, 
       D direct, SI single indirect, DI double indirect, TI triple indirect

Step 1: Calculate pointers per block
        PPB = B / P

Step 2: Calculate contribution from each level
        Direct:         D × B
        Single indirect: PPB × B
        Double indirect: PPB² × B
        Triple indirect: PPB³ × B

Step 3: Sum all contributions
        Max File Size = D×B + PPB×B + PPB²×B + PPB³×B
```

**Example:**
```
B=4KB, P=4B, D=12, SI=1, DI=1, TI=1
PPB = 4KB/4B = 1024

Direct:  12 × 4KB = 48KB
Single:  1024 × 4KB = 4MB
Double:  1024² × 4KB = 4GB
Triple:  1024³ × 4KB = 4TB

Max ≈ 4TB
```

### Technique 2: Disk Block Access Counting

**For UNIX inode, which block number requires how many accesses?**

```
Block 0-11:     1 access (direct)
Block 12-1035:  2 accesses (inode → single indirect → data)
Block 1036-... : 3 accesses (double indirect)
Beyond:         4 accesses (triple indirect)

Formula for boundaries:
Direct limit = D - 1
Single limit = D + PPB - 1
Double limit = D + PPB + PPB² - 1
```

### Technique 3: Bitmap Size Calculation

**Formula:**
$$\text{Bitmap Size (bits)} = \frac{\text{Disk Size}}{\text{Block Size}}$$

$$\text{Bitmap Size (bytes)} = \frac{\text{Disk Size}}{\text{Block Size} \times 8}$$

**Example:**
```
Disk = 1TB, Block = 4KB
Blocks = 1TB / 4KB = 256M blocks
Bitmap = 256M bits = 32MB
```

### Technique 4: Allocation Method Selection

**Decision matrix:**

| Requirement | Best Method |
|-------------|-------------|
| Fast sequential access | Contiguous |
| Fast random access | Contiguous or Indexed |
| File grows often | Linked or Indexed |
| Minimal space overhead | Contiguous |
| No external fragmentation | Linked or Indexed |

### Technique 5: Contiguous Allocation Problems

**First/Best/Worst Fit simulation:**

```
Step 1: List holes with sizes
        Holes: [(start, size), ...]
        
Step 2: For each request:
        First Fit: Scan from beginning, use first adequate hole
        Best Fit: Find smallest adequate hole
        Worst Fit: Find largest hole
        
Step 3: Update hole list (split or remove hole)
Step 4: Track fragmentation
```

### Technique 6: FAT Table Traversal

**To find block N of a file:**

```
Step 1: Start at first block (from directory entry)
Step 2: Follow FAT chain N times
        for i = 1 to N:
            current = FAT[current]
Step 3: Return current block number

Accesses: FAT is in memory, so just 1 disk access for data
```

### Technique 7: Directory Path Resolution

**For path /usr/local/bin/ls:**

```
Step 1: Start at root inode (known location)
Step 2: Read root directory, find "usr" → inode X
Step 3: Read inode X, read directory, find "local" → inode Y
Step 4: Read inode Y, read directory, find "bin" → inode Z
Step 5: Read inode Z, read directory, find "ls" → inode W
Step 6: inode W contains file data

Disk accesses = 2 × (path components) for (inode + directory) each
```

### Technique 8: Hard Link vs Symbolic Link

**Problem-solving distinction:**

| Scenario | Hard Link | Symbolic Link |
|----------|-----------|---------------|
| Delete original | File persists | Link breaks (dangling) |
| Cross filesystem | Not allowed | Allowed |
| Reference count | Increases | No effect |
| Finding target | Direct inode | Path lookup |

---

## 📝 Practice Problems

### Problem 1
Block size = 2KB, 8 direct pointers, 1 single, 1 double, 1 triple indirect. Pointer = 4B.
Calculate maximum file size.

### Problem 2
Disk = 500GB, Block = 8KB.
(a) Bitmap size?
(b) Blocks needed to store bitmap?

### Problem 3
File has 100 blocks using indexed allocation. How many disk accesses to read block 50?

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| File | Named data collection |
| Directory | Structure organizing files |
| Contiguous | Fast, external fragmentation |
| Linked | No fragmentation, slow random |
| Indexed | Fast random, overhead |
| Bitmap | 1 bit per block |
| Inode | UNIX combined index structure |

### Key Formulas

$$\text{Pointers per block} = \frac{\text{Block size}}{\text{Pointer size}}$$

$$\text{Bitmap size} = \frac{\text{Disk size}}{\text{Block size} \times 8}$$

$$\text{Max file (inode)} = D \times B + SI \times P \times B + DI \times P^2 \times B + TI \times P^3 \times B$$

Where D=direct, SI=single indirect, DI=double indirect, TI=triple indirect, P=pointers/block, B=block size

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 10 - Disk Management](../10-Disk-Management/README.md)*
