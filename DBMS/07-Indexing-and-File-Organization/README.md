# 📚 Chapter 07: Indexing & File Organization

> **The Atomic Truth**: *Trade space for speed using ordered access structures.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 4-6 marks |
| Frequency | 70% years |
| Type | NAT (B+ tree calculations, block access) |
| Difficulty | Medium-Hard |
| Hot Topics | B+ tree structure, index calculations, file organization |

---

## 1. File Organization Basics

### Why File Organization Matters
- Data is stored on disk in **blocks**
- Disk I/O is the primary performance bottleneck
- Goal: Minimize block accesses for queries

### Key Concepts

| Term | Definition |
|------|------------|
| **Block (Page)** | Unit of data transfer between disk and memory |
| **Record** | Collection of related data items (a row) |
| **Blocking Factor (bfr)** | Number of records per block |
| **Spanned** | Record can span multiple blocks |
| **Unspanned** | Each record fits entirely in one block |

### Blocking Factor Calculation

$$bfr = \lfloor \frac{B}{R} \rfloor$$

Where:
- $B$ = Block size (bytes)
- $R$ = Record size (bytes)

### Number of Blocks

$$b = \lceil \frac{r}{bfr} \rceil$$

Where:
- $r$ = Total number of records
- $bfr$ = Blocking factor

### Example Calculation

```
Given:
- Block size B = 1024 bytes
- Record size R = 100 bytes
- Number of records r = 30,000

Blocking factor:
bfr = ⌊1024/100⌋ = 10 records/block

Number of blocks:
b = ⌈30,000/10⌉ = 3,000 blocks
```

---

## 2. Types of File Organization

### Heap File (Unordered)

Records stored in order of insertion.

| Operation | Block Accesses |
|-----------|----------------|
| Insert | 1 (append at end) |
| Delete | Average: b/2 + 1 (find + mark) |
| Search (key) | Average: b/2, Worst: b |
| Search (range) | b (scan all) |

**Best for**: Bulk loading, frequent inserts, rare searches

### Sorted File (Sequential)

Records sorted on a key field.

| Operation | Block Accesses |
|-----------|----------------|
| Search (key) | $\lceil \log_2 b \rceil$ (binary search) |
| Search (range) | $\lceil \log_2 b \rceil + s$ where s = blocks in range |
| Insert | Expensive (need to shift) |
| Delete | Expensive (need to shift or mark) |

**Best for**: Range queries, when data is static

### Hashed File

Records distributed using hash function.

| Operation | Block Accesses |
|-----------|----------------|
| Search (key) | 1 (ideally) |
| Insert | 1 (ideally) |
| Search (range) | b (useless for range) |

**Best for**: Point queries, equality searches

---

## 3. Index Fundamentals

### What is an Index?
An **index** is a data structure that improves the speed of data retrieval operations.

### Index Entry
$$\langle \text{Key Value}, \text{Pointer} \rangle$$

### Types of Indices

```
                    INDICES
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
     ORDERED                      HASH
         │                        INDEX
    ┌────┴────┐
    ▼         ▼
 PRIMARY  SECONDARY
  INDEX     INDEX
    │
    ▼
  ┌─┴───┐
  ▼     ▼
Dense  Sparse
```

---

## 4. Primary Index

### Definition
A **primary index** is an ordered file whose records are of fixed length with two fields:
1. Primary key of data file
2. Pointer to disk block

### Characteristics
- **Ordered** on the primary key
- **One entry per block** (sparse index)
- Data file must be ordered on same key

### Structure

```
Primary Index                    Data File (Sorted)
┌─────┬────────┐                ┌────────────────┐
│ 10  │ Block1 │────────────────│ 10, Alice, ... │
├─────┼────────┤                │ 15, Bob, ...   │
│ 25  │ Block2 │───────┐        │ 20, Carol, ... │
├─────┼────────┤       │        ├────────────────┤
│ 40  │ Block3 │──┐    └───────►│ 25, David, ... │
└─────┴────────┘  │             │ 30, Eve, ...   │
                  │             │ 35, Frank, ... │
                  │             ├────────────────┤
                  └────────────►│ 40, Grace, ... │
                                │ 45, Henry, ... │
                                └────────────────┘
```

