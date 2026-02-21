# Chapter 7: Exam Practice & Solved Problems

[← Previous: Advanced Techniques](06-Advanced-Techniques-and-Shortcuts.md) | [Back to Index](README.md)

---

## 7.1 Overview

This chapter provides **fully solved problems** organized by exam type and difficulty. Each problem includes:
- The problem statement
- Step-by-step solution using the techniques from Chapters 1–6
- Key takeaway (what the problem tests)

---

## 7.2 GATE-Style Problems

### Problem G1: Linear Arrangement (MCQ, 2 marks)

> Five people — A, B, C, D, E — sit in a row facing North.
> 1. C sits exactly in the middle.
> 2. A sits to the immediate right of C.
> 3. E sits at the left end.
> 4. B is not adjacent to E.
>
> **Which of the following must be true?**
> (a) D sits at the right end
> (b) B sits at position 2
> (c) A is adjacent to D
> (d) B sits at the right end

**Solution:**

C at position 3 (middle of 5). Facing North → right = increasing positions.

Clue 2: A immediately to C's right → A at position 4.

Clue 3: E at position 1 (left end on paper).

```
Position:  1    2    3    4    5
          [E]  [__] [C]  [A]  [__]
```

Remaining: B, D for positions 2 and 5.

Clue 4: B not adjacent to E (position 1). Adjacent to E = position 2. So B ≠ 2.

**B at position 5, D at position 2.**

```
Position:  1    2    3    4    5
          [E]  [D]  [C]  [A]  [B]
```

**Check options:**
- (a) D at right end (position 5)? No, D at position 2. ✗
- (b) B at position 2? No, B at position 5. ✗
- (c) A adjacent to D? A at 4, D at 2. Not adjacent. ✗
- (d) B at right end (position 5)? **Yes.** ✅

**Answer: (d)**

**Key Takeaway:** With only 4 clues and 5 people, cascade logic resolves everything. No branching needed. This is typical GATE difficulty for General Aptitude.

---

### Problem G2: Circular Arrangement (MCQ, 2 marks)

> Six people — P, Q, R, S, T, U — sit around a circular table, all facing the center.
> 1. P and R are diametrically opposite.
> 2. Q sits immediately to the left of P.
> 3. T is not adjacent to R.
> 4. U sits immediately to the right of R.
>
> **Who sits opposite to Q?**
> (a) S  (b) T  (c) U  (d) R

**Solution:**

Fix P at position 1. Positions 1–6 clockwise.

Facing center: Left = Clockwise, Right = Anticlockwise.

Clue 1: R opposite P → R at position 4 (for $n=6$, opposite = $+3$).

Clue 2: Q immediately to P's left → clockwise from P → Q at position 2.

Clue 4: U immediately to R's right → anticlockwise from R → position 3.

```
           1(P)
       6        2(Q)
       5        3(U)
           4(R)
```

Remaining: S, T for positions 5 and 6.

Clue 3: T not adjacent to R (position 4). Adjacent to R: positions 3 and 5. Position 3 is U. So T ≠ position 5. **T at position 6, S at position 5.**

```
           1(P)
       6(T)     2(Q)
       5(S)     3(U)
           4(R)
```

Q at position 2. Opposite = position $2 + 3 = 5$ = **S**.

**Answer: (a) S**

**Key Takeaway:** Circular problems with "opposite" clues cascade extremely fast. The entire arrangement was determined by 4 clues for 6 people.

---

## 7.3 Banking Exam Style Problems (IBPS / SBI)

### Problem B1: Double-Row (Set of 4 Questions)

