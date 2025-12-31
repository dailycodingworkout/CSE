# Chapter 11: Mensuration

> **Measuring the unmeasurable - calculating areas and volumes of shapes**

---

## 🎯 Why Study This?

- Direct application of geometry concepts
- High frequency in GATE/ESE aptitude section
- Real-world: Engineering, architecture, estimation

---

## 📚 Part 1: 2D Shapes (Areas & Perimeters)

### Triangle

```
Area = (1/2) × base × height
     = (1/2) × a × b × sin(C)
     = √[s(s-a)(s-b)(s-c)]  (Heron's formula, s = semi-perimeter)
     
Perimeter = a + b + c
```

**Special Triangles**:
| Type | Area |
|------|------|
| Equilateral (side a) | (√3/4)a² |
| Right (legs a, b) | (1/2)ab |
| Isosceles (equal sides a, base b) | (b/4)√(4a² - b²) |

---

### Rectangle

```
Area = length × breadth = l × b
Perimeter = 2(l + b)
Diagonal = √(l² + b²)
```

---

### Square

```
Area = side² = a²
     = (diagonal²)/2 = d²/2
Perimeter = 4a
Diagonal = a√2
```

---

### Parallelogram

```
Area = base × height = b × h
     = ab × sin(θ)  (θ = included angle)
Perimeter = 2(a + b)
```

---

### Rhombus

```
Area = (1/2) × d₁ × d₂  (d₁, d₂ = diagonals)
     = side² × sin(θ)
Perimeter = 4 × side
Side = (1/2)√(d₁² + d₂²)
```

---

### Trapezium (Trapezoid)

```
Area = (1/2) × (sum of parallel sides) × height
     = (1/2) × (a + b) × h
```

---

### Circle

```
Area = πr²
Circumference = 2πr = πd
```

**Sector** (angle θ in degrees):
```
Area of sector = (θ/360) × πr²
Arc length = (θ/360) × 2πr = (θπr)/180
```

**Sector** (angle θ in radians):
```
Area = (1/2)r²θ
Arc length = rθ
```

**Segment** (region between chord and arc):
```
Area of segment = Area of sector - Area of triangle
                = (1/2)r²(θ - sin θ)  (θ in radians)
```

---

### Ring (Annulus)

```
Area = π(R² - r²) = π(R + r)(R - r)
Where R = outer radius, r = inner radius
```

---

### Regular Polygon (n sides, side length a)

```
Area = (1/4) × n × a² × cot(π/n)
     = (na²)/(4tan(π/n))
Perimeter = na
```

**Specific Regular Polygons**:
| Polygon | Area |
|---------|------|
| Pentagon | (a²/4)√(25 + 10√5) ≈ 1.72a² |
| Hexagon | (3√3/2)a² ≈ 2.598a² |
| Octagon | 2(1 + √2)a² ≈ 4.828a² |

---

## 📚 Part 2: 3D Shapes (Surface Areas & Volumes)

### Cube (side a)

```
Volume = a³
Total Surface Area (TSA) = 6a²
Lateral Surface Area (LSA) = 4a²
Diagonal = a√3
```

---

### Cuboid (l × b × h)

```
Volume = l × b × h
TSA = 2(lb + bh + lh)
LSA = 2h(l + b)
Diagonal = √(l² + b² + h²)
```

---

### Cylinder (radius r, height h)

```
Volume = πr²h
Curved Surface Area (CSA) = 2πrh
TSA = 2πr(r + h)
```

**Hollow Cylinder**:
```
Volume = πh(R² - r²)
TSA = 2π(R + r)(h + R - r)
```

---

### Cone (radius r, height h, slant height l)

```
l = √(r² + h²)

Volume = (1/3)πr²h
CSA = πrl
TSA = πr(r + l)
```

---

### Sphere (radius r)

```
Volume = (4/3)πr³
Surface Area = 4πr²
```

---

### Hemisphere (radius r)

```
Volume = (2/3)πr³
CSA = 2πr²
TSA = 3πr²
```

---

### Frustum of Cone (radii R and r, height h, slant height l)

```
l = √[h² + (R - r)²]

Volume = (1/3)πh(R² + r² + Rr)
CSA = π(R + r)l
TSA = π(R + r)l + πR² + πr²
```

---

### Prism (Base area A, height h)

```
Volume = A × h
LSA = Perimeter of base × h
TSA = LSA + 2A
```

---

### Pyramid (Base area A, height h)

```
Volume = (1/3) × A × h
```

---

## 📚 Part 3: Special Formulas & Relationships

### Euler's Formula (Polyhedra)

```
V - E + F = 2

Where:
V = vertices
E = edges
F = faces
```

---

### Scaling Laws

If linear dimensions are scaled by factor k:
```
Perimeter/Length → k times
Area/Surface Area → k² times
Volume → k³ times
```

**Example**: If radius doubles, volume becomes 8× (2³ = 8)

---

### Inscribed and Circumscribed Circles

