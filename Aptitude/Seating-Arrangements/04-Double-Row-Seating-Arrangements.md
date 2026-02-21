# Chapter 4: Double-Row (Parallel) Seating Arrangements

[← Previous: Circular Arrangements](03-Circular-Seating-Arrangements.md) | [Back to Index](README.md) | [Next: Complex & Hybrid Arrangements →](05-Complex-and-Hybrid-Arrangements.md)

---

## 4.1 What is a Double-Row Arrangement?

**The Atomic Truth:** *Two parallel rows; facing each other.*

Two rows of people sit facing each other. This is the **most common type** in banking exams (IBPS PO, SBI PO, RBI Grade B).

```
Row 1 (Facing South):  P1   P2   P3   P4   P5
                        ↓    ↓    ↓    ↓    ↓
                        ↑    ↑    ↑    ↑    ↑
Row 2 (Facing North):  Q1   Q2   Q3   Q4   Q5
```

### Key Properties

| Property | Detail |
|----------|--------|
| Number of rows | 2 |
| People per row | Usually equal ($n$ per row, $2n$ total) |
| Facing direction | Row 1 faces South, Row 2 faces North (standard) |
| "Opposite" | Person directly across in the other row |
| "Left/Right" | From the person's perspective (depends on which row) |

---

## 4.2 The Direction Convention — The Master Trap

This is where **most students lose marks**. The two rows face **opposite directions**, so "left" for Row 1 people is the **opposite** of "left" for Row 2 people.

### Row 1 (Facing South)

```
Row 1:     P1   P2   P3   P4   P5
           ↓    ↓    ↓    ↓    ↓    (all facing South)

From P's perspective: Right ←──── ────→ Left
```

Wait — when facing South, the person's left hand points to their left (which is to the East, i.e., toward higher position numbers on paper). Let me be precise:

**Convention:** Positions are numbered 1–5 from the **reader's left to right** on paper.

When someone **faces South** (downward on paper):
- Their **left** = towards higher position numbers (paper-right) = East
- Their **right** = towards lower position numbers (paper-left) = West

When someone **faces North** (upward on paper):
- Their **left** = towards lower position numbers (paper-left) = West
- Their **right** = towards higher position numbers (paper-right) = East

### The Visual Proof

Stand facing South (your back is to the North). Point your left arm: it points **East** (to your right on a map, but to YOUR left). Point your right arm: it points **West**.

Now turn around (face North). Point your left arm: it points **West**.

> **The Aha Moment:** Left/Right is from the PERSON's body, not from the paper. A person facing South has their "left" mirrored compared to a person facing North.

### Row 2 (Facing North)

```
Row 2:     Q1   Q2   Q3   Q4   Q5
           ↑    ↑    ↑    ↑    ↑    (all facing North)

From Q's perspective: Left ←──── ────→ Right
```

### Summary Table

| Person in... | Faces | Their Left (on paper) | Their Right (on paper) |
|:---:|:---:|:---:|:---:|
| Row 1 | South | Paper-Right → | ← Paper-Left |
| Row 2 | North | ← Paper-Left | Paper-Right → |

> **Memory Aid:** "**North-Left-West** (NLW): Facing **N**orth, **L**eft is **W**est (paper-left)."
> Facing South reverses it: left is East (paper-right).

---

## 4.3 The "Faces" / "Opposite" Concept

In a double-row setup, each person in Row 1 **faces** exactly one person in Row 2 (assuming equal row sizes and aligned positions).

```
Row 1 (South):  A    B    C    D    E
                |    |    |    |    |
Row 2 (North):  P    Q    R    S    T
```

A faces P. B faces Q. C faces R. D faces S. E faces T.

### The Facing Rule

If person X is at position $k$ in Row 1, the person directly opposite in Row 2 is also at position $k$.

> **Note:** Some problems offset the rows. Always check the problem diagram or description.

---

## 4.4 Position Mathematics

### 4.4.1 "Second to the left" — Row 1 (Facing South)

Person X at position $p$ in Row 1 (facing South). Y is $k$ places to X's left:

$$\text{Y's position} = p + k \quad \text{(Row 1, facing South, left = paper-right)}$$

### 4.4.2 "Second to the left" — Row 2 (Facing North)

Person X at position $p$ in Row 2 (facing North). Y is $k$ places to X's left:

$$\text{Y's position} = p - k \quad \text{(Row 2, facing North, left = paper-left)}$$

### 4.4.3 Quick Reference

| Action | Row 1 (South) | Row 2 (North) |
|--------|:---:|:---:|
| $k$ to the left | $p + k$ | $p - k$ |
| $k$ to the right | $p - k$ | $p + k$ |
| Immediately left | $p + 1$ | $p - 1$ |
| Immediately right | $p - 1$ | $p + 1$ |

---

## 4.5 Solved Example — Standard Double Row (Banking Style)

> **Convention Note:** In double-row problems, "left end" and "right end" of a row, as well as "second from the left" etc., refer to directions **from the person's own perspective** in that row. Since Row 1 faces South and Row 2 faces North, "left" points in opposite paper-directions for the two rows. Positions are numbered 1–$n$ from paper-left to paper-right.

### Problem

> Eight people — A, B, C, D and P, Q, R, S — sit in two rows.
> Row 1: A, B, C, D face South. Row 2: P, Q, R, S face North.
> Positions numbered 1–4 from left to right on paper.
>
> 1. B sits at position 3 in Row 1.
> 2. R faces B.
> 3. A sits immediately to B's right (from B's perspective).
> 4. S sits immediately to R's left (from R's perspective).
> 5. D is not adjacent to A.
> 6. P does not face D.

