# Chapter 9: Hashing

## 🎯 The Atomic Truth
> **"Hashing = Key → Index = O(1) Average Access"**

---

## 9.1 The Mental Model

### The Analogy 💡
Think of a **library card catalog**:
- Instead of searching every book, you look up by author name
- Author name maps to a specific drawer
- Direct access without scanning everything

### The Problem Hashing Solves

| Search Method | Time |
|---------------|------|
| Unsorted Array | O(n) |
| Sorted Array | O(log n) |
| BST | O(log n) |
| **Hash Table** | **O(1) average** |

### The Magic Formula
```
index = hash_function(key) % table_size
```

---

## 9.2 Hash Function

### Properties of Good Hash Function
1. **Deterministic**: Same key → same hash always
2. **Uniform Distribution**: Keys spread evenly across table
3. **Fast Computation**: O(1) time
4. **Minimize Collisions**: Different keys → different hashes (ideally)

### Common Hash Functions

#### Division Method
```python
def hash_div(key, m):
    return key % m

# Best when m is prime, not close to power of 2
```

#### Multiplication Method
```python
def hash_mult(key, m, A=0.6180339887):  # A = (√5 - 1) / 2
    return int(m * ((key * A) % 1))

# Works well for any m, A is usually golden ratio
```

#### Mid-Square Method
```python
def hash_midsquare(key, m):
    squared = key * key
    squared_str = str(squared)
    mid = len(squared_str) // 2
    return int(squared_str[mid-1:mid+1]) % m
```

#### Folding Method
```python
def hash_fold(key, m):
    key_str = str(key)
    chunk_size = len(str(m))
    total = 0
    for i in range(0, len(key_str), chunk_size):
        total += int(key_str[i:i+chunk_size])
    return total % m
```

#### String Hashing

```python
def hash_string(s, m):
    h = 0
    for char in s:
        h = (h * 31 + ord(char)) % m
    return h

# 31 is prime and allows efficient computation: 31 * x = (x << 5) - x
```

---

## 9.3 Collision Resolution

### What is a Collision?
Two different keys map to the same index.

```
hash("apple") = 5
hash("banana") = 5  ← Collision!
```

### Method 1: Chaining (Open Hashing)

Each bucket contains a linked list of entries.

```
Index  Chain
  0    → [20] → [30] → NULL
  1    → NULL
  2    → [42] → NULL
  3    → [33] → [73] → NULL
  4    → NULL
```

```python
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
```

**Complexity**:
| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Search | O(1 + α) | O(n) |
| Delete | O(1 + α) | O(n) |

Where α = n/m (load factor)

### Method 2: Open Addressing (Closed Hashing)

All elements stored in the hash table itself. On collision, probe for next empty slot.

#### Linear Probing

```python
def linear_probe(hash_val, i, m):
    return (hash_val + i) % m

# h(k, i) = (h'(k) + i) mod m
```

**Example**:
```
Insert 25, 35, 45 into table of size 10 (hash = key % 10)

25: index = 5 → insert at 5
35: index = 5 (collision) → try 6 → insert at 6
45: index = 5 (collision) → try 6 (collision) → try 7 → insert at 7

Table: [_, _, _, _, _, 25, 35, 45, _, _]
```

**Problem: Primary Clustering**
- Long runs of occupied slots form
- Subsequent insertions more likely to hit the cluster
- Performance degrades

#### Quadratic Probing

```python
def quadratic_probe(hash_val, i, m, c1=1, c2=1):
    return (hash_val + c1*i + c2*i*i) % m

# h(k, i) = (h'(k) + c₁i + c₂i²) mod m
```

**Problem: Secondary Clustering**
- Keys with same initial hash follow same probe sequence
- Better than linear, but not ideal

#### Double Hashing

```python
def double_hash(key, i, m):
    h1 = key % m
    h2 = 1 + (key % (m - 1))  # h2 must never be 0
    return (h1 + i * h2) % m

# h(k, i) = (h₁(k) + i × h₂(k)) mod m
```

**Best Choice**: Eliminates clustering

**Requirements for h₂**:
- h₂(k) ≠ 0 for any k
- h₂ must be relatively prime to m
- Common: h₂(k) = 1 + (k mod (m-1))

