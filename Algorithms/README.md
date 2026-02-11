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


---

# Chapter 5: Divide and Conquer

## 5.1 The Paradigm

> **Analogy:** Like a general breaking an army into smaller units, conquering each, then uniting them. You break a big problem into smaller identical subproblems, solve them independently, and combine the solutions.

**Three Steps:**
1. **Divide:** Break the problem into smaller subproblems of the same type
2. **Conquer:** Solve each subproblem recursively (base case: small enough to solve directly)
3. **Combine:** Merge the solutions of subproblems into the solution for the original problem

**General Recurrence:** T(n) = aT(n/b) + f(n)
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost of dividing and combining

---

## 5.2 Classic D&C Algorithms (Already Covered)

| Algorithm | Recurrence | Complexity |
|-----------|-----------|------------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort | T(n) = T(k) + T(n-k-1) + O(n) | O(n log n) avg |

---

## 5.3 Maximum Subarray Problem (Kadane's is better, but D&C is classic)

**Problem:** Find contiguous subarray with maximum sum.

**D&C Approach:**
1. Divide array into left and right halves
2. Maximum subarray is either:
   - Entirely in left half
   - Entirely in right half
   - **Crossing the midpoint** (key insight)
3. Find max crossing subarray in O(n)

```
MaxCrossing(A, low, mid, high):
    // Find max sum going left from mid
    leftSum = -∞, sum = 0
    for i = mid downto low:
        sum += A[i]
        if sum > leftSum: leftSum = sum
    // Find max sum going right from mid
    rightSum = -∞, sum = 0
    for j = mid+1 to high:
        sum += A[j]
        if sum > rightSum: rightSum = sum
    return leftSum + rightSum

MaxSubarray(A, low, high):
    if low == high: return A[low]
    mid = (low + high) / 2
    leftMax = MaxSubarray(A, low, mid)
    rightMax = MaxSubarray(A, mid+1, high)
    crossMax = MaxCrossing(A, low, mid, high)
    return max(leftMax, rightMax, crossMax)
```

**Time:** T(n) = 2T(n/2) + O(n) → **O(n log n)**

> **Note:** Kadane's algorithm solves this in O(n) using DP. But the D&C version is a classic GATE question.

---

## 5.4 Strassen's Matrix Multiplication

### Standard Matrix Multiplication

To multiply two n×n matrices: C = A × B

```
for i = 1 to n:
    for j = 1 to n:
        C[i][j] = 0
        for k = 1 to n:
            C[i][j] += A[i][k] * B[k][j]
```

**Time:** O(n³) — three nested loops.

### Strassen's Approach (1969)

**Key Idea:** Reduce the number of multiplications from 8 to 7 by using clever addition/subtraction.

**Standard D&C:**
Split each n×n matrix into four (n/2)×(n/2) submatrices:

```
A = | A₁₁  A₁₂ |    B = | B₁₁  B₁₂ |
    | A₂₁  A₂₂ |        | B₂₁  B₂₂ |

C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂
C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁
C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂
```

This needs **8 multiplications** → T(n) = 8T(n/2) + O(n²) → **O(n³)** (no improvement!)

**Strassen's 7 multiplications:**

```
M₁ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
M₂ = (A₂₁ + A₂₂)B₁₁
M₃ = A₁₁(B₁₂ - B₂₂)
M₄ = A₂₂(B₂₁ - B₁₁)
M₅ = (A₁₁ + A₁₂)B₂₂
M₆ = (A₂₁ - A₁₁)(B₁₁ + B₁₂)
M₇ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)

C₁₁ = M₁ + M₄ - M₅ + M₇
C₁₂ = M₃ + M₅
C₂₁ = M₂ + M₄
C₂₂ = M₁ - M₂ + M₃ + M₆
```

**Recurrence:** T(n) = 7T(n/2) + O(n²)

By Master Theorem: a=7, b=2, n^(log₂7) = n^2.807

Case 1: f(n) = O(n²) = O(n^(2.807-ε)) → **T(n) = Θ(n^log₂7) ≈ Θ(n^2.807)**

> **GATE Facts:**
> - Strassen's: O(n^2.807) vs standard O(n³)
> - Best known: O(n^2.3729) [Alman & Williams, 2024]
> - Lower bound: Ω(n²) (must read all elements)
> - In practice, Strassen's only helps for very large matrices

---

## 5.5 Karatsuba Multiplication (Fast Integer Multiplication)

### Standard Multiplication

Multiplying two n-digit numbers: O(n²) — multiply each digit pair.

### Karatsuba's Trick

Split each n-digit number into two halves:
```
x = xH · 10^(n/2) + xL
y = yH · 10^(n/2) + yL

x · y = xH·yH · 10ⁿ + (xH·yL + xL·yH) · 10^(n/2) + xL·yL
```

This needs 4 multiplications. Karatsuba's insight:

```
P₁ = xH · yH
P₂ = xL · yL
P₃ = (xH + xL) · (yH + yL)

x · y = P₁ · 10ⁿ + (P₃ - P₁ - P₂) · 10^(n/2) + P₂
```

**Only 3 multiplications!** (P₃ - P₁ - P₂ = xH·yL + xL·yH)

**Recurrence:** T(n) = 3T(n/2) + O(n) → **O(n^log₂3) ≈ O(n^1.585)**

> **How the trick works:** Instead of computing xH·yL and xL·yH separately, compute (xH+xL)(yH+yL) = xH·yH + xH·yL + xL·yH + xL·yL, then subtract the already-computed xH·yH and xL·yL.

---

## 5.6 Closest Pair of Points

**Problem:** Given n points in 2D, find the pair with minimum distance.

**Brute force:** Check all pairs → O(n²)

**D&C Approach:**
1. Sort points by x-coordinate
2. Divide into left and right halves by a vertical line
3. Recursively find closest pair in each half (δL, δR)
4. Let δ = min(δL, δR)
5. **Key Step:** Check points in a strip of width 2δ around the dividing line
6. For each point in strip, check at most **6-7 other points** (geometrically proven)

**Recurrence:** T(n) = 2T(n/2) + O(n) → **O(n log n)**

> **GATE Fact:** The strip checking step is O(n), not O(n²), because each point needs to be compared with at most O(1) other points in the strip (at most 6 for L∞ metric, 7 for L₂).

> **Why only 6-7 comparisons?** In a δ×2δ rectangle, at most 8 points can fit with pairwise distance ≥ δ (pigeon-hole argument on a grid).

---

## 5.7 Finding Median in O(n) — Median of Medians (SELECT)

**Problem:** Find the k-th smallest element in an unsorted array.

**Naive:** Sort, then return A[k] → O(n log n)

**Quick Select (randomized):** Average O(n), worst O(n²)

**Median of Medians (deterministic):**

```
SELECT(A, k):
    1. Divide A into groups of 5
    2. Find median of each group (O(n))
    3. Recursively find median of medians (T(n/5))
    4. Use this as pivot to partition
    5. Recurse on the appropriate side (T(7n/10))
```

**Recurrence:** T(n) = T(n/5) + T(7n/10) + O(n)

**Why 7n/10?** The median of medians is guaranteed to be ≥ 30% of elements and ≤ 30% of elements. So the worst case recursion is on at most 70% = 7n/10 elements.

**Proof that T(n) = O(n):**  
Guess T(n) ≤ cn. Then: T(n) ≤ cn/5 + 7cn/10 + an = cn(1/5 + 7/10) + an = cn(9/10) + an ≤ cn when c ≥ 10a.

> **GATE Fact:** k-th smallest element can be found in **O(n) worst case** using Median of Medians. Groups of 5 is not arbitrary — groups of 3 don't work (check: 1/3 + 2n/3 ≥ n).

---


---

# Chapter 6: Greedy Algorithms

## 6.1 The Greedy Paradigm

> **Analogy:** A greedy person at a buffet always picks the most appealing dish available right now, without worrying about what comes next. Sometimes this strategy works perfectly (you get the best meal), sometimes it doesn't (you fill up on appetizers and miss dessert).

**Key Properties:**
1. **Greedy Choice Property:** A globally optimal solution can be arrived at by making locally optimal (greedy) choices
2. **Optimal Substructure:** An optimal solution to the problem contains optimal solutions to subproblems

**When greedy works:** When making the locally best choice at each step leads to the globally best solution.  
**When greedy fails:** When local optimality doesn't guarantee global optimality (e.g., 0/1 Knapsack).

> **GATE Strategy:** To prove greedy is correct, use either:
> 1. **Exchange argument:** Show any non-greedy solution can be "improved" by swapping to greedy choice
> 2. **Greedy stays ahead:** Show greedy is always at least as good as any other solution at each step

---

## 6.2 Activity Selection Problem ⭐

**Problem:** Given n activities with start and finish times, select maximum number of non-overlapping activities.

**Greedy Strategy:** Always select the activity with the **earliest finish time** that doesn't conflict with already selected activities.

```
ActivitySelection(S, F, n):
    Sort activities by finish time
    selected = {1}        // First activity (earliest finish)
    lastFinish = F[1]
    for i = 2 to n:
        if S[i] >= lastFinish:
            selected = selected ∪ {i}
            lastFinish = F[i]
    return selected
```

**Time:** O(n log n) for sorting + O(n) for selection = **O(n log n)**

**Example:**
```
Activity:   A1   A2   A3   A4   A5   A6
Start:       1    3    0    5    3    5
Finish:      2    4    6    7    9   9

Sorted by finish: A1(1,2), A2(3,4), A3(0,6), A4(5,7), A5(3,9), A6(5,9)

Select A1 (finish=2) → Select A2 (start=3≥2, finish=4) → Skip A3 (start=0<4)
→ Select A4 (start=5≥4, finish=7) → Skip A5 (start=3<7) → Skip A6 (start=5<7)

Maximum activities: {A1, A2, A4} = 3 activities
```

> **Why earliest finish time?** By finishing early, we leave maximum room for future activities. Proof by exchange: if any optimal solution doesn't pick the earliest-finishing activity, we can swap its first activity with the earliest-finishing one without reducing the count.

> **GATE Trap:** Sorting by **start time** or by **shortest duration** does NOT work!
> - Start time fails: Activity (1,100) blocks everything
> - Duration fails: Short activity (4,6) might conflict with two good ones (1,5) and (6,10)

---

## 6.3 Fractional Knapsack ⭐

**Problem:** Given items with weights and values, and a knapsack of capacity W. Maximize value. **Fractions of items are allowed.**

**Greedy Strategy:** Sort by **value-to-weight ratio** (value/weight) in decreasing order. Take items greedily.