### Index Entries Calculation

$$\text{Index Entries} = \text{Number of Blocks} = \lceil \frac{r}{bfr_{data}} \rceil$$

### Blocking Factor for Index

$$bfr_i = \lfloor \frac{B}{K + P} \rfloor$$

Where:
- $K$ = Size of key field
- $P$ = Size of block pointer

### Index Blocks

$$b_i = \lceil \frac{\text{Index Entries}}{bfr_i} \rceil$$

### Search Cost with Primary Index

$$\text{Block Accesses} = \lceil \log_2(b_i) \rceil + 1$$

(Binary search on index + 1 data block access)

---

## 5. Clustering Index

### Definition
A **clustering index** is an ordered index on a non-key field that has duplicate values.

### Structure

```
Clustering Index              Data File (Sorted by dept)
┌──────┬────────┐            ┌────────────────────┐
│ CS   │ Block1 │───────────►│ 10, Alice, CS      │
├──────┼────────┤            │ 15, Bob, CS        │
│ EE   │ Block2 │───────┐    │ 20, Carol, CS      │
├──────┼────────┤       │    ├────────────────────┤
│ ME   │ Block3 │──┐    └───►│ 25, David, EE      │
└──────┴────────┘  │         │ 30, Eve, EE        │
                   │         ├────────────────────┤
                   └────────►│ 40, Grace, ME      │
                             └────────────────────┘
```

### Index Entries
$$\text{Index Entries} = \text{Number of Distinct Values}$$

---

## 6. Secondary Index

### Definition
A **secondary index** provides a secondary means of accessing data. Can be on any field.

### Characteristics
- Can be on non-ordering field
- **Dense index**: One entry per record
- Data file doesn't need to be sorted on this field

### Structure (Dense Secondary Index)

```
Secondary Index (on Name)     Data File (Sorted by ID)
┌───────┬────────┐           ┌────────────────┐
│ Alice │   •────│──────────►│ 10, Alice, CS  │
├───────┼────────┤           ├────────────────┤
│ Bob   │   •────│──────────►│ 15, Bob, EE    │
├───────┼────────┤           ├────────────────┤
│ Carol │   •────│──────────►│ 20, Carol, ME  │
└───────┴────────┘           └────────────────┘

(Each index entry points to exact record)
```

### Secondary Index Entries

$$\text{Index Entries} = r \text{ (number of records)}$$

### Secondary Index for Non-Unique Field
Use indirection through bucket of pointers:

```
Index                 Buckets              Data File
┌─────┬───────┐      ┌────────────┐       ┌──────────┐
│ CS  │   •───│─────►│ •  •  •    │──────►│ Records  │
├─────┼───────┤      └────────────┘       │ with     │
│ EE  │   •───│─────►│ •  •       │       │ various  │
└─────┴───────┘      └────────────┘       │ depts    │
                                          └──────────┘
```

---

## 7. Multi-Level Indices

### Why Multi-Level?
When index file itself is too large, create an index on the index!

### Structure

```
Level 2 Index          Level 1 Index           Data File
┌─────┬─────┐         ┌─────┬─────┐          ┌───────────┐
│  1  │  •──│────────►│  1  │  •──│─────────►│ Record 1  │
│ 50  │  •──│───┐     │ 10  │  •  │          │ ...       │
└─────┴─────┘   │     │ 20  │  •  │          ├───────────┤
                │     │ 30  │  •  │          │ ...       │
                │     │ 40  │  •  │          └───────────┘
                │     ├─────┼─────┤
                └────►│ 50  │  •  │
                      │ 60  │  •  │
                      │ 70  │  •  │
                      └─────┴─────┘
```

### Number of Levels

$$t = \lceil \log_{bfr_i}(b_1) \rceil$$

