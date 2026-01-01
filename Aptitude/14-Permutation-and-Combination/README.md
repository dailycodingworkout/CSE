# 🔢 Permutation and Combination | The Singularity

> **The Atomic Truth:** *Permutation = Ordered selection; Combination = Unordered selection.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Fundamental Counting Principle](#fundamental-counting-principle)
3. [Permutations](#permutations)
4. [Combinations](#combinations)
5. [Special Cases](#special-cases)
6. [Distribution Problems](#distribution-problems)
7. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
8. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why P&C Matters?
This is a **high-frequency GATE topic** because:
- Foundation for probability
- Tests logical thinking
- Appears in algorithms complexity
- Critical for DSA understanding

### The Core Distinction

| Concept | Order Matters? | Example |
|---------|---------------|---------|
| **Permutation** | Yes | Arranging books on shelf |
| **Combination** | No | Selecting team members |

> **💡 The Golden Pivot:** "Arrangement" = Permutation; "Selection" = Combination

### Factorial Definition

$$n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1$$

**Special cases:**
- $0! = 1$
- $1! = 1$

**Common values:**
| n | n! |
|---|-----|
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5040 |
| 10 | 3,628,800 |

---

## Fundamental Counting Principle

### Multiplication Principle (AND)

If task A can be done in $m$ ways AND task B can be done in $n$ ways, then both tasks can be done in $m \times n$ ways.

**Example:** 3 shirts and 4 pants = 3 × 4 = 12 outfits

### Addition Principle (OR)

If task A can be done in $m$ ways OR task B can be done in $n$ ways (mutually exclusive), then either task can be done in $m + n$ ways.

**Example:** Going from A to B via road (3 routes) OR rail (2 routes) = 3 + 2 = 5 ways

---

## Permutations

### Basic Formula

Arrangement of $r$ items from $n$ distinct items:

$$P(n,r) = ^nP_r = \frac{n!}{(n-r)!}$$

**Special case:** $P(n,n) = n!$ (arranging all items)

### Permutation Types

#### 1. All Items Different
$$P(n,n) = n!$$

#### 2. With Repetition Allowed
$$n^r$$ (n choices for each of r positions)

#### 3. With Identical Items

If among n items, there are $p$ identical of type 1, $q$ identical of type 2, etc.:

$$\text{Arrangements} = \frac{n!}{p! \times q! \times ...}$$

**Example:** Arrangements of "MISSISSIPPI"
- Letters: M(1), I(4), S(4), P(2)
- Total = 11 letters
$$\text{Arrangements} = \frac{11!}{4! \times 4! \times 2!} = \frac{39916800}{24 \times 24 \times 2} = 34650$$

### Circular Permutations

#### Fixed Direction
$$(n-1)!$$

**Why?** One element is fixed to remove rotational duplicates.

#### Both Directions (Necklace/Bracelet)
$$\frac{(n-1)!}{2}$$

**Why?** Clockwise and counter-clockwise arrangements are same.

---

## Combinations

### Basic Formula

Selection of $r$ items from $n$ distinct items:

$$C(n,r) = ^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

### Key Properties

1. **Symmetry:** $C(n,r) = C(n, n-r)$
2. **Pascal's Identity:** $C(n,r) = C(n-1, r-1) + C(n-1, r)$
3. **Sum of row:** $C(n,0) + C(n,1) + ... + C(n,n) = 2^n$
4. **Vandermonde's Identity:** $C(m+n, r) = \sum_{k=0}^{r} C(m,k) \times C(n, r-k)$

### Common Values

| Expression | Value |
|------------|-------|
| $C(n,0)$ | 1 |
| $C(n,1)$ | n |
| $C(n,2)$ | $\frac{n(n-1)}{2}$ |
| $C(n,n)$ | 1 |
| $C(n,n-1)$ | n |

---

## Special Cases

### 1. Selection with Repetition

Selecting $r$ items from $n$ types (repetition allowed):

$$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$$

**Example:** Ways to distribute 5 identical balls into 3 boxes
$$\binom{3+5-1}{5} = \binom{7}{5} = 21$$

### 2. Arrangement in a Row with Constraints

**Items together:** Treat as single unit, then arrange internally.

**Example:** Arrange GATE such that G and A are together.
- Treat GA as unit: {GA, T, E} = 3! = 6
- Internal arrangement of GA: 2! = 2
- Total = 6 × 2 = 12

**Items never together:** Total - Together

### 3. Derangements

Arrangements where no item is in its original position:

$$D_n = n! \left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + ... + (-1)^n \frac{1}{n!}\right)$$

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$

**Common values:**
| n | $D_n$ |
|---|-------|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 9 |
| 5 | 44 |

### 4. Choosing with Partition

Ways to partition n items into groups of sizes $r_1, r_2, ..., r_k$:

$$\frac{n!}{r_1! \times r_2! \times ... \times r_k!}$$

If groups are identical (unlabeled):
$$\frac{n!}{r_1! \times r_2! \times ... \times r_k! \times m!}$$

where m = number of groups with same size.

---

## Distribution Problems

### Distinct Objects to Distinct Boxes

| Constraint | Formula |
|------------|---------|
| No restriction | $n^r$ (r objects, n boxes) |
| Each box at most 1 | $P(n,r)$ |
| Each box at least 1 | Inclusion-Exclusion |

### Identical Objects to Distinct Boxes

| Constraint | Formula |
|------------|---------|
| No restriction | $\binom{n+r-1}{r}$ |
| Each box at least 1 | $\binom{r-1}{n-1}$ |

### Distinct Objects to Identical Boxes

Use Stirling Numbers of second kind:
$$S(n,k) = \text{ways to partition n objects into k non-empty subsets}$$

### Identical Objects to Identical Boxes

Partitions of n into at most k parts.

---

## GATE & ESE Problem Patterns

### Pattern 1: Basic Counting
> How many 3-digit numbers can be formed using {1,2,3,4,5} without repetition?
- First digit: 5 choices
- Second digit: 4 choices
- Third digit: 3 choices
- Total = 5 × 4 × 3 = **60**

### Pattern 2: Word Arrangements
> In how many ways can letters of "BANANA" be arranged?
- Letters: B(1), A(3), N(2)
$$\text{Arrangements} = \frac{6!}{3! \times 2!} = \frac{720}{12} = 60$$

### Pattern 3: Committee Selection
> From 5 men and 4 women, select a committee of 4 with at least 2 women.
- (2W, 2M): $C(4,2) × C(5,2) = 6 × 10 = 60$
- (3W, 1M): $C(4,3) × C(5,1) = 4 × 5 = 20$
- (4W, 0M): $C(4,4) × C(5,0) = 1 × 1 = 1$
- Total = 60 + 20 + 1 = **81**

### Pattern 4: Circular Arrangement
> In how many ways can 6 people sit around a circular table?
$$(6-1)! = 5! = 120$$

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"How many diagonals does a polygon with 10 sides have?"

Wrong approach: Connecting any 2 vertices = $C(10,2) = 45$

**The Elegant Solution:**
- Total line segments = $C(10,2) = 45$
- Sides of polygon = 10
- Diagonals = 45 - 10 = **35**

General formula: $\frac{n(n-3)}{2}$

**MSQ Logic Gate:**
- Check if order matters (arrangement vs selection)
- Check for repetition (with or without)
- Check for identical items

**NAT Precision Lock:**
- Factorial calculations must be exact
- Division must result in integer (if not, recheck)

---

## Speed Tricks & Shortcuts

### Trick 1: Quick nCr Calculation

$$C(n,r) = \frac{n \times (n-1) \times ... \times (n-r+1)}{r!}$$

**Example:** $C(7,3) = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \frac{210}{6} = 35$

### Trick 2: Symmetry Usage

Use $C(n,r) = C(n, n-r)$ when $r > n/2$

**Example:** $C(10,8) = C(10,2) = 45$

### Trick 3: At Least One Approach

P(at least 1) = Total - P(none)

### Trick 4: Identical Items Formula

Remember: Stars and Bars = $\binom{n+r-1}{r}$

### Trick 5: Circular vs Linear

Circular = Linear ÷ n

---

## Permanent Recall

### The Bizarre Mnemonic (P vs C)
*"**P**ermutation is **P**icky about **P**osition (order matters). **C**ombination **C**ouldn't **C**are about order (just selection)."*

### The Mental Slider
Visualize:
- Permutation: Arranging books on a specific shelf (left to right matters)
- Combination: Picking books to read (order doesn't matter)

### The 5-Second Snap-Check
- If "arrange/order/sequence" → Permutation
- If "select/choose/pick" → Combination
- Result must always be a positive integer

---

## Practice Problems

### Level 1: Fundamentals
1. In how many ways can 5 people be seated in a row?
2. From 8 different books, how many ways to select 3 books?
3. How many 4-letter words can be formed from "MATHEMATICS" using each letter once?

### Level 2: GATE Standard
4. In how many ways can the letters of "LEADING" be arranged so that vowels are always together?
5. A committee of 5 is to be formed from 6 men and 4 women. In how many ways can this be done if committee must have at least 2 women?
6. Find the number of ways to distribute 8 identical balls into 4 distinct boxes such that no box is empty.

### Level 3: IIT Examiner Level
7. In how many ways can 5 boys and 5 girls be seated in a row so that no two girls sit together?
8. Find the number of ways to select 4 letters from the word "PROPORTION".
9. How many 6-digit numbers can be formed using digits {1,2,3,4,5,6} without repetition that are divisible by 4?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. $5! = 5 \times 4 \times 3 \times 2 \times 1 = **120**$

2. $C(8,3) = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = \frac{336}{6} = **56**$

3. MATHEMATICS has: M(2), A(2), T(2), H(1), E(1), I(1), C(1), S(1) = 11 letters, 8 distinct
   Since we want 4-letter words using each letter once:
   $P(11,4) = 11 \times 10 \times 9 \times 8 = **7920**$
   
   Wait, "using each letter once" means from distinct letters.
   If selecting 4 from 8 distinct types: $8 \times 7 \times 6 \times 5 = **1680**$

4. LEADING: Vowels = E, A, I (3); Consonants = L, D, N, G (4)
   Treat vowels as one unit: {EAI}, L, D, N, G = 5 units
   Arrangements of 5 units = 5! = 120
   Internal arrangement of vowels = 3! = 6
   Total = 120 × 6 = **720**

5. 6 men, 4 women, committee of 5 with at least 2 women:
   - (2W, 3M): $C(4,2) × C(6,3) = 6 × 20 = 120$
   - (3W, 2M): $C(4,3) × C(6,2) = 4 × 15 = 60$
   - (4W, 1M): $C(4,4) × C(6,1) = 1 × 6 = 6$
   Total = 120 + 60 + 6 = **186**

6. 8 identical balls, 4 boxes, each box at least 1:
   First put 1 in each box (4 balls used)
   Remaining 4 balls in 4 boxes (no restriction):
   $C(4+4-1,4) = C(7,4) = **35**$

7. First arrange 5 boys: 5! ways
   Now there are 6 gaps (before, between, after boys): _B_B_B_B_B_
   Place 5 girls in 6 gaps: $P(6,5) = 6!/(6-5)! = 720$
   Total = 5! × P(6,5) = 120 × 720 = **86,400**

8. PROPORTION: P(2), R(2), O(3), T(1), I(1), N(1)
   Cases:
   - All 4 different: $C(6,4) = 15$ selections, but need to check which are available
   - 3 same + 1 different: Only O appears 3 times. $1 × C(5,1) = 5$
   - 2 same + 2 same: {P,P,R,R} or {P,P,O,O} or {R,R,O,O} = 3
   - 2 same + 2 different: Choose 1 from {P,R,O} to repeat, 2 from remaining 5 distinct
     = $3 × C(5,2) = 3 × 10 = 30$
   
   Total = 15 + 5 + 3 + 30 = **53**

9. For divisibility by 4, last two digits form number divisible by 4.
   Possible last two digits from {1,2,3,4,5,6}: 12, 16, 24, 32, 36, 52, 56, 64 = 8 options
   
   For each, remaining 4 digits can be arranged in 4! = 24 ways
   Total = 8 × 24 = **192**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Permutation & Combination with Probability for a Rank-1 simulation?
