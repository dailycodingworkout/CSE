# Chapter 3: Searching Algorithms

## 3.1 Linear Search (Sequential Search)

> **Analogy:** Looking for a book in an unsorted pile — check each one, one by one.

**Algorithm:**
```
LinearSearch(A, n, key):
    for i = 0 to n-1:
        if A[i] == key:
            return i
    return -1  // not found
```

| Metric | Value |
|--------|-------|
| Best Case | O(1) — found at first position |
| Worst Case | O(n) — found at last position or absent |
| Average Case | O(n) — checks ~n/2 elements on average |
| Space | O(1) |

**Works on:** Sorted or unsorted arrays, linked lists.

> **When to use:** When data is unsorted, small, or you need to search only once.

---

## 3.2 Binary Search ⭐ (Most Important for GATE)

> **Analogy:** Finding a word in a dictionary — open to the middle, decide which half the word is in, repeat.

**Prerequisite:** Array must be **sorted**.

**Algorithm:**
```
BinarySearch(A, low, high, key):
    while low ≤ high:
        mid = low + (high - low) / 2    // avoids overflow
        if A[mid] == key:
            return mid
        else if A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

| Metric | Value |
|--------|-------|
| Best Case | O(1) — found at middle |
| Worst Case | O(log n) |
| Average Case | O(log n) |
| Space | O(1) iterative, O(log n) recursive |

### Why O(log n)?

At each step, we **halve the search space:**
- After 1 comparison: n/2 elements remain
- After 2 comparisons: n/4 elements remain
- After k comparisons: n/2ᵏ elements remain
- Search ends when n/2ᵏ = 1 → **k = log₂ n**

### Key Variants for GATE

**Finding first occurrence (leftmost):**
```
BinarySearchFirst(A, n, key):
    low = 0, high = n-1, result = -1
    while low ≤ high:
        mid = (low + high) / 2
        if A[mid] == key:
            result = mid        // record it
            high = mid - 1      // search left for earlier occurrence
        else if A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

**Finding last occurrence:** Same but go `low = mid + 1` on finding key.

**Minimum comparisons in Binary Search:**
- Successful search: Best = 1, Worst = ⌊log₂ n⌋ + 1
- Unsuccessful search: ⌊log₂ n⌋ or ⌈log₂(n+1)⌉ comparisons

> **GATE Classic Question:** "Minimum number of comparisons to search in a sorted array of n elements?"
> Answer: ⌊log₂ n⌋ + 1 (worst case for successful), ⌈log₂(n+1)⌉ (unsuccessful)

### Binary Search Decision Tree

For n elements, the binary search creates a **binary decision tree:**
- **Internal nodes** = successful comparisons
- **External nodes** (null) = unsuccessful comparisons
- Height = ⌊log₂ n⌋
- Internal path length + 2(n+1) = External path length (for extended binary tree)

> **GATE Trap:** "Average number of comparisons for a successful search in binary search?"  
> It's NOT just log n. It's **(internal path length of the decision tree) / n**. For n = 7: tree has heights 1,2,2,3,3,3,3 → avg = (1+2+2+3+3+3+3)/7 ≈ 2.43.

---

## 3.3 Ternary Search

**Idea:** Instead of dividing into 2 parts, divide into **3 parts**.

```
TernarySearch(A, low, high, key):
    if high >= low:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        if A[mid1] == key: return mid1
        if A[mid2] == key: return mid2
        if key < A[mid1]: return TernarySearch(A, low, mid1-1, key)
        elif key > A[mid2]: return TernarySearch(A, mid2+1, high, key)
        else: return TernarySearch(A, mid1+1, mid2-1, key)
    return -1
```

**Time Complexity:** T(n) = T(n/3) + O(1) → **O(log₃ n)**

> **GATE Trap: Is Ternary Search faster than Binary Search?**  
> **NO!** log₃ n = log₂ n / log₂ 3. But each step of ternary search does **2 comparisons** vs 1 for binary.  
> Total comparisons: 2·log₃ n vs log₂ n. Since 2/log₂3 ≈ 1.26 > 1, **binary search is actually better!**

---

## 3.4 Interpolation Search

> **Analogy:** If you're looking for "A" in a phone book, you don't start in the middle — you start near the beginning. Interpolation search uses the **value distribution** to guess where the key might be.

**Probe position formula:**
```
pos = low + ((key - A[low]) × (high - low)) / (A[high] - A[low])
```

**How the formula came up:**  
We assume elements are **uniformly distributed**. Linear interpolation gives:  
(pos - low)/(high - low) = (key - A[low])/(A[high] - A[low])  
Solving for pos gives the formula above.

| Metric | Value |
|--------|-------|
| Best Case | O(1) |
| Average Case | **O(log log n)** — for uniformly distributed data |
| Worst Case | **O(n)** — for exponentially distributed data |
| Space | O(1) |

> **When to use:** When data is **uniformly distributed** and sorted.  
> **GATE fact:** Interpolation search is O(log log n) on average for uniform data.

---

## 3.5 Exponential Search

**Idea:** Find the range where the key exists using exponential jumps (1, 2, 4, 8, 16, ...), then binary search within that range.

```
ExponentialSearch(A, n, key):
    if A[0] == key: return 0
    i = 1
    while i < n and A[i] <= key:
        i = i * 2
    return BinarySearch(A, i/2, min(i, n-1), key)
```

**Time Complexity:** O(log n) — finding range is O(log n), binary search within range is O(log n).

**Why use it?** Useful when the target is **near the beginning** of the array — it performs better than binary search for such cases.

> **Use Case:** Searching in unbounded/infinite sorted arrays.

---

## 3.6 Jump Search (Block Search)

**Idea:** Jump ahead by fixed steps of size √n, then do linear search in the block.

```
JumpSearch(A, n, key):
    step = √n
    prev = 0
    while A[min(step, n)-1] < key:
        prev = step
        step += √n
        if prev >= n: return -1
    // Linear search in block [prev, step)
    while A[prev] < key:
        prev++
        if prev == min(step, n): return -1
    if A[prev] == key: return prev
    return -1
```

**Time Complexity:** O(√n)

**Optimal block size:** √n (minimizes worst-case: n/m + m where m is block size; minimized when m = √n)

> **How optimal block size is derived:**  
> Total comparisons = n/m (jumps) + m (linear search in block)  
> Minimize n/m + m: derivative = -n/m² + 1 = 0 → m = √n

---

## 3.7 Comparison of Searching Algorithms

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Sorted Required? |
|-----------|-------------|------------|--------------|-------|-----------------|
| Linear | O(1) | O(n) | O(n) | O(1) | No |
| Binary | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Ternary | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) | Yes + Uniform |
| Exponential | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Jump | O(1) | O(√n) | O(√n) | O(1) | Yes |

---


---
