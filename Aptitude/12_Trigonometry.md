# Chapter 12: Trigonometry

> **The mathematics of triangles and angles - bridging geometry with analysis**

---

## 🎯 Why Study This?

- Essential for heights and distances problems
- Foundation for coordinate geometry and calculus
- GATE/ESE includes trigonometry-based aptitude questions

---

## 📚 Part 1: Basic Trigonometric Ratios

### Right Triangle Definitions

For a right triangle with angle θ (not the right angle):

```
      |\
      | \  Hypotenuse
  Opp |  \
      |___\
       Adj
```

| Ratio | Definition | Mnemonic |
|-------|------------|----------|
| sin θ | Opposite/Hypotenuse | **S**OH |
| cos θ | Adjacent/Hypotenuse | **C**AH |
| tan θ | Opposite/Adjacent | **T**OA |
| csc θ | Hypotenuse/Opposite | 1/sin θ |
| sec θ | Hypotenuse/Adjacent | 1/cos θ |
| cot θ | Adjacent/Opposite | 1/tan θ |

**💡 Mnemonic**: **SOH-CAH-TOA** (Some Old Hag Caught A Hippie Tripping On Acid)

---

### Key Reciprocal Relations

```
sin θ × csc θ = 1
cos θ × sec θ = 1
tan θ × cot θ = 1
tan θ = sin θ / cos θ
cot θ = cos θ / sin θ
```

---

## 📊 Standard Angle Values (Memorize!)

| θ | 0° | 30° | 45° | 60° | 90° |
|---|-----|------|------|------|------|
| sin | 0 | 1/2 | 1/√2 | √3/2 | 1 |
| cos | 1 | √3/2 | 1/√2 | 1/2 | 0 |
| tan | 0 | 1/√3 | 1 | √3 | ∞ |

**⚡ Pattern Trick**:
```
sin: √0/2, √1/2, √2/2, √3/2, √4/2 = 0, 1/2, 1/√2, √3/2, 1
cos: Reverse of sin values
tan: sin/cos for each angle
```

---

## 📐 Pythagorean Identities

```
sin²θ + cos²θ = 1
1 + tan²θ = sec²θ
1 + cot²θ = csc²θ
```

**Derived Forms**:
```
sin²θ = 1 - cos²θ
cos²θ = 1 - sin²θ
tan²θ = sec²θ - 1
cot²θ = csc²θ - 1
```

---

## 🔄 Angle Transformation Formulas

### Complementary Angles (90° - θ)

```
sin(90° - θ) = cos θ
cos(90° - θ) = sin θ
tan(90° - θ) = cot θ
```

**💡 Key**: "Co-functions" swap (sin ↔ cos, tan ↔ cot, sec ↔ csc)

---

### Supplementary Angles (180° - θ)

```
sin(180° - θ) = sin θ
cos(180° - θ) = -cos θ
tan(180° - θ) = -tan θ
```

---

### Negative Angles

```
sin(-θ) = -sin θ    (odd function)
cos(-θ) = cos θ     (even function)
tan(-θ) = -tan θ    (odd function)
```

---

### Signs in Four Quadrants

```
        90°
         |
    II   |   I
  (sin+) | (all+)
---------|--------- 0°/360°
  (tan+) | (cos+)
   III   |   IV
         |
        270°
```

**💡 Mnemonic**: **A**ll **S**tudents **T**ake **C**alculus (I, II, III, IV)
- I: All positive
- II: Only Sin positive
- III: Only Tan positive
- IV: Only Cos positive

---

## ➕➖ Addition & Subtraction Formulas

### Compound Angles

```
sin(A + B) = sin A cos B + cos A sin B
sin(A - B) = sin A cos B - cos A sin B
cos(A + B) = cos A cos B - sin A sin B
cos(A - B) = cos A cos B + sin A sin B
tan(A + B) = (tan A + tan B)/(1 - tan A tan B)
tan(A - B) = (tan A - tan B)/(1 + tan A tan B)
```

---

### Double Angle Formulas

```
sin 2θ = 2 sin θ cos θ
cos 2θ = cos²θ - sin²θ = 2cos²θ - 1 = 1 - 2sin²θ
tan 2θ = 2tan θ/(1 - tan²θ)
```

---

### Half Angle Formulas

```
sin(θ/2) = ±√[(1 - cos θ)/2]
cos(θ/2) = ±√[(1 + cos θ)/2]
tan(θ/2) = (1 - cos θ)/sin θ = sin θ/(1 + cos θ)
```

---

### Triple Angle Formulas

```
sin 3θ = 3sin θ - 4sin³θ
cos 3θ = 4cos³θ - 3cos θ
tan 3θ = (3tan θ - tan³θ)/(1 - 3tan²θ)
```

---

## ✖️ Product & Sum Formulas

### Product to Sum

```
2 sin A cos B = sin(A+B) + sin(A-B)
2 cos A sin B = sin(A+B) - sin(A-B)
2 cos A cos B = cos(A+B) + cos(A-B)
2 sin A sin B = cos(A-B) - cos(A+B)
```

---

### Sum to Product

