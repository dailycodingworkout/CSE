# Chapter 4: Simple & Compound Interest

> **Time value of money - the mathematics of banking and finance**

---

## 🎯 Why Study This?

- Core topic in GATE/ESE aptitude section
- Foundation for financial calculations
- Real-world: Loans, investments, EMIs

---

## 📚 Fundamental Concept

**Interest** = Fee paid for borrowing money OR reward for lending money

**💡 Analogy**: Interest is the "rent" you pay for using someone else's money.

---

## 🔹 Simple Interest (SI)

### Core Concept

Interest is calculated only on the **original principal** throughout the period.

```
SI = (P × R × T) / 100

Where:
P = Principal (initial amount)
R = Rate of interest per annum (%)
T = Time in years
```

### Amount Formula

```
Amount (A) = Principal + Interest
A = P + SI = P + (PRT/100) = P(1 + RT/100)
```

---

### Derived Formulas

| To Find | Formula |
|---------|---------|
| Principal | P = (100 × SI)/(R × T) |
| Rate | R = (100 × SI)/(P × T) |
| Time | T = (100 × SI)/(P × R) |
| SI | A - P |

---

### Time Conversion

```
If time in months: T = months/12
If time in days: T = days/365
```

---

## 🔹 Compound Interest (CI)

### Core Concept

Interest is calculated on **principal + accumulated interest** (interest on interest).

```
A = P(1 + R/100)^T

CI = A - P = P[(1 + R/100)^T - 1]

Where:
P = Principal
R = Rate per annum (%)
T = Time in years
```

---

### Different Compounding Frequencies

| Compounding | Formula | Effective Rate |
|-------------|---------|----------------|
| Annually | P(1 + R/100)^T | R% |
| Half-yearly | P(1 + R/200)^(2T) | Higher than R% |
| Quarterly | P(1 + R/400)^(4T) | Higher still |
| Monthly | P(1 + R/1200)^(12T) | Even higher |
| n times/year | P(1 + R/(100n))^(nT) | Depends on n |

**⚡ Key Insight**: More frequent compounding = More interest earned/paid

---

### General Formula

```
A = P(1 + r/n)^(nt)

Where:
n = number of times interest compounds per year
t = time in years
r = annual interest rate (as decimal)
```

---

## ⚖️ SI vs CI Comparison

| Aspect | Simple Interest | Compound Interest |
|--------|-----------------|-------------------|
| Interest on | Principal only | Principal + Accumulated Interest |
| Growth | Linear | Exponential |
| Formula | P × R × T/100 | P[(1+R/100)^T - 1] |
| For T=1 year | SI = CI | SI = CI |
| For T>1 year | SI < CI | CI > SI |
| When used | Short-term loans | Savings, long-term loans |

---

## 🔗 Key Relationships

### Difference Between CI and SI

**For 2 years**:
```
CI - SI = P(R/100)² = PR²/10000
```

**For 3 years**:
```
CI - SI = P(R/100)²(3 + R/100) = PR²(300 + R)/1000000
```

**⚡ Shortcut for 2 years**: 
```
CI - SI = SI for first year × R/100
```

---

### Finding Rate When CI-SI is Given (2 years)

```
R = √((CI-SI)/P) × 100
```

Or if SI is given:
```
R = (CI - SI)/SI × 200
```

---

## 📊 Standard Problem Types

### Type 1: Basic Calculation

**Example**: Find CI on ₹10000 at 10% for 2 years
```
A = 10000(1 + 10/100)² = 10000 × 1.21 = 12100
CI = 12100 - 10000 = ₹2100
```

**Compare with SI**:
```
SI = 10000 × 10 × 2/100 = ₹2000
CI - SI = ₹100
```

---

### Type 2: Different Rates for Different Years

When rate is R₁% for first year, R₂% for second year:
```
A = P(1 + R₁/100)(1 + R₂/100)
```

**Example**: ₹5000 at 10% for first year, 12% for second year
```
A = 5000 × 1.10 × 1.12 = 6160
CI = ₹1160
```

---

### Type 3: Population/Value Growth

Same as CI formula:
```
Final = Initial × (1 + r/100)^n    (for growth)
Final = Initial × (1 - r/100)^n    (for decay/depreciation)
```

**Example**: Population 50000 grows at 5% p.a. for 3 years
```
Final = 50000 × (1.05)³ = 50000 × 1.157625 = 57881
```

---

### Type 4: Finding Time Period

**When does amount double at r% CI?**

Using Rule of 72 (approximation):
```
Time ≈ 72/r years
```

**Exact formula**:
```
n = log(2)/log(1 + r/100)
```

