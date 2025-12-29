# Chapter 9: File Organization & Indexing

---

## 🎯 Why File Organization Matters?

**Goal**: Minimize disk I/O operations
- Disk access is ~100,000x slower than memory
- Efficient organization = Faster queries

### 🎭 Analogy
> File organization = **Library organization**
> - Random shelving → Slow search
> - Organized by author/subject → Fast lookup

---

## 💾 Storage Hierarchy

```
┌──────────────────────────────────────────────────────────────┐
│                        CPU REGISTERS                          │
│                     (Fastest, Smallest)                       │
├──────────────────────────────────────────────────────────────┤
│                         L1 CACHE                              │
├──────────────────────────────────────────────────────────────┤
│                         L2 CACHE                              │
├──────────────────────────────────────────────────────────────┤
│                          L3 CACHE                             │
├──────────────────────────────────────────────────────────────┤
│                        MAIN MEMORY                            │
│                          (RAM)                                │
├──────────────────────────────────────────────────────────────┤
│                     SECONDARY STORAGE                         │
│                    (SSD, HDD) ← DBMS Focus                    │
├──────────────────────────────────────────────────────────────┤
│                      TERTIARY STORAGE                         │
│                  (Tape, Optical) - Backup                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 📦 Disk Structure

### Physical Components

```
           ┌────────────────────────────┐
           │        PLATTER             │
           │   ┌──────────────────┐     │
           │   │    ◄─ Track      │     │
           │   │  ┌────────────┐  │     │
           │   │  │            │  │     │
           │   │  │  ◄─ Sector │  │     │
           │   │  └────────────┘  │     │
           │   └──────────────────┘     │
           │                            │
           │        Spindle ─►  •       │
           └────────────────────────────┘
                              │
                         Read/Write Head
```

### Key Terms

| Term | Definition |
|------|------------|
| **Platter** | Circular disk surface |
| **Track** | Concentric circle on platter |
| **Sector** | Arc segment of track (512B - 4KB) |
| **Block/Page** | Unit of data transfer (4KB - 64KB) |
| **Cylinder** | Same track on all platters |

### Disk Access Time

```
Total Time = Seek Time + Rotational Latency + Transfer Time

Seek Time: Move head to correct track (~5-10ms)
Rotational Latency: Wait for sector to rotate under head (~4ms for 7200 RPM)
Transfer Time: Read/write data (~0.1ms per block)
```

### 🧠 Key Insight
> **Seek time dominates!**
> Minimize random seeks, prefer sequential access.

---

## 📊 File Organization Methods

### 1. Heap/Pile File Organization
Records stored in **order of insertion** (unordered).

```
┌────────────────────────────────────────┐
│ Rec5 │ Rec2 │ Rec8 │ Rec1 │ Rec4 │... │
└────────────────────────────────────────┘
        (No particular order)
```

| Operation | Cost |
|-----------|------|
| Insert | O(1) - Append to end |
| Search | O(n) - Linear scan |
| Delete | O(n) - Find + Mark deleted |
| Update | O(n) - Find + Modify |

**Best for**: Bulk loading, OLTP with mostly inserts

### 2. Sequential/Sorted File Organization
Records stored in **sorted order** by key.

```
┌────────────────────────────────────────┐
│ Rec1 │ Rec2 │ Rec4 │ Rec5 │ Rec8 │... │
└────────────────────────────────────────┘
        (Sorted by primary key)
```

| Operation | Cost |
|-----------|------|
| Insert | O(n) - Find position + Shift |
| Search | O(log n) - Binary search |
| Delete | O(n) - Find + Shift |
| Range Query | Excellent - Sequential access |

**Best for**: Range queries, ordered retrieval

### 3. Hash File Organization
Records stored using **hash function** on key.

```
Hash(Key) → Bucket Number

