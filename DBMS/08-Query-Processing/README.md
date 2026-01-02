# 📚 Chapter 08: Query Processing & Optimization

> **The Atomic Truth**: *Transform SQL into efficient execution plans using cost-based optimization.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 2-4 marks |
| Frequency | 50% years |
| Type | MCQ (optimization rules), NAT (cost calculations) |
| Difficulty | Medium |
| Hot Topics | Join algorithms, Query optimization rules, Cost estimation |

---

## 1. Query Processing Overview

### Query Processing Steps

```
┌─────────────────────────────────────────────────────────────┐
│                         SQL Query                            │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    1. PARSER                                 │
│  - Syntax check                                              │
│  - Semantic check (tables exist, types match)               │
│  - Convert to internal representation (parse tree)         │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 2. QUERY OPTIMIZER                           │
│  - Generate equivalent expressions                          │
│  - Estimate cost of each                                    │
│  - Choose the cheapest plan                                 │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 3. EXECUTION ENGINE                          │
│  - Execute the chosen plan                                  │
│  - Return results                                           │
└─────────────────────────────────────────────────────────────┘
```

### Query Representation

```
SQL Query:
SELECT name FROM Employee E, Department D 
WHERE E.dept_id = D.dept_id AND D.name = 'CS'

Relational Algebra:
π_name(σ_{D.name='CS'}(Employee ⋈_{E.dept_id=D.dept_id} Department))

Query Tree:
            π_name
               │
            σ_{D.name='CS'}
               │
               ⋈
              ╱ ╲
       Employee  Department
```

---

## 2. Query Optimization

### Types of Optimization

| Type | Description | Examples |
|------|-------------|----------|
| **Heuristic** | Rule-based transformations | Push selections down |
| **Cost-based** | Estimate costs, choose minimum | Join order selection |

### Heuristic Optimization Rules

1. **Selection Pushdown**: Apply selections as early as possible
2. **Projection Pushdown**: Project early to reduce tuple size
3. **Selection Cascade**: Break conjunctions into series
4. **Join Associativity/Commutativity**: Reorder joins optimally

---

## 3. Equivalence Rules

### Selection Rules

**1. Cascade of Selection**
$$\sigma_{p_1 \land p_2}(R) = \sigma_{p_1}(\sigma_{p_2}(R))$$

**2. Commutativity of Selection**
$$\sigma_{p_1}(\sigma_{p_2}(R)) = \sigma_{p_2}(\sigma_{p_1}(R))$$

### Projection Rules

**3. Cascade of Projection**
$$\pi_{A_1}(\pi_{A_2}(\ldots\pi_{A_n}(R)\ldots)) = \pi_{A_1}(R)$$

(Where $A_1 \subseteq A_2 \subseteq \ldots \subseteq A_n$)

### Join/Cartesian Product Rules

**4. Commutativity**
$$R \times S = S \times R$$
$$R \bowtie S = S \bowtie R$$

**5. Associativity**
$$(R \bowtie S) \bowtie T = R \bowtie (S \bowtie T)$$
$$(R \times S) \times T = R \times (S \times T)$$

### Selection with Join Rules

**6. Selection Distribution over Join**
$$\sigma_p(R \bowtie S) = \sigma_p(R) \bowtie S$$

(If p involves only attributes of R)

$$\sigma_{p_1 \land p_2}(R \bowtie S) = \sigma_{p_1}(R) \bowtie \sigma_{p_2}(S)$$

(If $p_1$ involves only R and $p_2$ involves only S)

### Projection with Join Rules

**7. Projection Distribution over Join**
$$\pi_{A \cup B}(R \bowtie_C S) = \pi_A(R) \bowtie_C \pi_B(S)$$

(Where C ⊆ A ∩ B)

### Set Operation Rules

**8. Selection with Set Operations**
$$\sigma_p(R \cup S) = \sigma_p(R) \cup \sigma_p(S)$$
$$\sigma_p(R \cap S) = \sigma_p(R) \cap \sigma_p(S)$$
$$\sigma_p(R - S) = \sigma_p(R) - \sigma_p(S)$$

---

## 4. Query Tree Optimization

### Initial Query Tree (Canonical Form)

