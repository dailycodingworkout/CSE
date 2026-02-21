---
layout: default
title: "Chapter 3: Circular Seating Arrangements"
description: "Round table arrangements, clockwise/anticlockwise conventions, opposite positions"
---

# Chapter 3: Circular Seating Arrangements

[← Previous: Linear Arrangements](02-Linear-Seating-Arrangements.html) | [Back to Index](./) | [Next: Double-Row Arrangements →](04-Double-Row-Seating-Arrangements.html)

---

## 3.1 What is a Circular Arrangement?

**The Atomic Truth:** *No endpoints; only relative positions matter.*

People sit around a round table. Unlike linear arrangements:
- There is **no "first" or "last" seat**.
- Positions are defined **relative to each other**, not absolute.
- **Clockwise** and **anticlockwise** replace left/right.

<div class="diagram">
<svg viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Nunito', sans-serif;">
  <!-- Table circle -->
  <circle cx="240" cy="175" r="120" fill="none" stroke="#d5dce4" stroke-width="2"/>
  <circle cx="240" cy="175" r="6" fill="#5d6d7e"/>
  <text x="240" y="195" text-anchor="middle" fill="#5d6d7e" font-size="9">center</text>

  <!-- CW arrow arc -->
  <path d="M 310 75 A 100 100 0 0 1 340 200" fill="none" stroke="#2e8b57" stroke-width="2" stroke-dasharray="6,3"/>
  <text x="365" y="130" fill="#2e8b57" font-size="11" font-weight="600">CW</text>

  <!-- ACW arrow arc -->
  <path d="M 170 75 A 100 100 0 0 0 140 200" fill="none" stroke="#d94f4f" stroke-width="2" stroke-dasharray="6,3"/>
  <text x="105" y="130" fill="#d94f4f" font-size="11" font-weight="600">ACW</text>

  <!-- Position 1 (top) -->
  <circle cx="240" cy="50" r="22" fill="#1a8a8a" stroke="#1a8a8a" stroke-width="2"/>
  <text x="240" y="55" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">1</text>

  <!-- Position 2 -->
  <circle cx="328" cy="87" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="328" y="92" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">2</text>

  <!-- Position 3 -->
  <circle cx="362" cy="175" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="362" y="180" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">3</text>

  <!-- Position 4 -->
  <circle cx="328" cy="263" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="328" y="268" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">4</text>

  <!-- Position 5 (bottom - opposite of 1) -->
  <circle cx="240" cy="300" r="22" fill="#e8a317" stroke="#e8a317" stroke-width="2"/>
  <text x="240" y="305" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">5</text>

  <!-- Position 6 -->
  <circle cx="152" cy="263" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="152" y="268" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">6</text>

  <!-- Position 7 -->
  <circle cx="118" cy="175" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="118" y="180" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">7</text>

  <!-- Position 8 -->
  <circle cx="152" cy="87" r="22" fill="#4a5da8" stroke="#4a5da8" stroke-width="2"/>
  <text x="152" y="92" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">8</text>

  <!-- Opposite line 1-5 -->
  <line x1="240" y1="72" x2="240" y2="278" stroke="#e8a317" stroke-width="1.5" stroke-dasharray="5,4"/>
  <text x="270" y="175" fill="#e8a317" font-size="10" font-weight="600">opposite</text>

  <!-- Legend -->
  <rect x="100" y="340" width="280" height="35" rx="8" fill="#f9fafb" stroke="#d5dce4" stroke-width="1.5"/>
  <circle cx="130" cy="357" r="6" fill="#1a8a8a"/>
  <text x="145" y="362" fill="#2c3e50" font-size="10">Fix as anchor</text>
  <circle cx="240" cy="357" r="6" fill="#e8a317"/>
  <text x="255" y="362" fill="#2c3e50" font-size="10">Opposite (n/2)</text>
  <text x="340" y="362" fill="#2e8b57" font-size="10">CW = clockwise</text>
</svg>
<div class="diagram-caption">Circular Table (8 seats): positions numbered clockwise, seat 1 opposite seat 5</div>
</div>

> **Analogy:** A clock has no "start" — 12 o'clock is a convention. Similarly, in circular seating, you **fix one person** as the reference point and describe everyone else relative to them.

---

## 3.2 Why Circular is Different — The Rotation Principle

