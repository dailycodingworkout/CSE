# Chapter 4: Sorting Algorithms

## 4.1 Why Study Sorting?

Sorting is the **most frequently tested topic** in GATE algorithms. Understanding sorting teaches you:
- Algorithm design paradigms (D&C, greedy, incremental)
- Time-space tradeoffs
- Stability and in-place concepts
- Lower bounds (Ω(n log n) for comparison sorts)

> **Analogy:** Sorting is like organizing a library. Different methods work better depending on how many books you have, how messy they are, and how much shelf space you have.

---

## 4.2 Key Terminology

| Term | Definition |
|------|-----------|
| **Stable** | Equal elements maintain their original relative order |
| **In-place** | Uses O(1) auxiliary space (ignoring recursion stack) |
| **Adaptive** | Performs better when input is partially sorted |
| **Online** | Can sort a list as it receives elements one by one |

> **GATE Favorite:** "Which sorting algorithms are stable?" — Bubble, Insertion, Merge, Counting, Radix (mnemonic: **BIMCR** — "BIM sorts CuRiously")

---

## 4.3 Bubble Sort

> **Analogy:** Like bubbles rising in water — larger elements "bubble up" to the end.

```
BubbleSort(A, n):
    for i = 0 to n-2:
        swapped = false
        for j = 0 to n-i-2:
            if A[j] > A[j+1]:
                swap(A[j], A[j+1])
                swapped = true
        if not swapped: break    // optimization
```

| Property | Value |
|----------|-------|
| Best Case | O(n) — already sorted (with optimization) |
| Average Case | O(n²) |
| Worst Case | O(n²) — reverse sorted |
| Space | O(1) |
| Stable | ✅ Yes |
| Adaptive | ✅ Yes (with flag) |
| In-place | ✅ Yes |

**Number of swaps (worst case):** n(n-1)/2 = inversions in reverse-sorted array

> **GATE Insight:** Number of swaps in bubble sort = number of **inversions** in the array. An inversion is a pair (i,j) where i < j but A[i] > A[j].

---

## 4.4 Selection Sort

> **Analogy:** Like picking the smallest card from a hand and placing it first, then the next smallest, etc.

```
SelectionSort(A, n):
    for i = 0 to n-2:
        minIdx = i
        for j = i+1 to n-1:
            if A[j] < A[minIdx]:
                minIdx = j
        swap(A[i], A[minIdx])
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All O(n²)** |
| Space | O(1) |
| Stable | ❌ No (swaps can change relative order) |
| Adaptive | ❌ No |
| In-place | ✅ Yes |
| Swaps | **O(n)** — minimum swaps among simple sorts |

> **GATE Fact:** Selection sort always does exactly n-1 swaps, regardless of input. It has the **minimum number of swaps** among O(n²) sorts.

> **Why not stable?** Consider [5a, 5b, 2]. After first pass: [2, 5b, 5a] — the order of 5s changed!

---

## 4.5 Insertion Sort ⭐

> **Analogy:** Like sorting playing cards in your hand — pick one card at a time and insert it into its correct position among the already-sorted cards.

```
InsertionSort(A, n):
    for i = 1 to n-1:
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

| Property | Value |
|----------|-------|
| Best Case | **O(n)** — already sorted |
| Average Case | O(n²) |
| Worst Case | O(n²) — reverse sorted |
| Space | O(1) |
| Stable | ✅ Yes |
| Adaptive | ✅ Yes |
| In-place | ✅ Yes |
| Online | ✅ Yes |

**Number of comparisons:**
- Best: n - 1
- Worst: n(n-1)/2
- Average: n(n-1)/4

> **GATE Gem:** Insertion sort is the **best choice for small arrays** (n < 20-30). Many practical sorting algorithms (like Tim Sort used in Python) use insertion sort for small subarrays.

> **GATE Fact:** Insertion sort's running time is **O(n + d)** where d is the number of inversions. For nearly sorted arrays (few inversions), it's nearly linear!

---

## 4.6 Merge Sort ⭐⭐

> **Analogy:** Splitting a deck of cards into two halves, sorting each half, then carefully merging them by comparing top cards.

