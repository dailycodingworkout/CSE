# Chapter 13: Advanced Data Structures

## 🎯 The Atomic Truth
> **"Advanced DS = Specialized Solutions for Specific Problems"**

---

## 13.1 Trie (Prefix Tree)

### The Mental Model 💡
Think of an **autocomplete system**:
- Each path from root represents a prefix
- Common prefixes share paths
- Efficient for prefix-based operations

### Structure

```
Words: ["cat", "car", "card", "care", "dog"]

           root
          /    \
         c      d
        /        \
       a          o
      / \          \
     t   r          g*
    *   / \
       d   e
      *    *

* = end of word
```

### Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| Prefix Search | O(m) | O(1) |
| Space (total) | - | O(ALPHABET × m × n) |

m = word length, n = number of words

### Applications
- Autocomplete
- Spell checkers
- IP routing (longest prefix match)
- Word games (Boggle, Scrabble)

---

## 13.2 Segment Tree

### The Mental Model 💡
Divide array into segments, store aggregate info for each segment.

### Use Cases
- Range sum queries
- Range min/max queries
- Range updates

### Structure

```
Array: [1, 3, 5, 7, 9, 11]

Segment Tree (Sum):
                [36]             (0-5)
               /    \
           [9]      [27]         (0-2) (3-5)
          /   \    /    \
        [4]  [5] [16]  [11]      (0-1) (2-2) (3-4) (5-5)
       /  \      /  \
      [1] [3]  [7] [9]           (0-0) (1-1) (3-3) (4-4)
```

### Implementation

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0  # Out of range
        if l <= start and end <= r:
            return self.tree[node]  # Completely inside
        
        mid = (start + end) // 2
        left_sum = self.query(2*node+1, start, mid, l, r)
        right_sum = self.query(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node+1, start, mid, idx, val)
            else:
                self.update(2*node+2, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
```

### Complexity

| Operation | Time |
|-----------|------|
| Build | O(n) |
| Query | O(log n) |
| Update | O(log n) |
| Space | O(n) |

---

## 13.3 Fenwick Tree (Binary Indexed Tree)

### The Mental Model 💡
Store cumulative frequencies using binary representation of indices.

### Advantage over Segment Tree
- Simpler implementation
- Less memory (n vs 4n)
- Same complexity

### Key Insight
```
Index i is responsible for range [i - lowbit(i) + 1, i]
lowbit(i) = i & (-i)  # Lowest set bit
```

### Implementation

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def prefix_sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total
    
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
```

### Complexity

| Operation | Time |
|-----------|------|
| Update | O(log n) |
| Prefix Sum | O(log n) |
| Range Sum | O(log n) |
| Space | O(n) |

---

## 13.4 Disjoint Set Union (Union-Find)

### The Mental Model 💡
Track connected components efficiently.

### Operations
- **Find**: Which set does element belong to?
- **Union**: Merge two sets

### Implementation with Path Compression & Union by Rank

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Complexity

| Operation | Time |
|-----------|------|
| Find | O(α(n)) ≈ O(1) |
| Union | O(α(n)) ≈ O(1) |
| Space | O(n) |

α(n) = inverse Ackermann function, practically constant

### Applications
- Kruskal's MST
- Cycle detection
- Connected components
- Percolation

---

## 13.5 Sparse Table

### Use Case
Range minimum/maximum queries on static array (no updates).

### Implementation

```python
import math

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        
        k = self.log[self.n] + 1
        self.table = [[0] * self.n for _ in range(k)]
        
        # Base case
        for i in range(self.n):
            self.table[0][i] = arr[i]
        
        # Build table
        for j in range(1, k):
            for i in range(self.n - (1 << j) + 1):
                self.table[j][i] = min(
                    self.table[j-1][i],
                    self.table[j-1][i + (1 << (j-1))]
                )
    
    def query(self, l, r):
        length = r - l + 1
        k = self.log[length]
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])
```

### Complexity

| Operation | Time |
|-----------|------|
| Build | O(n log n) |
| Query | O(1) |
| Space | O(n log n) |

---

## 13.6 LRU Cache

### Implementation using OrderedDict

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# All operations: O(1)
```

### Implementation using Doubly Linked List + Hash Map

```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
```

---

## 13.7 Bloom Filter

### Concept
Probabilistic data structure for set membership.

### Properties
- **False positives**: Possible (says "yes" when answer is "no")
- **False negatives**: Never (always correct when says "no")

### Implementation

```python
import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size
    
    def _hashes(self, item):
        result = []
        for i in range(self.hash_count):
            digest = hashlib.md5((str(i) + str(item)).encode()).hexdigest()
            result.append(int(digest, 16) % self.size)
        return result
    
    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = True
    
    def contains(self, item):
        return all(self.bit_array[idx] for idx in self._hashes(item))
```

### Use Cases
- Database query optimization
- Spell checkers
- Web crawlers (URL deduplication)

---

## 13.8 Skip List

### Concept
Probabilistic alternative to balanced trees.

### Structure

```
Level 3: HEAD ─────────────────────→ 50 ──────→ NULL
Level 2: HEAD ────→ 20 ─────────────→ 50 ──────→ NULL
Level 1: HEAD ────→ 20 ────→ 30 ────→ 50 ──────→ NULL
Level 0: HEAD → 10 → 20 → 25 → 30 → 40 → 50 → 60 → NULL
```

### Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Space | O(n) | O(n log n) |

---

## 13.9 Suffix Array & Suffix Tree

### Suffix Array
Sorted array of all suffixes' starting positions.

```
String: "banana"
Suffixes:
0: banana
1: anana
2: nana
3: ana
4: na
5: a

Sorted: a(5), ana(3), anana(1), banana(0), na(4), nana(2)
Suffix Array: [5, 3, 1, 0, 4, 2]
```

### Use Cases
- Pattern matching
- Finding longest repeated substring
- String compression

---

## 13.10 Comparison of Advanced DS

| Data Structure | Primary Use | Query | Update | Space |
|----------------|-------------|-------|--------|-------|
| Trie | Prefix operations | O(m) | O(m) | O(Σ×m×n) |
| Segment Tree | Range queries | O(log n) | O(log n) | O(n) |
| Fenwick Tree | Prefix sums | O(log n) | O(log n) | O(n) |
| Union-Find | Set operations | O(α(n)) | O(α(n)) | O(n) |
| Sparse Table | Static RMQ | O(1) | N/A | O(n log n) |
| Skip List | Ordered set | O(log n) | O(log n) | O(n) |
| Bloom Filter | Membership | O(k) | O(k) | O(m) |

---

## 📝 GATE Practice Problems

**Q1**: What is the space complexity of a Trie storing n words of average length m over alphabet Σ?

**Q2**: Compare Segment Tree vs Fenwick Tree for range sum queries.

**Q3**: In Union-Find with path compression and union by rank, what is the amortized time per operation?

**Q4**: Bloom filter has 10% false positive rate. What happens if we double the bit array size?

**Q5**: Which data structure would you use for finding longest common prefix among n strings?

---

## 🔑 Key Takeaways

1. **Trie** is essential for string prefix problems
2. **Segment Tree** handles range queries with updates
3. **Fenwick Tree** is simpler alternative for prefix sums
4. **Union-Find** is nearly O(1) for connected components
5. **Sparse Table** achieves O(1) query for static RMQ
6. **Choose based on specific requirements** - no one-size-fits-all

---

*Next: [Problem-Solving Patterns →](14-Problem-Patterns.md)*
