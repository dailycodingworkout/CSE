# Chapter 2: Percentages

> **The language of comparison - mastering this unlocks Profit/Loss, Interest, and Data Interpretation**

---

## 🎯 Why Study Percentages?

- Foundation for 40%+ of aptitude problems
- Essential for Data Interpretation (GATE favorite)
- Real-world: Discounts, Growth rates, Statistics

---

## 📚 Core Concept

**Percentage** = "Per hundred" = Parts out of 100

```
x% = x/100 = x per 100
```

**💡 Analogy**: Percentage is a universal translator - converts any number into a comparable scale of 100.

---

## 🔄 Fundamental Conversions

### Fraction ↔ Percentage ↔ Decimal

| Fraction | Decimal | Percentage |
|----------|---------|------------|
| 1/2 | 0.5 | 50% |
| 1/3 | 0.333... | 33.33% |
| 1/4 | 0.25 | 25% |
| 1/5 | 0.2 | 20% |
| 1/6 | 0.166... | 16.67% |
| 1/8 | 0.125 | 12.5% |
| 1/10 | 0.1 | 10% |
| 1/12 | 0.0833 | 8.33% |
| 1/15 | 0.0667 | 6.67% |
| 1/20 | 0.05 | 5% |
| 1/25 | 0.04 | 4% |

**⚡ Must Memorize**: These conversions save 30+ seconds per problem!

---

## 📐 Core Formulas

### Finding Percentage

```
What is x% of N?
Answer = (x/100) × N = N × x/100
```

**Example**: What is 35% of 240?
```
= 240 × 35/100 = 240 × 0.35 = 84
```

**⚡ Trick**: Break complex percentages
```
35% of 240 = 30% + 5%
           = (3 × 24) + (half of 24)
           = 72 + 12 = 84
```

---

### Finding What Percentage

```
A is what % of B?
Answer = (A/B) × 100
```

**Example**: 45 is what % of 180?
```
= (45/180) × 100 = 25%
```

---

### Finding the Base Value

```
x% of what number = A?
Answer = A × (100/x)
```

**Example**: 15% of what number is 45?
```
= 45 × (100/15) = 45 × (20/3) = 300
```

---

## 📈📉 Percentage Change

### Basic Formula

```
% Change = ((New - Old) / Old) × 100

% Increase = ((Final - Initial) / Initial) × 100
% Decrease = ((Initial - Final) / Initial) × 100
```

**⚠️ Critical**: Denominator is ALWAYS the original/initial value!

---

### Multiplying Factors

**This is the most powerful concept in percentages!**

| Change | Multiplying Factor |
|--------|-------------------|
| Increase by x% | × (1 + x/100) = × (100+x)/100 |
| Decrease by x% | × (1 - x/100) = × (100-x)/100 |

**Examples**:
```
Increase by 20% → Multiply by 1.2 or 120/100 or 6/5
Decrease by 25% → Multiply by 0.75 or 75/100 or 3/4
Increase by 33.33% → Multiply by 4/3
Decrease by 16.67% → Multiply by 5/6
```

**⚡ Why this matters**: 
```
Price increases 20%, then 25%:
Final = Original × 1.2 × 1.25 = Original × 1.5

So net increase = 50% (NOT 45%!)
```

---

## 🔗 Successive Percentage Changes

### Formula for Two Successive Changes

If two successive changes of a% and b%:
```
Net Change = a + b + (ab/100) %
```

**Example**: Two successive increases of 20% and 25%
```
Net = 20 + 25 + (20×25)/100 = 45 + 5 = 50%
```

**Example**: Increase of 20% followed by decrease of 20%
```
Net = 20 + (-20) + (20×(-20))/100 = 0 - 4 = -4%
```

**💡 Key Insight**: +x% followed by -x% ≠ 0%
```
Net = -x²/100 % (Always a loss!)
```

---

### Successive Same Percentage Changes

For n successive changes of r%:
```
Net Multiplier = (1 + r/100)ⁿ
```

**Example**: 3 successive increases of 10%
```
Multiplier = 1.1³ = 1.331
Net increase = 33.1%
```

---

## ⚖️ Comparison Percentages

### A is what % more/less than B

```
A is x% more than B → A = B × (1 + x/100)
A is x% less than B → A = B × (1 - x/100)
```

### Reverse Percentage

If A is x% more than B, then B is how much % less than A?

```
B is less than A by: (x / (100+x)) × 100 %
```

If A is x% less than B, then B is how much % more than A?
```
B is more than A by: (x / (100-x)) × 100 %
```

