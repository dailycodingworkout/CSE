# Chapter 9: File Systems

## 🎯 The Atomic Truth
> **File System = Name Data + Organize Data + Store Data Persistently**

---

## 🧠 The WHY of File Systems

### The Problem
- Data must survive power off
- Users want to name their data
- Multiple users need to share data
- Need efficient storage and retrieval

### The Solution
```
FILE SYSTEM:

┌─────────────────────────────────────────────────────────────┐
│ USER VIEW:        /home/user/document.txt                    │
│                                                              │
│ FILE SYSTEM:      Logical organization + metadata            │
│                                                              │
│ STORAGE:          Blocks on disk                             │
└─────────────────────────────────────────────────────────────┘

User sees: Named files in directories
Reality: Bits scattered across disk blocks
```

---

## 📄 File Concepts

### What is a File?

**File**: Named collection of related information stored on secondary storage.

### File Attributes

| Attribute | Description |
|-----------|-------------|
| **Name** | Human-readable identifier |
| **Identifier** | Unique tag (inode number) |
| **Type** | Extension or magic number |
| **Location** | Pointer to device and block |
| **Size** | Current and maximum |
| **Protection** | Access control (rwx) |
| **Time** | Created, modified, accessed |
| **Owner** | User who owns file |

### File Operations

```
BASIC OPERATIONS:

Create    → Allocate space, create directory entry
Delete    → Free space, remove directory entry
Open      → Fetch attributes to memory, return handle
Close     → Write back changes, free memory structures
Read      → Transfer data from disk to memory
Write     → Transfer data from memory to disk
Seek      → Move file pointer (random access)
Truncate  → Reduce file to zero length, keep attributes
```

### Open File Table

```
SYSTEM-WIDE OPEN FILE TABLE:
┌───────────────────────────────────────────────────────────┐
│ Entry │ File Pointer │ Disk Location │ Access Count │ ... │
├───────┼──────────────┼───────────────┼──────────────┼─────┤
│   0   │    1024      │   Block 500   │      3       │     │
│   1   │    0         │   Block 123   │      1       │     │
└───────┴──────────────┴───────────────┴──────────────┴─────┘

PER-PROCESS OPEN FILE TABLE:
┌───────────────────────────────────────────────────────────┐
│ fd  │ Pointer to System Table │ Mode │ File Position │    │
├─────┼─────────────────────────┼──────┼───────────────┼────┤
│  3  │         Entry 0         │  R   │    1024       │    │
│  4  │         Entry 1         │  RW  │    0          │    │
└─────┴─────────────────────────┴──────┴───────────────┴────┘
```

---

## 📁 Directory Structure

### What is a Directory?

**Directory**: Collection of nodes containing information about files.

### Operations on Directories

- Search for file
- Create/Delete file
- List contents
- Rename file
- Traverse file system

---

## 🏗️ Directory Organization

### 1. Single-Level Directory

**All files in one directory.**

```
ROOT DIRECTORY:
┌─────────────────────────────────────────────────────────┐
│ file1.txt │ file2.txt │ data.csv │ image.png │ ...     │
└─────────────────────────────────────────────────────────┘
```

| Pros | Cons |
|------|------|
| Simple | Naming conflicts |
| Easy to implement | No grouping |
| | Doesn't scale |

### 2. Two-Level Directory

**Separate directory per user.**

```
MASTER FILE DIRECTORY:
         ┌─────────────────────────────────────┐
         │ user1 │ user2 │ user3 │ user4 │ ... │
         └───┬───┴───┬───┴───┬───┴───────┴─────┘
             │       │       │
             ↓       ↓       ↓
         ┌──────┐ ┌──────┐ ┌──────┐
         │file1 │ │fileA │ │doc1  │
         │file2 │ │fileB │ │doc2  │
         └──────┘ └──────┘ └──────┘
```

| Pros | Cons |
|------|------|
| Isolation between users | No user-defined grouping |
| Unique names per user | No sharing |

### 3. Tree-Structured Directory

**Hierarchical, like folders.**

```
                    / (root)
                    │
        ┌───────────┼───────────┐
        │           │           │
       home        etc        var
        │           │           │
    ┌───┴───┐     ┌─┴─┐      ┌──┴──┐
   user1  user2  passwd    log  cache
    │       │      │        │
  ┌─┴─┐   ┌─┴─┐           ┌─┴─┐
 docs code bin           sys app
```

**Path Types**:
- **Absolute**: /home/user1/docs/file.txt
- **Relative**: ../user2/code (from user1)

### 4. Acyclic-Graph Directory

**Allows sharing via links (no cycles).**

```
        /home/user1                   /home/user2
             │                              │
         ┌───┴───┐                          │
        docs   shared ─────────────────────→│
         │                                  │
      file.txt                              │
         ↑                                  │
         └──────────────────────────────────┘
                    (Link to same file)
```

**Implementation**: 
- **Hard Link**: Multiple directory entries point to same inode
- **Soft Link (Symbolic)**: File contains path to target

