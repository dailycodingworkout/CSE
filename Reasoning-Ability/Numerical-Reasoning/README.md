# 🔢 Chapter 7: Numerical Reasoning

## The Atomic Truth
> **"Numbers follow patterns. Every sequence has a generator; find it, own it."**

---

## 📋 Topics Covered

1. [Number Series](#1-number-series)
2. [Mathematical Operations](#2-mathematical-operations)
3. [Number Systems](#3-number-systems)
4. [Clock Problems](#4-clock-problems)
5. [Calendar Problems](#5-calendar-problems)
6. [Age Problems](#6-age-problems)
7. [Speed, Time & Distance](#7-speed-time--distance)
8. [Work & Time](#8-work--time)

---

## 1. Number Series

### The Singularity
> **"Every series is a pattern in disguise. Find the generating function."**

### The Root Architecture

A number series follows a recurrence relation or closed-form formula:
$$a_n = f(n) \quad \text{or} \quad a_n = g(a_{n-1}, a_{n-2}, \ldots)$$

---

### 🔑 The 15 Master Series Patterns

#### Pattern 1: Arithmetic Progression (AP)
$$a_n = a_1 + (n-1)d$$

**Example:** 5, 8, 11, 14, **17** (d = 3)

#### Pattern 2: Geometric Progression (GP)
$$a_n = a_1 \cdot r^{n-1}$$

**Example:** 2, 6, 18, 54, **162** (r = 3)

#### Pattern 3: Fibonacci Type
$$a_n = a_{n-1} + a_{n-2}$$

**Example:** 1, 1, 2, 3, 5, 8, **13**

#### Pattern 4: Square Numbers
$$a_n = n^2$$

**Example:** 1, 4, 9, 16, 25, **36**

#### Pattern 5: Cube Numbers
$$a_n = n^3$$

**Example:** 1, 8, 27, 64, **125**

#### Pattern 6: Triangular Numbers
$$a_n = \frac{n(n+1)}{2}$$

**Example:** 1, 3, 6, 10, 15, **21**

#### Pattern 7: Prime Numbers
$$a_n = \text{n-th prime}$$

**Example:** 2, 3, 5, 7, 11, 13, **17**

#### Pattern 8: Difference of Squares
$$a_n = n^2 - k$$ or $$a_n = n^2 + k$$

**Example:** 0, 3, 8, 15, 24 (n² - 1)

#### Pattern 9: Alternating Sign
$$a_n = (-1)^n \cdot f(n)$$

**Example:** 1, -2, 3, -4, 5, **-6**

#### Pattern 10: Factorial Series
$$a_n = n!$$

**Example:** 1, 2, 6, 24, 120, **720**

#### Pattern 11: Two-Tier Arithmetic (Second Difference Constant)
$$d_1 = a_2 - a_1, d_2 = a_3 - a_2, \ldots$$
$$\text{Second difference: } d_2 - d_1 = \text{constant}$$

**Example:** 2, 5, 10, 17, 26, **37**
- First differences: 3, 5, 7, 9, **11**
- Second differences: 2, 2, 2, 2 (constant)

#### Pattern 12: Mixed Operations
$$a_n = a_{n-1} \times k + c$$

**Example:** 1, 5, 17, 53, **161** (×3 + 2)

#### Pattern 13: Alternating Operations
```
×2, +3, ×2, +3, ...
```

**Example:** 2, 4, 7, 14, 17, **34**

#### Pattern 14: Product Sequence
$$a_n = n \times (n+1)$$

**Example:** 2, 6, 12, 20, 30, **42**

#### Pattern 15: Sum of Digits Pattern
```
Each term derived from digit manipulation of previous
```

---

### 🎯 The Series Cracking Algorithm

```
Step 1: CALCULATE first differences: d_i = a_{i+1} - a_i
Step 2: If differences are constant → AP, use d to predict
Step 3: CALCULATE second differences
Step 4: If second differences constant → Quadratic pattern
Step 5: CHECK for multiplicative pattern: a_{i+1}/a_i
Step 6: If ratios constant → GP
Step 7: LOOK for squares, cubes, primes, factorials
Step 8: CHECK for alternating patterns (split into odd/even positions)
Step 9: TRY mixed operations: ×k±c
Step 10: If stuck, CHECK for wrong term in series
```

---

### 📊 The Difference Table Method

**Example:** 1, 4, 10, 20, 35, ?

| Level | Sequence |
|-------|----------|
| Original | 1, 4, 10, 20, 35, ? |
| 1st Diff | 3, 6, 10, 15, ? |
| 2nd Diff | 3, 4, 5, ? |
| 3rd Diff | 1, 1, 1 |

Working back:
- 3rd diff = 1
- Next 2nd diff = 5 + 1 = 6
- Next 1st diff = 15 + 6 = 21
- Next term = 35 + 21 = **56**

---

### ⚠️ The Genius Trap

**Trap 1: Wrong Number in Series**
```
Question: Find the wrong number: 2, 5, 10, 17, 24, 37

Differences: 3, 5, 7, 7, 13 ← 24 should be 26
Correct series: 2, 5, 10, 17, 26, 37 (differences: 3, 5, 7, 9, 11)

Answer: 24 is wrong (should be 26)
```

**Trap 2: Multiple Valid Patterns**
```
Series: 2, 4, 8, ?

Pattern 1: GP (r=2) → Next = 16
Pattern 2: Differences: 2, 4 → Next diff = 6 → Next = 14

GATE Rule: The SIMPLER pattern (GP) is usually correct.
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
Find the next term: 3, 9, 27, 81, ?
```

**Solution:**
- Check ratio: 9/3 = 3, 27/9 = 3, 81/27 = 3
- GP with r = 3
- Next term = 81 × 3 = **243**

**Problem 2:** (GATE NAT)
```
Find the next term: 2, 6, 12, 20, 30, ?
```

**Solution:**
- Differences: 4, 6, 8, 10 → Next diff = 12
- Or recognize: $a_n = n(n+1)$
  - 1×2=2, 2×3=6, 3×4=12, 4×5=20, 5×6=30, 6×7=**42**

**Problem 3:** (ESE Pattern)
```
Find the wrong number: 1, 8, 27, 64, 124, 216
```

**Solution:**
- Perfect cubes: 1³=1, 2³=8, 3³=27, 4³=64, 5³=125, 6³=216
- 124 should be 125
- **Answer:** 124 is wrong

---

## 2. Mathematical Operations

### The Singularity
> **"Symbols are operators. Decode the symbol, apply the operation."**

### The Root Architecture

Given symbolic representation:
$$a \oplus b = f(a, b)$$

Find f from examples, then apply.

---

### 🔑 Common Symbolic Patterns

| Symbol | Common Meanings |
|--------|-----------------|
| ⊕ | a + b, or a × b |
| ⊖ | a - b, or a ÷ b |
| ⊗ | a² + b², or ab |
| ⊙ | (a + b)/2, or √(ab) |
| @ | a² - b², or a + b + ab |
| # | a/b + b/a, or |a - b| |
| * | Often custom per question |

---

### 🎯 The Symbol Decoding Algorithm

```
Step 1: LOOK at given examples: a ⊕ b = c
Step 2: TRY basic operations: +, -, ×, ÷
Step 3: TRY compound operations: a² + b², a + b + 1, etc.
Step 4: VERIFY pattern with ALL given examples
Step 5: APPLY to question
```

---

### 📝 Practice Problems

**Problem 1:**
```
If 3 @ 4 = 25 and 5 @ 12 = 169, then 8 @ 15 = ?
```

**Solution:**
- 3 @ 4 = 25 = 5² = (3+4-2)²? No. = 3² + 4² = 9 + 16 = 25 ✓
- Verify: 5 @ 12 = 5² + 12² = 25 + 144 = 169 ✓
- Pattern: a @ b = a² + b²
- 8 @ 15 = 64 + 225 = **289**

**Problem 2:**
```
If 2 * 3 = 13 and 4 * 5 = 41, then 6 * 7 = ?
```

**Solution:**
- 2 * 3 = 13 → Try: 2² + 3² = 13 ✓
- 4 * 5 = 41 → Check: 16 + 25 = 41 ✓
- Pattern: a * b = a² + b²
- 6 * 7 = 36 + 49 = **85**

---

## 3. Number Systems

### The Singularity
> **"Numbers are just representations. The value is independent of the base."**

### The Root Architecture

Number in base $b$:
$$(d_n d_{n-1} \ldots d_1 d_0)_b = \sum_{i=0}^{n} d_i \times b^i$$

---

### 🔑 Common Bases

| Base | Name | Digits Used |
|------|------|-------------|
| 2 | Binary | 0, 1 |
| 8 | Octal | 0-7 |
| 10 | Decimal | 0-9 |
| 16 | Hexadecimal | 0-9, A-F |

---

### 🔑 Conversion Formulas

**Any Base to Decimal:**
$$(d_2 d_1 d_0)_b = d_2 \times b^2 + d_1 \times b^1 + d_0 \times b^0$$

**Decimal to Any Base:**
Repeatedly divide by base, collect remainders (bottom to top).

**Binary ↔ Octal:** Group binary digits in 3s (from right)
**Binary ↔ Hex:** Group binary digits in 4s (from right)

---

### 📝 Practice Problem

**Problem:**
```
Convert (1101)₂ to decimal.
```

**Solution:**
$$1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$
$$= 8 + 4 + 0 + 1 = 13$$

**Answer:** 13

---

## 4. Clock Problems

### The Singularity
> **"The clock is a race between hands. Track relative speed."**

### The Root Architecture

- Minute hand: Completes 360° in 60 minutes → **6° per minute**
- Hour hand: Completes 360° in 12 hours = 720 minutes → **0.5° per minute**
- Relative speed: 6 - 0.5 = **5.5° per minute**

---

### 🔑 Key Clock Formulas

**Angle at H hours and M minutes:**
$$\theta = \left|30H - \frac{11M}{2}\right|$$

If result > 180°, use (360° - result) for the smaller angle.

**Angle of hour hand from 12:**
$$\theta_H = 30H + \frac{M}{2}$$

**Angle of minute hand from 12:**
$$\theta_M = 6M$$

---

### 🔑 Special Cases

| Event | Frequency | Time Interval |
|-------|-----------|---------------|
| Hands overlap | 22 times in 24 hrs | Every 65.45 minutes |
| Hands at right angle | 44 times in 24 hrs | Every 32.73 minutes |
| Hands opposite | 22 times in 24 hrs | Every 65.45 minutes |
| Same position as 12:00 | 1 time (at 12:00 only) | 12 hours |

**Overlap times:** Starting from 12:00, hands overlap at:
12:00, 1:05:27, 2:10:55, 3:16:22, 4:21:49, 5:27:16, 6:32:44, 7:38:11, 8:43:38, 9:49:05, 10:54:33

---

### ⚠️ The Genius Trap

**Trap: Hands at 90° doesn't mean time is X:15 or X:45**
```
At 3:00, angle is exactly 90°.
But at 3:15, minute hand is at 90°, hour hand is at 97.5° (not 90° apart!)
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
What is the angle between the hands of a clock at 4:30?
```

**Solution:**
$$\theta = \left|30(4) - \frac{11(30)}{2}\right| = \left|120 - 165\right| = 45°$$

**Answer:** 45°

**Problem 2:**
```
At what time between 3 and 4 o'clock will the hands be together?
```

**Solution:**
At 3:00, hour hand is at 90°, minute hand at 0°.
Gap = 90°
Relative speed = 5.5° per minute
Time = 90 ÷ 5.5 = 16.36 minutes

**Answer:** 3:16:22 (approximately 3:16 and 4/11 minutes)

---

## 5. Calendar Problems

### The Singularity
> **"Days cycle in 7. Track the remainder, track the day."**

### The Root Architecture

**Days in a Year:**
- Regular year: 365 days = 52 weeks + 1 day (1 odd day)
- Leap year: 366 days = 52 weeks + 2 days (2 odd days)

**Leap Year Rule:**
- Divisible by 4: Leap year
- Exception: Century years (1700, 1800, 1900) NOT leap unless divisible by 400
- So: 2000 is leap, 1900 is not

---

### 🔑 Odd Days Calculation

| Period | Odd Days |
|--------|----------|
| 1 ordinary year | 1 |
| 1 leap year | 2 |
| 100 years | 5 (24 leap + 76 ordinary = 48 + 76 = 124, 124 mod 7 = 5) |
| 200 years | 3 |
| 300 years | 1 |
| 400 years | 0 (includes extra leap day for century) |

**Day of Week from Odd Days:**

| Odd Days | Day |
|----------|-----|
| 0 | Sunday |
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |

---

### 🎯 Finding Day of Week Algorithm

```
Step 1: Count complete centuries (use table for odd days)
Step 2: Add odd days for remaining years
Step 3: Add odd days for months (Jan=0, Feb=3, Mar=3, ...)
Step 4: Add the date
Step 5: Total mod 7 = Day of week
```

**Odd Days per Month:**
| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 3 | 0/1 | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 |

(Feb = 0 for non-leap, 1 for leap; values are cumulative from Jan)

---

### 📝 Practice Problem

**Problem:**
```
What day of the week was January 15, 2000?
```

**Solution:**

**Method: Using Reference Date**
- Known fact: January 1, 2000 was a Saturday
- From Jan 1 to Jan 15 = 14 days = 2 complete weeks
- 2 weeks = 0 odd days (no shift in day of week)
- Therefore, January 15, 2000 = Saturday + 0 = Saturday

**Answer:** Saturday

**Alternative Verification (Odd Days Method):**
- 1600 years: 0 odd days (400 years × 4)
- 300 years (1601-1900): 1 odd day
- 99 years (1901-1999): 24 leap + 75 ordinary = 24×2 + 75×1 = 123 odd days = 17×7 + 4 = 4 odd days
- Total for 1999 years: 0 + 1 + 4 = 5 odd days
- Year 2000 up to Jan 15: 15 days = 1 odd day
- Total: 5 + 1 = 6 odd days = Saturday ✓

---

## 6. Age Problems

### The Singularity
> **"Age differences are constant. Set equations, solve algebra."**

### The Root Architecture

If A's current age is $a$ and B's current age is $b$:
- $n$ years ago: A was $(a-n)$, B was $(b-n)$
- $n$ years hence: A will be $(a+n)$, B will be $(b+n)$
- Difference $|a-b|$ is CONSTANT across time

---

### 🔑 Age Problem Templates

**Template 1: Present + Future**
```
A is 20 years old. In how many years will A be twice as old as B, who is currently 8?
Equation: 20 + x = 2(8 + x)
Solution: 20 + x = 16 + 2x → x = 4 years
```

**Template 2: Present + Past**
```
A is 40, B is 20. How many years ago was A three times as old as B?
Equation: 40 - x = 3(20 - x)
Solution: 40 - x = 60 - 3x → 2x = 20 → x = 10 years ago
```

**Template 3: Sum/Difference of Ages**
```
Sum of ages of A and B is 50. A is 10 years older than B.
Equations: a + b = 50, a - b = 10
Solution: 2a = 60 → a = 30, b = 20
```

---

### 📝 Practice Problem

**Problem:**
```
The sum of ages of a father and son is 56 years. 
After 4 years, the father will be 3 times as old as the son.
Find their present ages.
```

**Solution:**
Let father's age = F, son's age = S
- F + S = 56 ... (1)
- F + 4 = 3(S + 4) ... (2)

From (2): F + 4 = 3S + 12 → F = 3S + 8 ... (3)

Substitute in (1): 3S + 8 + S = 56 → 4S = 48 → S = 12

F = 56 - 12 = 44

**Answer:** Father: 44 years, Son: 12 years

---

## 7. Speed, Time & Distance

### The Singularity
> **"Speed is distance over time. All problems reduce to this ratio."**

### The Root Architecture

$$\text{Speed} = \frac{\text{Distance}}{\text{Time}}$$
$$\text{Distance} = \text{Speed} \times \text{Time}$$
$$\text{Time} = \frac{\text{Distance}}{\text{Speed}}$$

---

### 🔑 Key Formulas

**Average Speed:**
$$\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}$$

For same distance at speeds $v_1$ and $v_2$:
$$\text{Average Speed} = \frac{2v_1 v_2}{v_1 + v_2}$$

**Relative Speed:**
- Same direction: $|v_1 - v_2|$
- Opposite direction: $v_1 + v_2$

**Trains Crossing:**
- Train crossing a pole: $t = \frac{L_{\text{train}}}{v}$
- Train crossing platform: $t = \frac{L_{\text{train}} + L_{\text{platform}}}{v}$
- Two trains crossing: $t = \frac{L_1 + L_2}{v_{\text{relative}}}$

---

### 📝 Practice Problem

**Problem:**
```
A train 150 m long is running at 54 km/h. 
How long will it take to cross a platform 100 m long?
```

**Solution:**
- Total distance = 150 + 100 = 250 m
- Speed = 54 km/h = 54 × (1000/3600) = 15 m/s
- Time = 250 ÷ 15 = 16.67 seconds

**Answer:** 16.67 seconds (or 50/3 seconds)

---

## 8. Work & Time

### The Singularity
> **"Work done = Rate × Time. Rates are additive when working together."**

### The Root Architecture

If A can do work in $a$ days:
$$\text{A's rate} = \frac{1}{a} \text{ (work per day)}$$

If A and B work together:
$$\text{Combined rate} = \frac{1}{a} + \frac{1}{b}$$

$$\text{Time together} = \frac{1}{\frac{1}{a} + \frac{1}{b}} = \frac{ab}{a+b}$$

---

### 🔑 Key Formulas

**Two Workers:**
$$T_{\text{together}} = \frac{ab}{a+b}$$

**Three Workers:**
$$T_{\text{together}} = \frac{abc}{ab + bc + ca}$$

**Work Completed:**
$$\text{Work done} = \text{Rate} \times \text{Time} = \frac{t}{T}$$

Where $t$ = time worked, $T$ = time to complete alone

---

### ⚠️ The Genius Trap

**Trap: Pipes and Cisterns (Negative Work)**
```
If a pipe fills in 6 hours and a leak empties in 10 hours:
Net rate = 1/6 - 1/10 = 5/30 - 3/30 = 2/30 = 1/15

Time to fill = 15 hours (not 6-10!)
```

---

### 📝 Practice Problem

**Problem:**
```
A can do a piece of work in 12 days. B can do it in 18 days.
They work together for 4 days, then A leaves.
How many more days will B take to finish the remaining work?
```

**Solution:**
- Combined rate = 1/12 + 1/18 = 3/36 + 2/36 = 5/36 per day
- Work done in 4 days = 4 × (5/36) = 20/36 = 5/9
- Remaining work = 1 - 5/9 = 4/9
- B's rate = 1/18 per day
- Time for B = (4/9) ÷ (1/18) = (4/9) × 18 = 8 days

**Answer:** 8 days

---

## 🧠 The Numerical Reasoning Mnemonic: "SPEED"

- **S**eries pattern (AP, GP, special)
- **P**ercentages and ratios
- **E**quations from word problems
- **E**stimate first, calculate later
- **D**ouble-check units

---

## 📊 Quick Reference: Mental Math

### Squares (11-30)
| n | n² | n | n² |
|---|----|----|---|
| 11 | 121 | 21 | 441 |
| 12 | 144 | 22 | 484 |
| 13 | 169 | 23 | 529 |
| 14 | 196 | 24 | 576 |
| 15 | 225 | 25 | 625 |
| 16 | 256 | 26 | 676 |
| 17 | 289 | 27 | 729 |
| 18 | 324 | 28 | 784 |
| 19 | 361 | 29 | 841 |
| 20 | 400 | 30 | 900 |

### Cubes (1-15)
| n | n³ |
|---|-----|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |
| 4 | 64 |
| 5 | 125 |
| 6 | 216 |
| 7 | 343 |
| 8 | 512 |
| 9 | 729 |
| 10 | 1000 |

### Prime Numbers (First 25)
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

---

## 🎯 Mastery Checklist

- [ ] Can identify series patterns in under 10 seconds
- [ ] Know all squares up to 30 and cubes up to 15
- [ ] Can solve clock angle problems without formula reference
- [ ] Can calculate day of week for any date
- [ ] Can set up age problem equations correctly
- [ ] Can solve work-time problems including pipes
- [ ] Can handle relative speed calculations

---

## ⏱️ The 5-Second Snap-Check

| Check | What to Verify |
|-------|---------------|
| ✅ Units | Are speed, time, distance in compatible units? |
| ✅ Reasonableness | Is the answer in expected range? |
| ✅ Sign | For relative calculations, is direction correct? |
| ✅ Pattern | Does identified pattern hold for ALL given terms? |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> 
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Number Series with Data Interpretation for a Rank-1 simulation?

[← Back to Main Index](../README.md) | [Previous: Critical Reasoning](../Critical-Reasoning/README.md)