**Triangle**:
```
Inradius (r) = Area/s = Δ/s (s = semi-perimeter)
Circumradius (R) = abc/(4Δ)
```

**For equilateral triangle (side a)**:
```
r = a/(2√3)
R = a/√3
R = 2r
```

**Square (side a)**:
```
Inscribed circle radius = a/2
Circumscribed circle radius = a√2/2
```

---

## 💡 Advanced Tricks

### Trick 1: Quick Volume Relations

```
Cylinder : Cone : Hemisphere = 3 : 1 : 2 (same base and height)

If h = 2r:
Cylinder : Cone : Sphere = 3 : 1 : 2
```

---

### Trick 2: Diagonal Length

**Rectangle**: d = √(l² + b²)
**Cuboid**: d = √(l² + b² + h²)
**Cube**: d = a√3

---

### Trick 3: Area via Integration Concept

For irregular shapes, break into smaller known shapes and sum.

---

### Trick 4: Circumference to Area

For circle:
```
Area = Circumference²/(4π)
A = C²/4π
```

---

### Trick 5: Maximum Volume Problems

**Cylinder inscribed in sphere (radius R)**:
```
Max volume when h = 2R/√3
```

**Square inscribed in circle (radius R)**:
```
Side = R√2
Max area = 2R²
```

---

## 📊 Comparative Tables

### 2D Shape Areas

| Shape | Area Formula |
|-------|--------------|
| Square (a) | a² |
| Rectangle (l, b) | lb |
| Triangle (base b, height h) | (1/2)bh |
| Equilateral Triangle (a) | (√3/4)a² |
| Circle (r) | πr² |
| Sector (r, θ°) | (θ/360)πr² |
| Trapezium | (1/2)(a+b)h |
| Rhombus (d₁, d₂) | (1/2)d₁d₂ |

---

### 3D Shape Volumes

| Shape | Volume Formula |
|-------|----------------|
| Cube (a) | a³ |
| Cuboid | lbh |
| Cylinder | πr²h |
| Cone | (1/3)πr²h |
| Sphere | (4/3)πr³ |
| Hemisphere | (2/3)πr³ |
| Pyramid | (1/3) × Base area × h |
| Prism | Base area × h |

---

## ⚠️ Edge Cases & Traps

### Trap 1: LSA vs TSA
```
LSA = Lateral/Curved surface only (excludes top/bottom)
TSA = Total surface (includes all surfaces)
```

### Trap 2: Slant Height vs Height
```
Cone: l² = r² + h²
Don't confuse slant height (l) with vertical height (h)
```

### Trap 3: Angle in Sector
```
Check if angle is in degrees or radians
Formulas differ accordingly
```

### Trap 4: Hollow Shapes
```
Volume = Outer volume - Inner volume
Surface includes inner + outer surfaces
```

### Edge Case: Degenerate Shapes
```
h → 0: Volume → 0
r → 0: Shape collapses
```

---

## 🚀 Formula Cheat Sheet

| Shape | Area/Volume | Surface/Perimeter |
|-------|-------------|-------------------|
| Circle | πr² | 2πr |
| Triangle | (1/2)bh | a+b+c |
| Equilateral △ | (√3/4)a² | 3a |
| Square | a² | 4a |
| Rectangle | lb | 2(l+b) |
| Cube | a³ | 6a² |
| Cuboid | lbh | 2(lb+bh+lh) |
| Cylinder | πr²h | 2πr(r+h) |
| Cone | (1/3)πr²h | πr(r+l) |
| Sphere | (4/3)πr³ | 4πr² |
| Hemisphere | (2/3)πr³ | 3πr² |

---

## 📝 GATE-Level Practice

**Q1**: A sector of angle 60° is cut from a circle of radius 21 cm. Find its area.
```
Area = (60/360) × π × 21² = (1/6) × (22/7) × 441
     = 22 × 63/6 = 231 cm²
```

**Q2**: Find volume of a cone with radius 7 cm and height 24 cm.
```
Volume = (1/3) × π × 7² × 24 = (1/3) × (22/7) × 49 × 24
       = 22 × 7 × 8 = 1232 cm³
```

**Q3**: A cube of side 10 cm is melted and recast into spheres of radius 1 cm. How many spheres?
```
Cube volume = 1000 cm³
Sphere volume = (4/3)π × 1 = (4/3)(22/7) = 88/21 cm³
Number = 1000/(88/21) = 21000/88 = 238.6 ≈ 238 spheres
```

**Q4**: Find the area of a rhombus with diagonals 12 cm and 16 cm.
```
Area = (1/2) × 12 × 16 = 96 cm²
```

**Q5**: A cylinder has curved surface area 1320 cm² and height 21 cm. Find radius.
```
CSA = 2πrh
1320 = 2 × (22/7) × r × 21
1320 = 132r
r = 10 cm
```

---

*← [Chapter 10 - Geometry](./10_Geometry.md) | [Chapter 12 - Trigonometry →](./12_Trigonometry.md)*
