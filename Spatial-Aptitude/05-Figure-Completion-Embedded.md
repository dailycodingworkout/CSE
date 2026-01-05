# Chapter 5: Figure Completion & Embedded Figures

## The Atomic Truth
> **Pattern recognition = Finding structure in visual chaos.**

---

## 5.1 Understanding Figure Completion

### What is Figure Completion?

Figure completion tests your ability to:
1. **Identify** the underlying pattern or rule
2. **Visualize** the missing part
3. **Select** the option that completes the figure logically

### Types of Figure Completion Problems

```
FIGURE COMPLETION
       │
       ├── MATRIX COMPLETION
       │     └── Complete a grid pattern
       │
       ├── SPLIT FIGURE COMPLETION
       │     └── Two halves must form a whole
       │
       ├── SEQUENCE COMPLETION
       │     └── Find the next in series
       │
       └── PATTERN COMPLETION
             └── Fill in missing section
```

---

## 5.2 Matrix Completion (3×3 Grids)

### 🎯 The Core Principle

> **Each row and column follows the SAME rule independently.**

### The Standard Matrix Structure

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │  ← Row 1 follows Rule R
├───┼───┼───┤
│ 4 │ 5 │ 6 │  ← Row 2 follows Rule R
├───┼───┼───┤
│ 7 │ 8 │ ? │  ← Row 3 follows Rule R
└───┴───┴───┘
  ↑   ↑   ↑
 Col  Col Col follows Rule C
  1    2   3
```

### Common Matrix Rules

| Rule Type | Description | Example |
|-----------|-------------|---------|
| **Union** | Cell 3 = Cell 1 + Cell 2 | △ + ○ = △○ |
| **Intersection** | Cell 3 = Common to Cell 1 & 2 | △○ ∩ ○□ = ○ |
| **Subtraction** | Cell 3 = Cell 1 - Cell 2 | △○ - ○ = △ |
| **Rotation** | Each cell rotates from previous | △ → ▷ → ▽ |
| **Counting** | Element count follows pattern | 1, 2, 3 elements |

### ⚡ Quick Trick: The "Row-Column Verification"

```
Step 1: Find rule for Row 1 (using cells 1, 2, 3)
Step 2: Verify rule works for Row 2
Step 3: Apply rule to Row 3 → Get answer
Step 4: VERIFY: Does answer work for Column 3?

If both row and column work → Confident answer
```

### 💡 Aha Moment: The Union Rule

Most common pattern in competitive exams:

```
Cell 1 + Cell 2 = Cell 3

Where "+" means:
- Combine all elements
- Remove duplicates (sometimes)
- Maintain positions (usually)

Example:
┌─────┐   ┌─────┐   ┌─────┐
│  △  │ + │  ○  │ = │ △ ○ │
│     │   │  □  │   │  □  │
└─────┘   └─────┘   └─────┘
```

### 🔴 Trap Alert: XOR vs OR

**OR (Union):** Element appears if in Cell 1 OR Cell 2
**XOR:** Element appears if in Cell 1 OR Cell 2, but NOT both

```
OR:  △○ + ○□ = △○□
XOR: △○ + ○□ = △□ (○ was in both, so removed)
```

**How to detect:** Look at completed rows—does doubling eliminate?

---

## 5.3 Split Figure Completion

### 🎯 The Core Principle

> **The two parts must form a complete, meaningful whole.**

### Types of Split Problems

```
TYPE 1: Two halves form complete figure
┌────┐   ┌────┐   ┌────────┐
│  ╱ │ + │ ╲  │ = │   ╱╲   │
│ ╱  │   │  ╲ │   │  ╱  ╲  │
└────┘   └────┘   └────────┘

TYPE 2: Pieces fit together (jigsaw style)
Irregular edges must match

TYPE 3: Overlapping completion
Parts overlay to form pattern
```

### The Matching Algorithm

```
Step 1: Analyze the given piece
        - Note edge patterns (straight, curved, notched)
        - Note internal elements

Step 2: For each option:
        - Check if edges mate properly
        - Verify complete figure makes sense

Step 3: Select the matching piece
```

### ⚡ Quick Trick: Edge Matching

```
Given Piece          Must Match With
───────────         ─────────────────
Convex edge    →    Concave edge (fitting into it)
Straight edge  →    Straight edge (aligned)
Pattern at edge →   Continuation of pattern
```

### 🔴 Trap Alert: Mirror vs Rotation

Sometimes options include:
- The correct piece
- Its mirror image
- Its rotation

**All three look similar but only ONE fits correctly.**

---

## 5.4 Embedded Figures

### 🎯 The Core Principle

> **Find the EXACT target figure hidden within the complex figure.**

### The Embedding Types

```
TYPE 1: Simple embedding
Target is directly visible but among distractors

