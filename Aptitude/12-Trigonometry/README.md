# 📐 Trigonometry | The Singularity

> **The Atomic Truth:** *Trigonometry relates angles to ratios of sides in triangles.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Trigonometric Ratios](#trigonometric-ratios)
3. [Standard Angle Values](#standard-angle-values)
4. [Trigonometric Identities](#trigonometric-identities)
5. [Heights and Distances](#heights-and-distances)
6. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
7. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
8. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Trigonometry Matters?
Though less frequent in GATE aptitude, trigonometry is essential for:
- Height and distance problems
- Engineering applications
- Signal processing foundations
- Geometry problem solving

### The Right Triangle Setup

In a right triangle with angle θ:
- **Opposite (P):** Side opposite to angle θ
- **Adjacent (B):** Side adjacent to angle θ (not hypotenuse)
- **Hypotenuse (H):** Side opposite to right angle (longest)

```
         /|
        / |
   H   /  | P (Opposite)
      /   |
     /θ___|
       B (Adjacent)
```

> **💡 The Golden Pivot:** "SOH-CAH-TOA" - The mnemonic for basic ratios.

---

## Trigonometric Ratios

### Six Basic Ratios

| Function | Definition | Reciprocal |
|----------|------------|------------|
| $\sin\theta$ | $\frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{P}{H}$ | $\csc\theta$ |
| $\cos\theta$ | $\frac{\text{Adjacent}}{\text{Hypotenuse}} = \frac{B}{H}$ | $\sec\theta$ |
| $\tan\theta$ | $\frac{\text{Opposite}}{\text{Adjacent}} = \frac{P}{B}$ | $\cot\theta$ |

### Reciprocal Relationships

$$\csc\theta = \frac{1}{\sin\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \cot\theta = \frac{1}{\tan\theta}$$

### Quotient Relationships

$$\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad \cot\theta = \frac{\cos\theta}{\sin\theta}$$

---

## Standard Angle Values

### Master Table

| Angle | 0° | 30° | 45° | 60° | 90° |
|-------|-----|-----|-----|-----|-----|
| $\sin$ | 0 | $\frac{1}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | 1 |
| $\cos$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$ | 0 |
| $\tan$ | 0 | $\frac{1}{\sqrt{3}}$ | 1 | $\sqrt{3}$ | ∞ |

### Memorization Pattern

**For sin:** $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$

**For cos:** Reverse of sin values

**For tan:** $\frac{\sin}{\cos}$ for each angle

### Additional Values

| Angle | sin | cos | tan |
|-------|-----|-----|-----|
| 15° | $\frac{\sqrt{6}-\sqrt{2}}{4}$ | $\frac{\sqrt{6}+\sqrt{2}}{4}$ | $2-\sqrt{3}$ |
| 75° | $\frac{\sqrt{6}+\sqrt{2}}{4}$ | $\frac{\sqrt{6}-\sqrt{2}}{4}$ | $2+\sqrt{3}$ |

### Quadrant Signs (ASTC Rule)

```
        90°
    II  |  I
   S    |    A (All positive)
--------|--------
   T    |    C
   III  |  IV
       270°
```

- **A**ll (I quadrant): All positive
- **S**in (II quadrant): Only sin positive
- **T**an (III quadrant): Only tan positive
- **C**os (IV quadrant): Only cos positive

---

## Trigonometric Identities

### Pythagorean Identities

$$\sin^2\theta + \cos^2\theta = 1$$
$$1 + \tan^2\theta = \sec^2\theta$$
$$1 + \cot^2\theta = \csc^2\theta$$

### Complementary Angle Relationships

$$\sin(90° - \theta) = \cos\theta$$
$$\cos(90° - \theta) = \sin\theta$$
$$\tan(90° - \theta) = \cot\theta$$

### Sum and Difference Formulas

$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$
$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$
$$\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$$

### Double Angle Formulas

$$\sin 2\theta = 2\sin\theta\cos\theta$$
$$\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$$
$$\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}$$

### Half Angle Formulas

$$\sin\frac{\theta}{2} = \pm\sqrt{\frac{1 - \cos\theta}{2}}$$
$$\cos\frac{\theta}{2} = \pm\sqrt{\frac{1 + \cos\theta}{2}}$$
$$\tan\frac{\theta}{2} = \frac{1 - \cos\theta}{\sin\theta} = \frac{\sin\theta}{1 + \cos\theta}$$

### Product to Sum

$$2\sin A \cos B = \sin(A+B) + \sin(A-B)$$
$$2\cos A \sin B = \sin(A+B) - \sin(A-B)$$
$$2\cos A \cos B = \cos(A+B) + \cos(A-B)$$
$$2\sin A \sin B = \cos(A-B) - \cos(A+B)$$

---

## Heights and Distances

### Key Terms

**Angle of Elevation:** Angle from horizontal UP to the object
**Angle of Depression:** Angle from horizontal DOWN to the object

> **Note:** Angle of elevation from A to B = Angle of depression from B to A

### Standard Configurations

#### Type 1: Simple Height Problem

Object height $h$, distance from base $d$, angle of elevation $\theta$:
$$\tan\theta = \frac{h}{d}$$

#### Type 2: Two Angles of Elevation

From two points at distances $d_1$ and $d_2$ from a tower of height $h$:
$$h = \frac{d_1 d_2 (\tan\theta_1 - \tan\theta_2)}{d_1 \tan\theta_1 - d_2 \tan\theta_2}$$

For a special case when observer moves distance $d$ towards tower:
$$h = \frac{d \tan\theta_1 \tan\theta_2}{\tan\theta_2 - \tan\theta_1}$$

#### Type 3: Object Moving

When angle of elevation changes from $\theta_1$ to $\theta_2$ as object approaches:
$$\text{Distance covered} = h(\cot\theta_1 - \cot\theta_2)$$

---

## GATE & ESE Problem Patterns

### Pattern 1: Basic Ratio Application
> If $\sin\theta = \frac{3}{5}$, find $\cos\theta$ and $\tan\theta$.

Using $\sin^2\theta + \cos^2\theta = 1$:
$$\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$$
$$\cos\theta = \frac{4}{5}$$ (assuming first quadrant)
$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{3}{4}$$

### Pattern 2: Height Calculation
> From a point 50m from a tower base, angle of elevation of top is 60°. Find height.

$$\tan 60° = \frac{h}{50}$$
$$\sqrt{3} = \frac{h}{50}$$
$$h = 50\sqrt{3} \approx 86.6$$ m

### Pattern 3: Shadow Problems
> A pole 6m high casts a shadow of 2√3 m. Find the angle of elevation of sun.

$$\tan\theta = \frac{6}{2\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3}$$
$$\theta = 60°$$

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"If tan θ = 4/3, find sin θ."

Wrong approach: sin θ = 4/3 (confusing ratios)

**The Elegant Solution:**
- tan θ = P/B = 4/3
- H = √(P² + B²) = √(16 + 9) = 5
- sin θ = P/H = **4/5**

**MSQ Logic Gate:**
- sin and cos are always between -1 and 1
- tan can be any real number
- Verify quadrant for sign

**NAT Precision Lock:**
- $\sqrt{2} \approx 1.414$
- $\sqrt{3} \approx 1.732$
- Use exact values when possible

---

## Speed Tricks & Shortcuts

### Trick 1: The 3-4-5 Triangle

When sin = 3/5 or cos = 4/5:
- Sides are 3, 4, 5 (or multiples)
- Quick calculation without Pythagorean theorem

### Trick 2: Complementary Pair

If $\alpha + \beta = 90°$:
$$\sin\alpha = \cos\beta, \quad \tan\alpha = \cot\beta$$

### Trick 3: Standard Triangle Ratios

| Triangle | Angles | Side Ratios |
|----------|--------|-------------|
| 30-60-90 | 30°, 60°, 90° | 1 : √3 : 2 |
| 45-45-90 | 45°, 45°, 90° | 1 : 1 : √2 |

### Trick 4: Quick tan from sin and cos

$$\tan\theta = \frac{\sin\theta}{\cos\theta}$$

Use mental division of the table values.

### Trick 5: Height-Distance Quick Formula

For angle of elevation θ from distance d:
$$h = d \times \tan\theta$$

---

## Permanent Recall

### The Bizarre Mnemonic (SOH-CAH-TOA)
*"**S**ome **O**ld **H**orse **C**aught **A**nother **H**orse **T**aking **O**ats **A**way"*

- Sin = Opposite/Hypotenuse
- Cos = Adjacent/Hypotenuse  
- Tan = Opposite/Adjacent

### The Mental Slider
Visualize a unit circle:
- sin θ = y-coordinate on circle
- cos θ = x-coordinate on circle
- As θ increases from 0° to 90°, sin increases, cos decreases

### The 5-Second Snap-Check
- sin 0° = 0, sin 90° = 1 (starts low, ends high)
- cos 0° = 1, cos 90° = 0 (starts high, ends low)
- tan 45° = 1 (equal opposite and adjacent)

---

## Practice Problems

### Level 1: Fundamentals
1. Find the value of $\sin 60° \cos 30° + \cos 60° \sin 30°$.
2. If $\cos\theta = \frac{5}{13}$, find $\sin\theta$ and $\tan\theta$.
3. A ladder 10m long reaches a window 8m high. Find the angle it makes with ground.

### Level 2: GATE Standard
4. Prove that $\frac{\sin\theta}{1 + \cos\theta} + \frac{1 + \cos\theta}{\sin\theta} = 2\csc\theta$.
5. From the top of a 100m tower, angles of depression of two cars on opposite sides are 30° and 45°. Find distance between cars.
6. If $\tan\theta + \cot\theta = 2$, find the value of $\tan^2\theta + \cot^2\theta$.

### Level 3: IIT Examiner Level
7. If $\sin\theta + \sin^2\theta = 1$, find the value of $\cos^{12}\theta + 3\cos^{10}\theta + 3\cos^8\theta + \cos^6\theta$.
8. The angle of elevation of the top of a tower from a point A due south is 30° and from B due east is 60°. If AB = 100m, find tower height.
9. Simplify: $\frac{\sin^3\theta + \cos^3\theta}{\sin\theta + \cos\theta} + \sin\theta\cos\theta$

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. $\sin 60° \cos 30° + \cos 60° \sin 30°$
   $= \frac{\sqrt{3}}{2} \times \frac{\sqrt{3}}{2} + \frac{1}{2} \times \frac{1}{2}$
   $= \frac{3}{4} + \frac{1}{4} = **1**$
   
   (This is $\sin(60° + 30°) = \sin 90° = 1$)

2. $\sin^2\theta = 1 - \frac{25}{169} = \frac{144}{169}$
   $\sin\theta = \frac{12}{13}$
   $\tan\theta = \frac{12/13}{5/13} = **\frac{12}{5}**$

3. $\sin\theta = \frac{8}{10} = \frac{4}{5}$
   $\theta = \sin^{-1}(0.8) ≈ **53.13°**$

4. LHS = $\frac{\sin^2\theta + (1+\cos\theta)^2}{\sin\theta(1+\cos\theta)}$
   $= \frac{\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta}{\sin\theta(1+\cos\theta)}$
   $= \frac{2 + 2\cos\theta}{\sin\theta(1+\cos\theta)}$
   $= \frac{2(1 + \cos\theta)}{\sin\theta(1+\cos\theta)}$
   $= \frac{2}{\sin\theta} = 2\csc\theta$ = RHS ✓

5. From top, angle of depression 30° means angle from ground is 30°.
   Distance of first car = $100\cot 30° = 100\sqrt{3}$ m
   Distance of second car = $100\cot 45° = 100$ m
   Total distance = $100\sqrt{3} + 100 = 100(\sqrt{3} + 1) ≈ **273.2$ m**

6. $\tan\theta + \cot\theta = 2$
   $\tan\theta + \frac{1}{\tan\theta} = 2$
   Let $\tan\theta = t$: $t + \frac{1}{t} = 2$
   $t^2 + 1 = 2t$
   $t^2 - 2t + 1 = 0$
   $(t-1)^2 = 0 \implies t = 1$
   
   $\tan^2\theta + \cot^2\theta = 1 + 1 = **2**$

7. $\sin\theta = 1 - \sin^2\theta = \cos^2\theta$
   
   Expression = $\cos^6\theta(\cos^6\theta + 3\cos^4\theta + 3\cos^2\theta + 1)$
   $= \cos^6\theta((\cos^2\theta + 1)^3)$
   $= \cos^6\theta(\sin\theta + 1)^3$
   
   Since $\sin\theta = \cos^2\theta$:
   $= \sin^3\theta(1 + \sin\theta)^3$
   
   From $\sin\theta + \sin^2\theta = 1$: $\sin\theta(1 + \sin\theta) = 1$
   So $(1 + \sin\theta) = \frac{1}{\sin\theta}$
   
   $= \sin^3\theta \times \frac{1}{\sin^3\theta} = **1**$

8. Let tower height = h
   From A (south): $\tan 30° = \frac{h}{d_A} \implies d_A = h\sqrt{3}$
   From B (east): $\tan 60° = \frac{h}{d_B} \implies d_B = \frac{h}{\sqrt{3}}$
   
   $d_A^2 + d_B^2 = 100^2$ (since A is south, B is east)
   $3h^2 + \frac{h^2}{3} = 10000$
   $\frac{10h^2}{3} = 10000$
   $h^2 = 3000$
   $h = **\sqrt{3000} = 10\sqrt{30} ≈ 54.77$ m**

9. $\frac{\sin^3\theta + \cos^3\theta}{\sin\theta + \cos\theta} + \sin\theta\cos\theta$
   
   Using $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$:
   $= \frac{(\sin\theta + \cos\theta)(\sin^2\theta - \sin\theta\cos\theta + \cos^2\theta)}{\sin\theta + \cos\theta} + \sin\theta\cos\theta$
   $= \sin^2\theta - \sin\theta\cos\theta + \cos^2\theta + \sin\theta\cos\theta$
   $= \sin^2\theta + \cos^2\theta = **1**$

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Trigonometry with Coordinate Geometry for a Rank-1 simulation?
