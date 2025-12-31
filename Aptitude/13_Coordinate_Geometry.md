# Chapter 13: Coordinate Geometry

> **Algebra meets geometry - plotting mathematical relationships on a plane**

---

## 🎯 Why Study This?

- Bridges algebraic equations with geometric figures
- Essential for understanding graphs and curves
- GATE/ESE uses coordinate geometry in aptitude section

---

## 📚 Part 1: Basics

### Cartesian Coordinate System

```
         Y
         |
    II   |   I
  (-,+)  |  (+,+)
---------O--------- X
  (-,-)  |  (+,-)
   III   |   IV
         |
```

**Point notation**: P(x, y) where x = abscissa, y = ordinate

---

### Distance Formula

Distance between P(x₁, y₁) and Q(x₂, y₂):
```
d = √[(x₂-x₁)² + (y₂-y₁)²]
```

**Special case**: Distance from origin to P(x, y):
```
d = √(x² + y²)
```

---

### Section Formula

Point dividing line joining (x₁, y₁) and (x₂, y₂):

**Internal division in ratio m:n**:
```
P = ((mx₂ + nx₁)/(m+n), (my₂ + ny₁)/(m+n))
```

**External division in ratio m:n**:
```
P = ((mx₂ - nx₁)/(m-n), (my₂ - ny₁)/(m-n))
```

**Midpoint (m = n = 1)**:
```
M = ((x₁+x₂)/2, (y₁+y₂)/2)
```

---

### Centroid, Incenter, Circumcenter

**Centroid** of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃):
```
G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)
```

**Incenter** (sides a, b, c opposite to respective vertices):
```
I = ((ax₁+bx₂+cx₃)/(a+b+c), (ay₁+by₂+cy₃)/(a+b+c))
```

---

### Area of Triangle

Vertices at (x₁,y₁), (x₂,y₂), (x₃,y₃):
```
Area = (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
```

**Collinearity**: Points are collinear if Area = 0

---

## 📚 Part 2: Straight Lines

### Slope (Gradient)

```
m = (y₂ - y₁)/(x₂ - x₁) = tan θ
```

Where θ is angle with positive x-axis.

| Line Type | Slope |
|-----------|-------|
| Horizontal | m = 0 |
| Vertical | m = undefined (∞) |
| Rising (↗) | m > 0 |
| Falling (↘) | m < 0 |

---

### Forms of Line Equation

**Slope-Intercept Form**:
```
y = mx + c
Where m = slope, c = y-intercept
```

**Point-Slope Form**:
```
y - y₁ = m(x - x₁)
```

**Two-Point Form**:
```
(y - y₁)/(y₂ - y₁) = (x - x₁)/(x₂ - x₁)
```

**Intercept Form**:
```
x/a + y/b = 1
Where a = x-intercept, b = y-intercept
```

**General Form**:
```
ax + by + c = 0
Slope = -a/b
```

**Normal Form**:
```
x cos α + y sin α = p
Where p = perpendicular distance from origin, α = angle of normal
```

---

### Parallel and Perpendicular Lines

**Parallel lines**: Same slope
```
m₁ = m₂
```

**Perpendicular lines**: Product of slopes = -1
```
m₁ × m₂ = -1
```

---

### Angle Between Two Lines

```
tan θ = |m₁ - m₂|/(1 + m₁m₂)
```

If m₁m₂ = -1, lines are perpendicular (θ = 90°)

---

### Distance from Point to Line

Distance from (x₁, y₁) to line ax + by + c = 0:
```
d = |ax₁ + by₁ + c|/√(a² + b²)
```

---

### Distance Between Parallel Lines

Lines ax + by + c₁ = 0 and ax + by + c₂ = 0:
```
d = |c₁ - c₂|/√(a² + b²)
```

---

### Intersection of Lines

For lines a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0:
```
x = (b₁c₂ - b₂c₁)/(a₁b₂ - a₂b₁)
y = (c₁a₂ - c₂a₁)/(a₁b₂ - a₂b₁)
```

---

## 📚 Part 3: Circles

### Standard Forms

**Center-Radius Form** (center (h,k), radius r):
```
(x - h)² + (y - k)² = r²
```

**General Form**:
```
x² + y² + 2gx + 2fy + c = 0

Center = (-g, -f)
Radius = √(g² + f² - c)
```

---

### Circle Properties

**Condition for valid circle**: g² + f² - c > 0

**Point and Circle**:
- Point (x₁, y₁) outside: x₁² + y₁² + 2gx₁ + 2fy₁ + c > 0
- Point on circle: x₁² + y₁² + 2gx₁ + 2fy₁ + c = 0
- Point inside: x₁² + y₁² + 2gx₁ + 2fy₁ + c < 0

---

### Tangent and Normal

**Tangent at (x₁, y₁) on circle x² + y² = r²**:
```
xx₁ + yy₁ = r²
```

**Tangent to general circle**:
```
xx₁ + yy₁ + g(x+x₁) + f(y+y₁) + c = 0
```

**Length of tangent from external point (x₁, y₁)**:
```
L = √(x₁² + y₁² + 2gx₁ + 2fy₁ + c)
```

---

## 📚 Part 4: Conic Sections

### Parabola

