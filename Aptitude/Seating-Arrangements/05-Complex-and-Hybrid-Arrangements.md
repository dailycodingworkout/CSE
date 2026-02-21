# Chapter 5: Complex & Hybrid Arrangements

[← Previous: Double-Row Arrangements](04-Double-Row-Seating-Arrangements.md) | [Back to Index](README.md) | [Next: Advanced Techniques →](06-Advanced-Techniques-and-Shortcuts.md)

---

## 5.1 Overview

**The Atomic Truth:** *Combine basic types; constraints multiply.*

Complex arrangements extend the fundamental linear and circular models into:
- **Rectangular / Square tables**
- **Polygonal (hexagonal, octagonal) tables**
- **Floor / Multi-level puzzles**
- **Matrix / Grid seating**
- **Hybrid** (mix of row + circular, floor + row, etc.)

These appear in:
- **Banking exams:** High-difficulty sets (25–30 mark level)
- **GATE/ESE:** Occasionally in General Aptitude as multi-constraint logic puzzles

---

## 5.2 Rectangular and Square Table Arrangements

### 5.2.1 The Layout

A rectangular table has **sides** and **corners**:

```
         ┌──────────────────┐
         │   2       3      │
     1   │                  │   4
         │                  │
     8   │                  │   5
         │   7       6      │
         └──────────────────┘
```

For a typical 8-person rectangular table:

```
              North Side
         ┌──────────────────┐
         │  P2      P3      │
   P1    │                  │   P4        ← Short sides (1 person each)
 (West)  │                  │  (East)
   P8    │                  │   P5
         │  P7      P6      │
         └──────────────────┘
              South Side
```

| Position Type | Count | Property |
|:---:|:---:|:---:|
| Long side (North/South) | 2 per side = 4 | Each person has 2 side-neighbours |
| Short side (East/West) | 2 per side = 4 | Each is a "corner" — has 2 neighbours from different sides |

**Corner vs. Side Rule:**
- Corner people sit at the ends of the long sides (or the middle of short sides, depending on the table shape).
- The problem will typically specify: "P sits at a corner" or "P sits on the longer side."

### 5.2.2 "Opposite" in a Rectangle

Unlike a circle where opposite is $+n/2$:
- **Long-side opposite:** P2 is opposite P7 (across the table on the same "column").
- **Short-side opposite:** P1 is opposite P4 (or P5, depending on geometry).

The question must specify the geometry or give a diagram. **Never assume** — different problems use different rectangular layouts.

### 5.2.3 Adjacency in Rectangular Tables

Adjacency wraps around corners:

```
P1 is adjacent to P2 and P8 (corner wraps to both sides).
P2 is adjacent to P1 and P3.
P4 is adjacent to P3 and P5 (corner wraps).
```

This is essentially a **circular arrangement with distinguished positions** (corners vs. sides).

---

## 5.3 Solved Example — Rectangular Table

### Problem

> Eight people A–H sit around a rectangular table with 3 people on each longer side and 1 on each shorter side.
>
> ```
>           ┌─────────────┐
>           │  B2  B3  B4 │
>     B1    │             │    B5
>           │  B8  B7  B6 │
>           └─────────────┘
> ```
>
> North side (top): 3 seats. South side (bottom): 3 seats. East/West: 1 seat each.
>
> **Clues:**
> 1. A sits on the shorter side (East or West).
> 2. E sits diagonally opposite to A.
> 3. B sits immediately to the right of A.
> 4. D sits on the North side.
> 5. C sits opposite to D (across the table on the South side).
> 6. F is not adjacent to A.
> 7. G sits to the immediate left of D.
> 8. H does not sit on a shorter side.

### Solution

Let me number positions as shown:

```
            ┌─────────────┐
            │  2    3    4 │   ← North side
      1     │              │     5    ← Shorter sides
            │  8    7    6 │   ← South side
            └─────────────┘
```

Adjacency: 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 7-8, 8-1.
Opposite pairs (across table): 2↔8, 3↔7, 4↔6, 1↔5 (diagonally across short sides).

Clue 1: A at position 1 or 5 (shorter sides).

Clue 3: B immediately to A's right.
- If A at position 1 (West side, facing East → right = North direction = position 2). B at 2.
- If A at position 5 (East side, facing West → right = South direction = position 6). B at 6.

Let's try A at position 1, B at position 2.

Clue 2: E diagonally opposite A. A at position 1 → diagonally opposite is position 5. **E at position 5.**

Clue 4: D on North side → positions 2, 3, or 4. Position 2 is B. D at position 3 or 4.