```
FractionalKnapsack(items, W):
    Sort items by value/weight ratio (decreasing)
    totalValue = 0
    for each item in sorted order:
        if W >= item.weight:
            Take entire item
            W -= item.weight
            totalValue += item.value
        else:
            Take fraction W/item.weight of item
            totalValue += item.value × (W / item.weight)
            break
    return totalValue
```

**Time:** O(n log n)

**Example:**
```
Items: (value, weight) = (60,10), (100,20), (120,30)
W = 50

Ratios: 60/10=6, 100/20=5, 120/30=4
Sorted: Item1(6), Item2(5), Item3(4)

Take Item1: W=50-10=40, value=60
Take Item2: W=40-20=20, value=60+100=160
Take 20/30 of Item3: value=160+120×(20/30)=160+80=240

Maximum value = 240
```

> **GATE Trap:** Greedy works for **Fractional** Knapsack but NOT for **0/1 Knapsack**!
> Example: Items = (60,10), (100,20), (120,30), W=50. Greedy gives 240, but 0/1 optimal is 220 (items 2,3).
> Actually, for fractional, greedy IS optimal. For 0/1, you need DP.

---

## 6.4 Huffman Coding ⭐⭐

**Problem:** Given characters with frequencies, find a prefix-free binary encoding that minimizes total encoding length.

> **Analogy:** In Morse code, common letters (E = ·) get shorter codes and rare letters (Q = − − · −) get longer codes. Huffman coding formalizes this optimally.

**Greedy Strategy:** Build a binary tree bottom-up by repeatedly merging the **two least frequent** nodes.

```
HuffmanCoding(chars, freqs):
    Create a min-heap Q from all characters
    while |Q| > 1:
        left = ExtractMin(Q)
        right = ExtractMin(Q)
        newNode = Node(freq = left.freq + right.freq)
        newNode.left = left
        newNode.right = right
        Insert(Q, newNode)
    return Q[0]  // Root of Huffman tree
```

**Time:** O(n log n) — n insertions/extractions on heap of size n

**Example:**
```
Characters: a(5), b(9), c(12), d(13), e(16), f(45)

Step 1: Merge a(5) + b(9) = [14]
Step 2: Merge c(12) + d(13) = [25]
Step 3: Merge [14] + e(16) = [30]
Step 4: Merge [25] + [30] = [55]
Step 5: Merge f(45) + [55] = [100]

Huffman Tree:
           (100)
          /     \
       f(45)   (55)
              /    \
           (25)   (30)
          /   \   /   \
       c(12) d(13) (14) e(16)
                  /   \
               a(5)  b(9)

Codes: f=0, c=100, d=101, a=1100, b=1101, e=111
```

**Total encoding length:** Σ(frequency × code length) = 45×1 + 12×3 + 13×3 + 5×4 + 9×4 + 16×3 = 45 + 36 + 39 + 20 + 36 + 48 = **224 bits**

### Key Properties

1. **Prefix-free:** No codeword is a prefix of another (required for unique decodability)
2. **Optimal:** Huffman coding minimizes weighted path length among all prefix-free codes
3. **Higher frequency → shorter code**
4. The two least frequent characters have the **same length** and differ only in the last bit
5. For n characters, Huffman tree has **n leaves** and **n-1 internal nodes**

> **GATE Trap:** Huffman coding is NOT unique — there can be multiple optimal Huffman trees. But the total cost (weighted path length) is always the same.

> **GATE Formula:** Cost = Σ(over all internal nodes) frequency of internal node = Σ(leaf freq × depth)

---

## 6.5 Job Sequencing with Deadlines

**Problem:** Given jobs with deadlines and profits, schedule jobs to maximize profit. Each job takes unit time.

**Greedy Strategy:** Sort jobs by profit (decreasing). For each job, schedule it at the **latest available slot** before its deadline.

```
JobSequencing(jobs, n):
    Sort jobs by profit (decreasing)
    maxDeadline = max of all deadlines
    slots[1..maxDeadline] = empty
    profit = 0
    for each job j (in decreasing profit order):
        for t = min(j.deadline, maxDeadline) downto 1:
            if slots[t] is empty:
                slots[t] = j
                profit += j.profit
                break
    return profit
```

**Time:** O(n²) naive, O(n log n) with disjoint sets

**Example:**
```
Jobs: (Id, Deadline, Profit) = (1,2,100), (2,1,19), (3,2,27), (4,1,25), (5,3,15)

Sorted by profit: J1(2,100), J3(2,27), J4(1,25), J2(1,19), J5(3,15)

J1: slot 2 → slots = [_, J1, _]
J3: slot 2 taken, slot 1 → slots = [J3, J1, _]
J4: slot 1 taken → skip
J2: slot 1 taken → skip
J5: slot 3 → slots = [J3, J1, J5]

Total profit = 27 + 100 + 15 = 142
```

---

## 6.6 Minimum Spanning Tree (MST) — Kruskal's Algorithm

**Problem:** Find a subset of edges that connects all vertices with minimum total weight and no cycles.

**Greedy Strategy:** Sort edges by weight. Add the lightest edge that doesn't form a cycle (using Union-Find).

```
Kruskal(G):
    Sort edges by weight (ascending)
    MST = {}
    Initialize Union-Find for each vertex
    for each edge (u, v, w) in sorted order:
        if Find(u) ≠ Find(v):    // No cycle
            MST = MST ∪ {(u,v)}
            Union(u, v)
    return MST
```

**Time:** O(E log E) = O(E log V) [since E ≤ V²]

> **Why O(E log E)?** Sorting E edges dominates. Union-Find with path compression + union by rank: nearly O(1) per operation (amortized α(n)).

### Key MST Properties for GATE

1. **Cut Property:** For any cut, the minimum weight edge crossing the cut is in some MST
2. **Cycle Property:** For any cycle, the maximum weight edge is NOT in any MST
3. **Uniqueness:** If all edge weights are distinct, the MST is unique
4. **Number of edges:** MST has exactly **V - 1** edges
5. **Adding an edge to MST creates exactly one cycle**
6. **Removing an edge from MST disconnects it into exactly two components**

---

## 6.7 Minimum Spanning Tree — Prim's Algorithm

**Greedy Strategy:** Start from any vertex. Repeatedly add the **lightest edge** connecting the tree to a vertex not yet in the tree.

```
Prim(G, source):
    key[v] = ∞ for all v; key[source] = 0
    inMST[v] = false for all v
    parent[source] = NIL
    Q = min-priority queue of all vertices by key

    while Q is not empty:
        u = ExtractMin(Q)
        inMST[u] = true
        for each neighbor v of u:
            if not inMST[v] and w(u,v) < key[v]:
                key[v] = w(u,v)
                parent[v] = u
                DecreaseKey(Q, v, key[v])
    return parent array (defines MST)
```

**Time Complexity:**

| Implementation | Time |
|---------------|------|
| Adjacency matrix + array | O(V²) |
| Adjacency list + binary heap | O((V + E) log V) |
| Adjacency list + Fibonacci heap | O(E + V log V) |

> **GATE Comparison:**
> | | Kruskal's | Prim's |
> |---|---|---|
> | Strategy | Edge-based | Vertex-based |
> | Data Structure | Union-Find | Priority Queue |
> | Better for | Sparse graphs (E ≈ V) | Dense graphs (E ≈ V²) |
> | Time | O(E log E) | O(V² or (V+E)log V) |

---

## 6.8 Dijkstra's Algorithm (Single-Source Shortest Path)

**Problem:** Find shortest paths from a source vertex to all other vertices. **Edge weights must be non-negative.**

**Greedy Strategy:** Always process the unvisited vertex with the **smallest tentative distance**.

```
Dijkstra(G, source):
    dist[v] = ∞ for all v; dist[source] = 0
    visited[v] = false
    Q = min-priority queue of all vertices by dist

    while Q is not empty:
        u = ExtractMin(Q)
        visited[u] = true
        for each neighbor v of u:
            if not visited[v] and dist[u] + w(u,v) < dist[v]:
                dist[v] = dist[u] + w(u,v)
                DecreaseKey(Q, v, dist[v])
    return dist[]
```

**Time Complexity:**

| Implementation | Time |
|---------------|------|
| Adjacency matrix + array | O(V²) |
| Adjacency list + binary heap | O((V + E) log V) |
| Adjacency list + Fibonacci heap | O(E + V log V) |

> **GATE Critical:** Dijkstra FAILS with negative weight edges!
> Example: A→B(1), A→C(5), B→C(-10). Dijkstra finalizes B with dist=1, but actual shortest to C through B is 1+(-10)=-9, which Dijkstra may miss.

> **Why greedy works here:** Once a vertex is "finalized" (extracted from min-heap), its shortest distance can't be improved — because all remaining paths go through vertices with equal or greater distance (no negative edges).

---

## 6.9 Huffman vs Shannon-Fano

| Property | Huffman | Shannon-Fano |
|----------|---------|-------------|
| Approach | Bottom-up (merge least frequent) | Top-down (divide into equal halves) |
| Optimality | ✅ Always optimal | ❌ Not always optimal |
| GATE relevance | High | Low (just know it exists) |

---

## 6.10 Greedy vs Dynamic Programming — When to Use Which?

| Greedy | Dynamic Programming |
|--------|-------------------|
| Makes one choice at each step | Considers all choices |
| No backtracking | Builds on all subproblem solutions |
| Works when greedy choice property holds | Works when optimal substructure holds |
| Generally faster | More versatile |
| Fractional Knapsack ✓ | 0/1 Knapsack ✓ |
| Activity Selection ✓ | Matrix Chain ✓ |
| Huffman Coding ✓ | LCS ✓ |

> **GATE Decision Rule:** "Can I prove a greedy choice property? If yes, use greedy. If not (or unsure), use DP."

---


---

# Chapter 7: Dynamic Programming

## 7.1 The DP Paradigm

> **Analogy:** Imagine climbing stairs. If someone asks "how many ways to climb 100 stairs?", you realize the answer for 100 depends on 99 and 98. Instead of recalculating from scratch each time (like recursion), you **write down answers on a cheat sheet** (table) and look them up when needed.

**Key Properties:**
1. **Optimal Substructure:** Optimal solution contains optimal solutions to subproblems
2. **Overlapping Subproblems:** Same subproblems are solved multiple times

**Two Approaches:**
| Approach | Description | Direction |
|----------|-------------|-----------|
| **Top-Down (Memoization)** | Recursive + cache results | Start from n, go down |
| **Bottom-Up (Tabulation)** | Iterative, fill table | Start from base, go up |

