# Chapter 19: Set Theory & Venn Diagrams

> **The foundation of modern mathematics - organizing and analyzing collections**

---

## 🎯 Why Study This?

- Foundation for logic and discrete mathematics
- Essential for GATE/ESE problem solving
- Venn diagrams are powerful visualization tools

---

## 📚 Part 1: Set Theory Basics

### Definitions

**Set**: A well-defined collection of distinct objects (elements)

**Notation**:
```
A = {1, 2, 3, 4, 5}  (Roster form)
A = {x : x is a natural number, x ≤ 5}  (Set-builder form)
```

**Element**: x ∈ A (x belongs to A), x ∉ A (x doesn't belong to A)

---

### Types of Sets

| Type | Definition | Example |
|------|------------|---------|
| **Empty Set** | No elements | ∅ or {} |
| **Singleton** | Exactly one element | {5} |
| **Finite** | Countable elements | {1, 2, 3} |
| **Infinite** | Uncountable elements | {1, 2, 3, ...} |
| **Universal Set** | Contains all elements under consideration | U |
| **Subset** | All elements of A are in B | A ⊆ B |
| **Proper Subset** | A ⊆ B and A ≠ B | A ⊂ B |
| **Power Set** | Set of all subsets | P(A) |

---

### Important Number Sets

```
N = {1, 2, 3, ...}      Natural numbers
Z = {..., -2, -1, 0, 1, 2, ...}  Integers
Q = {p/q : p, q ∈ Z, q ≠ 0}     Rational numbers
R = All real numbers
```

---

### Power Set

The set of all subsets of A:
```
|P(A)| = 2ⁿ  where n = |A|
```

**Example**: A = {1, 2}
```
P(A) = {∅, {1}, {2}, {1,2}}
|P(A)| = 2² = 4
```

---

## 📐 Set Operations

### Union (A ∪ B)

Elements in A OR B (or both):
```
A ∪ B = {x : x ∈ A or x ∈ B}
```

**Diagram**: All shaded areas combined

---

### Intersection (A ∩ B)

Elements in BOTH A AND B:
```
A ∩ B = {x : x ∈ A and x ∈ B}
```

**Diagram**: Only overlapping region

---

### Difference (A - B or A \ B)

Elements in A but NOT in B:
```
A - B = {x : x ∈ A and x ∉ B}
```

---

### Complement (A' or Aᶜ)

Elements NOT in A (but in universal set):
```
A' = {x : x ∈ U and x ∉ A}
A' = U - A
```

---

### Symmetric Difference (A Δ B)

Elements in A OR B but NOT both:
```
A Δ B = (A - B) ∪ (B - A) = (A ∪ B) - (A ∩ B)
```

---

## 🔗 Properties of Set Operations

### Commutative Laws
```
A ∪ B = B ∪ A
A ∩ B = B ∩ A
```

### Associative Laws
```
(A ∪ B) ∪ C = A ∪ (B ∪ C)
(A ∩ B) ∩ C = A ∩ (B ∩ C)
```

### Distributive Laws
```
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
```

### De Morgan's Laws
```
(A ∪ B)' = A' ∩ B'
(A ∩ B)' = A' ∪ B'
```

**💡 Mnemonic**: "Break the bar, change the sign"

### Identity Laws
```
A ∪ ∅ = A
A ∩ U = A
A ∪ U = U
A ∩ ∅ = ∅
```

### Complement Laws
```
A ∪ A' = U
A ∩ A' = ∅
(A')' = A
```

### Idempotent Laws
```
A ∪ A = A
A ∩ A = A
```

### Absorption Laws
```
A ∪ (A ∩ B) = A
A ∩ (A ∪ B) = A
```

---

## 📊 Cardinality Formulas

### Two Sets

```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Diagram Interpretation**:
```
Only A = |A| - |A ∩ B|
Only B = |B| - |A ∩ B|
Both = |A ∩ B|
Neither = |U| - |A ∪ B|
```

---

### Three Sets

```
|A ∪ B ∪ C| = |A| + |B| + |C| 
             - |A ∩ B| - |B ∩ C| - |A ∩ C| 
             + |A ∩ B ∩ C|
```

**7 Distinct Regions**:
```
1. Only A = |A| - |A∩B| - |A∩C| + |A∩B∩C|
2. Only B = |B| - |A∩B| - |B∩C| + |A∩B∩C|
3. Only C = |C| - |A∩C| - |B∩C| + |A∩B∩C|
4. Only A∩B = |A∩B| - |A∩B∩C|
5. Only B∩C = |B∩C| - |A∩B∩C|
6. Only A∩C = |A∩C| - |A∩B∩C|
7. A∩B∩C = |A∩B∩C|
8. None = |U| - |A∪B∪C|
```

---

## 📈 Venn Diagram Problem Solving

### Standard Approach

1. **Draw diagram** with appropriate circles
2. **Start from innermost region** (intersection of all sets)
3. **Work outward** to each region
4. **Use formulas** or fill in values systematically

---

### Example Problem

In a class of 100 students: 40 study Math, 30 study Physics, 20 study Chemistry, 10 study both Math & Physics, 8 study both Physics & Chemistry, 12 study both Math & Chemistry, 5 study all three.

**Find**: Students studying at least one subject.

```
|M ∪ P ∪ C| = 40 + 30 + 20 - 10 - 8 - 12 + 5 = 65
```

**Find**: Students studying only Math.
```
Only M = 40 - (10-5) - (12-5) - 5 = 40 - 5 - 7 - 5 = 23
```

---

## 💡 Advanced Tricks

### Trick 1: "At Least One" = Total - None

```
At least one = |A ∪ B| = Total - Neither
Neither = Total - |A ∪ B|
```

---

### Trick 2: "Exactly One" Category

```
Exactly one = Only A + Only B + Only C
            = |A∪B∪C| - |A∩B| - |B∩C| - |A∩C| + 2|A∩B∩C|
```

---

### Trick 3: Maximum and Minimum Values

**Maximum of |A ∩ B|** = min(|A|, |B|)
**Minimum of |A ∩ B|** = max(0, |A| + |B| - |U|)

**Maximum of |A ∪ B|** = min(|U|, |A| + |B|)
**Minimum of |A ∪ B|** = max(|A|, |B|)

---

### Trick 4: Complement Calculations

```
|A'| = |U| - |A|
|A - B| = |A| - |A ∩ B|
|A Δ B| = |A| + |B| - 2|A ∩ B|
```

---

### Trick 5: Survey Problems Pattern

Given: Total = T, A = a, B = b, Both = x, Neither = n
```
a + b - x + n = T
x = a + b + n - T
```

---

## 📊 Common Venn Diagram Types

### Two-Set Venn

```
    ┌───────────────────────────┐
    │           U               │
    │    ┌─────────────┐        │
    │    │      A      │        │
    │    │   ┌─────┐   │        │
    │    │   │ A∩B │   │        │
    │    │   └─────┘   │        │
    │    │      B      │        │
    │    └─────────────┘        │
    │                           │
    └───────────────────────────┘
```

**Regions**: Only A, Only B, A∩B, Neither

---

### Three-Set Venn

7 inner regions + 1 outer (neither)

---

## ⚠️ Edge Cases & Traps

### Trap 1: Don't Double Count
```
|A ∪ B| ≠ |A| + |B| (overlaps counted twice)
Must subtract |A ∩ B|
```

### Trap 2: "At Least" vs "Exactly"
```
At least two ≠ Exactly two
At least two = Exactly two + All three (for 3 sets)
```

### Trap 3: Empty Set Properties
```
∅ ⊆ A (for any A)
∅ ∈ P(A) (empty set is in power set)
|∅| = 0
|P(∅)| = 1 (only contains ∅)
```

### Trap 4: Set vs Element
```
{1} ≠ 1
{1} is a set, 1 is an element
{{1}} contains {1} as element
```

### Trap 5: Subset Symbol Direction
```
A ⊆ B means A is subset of B (A inside B)
A ⊇ B means A is superset of B (B inside A)
```

---

## 🚀 Formula Cheat Sheet

| Operation | Formula |
|-----------|---------|
| \|A ∪ B\| | \|A\| + \|B\| - \|A ∩ B\| |
| \|A ∪ B ∪ C\| | \|A\| + \|B\| + \|C\| - \|A∩B\| - \|B∩C\| - \|A∩C\| + \|A∩B∩C\| |
| \|A - B\| | \|A\| - \|A ∩ B\| |
| \|A'\| | \|U\| - \|A\| |
| \|A Δ B\| | \|A\| + \|B\| - 2\|A ∩ B\| |
| \|P(A)\| | 2^{\|A\|} |
| De Morgan | (A ∪ B)' = A' ∩ B' |
| Distributive | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |

---

## 📝 GATE-Level Practice

**Q1**: In a group of 50 people, 30 speak English, 25 speak French, 10 speak both. How many speak neither?
```
|E ∪ F| = 30 + 25 - 10 = 45
Neither = 50 - 45 = 5
```

**Q2**: If |A| = 10, |B| = 15, |A ∩ B| = 5, find |A ∪ B| and |A - B|.
```
|A ∪ B| = 10 + 15 - 5 = 20
|A - B| = 10 - 5 = 5
```

**Q3**: How many subsets does {a, b, c, d} have?
```
|P(A)| = 2⁴ = 16 subsets
```

**Q4**: If A = {1, 2, 3}, B = {2, 3, 4}, find A Δ B.
```
A Δ B = (A - B) ∪ (B - A)
      = {1} ∪ {4}
      = {1, 4}
```

**Q5**: In a survey of 100 students: 60 like tea, 50 like coffee, 30 like both. Find:
a) At least one drink
b) Only tea
c) Only coffee
```
a) |T ∪ C| = 60 + 50 - 30 = 80
b) Only tea = 60 - 30 = 30
c) Only coffee = 50 - 30 = 20
```

**Q6**: Apply De Morgan's law to (P ∪ Q)'.
```
(P ∪ Q)' = P' ∩ Q'
```

---

*← [Chapter 18 - Statistics](./18_Statistics.md) | [Chapter 20 - Logical Reasoning →](./20_Logical_Reasoning.md)*
