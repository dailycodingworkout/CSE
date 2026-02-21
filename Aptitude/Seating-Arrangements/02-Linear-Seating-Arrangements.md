# Chapter 2: Linear Seating Arrangements

[← Previous: Introduction](01-Introduction-and-Fundamentals.md) | [Back to Index](README.md) | [Next: Circular Arrangements →](03-Circular-Seating-Arrangements.md)

---

## 2.1 What is a Linear Arrangement?

**The Atomic Truth:** *People in a straight line; endpoints exist.*

People sit in a single straight row. Each person (except those at the ends) has exactly **two neighbours** — one on the left, one on the right. The end positions have only **one neighbour**.

```
Position:    1     2     3     4     5     6     7
            ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
            │   │ │   │ │   │ │   │ │   │ │   │ │   │
            └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘
            END                                   END
            (Left)                              (Right)
```

### Key Properties

| Property | Value |
|----------|-------|
| Total positions | $n$ |
| End positions | 2 |
| Middle positions | $n - 2$ |
| Exact middle (odd $n$) | Position $\frac{n+1}{2}$ |
| Max distance between two people | $n - 1$ positions apart |
| Neighbours of position $i$ | Positions $i-1$ and $i+1$ (if they exist) |

---

## 2.2 The Direction Convention — Single Direction

### All Facing the Same Direction

When all people face the **same direction** (e.g., all face North):

```
All facing North (↑):

            1     2     3     4     5
            ↑     ↑     ↑     ↑     ↑
           (A)   (B)   (C)   (D)   (E)

From THEIR perspective (facing North):
  ← Left                        Right →
```

**Rule:** When facing North, left = West, right = East.

When they **face South**:

```
All facing South (↓):

            1     2     3     4     5
            ↓     ↓     ↓     ↓     ↓
           (A)   (B)   (C)   (D)   (E)

From THEIR perspective (facing South):
  Right →                        ← Left
```

**Rule:** When facing South, left = East, right = West. The direction **flips**.

> **The Aha Moment:** Stand up. Face North. Your left hand points West. Now turn around (face South). Your left hand points East. *That's it.* The physical reality doesn't change — your orientation does.

---

## 2.3 Position Mathematics

### 2.3.1 "Second to the Left" — The Formula

If person X is at position $p$, and Y is $k$ places to the **left** of X:

$$\text{Position of Y} = p - k \quad \text{(when all face North)}$$

$$\text{Position of Y} = p + k \quad \text{(when all face South)}$$

**Why?** Because "left" is defined from the *person's perspective*. When facing North, left is towards lower position numbers. When facing South, left flips to higher position numbers.

### Example

> "7 people sit in a row facing North. C is at position 5. D is third to the left of C. What is D's position?"