Clue 7: G immediately to the left of D. If D at position 3 → G immediately to D's left.
People on the North side face South. Facing South → left = paper-right (increasing positions). G at position 4.
If D at position 4 → G at position 5. But E is at 5. So **D at position 3, G at position 4.**

Clue 5: C opposite D (across table). D at position 3 → opposite = position 7. **C at position 7.**

```
            ┌─────────────┐
            │ [B]  [D]  [G]│   ← North: 2, 3, 4
     [A]    │              │    [E]   ← Short: 1, 5
            │  8   [C]   6 │   ← South: 8, 7, 6
            └─────────────┘
```

Remaining: F, H for positions 6 and 8.

Clue 8: H not on shorter side. H is not at 1 or 5 (already occupied anyway). H at 6 or 8 — both are on longer side (South). Both valid.

Clue 6: F not adjacent to A (position 1). Adjacent to 1: positions 2 and 8. Position 2 is B. So F ≠ 8. **F at position 6, H at position 8.**

```
            ┌─────────────┐
            │ [B]  [D]  [G]│
     [A]    │              │    [E]
            │ [H]  [C]  [F]│
            └─────────────┘
```

**Verification:**
1. ✅ A at position 1 (shorter side)
2. ✅ E at position 5 (diagonally opposite A)
3. ✅ B at position 2 (immediately right of A)
4. ✅ D at position 3 (North side)
5. ✅ C at position 7 (opposite D on South side)
6. ✅ F at position 6, not adjacent to A
7. ✅ G at position 4 (immediately left of D from D's perspective facing South)
8. ✅ H at position 8 (not on shorter side) ✓

---

## 5.4 Floor / Multi-Level Puzzles

### 5.4.1 The Concept

People live on different floors of a building. "Above" and "below" replace "left" and "right."

```
Floor 5:  [__]    (topmost)
Floor 4:  [__]
Floor 3:  [__]
Floor 2:  [__]
Floor 1:  [__]    (ground floor / bottommost)
```

This is essentially a **vertical linear arrangement**.

### Key Properties

| Property | Detail |
|----------|--------|
| Endpoints | Top floor and bottom (ground) floor |
| "Above" | Higher floor number |
| "Below" | Lower floor number |
| "Immediately above" | Next floor up (floor + 1) |
| "Between" floors $a$ and $b$ | Floors strictly between $a$ and $b$ |
| "As many above as below" | Middle floor (odd count) |

### 5.4.2 The Ground Floor Trap

> **Critical:** Some problems start numbering from 0 (ground floor = 0, first floor = 1). Others start from 1 (ground floor = 1). Always check the problem statement.

In Indian convention: Ground floor is typically floor 0 or floor 1. The problem will specify.

### 5.4.3 Formula: Position from Top/Bottom

Same as linear arrangement:

$$\text{Floor from bottom} + \text{Floor from top} = n + 1$$

Where $n$ = total floors.

---

## 5.5 Solved Example — Floor Puzzle

### Problem

> Seven people — A, B, C, D, E, F, G — live on 7 different floors (1 = ground, 7 = top).
> 1. C lives on an odd-numbered floor.
> 2. B lives immediately above E.
> 3. A lives on floor 4.
> 4. D lives above A but not on the top floor.
> 5. F lives below C.
> 6. There are exactly two floors between B and G.
> 7. G lives above B.
>
> **Question:** On which floor does F live?

### Solution

Clue 3: A at floor 4.

Clue 4: D above A but not top. D ∈ {5, 6} (above 4, not 7).

Clue 2: B immediately above E → B = E + 1. They occupy consecutive floors, B higher.

Clue 6 & 7: G above B, exactly 2 floors between B and G → G = B + 3.

Possible (B, G) pairs: (1,4), (2,5), (3,6), (4,7). But A at 4, so B ≠ 4 and G ≠ 4.
- (1, 4): G = 4 → conflict with A.
- (2, 5): B=2, G=5. E = B-1 = 1. ✓
- (3, 6): B=3, G=6. E = B-1 = 2. ✓
- (4, 7): B=4 → conflict with A.

**Case I:** B=2, E=1, G=5.

Clue 4: D ∈ {5, 6}. G=5, so D=6.

Placed: E=1, B=2, A=4, G=5, D=6. Remaining: C, F for floors 3 and 7.

Clue 1: C on odd floor. Floors 3 (odd) and 7 (odd). Both are odd. C can be at either.
Clue 5: F below C. If C=3, F must be below 3. Available: only floor 7 is left for F, but 7 > 3. Contradiction. So C=7, F=3.

Check Clue 5: F=3 below C=7. ✅

**Answer (Case I): F lives on floor 3.**

Let me verify Case II is invalid:

**Case II:** B=3, E=2, G=6.

Clue 4: D ∈ {5, 6}. G=6, so D=5.

Placed: E=2, B=3, A=4, D=5, G=6. Remaining: C, F for floors 1 and 7.

Clue 1: C odd → C=1 or 7. Both available and both odd.
Clue 5: F below C. If C=1, F must be below 1 — impossible. So C=7, F=1.

Check: F=1 below C=7. ✅. This is also valid!

**Two valid arrangements!** The question asks "On which floor does F live?" If F=3 in Case I and F=1 in Case II, the answer depends on which case is valid.

Checking for additional constraints: All clues are satisfied in both cases. The question as stated would have options that include 1 and 3, and both would be marked correct, or additional clues would eliminate one case.

> **Exam Insight:** If a problem gives two valid arrangements, the question will ask something that has the **same answer in both cases**, or one case will be eliminated by a subtle clue. Always check both cases.

In this example, the question might instead ask "Who lives on floor 7?" — answer: C (same in both cases).

---

## 5.6 Matrix / Grid Seating

### 5.6.1 The Layout

People sit in a grid (e.g., 3×3 or 4×4):

```
        Col 1   Col 2   Col 3
Row 1:  [1,1]   [1,2]   [1,3]
Row 2:  [2,1]   [2,2]   [2,3]
Row 3:  [3,1]   [3,2]   [3,3]
```

### 5.6.2 Adjacency in a Grid

Each cell has up to 4 neighbors (up, down, left, right):

| Position | Neighbors |
|:---:|:---:|
| Corner (e.g., [1,1]) | 2 neighbours |
| Edge (e.g., [1,2]) | 3 neighbours |
| Center ([2,2]) | 4 neighbours |

### 5.6.3 Key Questions in Grid Puzzles

- "Who sits directly above X?" → Same column, row − 1.
- "Who sits diagonally to X?" → (row±1, col±1).
- "How many people are between X and Y in the same row?" → $|col_X - col_Y| - 1$.

---

## 5.7 Hybrid Arrangements

### 5.7.1 Row + Circular

> "Group A sits in a row. Group B sits around a table. One person from Group A faces a specific person in Group B."

Solve each group separately first, then use the cross-group constraint to link them.

### 5.7.2 Floor + Direction

> "People live on different floors and face either East or West."

This combines floor puzzle with directional constraints. Treat "floor" as position and "facing direction" as an additional attribute (like a flag).

### 5.7.3 Day / Schedule Based

> "Each person does a different activity on each day of the week."

This is a **schedule matrix** — rows are people, columns are days. Constraints are similar to seating but in a 2D assignment matrix.

> **Method:** Create a matrix with rows (people) and columns (positions/days/activities). Mark each cell as ✓ (confirmed), ✗ (eliminated), or ? (unknown). Apply constraints row by row and column by column.

---

## 5.8 Strategy for Complex Arrangements

### The Divide-and-Conquer Rule

1. **Identify the sub-type(s)** — Is it row? Circular? Floor? Grid?
2. **Solve the spatial layout first** — Fix positions before adding attributes (direction, activity, etc.).
3. **Chain constraints across sub-types** — Use linking clues to merge partial solutions.
4. **Final validation** — Check every clue against the combined solution.

### The Attribute-Overlay Method

For problems with multiple attributes (position + direction + favorite color, etc.):

```
Person:     A      B      C      D
Position:   2      4      1      3
Direction:  North  South  North  South
Color:      Red    Blue   ?      Green
```

Solve position first, then overlay direction, then overlay other attributes. Each layer adds constraints but doesn't change the base positions.

---

## 5.9 Summary

| Arrangement Type | Key Concept | Major Trap |
|:---:|:---:|:---:|
| Rectangular table | Corners have 2 neighbours from different sides | "Opposite" definition varies |
| Floor puzzle | Vertical linear arrangement | Ground floor numbering (0 vs. 1) |
| Grid / Matrix | 2D positions, up to 4 neighbours | Diagonal vs. adjacent confusion |
| Hybrid | Multiple sub-types combined | Solving one sub-type without linking to other |
| Multi-attribute | Position + direction + property | Over-constraining one attribute early |

---

[← Previous: Double-Row Arrangements](04-Double-Row-Seating-Arrangements.md) | [Back to Index](README.md) | [Next: Advanced Techniques →](06-Advanced-Techniques-and-Shortcuts.md)