```
MergeSort(A, low, high):
    if low < high:
        mid = (low + high) / 2
        MergeSort(A, low, mid)
        MergeSort(A, mid+1, high)
        Merge(A, low, mid, high)

Merge(A, low, mid, high):
    Create temp arrays L = A[low..mid], R = A[mid+1..high]
    i = j = 0, k = low
    while i < |L| and j < |R|:
        if L[i] <= R[j]:      // <= ensures stability
            A[k++] = L[i++]
        else:
            A[k++] = R[j++]
    Copy remaining elements
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All Θ(n log n)** |
| Space | **O(n)** auxiliary |
| Stable | ✅ Yes |
| Adaptive | ❌ No (always n log n) |
| In-place | ❌ No |

### Why Θ(n log n)?

Recurrence: T(n) = 2T(n/2) + Θ(n)

By Master Theorem: a=2, b=2, f(n)=n, n^(log₂2) = n → Case 2 → **Θ(n log n)**

### Key Properties for GATE

1. **Merge sort is optimal** for comparison-based sorting (matches Ω(n log n) lower bound)
2. **Best for linked lists** — no random access needed, and merge can be done in O(1) extra space
3. **Number of comparisons** (worst case): n⌈log₂n⌉ - 2^⌈log₂n⌉ + 1
4. **External sorting** uses merge sort (for data too large for RAM)

> **GATE Classic:** "Minimum comparisons to merge two sorted arrays of size m and n?"  
> Answer: min(m, n) comparisons (best case), m + n - 1 (worst case)

---

## 4.7 Quick Sort ⭐⭐

> **Analogy:** Organizing a group by height — pick one person (pivot), everyone shorter goes left, everyone taller goes right, repeat for each group.

```
QuickSort(A, low, high):
    if low < high:
        pivotIdx = Partition(A, low, high)
        QuickSort(A, low, pivotIdx - 1)
        QuickSort(A, pivotIdx + 1, high)

Partition(A, low, high):
    pivot = A[high]        // Last element as pivot
    i = low - 1
    for j = low to high - 1:
        if A[j] <= pivot:
            i++
            swap(A[i], A[j])
    swap(A[i+1], A[high])
    return i + 1
```

| Property | Value |
|----------|-------|
| Best Case | O(n log n) — balanced partition |
| Average Case | **O(n log n)** |
| Worst Case | **O(n²)** — already sorted (with last element pivot) |
| Space | O(log n) average, O(n) worst (recursion stack) |
| Stable | ❌ No |
| In-place | ✅ Yes |

### Why O(n²) Worst Case?

When array is **already sorted** and we pick the last element as pivot:
- Partition creates subarrays of size 0 and n-1
- T(n) = T(n-1) + T(0) + Θ(n) = T(n-1) + Θ(n) → **Θ(n²)**

### Why O(n log n) Average?

Even with random input, the **average partition splits somewhere between 1:9 and 9:1**.  
T(n) = T(n/10) + T(9n/10) + Θ(n)

Recursion tree: depth = log₁₀/₉ n = O(log n), each level costs O(n) → **O(n log n)**

> **Proof sketch:** The expected depth when pivot is chosen randomly is O(log n) because the probability of a "good" partition (that's at least 1/4 to 3/4) is 1/2.

### Randomized Quick Sort

Pick a **random element** as pivot → expected O(n log n) for any input.

> **GATE Fact:** Randomized Quick Sort has expected O(n log n) time for ALL inputs (no worst case input exists in expectation).

### Quick Sort Optimization Tricks

1. **Median-of-3:** Pick median of first, middle, last → avoids worst case for sorted input
2. **Switch to Insertion Sort** for small subarrays (n < 10)
3. **Tail recursion elimination:** Only recurse on the smaller half → O(log n) guaranteed stack space

### Partition Analysis

**Number of comparisons in partition:** n - 1 (each element compared with pivot exactly once)

**Quick Sort total comparisons:**
- Best: ~n log₂ n
- Average: ~1.39n log₂ n ≈ 2n ln n
- Worst: n(n-1)/2

> **GATE Trap:** "Quick sort is faster than Merge sort in practice because..."
> - Better **cache performance** (sequential access)
> - In-place (no extra array)
> - Inner loop is simple (just comparison + increment)
> - Despite same O(n log n), constant factors are smaller

---

## 4.8 Heap Sort

> **Analogy:** Build a tournament bracket (heap), repeatedly extract the champion (max), and the tree reorganizes itself.

```
HeapSort(A, n):
    // Build max-heap (bottom-up)
    for i = n/2 - 1 downto 0:
        Heapify(A, n, i)
    // Extract elements one by one
    for i = n-1 downto 1:
        swap(A[0], A[i])       // Move current max to end
        Heapify(A, i, 0)       // Heapify reduced heap

Heapify(A, n, i):
    largest = i
    left = 2i + 1
    right = 2i + 2
    if left < n and A[left] > A[largest]: largest = left
    if right < n and A[right] > A[largest]: largest = right
    if largest != i:
        swap(A[i], A[largest])
        Heapify(A, n, largest)
