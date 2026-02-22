# Chapter 5: Divide and Conquer

## 5.1 The Paradigm

> **Analogy:** Like a general breaking an army into smaller units, conquering each, then uniting them. You break a big problem into smaller identical subproblems, solve them independently, and combine the solutions.

**Three Steps:**
1. **Divide:** Break the problem into smaller subproblems of the same type
2. **Conquer:** Solve each subproblem recursively (base case: small enough to solve directly)
3. **Combine:** Merge the solutions of subproblems into the solution for the original problem

**General Recurrence:** T(n) = aT(n/b) + f(n)
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost of dividing and combining

---

## 5.2 Classic D&C Algorithms (Already Covered)

| Algorithm | Recurrence | Complexity |
|-----------|-----------|------------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort | T(n) = T(k) + T(n-k-1) + O(n) | O(n log n) avg |

---

## 5.3 Maximum Subarray Problem (Kadane's is better, but D&C is classic)

**Problem:** Find contiguous subarray with maximum sum.

**D&C Approach:**
1. Divide array into left and right halves
2. Maximum subarray is either:
   - Entirely in left half
   - Entirely in right half
   - **Crossing the midpoint** (key insight)
3. Find max crossing subarray in O(n)

```
MaxCrossing(A, low, mid, high):
    // Find max sum going left from mid
    leftSum = -∞, sum = 0
    for i = mid downto low:
        sum += A[i]
        if sum > leftSum: leftSum = sum
    // Find max sum going right from mid
    rightSum = -∞, sum = 0
    for j = mid+1 to high:
        sum += A[j]
        if sum > rightSum: rightSum = sum
    return leftSum + rightSum

MaxSubarray(A, low, high):
    if low == high: return A[low]
    mid = (low + high) / 2
    leftMax = MaxSubarray(A, low, mid)
    rightMax = MaxSubarray(A, mid+1, high)
    crossMax = MaxCrossing(A, low, mid, high)
    return max(leftMax, rightMax, crossMax)
```

**Time:** T(n) = 2T(n/2) + O(n) → **O(n log n)**

> **Note:** Kadane's algorithm solves this in O(n) using DP. But the D&C version is a classic GATE question.

---

## 5.4 Strassen's Matrix Multiplication

### Standard Matrix Multiplication

To multiply two n×n matrices: C = A × B

```
for i = 1 to n:
    for j = 1 to n:
        C[i][j] = 0
        for k = 1 to n:
            C[i][j] += A[i][k] * B[k][j]
```

**Time:** O(n³) — three nested loops.

### Strassen's Approach (1969)

**Key Idea:** Reduce the number of multiplications from 8 to 7 by using clever addition/subtraction.

**Standard D&C:**
Split each n×n matrix into four (n/2)×(n/2) submatrices:

```
A = | A₁₁  A₁₂ |    B = | B₁₁  B₁₂ |
    | A₂₁  A₂₂ |        | B₂₁  B₂₂ |

C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂
C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁
C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂
```

This needs **8 multiplications** → T(n) = 8T(n/2) + O(n²) → **O(n³)** (no improvement!)

**Strassen's 7 multiplications:**

```
M₁ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
M₂ = (A₂₁ + A₂₂)B₁₁
M₃ = A₁₁(B₁₂ - B₂₂)
M₄ = A₂₂(B₂₁ - B₁₁)
M₅ = (A₁₁ + A₁₂)B₂₂
M₆ = (A₂₁ - A₁₁)(B₁₁ + B₁₂)
M₇ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)

C₁₁ = M₁ + M₄ - M₅ + M₇
C₁₂ = M₃ + M₅
C₂₁ = M₂ + M₄
C₂₂ = M₁ - M₂ + M₃ + M₆
```

**Recurrence:** T(n) = 7T(n/2) + O(n²)

By Master Theorem: a=7, b=2, n^(log₂7) = n^2.807