**Standard forms**:
| Equation | Opens | Vertex | Focus | Directrix |
|----------|-------|--------|-------|-----------|
| y² = 4ax | Right | (0,0) | (a,0) | x = -a |
| y² = -4ax | Left | (0,0) | (-a,0) | x = a |
| x² = 4ay | Up | (0,0) | (0,a) | y = -a |
| x² = -4ay | Down | (0,0) | (0,-a) | y = a |

**Key property**: Distance from focus = Distance from directrix

---

### Ellipse

**Standard form** (a > b):
```
x²/a² + y²/b² = 1

Where: b² = a²(1 - e²) or c² = a² - b²
```

| Parameter | Value |
|-----------|-------|
| Center | (0, 0) |
| Major axis | 2a (along x-axis) |
| Minor axis | 2b (along y-axis) |
| Foci | (±c, 0) where c = ae |
| Eccentricity | e = c/a = √(1 - b²/a²), 0 < e < 1 |

---

### Hyperbola

**Standard form**:
```
x²/a² - y²/b² = 1

Where: b² = a²(e² - 1) or c² = a² + b²
```

| Parameter | Value |
|-----------|-------|
| Center | (0, 0) |
| Vertices | (±a, 0) |
| Foci | (±c, 0) where c = ae |
| Eccentricity | e = c/a > 1 |
| Asymptotes | y = ±(b/a)x |

---

### Eccentricity Summary

| Conic | Eccentricity |
|-------|--------------|
| Circle | e = 0 |
| Ellipse | 0 < e < 1 |
| Parabola | e = 1 |
| Hyperbola | e > 1 |

---

## 💡 Advanced Tricks

### Trick 1: Quick Collinearity Check

Three points (x₁,y₁), (x₂,y₂), (x₃,y₃) are collinear if:
```
x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂) = 0
```

---

### Trick 2: Reflection of Point

Reflection of (a, b) across line y = x:
```
Reflected point = (b, a)
```

Reflection across x-axis: (a, -b)
Reflection across y-axis: (-a, b)
Reflection across origin: (-a, -b)

---

### Trick 3: Foot of Perpendicular

Foot of perpendicular from (x₁, y₁) to line ax + by + c = 0:
```
(x, y) = (x₁ - a(ax₁+by₁+c)/(a²+b²), y₁ - b(ax₁+by₁+c)/(a²+b²))
```

---

### Trick 4: Image of Point in Line

Image of (x₁, y₁) in line ax + by + c = 0:
```
(x, y) = (x₁ - 2a(ax₁+by₁+c)/(a²+b²), y₁ - 2b(ax₁+by₁+c)/(a²+b²))
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Vertical Lines
```
Vertical lines have undefined slope
Equation: x = constant (not y = mx + c form)
```

### Trap 2: Circle Radius
```
g² + f² - c must be positive for real circle
If zero: point circle
If negative: imaginary circle
```

### Trap 3: Conic Axis Orientation
```
For x²/a² + y²/b²:
If a > b: major axis along x
If b > a: major axis along y
```

### Trap 4: Parallel Lines (No Intersection)
```
a₁/a₂ = b₁/b₂ ≠ c₁/c₂ means parallel, no solution
a₁/a₂ = b₁/b₂ = c₁/c₂ means same line, infinite solutions
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Distance | √[(x₂-x₁)² + (y₂-y₁)²] |
| Midpoint | ((x₁+x₂)/2, (y₁+y₂)/2) |
| Section (m:n internal) | ((mx₂+nx₁)/(m+n), ...) |
| Slope | (y₂-y₁)/(x₂-x₁) |
| Perpendicular slopes | m₁×m₂ = -1 |
| Point to line distance | \|ax₁+by₁+c\|/√(a²+b²) |
| Circle (general) | center (-g,-f), r = √(g²+f²-c) |
| Tangent length | √(S₁) where S₁ = point substituted |
| Area of triangle | (1/2)\|x₁(y₂-y₃)+x₂(y₃-y₁)+x₃(y₁-y₂)\| |

---

## 📝 GATE-Level Practice

**Q1**: Find distance between (3, 4) and (-2, -8).
```
d = √[(3-(-2))² + (4-(-8))²]
  = √[25 + 144] = √169 = 13
```

**Q2**: Find equation of line through (2, 3) with slope 4.
```
y - 3 = 4(x - 2)
y = 4x - 5
OR 4x - y - 5 = 0
```

**Q3**: Find the center and radius of x² + y² - 6x + 4y - 12 = 0.
```
2g = -6, g = -3, so -g = 3
2f = 4, f = 2, so -f = -2
Center = (3, -2)
r = √(9 + 4 + 12) = √25 = 5
```

**Q4**: Find distance from (4, 5) to line 3x + 4y - 12 = 0.
```
d = |3(4) + 4(5) - 12|/√(9 + 16)
  = |12 + 20 - 12|/5 = 20/5 = 4
```

**Q5**: Are points (1, 1), (2, 3), (4, 7) collinear?
```
Area = (1/2)|1(3-7) + 2(7-1) + 4(1-3)|
     = (1/2)|(-4) + 12 + (-8)|
     = (1/2)|0| = 0
Yes, collinear.
```

---

*← [Chapter 12 - Trigonometry](./12_Trigonometry.md) | [Chapter 14 - Logarithms →](./14_Logarithms.md)*
