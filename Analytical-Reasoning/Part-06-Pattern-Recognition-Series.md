# Part 6: Pattern Recognition & Series

## The Singularity

**The Atomic Truth:** *Patterns are rules waiting to be discovered.*

---

## 6.1 Understanding Pattern Recognition

### What is Pattern Recognition?

Pattern recognition involves:
1. **Identifying** recurring structures in data
2. **Extracting** the underlying rule
3. **Applying** the rule to predict next elements

### Types of Patterns in GATE/ESE

| Type | Description | Example |
|------|-------------|---------|
| Number Series | Sequence of numbers | 2, 4, 8, 16, ? |
| Letter Series | Sequence of letters | A, C, E, G, ? |
| Alphanumeric | Mix of letters and numbers | A1, B2, C4, D8, ? |
| Figure/Visual | Shapes and images | (Diagrams) |
| Mixed Patterns | Combination of types | 1A, 4B, 9C, ? |

---

## 6.2 Number Series

### 6.2.1 Basic Patterns

#### Arithmetic Progression (AP)
**Rule:** Add/subtract a constant difference.

$$a_n = a_1 + (n-1)d$$

**Examples:**
```
3, 7, 11, 15, ?
Difference: +4, +4, +4
Answer: 19
```

#### Geometric Progression (GP)
**Rule:** Multiply/divide by a constant ratio.

$$a_n = a_1 \times r^{(n-1)}$$

**Examples:**
```
2, 6, 18, 54, ?
Ratio: ×3, ×3, ×3
Answer: 162
```

#### Fibonacci-Type Series
**Rule:** Each term is sum of previous two.

$$a_n = a_{n-1} + a_{n-2}$$

**Examples:**
```
1, 1, 2, 3, 5, 8, ?
Pattern: 1+1=2, 1+2=3, 2+3=5, 3+5=8
Answer: 13
```

### 6.2.2 Difference Method

**When to Use:** When simple patterns don't apply.

**Method:**
1. Find first-level differences
2. If not constant, find second-level differences
3. Continue until pattern emerges

**Example:**
```
Series: 1, 4, 10, 20, 35, ?

Level 1 differences: 3, 6, 10, 15
Level 2 differences: 3, 4, 5
Level 3 differences: 1, 1  ← Constant!

Work backward:
Level 3: 1
Level 2: 5 + 1 = 6
Level 1: 15 + 6 = 21
Series: 35 + 21 = 56

Answer: 56
```

### 6.2.3 Power Series

**Patterns with Squares:**
```
1, 4, 9, 16, 25, ?
Pattern: 1², 2², 3², 4², 5²
Answer: 36 (6²)
```

**Patterns with Cubes:**
```
1, 8, 27, 64, ?
Pattern: 1³, 2³, 3³, 4³
Answer: 125 (5³)
```

**Modified Power Series:**
```
2, 5, 10, 17, 26, ?
Pattern: 1²+1, 2²+1, 3²+1, 4²+1, 5²+1
Answer: 37 (6²+1)
```

### 6.2.4 Alternating Series

**Two Interleaved Patterns:**
```
1, 10, 3, 12, 5, 14, ?
Pattern 1 (odd positions): 1, 3, 5, ? → 7
Pattern 2 (even positions): 10, 12, 14 → next is 16
Answer: 7 (odd position)
```

**Alternating Operations:**
```
2, 6, 4, 12, 10, ?
Operations: +4, -2, ×3, -2, ... 
Wait, let's re-examine:
2 (+4)→ 6 (-2)→ 4 (×3)→ 12 (-2)→ 10 (×3)→ 30
Answer: 30
```

### 6.2.5 Prime Number Based

**Prime Series:**
```
2, 3, 5, 7, 11, ?
Pattern: Consecutive primes
Answer: 13
```

**Prime-Derived Series:**
```
4, 9, 25, 49, ?
Pattern: 2², 3², 5², 7²
Answer: 121 (11²)
```

### 6.2.6 Factorial Based

**Factorial Series:**
```
1, 2, 6, 24, 120, ?
Pattern: 1!, 2!, 3!, 4!, 5!
Answer: 720 (6!)
```

---

## 6.3 Letter Series

### 6.3.1 Letter Position Basics

| Letter | Position | Letter | Position |
|--------|----------|--------|----------|
| A | 1 | N | 14 |
| B | 2 | O | 15 |
| C | 3 | P | 16 |
| D | 4 | Q | 17 |
| E | 5 | R | 18 |
| F | 6 | S | 19 |
| G | 7 | T | 20 |
| H | 8 | U | 21 |
| I | 9 | V | 22 |
| J | 10 | W | 23 |
| K | 11 | X | 24 |
| L | 12 | Y | 25 |
| M | 13 | Z | 26 |

