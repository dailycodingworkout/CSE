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

## 4.5 Solved Example 1 — Standard Double Row (Banking Style)

### Problem

> Ten people — A, B, C, D, E, P, Q, R, S, T — sit in two rows of 5 each.
> - Row 1: A, B, C, D, E sit facing South.
> - Row 2: P, Q, R, S, T sit facing North.
> - A person in Row 1 faces exactly one person in Row 2.
>
> **Clues:**
> 1. A sits at the left end of Row 1.
> 2. P faces A.
> 3. B sits second to the right of A.
> 4. Q sits immediately to the left of P.
> 5. D sits at the right end of Row 1.
> 6. S faces D.
> 7. R sits at the left end of Row 2.
> 8. C is not adjacent to D.
> 9. T does not face B.
>
> **Question:** Who faces C?

### Solution

**Step 1: Establish the grid.**

```
Row 1 (South):  __   __   __   __   __     (positions 1-5, left to right on paper)
                 |    |    |    |    |
Row 2 (North):  __   __   __   __   __     (positions 1-5, left to right on paper)
```

**Step 2: Place definite positions.**

Clue 1: A at the left end of Row 1. "Left end" — this is the end on the reader's left = position 1. But wait: A faces South, so A's "left" is paper-right. "Left end of the row" typically refers to the **reader's left** in exam convention (position 1). Let me use this.

But let me check: "left end of Row 1" — in banking exams, this is interpreted as the end that is to the left of people in Row 1. Row 1 faces South, so their left is paper-right. "Left end" from their perspective = position 5.

**Actually, banking exam convention:** "Left end" and "right end" are **from the person's own perspective**. So:
- Row 1 (facing South): Left end = paper-right (position 5). Right end = paper-left (position 1).
- Row 2 (facing North): Left end = paper-left (position 1). Right end = paper-right (position 5).

Hmm, this varies by exam. The safest approach: most banking exams define "left end" and "right end" based on the **person's facing direction**. Let me use this.

**Revised:**

Clue 1: A at the left end of Row 1. Row 1 faces South → left = paper-right → **A at position 5**.

Clue 5: D at the right end of Row 1. Row 1 faces South → right = paper-left → **D at position 1**.

Clue 7: R at the left end of Row 2. Row 2 faces North → left = paper-left → **R at position 1**.

```
Row 1 (South):  [D]  [__]  [__]  [__]  [A]     (positions 1-5)
                 |     |     |     |     |
Row 2 (North):  [R]  [__]  [__]  [__]  [__]    (positions 1-5)
```

Clue 2: P faces A. A is at Row 1 position 5. Person facing A = Row 2 position 5. **P at Row 2, position 5.**

Clue 6: S faces D. D at Row 1 position 1. **S at Row 2, position 1.** But R is at Row 2 position 1!

**Contradiction!** This means my "left end" convention is wrong. Let me try the other convention.

**Alternative Convention:** "Left end" / "right end" are from the **reader's perspective** (absolute), not the person's. This is actually more common in practice.

**Using reader's perspective:**

Clue 1: A at left end of Row 1 → **A at position 1**.

Clue 5: D at right end of Row 1 → **D at position 5**.

Clue 7: R at left end of Row 2 → **R at position 1**.

```
Row 1 (South):  [A]  [__]  [__]  [__]  [D]     (positions 1-5)
                 |     |     |     |     |
Row 2 (North):  [R]  [__]  [__]  [__]  [__]    (positions 1-5)
```

Clue 2: P faces A. A at Row 1 position 1. **P at Row 2 position 1.** But R is there!

Contradiction again!

Hmm. Let me try: "P faces A" might not mean directly opposite. Let me re-examine.

No — in double-row, "faces" means directly opposite. So P must be at Row 2 position 1, but R is there.

The issue is that my example clues conflict. Let me fix the clues to be consistent.

### Corrected Problem

> **Clues:**
> 1. A sits at one of the extreme ends of Row 1.
> 2. P faces A.
> 3. B sits second to the right of A (from A's perspective).
> 4. Q sits immediately to the right of P (from P's perspective).
> 5. D sits at the other extreme end of Row 1.
> 6. S faces D.
> 7. C is not adjacent to D.
> 8. T does not face B or E.
> 9. R sits exactly in the middle of Row 2.

### Solution (Corrected)

Positions 1–5 left to right on paper. Row 1 faces South, Row 2 faces North.

Clue 1: A at an extreme end of Row 1. A at position 1 or 5.

Clue 3: B second to the right of A. A faces South → A's right = paper-left = decreasing positions. If A at position 5: B at $5 - 2 = 3$. If A at position 1: B at $1 - 2 = -1$ → impossible. So **A at position 5**.

**B at position 3.**

Clue 5: D at the other end → **D at position 1**.

```
Row 1 (South):  [D]  [__]  [B]  [__]  [A]     (positions 1-5)
                 |     |     |     |     |
Row 2 (North):  [__]  [__]  [__]  [__]  [__]  (positions 1-5)
```

Clue 2: P faces A (position 5). **P at Row 2, position 5.**

Clue 6: S faces D (position 1). **S at Row 2, position 1.**

Clue 9: R in the middle of Row 2. **R at Row 2, position 3.**

```
Row 1 (South):  [D]  [__]  [B]  [__]  [A]
                 |     |     |     |     |
Row 2 (North):  [S]  [__]  [R]  [__]  [P]
```

Clue 4: Q immediately to the right of P. P faces North → right = paper-right = increasing positions. P at position 5 → Q at position 6. But only 5 positions! So Q at position $5 + 1$ is impossible.

Let me try: P's right (facing North) = paper-right. But position 5 is the rightmost. So Q can't be to P's right.

Maybe I should interpret "to the right" as towards increasing OR we placed A wrong. Let me reconsider: if facing North, right = East = paper-right. Position 5 is rightmost. Can't go further right.

Actually, when facing North, your right hand points East. If we define positions 1-5 from West to East (paper-left to paper-right), then "to the right" of position 5 is impossible. 

So let me change Clue 4 to: Q sits immediately to the **left** of P.

P faces North → left = paper-left = decreasing positions. Q at position 4.

```
Row 1 (South):  [D]  [__]  [B]  [__]  [A]
                 |     |     |     |     |
Row 2 (North):  [S]  [__]  [R]  [Q]   [P]
```

Remaining: Row 1 positions 2 and 4 for C and E. Row 2 position 2 for T.

**T at Row 2, position 2.**

Clue 7: C not adjacent to D (Row 1, position 1). Adjacent to D = position 2. So C ≠ position 2. **C at position 4, E at position 2.**

Clue 8: T does not face B or E. T at Row 2 position 2 faces Row 1 position 2 = E. T faces E! This contradicts Clue 8.

Hmm. T is the only remaining person for Row 2 position 2, so T must face whoever is at Row 1 position 2. If E is at position 2, T faces E (violated). If C is at position 2, T faces C. But Clue 7 says C not adjacent to D (position 1), and position 2 IS adjacent to position 1.

So: C can't be at position 2 (adjacent to D), and E at position 2 means T faces E (violating Clue 8).

Contradiction! I need to revisit. The issue is my constructed clues. Let me simplify to a clean, minimal example.

---

### Clean Example (Fully Verified)

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
- Row 1 (South): right = paper-left (decreasing position numbers).
- Row 2 (North): left = paper-left (decreasing position numbers).

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
