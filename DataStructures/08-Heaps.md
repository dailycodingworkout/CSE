# Chapter 8: Heaps & Priority Queues

## 🎯 The Atomic Truth
> **"Heap = Complete Binary Tree + Heap Property"**

---

## 8.1 The Mental Model

### The Analogy 💡
Think of a **tournament bracket**:
- Winner of each match moves up
- Champion (best) always at the top
- But losers are not fully sorted - just lost to someone better

### Why Heaps?
When you frequently need **the best** (max/min) element but don't need full sorting.

| Problem | Array | Sorted Array | Heap |
|---------|-------|--------------|------|
| Find Max | O(n) | O(1) | O(1) |
| Insert | O(1) | O(n) | O(log n) |
| Delete Max | O(n) | O(1) | O(log n) |

---

## 8.2 Heap Properties

### Max-Heap Property
Every parent ≥ its children

```
        90
       /  \
      80   70
     / \   /
    60 50 30

90 ≥ 80, 90 ≥ 70
80 ≥ 60, 80 ≥ 50
70 ≥ 30
```

### Min-Heap Property
Every parent ≤ its children

```
        10
       /  \
      20   30
     / \   /
    40 50 60

10 ≤ 20, 10 ≤ 30
20 ≤ 40, 20 ≤ 50
30 ≤ 60
```

### Complete Binary Tree Property
- All levels filled except possibly the last
- Last level filled left to right

---

## 8.3 Heap Representation

### Array Representation (Standard)

```
Heap Tree:       Array (1-indexed):
       90         [_, 90, 80, 70, 60, 50, 30]
      /  \            0   1   2   3   4   5   6
     80   70
    / \   /
   60 50 30

For node at index i:
- Parent: i / 2
- Left child: 2 * i
- Right child: 2 * i + 1
```

**0-indexed version**:
- Parent: (i - 1) / 2
- Left child: 2 * i + 1
- Right child: 2 * i + 2

---

## 8.4 Heap Operations

### Heapify (Fix Heap Property) - O(log n)

**Max-Heapify**: Assume subtrees are heaps, fix root violation

```python
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Time: O(log n), Space: O(log n) for recursion
```

**Visual Example**:
```
Before:          After max_heapify on index 0:
       10               90
      /  \             /  \
     90   30          10   30
    /               /
   40              40

Swap 10 and 90, then heapify subtree
```

### Insert - O(log n)

**Algorithm**:
1. Add element at end (maintain completeness)
2. "Bubble up" - swap with parent while larger (max-heap)

```python
def insert(heap, key):
    heap.append(key)
    i = len(heap) - 1
    
    # Bubble up
    while i > 0 and heap[parent(i)] < heap[i]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def parent(i):
    return (i - 1) // 2
```

**Visual**:
```
Insert 100:

Step 1: Add at end      Step 2: Bubble up
       90                      90              100
      /  \                    /  \            /   \
     80   70                 80   70         90    70
    / \                     / \   \         / \    \
   60 50                   60 50 100       60 50   80
                                ↑
                            Compare with 70, swap
                            Compare with 90, swap
```

### Extract Max/Min - O(log n)

**Algorithm**:
1. Save root (max/min element)
2. Replace root with last element
3. Remove last element
4. "Heapify down" from root

```python
def extract_max(heap):
    if len(heap) == 0:
        return None
    
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    
    if heap:
        max_heapify(heap, len(heap), 0)
    
    return max_val
```

### Build Heap - O(n)

**Naive**: Insert n elements → O(n log n)
**Optimal**: Bottom-up heapify → O(n)

```python
def build_max_heap(arr):
    n = len(arr)
    
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
```

**Why O(n)?**
- Most nodes are near bottom (more nodes, less work)
- Half the nodes are leaves (0 work)
- Mathematical sum: Σ (h-i) * 2^i ≈ O(n)

---

## 8.5 Heap Sort

### Algorithm

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        max_heapify(arr, i, 0)  # Heapify reduced heap

# Time: O(n log n), Space: O(1) - in-place!
```

### Properties of Heap Sort

| Property | Value |
|----------|-------|
| Time (all cases) | O(n log n) |
| Space | O(1) |
| Stable | No |
| In-place | Yes |
| Adaptive | No |

**Comparison**:
| Algorithm | Time | Space | Stable |
|-----------|------|-------|--------|
| Merge Sort | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) avg | O(log n) | No |
| Heap Sort | O(n log n) | O(1) | No |

---

## 8.6 Priority Queue

### ADT Definition

| Operation | Description |
|-----------|-------------|
| insert(x, priority) | Add element with priority |
| extractMax() / extractMin() | Remove highest priority element |
| peek() | View highest priority element |
| changePriority(x, newPriority) | Update priority |
| delete(x) | Remove specific element |

### Implementation Options

| Implementation | Insert | Extract | Peek |
|----------------|--------|---------|------|
| Unsorted Array | O(1) | O(n) | O(n) |
| Sorted Array | O(n) | O(1) | O(1) |
| Binary Heap | O(log n) | O(log n) | O(1) |
| Fibonacci Heap | O(1) | O(log n)* | O(1) |

*Amortized

### Python Implementation Using heapq

```python
import heapq

# Min-heap (default in Python)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
print(heapq.heappop(heap))  # 3 (smallest)

# Max-heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -7)
print(-heapq.heappop(max_heap))  # 7 (largest)

# Build heap from list
arr = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(arr)  # O(n)

# K largest elements
k_largest = heapq.nlargest(3, arr)

