# Chapter 16: Permutations & Combinations

> **The mathematics of counting - how many ways can things be arranged or selected?**

---

## 🎯 Why Study This?

- Foundation for probability theory
- High-frequency topic in GATE/ESE
- Essential for algorithm analysis (number of possibilities)

---

## 📚 Fundamental Concepts

### Factorial

```
n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1

Special cases:
0! = 1 (by definition)
1! = 1
```

**Common Values** (Memorize!):
```
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
10! = 3,628,800
```

---

### Fundamental Counting Principle

**Multiplication Principle**: If one event can happen in m ways, and another independent event in n ways, then both can happen in m × n ways.

**Addition Principle**: If one event can happen in m ways OR another mutually exclusive event in n ways, total ways = m + n.

---

## 🔄 Permutations (Arrangement)

### Definition

**Permutation** = Arrangement where **order matters**

**💡 Analogy**: Arranging books on a shelf - ABC ≠ BAC

---

### Permutation of n distinct objects

All n objects:
```
P(n) = n!
```

Taking r objects from n:
```
P(n,r) = ⁿPᵣ = n!/(n-r)!
```

**Example**: Arrange 3 books from 5
```
⁵P₃ = 5!/2! = 5 × 4 × 3 = 60 ways
```

---

### Permutation with Repetition

If we have n objects with repetitions (n₁ alike of type 1, n₂ alike of type 2, ...):
```
Permutations = n!/(n₁! × n₂! × n₃! × ...)
```

**Example**: Arrangements of MISSISSIPPI
```
Total = 11 letters
M = 1, I = 4, S = 4, P = 2
Arrangements = 11!/(1! × 4! × 4! × 2!) = 34,650
```

---

### Circular Permutations

Arranging n objects in a circle:
```
(n-1)! ways
```

**Why?** Fix one position, arrange remaining (n-1).

**If clockwise = anticlockwise** (e.g., necklace, bracelet - can be flipped):
```
(n-1)!/2 ways
```

**💡 Why divide by 2 for necklaces?**
A necklace can be **flipped over** (turned upside down), making clockwise and anticlockwise arrangements identical. For example, beads arranged as A-B-C-D clockwise look the same as A-D-C-B (anticlockwise) when you flip the necklace. Since each arrangement is counted twice (once for each orientation), we divide by 2.

**When NOT to divide by 2** (clockwise ≠ anticlockwise): If objects have a distinct "front" and "back" (like keys on a keyring with one-sided labels), flipping changes the arrangement, so use (n-1)! only.

---

## 📦 Combinations (Selection)

### Definition

**Combination** = Selection where **order doesn't matter**

**💡 Analogy**: Choosing team members - ABC = BAC = CAB (same team)

---

### Combination Formula

```
C(n,r) = ⁿCᵣ = n!/[r!(n-r)!] = ⁿPᵣ/r!
```

**Example**: Choose 3 books from 5
```
⁵C₃ = 5!/(3! × 2!) = 10 ways
```

---

### Key Properties

```
ⁿC₀ = ⁿCₙ = 1
ⁿC₁ = ⁿCₙ₋₁ = n
ⁿCᵣ = ⁿCₙ₋ᵣ
ⁿCᵣ + ⁿCᵣ₊₁ = ⁿ⁺¹Cᵣ₊₁  (Pascal's Identity)
ⁿC₀ + ⁿC₁ + ... + ⁿCₙ = 2ⁿ
```

---

### Combinations with Repetition

Selecting r items from n types (each type has unlimited supply):
```
= ⁿ⁺ʳ⁻¹Cᵣ = (n+r-1)!/[r!(n-1)!]
```

**💡 Stars and Bars**: Distributing r identical items into n distinct boxes.

---

## 📊 Key Problem Types

### Type 1: Arrangement with Restrictions

**Some objects always together**: Treat as single unit, arrange, then arrange within.
```
If AB must be together: Treat AB as one block
Arrangements = (n-1)! × 2! (2! for internal arrangement)
```

**Some objects never together**: Total - Together
```
Never together = Total arrangements - Together arrangements
```

---

### Type 2: Arrangement in Specific Positions

**Fixed positions**: Fill fixed first, arrange rest.

**Relative positions**: Use constraints systematically.

**Example**: 5 people, A must be to the left of B (not necessarily adjacent)
```
Total = 5! = 120
A left of B = 120/2 = 60 (by symmetry)
```

---

### Type 3: Selection with Constraints

**At least one / At most k / Exactly k**:

**At least 1**: Total - None
```
At least 1 = Total ways - Ways with none
```

**At most k**: Sum from 0 to k
```
At most 2 = C(n,0) + C(n,1) + C(n,2)
```

---

### Type 4: Division into Groups

**Into distinct groups** of sizes r₁, r₂, ...:
```
n!/(r₁! × r₂! × ...)
```

**Into identical groups** of size r each (n = kr):
```
n!/(r!)^k / k!
```

