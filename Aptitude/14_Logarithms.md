# Chapter 14: Logarithms

> **The inverse of exponentiation - transforming multiplication into addition**

---

## 🎯 Why Study This?

- Simplifies complex exponential calculations
- Essential for engineering calculations and analysis
- GATE/ESE aptitude section includes logarithm problems

---

## 📚 Core Concept

**Definition**: If aˣ = N, then x = log_a(N)

```
log_a(N) = x  ⟺  aˣ = N

Where:
a = base (a > 0, a ≠ 1)
N = argument (N > 0)
x = logarithm
```

**💡 Analogy**: Logarithm answers "What power do I raise the base to, to get this number?"

```
log₂(8) = ? → "2 to what power gives 8?" → 2³ = 8 → Answer: 3
```

---

## 📊 Common Logarithms

### Natural Logarithm (ln)

Base e (e ≈ 2.718281828...)
```
ln(x) = log_e(x)
```

### Common Logarithm (log)

Base 10
```
log(x) = log₁₀(x)
```

**⚡ In most contexts**: "log" without base means log₁₀ (in engineering) or ln (in mathematics)

---

## 📐 Fundamental Properties

### Basic Identities

```
log_a(1) = 0           (because a⁰ = 1)
log_a(a) = 1           (because a¹ = a)
log_a(aˣ) = x          (inverse property)
a^(log_a(x)) = x       (inverse property)
```

---

### Product Rule

```
log_a(MN) = log_a(M) + log_a(N)
```

**💡 Multiplication → Addition**

---

### Quotient Rule

```
log_a(M/N) = log_a(M) - log_a(N)
```

**💡 Division → Subtraction**

---

### Power Rule

```
log_a(Mⁿ) = n × log_a(M)
```

**💡 Exponent comes out front as multiplier**

---

### Root Rule

```
log_a(ⁿ√M) = log_a(M)/n = (1/n) × log_a(M)
```

---

## 🔄 Change of Base Formula

```
log_a(N) = log_b(N) / log_b(a)

Or equivalently:
log_a(N) = ln(N) / ln(a) = log(N) / log(a)
```

**⚡ Super useful**: Converts any base to calculator-friendly base 10 or e

**Example**:
```
log₃(7) = log₁₀(7) / log₁₀(3) = 0.845 / 0.477 ≈ 1.77
```

---

## 🔗 Important Relationships

### Reciprocal Rule

```
log_a(b) = 1 / log_b(a)
```

### Chain Rule

```
log_a(b) × log_b(c) = log_a(c)
```

### Swap Base and Argument

```
log_a(b) × log_b(a) = 1
```

### Power in Base

```
log_(aⁿ)(M) = (1/n) × log_a(M)
```

---

## 📊 Standard Values (Memorize!)

| Value | log₁₀ | ln |
|-------|-------|-----|
| 1 | 0 | 0 |
| 2 | 0.301 | 0.693 |
| 3 | 0.477 | 1.099 |
| e | 0.434 | 1 |
| 5 | 0.699 | 1.609 |
| 7 | 0.845 | 1.946 |
| 10 | 1 | 2.303 |

**Derived**:
```
log(4) = 2 × log(2) = 0.602
log(5) = log(10/2) = 1 - 0.301 = 0.699
log(6) = log(2) + log(3) = 0.778
log(8) = 3 × log(2) = 0.903
log(9) = 2 × log(3) = 0.954
```

---

## 📐 Characteristic and Mantissa

For common logarithm (base 10):
```
log(N) = Characteristic + Mantissa

Characteristic = Integer part (can be negative)
Mantissa = Decimal part (always positive, 0 ≤ m < 1)
```

**Finding Characteristic**:
- For N ≥ 1: (number of digits - 1)
- For N < 1: -(number of zeros after decimal including leading zeros + 1)

**Examples**:
```
log(452.7) = 2 + mantissa  (3 digits, char = 2)
log(0.0045) = -3 + mantissa (3 zeros after decimal)
            = 3̄ + mantissa (written with bar)
```

---

## 📚 Standard Problem Types

### Type 1: Simplification

**Example**: Simplify log₂(8) + log₂(4)
```
= log₂(8 × 4) = log₂(32) = log₂(2⁵) = 5
OR: log₂(8) + log₂(4) = 3 + 2 = 5
```

---

### Type 2: Finding Values

**Example**: If log 2 = 0.301, find log 50
```
log 50 = log(100/2) = log 100 - log 2 = 2 - 0.301 = 1.699
```

---

### Type 3: Solving Logarithmic Equations

**Example**: Solve log₃(x) = 4
```
3⁴ = x
x = 81
```

