# 📊 Chapter 5: Data Interpretation

## The Atomic Truth
> **"Data speaks through patterns. Tables encode facts, graphs encode trends."**

---

## 📋 Topics Covered

1. [Tables](#1-tables)
2. [Bar Charts](#2-bar-charts)
3. [Line Graphs](#3-line-graphs)
4. [Pie Charts](#4-pie-charts)
5. [Mixed Graphs](#5-mixed-graphs)
6. [Data Sufficiency](#6-data-sufficiency)
7. [Calculation Shortcuts](#7-calculation-shortcuts)

---

## 1. Tables

### The Singularity
> **"A table is a matrix of facts. Rows and columns define the coordinate system."**

### The Root Architecture

A data table is a 2D structure:
$$\text{Value} = T[\text{Row}][\text{Column}]$$

---

### 🔑 Key Table Operations

| Operation | Formula |
|-----------|---------|
| Row Total | $\sum_j T[i][j]$ |
| Column Total | $\sum_i T[i][j]$ |
| Grand Total | $\sum_i \sum_j T[i][j]$ |
| Row Average | $\frac{\text{Row Total}}{\text{Number of Columns}}$ |
| Column Average | $\frac{\text{Column Total}}{\text{Number of Rows}}$ |
| Percentage of Row | $\frac{T[i][j]}{\text{Row Total}} \times 100\%$ |
| Percentage of Column | $\frac{T[i][j]}{\text{Column Total}} \times 100\%$ |

---

### 🎯 The Table Reading Strategy

```
Step 1: READ the title (understand what data represents)
Step 2: SCAN row and column headers (identify dimensions)
Step 3: NOTE units (thousands, lakhs, millions, %)
Step 4: IDENTIFY what's being asked (specific cell, total, comparison)
Step 5: LOCATE relevant cells
Step 6: COMPUTE using appropriate operation
```

---

### ⚠️ The Genius Trap

**Trap 1: Unit Confusion**
```
Table shows data in 'lakhs' but question asks in 'crores'
1 crore = 100 lakhs
Always convert units before answering!
```

**Trap 2: Percentage OF vs Percentage POINTS**
```
If value increases from 20% to 25%:
- Increase of 5 PERCENTAGE POINTS
- Increase of 25% (as a percentage of original 20%)

GATE often tests this distinction!
```

---

### 📝 Practice Problem

**Problem:** (GATE Pattern)
```
Table: Production of Cars (in thousands)

| Company | 2019 | 2020 | 2021 | 2022 |
|---------|------|------|------|------|
| A       | 150  | 180  | 200  | 220  |
| B       | 200  | 210  | 230  | 250  |
| C       | 180  | 190  | 185  | 210  |

Q1: What is the percentage increase in Company A's production from 2019 to 2022?
Q2: Which company had the highest average production over 4 years?
```

**Solution:**

Q1: Percentage Increase for Company A
$$\text{Increase} = \frac{220 - 150}{150} \times 100 = \frac{70}{150} \times 100 = 46.67\%$$

Q2: Average Production
- Company A: $\frac{150+180+200+220}{4} = \frac{750}{4} = 187.5$
- Company B: $\frac{200+210+230+250}{4} = \frac{890}{4} = 222.5$
- Company C: $\frac{180+190+185+210}{4} = \frac{765}{4} = 191.25$

**Answer:** Q1: 46.67%, Q2: Company B

---

## 2. Bar Charts

### The Singularity
> **"Bar height encodes magnitude. Compare heights, compare values."**

### The Root Architecture

In a bar chart:
$$\text{Value} = \text{Bar Height} \times \text{Scale Factor}$$

---

### 🔑 Types of Bar Charts

#### Simple Bar Chart
- Single bar per category
- Direct value comparison

#### Grouped Bar Chart
- Multiple bars per category
- Compare sub-categories within categories

#### Stacked Bar Chart
- Bars divided into segments
- Shows composition AND total

```
Simple:        Grouped:       Stacked:
  ▓             ▓░            ▓▓▓▓
  ▓▓            ▓▓░░          ░░░░
  ▓▓▓           ▓▓▓░░░        ▒▒▒▒
```

---

### 🎯 Bar Chart Reading Strategy

```
Step 1: CHECK axis labels and units
Step 2: NOTE the scale (where does axis start? is it 0?)
Step 3: READ bar heights carefully (use gridlines)
Step 4: For stacked bars, calculate segment heights by subtraction
Step 5: COMPARE using visual estimation first, then precise calculation
```

---

### ⚠️ The Genius Trap

**Trap 1: Non-Zero Baseline**
```
If Y-axis starts at 100 instead of 0:
- Visual difference is exaggerated
- Calculate actual values, not visual ratios!
```

**Trap 2: 3D Bar Charts**
```
In 3D charts, perspective can distort heights.
Always read from the scale, not visual impression.
```

---

### 📝 Practice Problem

**Problem:**
```
Bar Chart: Monthly Sales (in ₹ lakhs)

January:  ████████████ (60)
February: ████████████████ (80)
March:    ██████████████████ (90)
April:    ████████████ (60)
May:      ██████████████ (70)

Q: What is the average monthly sales?
Q: In which month was the sales closest to the average?
```

**Solution:**
$$\text{Average} = \frac{60 + 80 + 90 + 60 + 70}{5} = \frac{360}{5} = 72 \text{ lakhs}$$

Deviations from average:
- January: |60 - 72| = 12
- February: |80 - 72| = 8
- March: |90 - 72| = 18
- April: |60 - 72| = 12
- May: |70 - 72| = 2

**Answer:** Average = ₹72 lakhs, Closest month = May (deviation of 2)

---

## 3. Line Graphs

### The Singularity
> **"Lines show trends. Slopes indicate rate of change."**

### The Root Architecture

A line graph shows change over time:
$$\text{Slope} = \frac{\Delta y}{\Delta x} = \text{Rate of Change}$$

---

### 🔑 Key Line Graph Concepts

| Concept | Visual | Interpretation |
|---------|--------|----------------|
| Rising Line | ╱ | Increasing values |
| Falling Line | ╲ | Decreasing values |
| Flat Line | ─ | No change |
| Steep Slope | Nearly vertical | Rapid change |
| Gentle Slope | Nearly horizontal | Slow change |
| Intersection | × | Equal values at that point |

---

### 🎯 Line Graph Analysis

```
Step 1: IDENTIFY what X-axis and Y-axis represent
Step 2: NOTE scale and units
Step 3: TRACE the line for overall trend
Step 4: IDENTIFY peaks (maxima) and troughs (minima)
Step 5: CALCULATE specific values and changes as needed
```

---

### 🔑 Important Formulas

**Percentage Change:**
$$\% \text{ Change} = \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100$$

**Average Rate of Change:**
$$\text{Avg Rate} = \frac{y_{\text{final}} - y_{\text{initial}}}{x_{\text{final}} - x_{\text{initial}}}$$

**Compound Annual Growth Rate (CAGR):**
$$\text{CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{\frac{1}{n}} - 1$$

Where $n$ = number of years

---

### ⚠️ The Genius Trap

**Trap 1: Visual vs Actual Growth**
```
A line rising from 100 to 200 (100% increase)
Another rising from 1000 to 1100 (10% increase)

Visually they might look similar if scales are different!
Always calculate percentages.
```

**Trap 2: Extrapolation Beyond Data**
```
Never assume trends continue beyond the shown data.
Questions might trick you into extrapolating incorrectly.
```

---

### 📝 Practice Problem

**Problem:**
```
Line Graph: Company Revenue (₹ Crores)

Year:    2018   2019   2020   2021   2022
Value:   100    120    108    135    162

Q1: What was the year-on-year growth rate in 2019?
Q2: What was the CAGR from 2018 to 2022?
Q3: In which year did the revenue decline?
```

**Solution:**

Q1: Growth Rate in 2019
$$\text{Growth} = \frac{120 - 100}{100} \times 100 = 20\%$$

Q2: CAGR from 2018 to 2022
$$\text{CAGR} = \left(\frac{162}{100}\right)^{\frac{1}{4}} - 1 = (1.62)^{0.25} - 1$$
$$(1.62)^{0.25} \approx 1.128$$
$$\text{CAGR} \approx 12.8\%$$

Q3: Revenue Decline
- 2019 vs 2018: 120 > 100 (increase)
- 2020 vs 2019: 108 < 120 (decrease ✓)
- 2021 vs 2020: 135 > 108 (increase)
- 2022 vs 2021: 162 > 135 (increase)

**Answer:** Q1: 20%, Q2: 12.8%, Q3: 2020

---

## 4. Pie Charts

### The Singularity
> **"A pie is 360°. Each slice's angle is proportional to its value."**

### The Root Architecture

$$\text{Angle of slice} = \frac{\text{Value of slice}}{\text{Total}} \times 360°$$

$$\text{Percentage of slice} = \frac{\text{Angle of slice}}{360°} \times 100\%$$

---

### 🔑 Key Pie Chart Formulas

| Conversion | Formula |
|------------|---------|
| Value to Angle | $\theta = \frac{V}{T} \times 360°$ |
| Angle to Percentage | $\% = \frac{\theta}{360} \times 100$ |
| Percentage to Value | $V = \% \times \frac{T}{100}$ |
| Angle to Value | $V = \frac{\theta}{360} \times T$ |

**Quick Conversion Table:**

| Percentage | Angle |
|------------|-------|
| 10% | 36° |
| 20% | 72° |
| 25% | 90° |
| 50% | 180° |
| 75% | 270° |
| 100% | 360° |

---

### 🎯 Pie Chart Reading Strategy

```
Step 1: NOTE the total value (if given)
Step 2: READ angles or percentages for each slice
Step 3: CONVERT as needed (angle ↔ percentage ↔ value)
Step 4: For comparison, calculate actual values, not just percentages
Step 5: For change across two pie charts, align categories carefully
```

---

### ⚠️ The Genius Trap

**Trap 1: Comparing Pie Charts of Different Sizes**
```
Pie Chart A: Total = ₹100 crores, Segment X = 30%
Pie Chart B: Total = ₹200 crores, Segment X = 20%

Segment X in A = ₹30 crores
Segment X in B = ₹40 crores

Even though 30% > 20%, the absolute value in B is higher!
```

**Trap 2: Multiple Pie Charts with Different Totals**
```
Always check if totals are the same before comparing percentages.
```

---

### 📝 Practice Problem

**Problem:**
```
Pie Chart: Monthly Expenditure (Total = ₹60,000)

Rent: 90°
Food: 72°
Transport: 54°
Utilities: 36°
Savings: 72°
Others: 36°

Q1: How much is spent on Food?
Q2: What percentage is saved?
Q3: How much more is spent on Rent than Transport?
```

**Solution:**

Q1: Food Expenditure
$$\text{Food} = \frac{72}{360} \times 60000 = \frac{72 \times 60000}{360} = ₹12,000$$

Q2: Savings Percentage
$$\% = \frac{72}{360} \times 100 = 20\%$$

Q3: Rent vs Transport
$$\text{Rent} = \frac{90}{360} \times 60000 = ₹15,000$$
$$\text{Transport} = \frac{54}{360} \times 60000 = ₹9,000$$
$$\text{Difference} = ₹15,000 - ₹9,000 = ₹6,000$$

**Answer:** Q1: ₹12,000, Q2: 20%, Q3: ₹6,000

---

## 5. Mixed Graphs

### The Singularity
> **"Combined representations demand combined reading skills."**

### 🔑 Common Mixed Graph Types

1. **Bar + Line:** Bars show absolute values, line shows trend/average
2. **Pie + Table:** Pie shows composition, table provides additional details
3. **Multiple Y-axes:** Two different metrics on same X-axis
4. **Stacked Bar + Line:** Composition with overlay trend

---

### 🎯 Mixed Graph Strategy

```
Step 1: IDENTIFY each component (bar, line, pie)
Step 2: NOTE what each component represents
Step 3: CHECK if scales are same or different (especially dual Y-axis)
Step 4: READ data from appropriate component for each question
Step 5: COMBINE data carefully, watching units
```

---

### ⚠️ The Genius Trap

**Trap: Dual Y-Axis Confusion**
```
Left Y-axis: Sales (in thousands)
Right Y-axis: Growth rate (in %)

Bar height of 50 on left axis = 50,000 units
Line value at 50 on right axis = 50%

These are completely different metrics!
```

---

## 6. Data Sufficiency

### The Singularity
> **"The question is not 'what is the answer?' but 'CAN you find the answer?'"**

### The Root Architecture

Data Sufficiency tests whether given information is sufficient to answer a question, NOT what the answer is.

---

### 🔑 Standard Answer Choices

| Choice | Meaning |
|--------|---------|
| (A) | Statement 1 ALONE is sufficient, but Statement 2 alone is not |
| (B) | Statement 2 ALONE is sufficient, but Statement 1 alone is not |
| (C) | BOTH statements TOGETHER are sufficient, but neither alone |
| (D) | EACH statement ALONE is sufficient |
| (E) | Statements 1 and 2 TOGETHER are NOT sufficient |

---

### 🎯 The Data Sufficiency Algorithm

```
Step 1: READ the question carefully (what's being asked?)
Step 2: TEST Statement 1 alone
        - Can you answer the question with ONLY this info?
        - If YES: Mark S1 sufficient
        - If NO: Mark S1 insufficient
Step 3: FORGET Statement 1, TEST Statement 2 alone
        - Same process
Step 4: If neither alone is sufficient, TEST BOTH together
Step 5: SELECT answer based on sufficiency pattern
```

---

### ⚠️ The Genius Trap

**Trap 1: Calculating Instead of Testing**
```
You don't need the actual answer!
Just determine if it's POSSIBLE to find the answer.
```

**Trap 2: Using Information from One Statement in Another**
```
When testing Statement 2 alone, completely ignore Statement 1.
```

**Trap 3: Assuming Additional Information**
```
Only use what's given. No real-world assumptions allowed.
```

---

### 📝 Practice Problem

**Problem:**
```
Question: What is the value of x + y?

Statement 1: x = 3y
Statement 2: x - y = 10

(A) Statement 1 alone is sufficient
(B) Statement 2 alone is sufficient
(C) Both together are sufficient
(D) Each alone is sufficient
(E) Neither is sufficient
```

**Solution:**

Testing Statement 1 alone: x = 3y
- We have x + y = 3y + y = 4y
- But we don't know y → INSUFFICIENT

Testing Statement 2 alone: x - y = 10
- We cannot find x + y from just x - y → INSUFFICIENT

Testing Both Together:
- From S1: x = 3y
- From S2: x - y = 10 → 3y - y = 10 → 2y = 10 → y = 5
- Therefore x = 15, x + y = 20 → SUFFICIENT

**Answer:** (C) Both statements together are sufficient

---

## 7. Calculation Shortcuts

### The Singularity
> **"Speed is accuracy divided by time. Shortcuts multiply speed."**

---

### 🔑 Essential Shortcuts

#### Percentage Shortcuts

| Percentage | Shortcut |
|------------|----------|
| 10% | Divide by 10 |
| 5% | Half of 10% |
| 1% | Divide by 100 |
| 25% | Divide by 4 |
| 33.33% | Divide by 3 |
| 50% | Divide by 2 |
| 75% | Multiply by 3, divide by 4 |

#### Quick Multiplication

| Pattern | Shortcut |
|---------|----------|
| ×11 | Sum of digits placed between (for 2-digit) |
| ×25 | Divide by 4, multiply by 100 |
| ×50 | Divide by 2, multiply by 100 |
| ×125 | Divide by 8, multiply by 1000 |

**Example:** 48 × 25 = 48 ÷ 4 × 100 = 12 × 100 = 1200

#### Fraction-Percentage Equivalents

| Fraction | Percentage | Fraction | Percentage |
|----------|------------|----------|------------|
| 1/2 | 50% | 1/6 | 16.67% |
| 1/3 | 33.33% | 1/7 | 14.28% |
| 1/4 | 25% | 1/8 | 12.5% |
| 1/5 | 20% | 1/9 | 11.11% |

---

#### Quick Division

| Divisor | Shortcut |
|---------|----------|
| ÷5 | ×2, ÷10 |
| ÷25 | ×4, ÷100 |
| ÷125 | ×8, ÷1000 |
| ÷8 | ÷2, ÷2, ÷2 |

---

#### Approximation Rules

1. **Round to nearest 5 or 10** for quick estimates
2. **Bound the answer** (calculate lower and upper limits)
3. **Use significant figures** (first 2-3 digits matter most)

**Example:**
$$\frac{4872}{243} \approx \frac{4900}{245} = \frac{4900}{245} = 20$$

Actual: 20.05 (very close!)

---

### 📝 Practice: Speed Calculation

**Problem:**
```
Calculate: 785 × 125 ÷ 25
```

**Solution using shortcuts:**
$$785 \times 125 \div 25 = 785 \times \frac{125}{25} = 785 \times 5 = 3925$$

Or:
$$785 \times 125 = 785 \times \frac{1000}{8} = \frac{785000}{8} = 98125$$
$$98125 \div 25 = 98125 \times \frac{4}{100} = \frac{392500}{100} = 3925$$

**Answer:** 3925

---

## 🧠 The DI Mnemonic: "READS"

- **R**ecognize chart type and structure
- **E**xamine axes, scales, and units
- **A**nalyze what's being asked
- **D**etermine relevant data points
- **S**olve using shortcuts when possible

---

## 📊 Quick Reference Card

### Common Percentage Changes

| Change | Calculation | Reverse |
|--------|-------------|---------|
| +10% | ×1.1 | ÷1.1 or ×0.909 |
| +20% | ×1.2 | ÷1.2 or ×0.833 |
| +25% | ×1.25 | ÷1.25 or ×0.8 |
| +50% | ×1.5 | ÷1.5 or ×0.667 |
| -10% | ×0.9 | ÷0.9 or ×1.111 |
| -20% | ×0.8 | ÷0.8 or ×1.25 |
| -25% | ×0.75 | ÷0.75 or ×1.333 |

### Successive Percentage Change

If value changes by $a\%$ and then by $b\%$:
$$\text{Net Change} = a + b + \frac{ab}{100}\%$$

**Example:** +10% then +20%
$$\text{Net} = 10 + 20 + \frac{10 \times 20}{100} = 32\%$$

---

## 🎯 Mastery Checklist

- [ ] Can read any table and extract required data in 10 seconds
- [ ] Can convert between angles, percentages, and values for pie charts
- [ ] Know all percentage-fraction equivalents by heart
- [ ] Can calculate CAGR without a calculator
- [ ] Can solve data sufficiency without calculating actual values
- [ ] Can approximate complex calculations within 5% error
- [ ] Can complete a 5-question DI set in under 5 minutes

---

## ⏱️ The 5-Second Snap-Check

| Check | What to Verify |
|-------|---------------|
| ✅ Units | Are values in same units as question asks? |
| ✅ Scale | Did I read from correct scale (especially dual-axis)? |
| ✅ Bounds | Is answer within reasonable range? |
| ✅ Direction | If percentage change, is sign correct (+/-)? |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

[← Back to Main Index](../README.md) | [Previous: Analytical Reasoning](../Analytical-Reasoning/README.md) | [Next: Critical Reasoning →](../Critical-Reasoning/README.md)