| Link Type | Same inode? | Cross filesystem? | Survives deletion? |
|-----------|-------------|-------------------|-------------------|
| **Hard** | Yes | No | Yes (until count=0) |
| **Soft** | No | Yes | No (dangling link) |

### 5. General Graph Directory

**Allows cycles (complex, needs cycle detection).**

---

## 💾 File Allocation Methods

### The Problem
How to allocate disk blocks to files?

---

### 1. Contiguous Allocation

**Each file occupies contiguous blocks.**

```
DIRECTORY ENTRY:
┌──────────┬───────────────┬────────────┐
│ Filename │ Start Block   │ Length     │
├──────────┼───────────────┼────────────┤
│ file.txt │     14        │     5      │
└──────────┴───────────────┴────────────┘

DISK:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │...│12 │13 │ 14│ 15│ 16│ 17│ 18│19 │20 │...│   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                           └───────file.txt───────┘
```

| Pros | Cons |
|------|------|
| Simple | External fragmentation |
| Fast sequential access | Hard to grow files |
| Fast random access | Need to know size in advance |

**Use Case**: CD-ROM, DVD (read-only, known sizes)

---

### 2. Linked Allocation

**Each block contains pointer to next block.**

```
DIRECTORY ENTRY:
┌──────────┬───────────────┬─────────────┐
│ Filename │ Start Block   │ End Block   │
├──────────┼───────────────┼─────────────┤
│ file.txt │      9        │     25      │
└──────────┴───────────────┴─────────────┘

BLOCKS (each has pointer to next):
┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
│ Block 9│───→│Block 16│───→│Block 1 │───→│Block 25│───→ NULL
│  Data  │    │  Data  │    │  Data  │    │  Data  │
└────────┘    └────────┘    └────────┘    └────────┘
```

| Pros | Cons |
|------|------|
| No external fragmentation | Slow random access (O(n)) |
| Files can grow easily | Pointer overhead |
| No compaction needed | Reliability (pointer corruption) |

**FAT (File Allocation Table)**: Variation where pointers stored in separate table.

```
FAT:
┌───────────┬─────────────┐
│ Block #   │ Next Block  │
├───────────┼─────────────┤
│    0      │     -1      │ (free or end)
│    1      │     25      │
│    9      │     16      │
│   16      │      1      │
│   25      │     -1      │ (end of file)
└───────────┴─────────────┘
```

---

### 3. Indexed Allocation

**Index block contains pointers to all data blocks.**

```
DIRECTORY ENTRY:
┌──────────┬───────────────┐
│ Filename │ Index Block   │
├──────────┼───────────────┤
│ file.txt │     19        │
└──────────┴───────────────┘

INDEX BLOCK 19:             DATA BLOCKS:
┌─────────────┐            ┌────────┐
│ ptr → 9     │───────────→│Block 9 │ Data...
│ ptr → 16    │───────────→│Block 16│ Data...
│ ptr → 1     │───────────→│Block 1 │ Data...
│ ptr → 25    │───────────→│Block 25│ Data...
│ null        │
│ ...         │
└─────────────┘
```

| Pros | Cons |
|------|------|
| No external fragmentation | Index block overhead |
| Fast random access | Wasted space for small files |
| Supports direct access | Limited file size (one index block) |

### Handling Large Files

#### Linked Scheme
Index blocks linked together.

#### Multi-level Index
Index block points to other index blocks.

```
MULTI-LEVEL INDEX:

┌──────────────┐
│ Main Index   │
│ ptr → Index1 │───→ ┌─────────┐
│ ptr → Index2 │     │ Index 1 │
│ ...          │     │ptr→data │
└──────────────┘     │ptr→data │
                     └─────────┘
```

#### Combined Scheme (UNIX inode)

```
INODE STRUCTURE:
┌─────────────────────────────────────┐
│ Mode, Owner, Size, Timestamps...    │
├─────────────────────────────────────┤
│ Direct Blocks (12 pointers)         │───→ Data
├─────────────────────────────────────┤
│ Single Indirect                     │───→ Index → Data
├─────────────────────────────────────┤
│ Double Indirect                     │───→ Index → Index → Data
├─────────────────────────────────────┤
│ Triple Indirect                     │───→ Index → Index → Index → Data
└─────────────────────────────────────┘
```

---

### Allocation Method Comparison

| Method | Sequential | Random | Space | Growth |
|--------|------------|--------|-------|--------|
| **Contiguous** | Excellent | Excellent | Fragmentation | Hard |
| **Linked** | Good | Poor | Good | Easy |
| **Indexed** | Good | Good | Index overhead | Easy |

---

## 🆓 Free Space Management

### How to Track Free Blocks?

---

### 1. Bit Vector (Bitmap)

**One bit per block: 1 = free, 0 = used.**

