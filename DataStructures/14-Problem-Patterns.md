# Chapter 14: Problem-Solving Patterns

## 🎯 The Atomic Truth
> **"Patterns = Recognizable Solutions for Similar Problems"**

---

## 14.1 Two Pointers

### When to Use
- Sorted array/linked list
- Finding pairs with specific property
- Partitioning

### Pattern 1: Opposite Direction

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    
    return None
```

### Pattern 2: Same Direction (Fast/Slow)

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1
```

### Common Problems
- Container with most water
- 3Sum, 4Sum
- Remove duplicates
- Trapping rain water
- Palindrome check

---

## 14.2 Sliding Window

### When to Use
- Contiguous subarray/substring
- Fixed or variable window size
- Optimization within window

### Pattern: Variable Window

```python
def longest_substring_k_distinct(s, k):
    char_count = {}
    left = max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Pattern: Fixed Window

```python
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Common Problems
- Maximum sum subarray of size K
- Longest substring without repeating
- Minimum window substring
- Fruits into baskets

---

## 14.3 Binary Search Pattern

### When to Use
- Sorted data
- Monotonic property
- Optimization problems

### Template

```python
def binary_search_condition(arr, condition):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if condition(mid):
            # Found valid, but search for better
            right = mid - 1  # or left = mid + 1
        else:
            left = mid + 1   # or right = mid - 1
    
    return left  # or right, depending on what we need
```

### Common Problems
- Search in rotated array
- Find peak element
- Median of two sorted arrays
- Capacity to ship packages

---

## 14.4 DFS/BFS Patterns

### DFS Template (Recursion)

```python
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    # Process node
    
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### BFS Template

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}
    level = 0
    
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            # Process node
            
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1
    
    return level
```

### When to Use What

| Use BFS | Use DFS |
|---------|---------|
| Shortest path | Explore all paths |
| Level by level | Deep exploration |
| Nearest neighbor | Cycle detection |
| Min moves | Topological sort |

---

## 14.5 Backtracking

### When to Use
- All possible solutions
- Combinations/permutations
- Constraint satisfaction

### Template

```python
def backtrack(current_state, choices):
    if is_solution(current_state):
        add_to_results(current_state)
        return
    
    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            backtrack(current_state, remaining_choices)
            undo_choice(choice)  # Backtrack
```

### Example: Subsets

```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

### Common Problems
- N-Queens
- Sudoku solver
- Permutations
- Combination sum

---

## 14.6 Dynamic Programming

### When to Use
- Optimal substructure
- Overlapping subproblems
- Counting/optimization

### Steps
1. Define state
2. Find recurrence
3. Base cases
4. Compute order
5. Optimize space (if possible)

### Template: Top-Down (Memoization)

```python
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    if n == base_case:
        return base_value
    
    memo[n] = recurrence(solve(n-1), solve(n-2), ...)
    return memo[n]
```

### Template: Bottom-Up (Tabulation)

```python
def solve(n):
    dp = [0] * (n + 1)
    dp[base] = base_value
    
    for i in range(1, n + 1):
        dp[i] = recurrence(dp[i-1], dp[i-2], ...)
    
    return dp[n]
```

### Common Patterns

| Pattern | Examples |
|---------|----------|
| Linear | Fibonacci, Climbing stairs |
| 2D Grid | Unique paths, Edit distance |
| Knapsack | 0/1 Knapsack, Subset sum |
| Interval | Matrix chain, Burst balloons |
| Subsequence | LCS, LIS |

---

## 14.7 Greedy

### When to Use
- Local optimal leads to global optimal
- Usually involves sorting

### Characteristics
- Make best choice at each step
- No backtracking
- Prove correctness (exchange argument)

### Common Problems
- Activity selection
- Huffman coding
- Fractional knapsack
- Job scheduling

### Example: Activity Selection

```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected
```

---

## 14.8 Divide and Conquer

### When to Use
- Problem can be broken into independent subproblems
- Same type of problem at smaller scale

### Template

```python
def divide_and_conquer(problem):
    if is_base_case(problem):
        return solve_directly(problem)
    
    left, right = divide(problem)
    
    left_result = divide_and_conquer(left)
    right_result = divide_and_conquer(right)
    
    return combine(left_result, right_result)
```

### Common Problems
- Merge sort
- Quick sort
- Binary search
- Maximum subarray (Kadane can be O(n))
- Closest pair of points

---

## 14.9 Stack-Based Patterns

### Monotonic Stack

```python
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result
```

### Common Problems
- Next greater element
- Largest rectangle in histogram
- Trapping rain water
- Valid parentheses

---

## 14.10 Heap-Based Patterns

### Top K Pattern

```python
import heapq

def top_k_frequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### Two Heaps Pattern (Median)

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap
    
    def add(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
```

---

## 14.11 Quick Pattern Selection Guide

| Problem Characteristic | Pattern |
|----------------------|---------|
| Sorted array, find pair | Two Pointers |
| Contiguous subarray | Sliding Window |
| Find in sorted | Binary Search |
| Graph traversal | BFS/DFS |
| All combinations | Backtracking |
| Optimal substructure | DP |
| Local → Global optimal | Greedy |
| Split and combine | Divide & Conquer |
| Previous elements matter | Stack |
| Top/Min/Max K elements | Heap |
| String prefix | Trie |
| Range queries | Segment Tree |
| Disjoint sets | Union-Find |

---

## 14.12 Complexity Quick Reference

| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(k) |
| Binary Search | O(log n) | O(1) |
| BFS/DFS | O(V+E) | O(V) |
| Backtracking | O(2ⁿ) or O(n!) | O(n) |
| DP | O(n²) typical | O(n) or O(n²) |
| Greedy | O(n log n) | O(1) |
| Divide & Conquer | O(n log n) | O(log n) |

---

## 📝 Practice Strategy

### Level 1: Master Basic Patterns
1. Two Pointers (20 problems)
2. Sliding Window (15 problems)
3. Binary Search (20 problems)

### Level 2: Graph & Tree
1. BFS/DFS (25 problems)
2. Tree traversals (15 problems)
3. Backtracking (15 problems)

### Level 3: Optimization
1. Dynamic Programming (30 problems)
2. Greedy (15 problems)
3. Advanced DS (20 problems)

---

## 🔑 Key Takeaways

1. **Recognize the pattern first**, then implement
2. **Most problems are variations** of standard patterns
3. **Practice pattern recognition** more than coding
4. **Start with brute force**, then optimize
5. **Analyze constraints** to choose appropriate algorithm
6. **Time complexity hints** at which pattern to use

---

*Next: [Previous Year Questions Analysis →](15-PYQ-Analysis.md)*