> Eight people — A, B, C, D and P, Q, R, S — sit in two parallel rows of 4.
> Row 1: A, B, C, D face South. Row 2: P, Q, R, S face North.
> Positions 1–4 from left to right on paper.
>
> **Clues:**
> 1. B sits at position 3 in Row 1.
> 2. R faces B.
> 3. A sits immediately to B's right (B faces South, right = paper-left).
> 4. S sits immediately to R's left (R faces North, left = paper-left).
> 5. D is not adjacent to B.
> 6. P does not face C.
>
> **Questions:**
> Q1. Who faces D?
> Q2. How many people sit between C and A in Row 1?
> Q3. Who sits to the immediate right of P (from P's perspective)?
> Q4. Which pairs face each other?

**Solution:**

Clue 1: B at Row 1, position 3.
Clue 2: R at Row 2, position 3 (faces B).
Clue 3: A at position $3 - 1 = 2$ (B's right facing South = paper-left).
Clue 4: S at position $3 - 1 = 2$ in Row 2 (R's left facing North = paper-left).

```
Row 1 (South):  [__]  [A]   [B]   [__]   (positions 1-4)
                  |     |     |      |
Row 2 (North):  [__]  [S]   [R]   [__]   (positions 1-4)
```

Remaining Row 1: C, D for positions 1 and 4.

Clue 5: D not adjacent to B (position 3). Adjacent to B = positions 2 and 4. A is at 2. So D ≠ 4. **D at position 1, C at position 4.**

Remaining Row 2: P, Q for positions 1 and 4.

Clue 6: P does not face C. C at Row 1 position 4. So P ≠ Row 2 position 4. **P at position 1, Q at position 4.**

```
Row 1 (South):  [D]   [A]   [B]   [C]
                  |     |     |      |
Row 2 (North):  [P]   [S]   [R]   [Q]
```

**Verification:**
1. ✅ B at position 3
2. ✅ R(Row 2, pos 3) faces B(Row 1, pos 3)
3. ✅ A(pos 2) is to B's right (facing South: right = paper-left = pos 2)
4. ✅ S(pos 2) is to R's left (facing North: left = paper-left = pos 2)
5. ✅ D(pos 1) not adjacent to B(pos 3): gap = 1 position, not adjacent ✓
6. ✅ P(pos 1) does not face C(pos 4): P faces D ✓

**Answers:**

**Q1:** D at Row 1 position 1. Faces Row 2 position 1 = **P**.

**Q2:** C at position 4, A at position 2. People between = $|4-2| - 1 = 1$ (B at position 3). **One person.**

**Q3:** P at Row 2 position 1, facing North. P's right = paper-right = position 2 = **S**.

**Q4:** Facing pairs: D↔P, A↔S, B↔R, C↔Q.

---

### Problem B2: Circular with Mixed Facing (Set of 5 Questions)

> Eight people — A, B, C, D, E, F, G, H — sit around a circular table.
> A, C, E, G face the center. B, D, F, H face outward.
>
> **Clues:**
> 1. A sits third to the left of B.
> 2. C sits opposite to A.
> 3. D sits immediately to the left of C.
> 4. E is not adjacent to A.
> 5. G sits immediately to the left of F.
> 6. H sits second to the right of D.
>
> **Questions:**
> Q1. Who sits opposite to B?
> Q2. Who sits to the immediate left of E?
> Q3. How many people sit between G and B (counting clockwise from G)?
> Q4. Who sits second to the right of F?
> Q5. Which of the following is true?
>     (a) E is adjacent to F  (b) H is adjacent to A  (c) G is adjacent to B  (d) D faces E

**Solution:**

Fix A at position 1. Positions 1–8 clockwise.

**Direction rules:**
- Facing center: Left = Clockwise, Right = Anticlockwise.
- Facing outward: Left = Anticlockwise, Right = Clockwise.

**Clue 1:** "A sits third to the left of B." A is at the position that is third to B's left. B faces outward → B's left = anticlockwise. Three seats anticlockwise from B: $B - 3 = A = 1$, so $B = 4$.

**B at position 4.**

**Clue 2:** C opposite A (position 1) → **C at position 5** ($1 + 4 = 5$).

**Clue 3:** D immediately to the left of C. C faces center → C's left = clockwise. Clockwise from position 5 = position 6. **D at position 6.**

```
              1(A↓)
        8           2
      7               3
        6(D↑)       4(B↑)
              5(C↓)

↓ = faces center, ↑ = faces outward
```

**Clue 6:** H second to the right of D. D faces outward → D's right = clockwise. Two clockwise steps from position 6: 6→7→8. **H at position 8.**

**Clue 5:** G immediately to the left of F. F faces outward → F's left = anticlockwise. So G is one seat anticlockwise from F: $G = F - 1$.

Remaining positions: 2, 3, 7 for E, F, G.

Testing: F=3, G=2 → valid (both available). E=7.
Other options: F=7, G=6 (taken ✗); F=2, G=1 (taken ✗).

**F at position 3, G at position 2, E at position 7.**

**Clue 4:** E not adjacent to A. E at position 7, A at position 1. Adjacent to A: positions 2 and 8. E at 7 — not adjacent. ✅

```
              1(A↓)
        8(H↑)       2(G↓)
      7(E↓)           3(F↑)
        6(D↑)       4(B↑)
              5(C↓)
```

**Verification:**
1. ✅ A third to B's left: B at 4 (outward), left=ACW, three ACW from 4: 4→3→2→1 = A
2. ✅ C(5) opposite A(1): difference = 4 = $n/2$
3. ✅ D(6) immediately to C's left: C at 5 (center), left=CW=6
4. ✅ E(7) not adjacent to A(1)
5. ✅ G(2) immediately to F's left: F at 3 (outward), left=ACW=2
6. ✅ H(8) second to D's right: D at 6 (outward), right=CW, 6→7→8

**Answers:**

**Q1:** B at position 4. Opposite = position $4+4=8$ = **H**.

**Q2:** E at position 7, faces center. E's left = CW = position 8 = **H**.

**Q3:** G at position 2, B at position 4. Clockwise from G: 2→3→4. People between = 1 (F at position 3). **One person.**

**Q4:** F at position 3, faces outward. F's right = CW. Two CW steps from 3: 3→4→5 = position 5 = **C**.

**Q5:**
- (a) E(7) adjacent to F(3)? $|7-3|=4$, min$(4, 8-4)=4$. Not adjacent. ✗
- (b) H(8) adjacent to A(1)? $|8-1|=7 = n-1$. Adjacent (wraps around). ✅ **TRUE**
- (c) G(2) adjacent to B(4)? $|4-2|=2$. Not adjacent. ✗
- (d) D(6) faces E(7)? Opposite of 6 is position 2 (not 7). ✗

**Answer: (b)**

---

## 7.4 ESE-Style Problem

### Problem E1: Multi-Attribute Arrangement

> Six people — A, B, C, D, E, F — sit in a row facing North. Each person likes a different color: Red, Blue, Green, Yellow, White, Black.
>
> **Clues:**
> 1. A sits at position 3 and likes Blue.
> 2. The person who likes Red sits at position 1.
> 3. B sits immediately to the right of A.
> 4. C likes Green and does not sit at an extreme end.
> 5. D likes White and sits at position 5.
> 6. F sits at position 6.
>
> **Q1:** Who likes Red?
> **Q2:** What color does the person at position 2 like?

**Solution:**

Clue 1: A at position 3 (Blue). Clue 3: B at position 4. Clue 5: D at position 5 (White). Clue 6: F at position 6.

```
Pos:    1      2      3      4      5      6
       [__]   [__]   [A]    [B]    [D]    [F]
Color:  Red    __    Blue    __    White    __
```

Remaining people: C, E for positions 1 and 2.

Clue 4: C likes Green and doesn't sit at an extreme end. Extreme ends = positions 1 and 6. C ≠ position 1. So **C at position 2 (Green). E at position 1.**

Clue 2: Person at position 1 likes Red → **E likes Red.**

Remaining colors: Yellow, Black for B (pos 4) and F (pos 6).

```
Pos:    1      2      3      4      5      6
       [E]    [C]    [A]    [B]    [D]    [F]
Color:  Red   Green  Blue    ?    White    ?
```

**Q1:** Who likes Red? → **E**

**Q2:** Color at position 2 → **Green**

---

## 7.5 PSU-Style Problem

### Problem P1: Circular Arrangement

> Six engineers — P, Q, R, S, T, U — sit around a circular table, all facing the center.
> 1. P sits opposite to S.
> 2. Q sits immediately to the left of P.
> 3. R is not adjacent to S.
> 4. T sits opposite to Q.
> 5. U sits immediately to the right of S.
>
> **Question:** Who sits to the immediate left of R?

**Solution:**

Fix P at position 1. Positions 1–6 clockwise. $n=6$, opposite = $+3$.

Facing center: Left = Clockwise, Right = Anticlockwise.

Clue 1: S opposite P → S at position 4.

Clue 2: Q immediately to P's left (CW from P) → Q at position 2.

Clue 4: T opposite Q (position 2) → T at position 5.

Clue 5: U immediately to S's right (ACW from S at position 4) → position 3. U at position 3.

```
           1(P)
       6        2(Q)
       5(T)     3(U)
           4(S)
```

Remaining: R at position 6.

Clue 3: R not adjacent to S (position 4). Adjacent to S: positions 3(U) and 5(T). R at 6, not adjacent to 4. ✅

Immediate left of R (position 6): CW from 6 = position 1 = **P**.

**Answer: P**

---

## 7.6 Common Exam Patterns — What to Expect

### GATE

| Pattern | Frequency | Difficulty |
|:---:|:---:|:---:|
| Simple linear (5–6 people) | High | Easy-Medium |
| Circular (6–8 people) | Medium | Medium |
| Logic puzzle (multi-attribute) | Medium | Medium-Hard |
| Double-row | Low | Medium |

### Banking (IBPS/SBI)

| Pattern | Frequency | Difficulty |
|:---:|:---:|:---:|
| Double-row (8–10 people) | Very High | Medium |
| Circular with mixed facing | Very High | Medium-Hard |
| Circular (8 people, single facing) | High | Easy-Medium |
| Rectangular/Square table | Medium | Hard |
| Floor + Direction | Medium | Medium-Hard |
| Triple-row / Multi-row | Low | Very Hard |

### ESE

| Pattern | Frequency | Difficulty |
|:---:|:---:|:---:|
| Linear arrangement | Medium | Easy-Medium |
| Multi-attribute logic | Medium | Medium |
| Circular | Low | Medium |

---

## 7.7 Final Exam Strategy

### The 4-Point Checklist Before Answering

1. **Did I use ALL the clues?** If a clue wasn't used, either the arrangement isn't fully determined, or you missed applying it.

2. **Does every person have a unique seat?** No two people in the same seat. No seat with two people.

3. **Did I check the question carefully?** "Must be true" vs. "Could be true" vs. "Cannot be true" are very different questions.

4. **Did I verify at least 3 clues?** Don't verify all (wastes time), but spot-check the most complex clues.

### The Anti-Mistake Protocol

| Mistake | Prevention |
|:---:|:---:|
| Left/Right confusion | Write "L=CW" or "L=paper-right" at the top of your rough sheet |
| Forgetting facing direction | Mark arrows (↑↓) on every person in your diagram |
| Missing a "NOT" | Circle every negative word in the question |
| Two valid arrangements | Check all questions — they might need only the common elements |
| Running out of time | If arrangement isn't solved in 3 min (GATE) or 5 min (Bank), skip |

---

## 7.8 Quick-Reference: All Formulas in One Place

| Formula | Context |
|:---:|:---:|
| $L + R = n + 1$ | Linear: position from left + right |
| $\|p_1 - p_2\| - 1$ | People between two positions (linear) |
| $(n-1)!$ | Circular permutations |
| Opposite $= p + \frac{n}{2}$ | Circular, even $n$ |
| Left (facing center) = CW | Circular |
| Left (facing outward) = ACW | Circular |
| Left (facing North) = paper-left | Linear / Double-row |
| Left (facing South) = paper-right | Linear / Double-row |
| Block of $m$ in row of $n$ | $n - m + 1$ positions |

---

[← Previous: Advanced Techniques](06-Advanced-Techniques-and-Shortcuts.md) | [Back to Index](README.md)
