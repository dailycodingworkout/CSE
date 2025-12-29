# Chapter 10: Query Processing & Optimization

---

## 🎯 What is Query Processing?

**Query Processing** = Translating SQL query into efficient execution plan.

```
SQL Query → Parser → Optimizer → Execution Engine → Result
```

### Processing Steps

```
┌─────────────────────────────────────────────────────────────────┐
│                        SQL QUERY                                 │
│     SELECT name FROM student WHERE dept = 'CS'                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    1. PARSING & TRANSLATION                      │
│              Check syntax, convert to internal form              │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                 2. RELATIONAL ALGEBRA EXPRESSION                 │
│                    π_name(σ_dept='CS'(Student))                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    3. QUERY OPTIMIZATION                         │
│              Choose best execution strategy                      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    4. QUERY EXECUTION                            │
│              Execute plan, return results                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Query Cost Measures

### Primary Cost: Disk I/O
```
Cost ≈ Number of block transfers + Number of seeks

Total Cost = b × t_T + S × t_S

Where:
b = number of blocks transferred
t_T = time per block transfer (~0.1 ms)
S = number of seeks
t_S = time per seek (~4 ms)
```

### Secondary Costs
- CPU time
- Network cost (distributed DB)
- Memory usage

### 🎯 Key Insight
> **Disk I/O dominates!**
> Optimize for minimum disk blocks read.

---

## 📐 Selection Operation (σ)

### Methods for σ_condition(R)

#### 1. Linear Search (File Scan)
```
Cost = b_r blocks (scan entire file)

Where b_r = number of blocks containing relation r
```

#### 2. Binary Search (Sorted File + Equality on Sort Key)
```
Cost = ⌈log₂(b_r)⌉ blocks

Requires: File sorted on search attribute
```

#### 3. Primary Index (Equality on Key)
```
Cost = Height of index + 1

Example: 3-level B+ tree → 4 block accesses
```

#### 4. Primary Index (Comparison)
```
For σ_A≥v(R) using primary index:

Cost = Height + ⌈b_r/2⌉  (approximately half the file)
```

#### 5. Secondary Index (Equality on Key)
```
Cost = Height + 1

(Index height + 1 data block)
```

#### 6. Secondary Index (Equality on Non-Key)
```
Cost = Height + Number of matching records

(Worst case: All records match → All blocks accessed)
```

### Selection Cost Summary

| Method | Cost (blocks) |
|--------|---------------|
| Linear Scan | b_r |
| Binary Search | ⌈log₂(b_r)⌉ |
| Primary Index (key) | h_i + 1 |
| Secondary Index (key) | h_i + 1 |
| Secondary Index (non-key) | h_i + n (n = matching records) |

---

## 🔗 Join Operations

### Types of Join Algorithms

```
                    Join Algorithms
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Nested Loop      Sort-Merge Join     Hash Join
       │
  ┌────┴────┐
  │         │
Simple  Block-based  Index-based
```

---

### 1. Nested Loop Join (NLJ)

#### Simple Nested Loop
```
For each tuple r in R:
    For each tuple s in S:
        If r and s satisfy join condition:
            Output (r, s)
```

**Cost**:
```
Cost = n_r × b_s + b_r

Where:
n_r = number of tuples in R (outer)
b_s = number of blocks in S (inner)
b_r = number of blocks in R
```

**Optimization**: Choose smaller relation as outer.

#### Block Nested Loop
```
For each block B_r in R:
    For each block B_s in S:
        For each tuple r in B_r:
            For each tuple s in B_s:
                If r and s satisfy condition:
                    Output (r, s)
```

**Cost**:
```
Cost = b_r × b_s + b_r

Much better than simple nested loop!
```

**With M memory buffers** (M-2 for outer, 1 for inner, 1 for output):
```
Cost = ⌈b_r / (M-2)⌉ × b_s + b_r
```

---

### 2. Indexed Nested Loop Join

Use index on inner relation's join attribute.

```
For each tuple r in R:
    Use index to find matching tuples in S
    Output matches
```

**Cost**:
```
Cost = b_r + n_r × c

Where:
c = cost of index lookup + retrieval
  = (h_i + 1) for primary index on key
  = (h_i + n) for secondary index
```

---

### 3. Sort-Merge Join

#### Algorithm
```
1. Sort R on join attribute
2. Sort S on join attribute
3. Merge sorted relations
```

#### Cost
```
Sort Cost = 2 × b_r × ⌈log_{M-1}(⌈b_r/M⌉)⌉  (for R)
          + 2 × b_s × ⌈log_{M-1}(⌈b_s/M⌉)⌉  (for S)

