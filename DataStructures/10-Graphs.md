# Chapter 10: Graphs

## 🎯 The Atomic Truth
> **"Graph = Vertices + Edges = Relationships"**

---

## 10.1 The Mental Model

### The Analogy 💡
Think of a **social network**:
- Each person is a **vertex (node)**
- Friendships are **edges (connections)**
- Some friendships are mutual (undirected)
- Some are one-way follows (directed)

### Real-World Examples
- Road networks (cities, roads)
- Web pages (pages, hyperlinks)
- Social networks (users, connections)
- Computer networks (devices, cables)
- Dependencies (tasks, prerequisites)

---

## 10.2 Graph Terminology

```
     A -------- B
    /|          |\
   / |          | \
  C  |          |  D
   \ |          | /
    \|          |/
     E -------- F

Vertices (V): {A, B, C, D, E, F}
Edges (E): {(A,B), (A,C), (A,E), (B,D), (B,F), (C,E), (D,F), (E,F)}
```

| Term | Definition |
|------|------------|
| **Vertex/Node** | Entity in the graph |
| **Edge** | Connection between vertices |
| **Directed Graph** | Edges have direction (A→B ≠ B→A) |
| **Undirected Graph** | Edges are bidirectional |
| **Weighted Graph** | Edges have weights/costs |
| **Degree** | Number of edges incident to vertex |
| **In-degree** | Edges coming into vertex (directed) |
| **Out-degree** | Edges going out of vertex (directed) |
| **Path** | Sequence of vertices connected by edges |
| **Cycle** | Path that starts and ends at same vertex |
| **Connected** | Path exists between every pair |
| **Strongly Connected** | Directed path both ways between every pair |
| **DAG** | Directed Acyclic Graph |

### Degree Formulas

**Undirected Graph**:
$$\sum_{v \in V} degree(v) = 2|E|$$

**Directed Graph**:
$$\sum_{v \in V} in\text{-}degree(v) = \sum_{v \in V} out\text{-}degree(v) = |E|$$

---

## 10.3 Graph Representations

### 1. Adjacency Matrix

```
Graph:              Matrix:
  A---B               A  B  C
  |\ /|             A [0, 1, 1]
  | X |             B [1, 0, 1]
  |/ \|             C [1, 1, 0]
  C---
```

```python
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # For undirected
```

| Operation | Time |
|-----------|------|
| Check edge | O(1) |
| All neighbors | O(V) |
| Add edge | O(1) |
| Space | O(V²) |

**Use when**: Dense graph (E ≈ V²)

### 2. Adjacency List

```
Graph:              List:
  A---B             A: [B, C]
  |\ /|             B: [A, C]
  | X |             C: [A, B]
  |/ \|
  C---
```

```python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected
```

| Operation | Time |
|-----------|------|
| Check edge | O(degree) |
| All neighbors | O(degree) |
| Add edge | O(1) |
| Space | O(V + E) |

**Use when**: Sparse graph (E << V²)

### Comparison

| Aspect | Matrix | List |
|--------|--------|------|
| Space | O(V²) | O(V + E) |
| Edge lookup | O(1) | O(deg) |
| Neighbor iteration | O(V) | O(deg) |
| Dense graphs | ✓ Better | |
| Sparse graphs | | ✓ Better |

---

## 10.4 Graph Traversals

### BFS (Breadth-First Search)

**Explore level by level** using a queue.

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Time: O(V + E), Space: O(V)
```

**Properties**:
- Finds shortest path in unweighted graphs
- Level-order exploration
- Uses queue (FIFO)

### DFS (Depth-First Search)

**Explore as deep as possible** before backtracking.

```python
# Recursive
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    result = [vertex]
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

# Iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

# Time: O(V + E), Space: O(V)
```

**Properties**:
- Uses stack (or recursion)
- Used for cycle detection, topological sort
- Can detect back edges

### BFS vs DFS

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Order | Level by level | Depth first |
| Shortest Path | Yes (unweighted) | No |
| Memory | O(width) | O(height) |
| Complete | Yes | Yes (finite graphs) |

---

## 10.5 Shortest Path Algorithms

### 1. BFS (Unweighted Graphs)

```python
def shortest_path_bfs(graph, start, end):
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == end:
            return path
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path exists
```

### 2. Dijkstra's Algorithm (Non-negative Weights)

```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    parent = {start: None}
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, parent

# Time: O((V + E) log V), Space: O(V)
```

### 3. Bellman-Ford Algorithm (Handles Negative Weights)

```python
def bellman_ford(vertices, edges, start):
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    
    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycle
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle exists
    
    return distances

# Time: O(VE), Space: O(V)
```

### 4. Floyd-Warshall (All Pairs Shortest Path)

```python
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    
    # Initialize
    for i in range(V):
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    
    # Dynamic programming
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Time: O(V³), Space: O(V²)
```

### Comparison

| Algorithm | Time | Space | Negative Weights | All Pairs |
|-----------|------|-------|------------------|-----------|
| BFS | O(V+E) | O(V) | No (unweighted) | No |
| Dijkstra | O((V+E)logV) | O(V) | No | No |
| Bellman-Ford | O(VE) | O(V) | Yes | No |
| Floyd-Warshall | O(V³) | O(V²) | Yes | Yes |

---

## 10.6 Minimum Spanning Tree (MST)

### Definition
A spanning tree that connects all vertices with minimum total edge weight.

### Prim's Algorithm

**Greedy**: Always pick minimum weight edge from tree to non-tree vertex.

```python
import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, weight))
        
        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (w, v, neighbor))
    
    return mst

