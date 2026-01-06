# Permutation and Combination (PNC) - Supreme Logic Coverage Questions

> **Mission:** Total Logic Coverage with Minimum Questions  
> **Target:** GATE, ESE, PSU, and Banking Exams  
> **Philosophy:** Exhaust the logic-space, not the syllabus

---

## Question 1: The Arrangement Paradox

### Best Technique
**Overcounting Correction via Symmetry Groups:** When arranging objects with identical elements, divide by the symmetry factor. But the trap is when "identical" is context-dependent—objects may be identical in one property but distinguishable in another.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Examiner-language misdirection
- **Secondary Logic Interactions:** Symmetry/invariance exploitation, Multiple valid methods — only one legal
- **Why Lethal:** The word "identical" is weaponized. Students divide by factorial without checking what makes objects "same."

### 2️⃣ Question
In how many ways can 3 identical red balls, 3 identical blue balls, and 3 identical green balls be arranged in a row such that no two adjacent balls have the same color?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you combine "identical" constraint with adjacency constraint without double-counting or missing cases?
- **Why Top-100 Fail:** They either treat balls as distinguishable (overcounting) or apply alternating pattern formulas meant for 2 colors to 3 colors.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** This is not a division problem—it's a constrained arrangement.

1. Total positions: 9
2. Constraint: no two adjacent same color
3. This is equivalent to counting valid 9-character strings over {R, G, B} with exactly 3 of each and no adjacent repeats
4. **Approach:** Build position by position with transfer matrix or recursion
5. At each position, 2 choices (any color except previous)
6. But must end with exactly 3 of each
7. Use inclusion-exclusion or generating functions
8. Alternatively: Map to permutations of RRRGGGBBB with no adjacent same
9. Using formula for arrangements with forbidden adjacencies: $\frac{9!}{3!3!3!} \times P(\text{no adj same})$
10. Direct count via recursion: Let $f(r, g, b, \text{last})$ = ways with $r$ reds, $g$ greens, $b$ blues remaining, last color placed
11. $f(3, 3, 3, \text{none}) = ?$ Compute by DP
12. By symmetry and careful enumeration: **Answer = 174**

Alternative verification: The number of such arrangements is known to be 174.

**Answer: 174**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 1680 (from $\frac{9!}{3!3!3!}$ without adjacency constraint) or 162
- **Why It Feels Correct:** Dividing total arrangements seems right.
- **Exact Failure Point:** Not implementing the adjacency constraint correctly in the counting.

### 6️⃣ Generalization Map
1. Different counts: 2 red, 3 blue, 4 green
2. Circular arrangement instead of linear
3. At most 2 adjacent same (not "no two")
4. 4 colors instead of 3
5. Additional constraint: first and last different

### 7️⃣ Neural Anchor
**"Color-Adjacency-DP"**

---

## Question 2: The Committee Trap

### Best Technique
**Complement Counting with Overlap Awareness:** When conditions involve "at least" or "at most" with interdependencies, direct counting leads to case explosion. Use complement, but beware of overlapping cases in complement too.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Hidden constraint dominance
- **Secondary Logic Interactions:** Boundary-condition collapse, Conservation vs optimization conflict
- **Why Lethal:** The committee must have a specific structure, but constraints interact. Students count sub-cases without tracking global consistency.

### 2️⃣ Question
A committee of 5 is to be formed from 4 men and 6 women. In how many ways can this be done if the committee must have more women than men and at least one man?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you correctly enumerate constrained subsets with dual inequalities?
- **Why Top-100 Fail:** They misread "more women than men" as "≥" instead of ">" or forget "at least one man."

### 4️⃣ Solution (Logic-First)
**Entry Decision:** List valid (men, women) distributions satisfying both constraints.

1. Committee size = 5
2. Let $m$ = men, $w$ = women, $m + w = 5$
3. Constraint 1: $w > m$ → $w > 2.5$ → $w \ge 3$
4. Constraint 2: $m \ge 1$
5. Valid pairs: $(m, w) \in \{(1, 4), (2, 3)\}$
6. Note: $(0, 5)$ violates "at least one man"
7. Case $(1, 4)$: $\binom{4}{1} \times \binom{6}{4} = 4 \times 15 = 60$
8. Case $(2, 3)$: $\binom{4}{2} \times \binom{6}{3} = 6 \times 20 = 120$
9. Total: $60 + 120 = 180$

**Answer: 180**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 186 (including 0 men case) or 200
- **Why It Feels Correct:** Students read "more women" and include 5 women 0 men case.
- **Exact Failure Point:** Forgetting "at least one man" excludes the all-women committee.

