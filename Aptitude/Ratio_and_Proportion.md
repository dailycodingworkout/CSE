# Ratio & Proportion: Complete GATE & ESE Study Notes

> **"Master the fundamentals, and complex problems become child's play."**

---

## Table of Contents

1. [Core Concepts](#1-core-concepts)
2. [Types of Ratios](#2-types-of-ratios)
3. [Proportion & Its Types](#3-proportion--its-types)
4. [Variation](#4-variation)
5. [Quick Tricks & Shortcuts](#5-quick-tricks--shortcuts)
6. [Common Mistakes & Edge Cases](#6-common-mistakes--edge-cases)
7. [GATE/ESE Pattern Questions](#7-gateese-pattern-questions)
8. [Formula Quick Reference](#8-formula-quick-reference)

---

## 1. Core Concepts

### What is a Ratio?

A **ratio** compares two quantities of the **same kind** using division.

```
Ratio of a to b = a : b = a/b  (where b ≠ 0)
```

**Analogy**: Think of ratio as a "recipe". If a cake recipe says flour:sugar = 3:1, for every 3 cups of flour, you need 1 cup of sugar.

**Key Points:**
- **a** = Antecedent (first term)
- **b** = Consequent (second term)
- Ratio has **no units** (pure number)
- Order matters: 3:4 ≠ 4:3

### Why Ratios Matter

| Real-World Use | Example |
|----------------|---------|
| Mixing solutions | Acid:Water = 2:5 |
| Map scales | 1 cm : 1 km |
| Financial ratios | Debt:Equity = 1:2 |
| Speed comparisons | Car:Bike = 5:3 |

### Properties of Ratios

| Property | Formula | Example |
|----------|---------|---------|
| Multiplication | a:b = ma:mb | 2:3 = 4:6 = 6:9 |
| Division | a:b = (a/m):(b/m) | 6:9 = 2:3 |
| Addition | (a+b):b or a:(a+b) | If a:b = 3:4, then (a+b):b = 7:4 |
| Inversion | a:b → b:a | 3:4 → 4:3 |

### Converting Ratios

**Ratio → Fraction → Percentage**
```
a:b → a/(a+b) and b/(a+b) → multiply by 100%
```

**Example**: If profit is divided in ratio 3:2
- First person gets: 3/(3+2) = 3/5 = 60%
- Second person gets: 2/(3+2) = 2/5 = 40%

---

## 2. Types of Ratios

### 2.1 Compound Ratio

When two or more ratios are multiplied together.

```
Compound ratio of (a:b) and (c:d) = ac : bd
```

**Example**: Compound ratio of 2:3 and 4:5 = (2×4) : (3×5) = 8:15

**Use Case**: Calculating combined effects (e.g., efficiency × time)

### 2.2 Duplicate Ratio

Square of a ratio.

```
Duplicate ratio of a:b = a² : b²
```

**Example**: Duplicate ratio of 3:4 = 9:16

**Use Case**: Problems involving areas (since Area ∝ side²)

### 2.3 Triplicate Ratio

Cube of a ratio.

```
Triplicate ratio of a:b = a³ : b³
```

**Example**: Triplicate ratio of 2:3 = 8:27

**Use Case**: Volume comparisons (Volume ∝ side³)

### 2.4 Sub-Duplicate Ratio

Square root of a ratio.

```
Sub-duplicate ratio of a:b = √a : √b
```

**Example**: Sub-duplicate ratio of 16:25 = 4:5

### 2.5 Sub-Triplicate Ratio

Cube root of a ratio.

```
Sub-triplicate ratio of a:b = ∛a : ∛b
```

**Example**: Sub-triplicate ratio of 8:27 = 2:3

### 2.6 Reciprocal/Inverse Ratio

```
Reciprocal ratio of a:b = 1/a : 1/b = b:a
```

**Example**: Reciprocal of 3:5 = 5:3

### Quick Comparison Table

| Ratio Type | Formula | 3:4 becomes |
|------------|---------|-------------|
| Compound (with 2:5) | (3×2):(4×5) | 6:20 = 3:10 |
| Duplicate | 3²:4² | 9:16 |
| Triplicate | 3³:4³ | 27:64 |
| Sub-duplicate | √3:√4 | √3:2 |
| Sub-triplicate | ∛3:∛4 | ∛3:∛4 |
| Reciprocal | 4:3 | 4:3 |

---

## 3. Proportion & Its Types

### What is Proportion?

Proportion is an **equality of two ratios**.

```
If a:b = c:d, then a, b, c, d are in proportion
Written as: a:b :: c:d  or  a/b = c/d
```

**Analogy**: If you're mixing paint, and Red:Blue = 2:3 gives a perfect purple, then 4:6 (same ratio) gives the identical shade.

### Key Terms

- **Extremes**: First and last terms (a and d)
- **Means**: Middle terms (b and c)
- **Product Rule**: Product of extremes = Product of means

```
a × d = b × c
```

### 3.1 Continued Proportion

Three quantities a, b, c are in continued proportion if:

```
a:b = b:c  →  b² = ac
```

Here, **b is the Mean Proportional** between a and c.

```
b = √(ac)
```

**Example**: Find mean proportional between 4 and 16.
- b = √(4×16) = √64 = 8
- Check: 4:8 = 8:16 ✓

### 3.2 Third Proportional

If a:b = b:x, then x is the **third proportional** to a and b.

```
x = b²/a
```

**Example**: Third proportional to 4 and 6:
- x = 6²/4 = 36/4 = 9
- Check: 4:6 = 6:9 ✓

### 3.3 Fourth Proportional

If a:b = c:x, then x is the **fourth proportional**.

```
x = (b × c)/a
```

**Example**: Fourth proportional to 3, 6, 8:
- x = (6×8)/3 = 16
- Check: 3:6 = 8:16 ✓

### Proportionality Summary

| Type | Condition | Formula |
|------|-----------|---------|
| Mean Proportional | a:b = b:c | b = √(ac) |
| Third Proportional | a:b = b:x | x = b²/a |
| Fourth Proportional | a:b = c:x | x = bc/a |

---

## 4. Variation

### 4.1 Direct Variation (Direct Proportion)

When two quantities increase/decrease together.

```
y ∝ x  →  y = kx  (k = constant of proportionality)
```

**Analogy**: More workers → More work done (assuming equal efficiency)

**Formula**: y₁/x₁ = y₂/x₂

**Example**: If 5 pens cost ₹40, what do 8 pens cost?
- Cost ∝ Pens
- 40/5 = x/8
- x = ₹64

### 4.2 Inverse Variation (Inverse Proportion)

When one quantity increases, the other decreases proportionally.

```
y ∝ 1/x  →  xy = k (constant)
```

**Analogy**: More workers → Less time to complete same work

**Formula**: x₁ × y₁ = x₂ × y₂

**Example**: 6 workers finish a job in 10 days. How many days for 15 workers?
- Workers × Days = constant
- 6 × 10 = 15 × d
- d = 60/15 = 4 days

### 4.3 Joint Variation

Quantity varies with two or more variables.

```
z ∝ xy  →  z = kxy
```

**Example**: Work done ∝ (Number of workers) × (Hours worked)

### 4.4 Combined Variation

Mix of direct and inverse variation.

```
z ∝ x/y  →  z = kx/y
```

**Example**: Speed ∝ Distance/Time

### Variation Identification Trick

| Keyword in Problem | Type of Variation |
|-------------------|-------------------|
| "varies as", "proportional to" | Direct |
| "inversely proportional", "varies inversely" | Inverse |
| "jointly varies" | Joint |
| Combination of above | Combined |

---

## 5. Quick Tricks & Shortcuts

### Trick 1: Ratio Distribution Formula

If total T is divided in ratio a:b:c, the parts are:
```
First part = T × a/(a+b+c)
Second part = T × b/(a+b+c)
Third part = T × c/(a+b+c)
```

**Example**: ₹1200 divided in 3:4:5
- First: 1200 × 3/12 = ₹300
- Second: 1200 × 4/12 = ₹400
- Third: 1200 × 5/12 = ₹500

### Trick 2: Combining Two Ratios (Bridge Method)

To combine A:B = 2:3 and B:C = 4:5, make B common:
```
A:B = 2:3 = 8:12  (multiply by 4)
B:C = 4:5 = 12:15 (multiply by 3)
∴ A:B:C = 8:12:15
```

### Trick 3: Component & Dividendo

If a/b = c/d, then:

| Name | Formula |
|------|---------|
| **Componendo** | (a+b)/b = (c+d)/d |
| **Dividendo** | (a-b)/b = (c-d)/d |
| **Componendo-Dividendo** | (a+b)/(a-b) = (c+d)/(c-d) |

**Super Useful For**: When sum/difference is given along with ratio.

**Example**: If (a+b):(a-b) = 5:3, find a:b
- Using Componendo-Dividendo in reverse:
- a+b = 5k, a-b = 3k
- Adding: 2a = 8k → a = 4k
- Subtracting: 2b = 2k → b = k
- a:b = 4:1

### Trick 4: Income/Expenditure/Savings

If Income ratio = a:b and Expenditure ratio = c:d, and both save equal amount S:

```
Income₁ - Expenditure₁ = Income₂ - Expenditure₂ = S
```

Set up equations:
- ax - cx' = S
- bx - dx' = S

Solve for x and x' to find actual values.

### Trick 5: Partnership Ratio

If partners invest in ratio a:b for times t₁:t₂:

```
Profit sharing ratio = (a×t₁) : (b×t₂)
```

**Example**: A invests ₹5000 for 4 months, B invests ₹4000 for 6 months.
- Profit ratio = 5000×4 : 4000×6 = 20000:24000 = 5:6

### Trick 6: Mixture & Alligation

To find mixing ratio when mixing two things of different values:

```
Mixing ratio = (Higher value - Mean) : (Mean - Lower value)
```

**Visual Method (Alligation Cross)**:
```
Value 1         Value 2
    \           /
      \       /
        Mean
      /       \
    /           \
(V2-M)        (M-V1)

Ratio = (Value2 - Mean) : (Mean - Value1)
```

**Example**: Mix 20% and 50% alcohol to get 30%
- Ratio = (50-30):(30-20) = 20:10 = 2:1

### Trick 7: Successive Ratio Changes

If original ratio a:b changes by adding x to each:

```
New ratio = (a+x):(b+x)
```

If original ratio a:b changes by multiplying by m:n:

```
New ratio = am:bn
```

### Trick 8: Finding Original Quantities from Ratio

If a:b = m:n and difference = d:

```
a = m×d/(m-n), b = n×d/(m-n)  [when m > n]
```

If a:b = m:n and sum = s:

```
a = m×s/(m+n), b = n×s/(m+n)
```

---

## 6. Common Mistakes & Edge Cases

### ❌ Mistake 1: Ignoring Order

**Wrong**: Treating 3:4 same as 4:3
**Right**: Order matters! a:b ≠ b:a (unless a = b)

### ❌ Mistake 2: Adding Ratios Incorrectly

**Wrong**: a:b + c:d = (a+c):(b+d)
**Right**: Convert to same base first, then compare

**Note**: (a+c):(b+d) gives a valid ratio but NOT the sum of two ratios. This is the **Weighted Average** effect.

### ❌ Mistake 3: Confusing Ratio vs Fraction

If boys:girls = 3:4, then:
- Boys/Total = 3/7 (not 3/4)
- Boys/Girls = 3/4

### ❌ Mistake 4: Direct vs Inverse Confusion

**Identify correctly**:
- More workers, less time → Inverse
- More speed, less time → Inverse  
- More distance, more time → Direct

### ❌ Mistake 5: Percentage in Ratios

If a:b = 4:5, then:
- a is NOT 80% of b
- a = (4/5)×b = 80% of b ✓
- a is 4/9 = 44.44% of total
- b is 5/9 = 55.56% of total

### Edge Case 1: Negative Ratios

Ratios are typically positive, but in some contexts (temperature, profit/loss):
- Profit:Loss = 3:(-2) is possible
- Handle sign carefully

### Edge Case 2: Zero in Ratio

- a:0 is undefined (division by zero)
- 0:b = 0 (meaningful in some contexts)

### Edge Case 3: Ratio of Same Quantities

a:a = 1:1 always, regardless of value of a (where a ≠ 0)

### Edge Case 4: Combining Unequal Bases

When A:B and C:D are given but B ≠ C, you CANNOT directly chain them.
Find a common link or additional information.

---

## 7. GATE/ESE Pattern Questions

### Pattern 1: Basic Ratio Division

**Q**: A sum of ₹7800 is divided among A, B, and C such that A's share is 3/4 of B's share and B's share is 2/3 of C's share. Find each share.

**Solution**:
- Let C's share = x
- B's share = (2/3)x
- A's share = (3/4)(2/3)x = (1/2)x
- Ratio A:B:C = (1/2)x : (2/3)x : x = 3:4:6
- Sum = 13 units = ₹7800
- Each unit = ₹600
- A = ₹1800, B = ₹2400, C = ₹3600

---

### Pattern 2: Componendo-Dividendo Application

**Q**: If (3a + 5b)/(3a - 5b) = 5/3, find a:b.

**Solution**:
- Apply Componendo-Dividendo:
- [(3a+5b)+(3a-5b)] / [(3a+5b)-(3a-5b)] = (5+3)/(5-3)
- 6a/10b = 8/2
- 6a/10b = 4
- a/b = 40/6 = 20/3
- **a:b = 20:3**

---

### Pattern 3: Age Problems with Ratio

**Q**: Present ages of A and B are in ratio 4:5. After 5 years, ratio becomes 5:6. Find present ages.

**Solution**:
- Let present ages = 4x and 5x
- After 5 years: (4x+5):(5x+5) = 5:6
- 6(4x+5) = 5(5x+5)
- 24x + 30 = 25x + 25
- x = 5
- Present ages: A = 20 years, B = 25 years

---

### Pattern 4: Mixture Problems

**Q**: In what ratio should water be mixed with milk costing ₹24/litre to get mixture worth ₹18/litre?

**Solution**:
- Using Alligation:
- Water cost = ₹0, Milk cost = ₹24, Mean = ₹18
- Ratio = (24-18):(18-0) = 6:18 = 1:3
- **Water:Milk = 1:3**

---

### Pattern 5: Partnership with Variable Investment

**Q**: A starts business with ₹45000. B joins after 3 months with ₹30000. At end of year, profit is ₹56000. Find each share.

**Solution**:
- A's investment-time = 45000 × 12 = 540000
- B's investment-time = 30000 × 9 = 270000
- Ratio = 540000:270000 = 2:1
- A's share = 56000 × 2/3 = ₹37333.33
- B's share = 56000 × 1/3 = ₹18666.67

---

### Pattern 6: Inverse Proportion Application

**Q**: 20 men can complete work in 24 days working 8 hours/day. How many hours/day must 30 men work to complete in 16 days?

**Solution**:
- Total work = Men × Days × Hours = 20 × 24 × 8 = 3840 man-hours
- For 30 men in 16 days: 30 × 16 × h = 3840
- h = 3840/480 = **8 hours/day**

---

### Pattern 7: Successive Changes in Ratio

**Q**: Ratio of A's and B's salaries is 3:4. If each gets ₹5000 increase, new ratio is 4:5. Find original salaries.

**Solution**:
- Let original salaries = 3x and 4x
- (3x + 5000)/(4x + 5000) = 4/5
- 5(3x + 5000) = 4(4x + 5000)
- 15x + 25000 = 16x + 20000
- x = 5000
- Original salaries: A = ₹15000, B = ₹20000

---

### Pattern 8: Three-Variable Ratio Chain

**Q**: If A:B = 2:3, B:C = 4:5, and C:D = 6:7, find A:B:C:D.

**Solution**:
- A:B = 2:3 = 8:12 (×4)
- B:C = 4:5 = 12:15 (×3)
- A:B:C = 8:12:15
- Now C = 15, but C:D = 6:7
- Make C common: 15 = 6×2.5, so D = 7×2.5 = 17.5
- Multiply all by 2: A:B:C:D = **16:24:30:35**

---

## 8. Formula Quick Reference

### Ratio Basics
```
a:b = a/b = ak:bk (any k ≠ 0)
```

### Compound Operations
| Operation | Result |
|-----------|--------|
| (a:b) × (c:d) | ac:bd |
| (a:b)² | a²:b² |
| (a:b)³ | a³:b³ |
| √(a:b) | √a:√b |
| ∛(a:b) | ∛a:∛b |
| 1/(a:b) | b:a |

### Proportionality
```
a:b = c:d  ⟹  ad = bc

Mean Proportional of a,c = √(ac)
Third Proportional of a,b = b²/a
Fourth Proportional of a,b,c = bc/a
```

### Variation
```
Direct:  y = kx  ⟹  y₁/x₁ = y₂/x₂
Inverse: xy = k  ⟹  x₁y₁ = x₂y₂
Joint:   z = kxy
```

### Componendo-Dividendo
```
If a/b = c/d, then:
(a+b)/(a-b) = (c+d)/(c-d)
```

### Division Formula
```
If T divided in a:b:c
Part₁ = T×a/(a+b+c)
Part₂ = T×b/(a+b+c)
Part₃ = T×c/(a+b+c)
```

### Alligation
```
Ratio = (V₂ - Mean):(Mean - V₁)
```

---

## Memory Hooks 🧠

| Concept | Memory Hook |
|---------|-------------|
| Componendo | "**C**omponendo = a**C**ts on both" (adds b to a, d to c) |
| Mean Proportional | "**M**ean is in **M**iddle" - √(ac) sits between a and c |
| Direct Variation | "**D**irect = **D**ancing together" (both move same direction) |
| Inverse Variation | "**I**nverse = **I**nversely linked" (one up, one down) |
| Alligation | "**A**lligation = **A**cross subtraction" (cross subtract from mean) |

---

## Practice Problems (Self-Assessment)

1. If 2A = 3B = 4C, find A:B:C.

2. ₹2430 is divided among A, B, C such that A gets 2/3 of what B gets, and B gets 3/4 of what C gets. Find each share.

3. The ratio of speeds of two trains is 7:8. If second train covers 400 km in 4 hours, find speed of first train.

4. Milk and water in vessel are in ratio 5:2. How much mixture must be drawn off and replaced with water to make ratio 5:4?

5. Present ratio of ages of A and B is 6:7. After 8 years, ratio will be 8:9. Find present ages.

<details>
<summary><b>Click for Answers</b></summary>

1. **A:B:C = 6:4:3**
   - 2A = 3B = 4C = k
   - A = k/2, B = k/3, C = k/4
   - A:B:C = 1/2 : 1/3 : 1/4 = 6:4:3

2. **A = ₹540, B = ₹810, C = ₹1080**
   - C = x, B = 3x/4, A = (2/3)(3x/4) = x/2
   - Ratio = 1/2 : 3/4 : 1 = 2:3:4
   - Total = 9 units = 2430, each unit = 270

3. **87.5 km/hr**
   - Second train speed = 400/4 = 100 km/hr
   - 7:8 = x:100
   - x = 700/8 = 87.5 km/hr

4. **Answer: 2/7 of the mixture must be drawn off and replaced**
   - Let vessel have 7 litres total (5L milk + 2L water)
   - Let y litres be drawn off and replaced with water
   - Milk removed = y × (5/7) = 5y/7
   - Water removed = y × (2/7) = 2y/7
   - Milk remaining = 5 - 5y/7 = (35 - 5y)/7
   - Water after replacement = 2 - 2y/7 + y = (14 - 2y + 7y)/7 = (14 + 5y)/7
   - New ratio: (35 - 5y):(14 + 5y) = 5:4
   - Cross multiply: 4(35 - 5y) = 5(14 + 5y)
   - 140 - 20y = 70 + 25y
   - 70 = 45y → y = 70/45 = 14/9
   - Fraction replaced = y/7 = (14/9)/7 = 14/63 = **2/9 of the mixture**

5. **A = 24 years, B = 28 years**
   - Let ages = 6x, 7x
   - After 8 years: (6x+8):(7x+8) = 8:9
   - Cross multiply: 9(6x+8) = 8(7x+8)
   - 54x + 72 = 56x + 64
   - 72 - 64 = 56x - 54x → 8 = 2x → x = 4
   - Present ages: A = 6×4 = 24 years, B = 7×4 = 28 years
   - Verify: After 8 years → 32:36 = 8:9 ✓

</details>

---

## Final Tips for GATE/ESE

1. ✅ **Always simplify** ratios to lowest terms
2. ✅ **Check units** - ratios of different units are meaningless
3. ✅ **Identify proportion type** before applying formula
4. ✅ **Use Componendo-Dividendo** for complex fraction equations
5. ✅ **Draw alligation cross** for mixture problems
6. ✅ **Convert to equations** when stuck - let a:b = x:y means a/b = x/y

---

*Last Updated: December 2025*  
*For GATE CSE, ECE, ME & ESE Aspirants*