┌─────┐
│  0  │ → [Records with Hash(key)=0]
├─────┤
│  1  │ → [Records with Hash(key)=1]
├─────┤
│ ... │
├─────┤
│  n  │ → [Records with Hash(key)=n]
└─────┘
```

| Operation | Cost |
|-----------|------|
| Insert | O(1) average |
| Search (equality) | O(1) average |
| Search (range) | O(n) - Hash destroys order! |
| Delete | O(1) average |

**Best for**: Equality searches, point queries

### 4. Clustered File Organization
Related records from **different tables** stored together.

```
Student-Department clustered:
┌─────────────────────────────────────────────────┐
│ Dept:CS │ Stud:Alice│ Stud:Bob│ Stud:Carol│    │
│ Dept:EE │ Stud:Dave │ Stud:Eve │              │
└─────────────────────────────────────────────────┘
```

**Best for**: Frequent joins between tables

---

## 📈 Indexing Fundamentals

### What is an Index?

An **index** is a data structure that speeds up data retrieval.

### 🎭 Analogy
> Index = **Book's index**
> - Without index: Read every page
> - With index: Jump to exact page

### Index Entry Structure
```
┌──────────────────┬──────────────────┐
│   Search Key     │    Pointer       │
│   (indexed attr) │ (to record/block)│
└──────────────────┴──────────────────┘
```

---

## 📊 Types of Indexes

### By Ordering

#### 1. Primary Index (Clustering Index)
- Index on **ordering key** of sorted file
- One index entry per **block** (sparse)
- File is physically sorted on index key

```
Data file sorted by Roll:
Block 1: [Roll 1-10]
Block 2: [Roll 11-20]
Block 3: [Roll 21-30]

Primary Index:
┌──────┬─────────┐
│  1   │ Block 1 │
│ 11   │ Block 2 │
│ 21   │ Block 3 │
└──────┴─────────┘
(One entry per block, first key of block)
```

#### 2. Secondary Index
- Index on **non-ordering** attribute
- One index entry per **record** (dense)
- File NOT sorted on index key

```
Data file (any order):
Block 1: [CGPA: 8.5, 9.0, 7.5]
Block 2: [CGPA: 9.5, 8.0, 6.5]

Secondary Index on CGPA:
┌──────┬───────────────┐
│ 6.5  │ Block 2, Rec3 │
│ 7.5  │ Block 1, Rec3 │
│ 8.0  │ Block 2, Rec2 │
│ 8.5  │ Block 1, Rec1 │
│ 9.0  │ Block 1, Rec2 │
│ 9.5  │ Block 2, Rec1 │
└──────┴───────────────┘
(One entry per record - Dense)
```

### Dense vs Sparse Index

| Type | Index Entries | Requirement |
|------|---------------|-------------|
| **Dense** | One per record | Works on any file |
| **Sparse** | One per block | Requires sorted file |

```
Dense Index:
┌───────────────────────────────────────┐
│ K1→R1 │ K2→R2 │ K3→R3 │ K4→R4 │...   │
└───────────────────────────────────────┘

Sparse Index:
┌───────────────────────────────────────┐
│ K1→B1  │  K4→B2  │  K7→B3  │...      │
└───────────────────────────────────────┘
(First key of each block only)
```

---

## 📊 Multi-Level Index

### Problem
Large index may not fit in memory → Multiple disk accesses

### Solution
Build index on index (meta-index)

```
                    Level 2 (Master Index)
                    ┌───────────────────┐
                    │ 1→L1.1 │100→L1.2 │
                    └───────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
       Level 1                        Level 1
    ┌───────────┐                  ┌───────────┐
    │ 1→D1      │                  │ 100→D4    │
    │ 25→D2    │                  │ 125→D5   │
    │ 50→D3    │                  │ 150→D6   │
    └───────────┘                  └───────────┘
            │                             │
            ▼                             ▼
         DATA                          DATA
```

### Number of Levels
```
If blocking factor of index = bfr_i
And total records = n

Level 1: ⌈n / bfr_i⌉ blocks
Level 2: ⌈Level1 / bfr_i⌉ blocks
...until 1 block

Number of levels = ⌈log_{bfr_i}(n)⌉
```

---

## 🌳 B-Tree

### Properties
1. **Balanced**: All leaves at same level
2. Each node has between ⌈n/2⌉ and n children
3. Root has at least 2 children (unless leaf)
4. All leaves at same depth

### Node Structure
```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ P0  │ K1  │ P1  │ K2  │ P2  │ ... │ Pn  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┘