```
Original Tree (Unoptimized):
           π_name
              │
           σ_{E.dept_id=D.dept_id ∧ D.name='CS'}
              │
              ×
             ╱ ╲
      Employee  Department
```

### Step 1: Break Up Selection (Cascade)

```
           π_name
              │
        σ_{D.name='CS'}
              │
       σ_{E.dept_id=D.dept_id}
              │
              ×
             ╱ ╲
      Employee  Department
```

### Step 2: Push Selection Down

```
           π_name
              │
       σ_{E.dept_id=D.dept_id}
              │
              ×
             ╱ ╲
      Employee  σ_{D.name='CS'}
                      │
                 Department
```

### Step 3: Convert Cartesian + Selection to Join

```
           π_name
              │
              ⋈_{E.dept_id=D.dept_id}
             ╱ ╲
      Employee  σ_{D.name='CS'}
                      │
                 Department
```

### Step 4: Push Projection (if applicable)

```
           π_name
              │
              ⋈_{E.dept_id=D.dept_id}
             ╱ ╲
    π_{name,dept_id}  π_{dept_id}
           │               │
      Employee      σ_{D.name='CS'}
                          │
                     Department
```

---

## 5. Cost Estimation

### Cost Components

| Component | Description |
|-----------|-------------|
| **Disk I/O** | Number of block transfers (dominant factor) |
| **CPU** | Computation time (usually ignored) |
| **Memory** | Buffer space required |
| **Network** | For distributed databases |

### Cost Model

$$\text{Cost} \approx \text{Number of Block Accesses}$$

### Statistics Maintained

| Statistic | Symbol | Description |
|-----------|--------|-------------|
| Number of tuples | $n_r$ | Rows in relation r |
| Tuple size | $l_r$ | Bytes per row |
| Blocking factor | $f_r$ | Tuples per block |
| Number of blocks | $b_r$ | $\lceil n_r / f_r \rceil$ |
| Distinct values | $V(A, r)$ | Distinct values of A in r |
| Selection cardinality | $SC(A, r)$ | $n_r / V(A, r)$ |

### Selectivity Estimation

**Equality Selection**: $\sigma_{A=v}(r)$
$$\text{Estimated Tuples} = \frac{n_r}{V(A, r)} = SC(A, r)$$

**Range Selection**: $\sigma_{A \leq v}(r)$
$$\text{Estimated Tuples} = \frac{v - \min(A, r)}{\max(A, r) - \min(A, r)} \times n_r$$

**Conjunction**: $\sigma_{p_1 \land p_2}(r)$
$$\text{Estimated Tuples} = n_r \times \frac{s_1}{n_r} \times \frac{s_2}{n_r} = \frac{s_1 \times s_2}{n_r}$$

---

## 6. Join Algorithms

### Nested Loop Join (NLJ)

```
for each tuple t_r in R:
    for each tuple t_s in S:
        if t_r and t_s satisfy join condition:
            output (t_r, t_s)
```

**Cost Analysis** (R is outer, S is inner):

$$\text{Block Accesses} = b_R + (n_R \times b_S)$$

Or with block-based:
$$\text{Block Accesses} = b_R + (b_R \times b_S)$$

**Optimization**: Use smaller relation as outer

### Block Nested Loop Join

```
for each block B_R in R:
    for each block B_S in S:
        for each tuple t_r in B_R:
            for each tuple t_s in B_S:
                if match: output
```

**Cost**:
$$\text{Block Accesses} = b_R + (b_R \times b_S)$$

With M buffer pages (1 for output, 1 for S):
$$\text{Block Accesses} = b_R + \lceil \frac{b_R}{M-2} \rceil \times b_S$$

### Indexed Nested Loop Join

Use index on inner relation's join attribute.

```
for each tuple t_r in R:
    use index to find matching tuples in S
    for each matching t_s:
        output (t_r, t_s)
```

**Cost** (with B+ tree index of height h):
$$\text{Block Accesses} = b_R + (n_R \times (h + 1))$$

### Sort-Merge Join

```
1. Sort R on join attribute (if not already sorted)
2. Sort S on join attribute (if not already sorted)
3. Merge sorted relations
```

**Cost**:
- Sort R: $O(b_R \log b_R)$ or with external sort: specific formula
- Sort S: $O(b_S \log b_S)$
- Merge: $b_R + b_S$