### The Key Formula: Arrangements of $n$ in a Circle

In a **line**, $n$ people can be arranged in $n!$ ways.

In a **circle**, we fix one person (to remove rotational equivalence), so:

$$\text{Circular permutations} = (n-1)!$$

**Why $(n-1)!$ ?** Imagine 4 people A, B, C, D around a table:

```
    A              B              C              D
  D   B    =     A   C    =     D   B    =     C   A
    C              D              A              B
```

All four of these are the **same** arrangement (just rotated). There are $n = 4$ rotations of each unique arrangement, so:

$$\frac{n!}{n} = (n-1)!$$

> **GATE Insight:** Circular permutation counting problems are rare in GATE but appear in probability questions. The arrangement-deduction type (who sits where) is much more common.

---

## 3.3 Clockwise and Anticlockwise

### Convention

Looking at the table **from above** (bird's eye view):

```
          12
     11        1
   10            2
   9      ●      3        Clockwise: 12→1→2→3→...→11→12
   8              4        Anticlockwise: 12→11→10→...→1→12
     7          5
          6
```

**Clockwise (CW):** Same direction as clock hands.

**Anticlockwise (ACW) / Counterclockwise (CCW):** Opposite direction.

### The CW/ACW Position Formula

If person X is at some position and Y is $k$ positions **clockwise** from X, count $k$ seats in the clockwise direction.

If there are $n$ seats total:

$$\text{Position of Y} = (\text{Position of X} + k) \mod n$$

(Using 0-indexed positions)

### Critical Trap: "To the Left" in Circular

> "A sits second to the left of B."

In circular arrangements, the convention is:

<div class="diagram">
<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Nunito', sans-serif;">
  <!-- FACING CENTER box -->
  <rect x="20" y="10" width="310" height="175" rx="12" fill="#e0f5f5" stroke="#1a8a8a" stroke-width="2"/>
  <text x="175" y="35" text-anchor="middle" fill="#1a8a8a" font-size="14" font-weight="700" font-family="Architects Daughter, cursive">Facing CENTER (inward)</text>
  <!-- Person icon facing center -->
  <circle cx="175" cy="90" r="20" fill="#1a8a8a" opacity="0.2" stroke="#1a8a8a" stroke-width="2"/>
  <text x="175" y="95" text-anchor="middle" fill="#1a8a8a" font-size="13" font-weight="700">P</text>
  <path d="M175,70 L175,55" stroke="#1a8a8a" stroke-width="2" marker-end="url(#afc)"/>
  <text x="175" y="50" text-anchor="middle" fill="#5d6d7e" font-size="9">faces center</text>
  <!-- Left arrow = CW -->
  <path d="M155,90 L80,90" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#afcl)"/>
  <text x="110" y="80" text-anchor="middle" fill="#2e8b57" font-size="12" font-weight="700">Left = CW</text>
  <!-- Right arrow = ACW -->
  <path d="M195,90 L270,90" stroke="#d94f4f" stroke-width="2.5" marker-end="url(#afcr)"/>
  <text x="240" y="80" text-anchor="middle" fill="#d94f4f" font-size="12" font-weight="700">Right = ACW</text>
  <!-- Physical test -->
  <text x="175" y="160" text-anchor="middle" fill="#5d6d7e" font-size="10">Your left hand points CW</text>
  <text x="175" y="175" text-anchor="middle" fill="#5d6d7e" font-size="10">when you face the center</text>

  <!-- FACING OUTWARD box -->
  <rect x="370" y="10" width="310" height="175" rx="12" fill="#fdeaea" stroke="#d94f4f" stroke-width="2"/>
  <text x="525" y="35" text-anchor="middle" fill="#d94f4f" font-size="14" font-weight="700" font-family="Architects Daughter, cursive">Facing OUTWARD</text>
  <!-- Person icon facing outward -->
  <circle cx="525" cy="90" r="20" fill="#d94f4f" opacity="0.2" stroke="#d94f4f" stroke-width="2"/>
  <text x="525" y="95" text-anchor="middle" fill="#d94f4f" font-size="13" font-weight="700">P</text>
  <path d="M525,110 L525,125" stroke="#d94f4f" stroke-width="2" marker-end="url(#afo)"/>
  <text x="525" y="140" text-anchor="middle" fill="#5d6d7e" font-size="9">faces outward</text>
  <!-- Left arrow = ACW (FLIPPED!) -->
  <path d="M505,90 L430,90" stroke="#d94f4f" stroke-width="2.5" marker-end="url(#afol)"/>
  <text x="460" y="80" text-anchor="middle" fill="#d94f4f" font-size="12" font-weight="700">Left = ACW</text>
  <!-- Right arrow = CW (FLIPPED!) -->
  <path d="M545,90 L620,90" stroke="#2e8b57" stroke-width="2.5" marker-end="url(#afor)"/>
  <text x="590" y="80" text-anchor="middle" fill="#2e8b57" font-size="12" font-weight="700">Right = CW</text>
  <!-- Physical test -->
  <text x="525" y="160" text-anchor="middle" fill="#5d6d7e" font-size="10">Your left hand points ACW</text>
  <text x="525" y="175" text-anchor="middle" fill="#5d6d7e" font-size="10">when you face outward</text>

  <!-- Arrow markers -->
  <defs>
    <marker id="afc" markerWidth="6" markerHeight="5" refX="3" refY="5" orient="auto"><path d="M0,5 L3,0 L6,5" fill="none" stroke="#1a8a8a" stroke-width="1.5"/></marker>
    <marker id="afo" markerWidth="6" markerHeight="5" refX="3" refY="0" orient="auto"><path d="M0,0 L3,5 L6,0" fill="none" stroke="#d94f4f" stroke-width="1.5"/></marker>
    <marker id="afcl" markerWidth="6" markerHeight="5" refX="0" refY="2.5" orient="auto"><path d="M6,0 L0,2.5 L6,5" fill="#2e8b57"/></marker>
    <marker id="afcr" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5" fill="#d94f4f"/></marker>
    <marker id="afol" markerWidth="6" markerHeight="5" refX="0" refY="2.5" orient="auto"><path d="M6,0 L0,2.5 L6,5" fill="#d94f4f"/></marker>
    <marker id="afor" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5" fill="#2e8b57"/></marker>
  </defs>
</svg>
<div class="diagram-caption">The Left/Right Flip: Direction reverses based on facing direction</div>
</div>

But **ONLY if they face the center** (which is the default in round table problems).

If they face **outward** (away from center), left and right swap!

| Facing | Left | Right |
|--------|------|-------|
| Inward (towards center) | Clockwise | Anticlockwise |
| Outward (away from center) | Anticlockwise | Clockwise |

> **The Aha Moment:** Sit at a round table. Face the center. Your left hand points clockwise around the table. Now turn around (face outward). Your left hand points anticlockwise. *The direction of "left" flips when facing flips.*

---

## 3.4 The "Opposite" Concept

In a circular arrangement of $n$ people (where $n$ is even), the person **directly opposite** to someone at position $p$ is at:

$$\text{Opposite position} = \left(p + \frac{n}{2}\right) \mod n$$

For $n = 8$: Opposite of position 1 is position 5. Opposite of position 3 is position 7.

If $n$ is **odd**, there is **no exact opposite** — this is a common trick question.

### Quick Table for Common Sizes

| People ($n$) | Opposite of seat $k$ | Neighbours of seat $k$ |
|:---:|:---:|:---:|
| 6 | $k + 3$ | $k-1$, $k+1$ |
| 8 | $k + 4$ | $k-1$, $k+1$ |
| 10 | $k + 5$ | $k-1$, $k+1$ |
| 12 | $k + 6$ | $k-1$, $k+1$ |

(All positions modulo $n$)

---

## 3.5 Solving Framework for Circular Arrangements

### Step 1: Fix the Anchor

Choose one person (usually the one mentioned first or most constrained) and **fix** them at a position. In circular problems, this person's absolute position doesn't matter — only relative positions do.

> **Convention:** Fix the anchor at the "12 o'clock" position (top of the circle).

### Step 2: Build Outward

From the anchor, place people using clockwise/anticlockwise clues.

### Step 3: Use the Opposite Shortcut

If A is opposite B, and you've placed A, B's position is determined immediately (for even $n$).

### Step 4: Apply "Not Adjacent" Constraints Last

Negative constraints ("C is not next to D") are best used for elimination after most people are placed.

---

## 3.6 Solved Example 1 — Basic Circular (GATE Style)

> **Important Convention Established Here:** For someone **facing the center** of a round table with positions numbered clockwise:
> - **Left = Clockwise** (your left hand points clockwise when facing inward)
> - **Right = Anticlockwise** (your right hand points anticlockwise when facing inward)
>
> Derivation: Person at position 1 (top) faces downward toward center. Their left hand points to position 2 (clockwise). Person at position 5 (bottom) faces upward toward center. Their left hand points to position 6 (clockwise). This holds for every position.

### Problem

> Eight people — A, B, C, D, E, F, G, H — sit around a circular table, all facing the center.
> 1. A sits opposite to E.
> 2. B sits immediately to the left of A.
> 3. H sits third to the left of E.
> 4. D sits opposite to B.
> 5. F sits immediately to the right of E.
> 6. C is not adjacent to D.
>
> **Question:** Who sits opposite to H?

### Solution

**Rule:** Facing center → Left = Clockwise, Right = Anticlockwise.

**Step 1:** Fix A at position 1 (top). Number positions 1–8 clockwise.

```
              1(A)
          8       2
        7           3
          6       4
              5
```

**Step 2:** Clue 1 → E opposite A. E at position 5 ($1 + 4 = 5$).

**Step 3:** Clue 2 → B immediately to A's left. Left = clockwise. B at position 2.

**Step 4:** Clue 4 → D opposite B (position 2). D at position 6 ($2 + 4 = 6$).

**Step 5:** Clue 5 → F immediately to E's right. Right = anticlockwise from position 5 → position 4. F at position 4.

**Step 6:** Clue 3 → H is third to the left of E. Left = clockwise from E (position 5). Three clockwise steps: 5→6→7→8. H at position 8.

```
              1(A)
        8(H)      2(B)
        7           3
          6(D)    4(F)
              5(E)
```

**Step 7:** Remaining: C, G for positions 3 and 7.

Clue 6: C not adjacent to D (position 6). Adjacent to D: positions 5 and 7. Position 5 is E. So C ≠ 7. **C at position 3, G at position 7.**

```
              1(A)
        8(H)      2(B)
      7(G)          3(C)
          6(D)    4(F)
              5(E)
```

**Verification:**
1. ✅ A(1) opposite E(5): difference = 4 = $n/2$
2. ✅ B(2) is one clockwise step from A(1) → B is to A's left
3. ✅ H(8) is three clockwise steps from E(5): 5→6→7→8
4. ✅ D(6) opposite B(2): difference = 4
5. ✅ F(4) is one anticlockwise step from E(5) → F is to E's right
6. ✅ C(3) not adjacent to D(6): 3 and 6 are not adjacent ✓

**Answer:** H is at position 8. Opposite = position $8 - 4 = 4$ = **F**.

**H sits opposite to F.**

---

## 3.7 The "Facing Outward" Variant

Some problems specify that some (or all) people face **away from the center** (outward). This flips the left/right convention for those people:

| Facing | Left | Right |
|--------|------|-------|
| Center (inward) | Clockwise | Anticlockwise |
| Outward | Anticlockwise | Clockwise |

### Mixed Facing Example

> "A faces the center. B faces outward. B is immediately to the left of A."

A faces center → A's left is clockwise.

But the question says B is to the left **of A**, so we use **A's perspective**. B is in the clockwise direction from A. ✓

> **Critical:** "X is to the left of Y" uses **Y's perspective** (not X's). Always ask: whose left?

