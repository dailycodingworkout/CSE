# 🎨 Chapter 3: Non-Verbal Reasoning

## The Atomic Truth
> **"Patterns in shapes obey the same logic as patterns in numbers."**

---

## 📋 Topics Covered

1. [Pattern Recognition & Completion](#1-pattern-recognition--completion)
2. [Figure Series](#2-figure-series)
3. [Figure Matrices](#3-figure-matrices)
4. [Mirror & Water Images](#4-mirror--water-images)
5. [Paper Folding & Cutting](#5-paper-folding--cutting)
6. [Embedded Figures](#6-embedded-figures)
7. [Figure Formation & Analysis](#7-figure-formation--analysis)
8. [Counting Figures](#8-counting-figures)
9. [Dice & Cube Problems](#9-dice--cube-problems)

---

## 1. Pattern Recognition & Completion

### The Singularity
> **"Every visual pattern has a generator rule. Find the rule, complete the pattern."**

### The Root Architecture

Visual patterns follow transformations that can be described mathematically:

$$\text{Figure}_{n+1} = T(\text{Figure}_n)$$

Where $T$ is a transformation function (rotation, reflection, scaling, addition, subtraction).

---

### 🔑 The 8 Fundamental Transformations

| # | Transformation | Description | Symbol |
|---|---------------|-------------|--------|
| 1 | **Rotation** | Turning by fixed angle | ↻ 90°, ↻ 180° |
| 2 | **Reflection** | Mirror along axis | ⟷ or ⟵ |
| 3 | **Translation** | Moving position | → ↓ ← ↑ |
| 4 | **Scaling** | Size change | ⊕ bigger, ⊖ smaller |
| 5 | **Addition** | Adding elements | + |
| 6 | **Subtraction** | Removing elements | - |
| 7 | **Substitution** | Replacing elements | ⇄ |
| 8 | **Color/Shading Change** | Fill pattern change | ■ → □ → ▤ |

---

### 🎯 The Pattern Analysis Algorithm

```
Step 1: COUNT - How many elements in each figure?
Step 2: POSITION - Where are elements located?
Step 3: ORIENTATION - What direction do elements face?
Step 4: SIZE - Are elements growing/shrinking?
Step 5: SHADING - Is fill pattern changing?
Step 6: MOVEMENT - Are elements shifting position?
Step 7: RULE - What operation connects consecutive figures?
```

---

### 📝 Pattern Types with Examples

#### Type 1: Rotation Patterns

**Example:**
```
Figure 1    Figure 2    Figure 3    Figure 4
   △          ▷           ▽          ◁
```
**Rule:** Clockwise rotation by 90° each step

**Mathematical Expression:**
$$\theta_{n+1} = \theta_n + 90° \mod 360°$$

#### Type 2: Addition Patterns

**Example:**
```
Figure 1    Figure 2    Figure 3    Figure 4
   ●          ●●         ●●●        ●●●●
```
**Rule:** Add one element each step

#### Type 3: Alternating Patterns

**Example:**
```
Figure 1    Figure 2    Figure 3    Figure 4
   ■           □           ■          □
```
**Rule:** Alternate between filled and empty

#### Type 4: Combined Transformation

**Example:**
```
Figure 1    Figure 2    Figure 3    Figure 4
   △●         ▷●●        ▽●●●       ◁●●●●
```
**Rule:** Rotate triangle 90° clockwise AND add one circle

---

### ⚠️ The Genius Trap

**Trap 1: Missing the Second Pattern**
```
Figures show: Triangle rotating AND circle count increasing
Many students see only ONE pattern and miss the other.
Always check for COMPOUND transformations.
```

**Trap 2: Confusing Clockwise vs Counter-Clockwise**
```
90° CW ≠ 270° CCW visually, but mathematically equivalent.
GATE often tests if you can track direction consistently.
```

---

## 2. Figure Series

### The Singularity
> **"A series is a sequence with a hidden generator function."**

### 🔑 Common Figure Series Rules

#### Rule 1: Element Count Progression
$$n_{\text{elements}} = f(\text{position})$$

**Examples:**
- Linear: 1, 2, 3, 4, 5...
- Squares: 1, 4, 9, 16, 25...
- Fibonacci: 1, 1, 2, 3, 5, 8...

#### Rule 2: Rotation Sequence
$$\text{Angle} = \text{Initial} + (n-1) \times \Delta\theta$$

**Common Rotations:**
- 45° per step
- 90° per step
- 180° per step

#### Rule 3: Shading Cycle
```
Empty → Quarter filled → Half filled → Three-quarter → Full → Repeat
  □    →      ◔       →      ◑      →       ◕      →   ●  → □
```

#### Rule 4: Position Shift
```
Clockwise corner movement:
Top-Left → Top-Right → Bottom-Right → Bottom-Left → Repeat
```

---

### 📝 Practice Problem

**Problem:** Find the next figure in the series:
```
┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐
│ ●○│  │ ○●│  │○● │  │●○ │  │ ? │
└───┘  └───┘  └───┘  └───┘  └───┘
```

**Solution:**
- Pattern: Two dots rotating around the square
- Step 1→2: Dots swap positions (left-right)
- Step 2→3: Dots move left
- Step 3→4: Dots swap again
- Step 4→5: Dots should move left again

**Answer:** Dots at left edge, with ○ on top of ●

---

## 3. Figure Matrices

### The Singularity
> **"Matrices have row rules, column rules, or both. Find the governing dimension."**

### The Root Architecture

In a 3×3 matrix, the missing cell (usually bottom-right) follows rules that may operate:
- **Row-wise:** Same transformation across each row
- **Column-wise:** Same transformation down each column
- **Diagonal-wise:** Corner-to-corner pattern

$$\text{Cell}(3,3) = f(\text{Row}_3) \cap g(\text{Column}_3)$$

---

### 🔑 Matrix Analysis Strategy

```
Step 1: Analyze Row 1 (left to right)
        What changes? What stays same?
        
Step 2: Verify same rule in Row 2
        
Step 3: Apply rule to Row 3 to find answer
        
Step 4: Cross-verify with column analysis
```

---

### 📝 Common Matrix Rules

| Rule Type | Description | Example |
|-----------|-------------|---------|
| Union | Row 3 = Row 1 ∪ Row 2 | All elements from both |
| Intersection | Row 3 = Row 1 ∩ Row 2 | Common elements only |
| XOR | Row 3 = (Row 1 ∪ Row 2) - (Row 1 ∩ Row 2) | Unique elements only |
| Rotation | Each cell rotated from previous | 90° turn |
| Negation | Opposite shading/orientation | Black ↔ White |

---

### 📝 Practice Problem

**Problem:**
```
Matrix:
┌─────┬─────┬─────┐
│ △○  │ ○□  │ △□  │
├─────┼─────┼─────┤
│ ●■  │ ■◆  │ ●◆  │
├─────┼─────┼─────┤
│ ★◇  │ ◇♦  │  ?  │
└─────┴─────┴─────┘
```

**Solution:**
- Analyze Row 1: △○ + ○□ = △□ (XOR operation - keep unique elements)
- Verify Row 2: ●■ + ■◆ = ●◆ (XOR confirmed)
- Apply to Row 3: ★◇ + ◇♦ = ★♦

**Answer:** ★♦

---

## 4. Mirror & Water Images

### The Singularity
> **"Mirror reflects horizontally; water reflects vertically."**

### The Root Architecture

#### Mirror Image (Lateral Inversion)
Reflection across vertical axis (y-axis):
$$\text{Mirror}(x, y) = (-x, y)$$

```
Original    Mirror (→|)
  ABC         CBA
  ◄─►         ►─◄
```

#### Water Image (Vertical Inversion)
Reflection across horizontal axis (x-axis):
$$\text{Water}(x, y) = (x, -y)$$

```
Original    Water (─|─)
  △              ▽
  A              ∀
```

---

### 🔑 Quick Reference: Letter/Number Mirror Images

#### Letters that remain same in mirror:
**A, H, I, M, O, T, U, V, W, X, Y**

#### Numbers that remain same in mirror:
**0, 1, 8**

#### Common Mirror Transformations:
| Original | Mirror |
|----------|--------|
| b | d |
| p | q |
| E | Ǝ |
| R | Я |
| 2 | S-like |
| 3 | Ɛ |
| 5 | 2-like |

---

### 🎯 The Mirror/Water Decision Tree

```
Question asks for MIRROR image?
├── Is mirror on RIGHT? → Flip left-right (standard)
├── Is mirror on LEFT? → Same as right (image appears on left)
├── Is mirror on TOP? → This is WATER image
└── Is mirror on BOTTOM? → This is WATER image

Key: MIRROR = Left-Right swap
     WATER = Up-Down swap
```

---

### ⚠️ The Genius Trap

**Trap 1: Clock Mirror Images**
```
Original time: 3:00
Mirror image shows: 9:00

Formula: Mirror time = 12:00 - Original time
Exception: 12:00 and 6:00 remain same
```

**Trap 2: Combined Reflection**
```
If asked for the mirror image of a water image, this equals a 180° rotation.
Mathematical notation: Mirror ∘ Water = Rotation(180°)
Example: Applying water reflection then mirror reflection produces the same result as rotating 180°.
```

---

### 📝 Practice Problems

**Problem 1:**
```
Find the mirror image of: EXAMINATION
```

**Solution:**
- Reverse the string: NOITANIMAXE
- Flip each letter horizontally
- **Answer:** ИOITAИIMAХE (with proper mirror flips)

**Problem 2:**
```
A clock shows 4:45. What will be the mirror image time?
```

**Solution:**
- Mirror time = 11:60 - 4:45 = 12:00 - 4:45 + 11:60
- Simplified: Mirror = 11:60 - Original = 7:15
- **Answer:** 7:15

---

## 5. Paper Folding & Cutting

### The Singularity
> **"Each fold doubles the cuts; unfold mentally layer by layer."**

### The Root Architecture

When paper is folded $n$ times and cut:
- Number of layers = $2^n$
- Each cut creates $2^n$ holes when unfolded

$$\text{Total holes} = \text{Cuts} \times 2^{\text{folds}}$$

---

### 🔑 The Fold Analysis Method

```
Step 1: Track each fold (note axis: horizontal/vertical)
Step 2: Mark where holes are punched on final folded paper
Step 3: Unfold in REVERSE order
Step 4: For each unfold, reflect holes across the fold line
Step 5: Combine all reflected holes
```

---

### 📝 Key Fold Types

#### Single Horizontal Fold (Top to Bottom)
```
Before Fold:    Folded:       Unfolded with hole:
┌─────┐        ┌─────┐        ┌─────┐
│     │   →    │     │   →    │  ○  │
│     │        │─────│        │─────│
│     │        (bottom layer)  │  ○  │
└─────┘        └─────┘        └─────┘
```
Hole in folded paper → Two holes symmetrical about center line

#### Single Vertical Fold (Left to Right)
```
Before Fold:    Folded:       Unfolded with hole:
┌─────┐        ┌───┐          ┌─────┐
│     │   →    │   │    →     │○   ○│
│     │        │   │          │     │
└─────┘        └───┘          └─────┘
```

#### Diagonal Fold
```
Hole placement reflects across the diagonal fold line.
```

---

### 📝 Practice Problem

**Problem:**
```
A square paper is folded twice:
1. First fold: Left edge to right edge (vertical fold)
2. Second fold: Top edge to bottom edge (horizontal fold)
A single hole is punched at the center of the folded paper.
How many holes appear when unfolded?
```

**Solution:**
- After 2 folds: 4 layers
- 1 punch creates 4 holes
- Position: 4 holes at quadrant centers (symmetrical)
- **Answer:** 4 holes in a 2×2 pattern

---

## 6. Embedded Figures

### The Singularity
> **"Find the shape hiding inside the complex figure."**

### 🔑 The Search Strategy

```
Step 1: Identify the target figure to find
Step 2: Look for its KEY FEATURES (angles, line ratios)
Step 3: Trace the outline mentally
Step 4: Ignore distractor lines
Step 5: Verify all parts of target are present
```

---

### 📝 Common Tricks

| Trick | Description |
|-------|-------------|
| Rotation | Target figure may be rotated |
| Size Change | Target may be scaled up/down |
| Hidden Lines | Target uses only some lines of complex figure |
| Shared Edges | Target shares edges with other shapes |

---

## 7. Figure Formation & Analysis

### The Singularity
> **"Some pieces fit together; others never will."**

### 🔑 Figure Formation Rules

#### Can pieces form the target?
1. **Area Conservation:** Sum of piece areas = Target area
2. **Edge Compatibility:** Edges must align without gaps/overlaps
3. **Angle Matching:** Corners must sum to correct angles

$$\sum \text{Area}_{\text{pieces}} = \text{Area}_{\text{target}}$$

---

### 📝 Practice Problem

**Problem:**
```
Which of the following pieces can form a square?

Pieces: Two right triangles with legs 1 and 2 units
```

**Solution:**
- Each triangle area = $\frac{1}{2} \times 1 \times 2 = 1$ sq unit
- Two triangles = 2 sq units
- For square: $s^2 = 2$, so $s = \sqrt{2}$
- Triangles can form a square with side $\sqrt{2}$ ✅

---

## 8. Counting Figures

### The Singularity
> **"Systematic counting = No double counting + No missing."**

### The Root Architecture

For counting geometric figures:

$$\text{Total} = \sum_{\text{size}=1}^{n} \text{Count}_{\text{size}}$$

---

### 🔑 Counting Formulas

#### Counting Triangles in a Triangle

For a triangle divided by lines parallel to sides:
$$\text{Total triangles} = \frac{n(n+2)(2n+1)}{8}$$

Where $n$ = number of divisions on each side.

**Quick counts:**
| Divisions | Small △ | Medium △ | Large △ | Total |
|-----------|---------|----------|---------|-------|
| 1 | 1 | 0 | 0 | 1 |
| 2 | 4 | 3 | 1 | 9 |
| 3 | 9 | 6 | 3 | 18 |
| 4 | 16 | 10 | 6 | 27 |

#### Counting Squares in a Rectangle

For $m \times n$ grid (m ≤ n):
$$\text{Squares} = \sum_{i=1}^{m} (m-i+1)(n-i+1)$$

**Quick formula for $n \times n$ grid:**
$$\text{Squares} = \frac{n(n+1)(2n+1)}{6}$$

| Grid Size | Total Squares |
|-----------|---------------|
| 1×1 | 1 |
| 2×2 | 5 |
| 3×3 | 14 |
| 4×4 | 30 |
| 5×5 | 55 |

#### Counting Rectangles in a Rectangle

For $m \times n$ grid:
$$\text{Rectangles} = \binom{m+1}{2} \times \binom{n+1}{2} = \frac{m(m+1)n(n+1)}{4}$$

---

### 📝 Practice Problem

**Problem:**
```
How many squares are there in a 4×4 grid?
```

**Solution:**
- 1×1 squares: 16
- 2×2 squares: 9
- 3×3 squares: 4
- 4×4 squares: 1
- **Total:** 16 + 9 + 4 + 1 = **30**

---

## 9. Dice & Cube Problems

### The Singularity
> **"Opposite faces never meet at an edge or corner."**

### The Root Architecture

Standard dice properties:
- Opposite faces sum to 7
- 1 opposite to 6
- 2 opposite to 5
- 3 opposite to 4

---

### 🔑 The Adjacent vs Opposite Rule

```
Adjacent faces: Can be seen together at a corner (max 3 faces visible)
Opposite faces: Never visible simultaneously
```

#### Finding Opposite Faces

From two views of a cube:
```
View 1:     View 2:
┌─────┐    ┌─────┐
│  A  │    │  A  │
│B   C│    │D   E│
└─────┘    └─────┘

Analysis:
- Face A is common (same orientation)
- B, C are adjacent to A
- D, E are adjacent to A
- B & D or B & E might be opposite (depending on rotation)
```

---

### 🔑 The Net Analysis Method

When cube is unfolded into a net:
```
    ┌───┐
    │ 1 │
┌───┼───┼───┬───┐
│ 2 │ 3 │ 4 │ 5 │
└───┼───┼───┴───┘
    │ 6 │
    └───┘

Opposites: 1-6, 2-5, 3-4 (for standard cross net)
```

**Rule:** In a cross-shaped net, the center face is opposite to the face that's two positions away in any direction.

---

### 📝 Practice Problem

**Problem:**
```
A cube has symbols on its faces: ●, ○, △, ▽, □, ■

Three views are given:
View 1: Top=●, Front=△, Right=○
View 2: Top=●, Front=□, Right=△
View 3: Top=○, Front=▽, Right=□

What is opposite to ●?
```

**Solution:**
- From View 1 & 2: ● (top) is adjacent to △, ○, □
- From View 3: ○ is top, ▽ and □ are adjacent
- Since ●, ○ can both be on top, they are NOT opposite
- ● is adjacent to △, ○, □ 
- Remaining faces: ▽, ■
- From View 3, ▽ is adjacent to ○, so ▽ is not opposite to ●
- **Answer:** ■ is opposite to ●

---

## 🧠 The Visual Reasoning Mnemonic: "CROPS"

- **C**ount elements systematically
- **R**otation direction (CW/CCW)
- **O**rientation changes
- **P**osition shifts
- **S**hading/fill pattern changes

---

## 📊 Quick Reference: Transformation Symbols

| Symbol | Meaning |
|--------|---------|
| ↻ | Clockwise rotation |
| ↺ | Counter-clockwise rotation |
| ⟷ | Horizontal reflection (mirror) |
| ⇵ | Vertical reflection (water) |
| → | Translation right |
| ⊕ | Size increase |
| ⊖ | Size decrease |
| ■→□ | Shading change |

---

## 🎯 Mastery Checklist

- [ ] Can identify rotation angles instantly
- [ ] Can track multiple simultaneous transformations
- [ ] Can find mirror/water images without drawing
- [ ] Can unfold paper folding problems mentally
- [ ] Can count figures systematically
- [ ] Can solve cube problems using elimination
- [ ] Can complete 3×3 matrices in under 1 minute

---

## ⏱️ The 5-Second Snap-Check

| Check | What to Verify |
|-------|---------------|
| ✅ Element Count | Same number before/after transformation? |
| ✅ Orientation | Rotation angle consistent with series? |
| ✅ Symmetry | Expected reflection type matches? |
| ✅ Position | Movement pattern verified? |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

[← Back to Main Index](../README.md) | [Previous: Logical Reasoning](../Logical-Reasoning/README.md) | [Next: Analytical Reasoning →](../Analytical-Reasoning/README.md)