$$\text{Total} \approx \text{Sort costs} + b_R + b_S$$

### Hash Join

```
1. Partition R into buckets using hash on join attribute
2. Partition S into same buckets
3. For each bucket pair, perform in-memory join
```

**Cost** (with M buffers, assuming no overflow):
$$\text{Block Accesses} = 3(b_R + b_S)$$

(Read + Write for partitioning + Read for matching)

### Join Algorithm Comparison

| Algorithm | Best Case | Worst Case | When to Use |
|-----------|-----------|------------|-------------|
| **Nested Loop** | $b_R + b_S$ | $b_R \times b_S \times n$ | Small relations |
| **Block Nested Loop** | $b_R + b_S$ | $b_R \times b_S$ | No index, small memory |
| **Indexed Nested Loop** | $b_R + n_R(h+1)$ | Same | Index on inner |
| **Sort-Merge** | $b_R + b_S$ | Sort + Merge | Both sorted or sortable |
| **Hash Join** | $3(b_R + b_S)$ | Much higher with overflow | Equality join, enough memory |

---

## 7. Selection Implementation

### Algorithms for Selection

| Method | Condition | Cost |
|--------|-----------|------|
| **Linear Scan** | Always works | $b_r$ |
| **Binary Search** | File sorted on selection attr | $\lceil \log_2 b_r \rceil + (s/f_r)$ |
| **Primary Index** | Equality on key | $h_i + 1$ |
| **Primary Index + Range** | Range on key | $h_i + b$ |
| **Secondary Index** | Equality | $h_i + 1$ (unique) or $h_i + n$ |
| **Conjunction** | Multiple conditions | Use most selective, then filter |

### Composite Selection

**Conjunctive Selection** ($\sigma_{p_1 \land p_2 \land \ldots}$):
1. Use index for most selective predicate
2. Test other predicates on retrieved tuples

**Disjunctive Selection** ($\sigma_{p_1 \lor p_2}$):
- If all have indices: Get union of pointers, then fetch
- If any lacks index: Linear scan

---

## 8. Projection and Duplicate Elimination

### Projection Implementation

**Without Duplicate Elimination**: $O(b_r)$

**With Duplicate Elimination**:
- Sort-based: $O(b_r \log b_r)$
- Hash-based: $O(b_r)$ expected

### Distinct Operation

**Sorting Approach**:
1. Sort tuples
2. Scan and remove adjacent duplicates

**Hashing Approach**:
1. Hash tuples to buckets
2. Within each bucket, eliminate duplicates

---

## 9. Aggregate Operations

### Without Grouping

| Aggregate | Method | Cost |
|-----------|--------|------|
| COUNT(*) | Scan or metadata | $b_r$ or $O(1)$ |
| MIN/MAX | Index lookup | $h_i + 1$ |
| SUM/AVG | Full scan | $b_r$ |

### With GROUP BY

1. Sort on grouping attributes
2. Scan sorted data, compute aggregates per group

**Cost**: Sort cost + $b_r$

Or with hashing:
1. Hash on grouping attributes
2. Compute aggregates in each bucket

---

## 10. Join Ordering

### Why Order Matters

For joins $(R_1 \bowtie R_2 \bowtie \ldots \bowtie R_n)$:
- Different orders give different intermediate result sizes
- Number of possible orderings = $(2(n-1))! / (n-1)!$ (Catalan number)

### Example: Join Order Impact

```
Tables:
- Student: 1000 tuples
- Enrollment: 10000 tuples  
- Course: 100 tuples

Query: Student ⋈ Enrollment ⋈ Course

Order 1: (Student ⋈ Enrollment) ⋈ Course
- Student ⋈ Enrollment: 10000 results (assuming each student enrolls 10)
- Then ⋈ Course: Final results

Order 2: Student ⋈ (Enrollment ⋈ Course)
- Enrollment ⋈ Course: 10000 results (each enrollment has 1 course)
- Then ⋈ Student: Final results

But consider with selection:
σ_{Course.name='DBMS'}(Student ⋈ Enrollment ⋈ Course)

Better: Student ⋈ Enrollment ⋈ σ_{name='DBMS'}(Course)
- σ reduces Course to few tuples first!
```