---

## 3.8 Solved Example 2 — Mixed Facing (Banking Style)

### Problem

> Six people — P, Q, R, S, T, U — sit around a circular table.
> P, R, and T face the center. Q, S, and U face outward.
> 1. P sits opposite to S.
> 2. Q sits immediately to the right of P.
> 3. R is not adjacent to Q.
> 4. T sits immediately to the left of S.
>
> **Question:** Who sits to the immediate left of R?

### Solution

Fix P at position 1 (top). Positions 1–6 clockwise.

```
           1(P↓) ← faces center
       6        2
     5            3
           4
```

Clue 1: S opposite P. S at position 4 (opposite = $+3$ for $n=6$). S faces outward (↑ from position 4).

Clue 2: Q immediately to the right of P. P faces center → P's right = anticlockwise → position 6. Q at position 6. Q faces outward.

Clue 4: T immediately to the left of S. S at position 4, faces outward. S's left = anticlockwise (since S faces outward). Anticlockwise from 4 = position 3. T at position 3. T faces center.

```
           1(P↓)
     6(Q↑)       2
     5            3(T↓)
           4(S↑)
```

Remaining: R and U for positions 2 and 5.

Clue 3: R not adjacent to Q (pos 6). Adjacent to Q: positions 5 and 1. R ≠ 5. So **R at position 2**. U at position 5.

