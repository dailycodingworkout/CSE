# Manim Animation Scripts — Seating Arrangements

Detailed Manim (Community Edition) animation scripts for every chapter of the Seating Arrangements study material. Each script contains multiple scenes that visually explain every concept with animations, analogies, and step-by-step walkthroughs.

## Prerequisites

Install Manim Community Edition:

```bash
pip install manim
```

For system dependencies (LaTeX, ffmpeg, etc.), see: https://docs.manim.community/en/stable/installation.html

## Scripts

| Script | Chapter | Scenes | Key Visuals |
|--------|---------|--------|-------------|
| `scene_01_introduction.py` | Ch 1: Introduction & Fundamentals | 7 scenes | Classification tree, terminology demo, 5-step pipeline, perspective trap |
| `scene_02_linear.py` | Ch 2: Linear Arrangements | 6 scenes | Direction convention (N/S), position formulas, L+R=n+1 proof, swap trick |
| `scene_03_circular.py` | Ch 3: Circular Arrangements | 7 scenes | Rotation principle, CW/ACW animation, opposite formula, facing center vs outward |
| `scene_04_double_row.py` | Ch 4: Double-Row Arrangements | 5 scenes | Direction reversal trap, facing pairs, position formulas, solved example |
| `scene_05_complex.py` | Ch 5: Complex & Hybrid | 5 scenes | Rectangular table, floor puzzle, grid adjacency, hybrid strategy |
| `scene_06_advanced.py` | Ch 6: Advanced Techniques | 7 scenes | BFS cascade, two-case split, elimination matrix, block method, symmetry |
| `scene_07_practice.py` | Ch 7: Practice Problems | 4 scenes | GATE linear/circular walkthroughs, banking direction trap, formula reference |

## How to Render

### Render all scenes in a script (1080p, with preview):
```bash
manim -pqh scene_01_introduction.py
```

### Render a specific scene:
```bash
manim -pqh scene_01_introduction.py ClassificationTree
```

### Render at lower quality (faster, for testing):
```bash
manim -pql scene_01_introduction.py ClassificationTree
```

### Render all scripts at once:
```bash
for f in scene_*.py; do manim -qh "$f"; done
```

Output videos are saved to `media/videos/` by default.

## Scene Index

### Scene 01 — Introduction & Fundamentals
1. **WhatIsSeatingArrangement** — Jigsaw puzzle analogy, people-to-positions mapping
2. **ClassificationTree** — Animated tree: Linear / Circular / Complex with exam frequency
3. **CoreTerminology** — Visual dictionary: immediate left/right, between, ends, perspective trap
4. **FiveStepFramework** — Assembly-line pipeline animation of the solving method
5. **NotationSystem** — Shorthand notation legend with examples
6. **ConstraintDensityPrinciple** — Network graph showing most-connected person = place first
7. **PerspectiveTrap** — Side-by-side wrong vs right interpretation of "left of"

### Scene 02 — Linear Arrangements
1. **LinearBasics** — Row construction, endpoints vs middle seats
2. **DirectionConvention** — North vs South facing, paper-direction reversal
3. **PositionMathematics** — Formula derivation with visual proof
4. **LinearSolvedExample** — 6-person GATE-style problem, step-by-step animated solution
5. **LRIdentity** — Visual proof of L + R = n + 1 (ruler analogy)
6. **SwapTrick** — Parallel-cases animation
7. **LinearEdgeCases** — "left of" vs "immediately left", odd/even middle

### Scene 03 — Circular Arrangements
1. **CircularBasics** — Round table with no endpoints
2. **RotationPrinciple** — Why n! becomes (n-1)!, two rotations shown as identical
3. **ClockwiseAnticlockwise** — Clock-hand animation for CW/ACW with position formula
4. **OppositeFormula** — Diameter lines on circle, formula derivation, odd-n warning
5. **FacingCenterVsOutward** — Split-screen: direction arrows flip, physical hand-pointing proof
6. **CircularSolvedExample** — 6-person GATE problem, step-by-step placement
7. **LinearVsCircular** — Comparison table animation

### Scene 04 — Double-Row Arrangements
1. **DoubleRowBasics** — Two rows facing each other, facing pairs construction
2. **DirectionTrap** — The master trap: directions are OPPOSITE between rows
3. **DoubleRowFormulas** — Position math for both rows with derivation
4. **DoubleRowSolvedExample** — 4+4 problem with cross-row constraint chaining
5. **DoubleRowTraps** — Visual catalogue of common mistakes

### Scene 05 — Complex & Hybrid
1. **ComplexOverview** — Card-based taxonomy of complex types
2. **RectangularTable** — Table geometry, corner vs side seats, "opposite" ambiguity
3. **FloorPuzzle** — Vertical linear arrangement, ground-floor numbering trap
4. **GridSeating** — 3x3 grid with adjacency highlighting (corner/edge/center)
5. **HybridStrategy** — Divide-and-conquer pipeline animation

### Scene 06 — Advanced Techniques
1. **FixedPointCascade** — BFS animation on constraint graph (domino analogy)
2. **TwoCaseSplit** — Fork-in-the-road: parallel paths, contradiction elimination
3. **NegativeConstraint** — Sudoku-style elimination matrix with naked singles
4. **BlockMethod** — Sliding block animation with position counting formula
5. **CountingShortcuts** — All counting formulas in one animated list
6. **SymmetryShortcut** — Mirror arrangements: same answer regardless
7. **TimeManagement** — 3-minute rule timelines for Banking and GATE

### Scene 07 — Practice Problems
1. **GATELinearProblem** — Full 5-person linear walkthrough with answer
2. **GATECircularProblem** — Full 6-person circular walkthrough with answer
3. **BankingDoubleRowTrap** — Direction mistake demonstration (wrong vs correct)
4. **FormulaQuickReference** — All formulas animated as a cheat sheet