Where $b_1$ = number of first-level index blocks

### Search Cost with Multi-Level Index

$$\text{Block Accesses} = t + 1$$

(One access per level + 1 data block)

---

## 8. B-Tree

### Properties of B-Tree of Order p

1. Each node has at most **p** tree pointers and **p-1** keys
2. Each node (except root) has at least **⌈p/2⌉** tree pointers
3. Root has at least 2 tree pointers (unless it's a leaf)
4. All leaves are at the same level
5. A non-leaf node with k keys has k+1 children

### B-Tree Node Structure

```
┌────┬─────┬────┬─────┬────┬─────┬────┐
│ P₁ │ K₁  │ P₂ │ K₂  │ P₃ │ K₃  │ P₄ │
└────┴─────┴────┴─────┴────┴─────┴────┘
  │     │    │    │     │    │    │
  ▼     │    ▼    │     ▼    │    ▼
<K₁     │  K₁-K₂  │   K₂-K₃  │  >K₃
        ▼         ▼          ▼
     Exact     Exact      Exact
     Match     Match      Match

K₁ < K₂ < K₃
P₁ points to keys < K₁
P₂ points to keys between K₁ and K₂
...
```

### B-Tree Order Calculation

For block size B, key size K, pointer size P, record pointer size Pr:

Internal node: $(p-1) \times K + p \times P \leq B$

$$p = \lfloor \frac{B + K}{K + P} \rfloor$$

### B-Tree vs B+ Tree

| Feature | B-Tree | B+ Tree |
|---------|--------|---------|
| Data pointers | All nodes | Leaves only |
| Key duplication | No | Yes (in leaves) |
| Leaf links | No | Yes (linked list) |
| Range queries | Slow | Fast |

---

## 9. B+ Tree (MOST IMPORTANT!)

### Why B+ Tree?
- Most commonly used index structure in databases
- Optimized for disk-based storage
- Excellent for range queries

### B+ Tree Properties

1. All data pointers are at leaf level
2. Leaves are linked in a linked list
3. Internal nodes have only keys and tree pointers
4. Leaf nodes have keys and data pointers (or records)

### B+ Tree Structure

```
                    [30 | 60]
                   /    |    \
                  /     |     \
         [10|20]    [40|50]    [70|80]
          /|\        /|\        /|\
         / | \      / | \      / | \
       ─┴──┴──┴────┴──┴──┴────┴──┴──┴─
       │10│→│20│→│30│→│40│→│50│→│60│→│70│→│80│
       └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘
        ↓   ↓    ↓    ↓    ↓    ↓    ↓    ↓
       Data Data Data Data Data Data Data Data
       
       Leaves linked for range queries
```

### B+ Tree Node Formulas

**Internal Node** (order p):
- Maximum keys: $p - 1$
- Maximum children: $p$
- Minimum children (non-root): $\lceil p/2 \rceil$
- Minimum keys (non-root): $\lceil p/2 \rceil - 1$

**Leaf Node** (order $p_L$):
- Maximum keys/data pointers: $p_L - 1$
- Minimum keys: $\lceil (p_L - 1)/2 \rceil$

### B+ Tree Order Calculation

**For Internal Nodes:**
$(p-1) \times K + p \times P \leq B$

$$p = \lfloor \frac{B + K}{K + P} \rfloor$$

**For Leaf Nodes:**
$(p_L - 1) \times (K + Pr) + P \leq B$

$$p_L = \lfloor \frac{B - P}{K + Pr} \rfloor + 1$$

Where Pr = record pointer size, P = sibling pointer size

### B+ Tree Height/Levels

Given n records and leaf order $p_L$, internal order $p$:

Minimum height:
$$h_{min} = \lceil \log_p(\lceil n/(p_L - 1) \rceil) \rceil + 1$$

For quick estimation:
$$h \approx \lceil \log_p(n) \rceil$$

### Search in B+ Tree

$$\text{Block Accesses} = h + 1 = \lceil \log_p(n) \rceil + 1$$

(h levels of tree + 1 data access, or just h if leaf contains record)

---

## 10. B+ Tree Operations

### Search Operation

```
Search(key K):
1. Start at root
2. At each internal node:
   - Find smallest key Kᵢ such that K ≤ Kᵢ
   - Follow pointer Pᵢ
3. At leaf node:
   - Find key K
   - Return associated record/pointer
```

### Insertion Operation

```
Insert(key K, record R):
1. Find leaf node L where K should be inserted
2. If L has space:
   - Insert (K, pointer to R) in sorted order
3. Else (L is full):
   - Split L into L and L'
   - Distribute entries evenly
   - Copy up middle key to parent
   - Recursively split parent if needed
```

### Insertion Example

```
Before: Leaf with order 3 (max 2 keys)
[10 | 30] → Insert 20

After Split:
      [20]        ← New/updated parent entry
      /  \
   [10] [20|30]   ← Split leaf nodes
```

### Deletion Operation

```
Delete(key K):
1. Find leaf node L containing K
2. Remove K from L
3. If L has enough keys:
   - Done
4. Else if sibling can lend:
   - Borrow from sibling
   - Update parent key
5. Else:
   - Merge with sibling
   - Delete parent key
   - Recursively merge if needed
```

---

## 11. Hashing

### Static Hashing

$$\text{Bucket Address} = h(\text{Key}) \mod M$$

Where M = number of buckets

### Collision Handling

| Method | Description |
|--------|-------------|
| **Open Addressing** | Find next empty bucket |
| **Chaining** | Link overflow records |
| **Multiple Hashing** | Use second hash function |

### Overflow Chains

```
Buckets          Overflow Area
┌────────┐
│ Bucket0├─────►[Record]→[Record]→null
├────────┤
│ Bucket1│
├────────┤
│ Bucket2├─────►[Record]→null
└────────┘
```

### Extendible Hashing

Dynamic hashing that grows gracefully.

**Key Concept**: Use i bits of hash value (global depth)

```
Directory (Global Depth = 2)
┌───┬───────┐
│00 │   •───│───►Bucket A (Local Depth = 2)
├───┼───────┤
│01 │   •───│───►Bucket B (Local Depth = 2)
├───┼───────┤
│10 │   •───│───►Bucket C (Local Depth = 1)
├───┼───────┤          ▲
│11 │   •───│──────────┘
└───┴───────┘

Two directory entries can point to same bucket
when Local Depth < Global Depth
```

### Extendible Hashing Split

When bucket overflows:
1. If local depth < global depth:
   - Split bucket, no directory change
2. If local depth = global depth:
   - Double directory
   - Split bucket
   - Increase global depth

### Linear Hashing

Alternative to extendible hashing that doesn't use directory.

---

## 12. Index Selection Guidelines

### When to Use B+ Tree Index
- Range queries
- ORDER BY queries
- Prefix matching (LIKE 'abc%')
- When selectivity is medium to high

### When to Use Hash Index
- Point queries (equality)
- Very high selectivity
- No range queries needed

### When NOT to Create Index
- Small tables
- Frequently updated columns
- Low selectivity columns (e.g., gender)
- Columns rarely used in WHERE

### Covering Index
Index that contains all columns needed by query, avoiding data access.

```sql
CREATE INDEX idx_covering ON Employee(dept_id, salary);

-- This query uses only index, no table access:
SELECT dept_id, salary FROM Employee WHERE dept_id = 5;
```

---

## 13. GATE Calculation Examples

### Example 1: Primary Index Size

```
Given:
- 300,000 records
- Record size = 100 bytes
- Block size = 4096 bytes
- Key size = 10 bytes
- Pointer size = 6 bytes

Step 1: Data file blocking factor
bfr_data = ⌊4096/100⌋ = 40 records/block

Step 2: Data blocks
b_data = ⌈300,000/40⌉ = 7,500 blocks

Step 3: Index entries (1 per block for sparse primary)
entries = 7,500

Step 4: Index blocking factor
bfr_index = ⌊4096/(10+6)⌋ = 256 entries/block

Step 5: Index blocks
b_index = ⌈7,500/256⌉ = 30 blocks

Search cost = ⌈log₂(30)⌉ + 1 = 5 + 1 = 6 block accesses
```

### Example 2: B+ Tree Calculations

```
Given:
- Block size = 512 bytes
- Key size = 10 bytes
- Tree pointer = 6 bytes
- Data pointer = 6 bytes
- 100,000 records

Step 1: Internal node order
p = ⌊(512 + 10)/(10 + 6)⌋ = ⌊522/16⌋ = 32

Step 2: Leaf node order
p_L = ⌊(512 - 6)/(10 + 6)⌋ + 1 = ⌊506/16⌋ + 1 = 31 + 1 = 32

Step 3: Number of leaf nodes
Leaves = ⌈100,000/(32-1)⌉ = ⌈100,000/31⌉ = 3,226 leaves

Step 4: Height
h = ⌈log₃₂(3,226)⌉ = ⌈2.3⌉ = 3

Step 5: Total search cost = 3 + 1 = 4 block accesses
(3 levels + 1 data block)
```

### Example 3: Secondary Index

```
Given:
- 10,000 records
- Secondary index (dense) on non-key field
- Block size = 1024 bytes
- Key = 15 bytes, Pointer = 5 bytes

Step 1: Index entries = 10,000 (one per record)

Step 2: Index blocking factor
bfr = ⌊1024/(15+5)⌋ = 51 entries/block

Step 3: Index blocks
b = ⌈10,000/51⌉ = 197 blocks

Step 4: Search cost
= ⌈log₂(197)⌉ + 1 = 8 + 1 = 9 block accesses
```

---

## 14. Common GATE Patterns

### Pattern 1: Calculate Index Size
Given record count and sizes, find index blocks.

### Pattern 2: B+ Tree Order
Apply formula to find p and p_L.

### Pattern 3: Search Cost Comparison
Compare heap vs sorted vs indexed.

### Pattern 4: Multi-level Index Levels
Find number of levels for multi-level index.

### Pattern 5: Hash Function
Calculate bucket address.

---

## 15. Summary Comparison

| Index Type | Entries | Search Cost | Best For |
|------------|---------|-------------|----------|
| **Primary** | 1 per block | log₂(b) + 1 | Point query on ordering key |
| **Clustering** | 1 per distinct value | log₂(b) + s | Range on non-key |
| **Secondary (Dense)** | 1 per record | log₂(b) + 1 | Point query on non-ordering |
| **B+ Tree** | All records in leaves | log_p(n) + 1 | Range + Point queries |
| **Hash** | 1 per record | 1 (ideal) | Point queries only |

---

## 🧠 Memory Techniques

### Index Types: "PCBS" (Primary, Clustering, B+, Secondary)
- **P**rimary: One entry per **P**age (block)
- **C**lustering: One entry per **C**ategory (distinct value)
- **B**+ tree: **B**est for ranges, all data in leaves
- **S**econdary: One entry per **S**ingle record

### B+ Tree: "Leaves Link, Levels Log"
- Leaves are linked for range queries
- Levels ≈ log(records)

### Order Formula: "Block Minus Overhead Divided By Entry"
$$p = \lfloor \frac{B + K}{K + P} \rfloor$$

---

## 🔑 Key Takeaways for GATE

1. **Blocking Factor**: $\lfloor B/R \rfloor$
2. **Primary Index is Sparse**: One entry per block
3. **Secondary Index is Dense**: One entry per record
4. **B+ Tree Order**: Know both internal and leaf formulas
5. **B+ Tree Height**: $\approx \log_p(n)$
6. **Search Cost**: Levels + 1 (for data access)

---

## 📚 Related Chapters
- [← Previous: Chapter 06 - Transactions & Concurrency](../06-Transactions-and-Concurrency/README.md)
- [Next: Chapter 08 - Query Processing →](../08-Query-Processing/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
