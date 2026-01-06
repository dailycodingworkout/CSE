# Chapter 15: Previous Year Questions Analysis

## 🎯 GATE/ESE/PSU Data Structures - Topic-wise Analysis

---

## 15.1 Topic Weightage Trends

### GATE CSE (Last 10 Years)

| Topic | Avg. Marks | Questions/Year | Priority |
|-------|------------|----------------|----------|
| Trees (Binary, BST, AVL) | 8-12 | 4-6 | ⭐⭐⭐⭐⭐ |
| Graphs | 8-10 | 3-5 | ⭐⭐⭐⭐⭐ |
| Hashing | 4-6 | 2-3 | ⭐⭐⭐⭐ |
| Stacks & Queues | 4-6 | 2-3 | ⭐⭐⭐⭐ |
| Linked Lists | 2-4 | 1-2 | ⭐⭐⭐ |
| Arrays | 2-4 | 1-2 | ⭐⭐⭐ |
| Heaps | 4-6 | 2-3 | ⭐⭐⭐⭐ |
| Sorting & Searching | 4-6 | 2-3 | ⭐⭐⭐⭐ |

### ESE (Engineering Services)

| Topic | Importance | Focus Areas |
|-------|------------|-------------|
| Basic DS | High | Arrays, Stacks, Queues |
| Trees | Very High | Traversals, BST operations |
| Graphs | Very High | BFS, DFS, Shortest paths |
| Complexity | High | Time & Space analysis |

---

## 15.2 Most Repeated Concepts

### Trees (Most Important!)

1. **Traversal Questions**
   - Given two traversals, find third
   - Count nodes, leaves, internal nodes
   - Height/depth calculations

2. **BST Operations**
   - Search, Insert, Delete complexity
   - Inorder predecessor/successor
   - BST validation

3. **AVL Trees**
   - Rotations after insertion
   - Minimum/maximum nodes for height h
   - Balance factor calculations

4. **Binary Tree Properties**
   - Number of trees with n nodes (Catalan)
   - NULL pointers count (n+1)
   - Maximum/minimum height

### Graphs

1. **Traversal**
   - BFS/DFS order
   - Time complexity on matrix vs list

2. **Shortest Path**
   - Dijkstra's algorithm trace
   - Bellman-Ford for negative weights
   - Floyd-Warshall complexity

3. **MST**
   - Prim's vs Kruskal's
   - Number of edges in MST (V-1)
   - Edge selection order

4. **Special Topics**
   - Topological sort
   - Cycle detection
   - Bipartite check

### Hashing

1. **Collision Resolution**
   - Linear/Quadratic probing sequences
   - Double hashing calculations
   - Chaining analysis

2. **Complexity Questions**
   - Average case search
   - Load factor effects
   - Worst case scenarios

### Stacks & Queues

1. **Expression Conversion**
   - Infix to Postfix
   - Postfix evaluation
   - Prefix conversions

2. **Implementation**
   - Queue using stacks
   - Stack using queues
   - Circular queue conditions

3. **Applications**
   - Balanced parentheses
   - Stack permutations (Catalan)

---

## 15.3 Question Type Analysis

### Numerical Answer Type (NAT)

**Common NAT Questions:**
- "How many comparisons in worst case?"
- "What is the height of tree after insertions?"
- "How many swaps in bubble sort?"
- "What is the load factor?"

**Strategy:** Practice exact calculations, no guessing possible

### Multiple Choice Questions (MCQ)

**Common Patterns:**
- "Which of the following is FALSE?"
- "Which data structure is best for...?"
- "Time complexity of operation X?"

**Strategy:** Eliminate options systematically

### Multiple Select Questions (MSQ)

**Common Patterns:**
- "Which of the following are TRUE?"
- "Select all valid properties"

**Strategy:** Evaluate each option independently

---

## 15.4 Year-wise Important Questions

### GATE 2023

**Q1**: AVL tree insertion requiring LR rotation
**Q2**: Hash table probe sequence with double hashing
**Q3**: BFS traversal order from given graph

### GATE 2022

**Q1**: Postfix expression evaluation
**Q2**: Minimum height of BST with n nodes
**Q3**: Dijkstra's algorithm intermediate state

### GATE 2021

**Q1**: Stack permutation validity
**Q2**: Number of BSTs with n nodes
**Q3**: Time complexity of heap build operation

### GATE 2020

**Q1**: AVL tree after series of insertions
**Q2**: Hashing with linear probing
**Q3**: DFS traversal on graph

---

## 15.5 High-Yield Formula Sheet

### Trees