```

| Property | Value |
|----------|-------|
| Best/Average/Worst | **All O(n log n)** |
| Space | **O(1)** |
| Stable | ❌ No |
| In-place | ✅ Yes |

### Build Heap: Why O(n) and not O(n log n)?

**Intuitive explanation:** Most nodes are at the bottom of the heap. Leaves (n/2 nodes) don't need heapifying. Each level above does decreasing work.

**Formal:** Cost = Σ(h=0 to ⌊log n⌋) ⌈n/2^(h+1)⌉ · O(h) = O(n · Σ h/2ʰ) = **O(n)**

The sum Σ(h=0 to ∞) h/2ʰ = 2 (converges!) → O(n × 2) = **O(n)**.

> **GATE Favorite:** "Time complexity of building a heap?" → **O(n)**, NOT O(n log n)!

> **GATE Trap:** "Heap sort is optimal and in-place. Why isn't it used more in practice?"  
> Poor **cache performance** — jumps around array non-sequentially. Quick sort with good pivot selection beats it in practice.

---

## 4.9 Counting Sort

> **Analogy:** Like sorting mail into post-office boxes by ZIP code — create a slot for each possible value.

**Prerequisite:** Elements must be **integers in range [0, k]**.

```
CountingSort(A, n, k):
    Count[0..k] = 0
    for j = 0 to n-1:
        Count[A[j]]++
    for i = 1 to k:
        Count[i] += Count[i-1]    // Cumulative count
    for j = n-1 downto 0:         // Reverse for stability
        B[Count[A[j]] - 1] = A[j]
        Count[A[j]]--
    Copy B to A
```

| Property | Value |
|----------|-------|
| Time | **O(n + k)** |
| Space | **O(n + k)** |
| Stable | ✅ Yes |
| In-place | ❌ No |

> **When to use:** When k = O(n) (range is linear in input size). If k = O(n²), counting sort is no better than comparison sorts.

> **GATE Fact:** Counting sort is NOT a comparison sort — it bypasses the Ω(n log n) lower bound!

---

## 4.10 Radix Sort

> **Analogy:** Like sorting paper forms — first by the last digit, then second-to-last, etc. (LSD — Least Significant Digit first)

```
RadixSort(A, n, d):
    for i = 1 to d:          // d = number of digits
        StableSort on digit i using CountingSort
```

| Property | Value |
|----------|-------|
| Time | **O(d × (n + b))** where b = base, d = digits |
| Space | O(n + b) |
| Stable | ✅ Yes (must use stable sort for each digit) |

If numbers are in range [0, nᵏ], use base n: d = k digits → Time = O(k × n) = **O(kn)**

> **GATE Trap:** "Why must the intermediate sort be stable?"  
> If it's not stable, sorting by digit i might undo the ordering achieved by digit i-1.

> **GATE Fact:** For n integers in range [0, nᶜ] for constant c, radix sort runs in **O(n)**.

---

## 4.11 Bucket Sort

> **Analogy:** Put items into labeled buckets based on value range, sort each bucket, then concatenate.

```
BucketSort(A, n):
    Create n empty buckets B[0..n-1]
    for i = 0 to n-1:
        Insert A[i] into B[⌊n × A[i]⌋]   // for values in [0, 1)
    for i = 0 to n-1:
        Sort B[i] using insertion sort
    Concatenate all buckets
```

| Property | Value |
|----------|-------|
| Average Case | **O(n)** for uniformly distributed input |
| Worst Case | O(n²) — all elements in one bucket |
| Space | O(n) |
| Stable | ✅ Yes (if using stable sort) |

> **When to use:** Input is **uniformly distributed** over a known range.

---

## 4.12 Lower Bound for Comparison-Based Sorting

### The Ω(n log n) Lower Bound — Why Can't We Do Better?

**Decision Tree Model:** Any comparison-based sort can be modeled as a binary decision tree where:
- Each internal node is a comparison (aᵢ vs aⱼ)
- Each leaf is a permutation (output)
- For n elements, there are **n! possible permutations**

**The tree must have ≥ n! leaves.** A binary tree of height h has at most 2ʰ leaves.

```
2ʰ ≥ n!
h ≥ log₂(n!)
h ≥ n log₂ n - n log₂ e    [Stirling's approximation]
h = Ω(n log n)
```

**Therefore: Any comparison-based sorting algorithm requires Ω(n log n) comparisons in the worst case.**

> **GATE Conclusion:**
> - Merge Sort, Heap Sort achieve this lower bound → they are **optimal comparison sorts**
> - Counting Sort, Radix Sort bypass this by not comparing elements
> - Bubble, Insertion, Selection are NOT optimal (O(n²) worst case)

---

## 4.13 Master Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✅ | ❌ |
| Radix Sort | O(d(n+b)) | O(d(n+b)) | O(d(n+b)) | O(n+b) | ✅ | ❌ |
| Bucket Sort | O(n+k) | O(n) | O(n²) | O(n) | ✅ | ❌ |

> **Trick to Remember:**
> - **In-place + O(n log n):** Only Heap Sort
> - **Stable + O(n log n):** Only Merge Sort
> - **No comparison sort is both stable and in-place with O(n log n) worst case**
> - **Best for nearly sorted:** Insertion Sort
> - **Best practical general-purpose:** Quick Sort (randomized)

---


---