---

## 9.4 Open Addressing Implementation

```python
class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = object()  # Tombstone marker
    
    def _hash1(self, key):
        return key % self.size
    
    def _hash2(self, key):
        return 1 + (key % (self.size - 1))
    
    def _probe(self, key, i):
        return (self._hash1(key) + i * self._hash2(key)) % self.size
    
    def insert(self, key, value):
        for i in range(self.size):
            index = self._probe(key, i)
            if self.table[index] is None or self.table[index] is self.DELETED:
                self.table[index] = (key, value)
                return True
        return False  # Table full
    
    def search(self, key):
        for i in range(self.size):
            index = self._probe(key, i)
            if self.table[index] is None:
                return None  # Not found
            if self.table[index] is not self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
        return None
    
    def delete(self, key):
        for i in range(self.size):
            index = self._probe(key, i)
            if self.table[index] is None:
                return False
            if self.table[index] is not self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED  # Tombstone
                return True
        return False
```

---

## 9.5 Load Factor and Rehashing

### Load Factor (α)
```
α = n / m

n = number of elements
m = table size
```

### Recommended Load Factors

| Method | Recommended α |
|--------|---------------|
| Chaining | α ≤ 1 (can exceed) |
| Open Addressing | α ≤ 0.5 to 0.7 |

### Rehashing

When load factor exceeds threshold:
1. Create new table (usually 2× size)
2. Recompute hash for all elements
3. Insert into new table

```python
def rehash(self):
    old_table = self.table
    self.size *= 2
    self.table = [[] for _ in range(self.size)]
    
    for bucket in old_table:
        for key, value in bucket:
            self.insert(key, value)
```

---

## 9.6 Complexity Analysis

### Chaining

| Case | Assumption | Complexity |
|------|------------|------------|
| Average Successful | Uniform hashing | O(1 + α/2) |
| Average Unsuccessful | Uniform hashing | O(1 + α) |
| Worst | All keys in one bucket | O(n) |

### Open Addressing

| Case | Type | Expected Probes |
|------|------|-----------------|
| Unsuccessful | Linear | ½(1 + 1/(1-α)²) |
| Successful | Linear | ½(1 + 1/(1-α)) |
| Unsuccessful | Double | 1/(1-α) |
| Successful | Double | (1/α)ln(1/(1-α)) |

---

## 9.7 Comparison: Chaining vs Open Addressing

| Aspect | Chaining | Open Addressing |
|--------|----------|-----------------|
| Space | Extra for pointers | In-table only |
| Load factor | Can exceed 1 | Must be < 1 |
| Clustering | No | Yes (linear) |
| Delete | Simple | Needs tombstone |
| Cache | Poor (pointers) | Good (contiguous) |
| Implementation | Simpler | More complex |

---

## 9.8 Hashing Applications

### Application 1: Count Frequency

```python
def count_frequency(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

# Time: O(n), Space: O(k) where k = distinct elements
```

### Application 2: Two Sum Problem

```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# Time: O(n), Space: O(n)
```

### Application 3: First Unique Character

```python
def first_unique(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# Time: O(n), Space: O(1) - at most 26 letters
```

### Application 4: Group Anagrams

```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

# Time: O(n × k log k), Space: O(nk)
```

### Application 5: LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
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

### Application 6: Subarray Sum Equals K

```python
def subarray_sum(arr, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}
    
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count

# Time: O(n), Space: O(n)
```

---

## 9.9 Perfect Hashing

### Concept
Guarantee O(1) worst case when key set is static.

### FKS (Fredman-Komlós-Szemerédi) Scheme

**Two-level hashing**:
1. First level: Standard hash to m buckets
2. Second level: For bucket with nᵢ elements, use table of size nᵢ²

**Space**: O(n) expected
**Lookup**: O(1) worst case

### Cuckoo Hashing

**Idea**: Use two hash functions, two tables

**Lookup**: O(1) worst case - check only 2 positions

**Insert**: May "kick out" existing element to its alternate position

```python
def cuckoo_insert(key):
    for _ in range(max_iterations):
        pos1 = h1(key) % size1
        if table1[pos1] is None:
            table1[pos1] = key
            return True
        
        key, table1[pos1] = table1[pos1], key
        
        pos2 = h2(key) % size2
        if table2[pos2] is None:
            table2[pos2] = key
            return True
        
        key, table2[pos2] = table2[pos2], key
    
    return False  # Need to rehash
```