> **GATE Tip:** Bottom-up is usually preferred in GATE (easier to analyze time & space). Top-down is easier to code but has recursion overhead.

---

## 7.2 Fibonacci Numbers — DP Introduction

**Recurrence:** F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1

**Naive Recursion:** T(n) = T(n-1) + T(n-2) + O(1) → **O(φⁿ) ≈ O(1.618ⁿ)** — Exponential!

**Why exponential?** The recursion tree has massive overlap:
```
             F(5)
           /      \
        F(4)      F(3)
       /    \     /   \
    F(3)   F(2) F(2) F(1)
    /  \   ...  ...
  F(2) F(1)
```
F(2) is computed 3 times, F(3) is computed 2 times...

**DP Solution (Bottom-Up):**
```
Fibonacci(n):
    dp[0] = 0, dp[1] = 1
    for i = 2 to n:
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
**Time: O(n), Space: O(n)** — or O(1) space with two variables.

> **GATE Takeaway:** DP trades space for time. By storing results, we go from O(2ⁿ) to O(n).

---

## 7.3 Longest Common Subsequence (LCS) ⭐⭐

**Problem:** Given two strings X and Y, find the length of their longest common subsequence.

> **Subsequence vs Substring:** Subsequence doesn't need to be contiguous. "ACE" is a subsequence of "ABCDE", but "AE" is not a substring of "ABCDE".

**Recurrence:**

```
LCS(X, Y, i, j):
    if i == 0 or j == 0:
        return 0
    if X[i] == Y[j]:
        return 1 + LCS(X, Y, i-1, j-1)      // Characters match
    else:
        return max(LCS(X, Y, i-1, j),         // Skip from X
                   LCS(X, Y, i, j-1))         // Skip from Y
```

**Why this recurrence?**
- If last characters match: they're part of the LCS, solve for remaining
- If they don't match: the LCS either doesn't include X[i] or doesn't include Y[j]

**DP Table (Bottom-Up):**
```
LCS_DP(X, Y):
    m = |X|, n = |Y|
    dp[0..m][0..n] = 0
    for i = 1 to m:
        for j = 1 to n:
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

**Time: O(mn), Space: O(mn)** (can be reduced to O(min(m,n)) for just the length)

**Example:** X = "ABCBDAB", Y = "BDCAB"

```
    ""  B  D  C  A  B
""   0  0  0  0  0  0
A    0  0  0  0  1  1
B    0  1  1  1  1  2
C    0  1  1  2  2  2
B    0  1  1  2  2  3
D    0  1  2  2  2  3
A    0  1  2  2  3  3
B    0  1  2  2  3  4
```

**LCS length = 4** (e.g., "BCAB")

> **GATE Tricks:**
> - LCS of X with itself = X (length n)
> - LCS(X, reverse(X)) = Longest Palindromic Subsequence
> - Minimum insertions to make palindrome = n - LPS length
> - Minimum deletions to make strings equal = m + n - 2×LCS

---

## 7.4 Longest Increasing Subsequence (LIS)

**Problem:** Find the length of the longest strictly increasing subsequence.

**DP Approach — O(n²):**
```
LIS(A, n):
    dp[i] = length of LIS ending at index i
    dp[i] = 1 for all i
    for i = 1 to n-1:
        for j = 0 to i-1:
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp[0..n-1])
```

**Example:** A = [10, 22, 9, 33, 21, 50, 41, 60, 80]

```
dp = [1, 2, 1, 3, 2, 4, 4, 5, 6]
LIS length = 6 (subsequence: 10, 22, 33, 50, 60, 80)
```

**Optimized O(n log n) approach:** Use patience sorting with binary search.

> **GATE Fact:** LIS can be solved in O(n log n) using binary search on a "tails" array. This is frequently asked.

---

## 7.5 Matrix Chain Multiplication (MCM) ⭐⭐

**Problem:** Given matrices A₁, A₂, ..., Aₙ with dimensions p₀×p₁, p₁×p₂, ..., pₙ₋₁×pₙ, find the parenthesization that minimizes total scalar multiplications.

> **Why does order matter?** Multiplying (10×30)(30×5)(5×60):
> - ((A₁A₂)A₃) = 10×30×5 + 10×5×60 = 1500 + 3000 = 4500
> - (A₁(A₂A₃)) = 30×5×60 + 10×30×60 = 9000 + 18000 = 27000
> - Same result, but 4500 vs 27000 multiplications!

**Recurrence:**
```
m[i][j] = minimum cost to multiply Aᵢ...Aⱼ

m[i][j] = 0                          if i == j
m[i][j] = min over k from i to j-1 {
    m[i][k] + m[k+1][j] + pᵢ₋₁ × pₖ × pⱼ
}
```

**Why this recurrence?** We try every possible "split point" k: multiply (Aᵢ...Aₖ) and (Aₖ₊₁...Aⱼ) separately, then multiply the results. The cost of the final multiplication is pᵢ₋₁ × pₖ × pⱼ.

**DP Implementation:**
```
MCM(p, n):
    m[i][i] = 0 for all i
    for len = 2 to n:           // chain length
        for i = 1 to n-len+1:
            j = i + len - 1
            m[i][j] = ∞
            for k = i to j-1:
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k     // optimal split point
    return m[1][n]
```

**Time: O(n³), Space: O(n²)**

**Example:** Dimensions: 10×30, 30×5, 5×60 → p = [10, 30, 5, 60]

```
m[1][1]=0, m[2][2]=0, m[3][3]=0
m[1][2] = 10×30×5 = 1500
m[2][3] = 30×5×60 = 9000
m[1][3] = min(m[1][1]+m[2][3]+10×30×60, m[1][2]+m[3][3]+10×5×60)
        = min(0+9000+18000, 1500+0+3000) = min(27000, 4500) = 4500
```

> **GATE Trick:** The number of ways to parenthesize n matrices is the **Catalan number** C(n-1) = (2n-2)! / (n!(n-1)!). For n=4: C(3)=5 ways.

---

## 7.6 0/1 Knapsack Problem ⭐⭐

**Problem:** Given n items with weights wᵢ and values vᵢ, and knapsack capacity W. Maximize value with constraint: each item is either fully taken or not.

**Recurrence:**
```
K[i][w] = maximum value using items 1..i with capacity w

K[i][w] = K[i-1][w]                                    if wᵢ > w (can't take)
K[i][w] = max(K[i-1][w], K[i-1][w-wᵢ] + vᵢ)          if wᵢ ≤ w
```

**Why?** For each item, two choices: don't take it (K[i-1][w]) or take it (K[i-1][w-wᵢ] + vᵢ).

**DP Implementation:**
```
Knapsack01(v, w, n, W):
    K[0..n][0..W] = 0
    for i = 1 to n:
        for j = 0 to W:
            K[i][j] = K[i-1][j]          // Don't take item i
            if w[i] <= j:
                K[i][j] = max(K[i][j], K[i-1][j-w[i]] + v[i])  // Take it
    return K[n][W]
```

**Time: O(nW), Space: O(nW)** (reducible to O(W) with 1D array)

**Example:**
```
Items: (value, weight) = (1,1), (4,3), (5,4), (7,5)
W = 7

     w→  0  1  2  3  4  5  6  7
  i=0    0  0  0  0  0  0  0  0
  i=1    0  1  1  1  1  1  1  1
  i=2    0  1  1  4  5  5  5  5
  i=3    0  1  1  4  5  6  6  9
  i=4    0  1  1  4  5  7  8  9

Maximum value = 9 (items 2 and 3: value 4+5=9, weight 3+4=7)
```

> **GATE Important:**
> - 0/1 Knapsack is NP-Hard, but O(nW) is **pseudo-polynomial** (polynomial in W, exponential in bits of W)
> - If W is exponential in n, this is exponential
> - Fractional Knapsack: Greedy O(n log n), 0/1 Knapsack: DP O(nW)

---

## 7.7 Floyd-Warshall Algorithm (All-Pairs Shortest Paths) ⭐

**Problem:** Find shortest paths between ALL pairs of vertices.

**Key Idea:** Consider whether each vertex k can serve as an intermediate vertex on the shortest path from i to j.

**Recurrence:**
```
d[i][j][k] = shortest path from i to j using only vertices 1..k as intermediaries

d[i][j][0] = w(i,j)    // Direct edge weight (∞ if no edge)
d[i][j][k] = min(d[i][j][k-1], d[i][k][k-1] + d[k][j][k-1])
```

**Why?** Either vertex k is on the shortest path (go i→k→j) or it isn't (keep old path).

**Implementation (space-optimized):**
```
FloydWarshall(W, n):
    d = W          // Initialize with edge weights
    for k = 1 to n:
        for i = 1 to n:
            for j = 1 to n:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
```

**Time: O(V³), Space: O(V²)**

**Detecting Negative Cycles:** If d[i][i] < 0 for any i after the algorithm, there's a negative cycle.

> **GATE Comparison:**
> | Algorithm | Problem | Time | Negative Edges |
> |-----------|---------|------|---------------|
> | Dijkstra | Single-source | O(V² or (V+E)logV) | ❌ No |
> | Bellman-Ford | Single-source | O(VE) | ✅ Yes (detects cycles) |
> | Floyd-Warshall | All-pairs | O(V³) | ✅ Yes (detects cycles) |
> | BFS | Single-source (unweighted) | O(V+E) | N/A |

---

## 7.8 Bellman-Ford Algorithm ⭐

**Problem:** Single-source shortest paths. **Handles negative edges!**

**Key Idea:** Relax all edges V-1 times. After k iterations, we have shortest paths using at most k edges.

```
BellmanFord(G, source):
    dist[v] = ∞ for all v; dist[source] = 0
    for i = 1 to V-1:
        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    // Check for negative cycles
    for each edge (u, v, w):
        if dist[u] + w < dist[v]:
            return "Negative cycle exists!"
    return dist[]
```

**Time: O(VE), Space: O(V)**

**Why V-1 iterations?** Shortest path has at most V-1 edges (in a graph with V vertices and no negative cycles). Each iteration "extends" paths by one edge.

> **GATE Trap:** If after V-1 iterations, we can still relax an edge → **negative weight cycle exists!**

---

## 7.9 Edit Distance (Levenshtein Distance)

**Problem:** Minimum number of operations (insert, delete, replace) to convert string A to string B.

