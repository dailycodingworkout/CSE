# 📊 Percentages | The Singularity

> **The Atomic Truth:** *Percentage = Parts per hundred, a ratio normalized to 100.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Percentage Conversions](#percentage-conversions)
3. [Percentage Change](#percentage-change)
4. [Successive Percentage Changes](#successive-percentage-changes)
5. [Percentage Points vs Percentage](#percentage-points-vs-percentage)
6. [Applications in Real Problems](#applications-in-real-problems)
7. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
8. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Percentages Matter?
Percentages are the **universal language of comparison**. They appear in:
- Profit & Loss calculations
- Interest computations
- Data Interpretation
- Growth rate analysis
- Population/production changes

### The Basic Definition

$$\text{Percentage} = \frac{\text{Part}}{\text{Whole}} \times 100\%$$

**Three Core Formulas:**
1. $x\% \text{ of } y = \frac{x \times y}{100}$
2. $x \text{ is what } \% \text{ of } y = \frac{x}{y} \times 100\%$
3. $x \text{ is } p\% \text{ more than } y \Rightarrow x = y\left(1 + \frac{p}{100}\right)$

---

## Percentage Conversions

### Master Fraction-to-Percentage Table

| Fraction | Percentage | Fraction | Percentage |
|----------|------------|----------|------------|
| 1/2 | 50% | 1/11 | 9.09% |
| 1/3 | 33.33% | 1/12 | 8.33% |
| 2/3 | 66.67% | 1/13 | 7.69% |
| 1/4 | 25% | 1/14 | 7.14% |
| 3/4 | 75% | 1/15 | 6.67% |
| 1/5 | 20% | 1/16 | 6.25% |
| 2/5 | 40% | 1/17 | 5.88% |
| 3/5 | 60% | 1/18 | 5.56% |
| 4/5 | 80% | 1/19 | 5.26% |
| 1/6 | 16.67% | 1/20 | 5% |
| 5/6 | 83.33% | 1/25 | 4% |
| 1/7 | 14.28% | 1/30 | 3.33% |
| 1/8 | 12.5% | 1/40 | 2.5% |
| 3/8 | 37.5% | 1/50 | 2% |
| 5/8 | 62.5% | 1/100 | 1% |
| 7/8 | 87.5% | | |
| 1/9 | 11.11% | | |
| 1/10 | 10% | | |

> **💡 The Golden Pivot:** Memorize these! They save 15-20 seconds per question.

### Quick Conversion Trick

For $\frac{1}{n}$ as percentage:
- $\frac{1}{n} \times 100 = \frac{100}{n}$

For fractions like $\frac{a}{b}$:
- Find the known fraction closest to it
- Adjust mentally

---

## Percentage Change

### Increase/Decrease Formulas

**Percentage Increase:**
$$\text{Increase} \% = \frac{\text{New} - \text{Original}}{\text{Original}} \times 100\%$$

**Percentage Decrease:**
$$\text{Decrease} \% = \frac{\text{Original} - \text{New}}{\text{Original}} \times 100\%$$

### The Multiplier Concept

| Change | Multiplier | Calculation |
|--------|------------|-------------|
| +10% | 1.10 | × 1.1 |
| +25% | 1.25 | × 1.25 |
| +33.33% | 4/3 | × (4/3) |
| -10% | 0.90 | × 0.9 |
| -20% | 0.80 | × 0.8 |
| -25% | 0.75 | × 0.75 |
| -33.33% | 2/3 | × (2/3) |

**Example:** If price increases by 25%, new price = Original × 1.25

### Reverse Percentage

If $A$ is $p\%$ more than $B$, then $B$ is what percent less than $A$?

$$\text{Required } \% = \frac{p}{100 + p} \times 100$$

**Example:** If A is 25% more than B, B is less than A by:
$$\frac{25}{125} \times 100 = 20\%$$

### The Symmetry Breaker
> **Critical Insight:** +25% and -25% are NOT inverse operations!
> - 100 + 25% = 125
> - 125 - 25% = 93.75 ≠ 100

**To reverse a $p\%$ increase, decrease by:** $\frac{100p}{100+p}\%$

**To reverse a $p\%$ decrease, increase by:** $\frac{100p}{100-p}\%$

---

## Successive Percentage Changes

### The Net Effect Formula

If there are successive changes of $a\%$ and $b\%$:

$$\text{Net Change} = a + b + \frac{ab}{100}\%$$

**Example:** Two successive discounts of 10% each
$$\text{Net discount} = 10 + 10 + \frac{10 \times (-10)}{100} = 10 + 10 - 1 = 19\%$$

Wait, let's recalculate with both as discounts (negative):
$$\text{Net} = -10 + (-10) + \frac{(-10)(-10)}{100} = -19\%$$

So net discount is 19%, NOT 20%.

### Triple Successive Changes

For three changes $a\%$, $b\%$, $c\%$:

$$\text{Net} = \left[\left(1 + \frac{a}{100}\right)\left(1 + \frac{b}{100}\right)\left(1 + \frac{c}{100}\right) - 1\right] \times 100\%$$

### Population Growth Formula

$$P_n = P_0 \left(1 + \frac{r}{100}\right)^n$$

Where:
- $P_n$ = Population after $n$ years
- $P_0$ = Initial population
- $r$ = Growth rate per period

---

## Percentage Points vs Percentage

### The Critical Distinction

**Percentage Points:** Absolute difference between two percentages
**Percentage Change:** Relative change from original

**Example:**
- Market share increases from 20% to 25%
- Increase in percentage points = 25 - 20 = **5 percentage points**
- Percentage increase = $\frac{5}{20} \times 100 = 25\%$

> **⚠️ GATE Trap:** Questions often ask "by what percentage" vs "by how many percentage points"

---

## Applications in Real Problems

### Application 1: Price-Quantity Expenditure

$$\text{Expenditure} = \text{Price} \times \text{Quantity}$$

If price changes by $p\%$ and quantity changes by $q\%$:
$$\text{Change in Expenditure} = p + q + \frac{pq}{100}\%$$

**Example:** Price increases by 20%, consumption decreases by 10%
$$\text{Expenditure change} = 20 - 10 + \frac{20 \times (-10)}{100} = 10 - 2 = 8\%$$
Expenditure increases by 8%.

### Application 2: Election Problems

**Two-candidate election:**
- If winner gets $x\%$, loser gets $(100-x)\%$
- Winning margin = $(2x - 100)\%$ of total votes

**Example:** Winner gets 60% votes, margin = 2000
- Winning margin = 20% of total
- Total votes = 2000 × 100/20 = 10,000

### Application 3: Examination Problems

$$\text{Pass Marks} = (\text{Pass } \%) \times (\text{Maximum Marks})$$

**Example:** A student scores 180 marks and fails by 20 marks. Pass percentage is 40%. Find maximum marks.
- Pass marks = 180 + 20 = 200
- 40% of Max = 200
- Max = 500

### Application 4: Income-Expenditure-Savings

$$\text{Income} = \text{Expenditure} + \text{Savings}$$

**Example:** A person saves 20% of income. If expenses increase by 35% and income increases by 20%, find the percentage change in savings.

Let Income = 100
- Original: Expenditure = 80, Savings = 20
- New Income = 120
- New Expenditure = 80 × 1.35 = 108
- New Savings = 120 - 108 = 12
- Change in savings = $\frac{12-20}{20} \times 100 = -40\%$

---

## GATE & ESE Problem Patterns

### Pattern 1: Data Interpretation with Percentages
> In a company, if sales in 2024 were ₹500 crore and increased by 20% in 2025, what were 2025 sales?
- **Answer:** 500 × 1.2 = ₹600 crore

### Pattern 2: Complex Successive Changes
> A number is increased by 10%, then decreased by 10%, then increased by 25%. Net change?
- Multiplier = 1.1 × 0.9 × 1.25 = 1.2375
- Net increase = 23.75%

### Pattern 3: Percentage of Percentage
> What is 20% of 30% of 500?
- = 0.20 × 0.30 × 500 = 30

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"If A's salary is 20% less than B's, what percent is B's salary more than A's?"

Wrong approach: Answering 20% (symmetric thinking)

**The Elegant Solution:**
- Let B = 100, then A = 80
- B is more than A by = $\frac{100-80}{80} \times 100 = 25\%$

**MSQ Logic Gate:**
- When comparing "A is x% more than B" vs "B is y% less than A"
- $x$ and $y$ are NEVER equal unless both are 0

**NAT Precision Lock:**
- For non-terminating percentages (like 33.33%), round to 2 decimal places
- Watch for: 1/7 = 14.29% (not 14.28%), 1/6 = 16.67% (not 16.66%)

---

## Speed Tricks & Shortcuts

### Trick 1: The 1% Method
Find 1% first, then scale.
- 17% of 250 = 1% × 17 = 2.5 × 17 = 42.5

### Trick 2: Breaking Complex Percentages
- 23% of 400 = 20% + 3% = 80 + 12 = 92
- 17.5% of 600 = 15% + 2.5% = 90 + 15 = 105

### Trick 3: Decimal Shifts
- 10% = divide by 10
- 1% = divide by 100
- 5% = half of 10%
- 25% = divide by 4
- 50% = divide by 2

### Trick 4: Complementary Percentages
- If 65% passed, 35% failed (no calculation needed)

### Trick 5: The Fraction Path
- 37.5% = 3/8 (faster to compute for nice numbers)
- 62.5% = 5/8
- 87.5% = 7/8

---

## Permanent Recall

### The Bizarre Mnemonic (Successive Changes)
*"The percentage party: first invite $a$, then $b$, but they bring a small gift of $\frac{ab}{100}$ together."*

### The Mental Slider
Visualize a dial:
- Center = 100% (base)
- Clockwise = increase (multiplier > 1)
- Counter-clockwise = decrease (multiplier < 1)
- The dial position directly gives you the multiplier

### The 5-Second Snap-Check
- Net of +50% and -50% should NOT be 0% (it's -25%)
- Percentage answer should make logical sense (can't spend 110% without debt)

---

## Practice Problems

### Level 1: Fundamentals
1. What is 17.5% of 400?
2. If 35% of a number is 70, find the number.
3. A number is increased by 20% and then decreased by 20%. Find the net change.

### Level 2: GATE Standard
4. In an election, candidate A got 55% of votes. If A won by 4000 votes, find total votes.
5. A's income is 25% more than B's. B's income is what percent less than A's?
6. The price of a commodity increased by 40%. By what percent should consumption be reduced to keep expenditure constant?

### Level 3: IIT Examiner Level
7. A person's salary increases by 10% annually. After 3 years, what is the net percentage increase (to 2 decimal places)?
8. If x% of y equals y% of z, and y is 50% of z, find x as a percentage of z.
9. The population of a town increases by 5% annually. What was the population 2 years ago if it is 11025 now?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. 17.5% of 400 = 17.5 × 4 = **70**

2. 35% of x = 70 → x = 70 × 100/35 = **200**

3. Net = 20 - 20 + (20 × -20)/100 = -4%. **Decrease of 4%**

4. Winning margin = 55% - 45% = 10% of total = 4000
   Total votes = **40,000**

5. Let B = 100, A = 125
   B is less than A by = 25/125 × 100 = **20%**

6. Let original price = P, consumption = C
   New price = 1.4P
   For same expenditure: 1.4P × new C = P × C
   New C = C/1.4
   Reduction = (C - C/1.4)/C × 100 = (1 - 1/1.4) × 100 = 2/7 × 100 = **28.57%**

7. Multiplier = (1.1)³ = 1.331
   Net increase = **33.10%**

8. x% of y = y% of z
   xy/100 = yz/100 → x = z
   Since y = 0.5z
   x = z, so x is **100%** of z

9. P × (1.05)² = 11025
   P × 1.1025 = 11025
   P = **10,000**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Percentages with Profit & Loss for a Rank-1 simulation?
