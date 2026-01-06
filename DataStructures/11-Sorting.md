# Chapter 11: Sorting Algorithms

## 🎯 The Atomic Truth
> **"Sorting = Arranging Elements in Order"**

---

## 11.1 Why Sorting Matters

### The Impact
- **Binary Search** requires sorted data → O(log n) vs O(n)
- **Finding duplicates** becomes trivial
- **Finding median/percentiles** becomes O(1)
- Many algorithms assume sorted input

### Classification

| Criterion | Types |
|-----------|-------|
| Time Complexity | O(n²), O(n log n), O(n) |
| Space | In-place (O(1)), Not in-place |
| Stability | Stable, Unstable |
| Adaptivity | Adaptive, Non-adaptive |
| Method | Comparison, Non-comparison |

---

## 11.2 Comparison-Based Sorting

### Lower Bound Theorem
**Any comparison-based sorting algorithm requires Ω(n log n) comparisons in worst case.**

**Proof sketch**: 
- n! possible permutations
- Decision tree has n! leaves
- Height of tree ≥ log(n!) = Ω(n log n)

---

## 11.3 Bubble Sort

### The Idea
Compare adjacent elements and swap if out of order. Largest "bubbles up" each pass.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization
            break
    return arr
```

**Visual**:
```
Pass 1: [5,3,8,4,2] → [3,5,8,4,2] → [3,5,8,4,2] → [3,5,4,8,2] → [3,5,4,2,8]
Pass 2: [3,5,4,2,8] → [3,5,4,2,8] → [3,4,5,2,8] → [3,4,2,5,8]
Pass 3: [3,4,2,5,8] → [3,4,2,5,8] → [3,2,4,5,8]
Pass 4: [3,2,4,5,8] → [2,3,4,5,8]
```

| Property | Value |
|----------|-------|
| Time (Best) | O(n) - already sorted |
| Time (Average) | O(n²) |
| Time (Worst) | O(n²) |
| Space | O(1) |
| Stable | Yes |
| Adaptive | Yes |

---

## 11.4 Selection Sort

### The Idea
Find minimum element and place at beginning. Repeat for remaining.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Visual**:
```
[5,3,8,4,2] → Find min=2 → [2,3,8,4,5]
[2,3,8,4,5] → Find min=3 → [2,3,8,4,5]
[2,3,8,4,5] → Find min=4 → [2,3,4,8,5]
[2,3,4,8,5] → Find min=5 → [2,3,4,5,8]
```

| Property | Value |
|----------|-------|
| Time (All cases) | O(n²) |
| Space | O(1) |
| Stable | No (standard), Yes (with modification) |
| Swaps | O(n) - minimum among O(n²) sorts |

**Use when**: Write operations are expensive (fewer swaps)

---

## 11.5 Insertion Sort

### The Idea
Build sorted array one element at a time by inserting each element at correct position.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Visual**:
```
[5,3,8,4,2]  key=3, insert before 5 → [3,5,8,4,2]
[3,5,8,4,2]  key=8, already in place → [3,5,8,4,2]
[3,5,8,4,2]  key=4, insert between 3,5 → [3,4,5,8,2]
[3,4,5,8,2]  key=2, insert at beginning → [2,3,4,5,8]
```

| Property | Value |
|----------|-------|
| Time (Best) | O(n) - already sorted |
| Time (Average) | O(n²) |
| Time (Worst) | O(n²) - reverse sorted |
| Space | O(1) |
| Stable | Yes |
| Adaptive | Yes |

**Use when**: 
- Small arrays (n < 50)
- Nearly sorted arrays
- Online sorting (elements arrive one by one)

---

## 11.6 Merge Sort

### The Idea
Divide array in half, recursively sort, then merge.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Visual**:
```
         [5,3,8,4,2]
        /           \
    [5,3,8]        [4,2]
    /     \        /    \
 [5,3]   [8]     [4]   [2]
 /   \
[5]  [3]

Merge back:
[3,5] + [8] = [3,5,8]
[2] + [4] = [2,4]
[3,5,8] + [2,4] = [2,3,4,5,8]
```

| Property | Value |
|----------|-------|
| Time (All cases) | O(n log n) |
| Space | O(n) |
| Stable | Yes |
| Adaptive | No |

**The "AHA" Moment** 💡:
> Merge sort is the only O(n log n) stable sort that's also consistent (same time for all inputs)

### Recurrence Relation
$$T(n) = 2T(n/2) + O(n)$$
**Solution**: O(n log n) by Master Theorem

---

## 11.7 Quick Sort

### The Idea
Choose pivot, partition array around pivot, recursively sort partitions.

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Visual**:
```
[5,3,8,4,2]  pivot=2
After partition: [2,3,8,4,5]  (2 is in place)

Left: [] (empty)
Right: [3,8,4,5]  pivot=5
After partition: [3,4,5,8] ...
```

| Property | Value |
|----------|-------|
| Time (Best) | O(n log n) |
| Time (Average) | O(n log n) |
| Time (Worst) | O(n²) - already sorted with bad pivot |
| Space | O(log n) - recursion stack |
| Stable | No |

### Pivot Selection Strategies

1. **Last element** (simple but bad for sorted input)
2. **First element** (same issue)
3. **Random element** (good average case)
4. **Median of three** (first, middle, last)

### Randomized Quick Sort

```python
import random

def randomized_partition(arr, low, high):
    random_idx = random.randint(low, high)
    arr[random_idx], arr[high] = arr[high], arr[random_idx]
    return partition(arr, low, high)
