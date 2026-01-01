# 🔢 Number System | The Singularity

> **The Atomic Truth:** *All numbers reduce to prime factor patterns.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Types of Numbers](#types-of-numbers)
3. [Divisibility Rules](#divisibility-rules)
4. [Factors and Multiples](#factors-and-multiples)
5. [Remainder Theorems](#remainder-theorems)
6. [HCF and LCM](#hcf-and-lcm)
7. [Unit Digit Concepts](#unit-digit-concepts)
8. [Number of Zeros](#number-of-zeros)
9. [Power Cycles](#power-cycles)
10. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
11. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Number System Matters?
The Number System is the **foundation of all quantitative aptitude**. Every calculation—whether in percentages, profit-loss, or probability—ultimately involves number manipulation.

### The Number Hierarchy

```
Real Numbers (ℝ)
├── Rational Numbers (ℚ) - Can be expressed as p/q
│   ├── Integers (ℤ)
│   │   ├── Whole Numbers (W) = {0, 1, 2, 3, ...}
│   │   │   └── Natural Numbers (ℕ) = {1, 2, 3, ...}
│   │   └── Negative Integers = {..., -3, -2, -1}
│   └── Fractions (proper, improper, mixed)
└── Irrational Numbers - Cannot be expressed as p/q
    Examples: √2, π, e
```

---

## Types of Numbers

### 1. Natural Numbers (ℕ)
- **Definition:** Counting numbers starting from 1
- **Set:** {1, 2, 3, 4, 5, ...}
- **Property:** Closed under addition and multiplication

### 2. Whole Numbers (W)
- **Definition:** Natural numbers including zero
- **Set:** {0, 1, 2, 3, 4, 5, ...}

### 3. Integers (ℤ)
- **Definition:** Whole numbers and their negatives
- **Set:** {..., -3, -2, -1, 0, 1, 2, 3, ...}

### 4. Prime Numbers
- **Definition:** Numbers greater than 1 with exactly **two** factors (1 and itself)
- **First 25 Primes:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

> **💡 The Golden Pivot:** 2 is the ONLY even prime number.

#### Quick Primality Test
For checking if $n$ is prime, test divisibility only up to $\sqrt{n}$

**Example:** Is 127 prime?
- $\sqrt{127} \approx 11.3$
- Check: 2, 3, 5, 7, 11
- 127 is not divisible by any → **127 is prime**

### 5. Composite Numbers
- **Definition:** Numbers with more than two factors
- **First few:** 4, 6, 8, 9, 10, 12, 14, 15, ...

> **⚠️ Edge Case:** 1 is neither prime nor composite!

### 6. Co-prime Numbers
- **Definition:** Two numbers with HCF = 1
- **Example:** 8 and 15 are co-prime (HCF = 1)

### 7. Twin Primes
- **Definition:** Primes differing by 2
- **Examples:** (3,5), (5,7), (11,13), (17,19), (29,31)

### 8. Perfect Numbers
- **Definition:** Sum of proper divisors equals the number
- **Examples:** 6 = 1+2+3, 28 = 1+2+4+7+14

---

## Divisibility Rules

### Master Table of Divisibility

| Divisor | Rule | Example |
|---------|------|---------|
| **2** | Last digit is even (0,2,4,6,8) | 1234 ✓ |
| **3** | Sum of digits divisible by 3 | 123 → 1+2+3=6 ✓ |
| **4** | Last 2 digits divisible by 4 | 1324 → 24÷4 ✓ |
| **5** | Last digit is 0 or 5 | 125 ✓ |
| **6** | Divisible by both 2 AND 3 | 126 ✓ |
| **7** | Double last digit, subtract from rest | 371 → 37-2=35 ✓ |
| **8** | Last 3 digits divisible by 8 | 1024 → 024÷8 ✓ |
| **9** | Sum of digits divisible by 9 | 729 → 7+2+9=18 ✓ |
| **10** | Last digit is 0 | 120 ✓ |
| **11** | (Sum of odd-place digits) - (Sum of even-place digits) = 0 or 11k | 2728 → (2+2)-(7+8)=-11 ✓ |
| **12** | Divisible by both 3 AND 4 | 144 ✓ |
| **13** | Add 4× last digit to rest | 247 → 24+28=52 → 5+8=13 ✓ |

### Why These Rules Work?

**For Divisibility by 3:**
Every number $N = a_n \cdot 10^n + a_{n-1} \cdot 10^{n-1} + ... + a_1 \cdot 10 + a_0$

Since $10 \equiv 1 \pmod{3}$, we have:
$$N \equiv a_n + a_{n-1} + ... + a_1 + a_0 \pmod{3}$$

Thus, $N$ is divisible by 3 iff the sum of digits is divisible by 3.

---

## Factors and Multiples

### Finding Number of Factors

If $N = p_1^{a_1} \times p_2^{a_2} \times p_3^{a_3} \times ... \times p_k^{a_k}$

Then: $$\text{Number of factors} = (a_1 + 1)(a_2 + 1)(a_3 + 1)...(a_k + 1)$$

**Example:** Find factors of 360
- $360 = 2^3 \times 3^2 \times 5^1$
- Number of factors = $(3+1)(2+1)(1+1) = 4 \times 3 \times 2 = 24$

### Sum of All Factors

$$\sigma(N) = \frac{p_1^{a_1+1} - 1}{p_1 - 1} \times \frac{p_2^{a_2+1} - 1}{p_2 - 1} \times ... \times \frac{p_k^{a_k+1} - 1}{p_k - 1}$$

**Example:** Sum of factors of 12
- $12 = 2^2 \times 3^1$
- Sum = $\frac{2^3-1}{2-1} \times \frac{3^2-1}{3-1} = 7 \times 4 = 28$
- Verification: 1+2+3+4+6+12 = 28 ✓

### Product of All Factors

$$\text{Product} = N^{\frac{\text{Number of factors}}{2}}$$

**Example:** Product of factors of 12
- Factors = 6, so Product = $12^{6/2} = 12^3 = 1728$
- Verification: $1 \times 2 \times 3 \times 4 \times 6 \times 12 = 1728$ ✓

### Number of Odd/Even Factors

For $N = 2^a \times (\text{odd part})^b$:
- **Odd factors:** Ignore the power of 2, calculate factors of odd part
- **Even factors:** Total factors - Odd factors

---

## Remainder Theorems

### Basic Remainder Concept
When $a$ is divided by $b$: $a = bq + r$ where $0 \leq r < b$

### Remainder Theorem Properties

1. **Addition:** $(a + b) \mod n = [(a \mod n) + (b \mod n)] \mod n$
2. **Subtraction:** $(a - b) \mod n = [(a \mod n) - (b \mod n)] \mod n$
3. **Multiplication:** $(a \times b) \mod n = [(a \mod n) \times (b \mod n)] \mod n$

### Fermat's Little Theorem
If $p$ is prime and $\gcd(a, p) = 1$:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Application:** Find remainder when $2^{100}$ is divided by 13
- By Fermat: $2^{12} \equiv 1 \pmod{13}$
- $2^{100} = 2^{12 \times 8 + 4} = (2^{12})^8 \times 2^4 \equiv 1^8 \times 16 \equiv 3 \pmod{13}$

### Euler's Theorem (Generalization)
For any $a$ and $n$ where $\gcd(a, n) = 1$:
$$a^{\phi(n)} \equiv 1 \pmod{n}$$

Where $\phi(n)$ is Euler's totient function.

### Euler's Totient Function

$$\phi(n) = n \times \prod_{p|n} \left(1 - \frac{1}{p}\right)$$

**Example:** $\phi(12) = 12 \times (1-\frac{1}{2}) \times (1-\frac{1}{3}) = 12 \times \frac{1}{2} \times \frac{2}{3} = 4$

---

## HCF and LCM

### Definitions
- **HCF (Highest Common Factor):** Largest number that divides all given numbers
- **LCM (Least Common Multiple):** Smallest number divisible by all given numbers

### Finding HCF

**Method 1: Prime Factorization**
- Take common primes with MINIMUM powers

**Method 2: Euclidean Algorithm**
$$\gcd(a, b) = \gcd(b, a \mod b)$$

**Example:** HCF(252, 105)
- $252 = 105 \times 2 + 42$
- $105 = 42 \times 2 + 21$
- $42 = 21 \times 2 + 0$
- **HCF = 21**

### Finding LCM

**Method 1: Prime Factorization**
- Take ALL primes with MAXIMUM powers

**Method 2: Using HCF**
$$\text{LCM}(a, b) = \frac{a \times b}{\text{HCF}(a, b)}$$

### The Golden Rule
$$\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b$$

> **⚠️ Edge Case:** This rule works ONLY for 2 numbers!

### HCF and LCM of Fractions

$$\text{HCF of fractions} = \frac{\text{HCF of numerators}}{\text{LCM of denominators}}$$

$$\text{LCM of fractions} = \frac{\text{LCM of numerators}}{\text{HCF of denominators}}$$

---

## Unit Digit Concepts

### The Power Cycle Pattern

Every number's unit digit follows a cyclical pattern:

| Last Digit | Cycle | Period |
|------------|-------|--------|
| 0 | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 2→4→8→6 | 4 |
| 3 | 3→9→7→1 | 4 |
| 4 | 4→6 | 2 |
| 5 | 5 | 1 |
| 6 | 6 | 1 |
| 7 | 7→9→3→1 | 4 |
| 8 | 8→4→2→6 | 4 |
| 9 | 9→1 | 2 |

### Quick Technique
For base ending in 2, 3, 7, 8 (cycle of 4):
1. Divide power by 4
2. Use remainder to find position in cycle
3. Remainder 0 means 4th position

**Example:** Unit digit of $7^{243}$
- $243 = 4 \times 60 + 3$
- Remainder = 3
- Cycle of 7: 7→9→3→1
- 3rd position = **3**

---

## Number of Zeros

### Trailing Zeros in n!

Trailing zeros come from factors of 10 = 2 × 5. Since factors of 2 > factors of 5, count factors of 5.

$$\text{Zeros in } n! = \left\lfloor\frac{n}{5}\right\rfloor + \left\lfloor\frac{n}{25}\right\rfloor + \left\lfloor\frac{n}{125}\right\rfloor + ...$$

**Example:** Trailing zeros in 100!
- $\lfloor\frac{100}{5}\rfloor + \lfloor\frac{100}{25}\rfloor + \lfloor\frac{100}{125}\rfloor = 20 + 4 + 0 = 24$

### Highest Power of Prime p in n!

$$\text{Highest power of } p \text{ in } n! = \sum_{i=1}^{\infty} \left\lfloor\frac{n}{p^i}\right\rfloor$$

---

## Power Cycles

### Last Two Digits (For Advanced GATE)

For finding last two digits of $a^n$:

**Case 1:** If $a$ ends in 1
- Pattern in units of tens digit based on $(a-1) \times n \mod 100$

**Case 2:** If $a$ ends in 5
- Last two digits are always 25 (for $n \geq 2$)

**Case 3:** If $a$ ends in 6
- Last two digits: 76 if even position in cycle, 76 or specific pattern

**Case 4:** For other cases
- Use $a^{40} \equiv 1 \pmod{100}$ for numbers coprime to 100

---

## GATE & ESE Problem Patterns

### Pattern 1: Remainder Problems
> Find the remainder when $17^{256}$ is divided by 17
- **Answer:** 0 (Any number is divisible by itself)

### Pattern 2: Factor Count
> How many factors of $2^4 \times 5^3 \times 7^4$ are perfect squares?
- For perfect square: powers must be even
- Choices for 2: 0,2,4 → 3 ways
- Choices for 5: 0,2 → 2 ways  
- Choices for 7: 0,2,4 → 3 ways
- **Answer:** $3 \times 2 \times 3 = 18$

### Pattern 3: Divisibility Applications
> What is the largest number that divides $n^3 - n$ for all positive integers $n$?
- $n^3 - n = n(n-1)(n+1)$
- Product of 3 consecutive integers
- Always divisible by 6
- **Answer:** 6

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
When asked "What is the remainder when $3^{100}$ is divided by 7?", students often:
1. Start calculating $3^1, 3^2, 3^3...$ manually
2. Forget to use Fermat's theorem
3. Make arithmetic errors in the cycle

**The Elegant Solution:**
- By Fermat: $3^6 \equiv 1 \pmod{7}$
- $3^{100} = 3^{6 \times 16 + 4} = (3^6)^{16} \times 3^4 \equiv 1 \times 81 \equiv 4 \pmod{7}$

**NAT Precision Lock:**
- When answer involves decimals (like $\phi$ calculations), maintain 4 decimal places
- Round only at the final step

---

## Permanent Recall

### The Bizarre Mnemonic (Divisibility by 7)
*"Double the last digit and SUBTRACT from the rest—think of it as a digit demanding TWICE its value before leaving."*

### The Mental Slider
Imagine a dial where:
- Left = Number size grows
- Right = Remainder possibilities shrink
- The Euler totient $\phi(n)$ controls the "cycle length" dial

### The 5-Second Snap-Check
For any remainder problem: The answer MUST be less than the divisor.

---

## Practice Problems

### Level 1: Fundamentals
1. Find the number of factors of 720.
2. What is the unit digit of $7^{2024}$?
3. Find HCF and LCM of 48 and 180.

### Level 2: GATE Standard
4. Find the remainder when $2^{256}$ is divided by 17.
5. How many trailing zeros are there in 250!?
6. Find the sum of all factors of 180.

### Level 3: IIT Examiner Level
7. What is the highest power of 12 that divides 50!?
8. If $N = 2^{10} \times 3^5 \times 5^2$, find the number of odd divisors of N.
9. Find the number of ordered pairs $(a, b)$ such that LCM$(a, b) = 2^3 \times 3^2$.

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. $720 = 2^4 \times 3^2 \times 5^1$ → Factors = $(4+1)(2+1)(1+1) = 30$

2. Cycle of 7: 7→9→3→1 (period 4). $2024 = 4 \times 506$, so unit digit = **1**

3. $48 = 2^4 \times 3$, $180 = 2^2 \times 3^2 \times 5$
   - HCF = $2^2 \times 3 = 12$
   - LCM = $2^4 \times 3^2 \times 5 = 720$

4. By Fermat: $2^{16} \equiv 1 \pmod{17}$
   - $2^{256} = (2^{16})^{16} \equiv 1 \pmod{17}$
   - **Remainder = 1**

5. Zeros = $\lfloor\frac{250}{5}\rfloor + \lfloor\frac{250}{25}\rfloor + \lfloor\frac{250}{125}\rfloor + \lfloor\frac{250}{625}\rfloor = 50 + 10 + 2 + 0 = 62$

6. $180 = 2^2 \times 3^2 \times 5$
   - Sum = $\frac{2^3-1}{1} \times \frac{3^3-1}{2} \times \frac{5^2-1}{4} = 7 \times 13 \times 6 = 546$

7. $12 = 2^2 \times 3$
   - Power of 2 in 50! = 25+12+6+3+1 = 47
   - Power of 3 in 50! = 16+5+1 = 22
   - Power of 12 = min(47/2, 22/1) = min(23, 22) = **22**

8. Odd divisors = factors of $3^5 \times 5^2 = (5+1)(2+1) = 18$

9. For LCM = $2^3 \times 3^2$, both $a$ and $b$ must have forms $2^x \times 3^y$ where max(x) = 3 and max(y) = 2.
   - For power of 2: pairs where max = 3: (0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0) = 7 pairs
   - For power of 3: pairs where max = 2: (0,2),(1,2),(2,2),(2,1),(2,0) = 5 pairs
   - Total = $7 \times 5 = 35$

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Number System with Permutation-Combination for a Rank-1 simulation?
