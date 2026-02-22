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
