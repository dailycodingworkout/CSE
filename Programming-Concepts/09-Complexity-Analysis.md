# Chapter 9: Complexity Analysis
## The Efficiency Measure | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Complexity tells us how algorithms scale; Big-O is the universal language."**

---

## 9.1 Why Complexity Analysis?

### The Motivation

| Array Size | O(n) | O(n²) | O(2ⁿ) |
|------------|------|-------|-------|
| 10 | 10 ops | 100 ops | 1024 ops |
| 100 | 100 ops | 10,000 ops | 10³⁰ ops |
| 1000 | 1000 ops | 1,000,000 ops | ∞ |

**Key Insight:** A better algorithm beats a faster computer.

### Types of Analysis

| Type | Description | When Used |
|------|-------------|-----------|
| **Best Case** | Minimum operations | Rarely useful |
| **Average Case** | Expected operations | Realistic estimate |
| **Worst Case** | Maximum operations | Guarantees upper bound |
| **Amortized** | Average over sequence | Data structures |

---

## 9.2 Asymptotic Notations

### Big-O (O): Upper Bound

$$f(n) = O(g(n)) \Leftrightarrow \exists \, c > 0, n_0 : f(n) \leq c \cdot g(n) \; \forall n \geq n_0$$

**Meaning:** f(n) grows **at most as fast as** g(n)

### Big-Omega (Ω): Lower Bound

$$f(n) = \Omega(g(n)) \Leftrightarrow \exists \, c > 0, n_0 : f(n) \geq c \cdot g(n) \; \forall n \geq n_0$$

**Meaning:** f(n) grows **at least as fast as** g(n)

### Big-Theta (Θ): Tight Bound

$$f(n) = \Theta(g(n)) \Leftrightarrow f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))$$

**Meaning:** f(n) grows **exactly as fast as** g(n)

### Little-o and Little-ω

$$f(n) = o(g(n)) \Leftrightarrow \lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$$

$$f(n) = \omega(g(n)) \Leftrightarrow \lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$$

### 🎯 Quick Comparison

| Notation | Meaning | Analogy |
|----------|---------|---------|
| O(g(n)) | ≤ | Upper bound (worst case) |
| Ω(g(n)) | ≥ | Lower bound (best case) |
| Θ(g(n)) | = | Exact bound |
| o(g(n)) | < | Strictly less than |
| ω(g(n)) | > | Strictly greater than |

---

## 9.3 Common Complexity Classes

### The Hierarchy (Fastest to Slowest)

$$O(1) < O(\log n) < O(\sqrt{n}) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

### Visual Guide

```
       ↑
       │    n!
       │   /
       │  / 2^n
       │ /
Time   │/   n³
       │   /
       │  / n²
       │ /
       │/ n log n
       │  n
       │ √n
       │ log n
       │___1_________→ n
```

### Examples of Each Class

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(√n) | Square root | Prime check |
| O(n) | Linear | Linear search, single loop |
| O(n log n) | Linearithmic | Merge sort, quick sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(n³) | Cubic | Matrix multiplication (naive) |
| O(2ⁿ) | Exponential | Recursive Fibonacci, power set |
| O(n!) | Factorial | Permutations, TSP brute force |

---

## 9.4 Analyzing Code Complexity

### Rule 1: Loops

```c
for (int i = 0; i < n; i++) {    // O(n)
    // O(1) work
}
```

### Rule 2: Nested Loops

```c
for (int i = 0; i < n; i++) {        // O(n)
    for (int j = 0; j < n; j++) {    // O(n)
        // O(1) work
    }
}
// Total: O(n × n) = O(n²)
```

### Rule 3: Sequential Statements

```c
for (int i = 0; i < n; i++) { }  // O(n)
for (int j = 0; j < m; j++) { }  // O(m)
// Total: O(n + m) = O(max(n, m))
```

### Rule 4: Logarithmic Loops

```c
for (int i = 1; i < n; i *= 2) { }  // O(log n)
for (int i = n; i > 0; i /= 2) { }  // O(log n)
```

