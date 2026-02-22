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
