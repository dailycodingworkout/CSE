# Number System - Complete Study Material for GATE & ESE

> 🎯 **Goal**: Master every concept with minimal effort, maximum retention.

---

## Table of Contents
1. [Classification of Numbers](#1-classification-of-numbers)
2. [Number Representations (Base Systems)](#2-number-representations-base-systems)
3. [Divisibility Rules](#3-divisibility-rules)
4. [HCF & LCM](#4-hcf--lcm)
5. [Prime Numbers & Factorization](#5-prime-numbers--factorization)
6. [Factors - Count, Sum & Product](#6-factors---count-sum--product)
7. [Remainder Theorems](#7-remainder-theorems)
8. [Unit Digit & Cyclicity](#8-unit-digit--cyclicity)
9. [Base Conversions](#9-base-conversions)
10. [Special Numbers & Patterns](#10-special-numbers--patterns)
11. [Word Problems Framework](#11-word-problems-framework)
12. [GATE/ESE Specific Tips](#12-gateese-specific-tips)

---

## 1. Classification of Numbers

### Hierarchy (Memory Map)
```
Complex (a + bi)
    └── Real
           ├── Rational (p/q, q≠0)
           │      ├── Integers (...-2,-1,0,1,2...)
           │      │      ├── Whole (0,1,2,3...)
           │      │      │      └── Natural (1,2,3...)
           │      │      └── Negative Integers (-1,-2,-3...)
           │      └── Fractions (proper, improper)
           └── Irrational (√2, π, e)
```

### Quick Reference

| Type | Definition | Examples | Key Property |
|------|------------|----------|--------------|
| **Natural (ℕ)** | Counting numbers | 1, 2, 3, ... | Closed under +, × |
| **Whole (W)** | Natural + 0 | 0, 1, 2, 3, ... | Smallest: 0 |
| **Integers (ℤ)** | Whole + negatives | ...-2, -1, 0, 1, 2... | Closed under +, -, × |
| **Rational (ℚ)** | p/q where q≠0, p,q∈ℤ | 1/2, -3/4, 5, 0.333... | Terminating or repeating decimals |
| **Irrational** | Non-repeating, non-terminating | √2, π, e | Cannot be expressed as p/q |
| **Real (ℝ)** | Rational ∪ Irrational | All above | Covers number line |
| **Complex (ℂ)** | a + bi, where i = √(-1) | 3+4i, -2i | i² = -1 |

### 🧠 Tricks & Insights

**Trick 1: Is it Rational?**
- Decimal terminates → Rational (0.25 = 1/4) ✓
- Decimal repeats → Rational (0.333... = 1/3) ✓
- Decimal non-repeating, non-terminating → Irrational (π = 3.14159...) ✓

**Trick 2: Converting Repeating Decimals to Fractions**
```
0.x̄ = x/9          → 0.7̄ = 7/9
0.x̄ȳ = xy/99       → 0.2̄3̄ = 23/99
0.xȳz̄ = (xyz-x)/990 → 0.12̄3̄ = (123-1)/990 = 122/990
```

**Formula**: For 0.abc...x̄ȳz̄ (n non-repeating, m repeating digits):
```
Fraction = (Full number - Non-repeating part) / (m 9's followed by n 0's)
```

### ⚠️ Edge Cases
- 0 is a whole number but NOT natural (in standard GATE definition)
- Every integer is rational (5 = 5/1)
- √4 = 2 is rational, not irrational (perfect squares under √ are rational)
- π/π = 1 is rational (irrational ÷ same irrational can be rational)

---

## 2. Number Representations (Base Systems)

### Base System Basics

| Base | Name | Digits Used | Example |
|------|------|-------------|---------|
| 2 | Binary | 0, 1 | (1101)₂ |
| 8 | Octal | 0-7 | (75)₈ |
| 10 | Decimal | 0-9 | (255)₁₀ |
| 16 | Hexadecimal | 0-9, A-F | (FF)₁₆ |

### 🔄 Conversion Table (Memorize This!)

| Decimal | Binary | Octal | Hex |
|---------|--------|-------|-----|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

### Conversion Shortcuts

#### Binary ↔ Octal (Group of 3 bits)
```
Binary: 110 101 011
Octal:   6   5   3  → (653)₈

Reverse: (47)₈ → 100 111 → (100111)₂
```

#### Binary ↔ Hexadecimal (Group of 4 bits)
```
Binary: 1010 1111 0011
Hex:      A    F    3  → (AF3)₁₆
```

#### Any Base to Decimal
```
(1101)₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8+4+0+1 = 13

(2F)₁₆ = 2×16¹ + 15×16⁰ = 32+15 = 47
```

#### Decimal to Any Base (Repeated Division)
```
Convert 25 to binary:
25 ÷ 2 = 12 R 1
12 ÷ 2 = 6  R 0
6  ÷ 2 = 3  R 0
3  ÷ 2 = 1  R 1
1  ÷ 2 = 0  R 1
Read bottom to top: (11001)₂
```

### 🧠 Tricks

**Trick 1: Quick Binary to Decimal (for small numbers)**
```
Powers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
Position:    0  1  2  3   4   5   6    7    8    9    10
```

**Trick 2: Count of n-digit numbers in base b**
- Smallest n-digit: b^(n-1)
- Largest n-digit: b^n - 1
- Total n-digit numbers: b^n - b^(n-1) = b^(n-1) × (b-1)

**Trick 3: Number of digits of N in base b**
```
Digits = ⌊log_b(N)⌋ + 1
```

### ⚠️ Edge Cases
- Leading zeros don't count: (007)₈ = (7)₈
- In base b, largest single digit is (b-1)
- (10)_b = b in decimal for any base b

---

## 3. Divisibility Rules

### Complete Divisibility Table

| Divisor | Rule | Example |
|---------|------|---------|
| **2** | Last digit even (0,2,4,6,8) | 1234 ✓ (4 is even) |
| **3** | Sum of digits divisible by 3 | 123 → 1+2+3=6 ✓ |
| **4** | Last 2 digits ÷ 4 | 1324 → 24÷4 ✓ |
| **5** | Last digit 0 or 5 | 125 ✓ |
| **6** | Divisible by both 2 and 3 | 324 ✓ |
| **7** | Double last digit, subtract from rest | 343 → 34-6=28 ✓ |
| **8** | Last 3 digits ÷ 8 | 1016 → 016÷8 ✓ |
| **9** | Sum of digits ÷ 9 | 729 → 7+2+9=18 ✓ |
| **10** | Last digit 0 | 1230 ✓ |
| **11** | (Sum odd positions) - (Sum even positions) ÷ 11 | 1364 → (1+6)-(3+4)=0 ✓ |
| **12** | Divisible by both 3 and 4 | 144 ✓ |
| **13** | Add 4× last digit to rest | 247 → 24+28=52 → 5+8=13 ✓ |
| **25** | Last 2 digits ÷ 25 | 175 → 75÷25 ✓ |
| **125** | Last 3 digits ÷ 125 | 2625 → 625÷125 ✓ |

### 🧠 Tricks

**Pattern Recognition:**
- 2, 4, 8, 16... → Check last 1, 2, 3, 4... digits (powers of 2)
- 5, 25, 125... → Check last 1, 2, 3... digits (powers of 5)

**Divisibility by 7 (Alternative Method):**
```
Multiply digits by pattern: 1, 3, 2, 6, 4, 5 (repeating from right)
If sum ÷ 7, number ÷ 7

Example: 1862 → 2×1 + 6×3 + 8×2 + 1×6 = 2+18+16+6 = 42 ÷ 7 ✓
```

### Osculator Method (For primes like 7, 11, 13, 17, 19...)

| Divisor | Osculator | Operation |
|---------|-----------|-----------|
| 7 | -2 | Subtract 2× last digit |
| 11 | -1 | Subtract last digit |
| 13 | +4 | Add 4× last digit |
| 17 | -5 | Subtract 5× last digit |
| 19 | +2 | Add 2× last digit |
| 23 | +7 | Add 7× last digit |

---

## 4. HCF & LCM

### Definitions
- **HCF (GCD)**: Largest number that divides all given numbers
- **LCM**: Smallest number divisible by all given numbers

### Methods to Find HCF

#### Method 1: Prime Factorization
```
HCF(48, 72) 
48 = 2⁴ × 3
72 = 2³ × 3²
HCF = 2³ × 3 = 24 (Take MIN power of common primes)
```

#### Method 2: Division Method (Euclidean Algorithm)
```
HCF(48, 72):
72 = 48 × 1 + 24
48 = 24 × 2 + 0
HCF = 24 (last non-zero remainder)
```

#### Method 3: Subtraction Method
```
HCF(48, 72):
72 - 48 = 24
48 - 24 = 24
24 - 24 = 0
HCF = 24
```

### Methods to Find LCM

#### Method 1: Prime Factorization
```
LCM(48, 72)
48 = 2⁴ × 3
72 = 2³ × 3²
LCM = 2⁴ × 3² = 144 (Take MAX power of all primes)
```

#### Method 2: Using HCF
```
LCM × HCF = Product of numbers
LCM(48, 72) = (48 × 72) / 24 = 144
```

### 🧠 Critical Formulas

```
For two numbers a, b:
• HCF(a,b) × LCM(a,b) = a × b
• LCM = (a × b) / HCF

For three numbers a, b, c:
• HCF(a,b,c) = HCF(HCF(a,b), c)
• LCM(a,b,c) = LCM(LCM(a,b), c)
• HCF × LCM ≠ a × b × c (This formula ONLY works for 2 numbers!)
```

### Properties Table

| Property | HCF | LCM |
|----------|-----|-----|
| Always divides | All numbers | - |
| Always divisible by | - | All numbers |
| For co-prime numbers | 1 | Product |
| HCF ≤ | Smallest number | - |
| LCM ≥ | - | Largest number |
| Relationship | HCF(a,b) divides a-b | LCM(a,b) is multiple of both |

### 🧠 Tricks

**Trick 1: HCF of Fractions**
```
HCF(a/b, c/d) = HCF(a,c) / LCM(b,d)
```

**Trick 2: LCM of Fractions**
```
LCM(a/b, c/d) = LCM(a,c) / HCF(b,d)
```

**Trick 3: For consecutive numbers**
```
HCF(n, n+1) = 1 (Always co-prime)
LCM(n, n+1) = n(n+1)
```

**Trick 4: Quick HCF Pattern**
```
HCF(a, b) = HCF(a-b, b) when a > b
HCF(a, b) = HCF(a, b mod a)
```

### Application Problems

**Type 1: Finding Largest Tile Size**
- Find HCF of dimensions

**Type 2: Finding Shortest Time for Meeting**
- Find LCM of individual times

**Type 3: Bells Ringing Together**
- Find LCM of intervals

### ⚠️ Edge Cases
- HCF(0, n) = n
- LCM(0, n) = 0
- HCF(a, a) = a
- LCM(a, a) = a

---

## 5. Prime Numbers & Factorization

### Definition
- **Prime**: Number with exactly 2 factors (1 and itself)
- **Composite**: More than 2 factors
- **1**: Neither prime nor composite (exactly 1 factor)

### First 25 Primes (Memorize!)
```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```
**Count**: 25 primes ≤ 100

### 🧠 Prime Testing Algorithm

**To check if N is prime, test divisibility by primes up to √N**

```
Is 97 prime?
√97 ≈ 9.8
Test: 2, 3, 5, 7 (primes ≤ 9)
97/2 ✗, 97/3 ✗, 97/5 ✗, 97/7 ✗
∴ 97 is prime
```

### Special Prime Types

| Type | Definition | Examples |
|------|------------|----------|
| **Twin Primes** | Differ by 2 | (3,5), (5,7), (11,13), (17,19) |
| **Co-Primes** | HCF = 1 | (4,9), (8,15) |
| **Mersenne Primes** | 2ⁿ - 1 | 3, 7, 31, 127 |
| **Fermat Primes** | 2^(2ⁿ) + 1 | 3, 5, 17, 257 |
| **Sophie Germain** | p and 2p+1 both prime | 2, 3, 5, 11, 23 |

### Prime Factorization

#### Unique Factorization Theorem
Every integer > 1 can be uniquely expressed as product of primes.

```
360 = 2³ × 3² × 5

Factor Tree:
    360
   /    \
  2      180
        /    \
       2      90
             /  \
            2    45
                /  \
               3    15
                   /  \
                  3    5
```

### Wilson's Theorem
**If p is prime, then (p-1)! ≡ -1 (mod p)**

```
Example: (4)! mod 5 = 24 mod 5 = 4 ≡ -1 (mod 5) ✓
```

### Fermat's Little Theorem
**If p is prime and gcd(a,p) = 1, then a^(p-1) ≡ 1 (mod p)**

```
Example: 2⁴ mod 5 = 16 mod 5 = 1 ✓
```

### 🧠 Tricks

**Trick 1: Quick Prime Check for 2-digit numbers**
- If ends in 0, 2, 4, 5, 6, 8 → NOT prime (except 2, 5)
- If digit sum ÷ 3 → NOT prime (except 3)

**Trick 2: Count of Primes (Prime Counting Function π(n))**
```
π(10) = 4    (2,3,5,7)
π(100) = 25
π(1000) = 168
Approximation: π(n) ≈ n/ln(n)
```

**Trick 3: Goldbach's Conjecture**
Every even number > 2 can be expressed as sum of two primes.
```
4 = 2+2, 6 = 3+3, 8 = 3+5, 10 = 5+5 = 3+7
```

---

## 6. Factors - Count, Sum & Product

### For N = p₁^a × p₂^b × p₃^c

| Property | Formula | Example: 72 = 2³ × 3² |
|----------|---------|------------------------|
| **Number of factors** | (a+1)(b+1)(c+1) | (3+1)(2+1) = 12 |
| **Sum of factors** | [(p₁^(a+1)-1)/(p₁-1)] × ... | [(16-1)/1]×[(9-1)/2] = 15×4 = 195 |
| **Product of factors** | N^(τ(N)/2) | 72^(12/2) = 72⁶ |
| **Sum of reciprocals** | (Sum of factors) / N | 195/72 |

### Worked Example
```
N = 72 = 2³ × 3²

Factors: 1,2,3,4,6,8,9,12,18,24,36,72 (12 factors ✓)

Sum = 1+2+3+4+6+8+9+12+18+24+36+72 = 195 ✓

Using formula: [(2⁴-1)/(2-1)] × [(3³-1)/(3-1)]
             = (15/1) × (26/2)
             = 15 × 13 = 195 ✓
```

### 🧠 Tricks

**Trick 1: Odd vs Even Factors**
```
N = 2ᵃ × (odd part)

Total factors of odd part = Odd factors of N
Total factors - Odd factors = Even factors
```

**Trick 2: Perfect Square Factors**
- Replace each exponent with ⌊a/2⌋ + 1 in counting formula

```
72 = 2³ × 3²
Perfect square factors = (⌊3/2⌋+1)(⌊2/2⌋+1) = (1+1)(1+1) = 4
They are: 1, 4, 9, 36
```

**Trick 3: Number of ways to express N as product of 2 factors**
```
If τ(N) = number of factors
• N is not perfect square: τ(N)/2 ways
• N is perfect square: (τ(N)+1)/2 ways (including √N × √N)
```

**Trick 4: Ordered pairs (a,b) where ab = N**
- Always = τ(N)

### Factor Table for Quick Reference

| N | Prime Factorization | τ(N) | σ(N) |
|---|---------------------|------|------|
| 12 | 2² × 3 | 6 | 28 |
| 24 | 2³ × 3 | 8 | 60 |
| 36 | 2² × 3² | 9 | 91 |
| 48 | 2⁴ × 3 | 10 | 124 |
| 60 | 2² × 3 × 5 | 12 | 168 |
| 100 | 2² × 5² | 9 | 217 |

---

## 7. Remainder Theorems

### Basic Remainder Concept
```
Dividend = Divisor × Quotient + Remainder
a = bq + r, where 0 ≤ r < b
```

### Key Theorems

#### 1. Addition Property
```
(a + b) mod n = [(a mod n) + (b mod n)] mod n
```

#### 2. Subtraction Property
```
(a - b) mod n = [(a mod n) - (b mod n) + n] mod n
```

#### 3. Multiplication Property
```
(a × b) mod n = [(a mod n) × (b mod n)] mod n
```

#### 4. Power Property
```
aᵏ mod n = [(a mod n)ᵏ] mod n
```

### Fermat's Little Theorem (Most Important!)
**If p is prime and gcd(a, p) = 1:**
```
a^(p-1) ≡ 1 (mod p)
∴ aⁿ mod p = a^(n mod (p-1)) mod p
```

**Example:** Find 2^100 mod 13
```
By Fermat: 2¹² ≡ 1 (mod 13)
100 = 12 × 8 + 4
2^100 = (2¹²)⁸ × 2⁴ ≡ 1⁸ × 16 ≡ 3 (mod 13)
```

### Euler's Theorem (Generalization)
**For any n, if gcd(a, n) = 1:**
```
a^φ(n) ≡ 1 (mod n)
```
where φ(n) = Euler's totient function

### Euler's Totient Function φ(n)
```
φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂) × ...

For n = p₁^a × p₂^b:
φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂)
```

**Quick Values:**
| n | φ(n) | Calculation |
|---|------|-------------|
| Prime p | p-1 | - |
| pᵏ | pᵏ - p^(k-1) | pᵏ(1-1/p) |
| 12 | 4 | 12(1-1/2)(1-1/3) = 12×½×⅔ |
| 15 | 8 | 15(1-1/3)(1-1/5) = 15×⅔×⅘ |

### Chinese Remainder Theorem (CRT)
If gcd(m, n) = 1, and:
```
x ≡ a (mod m)
x ≡ b (mod n)
```
Then there exists unique x (mod mn).

**Shortcut:** x = a + m × k where k satisfies:
```
a + mk ≡ b (mod n)
```

### 🧠 Tricks for Remainders

**Trick 1: Negative Remainders**
```
-3 mod 7 = 7 - 3 = 4
(-3 + 7) mod 7 = 4
```

**Trick 2: Pattern Recognition**
```
2¹ mod 7 = 2
2² mod 7 = 4
2³ mod 7 = 1 (cycle found!)
∴ 2^100 mod 7 = 2^(100 mod 3) mod 7 = 2¹ mod 7 = 2
```

**Trick 3: Breaking Down Large Numbers**
```
10^n mod 9 = 1 (always)
10^n mod 11: Alternates 10, 1, 10, 1...
```

**Trick 4: aⁿ - bⁿ Division**
- (aⁿ - bⁿ) is always divisible by (a - b)
- When n is even, also divisible by (a + b)

---

## 8. Unit Digit & Cyclicity

### Unit Digit Cycles (Memorize!)

| Digit | Cycle | Period |
|-------|-------|--------|
| 0 | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 2, 4, 8, 6 | 4 |
| 3 | 3, 9, 7, 1 | 4 |
| 4 | 4, 6 | 2 |
| 5 | 5 | 1 |
| 6 | 6 | 1 |
| 7 | 7, 9, 3, 1 | 4 |
| 8 | 8, 4, 2, 6 | 4 |
| 9 | 9, 1 | 2 |

### Master Formula
```
For unit digit of aⁿ:
1. Find unit digit of a (call it u)
2. Find cycle length of u (call it c)
3. Find n mod c (call it r)
4. Answer = uʳ (if r = 0, use uᶜ)
```

### Worked Examples

**Example 1:** Unit digit of 7^245
```
Cycle of 7: 7, 9, 3, 1 (period 4)
245 mod 4 = 1
Unit digit = 7¹ = 7
```

**Example 2:** Unit digit of 13^456
```
Unit digit of 13 = 3
Cycle of 3: 3, 9, 7, 1 (period 4)
456 mod 4 = 0 → Use 4th position
Unit digit = 1
```

**Example 3:** Last 2 digits of 7^100
```
Find 7^100 mod 100
7² = 49
7⁴ = 2401 ≡ 01 (mod 100)
7^100 = (7⁴)^25 ≡ 01^25 = 01 (mod 100)
Last 2 digits = 01
```

### 🧠 Tricks

**Trick 1: Powers of Numbers Ending in 1**
Last 2 digits of (...1)^n:
```
Unit digit = 1 always
Tens digit = (n × tens digit of base) mod 10
```

**Trick 2: Powers of Numbers Ending in 5**
```
...5^n always ends in:
25 if n ≥ 2
5 if n = 1
```

**Trick 3: Sum of Unit Digits in Series**
```
1¹ + 2² + 3³ + ... + n^n
Find unit digit of each, then add.
```

**Trick 4: Factorial Unit Digits**
```
n! ends in 0 for all n ≥ 5
(5! = 120, 6! = 720, ...)
```

### Last Two Digits Advanced Rules

**Rule 1: For odd numbers not ending in 5**
```
Find a^4 mod 100, then use cyclicity
```

**Rule 2: For a^b where a ends in 76**
```
76^n always ends in 76
```

**Rule 3: For 2^n (n ≥ 2)**
```
Cycle of period 20: Find n mod 20, then calculate
```

---

## 9. Base Conversions

### Method Summary

| From | To | Method |
|------|-----|--------|
| Base b | Decimal | Positional value sum |
| Decimal | Base b | Repeated division |
| Binary | Octal | Group 3 bits |
| Binary | Hex | Group 4 bits |
| Octal | Binary | Expand each digit to 3 bits |
| Hex | Binary | Expand each digit to 4 bits |

### Decimal Fraction Conversion

**Decimal → Binary (Fraction Part)**
```
0.625 to binary:
0.625 × 2 = 1.25 → 1
0.25 × 2 = 0.5 → 0  
0.5 × 2 = 1.0 → 1
Answer: 0.101₂
```

**Binary → Decimal (Fraction Part)**
```
0.101₂ = 1×2⁻¹ + 0×2⁻² + 1×2⁻³
       = 0.5 + 0 + 0.125 = 0.625
```

### 🧠 Tricks

**Trick 1: Quick Check**
- (abc)_b in decimal = a×b² + b×b + c
- Largest n-digit in base b = b^n - 1

**Trick 2: Same Number Different Bases**
```
If (ab)_p = (ba)_q
Then: ap + b = bq + a
Solve for relationship between p and q
```

**Trick 3: Arithmetic in Other Bases**
- Convert to decimal, compute, convert back
- OR perform arithmetic with carry/borrow rules of that base

### Common GATE Problems

**Type 1:** Convert (1A3)₁₆ to binary
```
1 → 0001
A → 1010  
3 → 0011
Answer: (000110100011)₂ = (110100011)₂
```

**Type 2:** (1101.01)₂ = ?₁₀
```
= 1×8 + 1×4 + 0×2 + 1×1 + 0×0.5 + 1×0.25
= 8 + 4 + 0 + 1 + 0 + 0.25 = 13.25
```

**Type 3:** Find base b where (121)_b = 144₁₀
```
1×b² + 2×b + 1 = 144
b² + 2b + 1 = 144
(b+1)² = 144
b + 1 = 12
b = 11
```

---

## 10. Special Numbers & Patterns

### Important Number Types

| Type | Definition | Examples | Formula/Check |
|------|------------|----------|---------------|
| **Perfect Square** | n = k² | 1, 4, 9, 16, 25 | Ends in 0,1,4,5,6,9 |
| **Perfect Cube** | n = k³ | 1, 8, 27, 64, 125 | - |
| **Perfect Number** | Sum of proper divisors = n | 6, 28, 496 | σ(n) - n = n |
| **Armstrong** | Sum of digits^(no. of digits) = n | 153, 370, 371, 407 | 1³+5³+3³=153 |
| **Palindrome** | Reads same both ways | 121, 1331 | - |
| **Harshad** | Divisible by digit sum | 18, 21, 27 | 18÷9=2 |

### Perfect Squares Properties

**Property 1: Unit Digits**
```
Perfect squares can only end in: 0, 1, 4, 5, 6, 9
Never in: 2, 3, 7, 8
```

**Property 2: Digital Root**
```
Perfect squares have digital root: 1, 4, 7, or 9
(Except those divisible by 9, which have digital root 9)
```

**Property 3: Sum of First n Odd Numbers**
```
1 + 3 + 5 + ... + (2n-1) = n²
```

**Property 4: Difference of Consecutive Squares**
```
n² - (n-1)² = 2n - 1
```

### Sum Formulas (Must Know!)

| Sum | Formula |
|-----|---------|
| 1 + 2 + 3 + ... + n | n(n+1)/2 |
| 1² + 2² + 3² + ... + n² | n(n+1)(2n+1)/6 |
| 1³ + 2³ + 3³ + ... + n³ | [n(n+1)/2]² |
| 1 + 3 + 5 + ... + (2n-1) | n² |
| 2 + 4 + 6 + ... + 2n | n(n+1) |

### Fibonacci Sequence Properties
```
F(n) = F(n-1) + F(n-2)
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

• F(n)×F(n+2) - F(n+1)² = (-1)^(n+1)
• gcd(F(m), F(n)) = F(gcd(m,n))
• F(n) is even iff 3|n
```

### 🧠 Tricks

**Trick 1: Quick Square Calculation**
```
Numbers ending in 5:
(a5)² = a(a+1) | 25
Example: 35² = 3×4 | 25 = 1225
         85² = 8×9 | 25 = 7225
```

**Trick 2: Near 50 Squaring**
```
(50±n)² = 2500 ± 100n + n²
Example: 53² = 2500 + 300 + 9 = 2809
         47² = 2500 - 300 + 9 = 2209
```

**Trick 3: Near 100 Squaring**
```
(100±n)² = 10000 ± 200n + n²
Example: 103² = 10000 + 600 + 9 = 10609
```

---

## 11. Word Problems Framework

### Problem Type Identification

| Keywords | Concept | Operation |
|----------|---------|-----------|
| "largest size", "maximum piece" | HCF | Find HCF |
| "together again", "coincide" | LCM | Find LCM |
| "remainder when divided" | Modular arithmetic | Find remainder |
| "smallest number divisible" | LCM | Find LCM |
| "largest number that divides" | HCF | Find HCF |
| "complete rows/groups" | Factors | Factorize |

### Common Problem Templates

**Template 1: Division with Same Remainder**
```
Find largest number that divides a, b, c leaving same remainder r.

Method: HCF(a-r, b-r, c-r)
OR if r unknown: HCF(|a-b|, |b-c|, |a-c|)
```

**Example:** Find largest number that divides 65, 81, 145 leaving same remainder.
```
Differences: 81-65=16, 145-81=64, 145-65=80
HCF(16, 64, 80) = 16
```

**Template 2: Find Missing Digit**
```
If 87_4 is divisible by 9, find _.

Sum = 8 + 7 + _ + 4 = 19 + _
For div by 9: 19 + _ ≡ 0 (mod 9)
_ = 8 (since 27 = 9×3)
```

**Template 3: Bells/Lights Problem**
```
Three bells ring at intervals of 12, 15, 20 minutes.
When do they ring together next?

LCM(12, 15, 20) = 60 minutes
```

**Template 4: Maximum Squares from Rectangle**
```
Largest square tiles for (l × w) floor?
Side = HCF(l, w)
Number of tiles = (l × w) / HCF(l,w)²
```

**Template 5: Arrange in Equal Rows**
```
n₁ items of type A, n₂ items of type B
Maximum per row with no mixing?
Answer = HCF(n₁, n₂)
```

### ⚠️ Edge Cases in Word Problems

1. **"At least" vs "At most"**
   - At least → Minimum → often involves LCM
   - At most → Maximum → often involves HCF

2. **Inclusive vs Exclusive Counting**
   - "From 1 to 100" → 100 numbers (inclusive)
   - "Between 1 and 100" → 98 numbers (exclusive)

3. **Time Problems**
   - Simultaneous start → First meeting at LCM
   - Consider if one measurement includes start time

---

## 12. GATE/ESE Specific Tips

### Exam Pattern Observations

**High-Frequency Topics:**
1. ⭐⭐⭐ Divisibility & Remainders
2. ⭐⭐⭐ Base Conversions
3. ⭐⭐ HCF/LCM applications
4. ⭐⭐ Unit Digit problems
5. ⭐ Factor counting

### Time-Saving Strategies

**Strategy 1: Option Elimination**
```
Q: Which number is NOT divisible by 6?
Check: Must be divisible by both 2 AND 3
Quickly eliminate even numbers with digit sum not ÷ 3
```

**Strategy 2: Boundary Testing**
```
Q: Find smallest 4-digit number divisible by 12
Start from 1000, check 1000, 1004, 1008...
1008 ÷ 12 = 84 ✓
```

**Strategy 3: Pattern Recognition for MSQs**
```
For "all that apply" questions:
- Test extreme cases first
- Look for counterexamples
```

### Common Traps to Avoid

| Trap | Reality |
|------|---------|
| 1 is prime | 1 is NEITHER prime nor composite |
| 0 is natural number | 0 is whole but NOT natural |
| HCF × LCM = product for 3 numbers | Only true for 2 numbers |
| √4 is irrational | √4 = 2 is rational |
| Every odd number is prime | 9, 15, 21... are odd but composite |

### Quick Formulas Card

```
╔════════════════════════════════════════════════════════════╗
║  NUMBERS QUICK CARD                                         ║
╠════════════════════════════════════════════════════════════╣
║  N = p₁^a × p₂^b × p₃^c                                     ║
║                                                             ║
║  Factors count: (a+1)(b+1)(c+1)                            ║
║  Sum of factors: Π[(p^(e+1)-1)/(p-1)]                      ║
║  HCF × LCM = Product (only 2 numbers!)                     ║
║                                                             ║
║  Fermat: a^(p-1) ≡ 1 (mod p), p prime                      ║
║  Euler: a^φ(n) ≡ 1 (mod n), gcd(a,n)=1                     ║
║                                                             ║
║  φ(p) = p-1                                                 ║
║  φ(p^k) = p^k - p^(k-1)                                    ║
║  φ(mn) = φ(m)×φ(n) if gcd(m,n)=1                           ║
║                                                             ║
║  Unit digit cycles: 2,3,7,8 → period 4                     ║
║                     4,9 → period 2                          ║
║                     0,1,5,6 → period 1                      ║
║                                                             ║
║  Sum 1 to n: n(n+1)/2                                       ║
║  Sum of squares: n(n+1)(2n+1)/6                            ║
║  Sum of cubes: [n(n+1)/2]²                                 ║
╚════════════════════════════════════════════════════════════╝
```

### Previous Year Question Types

**Type 1: Direct Computation**
```
Find HCF of 126 and 168.
→ Direct Euclidean algorithm or factorization
```

**Type 2: Application Based**
```
Three runners run around a circular track...
→ LCM/HCF application with unit conversion
```

**Type 3: Conceptual**
```
If p is prime, what is (p-1)! mod p?
→ Apply Wilson's theorem: Answer = p-1
```

**Type 4: Code Tracing (for CS)**
```
What does the following function return for GCD?
→ Understand Euclidean algorithm implementation
```

---

## 13. Practice Problems with Solutions

### Problem Set

**Q1.** Find the unit digit of 7^2021
<details>
<summary>Solution</summary>

```
Cycle of 7: 7, 9, 3, 1 (period 4)
2021 mod 4 = 1
Unit digit = 7¹ = 7
```
</details>

**Q2.** Find remainder when 2^100 is divided by 7
<details>
<summary>Solution</summary>

```
By Fermat: 2⁶ ≡ 1 (mod 7)
100 = 6×16 + 4
2^100 = (2⁶)^16 × 2⁴ ≡ 1 × 16 ≡ 2 (mod 7)
```
</details>

**Q3.** (1A.BC)₁₆ = ?₁₀
<details>
<summary>Solution</summary>

```
1A.BC₁₆ = 1×16 + 10×1 + 11×(1/16) + 12×(1/256)
        = 16 + 10 + 0.6875 + 0.046875
        = 26.734375
```
</details>

**Q4.** Find the smallest number which when divided by 12, 15, 18 leaves remainder 5 in each case
<details>
<summary>Solution</summary>

```
LCM(12, 15, 18) = 180
Required number = 180 + 5 = 185
```
</details>

**Q5.** How many factors of 720 are perfect squares?
<details>
<summary>Solution</summary>

```
720 = 2⁴ × 3² × 5
Perfect square factors: even powers of each prime
= (⌊4/2⌋+1)(⌊2/2⌋+1)(⌊1/2⌋+1)
= 3 × 2 × 1 = 6
```
</details>

**Q6.** Find largest 4-digit number divisible by 88
<details>
<summary>Solution</summary>

```
Largest 4-digit = 9999
9999 ÷ 88 = 113.625
Largest = 113 × 88 = 9944
```
</details>

**Q7.** If n! has exactly 24 trailing zeros, find n
<details>
<summary>Solution</summary>

```
Trailing zeros = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...

For n = 100: 20 + 4 + 0 = 24 ✓

But check n = 99: 19 + 3 = 22 ✗
Also valid: n = 100, 101, 102, 103, 104

Smallest n with 24 zeros = 100
```
</details>

**Q8.** Convert (0.6875)₁₀ to binary
<details>
<summary>Solution</summary>

```
0.6875 × 2 = 1.375 → 1
0.375 × 2 = 0.75 → 0
0.75 × 2 = 1.5 → 1
0.5 × 2 = 1.0 → 1
Answer: 0.1011₂
```
</details>

---

## 14. Mental Math Techniques

### Vedic Mathematics Shortcuts

**Nikhilam (Complement Method) for Multiplication**
```
98 × 97:
98 is 2 less than 100
97 is 3 less than 100

Step 1: Cross subtract: 98-3 = 95 OR 97-2 = 95
Step 2: Multiply differences: 2×3 = 06
Answer: 9506
```

**Squaring Numbers Near 50**
```
48² = (50-2)² = 2500 - 200 + 4 = 2304
52² = (50+2)² = 2500 + 200 + 4 = 2704
```

**Multiplication by 11**
```
72 × 11:
7_2 → Insert sum of digits: 7(7+2)2 = 792

47 × 11:
4_7 → 4(4+7)7 → 4(11)7 → Carry: 517
```

### Quick Division Tricks

**Dividing by 5**
```
n ÷ 5 = (n × 2) ÷ 10
Example: 345 ÷ 5 = 690 ÷ 10 = 69
```

**Dividing by 25**
```
n ÷ 25 = (n × 4) ÷ 100
Example: 175 ÷ 25 = 700 ÷ 100 = 7
```

**Dividing by 125**
```
n ÷ 125 = (n × 8) ÷ 1000
```

---

## Quick Revision Checklist

Before Exam, Verify You Know:
- [ ] All divisibility rules (2-13, 25, 125)
- [ ] HCF/LCM formulas and relation
- [ ] Unit digit cycles for 2,3,4,7,8,9
- [ ] Fermat's Little Theorem application
- [ ] Factor count formula
- [ ] Base conversion between Binary/Octal/Hex
- [ ] Sum formulas (n, n², n³)
- [ ] Wilson's theorem
- [ ] Euler's totient function
- [ ] Perfect square properties

---

*📚 All the best for GATE & ESE! Master these concepts and ace the Number System section! 🎯*