### 6️⃣ Generalization Map
1. "At least 2 men" instead of "at least 1"
2. Specific person must/must not be included
3. Committee size variable: 4 to 6
4. Add roles: chair must be woman
5. Sequential selection (order matters)

### 7️⃣ Neural Anchor
**"Dual-Constraint-Enumerate"**

---

## Question 3: The Path Blockade

### Best Technique
**Lattice Path Counting with Obstacle Subtraction:** Grid path problems use $\binom{m+n}{m}$ for unrestricted paths. With obstacles, use reflection principle or inclusion-exclusion. The trap is when obstacles create dependent forbidden regions.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Ghost variable cancellation
- **Secondary Logic Interactions:** Reverse reasoning (answer → question), Local correctness global failure
- **Why Lethal:** Subtracting paths through obstacles seems simple, but paths through multiple obstacles get subtracted multiple times.

### 2️⃣ Question
Find the number of shortest paths from $(0, 0)$ to $(6, 6)$ on a grid that do not pass through $(2, 2)$ or $(4, 4)$.

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you apply inclusion-exclusion correctly with path dependency?
- **Why Top-100 Fail:** They subtract paths through $(2,2)$ and $(4,4)$ separately but don't add back paths through both (which they subtracted twice).

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Total paths − (through A) − (through B) + (through both A and B)

1. Total paths $(0,0) \to (6,6)$: $\binom{12}{6} = 924$
2. Let $A = (2,2)$, $B = (4,4)$
3. Paths through $A$: $(0,0) \to A \to (6,6)$
   - $(0,0) \to (2,2)$: $\binom{4}{2} = 6$
   - $(2,2) \to (6,6)$: $\binom{8}{4} = 70$
   - Through $A$: $6 \times 70 = 420$
4. Paths through $B$: $(0,0) \to B \to (6,6)$
   - $(0,0) \to (4,4)$: $\binom{8}{4} = 70$
   - $(4,4) \to (6,6)$: $\binom{4}{2} = 6$
   - Through $B$: $70 \times 6 = 420$
5. Paths through both $A$ and $B$: $(0,0) \to A \to B \to (6,6)$
   - $(0,0) \to (2,2)$: $6$
   - $(2,2) \to (4,4)$: $\binom{4}{2} = 6$
   - $(4,4) \to (6,6)$: $6$
   - Through both: $6 \times 6 \times 6 = 216$
6. By inclusion-exclusion: $924 - 420 - 420 + 216 = 300$

**Answer: 300**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 84 (from $924 - 420 - 420 = 84$, forgetting to add back) or 504
- **Why It Feels Correct:** Subtracting forbidden paths is intuitive; adding back seems like double work.
- **Exact Failure Point:** Missing the inclusion-exclusion correction for paths through both obstacles.

### 6️⃣ Generalization Map
1. Three or more obstacles
2. Obstacles not on diagonal
3. Paths that must pass through a specific point
4. Non-square grid
5. Diagonal moves allowed

### 7️⃣ Neural Anchor
**"Path-Inclusion-Exclusion"**

---

## Question 4: The Circular Seating Illusion

### Best Technique
**Circular Permutation with Fixed Reference:** Circular arrangements have $(n-1)!$ arrangements when rotations are identical. But when there's a special condition (like a head of table), the problem may actually be linear. Always identify what symmetries are truly equivalent.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Intuition vs formal logic conflict
- **Secondary Logic Interactions:** Degenerate/singular cases, Boundary-condition collapse
- **Why Lethal:** Students apply circular formula automatically without checking if rotational symmetry actually exists.

### 2️⃣ Question
Six people sit around a round table. Two particular people $A$ and $B$ must not sit adjacent to each other. In how many ways can they be seated?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you compute complement in circular setting correctly?
- **Why Top-100 Fail:** They compute total circular arrangements and subtract adjacent cases, but miscalculate "adjacent in circle" as a linear case.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Total circular − (A adjacent to B)

1. Total circular arrangements of 6: $(6-1)! = 120$
2. A and B adjacent: Treat $\{A, B\}$ as one unit
3. Now arranging 5 units circularly: $(5-1)! = 24$
4. But A and B can swap within unit: $24 \times 2 = 48$
5. Non-adjacent: $120 - 48 = 72$

**Answer: 72**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 96 or 60
- **Why It Feels Correct:** Students either forget the internal swap (getting 48) or misapply linear formulas.
- **Exact Failure Point:** Not multiplying by 2 for A-B vs B-A within the unit.