### Solution

**Direction Rules:**
- Row 1 (facing South): right = paper-left (decreasing position numbers), left = paper-right (increasing).
- Row 2 (facing North): right = paper-right (increasing position numbers), left = paper-left (decreasing).

Clue 1: B at Row 1, position 3.

Clue 2: R faces B → R at Row 2, position 3.

Clue 3: A immediately to B's right. B faces South → B's right = paper-left → position $3-1=2$. **A at Row 1, position 2.**

Clue 4: S immediately to R's left. R faces North → R's left = paper-left → position $3-1=2$. **S at Row 2, position 2.**

```
Row 1 (South):  [__]  [A]  [B]  [__]     (positions 1-4)
                  |     |    |     |
Row 2 (North):  [__]  [S]  [R]  [__]     (positions 1-4)
```

Remaining Row 1: C, D for positions 1 and 4.
Remaining Row 2: P, Q for positions 1 and 4.

Clue 5: D not adjacent to A (position 2). Adjacent to A = positions 1 and 3. Position 3 is B. So D ≠ position 1. **D at position 4, C at position 1.**

Clue 6: P does not face D (Row 1, position 4). So P ≠ Row 2 position 4. **P at position 1, Q at position 4.**

```
Row 1 (South):  [C]  [A]  [B]  [D]
                  |    |    |    |
Row 2 (North):  [P]  [S]  [R]  [Q]
```

**Verification:**
1. ✅ B at position 3
2. ✅ R at Row 2 position 3, faces B
3. ✅ A at position 2 = B's right (facing South, right = paper-left)
4. ✅ S at position 2 = R's left (facing North, left = paper-left)
5. ✅ D at position 4, not adjacent to A (position 2) — gap of 1 (position 3 between them)
6. ✅ P at position 1, faces C (not D) ✓

**Who faces C?** C at Row 1 position 1. Opposite = Row 2 position 1 = **P**.

---

## 4.6 Advanced Double-Row: Unequal Rows

Some problems have unequal row sizes (e.g., 4 in Row 1, 5 in Row 2). The "facing" concept becomes trickier:

```
Row 1:    A    B    C    D         (4 people)
          |    |    |    |
Row 2:  P    Q    R    S    T      (5 people)
```

Not everyone in Row 2 faces someone in Row 1. The question will specify which positions face which.

> **Exam Tip:** In IBPS/SBI exams, unequal rows are rare. When they appear, the question always specifies the facing alignment. Don't assume.

---

## 4.7 Common Traps in Double-Row

### Trap 1: Left/Right Confusion Between Rows

> "A is second to the left of B (Row 1, facing South). Q is second to the left of R (Row 2, facing North)."

For A (Row 1, South): left = paper-right → A is 2 positions to the right on paper from B.
For Q (Row 2, North): left = paper-left → Q is 2 positions to the left on paper from R.

**The directions are opposite for the two rows!** Students who apply the same direction for both rows get the wrong answer.

### Trap 2: "Faces" vs. "Adjacent"

"Faces" = directly opposite in the other row.
"Adjacent" = next to in the **same** row.

A and B can be adjacent (same row). A and P can face each other (different rows). A and P are NOT adjacent.

### Trap 3: Diagonal Relationships

If A is at Row 1 position 2 and Q is at Row 2 position 3:
- A and Q are **not facing** each other.
- A and Q are **diagonally** placed.
- Most exam questions don't ask about diagonals, but some advanced ones do.

---

## 4.8 The "Facing Pair" Technique

### Method: List All Facing Pairs First

Before placing anyone, list who faces whom (if given directly or inferrable):

```
Facing Pairs:
A ↔ ?
B ↔ ?
C ↔ R  (from clue)
D ↔ ?
```

As you place people, fill in facing pairs. Any contradiction (two people facing the same person) means you've made an error.

### Method: Cross-Row Constraint Chaining

If you know: "A faces P" and "B is immediately to A's left" and "Q is immediately to P's right":

Row 1 (South): ... B A ... (B is paper-right of A since left = paper-right for South-facing)
Row 2 (North): ... P Q ... (Q is paper-right of P since right = paper-right for North-facing)

So B faces Q! This is a "cross-row chain" — placing 2 people automatically determines 2 facing pairs.

---

## 4.9 Quick Problem-Solving Strategy for Double-Row

1. **Draw both rows** with position numbers.
2. **Process "faces" clues first** — they link the two rows.
3. **Process "end" clues** — fix endpoints in each row.
4. **Process relative position clues** — careful with direction per row.
5. **Process "not adjacent" / "not faces" clues last** — for elimination.

> **Speed Tip:** In a well-constructed banking problem, 2–3 clues fix the core arrangement. The remaining clues are for validation or to resolve 1–2 ambiguities. Don't process every clue sequentially — scan for the most constraining ones first.

---

## 4.10 Summary: Double-Row Cheat Sheet

| Concept | Row 1 (Facing South) | Row 2 (Facing North) |
|---------|:---:|:---:|
| Left direction | Paper-right (+) | Paper-left (−) |
| Right direction | Paper-left (−) | Paper-right (+) |
| Faces | Same position number in other row | Same position number in other row |
| Adjacent | Same row, $\|p-q\| = 1$ | Same row, $\|p-q\| = 1$ |
| End positions | Position 1 and $n$ | Position 1 and $n$ |

---

[← Previous: Circular Arrangements](03-Circular-Seating-Arrangements.md) | [Back to Index](README.md) | [Next: Complex & Hybrid Arrangements →](05-Complex-and-Hybrid-Arrangements.md)
