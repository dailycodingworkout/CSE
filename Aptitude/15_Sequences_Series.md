# Chapter 15: Sequences & Series

> **Patterns in numbers - understanding progression and summation**

---

## 🎯 Why Study This?

- High-frequency topic in GATE/ESE aptitude
- Foundation for understanding patterns and growth
- Essential for time-value calculations and analysis

---

## 📚 Part 1: Arithmetic Progression (AP)

### Definition

A sequence where each term differs from the previous by a constant (common difference).

```
a, a+d, a+2d, a+3d, ...

Where:
a = first term
d = common difference
```

---

### Key Formulas

**nth term**:
```
Tₙ = a + (n-1)d
```

**Sum of first n terms**:
```
Sₙ = (n/2)[2a + (n-1)d]
   = (n/2)[first term + last term]
   = (n/2)(a + l)  where l = last term
```

**Common difference**:
```
d = Tₙ - Tₙ₋₁
```

**Number of terms**:
```
n = (l - a)/d + 1
```

---

### Properties of AP

1. If a, b, c are in AP, then b - a = c - b, so **2b = a + c**
2. **Arithmetic Mean (AM)** of a and b = (a + b)/2
3. Sum of n terms from both ends is constant = a + l
4. Tₙ = Sₙ - Sₙ₋₁

---

### Important Results

**Sum of first n natural numbers**:
```
1 + 2 + 3 + ... + n = n(n+1)/2
```

**Sum of first n odd numbers**:
```
1 + 3 + 5 + ... + (2n-1) = n²
```

**Sum of first n even numbers**:
```
2 + 4 + 6 + ... + 2n = n(n+1)
```

---

## 📚 Part 2: Geometric Progression (GP)

### Definition

A sequence where each term is a constant multiple (common ratio) of the previous.

```
a, ar, ar², ar³, ...

Where:
a = first term
r = common ratio
```

---

### Key Formulas

**nth term**:
```
Tₙ = arⁿ⁻¹
```

**Sum of first n terms**:
```
Sₙ = a(rⁿ - 1)/(r - 1)    when r > 1
   = a(1 - rⁿ)/(1 - r)    when r < 1
   = na                    when r = 1
```

**Sum to infinity** (when |r| < 1):
```
S∞ = a/(1 - r)
```

**Common ratio**:
```
r = Tₙ/Tₙ₋₁
```

---

### Properties of GP

1. If a, b, c are in GP, then b/a = c/b, so **b² = ac**
2. **Geometric Mean (GM)** of a and b = √(ab)
3. Product of terms equidistant from ends = a × l (first × last)
4. In a finite GP: GM² = (first term) × (last term)

---

### Important Results

**Sum of powers of 2**:
```
1 + 2 + 4 + 8 + ... + 2ⁿ⁻¹ = 2ⁿ - 1
```

---

## 📚 Part 3: Harmonic Progression (HP)

### Definition

A sequence whose reciprocals form an AP.

```
If 1/a, 1/b, 1/c are in AP, then a, b, c are in HP
```

---

### Key Formulas

**nth term**:
```
Convert to AP (reciprocals), find nth term of AP, take reciprocal
```

**Harmonic Mean (HM)** of a and b:
```
HM = 2ab/(a + b)
```

---

### No Direct Sum Formula

For HP sum, convert each term, use AP sum concepts.

---

## 📚 Part 4: Special Series

### Sum of Squares

```
1² + 2² + 3² + ... + n² = n(n+1)(2n+1)/6
```

### Sum of Cubes

```
1³ + 2³ + 3³ + ... + n³ = [n(n+1)/2]² = (Σn)²
```

**💡 Amazing**: Sum of cubes = (Sum of numbers)²

---

### Arithmetic-Geometric Series (AGP)

When AP and GP are multiplied:
```
a, (a+d)r, (a+2d)r², ...
```

**Sum to infinity** (when |r| < 1):
```
S∞ = a/(1-r) + dr/(1-r)²
```

---

## 📊 Comparison: AM, GM, HM

For positive numbers a and b:
```
AM ≥ GM ≥ HM

Where:
AM = (a + b)/2
GM = √(ab)
HM = 2ab/(a + b)

Special relationship:
GM² = AM × HM
```

**Equality holds when a = b**

---

## 🔗 Key Relationships

### Three Means Relationship

```
GM² = AM × HM
```

### Inserting Means

**n Arithmetic Means between a and b**:
```
Common difference d = (b - a)/(n + 1)
Means: a + d, a + 2d, ..., a + nd
```