**Quick Reference:**
- A = 1, E = 5, I = 9, O = 15, U = 21 (vowels)
- J = 10, T = 20 (decades)
- M = 13, N = 14 (middle)
- Z = 26 (last)

### 6.3.2 Simple Letter Patterns

**Skip Pattern:**
```
A, C, E, G, ?
Skip: +2, +2, +2
Answer: I (positions: 1, 3, 5, 7, 9)
```

**Reverse Pattern:**
```
Z, X, V, T, ?
Skip: -2, -2, -2
Answer: R (positions: 26, 24, 22, 20, 18)
```

### 6.3.3 Increasing Skip

```
A, B, D, G, K, ?
Differences: +1, +2, +3, +4, +5
Position: 1, 2, 4, 7, 11, 16
Answer: P (position 16)
```

### 6.3.4 Letter Groups

```
AB, DE, GH, ?, MN
Pattern: Groups skip by 2
Answer: JK
```

---

## 6.4 Alphanumeric Series

### 6.4.1 Position-Based

**Letter = Position Number:**
```
A1, B2, C3, D4, ?
Answer: E5
```

**Letter Position Squared:**
```
A1, B4, C9, D16, ?
Pattern: A=1, 1²=1; B=2, 2²=4; etc.
Answer: E25
```

### 6.4.2 Interleaved Patterns

```
A2, C4, E8, G16, ?
Letters: A, C, E, G, I (+2 skip)
Numbers: 2, 4, 8, 16, 32 (×2)
Answer: I32
```

### 6.4.3 Complex Combinations

```
1A, 3C, 6F, 10J, ?
Numbers: 1, 3, 6, 10, 15 (triangular: +2, +3, +4, +5)
Letters: A=1, C=3, F=6, J=10, O=15
Answer: 15O
```

---

## 6.5 Figure/Visual Patterns

### 6.5.1 Rotation Patterns

**Clockwise Rotation:**
```
Position 1: ↑
Position 2: →
Position 3: ↓
Position 4: ←
Pattern: 90° clockwise rotation
```

**Variable Rotation:**
```
Position 1: ↑ (0°)
Position 2: ↗ (45°)
Position 3: → (90°)
Position 4: ↘ (135°)
Pattern: 45° clockwise each step
```

### 6.5.2 Addition/Removal of Elements

**Progressive Addition:**
```
Frame 1: ○
Frame 2: ○○
Frame 3: ○○○
Frame 4: ?
Answer: ○○○○
```

**Cyclic Pattern:**
```
Frame 1: ○□△
Frame 2: □△○
Frame 3: △○□
Frame 4: ?
Answer: ○□△ (returns to Frame 1)
```

### 6.5.3 Mirror/Reflection Patterns

**Horizontal Mirror:**
```
Original: ◢     Mirrored: ◣
```

**Vertical Mirror:**
```
Original: ◢     Mirrored: ◥
```

**Point Reflection (180°):**
```
Original: ◢     Rotated: ◤
```

### 6.5.4 Shading Patterns

**Progressive Shading:**
```
Frame 1: □□□□ (0 filled)
Frame 2: ■□□□ (1 filled)
Frame 3: ■■□□ (2 filled)
Frame 4: ?
Answer: ■■■□ (3 filled)
```

### 6.5.5 Counting Elements

**Pattern Recognition:**
```
Frame 1: 3 sides (triangle)
Frame 2: 4 sides (square)
Frame 3: 5 sides (pentagon)
Frame 4: ?
Answer: 6 sides (hexagon)
```

---

## 6.6 Matrix Patterns

### 6.6.1 Row-Based Rules

**Each Row Follows Same Rule:**
```
┌───┬───┬───┐
│ 2 │ 4 │ 6 │  Rule: +2 each cell
├───┼───┼───┤
│ 3 │ 6 │ 9 │  Rule: +3 each cell
├───┼───┼───┤
│ 5 │ 10│ ? │  Rule: +5 each cell
└───┴───┴───┘
Answer: 15
```

### 6.6.2 Column-Based Rules

**Each Column Follows Same Rule:**
```
┌───┬───┬───┐
│ 2 │ 3 │ 5 │
├───┼───┼───┤
│ 4 │ 6 │ 10│  ×2 of row above
├───┼───┼───┤
│ 8 │ 12│ ? │  ×2 of row above
└───┴───┴───┘
Answer: 20
```

