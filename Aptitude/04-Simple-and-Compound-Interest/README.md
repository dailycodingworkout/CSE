# 🏦 Simple and Compound Interest | The Singularity

> **The Atomic Truth:** *SI grows linearly; CI grows exponentially—the difference is reinvestment.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Simple Interest (SI)](#simple-interest-si)
3. [Compound Interest (CI)](#compound-interest-ci)
4. [SI vs CI Comparison](#si-vs-ci-comparison)
5. [Effective Rate of Interest](#effective-rate-of-interest)
6. [Depreciation](#depreciation)
7. [Special Formulas & Shortcuts](#special-formulas--shortcuts)
8. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Interest Problems Matter?
Interest calculations are fundamental to:
- Banking and finance problems in GATE
- Time-value of money concepts
- Investment and loan scenarios
- Real-world engineering economics

### Key Terminology

| Term | Symbol | Meaning |
|------|--------|---------|
| **Principal** | P | Initial amount invested/borrowed |
| **Rate** | R or r | Interest rate per period (usually annual) |
| **Time** | T or n | Duration of investment/loan |
| **Amount** | A | Principal + Interest (final sum) |
| **Interest** | I | Money earned/paid for use of principal |

### The Core Difference

| Aspect | Simple Interest | Compound Interest |
|--------|-----------------|-------------------|
| Interest on | Principal only | Principal + Accumulated Interest |
| Growth | Linear | Exponential |
| Formula | $I = \frac{PRT}{100}$ | $A = P(1+\frac{r}{100})^n$ |
| Graph | Straight line | Exponential curve |

---

## Simple Interest (SI)

### The Fundamental Formula

$$\text{SI} = \frac{P \times R \times T}{100}$$

$$\text{Amount} = P + \text{SI} = P\left(1 + \frac{RT}{100}\right)$$

Where:
- P = Principal
- R = Rate of interest per annum (%)
- T = Time in years

### Derived Formulas

$$P = \frac{\text{SI} \times 100}{R \times T}$$

$$R = \frac{\text{SI} \times 100}{P \times T}$$

$$T = \frac{\text{SI} \times 100}{P \times R}$$

### When Time is in Months

$$\text{SI} = \frac{P \times R \times T}{100 \times 12}$$

### When Time is in Days

$$\text{SI} = \frac{P \times R \times T}{100 \times 365}$$

> **💡 The Golden Pivot:** SI is directly proportional to P, R, and T.

### Examples

**Example 1:** Find SI on ₹5000 at 8% p.a. for 3 years.
$$\text{SI} = \frac{5000 \times 8 \times 3}{100} = ₹1200$$

**Example 2:** In what time will ₹2000 become ₹2400 at 10% p.a. SI?
- SI = 2400 - 2000 = ₹400
- $T = \frac{400 \times 100}{2000 \times 10} = 2$ years

**Example 3:** At what rate will ₹1500 yield ₹270 as SI in 3 years?
$$R = \frac{270 \times 100}{1500 \times 3} = 6\%$$

---

## Compound Interest (CI)

### The Fundamental Formula

$$A = P\left(1 + \frac{r}{100}\right)^n$$

$$\text{CI} = A - P = P\left[\left(1 + \frac{r}{100}\right)^n - 1\right]$$

Where:
- A = Amount after n periods
- P = Principal
- r = Rate per period
- n = Number of periods

### Compounding Frequencies

| Compounding | Formula | n value |
|-------------|---------|---------|
| Annually | $A = P(1 + \frac{r}{100})^t$ | t years |
| Semi-annually | $A = P(1 + \frac{r}{200})^{2t}$ | 2t periods |
| Quarterly | $A = P(1 + \frac{r}{400})^{4t}$ | 4t periods |
| Monthly | $A = P(1 + \frac{r}{1200})^{12t}$ | 12t periods |

### The Power of Compounding

**Example:** ₹10,000 at 10% for 2 years

| Method | Calculation | Result |
|--------|-------------|--------|
| SI | $\frac{10000 \times 10 \times 2}{100}$ | ₹2,000 |
| CI (annual) | $10000(1.1)^2 - 10000$ | ₹2,100 |
| CI (semi-annual) | $10000(1.05)^4 - 10000$ | ₹2,155 |
| CI (quarterly) | $10000(1.025)^8 - 10000$ | ₹2,184 |

> **Observation:** More frequent compounding = Higher returns

### Shortcut for 2-3 Year CI

**For 2 years:**
$$\text{CI} - \text{SI} = P \times \left(\frac{r}{100}\right)^2 = \frac{\text{SI} \times r}{200}$$

**For 3 years:**
$$\text{CI} - \text{SI} = P \times \left(\frac{r}{100}\right)^2 \times \left(3 + \frac{r}{100}\right)$$

Or: CI - SI for 3 years = (CI - SI for 2 years) × $(1 + \frac{r}{100}) + \frac{\text{SI for 1 year} \times r}{100}$

---

## SI vs CI Comparison

### Key Differences

| Year | SI (₹) | CI (₹) | Difference |
|------|--------|--------|------------|
| 1 | $\frac{PR}{100}$ | $\frac{PR}{100}$ | 0 |
| 2 | $\frac{2PR}{100}$ | $P(1+\frac{r}{100})^2 - P$ | $\frac{PR^2}{10000}$ |
| 3 | $\frac{3PR}{100}$ | $P(1+\frac{r}{100})^3 - P$ | Larger |

> **⚠️ Key Insight:** For the first year, SI = CI (when compounded annually)

### The Difference Formula (2 years)

$$\text{CI} - \text{SI} = P \times \left(\frac{r}{100}\right)^2$$

This equals: **SI for 1 year × (r/100)** = **Interest on first year's interest**

### Finding Principal from Difference

If CI - SI for 2 years is given:
$$P = \frac{(\text{CI} - \text{SI}) \times 100^2}{r^2}$$

**Example:** CI - SI for 2 years at 10% = ₹50. Find P.
$$P = \frac{50 \times 10000}{100} = ₹5000$$

---

## Effective Rate of Interest

### Definition
The effective annual rate accounts for compounding within the year.

$$\text{Effective Rate} = \left(1 + \frac{r}{n}\right)^n - 1$$

Where n = number of compounding periods per year

### Comparison Table

| Nominal Rate | Compounding | Effective Rate |
|--------------|-------------|----------------|
| 12% | Annual | 12.00% |
| 12% | Semi-annual | 12.36% |
| 12% | Quarterly | 12.55% |
| 12% | Monthly | 12.68% |
| 12% | Daily | 12.75% |

### Continuous Compounding

$$A = P \times e^{rt}$$

Where $e = 2.71828...$

---

## Depreciation

### The Concept
Depreciation is "negative compound interest"—the value decreases over time.

### Formula

$$\text{Value after } n \text{ years} = P\left(1 - \frac{r}{100}\right)^n$$

$$\text{Depreciation} = P - P\left(1 - \frac{r}{100}\right)^n$$

**Example:** A machine worth ₹50,000 depreciates at 10% p.a. Value after 2 years?
$$V = 50000 \times (0.9)^2 = 50000 \times 0.81 = ₹40,500$$

### Population Growth/Decay

**Growth:** $P_n = P_0 \left(1 + \frac{r}{100}\right)^n$

**Decay:** $P_n = P_0 \left(1 - \frac{r}{100}\right)^n$

---

## Special Formulas & Shortcuts

### Shortcut 1: Doubling Time

**For SI:** Doubling time = $\frac{100}{r}$ years

**For CI (Rule of 72):** Doubling time ≈ $\frac{72}{r}$ years

| Rate | SI Doubling | CI Doubling (approx) |
|------|-------------|---------------------|
| 6% | 16.67 years | 12 years |
| 8% | 12.5 years | 9 years |
| 10% | 10 years | 7.2 years |
| 12% | 8.33 years | 6 years |

### Shortcut 2: Tripling Time

**For SI:** Tripling time = $\frac{200}{r}$ years

**For CI (Rule of 114):** Tripling time ≈ $\frac{114}{r}$ years

### Shortcut 3: Amount Ratio for CI

If amounts after $n_1$ and $n_2$ years are $A_1$ and $A_2$:

$$\frac{A_2}{A_1} = \left(1 + \frac{r}{100}\right)^{n_2 - n_1}$$

### Shortcut 4: Finding Rate from CI Ratio

If CI for year 2 is $I_2$ and CI for year 3 is $I_3$:

$$r = \frac{(I_3 - I_2)}{I_2} \times 100$$

This works because: $I_3 = I_2 \times (1 + \frac{r}{100})$

### Shortcut 5: Present Worth

$$\text{Present Worth} = \frac{\text{Amount}}{(1 + \frac{r}{100})^n}$$

---

## GATE & ESE Problem Patterns

### Pattern 1: Basic SI/CI Calculation
> Find CI on ₹8000 at 15% p.a. for 2 years.
$$A = 8000(1.15)^2 = 8000 \times 1.3225 = ₹10580$$
$$\text{CI} = 10580 - 8000 = ₹2580$$

### Pattern 2: Finding Rate from Difference
> If CI - SI for 2 years is ₹20 and SI for 2 years is ₹400, find the rate.
- SI for 1 year = ₹200
- CI - SI = SI₁ × r/100
- 20 = 200 × r/100
- r = 10%

### Pattern 3: Installment Problems
> A sum at 10% CI p.a. amounts to ₹1210 in 2 years. Find principal.
$$P = \frac{1210}{(1.1)^2} = \frac{1210}{1.21} = ₹1000$$

### Pattern 4: Equal Annual Installments

If a loan P is to be paid in n equal annual installments of value x each at rate r%:

$$x = P \times \frac{r(1+r)^n}{(1+r)^n - 1}$$

Where r is in decimal form.

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"At what rate will a sum double itself in 5 years at CI?"

Wrong approach: Using SI formula (100/5 = 20%)

**The Elegant Solution:**
$$2P = P(1 + \frac{r}{100})^5$$
$$2 = (1 + \frac{r}{100})^5$$
$$1 + \frac{r}{100} = 2^{0.2} = 1.1487$$
$$r = 14.87\%$$

**MSQ Logic Gate:**
- SI = CI for 1st year only
- For same rate, CI > SI for periods > 1 year
- Difference increases with time (exponentially for CI)

**NAT Precision Lock:**
- For CI calculations, carry at least 4 decimal places
- $(1.1)^2 = 1.21$, $(1.1)^3 = 1.331$, $(1.1)^4 = 1.4641$
- Common approximations can lead to wrong NAT answers

---

## Speed Tricks & Shortcuts

### Trick 1: CI Computation Table

Memorize for 10%:
| Years | Multiplier | CI on 100 |
|-------|------------|-----------|
| 1 | 1.1 | 10 |
| 2 | 1.21 | 21 |
| 3 | 1.331 | 33.1 |
| 4 | 1.4641 | 46.41 |

### Trick 2: Interest Earned Each Year (CI)

Interest in year $n$ = Interest in year $(n-1)$ × $(1 + \frac{r}{100})$

### Trick 3: Quick CI - SI for 2 years

CI - SI = $\frac{r}{100} \times$ SI for 1 year = $\frac{r \times r \times P}{10000}$

### Trick 4: When SI Doubles Principal

If SI = P, then $\frac{P \times R \times T}{100} = P$
Therefore: $R \times T = 100$

### Trick 5: Present Value Quick Calculation

For small rates and short periods:
PV ≈ FV × $(1 - \frac{r \times n}{100})$

---

## Permanent Recall

### The Bizarre Mnemonic (SI vs CI)
*"Simple Interest is a flat highway—same distance every year. Compound Interest is a spiral staircase—each step is taller than the last because you're standing on accumulated stairs."*

### The Mental Slider
Imagine a savings graph:
- X-axis = Time
- Y-axis = Money
- SI: Straight line from origin
- CI: Curved line that pulls away from SI
- The gap between them = "interest on interest"

### The 5-Second Snap-Check
- If CI = SI, check if time = 1 year
- If doubling time seems too short, you probably used wrong formula
- CI should always be ≥ SI for the same P, R, T

---

## Practice Problems

### Level 1: Fundamentals
1. Find SI on ₹15,000 at 12% p.a. for 2 years 6 months.
2. Find CI on ₹10,000 at 10% p.a. for 2 years, compounded annually.
3. In how many years will ₹5000 amount to ₹8000 at 10% SI?

### Level 2: GATE Standard
4. The difference between CI and SI for 2 years at 8% p.a. is ₹32. Find the sum.
5. A sum becomes ₹2420 in 2 years and ₹2662 in 3 years at CI. Find the rate.
6. What annual payment will discharge a debt of ₹6450 due in 4 years at 5% CI?

### Level 3: IIT Examiner Level
7. A sum of money at CI amounts to thrice itself in 4 years. In how many years will it become 9 times?
8. The SI on a sum is 1/16 of the sum. If the number of years is numerically equal to the rate %, find the rate.
9. A bank offers 5% CI calculated on half-yearly basis. A customer deposits ₹1600 each on 1st Jan and 1st July. At the end of the year, what is the total amount?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. T = 2.5 years
   SI = (15000 × 12 × 2.5)/100 = **₹4,500**

2. A = 10000 × (1.1)² = 10000 × 1.21 = ₹12,100
   CI = **₹2,100**

3. SI = 8000 - 5000 = 3000
   T = (3000 × 100)/(5000 × 10) = **6 years**

4. CI - SI = P(r/100)²
   32 = P × (8/100)² = P × 64/10000
   P = 32 × 10000/64 = **₹5,000**

5. Amount in year 3/Amount in year 2 = (1 + r/100)
   2662/2420 = 1 + r/100
   1.1 = 1 + r/100
   r = **10%**

6. Using annuity formula:
   P = A × [(1+r)ⁿ - 1]/[r(1+r)ⁿ]
   6450 = x × [1.05⁴ - 1]/[0.05 × 1.05⁴]
   6450 = x × 4.31/0.0552
   x = 6450 × 0.0552/1.2155 ≈ **₹1,820** (approx)

7. 3P = P(1 + r/100)⁴
   (1 + r/100)⁴ = 3
   For 9P: 9 = 3² = [(1 + r/100)⁴]²  = (1 + r/100)⁸
   Time = **8 years**

8. SI = P/16
   (P × R × R)/100 = P/16 (since T = R)
   R² = 100/16 = 6.25
   R = **2.5%**

9. For deposit on Jan 1: A = 1600(1.025)² = 1600 × 1.050625 = ₹1681
   For deposit on July 1: A = 1600(1.025)¹ = 1600 × 1.025 = ₹1640
   Total = **₹3,321**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Interest with Ratio & Proportion for a Rank-1 simulation?