**Recurrence:**
```
dp[i][j] = edit distance between A[1..i] and B[1..j]

dp[i][0] = i    (delete all characters from A)
dp[0][j] = j    (insert all characters of B)

dp[i][j] = dp[i-1][j-1]                          if A[i] == B[j]
dp[i][j] = 1 + min(dp[i-1][j],    // Delete from A
                    dp[i][j-1],    // Insert into A
                    dp[i-1][j-1])  // Replace in A
```

**Time: O(mn), Space: O(mn)**

**Example:** A = "kitten", B = "sitting"

```
     ""  s  i  t  t  i  n  g
 ""   0  1  2  3  4  5  6  7
 k    1  1  2  3  4  5  6  7
 i    2  2  1  2  3  4  5  6
 t    3  3  2  1  2  3  4  5
 t    4  4  3  2  1  2  3  4
 e    5  5  4  3  2  2  3  4
 n    6  6  5  4  3  3  2  3

Edit distance = 3 (replace k→s, replace e→i, insert g)
```

---

## 7.10 Coin Change Problem

**Problem 1: Minimum coins to make amount V**

```
dp[0] = 0
dp[v] = min over all coins c { dp[v-c] + 1 }  where c ≤ v
```

**Problem 2: Number of ways to make amount V**

```
dp[0] = 1
for each coin c:
    for v = c to V:
        dp[v] += dp[v-c]
```