### 6.6.3 Diagonal Patterns

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 2 │ 4 │ 6 │
├───┼───┼───┤
│ 3 │ 6 │ ? │
└───┴───┴───┘
Pattern: (row × column)
Answer: 9
```

### 6.6.4 Cross Relationships

```
┌───┬───┬───┐
│ 5 │ 2 │ 7 │  5 + 2 = 7
├───┼───┼───┤
│ 8 │ 3 │ 11│  8 + 3 = 11
├───┼───┼───┤
│ 4 │ 6 │ ? │  4 + 6 = ?
└───┴───┴───┘
Answer: 10
```

---

## 6.7 Coding-Decoding

### 6.7.1 Letter Shifting

**Forward Shift (+n):**
```
CAT coded as DBU (shift +1)
C → D, A → B, T → U
```

**Backward Shift (-n):**
```
CAT coded as BZS (shift -1)
C → B, A → Z, T → S
```

### 6.7.2 Position-Based Coding

**Variable Shift:**
```
GATE coded as HCWI
G(+1)→H, A(+2)→C, T(+3)→W, E(+4)→I
Pattern: Each letter shifted by its position
```

### 6.7.3 Reversal Coding

```
COMPUTER coded as RETUPMOC
Simple reversal
```

### 6.7.4 Number-Letter Substitution

```
A=1, B=2, ... Z=26
GATE = 7-1-20-5
```

### 6.7.5 Complex Coding

```
If PAINT is coded as TNIPA and TRAIN is coded as NIART
Rule: Reverse the word
Then BRAIN = ?
Answer: NIARB
```

---

## 6.8 Odd One Out

### 6.8.1 Number-Based

**Find the odd one:**
```
2, 3, 5, 7, 9, 11
Answer: 9 (not prime)
All others are prime numbers
```

### 6.8.2 Letter-Based

**Find the odd one:**
```
A, E, I, O, U, Y
Answer: Y (not always a vowel in English)
```

### 6.8.3 Pattern-Based

**Find the odd one:**
```
4, 9, 25, 49, 64, 121
Pattern: Perfect squares of primes
4=2², 9=3², 25=5², 49=7², 121=11²
Odd: 64=8² (8 is not prime)
```

---

## 6.9 Missing Number in Pattern

### 6.9.1 Grid-Based

**Magic Square Concept:**
```
┌───┬───┬───┐
│ 2 │ 7 │ 6 │
├───┼───┼───┤
│ 9 │ 5 │ 1 │
├───┼───┼───┤
│ 4 │ 3 │ ? │
└───┴───┴───┘
Each row/column/diagonal sums to 15
Row 3: 4 + 3 + ? = 15 → ? = 8
```

### 6.9.2 Circle Patterns

```
        8
       ╱ ╲
      4   2
       ╲ ╱
        ?
        
Pattern: Opposite pairs multiply to same value
8 × ? = 4 × 2 × 2 = 16
? = 16/8 = 2

Or: 8 × ? = constant
```

### 6.9.3 Triangle Patterns

```
      3
     ╱ ╲
    4   5
   ╱─────╲
  ?       2

