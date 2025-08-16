# Theory - Percentage

## Complete Theoretical Foundation for GATE 2026 CSE AIR 1

### 1. Fundamental Concepts of Percentage

#### 1.1 Definition and Mathematical Foundation
**Percentage** is a way of expressing a number as a fraction of 100. The word "percent" comes from the Latin "per centum," meaning "by the hundred."

**Mathematical Definition:**
```
Percentage = (Part / Whole) × 100
P% = (x/y) × 100, where x is the part and y is the whole
```

**Core Properties:**
1. **Additive Property**: If A = x% and B = y%, then A + B = (x + y)%
2. **Multiplicative Property**: x% of y% = (xy/100)%
3. **Reciprocal Property**: If A is x% more than B, then B is [x/(100+x)]×100% less than A

#### 1.2 Percentage as Ratio and Proportion
**Ratio Representation:**
- x% = x:100 = x/100
- Converting ratio a:b to percentage = (a/(a+b)) × 100%

**Proportion Representation:**
- If a:b = c:d, then a% of d = c% of b
- Cross multiplication: a×d = b×c

### 2. Calculation of Percentage

#### 2.1 Basic Percentage Calculations

**Type 1: Finding Percentage of a Number**
```
Formula: x% of N = (x/100) × N
Example: 15% of 80 = (15/100) × 80 = 12
```

**Type 2: Finding What Percentage One Number is of Another**
```
Formula: (x/y) × 100 = ?%
Example: What % is 25 of 125?
Answer: (25/125) × 100 = 20%
```

**Type 3: Finding the Whole When Part and Percentage are Known**
```
Formula: If x% of N = P, then N = (P × 100)/x
Example: 20% of ? = 40
Answer: N = (40 × 100)/20 = 200
```

#### 2.2 Advanced Percentage Calculations

**Compound Percentage Problems:**
When percentage is applied multiple times on the same base:
```
Final Value = Initial × (1 ± r₁/100) × (1 ± r₂/100) × ... × (1 ± rₙ/100)
```

**Weighted Percentage:**
When different parts have different percentage values:
```
Overall % = (w₁×p₁ + w₂×p₂ + ... + wₙ×pₙ)/(w₁ + w₂ + ... + wₙ)
where wᵢ are weights and pᵢ are percentages
```

### 3. Percentage & Fraction Relationship

#### 3.1 Converting Fractions to Percentages
**Standard Method:**
```
Fraction to % = (Numerator/Denominator) × 100
```

**Important Fraction-Percentage Equivalents:**
- 1/2 = 50%
- 1/3 = 33⅓%
- 2/3 = 66⅔%
- 1/4 = 25%
- 3/4 = 75%
- 1/5 = 20%
- 1/6 = 16⅔%
- 1/7 = 14²/₇%
- 1/8 = 12.5%
- 1/9 = 11¹/₉%
- 1/10 = 10%

#### 3.2 Converting Percentages to Fractions
**Method:**
1. Write percentage as fraction with denominator 100
2. Simplify to lowest terms

**Examples:**
- 25% = 25/100 = 1/4
- 37.5% = 375/1000 = 3/8
- 66⅔% = 200/3 ÷ 100 = 2/3

#### 3.3 Mixed Number Percentages
**Converting Mixed Percentages:**
```
a b/c % = (ac + b)/c ÷ 100 = (ac + b)/(100c)
```

**Example:**
```
12½% = 12.5% = 25/2 ÷ 100 = 25/200 = 1/8
```

### 4. Multiplication Factor Method

#### 4.1 Concept of Multiplication Factor
**Definition:** Multiplication factor is the decimal equivalent of percentage that can be directly multiplied to find the result.

**Formula:**
```
Multiplication Factor = (100 ± percentage)/100
```

**For Increase:** Factor = (100 + x)/100
**For Decrease:** Factor = (100 - x)/100

#### 4.2 Applications of Multiplication Factor

**Single Change:**
- 20% increase: Factor = 1.20
- 15% decrease: Factor = 0.85
- New Value = Original × Factor

**Multiple Changes:**
- Overall Factor = Factor₁ × Factor₂ × ... × Factorₙ
- Net Change% = (Overall Factor - 1) × 100

**Example:**
Price increases by 20%, then decreases by 10%:
```
Overall Factor = 1.20 × 0.90 = 1.08
Net Change = 8% increase
```

#### 4.3 Advanced Multiplication Factor Techniques

**Fractional Multiplication Factors:**
- 33⅓% increase: Factor = 4/3
- 25% decrease: Factor = 3/4
- 16⅔% increase: Factor = 7/6

**Quick Calculation Method:**
Instead of converting to decimals, use fractions for exact calculations.

### 5. Successive Percentage Change

#### 5.1 Theory of Successive Changes
When multiple percentage changes are applied sequentially to the same quantity.

**Formula for Two Changes:**
```
Net Change% = x + y + (xy/100)
where x and y are the individual percentage changes
```

**For n Changes:**
```
Final Value = Initial × ∏(1 ± rᵢ/100)
where rᵢ are individual percentage changes
```

#### 5.2 Types of Successive Changes