| Formula | Value |
|---------|-------|
| Max nodes at level i | 2ⁱ |
| Max nodes in BT of height h | 2^(h+1) - 1 |
| NULL pointers in BT of n nodes | n + 1 |
| Number of BSTs with n nodes | Cₙ = (2n)!/((n+1)!×n!) |
| Min height of BT with n nodes | ⌊log₂n⌋ |
| Leaves in full BT with n nodes | (n+1)/2 |
| Min nodes in AVL of height h | N(h) = N(h-1) + N(h-2) + 1 |

### Graphs

| Formula | Value |
|---------|-------|
| Edges in tree | V - 1 |
| Max edges in undirected | V(V-1)/2 |
| Max edges in directed | V(V-1) |
| Sum of degrees (undirected) | 2E |
| DFS/BFS complexity (list) | O(V + E) |
| DFS/BFS complexity (matrix) | O(V²) |
| Dijkstra complexity | O((V+E)log V) |
| Floyd-Warshall | O(V³) |

### Hashing

| Formula | Value |
|---------|-------|
| Load factor | α = n/m |
| Expected probes (linear, unsuccessful) | ½(1 + 1/(1-α)²) |
| Expected probes (linear, successful) | ½(1 + 1/(1-α)) |
| Chaining avg search | O(1 + α) |

### Sorting

| Algorithm | Best | Average | Worst | Stable |
|-----------|------|---------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | Yes |
| Insertion | O(n) | O(n²) | O(n²) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | No |
| Merge | O(n log n) | O(n log n) | O(n log n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | No |

---

## 15.6 Common Mistakes to Avoid

### Mistake 1: Height vs Depth Confusion
- **Height**: Measured from leaf (upward)
- **Depth**: Measured from root (downward)
- **Note**: Some books use different conventions - read question carefully!

### Mistake 2: Edge Cases in Complexity
- Empty input
- Single element
- Already sorted (for sorting)
- All elements same

### Mistake 3: Index Confusion
- 0-indexed vs 1-indexed arrays
- Heap parent/child formulas differ

### Mistake 4: Stability in Sorting
- Selection sort is NOT stable (standard)
- Quick sort is NOT stable
- Merge sort IS stable

### Mistake 5: Hash Table Worst Case
- Always O(n) in worst case
- O(1) is average case only

---

## 15.7 Quick Revision Checklist

### Before Exam, Verify You Can:

**Trees:**
- [ ] Draw tree from traversals
- [ ] Calculate height, depth, nodes
- [ ] Perform AVL rotations
- [ ] Find inorder predecessor/successor

**Graphs:**
- [ ] Write BFS/DFS from scratch
- [ ] Trace Dijkstra's algorithm
- [ ] Find MST using Prim's/Kruskal's
- [ ] Detect cycle in directed/undirected

**Hashing:**
- [ ] Calculate probe sequence
- [ ] Compute load factor impact
- [ ] Compare collision resolution methods

**Stacks/Queues:**
- [ ] Convert infix to postfix
- [ ] Evaluate postfix expression
- [ ] Implement circular queue conditions

**Sorting:**
- [ ] Know all complexities
- [ ] Trace through algorithms
- [ ] Identify stable sorts

---

## 15.8 Time Management Strategy

### 2-Mark Questions (1.5 min each)
- Quick conceptual questions
- Direct formula application
- Don't overthink

### 1-Mark Questions (1 min each)
- Usually straightforward
- May have negative marking
- Skip if unsure, return later

### NAT Questions (2 min each)
- No negative marking
- Always attempt
- Double-check calculations

---

## 15.9 Mock Test Approach

### Week Before Exam

| Day | Activity |
|-----|----------|
| Day 1-2 | Full mock tests |
| Day 3-4 | Weak topic revision |
| Day 5-6 | Formula review |
| Day 7 | Light revision, rest |

### During Mock Tests
1. First pass: Attempt all confident questions
2. Second pass: Attempt remaining
3. Third pass: Review answers

---

## 15.10 Final Tips

### The 80-20 Rule
80% of marks come from 20% of concepts:
1. Tree traversals and properties
2. Graph algorithms (BFS, DFS, Dijkstra)
3. Hashing collision resolution
4. Sorting complexity analysis
5. Stack applications

### Last Minute Reminders
1. **Read carefully** - "NOT" and "FALSE" questions
2. **Check units** - bits, bytes, words
3. **Verify formulas** - 0-indexed vs 1-indexed
4. **Don't panic** - unseen questions are often variations of known patterns

---

## 📚 Recommended Practice Resources

1. **GATE PYQs** - Last 15 years
2. **GO PDF** - GateOverflow compilation
3. **Made Easy Test Series**
4. **ACE Academy Materials**

---

## 🎯 Final Confidence Boosters

Remember:
- You've studied the material
- Most questions test the same concepts
- Stay calm and methodical
- Trust your preparation

> **"The expert in anything was once a beginner."**

---

**Good luck with your exam! 🍀**

---

*← Back to [README](README.md)*
