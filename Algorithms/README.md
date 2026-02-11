# 📘 Algorithms — Complete Study Material for GATE · ESE · PSU · BANK

> **"An algorithm must be seen to be believed."** — Donald Knuth

This is a **comprehensive, exam-focused, A-to-Z study material** for Algorithms, designed to help you **ace GATE CSE, ESE (Engineering Services), PSU exams, and Banking Technical rounds** with Rank-1 level preparation. Every concept is explained with:

- ✅ **Why** it exists (motivation & intuition)
- ✅ **How** it works (step-by-step with examples)
- ✅ **Formula derivations** (not just formulas — the story behind them)
- ✅ **Real-world analogies** to build lasting understanding
- ✅ **Tricks & shortcuts** for competitive exams
- ✅ **Edge cases & traps** that examiners love
- ✅ **Previous year patterns** and question-solving techniques

---

## 📑 Table of Contents

| # | Chapter | Key Topics |
|---|---------|------------|
| 1 | [Algorithm Analysis & Asymptotic Notations](#chapter-1-algorithm-analysis--asymptotic-notations) | Big-O, Ω, Θ, o, ω, Growth Rates, Comparison Techniques |
| 2 | [Recurrence Relations](#chapter-2-recurrence-relations) | Master Theorem, Substitution, Recursion Tree, Akra-Bazzi |
| 3 | [Searching Algorithms](#chapter-3-searching-algorithms) | Linear, Binary, Ternary, Interpolation, Exponential Search |
| 4 | [Sorting Algorithms](#chapter-4-sorting-algorithms) | Bubble, Selection, Insertion, Merge, Quick, Heap, Radix, Counting, Bucket |
| 5 | [Divide and Conquer](#chapter-5-divide-and-conquer) | Strategy, Merge Sort, Quick Sort, Strassen's, Karatsuba, Closest Pair |
| 6 | [Greedy Algorithms](#chapter-6-greedy-algorithms) | Activity Selection, Huffman, Kruskal, Prim, Dijkstra, Fractional Knapsack |
| 7 | [Dynamic Programming](#chapter-7-dynamic-programming) | LCS, LIS, MCM, 0/1 Knapsack, Floyd-Warshall, Bellman-Ford, Edit Distance |
| 8 | [Graph Algorithms](#chapter-8-graph-algorithms) | BFS, DFS, MST, Shortest Paths, Topological Sort, SCC, Bridges, Articulation |
| 9 | [Backtracking & Branch and Bound](#chapter-9-backtracking--branch-and-bound) | N-Queens, Subset Sum, Graph Coloring, TSP, 0/1 Knapsack |
| 10 | [String Matching Algorithms](#chapter-10-string-matching-algorithms) | Naive, KMP, Rabin-Karp, Finite Automata |
| 11 | [Complexity Classes & NP-Completeness](#chapter-11-complexity-classes--np-completeness) | P, NP, NP-Hard, NP-Complete, Reductions, Cook's Theorem |
| 12 | [Amortized Analysis](#chapter-12-amortized-analysis) | Aggregate, Accounting, Potential Method |
| 13 | [Miscellaneous & Advanced Topics](#chapter-13-miscellaneous--advanced-topics) | Hashing, Randomized Algorithms, Lower Bounds, Approximation |
| 14 | [GATE Exam Strategy & PYQ Patterns](#chapter-14-gate-exam-strategy--pyq-patterns) | Tricks, Time Management, Common Traps |

---

---

# Chapter 1: Algorithm Analysis & Asymptotic Notations

## 1.1 What is an Algorithm?

> **Analogy:** Think of an algorithm like a recipe. It has specific steps, a defined input (ingredients), and produces an output (the dish). A "good" recipe is one that's efficient (less time & resources) and correct (always gives the right dish).

**Formal Definition:** An algorithm is a **finite sequence of well-defined, unambiguous instructions** that, given some input, produces an output and terminates in a finite amount of time.

### Properties of an Algorithm (Knuth's 5 Properties)

| Property | Meaning | Example |
|----------|---------|---------|
| **Finiteness** | Must terminate after finite steps | A loop that always ends |
| **Definiteness** | Each step must be precisely defined | "Add 1 to x" (not "add something") |
| **Input** | Zero or more inputs | Array for sorting |
| **Output** | One or more outputs | Sorted array |
| **Effectiveness** | Each step must be basic enough to be carried out | Basic arithmetic, comparisons |

> **GATE Trap:** An algorithm MUST be finite. A procedure that runs forever is NOT an algorithm (it's a computational procedure). For example, an OS scheduler runs indefinitely — it's a procedure, not an algorithm.

---

## 1.2 Why Analyze Algorithms?

We analyze algorithms to **predict performance without running them** and to **compare algorithms** solving the same problem.

### Two Dimensions of Analysis

| Dimension | What it measures | Notation |
|-----------|-----------------|----------|
| **Time Complexity** | Number of basic operations as function of input size | T(n) |
| **Space Complexity** | Amount of memory used as function of input size | S(n) |

> **Key Insight:** We don't measure wall-clock time because it depends on hardware. Instead, we count the **number of fundamental operations** (comparisons, assignments, arithmetic ops).

---

## 1.3 Asymptotic Notations — The Language of Efficiency

### Why Asymptotic?

For small inputs, all algorithms are fast. We care about behavior as **n → ∞** (large inputs). Asymptotic notations let us **ignore constants and lower-order terms**, focusing on the **growth rate**.

> **Analogy:** If two cars are racing, one at speed `3n² + 5n + 100` km/h and another at `n³` km/h, for a very long road (large n), the second car always wins eventually — regardless of the constants.

---

### 1.3.1 Big-O Notation — O(g(n)) — Upper Bound

**Definition:**  
f(n) = O(g(n)) if there exist **positive constants c and n₀** such that:

```
f(n) ≤ c · g(n)  for all n ≥ n₀
```

**What it means:** f(n) grows **at most as fast as** g(n) (up to a constant factor) for large n.

**How the formula came up:**  
We want to say "f doesn't grow faster than g." But f might be `3n² + 5n`, and g is `n²`. Since `3n² + 5n ≤ 4n²` for n ≥ 5, we can pick c = 4 and n₀ = 5. The constants c and n₀ are the "witnesses" proving the bound.

**Example:**  
Prove: `3n + 2 = O(n)`  
We need: `3n + 2 ≤ c·n` for n ≥ n₀  
Pick c = 4: `3n + 2 ≤ 4n` → `2 ≤ n` → n₀ = 2 ✓  

**Example:**  
Prove: `n² + 3n = O(n²)`  
We need: `n² + 3n ≤ c·n²` → `1 + 3/n ≤ c`  
For n ≥ 1: `1 + 3 = 4 ≤ c` → Pick c = 4, n₀ = 1 ✓

> **GATE Trick:** To prove f(n) = O(g(n)), find valid c and n₀. To disprove, show no such c and n₀ can exist (often via contradiction or limit test).

**Limit Test Shortcut:**  
```
lim (n→∞) f(n)/g(n) = {
    0        → f(n) = O(g(n)) and f(n) = o(g(n))
    constant → f(n) = O(g(n)) and f(n) = Θ(g(n))
    ∞        → f(n) ≠ O(g(n))
}
```

---

### 1.3.2 Big-Omega Notation — Ω(g(n)) — Lower Bound

**Definition:**  
f(n) = Ω(g(n)) if there exist **positive constants c and n₀** such that:

```
f(n) ≥ c · g(n)  for all n ≥ n₀
```

**What it means:** f(n) grows **at least as fast as** g(n).

> **Analogy:** "At minimum, you'll need Ω(n) time" = "You can't do it in less than linear time."

**Example:**  
Prove: `5n² + 3n = Ω(n²)`  
We need: `5n² + 3n ≥ c·n²` → `5 + 3/n ≥ c`  
For all n ≥ 1: Pick c = 5, n₀ = 1 ✓ (since `5 + 3/n ≥ 5` for positive n)

> **Use Case:** Lower bounds tell us the **minimum work** required. Comparison-based sorting has a lower bound of Ω(n log n).

---

### 1.3.3 Big-Theta Notation — Θ(g(n)) — Tight Bound

**Definition:**  
f(n) = Θ(g(n)) if there exist **positive constants c₁, c₂, and n₀** such that:

```
c₁ · g(n) ≤ f(n) ≤ c₂ · g(n)  for all n ≥ n₀
```

**What it means:** f(n) grows **at the same rate** as g(n). This is the **tightest characterization**.

> **Key Relationship:** f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))

**Example:**  
Prove: `3n² + 5n + 2 = Θ(n²)`  
Lower bound: `3n² + 5n + 2 ≥ 3n²` → c₁ = 3  
Upper bound: `3n² + 5n + 2 ≤ 3n² + 5n² + 2n² = 10n²` for n ≥ 1 → c₂ = 10  
So with c₁ = 3, c₂ = 10, n₀ = 1 ✓

---

### 1.3.4 Little-o Notation — o(g(n)) — Strict Upper Bound

**Definition:**  
f(n) = o(g(n)) if for **every** positive constant c, there exists n₀ such that:

```
f(n) < c · g(n)  for all n ≥ n₀
```

Equivalently: `lim (n→∞) f(n)/g(n) = 0`

**Difference from Big-O:**  
- O(g(n)): f grows at most as fast as g (≤, allows equality)
- o(g(n)): f grows **strictly slower** than g (<, no equality)

**Example:** `n = o(n²)` because `lim(n/n²) = lim(1/n) = 0`  
**Counter-example:** `n² ≠ o(n²)` because `lim(n²/n²) = 1 ≠ 0`

---

### 1.3.5 Little-omega Notation — ω(g(n)) — Strict Lower Bound

**Definition:**  
f(n) = ω(g(n)) if for **every** positive constant c, there exists n₀ such that:

```
f(n) > c · g(n)  for all n ≥ n₀
```

Equivalently: `lim (n→∞) f(n)/g(n) = ∞`

**Example:** `n² = ω(n)` because `lim(n²/n) = ∞`

---

### 1.3.6 Complete Comparison Table

| Notation | Relation | Math Analogy | Meaning |
|----------|----------|-------------|---------|
| f = O(g) | f ≤ g | ≤ | f is upper bounded by g |
| f = Ω(g) | f ≥ g | ≥ | f is lower bounded by g |
| f = Θ(g) | f = g | = | f grows same rate as g |
| f = o(g) | f < g | < | f grows strictly slower |
| f = ω(g) | f > g | > | f grows strictly faster |

### Properties of Asymptotic Notations

| Property | O | Ω | Θ |
|----------|---|---|---|
| **Reflexive** | f = O(f) ✓ | f = Ω(f) ✓ | f = Θ(f) ✓ |
| **Symmetric** | ✗ | ✗ | f = Θ(g) ⟺ g = Θ(f) ✓ |
| **Transitive** | ✓ | ✓ | ✓ |
| **Transpose Symmetric** | f = O(g) ⟺ g = Ω(f) | (same) | — |

> **GATE Favorite:** "If f(n) = O(g(n)), then g(n) = Ω(f(n))." — TRUE (Transpose Symmetry)

---

## 1.4 Common Growth Rates (Sorted Slowest → Fastest)

```
O(1) < O(log log n) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!) < O(nⁿ)
```

| Complexity | Name | Example Algorithm |
|------------|------|-------------------|
| O(1) | Constant | Array index access, hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(√n) | Square root | Trial division primality |
| O(n) | Linear | Linear search, single pass |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Bubble sort, insertion sort |
| O(n³) | Cubic | Floyd-Warshall, matrix multiplication |
| O(2ⁿ) | Exponential | Subset generation, recursive Fibonacci |
| O(n!) | Factorial | Brute-force permutation |

### Useful Identities for GATE

```
log(n!) = Θ(n log n)           [Stirling's Approximation: n! ≈ √(2πn)(n/e)ⁿ]
Σ(i=1 to n) i = n(n+1)/2 = Θ(n²)
Σ(i=1 to n) i² = n(n+1)(2n+1)/6 = Θ(n³)
Σ(i=0 to n) xⁱ = (xⁿ⁺¹ - 1)/(x - 1)   [Geometric series]
Σ(i=1 to n) 1/i = Θ(log n)              [Harmonic series]
log(a·b) = log a + log b
log(aⁿ) = n·log a
a^(log_b(c)) = c^(log_b(a))             [GATE favorite identity]
```

> **Trick for GATE:** When comparing two functions f and g, take log of both sides. If `log f = O(log g)`, it often (but not always) implies `f = O(g)`. Be careful — this doesn't work in reverse for exponentials!

---

## 1.5 Best Case, Worst Case, Average Case

| Case | Definition | When to use |
|------|-----------|-------------|
| **Best Case** | Minimum operations for any input of size n | Rarely useful (too optimistic) |
| **Worst Case** | Maximum operations for any input of size n | **Default in GATE** — guarantees performance |
| **Average Case** | Expected operations over all inputs of size n | Needs probability distribution |

**Example — Linear Search in array of n elements:**
- Best case: Θ(1) — element at first position
- Worst case: Θ(n) — element at last position or absent
- Average case: Θ(n) — on average, checks n/2 elements

> **GATE Convention:** Unless stated otherwise, **assume worst case**. If the question says "expected time," use average case.

---

## 1.6 How to Analyze Code — Step by Step

### Rule 1: Simple Statements → O(1)
```
x = 5;          // O(1)
y = x + 3;      // O(1)
```

### Rule 2: Sequential Blocks → Add
```
Block1;  // O(f(n))
Block2;  // O(g(n))
// Total: O(f(n) + g(n)) = O(max(f(n), g(n)))
```

### Rule 3: If-Else → Take Maximum
```
if (condition)    // O(1)
    Block1;       // O(f(n))
else
    Block2;       // O(g(n))
// Total: O(max(f(n), g(n)))
```

### Rule 4: Loops → Multiply
```
for (i = 0; i < n; i++)      // Runs n times
    Statement;                 // O(1) each
// Total: O(n)
```

### Rule 5: Nested Loops → Multiply
```
for (i = 0; i < n; i++)           // n times
    for (j = 0; j < n; j++)       // n times each
        Statement;                  // O(1)
// Total: O(n²)
```

### Common Loop Patterns for GATE

**Pattern 1: Loop variable multiplied**
```c
for (i = 1; i <= n; i = i * 2)
    // Body
```
Iterations: i goes 1, 2, 4, 8, ..., n → **log₂(n)** iterations → **O(log n)**

**How?** After k iterations, i = 2ᵏ. Loop ends when 2ᵏ > n → k > log₂(n) → k = ⌈log₂(n)⌉ + 1

**Pattern 2: Loop variable divided**
```c
for (i = n; i >= 1; i = i / 2)
    // Body
```
Iterations: i goes n, n/2, n/4, ..., 1 → **log₂(n)** iterations → **O(log n)**

**Pattern 3: Nested with dependency**
```c
for (i = 1; i <= n; i++)
    for (j = 1; j <= i; j++)
        // Body
```
Total = Σ(i=1 to n) i = n(n+1)/2 = **O(n²)**

**Pattern 4: Both multiplied**
```c
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= n; j = j * 2)
        // Body
```
Total = log(n) × log(n) = **O(log²n)**

**Pattern 5: Inner depends on outer (multiplicative)**
```c
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= i; j++)
        // Body
```
Total = 1 + 2 + 4 + ... + n = 2n - 1 = **O(n)**

> **How?** The inner loop runs i times. i goes 1, 2, 4, ..., n. Sum = geometric series = (2·n - 1) = O(n).

**Pattern 6: Square root pattern**
```c
for (i = 1; i * i <= n; i++)
    // Body
```
Iterations: i goes 1, 2, 3, ..., √n → **O(√n)**

**Pattern 7: Logarithmic inner**
```c
for (i = 1; i <= n; i++)
    for (j = 1; j <= n; j = j + i)
        // Body
```
For each i, inner runs n/i times. Total = Σ(i=1 to n) n/i = n · Σ(1/i) = n · Hₙ = **O(n log n)**

> **This is a GATE classic!** The harmonic series sum Hₙ = Σ(1/i) = Θ(log n) appears frequently.

---

## 1.7 Space Complexity Analysis

**Space = Input Space + Auxiliary Space**

In GATE, when they ask for "space complexity," they usually mean **auxiliary space** (extra space beyond input).

| Algorithm | Time | Auxiliary Space |
|-----------|------|-----------------|
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(log n) — recursion stack |
| Heap Sort | O(n log n) | O(1) — in-place |
| Insertion Sort | O(n²) | O(1) — in-place |

> **GATE Trap:** Recursive algorithms use stack space! Quick Sort uses O(log n) auxiliary space for recursion (best/average), O(n) in worst case.

---


---

# Chapter 2: Recurrence Relations

## 2.1 What is a Recurrence Relation?

> **Analogy:** Imagine stacking Russian dolls. To know how many dolls are in the largest one, you need to open it and count the one inside, which itself contains another... A recurrence is like this — the answer for size n depends on the answer for a smaller size.

A **recurrence relation** defines a function T(n) in terms of T on smaller values. They naturally arise from **recursive algorithms**.

**Example:**  
```
T(n) = 2T(n/2) + n     [Merge Sort]
T(1) = 1               [Base case]
```
This says: "To sort n elements, we sort two halves (each takes T(n/2)) and merge them (takes n)."

---

## 2.2 Methods to Solve Recurrences

### Method 1: Substitution Method (Guess & Prove)

**Steps:**
1. **Guess** the form of the solution
2. **Prove** by mathematical induction
3. **Find constants** that work

**Example: T(n) = 2T(n/2) + n**

**Guess:** T(n) = O(n log n), so assume T(n) ≤ cn log n for some c > 0.

**Inductive Step:** Assume T(k) ≤ ck log k for all k < n.

```
T(n) = 2T(n/2) + n
     ≤ 2 · c(n/2)log(n/2) + n
     = cn(log n - log 2) + n
     = cn·log n - cn + n
     = cn·log n - (c-1)n
     ≤ cn·log n          [holds when c ≥ 1]
```

So T(n) = O(n log n) with c = 1. ✓

> **GATE Tip:** Substitution is powerful but requires a good initial guess. Use the recursion tree or Master Theorem to guess, then verify with substitution.

> **Common Trap:** Don't forget to verify the base case! A proof by induction requires both the inductive step AND the base case.

---

### Method 2: Recursion Tree Method

**Idea:** Expand the recurrence into a tree, where each node represents the cost at that level. Sum all levels to get the total.

**Example: T(n) = 2T(n/2) + n**

```
Level 0:                    n                      → Cost = n
                          /   \
Level 1:              n/2       n/2                 → Cost = 2 × n/2 = n
                     /   \     /   \
Level 2:          n/4   n/4  n/4   n/4              → Cost = 4 × n/4 = n
                  ...   ...  ...   ...
Level k:        n/2ᵏ  (repeated 2ᵏ times)          → Cost = 2ᵏ × n/2ᵏ = n
```

**Number of levels:** Tree bottoms out when n/2ᵏ = 1 → k = log₂ n

**Total cost:** n × (number of levels) = n × log₂ n = **Θ(n log n)**

**Example: T(n) = 3T(n/4) + cn²**

```
Level 0:           cn²                              → Cost = cn²
Level 1:     3 × c(n/4)²  = (3/16)cn²              → Cost = (3/16)cn²
Level 2:     9 × c(n/16)² = (3/16)²cn²             → Cost = (3/16)²cn²
...
Level k:     3ᵏ × c(n/4ᵏ)² = (3/16)ᵏ cn²
```

**Number of levels:** n/4ᵏ = 1 → k = log₄ n

**Total = cn² × Σ(i=0 to log₄n) (3/16)ⁱ**

Since 3/16 < 1, this is a **decreasing geometric series** → converges to cn² × 1/(1 - 3/16) = cn² × 16/13

**T(n) = Θ(n²)** — the root dominates!

> **Insight:** In a recursion tree:
> - If cost **decreases** geometrically → root dominates → T(n) = Θ(f(n))
> - If cost is **same** at each level → all levels matter → T(n) = Θ(f(n) · log n)
> - If cost **increases** geometrically → leaves dominate → T(n) = Θ(n^(log_b(a)))

---

### Method 3: Master Theorem ⭐ (Most Important for GATE)

**For recurrences of the form:**
```
T(n) = aT(n/b) + f(n)
```
where a ≥ 1, b > 1, and f(n) is asymptotically positive.

**Compare f(n) with n^(log_b(a)):**

| Case | Condition | Result |
|------|-----------|--------|
| **Case 1** | f(n) = O(n^(log_b(a) - ε)) for some ε > 0 | T(n) = Θ(n^(log_b(a))) |
| **Case 2** | f(n) = Θ(n^(log_b(a)) · logᵏ n) for k ≥ 0 | T(n) = Θ(n^(log_b(a)) · logᵏ⁺¹ n) |
| **Case 3** | f(n) = Ω(n^(log_b(a) + ε)) for some ε > 0 AND a·f(n/b) ≤ c·f(n) for c < 1 | T(n) = Θ(f(n)) |

#### How the Master Theorem Works — The Intuition

Think of a **battle between root work and leaf work:**

- **n^(log_b(a))** = total work done by ALL leaves (there are a^(log_b(n)) = n^(log_b(a)) leaves)
- **f(n)** = work done at the root level

| Who wins? | Result |
|-----------|--------|
| **Leaves win** (f is polynomially smaller) → Case 1 | Leaf cost dominates |
| **Tie** (same polynomial growth) → Case 2 | Both contribute, extra log factor |
| **Root wins** (f is polynomially larger) → Case 3 | Root cost dominates |

#### Detailed Examples

**Example 1: T(n) = 9T(n/3) + n**
- a = 9, b = 3, f(n) = n
- n^(log₃9) = n^2
- Compare: f(n) = n vs n² → n = O(n^(2-1)) → ε = 1
- **Case 1:** T(n) = Θ(n²)

**Example 2: T(n) = 2T(n/2) + n**
- a = 2, b = 2, f(n) = n
- n^(log₂2) = n^1 = n
- Compare: f(n) = n = Θ(n^1 · log⁰n) → k = 0
- **Case 2:** T(n) = Θ(n · log n)

**Example 3: T(n) = 3T(n/4) + n·log n**
- a = 3, b = 4, f(n) = n·log n
- n^(log₄3) = n^0.793
- Compare: f(n) = n·log n = Ω(n^(0.793 + ε)) → ε ≈ 0.2
- Check regularity: 3·(n/4)·log(n/4) ≤ c·n·log n → (3/4)·n·log(n/4) ≤ c·n·log n ✓ for c = 3/4
- **Case 3:** T(n) = Θ(n log n)

**Example 4: T(n) = 2T(n/2) + n·log n**
- a = 2, b = 2, f(n) = n·log n
- n^(log₂2) = n
- Compare: f(n) = n·log n = Θ(n¹ · log¹ n) → k = 1
- **Case 2 (extended):** T(n) = Θ(n · log² n)

#### When Master Theorem FAILS

The Master Theorem does **NOT** apply when:

1. **f(n) is not polynomially different** from n^(log_b(a))
   - Example: T(n) = 2T(n/2) + n/log n → Gap is only logarithmic, not polynomial

2. **a < 1** — Master theorem requires a ≥ 1

3. **Non-uniform subproblems** — T(n) = T(n/3) + T(2n/3) + n (different sized subproblems)

4. **f(n) is not asymptotically positive**

> **GATE Trick for Quick Application:**
> 1. Compute `log_b(a)` (call it p)
> 2. Compare f(n) with n^p:
>    - f(n) is "smaller" → Θ(n^p)
>    - f(n) is "equal" (within log factors) → Θ(n^p · log^(k+1) n)
>    - f(n) is "bigger" → Θ(f(n))

---

### Method 4: Extended Master Theorem (for log factors)

For T(n) = aT(n/b) + Θ(nᵏ logᵖ n):

| Condition | Result |
|-----------|--------|
| a > bᵏ | Θ(n^(log_b(a))) |
| a = bᵏ and p > -1 | Θ(nᵏ logᵖ⁺¹ n) |
| a = bᵏ and p = -1 | Θ(nᵏ log log n) |
| a = bᵏ and p < -1 | Θ(nᵏ) |
| a < bᵏ | Θ(nᵏ logᵖ n) |

---

### Method 5: Special Recurrences (Must Memorize for GATE)

| Recurrence | Solution | Algorithm |
|------------|----------|-----------|
| T(n) = T(n-1) + 1 | Θ(n) | Linear traversal |
| T(n) = T(n-1) + n | Θ(n²) | Selection sort inner |
| T(n) = T(n-1) + log n | Θ(n log n) | — |
| T(n) = 2T(n-1) + 1 | Θ(2ⁿ) | Tower of Hanoi |
| T(n) = 2T(n/2) + n | Θ(n log n) | Merge sort |
| T(n) = 2T(n/2) + 1 | Θ(n) | Binary tree traversal |
| T(n) = T(n/2) + 1 | Θ(log n) | Binary search |
| T(n) = T(n/2) + n | Θ(n) | — |
| T(n) = 2T(n/2) + n² | Θ(n²) | — |
| T(n) = T(√n) + 1 | Θ(log log n) | — |
| T(n) = 2T(√n) + log n | Θ(log n · log log n) | — |

#### How to Solve T(n) = T(√n) + 1

**Substitution:** Let n = 2ᵐ, then T(2ᵐ) = T(2^(m/2)) + 1

Let S(m) = T(2ᵐ): S(m) = S(m/2) + 1

By Master Theorem: S(m) = Θ(log m)

Back-substitute: m = log n → T(n) = Θ(log log n) ✓

> **GATE Trick:** For T(n) = T(√n) + ..., substitute n = 2ᵐ to convert to a standard form.

---

## 2.3 Solving Linear Recurrences (Characteristic Equation Method)

For **linear homogeneous** recurrences like T(n) = c₁T(n-1) + c₂T(n-2):

1. Write **characteristic equation:** x² = c₁x + c₂ → x² - c₁x - c₂ = 0
2. Find roots r₁, r₂
3. General solution:
   - **Distinct roots:** T(n) = A·r₁ⁿ + B·r₂ⁿ
   - **Repeated root r:** T(n) = (A + Bn)·rⁿ

**Example: Fibonacci — T(n) = T(n-1) + T(n-2)**

Characteristic equation: x² - x - 1 = 0  
Roots: r₁ = (1+√5)/2 = φ ≈ 1.618, r₂ = (1-√5)/2 ≈ -0.618

T(n) = A·φⁿ + B·((1-√5)/2)ⁿ

Since |r₂| < 1, the second term → 0, so **T(n) = Θ(φⁿ) ≈ Θ(1.618ⁿ)**

> **GATE Result:** The n-th Fibonacci number grows as Θ(φⁿ) where φ = (1+√5)/2 ≈ 1.618 (Golden Ratio).

---


---

# Chapter 3: Searching Algorithms

## 3.1 Linear Search (Sequential Search)

> **Analogy:** Looking for a book in an unsorted pile — check each one, one by one.

**Algorithm:**
```
LinearSearch(A, n, key):
    for i = 0 to n-1:
        if A[i] == key:
            return i
    return -1  // not found
```

| Metric | Value |
|--------|-------|
| Best Case | O(1) — found at first position |
| Worst Case | O(n) — found at last position or absent |
| Average Case | O(n) — checks ~n/2 elements on average |
| Space | O(1) |

**Works on:** Sorted or unsorted arrays, linked lists.

> **When to use:** When data is unsorted, small, or you need to search only once.

---

## 3.2 Binary Search ⭐ (Most Important for GATE)

> **Analogy:** Finding a word in a dictionary — open to the middle, decide which half the word is in, repeat.

**Prerequisite:** Array must be **sorted**.

**Algorithm:**
```
BinarySearch(A, low, high, key):
    while low ≤ high:
        mid = low + (high - low) / 2    // avoids overflow
        if A[mid] == key:
            return mid
        else if A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

| Metric | Value |
|--------|-------|
| Best Case | O(1) — found at middle |
| Worst Case | O(log n) |
| Average Case | O(log n) |
| Space | O(1) iterative, O(log n) recursive |

### Why O(log n)?

At each step, we **halve the search space:**
- After 1 comparison: n/2 elements remain
- After 2 comparisons: n/4 elements remain
- After k comparisons: n/2ᵏ elements remain
- Search ends when n/2ᵏ = 1 → **k = log₂ n**

### Key Variants for GATE

**Finding first occurrence (leftmost):**
```
BinarySearchFirst(A, n, key):
    low = 0, high = n-1, result = -1
    while low ≤ high:
        mid = (low + high) / 2
        if A[mid] == key:
            result = mid        // record it
            high = mid - 1      // search left for earlier occurrence
        else if A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

**Finding last occurrence:** Same but go `low = mid + 1` on finding key.

**Minimum comparisons in Binary Search:**
- Successful search: Best = 1, Worst = ⌊log₂ n⌋ + 1
- Unsuccessful search: ⌊log₂ n⌋ or ⌈log₂(n+1)⌉ comparisons

> **GATE Classic Question:** "Minimum number of comparisons to search in a sorted array of n elements?"
> Answer: ⌊log₂ n⌋ + 1 (worst case for successful), ⌈log₂(n+1)⌉ (unsuccessful)

### Binary Search Decision Tree

For n elements, the binary search creates a **binary decision tree:**
- **Internal nodes** = successful comparisons
- **External nodes** (null) = unsuccessful comparisons
- Height = ⌊log₂ n⌋
- Internal path length + 2(n+1) = External path length (for extended binary tree)

> **GATE Trap:** "Average number of comparisons for a successful search in binary search?"  
> It's NOT just log n. It's **(internal path length of the decision tree) / n**. For n = 7: tree has heights 1,2,2,3,3,3,3 → avg = (1+2+2+3+3+3+3)/7 ≈ 2.43.

---

## 3.3 Ternary Search

**Idea:** Instead of dividing into 2 parts, divide into **3 parts**.

```
TernarySearch(A, low, high, key):
    if high >= low:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        if A[mid1] == key: return mid1
        if A[mid2] == key: return mid2
        if key < A[mid1]: return TernarySearch(A, low, mid1-1, key)
        elif key > A[mid2]: return TernarySearch(A, mid2+1, high, key)
        else: return TernarySearch(A, mid1+1, mid2-1, key)
    return -1
```

**Time Complexity:** T(n) = T(n/3) + O(1) → **O(log₃ n)**

> **GATE Trap: Is Ternary Search faster than Binary Search?**  
> **NO!** log₃ n = log₂ n / log₂ 3. But each step of ternary search does **2 comparisons** vs 1 for binary.  
> Total comparisons: 2·log₃ n vs log₂ n. Since 2/log₂3 ≈ 1.26 > 1, **binary search is actually better!**

---

## 3.4 Interpolation Search

> **Analogy:** If you're looking for "A" in a phone book, you don't start in the middle — you start near the beginning. Interpolation search uses the **value distribution** to guess where the key might be.

**Probe position formula:**
```
pos = low + ((key - A[low]) × (high - low)) / (A[high] - A[low])
```

**How the formula came up:**  
We assume elements are **uniformly distributed**. Linear interpolation gives:  
(pos - low)/(high - low) = (key - A[low])/(A[high] - A[low])  
Solving for pos gives the formula above.

| Metric | Value |
|--------|-------|
| Best Case | O(1) |
| Average Case | **O(log log n)** — for uniformly distributed data |
| Worst Case | **O(n)** — for exponentially distributed data |
| Space | O(1) |

> **When to use:** When data is **uniformly distributed** and sorted.  
> **GATE fact:** Interpolation search is O(log log n) on average for uniform data.

---

## 3.5 Exponential Search

**Idea:** Find the range where the key exists using exponential jumps (1, 2, 4, 8, 16, ...), then binary search within that range.

```
ExponentialSearch(A, n, key):
    if A[0] == key: return 0
    i = 1
    while i < n and A[i] <= key:
        i = i * 2
    return BinarySearch(A, i/2, min(i, n-1), key)
```

**Time Complexity:** O(log n) — finding range is O(log n), binary search within range is O(log n).

**Why use it?** Useful when the target is **near the beginning** of the array — it performs better than binary search for such cases.

> **Use Case:** Searching in unbounded/infinite sorted arrays.

---

## 3.6 Jump Search (Block Search)

**Idea:** Jump ahead by fixed steps of size √n, then do linear search in the block.

```
JumpSearch(A, n, key):
    step = √n
    prev = 0
    while A[min(step, n)-1] < key:
        prev = step
        step += √n
        if prev >= n: return -1
    // Linear search in block [prev, step)
    while A[prev] < key:
        prev++
        if prev == min(step, n): return -1
    if A[prev] == key: return prev
    return -1
```

**Time Complexity:** O(√n)

**Optimal block size:** √n (minimizes worst-case: n/m + m where m is block size; minimized when m = √n)

> **How optimal block size is derived:**  
> Total comparisons = n/m (jumps) + m (linear search in block)  
> Minimize n/m + m: derivative = -n/m² + 1 = 0 → m = √n

---

## 3.7 Comparison of Searching Algorithms

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Sorted Required? |
|-----------|-------------|------------|--------------|-------|-----------------|
| Linear | O(1) | O(n) | O(n) | O(1) | No |
| Binary | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Ternary | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) | Yes + Uniform |
| Exponential | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Jump | O(1) | O(√n) | O(√n) | O(1) | Yes |

---


---

# Chapter 4: Sorting Algorithms

## 4.1 Why Study Sorting?

Sorting is the **most frequently tested topic** in GATE algorithms. Understanding sorting teaches you:
- Algorithm design paradigms (D&C, greedy, incremental)
- Time-space tradeoffs
- Stability and in-place concepts
- Lower bounds (Ω(n log n) for comparison sorts)

> **Analogy:** Sorting is like organizing a library. Different methods work better depending on how many books you have, how messy they are, and how much shelf space you have.

---

## 4.2 Key Terminology

| Term | Definition |
|------|-----------|
| **Stable** | Equal elements maintain their original relative order |
| **In-place** | Uses O(1) auxiliary space (ignoring recursion stack) |
| **Adaptive** | Performs better when input is partially sorted |
| **Online** | Can sort a list as it receives elements one by one |

> **GATE Favorite:** "Which sorting algorithms are stable?" — Bubble, Insertion, Merge, Counting, Radix (mnemonic: **BIMCR** — "BIM sorts CuRiously")

---

## 4.3 Bubble Sort

> **Analogy:** Like bubbles rising in water — larger elements "bubble up" to the end.

```
BubbleSort(A, n):
    for i = 0 to n-2:
        swapped = false
        for j = 0 to n-i-2:
            if A[j] > A[j+1]:
                swap(A[j], A[j+1])
                swapped = true
        if not swapped: break    // optimization
```

| Property | Value |
|----------|-------|
| Best Case | O(n) — already sorted (with optimization) |
| Average Case | O(n²) |
| Worst Case | O(n²) — reverse sorted |
| Space | O(1) |
| Stable | ✅ Yes |
| Adaptive | ✅ Yes (with flag) |
| In-place | ✅ Yes |

**Number of swaps (worst case):** n(n-1)/2 = inversions in reverse-sorted array

> **GATE Insight:** Number of swaps in bubble sort = number of **inversions** in the array. An inversion is a pair (i,j) where i < j but A[i] > A[j].

---

## 4.4 Selection Sort

> **Analogy:** Like picking the smallest card from a hand and placing it first, then the next smallest, etc.

```
SelectionSort(A, n):
    for i = 0 to n-2:
        minIdx = i
        for j = i+1 to n-1:
            if A[j] < A[minIdx]:
                minIdx = j
        swap(A[i], A[minIdx])
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All O(n²)** |
| Space | O(1) |
| Stable | ❌ No (swaps can change relative order) |
| Adaptive | ❌ No |
| In-place | ✅ Yes |
| Swaps | **O(n)** — minimum swaps among simple sorts |

> **GATE Fact:** Selection sort always does exactly n-1 swaps, regardless of input. It has the **minimum number of swaps** among O(n²) sorts.

> **Why not stable?** Consider [5a, 5b, 2]. After first pass: [2, 5b, 5a] — the order of 5s changed!

---

## 4.5 Insertion Sort ⭐

> **Analogy:** Like sorting playing cards in your hand — pick one card at a time and insert it into its correct position among the already-sorted cards.

```
InsertionSort(A, n):
    for i = 1 to n-1:
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

| Property | Value |
|----------|-------|
| Best Case | **O(n)** — already sorted |
| Average Case | O(n²) |
| Worst Case | O(n²) — reverse sorted |
| Space | O(1) |
| Stable | ✅ Yes |
| Adaptive | ✅ Yes |
| In-place | ✅ Yes |
| Online | ✅ Yes |

**Number of comparisons:**
- Best: n - 1
- Worst: n(n-1)/2
- Average: n(n-1)/4

> **GATE Gem:** Insertion sort is the **best choice for small arrays** (n < 20-30). Many practical sorting algorithms (like Tim Sort used in Python) use insertion sort for small subarrays.

> **GATE Fact:** Insertion sort's running time is **O(n + d)** where d is the number of inversions. For nearly sorted arrays (few inversions), it's nearly linear!

---

## 4.6 Merge Sort ⭐⭐

> **Analogy:** Splitting a deck of cards into two halves, sorting each half, then carefully merging them by comparing top cards.

```
MergeSort(A, low, high):
    if low < high:
        mid = (low + high) / 2
        MergeSort(A, low, mid)
        MergeSort(A, mid+1, high)
        Merge(A, low, mid, high)

Merge(A, low, mid, high):
    Create temp arrays L = A[low..mid], R = A[mid+1..high]
    i = j = 0, k = low
    while i < |L| and j < |R|:
        if L[i] <= R[j]:      // <= ensures stability
            A[k++] = L[i++]
        else:
            A[k++] = R[j++]
    Copy remaining elements
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All Θ(n log n)** |
| Space | **O(n)** auxiliary |
| Stable | ✅ Yes |
| Adaptive | ❌ No (always n log n) |
| In-place | ❌ No |

### Why Θ(n log n)?

Recurrence: T(n) = 2T(n/2) + Θ(n)

By Master Theorem: a=2, b=2, f(n)=n, n^(log₂2) = n → Case 2 → **Θ(n log n)**

### Key Properties for GATE

1. **Merge sort is optimal** for comparison-based sorting (matches Ω(n log n) lower bound)
2. **Best for linked lists** — no random access needed, and merge can be done in O(1) extra space
3. **Number of comparisons** (worst case): n⌈log₂n⌉ - 2^⌈log₂n⌉ + 1
4. **External sorting** uses merge sort (for data too large for RAM)

> **GATE Classic:** "Minimum comparisons to merge two sorted arrays of size m and n?"  
> Answer: min(m, n) comparisons (best case), m + n - 1 (worst case)

---

## 4.7 Quick Sort ⭐⭐

> **Analogy:** Organizing a group by height — pick one person (pivot), everyone shorter goes left, everyone taller goes right, repeat for each group.

```
QuickSort(A, low, high):
    if low < high:
        pivotIdx = Partition(A, low, high)
        QuickSort(A, low, pivotIdx - 1)
        QuickSort(A, pivotIdx + 1, high)

Partition(A, low, high):
    pivot = A[high]        // Last element as pivot
    i = low - 1
    for j = low to high - 1:
        if A[j] <= pivot:
            i++
            swap(A[i], A[j])
    swap(A[i+1], A[high])
    return i + 1
```

| Property | Value |
|----------|-------|
| Best Case | O(n log n) — balanced partition |
| Average Case | **O(n log n)** |
| Worst Case | **O(n²)** — already sorted (with last element pivot) |
| Space | O(log n) average, O(n) worst (recursion stack) |
| Stable | ❌ No |
| In-place | ✅ Yes |

### Why O(n²) Worst Case?

When array is **already sorted** and we pick the last element as pivot:
- Partition creates subarrays of size 0 and n-1
- T(n) = T(n-1) + T(0) + Θ(n) = T(n-1) + Θ(n) → **Θ(n²)**

### Why O(n log n) Average?

Even with random input, the **average partition splits somewhere between 1:9 and 9:1**.  
T(n) = T(n/10) + T(9n/10) + Θ(n)

Recursion tree: depth = log₁₀/₉ n = O(log n), each level costs O(n) → **O(n log n)**

> **Proof sketch:** The expected depth when pivot is chosen randomly is O(log n) because the probability of a "good" partition (that's at least 1/4 to 3/4) is 1/2.

### Randomized Quick Sort

Pick a **random element** as pivot → expected O(n log n) for any input.

> **GATE Fact:** Randomized Quick Sort has expected O(n log n) time for ALL inputs (no worst case input exists in expectation).

### Quick Sort Optimization Tricks

1. **Median-of-3:** Pick median of first, middle, last → avoids worst case for sorted input
2. **Switch to Insertion Sort** for small subarrays (n < 10)
3. **Tail recursion elimination:** Only recurse on the smaller half → O(log n) guaranteed stack space

### Partition Analysis

**Number of comparisons in partition:** n - 1 (each element compared with pivot exactly once)

**Quick Sort total comparisons:**
- Best: ~n log₂ n
- Average: ~1.39n log₂ n ≈ 2n ln n
- Worst: n(n-1)/2

> **GATE Trap:** "Quick sort is faster than Merge sort in practice because..."
> - Better **cache performance** (sequential access)
> - In-place (no extra array)
> - Inner loop is simple (just comparison + increment)
> - Despite same O(n log n), constant factors are smaller

---

## 4.8 Heap Sort

> **Analogy:** Build a tournament bracket (heap), repeatedly extract the champion (max), and the tree reorganizes itself.

```
HeapSort(A, n):
    // Build max-heap (bottom-up)
    for i = n/2 - 1 downto 0:
        Heapify(A, n, i)
    // Extract elements one by one
    for i = n-1 downto 1:
        swap(A[0], A[i])       // Move current max to end
        Heapify(A, i, 0)       // Heapify reduced heap

Heapify(A, n, i):
    largest = i
    left = 2i + 1
    right = 2i + 2
    if left < n and A[left] > A[largest]: largest = left
    if right < n and A[right] > A[largest]: largest = right
    if largest != i:
        swap(A[i], A[largest])
        Heapify(A, n, largest)
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All O(n log n)** |
| Space | **O(1)** |
| Stable | ❌ No |
| In-place | ✅ Yes |

### Build Heap: Why O(n) and not O(n log n)?

**Intuitive explanation:** Most nodes are at the bottom of the heap. Leaves (n/2 nodes) don't need heapifying. Each level above does decreasing work.

**Formal:** Cost = Σ(h=0 to ⌊log n⌋) ⌈n/2^(h+1)⌉ · O(h) = O(n · Σ h/2ʰ) = **O(n)**

The sum Σ(h=0 to ∞) h/2ʰ = 2 (converges!) → O(n × 2) = **O(n)**.

> **GATE Favorite:** "Time complexity of building a heap?" → **O(n)**, NOT O(n log n)!

> **GATE Trap:** "Heap sort is optimal and in-place. Why isn't it used more in practice?"  
> Poor **cache performance** — jumps around array non-sequentially. Quick sort with good pivot selection beats it in practice.

---

## 4.9 Counting Sort

> **Analogy:** Like sorting mail into post-office boxes by ZIP code — create a slot for each possible value.

**Prerequisite:** Elements must be **integers in range [0, k]**.

```
CountingSort(A, n, k):
    Count[0..k] = 0
    for j = 0 to n-1:
        Count[A[j]]++
    for i = 1 to k:
        Count[i] += Count[i-1]    // Cumulative count
    for j = n-1 downto 0:         // Reverse for stability
        B[Count[A[j]] - 1] = A[j]
        Count[A[j]]--
    Copy B to A
```

| Property | Value |
|----------|-------|
| Time | **O(n + k)** |
| Space | **O(n + k)** |
| Stable | ✅ Yes |
| In-place | ❌ No |

> **When to use:** When k = O(n) (range is linear in input size). If k = O(n²), counting sort is no better than comparison sorts.

> **GATE Fact:** Counting sort is NOT a comparison sort — it bypasses the Ω(n log n) lower bound!

---

## 4.10 Radix Sort

> **Analogy:** Like sorting paper forms — first by the last digit, then second-to-last, etc. (LSD — Least Significant Digit first)

```
RadixSort(A, n, d):
    for i = 1 to d:          // d = number of digits
        StableSort on digit i using CountingSort
```

| Property | Value |
|----------|-------|
| Time | **O(d × (n + b))** where b = base, d = digits |
| Space | O(n + b) |
| Stable | ✅ Yes (must use stable sort for each digit) |

If numbers are in range [0, nᵏ], use base n: d = k digits → Time = O(k × n) = **O(kn)**

> **GATE Trap:** "Why must the intermediate sort be stable?"  
> If it's not stable, sorting by digit i might undo the ordering achieved by digit i-1.

> **GATE Fact:** For n integers in range [0, nᶜ] for constant c, radix sort runs in **O(n)**.

---

## 4.11 Bucket Sort

> **Analogy:** Put items into labeled buckets based on value range, sort each bucket, then concatenate.

```
BucketSort(A, n):
    Create n empty buckets B[0..n-1]
    for i = 0 to n-1:
        Insert A[i] into B[⌊n × A[i]⌋]   // for values in [0, 1)
    for i = 0 to n-1:
        Sort B[i] using insertion sort
    Concatenate all buckets
```

| Property | Value |
|----------|-------|
| Average Case | **O(n)** for uniformly distributed input |
| Worst Case | O(n²) — all elements in one bucket |
| Space | O(n) |
| Stable | ✅ Yes (if using stable sort) |

> **When to use:** Input is **uniformly distributed** over a known range.

---

## 4.12 Lower Bound for Comparison-Based Sorting

### The Ω(n log n) Lower Bound — Why Can't We Do Better?

**Decision Tree Model:** Any comparison-based sort can be modeled as a binary decision tree where:
- Each internal node is a comparison (aᵢ vs aⱼ)
- Each leaf is a permutation (output)
- For n elements, there are **n! possible permutations**

**The tree must have ≥ n! leaves.** A binary tree of height h has at most 2ʰ leaves.

```
2ʰ ≥ n!
h ≥ log₂(n!)
h ≥ n log₂ n - n log₂ e    [Stirling's approximation]
h = Ω(n log n)
```

**Therefore: Any comparison-based sorting algorithm requires Ω(n log n) comparisons in the worst case.**

> **GATE Conclusion:**
> - Merge Sort, Heap Sort achieve this lower bound → they are **optimal comparison sorts**
> - Counting Sort, Radix Sort bypass this by not comparing elements
> - Bubble, Insertion, Selection are NOT optimal (O(n²) worst case)

---

## 4.13 Master Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✅ | ❌ |
| Radix Sort | O(d(n+b)) | O(d(n+b)) | O(d(n+b)) | O(n+b) | ✅ | ❌ |
| Bucket Sort | O(n+k) | O(n) | O(n²) | O(n) | ✅ | ❌ |

> **Trick to Remember:**
> - **In-place + O(n log n):** Only Heap Sort
> - **Stable + O(n log n):** Only Merge Sort
> - **No comparison sort is both stable and in-place with O(n log n) worst case**
> - **Best for nearly sorted:** Insertion Sort
> - **Best practical general-purpose:** Quick Sort (randomized)

---