**n Geometric Means between a and b**:
```
Common ratio r = (b/a)^(1/(n+1))
Means: ar, ar², ..., arⁿ
```

---

## 💡 Advanced Tricks

### Trick 1: AP Sum = Middle Term × n

For AP with odd number of terms:
```
Sum = Middle term × Number of terms
```

---

### Trick 2: Quick GP Sum Check

For GP with r = 2:
```
Sum of n terms = 2ⁿ - 1 (when a = 1)
```

---

### Trick 3: Recognizing Sequences

Check consecutive terms:
- Constant difference → AP
- Constant ratio → GP
- Neither → Check if differences form AP (quadratic sequence)

---

### Trick 4: Sum of Series Using Patterns

**Example**: 1 + 11 + 111 + 1111 + ... (n terms)
```
= (1/9)[9 + 99 + 999 + ...]
= (1/9)[(10-1) + (100-1) + (1000-1) + ...]
= (1/9)[10 + 100 + 1000 + ... - n]
= (1/9)[(10^(n+1) - 10)/9 - n]
```

---

### Trick 5: Telescoping Series

When consecutive terms cancel:
```
Σ(1/(n(n+1))) = Σ(1/n - 1/(n+1)) = 1 - 1/(n+1) = n/(n+1)
```

---

## 📊 Method of Differences

For finding nth term when pattern isn't obvious:

1. Find first differences (T₂-T₁, T₃-T₂, ...)
2. If constant → AP
3. If not, find second differences
4. If constant → Quadratic expression

**Quadratic sequence** (second differences constant):
```
Tₙ = An² + Bn + C
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: GP with r = 1
```
Sₙ = na (not the standard formula)
Each term is just 'a'
```

### Trap 2: GP with |r| ≥ 1
```
Sum to infinity doesn't exist
Series diverges
```

### Trap 3: HP ≠ Reciprocal of AP Sum
```
Sum of HP ≠ 1/(Sum of corresponding AP)
Must sum individual HP terms
```

### Trap 4: Negative Common Difference
```
AP can have d < 0 (decreasing sequence)
Sₙ formula still works
```

### Trap 5: r < 0 in GP
```
Terms alternate signs
Sum formulas still apply, but series oscillates
```

---

## 🚀 Formula Cheat Sheet

| Series | nth Term | Sum of n Terms |
|--------|----------|----------------|
| AP | a + (n-1)d | (n/2)[2a + (n-1)d] |
| GP | arⁿ⁻¹ | a(rⁿ-1)/(r-1) |
| GP (infinite) | - | a/(1-r) for \|r\|<1 |
| Natural numbers | n | n(n+1)/2 |
| Squares | n² | n(n+1)(2n+1)/6 |
| Cubes | n³ | [n(n+1)/2]² |
| Odd numbers | 2n-1 | n² |

| Mean | Formula |
|------|---------|
| AM of a, b | (a+b)/2 |
| GM of a, b | √(ab) |
| HM of a, b | 2ab/(a+b) |
| GM² = AM × HM | Always true for positive numbers |

---

## 📝 GATE-Level Practice

**Q1**: Sum of first 20 terms of AP: 3, 7, 11, 15, ...
```
a = 3, d = 4, n = 20
S₂₀ = (20/2)[2(3) + 19(4)] = 10[6 + 76] = 820
```

**Q2**: Sum to infinity: 1 + 1/2 + 1/4 + 1/8 + ...
```
a = 1, r = 1/2
S∞ = 1/(1 - 1/2) = 2
```

**Q3**: If 3, x, 27 are in GP, find x.
```
x² = 3 × 27 = 81
x = 9 (or -9 if signs not restricted)
```

**Q4**: Find 1² + 2² + 3² + ... + 10².
```
= 10(11)(21)/6 = 2310/6 = 385
```

**Q5**: The AM of two numbers is 25 and GM is 20. Find the numbers.
```
(a + b)/2 = 25 → a + b = 50
√(ab) = 20 → ab = 400
Solving: a = 40, b = 10 (or vice versa)
```

**Q6**: Sum: 1/1.2 + 1/2.3 + 1/3.4 + ... + 1/9.10
```
= (1/1 - 1/2) + (1/2 - 1/3) + ... + (1/9 - 1/10)
= 1 - 1/10 = 9/10
```

---

*← [Chapter 14 - Logarithms](./14_Logarithms.md) | [Chapter 16 - Permutations & Combinations →](./16_Permutations_Combinations.md)*