---

### Type 5: Distribution Problems

**Distinct objects into distinct boxes**: nʳ (each object has n choices)

**Identical objects into distinct boxes**: Use stars and bars.

**Distinct objects into identical boxes**: Stirling numbers (more complex)

---

## 📐 Special Formulas

### Derangements

Arrangements where NO object is in its original position:
```
Dₙ = n! × [1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!]
   = n! × Σ(-1)^k/k! for k = 0 to n
```

**First few values**:
```
D₁ = 0
D₂ = 1
D₃ = 2
D₄ = 9
D₅ = 44
```

**Approximation**: Dₙ ≈ n!/e (rounded to nearest integer)

---

### Geometric Arrangements

**Straight lines from n points** (no 3 collinear):
```
ⁿC₂ = n(n-1)/2
```

**Triangles from n points** (no 3 collinear):
```
ⁿC₃ = n(n-1)(n-2)/6
```

**Diagonals of n-sided polygon**:
```
ⁿC₂ - n = n(n-3)/2
```

---

### Handshakes and Matches

**Handshakes among n people**:
```
ⁿC₂ = n(n-1)/2
```

**Matches in round-robin tournament**:
```
ⁿC₂ = n(n-1)/2
```

---

## 💡 Advanced Tricks

### Trick 1: ⁿCᵣ Calculation Shortcut

```
⁵C₃ = 5C₂ (use smaller r)
    = (5 × 4)/(2 × 1) = 10
```

---

### Trick 2: Quick Factorial Division

```
10!/8! = 10 × 9 = 90
n!/(n-2)! = n(n-1)
```

---

### Trick 3: Complementary Counting

When "at least" or "not" appears:
```
Required = Total - Unwanted
```

---

### Trick 4: Identical Objects Shortcut

For selecting r objects from n where objects are identical:
```
Only 1 way (if r ≤ n, else 0)
```

---

### Trick 5: Multinomial Distribution

Distributing n distinct objects into k groups of sizes r₁, r₂, ..., rₖ:
```
Multinomial coefficient = n!/(r₁! × r₂! × ... × rₖ!)
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Permutation vs Combination
```
Arrangement (order matters) → Permutation
Selection (order doesn't matter) → Combination
```

### Trap 2: With vs Without Replacement
```
With replacement: n choices each time
Without replacement: decreasing choices
```

### Trap 3: Identical vs Distinct Groups
```
Distinct groups: Don't divide by k!
Identical groups: Divide by k!
```

### Trap 4: Circular vs Linear
```
Linear: n!
Circular: (n-1)!
Necklace/Bracelet: (n-1)!/2
```

### Trap 5: 0! = 1
```
Don't make 0! = 0
0! = 1 by definition
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Factorial | n! = n × (n-1) × ... × 1 |
| Permutation | ⁿPᵣ = n!/(n-r)! |
| Combination | ⁿCᵣ = n!/[r!(n-r)!] |
| Repeated permutation | n!/(n₁!n₂!...) |
| Circular arrangement | (n-1)! |
| With repetition (selection) | ⁿ⁺ʳ⁻¹Cᵣ |
| Derangement | n! × Σ(-1)^k/k! |
| Diagonals of polygon | n(n-3)/2 |
| ⁿC₀ + ⁿC₁ + ... + ⁿCₙ | 2ⁿ |

---

## 📝 GATE-Level Practice

**Q1**: How many 4-letter words can be formed from EQUATION using each letter once?
```
EQUATION has 8 distinct letters
⁸P₄ = 8!/4! = 8 × 7 × 6 × 5 = 1680
```

**Q2**: In how many ways can 5 people sit around a circular table?
```
(5-1)! = 4! = 24 ways
```

**Q3**: Number of ways to select 3 balls from 4 red, 5 blue, and 3 green balls if at least one of each color must be selected?
```
Select 1 red, 1 blue, 1 green = ⁴C₁ × ⁵C₁ × ³C₁ = 4 × 5 × 3 = 60
OR select 2 of one, 1 of others... (but question says exactly 3 with at least 1 each)
Answer: 60 ways
```

**Q4**: How many arrangements of MATHEMATICS are possible?
```
M = 2, A = 2, T = 2, H = 1, E = 1, I = 1, C = 1, S = 1
Total letters = 11
Arrangements = 11!/(2! × 2! × 2!) = 11!/8 = 4,989,600
```

**Q5**: Find number of diagonals in a decagon.
```
n = 10
Diagonals = 10(10-3)/2 = 10 × 7/2 = 35
```

**Q6**: How many ways to distribute 10 identical balls into 4 distinct boxes?
```
Stars and bars: ¹⁰⁺⁴⁻¹C₄₋₁ = ¹³C₃ = 286
```

---

*← [Chapter 15 - Sequences & Series](./15_Sequences_Series.md) | [Chapter 17 - Probability →](./17_Probability.md)*