TYPE 2: Rotated embedding
Target is rotated before embedding

TYPE 3: Scaled embedding
Target is enlarged or shrunk

TYPE 4: Multiple embeddings
Target appears more than once
```

### The Systematic Search Method

```
COMPLEX FIGURE SCANNING
         │
         ├── Step 1: ANCHOR
         │     └── Find unique feature of target
         │
         ├── Step 2: SCAN
         │     └── Look for anchor in complex figure
         │
         ├── Step 3: TRACE
         │     └── From anchor, trace target shape
         │
         └── Step 4: VERIFY
               └── Complete match confirmation
```

### 💡 Aha Moment: The Anchor Point Strategy

**Anchor = The most distinctive feature of the target figure**

```
Target: △ with a dot at apex

Complex Figure Search:
1. Find ALL dots in complex figure
2. For each dot, check if it's apex of a triangle
3. If yes, verify triangle matches target

Anchoring saves time by eliminating impossible positions
```

### ⚡ Quick Trick: Shape Signature

Create a mental "signature" of the target:

```
Target: Irregular quadrilateral

Signature:
- 4 vertices
- No parallel sides
- One acute angle (<90°)
- One obtuse angle (>90°)

Now scan for shapes matching ALL signature elements
```

### Common Embedded Figure Patterns

| Complex Figure Type | Search Strategy |
|---------------------|-----------------|
| Geometric grid | Focus on grid intersections |
| Overlapping shapes | Trace edges, ignore interior |
| Symmetric figures | Check all quadrants |
| Dense patterns | Systematic quadrant scan |

### 🔴 Trap Alert: Partial Matches

```
Target: Complete square ■

Trap: Finding a square that's part of larger figure
      
      ┌───┬───┐
      │ ■ │   │ ← This square is PART of rectangle
      └───┴───┘   Does it count?

Usually: Only count if target is EXACTLY embedded
         (not merged with other lines)
```

---

## 5.5 Pattern Completion

### 🎯 The Core Principle

> **Extend the pattern logically based on the visible structure.**

### Pattern Types

```
PATTERN TYPES
     │
     ├── LINEAR EXTENSION
     │     └── Pattern extends in one direction
     │
     ├── RADIAL EXTENSION
     │     └── Pattern radiates from center
     │
     ├── PERIODIC TILING
     │     └── Pattern repeats regularly
     │
     └── GROWTH PATTERNS
           └── Pattern evolves by rule
```

### Type 1: Linear Pattern Extension

```
Given:   ○ □ △ ○ □ △ ○ ?

Pattern: ○ □ △ repeating

Answer:  □
```

### Type 2: Radial Pattern

```
          ┌───┐
       ───│   │───
          │   │
       ───│   │───
          └───┘

Pattern radiates from center
Complete by extending radial symmetry
```

### Type 3: Tiling Pattern

```
┌──┬──┬──┐
│╱╲│╱╲│╱╲│
├──┼──┼──┤
│╲╱│╲╱│ ?│  ← What completes the tile?
└──┴──┴──┘

Pattern: Alternating triangle orientations
Answer: ╲╱
```

### ⚡ Quick Trick: The Rule Extraction Method

```
Step 1: Find the repeating unit
Step 2: Identify the transformation between units
Step 3: Apply transformation to get next unit
```

---

## 5.6 Counting Embedded Figures

### 🎯 The Core Principle

> **Systematically count ALL instances of a shape.**

### Counting Triangles in Complex Figures

```
Triangle Counting Protocol:
1. Identify ALL vertices (intersection points)
2. For each combination of 3 vertices:
   - Check if they form a triangle
   - Verify edges exist connecting them
3. Count avoiding duplicates
```

### The Size-Based Counting Method

```
For triangles:
Step 1: Count size-1 triangles (smallest unit)
Step 2: Count size-2 triangles (2 small triangles)
Step 3: Count size-3 triangles (3 small triangles)
...
Step n: Count the largest triangle

Total = Sum of all sizes
```

### Example: Counting in a Divided Triangle

```
    ╱╲
   ╱──╲
  ╱╲  ╱╲
 ╱──╲╱──╲
╱────────╲

Size 1 (smallest): 4 up-pointing + 1 down-pointing = 5
Size 2: 3 triangles
Size 3: Not applicable (skips)
Size 4 (full): 1 triangle

Total: 5 + 3 + 1 = 9 triangles
```

### Counting Rectangles/Squares

**For a grid of m×n lines:**

```
Rectangles = C(m,2) × C(n,2) = [m(m-1)/2] × [n(n-1)/2]

