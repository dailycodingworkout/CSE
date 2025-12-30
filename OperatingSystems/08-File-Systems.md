# Chapter 8: File Systems

> **"A file system is like a library's cataloging system - it organizes books (files) so you can find them when needed"**

---

## 🎯 What is a File?

**Definition:** Named collection of related information stored on secondary storage

### File Attributes

| Attribute | Description |
|-----------|-------------|
| **Name** | Human-readable identifier |
| **Identifier** | Unique number (inode number in UNIX) |
| **Type** | Executable, text, binary, etc. |
| **Location** | Pointer to file location on disk |
| **Size** | Current size (bytes/blocks) |
| **Protection** | Access control information |
| **Time stamps** | Creation, modification, access times |
| **Owner** | User who owns the file |

---

### File Types

```
By Content:
┌────────────────────────────────────────────────┐
│ Executable  │ .exe, .bin, .out                 │
│ Object      │ .o, .obj                         │
│ Source      │ .c, .java, .py                   │
│ Text        │ .txt, .md                        │
│ Archive     │ .tar, .zip                       │
│ Multimedia  │ .mp3, .jpg, .mp4                 │
└────────────────────────────────────────────────┘
```

**Extension vs Magic Number:**
- Extension: Hint to users and applications
- Magic Number: Bytes at file start identifying type

---

### File Structure

| Structure | Description | Example |
|-----------|-------------|---------|
| **None (Byte Sequence)** | OS sees sequence of bytes | UNIX, Windows |
| **Simple Record** | Lines of fixed/variable length | Text files |
| **Complex** | Indexed, formatted | Databases |

---

## 📁 File Operations

### Basic Operations

```c
create()   - Create new file
open()     - Prepare file for access
read()     - Read data from file
write()    - Write data to file
seek()     - Reposition file pointer
close()    - Release file resources
delete()   - Remove file
truncate() - Set file size to zero
```

### Open File Table

```
System-wide Open File Table:     Per-Process Open File Table:
┌─────────────────────────┐     ┌─────────────────────────┐
│ inode                   │     │ Pointer to system table │
│ File size               │◄────│ Current position        │
│ Location on disk        │     │ Access mode             │
│ Open count              │     │ Pointer to next         │
└─────────────────────────┘     └─────────────────────────┘
```

**File Descriptor (fd):** Index into per-process table

---

### File Locking

| Type | Description |
|------|-------------|
| **Shared Lock** | Multiple readers, no writers |
| **Exclusive Lock** | One writer, no readers |
| **Advisory Lock** | Processes cooperate voluntarily |
| **Mandatory Lock** | OS enforces lock |

---

## 📂 Directory Structure

### Single-Level Directory

```
┌────────────────────────────────────────────────┐
│    file1  file2  file3  file4  file5           │
└────────────────────────────────────────────────┘
```

**Problems:** Naming conflicts, no grouping

---

### Two-Level Directory

```
┌─────────────────────────────────────────────────┐
│               Root Directory                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │ User1   │  │ User2   │  │ User3   │         │
│  └────┬────┘  └────┬────┘  └────┬────┘         │
│       │            │            │               │
│    ┌──┴──┐      ┌──┴──┐      ┌──┴──┐           │
│    │files│      │files│      │files│           │
└─────────────────────────────────────────────────┘
```

**Path:** /User1/file1

---

### Tree-Structured Directory

```
             ┌─────────────┐
             │    root     │
             └──────┬──────┘
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       ┌─────┐  ┌─────┐  ┌─────┐
       │home │  │ var │  │ etc │
       └──┬──┘  └─────┘  └─────┘
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
  user1 user2 user3
    │
 ┌──┼──┐
 ▼  ▼  ▼
doc bin src
```

**Absolute Path:** /home/user1/doc/file.txt
**Relative Path:** doc/file.txt (from user1)

---

### Acyclic Graph Directory

**Allows sharing:** Same file in multiple directories

```
         ┌──────────────┐
         │     root     │
         └──────┬───────┘
         ┌──────┼──────┐
         ▼      ▼      ▼
       dir1   dir2   dir3
         │      │      │
         └──────┼──────┘
                ▼
            shared_file
```

**Implementation:**
- **Hard Link:** Multiple directory entries point to same inode
- **Symbolic Link:** Special file containing path to target

**Deletion Problem:**
- Hard link: Delete when link count = 0
- Symbolic link: Dangling reference possible

---

### General Graph Directory

**Allows cycles** (not recommended)

**Problems:**
- Infinite loops in traversal
- File may never be deleted (cyclic reference)

**Solution:** Garbage collection or prohibit cycles

---

## 🗄️ File System Implementation

### On-Disk Structure

```
┌────────────────────────────────────────────────────────────┐
│ Boot  │ Super  │ Free Space │ inode   │ Data Blocks        │
│ Block │ Block  │ Management │ Table   │                    │
└────────────────────────────────────────────────────────────┘
```