Pattern: Base = (Left × Right) / Top
? = (4 × 5) / 3 × 2? 
Need more context; check relationship.
```

---

## 6.10 Advanced: Multi-Level Patterns

### 6.10.1 Nested Patterns

```
1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ?
Pattern: Number repeated that many times
1 appears 1 time
2 appears 2 times
3 appears 3 times
4 appears 4 times
Next: 5 (appears 5 times)
Answer: 5
```

### 6.10.2 Operation Alternation

```
2, 3, 6, 18, 108, ?
Operations: ×1.5, ×2, ×3, ×6, ×?
Pattern of multipliers: 1.5, 2, 3, 6 (×2 pattern: 1.5×2=3... no)
Actually: 2(+1)→3(×2)→6(×3)→18(×6)→108(×?)
Pattern in multipliers: +1, ×2, ×3... ?
108 × 12 = 1296 (if ×12, following ×6×2)
```

### 6.10.3 Prime-Composite Alternation

```
2, 4, 3, 9, 5, 25, 7, ?
Odd positions: 2, 3, 5, 7 (primes)
Even positions: 4, 9, 25, ? (squares of primes)
Next even position: 7² = 49
Answer: 49
```

---

## 6.11 GATE-Specific Patterns

### Pattern 1: Combination Series

**Format:** Numbers that follow multiple rules simultaneously.

**Example:**
```
1, 1, 2, 6, 24, 120, ?
Pattern: Factorials: 1!, 1!, 2!, 3!, 4!, 5!, 6!
Answer: 720
```

### Pattern 2: Hidden Operations

**Format:** Operations are not immediately obvious.

**Example:**
```
3, 5, 9, 17, 33, ?
Differences: 2, 4, 8, 16, 32
Pattern: Differences are powers of 2
Next difference: 32
Answer: 65
```

### Pattern 3: Two-Track Series

**Format:** Alternate terms follow different rules.

**Example:**
```
1, 2, 2, 4, 3, 8, 4, ?
Track 1 (positions 1,3,5,7): 1, 2, 3, 4 (arithmetic +1)
Track 2 (positions 2,4,6,8): 2, 4, 8, 16 (geometric ×2)
Answer: 16
```

---

## 6.12 Speed Techniques

### Technique 1: First-Second-Third Difference

Always try:
1. Direct pattern
2. First differences
3. Second differences

Most GATE series resolve by level 2.

### Technique 2: Ratio Check

Calculate ratios between consecutive terms:
```
2, 6, 18, 54
Ratios: 3, 3, 3 → GP with r=3
```

### Technique 3: Prime Awareness

Keep prime numbers in mind:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...

### Technique 4: Power Awareness

Keep powers handy:
- Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100...
- Cubes: 1, 8, 27, 64, 125, 216, 343, 512...

### Technique 5: Factorial Awareness

1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040

### Technique 6: Letter Position Arithmetic

Quickly convert: A=1, J=10, T=20, Z=26
For any letter: Position = (Letter - A) + 1

---

## 6.13 Practice Problems

### Problem 1: Number Series
**Series:** 3, 6, 11, 18, 27, ?

**Solution:**
```
Differences: 3, 5, 7, 9, ?
Second differences: 2, 2, 2
Next first difference: 11
Answer: 27 + 11 = 38
```

### Problem 2: Letter Series
**Series:** B, E, I, N, ?

**Solution:**
```
Positions: 2, 5, 9, 14, ?
Differences: 3, 4, 5, 6
Next position: 14 + 6 = 20
Answer: T (position 20)
```

### Problem 3: Alphanumeric
**Series:** A2, C6, E12, G20, ?

**Solution:**
```
Letters: A, C, E, G, I (skip 1)
Numbers: 2, 6, 12, 20, ?
Differences: 4, 6, 8, 10
Answer: I30
```

### Problem 4: Matrix
```
┌───┬───┬───┐
│ 5 │ 7 │ 12│
├───┼───┼───┤
│ 8 │ 11│ 19│
├───┼───┼───┤
│ 6 │ 13│ ? │
└───┴───┴───┘
```

**Solution:**
```
Pattern: Column 1 + Column 2 = Column 3
Row 1: 5 + 7 = 12 ✓
Row 2: 8 + 11 = 19 ✓
Row 3: 6 + 13 = 19
Answer: 19
```

### Problem 5: Missing Number
```
  2   3   5
 ─┼───┼───┼─
  8   27  ?
```

**Solution:**
```
Pattern: Top^3 = Bottom
2³ = 8 ✓
3³ = 27 ✓
5³ = 125
Answer: 125
```

### Problem 6: Coding
**If GARDEN is coded as ICTHGQ, then FLOWER is coded as?**

**Solution:**
```
G → I (+2)
A → C (+2)
R → T (+2)
D → H (+4)
E → G (+2)
N → Q (+3)

Pattern not consistent... let's try:
Position: 1(+2), 2(+2), 3(+2), 4(+4), 5(+2), 6(+3)

For FLOWER:
F(+2)→H, L(+2)→N, O(+2)→Q, W(+4)→A, E(+2)→G, R(+3)→U
Answer: HNQAGU

Or if different pattern, re-examine...
```

---

## 6.14 Key Takeaways

### The 5-Second Snap-Check

Before finalizing:
1. ✓ Did I verify the pattern with ALL given terms?
2. ✓ Did I check for alternative patterns?
3. ✓ Does my answer fit the pattern type (number, letter, etc.)?
4. ✓ Did I handle the sequence correctly (not off-by-one)?

### Memory Anchors

**For Number Series:**
> "Difference first, ratio second, powers third."

**For Letter Series:**
> "Position is everything—convert and compute."

**For Visual Patterns:**
> "Rotate, reflect, repeat—the three Rs."

### The Mental Slider

**Imagine a pattern decoder:**
- Input: Given sequence
- Slider 1: Difference (AP pattern)
- Slider 2: Ratio (GP pattern)
- Slider 3: Power/Prime (Special pattern)
- Output: Next term

---

## Navigation

[◀ Previous: Critical Reasoning](Part-05-Critical-Reasoning.md) | [Contents](README.md) | [Next: Advanced Problem-Solving ▶](Part-07-Advanced-Problem-Solving.md)
