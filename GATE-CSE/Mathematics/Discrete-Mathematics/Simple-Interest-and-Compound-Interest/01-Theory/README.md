# Simple Interest & Compound Interest - Complete Theory
## GATE 2026 CSE AIR 1 Preparation

### Table of Contents
1. [Simple Interest](#simple-interest)
2. [Compound Interest](#compound-interest)
   - [Case 1: Annual Compounding](#case-1-annual-compounding)
   - [Case 2: Half-Yearly Compounding](#case-2-half-yearly-compounding)
   - [Case 3: Quarterly Compounding](#case-3-quarterly-compounding)
   - [Case 4: Differential Rate of Interest](#case-4-differential-rate-of-interest)
3. [Mathematical Foundations](#mathematical-foundations)
4. [Advanced Concepts](#advanced-concepts)

---

## Simple Interest

### Definition and Core Concepts

**Simple Interest** is the interest calculated only on the principal amount throughout the entire period. It remains constant for each time period and does not compound.

**Mathematical Foundation:**
```
Simple Interest (SI) = (Principal × Rate × Time) / 100
SI = (P × R × T) / 100
```

**Amount Formula:**
```
Amount (A) = Principal + Simple Interest
A = P + SI = P + (P × R × T) / 100
A = P(1 + RT/100)
```

### Fundamental Parameters

1. **Principal (P)**: The initial sum of money borrowed or invested
2. **Rate (R)**: The percentage of interest per annum
3. **Time (T)**: The duration for which money is borrowed or invested
4. **Simple Interest (SI)**: The interest earned or paid
5. **Amount (A)**: The total sum (Principal + Interest)

### Key Relationships and Derivations

**Deriving Principal:**
```
P = (SI × 100) / (R × T)
P = A / (1 + RT/100)
```

**Deriving Rate:**
```
R = (SI × 100) / (P × T)
R = ((A - P) × 100) / (P × T)
```

**Deriving Time:**
```
T = (SI × 100) / (P × R)
T = ((A - P) × 100) / (P × R)
```

### Advanced Simple Interest Concepts

#### 1. Difference Between Two Rates
When money is lent at two different rates R₁ and R₂ for the same time T:
```
Difference in SI = P × (R₁ - R₂) × T / 100
```

#### 2. Sum Lent in Parts
If a sum P is divided into two parts such that:
- First part earns SI at rate R₁
- Second part earns SI at rate R₂
- Total SI = Given amount

**Formula:**
```
If P = P₁ + P₂
P₁ = P × (R₂T - 100×Total SI/P) / (R₂ - R₁)T
P₂ = P - P₁
```

#### 3. True Discount and Banker's Discount
**True Discount (TD)**: SI on present worth for given time
**Banker's Discount (BD)**: SI on face value for given time

```
TD = (PW × R × T) / 100
BD = (FV × R × T) / 100
BD - TD = (TD² × R × T) / (100 × PW)
```

---

## Compound Interest

### Definition and Mathematical Foundation

**Compound Interest** is the interest calculated on the principal amount and also on the accumulated interest of previous periods. It exhibits exponential growth.

**Core Formula:**
```
Amount = P(1 + R/100)ⁿ
Compound Interest = P(1 + R/100)ⁿ - P
CI = P[(1 + R/100)ⁿ - 1]
```

Where:
- P = Principal
- R = Rate per annum
- n = Number of years
- CI = Compound Interest

### Case 1: Annual Compounding

When interest is compounded annually, the formula remains in its standard form:

```
A = P(1 + R/100)ⁿ
CI = P[(1 + R/100)ⁿ - 1]
```

**Year-wise Breakdown:**
- After 1 year: A₁ = P(1 + R/100)
- After 2 years: A₂ = P(1 + R/100)²
- After n years: Aₙ = P(1 + R/100)ⁿ

**Mathematical Proof:**
Let P = Initial principal
After 1 year: A₁ = P + PR/100 = P(1 + R/100)
After 2 years: A₂ = A₁(1 + R/100) = P(1 + R/100)²
By induction: Aₙ = P(1 + R/100)ⁿ

### Case 2: Half-Yearly Compounding

When interest is compounded twice a year (every 6 months):

```
A = P(1 + R/200)²ⁿ
CI = P[(1 + R/200)²ⁿ - 1]
```

**Logic:**
- Rate per half-year = R/2%
- Number of half-years in n years = 2n
- Compounding happens 2n times

**Derivation:**
If annual rate = R%, then half-yearly rate = R/2%
Number of compounding periods = 2n
Therefore: A = P(1 + R/200)²ⁿ

### Case 3: Quarterly Compounding

When interest is compounded four times a year (every 3 months):

```
A = P(1 + R/400)⁴ⁿ
CI = P[(1 + R/400)⁴ⁿ - 1]
```

**Logic:**
- Rate per quarter = R/4%
- Number of quarters in n years = 4n
- Compounding happens 4n times

**General Formula for m times compounding:**
```
A = P(1 + R/(100m))^(mn)
```
Where m = number of times interest is compounded per year

### Case 4: Differential Rate of Interest

When different rates are applied for different years:

**For varying annual rates:**
```
A = P(1 + R₁/100)(1 + R₂/100)(1 + R₃/100)...(1 + Rₙ/100)
```

**Example:** Principal P, Rate R₁% for 1st year, R₂% for 2nd year, R₃% for 3rd year
```
Amount after 3 years = P(1 + R₁/100)(1 + R₂/100)(1 + R₃/100)
```

**Mathematical Foundation:**
Each year, the amount becomes the principal for the next year with the new rate.

### Advanced Compound Interest Concepts

#### 1. Effective Annual Rate
When compounding frequency increases:
```
Effective Rate = (1 + R/(100m))^m - 1
```
Where m = compounding frequency per year

#### 2. Continuous Compounding
When compounding approaches infinity:
```
A = Pe^(Rt)
```
Where e = 2.71828... (Euler's number)

#### 3. Population Growth Model
CI formula applies to population growth:
```
Population after n years = P₀(1 + r/100)ⁿ
```

#### 4. Depreciation Model
For depreciation (negative growth):
```
Value after n years = P₀(1 - r/100)ⁿ
```

---

## Mathematical Foundations

### Binomial Expansion for Approximations

For small values of R:
```
(1 + R/100)ⁿ ≈ 1 + nR/100 + n(n-1)R²/(2×100²) + ...
```

**First-order approximation:**
```
CI ≈ SI + (SI×R×(n-1))/(200)
```

### Logarithmic Relationships

**Finding Time in CI:**
```
n = log(A/P) / log(1 + R/100)
```

**Finding Rate in CI:**
```
R = 100[(A/P)^(1/n) - 1]
```

### Series and Sequences

**Sum of CI for multiple years:**
```
Total CI = P[(1+R/100)ⁿ - 1]
```

**Geometric progression relationship:**
Amounts form a GP: P, P(1+R/100), P(1+R/100)², ...

---

## Advanced Concepts

### 1. Difference Between CI and SI

**For 2 years:**
```
CI - SI = P(R/100)²
```

**For 3 years:**
```
CI - SI = P(R/100)² × (300 + R)/100
```

**General formula for n years:**
```
CI - SI = SI × [((1 + R/100)ⁿ⁻¹ - 1) × 100] / (R × n)
```

### 2. Installment Methods

**Present value of installments:**
```
PV = I/(1+R/100) + I/(1+R/100)² + ... + I/(1+R/100)ⁿ
PV = I × [1 - (1+R/100)⁻ⁿ] / (R/100)
```

### 3. Equated Monthly Installments (EMI)

```
EMI = P × R(1+R)ⁿ / [12 × ((1+R)ⁿ - 1)]
```
Where R = annual rate/100, n = number of years

### 4. Doubling and Tripling Time

**Doubling time:**
```
n = log(2) / log(1 + R/100) ≈ 72/R (Rule of 72)
```

**Tripling time:**
```
n = log(3) / log(1 + R/100) ≈ 110/R (Rule of 110)
```

### 5. Mixed Interest Problems

When part is at SI and part at CI:
```
Total Interest = SI₁ + CI₂
```
Solve using system of equations based on given conditions.

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Simple Interest | SI = PRT/100 |
| Amount (SI) | A = P(1 + RT/100) |
| Compound Interest (Annual) | CI = P[(1 + R/100)ⁿ - 1] |
| Amount (CI Annual) | A = P(1 + R/100)ⁿ |
| Half-yearly Compounding | A = P(1 + R/200)²ⁿ |
| Quarterly Compounding | A = P(1 + R/400)⁴ⁿ |
| Differential Rates | A = P(1 + R₁/100)(1 + R₂/100)... |
| CI - SI (2 years) | P(R/100)² |
| CI - SI (3 years) | P(R/100)²(300 + R)/100 |
| Effective Rate | (1 + R/(100m))^m - 1 |
| Doubling Time | 72/R years |

---

## Applications in GATE CSE

1. **Algorithm Analysis**: Understanding exponential vs linear growth
2. **Database Optimization**: Cost-benefit analysis of indexing
3. **Network Performance**: Exponential backoff algorithms
4. **Computer Graphics**: Transformation matrices and scaling
5. **Machine Learning**: Learning rate optimization
6. **System Design**: Capacity planning and resource allocation

This comprehensive theory forms the foundation for mastering Simple Interest and Compound Interest problems in GATE 2026 CSE, ensuring complete conceptual clarity for AIR 1 achievement.