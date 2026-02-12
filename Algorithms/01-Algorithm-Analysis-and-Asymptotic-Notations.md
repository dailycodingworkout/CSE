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


