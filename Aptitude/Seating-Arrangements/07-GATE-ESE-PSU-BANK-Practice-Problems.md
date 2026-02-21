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

> Five people — A, B, C, D, E — sit in a row facing North. B sits in the middle. A is not adjacent to B. D is to the immediate left of E. C sits at one of the ends.
>
> **Which of the following must be true?**
> (a) A sits at the left end
> (b) D is adjacent to B
> (c) C sits at the right end
> (d) E is adjacent to B

**Solution:**

Setup: 5 seats, all face North. Positions 1–5.

- B in the middle → **B at position 3**.
- C at one of the ends → C at position 1 or 5.
- A not adjacent to B → A ∉ {2, 4}.
- D immediately to the left of E (facing North, left = lower position). D at position $p$, E at position $p+1$.

A can be at positions 1 or 5 (not 2 or 4, not 3 since B is there).

**Case I:** C at position 1, A at position 5.
- D immediately left of E: D and E occupy positions 2 and 4 → D at 2, E at... wait, D at position $p$, E at $p+1$. Available: {2, 4}. D=2, E=3 (taken) ✗. D=4, E=5 (A is there) ✗.

Hmm, remaining positions are 2 and 4. D-E must be consecutive. But 2 and 4 are not consecutive. ✗

Actually wait — remaining positions for D and E: {2, 4}. These aren't consecutive, so "D immediately to left of E" (consecutive pair) can't be satisfied.

So **Case I fails**.

**Case II:** C at position 5, A at position 1.
- Remaining: D, E for positions {2, 4}. D at $p$, E at $p+1$. Positions 2 and 4 aren't consecutive. ✗

**Case II also fails?** Let me re-examine.

Wait — A not adjacent to B (position 3) → A ∉ {2, 4}. A ∈ {1, 5}. C at end → C ∈ {1, 5}. If C=1 and A=5, or C=5 and A=1.

But D and E are left with positions 2 and 4 in both cases. And D immediately left of E requires them to be consecutive. 2 and 4 aren't consecutive.

**I must have an error.** Let me reconsider: "to the immediate left" when facing North — left = towards position 1 (decreasing). So "D is to the immediate left of E" means D is at position $e-1$ where E is at position $e$. They need consecutive positions with D on the lower-numbered side.

From {2, 4}: D=2, E=4? Not consecutive (gap of 1 position). ✗

Hmm. Let me re-read: do I have the constraint right? A not adjacent to B means A ∉ {2, 4}. That's correct.

But maybe A could be at position 4 if... no, position 4 is adjacent to B (position 3).

So the constraint set as I wrote it has no solution! Let me fix: change "A is not adjacent to B" to "A is not adjacent to **C**."

**Corrected Problem G1:**

> Five people — A, B, C, D, E — sit in a row facing North. B sits in the middle. A is not adjacent to C. D is to the immediate left of E. C sits at one of the ends.
>
> **Which of the following must be true?**
> (a) A sits at position 2
> (b) D is adjacent to B
> (c) C sits at the right end
> (d) E is adjacent to B

**Solution (Corrected):**

B at position 3 (middle).

C at position 1 or 5.

D immediately left of E → D at $p$, E at $p+1$.

A not adjacent to C.

**Case I:** C at position 1.
- A not adjacent to C (position 1) → A ≠ position 2.
- A can be at {2, 4, 5} minus {2} = {4, 5}.
- D-E consecutive pair from remaining positions.

  **Sub-case I-A:** A at position 4.
  - Remaining: D, E for {2, 5}. Not consecutive. ✗

  **Sub-case I-B:** A at position 5.
  - Remaining: D, E for {2, 4}. Not consecutive. ✗

  **Case I fails entirely.**

**Case II:** C at position 5.
- A not adjacent to C (position 5) → A ≠ position 4.
- A ∈ {1, 2, 4} \ {4} = {1, 2}.

  **Sub-case II-A:** A at position 1.
  - Remaining: D, E for {2, 4}. Not consecutive. ✗

  **Sub-case II-B:** A at position 2.
  - Remaining: D, E for {1, 4}. Not consecutive. ✗

**All cases fail!** The constraint set is again inconsistent.

The issue is that with B fixed at 3 and C at an end, the remaining positions for D-E are always non-consecutive from the set {1,2,4,5} minus A's position.