---

## 9.10 GATE Exam Patterns

### Pattern 1: Probe Sequence

**Q**: In a hash table of size 10 using linear probing, insert keys 25, 35, 45, 55 (hash = key % 10). Find final positions.

```
25 → 5, insert at 5
35 → 5 (collision), 6, insert at 6
45 → 5 (collision), 6 (collision), 7, insert at 7
55 → 5 (collision), 6 (collision), 7 (collision), 8, insert at 8

Positions: 25→5, 35→6, 45→7, 55→8
```

### Pattern 2: Search Comparisons

**Q**: How many comparisons to search for 45 in above table?

**Answer**: 3 (check 5, 6, 7 → found at 7)

### Pattern 3: Unsuccessful Search

**Q**: How many comparisons to search for 65?

```
65 → 5 (25, not match)
   → 6 (35, not match)
   → 7 (45, not match)
   → 8 (55, not match)
   → 9 (empty, stop)

Answer: 5 comparisons
```

### Pattern 4: Load Factor Calculation

**Q**: Hash table has 100 slots, 70 elements. What is load factor?

**Answer**: α = 70/100 = 0.7

### Pattern 5: Double Hashing Probe

**Q**: h₁(k) = k mod 7, h₂(k) = 1 + (k mod 5). Find probe sequence for k = 14.

```
h₁(14) = 14 mod 7 = 0
h₂(14) = 1 + (14 mod 5) = 1 + 4 = 5

Probe sequence:
i=0: (0 + 0×5) mod 7 = 0
i=1: (0 + 1×5) mod 7 = 5
i=2: (0 + 2×5) mod 7 = 3
i=3: (0 + 3×5) mod 7 = 1
i=4: (0 + 4×5) mod 7 = 6
i=5: (0 + 5×5) mod 7 = 4
i=6: (0 + 6×5) mod 7 = 2
```

---

## 9.11 Edge Cases & Traps

### Common Traps ⚠️

**Trap 1**: Forgetting tombstones in open addressing
- Don't stop search at tombstone
- May insert at tombstone

**Trap 2**: Hash table size matters
- Prime sizes reduce clustering
- Powers of 2 can cause issues with certain hash functions

**Trap 3**: String hashing overflow
- Use modular arithmetic throughout

**Trap 4**: Deleting in linear probing
- Can't simply delete - breaks probe chain
- Must use tombstone or rehash

---

## 📝 GATE Practice Problems

**Q1**: A hash table of size 11 uses h(k) = k mod 11. Insert 31, 22, 42, 33, 53, 43 using linear probing. Show final table.

**Q2**: What is the average number of probes for successful search in a hash table with load factor 0.5 using linear probing?

**Q3**: A hash table uses chaining. Average chain length is 5. What is the expected time for unsuccessful search?

**Q4**: Double hashing uses h₁(k) = k mod 10 and h₂(k) = k mod 9 + 1. Why must h₂ never be 0?

**Q5**: Compare expected number of probes for open addressing when α = 0.5 vs α = 0.9.

---

## 🎯 Quick Reference

### Hash Function Selection

| Method | When to Use |
|--------|-------------|
| Division | General purpose, m should be prime |
| Multiplication | m can be any value |
| Universal | Need guaranteed performance |
| Cryptographic | Security applications |

### Collision Resolution Selection

| Method | When to Use |
|--------|-------------|
| Chaining | Simple, can exceed α = 1 |
| Linear Probing | Good cache, simple |
| Quadratic | Avoid primary clustering |
| Double Hashing | Best probe distribution |
| Cuckoo | O(1) worst case lookup needed |

---

## 🔑 Key Takeaways

1. **O(1) average** for insert, search, delete - the main advantage
2. **Load factor** determines performance - keep low
3. **Chaining**: Simple, allows α > 1
4. **Open Addressing**: Better cache, but clustering issues
5. **Double hashing**: Best open addressing technique
6. **Rehash when α exceeds threshold** to maintain O(1)

---

*Next: [Graphs →](10-Graphs.md)*
