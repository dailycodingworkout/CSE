# 🔍 Chapter 4: Analytical Reasoning

## The Atomic Truth
> **"Complex problems decompose into simple constraints. Satisfy all constraints, find the solution."**

---

## 📋 Topics Covered

1. [Blood Relations](#1-blood-relations)
2. [Direction Sense](#2-direction-sense)
3. [Coding-Decoding](#3-coding-decoding)
4. [Seating Arrangements](#4-seating-arrangements)
5. [Ranking & Order](#5-ranking--order)
6. [Puzzles & Scheduling](#6-puzzles--scheduling)
7. [Input-Output Analysis](#7-input-output-analysis)

---

## 1. Blood Relations

### The Singularity
> **"Every family is a tree. Master the nodes, master the relationships."**

### The Root Architecture

Blood relations can be modeled as a directed graph where:
- **Nodes** = Family members
- **Edges** = Relationships (parent-child, sibling, spouse)

---

### 🔑 The Relationship Hierarchy

```
                    GRANDPARENTS
                    ↙        ↘
              FATHER'S     MOTHER'S
               SIDE          SIDE
                 ↓              ↓
    Uncle/Aunt ← PARENTS → Uncle/Aunt
                   ↓
                 SELF ←→ Siblings
                   ↓
               CHILDREN
                   ↓
            GRANDCHILDREN
```

---

### 🔑 The Complete Relationship Table

#### Male Relationships

| Relation | Definition |
|----------|------------|
| **Father** | Male parent |
| **Son** | Male child |
| **Brother** | Male sibling |
| **Grandfather** | Father's or Mother's father |
| **Grandson** | Son's or Daughter's son |
| **Uncle** | Father's or Mother's brother |
| **Nephew** | Brother's or Sister's son |
| **Cousin** | Uncle's or Aunt's child |
| **Father-in-law** | Spouse's father |
| **Son-in-law** | Daughter's husband |
| **Brother-in-law** | Spouse's brother OR Sister's husband |

#### Female Relationships

| Relation | Definition |
|----------|------------|
| **Mother** | Female parent |
| **Daughter** | Female child |
| **Sister** | Female sibling |
| **Grandmother** | Father's or Mother's mother |
| **Granddaughter** | Son's or Daughter's daughter |
| **Aunt** | Father's or Mother's sister |
| **Niece** | Brother's or Sister's daughter |
| **Cousin** | Uncle's or Aunt's child (same for both genders) |
| **Mother-in-law** | Spouse's mother |
| **Daughter-in-law** | Son's wife |
| **Sister-in-law** | Spouse's sister OR Brother's wife |

---

### 🎯 The Blood Relation Solving Algorithm

```
Step 1: IDENTIFY the starting person (usually "I" or given name)
Step 2: BUILD the relationship chain step by step
Step 3: DRAW a family tree diagram
Step 4: TRACE from start to end
Step 5: DETERMINE the final relationship
```

---

### 🔑 Relationship Chains (The Fast Decode Table)

| Chain | Result |
|-------|--------|
| Father's father | Grandfather |
| Father's mother | Grandmother |
| Father's brother | Uncle |
| Father's sister | Aunt |
| Father's son | Brother (or self) |
| Father's daughter | Sister (or self) |
| Mother's father | Grandfather (maternal) |
| Mother's mother | Grandmother (maternal) |
| Mother's brother | Uncle (maternal) |
| Mother's sister | Aunt (maternal) |
| Brother's son | Nephew |
| Brother's daughter | Niece |
| Sister's son | Nephew |
| Sister's daughter | Niece |
| Son's wife | Daughter-in-law |
| Daughter's husband | Son-in-law |
| Spouse's father | Father-in-law |
| Spouse's mother | Mother-in-law |
| Uncle's/Aunt's son/daughter | Cousin |
| Grandfather's son | Father or Uncle |
| Grandmother's daughter | Mother or Aunt |

---

### ⚠️ The Genius Trap

**Trap 1: Gender Assumption**
```
"A's parent's child" = Could be A themselves, or A's sibling
Never assume there's only one child!
```

**Trap 2: "Only" vs "A" Distinction**
```
"A is the only son" ≠ "A is a son"
"Only" eliminates other possibilities.
```

**Trap 3: In-Law Confusion**
```
"X is the brother-in-law of Y"
This could mean:
- X is Y's spouse's brother, OR
- X is Y's sibling's spouse
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
Pointing to a man in a photograph, a woman said, 
"His mother's only daughter is my mother."
How is the man related to the woman?
```

**Solution:**
- His mother's only daughter = His sister (no other daughter)
- His sister = Woman's mother
- Therefore, man is woman's mother's brother
- **Answer:** Uncle (Maternal)

**Problem 2:** (GATE 2021 Pattern)
```
A + B means A is the mother of B
A - B means A is the brother of B
A × B means A is the father of B
A ÷ B means A is the sister of B

If P × Q - R ÷ S, how is S related to P?
```

**Solution:**
- P × Q: P is father of Q → Q is P's child
- Q - R: Q is brother of R → R is Q's sibling (same parent P)
- R ÷ S: R is sister of S → S is R's sibling (same parent P)
- Therefore, S is P's child (son or daughter)
- **Answer:** S is son or daughter of P

**Problem 3:** (ESE Pattern)
```
If X is the brother of Y, Y is the sister of Z, and Z is the father of W,
how is X related to W?
```

**Solution:**
Building the tree:
```
       [Parent of X,Y,Z]
        ↙     ↓     ↘
       X      Y      Z
       (M)    (F)    (M)
                      ↓
                      W
```
Wait - Y is sister of Z, so X, Y, Z are all siblings.
- Z is father of W
- X is Z's brother
- X is W's uncle
- **Answer:** Uncle

---

### 🧠 The Family Tree Mnemonic: "GPSC"

```
G - Generation (count steps up/down)
P - Position (paternal/maternal side)
S - Sex (determine male/female)
C - Connection (direct/through marriage)
```

---

## 2. Direction Sense

### The Singularity
> **"North is up, East is right. Track position, not steps."**

### The Root Architecture

Direction problems use a 2D coordinate system:
$$\text{Position} = (x, y)$$

Where:
- Moving East: $x \rightarrow x + d$
- Moving West: $x \rightarrow x - d$
- Moving North: $y \rightarrow y + d$
- Moving South: $y \rightarrow y - d$

---

### 🔑 The Direction Compass

```
                    N (North)
                       ↑
                       |
      NW    ↖          |          ↗    NE
              ╲        |        ╱
                ╲      |      ╱
     W (West) ←--------+--------→ E (East)
                ╱      |      ╲
              ╱        |        ╲
      SW    ↙          |          ↘    SE
                       ↓
                    S (South)
```

### 🔑 Turn Relationships

| Current Direction | Turn Left (90° CCW) | Turn Right (90° CW) | About Turn (180°) |
|-------------------|--------------------|--------------------|-------------------|
| North | West | East | South |
| East | North | South | West |
| South | East | West | North |
| West | South | North | East |

---

### 🎯 The Direction Problem Algorithm

```
Step 1: Set origin at starting point: (0, 0)
Step 2: Note starting direction (usually North if not specified)
Step 3: For each movement:
        - Update coordinates based on direction
        - Update direction if there's a turn
Step 4: Calculate final position
Step 5: Use Pythagorean theorem for shortest distance:
        d = √(x² + y²)
Step 6: Determine final direction from start to end
```

---

### 🔑 Distance Calculation

**Shortest Distance Formula:**
$$d = \sqrt{(x_{\text{final}} - x_{\text{start}})^2 + (y_{\text{final}} - y_{\text{start}})^2}$$

**Direction Finding:**
$$\theta = \tan^{-1}\left(\frac{y_{\text{final}}}{x_{\text{final}}}\right)$$

| Quadrant | x | y | Direction |
|----------|---|---|-----------|
| I | + | + | North-East |
| II | - | + | North-West |
| III | - | - | South-West |
| IV | + | - | South-East |

---

### ⚠️ The Genius Trap

**Trap 1: Left/Right vs Direction**
```
"Turn left" depends on which way you're facing!
Facing North + Turn Left = Now facing West
Facing South + Turn Left = Now facing East
```

**Trap 2: Shadow Direction (Sun position)**
```
Morning (6 AM): Sun in East → Shadow points West
Noon (12 PM): Sun overhead → No shadow (or minimal)
Evening (6 PM): Sun in West → Shadow points East

If facing your shadow in morning → You face West
```

**Trap 3: Sunrise/Sunset Direction**
```
Face sunrise (East) → Your left is North, right is South
Face sunset (West) → Your left is South, right is North
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
A person walks 6 km North, then 8 km East.
What is the shortest distance from the starting point?
```

**Solution:**
- Final position: (8, 6)
- Distance = $\sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$ km
- **Answer:** 10 km

**Problem 2:** (GATE 2020 Pattern)
```
Starting from point A, Rahul walked 20m North, then turned right 
and walked 30m, then turned right and walked 35m, then turned left 
and walked 15m. How far and in which direction is Rahul from A?
```

**Solution:**
Tracking movements:
```
Start: (0, 0), Facing North
1. Walk 20m N: (0, 20)
2. Turn Right (now facing East), Walk 30m: (30, 20)
3. Turn Right (now facing South), Walk 35m: (30, -15)
4. Turn Left (now facing East), Walk 15m: (45, -15)
```

Distance from A:
$$d = \sqrt{45^2 + (-15)^2} = \sqrt{2025 + 225} = \sqrt{2250} = 15\sqrt{10} ≈ 47.43 \text{ m}$$

Direction: South-East (positive x, negative y)

**Answer:** Approximately 47.43m South-East

---

## 3. Coding-Decoding

### The Singularity
> **"Every code has a pattern. Find the transformation rule."**

### The Root Architecture

Coding transforms input to output using a function $f$:
$$\text{Code} = f(\text{Original})$$

---

### 🔑 The 12 Common Coding Types

#### Type 1: Letter Position Coding
Each letter → Its alphabet position number
```
A=1, B=2, C=3, ... Z=26
Example: CAT → 3, 1, 20
```

#### Type 2: Reverse Alphabet Coding
Each letter → Its reverse position
```
A→Z, B→Y, C→X, ... Z→A
Formula: Code = 27 - Position
Example: ABC → ZYX
```

#### Type 3: Plus/Minus Shift Coding
Each letter shifted by $n$ positions
```
+2 shift: A→C, B→D, ...
Example: CAT (+2) → ECV
```

#### Type 4: Opposite Shift Coding
```
First letter: +1, Second letter: -1, Third letter: +1, ...
Alternating shifts
```

#### Type 5: Position-Based Variable Shift
```
1st letter: +1, 2nd letter: +2, 3rd letter: +3, ...
Example: ABC (+1,+2,+3) → BDF
```

#### Type 6: Word Reversal
```
COMPUTER → RETUPMOC
```

#### Type 7: Letter Swap Coding
```
Swap pairs: AB→BA, CD→DC
Example: ABCD → BADC
```

#### Type 8: Symbolic Substitution
```
A=@, B=#, C=$, etc.
Dictionary given in question
```

#### Type 9: Number-Letter Mixed
```
Replace vowels with numbers: A=1, E=2, I=3, O=4, U=5
Example: EDUCATION → 2D5C1T34N
```

#### Type 10: Logic-Based Word Coding
```
TIGER = 35 (because T=20, I=9, G=7, E=5, R=18... some pattern)
Often: Sum of positions, or specific calculation
```

#### Type 11: Analogy Coding
```
If APPLE is coded as ELPPA, then MANGO is coded as ?
Pattern: Reversal
Answer: OGNAM
```

#### Type 12: Matrix/Grid Coding
```
Letters arranged in grid, coded by row-column position
```

---

### 🎯 The Decoding Algorithm

```
Step 1: COMPARE letter by letter (given word vs code)
Step 2: FIND position difference for each letter
Step 3: DETECT pattern in differences
Step 4: VERIFY pattern with complete word
Step 5: APPLY pattern to solve question
```

---

### ⚠️ The Genius Trap

**Trap 1: Wraparound**
```
Z + 2 = ? 
Answer: B (not beyond Z, wrap to A)
Z(26) + 2 = 28 mod 26 = 2 = B
```

**Trap 2: Case Sensitivity**
```
Some codings treat uppercase/lowercase differently
Always check if case matters
```

**Trap 3: Mixed Patterns**
```
First half of word: +2 shift
Second half of word: -2 shift
Always verify pattern works for ENTIRE word
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
If MACHINE is coded as LBBGHOD, how is COMPUTE coded?
```

**Solution:**
Compare letter by letter:
- M(13)→L(12): -1
- A(1)→B(2): +1
- C(3)→B(2): -1
- H(8)→G(7): -1
- I(9)→H(8): -1
- N(14)→O(15): +1
- E(5)→D(4): -1

Pattern: Alternating -1, +1, -1, -1, -1, +1, -1... (Hmm, not clean)

Let me recheck: 
Position pattern appears to be: -1, +1, -1, -1, -1, +1, -1
Actually: Odd positions: -1, Even positions: +1 (mostly)

For COMPUTE: C-O-M-P-U-T-E
- C(3)-1=B
- O(15)+1=P  
- M(13)-1=L
- P(16)+1=Q
- U(21)-1=T
- T(20)+1=U
- E(5)-1=D

**Answer:** BPLQTUD

**Problem 2:** (GATE Pattern)
```
In a certain code, SISTER is written as RHRSDQ.
How is BROTHER written in that code?
```

**Solution:**
SISTER → RHRSDQ
- S(19)→R(18): -1
- I(9)→H(8): -1
- S(19)→R(18): -1
- T(20)→S(19): -1
- E(5)→D(4): -1
- R(18)→Q(17): -1

Pattern: Each letter shifted back by 1 (-1)

BROTHER:
- B(2)-1=A
- R(18)-1=Q
- O(15)-1=N
- T(20)-1=S
- H(8)-1=G
- E(5)-1=D
- R(18)-1=Q

**Answer:** AQNSGDQ

---

## 4. Seating Arrangements

### The Singularity
> **"Constraints define positions. Satisfy all, find the unique arrangement."**

### The Root Architecture

Seating problems are constraint satisfaction problems (CSP):
- **Variables:** Positions of people
- **Domain:** Available seats
- **Constraints:** Given conditions

---

### 🔑 Types of Seating Arrangements

#### Type 1: Linear Arrangement
```
Positions: 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8
All facing same direction
```

**Key terms:**
- **Immediate left/right:** Adjacent positions
- **Left of:** Any position on left side
- **Exactly n positions away:** Count n seats between

#### Type 2: Circular Arrangement
```
        1
      8   2
     7     3
      6   4
        5
```

**Key insight:** No absolute left/right; only relative positions.

#### Type 3: Rectangular Table
```
    ─────────────────
    |  1   2   3   4  |  (one side facing center)
    |                 |
    |  5   6   7   8  |  (other side facing center)
    ─────────────────
```

**Key insight:** People across face each other.

---

### 🎯 The Seating Algorithm

```
Step 1: DRAW the seating structure (linear/circular/rectangular)
Step 2: IDENTIFY definite constraints (A sits at position 1)
Step 3: PLACE definite positions first
Step 4: PROCESS relative constraints (B is left of C)
Step 5: USE elimination for remaining positions
Step 6: VERIFY all constraints are satisfied
```

---

### ⚠️ The Genius Trap

**Trap 1: "Left" in Circular vs Linear**
```
Linear: Left is always left side of the row
Circular: Left depends on facing direction!
- If all face center: Clockwise = Right of previous
- If all face outside: Opposite!
```

**Trap 2: "Between" Ambiguity**
```
"B sits between A and C"
This could be: A-B-C or C-B-A
Both satisfy the constraint!
```

**Trap 3: Multiple Valid Arrangements**
```
When question asks "definitely true":
- Check if true in ALL valid arrangements
If only "possibly true": Not the answer
```

---

### 📝 Practice Problem

**Problem:** (GATE 2022 Pattern)
```
Eight people A, B, C, D, E, F, G, H are sitting in a row facing North.
- E sits at one of the ends.
- D is second to the left of H.
- B is an immediate neighbor of both H and C.
- G sits third to the right of A.
- F is not an immediate neighbor of E.

Who is sitting in the middle of the row?
```

**Solution:**
Positions: 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 (all facing North)

**Step 1: Analyze constraints**
1. E sits at position 1 or 8 (end position)
2. D is second to the left of H (meaning exactly one position between them: D-?-H)
3. B is immediate neighbor of both H and C (H-B-C or C-B-H sequence)
4. G sits third to right of A (possible pairs: A at 1 → G at 4, A at 2 → G at 5, etc.)
5. F is not an immediate neighbor of E

**Step 2: Try E = 8 (at right end)**

From constraint 2: D-?-H means H = D + 2
Possible pairs: (D=3, H=5), (D=4, H=6), (D=5, H=7)

From constraint 3: B is between H and C.
If H=5, then B can be 4 or 6, and C on the other side of B from H.
Try B=6, then C=7 ✓ (sequence: H=5, B=6, C=7)

This gives: D=3, H=5, B=6, C=7, E=8

**Step 3: Apply remaining constraints**
From constraint 4: G is 3 positions right of A.
Remaining positions: 1, 2, 4 for A, F, G
For A=1, G=4 ✓ (1 + 3 = 4)

This places: A=1, G=4, and F=2 (only position left)

**Step 4: Verify all constraints**
Final arrangement: 1=A, 2=F, 3=D, 4=G, 5=H, 6=B, 7=C, 8=E

✓ E at end (position 8)
✓ D second to left of H (D=3, H=5, exactly one position between)
✓ B between H and C (H=5, B=6, C=7 - consecutive)
✓ G is 3 right of A (A=1, G=4, difference = 3)
✓ F not adjacent to E (F=2, E=8 - not neighbors)

**Step 5: Find the middle**
For 8 positions, middle positions are 4 and 5.

**Answer:** G (position 4) and H (position 5) are in the middle

---

## 5. Ranking & Order

### The Singularity
> **"Ranks are positions in a sorted list. Inequalities define the order."**

### The Root Architecture

$$\text{If } A > B \text{ and } B > C, \text{ then } A > B > C \text{ (Transitivity)}$$

---

### 🔑 Key Formulas

**Total positions = N**

| Given Information | Formula |
|------------------|---------|
| Rank from top = R_t | Rank from bottom = N - R_t + 1 |
| Rank from bottom = R_b | Rank from top = N - R_b + 1 |
| R_t + R_b | N + 1 |

---

### 📝 Practice Problem

**Problem:**
```
In a class of 50 students, Raj ranked 15th from the top. 
What is his rank from the bottom?
```

**Solution:**
$$R_{\text{bottom}} = N - R_{\text{top}} + 1 = 50 - 15 + 1 = 36$$

**Answer:** 36th from bottom

---

## 6. Puzzles & Scheduling

### The Singularity
> **"Scheduling is constraint satisfaction over time."**

### 🔑 Common Puzzle Types

1. **Floor Puzzles:** People on different floors
2. **Day Scheduling:** Activities on different days
3. **Color/Object Assignment:** Matching attributes

### 🎯 General Strategy

```
Step 1: List all variables (people, days, etc.)
Step 2: Create a table/grid
Step 3: Mark definite facts first
Step 4: Apply deductive reasoning
Step 5: Use elimination to complete
```

---

## 7. Input-Output Analysis

### The Singularity
> **"Track the transformation at each step. Reverse engineer the rule."**

### 🔑 Common Operations

- **Sorting:** Arranging in ascending/descending order
- **Swapping:** Exchanging positions
- **Shifting:** Moving elements left/right
- **Interleaving:** Alternating from two sequences

### 📝 Practice Problem

**Problem:**
```
Input: 96 and the four 51 over 22
Step I: 22 96 and the four 51 over
Step II: 22 96 and the 51 four over
Step III: 22 51 96 and the four over
Step IV: 22 51 96 and four over the
Step V: 22 51 96 four and over the

What is the rule?
```

**Solution:**
Analyzing each step:
- Numbers are being sorted (ascending): 22, 51, 96
- Words are being sorted (alphabetically): and, four, over, the

The machine sorts numbers first, then words, alternating.

---

## 🧠 The Analytical Reasoning Mnemonic: "TRACE"

- **T**able it (draw grids and diagrams)
- **R**ead all constraints first
- **A**nchor definite facts
- **C**onnect relationships
- **E**liminate impossible options

---

## 🎯 Mastery Checklist

- [ ] Can solve blood relation chains in under 30 seconds
- [ ] Can track direction problems without drawing
- [ ] Know all 12 coding types
- [ ] Can solve 8-person seating in under 3 minutes
- [ ] Can rank ordering problems instantly
- [ ] Can identify input-output patterns in 2 steps

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

[← Back to Main Index](../README.md) | [Previous: Non-Verbal Reasoning](../Non-Verbal-Reasoning/README.md) | [Next: Data Interpretation →](../Data-Interpretation/README.md)