**Type 1: All Increases**
```
If increases are x₁%, x₂%, ..., xₙ%
Net Increase% = [(1 + x₁/100)(1 + x₂/100)...(1 + xₙ/100) - 1] × 100
```

**Type 2: All Decreases**
```
If decreases are x₁%, x₂%, ..., xₙ%
Net Decrease% = [1 - (1 - x₁/100)(1 - x₂/100)...(1 - xₙ/100)] × 100
```

**Type 3: Mixed Changes**
Apply signs accordingly (+ for increase, - for decrease)

#### 5.3 Special Cases in Successive Changes

**Equal Successive Changes:**
If same percentage change r is applied n times:
```
Final Value = Initial × (1 ± r/100)ⁿ
```

**Alternating Changes:**
If alternating increases and decreases of same magnitude:
- After even number of changes: Net effect depends on the square of individual change
- After odd number of changes: One extra change remains

**Reversing Changes:**
If change x% is followed by change y% such that final value equals initial:
```
y = -x/(1 + x/100) × 100
```

### 6. Comparison Leading to Base Change

#### 6.1 Concept of Base Change
When comparing quantities, the choice of base affects the percentage calculation significantly.

**Fundamental Principle:**
```
A is x% more than B ≠ B is x% less than A
```

**Mathematical Relationship:**
```
If A = B(1 + x/100), then B = A/(1 + x/100) = A(1 - y/100)
where y = x/(1 + x/100) × 100
```

#### 6.2 Base Change Formulas

**From Larger to Smaller Base:**
```
If A is x% more than B, then B is [x/(100 + x)] × 100% less than A
```

**From Smaller to Larger Base:**
```
If B is y% less than A, then A is [y/(100 - y)] × 100% more than B
```

#### 6.3 Applications in Comparison Problems

**Price Comparison:**
- If price of A is 25% more than B, then price of B is 20% less than A
- Calculation: 25/(100+25) × 100 = 20%

**Ratio Comparison:**
- If ratio changes from a:b to c:d, percentage change in ratio = [(c/d)/(a/b) - 1] × 100

**Speed/Time Comparison:**
- If speed increases by x%, time decreases by x/(100+x) × 100%
- If time decreases by y%, speed increases by y/(100-y) × 100%

### 7. Advanced Percentage Concepts for GATE CSE

#### 7.1 Percentage in Data Interpretation
**Statistical Percentages:**
- Percentile calculations
- Percentage distribution in datasets
- Cumulative percentage analysis

**Error Percentage:**
```
Percentage Error = |Measured Value - True Value|/True Value × 100
```

#### 7.2 Percentage in Algorithm Analysis
**Performance Improvement:**
```
Performance Gain% = (New Time - Old Time)/Old Time × 100
```

**Accuracy Metrics:**
```
Accuracy% = (Correct Predictions/Total Predictions) × 100
```

#### 7.3 Percentage in Probability
**Probability Percentage:**
```
P(Event) × 100 = Percentage chance of event occurrence
```

**Conditional Percentage:**
```
P(A|B) × 100 = Percentage of A given B has occurred
```

### 8. Mathematical Proofs and Derivations

#### 8.1 Proof of Successive Percentage Formula
**Given:** Two successive changes of x% and y%
**To Prove:** Net change = x + y + xy/100

**Proof:**
Let initial value = 100 units
After first change = 100(1 ± x/100) = 100 ± x
After second change = (100 ± x)(1 ± y/100) = 100 ± x ± y ± xy/100
Net change = ±x ± y ± xy/100 = ±(x + y + xy/100)

#### 8.2 Proof of Base Change Formula
**Given:** A is x% more than B
**To Prove:** B is x/(100+x) × 100% less than A

**Proof:**
A = B(1 + x/100)
B = A/(1 + x/100) = A(100/(100+x))
Percentage decrease = [1 - 100/(100+x)] × 100 = x/(100+x) × 100%

### 9. Error Analysis in Percentage Calculations

#### 9.1 Common Conceptual Errors
1. **Base Confusion:** Using wrong reference point
2. **Formula Misapplication:** Incorrect application of percentage formulas
3. **Sign Errors:** Wrong signs in successive changes
4. **Approximation Errors:** Rounding off at wrong stages

#### 9.2 Precision in Calculations
**Exact vs Approximate Values:**
- Use fractions for exact calculations
- Decimal approximations only for final answers
- Maintain precision throughout intermediate steps

**Significant Figures in Percentage:**
- Round final percentage to appropriate decimal places
- Consider context for required precision

### 10. Real-world Applications

#### 10.1 Business and Finance
- Profit/Loss percentage calculations
- Interest rate computations
- Discount and markup problems
- Tax calculations

#### 10.2 Computer Science Applications
- Algorithm efficiency improvements
- Data compression ratios
- System performance metrics
- Error rates in computations

#### 10.3 Statistical Analysis
- Survey result interpretation
- Trend analysis
- Performance benchmarking
- Quality metrics

This comprehensive theory provides the mathematical foundation necessary for achieving AIR 1 in GATE 2026 CSE. Master each concept with practice and application to build unshakeable confidence in percentage problems.