R faces center. U faces outward.

```
            1(P↓)
     6(Q↑)       2(R↓)
     5(U↑)       3(T↓)
            4(S↑)
     
↓ = facing center, ↑ = facing outward
```

**Who sits to the immediate left of R?**

R is at position 2, faces center. R's left = clockwise = position 3 = **T**.

**Answer: T**

---

## 3.9 Edge Cases in Circular Arrangements

### Edge Case 1: Odd Number of People — No Exact Opposite

With $n = 7$ (odd), there is no seat directly opposite any other seat. If a question mentions "opposite" with odd $n$, it's either:
- A trick question (answer: "not possible").
- Using "opposite" loosely to mean "across the table" (the two seats $\lfloor n/2 \rfloor$ apart).

### Edge Case 2: "Between" in Circular — Two Paths

"How many people sit between A and B?"

In a circle, there are **two arcs** between any two people. Unless specified (clockwise or anticlockwise), the question usually means the **shorter arc** — but **read carefully**.

For $n = 8$, A at position 1, B at position 4:
- Clockwise path: 1→2→3→4 (2 people between)
- Anticlockwise path: 1→8→7→6→5→4 (4 people between)

If the question says "between A and B when going clockwise from A," the answer is 2.

### Edge Case 3: "Third to the left" Wrapping Around