$$\text{D's position} = 5 - 3 = 2$$

> Now if they all face South:

$$\text{D's position} = 5 + 3 = 8 \quad \text{(invalid! only 7 seats)} \implies \text{Arrangement is impossible.}$$

### 2.3.2 "Between" — Counting Gaps

> "How many people sit between A (position 2) and B (position 6)?"

$$\text{People between A and B} = |p_B - p_A| - 1 = |6 - 2| - 1 = 3$$

**Formula:** People between positions $p_1$ and $p_2$:

$$\text{Count} = |p_1 - p_2| - 1$$

**Why does this work?** Positions 2 and 6 have positions 3, 4, 5 between them. That's $6 - 2 - 1 = 3$ positions.

### 2.3.3 "Opposite Ends" Check

> "A sits at the left end, B sits at the right end."

In a row of $n$ people: A is at position 1, B is at position $n$.

People between them: $n - 2$.

---

## 2.4 Solved Example 1 — Basic Linear (GATE Style)

### Problem

> Six people — P, Q, R, S, T, U — sit in a straight line facing North.
> 1. P sits at the left end.
> 2. Q sits third to the right of P.
> 3. R sits immediately to the right of Q.
> 4. S does not sit adjacent to P.
> 5. T sits at the right end.
> 6. U sits between P and Q.
>
> **Question:** Who sits at position 4?

### Solution — Using the 5-Step Framework

**Step 1: Draw the skeleton**

```
Position:   1    2    3    4    5    6
           [ ]  [ ]  [ ]  [ ]  [ ]  [ ]
All face North → Left is towards position 1
```

**Step 2: Identify definite clues**

- Clue 1: P at position 1 ✓ (definite)
- Clue 5: T at position 6 ✓ (definite)

**Step 3: Place anchors**

```
Position:   1    2    3    4    5    6
           [P]  [ ]  [ ]  [ ]  [ ]  [T]
```

**Step 4: Apply relative clues**

- Clue 2: Q is 3rd to the right of P → $1 + 3 = 4$ → Q at position 4.
- Clue 3: R is immediately right of Q → $4 + 1 = 5$ → R at position 5.

```
Position:   1    2    3    4    5    6
           [P]  [ ]  [ ]  [Q]  [R]  [T]
```

- Clue 6: U sits between P and Q → Between positions 1 and 4 → positions 2 or 3.
- Clue 4: S does NOT sit adjacent to P → S is NOT at position 2.

Remaining: S and U need positions 2 and 3.
Since S ≠ position 2 → S at position 3, U at position 2.

**Step 5: Final arrangement**

```
Position:   1    2    3    4    5    6
           [P]  [U]  [S]  [Q]  [R]  [T]
```

**Verify all clues:**
1. ✅ P at left end (position 1)
2. ✅ Q is 3rd to right of P (position 4 = 1 + 3)
3. ✅ R immediately right of Q (position 5)
4. ✅ S not adjacent to P (S at 3, P at 1 — gap of 1 person)
5. ✅ T at right end (position 6)
6. ✅ U between P and Q (position 2 is between 1 and 4)

**Answer:** Q sits at position 4.

---

## 2.5 Solved Example 2 — With Branching (Banking Style)

### Problem

> Eight people — A, B, C, D, E, F, G, H — sit in a row facing North.
> 1. D sits fourth from the left end.
> 2. A sits second to the right of D.
> 3. H sits at one of the extreme ends.
> 4. B sits third to the left of A.
> 5. C sits immediately to the left of D.
> 6. G is not adjacent to A.
> 7. E sits immediately to the right of A.
> 8. F does not sit at any extreme end.
>
> **Question:** How many people sit between B and H?

### Solution

**Step 1: Skeleton**

```
Position:   1    2    3    4    5    6    7    8
           [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]
```

**Step 2 & 3: Place definite clues**

- Clue 1: D at position 4.
- Clue 2: A second to right of D → $4 + 2 = 6$ → A at position 6.
- Clue 4: B third to left of A → $6 - 3 = 3$ → B at position 3.
- Clue 5: C immediately left of D → $4 - 1 = 3$ → Position 3.

**Conflict!** B is at position 3 (Clue 4) and C should be at position 3 (Clue 5). Both can't be there.

Wait — let me re-check. Clue 5 says C is immediately to the left of D. D is at position 4. So C is at position 3. But B is also at position 3 from Clue 4.

**Re-read Clue 4:** "B sits third to the left of A." A is at position 6. Third to the left = $6 - 3 = 3$.

This contradicts Clue 5. Let me check if there's flexibility elsewhere...

Actually, Clue 1 says "D sits fourth from the left end" — this means D is at position 4. This is fixed.

Hmm, let me re-examine. With "facing North", "left" is from their perspective = towards position 1. So "third to the left of A" = position $6 - 3 = 3$. And "immediately to the left of D" = position $4 - 1 = 3$. So B = C at position 3? That's impossible.

**The Trap!** Let me re-read more carefully. "B sits third to the left of A" — this could mean there are 3 people between B and A towards the left. Let me consider both interpretations:

**Interpretation 1:** B is at position $6 - 3 = 3$ (third seat to the left). ← Standard interpretation.

This creates a conflict. So the question might use "third to the left" as a different convention. But in standard exam problems, "third to the left" = 3 positions to the left.

Since there's a genuine conflict, let me re-examine Clue 5: "C sits immediately to the left of D." Maybe I should verify — C is at position 3 and B is at position 3 is impossible. Let me re-read the question...

Actually, I made this problem up for illustration. Let me fix it to be consistent.

**Corrected Clue 4:** B sits third to the left of **H** (not A). Let me redo:

### Corrected Problem

> 1. D sits fourth from the left end.
> 2. A sits second to the right of D.
> 3. H sits at one of the extreme ends.
> 4. B sits third to the left of H.
> 5. C sits immediately to the left of D.
> 6. G is not adjacent to A.
> 7. E sits immediately to the right of A.
> 8. F does not sit at any extreme end.

### Solution (Corrected)

- Clue 1: D at position 4.
- Clue 2: A at position $4 + 2 = 6$.
- Clue 5: C at position $4 - 1 = 3$.
- Clue 7: E at position $6 + 1 = 7$.
- Clue 3: H at position 1 or 8.
- Clue 4: B is third to the left of H.
  - If H at position 8 → B at $8 - 3 = 5$.
  - If H at position 1 → B at $1 - 3 = -2$ (impossible).
  - So **H at position 8, B at position 5**.

```
Position:   1    2    3    4    5    6    7    8
           [ ]  [ ]  [C]  [D]  [B]  [A]  [E]  [H]
```

Remaining: F, G for positions 1 and 2.
- Clue 8: F not at any extreme end → F ≠ position 1 → F at position 2, G at position 1.
- Clue 6: G not adjacent to A → G at position 1, A at position 6. Not adjacent. ✅

```
Position:   1    2    3    4    5    6    7    8
           [G]  [F]  [C]  [D]  [B]  [A]  [E]  [H]
```

**People between B (position 5) and H (position 8):** $|8 - 5| - 1 = 2$ (A and E).

**Answer:** 2

### What This Example Teaches

1. **Start with definite positions** (D at 4 is the anchor).
2. **Chain relative clues** from the anchor outward.
3. **Test extreme-position clues** (H at ends) — one option often becomes impossible.
4. **Use elimination** for the last 2–3 people.

---

## 2.6 Edge Cases in Linear Arrangements

### Edge Case 1: "Left of" vs. "Immediately to the Left of"

| Phrase | Meaning | Positions |
|--------|---------|-----------|
| "A is to the left of B" | A is *anywhere* to B's left | A could be 1, 2, ..., many seats to the left |
| "A is immediately to the left of B" | A is *directly* next to B, on B's left | $p_A = p_B - 1$ (facing North) |
| "A is second to the left of B" | A is *exactly* 2 seats to B's left | $p_A = p_B - 2$ (facing North) |

> **Exam Trap:** If a clue says "A is to the left of B" (without "immediately" or a number), it means A is **anywhere** to B's left. This gives you a range, not a fixed position. Many students over-constrain this.

### Edge Case 2: Odd vs. Even Number of People

For $n$ people in a row:
- If $n$ is **odd**: There is a unique middle position = $\frac{n+1}{2}$.
- If $n$ is **even**: There is no single middle position. "Middle" might refer to positions $\frac{n}{2}$ and $\frac{n}{2}+1$.

### Edge Case 3: "From the Left" vs. "From the Right"

> "P is 3rd from the left end."

Position = 3 (counting from left).

> "P is 3rd from the right end."

Position = $n - 3 + 1 = n - 2$ (counting from right).

**General Formula:**

$$\text{Position from left} + \text{Position from right} = n + 1$$

So if someone is 3rd from the right in a row of 8: position from left = $8 + 1 - 3 = 6$.

**Why?** The positions from left (1-indexed) and from right (1-indexed) always add up to $n + 1$ because they count the same seat once from each end.

---

## 2.7 The "From Left + From Right" Identity

This is one of the most powerful formulas in linear arrangement:

$$\boxed{L + R = n + 1}$$

Where:
- $L$ = position number counted from the left
- $R$ = position number counted from the right
- $n$ = total number of people

### Derivation

Position from the left for seat at index $i$ (0-indexed from left): $L = i + 1$.

Position from the right: $R = n - i$.

Sum: $L + R = (i + 1) + (n - i) = n + 1$. ∎

### Application

> "In a row of people, A is 5th from the left and 4th from the right. How many people are in the row?"

$$n = L + R - 1 = 5 + 4 - 1 = 8$$

> "In a row of 10, A is 3rd from the left. What is A's position from the right?"

$$R = 10 + 1 - 3 = 8$$

---

## 2.8 The Swap Trick — When Two Arrangements Are Possible

Sometimes constraints allow two valid arrangements (a "branch"). Here's how to handle it:

### Method: Parallel Tracking

Draw **both** possible arrangements side by side:

```
Case I:    [P]  [Q]  [R]  [S]  [ ]  [ ]
Case II:   [P]  [R]  [Q]  [S]  [ ]  [ ]
```

Continue applying clues to **both** cases. One case will eventually produce a contradiction — eliminate it.

> **Speed Tip:** Don't abandon a case until you find a **hard contradiction** (two people in the same seat, or a required position outside the row). Soft discomfort ("this feels wrong") is not a reason to eliminate.

---

## 2.9 Tricks for Linear Arrangements

### Trick 1: The Endpoint Anchor

If a clue says someone sits at an end, **fix them first**. End positions are the most constrained (only 1 neighbour), so they propagate the most information.

### Trick 2: The Chain Method

If you have: "A is immediately left of B, B is immediately left of C, C is immediately left of D":

$$A \_ B \_ C \_ D$$

This is a **chain** — a block of 4 consecutive people. Treat the entire block as a single unit and slide it along the row.

For a row of 7: This block of 4 can start at positions 1, 2, 3, or 4 (that's $7 - 4 + 1 = 4$ positions).

### Trick 3: The Negative Space Method

Instead of tracking where people **are**, track where they **cannot** be:

```
Position:   1    2    3    4    5    6
A:          ✓    ✓    ✗    ✗    ✓    ✓
B:          ✗    ✓    ✓    ✓    ✓    ✗
C:          ✗    ✗    ✓    ✓    ✗    ✗
```

When a person has only **one possible position** left, they must be there. This is exactly how Sudoku players find "naked singles."

### Trick 4: Count Available Positions

Before diving into a problem, count:
- Total people = $n$
- Total clues that give definite positions → subtract these from unknowns
- If $n - \text{definite clues} \leq 2$, the problem is trivially solvable by elimination

---

## 2.10 Practice Problem (Try Before Reading Solution)

> Seven people — J, K, L, M, N, O, P — sit in a row facing South.
> 1. M sits at the extreme right end.
> 2. K sits third from the left end.
> 3. J sits immediately to the right of K.
> 4. N sits second to the right of M.
> 5. O and L are adjacent to each other.
> 6. P does not sit adjacent to M.
>
> **Q1:** Who sits at the left end?
> **Q2:** How many people sit between O and M?

<details>
<summary><strong>Click to reveal solution</strong></summary>

**Setup:** 7 people, facing South. Remember: facing South flips left/right.

When facing South:
- "Right" from person's perspective = towards position 1 (left on paper)
- "Left" from person's perspective = towards position 7 (right on paper)

Wait — let's be precise. Standard convention in exam problems:

The positions are numbered 1 to 7 from left to right on paper. When people face South:
- Their "right" = towards lower position numbers (paper-left)
- Their "left" = towards higher position numbers (paper-right)

Clue 1: M at the extreme right end. "Right end" from person's perspective (facing South) = position 1 (paper-left). So **M at position 1**.

Clue 2: K third from the left end. "Left end" — this is typically a positional statement, not perspective-based. It usually means 3rd from position 1. So **K at position 3**.

Actually, "from the left end" in exam context typically means from the reader's left = position 1 side. So K at position 3.

But Clue 1 says "extreme right end." If facing South, right from their perspective = position 1. Most exams disambiguate this with "right end of the row" meaning position $n$.

**Standard Banking Exam Convention:** "Left end" = position 1 on paper, "Right end" = position $n$ on paper, **regardless of facing direction**. The facing direction only matters for "to the left/right **of** a person."

Using this convention:
- Clue 1: M at position 7 (right end of row).
- Clue 2: K at position 3.

Clue 3: J immediately to the right of K. "Right of K" is from K's perspective (facing South). K faces South, so K's right = towards position 1. J at position $3 - 1 = 2$.

Clue 4: N second to the right of M. M is at position 7, facing South. M's right = towards position 1. N at $7 - 2 = 5$.

```
Position:   1    2    3    4    5    6    7
           [ ]  [J]  [K]  [ ]  [N]  [ ]  [M]
```

Remaining: L, O, P for positions 1, 4, 6.

Clue 6: P not adjacent to M. M is at position 7. Adjacent = position 6. So P ≠ position 6.

Clue 5: O and L are adjacent. Possible pairs from {1, 4, 6}: Only (4, 6) are adjacent — but not (1, 4) since they're not adjacent either... wait: positions 1 and 4 are not adjacent (gap of 2). Positions 4 and 6 are not adjacent (gap of 1). Actually 4 and 6 have position 5 between them — not adjacent.

Hmm. Available: 1, 4, 6. Adjacent pairs: none of these are adjacent to each other!

Let me recheck. 1 and 2 are adjacent (but 2 is taken by J). 4 and 5 are adjacent (but 5 is taken by N). 6 and 7 are adjacent (but 7 is taken by M).

Wait — O and L need to be adjacent to each other, and they're going into positions 1, 4, 6. Positions 1-2 are adjacent but seat 2 is taken. So the only way O and L are adjacent is... this seems contradictory.

Let me re-examine the direction convention. Perhaps "right end" means the right end as seen from the reader, position 7. But "to the right of" uses the person's facing direction.

Alternatively, if "right end" when facing South means position 1:
- M at position 1.
- K at position 3 (3rd from left end = position 3).
- J immediately to the right of K (K's right facing South = towards position 1 side). J at position 2.
- N second to the right of M (M's right facing South, M at position 1). N at position $1 - 2 = -1$ → impossible.

So M must be at position 7. The issue is with clue 5. Let me reinterpret: perhaps "right" in clues 3 and 4 is paper-right (not perspective-based) since some exam setups use absolute directions when directions are not explicitly stated as "his/her right."

**Re-solving with absolute direction convention:**

- Clue 1: M at position 7.
- Clue 2: K at position 3.
- Clue 3: J immediately to the right of K → J at position 4.
- Clue 4: N second to the right of M → position $7 + 2 = 9$ → impossible.

Clue 4 doesn't work with absolute right. So "to the right" must be from M's perspective (facing South = towards position 1). N at $7 - 2 = 5$.

Let me also reconsider Clue 3 with perspective: J immediately to the right of K. K at position 3, facing South. K's right = towards position 1. J at position 2.

```
Position:   1    2    3    4    5    6    7
           [ ]  [J]  [K]  [ ]  [N]  [ ]  [M]
```

Remaining: L, O, P for positions 1, 4, 6.

O and L must be adjacent. Available pairs: (1,4) no — gap = 3. (4,6) no — gap = 2. (1,6) no — gap = 5.

None are adjacent! This means I must have an error. Let me try the other interpretation where all "left/right" in clue phrasing is from reader's perspective:

- Clue 3: J immediately to the right of K → J at position 4 (paper-right).
- Clue 4: N second to the right of M → position $7 + 2 = 9$ → impossible.

Since clue 4 fails, let's try: N second to the LEFT of M → position $7 - 2 = 5$. Maybe I misread my own problem. Let me re-read: "N sits second to the right of M." If this uses perspective (M faces South), right = towards position 1 = $7 - 2 = 5$. ✓

Let's use perspective for ALL directional clues:
- Clue 3 (perspective): J at $3 - 1 = 2$. ← This gives the adjacency problem.
- Clue 3 (absolute): J at $3 + 1 = 4$. ← Let me try this.

**With Clue 3 as absolute right:**

```
Position:   1    2    3    4    5    6    7
           [ ]  [ ]  [K]  [J]  [N]  [ ]  [M]
```

Remaining: L, O, P for positions 1, 2, 6.

Clue 5: O and L adjacent. From {1, 2, 6}: positions 1 and 2 are adjacent! ✓

So O and L are at positions 1 and 2 (in some order). P at position 6.

Clue 6: P not adjacent to M. P at 6, M at 7. They ARE adjacent! Contradiction.

So P ≠ position 6 → P can't be the remaining person for position 6.

That means P must be in {1, 2}, and one of {O, L} goes to position 6. But O and L must be adjacent. If one of them is at 6, the other must be at 5 or 7 — but both are taken. So O and L can't be split.

The only adjacent pair from {1, 2, 6} is (1, 2). So O and L are at positions 1 and 2, P at position 6.

But P at position 6 is adjacent to M at position 7, violating Clue 6.

This is contradictory in this interpretation too. The problem as stated has a subtle inconsistency (since I constructed it for illustration). The important lesson is:

> **Always verify the direction convention** used in the problem. Different exams use different conventions. GATE problems typically state explicitly ("all face North, left/right from their perspective"). Banking problems usually specify the convention at the start of the set.

For this practice problem, let's use: "N sits second to the **left** of M" (correcting Clue 4), and "right" = paper-right.

**Corrected solve:**
- M at position 7. K at position 3. J at position 4 (paper-right of K).
- N second to the left of M → $7 - 2 = 5$.
- Remaining: L, O, P for positions 1, 2, 6.
- O and L adjacent → positions 1 and 2.
- P at position 6. P adjacent to M (position 7) — if Clue 6 says "P not adjacent to M", we need P ≠ 6.

Correcting Clue 6 to "P does not sit adjacent to J":
- J at position 4. Adjacent = 3 or 5. P isn't at 3 or 5 anyway (already filled). So P at position 6. ✓

```
Position:   1      2      3    4    5    6    7
           [O/L]  [L/O]  [K]  [J]  [N]  [P]  [M]
```

Since no clue distinguishes O and L's order, both (O at 1, L at 2) and (L at 1, O at 2) are valid.

**Q1:** O or L sits at the left end. (The question would give options to disambiguate.)

**Q2:** People between O and M: If O at position 1, between O and M = $|7-1| - 1 = 5$.

</details>

> **The Key Lesson:** Direction conventions are the **#1 source of errors** in linear arrangement problems. Before solving, establish: are left/right from the person's perspective or from the reader's perspective? The problem statement will tell you.

---

## 2.11 Summary: Linear Arrangement Cheat Sheet

| Concept | Formula / Rule |
|---------|---------------|
| Position from left + from right | $L + R = n + 1$ |
| People between positions $p_1$, $p_2$ | $\|p_1 - p_2\| - 1$ |
| $k$-th to the right (facing North) | $p + k$ |
| $k$-th to the left (facing North) | $p - k$ |
| $k$-th to the right (facing South) | $p - k$ |
| $k$-th to the left (facing South) | $p + k$ |
| Middle position (odd $n$) | $\frac{n+1}{2}$ |
| Chain of $m$ consecutive people in row of $n$ | Can start at $n - m + 1$ positions |
| End positions | Only 1 neighbour; most constrained |

---

[← Previous: Introduction](01-Introduction-and-Fundamentals.md) | [Back to Index](README.md) | [Next: Circular Arrangements →](03-Circular-Seating-Arrangements.md)
