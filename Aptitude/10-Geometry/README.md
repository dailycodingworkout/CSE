# 📐 Geometry | The Singularity

> **The Atomic Truth:** *Geometry is the study of shapes, sizes, and relative positions of figures.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Lines and Angles](#lines-and-angles)
3. [Triangles](#triangles)
4. [Quadrilaterals](#quadrilaterals)
5. [Circles](#circles)
6. [Coordinate Geometry](#coordinate-geometry)
7. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
8. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Geometry Matters?
Geometry in GATE/ESE tests:
- Spatial reasoning abilities
- Logical deduction skills
- Application of formulas
- Visualization capabilities

### Basic Definitions

| Term | Definition |
|------|------------|
| **Point** | Location with no dimension |
| **Line** | One-dimensional, extends infinitely |
| **Ray** | Half-line with one endpoint |
| **Line Segment** | Portion between two points |
| **Plane** | Two-dimensional flat surface |
| **Angle** | Measure of rotation between two rays |

---

## Lines and Angles

### Types of Angles

| Angle Type | Range |
|------------|-------|
| Acute | $0° < \theta < 90°$ |
| Right | $\theta = 90°$ |
| Obtuse | $90° < \theta < 180°$ |
| Straight | $\theta = 180°$ |
| Reflex | $180° < \theta < 360°$ |

### Angle Relationships

| Relationship | Property |
|--------------|----------|
| **Complementary** | Sum = 90° |
| **Supplementary** | Sum = 180° |
| **Vertically Opposite** | Equal |
| **Linear Pair** | Sum = 180° |

### Parallel Lines & Transversal

When a transversal crosses parallel lines:
- **Corresponding angles** = Equal
- **Alternate interior angles** = Equal
- **Alternate exterior angles** = Equal
- **Co-interior angles** = Sum to 180°

> **💡 The Golden Pivot:** F-shape (corresponding), Z-shape (alternate), C-shape (co-interior)

---

## Triangles

### Basic Properties

1. Sum of angles = 180°
2. Sum of any two sides > Third side
3. Exterior angle = Sum of non-adjacent interior angles

### Types by Sides

| Type | Property |
|------|----------|
| Equilateral | All sides equal, all angles = 60° |
| Isosceles | Two sides equal, two angles equal |
| Scalene | All sides different |

### Types by Angles

| Type | Property |
|------|----------|
| Acute | All angles < 90° |
| Right | One angle = 90° |
| Obtuse | One angle > 90° |

### Important Theorems

**Pythagoras Theorem (Right Triangle):**
$$c^2 = a^2 + b^2$$

**Converse:** If $c^2 = a^2 + b^2$, triangle is right-angled.

**Angle-Side Relationships:**
- Largest angle opposite to longest side
- Smallest angle opposite to shortest side

### Triangle Centers

| Center | Definition | Property |
|--------|------------|----------|
| **Centroid (G)** | Intersection of medians | Divides median in 2:1 |
| **Incenter (I)** | Intersection of angle bisectors | Center of inscribed circle |
| **Circumcenter (O)** | Intersection of perpendicular bisectors | Center of circumscribed circle |
| **Orthocenter (H)** | Intersection of altitudes | Inside for acute, outside for obtuse |

### Important Formulas

**Area of Triangle:**
$$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}$$

**Heron's Formula:**
$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$$
where $s = \frac{a+b+c}{2}$ (semi-perimeter)

**Area using coordinates:**
$$\text{Area} = \frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$$

### Special Triangles

**30-60-90 Triangle:**
- Sides in ratio $1 : \sqrt{3} : 2$

**45-45-90 Triangle:**
- Sides in ratio $1 : 1 : \sqrt{2}$

**Equilateral Triangle (side $a$):**
- Height = $\frac{\sqrt{3}}{2}a$
- Area = $\frac{\sqrt{3}}{4}a^2$

### Similarity Theorems

**AA (Angle-Angle):** Two pairs of corresponding angles equal

**SSS Similarity:** All three pairs of sides in same ratio

**SAS Similarity:** Two pairs of sides in same ratio, included angle equal

**Property of Similar Triangles:**
$$\frac{\text{Area}_1}{\text{Area}_2} = \left(\frac{\text{Side}_1}{\text{Side}_2}\right)^2$$

---

## Quadrilaterals

### Properties Summary

| Quadrilateral | Diagonals | Angles |
|---------------|-----------|--------|
| **Parallelogram** | Bisect each other | Opposite angles equal |
| **Rectangle** | Equal, bisect each other | All 90° |
| **Rhombus** | Perpendicular bisectors | Opposite angles equal |
| **Square** | Equal, perpendicular bisectors | All 90° |
| **Trapezium** | No special property | Sum = 360° |

### Area Formulas

| Shape | Area Formula |
|-------|--------------|
| Rectangle | $l \times b$ |
| Square | $a^2$ |
| Parallelogram | $b \times h$ |
| Rhombus | $\frac{1}{2} d_1 d_2$ |
| Trapezium | $\frac{1}{2}(a+b) \times h$ |

### Diagonal Properties

**Rectangle:** $d = \sqrt{l^2 + b^2}$

**Square:** $d = a\sqrt{2}$

**Rhombus:** $a^2 = \left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2$

---

## Circles

### Basic Elements

- **Radius (r):** Distance from center to circumference
- **Diameter (d):** Twice the radius ($d = 2r$)
- **Chord:** Line segment with endpoints on circle
- **Arc:** Portion of circumference
- **Sector:** Region bounded by two radii and arc
- **Segment:** Region bounded by chord and arc

### Important Theorems

1. **Angle at center = 2 × Angle at circumference** (for same arc)
2. **Angle in semicircle = 90°**
3. **Equal chords are equidistant from center**
4. **Perpendicular from center to chord bisects the chord**
5. **Angles in same segment are equal**

### Tangent Properties

1. Tangent ⊥ Radius at point of contact
2. From external point, two tangents are equal in length
3. **Tangent-Secant:** If tangent = $t$ and secant = $s$, passing through external point: $t^2 = s_1 \times s_2$

### Formulas

**Circumference:** $C = 2\pi r$

**Area of Circle:** $A = \pi r^2$

**Arc Length:** $l = \frac{\theta}{360°} \times 2\pi r$ (θ in degrees)

**Area of Sector:** $A = \frac{\theta}{360°} \times \pi r^2$

**Area of Segment:** $A = \frac{1}{2}r^2(\theta - \sin\theta)$ (θ in radians)

---

## Coordinate Geometry

### Distance Formula
$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$

### Section Formula

Point dividing $(x_1, y_1)$ and $(x_2, y_2)$ in ratio $m:n$:

**Internal Division:**
$$\left(\frac{mx_2 + nx_1}{m+n}, \frac{my_2 + ny_1}{m+n}\right)$$

**External Division:**
$$\left(\frac{mx_2 - nx_1}{m-n}, \frac{my_2 - ny_1}{m-n}\right)$$

### Midpoint Formula
$$\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$

### Slope of Line
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \tan\theta$$

### Equation of Line

**Slope-Intercept Form:** $y = mx + c$

**Point-Slope Form:** $y - y_1 = m(x - x_1)$

**Two-Point Form:** $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$

**Intercept Form:** $\frac{x}{a} + \frac{y}{b} = 1$

### Parallel & Perpendicular Lines

**Parallel:** $m_1 = m_2$

**Perpendicular:** $m_1 \times m_2 = -1$

### Distance from Point to Line

Distance from $(x_0, y_0)$ to line $ax + by + c = 0$:
$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$

---

## GATE & ESE Problem Patterns

### Pattern 1: Triangle Property Application
> In a triangle, angles are in ratio 1:2:3. Find all angles.
- Sum = 180°
- $x + 2x + 3x = 180° \implies 6x = 180° \implies x = 30°$
- Angles: **30°, 60°, 90°**

### Pattern 2: Similar Triangles
> Two similar triangles have areas 16 cm² and 25 cm². If a side of smaller triangle is 4 cm, find corresponding side of larger.
- $\frac{16}{25} = \left(\frac{4}{x}\right)^2$
- $\frac{4}{x} = \frac{4}{5}$
- $x = 5$ cm

### Pattern 3: Circle Theorems
> A chord 6 cm long is 4 cm from center. Find radius.
- Half-chord = 3 cm, distance = 4 cm
- $r = \sqrt{3^2 + 4^2} = 5$ cm

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"If the diagonals of a quadrilateral bisect each other, it is a..."

Wrong answer: Rectangle (jumping to conclusion)

**The Elegant Solution:**
- Diagonals bisecting each other → **Parallelogram**
- For rectangle: Need additional condition (diagonals equal)
- For rhombus: Need diagonals perpendicular
- For square: Need both

**MSQ Logic Gate:**
- Not all parallelograms are rectangles
- Properties are hierarchical (square ⊂ rhombus ⊂ parallelogram)

**NAT Precision Lock:**
- Use $\pi = 3.14$ or as specified
- Keep intermediate calculations precise

---

## Speed Tricks & Shortcuts

### Trick 1: Triangle Angle Sum
Third angle = 180° - (sum of other two)

### Trick 2: Pythagoras Triplets

Common triplets: (3,4,5), (5,12,13), (8,15,17), (7,24,25)
Multiples also work: (6,8,10), (9,12,15)

### Trick 3: Quick Area of Equilateral Triangle
$$A = \frac{\sqrt{3}}{4}a^2 \approx 0.433a^2$$

### Trick 4: Diagonal of Square
$$d = a\sqrt{2} \approx 1.414a$$

### Trick 5: Circumference-Area Relationship
If circumference is known: $A = \frac{C^2}{4\pi}$

---

## Permanent Recall

### The Bizarre Mnemonic (Triangle Centers)
*"**C**entroid: **C**enter of mass, divides medians 2:1
**I**ncenter: **I**nscribed circle lives here
**O**rthocenter: **O**utside for obtuse triangles
**C**ircumcenter: **C**ircumscribed circle's home"*

### The Mental Slider
Visualize triangles morphing:
- As one angle approaches 180°, area approaches 0
- As angles equalize, triangle becomes more regular
- Circumcenter moves outside for obtuse triangles

### The 5-Second Snap-Check
- Sum of triangle angles = 180° (always)
- Sum of quadrilateral angles = 360° (always)
- Diagonal of square > side (always)

---

## Practice Problems

### Level 1: Fundamentals
1. Find the area of a triangle with sides 5, 12, and 13 cm.
2. A circle has circumference 44 cm. Find its area. (Use π = 22/7)
3. Find the equation of line passing through (2, 3) with slope 4.

### Level 2: GATE Standard
4. In a rhombus, diagonals are 16 cm and 12 cm. Find the side and area.
5. Find the distance between parallel lines 3x + 4y = 5 and 3x + 4y = 15.
6. Two circles of radii 5 cm and 3 cm touch externally. Find distance between centers.

### Level 3: IIT Examiner Level
7. A triangle has vertices at (0,0), (4,0), and (0,3). Find the coordinates of its centroid and area.
8. In a circle of radius 10 cm, a chord subtends 60° at center. Find chord length and area of minor segment.
9. A point moves such that its distance from (3,0) is twice its distance from (0,0). Find the locus.

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Check: 5² + 12² = 25 + 144 = 169 = 13² → Right triangle
   Area = ½ × 5 × 12 = **30 cm²**

2. $C = 2\pi r = 44$
   $r = \frac{44 \times 7}{2 \times 22} = 7$ cm
   Area = $\pi r^2 = \frac{22}{7} \times 49 = **154 cm²**$

3. $y - 3 = 4(x - 2)$
   $y = 4x - 5$ or **$4x - y - 5 = 0$**

4. Half-diagonals: 8 cm and 6 cm
   Side = $\sqrt{8^2 + 6^2} = \sqrt{100} = **10 cm**$
   Area = $\frac{1}{2} × 16 × 12 = **96 cm²**$

5. Distance between parallel lines $ax + by = c_1$ and $ax + by = c_2$:
   $d = \frac{|c_2 - c_1|}{\sqrt{a^2 + b^2}} = \frac{|15-5|}{\sqrt{9+16}} = \frac{10}{5} = **2 units**$

6. External touch: Distance = $r_1 + r_2 = 5 + 3 = **8 cm**$

7. Centroid = $\left(\frac{0+4+0}{3}, \frac{0+0+3}{3}\right) = **\left(\frac{4}{3}, 1\right)$**
   Area = $\frac{1}{2}|0(0-3) + 4(3-0) + 0(0-0)| = \frac{1}{2} × 12 = **6 sq units**$

8. Chord length: In isoceles triangle with two radii and 60° angle:
   Using cosine rule: $c^2 = 10^2 + 10^2 - 2(10)(10)\cos 60°$
   $c^2 = 100 + 100 - 100 = 100$
   Chord = **10 cm** (equilateral triangle formed!)
   
   Area of sector = $\frac{60}{360} × \pi × 100 = \frac{50\pi}{3}$ cm²
   Area of triangle = $\frac{\sqrt{3}}{4} × 100 = 25\sqrt{3}$ cm²
   Area of segment = $\frac{50\pi}{3} - 25\sqrt{3} ≈ **9.06 cm²**$

9. Let point be $(x, y)$
   $\sqrt{(x-3)^2 + y^2} = 2\sqrt{x^2 + y^2}$
   $(x-3)^2 + y^2 = 4(x^2 + y^2)$
   $x^2 - 6x + 9 + y^2 = 4x^2 + 4y^2$
   $3x^2 + 3y^2 + 6x - 9 = 0$
   $x^2 + y^2 + 2x - 3 = 0$
   **$(x+1)^2 + y^2 = 4$** (Circle with center (-1,0), radius 2)

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Geometry with Mensuration for a Rank-1 simulation?