| Component | Contents |
|-----------|----------|
| **Boot Block** | Bootstrap code |
| **Super Block** | File system metadata (size, block count, free blocks) |
| **Free Space** | Bitmap or linked list of free blocks |
| **inode Table** | File metadata (not name!) |
| **Data Blocks** | Actual file contents |

---

### Directory Implementation

**Linear List:**
```
┌────────────┬───────────────┐
│ file_name  │ inode_number  │
├────────────┼───────────────┤
│ "file1"    │     142       │
│ "file2"    │     87        │
│ "subdir"   │     203       │
└────────────┴───────────────┘

Search: O(n) - slow for large directories
```

**Hash Table:**
```
Hash(filename) → bucket → linear search within bucket
Search: O(1) average
```

**B+ Tree:** Used in NTFS, HFS+ for large directories

---

## 📦 File Allocation Methods

### 1️⃣ Contiguous Allocation

```
Directory Entry:
┌──────────────┬───────────┬────────┐
│ Filename     │ Start     │ Length │
│ "file1"      │ Block 19  │ 6      │
└──────────────┴───────────┴────────┘

Disk:
Block: 0 1 2 3 ... 18 [19 20 21 22 23 24] 25 26 ...
                       └─── file1 ────┘
```

**Advantages:**
- Simple implementation
- Excellent sequential access (no seek)
- Direct access: Block i at (start + i)

**Disadvantages:**
- External fragmentation
- File growth difficult
- Must know file size in advance

**💡 Use Case:** CD-ROM (read-only, sizes known)

---

### 2️⃣ Linked Allocation

```
Directory Entry:
┌──────────────┬───────────┬─────────┐
│ Filename     │ Start     │ End     │
│ "file1"      │ Block 9   │ Block 25│
└──────────────┴───────────┴─────────┘

Disk (each block has pointer to next):
Block 9 → Block 16 → Block 1 → Block 10 → Block 25 → null
  data      data       data      data       data
  [next]    [next]     [next]    [next]     [next]
```

**Advantages:**
- No external fragmentation
- File can grow easily
- No need to declare size

**Disadvantages:**
- Poor random access: O(n) to reach block n
- Pointer overhead (part of each block)
- Reliability (lost pointer = lost file)

---

#### FAT (File Allocation Table)

**Move pointers to separate table:**

```
FAT:                          Directory:
Block   Next                  file1: start = 217
217     618                   file2: start = 339
618     EOF
339     340
340     EOF

Advantage: FAT can be cached in memory
```

---

### 3️⃣ Indexed Allocation

```
Directory Entry:
┌──────────────┬─────────────┐
│ Filename     │ Index Block │
│ "file1"      │ Block 19    │
└──────────────┴─────────────┘

Index Block (Block 19):      Data Blocks:
┌────────────────┐           
│ Pointer to 9   │───────────► Block 9 (data)
│ Pointer to 16  │───────────► Block 16 (data)
│ Pointer to 1   │───────────► Block 1 (data)
│ Pointer to 10  │───────────► Block 10 (data)
│ null           │
└────────────────┘
```

**Advantages:**
- Direct access without traversing
- No external fragmentation

**Disadvantages:**
- Index block overhead
- Index block size limits file size

---

#### Handling Large Files

**Linked Index Blocks:**
```
Index Block 1 → Index Block 2 → Index Block 3
     │               │               │
     ▼               ▼               ▼
  [pointers]     [pointers]     [pointers]
```

**Multi-level Index:**
```
        1st Level Index
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
    2nd     2nd     2nd
    Level   Level   Level
```

---

### UNIX inode Structure (Combined Scheme)

```
┌────────────────────────────────────────────────┐
│              inode                             │
├────────────────────────────────────────────────┤
│ Mode (permissions)                             │
│ Owner, Group                                   │
│ Size                                           │
│ Timestamps                                     │
│ Link count                                     │
├────────────────────────────────────────────────┤
│ Direct pointers (12)         → Data blocks     │
│ Single indirect pointer      → Index block     │
│ Double indirect pointer      → Index → Index   │
│ Triple indirect pointer      → Index → Index → Index │
└────────────────────────────────────────────────┘
```

**Maximum File Size Calculation:**

```
Block size = 4 KB
Pointer size = 4 bytes
Pointers per block = 4096/4 = 1024

Direct: 12 × 4KB = 48 KB
Single: 1024 × 4KB = 4 MB
Double: 1024 × 1024 × 4KB = 4 GB
Triple: 1024 × 1024 × 1024 × 4KB = 4 TB

Total: ~4 TB
```

---

### Allocation Comparison

| Aspect | Contiguous | Linked | Indexed |
|--------|-----------|--------|---------|
| Sequential | Excellent | Good | Good |
| Random | Good | Poor | Good |
| Space | External frag | Pointer overhead | Index overhead |
| Growth | Difficult | Easy | Easy |