**Example**: A is 25% more than B. B is how much % less than A?
```
= (25/125) × 100 = 20%
```

**⚡ Quick Reference Table**:

| A more than B by | B less than A by |
|-----------------|------------------|
| 10% | 9.09% (1/11) |
| 20% | 16.67% (1/6) |
| 25% | 20% (1/5) |
| 33.33% | 25% (1/4) |
| 50% | 33.33% (1/3) |
| 100% | 50% (1/2) |

---

## 🧮 Population/Value Growth Problems

### Compound Growth Formula

```
Final = Initial × (1 + r/100)ⁿ

Where:
r = growth rate per period
n = number of periods
```

**Example**: Population grows 10% annually. Population after 3 years if current = 10000?
```
= 10000 × (1.1)³ = 10000 × 1.331 = 13310
```

### Depreciation Formula

```
Final = Initial × (1 - r/100)ⁿ
```

**Example**: Machine depreciates 20% annually. Value after 2 years if initial = 50000?
```
= 50000 × (0.8)² = 50000 × 0.64 = 32000
```

---

## 💡 Advanced Tricks

### Trick 1: Percentage of Percentage

x% of y% of N = (xy/10000) × N

**Example**: 20% of 30% of 500
```
= (20 × 30 / 10000) × 500 = 30
```

---

### Trick 2: Constant Product Rule

If A × B = Constant, and A changes by x%, then B changes by:
```
-x/(100+x) × 100 % (for increase)
x/(100-x) × 100 % (for decrease)
```

**Example**: Speed increases by 25%, journey time changes by?
```
(Distance = Speed × Time = Constant)
Time change = -25/125 × 100 = -20%
```

---

### Trick 3: Area/Volume Changes

For rectangle with sides changing by a% and b%:
```
Area change = a + b + ab/100 %
```

For cube/square with side changing by x%:
```
Area change ≈ 2x% (for small x)
Volume change ≈ 3x% (for small x)

Exact: Area = (1+x/100)² - 1 in percentage
       Volume = (1+x/100)³ - 1 in percentage
```

---

### Trick 4: Expenditure = Price × Consumption

```
If price ↑ by x%, to maintain same expenditure:
Consumption must ↓ by: x/(100+x) × 100 %

If price ↓ by x%, to maintain same expenditure:
Consumption must ↑ by: x/(100-x) × 100 %
```

**Example**: Sugar price increases by 25%. By what % should consumption reduce to maintain same expenditure?
```
= 25/125 × 100 = 20%
```

---

## ⚠️ Common Traps & Edge Cases

### Trap 1: Wrong Base
```
❌ A increased from B to C. % increase = (C-B)/C × 100
✅ % increase = (C-B)/B × 100 (Base is ORIGINAL)
```

### Trap 2: Percentage Points vs Percentage Change
```
Rate changed from 20% to 25%
Increase in percentage points = 5
% increase = (5/20) × 100 = 25%
```

### Trap 3: Successive ≠ Sum
```
10% + 10% ≠ 20%
1.1 × 1.1 = 1.21 = 21% increase
```

### Trap 4: Reverse Percentage Asymmetry
```
A is 50% more than B
B is NOT 50% less than A
B is 33.33% less than A
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| x% of N | N × x/100 |
| A is what % of B | (A/B) × 100 |
| % change | ((New-Old)/Old) × 100 |
| Successive a%, b% | a + b + ab/100 |
| Same x% twice | x² term appears |
| Reverse % | x/(100±x) × 100 |
| Growth n years | P(1+r/100)ⁿ |
| If A→B const product | x/(100+x) opposite |

---

## 📝 GATE-Level Practice

**Q1**: A's salary is 20% less than B's. B's salary is what % more than A's?
```
Let B = 100, then A = 80
B is more by = (20/80) × 100 = 25%
```

**Q2**: Price rises 20%, by what % reduce consumption to keep expenditure same?
```
= 20/120 × 100 = 16.67%
```

**Q3**: After two successive discounts of 20% and 10%, what is the net discount?
```
Net = 20 + 10 - (20×10)/100 = 28%
(Note: For discounts, subtract the ab/100 term)
Or: 0.8 × 0.9 = 0.72 = 28% off
```

**Q4**: A number increased by 20% and then decreased by 20%. Net change?
```
= 20 - 20 - 400/100 = -4% (decrease)
```

---

*← [Chapter 1 - Number Systems](./01_Number_Systems.md) | [Chapter 3 - Profit, Loss & Discount →](./03_Profit_Loss_Discount.md)*
