# 📏 Mensuration | The Singularity

> **The Atomic Truth:** *Mensuration measures shapes—perimeter encloses, area covers, volume fills.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [2D Shapes - Perimeter and Area](#2d-shapes---perimeter-and-area)
3. [3D Shapes - Surface Area and Volume](#3d-shapes---surface-area-and-volume)
4. [Conversions and Scaling](#conversions-and-scaling)
5. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
6. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
7. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Mensuration Matters?
Mensuration directly applies to engineering problems:
- Material estimation
- Container design
- Surface coating calculations
- Space optimization

### Key Definitions

| Term | Definition | Unit |
|------|------------|------|
| **Perimeter** | Length of boundary | m, cm |
| **Area** | Surface covered | m², cm² |
| **Volume** | Space occupied | m³, cm³ |
| **Surface Area** | Total outer surface | m², cm² |

> **💡 The Golden Pivot:** Area scales with square of length; Volume scales with cube of length.

---

## 2D Shapes - Perimeter and Area

### Square (side $a$)

| Property | Formula |
|----------|---------|
| Perimeter | $4a$ |
| Area | $a^2$ |
| Diagonal | $a\sqrt{2}$ |

### Rectangle (length $l$, breadth $b$)

| Property | Formula |
|----------|---------|
| Perimeter | $2(l + b)$ |
| Area | $l \times b$ |
| Diagonal | $\sqrt{l^2 + b^2}$ |

### Triangle

| Type | Area Formula |
|------|--------------|
| General | $\frac{1}{2} \times \text{base} \times \text{height}$ |
| Heron's | $\sqrt{s(s-a)(s-b)(s-c)}$, where $s = \frac{a+b+c}{2}$ |
| Equilateral (side $a$) | $\frac{\sqrt{3}}{4}a^2$ |
| Right-angled | $\frac{1}{2} \times \text{leg}_1 \times \text{leg}_2$ |

### Circle (radius $r$)

| Property | Formula |
|----------|---------|
| Circumference | $2\pi r$ |
| Area | $\pi r^2$ |
| Diameter | $2r$ |

### Semicircle

| Property | Formula |
|----------|---------|
| Perimeter | $\pi r + 2r$ |
| Area | $\frac{\pi r^2}{2}$ |

### Sector (radius $r$, angle $\theta$)

| Property | Formula (θ in degrees) |
|----------|------------------------|
| Arc Length | $\frac{\theta}{360} \times 2\pi r$ |
| Area | $\frac{\theta}{360} \times \pi r^2$ |

### Ring/Annulus (outer radius $R$, inner radius $r$)

$$\text{Area} = \pi(R^2 - r^2) = \pi(R+r)(R-r)$$

### Parallelogram (base $b$, height $h$)

$$\text{Area} = b \times h$$

### Rhombus (diagonals $d_1$ and $d_2$)

$$\text{Area} = \frac{1}{2} \times d_1 \times d_2$$

### Trapezium (parallel sides $a$ and $b$, height $h$)

$$\text{Area} = \frac{1}{2}(a + b) \times h$$

### Regular Polygon (n sides, side length $a$)

$$\text{Area} = \frac{na^2}{4}\cot\left(\frac{\pi}{n}\right)$$

For hexagon ($n = 6$):
$$\text{Area} = \frac{3\sqrt{3}}{2}a^2$$

---

## 3D Shapes - Surface Area and Volume

### Cube (side $a$)

| Property | Formula |
|----------|---------|
| Volume | $a^3$ |
| Total Surface Area (TSA) | $6a^2$ |
| Diagonal | $a\sqrt{3}$ |

### Cuboid (length $l$, breadth $b$, height $h$)

| Property | Formula |
|----------|---------|
| Volume | $l \times b \times h$ |
| TSA | $2(lb + bh + lh)$ |
| Lateral Surface Area (LSA) | $2h(l + b)$ |
| Diagonal | $\sqrt{l^2 + b^2 + h^2}$ |

### Cylinder (radius $r$, height $h$)

| Property | Formula |
|----------|---------|
| Volume | $\pi r^2 h$ |
| Curved Surface Area (CSA) | $2\pi r h$ |
| TSA | $2\pi r(r + h)$ |

### Hollow Cylinder (outer radius $R$, inner radius $r$, height $h$)

| Property | Formula |
|----------|---------|
| Volume | $\pi h(R^2 - r^2)$ |
| TSA | $2\pi(R + r)(h + R - r)$ |

### Cone (radius $r$, height $h$, slant height $l$)

$$l = \sqrt{r^2 + h^2}$$

| Property | Formula |
|----------|---------|
| Volume | $\frac{1}{3}\pi r^2 h$ |
| CSA | $\pi r l$ |
| TSA | $\pi r(r + l)$ |

### Sphere (radius $r$)

| Property | Formula |
|----------|---------|
| Volume | $\frac{4}{3}\pi r^3$ |
| Surface Area | $4\pi r^2$ |

### Hemisphere (radius $r$)

| Property | Formula |
|----------|---------|
| Volume | $\frac{2}{3}\pi r^3$ |
| Curved Surface Area | $2\pi r^2$ |
| TSA | $3\pi r^2$ |

### Frustum of Cone (radii $r_1$ and $r_2$, height $h$, slant height $l$)

$$l = \sqrt{h^2 + (r_1 - r_2)^2}$$

| Property | Formula |
|----------|---------|
| Volume | $\frac{1}{3}\pi h(r_1^2 + r_2^2 + r_1 r_2)$ |
| CSA | $\pi l(r_1 + r_2)$ |
| TSA | $\pi[r_1^2 + r_2^2 + l(r_1 + r_2)]$ |

### Prism (base area $A$, height $h$)

| Property | Formula |
|----------|---------|
| Volume | $A \times h$ |
| LSA | Perimeter of base × $h$ |

### Pyramid (base area $A$, height $h$)

| Property | Formula |
|----------|---------|
| Volume | $\frac{1}{3} \times A \times h$ |

---

## Conversions and Scaling

### Unit Conversions

| Conversion | Relation |
|------------|----------|
| 1 m | 100 cm |
| 1 m² | 10,000 cm² |
| 1 m³ | 1,000,000 cm³ |
| 1 litre | 1000 cm³ = 0.001 m³ |
| 1 m³ | 1000 litres |

### Scaling Laws

When linear dimensions scale by factor $k$:
- **Perimeter** scales by $k$
- **Area** scales by $k^2$
- **Volume** scales by $k^3$

**Example:** If all dimensions of a cube double:
- New volume = $2^3 = 8$ times original

---

## GATE & ESE Problem Patterns

### Pattern 1: Volume to Surface Area
> A sphere has volume 36π cm³. Find its surface area.

$$\frac{4}{3}\pi r^3 = 36\pi$$
$$r^3 = 27 \implies r = 3$$
Surface Area = $4\pi(9) = 36\pi$ cm²

### Pattern 2: Combined Shapes
> A toy is in the form of a cone mounted on a hemisphere of same radius 3 cm. Total height is 7 cm. Find volume.

- Cone height = 7 - 3 = 4 cm
- Cone volume = $\frac{1}{3}\pi(9)(4) = 12\pi$
- Hemisphere volume = $\frac{2}{3}\pi(27) = 18\pi$
- Total = $30\pi$ cm³

### Pattern 3: Melting & Recasting
> A metallic sphere of radius 6 cm is melted and recast into a cylinder of radius 4 cm. Find height.

Volume conserved:
$$\frac{4}{3}\pi(6)^3 = \pi(4)^2 \times h$$
$$\frac{4}{3}(216) = 16h$$
$$h = 18$$ cm

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"If the radius of a sphere is halved, by what percentage does volume decrease?"

Wrong approach: 50% (linear thinking)

**The Elegant Solution:**
- Original volume = $\frac{4}{3}\pi r^3$
- New volume = $\frac{4}{3}\pi (\frac{r}{2})^3 = \frac{4}{3}\pi \frac{r^3}{8}$
- New volume = $\frac{1}{8}$ of original
- Decrease = $\frac{7}{8} = 87.5\%$

**MSQ Logic Gate:**
- Volume scales with cube of radius
- Area scales with square of radius
- Don't confuse 2D and 3D scaling

**NAT Precision Lock:**
- Use $\pi = 3.14159$ unless specified otherwise
- Keep $\pi$ in answer if possible for exact value

---

## Speed Tricks & Shortcuts

### Trick 1: Sphere-Cylinder-Cone Relationship

For same base radius and height:
$$V_{\text{cone}} : V_{\text{hemisphere}} : V_{\text{cylinder}} = 1 : 2 : 3$$

### Trick 2: Quick π Approximations

| Calculation | Approximation |
|-------------|---------------|
| $\pi$ | 3.14 or 22/7 |
| $\pi^2$ | 10 (rough) |
| $\sqrt{\pi}$ | 1.77 |

### Trick 3: Diagonal Memory

- Square diagonal: side × $\sqrt{2}$ ≈ side × 1.414
- Cube diagonal: side × $\sqrt{3}$ ≈ side × 1.732

### Trick 4: Equilateral Triangle Quick Area

$$\text{Area} ≈ 0.433 \times \text{side}^2$$

### Trick 5: Cone-Cylinder Comparison

Cone is exactly $\frac{1}{3}$ of cylinder with same base and height.

---

## Permanent Recall

### The Bizarre Mnemonic (Volume Formulas)
*"A cylinder is a full pizza. A cone is just a third of that pizza (stacked differently). A sphere is four-thirds (greedy sphere takes more than cone's share)!"*

### The Mental Slider
Visualize inflation:
- Doubling radius of sphere → Volume becomes 8×
- Halving height of cylinder → Volume becomes half
- Both radius and height double → Volume becomes 8× (not 4×!)

### The 5-Second Snap-Check
- Sphere has no edges or corners
- Cylinder TSA > CSA (adds two circles)
- Volume of cone = ⅓ × cylinder of same dimensions

---

## Practice Problems

### Level 1: Fundamentals
1. Find the area of a sector with radius 14 cm and angle 90°.
2. A cylinder has radius 7 cm and height 10 cm. Find volume and TSA.
3. What is the volume of a hemisphere of diameter 12 cm?

### Level 2: GATE Standard
4. A rectangular sheet 44 cm × 20 cm is rolled to form a cylinder. Find the volume.
5. A cone and cylinder have same base radius and height. If cone's volume is 100 cm³, find cylinder's volume.
6. Water in a cylindrical vessel of radius 10 cm rises by 5 cm when a sphere is immersed. Find sphere's radius.

### Level 3: IIT Examiner Level
7. A right circular cone is divided by a plane parallel to base into two parts of equal volumes. Find the ratio of heights of the two parts.
8. A solid metallic right circular cone of height 20 cm and base radius 5 cm is melted and recast into a solid sphere. Find the radius of sphere.
9. The volume of a cube is numerically equal to its surface area. Find the edge length.

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Area = $\frac{90}{360} × \pi × 14^2 = \frac{1}{4} × \frac{22}{7} × 196 = **154 cm²**$

2. Volume = $\pi r^2 h = \frac{22}{7} × 49 × 10 = **1540 cm³**$
   TSA = $2\pi r(r+h) = 2 × \frac{22}{7} × 7 × 17 = **748 cm²**$

3. Radius = 6 cm
   Volume = $\frac{2}{3}\pi r^3 = \frac{2}{3} × \pi × 216 = 144\pi = **452.16 cm³**$

4. When 44 cm becomes circumference: $2\pi r = 44 \implies r = 7$ cm, height = 20 cm
   Volume = $\pi × 49 × 20 = **3080 cm³**$
   
   Or if 20 cm is circumference: $r = 10/\pi$, height = 44 cm
   (Usually the longer side becomes circumference for maximum volume)

5. Cylinder volume = 3 × Cone volume = **300 cm³**

6. Volume of sphere = Volume of water displaced = $\pi × 100 × 5 = 500\pi$
   $\frac{4}{3}\pi r^3 = 500\pi$
   $r^3 = 375$
   **$r = \sqrt[3]{375} ≈ 7.21$ cm**

7. Let original cone height = $h$, radius = $r$
   Smaller cone (top part) has height $h_1$ and radius $r_1$
   By similar triangles: $\frac{r_1}{r} = \frac{h_1}{h}$
   
   Volume of top part = $\frac{1}{3}\pi r_1^2 h_1 = \frac{1}{2} × \frac{1}{3}\pi r^2 h$
   
   Since shapes are similar: $\left(\frac{h_1}{h}\right)^3 = \frac{1}{2}$
   $h_1 = h × 2^{-1/3} = h/\sqrt[3]{2}$
   
   Lower part height = $h - h_1 = h(1 - 2^{-1/3})$
   
   Ratio = $h_1 : (h - h_1) = 1 : (\sqrt[3]{2} - 1) ≈ **1 : 0.26**$ or approximately **4:1**

8. Volume of cone = $\frac{1}{3}\pi × 25 × 20 = \frac{500\pi}{3}$
   
   $\frac{4}{3}\pi r^3 = \frac{500\pi}{3}$
   $r^3 = 125$
   **$r = 5$ cm**

9. $a^3 = 6a^2$
   $a = 6$
   **Edge = 6 units**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Mensuration with Trigonometry for a Rank-1 simulation?