---

## 🆓 Free Space Management

### 1️⃣ Bitmap (Bit Vector)

```
Block:  0 1 2 3 4 5 6 7 8 9 ...
Bitmap: 1 1 0 1 1 0 0 1 1 1 ...
        │ │ ▲ │ │ ▲ ▲
        │ │ │ │ │ │ └── Free
        │ │ │ │ │ └──── Free
        │ │ │ │ └────── Allocated
        │ │ │ └──────── Allocated
        │ │ └────────── Free
        │ └──────────── Allocated
        └────────────── Allocated
```

**Find free block:** Scan for first 0
**Find contiguous:** Scan for consecutive 0s

**Space:** 1 bit per block
```
1 TB disk, 4 KB blocks = 256M blocks = 32 MB bitmap
```

---

### 2️⃣ Linked List

```
Free Block → Free Block → Free Block → null
    10     →     32     →     45     →
```

**Problem:** Traversal expensive
**Optimization:** Store multiple pointers in each free block

---

### 3️⃣ Grouping

```
First free block contains:
- Addresses of n free blocks
- Last address points to another block with more addresses
```

---

### 4️⃣ Counting

```
Keep (start, count) pairs:
(Block 2, 3)  → Blocks 2, 3, 4 are free
(Block 17, 5) → Blocks 17-21 are free
```

**Best when:** Free blocks are contiguous (common)

---

## ⚡ File System Performance

### Caching

**Buffer Cache:** Recently used disk blocks in memory

```
         ┌─────────┐
   CPU ─►│ Buffer  │─► Disk
         │ Cache   │
         └─────────┘
         
Read: Check cache first
Write: Write to cache, sync later
```

**Read-Ahead:** Prefetch sequential blocks

---

### Write Policies

| Policy | Description | Risk |
|--------|-------------|------|
| **Synchronous** | Write to disk immediately | Slow, safe |
| **Asynchronous** | Write to cache, later to disk | Fast, risky |
| **Write-Behind** | Batch writes periodically | Balanced |

---

## 🔒 File System Protection

### Access Control List (ACL)

```
file1:
  owner: read, write, execute
  group: read, execute
  others: read
  specific_user1: write
  specific_group2: execute
```

### UNIX Permission Bits

```
      Owner  Group  Others
      rwx    rwx    rwx
      421    421    421
      
Example: 755 = rwxr-xr-x
         Owner: 7 (rwx)
         Group: 5 (r-x)
         Others: 5 (r-x)
```

---

## 📊 File System Types

### Common File Systems

| File System | OS | Max File Size | Features |
|-------------|----|--------------|----|
| FAT32 | Windows/Linux | 4 GB | Simple, universal |
| NTFS | Windows | 16 EB | Journaling, ACL |
| ext4 | Linux | 16 TB | Journaling, extents |
| HFS+ | macOS | 8 EB | Journaling |
| ZFS | Solaris/FreeBSD | 16 EB | RAID, snapshots |

---

### Journaling

**Problem:** Crash during write leaves inconsistent state

**Solution:** Write changes to journal first

```
1. Write changes to journal (log)
2. Apply changes to file system
3. Mark journal entry as complete
4. If crash: replay journal on recovery
```

**Journal Types:**
- **Metadata journaling:** Only file system metadata
- **Full journaling:** Data and metadata (slower, safer)

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **inode calculation:** Max file size
2. **Block addressing:** Direct/indirect access
3. **Allocation method comparison:** Which is better when
4. **Free space bitmap:** Calculate size
5. **Directory structure:** Path resolution

### ⚠️ Edge Cases:
1. **inode doesn't contain filename** (directory does)
2. **Hard link shares inode** (soft link has own inode)
3. **Root inode is typically inode 2**
4. **Indirect blocks count toward disk usage**

---

## 🎯 Quick Revision Points

```
✓ File = named data + attributes
✓ inode = file metadata (not name)
✓ Directory = mapping (name → inode)
✓ Contiguous: Fast but external fragmentation
✓ Linked: No fragmentation but slow random access
✓ Indexed: Best of both but overhead
✓ UNIX: 12 direct + single + double + triple indirect
✓ Bitmap: 1 bit per block
✓ Hard link: Same inode, link count++
✓ Soft link: Separate file with path
✓ Journaling: Crash recovery
```

---

## 📚 Key Formulas

```
Bitmap size = Total blocks / 8 bytes

UNIX file size (block size B, pointer size P):
Direct = 12 × B
Single indirect = (B/P) × B
Double indirect = (B/P)² × B
Triple indirect = (B/P)³ × B

Pointers per block = Block size / Pointer size

FAT table size = Total blocks × Entry size
```

---

[← Previous: Virtual Memory](./07-Virtual-Memory.md) | [Next: I/O Systems →](./09-IO-Systems.md)
