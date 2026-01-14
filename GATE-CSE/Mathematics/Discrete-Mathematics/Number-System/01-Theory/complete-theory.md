# Number System - Complete Theory for GATE 2026 CSE AIR 1

## 📑 Table of Contents

1. [Classifications of Numbers](#1-classifications-of-numbers)
2. [Natural Numbers](#2-natural-numbers)
3. [Whole Numbers](#3-whole-numbers)
4. [Even & Odd Numbers](#4-even--odd-numbers)
5. [Prime & Composite Numbers](#5-prime--composite-numbers)
6. [Test of Divisibility](#6-test-of-divisibility)
7. [HCF and LCM](#7-hcf-and-lcm)
8. [Algebraic Formulae](#8-algebraic-formulae)
9. [Factors and Trailing Zeros](#9-factors-and-trailing-zeros)
10. [Cyclicity and Remainder Theorem](#10-cyclicity-and-remainder-theorem)
11. [Base System](#11-base-system)

---

## 1. Classifications of Numbers

### 1.1 Complex Numbers (ℂ)
**Definition**: Numbers of the form a + bi, where a, b ∈ ℝ and i = √(-1)

**Properties**:
- **Real Part**: Re(z) = a
- **Imaginary Part**: Im(z) = b
- **Modulus**: |z| = √(a² + b²)
- **Conjugate**: z̄ = a - bi

**Operations**:
- Addition: (a + bi) + (c + di) = (a + c) + (b + d)i
- Multiplication: (a + bi)(c + di) = (ac - bd) + (ad + bc)i

### 1.2 Real Numbers (ℝ)
All numbers on the number line, including rational and irrational numbers.

#### 1.2.1 Rational Numbers (ℚ)
**Definition**: Numbers that can be expressed as p/q where p, q ∈ ℤ and q ≠ 0

**Types**:

**A. Terminating Decimals**
- Example: 1/4 = 0.25, 3/8 = 0.375
- **Condition**: Denominator has only factors of 2 and 5

**B. Non-terminating but Recurring Decimals**
- Example: 1/3 = 0.333..., 22/7 = 3.142857142857...
- **Pure Recurring**: 0.333... = 1/3
- **Mixed Recurring**: 0.1666... = 1/6

**C. Fractions**
- **Proper Fraction**: Numerator < Denominator (e.g., 3/5)
- **Improper Fraction**: Numerator ≥ Denominator (e.g., 7/5)
- **Mixed Fraction**: Whole number + Proper fraction (e.g., 2¾)

**Conversion Formulas**:
- Mixed to Improper: a(b/c) = (ac + b)/c
- Improper to Mixed: (p/q) = (p ÷ q) + (p mod q)/q

#### 1.2.2 Irrational Numbers
**Definition**: Numbers that cannot be expressed as a ratio of integers

**Types**:

**A. Surds**
- **Definition**: √n where n is not a perfect square
- **Examples**: √2, √3, √5, ∛7
- **Properties**:
  - √a × √b = √(ab)
  - √a / √b = √(a/b)
  - (√a)² = a

**B. Transcendental Numbers**
- **Definition**: Numbers that are not roots of any polynomial with integer coefficients
- **Examples**: π, e, sin(1°), log(2)

#### 1.2.3 Integers (ℤ)
**Definition**: {..., -3, -2, -1, 0, 1, 2, 3, ...}

**Classification**:
- **Negative Integers**: {..., -3, -2, -1}
- **Zero**: {0}
- **Positive Integers**: {1, 2, 3, ...}

---

## 2. Natural Numbers (ℕ)

**Definition**: {1, 2, 3, 4, ...} - Counting numbers

**Properties**:
1. **Closure**: a + b ∈ ℕ for all a, b ∈ ℕ
2. **Associativity**: (a + b) + c = a + (b + c)
3. **Commutativity**: a + b = b + a
4. **Well-Ordering**: Every non-empty subset has a smallest element

**Mathematical Induction**:
- **Base Case**: Prove P(1) is true
- **Inductive Step**: Prove P(k) ⟹ P(k+1)
- **Conclusion**: P(n) is true for all n ∈ ℕ

---

## 3. Whole Numbers

**Definition**: {0, 1, 2, 3, ...} = ℕ ∪ {0}

**Properties**:
- **Additive Identity**: 0 + a = a = a + 0
- **Multiplicative Identity**: 1 × a = a = a × 1
- **Multiplicative Property of Zero**: 0 × a = 0

---

## 4. Even & Odd Numbers

### 4.1 Definitions
- **Even**: Numbers divisible by 2 (2k where k ∈ ℤ)
- **Odd**: Numbers not divisible by 2 (2k + 1 where k ∈ ℤ)

### 4.2 Properties

**Addition**:
- Even + Even = Even
- Odd + Odd = Even
- Even + Odd = Odd

**Multiplication**:
- Even × Even = Even
- Even × Odd = Even
- Odd × Odd = Odd

**Powers**:
- Even^n = Even (for n ≥ 1)
- Odd^n = Odd (for all n)

**Key Theorems**:
1. **Sum of first n even numbers**: n(n + 1)
2. **Sum of first n odd numbers**: n²

---

## 5. Prime & Composite Numbers

### 5.1 Prime Numbers
**Definition**: Natural numbers greater than 1 with exactly two factors: 1 and itself

**First 25 Primes**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

**Properties**:
- Only even prime: 2
- All primes > 2 are odd
- Primes > 3 are of form 6k ± 1

### 5.2 Composite Numbers
**Definition**: Natural numbers > 1 that are not prime

**Properties**:
- Has more than two factors
- Can be factorized into prime factors
- Every composite number has a prime factor ≤ √n

### 5.3 Primality Testing Algorithms

**Trial Division Method**:
```
isPrime(n):
    if n ≤ 1: return false
    if n ≤ 3: return true
    if n % 2 = 0 or n % 3 = 0: return false
    for i = 5 to √n step 6:
        if n % i = 0 or n % (i+2) = 0:
            return false
    return true
```

**Sieve of Eratosthenes** (for finding all primes up to n):
```
sieve(n):
    prime = array[2..n] filled with true
    for p = 2 to √n:
        if prime[p]:
            for i = p² to n step p:
                prime[i] = false
    return all indices where prime[i] = true
```

**Advanced Tests**:
- **Fermat's Little Theorem**: If p is prime and gcd(a,p) = 1, then a^(p-1) ≡ 1 (mod p)
- **Miller-Rabin Test**: Probabilistic primality test
- **AKS Test**: Deterministic polynomial-time test

---

## 6. Test of Divisibility

### 6.1 Divisibility by 2
**Rule**: Last digit is even (0, 2, 4, 6, 8)
**Reason**: 10 ≡ 0 (mod 2)

### 6.2 Divisibility by 3
**Rule**: Sum of digits is divisible by 3
**Reason**: 10 ≡ 1 (mod 3), so 10^k ≡ 1 (mod 3)

### 6.3 Divisibility by 4
**Rule**: Last two digits form a number divisible by 4
**Reason**: 100 ≡ 0 (mod 4)

### 6.4 Divisibility by 5
**Rule**: Last digit is 0 or 5
**Reason**: 10 ≡ 0 (mod 5)

### 6.5 Divisibility by 6
**Rule**: Divisible by both 2 and 3
**Reason**: 6 = 2 × 3 and gcd(2,3) = 1

### 6.6 Divisibility by 8
**Rule**: Last three digits form a number divisible by 8
**Reason**: 1000 ≡ 0 (mod 8)

### 6.7 Divisibility by 9
**Rule**: Sum of digits is divisible by 9
**Reason**: 10 ≡ 1 (mod 9), so 10^k ≡ 1 (mod 9)

### 6.8 Divisibility by 10
**Rule**: Last digit is 0
**Reason**: Direct consequence of decimal system

### 6.9 Divisibility by 11
**Rule**: Alternating sum of digits is divisible by 11
**Example**: 1331 → 1 - 3 + 3 - 1 = 0, divisible by 11
**Reason**: 10 ≡ -1 (mod 11), so 10^k ≡ (-1)^k (mod 11)

---

## 7. HCF and LCM

### 7.1 Highest Common Factor (HCF/GCD)
**Definition**: Largest positive integer that divides all given numbers

**Euclidean Algorithm**:
```
gcd(a, b):
    while b ≠ 0:
        temp = b
        b = a mod b
        a = temp
    return a
```

**Extended Euclidean Algorithm**:
Finds integers x, y such that ax + by = gcd(a, b)

### 7.2 Least Common Multiple (LCM)
**Definition**: Smallest positive integer divisible by all given numbers

**Formula**: LCM(a, b) = |ab| / GCD(a, b)

**For multiple numbers**: LCM(a, b, c) = LCM(LCM(a, b), c)

### 7.3 Properties
1. **HCF × LCM = Product of numbers** (for two numbers)
2. **HCF(a, b) ≤ min(a, b)**
3. **LCM(a, b) ≥ max(a, b)**
4. **If gcd(a, b) = 1, then LCM(a, b) = ab**

### 7.4 LCM and HCF of Fractions
**For fractions a/b and c/d**:
- **HCF = HCF(a, c) / LCM(b, d)**
- **LCM = LCM(a, c) / HCF(b, d)**

---

## 8. Important Algebraic Formulae

### 8.1 Basic Identities
1. **(a + b)² = a² + 2ab + b²**
2. **(a - b)² = a² - 2ab + b²**
3. **a² - b² = (a + b)(a - b)**
4. **(a + b)³ = a³ + 3a²b + 3ab² + b³**
5. **(a - b)³ = a³ - 3a²b + 3ab² - b³**
6. **a³ + b³ = (a + b)(a² - ab + b²)**
7. **a³ - b³ = (a - b)(a² + ab + b²)**

### 8.2 Higher Order Identities
1. **(a + b + c)² = a² + b² + c² + 2(ab + bc + ca)**
2. **a³ + b³ + c³ - 3abc = (a + b + c)(a² + b² + c² - ab - bc - ca)**
3. **If a + b + c = 0, then a³ + b³ + c³ = 3abc**

### 8.3 Condition of Divisibility for Algebraic Functions
**For polynomial P(x)**:
- **P(x) is divisible by (x - a) ⟺ P(a) = 0**
- **P(x) is divisible by (x + a) ⟺ P(-a) = 0**
- **Factor Theorem**: If P(a) = 0, then (x - a) is a factor of P(x)

---

## 9. Factors and Trailing Zeros

### 9.1 Finding Number of Factors
**For n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ**:
- **Number of factors = (a₁ + 1)(a₂ + 1)...(aₖ + 1)**
- **Sum of factors = [(p₁^(a₁+1) - 1)/(p₁ - 1)] × ... × [(pₖ^(aₖ+1) - 1)/(pₖ - 1)]**

### 9.2 Counting Trailing Zeros
**In n!**: Count the number of times 10 divides n!
**Formula**: ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...

**Reasoning**: Trailing zeros come from factors of 10 = 2 × 5. Since there are more factors of 2 than 5 in n!, we count factors of 5.

---

## 10. Cyclicity and Remainder Theorem

### 10.1 Cyclicity of Unit Digits
**Pattern of last digits for powers**:
- **2**: 2, 4, 8, 6, 2, 4, 8, 6, ... (cycle of 4)
- **3**: 3, 9, 7, 1, 3, 9, 7, 1, ... (cycle of 4)
- **4**: 4, 6, 4, 6, ... (cycle of 2)
- **5**: 5, 5, 5, ... (cycle of 1)
- **6**: 6, 6, 6, ... (cycle of 1)
- **7**: 7, 9, 3, 1, 7, 9, 3, 1, ... (cycle of 4)
- **8**: 8, 4, 2, 6, 8, 4, 2, 6, ... (cycle of 4)
- **9**: 9, 1, 9, 1, ... (cycle of 2)

### 10.2 Remainder Theorem
**Statement**: When polynomial P(x) is divided by (x - a), the remainder is P(a)

**Applications**:
- **Finding remainders of large numbers**
- **Factorization of polynomials**
- **Solving modular arithmetic problems**

### 10.3 Chinese Remainder Theorem
**For system**:
- x ≡ a₁ (mod m₁)
- x ≡ a₂ (mod m₂)
- ...
- x ≡ aₖ (mod mₖ)

**Solution exists and is unique modulo M = m₁m₂...mₖ** if gcd(mᵢ, mⱼ) = 1 for i ≠ j

---

## 11. Base System

### 11.1 Converting from Any Base to Decimal

**Method**: Positional notation
**For number (dₙdₙ₋₁...d₁d₀)ᵦ**:
**Decimal value = dₙ × b^n + dₙ₋₁ × b^(n-1) + ... + d₁ × b¹ + d₀ × b⁰**

**Example**: (1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀

### 11.2 Converting from Decimal to Any Base

**Method**: Repeated division
```
convertToBase(decimal_num, base):
    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = remainder + result
        decimal_num = decimal_num // base
    return result
```

**Example**: Convert 13₁₀ to binary
- 13 ÷ 2 = 6 remainder 1
- 6 ÷ 2 = 3 remainder 0  
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1
- **Result**: (1101)₂

### 11.3 Base Conversion Shortcuts

**Binary ⟷ Octal**:
- Group binary digits in sets of 3 from right
- Each group represents one octal digit

**Binary ⟷ Hexadecimal**:
- Group binary digits in sets of 4 from right
- Each group represents one hex digit

**Common Bases**:
- **Binary (Base 2)**: 0, 1
- **Octal (Base 8)**: 0, 1, 2, 3, 4, 5, 6, 7
- **Decimal (Base 10)**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Hexadecimal (Base 16)**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

---

## 🎯 Key Theorems for GATE

1. **Fundamental Theorem of Arithmetic**: Every integer > 1 is either prime or can be uniquely factorized into primes
2. **Euclid's Theorem**: There are infinitely many primes
3. **Fermat's Little Theorem**: If p is prime and p ∤ a, then a^(p-1) ≡ 1 (mod p)
4. **Wilson's Theorem**: (p-1)! ≡ -1 (mod p) if and only if p is prime
5. **Bertrand's Postulate**: For n > 1, there exists a prime p such that n < p < 2n

---

## 📝 Summary Checklist

- [ ] Understand number classifications and their properties
- [ ] Master divisibility rules and their proofs
- [ ] Practice HCF/LCM calculations and applications
- [ ] Memorize important algebraic identities
- [ ] Learn factor counting and trailing zero formulas
- [ ] Understand cyclicity patterns and remainder calculations
- [ ] Master base conversion techniques
- [ ] Practice primality testing algorithms
- [ ] Apply theorems in problem-solving contexts

**Next**: [Tips and Tricks](../02-Tips-and-Tricks/)