**Example**: Solve log(x) + log(x-3) = 1
```
log[x(x-3)] = 1
x(x-3) = 10
x² - 3x - 10 = 0
(x-5)(x+2) = 0
x = 5 (valid) or x = -2 (invalid, x must > 3)
```

---

### Type 4: Finding Number of Digits

Number of digits in N = ⌊log₁₀(N)⌋ + 1

**Example**: How many digits in 2¹⁰⁰?
```
log₁₀(2¹⁰⁰) = 100 × log₁₀(2) = 100 × 0.301 = 30.1
Number of digits = ⌊30.1⌋ + 1 = 31 digits
```

---

### Type 5: Compound Problems

**Example**: Find value of log₂(log₃(log₄(64)))
```
Inner: log₄(64) = log₄(4³) = 3
Middle: log₃(3) = 1
Outer: log₂(1) = 0
Answer: 0
```

---

## 💡 Advanced Tricks

### Trick 1: Comparing Logarithms

For log_a(x) and log_b(x):
- If x > 1 and a > b > 1: log_a(x) < log_b(x)
- If x > 1 and 0 < a < b < 1: log_a(x) > log_b(x)

---

### Trick 2: Quick Mental Calculation

```
log₂(1024) = log₂(2¹⁰) = 10
log₃(243) = log₃(3⁵) = 5
log₁₀(10000) = log₁₀(10⁴) = 4
```

---

### Trick 3: Negative Argument Trick

```
log|x| when x can be negative
But log(x) itself undefined for x ≤ 0
```

---

### Trick 4: Log of Very Large/Small Numbers

```
log(a × 10ⁿ) = log(a) + n
log(a × 10⁻ⁿ) = log(a) - n
```

**Example**: log(3.5 × 10⁸) = log(3.5) + 8 ≈ 0.544 + 8 = 8.544

---

### Trick 5: Relationship with Exponentials

```
ln(eˣ) = x
e^(ln x) = x
10^(log x) = x
log(10ˣ) = x
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Domain Restrictions
```
log_a(x) is defined only for x > 0
Cannot take log of 0 or negative numbers (in real numbers)
```

### Trap 2: Base Restrictions
```
Base must be positive and ≠ 1
log₁(x) is undefined
log₀(x) is undefined
log₍₋₂₎(x) is undefined
```

### Trap 3: log(A + B) ≠ log(A) + log(B)
```
❌ log(A + B) = log A + log B
✅ log(A × B) = log A + log B
```

### Trap 4: log(Aⁿ) vs (log A)ⁿ
```
log(A²) = 2 log A
(log A)² ≠ 2 log A
```

### Trap 5: Checking Solutions
```
Always verify solutions in original equation
Logarithmic equations may yield extraneous solutions
```

---

## 🚀 Formula Cheat Sheet

| Rule | Formula |
|------|---------|
| Definition | log_a(N) = x ⟺ aˣ = N |
| Product | log(MN) = log M + log N |
| Quotient | log(M/N) = log M - log N |
| Power | log(Mⁿ) = n log M |
| Change of base | log_a(N) = log N / log a |
| Reciprocal | log_a(b) = 1/log_b(a) |
| log_a(1) | 0 |
| log_a(a) | 1 |
| Number of digits | ⌊log₁₀ N⌋ + 1 |

---

## 📝 GATE-Level Practice

**Q1**: Find log₈(128).
```
log₈(128) = log₈(2⁷) = 7 × log₈(2)
          = 7 × log₂(2)/log₂(8) = 7 × 1/3 = 7/3
OR: 8^x = 128, (2³)^x = 2⁷, x = 7/3
```

**Q2**: If log 2 = 0.301, log 3 = 0.477, find log 72.
```
72 = 8 × 9 = 2³ × 3²
log 72 = 3 log 2 + 2 log 3
       = 3(0.301) + 2(0.477)
       = 0.903 + 0.954 = 1.857
```

**Q3**: Solve log₂(x-1) + log₂(x+1) = 3.
```
log₂[(x-1)(x+1)] = 3
x² - 1 = 8
x² = 9
x = 3 (valid) or x = -3 (invalid)
```

**Q4**: Find the number of digits in 3⁵⁰. (Given log 3 = 0.477)
```
log(3⁵⁰) = 50 × 0.477 = 23.85
Digits = 23 + 1 = 24 digits
```

**Q5**: Simplify log₃(27) × log₉(81) × log₄(2).
```
log₃(27) = log₃(3³) = 3
log₉(81) = log₉(9²) = 2
log₄(2) = log₄(4^(1/2)) = 1/2
Product = 3 × 2 × 1/2 = 3
```

---

*← [Chapter 13 - Coordinate Geometry](./13_Coordinate_Geometry.md) | [Chapter 15 - Sequences & Series →](./15_Sequences_Series.md)*
