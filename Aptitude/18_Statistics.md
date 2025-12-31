# Chapter 18: Statistics

> **The science of data - extracting meaning from numbers**

---

## 🎯 Why Study This?

- Essential for Data Interpretation in GATE/ESE
- Foundation for data analysis and research
- Real-world: Surveys, experiments, business analytics

---

## 📚 Part 1: Measures of Central Tendency

### Mean (Arithmetic Average)

```
Mean (x̄) = Sum of all values / Number of values
         = Σxᵢ / n
```

**Weighted Mean**:
```
Weighted Mean = Σ(wᵢ × xᵢ) / Σwᵢ
```

**For Grouped Data** (class intervals):
```
Mean = Σ(fᵢ × xᵢ) / Σfᵢ

Where fᵢ = frequency, xᵢ = class midpoint
```

**Properties**:
- Affected by extreme values (outliers)
- Sum of deviations from mean = 0
- If each value multiplied by k, mean is multiplied by k
- If k added to each value, mean increases by k

---

### Median

**The middle value** when data is arranged in order.

**For Raw Data**:
```
If n is odd: Median = ((n+1)/2)th value
If n is even: Median = Average of (n/2)th and ((n/2)+1)th values
```

**For Grouped Data**:
```
Median = L + [(N/2 - cf)/f] × h

Where:
L = Lower limit of median class
N = Total frequency
cf = Cumulative frequency before median class
f = Frequency of median class
h = Class width
```

**Properties**:
- Not affected by extreme values
- Best for skewed distributions
- Divides data into two equal halves

---

### Mode

**Most frequently occurring value**

**For Grouped Data**:
```
Mode = L + [(f₁ - f₀)/(2f₁ - f₀ - f₂)] × h

Where:
L = Lower limit of modal class
f₁ = Frequency of modal class
f₀ = Frequency of class before modal class
f₂ = Frequency of class after modal class
h = Class width
```

**Types**:
- Unimodal: One mode
- Bimodal: Two modes
- Multimodal: More than two modes

---

### Empirical Relationship

For moderately skewed distributions:
```
Mode = 3 × Median - 2 × Mean

Or: Mean - Mode = 3(Mean - Median)
```

---

## 📚 Part 2: Measures of Dispersion

### Range

```
Range = Maximum value - Minimum value
```

Simple but affected by extreme values.

---

### Variance

**Population Variance**:
```
σ² = Σ(xᵢ - μ)² / N
   = (Σxᵢ²/N) - (Σxᵢ/N)²
   = E(X²) - [E(X)]²
```

