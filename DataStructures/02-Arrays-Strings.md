# Chapter 2: Arrays & Strings

## 🎯 The Atomic Truth
> **"Array = Contiguous Memory + Index-Based Access"**

---

## 2.1 Array Fundamentals

### The Mental Model 🧠
Imagine a **row of lockers** in a school:
- Each locker has a **number** (index)
- All lockers are **same size** (same data type)
- Lockers are **adjacent** (contiguous memory)
- You can directly go to locker #50 without checking 1-49 (random access)

### Definition
An **Array** is a collection of elements of the same data type stored in contiguous memory locations.

### Memory Layout

```
Array: [10, 20, 30, 40, 50]

Memory Address:
1000     1004     1008     1012     1016
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
  arr[0]   arr[1]   arr[2]   arr[3]   arr[4]

Address of arr[i] = Base Address + (i × Size of element)
                  = 1000 + (i × 4)  [for 4-byte integers]
```

---

## 2.2 Types of Arrays

### 1. One-Dimensional Array (1D)

```
Declaration: int arr[5] = {1, 2, 3, 4, 5};

Memory: [1][2][3][4][5]
         ↑
    Base Address
```

**Address Formula**: `addr(arr[i]) = Base + i × sizeof(element)`

### 2. Two-Dimensional Array (2D)

```
Declaration: int matrix[3][4];

Logical View:          
    Col 0  Col 1  Col 2  Col 3
   ┌──────┬──────┬──────┬──────┐
Row 0 │  1   │  2   │  3   │  4   │
   ├──────┼──────┼──────┼──────┤
Row 1 │  5   │  6   │  7   │  8   │
   ├──────┼──────┼──────┼──────┤
Row 2 │  9   │  10  │  11  │  12  │
   └──────┴──────┴──────┴──────┘
```

### Row-Major Order (Most Common - C, C++, Java, Python)

```
Elements stored row by row:
[1][2][3][4][5][6][7][8][9][10][11][12]
 ←─Row 0─→ ←─Row 1─→  ←──Row 2──→

Address Formula:
addr(arr[i][j]) = Base + (i × num_columns + j) × sizeof(element)
```

### Column-Major Order (Fortran, MATLAB)

```
Elements stored column by column:
[1][5][9][2][6][10][3][7][11][4][8][12]
 ←Col 0→ ←Col 1→  ←Col 2→  ←Col 3→

Address Formula:
addr(arr[i][j]) = Base + (j × num_rows + i) × sizeof(element)
```

### 🎯 GATE Trap Alert!
> **Most GATE questions on 2D arrays test Row-Major vs Column-Major formulas**

**Quick Memory Trick**:
- **R**ow-Major = **R**ight order (row index × columns)
- **C**olumn-Major = **C**razy order (column index × rows)

---

## 2.3 Array Operations Complexity

| Operation | Time Complexity | Explanation |
|-----------|-----------------|-------------|
| Access by index | O(1) | Direct address calculation |
| Search (unsorted) | O(n) | Must check each element |
| Search (sorted) | O(log n) | Binary search possible |
| Insert at end | O(1) | If space available |
| Insert at beginning | O(n) | Shift all elements |
| Insert at position k | O(n-k) | Shift elements after k |
| Delete at end | O(1) | Just decrement size |
| Delete at beginning | O(n) | Shift all elements |
| Delete at position k | O(n-k) | Shift elements after k |

---

## 2.4 Address Calculation Problems

### Problem Type 1: 1D Array Address

**Question**: An array A[1...100] has base address 2000. If each element takes 4 bytes, what is the address of A[25]?

**Solution**:
```
Formula: Address(A[i]) = Base + (i - Lower_Bound) × Size

Address(A[25]) = 2000 + (25 - 1) × 4
               = 2000 + 24 × 4
               = 2000 + 96
               = 2096
```

### Problem Type 2: 2D Array Row-Major

**Question**: A 2D array A[5][10] has base address 1000. Each element is 2 bytes. Find address of A[3][7] in Row-Major.