# K smallest elements
k_smallest = heapq.nsmallest(3, arr)
```

---

## 8.7 Heap Applications

### Application 1: K Largest Elements

```python
import heapq

def k_largest(arr, k):
    # Use min-heap of size k
    heap = arr[:k]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap

# Time: O(n log k), Space: O(k)
```

### Application 2: Kth Largest Element

```python
def find_kth_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

# Time: O(n log k), Space: O(k)
```

### Application 3: Merge K Sorted Lists

```python
import heapq

def merge_k_lists(lists):
    heap = []
    
    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# Time: O(N log k), where N = total elements, k = number of lists
```

### Application 4: Median in Stream

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Lower half (negated for max behavior)
        self.min_heap = []  # Upper half
    
    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        
        # Ensure max_heap's max <= min_heap's min
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Balance sizes
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Add: O(log n), Find Median: O(1)
```

### Application 5: Top K Frequent Elements

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Time: O(n log k)
```

### Application 6: Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Time: O((V + E) log V)
```

---

## 8.8 Special Heaps

### Binomial Heap

**Properties**:
- Collection of binomial trees
- Binomial tree Bₖ has 2^k nodes
- Union operation: O(log n)

### Fibonacci Heap

**Properties**:
- Collection of min-heap trees
- Decrease key: O(1) amortized
- Used in advanced graph algorithms

| Operation | Binary Heap | Fibonacci Heap |
|-----------|-------------|----------------|
| Insert | O(log n) | O(1) |
| Extract Min | O(log n) | O(log n) |
| Decrease Key | O(log n) | O(1)* |
| Merge | O(n) | O(1) |

*Amortized

### Min-Max Heap

**Property**: 
- Even levels: min-heap property
- Odd levels: max-heap property
- Both min and max accessible in O(1)

---

## 8.9 GATE Exam Patterns

### Pattern 1: Build Heap Complexity

**Trap Question**: Building heap from n elements takes?

**Wrong Answer**: O(n log n) - because n inserts of O(log n) each
**Correct Answer**: O(n) - using bottom-up heapify

### Pattern 2: Array to Heap Visualization

**Q**: Is [90, 80, 70, 60, 50, 40, 30] a valid max-heap?

**Check**: Draw tree and verify parent ≥ children
```
        90
       /  \
      80   70
     / \   / \
    60 50 40 30

90 ≥ 80 ✓, 90 ≥ 70 ✓
80 ≥ 60 ✓, 80 ≥ 50 ✓
70 ≥ 40 ✓, 70 ≥ 30 ✓

Valid max-heap!
```

### Pattern 3: Heap Operations Sequence

**Q**: After inserting 100 into [90, 80, 70], what is the array?

```
Before: [90, 80, 70]
        90
       /  \
      80   70

Insert 100 at index 3 (0-indexed)
        90
       /  \
      80   70
     /
   100

Bubble up: 100 > 80, swap
        90
       /  \
     100   70
     /
    80

Bubble up: 100 > 90, swap
       100
       /  \
      90   70
     /
    80

Array: [100, 90, 70, 80]
```

### Pattern 4: Number of Comparisons

**Q**: Maximum comparisons to insert element in heap of size n?

**Answer**: O(log n) - height of tree

**Q**: Maximum comparisons to delete max from heap of size n?

**Answer**: 2 log n - at each level, compare with both children

---

## 8.10 Edge Cases & Traps

### Common Traps ⚠️

**Trap 1**: Heap is NOT a sorted array
```
Max-heap [90, 80, 70] → 90 is max, but 70 might not be min
[90, 30, 70, 10, 20, 60] is valid max-heap
(70 > 60, but 70 appears after 30)
```

**Trap 2**: Heap vs BST
- Heap: Parent ≥ children (or ≤), no left-right ordering
- BST: Left < Parent < Right

**Trap 3**: Delete arbitrary element
- Heap doesn't efficiently support finding arbitrary element
- Need O(n) search first

**Trap 4**: Heap sort not stable
- Equal elements may not maintain relative order

---

## 📝 GATE Practice Problems

**Q1**: A min-heap has 7 elements. Where can the largest element be located?

**Q2**: Convert array [4, 10, 3, 5, 1, 8, 7] into max-heap using bottom-up approach.

**Q3**: What is the minimum number of comparisons to find both max and min in array of n elements using a tournament tree?

**Q4**: In a max-heap with n elements, what is the minimum number of elements in the last level?

**Q5**: After 5 extract-max operations on max-heap [100, 80, 70, 60, 50, 40, 30, 20, 10], what is the heap?

---

## 🎯 Quick Reference

### Heap Formulas

| Property | Formula |
|----------|---------|
| Parent of i | (i-1)/2 or i/2 (1-indexed) |
| Left child of i | 2i+1 or 2i (1-indexed) |
| Right child of i | 2i+2 or 2i+1 (1-indexed) |
| Last non-leaf | n/2 - 1 or n/2 (1-indexed) |
| Height | ⌊log₂n⌋ |

### Complexity Summary

| Operation | Time |
|-----------|------|
| Build heap | O(n) |
| Insert | O(log n) |
| Extract max/min | O(log n) |
| Peek max/min | O(1) |
| Heap sort | O(n log n) |
| K largest | O(n log k) |

---

## 🔑 Key Takeaways

1. **Heap = Complete BT + Heap Property** - both must hold
2. **Build heap is O(n)**, not O(n log n)
3. **Heap is ideal for priority queue** implementation
4. **Heap sort is in-place** but not stable
5. **Use min-heap for K largest**, max-heap for K smallest
6. **Two heaps technique** for running median

---

*Next: [Hashing →](09-Hashing.md)*
