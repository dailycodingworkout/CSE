# Permutation & Combination | GATE & ESE Comprehensive Study Material

> **The Atomic Truth:** *Counting distinct arrangements vs. selections.*

---

## Table of Contents

1. [Fundamental Principles](#1-fundamental-principles)
2. [Permutations](#2-permutations)
3. [Combinations](#3-combinations)
4. [Advanced Counting Techniques](#4-advanced-counting-techniques)
5. [Special Counting Problems](#5-special-counting-problems)
6. [GATE/ESE Specific Tricks & Shortcuts](#6-gateese-specific-tricks--shortcuts)
7. [Edge Cases & Common Traps](#7-edge-cases--common-traps)
8. [Practice Problems with Solutions](#8-practice-problems-with-solutions)
9. [Quick Reference Formulas](#9-quick-reference-formulas)
10. [Mental Models & Mnemonics](#10-mental-models--mnemonics)

---

## 1. Fundamental Principles

### 1.1 The Addition Principle (Rule of Sum)

**The Core Logic:**
If task A can be done in $m$ ways AND task B can be done in $n$ ways, and these tasks are **mutually exclusive** (cannot occur simultaneously), then:

$$\text{Total ways} = m + n$$

**Why It Works:**
- Events partition the sample space
- No overlap means no double-counting
- Think: "OR" scenarios → ADD

**Example:**
A student can go from home to college by bus (3 routes) OR by train (2 routes).
Total ways = $3 + 2 = 5$

**Edge Case Alert:**
If tasks are NOT mutually exclusive, use: $m + n - \text{(overlap)}$

---

### 1.2 The Multiplication Principle (Rule of Product)

**The Core Logic:**
If task A can be done in $m$ ways AND (after A) task B can be done in $n$ ways, and these tasks are **independent**, then:

$$\text{Total ways} = m \times n$$

**Why It Works:**
- Each choice for A pairs with every choice for B
- Creates a Cartesian product of possibilities
- Think: "AND" scenarios → MULTIPLY

**Example:**
A person has 4 shirts and 3 pants. Total outfits = $4 \times 3 = 12$

**The Golden Pivot:**
Always identify if tasks are **sequential and independent** or **mutually exclusive**.

---

### 1.3 The Bijection Principle

**Core Idea:** If you can establish a one-to-one correspondence between two sets, they have the same cardinality.

**Application:** Transform a difficult counting problem into an equivalent simpler one.

**Example:**
Number of binary strings of length $n$ = Number of subsets of an $n$-element set = $2^n$

Each bit position corresponds to including (1) or excluding (0) an element.

---

### 1.4 The Complement Principle

**The Formula:**
$$\text{Count(desired)} = \text{Count(total)} - \text{Count(undesired)}$$

**When to Use:**
- When "at least one" appears in the problem
- When counting exclusions is simpler than inclusions
- When negative constraints are easier to handle

**Example:**
Number of 4-digit numbers with at least one repeated digit:
- Total 4-digit numbers: $9 \times 10^3 = 9000$
- 4-digit numbers with all distinct digits: $9 \times 9 \times 8 \times 7 = 4536$
- Answer: $9000 - 4536 = 4464$

---

## 2. Permutations

### 2.1 Definition & Fundamental Formula

**Definition:** A permutation is an **ordered arrangement** of objects.

**Key Insight:** Order matters. $(A, B) \neq (B, A)$

**Formula for $n$ distinct objects taken $r$ at a time:**

$$P(n, r) = ^nP_r = \frac{n!}{(n-r)!}$$

**Why This Formula Works:**
- First position: $n$ choices
- Second position: $(n-1)$ choices
- ...
- $r$-th position: $(n-r+1)$ choices
- Product: $n \times (n-1) \times ... \times (n-r+1) = \frac{n!}{(n-r)!}$

---

### 2.2 Permutations of All Objects

$$P(n, n) = n!$$

**Proof:** $\frac{n!}{(n-n)!} = \frac{n!}{0!} = n!$ (since $0! = 1$)

**Critical Edge Case:** 
- $0! = 1$ by definition (empty product = multiplicative identity)
- This is not arbitrary; it ensures $P(n, n) = n!$ works correctly

---

### 2.3 Permutations with Repetition

**Scenario:** $n$ objects where some are identical.

**Formula:**
If we have $n$ objects with $n_1$ identical of type 1, $n_2$ identical of type 2, ..., $n_k$ identical of type $k$:

$$\text{Permutations} = \frac{n!}{n_1! \cdot n_2! \cdot ... \cdot n_k!}$$

where $n_1 + n_2 + ... + n_k = n$

**Why Divide?**
- Rearranging identical objects among themselves doesn't create new arrangements
- We "factor out" these indistinguishable swaps

**Example:**
Arrangements of "MISSISSIPPI":
- Total letters: 11
- M: 1, I: 4, S: 4, P: 2

$$\text{Answer} = \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39916800}{1 \times 24 \times 24 \times 2} = 34650$$

---

### 2.4 Permutations with Repetition Allowed

**Scenario:** Selecting $r$ items from $n$ types, with repetition allowed, where order matters.

$$\text{Permutations} = n^r$$

**Example:**
Number of 4-digit PINs using digits 0-9: $10^4 = 10000$

**GATE Trap:** For 4-digit numbers (not PINs), first digit ≠ 0:
$$9 \times 10^3 = 9000$$

---

### 2.5 Circular Permutations

**Core Concept:** Arrangements in a circle where rotations are considered identical.

**Formula for $n$ distinct objects:**
$$(n-1)!$$

**Why $(n-1)!$?**
- Fix one object to break rotational symmetry
- Arrange remaining $(n-1)$ objects: $(n-1)!$ ways

**Clockwise vs. Counter-clockwise Different:**
$$(n-1)!$$

**Clockwise = Counter-clockwise (e.g., beads on necklace):**
$$\frac{(n-1)!}{2}$$

**Example:**
Seating 6 people around a circular table:
- Standard circular: $(6-1)! = 120$
- If necklace/bracelet type: $\frac{120}{2} = 60$

---

### 2.6 Permutations with Restrictions

#### Case 1: Certain objects always together

**Method:** Treat the group as a single "super-object"

**Example:** 7 people where A and B must sit together:
1. Treat {A,B} as one unit → 6 units total
2. Arrange 6 units: $6!$
3. A and B can swap within unit: $2!$
4. Answer: $6! \times 2! = 720 \times 2 = 1440$

#### Case 2: Certain objects never together

**Method:** Complement or Slot Method

**Using Complement:**
- Total arrangements - Arrangements with them together

**Using Slot Method:**
1. Arrange other objects first
2. Place restricted objects in gaps

**Example:** 5 people where A and B must NOT sit together:
- Total: $5! = 120$
- A and B together: $4! \times 2! = 48$
- Answer: $120 - 48 = 72$

**Alternative (Slot Method):**
1. Arrange other 3: $3! = 6$
2. Gaps available: 4 (\_C\_D\_E\_)
3. Place A and B in 2 of 4 gaps: $P(4,2) = 12$
4. Answer: $6 \times 12 = 72$ ✓

#### Case 3: Relative order fixed

**Example:** 5 books on shelf, 3 specific books must maintain relative order (Math before Physics before Chemistry):

$$\frac{5!}{3!} = 20$$

**Why?** Total arrangements ÷ Internal arrangements of the fixed-order group.

---

### 2.7 Permutations with Constraints on Positions

**Example:** Arrangements of VOWEL such that vowels occupy only odd positions.

**Analysis:**
- Word: V-O-W-E-L (5 letters)
- Vowels: O, E (2)
- Consonants: V, W, L (3)
- Odd positions: 1, 3, 5 (3 positions)
- Even positions: 2, 4 (2 positions)

**Solution:**
1. Place vowels in 2 of 3 odd positions: $P(3,2) = 6$
2. Place consonants in remaining 3 positions: $3! = 6$
3. Answer: $6 \times 6 = 36$

---

## 3. Combinations

### 3.1 Definition & Fundamental Formula

**Definition:** A combination is an **unordered selection** of objects.

**Key Insight:** Order doesn't matter. $\{A, B\} = \{B, A\}$

**Formula for selecting $r$ objects from $n$ distinct objects:**

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

**Relationship with Permutations:**
$$\binom{n}{r} = \frac{P(n,r)}{r!}$$

**Why Divide by $r!$?**
Each combination corresponds to $r!$ permutations (all orderings of the same selection). We eliminate duplicates.

---

### 3.2 Properties of Combinations

**Property 1: Symmetry**
$$\binom{n}{r} = \binom{n}{n-r}$$

**Intuition:** Choosing $r$ items to include = Choosing $(n-r)$ items to exclude.

**Property 2: Pascal's Identity**
$$\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$$

**Proof Logic:** Consider element $x$:
- Combinations containing $x$: Choose remaining $(r-1)$ from $(n-1)$ = $\binom{n-1}{r-1}$
- Combinations not containing $x$: Choose all $r$ from $(n-1)$ = $\binom{n-1}{r}$

**Property 3: Sum of Row**
$$\sum_{r=0}^{n} \binom{n}{r} = 2^n$$

**Proof:** $(1+1)^n = \sum_{r=0}^{n} \binom{n}{r} \cdot 1^r \cdot 1^{n-r}$

**Property 4: Vandermonde's Identity**
$$\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k}$$

**Property 5:**
$$\binom{n}{0} + \binom{n}{2} + \binom{n}{4} + ... = \binom{n}{1} + \binom{n}{3} + \binom{n}{5} + ... = 2^{n-1}$$

**Proof:** Put $x = -1$ in $(1+x)^n$ and add with $(1+1)^n$.

---

### 3.3 Combinations with Repetition

**Problem:** Select $r$ items from $n$ types with unlimited supply of each type.

**Formula:**
$$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$$

**Why This Formula? (Stars and Bars)**

**The Bijection:**
Map each selection to a sequence of $r$ stars and $(n-1)$ bars.

**Example:** Select 4 fruits from {Apple, Banana, Cherry}
- Choosing 2 Apples, 1 Banana, 1 Cherry → ★★|★|★
- Total arrangements of 4 stars and 2 bars: $\binom{6}{2} = 15$

**General:** $r$ stars + $(n-1)$ bars = $(n+r-1)$ positions
Choose positions for bars (or stars): $\binom{n+r-1}{n-1}$ or $\binom{n+r-1}{r}$

---

### 3.4 Distribution Problems

#### Case 1: Distributing $n$ identical objects into $r$ distinct groups

**Without restrictions:**
$$\binom{n+r-1}{r-1}$$

**Each group gets at least 1:**
First give 1 to each group, then distribute remaining:
$$\binom{n-r+r-1}{r-1} = \binom{n-1}{r-1}$$

**Example:** Distribute 10 identical balls into 4 distinct boxes:
- Without restriction: $\binom{10+4-1}{4-1} = \binom{13}{3} = 286$
- Each box ≥ 1: $\binom{10-1}{4-1} = \binom{9}{3} = 84$

---

#### Case 2: Distributing $n$ distinct objects into $r$ distinct groups

**Without restrictions:** Each object has $r$ choices:
$$r^n$$

**Each group non-empty:** Surjective functions / Stirling numbers:
$$r! \cdot S(n, r)$$

where $S(n, r)$ is Stirling number of second kind.

**Using Inclusion-Exclusion:**
$$\sum_{i=0}^{r} (-1)^i \binom{r}{i} (r-i)^n$$

---

#### Case 3: Distributing $n$ distinct objects into $r$ identical groups

**All groups used:** Stirling number of second kind $S(n, r)$

**Groups may be empty:** Bell number $B_n = \sum_{k=0}^{n} S(n,k)$

---

#### Case 4: Distributing $n$ identical objects into $r$ identical groups

This is the **partition** of $n$ into at most $r$ parts.

**Example:** Partition 5 into at most 3 parts:
- 5 = 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
- Valid (≤ 3 parts): 5, 4+1, 3+2, 3+1+1, 2+2+1 = **5 ways**

---

### 3.5 Division into Groups

#### Distinct Groups:

**$n$ objects into groups of sizes $r_1, r_2, ..., r_k$:**
$$\frac{n!}{r_1! \cdot r_2! \cdot ... \cdot r_k!}$$

**Example:** Divide 10 people into groups of 5, 3, and 2:
$$\frac{10!}{5! \cdot 3! \cdot 2!} = 2520$$

---

#### Identical Groups:

**$n$ objects into $k$ identical groups of size $r$ each (where $n = kr$):**
$$\frac{n!}{(r!)^k \cdot k!}$$

**Example:** Divide 12 people into 4 identical groups of 3 each:
$$\frac{12!}{(3!)^4 \cdot 4!} = \frac{479001600}{1296 \times 24} = 15400$$

---

## 4. Advanced Counting Techniques

### 4.1 The Inclusion-Exclusion Principle

**Two Sets:**
$$|A \cup B| = |A| + |B| - |A \cap B|$$

**Three Sets:**
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

**General Formula:**
$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{i} |A_i| - \sum_{i<j} |A_i \cap A_j| + \sum_{i<j<k} |A_i \cap A_j \cap A_k| - ... + (-1)^{n+1}|A_1 \cap ... \cap A_n|$$

**Key Pattern:** Add single, subtract pairs, add triples, subtract quadruples...

---

### 4.2 Derangements

**Definition:** A derangement is a permutation where no element appears in its original position.

**Formula:**
$$D_n = n! \sum_{i=0}^{n} \frac{(-1)^i}{i!}$$

**Approximate Formula:**
$$D_n \approx \frac{n!}{e}$$

**Recurrence Relations:**
$$D_n = (n-1)(D_{n-1} + D_{n-2})$$
$$D_n = n \cdot D_{n-1} + (-1)^n$$

**Base Cases:** $D_0 = 1$, $D_1 = 0$, $D_2 = 1$

**Small Values Table:**

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| $D_n$ | 1 | 0 | 1 | 2 | 9 | 44 | 265 | 1854 |

**GATE Trick:** For quick calculation:
$$D_n = n! \left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + ... + \frac{(-1)^n}{n!}\right)$$

**Example:** Derangements of 4 elements:
$$D_4 = 4!\left(\frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right) = 24\left(\frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 24 \times \frac{9}{24} = 9$$

---

### 4.3 Generating Functions

**Ordinary Generating Function (OGF):**
$$G(x) = \sum_{n=0}^{\infty} a_n x^n$$

**Key OGFs:**

| Sequence | OGF |
|----------|-----|
| $1, 1, 1, ...$ | $\frac{1}{1-x}$ |
| $1, 2, 3, 4, ...$ | $\frac{1}{(1-x)^2}$ |
| $1, 0, 1, 0, 1, ...$ | $\frac{1}{1-x^2}$ |
| $\binom{n}{0}, \binom{n}{1}, ...$ | $(1+x)^n$ |
| $\binom{n+k-1}{k}$ for $k \geq 0$ | $\frac{1}{(1-x)^n}$ |

**Application:** Coefficient of $x^r$ in product of GFs gives combinations.

**Example:** Number of ways to select $r$ items from $n$ types (≥0 of each):
$$\text{Coefficient of } x^r \text{ in } \left(\frac{1}{1-x}\right)^n = \binom{n+r-1}{r}$$

---

### 4.4 Recurrence Relations for Counting

**Fibonacci-like Counting:**

**Problem:** Number of binary strings of length $n$ with no consecutive 1s.

**Recurrence:** $f(n) = f(n-1) + f(n-2)$

**Logic:**
- String ending in 0: Append 0 to any valid string of length $(n-1)$
- String ending in 1: Must end in "01", so append "01" to any valid string of length $(n-2)$

**Solution:** $f(n) = F_{n+2}$ (Fibonacci number)

---

### 4.5 Catalan Numbers

**Definition:**
$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)! \cdot n!}$$

**Recurrence:**
$$C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-1-i}, \quad C_0 = 1$$

**First few values:** 1, 1, 2, 5, 14, 42, 132, 429, 1430, ...

**Applications (All count $C_n$):**

1. **Balanced parentheses:** Sequences of $n$ pairs of matched parentheses
2. **Binary trees:** Number of distinct binary trees with $n$ nodes
3. **Full binary trees:** Trees with $n+1$ leaves
4. **Dyck paths:** Paths from $(0,0)$ to $(2n,0)$ using $(1,1)$ and $(1,-1)$ never going below x-axis
5. **Triangulations:** Ways to triangulate a convex $(n+2)$-gon
6. **Non-crossing partitions:** of set $\{1, 2, ..., n\}$
7. **Mountain ranges:** with $n$ up-strokes and $n$ down-strokes
8. **Stack-sortable permutations:** Permutations of $n$ elements sortable by a stack

---

## 5. Special Counting Problems

### 5.1 Committee/Selection Problems

**Type 1: Simple Selection**
Select $r$ from $n$ people: $\binom{n}{r}$

**Type 2: With Mandatory Inclusions**
Select 5 from 12 people where 2 specific people must be included:
$$\binom{10}{3} = 120$$
(Already selected 2, choose remaining 3 from 10)

**Type 3: With Exclusions**
Select 5 from 12 where 2 specific people cannot both be selected:
- Total: $\binom{12}{5}$
- Both excluded people included: $\binom{10}{3}$
- Answer: $\binom{12}{5} - \binom{10}{3} = 792 - 120 = 672$

**Type 4: From Multiple Groups**
Select 4 from 5 boys and 4 girls, at least 2 boys:
- 2B + 2G: $\binom{5}{2}\binom{4}{2} = 60$
- 3B + 1G: $\binom{5}{3}\binom{4}{1} = 40$
- 4B + 0G: $\binom{5}{4}\binom{4}{0} = 5$
- Total: $60 + 40 + 5 = 105$

---

### 5.2 Grid Path Counting

**Problem:** Count paths from $(0,0)$ to $(m,n)$ using only Right (R) and Up (U) moves.

**Solution:**
$$\binom{m+n}{m} = \binom{m+n}{n}$$

**Why?** 
- Total moves: $m + n$
- Choose which $m$ are Right (rest are Up)

**With Obstacles:**
Use the **Reflection Principle** or **Lindström-Gessel-Viennot Lemma**.

**Paths avoiding $(a, b)$:**
Total paths - Paths through $(a, b)$
$$\binom{m+n}{m} - \binom{a+b}{a} \cdot \binom{(m-a)+(n-b)}{m-a}$$

---

### 5.3 Integer Solutions (Non-negative)

**Problem:** Find number of non-negative integer solutions to:
$$x_1 + x_2 + ... + x_r = n$$

**Solution:** Stars and Bars
$$\binom{n+r-1}{r-1}$$

**With constraints $x_i \geq a_i$:**
Substitute $y_i = x_i - a_i$, solve for non-negative $y_i$:
$$y_1 + y_2 + ... + y_r = n - (a_1 + a_2 + ... + a_r)$$

**With upper bounds $x_i \leq b_i$:** Use Inclusion-Exclusion.

---

### 5.4 Probability Connection

**Key Formula:**
$$P(\text{event}) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}$$

**Common Applications:**

**Birthday Problem:** Probability that at least 2 of $n$ people share a birthday:
$$P = 1 - \frac{365!}{365^n \cdot (365-n)!}$$

**Matching Problem (Derangement):** Probability of no fixed points:
$$P = \frac{D_n}{n!} \to \frac{1}{e} \approx 0.368 \text{ as } n \to \infty$$

---

## 6. GATE/ESE Specific Tricks & Shortcuts

### 6.1 The 5-Second Sanity Checks

**Check 1: Boundary Verification**
Always verify your formula at extreme values:
- $n = r$: Should give 1 for combinations, $n!$ for permutations
- $r = 0$: Should give 1 (empty selection/arrangement)
- $r = 1$: Should give $n$

**Check 2: Symmetry Check**
$\binom{n}{r} = \binom{n}{n-r}$

If $\binom{100}{97}$ appears, compute $\binom{100}{3} = \frac{100 \times 99 \times 98}{6} = 161700$

**Check 3: Pascal's Triangle Verification**
For small values, verify using Pascal's identity.

---

### 6.2 Rapid Calculation Techniques

**Technique 1: Cancellation First**
For $\binom{20}{3}$:
$$\binom{20}{3} = \frac{20 \times 19 \times 18}{3 \times 2 \times 1}$$

Cancel: $\frac{20}{2} = 10$, $\frac{18}{3} = 6$

Answer: $10 \times 19 \times 6 = 1140$

**Technique 2: Factorials Shortcut**
$\frac{n!}{(n-r)!}$ = Product of $r$ consecutive integers starting from $n$ going down.

**Technique 3: For "At Least" Problems**
Use complement: $P(\text{at least 1}) = 1 - P(\text{none})$

---

### 6.3 Pattern Recognition

**Pattern 1: Power of 2**
If answer involves all subsets → $2^n$

**Pattern 2: Stirling Connection**
Onto functions from $n$-set to $r$-set → Stirling number × $r!$

**Pattern 3: Catalan Appearance**
If problem involves:
- Balanced structures
- Binary trees
- Non-crossing patterns
- Recursive halving

→ Think Catalan numbers

**Pattern 4: Derangement Cue**
"No element in original position" → Derangement

---

### 6.4 MSQ (Multiple Select Question) Strategy

**Rule 1: Partial Credit Awareness**
In GATE MSQ, partial marking exists. Verify each option independently.

**Rule 2: Contradiction Check**
If two options contradict each other, at least one is wrong.

**Rule 3: Extreme Case Testing**
Test each option with $n=1$ or $r=0$ edge cases.

---

### 6.5 NAT (Numerical Answer Type) Precision

**Precision Rules for GATE:**
- Usually integers for counting problems
- If decimal, typically round to 2-3 decimal places
- Watch for "exact value" vs "approximate"

**Common Precision Traps:**
- $e^{-1} \approx 0.368$ (not 0.37)
- $\frac{1}{\sqrt{2}} \approx 0.707$ (not 0.71)
- Derangement ratio → $\frac{1}{e} \approx 0.3679$

---

## 7. Edge Cases & Common Traps

### 7.1 The Zero Factorial Trap

**$0! = 1$, not 0.**

This is crucial for:
- $\binom{n}{n} = \frac{n!}{n! \cdot 0!} = 1$ ✓
- $\binom{n}{0} = \frac{n!}{0! \cdot n!} = 1$ ✓
- $P(n, n) = \frac{n!}{0!} = n!$ ✓

---

### 7.2 The Empty Set Trap

**The empty set is a valid selection.**

$\binom{n}{0} = 1$ (There's exactly one way to choose nothing)

Total subsets of $n$-element set = $2^n$ (includes empty set)

---

### 7.3 The Overcounting Trap

**Common Scenario:** Counting same arrangement multiple times.

**Example Error:** "Distribute 4 identical balls into 2 identical boxes"

**Wrong approach:** $\binom{4+2-1}{2-1} = 5$ (This is for distinct boxes!)

**Correct approach:** Enumerate partitions of 4: 
- (4,0), (3,1), (2,2) = 3 ways

---

### 7.4 The Circular vs. Linear Trap

**Linear arrangement of $n$:** $n!$

**Circular arrangement of $n$:** $(n-1)!$

**GATE Trap:** Arranging people around a table that can also be flipped (like a turntable):
$$\frac{(n-1)!}{2}$$

---

### 7.5 The "At Least" vs. "Exactly" Trap

**"At least $k$"** → Use complement or sum from $k$ to max

**"Exactly $k$"** → Single term calculation

**"At most $k$"** → Sum from 0 to $k$ or complement of "at least $k+1$"

---

### 7.6 The Distinct vs. Identical Trap

**Always identify:**
- Are objects identical or distinct?
- Are positions/groups identical or distinct?

**Four-way Classification:**

| Objects | Groups | Method |
|---------|--------|--------|
| Distinct | Distinct | $r^n$ or Stirling |
| Distinct | Identical | Stirling number $S(n,r)$ |
| Identical | Distinct | Stars and bars |
| Identical | Identical | Partition function |

---

### 7.7 The Repetition Allowed Trap

**Without repetition:** Standard permutation/combination

**With repetition:** 
- Permutation: $n^r$
- Combination: $\binom{n+r-1}{r}$

**GATE Trap:** Problem says "digits can repeat" but asks for a "number" (first digit ≠ 0).

---

### 7.8 The Relative Position Trap

**"A comes before B"** in a sequence of $n$ elements:
$$\frac{n!}{2}$$

**Why?** By symmetry, exactly half the arrangements have A before B.

---

## 8. Practice Problems with Solutions

### Problem 1: Word Arrangements (Medium)

**Question:** How many arrangements of MATHEMATICS have all vowels together?

**Solution:**
- Vowels: A, E, A, I (4 letters with A repeated)
- Consonants: M, T, H, M, T, C, S (7 letters with M, T repeated)

**Step 1:** Treat vowels as one unit.
Total units: 7 consonants + 1 vowel block = 8 units

**Step 2:** Arrange 8 units with M, T repeated:
$$\frac{8!}{2! \cdot 2!} = \frac{40320}{4} = 10080$$

**Step 3:** Arrange vowels within block (A repeated):
$$\frac{4!}{2!} = 12$$

**Answer:** $10080 \times 12 = 120960$

---

### Problem 2: Committee Formation (Medium)

**Question:** Form a committee of 5 from 6 men and 4 women, with at least 3 men. How many ways?

**Solution:**
- Case 1: 3M + 2W = $\binom{6}{3}\binom{4}{2} = 20 \times 6 = 120$
- Case 2: 4M + 1W = $\binom{6}{4}\binom{4}{1} = 15 \times 4 = 60$
- Case 3: 5M + 0W = $\binom{6}{5}\binom{4}{0} = 6 \times 1 = 6$

**Answer:** $120 + 60 + 6 = 186$

---

### Problem 3: Integer Solutions (Medium-Hard)

**Question:** Find non-negative integer solutions to $x + y + z = 20$ where $x \leq 5$.

**Solution:**
Using complement:
- Total solutions (no upper bound): $\binom{20+3-1}{3-1} = \binom{22}{2} = 231$
- Solutions where $x \geq 6$: Substitute $x' = x - 6$, so $x' + y + z = 14$
  - Count: $\binom{14+3-1}{3-1} = \binom{16}{2} = 120$

**Answer:** $231 - 120 = 111$

---

### Problem 4: Derangement Application (Hard)

**Question:** 5 distinct letters are placed in 5 distinct envelopes. Find the probability that exactly 2 letters are in correct envelopes.

**Solution:**
- Choose which 2 are correct: $\binom{5}{2} = 10$
- Remaining 3 must all be wrong: $D_3 = 2$
- Total favorable: $10 \times 2 = 20$
- Total arrangements: $5! = 120$

**Answer:** $P = \frac{20}{120} = \frac{1}{6}$

---

### Problem 5: Grid Path with Constraint (Hard)

**Question:** Paths from $(0,0)$ to $(6,6)$ not passing through $(3,3)$?

**Solution:**
- Total paths: $\binom{12}{6} = 924$
- Paths through $(3,3)$: $\binom{6}{3} \times \binom{6}{3} = 20 \times 20 = 400$

**Answer:** $924 - 400 = 524$

---

### Problem 6: Circular Arrangement with Constraints (Hard)

**Question:** 8 people sit around a circular table. 3 specific people must not sit together. How many arrangements?

**Solution:**
**Method:** Complement (easier than direct)

- Total circular arrangements: $(8-1)! = 5040$
- Arrangements where 3 are together: 
  - Treat 3 as one unit → 6 units
  - Circular arrangements: $(6-1)! = 120$
  - Internal arrangements of 3: $3! = 6$
  - Subtotal: $120 \times 6 = 720$

**Answer:** $5040 - 720 = 4320$

---

### Problem 7: Distribution Problem (Hard)

**Question:** Distribute 6 distinct balls into 3 identical boxes such that no box is empty.

**Solution:**
This is Stirling number of second kind $S(6, 3)$.

**Using formula:**
$$S(n,r) = \frac{1}{r!}\sum_{k=0}^{r}(-1)^k\binom{r}{k}(r-k)^n$$

$$S(6,3) = \frac{1}{6}\left[\binom{3}{0}3^6 - \binom{3}{1}2^6 + \binom{3}{2}1^6 - \binom{3}{3}0^6\right]$$

$$= \frac{1}{6}\left[729 - 192 + 3 - 0\right] = \frac{540}{6} = 90$$

**Answer:** 90

---

### Problem 8: Multinomial Coefficient (Medium)

**Question:** In how many ways can 10 students be divided into 3 groups of sizes 3, 3, and 4?

**Solution:**
Since two groups have the same size (3), and groups are distinguishable by size difference:

**If groups labeled (A: 3, B: 3, C: 4):**
$$\frac{10!}{3! \cdot 3! \cdot 4!} = \frac{3628800}{6 \times 6 \times 24} = 4200$$

**If the two size-3 groups are identical:**
$$\frac{4200}{2!} = 2100$$

**Clarification needed** — if groups are purely "3,3,4" with no labels on equal-sized groups, answer is 2100.

---

### Problem 9: Catalan Application (Hard)

**Question:** Number of ways to triangulate a convex hexagon (6 vertices)?

**Solution:**
For an $(n+2)$-gon, the answer is $C_n$ (Catalan number).

Here $n + 2 = 6 \Rightarrow n = 4$

$$C_4 = \frac{1}{5}\binom{8}{4} = \frac{70}{5} = 14$$

**Answer:** 14

---

### Problem 10: Complex Constraint (GATE Level)

**Question:** 5-digit numbers divisible by 3, using digits 1, 2, 3, 4, 5, 6 without repetition?

**Solution:**
**Divisibility by 3:** Sum of digits ≡ 0 (mod 3)

Available digits: 1, 2, 3, 4, 5, 6
- Sum mod 3: 1≡1, 2≡2, 3≡0, 4≡1, 5≡2, 6≡0

**Group by residue:**
- Residue 0: {3, 6}
- Residue 1: {1, 4}
- Residue 2: {2, 5}

**Need 5 digits with sum ≡ 0 (mod 3).**

**Valid combinations (choose 5 from 6, excluding one):**
- Exclude 1: Sum = 2+3+4+5+6 = 20 ≡ 2 ✗
- Exclude 2: Sum = 1+3+4+5+6 = 19 ≡ 1 ✗
- Exclude 3: Sum = 1+2+4+5+6 = 18 ≡ 0 ✓
- Exclude 4: Sum = 1+2+3+5+6 = 17 ≡ 2 ✗
- Exclude 5: Sum = 1+2+3+4+6 = 16 ≡ 1 ✗
- Exclude 6: Sum = 1+2+3+4+5 = 15 ≡ 0 ✓

**Valid sets:** {1,2,4,5,6} and {1,2,3,4,5}

**Each set gives:** $5! = 120$ arrangements

**Answer:** $120 + 120 = 240$

---

## 9. Quick Reference Formulas

### Basic Formulas

| Concept | Formula |
|---------|---------|
| Permutation | $P(n,r) = \frac{n!}{(n-r)!}$ |
| Combination | $C(n,r) = \frac{n!}{r!(n-r)!}$ |
| Permutation with repetition | $\frac{n!}{n_1! \cdot n_2! \cdot ... \cdot n_k!}$ |
| Combination with repetition | $\binom{n+r-1}{r}$ |
| Circular permutation | $(n-1)!$ |
| Circular (reversible) | $\frac{(n-1)!}{2}$ |

### Advanced Formulas

| Concept | Formula |
|---------|---------|
| Derangement | $D_n = n!\sum_{i=0}^{n}\frac{(-1)^i}{i!}$ |
| Catalan Number | $C_n = \frac{1}{n+1}\binom{2n}{n}$ |
| Stirling (2nd kind) | $S(n,k) = k \cdot S(n-1,k) + S(n-1,k-1)$ |
| Bell Number | $B_n = \sum_{k=0}^{n}S(n,k)$ |
| Grid Paths | $\binom{m+n}{m}$ |

### Key Identities

| Identity | Formula |
|----------|---------|
| Pascal's | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ |
| Symmetry | $\binom{n}{r} = \binom{n}{n-r}$ |
| Sum of row | $\sum_{r=0}^{n}\binom{n}{r} = 2^n$ |
| Vandermonde | $\binom{m+n}{r} = \sum_{k}\binom{m}{k}\binom{n}{r-k}$ |

### Distribution Summary

| Objects | Groups | Empty OK | Formula |
|---------|--------|----------|---------|
| Identical | Distinct | Yes | $\binom{n+r-1}{r-1}$ |
| Identical | Distinct | No | $\binom{n-1}{r-1}$ |
| Distinct | Distinct | Yes | $r^n$ |
| Distinct | Distinct | No | $r! \cdot S(n,r)$ |
| Distinct | Identical | No | $S(n,r)$ |
| Identical | Identical | - | Partition $p(n,r)$ |

---

## 10. Mental Models & Mnemonics

### 10.1 The PACE Framework

**P**ermutation = **P**osition matters = **P**roduct descending
**A**rrangement = **A**ll orderings count
**C**ombination = **C**hoice only = **C**ancelation by $r!$
**E**xclusion = **E**liminate overlaps (Inclusion-Exclusion)

---

### 10.2 The Box-Ball Visualizer

**Mental Model:** Always visualize the problem as putting balls in boxes.

- **Balls = Objects being distributed**
- **Boxes = Groups/positions receiving them**

Ask:
1. Are balls identical or distinct? (Do they have names?)
2. Are boxes identical or distinct? (Do they have labels?)
3. Can boxes be empty?

---

### 10.3 The Stars-and-Bars Cinema

**Mental Image:** Stars ★ are identical candies. Bars | are dividers between friends.

To share 7 candies among 3 friends:
- Visualize: ★★|★★★|★★
- Count arrangements of 7 stars and 2 bars: $\binom{9}{2} = 36$

---

### 10.4 The Catalan Staircase

**Mental Image:** You're climbing a staircase where:
- You can only step UP (+1) or DOWN (-1)
- You can never go below ground level
- You must return to ground at the end

The number of valid paths with $n$ UPs and $n$ DOWNs = $C_n$

---

### 10.5 The Derangement Shuffle

**Mental Image:** A party where everyone throws their hat in a pile.

- $D_n$ = Ways for everyone to get someone else's hat
- Probability → $\frac{1}{e} \approx 37\%$ get their own hat on average

**Mnemonic:** "Deranged = Displaced = Nobody home"

---

### 10.6 The Multiplication-Addition Detector

**Key Question:** "AND" or "OR"?

- **Sequential tasks (AND):** MULTIPLY
- **Alternative choices (OR):** ADD

**Signal Words:**
- "then", "followed by", "and then" → MULTIPLY
- "or", "either", "alternatively" → ADD

---

### 10.7 The Complementary Glasses

**When to Use Complement?**

Look for keywords:
- "At least one"
- "Not all"
- "Some but not all"

**Formula:** Desired = Total − Opposite

---

### 10.8 The Division Checker

Before submitting, verify with small cases:

**Permutation check:** $P(3,2) = 3 \times 2 = 6$ ✓
**Combination check:** $\binom{4}{2} = 6$ ✓
**Derangement check:** $D_3 = 2$ (BAC, CAB for ABC) ✓

---

## Appendix: Common GATE Questions Classified

### Type A: Arrangement with Restrictions
- Words with vowels together/separated
- People with constraints around a table
- Books on shelf with conditions

### Type B: Selection with Conditions
- Committee formation with gender/skill constraints
- Choosing items with mandatory inclusions/exclusions

### Type C: Distribution
- Balls into boxes (all 4 variations)
- Dividing people into teams

### Type D: Counting Paths
- Grid problems
- Staircase problems (Catalan)

### Type E: Special Numbers
- Derangements
- Catalan applications
- Stirling/Bell numbers

### Type F: Probability Applications
- Birthday problem
- Matching/hat problem
- Random selection

---

**Logic Singularity verified for GATE/ESE 2026 Standards. Mastery Level: Sovereign.**

---

*Document Version: 1.0 | Last Updated: January 2026*
*For GATE CSE, ESE, and competitive exam preparation*
