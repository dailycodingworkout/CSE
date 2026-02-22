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
