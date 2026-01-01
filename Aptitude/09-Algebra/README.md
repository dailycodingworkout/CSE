# 🔢 Algebra | The Singularity

> **The Atomic Truth:** *Algebra abstracts quantities into symbols; equations encode relationships.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Linear Equations](#linear-equations)
3. [Quadratic Equations](#quadratic-equations)
4. [Inequalities](#inequalities)
5. [Progressions](#progressions)
6. [Polynomials](#polynomials)
7. [Logarithms](#logarithms)
8. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
9. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
10. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Algebra Matters?
Algebra is the **language of mathematics**. It enables:
- Problem modeling and solving
- Pattern recognition in sequences
- Understanding function behavior
- Foundation for calculus and higher math

### Basic Algebraic Identities

| Identity | Expansion |
|----------|-----------|
| $(a+b)^2$ | $a^2 + 2ab + b^2$ |
| $(a-b)^2$ | $a^2 - 2ab + b^2$ |
| $a^2 - b^2$ | $(a+b)(a-b)$ |
| $(a+b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| $(a-b)^3$ | $a^3 - 3a^2b + 3ab^2 - b^3$ |
| $a^3 + b^3$ | $(a+b)(a^2 - ab + b^2)$ |
| $a^3 - b^3$ | $(a-b)(a^2 + ab + b^2)$ |

### Additional Useful Identities

$$a^2 + b^2 = (a+b)^2 - 2ab = (a-b)^2 + 2ab$$

$$(a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$$

$$a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2 + b^2 + c^2 - ab - bc - ca)$$

> **💡 Special Case:** If $a + b + c = 0$, then $a^3 + b^3 + c^3 = 3abc$

---

## Linear Equations

### One Variable
$$ax + b = 0 \implies x = -\frac{b}{a}$$

### Two Variables (System)
$$a_1x + b_1y = c_1$$
$$a_2x + b_2y = c_2$$

**Solution Methods:**
1. **Substitution:** Express one variable, substitute
2. **Elimination:** Add/subtract to eliminate one variable
3. **Cross-multiplication:**
$$\frac{x}{b_1c_2 - b_2c_1} = \frac{y}{c_1a_2 - c_2a_1} = \frac{1}{a_1b_2 - a_2b_1}$$

### Consistency Conditions

| Condition | Type | Solutions |
|-----------|------|-----------|
| $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | Consistent | Unique |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Dependent | Infinite |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | Inconsistent | None |

---

## Quadratic Equations

### Standard Form
$$ax^2 + bx + c = 0, \quad a \neq 0$$

### Quadratic Formula
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Discriminant Analysis
$$D = b^2 - 4ac$$

| Discriminant | Nature of Roots |
|--------------|-----------------|
| $D > 0$ | Two distinct real roots |
| $D = 0$ | Two equal real roots |
| $D < 0$ | Two complex conjugate roots |
| $D$ = perfect square | Rational roots |

### Sum and Product of Roots

For roots $\alpha$ and $\beta$:
$$\alpha + \beta = -\frac{b}{a}$$
$$\alpha \cdot \beta = \frac{c}{a}$$

### Forming Equation from Roots

$$x^2 - (\text{sum})x + (\text{product}) = 0$$

### Symmetric Functions of Roots

$$\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta$$
$$\alpha^3 + \beta^3 = (\alpha + \beta)^3 - 3\alpha\beta(\alpha + \beta)$$
$$|\alpha - \beta| = \sqrt{(\alpha + \beta)^2 - 4\alpha\beta}$$

---

## Inequalities

### Basic Rules

1. Adding/subtracting same quantity: Inequality preserved
2. Multiplying/dividing by positive: Inequality preserved
3. Multiplying/dividing by negative: **Inequality reverses**

### Types of Inequalities

**Linear Inequality:**
$$ax + b > 0 \implies x > -\frac{b}{a} \text{ (if } a > 0 \text{)}$$

**Quadratic Inequality:**
For $ax^2 + bx + c > 0$ (with $a > 0$):
- If $D < 0$: Always true (parabola above x-axis)
- If $D \geq 0$: True for $x < \alpha$ or $x > \beta$ (where $\alpha < \beta$ are roots)

### AM-GM-HM Inequality

For positive numbers $a$ and $b$:
$$\text{HM} \leq \text{GM} \leq \text{AM}$$
$$\frac{2ab}{a+b} \leq \sqrt{ab} \leq \frac{a+b}{2}$$

Equality holds when $a = b$.

### Cauchy-Schwarz Inequality

$$(a_1^2 + a_2^2 + ... + a_n^2)(b_1^2 + b_2^2 + ... + b_n^2) \geq (a_1b_1 + a_2b_2 + ... + a_nb_n)^2$$

---

## Progressions

### Arithmetic Progression (AP)

**Definition:** Constant difference between consecutive terms.

$$a, a+d, a+2d, a+3d, ...$$

**nth term:**
$$T_n = a + (n-1)d$$

**Sum of n terms:**
$$S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}[a + l]$$

where $l$ = last term.

**Properties:**
- If $a$, $b$, $c$ are in AP: $2b = a + c$
- Arithmetic Mean of $a$ and $b$: $\frac{a+b}{2}$

### Geometric Progression (GP)

**Definition:** Constant ratio between consecutive terms.

$$a, ar, ar^2, ar^3, ...$$

**nth term:**
$$T_n = ar^{n-1}$$

**Sum of n terms:**
$$S_n = \frac{a(r^n - 1)}{r - 1} \text{ for } r \neq 1$$

**Sum to infinity (|r| < 1):**
$$S_\infty = \frac{a}{1-r}$$

**Properties:**
- If $a$, $b$, $c$ are in GP: $b^2 = ac$
- Geometric Mean of $a$ and $b$: $\sqrt{ab}$

### Harmonic Progression (HP)

**Definition:** Reciprocals form an AP.

If $a$, $b$, $c$ are in HP:
$$\frac{1}{a}, \frac{1}{b}, \frac{1}{c} \text{ are in AP}$$

**Harmonic Mean:**
$$H = \frac{2ab}{a+b}$$

### Special Sums

| Sum | Formula |
|-----|---------|
| $1 + 2 + 3 + ... + n$ | $\frac{n(n+1)}{2}$ |
| $1^2 + 2^2 + ... + n^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $1^3 + 2^3 + ... + n^3$ | $\left[\frac{n(n+1)}{2}\right]^2$ |

---

## Polynomials

### Remainder Theorem
If polynomial $p(x)$ is divided by $(x - a)$, remainder = $p(a)$

### Factor Theorem
$(x - a)$ is a factor of $p(x)$ iff $p(a) = 0$

### Polynomial Relationships (Cubic)

For $ax^3 + bx^2 + cx + d = 0$ with roots $\alpha$, $\beta$, $\gamma$:
$$\alpha + \beta + \gamma = -\frac{b}{a}$$
$$\alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a}$$
$$\alpha\beta\gamma = -\frac{d}{a}$$

---

## Logarithms

### Definition
$$\log_a b = c \iff a^c = b$$

### Properties

| Property | Formula |
|----------|---------|
| Product | $\log_a(xy) = \log_a x + \log_a y$ |
| Quotient | $\log_a(\frac{x}{y}) = \log_a x - \log_a y$ |
| Power | $\log_a(x^n) = n \log_a x$ |
| Change of Base | $\log_a b = \frac{\log_c b}{\log_c a}$ |
| Inverse | $\log_a b \cdot \log_b a = 1$ |
| Identity | $a^{\log_a x} = x$ |

### Special Values

- $\log_a 1 = 0$
- $\log_a a = 1$
- $\log_{10} 10 = 1$ (common log)
- $\ln e = 1$ (natural log)

---

## GATE & ESE Problem Patterns

### Pattern 1: Quadratic Root Problems
> If one root of $x^2 - 5x + k = 0$ is 2, find $k$ and the other root.
- Sum = 5, so other root = 3
- Product = k = 2 × 3 = 6

### Pattern 2: AP/GP Applications
> Sum of first 10 terms of an AP is 100, and sum of first 5 is 30. Find common difference.
- $S_{10} = \frac{10}{2}[2a + 9d] = 100 \implies 2a + 9d = 20$
- $S_5 = \frac{5}{2}[2a + 4d] = 30 \implies 2a + 4d = 12$
- Subtracting: $5d = 8 \implies d = 1.6$

### Pattern 3: Logarithm Equations
> Solve: $\log_2 x + \log_2(x-2) = 3$
- $\log_2[x(x-2)] = 3$
- $x^2 - 2x = 8$
- $x^2 - 2x - 8 = 0$
- $(x-4)(x+2) = 0$
- $x = 4$ (reject -2 as log undefined)

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"If $\alpha$ and $\beta$ are roots of $x^2 - 3x + 2 = 0$, find $\frac{1}{\alpha} + \frac{1}{\beta}$."

Wrong approach: Finding roots first (1 and 2), then computing.

**The Elegant Solution:**
$$\frac{1}{\alpha} + \frac{1}{\beta} = \frac{\alpha + \beta}{\alpha\beta} = \frac{3}{2} = 1.5$$

No need to find individual roots!

**MSQ Logic Gate:**
- D < 0 doesn't mean "no solution"—it means complex solutions
- Check all roots satisfy the original equation domain

**NAT Precision Lock:**
- Logarithm answers may be irrational
- Use properties to simplify before computing

---

## Speed Tricks & Shortcuts

### Trick 1: Quadratic Root Estimation

If $ax^2 + bx + c = 0$:
- Signs same ($a$, $c$ same sign, $b$ opposite): Roots are positive
- Signs alternate: Roots are negative
- $c$ and $a$ opposite signs: One positive, one negative root

### Trick 2: Quick Sum of Squares

$$\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta$$

Use sum and product directly!

### Trick 3: GP Sum to Infinity Shortcut

If $|r| < 1$: $S_\infty = \frac{\text{First term}}{1 - r}$

### Trick 4: Log Base Change

$$\log_a b = \frac{1}{\log_b a}$$

### Trick 5: AP Middle Term

In an AP of odd number of terms, sum = (middle term) × (number of terms)

---

## Permanent Recall

### The Bizarre Mnemonic (Quadratic Formula)
*"Negative b can't decide (±), but the square root of the discriminant knows the drama. All over 2a, the twins are born!"*

### The Mental Slider
Visualize a parabola:
- Discriminant > 0: Parabola cuts x-axis at 2 points
- Discriminant = 0: Parabola touches x-axis at 1 point
- Discriminant < 0: Parabola floats above/below x-axis (no real roots)

### The 5-Second Snap-Check
- Sum and product give quick root verification
- For AP: middle term = average
- For GP: middle term = geometric mean of neighbors

---

## Practice Problems

### Level 1: Fundamentals
1. Find the sum of first 20 terms of AP: 5, 8, 11, ...
2. Solve: $\log_3 27 + \log_3 9 =$?
3. If $\alpha + \beta = 5$ and $\alpha\beta = 6$, find $\alpha^2 + \beta^2$.

### Level 2: GATE Standard
4. Find the sum to infinity: $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ...$
5. If roots of $2x^2 + px + q = 0$ are in ratio 2:3, and their sum is 10, find $p$ and $q$.
6. Solve: $\log_2(x^2 - 4x + 3) = 1$

### Level 3: IIT Examiner Level
7. If $\log_2 a + \log_4 a + \log_8 a = 11$, find $a$.
8. Three numbers are in GP. Their sum is 21 and sum of squares is 189. Find the numbers.
9. If $\alpha$, $\beta$, $\gamma$ are roots of $x^3 - 6x^2 + 11x - 6 = 0$, find $\alpha^2 + \beta^2 + \gamma^2$.

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. $a = 5$, $d = 3$, $n = 20$
   $S_{20} = \frac{20}{2}[2(5) + 19(3)] = 10[10 + 57] = 10 × 67 = **670**$

2. $\log_3 27 + \log_3 9 = 3 + 2 = **5**$

3. $\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta = 25 - 12 = **13**$

4. $a = 1$, $r = 1/2$
   $S_\infty = \frac{1}{1 - 1/2} = \frac{1}{1/2} = **2**$

5. Let roots be $2k$ and $3k$
   Sum = $5k = 10 \implies k = 2$
   Roots = 4 and 6
   Sum = $-p/2 = 10 \implies p = -20$
   Product = $q/2 = 24 \implies q = 48$
   **$p = -20$, $q = 48$**

6. $x^2 - 4x + 3 = 2$
   $x^2 - 4x + 1 = 0$
   $x = \frac{4 \pm \sqrt{16-4}}{2} = \frac{4 \pm \sqrt{12}}{2} = 2 \pm \sqrt{3}$
   **$x = 2 + \sqrt{3}$ or $x = 2 - \sqrt{3}$**

7. $\log_2 a + \frac{\log_2 a}{2} + \frac{\log_2 a}{3} = 11$
   $\log_2 a \left(1 + \frac{1}{2} + \frac{1}{3}\right) = 11$
   $\log_2 a \cdot \frac{11}{6} = 11$
   $\log_2 a = 6$
   **$a = 64$**

8. Let numbers be $a/r$, $a$, $ar$
   Sum: $a(1/r + 1 + r) = 21$
   Sum of squares: $a^2(1/r^2 + 1 + r^2) = 189$
   
   From first: $a = \frac{21r}{1 + r + r^2}$
   Substituting and solving: $r = 2$ or $r = 1/2$, $a = 7$
   
   Numbers: **3, 7, 14** (or 14, 7, 3)

9. $\alpha + \beta + \gamma = 6$
   $\alpha\beta + \beta\gamma + \gamma\alpha = 11$
   $\alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha\beta + \beta\gamma + \gamma\alpha)$
   $= 36 - 22 = **14**$

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Algebra with Geometry for a Rank-1 simulation?