Merge Cost = b_r + b_s

Total = Sort Cost + Merge Cost
```

#### When Is It Good?
- Relations already sorted
- Output needs to be sorted
- Many duplicates

---

### 4. Hash Join

#### Algorithm
```
1. Build Phase: Hash smaller relation (R) into buckets
2. Probe Phase: Hash larger relation (S), probe matching buckets
```

```
Build Phase:
R → Hash(join key) → Buckets R₀, R₁, ..., R_n

Probe Phase:
For each tuple s in S:
    h = Hash(s.join_key)
    Search bucket R_h for matches
```

#### Cost
```
Cost = 3 × (b_r + b_s)

(Read both relations, write partitions, read partitions)
```

**Best case** (smaller relation fits in memory):
```
Cost = b_r + b_s
```

---

## 📊 Join Cost Comparison

| Algorithm | Best Case | Typical Case |
|-----------|-----------|--------------|
| **Nested Loop** | b_r + b_s | b_r × b_s |
| **Block Nested Loop** | b_r + b_s | b_r × b_s / M |
| **Index Nested Loop** | b_r + n_r | b_r + n_r × (h+1) |
| **Sort-Merge** | b_r + b_s | Sort + b_r + b_s |
| **Hash Join** | b_r + b_s | 3 × (b_r + b_s) |

### When to Use Which?

| Situation | Best Algorithm |
|-----------|----------------|
| Small relations | Nested Loop |
| Index exists on join attr | Index Nested Loop |
| Relations sorted/need sorted output | Sort-Merge |
| One relation fits in memory | Hash Join |
| Large unsorted relations | Hash Join |

---

## 🔄 Query Optimization

### Two Types

#### 1. Heuristic (Rule-Based) Optimization
Apply transformation rules that usually improve performance.

#### 2. Cost-Based Optimization
Estimate cost of different plans, choose cheapest.

---

## 📐 Equivalence Rules for Optimization

### 1. Selection Cascade
```
σ_p₁∧p₂(R) = σ_p₁(σ_p₂(R))
```

### 2. Selection Commutativity
```
σ_p₁(σ_p₂(R)) = σ_p₂(σ_p₁(R))
```

### 3. Projection Cascade
```
π_L₁(π_L₂(R)) = π_L₁(R)  if L₁ ⊆ L₂
```

### 4. Selection-Projection Commute
```
π_L(σ_p(R)) = σ_p(π_L(R))  if p involves only attrs in L
```

### 5. Selection-Join Commute
```
σ_p(R ⋈ S) = σ_p(R) ⋈ S   if p involves only R's attrs
```

### 6. Join Commutativity
```
R ⋈ S = S ⋈ R
```

### 7. Join Associativity
```
(R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)
```

### 8. Selection Distribution
```
σ_p₁∧p₂(R ⋈ S) = σ_p₁(R) ⋈ σ_p₂(S)
if p₁ involves only R and p₂ involves only S
```

---

## 📝 Heuristic Optimization Rules

### Priority Order

1. **Push Selections Down** (Most Important!)
   - Apply selection as early as possible
   - Reduces tuple count early

2. **Push Projections Down**
   - Remove unnecessary attributes early
   - Reduces tuple size

3. **Perform Most Restrictive Selection First**
   - Smallest result first

4. **Avoid Cartesian Products**
   - Convert to joins with conditions

5. **Use Indexes**
   - Prefer indexed attributes in selections

### Example Optimization

```
Original:
π_name(σ_salary>50000 ∧ dept='CS'(Employee ⋈ Department))

Step 1: Push selection into join
π_name(σ_salary>50000(Employee) ⋈ σ_dept='CS'(Department))

Step 2: Push projection
π_name(π_name,dept_id(σ_salary>50000(Employee)) ⋈ σ_dept='CS'(Department))

Much more efficient!
```

---

## 📊 Cost-Based Optimization

### Statistics Maintained

| Statistic | Symbol | Description |
|-----------|--------|-------------|
| Tuples | n_r | Number of tuples in r |
| Blocks | b_r | Number of blocks containing r |
| Tuple size | l_r | Size of each tuple |
| Distinct values | V(A, r) | Number of distinct values of A in r |
| Selection cardinality | SC(A, r) | Average tuples satisfying equality on A |

### Selection Cardinality
```
SC(A, r) = n_r / V(A, r)