| Rate | Approx Time to Double |
|------|----------------------|
| 6% | 12 years |
| 8% | 9 years |
| 10% | 7.2 years |
| 12% | 6 years |
| 15% | 4.8 years |

---

### Type 5: Present Worth

**What principal gives Amount A after T years at R% CI?**
```
P = A / (1 + R/100)^T
```

**Example**: What sum will become ₹13310 in 3 years at 10% CI?
```
P = 13310/(1.1)³ = 13310/1.331 = ₹10000
```

---

### Type 6: Equal Installments

**To repay a loan P at r% in n equal annual installments**:
```
Each Installment = P × r(1+r)^n / [(1+r)^n - 1]

Where r = R/100
```

**Simpler approach**: If installment = X, then:
```
P = X/(1+r) + X/(1+r)² + ... + X/(1+r)^n
```

---

### Type 7: Mixed SI and CI

**SI for some years, CI for remaining**:
Calculate separately and add.

**Example**: ₹10000 at 10% SI for 2 years, then CI for next 2 years
```
After SI phase: 10000 + 2000 = ₹12000
After CI phase: 12000 × (1.1)² = ₹14520
Total Interest = ₹4520
```

---

## 💡 Advanced Tricks

### Trick 1: CI Calculation Without Formula

For 2 years at r%:
```
Year 1 interest = P × r/100
Year 2 interest = (P + Year 1 interest) × r/100
CI = Year 1 + Year 2 interest
```

---

### Trick 2: Quick CI for 2 Years

```
CI for 2 years = 2 × SI for 1 year + (SI for 1 year × r/100)
              = SI₁(2 + r/100)
```

**Example**: P = 1000, r = 10%, T = 2 years
```
SI₁ = 100
CI = 100 × (2 + 0.1) = 100 × 2.1 = 210
```

---

### Trick 3: Effective Annual Rate

When compounded n times per year at nominal rate r%:
```
Effective Rate = (1 + r/(100n))^n - 1
```

**Example**: 12% compounded monthly
```
Effective = (1 + 0.01)^12 - 1 = 1.1268 - 1 = 12.68%
```

---

### Trick 4: SI and CI Same for First Year

Use this to find Year 2 CI:
```
CI for 2nd year alone = SI + (SI × r/100)
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Rate and Time Units Must Match
```
If rate is per annum, time must be in years
If rate is per month, time must be in months
```

### Trap 2: Compounding Frequency
```
"10% compounded half-yearly" ≠ "10% compounded annually"
Half-yearly: P(1 + 5/100)² = P × 1.1025
Annually: P(1 + 10/100) = P × 1.1
```

### Trap 3: SI = CI only for T = 1
```
For T > 1 year, CI > SI (always)
```

### Trap 4: "Rate per annum" vs "Rate per period"
```
12% per annum compounded monthly
Rate per period = 12/12 = 1% per month
```

### Edge Case: Fractional Time Period in CI

For time = n years and m months at annual compounding:
```
A = P(1 + R/100)^n × (1 + (m/12) × R/100)
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| Simple Interest | PRT/100 |
| SI Amount | P(1 + RT/100) |
| Compound Interest | P[(1+R/100)^T - 1] |
| CI Amount | P(1+R/100)^T |
| CI - SI (2 years) | P(R/100)² |
| Half-yearly CI | P(1+R/200)^(2T) |
| Time to double (Rule of 72) | 72/R years |
| Present Worth | A/(1+R/100)^T |
| Effective Rate (n compounds) | (1+r/100n)^n - 1 |

---

## 📝 GATE-Level Practice

**Q1**: Difference between CI and SI on ₹8000 for 2 years at 5%?
```
CI - SI = P(R/100)² = 8000 × (5/100)² = 8000 × 0.0025 = ₹20
```

**Q2**: A sum doubles in 5 years at SI. Rate of interest?
```
SI = P (amount doubled, so SI = P)
P = P × R × 5/100
R = 20%
```

**Q3**: ₹1000 at 10% CI compounded half-yearly for 1 year. Find amount.
```
A = 1000(1 + 5/100)² = 1000 × 1.1025 = ₹1102.50
```

**Q4**: In what time will ₹1600 become ₹1852.20 at 5% CI?
```
1852.20/1600 = (1.05)^T
1.157625 = 1.05^T
1.05³ = 1.157625
T = 3 years
```

**Q5**: A machine depreciates 10% annually. Value after 3 years if initial = ₹50000?
```
Value = 50000 × (0.9)³ = 50000 × 0.729 = ₹36450
```

---

*← [Chapter 3 - Profit, Loss & Discount](./03_Profit_Loss_Discount.md) | [Chapter 5 - Ratio & Proportion →](./05_Ratio_Proportion.md)*