P_i = Pointer to child
K_i = Key value
Data pointer stored with each key (in B-tree)
```

### B-Tree Parameters

| Parameter | Value |
|-----------|-------|
| Order (n) | Max children per node |
| Max keys per node | n - 1 |
| Min keys per node (non-root) | ⌈n/2⌉ - 1 |
| Max children | n |
| Min children (non-root) | ⌈n/2⌉ |

### B-Tree Operations

| Operation | Complexity |
|-----------|------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

---

## 🌳 B+ Tree (GATE Favorite!)

### Key Difference from B-Tree
1. **Data pointers only at leaves**
2. **Leaves linked** for range queries
3. Internal nodes only for navigation

### Structure

```
                    [50]                    Internal
                   /    \                   Node
                  /      \
            [20|35]      [65|80]            Internal
           /  |  \       /  |  \            Nodes
          /   |   \     /   |   \
        [10|15] [20|25|30] [35|40|45] [50|55|60] [65|70|75] [80|85|90]
                                                                  ↓
                        Leaf nodes linked → → → → → → → → → → → →
```

### B+ Tree Properties

| Parameter | Value |
|-----------|-------|
| Order (n) | Max pointers per node |
| Internal node: Max keys | n - 1 |
| Internal node: Max children | n |
| Leaf node: Max records | n - 1 (or varies) |
| Leaf node: Min records | ⌈(n-1)/2⌉ |

### 🔢 B+ Tree Formulas (GATE Critical!)

#### For Internal Nodes
```
Max keys = n - 1
Max children (pointers) = n
Min children (non-root) = ⌈n/2⌉
Min keys (non-root) = ⌈n/2⌉ - 1
```

#### For Leaf Nodes
```
Max records = n - 1 (or specific to implementation)
Min records = ⌈(n-1)/2⌉
```

#### Height Calculation
```
With N records and order n:

Min height = ⌈log_n(N)⌉
Max height = ⌈log_{⌈n/2⌉}(N/2)⌉ + 1

For max records with height h:
Max records = (n-1) × n^(h-1) leaf nodes × records per leaf
```

### B+ Tree vs B-Tree

| Aspect | B-Tree | B+ Tree |
|--------|--------|---------|
| Data location | All nodes | Leaves only |
| Leaf links | No | Yes (linked list) |
| Range query | Poor | Excellent |
| Storage | Less efficient | More efficient |
| Internal traversal | May find data early | Must reach leaf |

### 🎯 Why B+ Tree is Preferred

1. **More keys per node** (no data pointers in internal nodes)
2. **Sequential access** via leaf links
3. **Predictable access time** (always go to leaf)
4. **Better cache utilization**

---

## #️⃣ Hashing

### Static Hashing
Fixed number of buckets.

```
Hash Function: h(key) = key mod m

m = 10 buckets (0-9)

h(25) = 25 mod 10 = 5 → Bucket 5
h(45) = 45 mod 10 = 5 → Bucket 5 (Collision!)
```

### Collision Handling

#### 1. Open Addressing
```
Linear Probing: Try next bucket
h'(k,i) = (h(k) + i) mod m

Quadratic Probing: Try i² positions away
h'(k,i) = (h(k) + c₁i + c₂i²) mod m
```

#### 2. Chaining (Overflow Buckets)
```
Bucket 5 → [25] → [45] → [55] → NULL
                  (Linked list of collisions)
```

### Static Hashing Problem
- Fixed buckets → Overflow or waste
- Can't adapt to data growth

---

## #️⃣ Dynamic Hashing

### Extendible Hashing
Uses **directory** that can grow/shrink.

```
Global Depth = 2 (use 2 bits of hash)