**Solution**:
```
Formula: Address(A[i][j]) = Base + (i × Columns + j) × Size

Address(A[3][7]) = 1000 + (3 × 10 + 7) × 2
                 = 1000 + (30 + 7) × 2
                 = 1000 + 37 × 2
                 = 1000 + 74
                 = 1074
```

### Problem Type 3: 2D Array Column-Major

**Question**: Same array A[5][10], find address of A[3][7] in Column-Major.

**Solution**:
```
Formula: Address(A[i][j]) = Base + (j × Rows + i) × Size

Address(A[3][7]) = 1000 + (7 × 5 + 3) × 2
                 = 1000 + (35 + 3) × 2
                 = 1000 + 38 × 2
                 = 1000 + 76
                 = 1076
```

### Problem Type 4: Non-Zero Based Indexing

**Question**: Array A[2:10][3:15] with base 1000, element size 4. Find A[5][10] in Row-Major.

**Solution**:
```
Step 1: Normalize indices
- Rows: 2 to 10 → 9 rows (10 - 2 + 1)
- Columns: 3 to 15 → 13 columns (15 - 3 + 1)

Step 2: Convert to 0-based
- Row index: 5 - 2 = 3
- Column index: 10 - 3 = 7

Step 3: Apply formula
Address = 1000 + (3 × 13 + 7) × 4
        = 1000 + (39 + 7) × 4
        = 1000 + 46 × 4
        = 1000 + 184
        = 1184
```

---

## 2.5 Array Techniques for Problem Solving

### Technique 1: Two Pointers

**Use Case**: Finding pairs, reversing, partitioning

```python
# Find pair with given sum in sorted array
def find_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Time: O(n), Space: O(1)
```

### Technique 2: Sliding Window

**Use Case**: Subarray problems with fixed or variable size

```python
# Maximum sum subarray of size k
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Time: O(n), Space: O(1)
```

### Technique 3: Prefix Sum

**Use Case**: Range sum queries, subarray sums

```python
# Build prefix sum array
def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    return prefix

# Query sum from index l to r (inclusive)
def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]

# Build: O(n), Query: O(1)
```

### Technique 4: Kadane's Algorithm

**Use Case**: Maximum sum contiguous subarray

```python
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Time: O(n), Space: O(1)
```

**The "AHA" Moment** 💡:
> At each position, either start fresh or extend the previous subarray

### Technique 5: Dutch National Flag (3-Way Partitioning)

**Use Case**: Sorting array with 3 distinct values

```python
def dutch_national_flag(arr):
    low = mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    return arr

# Time: O(n), Space: O(1)
```

---

## 2.6 Strings

### String Fundamentals

**Definition**: A string is an array of characters ending with a null character '\0' in C/C++.

```c
char str[6] = "Hello";
// Memory: ['H']['e']['l']['l']['o']['\0']
//           0    1    2    3    4    5
```

### String Length Calculation

```c
int strlen(char *s) {
    int len = 0;
    while (s[len] != '\0') {
        len++;
    }
    return len;
}
// Time: O(n), Space: O(1)
```

### String Operations Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Length | O(n) |
| Concatenation | O(n + m) |
| Comparison | O(min(n, m)) |
| Substring | O(k) where k is substring length |
| Search (naive) | O(n × m) |
| Search (KMP) | O(n + m) |

---

## 2.7 String Pattern Matching

### Naive Pattern Matching

```python
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    positions = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    
    return positions

# Time: O((n-m+1) × m) = O(nm) worst case
```

### KMP (Knuth-Morris-Pratt) Algorithm

**The "AHA" Moment** 💡:
> Don't re-compare characters you already know match!

**Step 1: Build LPS (Longest Proper Prefix Suffix) Array**

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps
```

**Step 2: Pattern Search Using LPS**

```python
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    i = j = 0  # i for text, j for pattern
    positions = []
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions

# Time: O(n + m), Space: O(m)
```

### Rabin-Karp Algorithm (Hashing-Based)

```python
def rabin_karp(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    h = pow(d, m - 1) % q
    p = t = 0  # hash values
    positions = []
    
    # Calculate hash for pattern and first window
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p == t:  # Hash match
            # Verify character by character
            if text[i:i+m] == pattern:
                positions.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    
    return positions

# Average: O(n + m), Worst: O(nm)
```

---

## 2.8 Important String Problems

### 1. Check Anagram

```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = [0] * 256  # ASCII characters
    
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    
    return all(c == 0 for c in count)

# Time: O(n), Space: O(1) - constant 256 array
```

### 2. Check Palindrome

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Time: O(n), Space: O(1)
```

### 3. Longest Palindromic Substring

```python
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length
        len2 = expand_around_center(i, i + 1)  # Even length
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

# Time: O(n²), Space: O(1)
```

---

## 2.9 Edge Cases & Traps

### Common Edge Cases

| Case | Example | Watch For |
|------|---------|-----------|
| Empty array | arr = [] | Index out of bounds |
| Single element | arr = [5] | Off-by-one errors |
| All same elements | arr = [7,7,7,7] | Duplicate handling |
| Negative numbers | arr = [-1,-2,-3] | Sum/product problems |
| Large numbers | Integer overflow | Use long/BigInteger |
| Non-zero indexing | A[2:10] | Adjust base formula |

### GATE Trap Alert ⚠️

**Trap 1: String Length vs Array Size**
```c
char str[] = "Hello";
sizeof(str) = 6  // Includes '\0'
strlen(str) = 5  // Excludes '\0'
```

**Trap 2: Pointer vs Array**
```c
char str1[] = "Hello";  // Array - can modify
char *str2 = "Hello";   // Pointer to literal - read-only!
```

**Trap 3: 2D Array Parameter Passing**
```c
void func(int arr[][10], int rows);  // Column size required!
// OR
void func(int (*arr)[10], int rows); // Pointer to array of 10 ints
```

---

## 2.10 Comparison: Array vs Linked List

| Aspect | Array | Linked List |
|--------|-------|-------------|
| Memory | Contiguous | Non-contiguous |
| Access | O(1) random | O(n) sequential |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1) amortized | O(n) or O(1)* |
| Insert at middle | O(n) | O(n) find + O(1) insert |
| Memory overhead | None | Pointer per node |
| Cache performance | Excellent | Poor |
| Size | Fixed (static) | Dynamic |

*O(1) if tail pointer maintained

---

## 📝 GATE Practice Problems

**Q1**: An array A[1:10][1:15] requires 4 bytes per element. If base address is 2000, find address of A[5][10] using:
- (a) Row-major order
- (b) Column-major order

**Q2**: What is the time complexity of finding the second largest element in an unsorted array of n elements?

**Q3**: Given an array of n integers, find the length of longest increasing subsequence (not necessarily contiguous).

**Q4**: A string pattern P of length m is searched in text T of length n using KMP. What is the time complexity?

---

## 🎯 Quick Reference: Array Tricks

| Problem Type | Technique | Time |
|--------------|-----------|------|
| Find pair with sum | Two Pointers (sorted) | O(n) |
| Max subarray sum | Kadane's Algorithm | O(n) |
| Range sum queries | Prefix Sum | O(1) query |
| Fixed-size subarray | Sliding Window | O(n) |
| Sort 0,1,2 | Dutch National Flag | O(n) |
| Pattern matching | KMP | O(n+m) |
| Check duplicates | Hashing | O(n) |
| Find majority | Boyer-Moore Voting | O(n) |

---

## 🔑 Key Takeaways

1. **Arrays provide O(1) access** - the fundamental advantage
2. **Address calculation** is a GATE favorite - master the formulas
3. **Row-major vs Column-major** - know when each is used
4. **Two pointers and sliding window** - solve 50% of array problems
5. **Strings are character arrays** - same principles apply
6. **KMP algorithm** - O(n+m) pattern matching is exam critical

---

*Next: [Linked Lists →](03-Linked-Lists.md)*