Example: 10,000 employees in 50 departments
SC(dept, Employee) = 10000/50 = 200 employees per dept
```

### Result Size Estimation

#### Equality Selection
```
|σ_A=v(r)| = n_r / V(A, r)
```

#### Range Selection
```
|σ_A≥v(r)| ≈ n_r × (max(A) - v) / (max(A) - min(A))
```

#### Join Result Size
```
|r ⋈ s| ≤ n_r × n_s  (upper bound)

If join on key of R:
|r ⋈ s| ≤ n_s

If join on common attribute A:
|r ⋈ s| = (n_r × n_s) / max(V(A,r), V(A,s))
```

---

## 🌳 Query Execution Plans

### Query Tree
```
        π_name
           │
          ⋈
         / \
        /   \
   σ_dept='CS'  Course
       │
   Student
```

### Physical Query Plan
```
        π_name
           │
      Index NL Join (Student.cid = Course.cid)
         /              \
        /                \
Index Scan (dept)    Table Scan
   Student             Course
```

---

## 📱 Pipelining vs Materialization

### Materialization
```
Execute each operation fully, store result, then proceed.

σ_dept='CS'(Student) → Temp1
Temp1 ⋈ Course → Temp2
π_name(Temp2) → Result

Disadvantage: Disk I/O for intermediate results
```

### Pipelining
```
Pass tuples directly between operations without storing.

Student → σ_dept='CS' → ⋈ → π_name → Result
              ↓
         No temp storage!

Advantage: Reduced I/O, better memory use
```

---

## 🔢 Join Ordering

### Problem
For n relations: (2n-2)! / (n-1)! possible join orders

```
3 relations: 12 orders
5 relations: 1680 orders
10 relations: ~17.6 billion orders!
```

### Approach
Use **dynamic programming** for optimal order.

### Heuristics
1. Start with smallest relation
2. Avoid Cartesian products
3. Consider index availability

---

## ⚠️ Common GATE Traps

### Trap 1: Join Order Matters
```
(R ⋈ S) ⋈ T can have very different cost from R ⋈ (S ⋈ T)
```

### Trap 2: Selection Selectivity
```
High selectivity = Few rows selected (good for index)
Low selectivity = Many rows selected (use scan)

Counterintuitive naming!
```

### Trap 3: Block NL vs Simple NL
```
Simple NL: n_r × b_s + b_r
Block NL: b_r × b_s + b_r

Block NL much better for large relations!
```

### Trap 4: Index Usage
```
Index is NOT always better!
- Full table scan for low selectivity
- Sequential scan for range on unsorted data
```

---

## 🧪 Practice Problems

### Q1: Join Cost
```
R: 10,000 tuples, 100 blocks
S: 5,000 tuples, 50 blocks
Available memory: 10 blocks

Block Nested Loop Join (R outer):
Cost = ⌈100/(10-2)⌉ × 50 + 100
     = 13 × 50 + 100
     = 750 block transfers

Block Nested Loop Join (S outer):
Cost = ⌈50/(10-2)⌉ × 100 + 50
     = 7 × 100 + 50
     = 750 block transfers
```

### Q2: Selection Cardinality
```
Employee table: 10,000 rows
V(dept, Employee) = 20
V(salary, Employee) = 500

σ_dept='CS'(Employee): 10000/20 = 500 rows expected
σ_salary=50000(Employee): 10000/500 = 20 rows expected
```

### Q3: Optimization
```
Original: σ_A=5(R × S)
R: 1000 tuples
S: 500 tuples
V(A, R) = 100

Without optimization: 1000 × 500 = 500,000 comparisons
With push-down: σ_A=5(R) × S = 10 × 500 = 5,000 comparisons
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Cost Measure** | Disk I/O (block transfers) |
| **Selection** | Index best for high selectivity |
| **Join Algorithms** | NL, Block NL, Index NL, Sort-Merge, Hash |
| **Optimization** | Push selection/projection down |
| **Equivalence** | σ, π, ⋈ transformations |
| **Pipelining** | Avoid intermediate storage |

---

## 🎓 Quick Revision Points

1. ✅ Cost ≈ Disk block transfers
2. ✅ Push selections down (most important!)
3. ✅ Block NL >> Simple NL
4. ✅ Hash join best for equality, unsorted
5. ✅ Sort-merge best when sorted or need sorted output
6. ✅ Join order significantly affects cost
7. ✅ Pipelining avoids materialization overhead

---

*Previous: [File Organization & Indexing](./09-File-Organization-and-Indexing.md) | Next: [Recovery System](./11-Recovery-System.md)*