> **GATE Trap:** In Problem 2, iterating coins in the outer loop gives **combinations** (order doesn't matter). If V is in the outer loop, you get **permutations** (order matters).

---

## 7.11 DP Problem-Solving Strategy for GATE

1. **Identify:** Does the problem have optimal substructure and overlapping subproblems?
2. **Define state:** What does dp[i] or dp[i][j] represent?
3. **Write recurrence:** How does the current state relate to smaller states?
4. **Base cases:** What are the trivially known values?
5. **Order of computation:** Fill table so that all needed values are already computed
6. **Backtracking:** How to reconstruct the actual solution (not just the optimal value)?

---


---

# Chapter 8: Graph Algorithms

## 8.1 Graph Representations

### Adjacency Matrix
- 2D array of size V×V
- A[i][j] = 1 (or weight) if edge (i,j) exists, 0 otherwise
- **Space:** O(V²)
- **Edge lookup:** O(1)
- **Best for:** Dense graphs

### Adjacency List
- Array of V linked lists (or vectors)
- Each list[i] contains all neighbors of vertex i
- **Space:** O(V + E)
- **Edge lookup:** O(degree(v))
- **Best for:** Sparse graphs (most real-world graphs)

> **GATE Comparison:**
> | Operation | Matrix | List |
> |-----------|--------|------|
> | Space | O(V²) | O(V+E) |
> | Check edge (u,v) | O(1) | O(deg(u)) |
> | List neighbors | O(V) | O(deg(u)) |
> | Add edge | O(1) | O(1) |
> | BFS/DFS total | O(V²) | O(V+E) |

---

## 8.2 Breadth-First Search (BFS) ⭐⭐

> **Analogy:** Like dropping a stone in water — explore in expanding circles (level by level). First all neighbors, then neighbors of neighbors, etc.

```
BFS(G, source):
    visited[v] = false for all v
    queue Q
    visited[source] = true
    dist[source] = 0
    Q.enqueue(source)
    
    while Q is not empty:
        u = Q.dequeue()
        for each neighbor v of u:
            if not visited[v]:
                visited[v] = true
                dist[v] = dist[u] + 1
                parent[v] = u
                Q.enqueue(v)
```

| Property | Value |
|----------|-------|
| Time | O(V + E) |
| Space | O(V) — queue + visited array |
| Data Structure | **Queue** (FIFO) |
| Shortest Path | ✅ Yes (unweighted graphs) |

### BFS Applications

1. **Shortest path in unweighted graphs** — dist[v] gives minimum number of edges from source
2. **Level-order traversal** of a tree
3. **Connected components** — run BFS from each unvisited vertex
4. **Bipartite checking** — 2-color the graph using BFS levels
5. **Cycle detection in undirected graphs** — if BFS finds an already-visited non-parent vertex
6. **Minimum edges to disconnect** (edge connectivity)

### BFS Edge Classification

| Edge Type | Definition |
|-----------|-----------|
| **Tree edge** | Edge in BFS tree (u discovered v) |
| **Cross edge** | Edge between vertices at same or adjacent level |

> **GATE Fact:** BFS in an undirected graph produces only **tree edges and cross edges** (no back edges or forward edges). Cross edges connect vertices whose levels differ by at most 1.

---

## 8.3 Depth-First Search (DFS) ⭐⭐

> **Analogy:** Like exploring a maze — go as deep as possible, then backtrack when stuck.

```
DFS(G):
    visited[v] = false for all v
    time = 0
    for each vertex u in G:
        if not visited[u]:
            DFS-Visit(u)

DFS-Visit(u):
    visited[u] = true
    discovery[u] = ++time
    for each neighbor v of u:
        if not visited[v]:
            parent[v] = u
            DFS-Visit(v)
    finish[u] = ++time
```

| Property | Value |
|----------|-------|
| Time | O(V + E) |
| Space | O(V) — recursion stack + visited |
| Data Structure | **Stack** (implicit via recursion) |

### DFS Timestamps and Parenthesis Theorem

Each vertex u has:
- **discovery[u]:** when u is first visited
- **finish[u]:** when u's exploration is complete

**Parenthesis Theorem:** For any two vertices u and v:
- [d[u], f[u]] and [d[v], f[v]] are either **completely nested** or **completely disjoint**
- They **never partially overlap**

> **Meaning:** If u is an ancestor of v in DFS tree, then d[u] < d[v] < f[v] < f[u].

### DFS Edge Classification ⭐

| Edge (u,v) | Condition | Meaning |
|------------|-----------|---------|
| **Tree edge** | v is discovered via u | Part of DFS tree |
| **Back edge** | v is an ancestor of u | d[v] < d[u] < f[u] < f[v] |
| **Forward edge** | v is a descendant of u (not tree edge) | d[u] < d[v] < f[v] < f[u] |
| **Cross edge** | No ancestor-descendant relationship | d[v] < f[v] < d[u] < f[u] |

> **GATE Critical Facts:**
> - **Undirected graph:** DFS produces only **tree edges and back edges** (no forward or cross edges!)
> - **Directed graph:** All four types are possible
> - **Back edge ⟺ cycle exists** (in both directed and undirected)

### DFS Applications

1. **Cycle detection** — back edge exists ⟹ cycle exists
2. **Topological sort** — decreasing order of finish times
3. **Strongly connected components** (Kosaraju's/Tarjan's)
4. **Articulation points and bridges**
5. **Biconnected components**
6. **Path finding and connectivity**

---

## 8.4 Topological Sort ⭐

**Problem:** Given a DAG (Directed Acyclic Graph), arrange vertices in a linear order such that for every directed edge (u,v), u comes before v.

> **Analogy:** Course prerequisites — CS201 must come before CS301. Topological sort gives a valid course sequence.

### Method 1: DFS-Based

```
TopologicalSort(G):
    DFS(G) and compute finish times
    Output vertices in decreasing order of finish time
```

**Why?** If (u,v) is an edge, DFS finishes v before u. So higher finish time = earlier in order.

### Method 2: Kahn's Algorithm (BFS-Based)

```
KahnTopologicalSort(G):
    Compute in-degree of each vertex
    Q = queue of all vertices with in-degree 0
    order = []
    while Q is not empty:
        u = Q.dequeue()
        order.append(u)
        for each neighbor v of u:
            in-degree[v]--
            if in-degree[v] == 0:
                Q.enqueue(v)
    if |order| ≠ V: "Graph has a cycle!" (not a DAG)
    return order
```

**Time: O(V + E)**

> **GATE Facts:**
> - Topological sort exists **if and only if** the graph is a DAG
> - Topological order is **NOT unique** (multiple valid orderings possible)
> - Number of topological orderings can be exponential
> - Kahn's algorithm also detects cycles (if not all vertices are output)

---

## 8.5 Strongly Connected Components (SCC) ⭐

**Definition:** In a directed graph, a SCC is a maximal set of vertices such that every vertex is reachable from every other vertex in the set.

### Kosaraju's Algorithm

```
KosarajuSCC(G):
    1. Run DFS on G, compute finish times
    2. Compute Gᵀ (transpose graph — reverse all edges)
    3. Run DFS on Gᵀ in decreasing order of finish times
    4. Each DFS tree in step 3 is one SCC
```

**Time: O(V + E)**

**Why it works:**
- Step 1 finds the "exit order" — vertices that can "reach out" finish later
- Step 3 on Gᵀ finds vertices that can "reach back" — combined with step 1, this means both-way reachability = SCC

### Tarjan's Algorithm (Single DFS)

Uses a **stack** and **low-link values:**
- `disc[u]`: discovery time
- `low[u]`: lowest discovery time reachable from u's subtree via back edges

```
TarjanSCC(u):
    disc[u] = low[u] = ++timer
    stack.push(u)
    onStack[u] = true
    
    for each neighbor v of u:
        if disc[v] == -1:
            TarjanSCC(v)
            low[u] = min(low[u], low[v])
        elif onStack[v]:
            low[u] = min(low[u], disc[v])
    
    if low[u] == disc[u]:     // u is root of SCC
        SCC = {}
        repeat:
            v = stack.pop()
            onStack[v] = false
            SCC = SCC ∪ {v}
        until v == u
        Output SCC
```

> **GATE Fact:** A DAG of SCCs (condensation graph) is always acyclic. The number of SCCs in a graph can be from 1 (entire graph is one SCC) to V (each vertex is its own SCC).

---

## 8.6 Shortest Path Algorithms — Complete Summary

### 8.6.1 BFS (Unweighted)
- **Time:** O(V+E)
- **Works for:** Unweighted or unit-weight graphs
- **Negative edges:** N/A

### 8.6.2 Dijkstra's (Non-Negative Weights)
- Already covered in Chapter 6
- **Time:** O((V+E)log V) with binary heap
- **Fails with negative edges**

### 8.6.3 Bellman-Ford (Handles Negative Edges)
- Already covered in Chapter 7
- **Time:** O(VE)
- **Detects negative cycles**

### 8.6.4 Floyd-Warshall (All-Pairs)
- Already covered in Chapter 7
- **Time:** O(V³)

### 8.6.5 DAG Shortest Path
```
DAGShortestPath(G, source):
    TopSort = TopologicalSort(G)
    dist[v] = ∞ for all v; dist[source] = 0
    for each vertex u in TopSort order:
        for each neighbor v of u:
            if dist[u] + w(u,v) < dist[v]:
                dist[v] = dist[u] + w(u,v)
    return dist[]
```
- **Time:** O(V+E)
- **Works with negative edges** (no cycles possible in DAG)

### Master Comparison Table

| Algorithm | Type | Time | Space | Neg. Edges | Neg. Cycles |
|-----------|------|------|-------|------------|-------------|
| BFS | SSSP | O(V+E) | O(V) | N/A | N/A |
| Dijkstra | SSSP | O((V+E)logV) | O(V) | ❌ | ❌ |
| Bellman-Ford | SSSP | O(VE) | O(V) | ✅ | Detects ✅ |
| DAG Shortest | SSSP | O(V+E) | O(V) | ✅ | N/A (DAG) |
| Floyd-Warshall | APSP | O(V³) | O(V²) | ✅ | Detects ✅ |
| Johnson's | APSP | O(V²logV+VE) | O(V²) | ✅ | Detects ✅ |

> **GATE Decision Tree for Shortest Path:**
> - Unweighted? → **BFS**
> - DAG? → **DAG Shortest Path** (O(V+E))
> - Non-negative weights? → **Dijkstra**
> - Negative edges possible? → **Bellman-Ford**
> - All pairs needed? → **Floyd-Warshall** (or Johnson's for sparse graphs)

---

## 8.7 Minimum Spanning Tree — Additional Properties

### Properties Often Tested in GATE

1. **MST has V-1 edges** (it's a tree)
2. **Adding any non-MST edge creates exactly one cycle**
3. **Removing any MST edge disconnects the graph into 2 components**
4. **If all edge weights are distinct, MST is unique**
5. **If graph is not connected, MST doesn't exist** (but Minimum Spanning Forest does)
6. **Second-best MST** differs from best MST in exactly one edge swap
7. **Maximum edge in MST path from u to v = bottleneck of u-v path**

### MST and Shortest Path — Are They Related?

> **GATE Trap:** MST edge may NOT be on the shortest path!
> Example: Triangle A-B(1), B-C(1), A-C(3). MST uses A-B and B-C. But shortest A-C path uses direct edge (weight 3), not MST path (weight 2 through B)... wait, MST path IS shorter here. But in general, MST minimizes TOTAL weight, not individual path weights.

---

## 8.8 Articulation Points (Cut Vertices) and Bridges (Cut Edges)

**Articulation Point:** A vertex whose removal disconnects the graph.  
**Bridge:** An edge whose removal disconnects the graph.

### Finding Articulation Points (Tarjan's Method)

Use DFS with `disc[]` and `low[]`:

A vertex u is an articulation point if:
1. u is **root of DFS tree** and has **2 or more children**, OR
2. u is **not root** and has a child v such that **low[v] ≥ disc[u]** (no back edge from v's subtree goes above u)

### Finding Bridges

Edge (u,v) is a bridge if **low[v] > disc[u]** (strictly greater — no back edge from v's subtree reaches u or above).

**Time: O(V + E)**

> **GATE Note:**
> - Every bridge connects two articulation points (or one endpoint has degree 1)
> - A graph is **biconnected** if it has no articulation points
> - A tree has **V-1 bridges** and **V-2 articulation points** (all internal nodes)

---

## 8.9 Bipartite Graph Checking

**Bipartite:** Graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to the other.

**Algorithm:** BFS/DFS 2-coloring. Color source with color 0, all its neighbors with color 1, their neighbors with 0, etc. If a conflict arises (same color on both endpoints of an edge), the graph is NOT bipartite.

> **GATE Theorem:** A graph is bipartite **if and only if** it contains **no odd-length cycle**.

---


---

# Chapter 9: Backtracking & Branch and Bound

## 9.1 Backtracking — The Paradigm

> **Analogy:** Like navigating a maze — go forward, and when you hit a dead end, **backtrack** to the last decision point and try a different path. You systematically explore all possibilities but **prune** paths that can't lead to a solution.

**When to use:** Problems requiring exploration of all possible configurations (permutations, combinations, subsets) where some paths can be eliminated early.

**General Template:**
```
Backtrack(state):
    if state is a complete solution:
        process/output the solution
        return
    for each possible next choice:
        if choice is valid (pruning condition):
            make the choice
            Backtrack(new state)
            undo the choice          // BACKTRACK
```

**Key difference from brute force:** Backtracking **prunes** (skips) branches that are guaranteed not to lead to valid solutions.

---

## 9.2 N-Queens Problem ⭐

**Problem:** Place N queens on an N×N chessboard such that no two queens attack each other (no two in same row, column, or diagonal).

```
NQueens(board, row):
    if row == N:
        print board        // All queens placed
        return
    for col = 0 to N-1:
        if isSafe(board, row, col):
            board[row] = col
            NQueens(board, row + 1)
            board[row] = -1     // Backtrack

isSafe(board, row, col):
    for i = 0 to row-1:
        if board[i] == col:                         return false  // Same column
        if |board[i] - col| == |i - row|:           return false  // Same diagonal
    return true
```

**Time Complexity:** O(N!) approximately (with pruning, much less in practice)

**Solutions for small N:**
| N | # Solutions |
|---|-------------|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 8 | 92 |

> **GATE Note:** The N-Queens problem has no known polynomial-time algorithm. The decision version (does a solution exist for N ≥ 4?) always returns YES, but finding all solutions requires exponential time.

---

## 9.3 Subset Sum Problem

**Problem:** Given a set S of n integers and a target T, find if there exists a subset whose sum equals T.

```
SubsetSum(S, n, T, subset):
    if T == 0:
        print subset
        return true
    if n == 0:
        return false
    // Pruning: skip if current element > target
    if S[n] > T:
        return SubsetSum(S, n-1, T, subset)
    // Include S[n] or exclude it
    return SubsetSum(S, n-1, T-S[n], subset ∪ {S[n]}) OR
           SubsetSum(S, n-1, T, subset)
```

**With additional pruning:** Sort the array and use the remaining sum to prune:
- If `sum of remaining elements < T`, stop (can't reach target)
- If `current element > T`, stop (overshot)

> **GATE Fact:** Subset Sum is NP-Complete. The backtracking solution with pruning is much faster than 2ⁿ in practice but still exponential in the worst case.

---

## 9.4 Graph Coloring

**Problem:** Assign m colors to vertices such that no two adjacent vertices have the same color. Find if a valid coloring exists (or find all valid colorings).

```
GraphColoring(graph, colors, vertex):
    if vertex == V:
        print colors
        return true
    for c = 1 to m:
        if isSafe(graph, colors, vertex, c):
            colors[vertex] = c
            if GraphColoring(graph, colors, vertex + 1):
                return true
            colors[vertex] = 0    // Backtrack
    return false

isSafe(graph, colors, vertex, c):
    for each neighbor u of vertex:
        if colors[u] == c:
            return false
    return true
```

> **GATE Facts:**
> - **Chromatic number** χ(G) = minimum number of colors needed
> - **Complete graph Kₙ:** χ(Kₙ) = n
> - **Bipartite graph:** χ(G) = 2 (if non-trivial)
> - **Tree:** χ(T) = 2 (trees are bipartite)
> - **Odd cycle:** χ = 3
> - **Planar graph:** χ ≤ 4 (Four Color Theorem)
> - Graph coloring is NP-Complete for m ≥ 3 colors

---

## 9.5 Hamiltonian Path/Cycle

**Problem:** Find a path/cycle that visits every vertex exactly once.

```
HamiltonianCycle(graph, path, pos):
    if pos == V:
        if graph[path[pos-1]][path[0]]:    // Last vertex connected to first
            return true
        return false
    for v = 1 to V-1:
        if isSafe(v, graph, path, pos):
            path[pos] = v
            if HamiltonianCycle(graph, path, pos + 1):
                return true
            path[pos] = -1    // Backtrack
    return false
```

> **GATE Comparison:**
> | Property | Eulerian Path/Circuit | Hamiltonian Path/Cycle |
> |----------|----------------------|----------------------|
> | Visits | Every **edge** once | Every **vertex** once |
> | Easy check exists? | ✅ Yes (degree conditions) | ❌ No (NP-Complete) |
> | Euler condition (undirected) | Connected + all even degrees | No simple condition |
> | Complexity | O(E) — Hierholzer's | NP-Complete |

---

## 9.6 Branch and Bound

> **Analogy:** Like backtracking, but instead of just checking if a path is valid, we also estimate whether this path can lead to a BETTER solution than what we already have. If not, we prune it.

**Key difference from Backtracking:**
| Backtracking | Branch and Bound |
|-------------|-----------------|
| For feasibility problems | For optimization problems |
| Prunes infeasible paths | Prunes suboptimal paths |
| No bound computation | Computes bounds to prune |

### Branch and Bound for 0/1 Knapsack

**Strategy:** Use a priority queue (best-first search). At each node:
- **Bound:** Upper bound on best value achievable from this node (using fractional relaxation)
- **Prune:** If bound ≤ current best, skip this branch

```
BB_Knapsack(items, W):
    Sort items by value/weight ratio (decreasing)
    Q = priority queue (max-heap by bound)
    best = 0
    Q.push(root node with bound = totalValue)
    
    while Q is not empty:
        node = Q.pop()
        if node.bound <= best: continue      // Prune
        if node.level == n: continue
        
        // Branch: include next item
        include = node + item[node.level]
        if include.weight ≤ W and include.value > best:
            best = include.value
        include.bound = computeBound(include)
        if include.bound > best:
            Q.push(include)
        
        // Branch: exclude next item
        exclude = node (without item[node.level])
        exclude.bound = computeBound(exclude)
        if exclude.bound > best:
            Q.push(exclude)
    
    return best
```

### Branch and Bound for TSP

**Travelling Salesman Problem:** Find minimum cost Hamiltonian cycle.

**Lower bound estimation:** Reduce the cost matrix by subtracting row and column minimums. The sum of reductions gives a lower bound.

**Strategy:**
1. Start with the reduced cost matrix
2. For each possible next city, compute the reduced cost
3. Explore the node with the **minimum lower bound** (best-first)
4. Prune branches whose lower bound ≥ current best tour cost

> **GATE Fact:** TSP is NP-Hard. Branch and Bound doesn't change the worst-case complexity but dramatically reduces average exploration.

---

## 9.7 Comparison: Backtracking vs Branch and Bound vs DP

| Feature | Backtracking | Branch & Bound | DP |
|---------|-------------|---------------|-----|
| Problem type | Feasibility | Optimization | Optimization |
| Search | DFS | BFS/Best-first | Bottom-up |
| Pruning | Validity check | Bound-based | Subproblems |
| State space | Tree | Tree | Table |
| All solutions | ✅ Can find all | ❌ Usually one | ❌ Usually one |
| Optimal | ❌ First found | ✅ Guaranteed | ✅ Guaranteed |

---


---

# Chapter 10: String Matching Algorithms

## 10.1 The Problem

**Given:** Text T of length n, Pattern P of length m. Find all occurrences of P in T.

> **Analogy:** Like using Ctrl+F to find a word in a document. How efficiently can the computer do this?

---

## 10.2 Naive (Brute Force) String Matching

```
NaiveMatch(T, P):
    n = |T|, m = |P|
    for s = 0 to n-m:
        match = true
        for j = 0 to m-1:
            if T[s+j] ≠ P[j]:
                match = false
                break
        if match:
            print "Pattern found at shift " + s
```

| Metric | Value |
|--------|-------|
| Best Case | O(n) — first character always mismatches |
| Worst Case | **O((n-m+1)×m) = O(nm)** |
| Space | O(1) |

**Worst case example:** T = "AAAAAAAAB", P = "AAAB" — mismatch always at last character.

---

## 10.3 KMP Algorithm (Knuth-Morris-Pratt) ⭐⭐

> **Key Insight:** When a mismatch occurs, we already know some of the characters that match. Don't re-compare them! Use a **prefix function (failure function)** to skip ahead.

### The Prefix Function (LPS Array)

**LPS[i]** = length of the longest **proper prefix** of P[0..i] that is also a **suffix** of P[0..i].

**How to compute:**
```
ComputeLPS(P, m):
    LPS[0] = 0
    len = 0          // length of previous longest prefix suffix
    i = 1
    while i < m:
        if P[i] == P[len]:
            len++
            LPS[i] = len
            i++
        else:
            if len != 0:
                len = LPS[len-1]    // Key: don't increment i!
            else:
                LPS[i] = 0
                i++
    return LPS
```

**Example:** P = "ABCABD"
```
i=0: LPS[0] = 0                          → [0, _, _, _, _, _]
i=1: P[1]='B' ≠ P[0]='A' → LPS[1] = 0   → [0, 0, _, _, _, _]
i=2: P[2]='C' ≠ P[0]='A' → LPS[2] = 0   → [0, 0, 0, _, _, _]
i=3: P[3]='A' = P[0]='A' → LPS[3] = 1   → [0, 0, 0, 1, _, _]
i=4: P[4]='B' = P[1]='B' → LPS[4] = 2   → [0, 0, 0, 1, 2, _]
i=5: P[5]='D' ≠ P[2]='C', len=LPS[1]=0
     P[5]='D' ≠ P[0]='A' → LPS[5] = 0   → [0, 0, 0, 1, 2, 0]
```

### KMP Search

```
KMP(T, P):
    n = |T|, m = |P|
    LPS = ComputeLPS(P, m)
    i = 0    // index in T
    j = 0    // index in P
    while i < n:
        if T[i] == P[j]:
            i++; j++
        if j == m:
            print "Pattern found at index " + (i-j)
            j = LPS[j-1]
        elif i < n and T[i] ≠ P[j]:
            if j != 0:
                j = LPS[j-1]    // Use failure function (don't move i!)
            else:
                i++
```

| Metric | Value |
|--------|-------|
| Preprocessing | O(m) — building LPS array |
| Matching | **O(n)** |
| Total | **O(n + m)** |
| Space | O(m) — for LPS array |

### Why KMP is O(n)?

**Key observation:** In each step, either:
- i advances (happens at most n times), OR
- j decreases (but j can't decrease more than it has increased, which is at most n times)

Total steps ≤ 2n → **O(n)**

> **GATE Favorite Questions:**
> 1. "Build the LPS/failure function array for pattern P" — Very common!
> 2. "How many character comparisons does KMP make?"
> 3. "What is the worst-case number of comparisons?"

---

## 10.4 Rabin-Karp Algorithm ⭐

> **Key Idea:** Use **hashing** to compare pattern with text windows. Only do character-by-character comparison when hashes match.

### Rolling Hash

**Hash function:** Treat string as a number in base d (alphabet size):
```
hash("abc") = a × d² + b × d¹ + c × d⁰
```

**Rolling hash update:** When sliding from T[s..s+m-1] to T[s+1..s+m]:
```
h(s+1) = d × (h(s) - T[s] × dᵐ⁻¹) + T[s+m]
```

**All computations done mod q** (a large prime) to prevent overflow.

```
RabinKarp(T, P, d, q):
    n = |T|, m = |P|
    h = d^(m-1) mod q        // Precompute highest power
    p = hash(P)              // Pattern hash
    t = hash(T[0..m-1])      // First window hash
    
    for s = 0 to n-m:
        if t == p:
            // Verify character by character (avoid spurious hits)
            if T[s..s+m-1] == P[0..m-1]:
                print "Pattern found at shift " + s
        if s < n-m:
            t = (d × (t - T[s] × h) + T[s+m]) mod q
```

| Metric | Value |
|--------|-------|
| Best/Average | **O(n + m)** |
| Worst Case | **O(nm)** — many spurious hash matches |
| Space | O(1) |

**When is worst case?** When hash function has many collisions. Example: all characters same, T = "AAAA...A", P = "AAA".

> **GATE Facts:**
> - Rabin-Karp is great for **multiple pattern search** (compute hash for each pattern)
> - Average case is O(n+m) with a good hash function
> - Used in plagiarism detection (multiple substring matching)
> - The hash function choice significantly affects performance

---

## 10.5 Finite Automaton Based Matching

**Idea:** Build a DFA (Deterministic Finite Automaton) for the pattern, then process text through it.

**State:** Number of characters matched so far.
**Transition function:** δ(state, character) = length of longest proper suffix of P[0..state]+character that is a prefix of P.

| Metric | Value |
|--------|-------|
| Preprocessing | O(m × |Σ|) — building transition table |
| Matching | **O(n)** — single pass through text |
| Space | O(m × |Σ|) |

> **Comparison with KMP:** KMP uses LPS to implicitly handle the same transitions with O(m) space instead of O(m|Σ|).

---

## 10.6 Comparison of String Matching Algorithms

| Algorithm | Preprocessing | Matching | Total | Space |
|-----------|---------------|----------|-------|-------|
| Naive | None | O(nm) | O(nm) | O(1) |
| KMP | O(m) | O(n) | **O(n+m)** | O(m) |
| Rabin-Karp | O(m) | O(n) avg | O(n+m) avg | O(1) |
| Finite Automaton | O(m\|Σ\|) | O(n) | O(n+m\|Σ\|) | O(m\|Σ\|) |

---


---

# Chapter 11: Complexity Classes & NP-Completeness

## 11.1 Why This Matters

> **The Biggest Open Question in Computer Science:** Is **P = NP**? This $1 million Millennium Prize Problem asks whether every problem whose solution can be verified quickly can also be solved quickly.

Understanding complexity classes helps you:
1. Know when to stop searching for an efficient algorithm (the problem is hard!)
2. Recognize NP-Complete problems in exams and in practice
3. Use approximation or heuristic algorithms instead

---

## 11.2 Decision Problems

A **decision problem** is one with a yes/no answer. Every optimization problem can be converted to a decision version.

| Optimization | Decision Version |
|-------------|-----------------|
| Shortest path from s to t | Is there a path from s to t with length ≤ k? |
| Minimum vertex cover | Is there a vertex cover of size ≤ k? |
| Maximum clique | Is there a clique of size ≥ k? |

---

## 11.3 Complexity Classes — Definitions

### Class P (Polynomial Time)

**P** = Set of decision problems solvable by a **deterministic** Turing machine in **polynomial time** O(nᵏ) for some constant k.

**Examples in P:**
- Sorting (O(n log n))
- Shortest path (O(V² or (V+E)log V))
- MST (O(E log V))
- 2-SAT, 2-coloring
- Matching in bipartite graphs
- Linear programming

> **Intuition:** "Problems we can SOLVE efficiently."

### Class NP (Nondeterministic Polynomial Time)

**NP** = Set of decision problems where a YES answer can be **verified** by a deterministic Turing machine in polynomial time, given a **certificate** (witness/proof).

**Alternative definition:** Problems solvable by a **nondeterministic** Turing machine in polynomial time.

**Examples in NP:**
- All problems in P (trivially — if you can solve it, you can verify it)
- SAT, 3-SAT
- Hamiltonian cycle (certificate: the cycle itself — verify in O(V))
- Graph coloring (certificate: the coloring — verify in O(V+E))
- Subset sum (certificate: the subset — verify in O(n))
- Travelling Salesman (decision version)

> **Intuition:** "Problems where we can VERIFY a solution efficiently."

> **GATE Critical:** **P ⊆ NP** always holds. The open question is whether **P = NP** or **P ⊂ NP** (strict subset).

### Class co-NP

**co-NP** = Set of decision problems where a NO answer can be verified in polynomial time.

**Example:** "Is this number composite?" is in NP (certificate: a factor). "Is this number prime?" is in co-NP (and also in P — AKS primality test).

---

### Class NP-Hard

**NP-Hard** = A problem H is NP-Hard if every problem in NP can be **polynomial-time reduced** to H.

In other words: H is "at least as hard as" the hardest problems in NP.

> **NP-Hard problems are NOT necessarily in NP!** They could be even harder (undecidable, for example).

**Examples:** Halting problem (undecidable, NP-Hard but not in NP), TSP optimization version.

### Class NP-Complete

**NP-Complete** = NP ∩ NP-Hard

A problem L is NP-Complete if:
1. L ∈ NP (solutions can be verified in polynomial time)
2. L is NP-Hard (every NP problem reduces to L)

> **Intuition:** "The hardest problems in NP."

```
         ┌─────────────────────────┐
         │           NP-Hard       │
         │    ┌──────────────┐     │
         │    │  NP-Complete │     │
         │    │   ┌──────┐   │     │
         │    │   │  P   │   │     │
         │    │   └──────┘   │     │
         │    └──────────────┘     │
         │          NP             │
         └─────────────────────────┘
```

(Assuming P ≠ NP)

---

## 11.4 Polynomial-Time Reductions

**Definition:** Problem A reduces to problem B (written A ≤ₚ B) if there exists a polynomial-time function f such that:
- x is a YES instance of A ⟺ f(x) is a YES instance of B

**What this means:** If we can solve B, we can solve A (by transforming A's input to B's format).

**Key implication:** If A ≤ₚ B and A is NP-Hard → B is NP-Hard too!

> **Analogy:** "If I can't climb a 100m wall (A), and a 200m wall (B) is definitely not easier, then I can't climb B either."

**Direction of reduction (GATE TRAP):**

To prove X is NP-Complete:
1. Show X ∈ NP
2. Take a **known NP-Complete** problem Y
3. Show Y ≤ₚ X (reduce FROM the known hard problem TO the new problem)

> **Common mistake:** Students reduce in the wrong direction! Always reduce FROM the known NP-Complete problem TO the one you're trying to prove NP-Complete.

---

## 11.5 Cook's Theorem (SAT is NP-Complete) — The First NP-Complete Problem

**SAT (Boolean Satisfiability):** Given a Boolean formula, is there an assignment of variables that makes it TRUE?

**Cook-Levin Theorem (1971):** SAT is NP-Complete.

**Proof idea:** Any NP problem can be expressed as a polynomial-time verification by a Turing machine. The TM's computation can be encoded as a Boolean formula that is satisfiable iff the TM accepts.

> **Significance:** This was the FIRST problem proved NP-Complete. All subsequent proofs reduce from SAT (or from other known NP-Complete problems).

---

## 11.6 Famous NP-Complete Problems ⭐

| Problem | Description |
|---------|-------------|
| **SAT** | Is a Boolean formula satisfiable? |
| **3-SAT** | SAT with each clause having exactly 3 literals |
| **Vertex Cover** | Is there a vertex cover of size ≤ k? |
| **Independent Set** | Is there an independent set of size ≥ k? |
| **Clique** | Is there a clique of size ≥ k? |
| **Hamiltonian Cycle** | Does a Hamiltonian cycle exist? |
| **TSP (decision)** | Is there a tour of cost ≤ k? |
| **Subset Sum** | Is there a subset summing to T? |
| **Graph Coloring (≥3)** | Can the graph be colored with ≤ k colors (k≥3)? |
| **3D Matching** | Does a perfect 3D matching exist? |
| **Set Cover** | Can the universe be covered with ≤ k sets? |
| **Partition** | Can a set be split into two equal-sum subsets? |
| **0/1 Knapsack (decision)** | Is there a subset with weight ≤ W and value ≥ V? |

### Standard Reduction Chain

```
SAT → 3-SAT → Clique → Vertex Cover → Independent Set
                  ↓
            Hamiltonian Cycle → TSP
                  ↓
            Subset Sum → Partition → Knapsack
                  ↓
            3-Coloring → k-Coloring
```

---

## 11.7 Key Relationships for GATE

### Problems in P (polynomial time solvable)

| Problem | Time |
|---------|------|
| 2-SAT | O(V+E) |
| 2-Coloring (Bipartite check) | O(V+E) |
| Shortest Path | O(V² or (V+E)logV) |
| MST | O(E log V) |
| Maximum Bipartite Matching | O(V·E) |
| Euler Circuit | O(E) |
| Topological Sort | O(V+E) |

### NP-Complete (no known polynomial solution)

| Problem | NP-Complete? |
|---------|-------------|
| 3-SAT | ✅ |
| 2-SAT | ❌ (in P!) |
| 3-Coloring | ✅ |
| 2-Coloring | ❌ (in P!) |
| Hamiltonian Path | ✅ |
| Euler Path | ❌ (in P!) |
| 0/1 Knapsack | ✅ |
| Fractional Knapsack | ❌ (in P!) |

> **GATE Pattern:** Often "2 vs 3" determines complexity:
> - 2-SAT (P) vs 3-SAT (NPC)
> - 2-Coloring (P) vs 3-Coloring (NPC)
> - 2-Partition (P for some variants) vs 3-Partition (NPC)

---

## 11.8 Important Theorems for GATE

1. **If any NP-Complete problem has a polynomial-time algorithm, then P = NP**
2. **If P ≠ NP, no NP-Complete problem has a polynomial-time algorithm**
3. **Complement:** If L is NP-Complete and L's complement is in NP, and if P = NP, then NP = co-NP
4. **Vertex Cover + Independent Set + Clique:** These are related:
   - S is a vertex cover ⟺ V-S is an independent set
   - G has a clique of size k ⟺ complement graph G̅ has an independent set of size k

5. **Transitivity of reductions:** If A ≤ₚ B and B ≤ₚ C, then A ≤ₚ C

---

## 11.9 Pseudo-Polynomial and Approximation

### Pseudo-Polynomial Algorithms

Some NP-Complete problems have algorithms that are polynomial in the **numeric value** of input but exponential in the **size (bits)** of input.

**Example:** 0/1 Knapsack O(nW) — polynomial in n and W, but W could need log W bits to represent. If W = 2ⁿ, this is O(n·2ⁿ) = exponential.

> **GATE Fact:** Problems that are NP-Complete but have pseudo-polynomial algorithms are called **weakly NP-Complete** (e.g., Subset Sum, Knapsack, Partition).

> Problems that remain NP-Complete even with unary input are **strongly NP-Complete** (e.g., 3-SAT, 3-Coloring, TSP).

### Approximation Algorithms

When exact solutions are too slow, use approximation:

| Problem | Best Approximation Ratio |
|---------|-------------------------|
| Vertex Cover | 2-approximation (always within factor 2 of optimal) |
| TSP (metric) | 3/2-approximation (Christofides) |
| Set Cover | O(log n)-approximation |
| MAX-SAT | 3/4-approximation |
| General TSP | No constant-factor approximation (unless P=NP) |

---


---

# Chapter 12: Amortized Analysis

## 12.1 What is Amortized Analysis?

> **Analogy:** Imagine you put money in a piggy bank every day. Some days you withdraw a large amount. If someone sees only the withdrawal day, they think you're spending a lot. But **amortized** over many days, your average spending is low. Amortized analysis gives a **more accurate average** cost per operation in a sequence.

**Key idea:** Instead of analyzing the worst-case cost of a **single operation**, analyze the **average cost per operation** over a **sequence of operations**.

**Important:** This is NOT average-case analysis (which uses probability). Amortized analysis is a **worst-case guarantee** for the total cost of a sequence.

---

## 12.2 Three Methods of Amortized Analysis

### Method 1: Aggregate Method

**Idea:** Compute the total cost of n operations, then divide by n.

**amortized cost = T(n) / n**

**Example: Stack with Multipop**

Stack supports:
- PUSH(x) — cost 1
- POP() — cost 1
- MULTIPOP(k) — pop min(k, stack_size) elements, cost = min(k, stack_size)

**Worst case of MULTIPOP:** O(n) if stack has n elements.

**But amortized?** In n operations:
- Each element is pushed at most once → at most n pushes (total cost n)
- Each element can be popped at most once → total pops ≤ n
- Total cost of n operations ≤ 2n

**Amortized cost per operation = 2n/n = O(1)** ✓

---

### Method 2: Accounting Method (Banker's Method)

**Idea:** Charge each operation an **amortized cost**. If the amortized cost exceeds the actual cost, the difference is stored as **credit** on the data structure. Later, expensive operations use this credit.

**Rule:** Total amortized cost ≥ Total actual cost (credit never goes negative)

**Example: Stack with Multipop**

| Operation | Actual Cost | Amortized Cost | Credit Change |
|-----------|------------|----------------|---------------|
| PUSH | 1 | **2** | +1 per element |
| POP | 1 | 0 | -1 (use element's credit) |
| MULTIPOP(k) | k | 0 | -k (use elements' credits) |

Each PUSH pays 1 for itself + 1 as "prepayment" for a future POP/MULTIPOP.

Total amortized cost of n operations = at most 2n → **amortized O(1) per operation**.

> **Why this works:** We're "overcharging" cheap operations to "subsidize" expensive ones.

---

### Method 3: Potential Method (Physicist's Method)

**Idea:** Define a **potential function** Φ that maps the state of the data structure to a number. The amortized cost is:

```
ĉᵢ = cᵢ + Φ(Dᵢ) - Φ(Dᵢ₋₁)
```

where cᵢ is the actual cost, Dᵢ is the state after operation i.

**Requirements:**
- Φ(D₀) = 0 (initial potential)
- Φ(Dᵢ) ≥ 0 for all i (potential never negative)

**Total amortized cost = Σĉᵢ = Σcᵢ + Φ(Dₙ) - Φ(D₀) ≥ Σcᵢ**

**Example: Stack with Multipop**

Let Φ = number of elements in the stack.

| Operation | Actual Cost cᵢ | ΔΦ | Amortized ĉᵢ |
|-----------|---------------|-----|---------------|
| PUSH | 1 | +1 | 1 + 1 = **2** |
| POP | 1 | -1 | 1 - 1 = **0** |
| MULTIPOP(k) | k | -k | k - k = **0** |

Amortized cost per operation = **O(1)** ✓

---

## 12.3 Classic Example: Dynamic Array (Amortized Doubling) ⭐

**Scenario:** An array that doubles in size when full.

| Operation | Actual Cost |
|-----------|------------|
| INSERT (no resize) | O(1) |
| INSERT (with resize) | O(n) — copy all n elements |

**Is INSERT O(n) or O(1)?**

### Aggregate Analysis

For n insertions:
- Resize happens at sizes 1, 2, 4, 8, ..., 2ᵏ where 2ᵏ ≤ n
- Total resize cost = 1 + 2 + 4 + ... + 2ᵏ < 2n

Total cost = n (for insertions) + 2n (for all resizes) = 3n

**Amortized cost per INSERT = 3n/n = O(1)** ✓

### Accounting Analysis

Charge each INSERT **3 units:**
- 1 for the insertion itself
- 1 prepaid for copying THIS element in a future resize
- 1 prepaid for copying an OLD element that didn't pay for itself

### Potential Analysis

Let Φ = 2 × (number of elements) - (capacity of array)

After resize: array is half full, so Φ = 2(n/2) - n = 0  
Just before resize: array is full, so Φ = 2n - n = n

INSERT without resize: cᵢ = 1, ΔΦ = 2, ĉᵢ = 3  
INSERT with resize from capacity n to 2n: cᵢ = n+1, ΔΦ = 2-(2n-n) = 2-n, ĉᵢ = n+1+2-n = **3**

**Amortized cost = O(1)** in all cases ✓

> **GATE Application:** This is why `ArrayList` in Java / `vector` in C++ / `list` in Python have O(1) amortized append, despite occasional O(n) resizing.

---

## 12.4 Amortized Analysis of Union-Find

With **union by rank** and **path compression:**

| Per operation | Actual worst case | Amortized |
|--------------|-------------------|-----------|
| FIND | O(log n) | **O(α(n))** |
| UNION | O(log n) | **O(α(n))** |

where α(n) is the **inverse Ackermann function** — grows so slowly that α(n) ≤ 4 for any practical n (up to ~10⁸⁰).

> **GATE Fact:** For all practical purposes, Union-Find operations are **O(1) amortized**.

---

## 12.5 Amortized Analysis of Splay Trees

A splay tree guarantees that any sequence of m operations on a tree with n nodes takes **O(m log n)** total time.

**Amortized cost per operation: O(log n)**

Even though individual operations can take O(n), the splay operation ensures frequently accessed elements move to the root, amortizing the cost.

> **GATE Fact:** Splay trees have O(log n) amortized time for search, insert, and delete, but O(n) worst case for a single operation.

---

## 12.6 When to Use Which Method

| Method | Best When | Difficulty |
|--------|-----------|-----------|
| Aggregate | Total cost is easy to bound directly | Easiest |
| Accounting | Different operations have clearly different costs | Medium |
| Potential | Need a precise mathematical proof | Hardest |

> **GATE Tip:** For GATE questions, the aggregate method usually suffices. Potential method is needed for rigorous proofs (rarely asked in detail).

---


---

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

# Chapter 14: GATE Exam Strategy & PYQ Patterns

## 14.1 Topic-wise Weightage in GATE (Approximate)

| Topic | Weightage | Difficulty | Priority |
|-------|-----------|-----------|----------|
| **Asymptotic Analysis** | 2-4 marks | Easy-Medium | ⭐⭐⭐ |
| **Recurrences** | 2-4 marks | Medium | ⭐⭐⭐ |
| **Sorting** | 2-4 marks | Medium | ⭐⭐⭐ |
| **Graph Algorithms** | 4-8 marks | Medium-Hard | ⭐⭐⭐⭐⭐ |
| **Greedy** | 2-4 marks | Medium | ⭐⭐⭐⭐ |
| **Dynamic Programming** | 4-6 marks | Hard | ⭐⭐⭐⭐⭐ |
| **NP-Completeness** | 2-4 marks | Medium | ⭐⭐⭐ |
| **Searching** | 1-2 marks | Easy | ⭐⭐ |
| **Hashing** | 1-2 marks | Easy-Medium | ⭐⭐ |
| **String Matching** | 0-2 marks | Medium | ⭐⭐ |

> **Strategy:** Master Graph Algorithms and DP — together they account for ~50% of algorithm questions.

---

## 14.2 Common GATE Question Patterns

### Pattern 1: "Find the time complexity"

**Strategy:**
1. Identify the loop structure (nested? dependent? multiplicative?)
2. Write the recurrence if recursive
3. Apply Master Theorem or summation
4. Check for common patterns from Chapter 1

**Common traps:**
- `i = i * 2` → O(log n), not O(n)
- Nested dependent loops → sum, not multiply
- `for(i=1; i<=n; i++) for(j=1; j<=n; j+=i)` → O(n log n) (harmonic series)

### Pattern 2: "Apply algorithm X to this input"

**Strategy:** Trace through the algorithm step by step. These are FREE marks if you know the algorithm well.

**Most commonly asked:**
- Dijkstra's on a weighted graph
- BFS/DFS traversal order
- Quick sort partition steps
- Build heap from array
- Huffman coding tree
- KMP failure function computation

### Pattern 3: "Which of the following is true?"

**Strategy:** Know the properties! These are theory questions testing deep understanding.

**Commonly tested properties:**
- MST uniqueness conditions
- DFS edge classification (back edge → cycle)
- Stable vs unstable sorts
- When greedy works vs when DP is needed
- NP-Complete relationships

### Pattern 4: "Minimum comparisons to..."

**Strategy:** Know the lower bounds from Chapter 13.
- Find max: n-1
- Find max and min: ⌈3n/2⌉ - 2
- Find 2nd largest: n + ⌈log₂ n⌉ - 2
- Sort: ⌈log₂(n!)⌉
- Search sorted: ⌈log₂(n+1)⌉

### Pattern 5: Recurrence solving

**Strategy:** Try Master Theorem first. If it doesn't apply, use recursion tree. Special forms (T(√n), T(n-1)) have memorizable solutions.

---

## 14.3 Time Management Strategy

| Question Type | Recommended Time | Strategy |
|-------------|-----------------|----------|
| 1-mark MCQ | 1-2 minutes | Quick recall or elimination |
| 2-mark MCQ | 3-4 minutes | Work through systematically |
| 1-mark NAT | 2-3 minutes | Careful calculation |
| 2-mark NAT | 4-5 minutes | Double-check computation |
| MSQ | 3-5 minutes | Verify each option independently |

---

## 14.4 Common Mistakes to Avoid

1. **Confusing O and Θ:** O is upper bound, Θ is tight bound. Saying "Merge Sort is O(n³)" is technically true but useless.

2. **Wrong direction of reduction:** To prove X is NP-Complete, reduce FROM a known NPC problem TO X, not the other way.

3. **Forgetting base cases:** In recurrences, the base case T(1) matters for exact solutions.

4. **Dijkstra with negative edges:** Dijkstra FAILS with negative edges. Use Bellman-Ford instead.

5. **Assuming Quick Sort is always O(n log n):** Worst case is O(n²). Only randomized version has expected O(n log n) for all inputs.

6. **Confusing stable vs unstable:** Selection sort is NOT stable. Merge sort IS stable.

7. **MST ≠ Shortest Path Tree:** They are different! MST minimizes total weight, SPT minimizes individual path weights.

8. **Build heap is O(n), not O(n log n):** Bottom-up heap construction is linear.

9. **NP doesn't mean "hard":** NP means verifiable in polynomial time. P ⊆ NP. Everything in P is also in NP.

10. **Amortized ≠ Average case:** Amortized is worst-case guarantee for a sequence. Average case uses probability.

---

## 14.5 Quick Reference — Algorithm Complexities

### Sorting
| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Insertion | n | n² | n² | 1 | ✅ |
| Merge | n log n | n log n | n log n | n | ✅ |
| Quick | n log n | n log n | n² | log n | ❌ |
| Heap | n log n | n log n | n log n | 1 | ❌ |
| Counting | n+k | n+k | n+k | n+k | ✅ |
| Radix | d(n+b) | d(n+b) | d(n+b) | n+b | ✅ |

### Graph Algorithms
| Algorithm | Time | Space | Purpose |
|-----------|------|-------|---------|
| BFS | O(V+E) | O(V) | SSSP (unweighted), levels |
| DFS | O(V+E) | O(V) | Cycles, SCC, topo sort |
| Dijkstra | O((V+E)logV) | O(V) | SSSP (non-neg weights) |
| Bellman-Ford | O(VE) | O(V) | SSSP (neg weights) |
| Floyd-Warshall | O(V³) | O(V²) | APSP |
| Kruskal | O(E log E) | O(V) | MST |
| Prim | O((V+E)logV) | O(V) | MST |
| Topological Sort | O(V+E) | O(V) | DAG ordering |
| Kosaraju/Tarjan | O(V+E) | O(V) | SCC |

### Dynamic Programming
| Problem | Time | Space |
|---------|------|-------|
| LCS | O(mn) | O(mn) |
| LIS | O(n²) or O(n log n) | O(n) |
| MCM | O(n³) | O(n²) |
| 0/1 Knapsack | O(nW) | O(nW) |
| Edit Distance | O(mn) | O(mn) |
| Floyd-Warshall | O(V³) | O(V²) |
| Coin Change | O(nV) | O(V) |

### Searching
| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Linear | O(1) | O(n) | O(n) |
| Binary | O(1) | O(log n) | O(log n) |
| Interpolation | O(1) | O(log log n) | O(n) |
| Jump | O(1) | O(√n) | O(√n) |

---

## 14.6 ESE & PSU Specific Tips

ESE (Engineering Services Exam) and PSU exams tend to:
1. **Focus more on basics** — definitions, properties, simple applications
2. **Ask about real-world applications** of algorithms
3. **Include more numerical problems** — trace through algorithms, compute exact values
4. **Test knowledge of tradeoffs** — when to use which algorithm and why

**Extra topics for ESE/PSU:**
- Algorithm design strategies (comparison of paradigms)
- Real-world applications (database query optimization, network routing)
- Parallel algorithms basics
- Cache-friendly algorithms

---

## 14.7 Banking Exam Tips (IT Officer / Specialist Officer)

Banking technical exams for IT roles may include:
1. Basic complexity analysis (identify O(n), O(n²), O(log n))
2. Sorting algorithm properties (stable, in-place)
3. Basic graph traversals (BFS, DFS)
4. Simple DP problems (Fibonacci, basic Knapsack)
5. Hashing concepts (collision resolution)

**Focus on:** Breadth over depth. Know what each algorithm does and its complexity, less focus on proofs.

---

## 14.8 Final Checklist Before the Exam

- [ ] Can you solve any recurrence using Master Theorem in under 30 seconds?
- [ ] Can you trace BFS, DFS, Dijkstra, Prim, Kruskal on a graph?
- [ ] Do you know all sorting algorithms' complexities, stability, and space usage by heart?
- [ ] Can you write the recurrence for LCS, MCM, Knapsack, Edit Distance?
- [ ] Do you know which problems are in P, which are NP-Complete?
- [ ] Can you build a KMP failure function from a pattern?
- [ ] Do you know when Dijkstra fails and what to use instead?
- [ ] Can you explain why Build Heap is O(n), not O(n log n)?
- [ ] Do you know the lower bounds for comparisons (max, sort, merge)?
- [ ] Can you differentiate amortized O(1) from average O(1)?

If you can answer YES to all of these, you're ready to ace the algorithms section! 🎯

---

## References

1. **Introduction to Algorithms** — Cormen, Leiserson, Rivest, Stein (CLRS), 4th Edition
2. **Algorithm Design Manual** — Steven Skiena, 3rd Edition
3. **Algorithms** — Dasgupta, Papadimitriou, Vazirani
4. **GATE Previous Year Papers** (2000-2025) — GateOverflow
5. **Computer Science: A Modern Approach** — Standard ESE references
6. **Discrete Mathematics and Its Applications** — Kenneth Rosen

---

> **Final Note:** This material covers the complete GATE/ESE/PSU/BANK syllabus for Algorithms. Master each chapter sequentially, practice PYQs after each topic, and revisit the quick reference tables before the exam. The key to Rank-1 is not just knowing algorithms — it's understanding WHY they work and recognizing WHICH one to apply. Good luck! 🏆