### Rule 5: Dependent Loops

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        // O(1) work
    }
}
// Sum: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n²)
```

### Rule 6: Log in Loop

```c
for (int i = 0; i < n; i++) {       // O(n)
    for (int j = 1; j < n; j *= 2) { // O(log n)
        // O(1) work
    }
}
// Total: O(n log n)
```

---

## 9.5 Analyzing Recursive Algorithms

### Recurrence Relations

**General Form:** $T(n) = aT(n/b) + f(n)$

Where:
- $a$ = number of subproblems
- $n/b$ = size of each subproblem
- $f(n)$ = work done outside recursion

### Substitution Method

**Example:** Solve $T(n) = 2T(n/2) + n$

1. Guess: $T(n) = O(n \log n)$
2. Assume: $T(k) \leq c \cdot k \log k$ for $k < n$
3. Prove: $T(n) \leq c \cdot n \log n$

$$T(n) = 2T(n/2) + n \leq 2c(n/2)\log(n/2) + n$$
$$= cn(\log n - 1) + n = cn\log n - cn + n$$
$$\leq cn\log n \text{ (for } c \geq 1)$$

### Recursion Tree Method

**Example:** $T(n) = 2T(n/2) + n$

```
                n                    Level 0: n
              /   \
           n/2     n/2               Level 1: n
          /  \    /  \
        n/4  n/4 n/4  n/4            Level 2: n
        ...
```

Total levels: $\log n$
Work per level: $n$
Total: $n \times \log n = O(n \log n)$

### Master Theorem

For $T(n) = aT(n/b) + f(n)$, let $c = \log_b a$

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $f(n) = O(n^{c-\epsilon})$ for some $\epsilon > 0$ | $T(n) = \Theta(n^c)$ |
| 2 | $f(n) = \Theta(n^c \log^k n)$ | $T(n) = \Theta(n^c \log^{k+1} n)$ |
| 3 | $f(n) = \Omega(n^{c+\epsilon})$ and regularity | $T(n) = \Theta(f(n))$ |

### 🎯 Master Theorem Examples

| Recurrence | a | b | c = log_b(a) | f(n) | Case | Result |
|------------|---|---|--------------|------|------|--------|
| $T(n) = 2T(n/2) + n$ | 2 | 2 | 1 | n | 2 | $\Theta(n \log n)$ |
| $T(n) = 2T(n/2) + 1$ | 2 | 2 | 1 | 1 | 1 | $\Theta(n)$ |
| $T(n) = 2T(n/2) + n^2$ | 2 | 2 | 1 | n² | 3 | $\Theta(n^2)$ |
| $T(n) = T(n/2) + 1$ | 1 | 2 | 0 | 1 | 2 | $\Theta(\log n)$ |
| $T(n) = 4T(n/2) + n$ | 4 | 2 | 2 | n | 1 | $\Theta(n^2)$ |
| $T(n) = T(n/2) + n$ | 1 | 2 | 0 | n | 3 | $\Theta(n)$ |

### Extended Master Theorem (Akra-Bazzi)

For $T(n) = \sum_{i=1}^{k} a_i T(n/b_i) + f(n)$

Find $p$ such that $\sum_{i=1}^{k} a_i / b_i^p = 1$

$$T(n) = \Theta\left(n^p \left(1 + \int_1^n \frac{f(u)}{u^{p+1}} du\right)\right)$$

---

## 9.6 Space Complexity

### Types of Space

1. **Fixed Part:** Code, constants, simple variables
2. **Variable Part:** Dynamic allocation, recursion stack

### Space for Recursive Functions

```c
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
// Space: O(n) - n stack frames
```

### Tail Recursion Optimization

```c
int factorial_tail(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_tail(n - 1, n * acc);
}
// Can be optimized to O(1) space by compiler
```

### Space Complexity Examples

| Algorithm | Time | Space |
|-----------|------|-------|
| Bubble Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(log n) |
| BFS | O(V + E) | O(V) |
| DFS (recursive) | O(V + E) | O(V) |
| Dynamic Programming | Varies | O(state space) |

### In-Place Algorithms

Use O(1) extra space (not counting input).

Examples:
- Bubble Sort, Selection Sort, Insertion Sort
- Quick Sort (ignoring recursion stack)
- Heap Sort

---

## 9.7 Amortized Analysis

### When to Use
When a sequence of operations has occasional expensive operations but average is cheap.

### Techniques

1. **Aggregate Analysis:** Total cost / number of operations
2. **Accounting Method:** Assign "credits" to cheap operations
3. **Potential Method:** Use potential function

### Example: Dynamic Array

```c
// Push to dynamic array
// Usually O(1), occasionally O(n) when resize
void push(DynamicArray* arr, int val) {
    if (arr->size == arr->capacity) {
        resize(arr, 2 * arr->capacity);  // O(n)
    }
    arr->data[arr->size++] = val;  // O(1)
}
```

**Amortized Analysis:**
- n pushes total
- Resize at 1, 2, 4, 8, ..., n
- Total copy work: 1 + 2 + 4 + ... + n ≈ 2n
- Amortized per push: O(2n/n) = O(1)

---

## 9.8 Complexity of Common Operations

### Data Structures

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | - | O(1)** | O(1)** | O(1)** |
| BST | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | - | O(n) | O(log n) | O(log n) |

*At known position, **Average case

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

### Graph Algorithms

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS/DFS | O(V + E) | O(V) |
| Dijkstra (heap) | O((V + E) log V) | O(V) |
| Bellman-Ford | O(VE) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Prim (matrix) | O(V²) | O(V) |
| Kruskal | O(E log E) | O(V) |
| Topological Sort | O(V + E) | O(V) |

---

## 9.9 Problem-Solving Patterns

### Identify Complexity from Constraints

| n ≤ | Acceptable Complexity | Common Pattern |
|-----|----------------------|----------------|
| 10 | O(n!), O(2ⁿ) | Brute force, backtracking |
| 20 | O(2ⁿ) | Bitmask DP |
| 100 | O(n³) | DP, matrix operations |
| 1000 | O(n²) | Nested loops |
| 10⁵ | O(n log n) | Sorting, trees |
| 10⁶ | O(n) | Linear scan |
| 10⁸ | O(log n), O(1) | Binary search, math |

### 🎯 Quick Estimation

- **1 second ≈ 10⁸ operations** (rough rule)
- If n = 10⁵, O(n²) = 10¹⁰ → Too slow!
- If n = 10⁵, O(n log n) ≈ 1.7 × 10⁶ → Fast!

---

## 🎯 Practice Problems

### Problem 1: Loop Analysis
```c
for (int i = 1; i < n; i *= 2)
    for (int j = 0; j < i; j++)
        // O(1)
