# Chapter 12: Searching Algorithms

## 🎯 The Atomic Truth
> **"Searching = Finding Target in Data"**

---

## 12.1 Types of Searching

| Type | Time | Requirement |
|------|------|-------------|
| Linear Search | O(n) | None |
| Binary Search | O(log n) | Sorted data |
| Hash-based | O(1) avg | Hash table |
| Tree-based | O(log n) | BST/Balanced tree |

---

## 12.2 Linear Search

### Basic Implementation

```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# Time: O(n), Space: O(1)
```

### With Sentinel

```python
def linear_search_sentinel(arr, target):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = target  # Sentinel
    
    i = 0
    while arr[i] != target:
        i += 1
    
    arr[n - 1] = last  # Restore
    
    if i < n - 1 or arr[n - 1] == target:
        return i
    return -1
```

**Advantage**: Eliminates bound check in loop (slightly faster)

### Complexity Analysis

| Case | Comparisons |
|------|-------------|
| Best | 1 |
| Average | n/2 |
| Worst | n |

---

## 12.3 Binary Search

### The "AHA" Moment 💡
> Each comparison eliminates half the remaining elements!

### Classic Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Time: O(log n), Space: O(1)
```

### Recursive Implementation

```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Time: O(log n), Space: O(log n) - recursion stack
```

### Why `mid = left + (right - left) // 2`?

```
left + right could overflow for large arrays
Example: left = 2^30, right = 2^30
left + right = 2^31 → overflow!

Safe: left + (right - left) // 2 stays within bounds
```

---

## 12.4 Binary Search Variations

### Find First Occurrence

```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Find Last Occurrence

```python
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Count Occurrences

```python
def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0
    last = find_last(arr, target)
    return last - first + 1
```

### Lower Bound (First >= target)

```python
def lower_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### Upper Bound (First > target)

```python
def upper_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

---

## 12.5 Binary Search on Answer

### Concept
When the answer has monotonic property, binary search on the answer space.

### Example: Square Root

```python
def sqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor of sqrt
```

### Example: Minimum Capacity to Ship

```python
def ship_within_days(weights, days):
    def can_ship(capacity):
        current_load = 0
        days_needed = 1
        
        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = 0
            current_load += w
        
        return days_needed <= days
    
    left, right = max(weights), sum(weights)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

---

## 12.6 Search in Rotated Sorted Array

### Find Pivot (Minimum Element)

```python
def find_pivot(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### Search in Rotated Array

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

## 12.7 Search in 2D Matrix

### Row-wise and Column-wise Sorted

```python
def search_matrix(matrix, target):
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from top-right
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False

# Time: O(m + n), Space: O(1)
```

### Fully Sorted (Each row starts after previous ends)

```python
def search_matrix_sorted(matrix, target):
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Time: O(log(m*n)), Space: O(1)
```

---

## 12.8 Special Searches

### Peak Element

```python
def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Time: O(log n)
```

### Minimum in Rotated Sorted Array

```python
def find_min(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]
```

### Search Insert Position

```python
def search_insert(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

---

## 12.9 Ternary Search

### Concept
For unimodal functions (one peak/valley), ternary search finds the extremum.

```python
def ternary_search_max(f, left, right, epsilon=1e-9):
    while right - left > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        if f(mid1) < f(mid2):
            left = mid1
        else:
            right = mid2
    
    return (left + right) / 2

# Time: O(log n)
```

### Ternary vs Binary

- Binary: Monotonic functions
- Ternary: Unimodal functions

---

## 12.10 Interpolation Search

### Concept
Estimate position based on value distribution (like finding word in dictionary).

```python
def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        
        # Estimate position
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

| Case | Time |
|------|------|
| Best | O(1) |
| Average (uniform) | O(log log n) |
| Worst | O(n) |

**Use when**: Data is uniformly distributed

---

## 12.11 Exponential Search

### Concept
Find range, then binary search. Good for unbounded arrays.

```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    # Find range
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Binary search in range
    return binary_search(arr, target, i // 2, min(i, len(arr) - 1))

# Time: O(log n)
```

**Use when**: 
- Target is near the beginning
- Array size is unknown

---

## 12.12 Jump Search

### Concept
Jump by fixed steps, then linear search in block.

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal step size
    
    # Find block
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

# Time: O(√n), Space: O(1)
```

---

## 12.13 Search Comparison

| Algorithm | Time | Space | Requirement |
|-----------|------|-------|-------------|
| Linear | O(n) | O(1) | None |
| Binary | O(log n) | O(1) | Sorted |
| Jump | O(√n) | O(1) | Sorted |
| Interpolation | O(log log n)* | O(1) | Sorted, uniform |
| Exponential | O(log n) | O(1) | Sorted |
| Ternary | O(log n) | O(1) | Unimodal |
| Hash | O(1)* | O(n) | Hash table |

*Average case

---

## 12.14 GATE Exam Patterns

### Pattern 1: Comparison Count

**Q**: Binary search on 1000 elements. Maximum comparisons?

**Answer**: ⌈log₂1000⌉ + 1 = 10 + 1 = 11 (or 10 depending on implementation)

### Pattern 2: Array Size Questions

**Q**: Binary search takes at most 10 comparisons. Maximum array size?

**Answer**: 2^10 - 1 = 1023 (or 2^10 = 1024)

### Pattern 3: Algorithm Identification

**Q**: Which search works on unsorted arrays?

**Answer**: Linear search, Hash-based search

### Pattern 4: Search Modifications

**Q**: Find floor/ceiling of target in sorted array.

**Solution**: Modify binary search to track closest smaller/larger

---

## 📝 GATE Practice Problems

**Q1**: Binary search is performed on sorted array of 500 elements. In worst case, how many comparisons?

**Q2**: An array has elements {1, 2, 3, ..., 100}. How many comparisons to search for 75 using interpolation search?

**Q3**: Jump search optimal step size for array of size n?

**Q4**: Searching for key in balanced BST with 1 million nodes takes at most how many comparisons?

**Q5**: In exponential search, after finding the range, what's the binary search range size?

---

## 🎯 Quick Reference

### Binary Search Template

```python
def binary_search_template(arr, condition):
    left, right = 0, len(arr) - 1
    
    while left <= right:  # or left < right for some variants
        mid = left + (right - left) // 2
        
        if condition(mid):
            # Found or search right
            pass
        else:
            # Search left
            pass
    
    return result
```

### Common Patterns

| Pattern | Condition | Search Direction |
|---------|-----------|------------------|
| Find exact | arr[mid] == target | Return |
| Find first >= | arr[mid] >= target | Search left |
| Find last <= | arr[mid] <= target | Search right |
| Find peak | arr[mid] > arr[mid+1] | Search left |

---

## 🔑 Key Takeaways

1. **Binary search requires sorted data** - the fundamental requirement
2. **Use `left + (right - left) // 2`** to avoid overflow
3. **Variations are key** - first occurrence, last occurrence, bounds
4. **Binary search on answer** is a powerful technique
5. **Choose algorithm based on data characteristics**
6. **O(log n) is the best for sorted search** without extra space

---

*Next: [Advanced Data Structures →](13-Advanced-DS.md)*