Let me construct a **valid** GATE problem:

### Problem G1 (Final Version)

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

### Problem B1: Double-Row (Set of 5 Questions)

> Eight people — A, B, C, D and P, Q, R, S — sit in two parallel rows of 4 each.
> Row 1: A, B, C, D sit facing South.
> Row 2: P, Q, R, S sit facing North.
> Each person in Row 1 faces exactly one person in Row 2.
>
> **Clues:**
> 1. B sits second from the right end of Row 1.
> 2. Q faces B.
> 3. A sits at the right end of Row 1.
> 4. R sits immediately to the right of Q.
> 5. D is not adjacent to B.
> 6. P does not face A.
>
> **Questions:**
> Q1. Who sits at the left end of Row 2?
> Q2. Who faces D?
> Q3. How many people sit between C and A in Row 1?
> Q4. Who sits to the immediate right of P?
> Q5. Which of the following pairs face each other?

**Solution:**

Positions 1–4, left to right on paper. Row 1 faces South, Row 2 faces North.

**Direction convention:**
- Row 1 (South): their right = paper-left (decreasing positions), their left = paper-right (increasing positions).
- Row 2 (North): their right = paper-right (increasing positions), their left = paper-left (decreasing positions).

Wait — "right end of Row 1" — in banking exams, "right end" and "left end" typically refer to the **reader's perspective** (or equivalently, from the perspective of the people in that row). Let me go with the person's perspective:

Row 1 faces South → their right = paper-left → "right end" = position 1 (paper-left end).

Hmm, this is ambiguous. Let me use the standard banking exam convention where positions are numbered from the perspective of the row's inhabitants:

**Simplified convention:** 

For Row 1 (facing South): Seat numbers 1-4 from THEIR left to THEIR right.
- Their left = paper-right → Seat 1 = paper-right position.
- Their right = paper-left → Seat 4 = paper-left position.

This gets confusing. Let me use the most common convention: **positions 1-4 from left to right on paper, and "left/right end" refers to paper-left/right regardless of facing.**

**Using paper-based convention:**

Clue 3: A at the right end of Row 1 → A at position 4.

Clue 1: B second from the right end of Row 1 → B at position 3 (counting from the right: 4, 3, 2, 1 → second from right = position 3).

Clue 2: Q faces B → Q at Row 2, position 3.

```
Row 1 (South):  [__]  [__]  [B]   [A]     (positions 1-4)
                  |     |     |      |
Row 2 (North):  [__]  [__]  [Q]   [__]    (positions 1-4)
```

Clue 4: R immediately to the right of Q. "Right of Q" — Q is in Row 2, facing North. Q's right = paper-right = position 4. **R at Row 2, position 4.**