```
**Answer:** $1 + 2 + 4 + ... + n/2 = O(n)$

### Problem 2: Recurrence
**Q:** Solve $T(n) = T(n-1) + n$
**Solution:** $T(n) = n + (n-1) + ... + 1 = n(n+1)/2 = O(n²)$

### Problem 3: Master Theorem
**Q:** $T(n) = 3T(n/2) + n²$
**Answer:** $a=3, b=2, c=\log_2 3 ≈ 1.58$. Since $n² = \Omega(n^{1.58+\epsilon})$, Case 3 → $T(n) = \Theta(n²)$

### Problem 4: Space Complexity
```c
int fib(int n) {
    int dp[n+1];
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; i++)
        dp[i] = dp[i-1] + dp[i-2];
    return dp[n];
}
```
**Answer:** Time O(n), Space O(n)

### Problem 5: Amortized
**Q:** In a dynamic array starting with size 1, what's the amortized cost of n insertions?
**Answer:** O(1) per insertion (despite occasional O(n) resize)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Oh Log, it's Not Squared! Log's Nice, so Squared Cubes Explode Factorially!"**
- **O**(1) - **L**og n - n - **N**log n - n**S**quared - n**C**ubed - **E**xponential - **F**actorial

### The Mental Slider
Imagine a growth dial:
- O(1): Flat line
- O(log n): Slow rise, flattening
- O(n): Straight diagonal
- O(n²): Parabola shooting up
- O(2ⁿ): Rocket launch!

### The 5-Second Snap-Check
1. **Nested loops?** Multiply complexities
2. **Halving each step?** O(log n)
3. **Single loop over n?** O(n)
4. **Sort then scan?** O(n log n)
5. **All pairs/subsets?** O(n²) or O(2ⁿ)

---

## 📈 Cheat Sheet

### Big-O Simplification Rules

1. $O(c \cdot f(n)) = O(f(n))$ (drop constants)
2. $O(f(n) + g(n)) = O(\max(f(n), g(n)))$ (drop lower order)
3. $O(f(n) \cdot g(n)) = O(f(n)) \cdot O(g(n))$ (multiply)
4. $O(\log_a n) = O(\log_b n)$ (log base doesn't matter)

### Common Recurrences

| Recurrence | Solution |
|------------|----------|
| $T(n) = T(n-1) + 1$ | O(n) |
| $T(n) = T(n-1) + n$ | O(n²) |
| $T(n) = T(n/2) + 1$ | O(log n) |
| $T(n) = T(n/2) + n$ | O(n) |
| $T(n) = 2T(n/2) + 1$ | O(n) |
| $T(n) = 2T(n/2) + n$ | O(n log n) |
| $T(n) = 2T(n-1) + 1$ | O(2ⁿ) |
| $T(n) = T(n-1) + T(n-2)$ | O(φⁿ) ≈ O(1.618ⁿ) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: OOP](08-OOP.md) | [Next: Practice Problems →](10-Practice-Problems.md)
