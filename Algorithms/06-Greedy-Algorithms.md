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
