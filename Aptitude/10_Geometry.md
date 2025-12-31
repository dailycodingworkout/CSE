# Chapter 10: Geometry

> **The mathematics of shapes - visual reasoning meets logical deduction**

---

## 🎯 Why Study This?

- Tests spatial reasoning and visualization
- Foundation for mensuration and coordinate geometry
- GATE/ESE includes geometry in aptitude section

---

## 📚 Part 1: Lines & Angles

### Basic Angle Relationships

| Type | Measure | Visual |
|------|---------|--------|
| Acute | 0° < θ < 90° | Sharp |
| Right | θ = 90° | L-shape |
| Obtuse | 90° < θ < 180° | Wide |
| Straight | θ = 180° | Line |
| Reflex | 180° < θ < 360° | Beyond straight |

---

### Angle Pairs

**Complementary**: Sum = 90°
**Supplementary**: Sum = 180°
**Linear Pair**: Adjacent angles on a straight line (supplementary)
**Vertically Opposite**: Equal angles formed by intersecting lines

---

### Parallel Lines & Transversal

When a transversal cuts parallel lines:
```
Corresponding angles: Equal
Alternate interior angles: Equal
Alternate exterior angles: Equal
Co-interior (same-side interior): Supplementary (sum = 180°)
```

**💡 Mnemonic**: "F-angles" (corresponding), "Z-angles" (alternate), "C-angles" (co-interior)

---

## 📚 Part 2: Triangles

### Classification

**By Sides**:
| Type | Property |
|------|----------|
| Equilateral | All sides equal, all angles = 60° |
| Isosceles | Two sides equal, two angles equal |
| Scalene | All sides different |

**By Angles**:
| Type | Property |
|------|----------|
| Acute | All angles < 90° |
| Right | One angle = 90° |
| Obtuse | One angle > 90° |

---

### Fundamental Properties

**Angle Sum Property**:
```
Sum of angles = 180°
∠A + ∠B + ∠C = 180°
```

**Exterior Angle Theorem**:
```
Exterior angle = Sum of non-adjacent interior angles
```

**Triangle Inequality**:
```
Sum of any two sides > Third side
|a - b| < c < a + b
```

---

### Special Lines in Triangles

| Line | Definition | Property |
|------|------------|----------|
| Median | Vertex to midpoint of opposite side | Divides triangle into equal areas |
| Altitude | Perpendicular from vertex to opposite side | Height for area calculation |
| Angle Bisector | Divides angle into two equal parts | Bisector theorem applies |
| Perpendicular Bisector | ⊥ to side through midpoint | Equidistant from endpoints |

**Concurrency Points**:
| Lines | Point | Property |
|-------|-------|----------|
| Medians | Centroid (G) | Divides medians 2:1 from vertex |
| Altitudes | Orthocenter (H) | - |
| Angle Bisectors | Incenter (I) | Center of inscribed circle |
| ⊥ Bisectors | Circumcenter (O) | Center of circumscribed circle |

---

### Important Triangle Theorems

**Basic Proportionality (BPT) / Thales Theorem**:
If DE ∥ BC in △ABC, then:
```
AD/DB = AE/EC
```

**Mid-Point Theorem**:
Line joining midpoints of two sides is parallel to third side and half its length.

**Angle Bisector Theorem**:
```
BD/DC = AB/AC
```

---

### Pythagoras Theorem (Right Triangle)

```
Hypotenuse² = Base² + Perpendicular²
c² = a² + b²
```

**Pythagorean Triplets** (Memorize!):
```
(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)
(6, 8, 10), (9, 12, 15), (12, 16, 20) — multiples of 3-4-5
```

**Converse**: If c² = a² + b², then angle opposite to c is 90°.

---

### Similarity & Congruence

**Congruence (≅)**: Same shape AND size
- Tests: SSS, SAS, ASA, AAS, RHS

**Similarity (~)**: Same shape, proportional sizes
- Tests: AAA, AA, SSS (ratio), SAS (ratio)

**For similar triangles**:
```
Ratio of sides = k
Ratio of perimeters = k
Ratio of areas = k²
Ratio of volumes = k³
```

---

### Area Formulas for Triangles

```
Area = (1/2) × base × height
     = (1/2) × a × b × sin(C)
     = √[s(s-a)(s-b)(s-c)]    (Heron's formula)
     
where s = (a+b+c)/2 (semi-perimeter)
```

**Special Cases**:
```
Equilateral: (√3/4) × side²
Right: (1/2) × leg₁ × leg₂
```

---

## 📚 Part 3: Quadrilaterals

### Types and Properties

| Shape | Properties |
|-------|------------|
| **Parallelogram** | Opposite sides equal & parallel, opposite angles equal, diagonals bisect each other |
| **Rectangle** | Parallelogram + all angles 90°, diagonals equal |
| **Rhombus** | Parallelogram + all sides equal, diagonals bisect at 90° |
| **Square** | Rectangle + Rhombus (all properties) |
| **Trapezium** | One pair of parallel sides |
| **Kite** | Two pairs of adjacent sides equal, diagonals perpendicular |

---

### Angle Sum

```
Sum of interior angles of quadrilateral = 360°
```

---

### Diagonal Properties