Directory:
00 → Bucket A (Local Depth 2)
01 → Bucket B (Local Depth 2)
10 → Bucket C (Local Depth 1)
11 → Bucket C (Same bucket!)
```

### Key Concepts
- **Global Depth**: Bits used by directory
- **Local Depth**: Bits used by bucket
- When bucket overflows and Local = Global: Double directory
- When bucket overflows and Local < Global: Split bucket only

### Linear Hashing
- Buckets added **one at a time** in round-robin
- Uses **split pointer** to track next bucket to split
- No directory needed

---

## 📊 Index Selection Guidelines

| Query Type | Best Index |
|------------|------------|
| Equality (WHERE key = value) | Hash or B+ Tree |
| Range (WHERE key BETWEEN a AND b) | B+ Tree |
| Ordering (ORDER BY key) | B+ Tree |
| Pattern (WHERE name LIKE 'A%') | B+ Tree |
| Join | B+ Tree (usually) |

---

## 📐 Important Formulas

### Blocking Factor
```
bfr = ⌊Block Size / Record Size⌋
```

### Number of Blocks
```
Number of blocks = ⌈Total Records / Blocking Factor⌉
```

### Index Size Calculation
```
Index Entry Size = Key Size + Pointer Size
Index Blocking Factor = ⌊Block Size / Index Entry Size⌋
Index Blocks = ⌈Number of Records / Index BF⌉  (for dense)
Index Blocks = ⌈Number of Data Blocks / Index BF⌉  (for sparse)
```

### B+ Tree Calculations

```
Given:
- Block size = B
- Key size = K
- Pointer size = P
- Record size = R

Order n = ⌊(B - P) / (K + P)⌋ + 1
(Derived from: n×P + (n-1)×K ≤ B)

Max records for height h:
= (n-1) × n^(h-1) × (leaf capacity)

Height for N records:
h = ⌈log_{⌈n/2⌉}(N)⌉
```

---

## ⚠️ Common GATE Traps

### Trap 1: B vs B+ Tree Order
```
B-Tree: Order = max children
B+ Tree: Order can mean max children OR max keys (clarify!)
```

### Trap 2: Primary vs Clustering Index
```
Primary Index = Index on primary key of sorted file (sparse)
Clustering Index = Index on non-key attribute of sorted file
Secondary Index = Index on unsorted attribute (dense)
```

### Trap 3: Leaf Capacity
```
B+ Tree leaf stores actual data OR data pointers
Internal node: (n-1) keys, n pointers
Leaf node: capacity may be calculated differently
```

### Trap 4: Minimum Fill
```
Non-root internal: ⌈n/2⌉ children
Non-root leaf: ⌈(n-1)/2⌉ records
Root: Minimum 1 key (2 children if internal)
```

---

## 🧪 Practice Problems

### Q1: B+ Tree Order
```
Block size = 512 bytes
Key size = 10 bytes
Pointer size = 6 bytes

Order n = ⌊(512 - 6) / (10 + 6)⌋ + 1
        = ⌊506 / 16⌋ + 1
        = 31 + 1
        = 32

Each internal node: up to 31 keys, 32 pointers
```

### Q2: Height Calculation
```
N = 1,000,000 records
Order n = 100

Min height = ⌈log₁₀₀(1,000,000)⌉
           = ⌈3⌉ = 3

Access = 3 disk reads (one per level)
```

### Q3: Dense vs Sparse
```
10,000 records
Block size = 1024 bytes
Record size = 100 bytes
Key size = 10 bytes
Pointer size = 6 bytes

Data blocks = ⌈10000 / ⌊1024/100⌋⌉ = ⌈10000/10⌉ = 1000

Dense index entries = 10,000
Sparse index entries = 1,000

Index entry size = 10 + 6 = 16
Index blocking factor = ⌊1024/16⌋ = 64

Dense index blocks = ⌈10000/64⌉ = 157
Sparse index blocks = ⌈1000/64⌉ = 16
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **File Organization** | Heap, Sequential, Hash, Clustered |
| **Primary Index** | Sparse, on sorted file |
| **Secondary Index** | Dense, on unsorted attribute |
| **B+ Tree** | Balanced, data in leaves, leaves linked |
| **B+ Tree Order** | Max children = n, Max keys = n-1 |
| **Hashing** | O(1) equality, bad for range |

---

## 🎓 Quick Revision Points

1. ✅ Primary index = Sparse (one per block)
2. ✅ Secondary index = Dense (one per record)
3. ✅ B+ Tree: Data only in leaves
4. ✅ B+ Tree: Leaves are linked
5. ✅ Order n → Max (n-1) keys, n children
6. ✅ Height h → O(h) disk accesses
7. ✅ Hash: O(1) equality, O(n) range

---

*Previous: [Concurrency Control](./08-Concurrency-Control.md) | Next: [Query Processing & Optimization](./10-Query-Processing-and-Optimization.md)*