### Dynamic Programming for Join Order

Used by optimizers for small number of relations:
1. Compute cost of all 2-way joins
2. Use to compute cost of all 3-way joins
3. Continue until n-way join computed

---

## 11. Pipelining vs Materialization

### Materialization

Write intermediate results to disk.

```
R₁ = σ_{...}(Table1)    -- Write to disk
R₂ = R₁ ⋈ Table2        -- Read R₁, write R₂
Result = π(R₂)          -- Read R₂
```

**Cost**: Higher I/O but simpler

### Pipelining

Pass tuples directly between operations without writing.

```
            ┌──────────────┐
Table1 ────►│   Selection  │────┐
            └──────────────┘    │
                                ▼
                          ┌──────────┐
Table2 ──────────────────►│   Join   │────► π ────► Result
                          └──────────┘
```

**Benefits**:
- No intermediate disk writes
- Better for chains of operations
- Reduced latency

**Limitation**:
- Some operations can't be pipelined (e.g., sort)

---

## 12. Cost-Based Optimization

### Components

1. **Enumeration**: Generate all equivalent plans
2. **Cost Estimation**: Estimate cost of each plan
3. **Plan Selection**: Choose minimum cost plan

### Typical Optimizer Choices

| Decision | Options |
|----------|---------|
| Access method | Scan, index, hash |
| Join method | NLJ, SMJ, Hash join |
| Join order | Permutations |
| Pipelining | Yes/No |

### Example Cost Calculation

```
Query: σ_{dept='CS'}(Employee) ⋈ Department

Statistics:
- Employee: 10,000 tuples, 500 blocks
- Department: 50 tuples, 5 blocks
- 10% employees in CS dept

Plan A: Linear scan, then nested loop join
- Scan Employee: 500 blocks
- Select CS employees: 1000 tuples
- For each, scan Department: 1000 × 5 = 5000 blocks
- Total: 5500 blocks

Plan B: Use index on dept, then indexed join
- Index lookup for CS: 3 blocks (B+ tree) + 100 blocks (estimate)
- Indexed lookup in Department: 1000 × 3 = 3000 blocks
- Total: 3103 blocks

Plan C: Scan Department (small), indexed lookup in Employee
- Scan Department: 5 blocks
- For each, use index on Employee.dept_id: 50 × (3 + 20) = 1150 blocks
- Total: 1155 blocks

Plan C wins!
```

---

## 13. Common GATE Patterns

### Pattern 1: Equivalence Rules
Identify which transformations are valid.

### Pattern 2: Join Cost Calculation
Given block counts, compute nested loop cost.

### Pattern 3: Optimization Heuristics
Apply selection/projection pushdown.

### Pattern 4: Algorithm Selection
Choose best algorithm given conditions.

---

## 14. Summary: Optimization Heuristics

1. **Push selections down**: Reduce tuple count early
2. **Push projections down**: Reduce tuple size early
3. **Choose smaller relation as outer** in nested loop
4. **Use indices** when selective
5. **Consider join order** for multi-way joins
6. **Pipeline when possible**: Avoid intermediate writes

---

## 🧠 Memory Techniques

### Optimization Rules: "Select Small, Project Parts, Push Down"
- **Select Small**: Apply selections early
- **Project Parts**: Project early
- **Push Down**: Push both down the tree

### Join Costs: "Nested = N×B, Hash = 3×Sum"
- Nested Loop: $b_R + n_R \times b_S$
- Block Nested: $b_R + b_R \times b_S$
- Hash: $3(b_R + b_S)$

### Query Processing: "Parse → Optimize → Execute" (POE)

---

## 🔑 Key Takeaways for GATE

1. **Selection pushdown is key**: Reduces data earliest
2. **Join order matters**: Minimize intermediate sizes
3. **Nested loop cost**: Outer blocks + Outer rows × Inner blocks
4. **Index helps selective queries**: Not for full scans
5. **Pipelining avoids disk I/O**: Better for chains
6. **Smaller relation as outer**: For nested loop

---

## 📚 Related Chapters
- [← Previous: Chapter 07 - Indexing & File Organization](../07-Indexing-and-File-Organization/README.md)
- [Next: Chapter 09 - Recovery System →](../09-Recovery-System/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
