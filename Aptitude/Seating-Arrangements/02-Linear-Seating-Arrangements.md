---
layout: default
title: "Chapter 2: Linear Seating Arrangements"
description: "Single row arrangements, direction conventions, position formulas"
---

# Chapter 2: Linear Seating Arrangements

[← Previous: Introduction](01-Introduction-and-Fundamentals.html) | [Back to Index](./) | [Next: Circular Arrangements →](03-Circular-Seating-Arrangements.html)

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
> 4. B sits third to the left of H.
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

**Step 2: Place definite clues and chain outward**

- Clue 1: D at position 4.
- Clue 2: A second to right of D → $4 + 2 = 6$ → A at position 6.
- Clue 5: C immediately left of D → $4 - 1 = 3$ → C at position 3.
- Clue 7: E immediately right of A → $6 + 1 = 7$ → E at position 7.

**Step 3: Resolve the branching clue**

- Clue 3: H at position 1 or 8 (extreme end).
- Clue 4: B is third to the left of H → B at $H - 3$.
  - If H = 8 → B at $8 - 3 = 5$. ✓
  - If H = 1 → B at $1 - 3 = -2$ (impossible). ✗
  - So **H at position 8, B at position 5**.

```
Position:   1    2    3    4    5    6    7    8
           [ ]  [ ]  [C]  [D]  [B]  [A]  [E]  [H]
```

**Step 4: Eliminate for remaining people**

Remaining: F, G for positions 1 and 2.

- Clue 8: F not at any extreme end → F ≠ position 1 → **F at position 2, G at position 1**.
- Clue 6: G not adjacent to A → G at position 1, A at position 6. Not adjacent. ✅

**Step 5: Final arrangement**

```
Position:   1    2    3    4    5    6    7    8
           [G]  [F]  [C]  [D]  [B]  [A]  [E]  [H]
```

**Verify all clues:**
1. ✅ D at position 4 (fourth from left)
2. ✅ A at position 6 (second to right of D)
3. ✅ H at position 8 (extreme end)
4. ✅ B at position 5 (third to left of H: $8 - 3 = 5$)
5. ✅ C at position 3 (immediately left of D)
6. ✅ G(1) not adjacent to A(6)
7. ✅ E at position 7 (immediately right of A)
8. ✅ F at position 2 (not at extreme end)

**People between B (pos 5) and H (pos 8):** $|8 - 5| - 1 = 2$ (A and E).

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

> Seven people — J, K, L, M, N, O, P — sit in a row facing North.
> 1. M sits at the right end (position 7).
> 2. K sits third from the left end.
> 3. J sits immediately to the right of K.
> 4. N sits second to the left of M.
> 5. O and L are adjacent to each other.
> 6. P does not sit adjacent to J.
>
> **Q1:** Who sits at the left end?
> **Q2:** How many people sit between O and M?

<details>
<summary><strong>Click to reveal solution</strong></summary>

**Setup:** 7 people, facing North. Positions 1–7, left to right on paper.

Facing North: right = increasing position numbers, left = decreasing position numbers.

**Step 1: Place definite positions**

- Clue 1: M at position 7.
- Clue 2: K at position 3.
- Clue 3: J immediately to K's right → J at position $3 + 1 = 4$.
- Clue 4: N second to M's left → N at position $7 - 2 = 5$.

```
Position:   1    2    3    4    5    6    7
           [ ]  [ ]  [K]  [J]  [N]  [ ]  [M]
```

**Step 2: Place remaining people**

Remaining: L, O, P for positions 1, 2, 6.

- Clue 5: O and L are adjacent. From {1, 2, 6}: positions 1 and 2 are adjacent ✓. So **O and L occupy positions 1 and 2** (in some order). **P at position 6.**
- Clue 6: P not adjacent to J (position 4). P at position 6. Adjacent to J = positions 3 and 5. P(6) is not adjacent to J(4). ✅

```
Position:   1      2      3    4    5    6    7
           [O/L]  [L/O]  [K]  [J]  [N]  [P]  [M]
```

O and L can be in either order at positions 1 and 2 (no clue distinguishes them).

**Q1:** O or L sits at the left end (position 1). If the exam gives options, one of these will appear.

**Q2:** People between O and M:
- If O at position 1: between O(1) and M(7) = $|7 - 1| - 1 = 5$ people.
- If O at position 2: between O(2) and M(7) = $|7 - 2| - 1 = 4$ people.

The answer depends on O's position. An exam question would either fix this with additional clues or ask about L and M instead (which gives a definite answer).

**Between L and M:** If L at position 2, $|7-2|-1 = 4$. If L at position 1, $|7-1|-1 = 5$.

</details>

> **Key Lesson:** Always verify the direction convention before solving. "Left end" / "right end" of a row typically refers to the reader's perspective. "To the left/right of a person" uses that person's facing direction.

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

[← Previous: Introduction](01-Introduction-and-Fundamentals.html) | [Back to Index](./) | [Next: Circular Arrangements →](03-Circular-Seating-Arrangements.html)