Where m = horizontal lines, n = vertical lines
```

### 💡 Aha Moment: The Selection Formula

```
Number of rectangles = (Ways to choose 2 horizontal lines)
                     × (Ways to choose 2 vertical lines)

Because:
- 2 horizontal lines define top and bottom
- 2 vertical lines define left and right
- Together they define exactly one rectangle
```

---

## 5.7 The Mental Machinery for This Chapter

### Machine 1: The Pattern Extractor

```
INPUT: Visual pattern
PROCESS:
  1. Identify elements
  2. Find relationships
  3. Extract rule
OUTPUT: Predictive rule
```

### Machine 2: The Figure Scanner

```
INPUT: Target + Complex figure
PROCESS:
  1. Create target signature
  2. Scan for anchor points
  3. Trace and verify
OUTPUT: Location(s) of embedded figure
```

### Machine 3: The Completion Predictor

```
INPUT: Partial figure + Rule
PROCESS:
  1. Apply rule to visible parts
  2. Extend to missing section
  3. Generate completion
OUTPUT: Missing piece
```

---

## 5.8 Exam-Specific Strategies

### GATE Figure Completion

**Common types:**
- Matrix completion (3×3)
- Pattern series

**Approach:**
1. Quick rule identification (30 sec)
2. Apply and verify (30 sec)
3. Total: 60 seconds

### ESE Figure Completion

**Focus areas:**
- Complex matrices (4×4)
- Embedded figures (more complex)
- Counting problems

**Time:** 45-60 seconds per question

### PSU Figure Completion

**Pattern:** Similar to GATE
**Tip:** Look for the most obvious rule first

### BANK Figure Completion

**Common in reasoning section:**
- Simple matrix completion
- Series completion
- Embedded figures (simpler)

**Time:** 30-45 seconds

---

## 5.9 Common Traps and Solutions

### 🔴 Trap 1: Multiple Valid Rules

**Problem:** More than one rule seems to fit
**Solution:** Apply ALL candidate rules to ALL rows/columns
           Only one will work consistently

### 🔴 Trap 2: Rotation Confusion

**Problem:** Target might be rotated in complex figure
**Solution:** Always check all 4 rotations (0°, 90°, 180°, 270°)

### 🔴 Trap 3: Counting Errors

**Problem:** Missing or double-counting shapes
**Solution:** Use systematic size-based counting

### 🔴 Trap 4: Partial Embeddings

**Problem:** Finding parts of the target but not complete
**Solution:** Trace COMPLETE target from anchor

---

## 5.10 Practice Framework

### 🧮 Skill Building Sequence

**Week 1: Matrix Mastery**
| Day | Focus | Questions |
|-----|-------|-----------|
| 1-2 | Simple matrices (OR rule) | 20 |
| 3-4 | Complex matrices (multi-rule) | 20 |
| 5-7 | Mixed with time pressure | 30 |

**Week 2: Embedded Figures**
| Day | Focus | Questions |
|-----|-------|-----------|
| 1-2 | Simple embeddings | 15 |
| 3-4 | Rotated embeddings | 15 |
| 5-7 | Complex figures | 20 |

**Week 3: Counting & Completion**
| Day | Focus | Questions |
|-----|-------|-----------|
| 1-2 | Triangle counting | 15 |
| 3-4 | Rectangle/square counting | 15 |
| 5-7 | Mixed completion problems | 25 |

### Error Categories

```
□ Rule identification error
□ Application error (wrong cell)
□ Rotation missed
□ Embedding not found
□ Counting error (under/over)
□ Time exceeded
```

---

## 5.11 Chapter Summary

### Mental Machines Built

1. **Pattern Extractor** - Find rules in matrices
2. **Figure Scanner** - Locate embedded figures
3. **Completion Predictor** - Fill missing sections

### Quick Reference

| Problem Type | Key Technique | Time Target |
|--------------|---------------|-------------|
| Matrix completion | Row-column verification | 45-60 sec |
| Split figures | Edge matching | 30-45 sec |
| Embedded figures | Anchor point scan | 45-60 sec |
| Pattern completion | Rule extraction | 45-60 sec |
| Counting | Size-based systematic | 60-90 sec |

### Key Formulas

**Rectangles in m×n grid:**
```
R = [m(m-1)/2] × [n(n-1)/2]
```

**Matrix rules to check first:**
1. Union (most common)
2. Rotation
3. XOR
4. Subtraction

### Before Moving On

✅ Can solve 3×3 matrices quickly
✅ Can find embedded figures systematically
✅ Know counting formulas for grids
✅ Can identify pattern rules

---

*Next: [Chapter 6 - Mental Rotation & Transformation →](./06-Mental-Rotation-Transformation.md)*
