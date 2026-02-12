# Chapter 12: Amortized Analysis

## 12.1 What is Amortized Analysis?

> **Analogy:** Imagine you put money in a piggy bank every day. Some days you withdraw a large amount. If someone sees only the withdrawal day, they think you're spending a lot. But **amortized** over many days, your average spending is low. Amortized analysis gives a **more accurate average** cost per operation in a sequence.

**Key idea:** Instead of analyzing the worst-case cost of a **single operation**, analyze the **average cost per operation** over a **sequence of operations**.

**Important:** This is NOT average-case analysis (which uses probability). Amortized analysis is a **worst-case guarantee** for the total cost of a sequence.

---

## 12.2 Three Methods of Amortized Analysis

### Method 1: Aggregate Method

**Idea:** Compute the total cost of n operations, then divide by n.

**amortized cost = T(n) / n**

**Example: Stack with Multipop**

Stack supports:
- PUSH(x) — cost 1
- POP() — cost 1
- MULTIPOP(k) — pop min(k, stack_size) elements, cost = min(k, stack_size)

**Worst case of MULTIPOP:** O(n) if stack has n elements.

**But amortized?** In n operations:
- Each element is pushed at most once → at most n pushes (total cost n)
- Each element can be popped at most once → total pops ≤ n
- Total cost of n operations ≤ 2n

**Amortized cost per operation = 2n/n = O(1)** ✓

---

### Method 2: Accounting Method (Banker's Method)

**Idea:** Charge each operation an **amortized cost**. If the amortized cost exceeds the actual cost, the difference is stored as **credit** on the data structure. Later, expensive operations use this credit.

**Rule:** Total amortized cost ≥ Total actual cost (credit never goes negative)

**Example: Stack with Multipop**

| Operation | Actual Cost | Amortized Cost | Credit Change |
|-----------|------------|----------------|---------------|
| PUSH | 1 | **2** | +1 per element |
| POP | 1 | 0 | -1 (use element's credit) |
| MULTIPOP(k) | k | 0 | -k (use elements' credits) |

Each PUSH pays 1 for itself + 1 as "prepayment" for a future POP/MULTIPOP.

Total amortized cost of n operations = at most 2n → **amortized O(1) per operation**.

> **Why this works:** We're "overcharging" cheap operations to "subsidize" expensive ones.

---

### Method 3: Potential Method (Physicist's Method)

**Idea:** Define a **potential function** Φ that maps the state of the data structure to a number. The amortized cost is:

```
ĉᵢ = cᵢ + Φ(Dᵢ) - Φ(Dᵢ₋₁)
```

where cᵢ is the actual cost, Dᵢ is the state after operation i.

**Requirements:**
- Φ(D₀) = 0 (initial potential)
- Φ(Dᵢ) ≥ 0 for all i (potential never negative)

**Total amortized cost = Σĉᵢ = Σcᵢ + Φ(Dₙ) - Φ(D₀) ≥ Σcᵢ**

**Example: Stack with Multipop**

Let Φ = number of elements in the stack.

| Operation | Actual Cost cᵢ | ΔΦ | Amortized ĉᵢ |
|-----------|---------------|-----|---------------|
| PUSH | 1 | +1 | 1 + 1 = **2** |
| POP | 1 | -1 | 1 - 1 = **0** |
| MULTIPOP(k) | k | -k | k - k = **0** |

Amortized cost per operation = **O(1)** ✓

---

## 12.3 Classic Example: Dynamic Array (Amortized Doubling) ⭐

**Scenario:** An array that doubles in size when full.

| Operation | Actual Cost |
|-----------|------------|
| INSERT (no resize) | O(1) |
| INSERT (with resize) | O(n) — copy all n elements |

**Is INSERT O(n) or O(1)?**

### Aggregate Analysis

For n insertions:
- Resize happens at sizes 1, 2, 4, 8, ..., 2ᵏ where 2ᵏ ≤ n
- Total resize cost = 1 + 2 + 4 + ... + 2ᵏ < 2n

Total cost = n (for insertions) + 2n (for all resizes) = 3n

**Amortized cost per INSERT = 3n/n = O(1)** ✓

### Accounting Analysis

Charge each INSERT **3 units:**
- 1 for the insertion itself
- 1 prepaid for copying THIS element in a future resize
- 1 prepaid for copying an OLD element that didn't pay for itself

### Potential Analysis

Let Φ = 2 × (number of elements) - (capacity of array)

After resize: array is half full, so Φ = 2(n/2) - n = 0  
Just before resize: array is full, so Φ = 2n - n = n

INSERT without resize: cᵢ = 1, ΔΦ = 2, ĉᵢ = 3  
INSERT with resize from capacity n to 2n: cᵢ = n+1, ΔΦ = 2-(2n-n) = 2-n, ĉᵢ = n+1+2-n = **3**

**Amortized cost = O(1)** in all cases ✓

> **GATE Application:** This is why `ArrayList` in Java / `vector` in C++ / `list` in Python have O(1) amortized append, despite occasional O(n) resizing.

---

## 12.4 Amortized Analysis of Union-Find

With **union by rank** and **path compression:**

| Per operation | Actual worst case | Amortized |
|--------------|-------------------|-----------|
| FIND | O(log n) | **O(α(n))** |
| UNION | O(log n) | **O(α(n))** |

where α(n) is the **inverse Ackermann function** — grows so slowly that α(n) ≤ 4 for any practical n (up to ~10⁸⁰).

> **GATE Fact:** For all practical purposes, Union-Find operations are **O(1) amortized**.

---

## 12.5 Amortized Analysis of Splay Trees

A splay tree guarantees that any sequence of m operations on a tree with n nodes takes **O(m log n)** total time.

**Amortized cost per operation: O(log n)**

Even though individual operations can take O(n), the splay operation ensures frequently accessed elements move to the root, amortizing the cost.

> **GATE Fact:** Splay trees have O(log n) amortized time for search, insert, and delete, but O(n) worst case for a single operation.

---

## 12.6 When to Use Which Method

| Method | Best When | Difficulty |
|--------|-----------|-----------|
| Aggregate | Total cost is easy to bound directly | Easiest |
| Accounting | Different operations have clearly different costs | Medium |
| Potential | Need a precise mathematical proof | Hardest |

> **GATE Tip:** For GATE questions, the aggregate method usually suffices. Potential method is needed for rigorous proofs (rarely asked in detail).

---


---