# Time: O(E log V), Space: O(V + E)
```

### Kruskal's Algorithm

**Greedy**: Sort edges, add smallest that doesn't create cycle.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(vertices)
    mst = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == vertices - 1:
                break
    
    return mst

# Time: O(E log E), Space: O(V)
```

### Prim vs Kruskal

| Aspect | Prim | Kruskal |
|--------|------|---------|
| Approach | Vertex-based | Edge-based |
| Data Structure | Priority Queue | Union-Find |
| Time (adj list) | O(E log V) | O(E log E) |
| Dense graphs | Better | |
| Sparse graphs | | Better |

---

## 10.7 Topological Sort

### Definition
Linear ordering of vertices in DAG such that for every edge u→v, u comes before v.

### Kahn's Algorithm (BFS-based)

```python
from collections import deque

def topological_sort_kahn(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
    
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(result) != len(graph):
        return None  # Cycle exists
    
    return result

# Time: O(V + E)
```

### DFS-based Topological Sort

```python
def topological_sort_dfs(graph):
    visited = set()
    stack = []
    
    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)
    
    for u in graph:
        if u not in visited:
            dfs(u)
    
    return stack[::-1]
```

---

## 10.8 Cycle Detection

### Undirected Graph (DFS)

```python
def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(u, parent):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False
    
    for u in graph:
        if u not in visited:
            if dfs(u, None):
                return True
    
    return False
```

### Directed Graph (DFS with colors)

```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    
    def dfs(u):
        color[u] = GRAY
        for v in graph[u]:
            if color[v] == GRAY:  # Back edge
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False
    
    for u in graph:
        if color[u] == WHITE:
            if dfs(u):
                return True
    return False
```

---

## 10.9 Special Graph Algorithms

### Bipartite Check (2-coloring)

```python
def is_bipartite(graph):
    color = {}
    
    for start in graph:
        if start in color:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    
    return True
```

### Strongly Connected Components (Kosaraju)

```python
def kosaraju(graph):
    # Step 1: Fill vertices in stack according to finish times
    visited = set()
    stack = []
    
    def dfs1(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v)
        stack.append(u)
    
    for u in graph:
        if u not in visited:
            dfs1(u)
    
    # Step 2: Create reversed graph
    reversed_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].append(u)
    
    # Step 3: Process vertices in order of decreasing finish time
    visited.clear()
    sccs = []
    
    def dfs2(u, component):
        visited.add(u)
        component.append(u)
        for v in reversed_graph[u]:
            if v not in visited:
                dfs2(v, component)
    
    while stack:
        u = stack.pop()
        if u not in visited:
            component = []
            dfs2(u, component)
            sccs.append(component)
    
    return sccs

# Time: O(V + E)
```

---

## 10.10 GATE Exam Patterns

### Pattern 1: Traversal Order

**Q**: Give BFS and DFS order starting from vertex A.

**Method**: Trace through algorithm, breaking ties alphabetically.

### Pattern 2: Number of Edges

**Q**: A connected graph has n vertices. Minimum and maximum edges?

**Answer**:
- Minimum: n - 1 (tree)
- Maximum: n(n-1)/2 (complete graph)

### Pattern 3: MST Weight

**Q**: Find total weight of MST.

**Method**: Apply Prim's or Kruskal's, sum selected edges.

### Pattern 4: Shortest Path

**Q**: Find shortest path from A to B in weighted graph.

**Method**: Apply Dijkstra's algorithm.

### Pattern 5: Topological Sort

**Q**: Is topological sort possible? If yes, give one ordering.

**Answer**: Possible only if DAG (no cycle).

---

## 📝 GATE Practice Problems

**Q1**: A graph has 10 vertices. If it's a tree, how many edges?

**Q2**: Apply Dijkstra from vertex S. Find shortest path to all vertices.

**Q3**: Is the graph bipartite? If yes, partition vertices.

**Q4**: Find all strongly connected components.

**Q5**: What is the time complexity of DFS on a graph represented as adjacency matrix vs adjacency list?

---

## 🎯 Quick Reference

### Algorithm Selection

| Problem | Algorithm | Time |
|---------|-----------|------|
| Shortest path (unweighted) | BFS | O(V+E) |
| Shortest path (non-neg) | Dijkstra | O(ElogV) |
| Shortest path (negative) | Bellman-Ford | O(VE) |
| All pairs shortest | Floyd-Warshall | O(V³) |
| MST | Prim/Kruskal | O(ElogV) |
| Topological Sort | Kahn/DFS | O(V+E) |
| Cycle Detection | DFS | O(V+E) |
| SCC | Kosaraju/Tarjan | O(V+E) |

---

## 🔑 Key Takeaways

1. **Choose representation based on density** - Matrix for dense, List for sparse
2. **BFS for shortest path** in unweighted graphs
3. **Dijkstra fails with negative edges** - use Bellman-Ford
4. **Topological sort only for DAGs**
5. **MST has exactly V-1 edges**
6. **Know Union-Find** for Kruskal's algorithm

---

*Next: [Sorting Algorithms →](11-Sorting.md)*
