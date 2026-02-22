# Chapter 13: Miscellaneous & Advanced Topics

## 13.1 Hashing

### Hash Table Basics

> **Analogy:** A library catalog — instead of searching every shelf, use the catalog (hash function) to go directly to the right shelf.

**Hash function:** h(key) → index in table of size m

**Desired properties:**
1. **Uniform distribution** — keys spread evenly
2. **Fast to compute** — O(1)
3. **Deterministic** — same key always gives same hash

### Common Hash Functions

| Method | Formula | Notes |
|--------|---------|-------|
| Division | h(k) = k mod m | m should be prime, not power of 2 |
| Multiplication | h(k) = ⌊m(kA mod 1)⌋ | A ≈ (√5 - 1)/2 ≈ 0.618 (Knuth) |
| Universal | h(k) = ((ak+b) mod p) mod m | a,b random, p prime > m |

### Collision Resolution

#### 1. Chaining (Open Hashing)

Each table slot holds a linked list of elements that hash to that slot.

| Metric | Value |
|--------|-------|
| Load factor α | n/m (average list length) |
| Search (avg successful) | 1 + α/2 |
| Search (avg unsuccessful) | 1 + α |
| Worst case | O(n) — all keys in one chain |

#### 2. Open Addressing (Closed Hashing)

All elements stored in the table itself. On collision, **probe** for the next empty slot.

**Probe sequences:**

| Method | Probe Sequence h(k,i) | Pros | Cons |
|--------|----------------------|------|------|
| **Linear Probing** | (h(k) + i) mod m | Cache friendly | Primary clustering |
| **Quadratic Probing** | (h(k) + c₁i + c₂i²) mod m | Reduced clustering | Secondary clustering |
| **Double Hashing** | (h₁(k) + i·h₂(k)) mod m | Best distribution | h₂ must be coprime to m |