In a circle of 6, if A is at position 2 and B is "4th to the left (clockwise) of A":
- Clockwise: 2→3→4→5→6. B at position 6.
- This wraps around naturally in circles.

---

## 3.10 Circular Arrangement Tricks

### Trick 1: The Opposite Cascade

If you know A opposite E, and B opposite D, you've fixed 4 out of 8 positions with just 2 clues. Always process "opposite" clues first — they give maximum information per clue.

### Trick 2: The Gap Counter

To verify adjacency: in an 8-seat circle, positions $p$ and $q$ are adjacent if and only if:

$$|p - q| = 1 \quad \text{or} \quad |p - q| = n - 1$$

(The second condition handles the wrap-around: positions 1 and 8 are adjacent.)

### Trick 3: Fix and Forget

After fixing the anchor, **never move them**. All other positions are relative. If you get a contradiction, the error is in your placement of someone *other than* the anchor.

### Trick 4: The "Unfolded Circle" Method

For complex circular problems, mentally "cut" the circle and lay it flat:

```
Circle: 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - [back to 1]
Flat:   1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 1' - 2' - 3'...
```

This lets you use linear techniques. Just remember that position $n+1$ = position 1.

---

## 3.11 Comparison: Linear vs. Circular

| Feature | Linear | Circular |
|---------|--------|----------|
| Endpoints | Yes (2) | No |
| Absolute positions | Yes | No (one must be fixed) |
| "Opposite" | Not applicable | $p + n/2$ (even $n$ only) |
| Left/Right | Depends on facing direction | Depends on facing + CW/ACW |
| "Between" | Only one path | Two paths (arcs) |
| Total arrangements | $n!$ | $(n-1)!$ |
| Wrapping | No | Yes |

---

## 3.12 Summary: Circular Arrangement Cheat Sheet

| Concept | Formula / Rule |
|---------|---------------|
| Circular permutations | $(n-1)!$ |
| Opposite position ($n$ even) | $(p + n/2) \mod n$ |
| Left (facing center) | Clockwise direction |
| Right (facing center) | Anticlockwise direction |
| Left (facing outward) | Anticlockwise direction |
| Right (facing outward) | Clockwise direction |
| Adjacent positions | $\|p-q\| = 1$ or $\|p-q\| = n-1$ |
| "Between" on shorter arc | $\min(d, n-d) - 1$ where $d = \|p-q\|$ |

---

[← Previous: Linear Arrangements](02-Linear-Seating-Arrangements.html) | [Back to Index](./) | [Next: Double-Row Arrangements →](04-Double-Row-Seating-Arrangements.html)
