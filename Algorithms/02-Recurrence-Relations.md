# Chapter 2: Recurrence Relations

## 2.1 What is a Recurrence Relation?

> **Analogy:** Imagine stacking Russian dolls. To know how many dolls are in the largest one, you need to open it and count the one inside, which itself contains another... A recurrence is like this — the answer for size n depends on the answer for a smaller size.

A **recurrence relation** defines a function T(n) in terms of T on smaller values. They naturally arise from **recursive algorithms**.

**Example:**  
```
T(n) = 2T(n/2) + n     [Merge Sort]
T(1) = 1               [Base case]
```
This says: "To sort n elements, we sort two halves (each takes T(n/2)) and merge them (takes n)."

---

## 2.2 Methods to Solve Recurrences

### Method 1: Substitution Method (Guess & Prove)

**Steps:**
1. **Guess** the form of the solution
2. **Prove** by mathematical induction
3. **Find constants** that work

**Example: T(n) = 2T(n/2) + n**

**Guess:** T(n) = O(n log n), so assume T(n) ≤ cn log n for some c > 0.

**Inductive Step:** Assume T(k) ≤ ck log k for all k < n.

```
T(n) = 2T(n/2) + n
     ≤ 2 · c(n/2)log(n/2) + n
     = cn(log n - log 2) + n
     = cn·log n - cn + n
     = cn·log n - (c-1)n
     ≤ cn·log n          [holds when c ≥ 1]
```

So T(n) = O(n log n) with c = 1. ✓

> **GATE Tip:** Substitution is powerful but requires a good initial guess. Use the recursion tree or Master Theorem to guess, then verify with substitution.

> **Common Trap:** Don't forget to verify the base case! A proof by induction requires both the inductive step AND the base case.

---

### Method 2: Recursion Tree Method

**Idea:** Expand the recurrence into a tree, where each node represents the cost at that level. Sum all levels to get the total.

**Example: T(n) = 2T(n/2) + n**

```
Level 0:                    n                      → Cost = n
                          /   \
Level 1:              n/2       n/2                 → Cost = 2 × n/2 = n
                     /   \     /   \
Level 2:          n/4   n/4  n/4   n/4              → Cost = 4 × n/4 = n
                  ...   ...  ...   ...
Level k:        n/2ᵏ  (repeated 2ᵏ times)          → Cost = 2ᵏ × n/2ᵏ = n
```

**Number of levels:** Tree bottoms out when n/2ᵏ = 1 → k = log₂ n

**Total cost:** n × (number of levels) = n × log₂ n = **Θ(n log n)**

**Example: T(n) = 3T(n/4) + cn²**

```
Level 0:           cn²                              → Cost = cn²
Level 1:     3 × c(n/4)²  = (3/16)cn²              → Cost = (3/16)cn²
Level 2:     9 × c(n/16)² = (3/16)²cn²             → Cost = (3/16)²cn²
...
Level k:     3ᵏ × c(n/4ᵏ)² = (3/16)ᵏ cn²
```

**Number of levels:** n/4ᵏ = 1 → k = log₄ n

**Total = cn² × Σ(i=0 to log₄n) (3/16)ⁱ**

Since 3/16 < 1, this is a **decreasing geometric series** → converges to cn² × 1/(1 - 3/16) = cn² × 16/13

**T(n) = Θ(n²)** — the root dominates!

> **Insight:** In a recursion tree:
> - If cost **decreases** geometrically → root dominates → T(n) = Θ(f(n))
> - If cost is **same** at each level → all levels matter → T(n) = Θ(f(n) · log n)
> - If cost **increases** geometrically → leaves dominate → T(n) = Θ(n^(log_b(a)))

---

### Method 3: Master Theorem ⭐ (Most Important for GATE)

**For recurrences of the form:**
```
T(n) = aT(n/b) + f(n)
```
where a ≥ 1, b > 1, and f(n) is asymptotically positive.

**Compare f(n) with n^(log_b(a)):**

| Case | Condition | Result |
|------|-----------|--------|
| **Case 1** | f(n) = O(n^(log_b(a) - ε)) for some ε > 0 | T(n) = Θ(n^(log_b(a))) |
| **Case 2** | f(n) = Θ(n^(log_b(a)) · logᵏ n) for k ≥ 0 | T(n) = Θ(n^(log_b(a)) · logᵏ⁺¹ n) |
| **Case 3** | f(n) = Ω(n^(log_b(a) + ε)) for some ε > 0 AND a·f(n/b) ≤ c·f(n) for c < 1 | T(n) = Θ(f(n)) |

#### How the Master Theorem Works — The Intuition

Think of a **battle between root work and leaf work:**

- **n^(log_b(a))** = total work done by ALL leaves (there are a^(log_b(n)) = n^(log_b(a)) leaves)
- **f(n)** = work done at the root level

| Who wins? | Result |
|-----------|--------|
| **Leaves win** (f is polynomially smaller) → Case 1 | Leaf cost dominates |
| **Tie** (same polynomial growth) → Case 2 | Both contribute, extra log factor |
| **Root wins** (f is polynomially larger) → Case 3 | Root cost dominates |

#### Detailed Examples