```
Block:  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
Bitmap: 0  0  1  1  0  0  0  1  0  0  1  1  0  0  1  0
             ↑  ↑           ↑        ↑  ↑        ↑
           Free blocks: 2, 3, 7, 10, 11, 14
```

| Pros | Cons |
|------|------|
| Simple | Large for huge disks |
| Fast consecutive block finding | |

**Space**: n blocks need n bits = n/8 bytes

**Example**: 1 TB disk, 4 KB blocks
- Blocks = 1TB / 4KB = 256M blocks
- Bitmap = 256M bits = 32 MB

---

### 2. Linked List

**Free blocks linked together.**

```
Free List Head → Block 2 → Block 7 → Block 14 → Block 3 → NULL
```

| Pros | Cons |
|------|------|
| Uses free blocks themselves | Slow to find consecutive |
| No extra space | Need to traverse list |

---

### 3. Grouping

**First free block stores addresses of n free blocks. Last points to another group.**

```
┌────────────────────────────────┐
│ Block 2: [5, 7, 9, 14, 22, →] │───→ ┌────────────────┐
│          (next group)          │     │ Block 22: ...  │
└────────────────────────────────┘     └────────────────┘
```

---

### 4. Counting

**Store: (first_free_block, count) pairs.**

```
Free List:
(Block 2, 3)  → Blocks 2, 3, 4 are free
(Block 10, 5) → Blocks 10, 11, 12, 13, 14 are free
```

Best when consecutive blocks often freed together.

---

## 🧮 GATE Numerical Examples

### Example 1: Indexed Allocation File Size

**Given**:
- Block size: 1 KB
- Block pointer: 4 bytes
- One index block

**Find**: Maximum file size

**Solution**:
- Pointers per index block = 1024 / 4 = 256
- Max file = 256 × 1 KB = **256 KB**

---

### Example 2: Multi-level Index

**Given**:
- Block size: 4 KB
- Pointer size: 4 bytes
- Two-level indexing

**Find**: Maximum file size

**Solution**:
- Pointers per block = 4096 / 4 = 1024
- Level 1: 1024 pointers to level 2 blocks
- Level 2: 1024 pointers to data blocks each
- Total data blocks = 1024 × 1024 = 1M
- Max file = 1M × 4 KB = **4 GB**

---

### Example 3: Bitmap Size

**Given**:
- Disk: 2 TB
- Block size: 8 KB

**Find**: Bitmap size

**Solution**:
- Total blocks = 2 TB / 8 KB = 2 × 2⁴⁰ / 2¹³ = 2²⁷ blocks
- Bitmap = 2²⁷ bits = 2²⁴ bytes = **16 MB**

---

### Example 4: UNIX inode

**Given**:
- Block size: 4 KB
- Pointer size: 4 bytes
- 12 direct, 1 single indirect, 1 double indirect, 1 triple indirect

**Find**: Maximum file size

**Solution**:
- Pointers per block = 4096 / 4 = 1024
- Direct: 12 × 4 KB = 48 KB
- Single: 1024 × 4 KB = 4 MB
- Double: 1024² × 4 KB = 4 GB
- Triple: 1024³ × 4 KB = 4 TB
- **Max = 48 KB + 4 MB + 4 GB + 4 TB ≈ 4 TB**

---

## 🎯 GATE Traps and Anti-Solutions

### Trap 1: Contiguous vs Linked
- Contiguous: Best for read-only media
- Linked: External fragmentation = NONE

### Trap 2: FAT Location
- FAT is stored SEPARATELY from data blocks
- Not inline with data

### Trap 3: Hard vs Soft Links
- Hard link deletion: File exists until all links deleted
- Soft link deletion: Original deleted = dangling link

### Trap 4: Index Block Size
- Large files need multi-level indexing
- Small files waste index block space

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2018)
**Which allocation method has no external fragmentation?**

(A) Contiguous  
(B) Linked ✓  
(C) Both  
(D) None

---

### Q2: (GATE 2019)
**In UNIX, which is used for file allocation?**

(A) Contiguous  
(B) Linked  
(C) Indexed (inode-based) ✓  
(D) FAT

---

### Q3: (GATE 2017)
**Hard link differs from soft link in:**

(A) Hard links can cross file systems  
(B) Hard links share the same inode ✓  
(C) Soft links survive original deletion  
(D) Both are identical

---

## ⚡ The 5-Second Snap-Check

1. **No fragmentation?** → Linked allocation
2. **Fast random access?** → Contiguous or Indexed
3. **UNIX files?** → inode with direct + indirect blocks
4. **Bitmap size?** → Total blocks / 8 bytes

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Contiguous | Fast but fragments externally |
| Linked | No fragmentation but slow random access |
| Indexed | Best of both, overhead for small files |
| FAT | Linked with separate table |
| inode | Direct + 3 levels of indirect |
| Hard Link | Same inode, can't cross filesystems |
| Soft Link | Path-based, can dangle |
| Bitmap | 1 bit per block |

---

*Next Chapter: [Disk Management →](10-Disk-Management.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