**Parallelogram**: Diagonals bisect each other
**Rectangle**: Diagonals equal and bisect each other
**Rhombus**: Diagonals bisect at right angles
**Square**: All of the above

---

## 📚 Part 4: Circles

### Basic Terminology

```
Radius (r): Center to any point on circle
Diameter (d): d = 2r
Chord: Line segment with both endpoints on circle
Arc: Part of circumference
Sector: Pie-slice (two radii + arc)
Segment: Chord cuts off a region
```

---

### Angle Properties

**Central Angle**: Angle at center = Arc/Radius = θ (in radians)

**Inscribed Angle**: Angle formed by two chords meeting on circle
```
Inscribed angle = (1/2) × Central angle (for same arc)
```

**Angle in Semicircle**: 90° (always)

**Angles in Same Segment**: Equal

**Cyclic Quadrilateral**: Opposite angles sum to 180°

---

### Chord Properties

**Equal chords**: Equidistant from center
**Perpendicular from center**: Bisects chord

**Intersecting Chords Theorem**:
If chords AB and CD intersect at P:
```
PA × PB = PC × PD
```

---

### Tangent Properties

**Tangent**: Line touching circle at exactly one point

- Tangent ⊥ Radius at point of contact
- Two tangents from external point are equal
- Angle between tangent and chord = Inscribed angle in alternate segment

**Power of a Point**:
```
Tangent² = PA × PB (for secant through same point)
```

---

### Important Circle Theorems

**Tangent-Secant**:
```
PT² = PA × PB
Where PT = tangent, PA, PB = secant segments
```

**Two Secants**:
```
PA × PB = PC × PD
```

---

## 📚 Part 5: Polygons

### Regular Polygons

| n | Name | Interior Angle | Sum of Angles |
|---|------|---------------|---------------|
| 3 | Triangle | 60° | 180° |
| 4 | Square | 90° | 360° |
| 5 | Pentagon | 108° | 540° |
| 6 | Hexagon | 120° | 720° |
| 8 | Octagon | 135° | 1080° |

**Formulas**:
```
Sum of interior angles = (n-2) × 180°
Each interior angle (regular) = (n-2) × 180° / n
Each exterior angle (regular) = 360° / n
Number of diagonals = n(n-3)/2
```

---

## 💡 Advanced Tricks

### Trick 1: Finding Unknown Angles

Look for:
- Parallel lines (alternate, corresponding)
- Isosceles triangles (equal angles)
- Circle properties (inscribed angles)
- Angle sum (triangle = 180°, quadrilateral = 360°)

---

### Trick 2: Similar Triangle Shortcuts

```
If triangles are similar:
Ratio of altitudes = Ratio of corresponding sides
Ratio of areas = (Ratio of sides)²
```

---

### Trick 3: 30-60-90 and 45-45-90 Triangles

**45-45-90**: Sides in ratio 1:1:√2
**30-60-90**: Sides in ratio 1:√3:2

---

### Trick 4: Stewart's Theorem

For cevian AD in triangle ABC with D on BC:
```
b²m + c²n - amn = a × AD²
where BD = m, DC = n
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Angle at Center vs Inscribed
```
Central angle = 2 × Inscribed angle (for same arc)
Don't confuse which is which
```

### Trap 2: Exterior Angle Direction
```
Exterior angle of polygon = 360°/n (for regular polygon)
Not (n-2)×180°/n
```

### Trap 3: Similarity vs Congruence
```
Similar doesn't mean equal sides
Proportional sides with equal angles = Similar
```

### Trap 4: Degenerate Triangles
```
If a + b = c, the triangle collapses to a line
Strict inequality required: a + b > c
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Triangle angle sum | 180° |
| Quadrilateral angle sum | 360° |
| Polygon angle sum | (n-2) × 180° |
| Exterior angle | Sum of non-adjacent interior |
| Pythagoras | c² = a² + b² |
| Heron's area | √[s(s-a)(s-b)(s-c)] |
| Similar triangles area ratio | k² |
| Inscribed angle | (1/2) × central angle |
| Tangent from external point | Equal lengths |
| Diagonals of n-gon | n(n-3)/2 |

---

## 📝 GATE-Level Practice

**Q1**: In △ABC, ∠A = 50°, ∠B = 60°. Find exterior angle at C.
```
∠C = 180° - 50° - 60° = 70°
Exterior angle at C = 180° - 70° = 110°
OR = 50° + 60° = 110° (exterior angle theorem)
```

**Q2**: Sides of a triangle are 5, 12, 13. Is it a right triangle?
```
5² + 12² = 25 + 144 = 169 = 13²
Yes, it's a right triangle (90° opposite to side 13)
```

**Q3**: Two similar triangles have areas 16 and 25 cm². Ratio of perimeters?
```
Area ratio = k² = 16/25
k = 4/5
Perimeter ratio = 4:5
```

**Q4**: Find interior angle of a regular octagon.
```
= (8-2) × 180° / 8 = 1080°/8 = 135°
```

**Q5**: A chord 8 cm long is 3 cm from center. Find radius.
```
Half chord = 4 cm, distance = 3 cm
r² = 4² + 3² = 25
r = 5 cm
```

---

*← [Chapter 9 - Algebra](./09_Algebra.md) | [Chapter 11 - Mensuration →](./11_Mensuration.md)*