```

---

## 11.8 Heap Sort

### The Idea
Build max-heap, repeatedly extract max.

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

| Property | Value |
|----------|-------|
| Time (All cases) | O(n log n) |
| Space | O(1) |
| Stable | No |
| In-place | Yes |

---

## 11.9 Non-Comparison Sorts

### Counting Sort (O(n + k))

**Constraint**: Integer keys in range [0, k]

```python
def counting_sort(arr, max_val=None):
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output (stable)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output
```

| Property | Value |
|----------|-------|
| Time | O(n + k) |
| Space | O(n + k) |
| Stable | Yes |

### Radix Sort (O(d × (n + k)))

**Constraint**: Integer keys with d digits

```python
def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for num in reversed(arr):
        digit = (num // exp) % 10
        output[count[digit] - 1] = num
        count[digit] -= 1
    
    for i in range(n):
        arr[i] = output[i]
```

| Property | Value |
|----------|-------|
| Time | O(d × n) where d = digits |
| Space | O(n + 10) |
| Stable | Yes |

### Bucket Sort (O(n) average)

**Constraint**: Uniformly distributed data

```python
def bucket_sort(arr, num_buckets=10):
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / num_buckets + 1
    
    buckets = [[] for _ in range(num_buckets)]
    
    for num in arr:
        bucket_idx = int((num - min_val) / bucket_range)
        buckets[bucket_idx].append(num)
    
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))  # Use insertion sort for small buckets
    
    return result
```

| Property | Value |
|----------|-------|
| Time (Average) | O(n) |
| Time (Worst) | O(n²) |
| Space | O(n) |
| Stable | Depends on bucket sort |

---

## 11.10 Sorting Algorithm Comparison

### Complete Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✓ | ✓ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ✗ | ✓ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✓ | ✓ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ | ✗ |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ | ✓ |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ | ✓ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✓ | ✗ |
| Radix | O(dn) | O(dn) | O(dn) | O(n+k) | ✓ | ✗ |
| Bucket | O(n) | O(n) | O(n²) | O(n) | ✓ | ✗ |

### Which to Choose?

| Scenario | Best Algorithm |
|----------|----------------|
| Small array (n < 50) | Insertion Sort |
| Nearly sorted | Insertion Sort |
| Guaranteed O(n log n) | Merge Sort |
| Average performance, in-place | Quick Sort |
| Limited extra memory | Heap Sort |
| Integer keys, small range | Counting Sort |
| Integer keys, large range | Radix Sort |
| Uniformly distributed | Bucket Sort |
| Stability required | Merge Sort |
| External sorting | Merge Sort |

---

## 11.11 GATE Exam Patterns

### Pattern 1: Number of Comparisons

**Q**: Minimum comparisons to sort array of n elements?

**Answer**: n log n (lower bound)

**Q**: Comparisons in specific algorithm?

| Algorithm | Comparisons |
|-----------|-------------|
| Bubble (worst) | n(n-1)/2 |
| Insertion (worst) | n(n-1)/2 |
| Selection | n(n-1)/2 |
| Merge | n log n |

### Pattern 2: Number of Swaps

**Q**: Which algorithm minimizes swaps?

**Answer**: Selection Sort - O(n) swaps

### Pattern 3: Best Algorithm for Given Scenario

**Q**: Best sort for nearly sorted array?

**Answer**: Insertion Sort - O(n) for almost sorted

**Q**: Best sort for linked list?

**Answer**: Merge Sort - no random access needed

### Pattern 4: Stability Questions

**Q**: Which sorts are stable?

**Stable**: Bubble, Insertion, Merge, Counting, Radix
**Unstable**: Selection, Quick, Heap

### Pattern 5: Pass Analysis

**Q**: After k passes of bubble sort, what's guaranteed?

**Answer**: Last k elements are in final position

---

## 11.12 Advanced: External Sorting

### When Data Doesn't Fit in Memory

**Solution**: External Merge Sort

1. Divide data into chunks that fit in memory
2. Sort each chunk in memory
3. Write sorted chunks to disk
4. Merge sorted chunks

**Key Metric**: Minimize disk I/O

---

## 📝 GATE Practice Problems

**Q1**: An array has 10 elements. After one pass of bubble sort (largest to end), how many elements are definitely in correct position?

**Q2**: Quick sort is called on array [3,2,1,4,5]. Pivot is first element. Show array after first partition.

**Q3**: What is the minimum number of comparisons to find median of 5 elements?

**Q4**: Merge sort requires how many comparisons to merge two sorted arrays of size n/2 each?

**Q5**: Can radix sort be used for floating point numbers? If yes, how?

---

## 🎯 Quick Reference

### Recurrence Relations

| Algorithm | Recurrence | Solution |
|-----------|------------|----------|
| Merge Sort | T(n) = 2T(n/2) + n | O(n log n) |
| Quick Sort (best) | T(n) = 2T(n/2) + n | O(n log n) |
| Quick Sort (worst) | T(n) = T(n-1) + n | O(n²) |
| Binary Search | T(n) = T(n/2) + 1 | O(log n) |

### Number of Inversions

**Definition**: Pair (i, j) where i < j but arr[i] > arr[j]

**Count via Merge Sort**: O(n log n)
- Count inversions during merge step

---

## 🔑 Key Takeaways

1. **O(n log n) is the lower bound** for comparison-based sorting
2. **Quick Sort is fastest in practice** despite O(n²) worst case
3. **Merge Sort is the only stable O(n log n)** sort
4. **Insertion Sort is best for small/nearly sorted** arrays
5. **Use non-comparison sorts** when applicable (integers, limited range)
6. **Stability matters** when sorting objects by multiple keys

---

*Next: [Searching Algorithms →](12-Searching.md)*
