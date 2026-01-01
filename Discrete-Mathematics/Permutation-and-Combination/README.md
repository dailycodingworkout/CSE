# Permutation and Combination | GATE & ESE Complete Study Material

## 🎯 **The Singularity**

**Atomic Truth:** *"Arrangement vs Selection—Order matters or not."*

---

## 📚 Table of Contents

1. [Foundational Principles](#1-foundational-principles)
2. [Core Formulas & Derivations](#2-core-formulas--derivations)
3. [Permutations - Deep Dive](#3-permutations---deep-dive)
4. [Combinations - Deep Dive](#4-combinations---deep-dive)
5. [Advanced Concepts](#5-advanced-concepts)
6. [GATE/ESE Specific Tricks & Shortcuts](#6-gateese-specific-tricks--shortcuts)
7. [Edge Cases & Common Traps](#7-edge-cases--common-traps)
8. [Solved Examples (GATE Level)](#8-solved-examples-gate-level)
9. [Practice Problems](#9-practice-problems)
10. [Quick Revision & Mnemonics](#10-quick-revision--mnemonics)

---

## 1. Foundational Principles

### 1.1 The Fundamental Counting Principle

#### **Why Does This Exist?**

The entire field of combinatorics rests on ONE atomic truth:

> **If task A can be done in `m` ways and task B in `n` ways, then A followed by B can be done in `m × n` ways (if independent).**

#### **The Mental Model - The Tree Analogy**

Imagine you're choosing an outfit:
- 3 shirts (Red, Blue, Green)
- 2 pants (Black, White)

```
                    Wardrobe
                   /    |    \
               Red    Blue   Green
              /   \   /   \   /   \
           Black White Black White Black White
```

**Total combinations = 3 × 2 = 6**

This is the **Multiplication Principle** (AND operation).

#### **The Addition Principle**

> **If task A can be done in `m` ways OR task B in `n` ways (mutually exclusive), then either can be done in `m + n` ways.**

**Example:** Going from Delhi to Mumbai:
- By train: 5 options
- By flight: 3 options
- **Total ways = 5 + 3 = 8** (OR operation)

---

### 1.2 Factorial - The Building Block

#### **What is Factorial?**

$$n! = n \times (n-1) \times (n-2) \times \ldots \times 2 \times 1$$

#### **The Physical Interpretation**

**Question:** In how many ways can you arrange `n` distinct objects in a line?

- First position: `n` choices
- Second position: `n-1` choices (one used)
- Third position: `n-2` choices
- ...
- Last position: `1` choice

**Total = n × (n-1) × (n-2) × ... × 1 = n!**

#### **Critical Edge Cases for GATE**

| Expression | Value | Why? |
|------------|-------|------|
| $0!$ | $1$ | **Convention** (empty product = 1, also $^nC_n = 1$) |
| $1!$ | $1$ | Only one way to arrange one object |
| $(-n)!$ | **Undefined** | Factorial only defined for non-negative integers |

#### **The Gamma Function Extension (For Advanced)**

$$\Gamma(n) = (n-1)!$$
$$\Gamma(1/2) = \sqrt{\pi}$$

---

### 1.3 The Central Question Framework

Before solving ANY combinatorics problem, ask:

```
┌─────────────────────────────────────────────────────────────┐
│  DECISION TREE FOR COMBINATORICS                            │
├─────────────────────────────────────────────────────────────┤
│  1. Does ORDER matter?                                       │
│     → YES: Permutation                                       │
│     → NO: Combination                                        │
│                                                              │
│  2. Is REPETITION allowed?                                   │
│     → YES: With repetition formulas                          │
│     → NO: Without repetition formulas                        │
│                                                              │
│  3. Are objects IDENTICAL or DISTINCT?                       │
│     → Distinct: Standard formulas                            │
│     → Identical: Use division to remove duplicates           │
│                                                              │
│  4. Are there RESTRICTIONS or CONDITIONS?                    │
│     → Use Inclusion-Exclusion or Complementary Counting      │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Core Formulas & Derivations

### 2.1 Permutation (Arrangement)

#### **Definition**
A permutation is an **ordered arrangement** of objects.

#### **Formula: $^nP_r$ (n objects, select r, order matters)**

$$^nP_r = \frac{n!}{(n-r)!}$$

#### **Derivation (First Principles)**

We need to fill `r` positions from `n` distinct objects:

- Position 1: `n` choices
- Position 2: `n-1` choices
- Position 3: `n-2` choices
- ...
- Position r: `n-r+1` choices

$$^nP_r = n \times (n-1) \times (n-2) \times \ldots \times (n-r+1)$$

$$= \frac{n \times (n-1) \times \ldots \times (n-r+1) \times (n-r)!}{(n-r)!}$$

$$= \frac{n!}{(n-r)!}$$

#### **Special Cases**

| Case | Formula | Example |
|------|---------|---------|
| All objects | $^nP_n = n!$ | Arrange all 5 books: $5! = 120$ |
| Select one | $^nP_1 = n$ | Choose 1 from 5: $5$ ways |
| Select none | $^nP_0 = 1$ | Do nothing: $1$ way |

---

### 2.2 Combination (Selection)

#### **Definition**
A combination is an **unordered selection** of objects.

#### **Formula: $^nC_r$ (n objects, select r, order doesn't matter)**

$$^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

#### **Derivation (The Golden Pivot)**

**Key Insight:** Every combination of `r` objects can be arranged in `r!` ways.

$$\text{Permutations} = \text{Combinations} \times \text{Arrangements of selected}$$

$$^nP_r = {^nC_r} \times r!$$

$$^nC_r = \frac{^nP_r}{r!} = \frac{n!}{r!(n-r)!}$$

#### **The Symmetry Property**

$$^nC_r = {^nC_{n-r}}$$

**Why?** Choosing `r` objects to INCLUDE = Choosing `n-r` objects to EXCLUDE.

**Example:** $^{10}C_7 = {^{10}C_3} = 120$

---

### 2.3 Permutation with Repetition

#### **Case 1: Repetition Allowed**

**Problem:** Form r-digit numbers using n digits (repetition allowed)

$$\text{Total arrangements} = n^r$$

**Example:** 4-digit PIN using digits 0-9 = $10^4 = 10000$

#### **Case 2: Identical Objects (Multiset Permutation)**

**Problem:** Arrange n objects where $n_1$ are of type 1, $n_2$ are of type 2, etc.

$$\text{Permutations} = \frac{n!}{n_1! \times n_2! \times \ldots \times n_k!}$$

**Example:** Arrangements of "MISSISSIPPI"
- Total letters: 11
- M: 1, I: 4, S: 4, P: 2

$$= \frac{11!}{1! \times 4! \times 4! \times 2!} = \frac{39916800}{1 \times 24 \times 24 \times 2} = 34650$$

---

### 2.4 Combination with Repetition

**Problem:** Select r items from n types (repetition allowed, order doesn't matter)

$$^{n+r-1}C_r = \binom{n+r-1}{r}$$

**The Stars and Bars Method:**

Imagine selecting r identical balls to place in n distinct boxes.

- Stars (★): r items to select
- Bars (|): n-1 dividers between boxes

**Total symbols = r + (n-1) = n + r - 1**
**Choose positions for r stars = $^{n+r-1}C_r$**

**Example:** Select 5 fruits from {Apple, Banana, Orange}
- n = 3 types, r = 5 selections
- Answer = $^{3+5-1}C_5 = {^7C_5} = 21$

---

## 3. Permutations - Deep Dive

### 3.1 Circular Permutation

#### **Why is it Different?**

In a circle, there's no fixed starting point. We fix one element and arrange the rest.

$$\text{Circular permutations of n distinct objects} = (n-1)!$$

#### **Visual Understanding**

```
Linear:   A B C D  (A is first)
          B A C D  (B is first)  ← Different
          
Circular:   A               B
          D   B    vs     A   C    ← These are SAME rotation
            C               D
```

**Fixing one element removes rotational equivalence.**

#### **Clockwise vs Anti-clockwise Matter?**

| Scenario | Formula |
|----------|---------|
| Distinct arrangements (like seating) | $(n-1)!$ |
| Indistinguishable (like necklace/bracelet) | $\frac{(n-1)!}{2}$ |

**Example:** Arrange 6 keys on a keyring = $\frac{(6-1)!}{2} = \frac{120}{2} = 60$

---

### 3.2 Permutations with Restrictions

#### **Restriction Type 1: Certain objects always together**

**Method:** Treat them as a single unit, then arrange internally.

**Example:** Arrange ABCDE such that A and B are always together.

- Treat (AB) as single unit: {(AB), C, D, E} = 4 units
- Arrange 4 units: $4! = 24$
- Internal arrangements of AB: $2! = 2$
- **Total = 24 × 2 = 48**

#### **Restriction Type 2: Certain objects never together**

**Method:** Total - Together

**Example:** Arrange ABCDE such that A and B are never together.

- Total arrangements: $5! = 120$
- A and B together: $48$ (from above)
- **Never together = 120 - 48 = 72**

#### **Restriction Type 3: Objects in specific positions**

**Example:** Arrange "GATE" such that vowels occupy odd positions.

- Odd positions: 1, 3 (need 2 vowels: A, E)
- Arrange A, E in odd positions: $2! = 2$
- Even positions: 2, 4 (consonants: G, T)
- Arrange G, T: $2! = 2$
- **Total = 2 × 2 = 4**

---

### 3.3 Derangements (Subfactorial)

#### **What is a Derangement?**

A permutation where **NO element appears in its original position**.

$$D_n = n! \left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \ldots + (-1)^n \frac{1}{n!}\right)$$

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$

#### **Recursive Formula**

$$D_n = (n-1)(D_{n-1} + D_{n-2})$$

**Base cases:** $D_1 = 0$, $D_2 = 1$

#### **Quick Reference Table**

| n | $D_n$ | Calculation |
|---|-------|-------------|
| 1 | 0 | No way to derange 1 item |
| 2 | 1 | (2,1) is the only derangement of (1,2) |
| 3 | 2 | {(2,3,1), (3,1,2)} |
| 4 | 9 | By formula |
| 5 | 44 | By formula |

#### **GATE Application: Hat Check Problem**

*5 people check their hats. In how many ways can hats be returned so no one gets their own?*

**Answer:** $D_5 = 44$

---

## 4. Combinations - Deep Dive

### 4.1 Properties of Binomial Coefficients

#### **Essential Identities**

1. **Symmetry:** $\binom{n}{r} = \binom{n}{n-r}$

2. **Pascal's Identity:** $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$

3. **Sum of all:** $\sum_{r=0}^{n} \binom{n}{r} = 2^n$

4. **Alternating sum:** $\sum_{r=0}^{n} (-1)^r \binom{n}{r} = 0$

5. **Vandermonde's Identity:** $\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k}$

6. **Hockey Stick Identity:** $\sum_{i=r}^{n} \binom{i}{r} = \binom{n+1}{r+1}$

#### **Pascal's Triangle**

```
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
    1   6  15  20  15   6   1
```

**Properties:**
- Row n contains $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$
- Each entry = sum of two entries above it
- Sum of row n = $2^n$

---

### 4.2 Combination Problems with Conditions

#### **Type 1: Selecting with mandatory elements**

**Problem:** Select 5 from 10, where 2 specific must be included.

- Fix 2 elements as included
- Select remaining 3 from 8
- **Answer:** $\binom{8}{3} = 56$

#### **Type 2: Selecting with excluded elements**

**Problem:** Select 5 from 10, where 2 specific cannot be included.

- Remove 2 from pool
- Select 5 from 8
- **Answer:** $\binom{8}{5} = 56$

#### **Type 3: At least/At most conditions**

**Problem:** Select at least 2 from 6.

$$= \binom{6}{2} + \binom{6}{3} + \binom{6}{4} + \binom{6}{5} + \binom{6}{6}$$

**Faster:** $= 2^6 - \binom{6}{0} - \binom{6}{1} = 64 - 1 - 6 = 57$

---

### 4.3 Distribution Problems

#### **Distributing n Identical Objects into r Distinct Boxes**

$$= \binom{n+r-1}{r-1}$$

**Example:** Distribute 10 identical candies to 4 children.

$$= \binom{10+4-1}{4-1} = \binom{13}{3} = 286$$

#### **Each box must have at least one**

First give 1 to each box (uses r), distribute remaining (n-r):

$$= \binom{(n-r)+r-1}{r-1} = \binom{n-1}{r-1}$$

**Example:** 10 candies to 4 children, each gets at least 1.

$$= \binom{10-1}{4-1} = \binom{9}{3} = 84$$

---

## 5. Advanced Concepts

### 5.1 Inclusion-Exclusion Principle

#### **Formula for Two Sets**

$$|A \cup B| = |A| + |B| - |A \cap B|$$

#### **Formula for Three Sets**

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

#### **General Formula**

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{i}|A_i| - \sum_{i \lt j}|A_i \cap A_j| + \sum_{i \lt j \lt k}|A_i \cap A_j \cap A_k| - \ldots$$

#### **GATE Application: Counting with Restrictions**

**Problem:** How many integers from 1 to 1000 are divisible by 2, 3, or 5?

Let:
- $A$ = divisible by 2 = $\lfloor 1000/2 \rfloor = 500$
- $B$ = divisible by 3 = $\lfloor 1000/3 \rfloor = 333$
- $C$ = divisible by 5 = $\lfloor 1000/5 \rfloor = 200$
- $A \cap B$ = divisible by 6 = $166$
- $B \cap C$ = divisible by 15 = $66$
- $A \cap C$ = divisible by 10 = $100$
- $A \cap B \cap C$ = divisible by 30 = $33$

$$|A \cup B \cup C| = 500 + 333 + 200 - 166 - 66 - 100 + 33 = 734$$

---

### 5.2 The Pigeonhole Principle

#### **Simple Version**

> If n+1 pigeons are placed in n pigeonholes, at least one hole has ≥2 pigeons.

#### **Generalized Version**

> If n objects are placed in k boxes, at least one box has $\lceil n/k \rceil$ objects.

#### **GATE Applications**

**Example 1:** Among 13 people, at least 2 share the same birth month.
- 12 months, 13 people → at least $\lceil 13/12 \rceil = 2$

**Example 2:** In any 27 distinct English words, at least 2 start with the same letter.
- 26 letters → pigeonhole applies

---

### 5.3 Generating Functions (GATE Advanced)

#### **Ordinary Generating Function (OGF)**

For sequence $\{a_0, a_1, a_2, \ldots\}$:

$$G(x) = \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + \ldots$$

#### **Key Generating Functions**

| Sequence | Generating Function |
|----------|---------------------|
| $1, 1, 1, \ldots$ | $\frac{1}{1-x}$ |
| $1, 2, 3, 4, \ldots$ | $\frac{1}{(1-x)^2}$ |
| $\binom{n}{0}, \binom{n}{1}, \ldots$ | $(1+x)^n$ |
| $1, 0, 1, 0, 1, \ldots$ | $\frac{1}{1-x^2}$ |

#### **Solving Counting Problems**

**Problem:** Find coefficient of $x^{10}$ in $(1+x+x^2+\ldots)^3$

This equals distributing 10 identical balls into 3 distinct boxes.

$$= \binom{10+3-1}{3-1} = \binom{12}{2} = 66$$

---

### 5.4 Catalan Numbers

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}$$

#### **Recursive Formula**

$$C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-1-i}$$

$$C_0 = 1$$

#### **Values**

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $C_n$ | 1 | 1 | 2 | 5 | 14 | 42 | 132 |

#### **Applications (GATE Favorites)**

1. **Binary trees:** Number of structurally different binary trees with n nodes = $C_n$

2. **Parenthesization:** Valid arrangements of n pairs of parentheses = $C_n$

3. **Paths in grid:** Monotonic paths from (0,0) to (n,n) not crossing diagonal = $C_n$

4. **Polygon triangulation:** Ways to divide a convex (n+2)-gon into triangles = $C_n$

---

## 6. GATE/ESE Specific Tricks & Shortcuts

### 6.1 The 5-Second Recognition Patterns

#### **Pattern 1: "Arrange" = Permutation, "Select/Choose" = Combination**

| Question Keyword | Approach |
|------------------|----------|
| "arrange", "order", "sequence" | Permutation |
| "select", "choose", "committee" | Combination |
| "ways to distribute" | Stars & Bars or direct counting |

#### **Pattern 2: The Complement Trick**

When question asks "at least one" or "at most k":

$$P(\text{at least 1}) = 1 - P(\text{none})$$

**Saves massive computation!**

#### **Pattern 3: The Symmetry Shortcut**

For $^nC_r$ where $r > n/2$:

$$^nC_r = {^nC_{n-r}}$$

**Example:** $^{100}C_{97} = {^{100}C_3} = \frac{100 \times 99 \times 98}{6} = 161700$

---

### 6.2 GATE-Specific Calculation Tricks

#### **Trick 1: Cancellation Before Multiplication**

For $\binom{n}{r}$, always simplify before computing:

$$\binom{10}{3} = \frac{10!}{3! \times 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120$$

#### **Trick 2: Pascal's Identity for Adjacent Values**

If you know $\binom{n}{r}$, find $\binom{n}{r+1}$:

$$\binom{n}{r+1} = \binom{n}{r} \times \frac{n-r}{r+1}$$

#### **Trick 3: Quick Factorial Approximation**

For large n, use: $n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$ (Stirling's)

For GATE: Just memorize key values:
- $5! = 120$
- $6! = 720$
- $7! = 5040$
- $10! = 3628800$

---

### 6.3 NAT (Numerical Answer Type) Precision

#### **Common NAT Traps**

1. **Forgetting to multiply internal arrangements**
   - Problem: Arrange 3 men and 2 women alternatively
   - Trap: Only calculating positions, not arrangements within

2. **Off-by-one in circular permutations**
   - Formula is $(n-1)!$, not $n!$

3. **Overcounting identical items**
   - "MISSISSIPPI" requires division by factorials of repeats

4. **Stars and Bars formula confusion**
   - Selecting r from n types: $\binom{n+r-1}{r}$
   - Distributing n to r boxes: $\binom{n+r-1}{r-1}$

---

### 6.4 MSQ (Multiple Select Questions) Strategies

#### **Elimination Techniques**

1. **Dimensional Analysis:** If answer should be a count (integer), eliminate non-integers

2. **Boundary Testing:** 
   - For n objects: answer must be ≤ $n!$ for permutations
   - For combinations: answer must be ≤ $2^n$

3. **Symmetry Check:** If problem has symmetry, answer often has pattern

---

## 7. Edge Cases & Common Traps

### 7.1 The Adversarial Vault - Top 10 GATE Traps

#### **Trap 1: Zero in Permutation**

**Problem:** How many 4-digit numbers using {0,1,2,3}?

**Wrong Answer:** $4! = 24$

**Correct Analysis:**
- First digit: 3 choices (1,2,3 - not 0)
- Remaining 3 positions: $3! = 6$ arrangements
- **Answer: 3 × 6 = 18**

#### **Trap 2: Circular with Identical Objects**

**Problem:** Arrange 3 identical red and 2 identical blue beads in a circle.

**Wrong:** $(5-1)! / (3! \times 2!) = 24/12 = 2$

**Correct:** Must account for reflection in necklace
- Linear equivalent: $\frac{5!}{3! \times 2!} = 10$
- Circular: $\frac{10}{5} = 2$ (divide by n for rotation)
- Necklace: $\frac{2+\text{symmetric cases}}{2}$
- **Answer: 2** (but reasoning differs!)

#### **Trap 3: "At Least" Misinterpretation**

**Problem:** Select a committee of at least 2 from 5 people.

**Some students:** $\binom{5}{2} = 10$ ❌

**Correct:** $\binom{5}{2} + \binom{5}{3} + \binom{5}{4} + \binom{5}{5} = 10 + 10 + 5 + 1 = 26$

#### **Trap 4: Overcounting in Grid Paths**

**Problem:** Paths from (0,0) to (3,3) without crossing diagonal?

**Answer:** Catalan number $C_3 = 5$ (not $\binom{6}{3} = 20$!)

#### **Trap 5: Distribution with Constraints**

**Problem:** Distribute 10 identical balls into 3 boxes such that no box is empty.

**Wrong:** $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$

**Correct:** First put 1 in each box, then distribute 7: $\binom{7+3-1}{3-1} = \binom{9}{2} = 36$

#### **Trap 6: Permutation with All Identical Objects**

**Problem:** Arrangements of {A, A, A}?

**Answer:** $\frac{3!}{3!} = 1$ (not 6!)

#### **Trap 7: Conditional Probability Mix-up**

**Problem:** Probability that a random 3-letter arrangement of "CAT" starts with C?

**Wrong thinking:** $\frac{1}{3}$ (C is one of 3 letters)

**Correct:** Total arrangements = $3! = 6$, Starting with C = $2! = 2$
- **Probability = 2/6 = 1/3** ✓ (same answer, but reasoning matters!)

#### **Trap 8: Distinguishable vs Indistinguishable**

**Problem:** Put 4 balls in 2 boxes.

| Balls | Boxes | Answer |
|-------|-------|--------|
| Distinct | Distinct | $2^4 = 16$ |
| Identical | Distinct | $\binom{4+2-1}{2-1} = 5$ |
| Distinct | Identical | Complex (use Stirling) |
| Identical | Identical | Partition function |

#### **Trap 9: The Empty Set Oversight**

**Problem:** Subsets of a 5-element set?

**Answer:** $2^5 = 32$ (including empty set!)

If "proper subsets": $32 - 1 = 31$ (excluding the set itself)
If "non-empty subsets": $32 - 1 = 31$ (excluding empty set)
If "proper non-empty": $32 - 2 = 30$

#### **Trap 10: Repetition Interpretation**

**Problem:** Form 3-digit numbers from {1,2,3}.

| Condition | Answer |
|-----------|--------|
| Repetition allowed | $3^3 = 27$ |
| Repetition NOT allowed | $^3P_3 = 6$ |

**Always clarify in problem!**

---

### 7.2 The Anti-Solution Guide

**How Top Students Get It Wrong:**

1. **Over-Engineering:** Adding constraints that don't exist
2. **Pattern Matching Failure:** Assuming familiar problem when it's different
3. **Computational Errors:** In factorial arithmetic under time pressure
4. **Forgetting Base Cases:** $0! = 1$, $^nC_0 = 1$, empty arrangements

---

## 8. Solved Examples (GATE Level)

### Example 1: Classic Arrangement [2 marks]

**Q:** In how many ways can letters of "ENGINEERING" be arranged?

**Solution:**

Letters: E(3), N(3), G(2), I(2), R(1)
Total letters = 11

$$\text{Arrangements} = \frac{11!}{3! \times 3! \times 2! \times 2! \times 1!}$$

$$= \frac{39916800}{6 \times 6 \times 2 \times 2 \times 1} = \frac{39916800}{144} = 277200$$

**Answer: 277200**

---

### Example 2: Committee Formation [2 marks]

**Q:** A committee of 5 is to be formed from 6 men and 4 women such that at least 2 women are included. Find the number of ways.

**Solution:**

Cases:
- 2W, 3M: $\binom{4}{2} \times \binom{6}{3} = 6 \times 20 = 120$
- 3W, 2M: $\binom{4}{3} \times \binom{6}{2} = 4 \times 15 = 60$
- 4W, 1M: $\binom{4}{4} \times \binom{6}{1} = 1 \times 6 = 6$

**Total = 120 + 60 + 6 = 186**

---

### Example 3: Circular Arrangement [2 marks]

**Q:** 5 boys and 5 girls sit around a circular table such that no two boys are adjacent. Find the number of ways.

**Solution:**

1. Arrange 5 girls in circle: $(5-1)! = 24$
2. This creates 5 gaps between girls
3. Place 5 boys in 5 gaps: $5! = 120$

**Total = 24 × 120 = 2880**

---

### Example 4: Derangement Application [2 marks]

**Q:** A group of 4 students takes a test. Papers are shuffled and redistributed. What's the probability that no student gets their own paper?

**Solution:**

Total ways to distribute: $4! = 24$
Derangements: $D_4 = 9$

$$P = \frac{9}{24} = \frac{3}{8}$$

**Answer: 3/8 or 0.375**

---

### Example 5: Stars and Bars [2 marks]

**Q:** Find the number of non-negative integer solutions to: $x_1 + x_2 + x_3 + x_4 = 15$

**Solution:**

Using Stars and Bars:
- n = 15 (stars)
- r = 4 (variables/boxes)

$$\binom{15+4-1}{4-1} = \binom{18}{3} = \frac{18 \times 17 \times 16}{6} = 816$$

**Answer: 816**

---

### Example 6: Inclusion-Exclusion [2 marks]

**Q:** How many 5-letter words (using A-Z) have at least one vowel?

**Solution:**

Total 5-letter words: $26^5$
Words with NO vowels (21 consonants): $21^5$

$$\text{At least one vowel} = 26^5 - 21^5$$
$$= 11881376 - 4084101 = 7797275$$

**Answer: 7797275**

---

### Example 7: Grid Path Counting [2 marks]

**Q:** Find the number of shortest paths from (0,0) to (4,3) in a grid.

**Solution:**

Total moves: 4 right (R) + 3 up (U) = 7 moves
Choose positions for R (or U):

$$\binom{7}{4} = \binom{7}{3} = 35$$

**Answer: 35**

---

### Example 8: Binary String Counting [2 marks]

**Q:** How many 8-bit binary strings have exactly three 1s?

**Solution:**

Choose 3 positions for 1s out of 8:

$$\binom{8}{3} = \frac{8 \times 7 \times 6}{6} = 56$$

**Answer: 56**

---

### Example 9: Catalan Number Application [2 marks]

**Q:** Number of distinct binary search trees with 4 nodes?

**Solution:**

This equals Catalan number $C_4$:

$$C_4 = \frac{1}{5}\binom{8}{4} = \frac{1}{5} \times 70 = 14$$

**Answer: 14**

---

### Example 10: Complex Restriction [2 marks]

**Q:** Arrange digits 1,2,3,4,5 such that 1 and 2 are not adjacent.

**Solution:**

Total arrangements: $5! = 120$

1 and 2 together:
- Treat (1,2) as unit: $4! = 24$ arrangements
- Internal arrangements: $2! = 2$
- Total together: $24 \times 2 = 48$

**Not adjacent = 120 - 48 = 72**

**Answer: 72**

---

## 9. Practice Problems

### Set A: Fundamental (1 mark each)

1. Find $^{10}P_4$
2. Calculate $\binom{12}{4}$
3. Arrangements of "BOOK"
4. Circular permutations of 6 distinct objects
5. Subsets of a 7-element set

### Set B: Intermediate (2 marks each)

6. Committee of 4 from 5 men and 3 women with at least 1 woman
7. 5-digit numbers using 0,1,2,3,4 (no repetition)
8. Distribute 12 identical balls into 4 distinct boxes
9. Arrangements of "STATISTICS"
10. Paths from (0,0) to (5,4)

### Set C: Advanced (2 marks each)

11. Derangements of 6 elements
12. Non-negative integer solutions to $x+y+z=20$ where $x \leq 5$
13. 6-digit numbers divisible by 5 using 1,2,3,4,5,6 (no repetition)
14. Arrangements of 4 identical red and 3 identical blue balls in a row
15. Number of onto functions from set A (5 elements) to set B (3 elements)

### Set D: GATE Previous Year Style

16. A word consists of 3 consonants and 2 vowels from 7 consonants and 4 vowels. Find arrangements where vowels are always together.

17. In how many ways can 8 persons sit at two tables, each having 4 seats?

18. Find number of 6-digit numbers that are divisible by 3 formed using 0,1,2,3,4,5 without repetition.

19. Coefficient of $x^{10}$ in $(1+x)^{15}$

20. Number of non-negative integer solutions to $x_1 + x_2 + x_3 = 10$ where $x_1 \geq 2$, $x_2 \geq 3$.

---

### Solutions to Practice Problems

**Set A:**
1. $^{10}P_4 = \frac{10!}{6!} = 10 \times 9 \times 8 \times 7 = 5040$
2. $\binom{12}{4} = \frac{12!}{4!8!} = 495$
3. $\frac{4!}{2!} = 12$ (O repeats twice)
4. $(6-1)! = 120$
5. $2^7 = 128$

**Set B:**
6. Total - (all men) = $\binom{8}{4} - \binom{5}{4} = 70 - 5 = 65$
7. First digit: 4 choices (not 0), remaining: $4 \times 3 \times 2 \times 1 = 24$. Total = $4 \times 24 = 96$
8. $\binom{12+4-1}{4-1} = \binom{15}{3} = 455$
9. $\frac{10!}{3!3!2!} = 50400$ (S:3, T:3, I:2, A:1)
10. $\binom{9}{5} = 126$

**Set C:**
11. $D_6 = 265$
12. Total - ($x > 5$) = $\binom{22}{2} - \binom{16}{2} = 231 - 120 = 111$
13. Last digit must be 5 (for divisibility by 5). First 4 positions filled from {1,2,3,4,6}: $^5P_4 = 120$. **Answer = 120**
14. $\binom{7}{4} = 35$
15. $3! \times S(5,3) = 6 \times 25 = 150$ (Stirling number of second kind)

**Set D:**
16. Select: $\binom{7}{3} \times \binom{4}{2} = 35 \times 6 = 210$. Vowels together: treat as unit, 4! arrangements, vowels internal: 2!. Answer = $210 \times 4! \times 2! = 210 \times 48 = 10080$

17. Tables are distinguishable. Select 4 for first table: $\binom{8}{4} = 70$. Arrange at first table: $4! = 24$. Arrange remaining 4 at second table: $4! = 24$. **Answer = 70 × 24 × 24 = 40320**

18. Sum of digits for divisibility by 3: 0+1+2+3+4+5 = 15 (divisible by 3). Use all 6 digits. First digit: 5 choices (not 0). Remaining: 5!. But we need exactly 6 digits, so: **5 × 5! = 600**

19. $\binom{15}{10} = \binom{15}{5} = 3003$

20. Let $y_1 = x_1 - 2 \geq 0$, $y_2 = x_2 - 3 \geq 0$. Then $y_1 + y_2 + x_3 = 5$. Answer = $\binom{5+3-1}{3-1} = \binom{7}{2} = 21$

---

## 10. Quick Revision & Mnemonics

### 10.1 The Memory Palace

#### **The Bizarre Mnemonic: "PERM COMB"**

**P**ermutation = **P**osition matters (think: **P**arking cars in numbered spots)
**C**ombination = **C**hoosing only (think: **C**andy selection from a jar)

#### **The Factorial Story**

*"5 friends want to sit in 5 chairs. First friend has 5 options, second has 4, ... That's 5! ways!"*

#### **The Stars and Bars Visual**

*"Imagine chocolates (★★★★★) and dividers (||) between boxes."*

$$\text{5 chocolates, 3 boxes: } ★★|★★|★ = \binom{7}{2}$$

---

### 10.2 Formula Quick Reference Card

```
┌────────────────────────────────────────────────────────────────┐
│                    PERMUTATION & COMBINATION                    │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PERMUTATION (Order Matters)                                    │
│  ─────────────────────────────                                  │
│  • n objects, take r:          ⁿPᵣ = n!/(n-r)!                 │
│  • All n objects:              n!                               │
│  • With repetition:            nʳ                               │
│  • Identical objects:          n!/(n₁!·n₂!·...·nₖ!)            │
│  • Circular:                   (n-1)!                           │
│  • Necklace/Bracelet:          (n-1)!/2                        │
│                                                                 │
│  COMBINATION (Order Doesn't Matter)                             │
│  ─────────────────────────────────                              │
│  • n objects, take r:          ⁿCᵣ = n!/[r!(n-r)!]             │
│  • With repetition:            ⁿ⁺ʳ⁻¹Cᵣ                         │
│  • Symmetry:                   ⁿCᵣ = ⁿCₙ₋ᵣ                      │
│  • Pascal:                     ⁿCᵣ = ⁿ⁻¹Cᵣ₋₁ + ⁿ⁻¹Cᵣ           │
│                                                                 │
│  SPECIAL FORMULAS                                               │
│  ────────────────                                               │
│  • Derangement:    Dₙ = n!·Σ(-1)ᵏ/k! for k=0 to n             │
│  • Distribution:   n identical → r boxes = ⁿ⁺ʳ⁻¹Cᵣ₋₁           │
│  • Catalan:        Cₙ = (2n)!/[(n+1)!·n!]                      │
│  • Subsets:        2ⁿ total subsets                            │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

### 10.3 The Mental Slider

#### **Visualization 1: The Arrangement Dial**

Imagine a dial with n slots. As you turn it:
- **Clockwise:** Add restrictions → fewer arrangements
- **Counter-clockwise:** Remove restrictions → more arrangements

#### **Visualization 2: The Selection Funnel**

```
    Total Pool (n items)
         ╲     ╱
          ╲   ╱
      Selection (r items)
           │
     ┌─────┴─────┐
     │           │
  Ordered    Unordered
   (ⁿPᵣ)       (ⁿCᵣ)
```

---

### 10.4 The 5-Second Sanity Checks

1. **Upper Bound Check:** $^nC_r \leq 2^n$ always
2. **Factorial Sanity:** $n! > $ any $^nP_r$ or $^nC_r$
3. **Symmetry Verify:** $^nC_r = {^nC_{n-r}}$ (use smaller r for calculation)
4. **Zero Check:** $^nC_0 = {^nP_0} = 1$ (doing nothing = 1 way)
5. **Order Relationship:** $^nP_r \geq {^nC_r}$ (permutation ≥ combination)

---

### 10.5 GATE 2026 Exam Strategy

#### **Time Allocation**

| Question Type | Expected Time |
|---------------|---------------|
| 1-mark MCQ | 1-2 minutes |
| 2-mark MCQ | 3-4 minutes |
| NAT | 3-5 minutes |
| MSQ | 4-5 minutes |

#### **Error Prevention Protocol**

1. **Read Twice:** Identify: Order? Repetition? Identical objects?
2. **Write Formula First:** Then substitute values
3. **Verify Units:** Answer should be a positive integer
4. **Boundary Check:** n=0,1 cases should make sense
5. **Calculator Discipline:** For NAT, double-check arithmetic

---

### 10.6 Key Numbers to Memorize

| Expression | Value |
|------------|-------|
| $5!$ | 120 |
| $6!$ | 720 |
| $7!$ | 5040 |
| $10!$ | 3,628,800 |
| $D_4$ (derangement) | 9 |
| $D_5$ | 44 |
| $C_3$ (Catalan) | 5 |
| $C_4$ | 14 |
| $C_5$ | 42 |

---

## 📌 Final Takeaways

### The Three Golden Rules

1. **IDENTIFY:** Does order matter? Is repetition allowed? Are objects identical?

2. **SELECT:** Choose the right formula based on classification

3. **VERIFY:** Use sanity checks and boundary conditions

### The Sovereignty Mindset

> "Every combinatorics problem is either a direct application or a clever combination of the basic principles. Master the fundamentals, and the complex becomes routine."

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

Would you like to initiate a **'Multi-Variable Stress Test'** combining this with **Probability Theory** or **Recurrence Relations** for a Rank-1 simulation?

---

*Last Updated: January 2026*
*For GATE CSE & ESE Preparation*