**Sample Variance** (with Bessel's correction):
```
s² = Σ(xᵢ - x̄)² / (n-1)
```

---

### Standard Deviation

```
σ = √Variance = √[Σ(xᵢ - μ)² / N]
```

**Properties**:
- Same units as original data
- If each value multiplied by k, SD is multiplied by |k|
- If k added to each value, SD remains unchanged

---

### Coefficient of Variation (CV)

```
CV = (Standard Deviation / Mean) × 100%
   = (σ/μ) × 100%
```

**Use**: Compare variability between datasets with different units or means.

---

### Mean Absolute Deviation (MAD)

```
MAD = Σ|xᵢ - x̄| / n
```

---

## 📚 Part 3: Quartiles & Percentiles

### Quartiles

Divide data into 4 equal parts:
```
Q₁ (25th percentile): First quartile
Q₂ (50th percentile): Median
Q₃ (75th percentile): Third quartile
```

**For ungrouped data**:
```
Q₁ = Value at position (n+1)/4
Q₂ = Value at position (n+1)/2
Q₃ = Value at position 3(n+1)/4
```

---

### Interquartile Range (IQR)

```
IQR = Q₃ - Q₁
```

Measures spread of middle 50% of data.

---

### Percentiles

**Pₖ**: Value below which k% of data falls
```
Position of Pₖ = k(n+1)/100
```

---

### Outlier Detection (Box Plot Method)

```
Lower fence = Q₁ - 1.5 × IQR
Upper fence = Q₃ + 1.5 × IQR

Values outside fences are outliers
```

---

## 📚 Part 4: Distribution Shape

### Skewness

Measures asymmetry of distribution.

```
Skewness = (Mean - Mode) / Standard Deviation
         = 3(Mean - Median) / Standard Deviation
```

| Skewness | Description | Tail |
|----------|-------------|------|
| = 0 | Symmetric | No skew |
| > 0 | Positive/Right | Tail extends right |
| < 0 | Negative/Left | Tail extends left |

**For positive skew**: Mean > Median > Mode
**For negative skew**: Mode > Median > Mean

---

### Kurtosis

Measures "tailedness" of distribution.

```
Kurtosis = μ₄/σ⁴

Where μ₄ = fourth central moment
```

| Type | Kurtosis | Shape |
|------|----------|-------|
| Mesokurtic | = 3 | Normal |
| Leptokurtic | > 3 | Heavy tails, peaked |
| Platykurtic | < 3 | Light tails, flat |

---

## 📚 Part 5: Correlation & Regression

### Correlation Coefficient (r)

Measures linear relationship between two variables.

```
r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² × Σ(yᵢ - ȳ)²]

  = [nΣxy - ΣxΣy] / √[(nΣx² - (Σx)²)(nΣy² - (Σy)²)]

  = Cov(X,Y) / (σₓ × σᵧ)
```

**Range**: -1 ≤ r ≤ 1

| Value | Interpretation |
|-------|----------------|
| r = 1 | Perfect positive correlation |
| r = -1 | Perfect negative correlation |
| r = 0 | No linear correlation |
| 0.7-1 | Strong positive |
| 0.3-0.7 | Moderate positive |
| 0-0.3 | Weak positive |

---

### Covariance

```
Cov(X,Y) = Σ(xᵢ - x̄)(yᵢ - ȳ) / n
         = E(XY) - E(X)E(Y)
```

---

### Regression Line

**Line of y on x**:
```
y - ȳ = byx(x - x̄)

byx = r × (σy/σx) = Cov(X,Y)/Var(X)
```

**Line of x on y**:
```
x - x̄ = bxy(y - ȳ)

bxy = r × (σx/σy) = Cov(X,Y)/Var(Y)
```

**Properties**:
- Both regression lines pass through (x̄, ȳ)
- r² = byx × bxy
- If r = ±1, both lines coincide

---

## 💡 Advanced Tricks

### Trick 1: Combined Mean of Two Groups

```
Combined mean = (n₁x̄₁ + n₂x̄₂) / (n₁ + n₂)
```

---

### Trick 2: Combined Variance

```
Combined σ² = [n₁(σ₁² + d₁²) + n₂(σ₂² + d₂²)] / (n₁ + n₂)

Where d₁ = x̄₁ - x̄combined, d₂ = x̄₂ - x̄combined
```

---

### Trick 3: Variance from Σx and Σx²

```
σ² = (Σx²/n) - (Σx/n)²
```

---

### Trick 4: Change of Scale

If Y = aX + b:
```
Mean(Y) = a × Mean(X) + b
Var(Y) = a² × Var(X)
SD(Y) = |a| × SD(X)
```

---

### Trick 5: Quick Median for Ordered Data

For n values: Median position = (n+1)/2

---

## ⚠️ Edge Cases & Traps

### Trap 1: Sample vs Population

Sample uses (n-1) for variance, population uses N.

### Trap 2: Mode May Not Exist

If all values occur once, no mode exists.

### Trap 3: Correlation ≠ Causation

High correlation doesn't imply one causes the other.

### Trap 4: Outliers Affect Mean

Median is more robust to outliers than mean.

### Trap 5: Variance is Never Negative

SD is always non-negative (zero only if all values equal).

---

## 🚀 Formula Cheat Sheet

| Measure | Formula |
|---------|---------|
| Mean | Σxᵢ/n |
| Median (odd n) | ((n+1)/2)th value |
| Mode (grouped) | L + [(f₁-f₀)/(2f₁-f₀-f₂)]h |
| Variance | Σ(xᵢ-μ)²/N |
| Standard Deviation | √Variance |
| CV | (σ/μ) × 100% |
| IQR | Q₃ - Q₁ |
| Correlation | Cov(X,Y)/(σₓσᵧ) |
| Regression (y on x) | byx = r(σy/σx) |
| Mode-Median-Mean | Mode = 3Median - 2Mean |

---

## 📝 GATE-Level Practice

**Q1**: Mean of 5 numbers is 20. If each is multiplied by 3, new mean?
```
New mean = 3 × 20 = 60
```

**Q2**: Find variance: 2, 4, 6, 8, 10
```
Mean = 6
Variance = [(2-6)² + (4-6)² + (6-6)² + (8-6)² + (10-6)²]/5
         = [16 + 4 + 0 + 4 + 16]/5 = 40/5 = 8
```

**Q3**: If CV = 25% and σ = 15, find mean.
```
CV = (σ/μ) × 100
25 = (15/μ) × 100
μ = 1500/25 = 60
```

**Q4**: Median of: 3, 7, 2, 9, 5, 8, 1
```
Ordered: 1, 2, 3, 5, 7, 8, 9
n = 7 (odd)
Median = 4th value = 5
```

**Q5**: If r = 0.8, σx = 5, σy = 10, find byx.
```
byx = r × (σy/σx) = 0.8 × (10/5) = 1.6
```

**Q6**: Mean = 50, Mode = 44. Find Median.
```
Mode = 3 × Median - 2 × Mean
44 = 3 × Median - 100
Median = 144/3 = 48
```

---

*← [Chapter 17 - Probability](./17_Probability.md) | [Chapter 19 - Set Theory & Venn Diagrams →](./19_Set_Theory_Venn.md)*