**Example 1: T(n) = 9T(n/3) + n**
- a = 9, b = 3, f(n) = n
- n^(log₃9) = n^2
- Compare: f(n) = n vs n² → n = O(n^(2-1)) → ε = 1
- **Case 1:** T(n) = Θ(n²)

**Example 2: T(n) = 2T(n/2) + n**
- a = 2, b = 2, f(n) = n
- n^(log₂2) = n^1 = n
- Compare: f(n) = n = Θ(n^1 · log⁰n) → k = 0
- **Case 2:** T(n) = Θ(n · log n)

**Example 3: T(n) = 3T(n/4) + n·log n**
- a = 3, b = 4, f(n) = n·log n
- n^(log₄3) = n^0.793
- Compare: f(n) = n·log n = Ω(n^(0.793 + ε)) → ε ≈ 0.2
- Check regularity: 3·(n/4)·log(n/4) ≤ c·n·log n → (3/4)·n·log(n/4) ≤ c·n·log n ✓ for c = 3/4
- **Case 3:** T(n) = Θ(n log n)

**Example 4: T(n) = 2T(n/2) + n·log n**
- a = 2, b = 2, f(n) = n·log n
- n^(log₂2) = n
- Compare: f(n) = n·log n = Θ(n¹ · log¹ n) → k = 1
- **Case 2 (extended):** T(n) = Θ(n · log² n)

#### When Master Theorem FAILS

The Master Theorem does **NOT** apply when:

1. **f(n) is not polynomially different** from n^(log_b(a))
   - Example: T(n) = 2T(n/2) + n/log n → Gap is only logarithmic, not polynomial

2. **a < 1** — Master theorem requires a ≥ 1

3. **Non-uniform subproblems** — T(n) = T(n/3) + T(2n/3) + n (different sized subproblems)

4. **f(n) is not asymptotically positive**

> **GATE Trick for Quick Application:**
> 1. Compute `log_b(a)` (call it p)
> 2. Compare f(n) with n^p:
>    - f(n) is "smaller" → Θ(n^p)
>    - f(n) is "equal" (within log factors) → Θ(n^p · log^(k+1) n)
>    - f(n) is "bigger" → Θ(f(n))

---

### Method 4: Extended Master Theorem (for log factors)

For T(n) = aT(n/b) + Θ(nᵏ logᵖ n):

| Condition | Result |
|-----------|--------|
| a > bᵏ | Θ(n^(log_b(a))) |
| a = bᵏ and p > -1 | Θ(nᵏ logᵖ⁺¹ n) |
| a = bᵏ and p = -1 | Θ(nᵏ log log n) |
| a = bᵏ and p < -1 | Θ(nᵏ) |
| a < bᵏ | Θ(nᵏ logᵖ n) |

---

### Method 5: Special Recurrences (Must Memorize for GATE)

| Recurrence | Solution | Algorithm |
|------------|----------|-----------|
| T(n) = T(n-1) + 1 | Θ(n) | Linear traversal |
| T(n) = T(n-1) + n | Θ(n²) | Selection sort inner |
| T(n) = T(n-1) + log n | Θ(n log n) | — |
| T(n) = 2T(n-1) + 1 | Θ(2ⁿ) | Tower of Hanoi |
| T(n) = 2T(n/2) + n | Θ(n log n) | Merge sort |
| T(n) = 2T(n/2) + 1 | Θ(n) | Binary tree traversal |
| T(n) = T(n/2) + 1 | Θ(log n) | Binary search |
| T(n) = T(n/2) + n | Θ(n) | — |
| T(n) = 2T(n/2) + n² | Θ(n²) | — |
| T(n) = T(√n) + 1 | Θ(log log n) | — |
| T(n) = 2T(√n) + log n | Θ(log n · log log n) | — |

#### How to Solve T(n) = T(√n) + 1

**Substitution:** Let n = 2ᵐ, then T(2ᵐ) = T(2^(m/2)) + 1

Let S(m) = T(2ᵐ): S(m) = S(m/2) + 1

By Master Theorem: S(m) = Θ(log m)

Back-substitute: m = log n → T(n) = Θ(log log n) ✓

> **GATE Trick:** For T(n) = T(√n) + ..., substitute n = 2ᵐ to convert to a standard form.

---

## 2.3 Solving Linear Recurrences (Characteristic Equation Method)

For **linear homogeneous** recurrences like T(n) = c₁T(n-1) + c₂T(n-2):

1. Write **characteristic equation:** x² = c₁x + c₂ → x² - c₁x - c₂ = 0
2. Find roots r₁, r₂
3. General solution:
   - **Distinct roots:** T(n) = A·r₁ⁿ + B·r₂ⁿ
   - **Repeated root r:** T(n) = (A + Bn)·rⁿ

**Example: Fibonacci — T(n) = T(n-1) + T(n-2)**

Characteristic equation: x² - x - 1 = 0  
Roots: r₁ = (1+√5)/2 = φ ≈ 1.618, r₂ = (1-√5)/2 ≈ -0.618

T(n) = A·φⁿ + B·((1-√5)/2)ⁿ

Since |r₂| < 1, the second term → 0, so **T(n) = Θ(φⁿ) ≈ Θ(1.618ⁿ)**

> **GATE Result:** The n-th Fibonacci number grows as Θ(φⁿ) where φ = (1+√5)/2 ≈ 1.618 (Golden Ratio).

---