Case 1: f(n) = O(n²) = O(n^(2.807-ε)) → **T(n) = Θ(n^log₂7) ≈ Θ(n^2.807)**

> **GATE Facts:**
> - Strassen's: O(n^2.807) vs standard O(n³)
> - Best known: O(n^2.3729) [Alman & Williams, 2024]
> - Lower bound: Ω(n²) (must read all elements)
> - In practice, Strassen's only helps for very large matrices

---

## 5.5 Karatsuba Multiplication (Fast Integer Multiplication)

### Standard Multiplication

Multiplying two n-digit numbers: O(n²) — multiply each digit pair.

### Karatsuba's Trick

Split each n-digit number into two halves:
```
x = xH · 10^(n/2) + xL
y = yH · 10^(n/2) + yL

x · y = xH·yH · 10ⁿ + (xH·yL + xL·yH) · 10^(n/2) + xL·yL
```

This needs 4 multiplications. Karatsuba's insight:

```
P₁ = xH · yH
P₂ = xL · yL
P₃ = (xH + xL) · (yH + yL)

x · y = P₁ · 10ⁿ + (P₃ - P₁ - P₂) · 10^(n/2) + P₂
```

**Only 3 multiplications!** (P₃ - P₁ - P₂ = xH·yL + xL·yH)

**Recurrence:** T(n) = 3T(n/2) + O(n) → **O(n^log₂3) ≈ O(n^1.585)**

> **How the trick works:** Instead of computing xH·yL and xL·yH separately, compute (xH+xL)(yH+yL) = xH·yH + xH·yL + xL·yH + xL·yL, then subtract the already-computed xH·yH and xL·yL.

---

## 5.6 Closest Pair of Points

**Problem:** Given n points in 2D, find the pair with minimum distance.

**Brute force:** Check all pairs → O(n²)

**D&C Approach:**
1. Sort points by x-coordinate
2. Divide into left and right halves by a vertical line
3. Recursively find closest pair in each half (δL, δR)
4. Let δ = min(δL, δR)
5. **Key Step:** Check points in a strip of width 2δ around the dividing line
6. For each point in strip, check at most **6-7 other points** (geometrically proven)

**Recurrence:** T(n) = 2T(n/2) + O(n) → **O(n log n)**

> **GATE Fact:** The strip checking step is O(n), not O(n²), because each point needs to be compared with at most O(1) other points in the strip (at most 6 for L∞ metric, 7 for L₂).

> **Why only 6-7 comparisons?** In a δ×2δ rectangle, at most 8 points can fit with pairwise distance ≥ δ (pigeon-hole argument on a grid).

---

## 5.7 Finding Median in O(n) — Median of Medians (SELECT)

**Problem:** Find the k-th smallest element in an unsorted array.

**Naive:** Sort, then return A[k] → O(n log n)

**Quick Select (randomized):** Average O(n), worst O(n²)

**Median of Medians (deterministic):**

```
SELECT(A, k):
    1. Divide A into groups of 5
    2. Find median of each group (O(n))
    3. Recursively find median of medians (T(n/5))
    4. Use this as pivot to partition
    5. Recurse on the appropriate side (T(7n/10))
```

**Recurrence:** T(n) = T(n/5) + T(7n/10) + O(n)

**Why 7n/10?** The median of medians is guaranteed to be ≥ 30% of elements and ≤ 30% of elements. So the worst case recursion is on at most 70% = 7n/10 elements.

**Proof that T(n) = O(n):**  
Guess T(n) ≤ cn. Then: T(n) ≤ cn/5 + 7cn/10 + an = cn(1/5 + 7/10) + an = cn(9/10) + an ≤ cn when c ≥ 10a.

> **GATE Fact:** k-th smallest element can be found in **O(n) worst case** using Median of Medians. Groups of 5 is not arbitrary — groups of 3 don't work (check: 1/3 + 2n/3 ≥ n).

---


---