Clue 6: P does not face A. A at Row 1 position 4. P ≠ Row 2 position 4. R is at position 4, so this is automatically satisfied (P isn't there anyway). But we still need to place P.

Remaining Row 2: P, S for positions 1 and 2.

Actually, does Clue 6 give us more? P not at Row 2 position 4 (already occupied by R). No additional constraint from Clue 6 since R is already there.

Remaining Row 1: C, D for positions 1 and 2.

Clue 5: D not adjacent to B (position 3). Adjacent to B: positions 2 and 4. Position 4 is A. So D ≠ position 2. **D at position 1, C at position 2.**

```
Row 1 (South):  [D]   [C]   [B]   [A]     (positions 1-4)
                  |     |     |      |
Row 2 (North):  [__]  [__]  [Q]   [R]     (positions 1-4)
```

Now, Clue 6 again: P does not face A. A at position 4, facing position = Row 2 position 4 = R. P doesn't face A → P ≠ position 4 (already satisfied).

Remaining Row 2: P, S for positions 1 and 2. No further constraints distinguish them from the given clues.

Wait — let me re-check if there are implicit constraints. We have P and S for positions 1 and 2 in Row 2. Clue 6 says P doesn't face A (position 4). P is going to position 1 or 2, neither of which faces position 4. So Clue 6 is satisfied regardless.

Both arrangements (P at 1, S at 2) and (P at 2, S at 1) are valid. Let me check if any question needs disambiguation:

Actually, in banking exams, usually the clues uniquely determine the arrangement. Let me see if I missed something.

Re-reading clues... I've used all 6 clues. With P and S both possible at positions 1 and 2, we have two valid arrangements:

```
Arrangement I:
Row 1 (South):  [D]   [C]   [B]   [A]
                  |     |     |      |
Row 2 (North):  [P]   [S]   [Q]   [R]

Arrangement II:
Row 1 (South):  [D]   [C]   [B]   [A]
                  |     |     |      |
Row 2 (North):  [S]   [P]   [Q]   [R]
```

**Answering Questions:**

**Q1: Who sits at the left end of Row 2?**
- Arrangement I: P. Arrangement II: S.
- Answer depends on arrangement. In an exam, the options would include only one of these, or the question would ask "Who COULD sit at the left end?" with both as options.

Since the problem has ambiguity, let me add a clue to resolve it:

**Additional Clue 7:** S is adjacent to Q.

Q at position 3. Adjacent = positions 2 and 4. Position 4 = R. So S at position 2. P at position 1.

```
Row 1 (South):  [D]   [C]   [B]   [A]
                  |     |     |      |
Row 2 (North):  [P]   [S]   [Q]   [R]
```

**Answers:**

**Q1:** Left end of Row 2 = position 1 = **P**.

**Q2:** D at Row 1 position 1. Faces Row 2 position 1 = **P**.

**Q3:** C at position 2, A at position 4. People between = $|4-2| - 1 = 1$ (B at position 3). **One person.**

**Q4:** P at Row 2 position 1, facing North. P's right = paper-right = position 2 = **S**.

**Q5:** Facing pairs: D↔P, C↔S, B↔Q, A↔R. Answer from options would match one of these.

---

### Problem B2: Circular with Mixed Facing (Set of 5 Questions)

> Eight people — A, B, C, D, E, F, G, H — sit around a circular table.
> A, C, E, G face the center. B, D, F, H face outward.
>
> **Clues:**
> 1. A sits third to the left of B.
> 2. C sits opposite to A.
> 3. D sits immediately to the right of C.
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
>     (a) E is adjacent to F  (b) H is opposite G  (c) G is adjacent to B  (d) D faces E

**Solution:**

Fix A at position 1. Positions 1–8 clockwise.

**Direction rules:**
- Facing center: Left = Clockwise, Right = Anticlockwise.
- Facing outward: Left = Anticlockwise, Right = Clockwise.

Clue 1: A sits third to the left of B.

A faces center → A's left = clockwise.

But wait: "A sits third to the left of B" — this means A is at the position that is 3 seats to B's left. So we need to use B's perspective. B faces outward → B's left = anticlockwise.

Third to the left of B (anticlockwise from B): if B at position $b$, then third anticlockwise = $b - 3$ (in clockwise numbering, going anticlockwise means decreasing).

A at position 1. So $b - 3 ≡ 1 \pmod{8}$, i.e., $b = 4$.

**B at position 4.**

Clue 2: C opposite A (position 1). C at position 5.

Clue 3: D immediately to the right of C. C faces center → C's right = anticlockwise = decreasing in our numbering. D at position 4. But B is at position 4! ✗

Let me reconsider. "Immediately to the right of C" — from C's perspective. C faces center (at position 5, facing toward center which is roughly "up"). C's right = anticlockwise.

Anticlockwise from position 5 in clockwise numbering: 5 → 4. Position 4 = B. Conflict.

Alternative: Maybe "A sits third to the left of B" uses A's perspective. A faces center → A's left = clockwise. Third clockwise from A (position 1): 1→2→3→4. So B at position 4.

Same result. Let me try the other interpretation: "A sits third to the left of B" means A is in the direction of B's left, 3 seats away. B faces outward → B's left = anticlockwise. Three seats anticlockwise from B: B→(B-1)→(B-2)→(B-3). A = B-3. So B = A+3 = 1+3 = 4. Same result.

The conflict is with Clue 3. Let me adjust Clue 3: "D sits immediately to the **left** of C." C's left = clockwise (facing center). Clockwise from position 5 = position 6. D at position 6. ✓

**Corrected Clue 3: D sits immediately to the left of C.**

```
              1(A↓)
        8           2
      7               3
        6(D↑)       4(B↑)
              5(C↓)

↓ = faces center, ↑ = faces outward
```

Clue 6: H second to the right of D. D faces outward → D's right = clockwise = increasing. Two clockwise from D (position 6): 6→7→8. **H at position 8.**

```
              1(A↓)
        8(H↑)       2
      7               3
        6(D↑)       4(B↑)
              5(C↓)
```

Clue 5: G immediately to the left of F. We need to know who faces where.
G faces center → G's left = clockwise.
F faces outward → But the clue says "G sits to the left of F", which uses F's perspective.

"G sits immediately to the left of F" = G is at the position that is to F's left. F faces outward → F's left = anticlockwise. So G is one seat anticlockwise from F.

Remaining positions: 2, 3, 7 for E, F, G.

If F at position $f$, G is one anticlockwise from F = $f - 1$.

From {2, 3, 7}:
- F=3, G=2: valid (both in available set). E=7.
- F=7, G=6: position 6 is taken (D). ✗
- F=2, G=1: position 1 is taken (A). ✗

**F at position 3, G at position 2, E at position 7.**

Clue 4: E not adjacent to A. E at position 7, A at position 1. Adjacent to A: positions 2 and 8. E at 7 — not adjacent. ✅

```
              1(A↓)
        8(H↑)       2(G↓)
      7(E↓)           3(F↑)
        6(D↑)       4(B↑)
              5(C↓)
```

**Verification:**
1. A third to the left of B: B at 4, faces outward, B's left = anticlockwise. Three ACW from 4: 4→3→2→1 = A. ✅
2. C opposite A: positions 1 and 5, difference = 4 = $n/2$. ✅
3. D immediately to C's left: C at 5 faces center, left = CW = 6 = D. ✅
4. E at 7, not adjacent to A (1). Adjacent to 1: 2 and 8. ✅
5. G immediately to F's left: F at 3 faces outward, left = ACW = 2 = G. ✅
6. H second to D's right: D at 6 faces outward, right = CW. 6→7→8 = H. ✅

**All verified.** ✅

**Answers:**

**Q1:** B at position 4. Opposite = position $4+4=8$ = **H**.

**Q2:** E at position 7, faces center. E's left = CW = position 8 = **H**.

**Q3:** G at position 2, B at position 4. Clockwise from G: 2→3→4. People between = 1 (F at position 3). **One person.**

**Q4:** F at position 3, faces outward. F's right = CW = position 4 → but that's "immediately right." Second to the right = 2 CW steps: 3→4→5 = **C at position 5**.

Wait: re-read: "second to the right of F." F faces outward → right = CW. Two CW from 3: 3→4→5 = position 5 = **C**.

**Q5:**
- (a) E(7) adjacent to F(3)? 7 and 3 differ by 4, and by $8-4=4$. Not adjacent (need diff of 1 or 7). ✗
- (b) H(8) opposite G(2)? $|8-2| = 6 \neq 4$. ✗
- (c) G(2) adjacent to B(4)? $|4-2| = 2 \neq 1$. ✗
- (d) D(6) faces E(7)? "Faces" typically means opposite. $|7-6| = 1 \neq 4$. Not opposite. ✗

Hmm, none are true! Let me re-check.

Actually, let me reconsider option (b): H at 8, G at 2. $|8-2| = 6$, and $8-6 = 2$. Min distance = 2. Not opposite (need 4). ✗

Let me offer corrected options:
- (a) E is adjacent to G → E(7), G(2). $|7-2|=5$, $8-5=3$. Not adjacent. ✗
- (b) H is adjacent to A → H(8), A(1). $|8-1|=7 = n-1$. Adjacent (wraps around). ✅

So a corrected option (b) "H is adjacent to A" would be true.

Let me use this for the final answer:

**Q5 (corrected options):**
- (a) E is adjacent to F → ✗
- (b) H is adjacent to A → ✅ **TRUE**
- (c) G is adjacent to B → ✗
- (d) D faces E → ✗

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
> 4. C likes Green and sits to the left of B (not immediately).
> 5. D likes Yellow.
> 6. E does not sit adjacent to the person who likes Red.
> 7. F sits at position 6.
> 8. The person at position 5 likes White.
>
> **Q1:** Who likes Red?
> **Q2:** What color does the person at position 2 like?

**Solution:**

**Positions:**

Clue 1: A at position 3 (Blue).

Clue 3: B immediately to A's right (facing North, right = increasing). B at position 4.

Clue 7: F at position 6.

Clue 8: Position 5 has White.

```
Pos:    1      2      3      4      5      6
       [__]   [__]   [A]    [B]    [__]   [F]
Color:  Red    __    Blue    __    White    __
```

Clue 4: C likes Green, sits to the left of B (position 4), not immediately next to B. So C is at position 1 or 2 (not position 3 which is A, not position 2+1=3... wait "not immediately" means C ≠ position 3, which is already A). C to the left of B and not immediately left means C ∈ {1, 2} and C ≠ 3.

But position 1 has Red (Clue 2), and C likes Green. So C ≠ position 1.

**C at position 2 (Green).**

Clue 5: D likes Yellow. D can be at position 1, 5, or (remaining). Placed: A(3), B(4), C(2), F(6). Remaining: D, E for positions 1 and 5.

Clue 6: E not adjacent to the Red person (position 1). Adjacent to position 1 = position 2. E ≠ position 2 (already C's). But E could be at position 1 itself — the question is "not adjacent to the Red person," and if E IS the Red person, they're not adjacent to themselves (trivially true). Actually, "not adjacent to" typically means not in a neighboring seat, not about being the same person. If E is at position 1, the question becomes moot.

Let me interpret: E does not sit adjacent to position 1. Adjacent to position 1 = position 2 (C is there). So this constraint just says E ≠ position 2, which is already satisfied.

D likes Yellow. Position 1 has Red, position 5 has White. If D at position 1, D has Red but D likes Yellow — contradiction. **D at position 5 (White)**. But D likes Yellow, and position 5 has White. Contradiction!

So neither position works for D? D at 1 → D has Red (but likes Yellow) ✗. D at 5 → D has White (but likes Yellow) ✗.

Let me re-examine. The remaining positions for D and E are 1 and 5. Position 1's color = Red, Position 5's color = White. D likes Yellow. Neither matches.

This is contradictory. Let me fix: remove Clue 5 and change to "D likes White."

**Corrected Clue 5:** D likes White.

D at position 5 (White) ✓. **E at position 1 (Red).**

But Clue 6: E not adjacent to the Red person. E IS the Red person. "E does not sit adjacent to the person who likes Red" — if E IS that person, the statement is vacuously true (you can't be adjacent to yourself).

Remaining colors: Yellow, Black for B (position 4) and F (position 6).

No further constraints on colors. B gets Yellow or Black, F gets the other.

```
Pos:    1      2      3      4      5      6
       [E]    [C]    [A]    [B]    [D]    [F]
Color:  Red   Green  Blue    ?    White    ?
```

Remaining colors for positions 4 and 6: Yellow, Black.

**Q1:** Who likes Red? → **E**

**Q2:** Color at position 2 → **Green**

---

## 7.5 PSU-Style Problem

### Problem P1: Circular with Ranking Logic

> Five engineers — P, Q, R, S, T — sit around a circular table for a meeting, all facing the center. They are ranked 1st to 5th in seniority (1 = most senior).
>
> 1. The most senior engineer sits opposite to the least senior.
> 2. P is 2nd in seniority and sits immediately to the left of Q.
> 3. R is 4th in seniority and is not adjacent to P.
> 4. S sits immediately to the right of T.
>
> **Question:** What is Q's seniority rank?

**Solution:**

Fix positions 1–5 clockwise. Facing center: Left = CW, Right = ACW. $n=5$ (odd, no exact opposite).

Wait — $n=5$ is odd. Clue 1 says "sits opposite." With odd $n$, there's no exact diametrically opposite seat. This is a trap!

In a 5-seat circle, "opposite" could mean the seat(s) farthest away, which would be 2 seats away (both sides). The problem likely means the two people are as far apart as possible: 2 seats apart.

Or the problem expects us to recognize this is impossible with 5 seats. But most exam problems with "opposite" use even $n$.

For this problem, let me change to 6 people to make it consistent:

**Corrected:** Six engineers P, Q, R, S, T, U around a table.

Actually, let me simplify and present a clean problem:

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
