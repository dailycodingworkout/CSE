# Simple Interest & Compound Interest - The Complete Guide

> **For GATE & ESE | Genius-Level Notes | Zero to Mastery**

---

## 📚 Table of Contents
1. [Core Philosophy: Why Interest Exists](#core-philosophy)
2. [Simple Interest (SI)](#simple-interest)
3. [Compound Interest (CI)](#compound-interest)
4. [SI vs CI: The Critical Difference](#si-vs-ci)
5. [Master Formulas with Derivations](#master-formulas)
6. [Lightning Tricks & Shortcuts](#tricks)
7. [Edge Cases & Traps](#edge-cases)
8. [GATE-Level Problem Patterns](#problem-patterns)
9. [Cheat Sheet](#cheat-sheet)

---

<a name="core-philosophy"></a>
## 1. 🧠 Core Philosophy: Why Interest Exists

### The Fundamental Truth
**Money has time value.** ₹100 today is worth MORE than ₹100 one year later.

**Why?**
- **Opportunity Cost**: That ₹100 could be invested elsewhere
- **Inflation**: Purchasing power decreases over time
- **Risk**: Future is uncertain

> **Analogy**: Think of money as a seed. If you plant it today (invest), it grows into a tree (returns). If you keep it in your pocket, it stays a seed while others' trees are growing.

### The Core Variables
| Symbol | Meaning | Unit |
|--------|---------|------|
| **P** | Principal (initial amount) | Currency (₹) |
| **R** | Rate of interest | % per annum |
| **T** or **N** | Time period | Years |
| **A** | Amount (Principal + Interest) | Currency (₹) |
| **I** | Interest earned | Currency (₹) |

**Golden Relationship**: 
```
A = P + I
```

---

<a name="simple-interest"></a>
## 2. 💰 Simple Interest (SI)

### What is SI?
Interest calculated **ONLY on the original principal** — never on accumulated interest.

> **Analogy**: Imagine a cow that gives 1 liter milk daily. SI is like getting milk only from this one cow forever. The milk she produces doesn't create new cows.

### The Formula & Its Derivation

```
SI = (P × R × T) / 100
```

**Why divide by 100?** Because R is in percentage. 
- If R = 5%, then R/100 = 0.05 (the actual multiplier)

**Derivation Logic:**
- Interest for 1 year at R% = P × (R/100)
- Interest for T years = P × (R/100) × T
- Therefore: **SI = PRT/100**

### Amount Formula
```
A = P + SI = P + (PRT/100) = P(1 + RT/100)
```

### Visual Understanding

**Year-by-Year Growth (P = ₹1000, R = 10%)**

| Year | Principal | Interest This Year | Total Interest | Amount |
|------|-----------|-------------------|----------------|--------|
| 0 | 1000 | 0 | 0 | 1000 |
| 1 | 1000 | 100 | 100 | 1100 |
| 2 | 1000 | 100 | 200 | 1200 |
| 3 | 1000 | 100 | 300 | 1300 |

**Key Insight**: Interest per year is CONSTANT (₹100 each year)

### Quick Examples

**Example 1**: Find SI on ₹5000 at 8% for 3 years.
```
SI = (5000 × 8 × 3) / 100 = ₹1200
```

**Example 2**: If SI on a sum for 4 years at 5% is ₹800, find the principal.
```
800 = (P × 5 × 4) / 100
P = 80000/20 = ₹4000
```

---

<a name="compound-interest"></a>
## 3. 📈 Compound Interest (CI)

### What is CI?
Interest calculated on **Principal + Accumulated Interest** — interest earns interest!

> **Analogy**: The cow that gives milk, and that milk is sold to buy another cow. Now both cows give milk. This continues — exponential growth!

### The Formula & Its Derivation

```
A = P(1 + R/100)^n
CI = A - P = P[(1 + R/100)^n - 1]
```

**Derivation (Step by Step):**

Let's derive it intuitively for n years:

| End of Year | Amount |
|-------------|--------|
| Year 1 | P + P(R/100) = P(1 + R/100) |
| Year 2 | P(1 + R/100) + P(1 + R/100)(R/100) = P(1 + R/100)² |
| Year 3 | P(1 + R/100)² × (1 + R/100) = P(1 + R/100)³ |
| Year n | **P(1 + R/100)ⁿ** |

### Visual Understanding

**Year-by-Year Growth (P = ₹1000, R = 10%)**

| Year | Opening Balance | Interest This Year | Amount |
|------|-----------------|-------------------|--------|
| 0 | 1000 | 0 | 1000 |
| 1 | 1000 | 100.00 | 1100.00 |
| 2 | 1100 | 110.00 | 1210.00 |
| 3 | 1210 | 121.00 | 1331.00 |

**Key Insight**: Interest per year INCREASES (100 → 110 → 121)

### Compounding Frequency

When interest compounds **n times per year** at annual rate R:

```
A = P(1 + R/(100×n))^(n×T)
```

| Compounding | n | Formula |
|-------------|---|---------|
| Annually | 1 | P(1 + R/100)^T |
| Half-yearly | 2 | P(1 + R/200)^(2T) |
| Quarterly | 4 | P(1 + R/400)^(4T) |
| Monthly | 12 | P(1 + R/1200)^(12T) |
| Continuously | ∞ | Pe^(RT/100) |

> **Insight**: More frequent compounding = More total interest (but diminishing returns)

### Quick Example

**Example**: Find CI on ₹10000 at 10% for 2 years compounded annually.
```
A = 10000(1 + 10/100)² = 10000 × 1.21 = ₹12100
CI = 12100 - 10000 = ₹2100
```

Compare with SI = (10000 × 10 × 2)/100 = ₹2000

**Difference = ₹100** (This is interest on first year's interest)

---

<a name="si-vs-ci"></a>
## 4. ⚔️ SI vs CI: The Critical Difference

### Head-to-Head Comparison

| Aspect | Simple Interest | Compound Interest |
|--------|-----------------|-------------------|
| Interest Base | Only Principal | Principal + Accumulated Interest |
| Growth Pattern | Linear | Exponential |
| Formula | PRT/100 | P[(1+R/100)ⁿ - 1] |
| For n=1 year | **SAME** | **SAME** |
| For n>1 years | Less | More |

### The Magic Formula: CI - SI

For **2 years**:
```
CI - SI = P(R/100)² = SI × R / (2 × 100)
```

**Why?** 
- SI for 2 years = 2PR/100
- CI for 2 years = P(1+R/100)² - P = 2PR/100 + P(R/100)²
- Difference = P(R/100)² = Interest on first year's interest!

For **3 years**:
```
CI - SI = P(R/100)² × (3 + R/100)
```

### Graphical Intuition

```
Amount
  ↑
  |                    ....CI (curve - exponential)
  |              .....
  |         ....
  |     ...________-------- SI (straight line)
  | ...--------
  |________________________________________→ Time
```

> **Key Insight**: For short durations, SI ≈ CI. The gap widens significantly for longer periods.

---

<a name="master-formulas"></a>
## 5. 🔧 Master Formulas with Derivations

### Essential SI Formulas

| To Find | Formula |
|---------|---------|
| SI | PRT/100 |
| P | (SI × 100)/(R × T) |
| R | (SI × 100)/(P × T) |
| T | (SI × 100)/(P × R) |
| A | P(1 + RT/100) |

### Essential CI Formulas

| To Find | Formula |
|---------|---------|
| A | P(1 + R/100)ⁿ |
| CI | P[(1 + R/100)ⁿ - 1] |
| P | A/(1 + R/100)ⁿ |

### Population/Depreciation Applications

**Growth** (Population, Price Increase):
```
Final = Initial × (1 + R/100)ⁿ
```

**Decay** (Depreciation, Value Decrease):
```
Final = Initial × (1 - R/100)ⁿ
```

**Mixed Rates** (Different rates for different years R₁, R₂, R₃):
```
Final = P × (1 + R₁/100) × (1 + R₂/100) × (1 + R₃/100)
```

### Effective Annual Rate (EAR)

When compounded n times per year:
```
EAR = (1 + R/(100n))ⁿ - 1
```

**Example**: 12% compounded monthly
```
EAR = (1 + 12/1200)¹² - 1 = (1.01)¹² - 1 ≈ 12.68%
```

### Present Value (PV)

The principal that will grow to Amount A in n years:
```
PV = A / (1 + R/100)ⁿ
```

---

<a name="tricks"></a>
## 6. ⚡ Lightning Tricks & Shortcuts

### Trick 1: The Rule of 72 (Doubling Time)

**Time to double money ≈ 72/R years** (for CI)

| Rate | Doubling Time |
|------|--------------|
| 6% | 12 years |
| 8% | 9 years |
| 12% | 6 years |
| 24% | 3 years |

**Why 72?** It's an approximation of 100×ln(2) ≈ 69.3, rounded to 72 for easy division.

### Trick 2: Tripling Time

**Time to triple ≈ 115/R years** (for CI)

### Trick 3: Quick CI Calculation for 2 Years

```
CI = 2 × (Simple Interest for 1 year) + (SI for 1 year × R/100)
```

**Example**: P = ₹10000, R = 10%, n = 2
- SI for 1 year = 1000
- CI = 2(1000) + 1000(10/100) = 2000 + 100 = ₹2100 ✓

### Trick 4: Interest Ratio Method

If amounts become A₁ and A₂ after n and (n+1) years respectively:
```
R = (A₂ - A₁) × 100 / A₁
```

### Trick 5: Installment Formula

For **n equal annual installments** of amount I each to repay loan P at R%:

```
P = I/(1+R/100) + I/(1+R/100)² + ... + I/(1+R/100)ⁿ
P = I × [(1+R/100)ⁿ - 1] / [R/100 × (1+R/100)ⁿ]
```

### Trick 6: SI and CI are Equal for Year 1

**Always true**: SI₁ = CI₁

Use this to verify calculations or solve problems.

### Trick 7: Percentage Increase Method for CI

For 2 years at R%:
```
Effective Rate = 2R + R²/100
```

**Example**: 10% for 2 years
- Effective = 2(10) + 100/100 = 21%
- On ₹10000: CI = 2100 ✓

### Trick 8: Monthly to Annual Conversion

If monthly rate is r%, annual CI:
```
A = P(1 + r/100)¹²
```

### Trick 9: The "Plus 1" Pattern

(1 + R/100)² = 1 + 2R/100 + R²/10000

For small R, the R²/10000 term is negligible → Quick mental math!

---

<a name="edge-cases"></a>
## 7. 🚨 Edge Cases & Common Traps

### Edge Case 1: Time in Months
Always convert to years: T = months/12

**Trap**: Given T = 6 months, R = 12% → T = 0.5 years, not 6!

### Edge Case 2: Rate Given Per Month
If R = 2% per month and T = 6 months:
- For SI: SI = P × 2 × 6 / 100 (use monthly rate directly)
- For CI: A = P(1.02)⁶

### Edge Case 3: Half-Yearly vs Annually

**Trap Question**: "10% compounded half-yearly for 1 year" ≠ "10% compounded annually"

Half-yearly: A = P(1.05)² = 1.1025P (Effective: 10.25%)
Annually: A = P(1.10) = 1.10P

### Edge Case 4: Days Given as Time

Convert carefully:
- 73 days = 73/365 years = 1/5 year
- Look for "banker's year" (360 days in exams)

### Edge Case 5: When Principal Changes

If additional deposit or withdrawal happens:
- Calculate interest up to that point
- Adjust principal
- Calculate interest for remaining period

### Edge Case 6: Fraction in Rate or Time

R = 12.5% = 25/2%
T = 2½ years = 5/2 years

Keep as fractions for clean calculations!

### Edge Case 7: SI = CI Condition

SI = CI **only when n = 1 year**

If someone claims SI = CI for multiple years, it's wrong (unless R = 0%).

### Edge Case 8: Negative Rates (Depreciation)

When value decreases:
```
Final = Initial × (1 - R/100)ⁿ
```

**Don't use**: (1 + R/100)ⁿ for depreciation!

### Common Mistakes to Avoid

1. **Forgetting to convert percentage**: R = 5% means use 5, not 0.05 in PRT/100
2. **Time unit mismatch**: If R is annual, T must be in years
3. **Confusing Amount and Interest**: A = P + I, not I
4. **Wrong compounding formula**: For half-yearly at R%, use R/2 for 2n periods
5. **Applying SI formula to CI problems**: Read carefully!

---

<a name="problem-patterns"></a>
## 8. 📝 GATE-Level Problem Patterns

### Pattern 1: Find Missing Variable

**Problem**: The SI on a sum for 4 years at 8% p.a. equals ₹1280. Find the sum.

**Solution**:
```
SI = PRT/100
1280 = P × 8 × 4 / 100
P = 128000/32 = ₹4000
```

### Pattern 2: CI - SI Difference

**Problem**: The difference between CI and SI on ₹8000 for 2 years is ₹20. Find the rate.

**Solution**:
```
CI - SI = P(R/100)²
20 = 8000 × R² / 10000
R² = 25
R = 5%
```

### Pattern 3: Ratio Problems

**Problem**: SI on a sum at 6% for 3 years = CI on same sum at 6% for 2 years. Find the sum.

**Solution**:
```
P × 6 × 3 / 100 = P[(1.06)² - 1]
18P/100 = P × 0.1236
18/100 = 0.1236
```
This gives contradiction → Such P doesn't exist (verify carefully in exam!)

### Pattern 4: Population Growth

**Problem**: A town's population increases 10% annually. If current population is 20000, find population after 3 years.

**Solution**:
```
Final = 20000 × (1.1)³ = 20000 × 1.331 = 26620
```

### Pattern 5: Depreciation

**Problem**: A car worth ₹500000 depreciates 15% annually. Find value after 2 years.

**Solution**:
```
Value = 500000 × (0.85)² = 500000 × 0.7225 = ₹361250
```

### Pattern 6: Effective Rate

**Problem**: What is the effective annual rate if 8% is compounded quarterly?

**Solution**:
```
EAR = (1 + 8/400)⁴ - 1 = (1.02)⁴ - 1 = 1.0824 - 1 = 8.24%
```

### Pattern 7: Present Value

**Problem**: What sum will amount to ₹13310 in 3 years at 10% CI?

**Solution**:
```
P = 13310/(1.1)³ = 13310/1.331 = ₹10000
```

### Pattern 8: Time to Reach Target

**Problem**: In how many years will ₹5000 become ₹6655 at 10% CI?

**Solution**:
```
6655 = 5000(1.1)ⁿ
(1.1)ⁿ = 1.331 = (1.1)³
n = 3 years
```

### Pattern 9: Equal Installments

**Problem**: A loan of ₹10000 at 10% CI is to be repaid in 2 equal annual installments. Find installment amount.

**Solution**:
```
Let installment = I
10000 = I/1.1 + I/1.21
10000 = I(1.1 + 1)/1.21 = 2.1I/1.21
I = 10000 × 1.21/2.1 = ₹5762 (approximately)
```

### Pattern 10: Multiple Rates

**Problem**: Find CI on ₹20000 for 3 years if rates are 5%, 10%, 15% for consecutive years.

**Solution**:
```
A = 20000 × 1.05 × 1.10 × 1.15 = 20000 × 1.32825 = ₹26565
CI = 26565 - 20000 = ₹6565
```

---

<a name="cheat-sheet"></a>
## 9. 📋 Ultimate Cheat Sheet

### Core Formulas (Memorize These!)

```
┌─────────────────────────────────────────────────────────────┐
│ SIMPLE INTEREST                                             │
│ ─────────────────                                           │
│ SI = PRT/100                                                │
│ A = P(1 + RT/100)                                           │
│ P = (100 × SI)/(R × T)                                      │
├─────────────────────────────────────────────────────────────┤
│ COMPOUND INTEREST                                           │
│ ─────────────────                                           │
│ A = P(1 + R/100)ⁿ           [Annual]                        │
│ A = P(1 + R/200)²ⁿ          [Half-yearly]                   │
│ A = P(1 + R/400)⁴ⁿ          [Quarterly]                     │
│ CI = A - P                                                  │
├─────────────────────────────────────────────────────────────┤
│ CI - SI DIFFERENCE                                          │
│ ─────────────────                                           │
│ 2 years: CI - SI = P(R/100)²                                │
│ 3 years: CI - SI = P(R/100)²(3 + R/100)                     │
├─────────────────────────────────────────────────────────────┤
│ GROWTH & DEPRECIATION                                       │
│ ─────────────────────                                       │
│ Growth: Final = Initial × (1 + R/100)ⁿ                      │
│ Decay:  Final = Initial × (1 - R/100)ⁿ                      │
├─────────────────────────────────────────────────────────────┤
│ QUICK RULES                                                 │
│ ───────────                                                 │
│ Rule of 72: Doubling time ≈ 72/R years                      │
│ Rule of 115: Tripling time ≈ 115/R years                    │
│ For n=1: SI = CI (Always!)                                  │
│ Effective 2-year rate: 2R + R²/100                          │
└─────────────────────────────────────────────────────────────┘
```

### Power Values (Pre-Calculate!)

| (1.05)² = 1.1025 | (1.10)² = 1.21   | (1.15)² = 1.3225 |
|------------------|------------------|------------------|
| (1.05)³ = 1.1576 | (1.10)³ = 1.331  | (1.15)³ = 1.5209 |
| (1.05)⁴ = 1.2155 | (1.10)⁴ = 1.4641 | (1.20)² = 1.44   |

### Decimal Equivalents

| Fraction | Decimal | % |
|----------|---------|---|
| 1/2 | 0.5 | 50% |
| 1/3 | 0.333 | 33.33% |
| 1/4 | 0.25 | 25% |
| 1/5 | 0.2 | 20% |
| 1/6 | 0.167 | 16.67% |
| 1/8 | 0.125 | 12.5% |
| 1/10 | 0.1 | 10% |
| 1/12 | 0.0833 | 8.33% |
| 1/20 | 0.05 | 5% |

### Problem-Solving Approach

```
1. READ: Identify SI or CI? What's given? What's asked?
2. CONVERT: Units consistent? (R annual, T in years)
3. SELECT: Choose appropriate formula
4. CALCULATE: Use tricks for speed
5. VERIFY: Does answer make sense? (CI > SI for n > 1)
```

---

## 🎯 Final Tips for GATE/ESE

1. **Time Management**: SI/CI questions should take ≤2 minutes
2. **Calculator Dependency**: Practice mental math for small numbers
3. **Memorize Powers**: (1.1)², (1.1)³, etc. are frequently needed
4. **Watch Units**: Always verify rate and time units match
5. **Read Carefully**: "Compounded" vs "Simple" changes everything
6. **Approximation**: For MCQs, use Rule of 72 to eliminate options quickly

---

*Last Updated: 2024 | For GATE & ESE Aspirants*
*Created with ❤️ for Future Engineers*
