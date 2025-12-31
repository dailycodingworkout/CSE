# Chapter 9: Algebra

> **The language of mathematics - solving the unknown through structured relationships**

---

## 🎯 Why Study This?

- Foundation for all mathematical problem-solving
- GATE/ESE tests algebraic manipulation heavily
- Essential for understanding functions, equations, and optimization

---

## 📚 Part 1: Equations

### Linear Equations (Degree 1)

**Single Variable**: ax + b = 0
```
Solution: x = -b/a
```

**Two Variables**: a₁x + b₁y = c₁ and a₂x + b₂y = c₂
```
Consistent (unique solution): a₁/a₂ ≠ b₁/b₂
Infinite solutions: a₁/a₂ = b₁/b₂ = c₁/c₂
No solution (parallel): a₁/a₂ = b₁/b₂ ≠ c₁/c₂
```

**Solving Methods**:
- Substitution
- Elimination
- Cross-multiplication: x/(b₁c₂-b₂c₁) = y/(c₁a₂-c₂a₁) = 1/(a₁b₂-a₂b₁)
- Matrix method (Cramer's Rule)

---

### Quadratic Equations (Degree 2)

**Standard Form**: ax² + bx + c = 0

**Quadratic Formula**:
```
x = (-b ± √(b² - 4ac)) / 2a
```

**Discriminant (D = b² - 4ac)**:
| D Value | Nature of Roots |
|---------|-----------------|
| D > 0 | Two distinct real roots |
| D = 0 | Two equal real roots |
| D < 0 | Two complex conjugate roots |
| D = perfect square | Rational roots |

---

### Vieta's Formulas (Sum/Product of Roots)

For ax² + bx + c = 0 with roots α, β:
```
Sum of roots: α + β = -b/a
Product of roots: αβ = c/a
```

**⚡ Useful Derived Relations**:
```
α² + β² = (α+β)² - 2αβ
α³ + β³ = (α+β)³ - 3αβ(α+β)
|α - β| = √D / |a|
1/α + 1/β = (α+β)/αβ = -b/c
```

---

### Forming Equations from Roots

Equation with roots α, β:
```
x² - (α+β)x + αβ = 0
```

**Example**: Roots are 3 and -2
```
Sum = 1, Product = -6
Equation: x² - x - 6 = 0
```

---

### Higher Degree Equations

**Cubic**: ax³ + bx² + cx + d = 0 (roots α, β, γ)
```
α + β + γ = -b/a
αβ + βγ + γα = c/a
αβγ = -d/a
```

**Quartic**: Similar pattern continues

---

## 📚 Part 2: Inequalities

### Linear Inequalities

**Rules**:
- Adding/subtracting same number: Inequality preserved
- Multiplying/dividing by positive: Inequality preserved
- Multiplying/dividing by negative: **Inequality reverses**

```
2x - 5 < 7
2x < 12
x < 6
```

---

### Quadratic Inequalities

**Method**: 
1. Find roots of equality
2. Test intervals between roots
3. Determine where inequality holds

**For (x-a)(x-b) > 0** (a < b):
```
Solution: x < a OR x > b
```

**For (x-a)(x-b) < 0** (a < b):
```
Solution: a < x < b
```

**⚡ Trick**: 
- For product > 0: Same signs (both intervals outside roots)
- For product < 0: Opposite signs (interval between roots)

---

### Modulus/Absolute Value

```
|x| = x if x ≥ 0
    = -x if x < 0
```

**Key Inequalities**:
```
|x| < a ⟺ -a < x < a
|x| > a ⟺ x < -a OR x > a
|x + y| ≤ |x| + |y| (Triangle inequality)
||x| - |y|| ≤ |x - y|
```

---

### AM-GM-HM Inequality

For positive numbers a₁, a₂, ..., aₙ:
```
AM ≥ GM ≥ HM

(a₁+a₂+...+aₙ)/n ≥ ⁿ√(a₁×a₂×...×aₙ) ≥ n/(1/a₁+1/a₂+...+1/aₙ)
```

Equality holds when a₁ = a₂ = ... = aₙ

**Application**: Finding minimum of sum when product is fixed (or vice versa)

---

## 📚 Part 3: Polynomials

### Polynomial Division

```
Dividend = Divisor × Quotient + Remainder
P(x) = D(x) × Q(x) + R(x)
```

**Remainder Theorem**:
When P(x) is divided by (x-a), remainder = P(a)

**Factor Theorem**:
(x-a) is a factor of P(x) iff P(a) = 0

---

### Factoring Techniques

**Common Identities** (Memorize!):
```
a² - b² = (a+b)(a-b)
a² + 2ab + b² = (a+b)²
a² - 2ab + b² = (a-b)²
a³ + b³ = (a+b)(a² - ab + b²)
a³ - b³ = (a-b)(a² + ab + b²)
a³ + b³ + c³ - 3abc = (a+b+c)(a² + b² + c² - ab - bc - ca)
(a+b+c)² = a² + b² + c² + 2(ab + bc + ca)
(a+b+c)³ = a³ + b³ + c³ + 3(a+b)(b+c)(c+a)
```

**⚡ Special**: If a + b + c = 0, then a³ + b³ + c³ = 3abc

---

## 📚 Part 4: Functions

### Types of Functions

| Type | Definition | Example |
|------|------------|---------|
| One-to-one (Injective) | f(a) = f(b) ⟹ a = b | f(x) = 2x |
| Onto (Surjective) | Every y has a pre-image | f(x) = x³ (R→R) |
| Bijective | Both one-to-one and onto | f(x) = 2x+1 |
| Even | f(-x) = f(x) | f(x) = x² |
| Odd | f(-x) = -f(x) | f(x) = x³ |

---

### Domain and Range

**Domain**: All valid input values
**Range**: All possible output values

**Common Restrictions**:
```
√(expression) : expression ≥ 0
1/(expression) : expression ≠ 0
log(expression) : expression > 0
```

---

### Composite Functions

```
(f ∘ g)(x) = f(g(x))
(g ∘ f)(x) = g(f(x))
```

**⚠️ Generally**: f ∘ g ≠ g ∘ f

---

### Inverse Functions

If f(x) = y, then f⁻¹(y) = x

**Finding Inverse**:
1. Write y = f(x)
2. Solve for x in terms of y
3. Replace x with f⁻¹(y)

**Properties**:
```
f(f⁻¹(x)) = x
f⁻¹(f(x)) = x
(f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹
```

---

## 📚 Part 5: Exponents & Surds

### Laws of Exponents

```
aᵐ × aⁿ = aᵐ⁺ⁿ
aᵐ / aⁿ = aᵐ⁻ⁿ
(aᵐ)ⁿ = aᵐⁿ
(ab)ⁿ = aⁿbⁿ
a⁰ = 1 (a ≠ 0)
a⁻ⁿ = 1/aⁿ
a^(m/n) = ⁿ√(aᵐ)
```

---

### Surds (Irrational Roots)

**Rationalizing**:
```
a/(√b + √c) = a(√b - √c)/(b - c)
1/(√a + √b) = (√a - √b)/(a - b)
```

**Conjugate Surds**: √a + √b and √a - √b

---

## 💡 Advanced Tricks

### Trick 1: Symmetric Functions of Roots

If you need α² + β² but only know α + β and αβ:
```
α² + β² = (α + β)² - 2αβ
```

---

### Trick 2: Sign Analysis for Inequalities

```
For (x-a)(x-b)(x-c) where a < b < c:
Check intervals: (-∞,a), (a,b), (b,c), (c,∞)
Signs alternate starting from rightmost
```

---

### Trick 3: Completing the Square

```
ax² + bx + c = a[(x + b/2a)² - (b²-4ac)/4a²]
              = a(x + b/2a)² - (b²-4ac)/4a
```

Minimum value of ax² + bx + c (for a > 0) = c - b²/4a

---

### Trick 4: Maxima/Minima Using AM-GM

**Example**: Minimize x + 1/x for x > 0
```
By AM-GM: (x + 1/x)/2 ≥ √(x × 1/x) = 1
So x + 1/x ≥ 2
Minimum = 2 at x = 1
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Division by Variable
```
Don't divide by x unless you know x ≠ 0
You might lose solutions
```

### Trap 2: Squaring Both Sides
```
May introduce extraneous solutions
Always verify answers in original equation
```

### Trap 3: Domain Restrictions
```
√(x²) = |x|, not x
Log and exp have restricted domains
```

### Trap 4: Inequality Direction
```
Multiplying by negative reverses inequality
1/x < 1/y doesn't imply x > y (check signs!)
```

### Edge Case: Complex Roots
```
Complex roots come in conjugate pairs
If 2+3i is a root, 2-3i is also a root (for real coefficients)
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Quadratic roots | (-b ± √(b²-4ac))/2a |
| Sum of roots | -b/a |
| Product of roots | c/a |
| Discriminant | b² - 4ac |
| AM ≥ GM | (a+b)/2 ≥ √(ab) |
| (a+b)² | a² + 2ab + b² |
| a³ + b³ | (a+b)(a² - ab + b²) |
| Remainder theorem | P(x)/(x-a) remainder = P(a) |
| Min of ax²+bx+c | (4ac-b²)/4a |

---

## 📝 GATE-Level Practice

**Q1**: If α, β are roots of x² - 5x + 6 = 0, find α³ + β³.
```
α + β = 5, αβ = 6
α³ + β³ = (α+β)³ - 3αβ(α+β) = 125 - 3(6)(5) = 125 - 90 = 35
```

**Q2**: Solve x² - 5|x| + 6 = 0
```
Let |x| = y, y ≥ 0
y² - 5y + 6 = 0
y = 2 or y = 3
x = ±2 or ±3
```

**Q3**: Find minimum value of x² + 4x + 8.
```
= (x+2)² + 4
Minimum = 4 at x = -2
OR using formula: (4×8 - 16)/4 = 16/4 = 4
```

**Q4**: If f(x) = 2x + 3, find f⁻¹(x).
```
y = 2x + 3
x = (y-3)/2
f⁻¹(x) = (x-3)/2
```

**Q5**: For what values of k does x² + 2x + k = 0 have equal roots?
```
D = 0 for equal roots
4 - 4k = 0
k = 1
```

---

*← [Chapter 8 - Time, Speed & Distance](./08_Time_Speed_Distance.md) | [Chapter 10 - Geometry →](./10_Geometry.md)*