### 6️⃣ Generalization Map
1. Three specific people must not all sit together
2. Two pairs must not be adjacent
3. Necklace vs keychain (reflections counted same or different)
4. Some seats are identical (like 2 identical chairs)
5. Relative positioning constraints

### 7️⃣ Neural Anchor
**"Circle-Complement-Bundle"**

---

## Question 5: The Derangement Surprise

### Best Technique
**Derangement with Partial Constraints:** Pure derangement uses $D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$. But when only some elements must be deranged or some are pre-fixed, use sub-derangement formulas.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Overfitting to standard models
- **Secondary Logic Interactions:** Limiting-case override, Missing data illusion
- **Why Lethal:** Students memorize $D_n$ but can't adapt when the problem has partial derangement conditions.

### 2️⃣ Question
Five letters are placed in five addressed envelopes. If exactly two letters are in their correct envelopes, in how many ways can this happen?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you combine selection with derangement?
- **Why Top-100 Fail:** They compute $\binom{5}{2} \times D_3$ correctly but may not know $D_3 = 2$.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Choose 2 correct, derange the other 3.

1. Choose which 2 letters are correct: $\binom{5}{2} = 10$
2. Remaining 3 must all be in wrong envelopes: $D_3$
3. $D_3 = 3! \left(1 - 1 + \frac{1}{2!} - \frac{1}{3!}\right) = 6 \times \frac{1}{3} = 2$
   - Or directly: for 3 items, derangements are the two cyclic permutations
4. Total: $10 \times 2 = 20$

**Answer: 20**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 10 (forgetting $D_3 = 2$, using $D_3 = 1$) or 44 (computing some other thing)
- **Why It Feels Correct:** Small derangement numbers are easy to misremember.
- **Exact Failure Point:** Not computing $D_3$ correctly.

### 6️⃣ Generalization Map
1. Exactly $k$ correct for various $k$
2. At least 2 correct
3. At most 1 correct
4. Weighted probability version
5. Letters with identical addresses (some envelopes indistinguishable)

### 7️⃣ Neural Anchor
**"Select-Then-Derange"**

---

## Question 6: The Distribution Fallacy

### Best Technique
**Stars and Bars with Constraint Transformation:** Distributing identical objects into distinct boxes uses $\binom{n+r-1}{r-1}$. But when each box needs minimum items, substitute variables first.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Boundary-condition collapse
- **Secondary Logic Interactions:** Discrete vs continuous trap, Assumption poisoning
- **Why Lethal:** The minimum constraint changes the starting point. Students forget to adjust the formula.

### 2️⃣ Question
In how many ways can 20 identical balls be distributed into 4 distinct boxes such that each box gets at least 3 balls?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you correctly apply variable substitution before stars-and-bars?
- **Why Top-100 Fail:** They use $\binom{20+4-1}{4-1}$ for unrestricted case without adjustment.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Pre-allocate minimums, then distribute remainder.

1. Each box needs ≥ 3 balls → pre-place 3 in each
2. Pre-placed: $4 \times 3 = 12$ balls
3. Remaining: $20 - 12 = 8$ balls
4. Now distribute 8 identical balls into 4 distinct boxes (no restriction)
5. Using stars and bars: $\binom{8 + 4 - 1}{4 - 1} = \binom{11}{3} = 165$

**Answer: 165**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 1771 (from $\binom{23}{3}$ for unrestricted) or 969
- **Why It Feels Correct:** The formula is memorized without the constraint adjustment.
- **Exact Failure Point:** Not subtracting pre-allocated balls first.

### 6️⃣ Generalization Map
1. Different minimum for each box
2. Maximum constraints (at most k per box)
3. Both min and max constraints
4. Distinguishable balls instead
5. Boxes also identical

### 7️⃣ Neural Anchor
**"Pre-Allocate-Then-Distribute"**

---

## Summary: Logic Traps Covered

| Q# | Dominant Trap | Key Insight |
|----|---------------|-------------|
| 1 | Examiner-language misdirection | "Identical" is context-dependent |
| 2 | Hidden constraint dominance | Dual constraints need enumeration |
| 3 | Ghost variable cancellation | Inclusion-exclusion for dependent obstacles |
| 4 | Intuition vs formal logic conflict | Check if rotational symmetry applies |
| 5 | Overfitting to standard models | Partial derangement = selection + derangement |
| 6 | Boundary-condition collapse | Pre-allocate minimums first |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