```
sin A + sin B = 2 sin[(A+B)/2] cos[(A-B)/2]
sin A - sin B = 2 cos[(A+B)/2] sin[(A-B)/2]
cos A + cos B = 2 cos[(A+B)/2] cos[(A-B)/2]
cos A - cos B = -2 sin[(A+B)/2] sin[(A-B)/2]
```

---

## 📐 Triangle Solutions

### Sine Rule

```
a/sin A = b/sin B = c/sin C = 2R

Where R = circumradius
```

**Use when**: Given 2 angles + 1 side, or 2 sides + 1 angle (non-included)

---

### Cosine Rule

```
a² = b² + c² - 2bc cos A
b² = a² + c² - 2ac cos B
c² = a² + b² - 2ab cos C
```

**Use when**: Given 3 sides, or 2 sides + included angle

---

### Area of Triangle

```
Area = (1/2) × a × b × sin C
     = (1/2) × b × c × sin A
     = (1/2) × a × c × sin B
```

---

## 🏔️ Heights and Distances

### Standard Problem Types

**Type 1: Angle of Elevation**
```
Looking UP from horizontal
tan θ = height / distance
```

**Type 2: Angle of Depression**
```
Looking DOWN from horizontal
Equals angle of elevation from ground (alternate angles)
```

**Type 3: Object on Hill**
If object height = h on hill of height H:
```
From distance d: tan α = H/d, tan β = (H+h)/d
h = d(tan β - tan α)
```

---

### Two-Position Problems

From two points at distances d₁ and d₂ from a tower of height h:
```
h = d₁ × tan θ₁ = d₂ × tan θ₂
```

**Moving toward/away**:
```
If angles are α and β, distance moved = d
h = d × tan α × tan β / (tan α - tan β)    [for α > β, moving away]
```

---

## 💡 Advanced Tricks

### Trick 1: Max/Min Values

```
-1 ≤ sin θ ≤ 1
-1 ≤ cos θ ≤ 1
-∞ < tan θ < ∞

For a sin θ + b cos θ:
Max = √(a² + b²)
Min = -√(a² + b²)
```

---

### Trick 2: Quick Calculation

```
sin 15° = (√6 - √2)/4
cos 15° = (√6 + √2)/4
sin 75° = (√6 + √2)/4
cos 75° = (√6 - √2)/4
```

---

### Trick 3: Small Angle Approximations

For θ in radians, when θ → 0:
```
sin θ ≈ θ
cos θ ≈ 1 - θ²/2
tan θ ≈ θ
```

---

### Trick 4: Converting Between Degrees and Radians

```
180° = π radians
1° = π/180 radians
1 radian = 180°/π ≈ 57.3°
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Quadrant Awareness
```
sin 150° = sin 30° = 0.5 (not -0.5)
cos 150° = -cos 30° = -√3/2
Always check the quadrant for signs
```

### Trap 2: Domain Restrictions
```
sin⁻¹(x): -1 ≤ x ≤ 1
cos⁻¹(x): -1 ≤ x ≤ 1
tan⁻¹(x): all real x
```

### Trap 3: Inverse Function Range
```
sin⁻¹: [-π/2, π/2]
cos⁻¹: [0, π]
tan⁻¹: (-π/2, π/2)
```

### Trap 4: sec and csc Undefined
```
sec 90° = 1/cos 90° = undefined (∞)
csc 0° = 1/sin 0° = undefined (∞)
```

---

## 🚀 Formula Cheat Sheet

| Identity | Formula |
|----------|---------|
| sin²θ + cos²θ | 1 |
| 1 + tan²θ | sec²θ |
| 1 + cot²θ | csc²θ |
| sin 2θ | 2 sin θ cos θ |
| cos 2θ | cos²θ - sin²θ |
| sin(A±B) | sin A cos B ± cos A sin B |
| cos(A±B) | cos A cos B ∓ sin A sin B |
| a/sin A | b/sin B = c/sin C = 2R |
| a² | b² + c² - 2bc cos A |
| Area | (1/2)ab sin C |

---

## 📝 GATE-Level Practice

**Q1**: Find the value of sin 75°.
```
sin 75° = sin(45° + 30°)
        = sin 45° cos 30° + cos 45° sin 30°
        = (1/√2)(√3/2) + (1/√2)(1/2)
        = (√3 + 1)/(2√2) = (√6 + √2)/4
```

**Q2**: If tan θ = 3/4, find sin θ (θ in first quadrant).
```
tan θ = 3/4 = Opp/Adj
Hypotenuse = √(9 + 16) = 5
sin θ = 3/5
```

**Q3**: From a point 100m from a tower, angle of elevation to top is 30°. Find height.
```
tan 30° = h/100
h = 100 × (1/√3) = 100√3/3 ≈ 57.7 m
```

**Q4**: Simplify: (sin 2θ)/(1 + cos 2θ)
```
= 2 sin θ cos θ / (1 + 2cos²θ - 1)
= 2 sin θ cos θ / 2cos²θ
= sin θ / cos θ
= tan θ
```

**Q5**: Find the maximum value of 3 sin x + 4 cos x.
```
Max = √(3² + 4²) = √25 = 5
```

---

*← [Chapter 11 - Mensuration](./11_Mensuration.md) | [Chapter 13 - Coordinate Geometry →](./13_Coordinate_Geometry.md)*