**Load factor constraint:** α < 1 for open addressing (table can't be full)

### Expected Number of Probes

| Operation | Chaining | Open Addressing (uniform) |
|-----------|----------|---------------------------|
| Unsuccessful search | 1 + α | 1/(1-α) |
| Successful search | 1 + α/2 | -(1/α)·ln(1-α) |

> **GATE Favorites:**
> 1. "Average probes for unsuccessful search with load factor 0.5?" → Open addressing: 1/(1-0.5) = 2
> 2. "What load factor gives average 4 probes for unsuccessful search?" → 1/(1-α)=4 → α=0.75
> 3. "Primary clustering occurs in which probing?" → **Linear probing**
> 4. "For double hashing, h₂(k) should never be?" → **0** (causes infinite loop)

---

## 13.2 Randomized Algorithms

### Types

| Type | Definition | Example |
|------|-----------|---------|
| **Las Vegas** | Always correct, randomized running time | Randomized Quick Sort |
| **Monte Carlo** | Randomized correctness, guaranteed running time | Miller-Rabin Primality |

### Randomized Quick Sort

Pick pivot uniformly at random → **expected O(n log n)** for any input.

**Key insight:** No adversarial input can force worst case, because the pivot is random.

### Randomized Selection (Quick Select)

Finding k-th smallest: expected O(n), worst O(n²).

> **GATE Fact:** Randomized algorithms use random choices but provide expected guarantees. Las Vegas = always correct, Monte Carlo = might be wrong.

---

## 13.3 Lower Bounds for Algorithms

### Comparison-Based Lower Bounds

| Problem | Lower Bound | Achieved By |
|---------|-------------|-------------|
| Sorting | Ω(n log n) | Merge Sort, Heap Sort |
| Finding max | Ω(n) — need n-1 comparisons | Single pass |
| Finding max AND min | ⌈3n/2⌉ - 2 | Tournament method |
| Finding 2nd largest | n + ⌈log n⌉ - 2 | Tournament + losers of winner |
| Merging two sorted arrays | m + n - 1 (worst case) | Standard merge |
| Searching sorted array | Ω(log n) | Binary search |

### How to Derive: Finding Max needs n-1 comparisons

**Lower bound argument:** There are n elements. Each comparison can eliminate at most 1 candidate for the maximum. To narrow down from n candidates to 1, need at least n-1 comparisons.

### Finding Max AND Min simultaneously

**Naive:** 2n - 3 comparisons (find max using n-1, then find min using n-2)

**Better (Tournament):** Process elements in pairs:
1. Compare pairs: n/2 comparisons (determines potential maxes and mins)
2. Find max among n/2 candidates: n/2 - 1 comparisons
3. Find min among n/2 candidates: n/2 - 1 comparisons

Total = n/2 + (n/2-1) + (n/2-1) = **3n/2 - 2** comparisons

> **GATE Fact:** This is optimal — no comparison-based algorithm can find both max and min in fewer than ⌈3n/2⌉ - 2 comparisons.

---

## 13.4 Order Statistics

**k-th order statistic** = k-th smallest element in an unsorted array.

| Method | Time | Space | Guarantee |
|--------|------|-------|-----------|
| Sort, then index | O(n log n) | O(1)-O(n) | Deterministic |
| Quick Select | O(n) expected, O(n²) worst | O(1) | Randomized |
| Median of Medians | **O(n) worst case** | O(log n) | Deterministic |

> Already covered in Chapter 5 (Section 5.7).

---

## 13.5 Approximation Algorithms (Brief)

For NP-Hard optimization problems, approximation algorithms find solutions within a guaranteed factor of optimal.

**Approximation Ratio:** ρ(n) where max(C/C*, C*/C) ≤ ρ(n)

| Problem | Algorithm | Ratio |
|---------|-----------|-------|
| Vertex Cover | Take both endpoints of each edge in a maximal matching | 2 |
| TSP (triangle inequality) | MST-based tour | 2 |
| TSP (triangle inequality) | Christofides | 3/2 |
| Set Cover | Greedy | O(ln n) |
| Bin Packing (online) | First Fit Decreasing | 11/9 OPT + 6/9 |

### Vertex Cover 2-Approximation

```
ApproxVertexCover(G):
    C = ∅
    E' = E
    while E' ≠ ∅:
        Pick any edge (u,v) from E'
        C = C ∪ {u, v}
        Remove all edges incident to u or v
    return C
```

**Why ratio = 2?** The maximal matching has k edges, so our cover has 2k vertices. But each edge in the matching needs at least one endpoint in any cover → optimal ≥ k. So our solution ≤ 2 × optimal.

---

## 13.6 Important Algorithmic Identities & Results for GATE

### Sum Formulas
```
Σ(i=1 to n) 1 = n
Σ(i=1 to n) i = n(n+1)/2
Σ(i=1 to n) i² = n(n+1)(2n+1)/6
Σ(i=1 to n) i³ = [n(n+1)/2]²
Σ(i=0 to n) xⁱ = (xⁿ⁺¹ - 1)/(x - 1)  for x ≠ 1
Σ(i=1 to n) 1/i = Θ(ln n) ≈ ln n + 0.577  [Harmonic series]
Σ(i=0 to ∞) xⁱ = 1/(1-x)  for |x| < 1
Σ(i=0 to ∞) i·xⁱ = x/(1-x)²  for |x| < 1
```

### Logarithmic Identities
```
log(ab) = log a + log b
log(a/b) = log a - log b
log(aⁿ) = n·log a
log_b(a) = log_c(a) / log_c(b)    [Change of base]
a^(log_b(c)) = c^(log_b(a))       [GATE favorite!]
2^(log₂ n) = n
log₂(n!) = Θ(n log n)             [Stirling's approximation]
```

### Catalan Numbers
The n-th Catalan number: C(n) = (2n)! / ((n+1)! × n!) = C(2n, n) / (n+1)

| n | C(n) |
|---|------|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 14 |
| 5 | 42 |

**Appearances in GATE:**
- Number of distinct binary trees with n nodes
- Number of ways to parenthesize n+1 factors
- Number of valid arrangements of n pairs of parentheses
- Number of paths in an n×n grid (from corner to corner without crossing diagonal)
- Number of full binary trees with n+1 leaves

---


---
