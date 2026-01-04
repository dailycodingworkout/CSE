# Data Interpretation - Complete Study Material
## For GATE | ESE | PSU | BANK Examinations

---

## Table of Contents

1. [Introduction to Data Interpretation](#1-introduction-to-data-interpretation)
2. [Types of Data Interpretation](#2-types-of-data-interpretation)
3. [Tables](#3-tables)
4. [Bar Charts](#4-bar-charts)
5. [Pie Charts](#5-pie-charts)
6. [Line Graphs](#6-line-graphs)
7. [Mixed/Caselets](#7-mixedcaselets)
8. [Essential Calculation Techniques](#8-essential-calculation-techniques)
9. [Percentage Tricks & Shortcuts](#9-percentage-tricks--shortcuts)
10. [Ratio & Proportion Mastery](#10-ratio--proportion-mastery)
11. [Average & Weighted Average](#11-average--weighted-average)
12. [Approximation Techniques](#12-approximation-techniques)
13. [Common Traps & Edge Cases](#13-common-traps--edge-cases)
14. [Exam-Specific Strategies](#14-exam-specific-strategies)
15. [Practice Problems with Solutions](#15-practice-problems-with-solutions)
16. [Quick Reference Formulas](#16-quick-reference-formulas)

---

## 1. Introduction to Data Interpretation

### What is Data Interpretation?

**Atomic Truth:** *Converting raw data into actionable insights.*

Data Interpretation (DI) is the process of analyzing, organizing, and making sense of collected data presented in various formats like tables, charts, graphs, or combinations thereof.

### Why is DI Important?

| Exam | DI Weightage | Marks | Time Pressure |
|------|-------------|-------|---------------|
| GATE | 10-15 marks | 10-15% | High |
| ESE | 10-15 marks | 10-15% | High |
| PSU | 20-30 marks | 15-25% | Medium-High |
| BANK (Prelims) | 15-20 marks | 15-25% | Extreme |
| BANK (Mains) | 30-40 marks | 25-35% | Extreme |

### The Mental Framework

```
Data → Pattern Recognition → Calculation → Verification → Answer
```

**Key Insight:** DI tests not just your math skills but your ability to:
1. **Extract** relevant information quickly
2. **Ignore** irrelevant data
3. **Calculate** efficiently (not necessarily accurately to the decimal)
4. **Verify** through logical bounds

---

## 2. Types of Data Interpretation

### 2.1 Classification by Format

| Type | Description | Difficulty | Frequency |
|------|-------------|------------|-----------|
| **Tables** | Raw numerical data in rows/columns | Easy-Medium | Very High |
| **Bar Charts** | Vertical/Horizontal bars representing values | Easy | High |
| **Pie Charts** | Circular representation of parts of whole | Medium | High |
| **Line Graphs** | Trends over time/categories | Medium | Medium |
| **Caselets** | Data given in paragraph form | High | Medium |
| **Mixed DI** | Combination of 2+ formats | High | Medium-High |
| **Radar/Spider Charts** | Multi-dimensional data | Very High | Low |
| **Missing DI** | Incomplete data to be calculated | Very High | Low-Medium |

### 2.2 Classification by Complexity

```
Level 1: Direct Reading
↓
Level 2: Simple Calculation (Add/Subtract)
↓
Level 3: Intermediate Calculation (%, Ratio)
↓
Level 4: Complex Calculation (Multiple Steps)
↓
Level 5: Inference & Analysis
```

---

## 3. Tables

### 3.1 Understanding Table Structure

**Example: Company Sales Data (in Lakhs)**

| Year | Product A | Product B | Product C | Product D | Total |
|------|-----------|-----------|-----------|-----------|-------|
| 2019 | 120 | 85 | 200 | 95 | 500 |
| 2020 | 135 | 90 | 210 | 105 | 540 |
| 2021 | 150 | 100 | 180 | 120 | 550 |
| 2022 | 165 | 95 | 220 | 130 | 610 |
| 2023 | 180 | 110 | 250 | 140 | 680 |

### 3.2 Types of Questions

#### Type 1: Direct Value Questions
*"What is the sales of Product C in 2021?"*

**Answer:** 180 lakhs (Direct reading)

**Time:** < 5 seconds

#### Type 2: Comparison Questions
*"In which year was the sales of Product A the highest?"*

**Method:** Scan the Product A column → Find maximum
**Answer:** 2023 (180 lakhs)

**Time:** 10-15 seconds

#### Type 3: Aggregate Questions
*"What is the total sales of all products in 2020?"*

**Method:** Read the Total column or sum: 135 + 90 + 210 + 105 = 540
**Answer:** 540 lakhs

**Time:** 15-20 seconds

#### Type 4: Percentage Questions
*"What percentage of total sales in 2019 was from Product C?"*

**Formula:** (Product C sales / Total sales) × 100
**Calculation:** (200/500) × 100 = 40%

**Trick:** 200/500 = 2/5 = 0.4 = 40%

#### Type 5: Growth/Change Questions
*"What is the percentage increase in Product A sales from 2019 to 2023?"*

**Formula:** ((Final - Initial) / Initial) × 100

**Calculation:** ((180 - 120) / 120) × 100 = (60/120) × 100 = 50%

**Trick:** 60/120 = 1/2 = 50%

#### Type 6: Ratio Questions
*"What is the ratio of Product B sales to Product D sales in 2021?"*

**Calculation:** 100 : 120 = 5 : 6

**Trick:** Divide both by HCF (20)

### 3.3 Table Reading Strategies

**The 5-Step Method:**

1. **Scan Headers** (5 sec) - Understand what rows/columns represent
2. **Note Units** (3 sec) - Lakhs? Crores? Thousands?
3. **Identify Totals** (3 sec) - Are totals given or to be calculated?
4. **Read Question** (5 sec) - What exactly is being asked?
5. **Locate Data** (5 sec) - Find the relevant cells

**Golden Rule:** *Never calculate what you can read directly.*

---

## 4. Bar Charts

### 4.1 Types of Bar Charts

#### Simple Bar Chart
- Single set of bars
- Direct value comparison

#### Grouped/Clustered Bar Chart
- Multiple bars per category
- Comparison across categories and within groups

#### Stacked Bar Chart
- Bars divided into segments
- Shows part-to-whole relationships

#### Horizontal Bar Chart
- Same as vertical but rotated
- Better for long category names

### 4.2 Reading Bar Charts

**Example Scenario:**
```
Production (in '000 units)

     2019  2020  2021  2022  2023
     ----  ----  ----  ----  ----
A:   |40|  |45|  |50|  |55|  |60|
B:   |30|  |35|  |40|  |45|  |50|
C:   |25|  |30|  |35|  |30|  |40|
```

### 4.3 Common Question Types

#### Estimation from Scale
*"Approximate production of A in 2020?"*

**Technique:**
1. Locate the bar
2. Read against the Y-axis scale
3. If exact value not on gridline, estimate

**Critical Insight:** In exams, bar heights are deliberately placed between gridlines. Master the skill of proportional reading.

#### Finding Differences
*"By how much did production of B exceed that of C in 2023?"*

**Calculation:** 50 - 40 = 10 ('000 units)

#### Finding Ratios
*"What is the ratio of A's production to B's production in 2021?"*

**Calculation:** 50 : 40 = 5 : 4

### 4.4 Bar Chart Tricks

**Trick 1: Visual Comparison**
Instead of calculating each value, compare bar heights visually for "maximum" or "minimum" questions.

**Trick 2: Proportional Reading**
If scale shows 0, 20, 40, 60... and bar is at 3/4 between 40 and 60:
Value ≈ 40 + (3/4 × 20) = 40 + 15 = 55

**Trick 3: Stacked Bar Segments**
In stacked bars, to find a segment's value:
Value = Top of segment - Bottom of segment

---

## 5. Pie Charts

### 5.1 Fundamentals

**Core Principle:** A pie chart represents **100%** or **360°**

**Key Relationships:**

| Percentage | Degree | Fraction |
|------------|--------|----------|
| 100% | 360° | 1 |
| 50% | 180° | 1/2 |
| 25% | 90° | 1/4 |
| 20% | 72° | 1/5 |
| 12.5% | 45° | 1/8 |
| 10% | 36° | 1/10 |
| 5% | 18° | 1/20 |
| 1% | 3.6° | 1/100 |

**Conversion Formulas:**
- Degree to Percentage: (Degree / 360) × 100
- Percentage to Degree: (Percentage / 100) × 360
- Percentage to Value: (Percentage / 100) × Total

### 5.2 Pie Chart Example

**Company Budget Distribution (Total: ₹500 Crores)**

```
           Salaries
             40%
        .---------. 
      .'           `.
     /   Marketing   \
    |      20%        |
    |   .-------.     |
    |  /         \    |
     \|   R&D    |   /
      \   15%   /   /
       `.     .'   /
         `---'    /
     Operations  /
        25%    /
        ------'
```

| Category | Percentage | Degrees | Value (Crores) |
|----------|------------|---------|----------------|
| Salaries | 40% | 144° | 200 |
| Operations | 25% | 90° | 125 |
| Marketing | 20% | 72° | 100 |
| R&D | 15% | 54° | 75 |
| **Total** | **100%** | **360°** | **500** |

### 5.3 Question Types

#### Type 1: Finding Absolute Value
*"What is the budget for R&D?"*

**Calculation:** 15% of 500 = 0.15 × 500 = 75 Crores

**Quick Method:** 15% = 10% + 5% = 50 + 25 = 75

#### Type 2: Finding Difference
*"How much more is spent on Salaries than Marketing?"*

**Calculation:** (40% - 20%) of 500 = 20% of 500 = 100 Crores

#### Type 3: Ratio Between Sectors
*"What is the ratio of Operations budget to R&D budget?"*

**Calculation:** 25% : 15% = 25 : 15 = 5 : 3

**Insight:** When finding ratios, you don't need the total value—just use percentages directly!

#### Type 4: Combined Sectors
*"What percentage of budget is spent on Salaries and Operations together?"*

**Calculation:** 40% + 25% = 65%

#### Type 5: Degree-Based Questions
*"What is the central angle for Marketing?"*

**Calculation:** 20% of 360° = 72°

### 5.4 Pie Chart Shortcuts

**Shortcut 1: Sector Comparison**
Larger sector = Larger percentage (visual comparison without calculation)

**Shortcut 2: Quick Percentage Estimation**
- Quarter of pie ≈ 25%
- Third of pie ≈ 33.33%
- One-sixth of pie ≈ 16.67%

**Shortcut 3: The Complement Rule**
If asked "What percentage is NOT Category X?"
Answer = 100% - X%

**Shortcut 4: Using Degrees for Comparison**
If Sector A = 90° and Sector B = 45°
Ratio A:B = 90:45 = 2:1

---

## 6. Line Graphs

### 6.1 Understanding Line Graphs

**Purpose:** Show trends, changes over time, comparisons across periods

**Components:**
- X-axis: Usually time periods (years, months, quarters)
- Y-axis: The measured quantity
- Line(s): Connect data points to show trend

### 6.2 Example Line Graph

**Temperature Variation (°C) Over a Week**

```
40 |                        *
35 |           *    *      / \
30 |      *   / \  / \    /   *
25 |     / \ /   \/   \  /
20 |    /   *          \/
15 |   *
10 |
   +---+---+---+---+---+---+---+
     Mon Tue Wed Thu Fri Sat Sun

Mon: 15°C, Tue: 30°C, Wed: 25°C, Thu: 35°C
Fri: 32°C, Sat: 25°C, Sun: 40°C
```

### 6.3 Key Concepts

#### Trend Analysis
- **Upward Trend:** Line moving from bottom-left to top-right
- **Downward Trend:** Line moving from top-left to bottom-right
- **Flat Trend:** Horizontal line
- **Volatile:** Line with many ups and downs

#### Rate of Change
- **Steep slope:** Rapid change
- **Gentle slope:** Gradual change
- **Horizontal:** No change

#### Identifying Peaks and Troughs
- **Peak (Maximum):** Highest point on the line
- **Trough (Minimum):** Lowest point on the line

### 6.4 Question Types

#### Finding Maximum/Minimum
*"On which day was the temperature highest?"*

**Answer:** Sunday (40°C) - Visual identification

#### Calculating Increase/Decrease
*"What is the increase in temperature from Monday to Sunday?"*

**Calculation:** 40 - 15 = 25°C

#### Percentage Change
*"What is the percentage increase from Monday to Tuesday?"*

**Formula:** ((New - Old) / Old) × 100
**Calculation:** ((30 - 15) / 15) × 100 = (15/15) × 100 = 100%

#### Average Calculation
*"What is the average temperature for the week?"*

**Calculation:** (15 + 30 + 25 + 35 + 32 + 25 + 40) / 7 = 202/7 ≈ 28.86°C

#### Finding Specific Changes
*"On how many days did temperature decrease from the previous day?"*

**Analysis:**
- Mon → Tue: 15 → 30 (Increase)
- Tue → Wed: 30 → 25 (Decrease) ✓
- Wed → Thu: 25 → 35 (Increase)
- Thu → Fri: 35 → 32 (Decrease) ✓
- Fri → Sat: 32 → 25 (Decrease) ✓
- Sat → Sun: 25 → 40 (Increase)

**Answer:** 3 days

### 6.5 Multi-Line Graph Analysis

When comparing multiple lines:

1. **Parallel lines:** Similar trends
2. **Converging lines:** Gap decreasing
3. **Diverging lines:** Gap increasing
4. **Crossing lines:** One overtakes another

---

## 7. Mixed/Caselets

### 7.1 What are Caselets?

Caselets present data in **paragraph form** rather than structured tables or charts. They require you to:
1. Extract relevant numbers
2. Organize data mentally or on paper
3. Solve questions based on inferred relationships

### 7.2 Example Caselet

**Passage:**
*"A company has three departments: HR, Finance, and IT. The IT department has 120 employees, which is 40% of the total workforce. The HR department has 25% fewer employees than the IT department. The remaining employees work in Finance. If 60% of IT employees are male and the ratio of male to female in HR is 2:1, find the required values."*

**Step-by-Step Extraction:**

| Information | Value |
|-------------|-------|
| IT employees | 120 |
| IT = 40% of total | Total = 120/0.4 = 300 |
| HR = 25% less than IT | HR = 120 - 30 = 90 |
| Finance | 300 - 120 - 90 = 90 |
| IT males | 60% of 120 = 72 |
| IT females | 120 - 72 = 48 |
| HR male:female = 2:1 | Males = 60, Females = 30 |

### 7.3 Caselet Solving Strategy

**The DEOS Method:**

1. **D**etect key numbers (underline/highlight)
2. **E**stablish relationships (equations/ratios)
3. **O**rganize into table format
4. **S**olve systematically

### 7.4 Mixed DI (Combination Charts)

**Example:** A pie chart showing distribution + A table showing actual values

**Key:** Cross-reference data between representations

**Common Combinations:**
- Pie + Table
- Bar + Line
- Two Pie Charts
- Table + Caselet

**Strategy:** Identify the connecting element between representations

---

## 8. Essential Calculation Techniques

### 8.1 Mental Math Foundations

#### Multiplication Tables (Must Know Instantly)

| × | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| 12 | 24 | 36 | 48 | 60 | 72 | 84 | 96 | 108 |
| 13 | 26 | 39 | 52 | 65 | 78 | 91 | 104 | 117 |
| 14 | 28 | 42 | 56 | 70 | 84 | 98 | 112 | 126 |
| 15 | 30 | 45 | 60 | 75 | 90 | 105 | 120 | 135 |
| 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 |
| 17 | 34 | 51 | 68 | 85 | 102 | 119 | 136 | 153 |
| 18 | 36 | 54 | 72 | 90 | 108 | 126 | 144 | 162 |
| 19 | 38 | 57 | 76 | 95 | 114 | 133 | 152 | 171 |

#### Squares (1-30)

| n | n² | n | n² | n | n² |
|---|-----|---|-----|---|-----|
| 1 | 1 | 11 | 121 | 21 | 441 |
| 2 | 4 | 12 | 144 | 22 | 484 |
| 3 | 9 | 13 | 169 | 23 | 529 |
| 4 | 16 | 14 | 196 | 24 | 576 |
| 5 | 25 | 15 | 225 | 25 | 625 |
| 6 | 36 | 16 | 256 | 26 | 676 |
| 7 | 49 | 17 | 289 | 27 | 729 |
| 8 | 64 | 18 | 324 | 28 | 784 |
| 9 | 81 | 19 | 361 | 29 | 841 |
| 10 | 100 | 20 | 400 | 30 | 900 |

#### Cubes (1-15)

| n | n³ |
|---|------|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |
| 4 | 64 |
| 5 | 125 |
| 6 | 216 |
| 7 | 343 |
| 8 | 512 |
| 9 | 729 |
| 10 | 1000 |
| 11 | 1331 |
| 12 | 1728 |
| 13 | 2197 |
| 14 | 2744 |
| 15 | 3375 |

### 8.2 Division Tricks

#### Division by 5
Multiply by 2, then divide by 10

**Example:** 245 ÷ 5 = 245 × 2 ÷ 10 = 490 ÷ 10 = 49

#### Division by 25
Multiply by 4, then divide by 100

**Example:** 175 ÷ 25 = 175 × 4 ÷ 100 = 700 ÷ 100 = 7

#### Division by 50
Multiply by 2, then divide by 100

**Example:** 350 ÷ 50 = 350 × 2 ÷ 100 = 700 ÷ 100 = 7

#### Division by 125
Multiply by 8, then divide by 1000

**Example:** 625 ÷ 125 = 625 × 8 ÷ 1000 = 5000 ÷ 1000 = 5

### 8.3 Multiplication Tricks

#### Multiplying by 11
Add the digits, put sum in middle

**Example:** 34 × 11 = 3(3+4)4 = 374

**For carry:** 78 × 11 = 7(7+8)8 = 7(15)8 = 858

#### Multiplying by 9, 99, 999
Subtract from next power of 10

**Example:** 47 × 9 = 47 × 10 - 47 = 470 - 47 = 423
**Example:** 34 × 99 = 34 × 100 - 34 = 3400 - 34 = 3366

#### Multiplying numbers near 100
(100-a) × (100-b) = 10000 - 100(a+b) + ab

**Example:** 97 × 96 = (100-3) × (100-4) = 10000 - 700 + 12 = 9312

### 8.4 Vedic Mathematics Techniques

#### Nikhilam Method (Near Base)
For numbers close to a base (10, 100, 1000)

**Example:** 88 × 97 (Base 100)
- 88 is 12 below 100
- 97 is 3 below 100
- Product: (88-3) or (97-12) | (12×3) = 85|36 = 8536

#### Urdhva-Tiryagbhyam (Vertically and Crosswise)
For general multiplication

**Example:** 23 × 14
```
  2  3
  ×  ×
  1  4
  
Step 1: 3 × 4 = 12 (units: 2, carry: 1)
Step 2: (2×4) + (3×1) = 8 + 3 = 11 + 1(carry) = 12 (tens: 2, carry: 1)
Step 3: 2 × 1 = 2 + 1(carry) = 3 (hundreds)

Answer: 322
```

---

## 9. Percentage Tricks & Shortcuts

### 9.1 Percentage Fundamentals

**Definition:** "Per cent" = "Per hundred" = Out of 100

**Basic Formula:** Percentage = (Part / Whole) × 100

### 9.2 Percentage-Fraction Equivalents (MUST MEMORIZE)

| Fraction | Percentage | Fraction | Percentage |
|----------|------------|----------|------------|
| 1/2 | 50% | 1/8 | 12.5% |
| 1/3 | 33.33% | 2/3 | 66.67% |
| 1/4 | 25% | 3/4 | 75% |
| 1/5 | 20% | 2/5 | 40% |
| 1/6 | 16.67% | 5/6 | 83.33% |
| 1/7 | 14.28% | 2/7 | 28.57% |
| 1/9 | 11.11% | 1/11 | 9.09% |
| 1/10 | 10% | 1/12 | 8.33% |
| 1/15 | 6.67% | 1/20 | 5% |
| 1/25 | 4% | 1/50 | 2% |

### 9.3 Breaking Down Percentages

**The Building Block Method:**

Calculate 10% and 1%, then combine:

**Example:** Find 37% of 450
- 10% of 450 = 45
- 30% = 45 × 3 = 135
- 1% = 4.5
- 7% = 4.5 × 7 = 31.5
- 37% = 135 + 31.5 = 166.5

**Example:** Find 76% of 250
- 50% of 250 = 125
- 25% of 250 = 62.5
- 1% = 2.5
- 76% = 75% + 1% = (50% + 25%) + 1% = 125 + 62.5 + 2.5 = 190

### 9.4 Percentage Change Formula

**Formula:** % Change = ((New - Old) / Old) × 100

**For Increase:** ((Final - Initial) / Initial) × 100

**For Decrease:** ((Initial - Final) / Initial) × 100

### 9.5 Successive Percentage Changes

**Formula:** Net % = a + b + (a×b)/100

Where a and b are successive percentage changes

**Example:** Two successive increases of 10% each
Net % = 10 + 10 + (10×10)/100 = 20 + 1 = 21%

**Example:** 20% increase followed by 10% decrease
Net % = 20 + (-10) + (20×(-10))/100 = 10 - 2 = 8% increase

### 9.6 The Net Effect Table (For Quick Reference)

| First Change | Second Change | Net Effect |
|--------------|---------------|------------|
| +10% | +10% | +21% |
| +20% | +20% | +44% |
| +25% | -20% | 0% |
| +20% | -20% | -4% |
| +10% | -10% | -1% |
| +50% | -50% | -25% |
| +100% | -50% | 0% |

**Golden Insight:** An x% increase followed by x% decrease always results in a net LOSS of (x²/100)%

### 9.7 Reverse Percentage Problems

**If something increases by x%, to get back to original, decrease by:**
(x / (100 + x)) × 100

**Example:** If price increases by 25%, what decrease brings it back?
Decrease = (25/125) × 100 = 20%

**If something decreases by x%, to get back to original, increase by:**
(x / (100 - x)) × 100

**Example:** If salary decreases by 20%, what increase restores it?
Increase = (20/80) × 100 = 25%

---

## 10. Ratio & Proportion Mastery

### 10.1 Basic Concepts

**Ratio:** Comparison of two quantities of the same kind
- Notation: a:b or a/b
- a is antecedent, b is consequent

**Proportion:** Equality of two ratios
- If a:b = c:d, then a, b, c, d are in proportion
- Product of extremes = Product of means (a × d = b × c)

### 10.2 Types of Ratios

| Type | Definition | Example |
|------|------------|---------|
| **Duplicate Ratio** | a² : b² | Duplicate of 2:3 is 4:9 |
| **Triplicate Ratio** | a³ : b³ | Triplicate of 2:3 is 8:27 |
| **Sub-duplicate Ratio** | √a : √b | Sub-duplicate of 4:9 is 2:3 |
| **Inverse/Reciprocal Ratio** | b : a | Inverse of 2:3 is 3:2 |
| **Compound Ratio** | (a×c) : (b×d) | 2:3 and 4:5 → 8:15 |

### 10.3 Ratio Operations

#### Finding Actual Values from Ratio

**If A:B = 3:4 and total = 70**
- Sum of ratio parts = 3 + 4 = 7
- A = (3/7) × 70 = 30
- B = (4/7) × 70 = 40

#### Combining Ratios

**If A:B = 2:3 and B:C = 4:5, find A:B:C**

Method: Make B same in both ratios
- A:B = 2:3 → Multiply by 4 → A:B = 8:12
- B:C = 4:5 → Multiply by 3 → B:C = 12:15
- A:B:C = 8:12:15

#### Dividing in Given Ratio

**Divide 120 in ratio 2:3:5**
- Sum = 2 + 3 + 5 = 10
- Parts: (2/10)×120 = 24, (3/10)×120 = 36, (5/10)×120 = 60

### 10.4 The Alligation Method

**For mixing two items to get a mean value:**

```
       Cost of cheaper          Cost of dearer
            |                        |
            v                        v
    (d - m) <------ Mean ------> (m - c)
```

**Ratio = (d - m) : (m - c)**

Where:
- c = cheaper price
- d = dearer price  
- m = mean price

**Example:** Mix rice at ₹20/kg with rice at ₹30/kg to get mixture worth ₹24/kg

```
    20                          30
      \                        /
       \      24              /
        \    /   \           /
        (30-24)   (24-20)
           6    :    4
           3    :    2
```

**Ratio = 3:2** (cheaper : dearer)

### 10.5 Partnership Ratio

**Simple Partnership:** Profit ratio = Capital ratio

**Compound Partnership:** Profit ratio = (Capital × Time) ratio

**Example:** A invests ₹10,000 for 12 months, B invests ₹15,000 for 8 months
- A's share: 10,000 × 12 = 120,000
- B's share: 15,000 × 8 = 120,000
- Ratio = 1:1

---

## 11. Average & Weighted Average

### 11.1 Simple Average

**Formula:** Average = Sum of observations / Number of observations

**Properties:**
1. Average lies between smallest and largest values
2. Sum of deviations from average = 0
3. If all values are increased by k, average increases by k
4. If all values are multiplied by k, average is multiplied by k

### 11.2 Weighted Average

**Formula:** Weighted Average = Σ(Value × Weight) / Σ(Weight)

**Example:** 
- Subject A: Marks = 80, Credit = 3
- Subject B: Marks = 70, Credit = 4
- Subject C: Marks = 90, Credit = 3

Weighted Avg = (80×3 + 70×4 + 90×3) / (3+4+3) = (240 + 280 + 270) / 10 = 79

### 11.3 Average in DI Context

**Finding Average from Data:**

| Year | Sales |
|------|-------|
| 2019 | 100 |
| 2020 | 120 |
| 2021 | 110 |
| 2022 | 130 |
| 2023 | 140 |

Average = (100 + 120 + 110 + 130 + 140) / 5 = 600 / 5 = 120

### 11.4 Quick Average Estimation

**Method: Assumed Mean**

When numbers are close to a round value:

**Example:** Average of 98, 102, 97, 103, 100

Assume mean = 100
Deviations: -2, +2, -3, +3, 0
Sum of deviations = 0
Average = 100 + 0/5 = 100

**Example:** Average of 47, 52, 48, 53, 45

Assume mean = 50
Deviations: -3, +2, -2, +3, -5
Sum of deviations = -5
Average = 50 + (-5)/5 = 50 - 1 = 49

---

## 12. Approximation Techniques

### 12.1 Why Approximation?

In competitive exams:
1. Time is limited
2. Options are usually well-spaced
3. Exact calculations are often unnecessary

### 12.2 Rounding Rules

**Round to Nearest 10:**
- 47 → 50
- 43 → 40
- 125 → 130

**Round to Nearest 5:**
- 47 → 45
- 43 → 45
- 78 → 80

**Round to Significant Figures:**
- 4873 → 4900 (2 SF) or 4870 (3 SF)

### 12.3 Approximation Strategies

#### Strategy 1: Round All Numbers
*Question: What is 47.8% of 5123?*

Approximate: 48% of 5100 = 0.48 × 5100 = 2448

**Actual:** 47.8% of 5123 = 2448.79

#### Strategy 2: Compensating Errors
When one value is rounded up, round another down

*Question: 52 × 48*

Method: (50 + 2)(50 - 2) = 2500 - 4 = 2496

**Actual:** 52 × 48 = 2496 ✓

#### Strategy 3: Order of Magnitude Check
Ensure answer is in correct range

*Question: 0.23 × 4578*

Rough check: 0.25 × 4600 = 1150
Answer should be close to 1000-1150

**Actual:** 0.23 × 4578 = 1052.94

### 12.4 The "1% Method"

**For any percentage calculation:**

1. Find 1% of the number
2. Scale up or down

*Question: 73% of 4200*

- 1% of 4200 = 42
- 70% = 42 × 70 = 2940
- 3% = 42 × 3 = 126
- 73% = 2940 + 126 = 3066

### 12.5 Division Approximation

#### Using Nearby Nice Numbers

*Question: 4578 ÷ 23*

Approximate: 4600 ÷ 23 ≈ 4600 ÷ 25 = 184

Or: 4600 ÷ 23 = 200 (since 23 × 200 = 4600)

**Actual:** 4578 ÷ 23 = 199.04

#### The "Factor Out" Method

*Question: 7845 ÷ 35*

7845 ÷ 35 = 7845 ÷ 7 ÷ 5 = 1120.7 ÷ 5 ≈ 224

**Actual:** 7845 ÷ 35 = 224.14

---

## 13. Common Traps & Edge Cases

### 13.1 The Percentage vs. Percentage Point Trap

**Trap:** Confusing "percentage" with "percentage points"

**Example:** 
- Year 1: Pass rate = 60%
- Year 2: Pass rate = 72%

*Wrong interpretation:* Pass rate increased by 12%

*Correct interpretation:* 
- Percentage point increase = 12 percentage points
- Percentage increase = (12/60) × 100 = 20%

### 13.2 The Base Change Trap

**Trap:** Using wrong base for percentage calculations

**Example:** A is 25% more than B. What percent is B less than A?

*Wrong:* B is 25% less than A

*Correct:* 
- If B = 100, then A = 125
- B less than A = (25/125) × 100 = 20%

### 13.3 The "Per" vs. "Of" Trap

**"X per Y"** means X divided by Y
**"X of Y"** means X times Y

### 13.4 The Scale Misread Trap

**Trap:** Misreading graph scales

**Example:** Y-axis starts at 100, not 0

```
150 |----*
140 |   /
130 |  /
120 | /
110 |/
100 +--------
```

The line shows 50% increase (100 to 150), NOT 150 units!

### 13.5 The Ratio vs. Absolute Trap

**Trap:** Confusing ratio comparison with absolute comparison

**Example:**
- Company A: Revenue = ₹100 Cr, Profit = ₹10 Cr (10% margin)
- Company B: Revenue = ₹50 Cr, Profit = ₹8 Cr (16% margin)

*Question:* Which company is more profitable?

*Trap Answer:* B (higher margin)

*Correct Analysis:* Depends on what "profitable" means:
- Higher profit margin: B (16% > 10%)
- Higher absolute profit: A (₹10 Cr > ₹8 Cr)

### 13.6 The Cumulative vs. Year-on-Year Trap

**Trap:** Confusing cumulative data with periodic data

**Example:** Sales Growth Chart

| Year | Cumulative Sales | Year-on-Year Sales |
|------|------------------|-------------------|
| 2019 | 100 | 100 |
| 2020 | 230 | 130 |
| 2021 | 380 | 150 |
| 2022 | 500 | 120 |

If asked "In which year was sales highest?" - Answer depends on data type!

### 13.7 GATE/ESE Specific Traps

#### The NAT Precision Trap
- Answer: 3.333...
- If asked for 2 decimal places: 3.33
- If asked for 3 decimal places: 3.333

**Never round intermediate calculations!**

#### The MSQ Partial Credit Trap
- In MSQ, you get partial marks but also partial negative marks
- A wrong selection can reduce your score
- When uncertain, only mark what you're confident about

### 13.8 Banking Exam Specific Traps

#### The Speed Trap
- Questions designed to be solved in 45-60 seconds
- If you're taking more than 90 seconds, move on

#### The "Approximately Equal" Trap
- Options like: 280, 285, 290, 295, 300
- Approximation alone won't work; precise calculation needed

---

## 14. Exam-Specific Strategies

### 14.1 GATE (Graduate Aptitude Test in Engineering)

**DI Characteristics:**
- 1-2 DI sets typically
- 5-10 marks worth
- NAT (Numerical Answer Type) common
- Higher complexity, lower speed pressure

**Strategy:**

1. **Time Allocation:** 8-10 minutes per DI set
2. **Accuracy Focus:** NAT questions require exact answers
3. **Unit Awareness:** Watch for unit conversions
4. **Virtual Calculator:** Use the on-screen calculator wisely
5. **Question Selection:** Do easier questions first in each set

**Recommended Approach:**
```
Step 1: Read all questions in the set (1 min)
Step 2: Identify easy vs. hard questions
Step 3: Solve easy questions first
Step 4: Attempt hard questions with remaining time
Step 5: Double-check NAT answers before moving on
```

### 14.2 ESE (Engineering Services Examination)

**DI Characteristics:**
- Part of Paper 1 (General Studies)
- 15-20 marks worth
- MCQ format
- Moderate complexity

**Strategy:**

1. **Time Allocation:** 1.5-2 minutes per question
2. **Option Elimination:** Use options to guide calculations
3. **Approximation Friendly:** Options usually well-spaced
4. **Smart Marking:** Mark uncertain answers for review

### 14.3 PSU (Public Sector Undertaking) Exams

**DI Characteristics:**
- Varies by PSU (BARC, ISRO, SAIL, etc.)
- Usually 15-25 marks
- MCQ format
- Moderate to high complexity

**Strategy:**

1. **Pattern Recognition:** Each PSU has favored question types
2. **Previous Papers:** Very repetitive patterns
3. **Speed + Accuracy:** Balance required
4. **Sectional Time Management:** Don't overspend on DI

### 14.4 Banking Exams

#### Prelims Strategy

**Characteristics:**
- 15-20 questions
- 20-25 marks
- Extreme time pressure (20 min for section)
- Easy to moderate difficulty

**Strategy:**
1. **Speed is King:** 45 seconds per question max
2. **Attempt All:** No negative marking in some exams
3. **Smart Skipping:** Skip time-consuming questions
4. **Approximation Heavy:** Options are well-spaced

#### Mains Strategy

**Characteristics:**
- 30-40 questions in DI/Analysis section
- 35-50 marks
- High complexity
- Mixed DI common

**Strategy:**
1. **Set Selection:** Choose easier DI sets first
2. **Time per Set:** 8-10 minutes for 5 questions
3. **Leave Difficult Sets:** Don't waste time
4. **Cross-Reference:** Use data from one question to verify another

### 14.5 Time Management Matrix

| Exam | Total DI Questions | Time Available | Time per Question |
|------|-------------------|----------------|-------------------|
| GATE | 5-10 | 20-25 min | 2-3 min |
| ESE | 10-15 | 20-25 min | 1.5-2 min |
| PSU | 10-20 | 15-25 min | 1-1.5 min |
| Bank Prelim | 15-20 | 15-20 min | 45-60 sec |
| Bank Mains | 30-40 | 35-45 min | 50-70 sec |

---

## 15. Practice Problems with Solutions

### Problem Set 1: Tables

**Data: Company Employee Distribution**

| Department | 2020 | 2021 | 2022 | 2023 |
|------------|------|------|------|------|
| Engineering | 150 | 180 | 200 | 220 |
| Marketing | 80 | 85 | 90 | 100 |
| Finance | 40 | 45 | 50 | 55 |
| HR | 30 | 35 | 40 | 45 |
| **Total** | **300** | **345** | **380** | **420** |

**Q1.** What is the percentage increase in total employees from 2020 to 2023?

**Solution:**
- Increase = 420 - 300 = 120
- Percentage increase = (120/300) × 100 = 40%

**Answer: 40%**

**Q2.** In which year did the Engineering department have the highest proportion of total employees?

**Solution:**
- 2020: 150/300 = 50%
- 2021: 180/345 = 52.17%
- 2022: 200/380 = 52.63%
- 2023: 220/420 = 52.38%

**Answer: 2022 (52.63%)**

**Q3.** What is the ratio of Marketing employees to HR employees in 2023?

**Solution:**
- Marketing: 100
- HR: 45
- Ratio = 100:45 = 20:9

**Answer: 20:9**

**Q4.** By what percent did Finance department employees increase from 2020 to 2023?

**Solution:**
- Increase = 55 - 40 = 15
- Percentage = (15/40) × 100 = 37.5%

**Answer: 37.5%**

**Q5.** What is the average annual increase in total employees?

**Solution:**
- Total increase = 420 - 300 = 120
- Number of years = 3 (2020 to 2023)
- Average annual increase = 120/3 = 40

**Answer: 40 employees per year**

---

### Problem Set 2: Bar Charts

**Data: Monthly Sales (in ₹ Lakhs)**

```
Product A:  Jan: 40, Feb: 45, Mar: 50, Apr: 55, May: 60, Jun: 65
Product B:  Jan: 30, Feb: 35, Mar: 40, Apr: 45, May: 50, Jun: 55
```

**Q1.** What is the total sales of Product A in the first quarter (Jan-Mar)?

**Solution:**
Total = 40 + 45 + 50 = 135 lakhs

**Answer: ₹135 Lakhs**

**Q2.** In which month was the difference between Product A and Product B sales maximum?

**Solution:**
Differences:
- Jan: 40 - 30 = 10
- Feb: 45 - 35 = 10
- Mar: 50 - 40 = 10
- Apr: 55 - 45 = 10
- May: 60 - 50 = 10
- Jun: 65 - 55 = 10

**Answer: All months have equal difference of ₹10 Lakhs**

**Q3.** What is the percentage increase in Product B sales from January to June?

**Solution:**
- Increase = 55 - 30 = 25
- Percentage = (25/30) × 100 = 83.33%

**Answer: 83.33%**

**Q4.** What is the ratio of total Product A sales to total Product B sales for the six months?

**Solution:**
- Product A total = 40 + 45 + 50 + 55 + 60 + 65 = 315
- Product B total = 30 + 35 + 40 + 45 + 50 + 55 = 255
- Ratio = 315:255 = 21:17

**Answer: 21:17**

---

### Problem Set 3: Pie Charts

**Data: Budget Allocation of a Company (Total: ₹50 Crores)**

| Category | Percentage |
|----------|------------|
| Salaries | 35% |
| Raw Materials | 25% |
| Marketing | 15% |
| R&D | 10% |
| Operations | 10% |
| Miscellaneous | 5% |

**Q1.** What is the budget allocated for Salaries?

**Solution:**
Salaries = 35% of 50 Cr = 0.35 × 50 = 17.5 Cr

**Answer: ₹17.5 Crores**

**Q2.** What is the central angle for R&D in the pie chart?

**Solution:**
Angle = 10% of 360° = 36°

**Answer: 36°**

**Q3.** How much more is spent on Salaries than on Marketing?

**Solution:**
Difference = 35% - 15% = 20% of 50 Cr = 10 Cr

**Answer: ₹10 Crores**

**Q4.** What is the ratio of Raw Materials budget to Miscellaneous budget?

**Solution:**
Ratio = 25% : 5% = 5:1

**Answer: 5:1**

**Q5.** If next year, Marketing budget increases by 20% and total budget remains same, what will be the new Marketing allocation?

**Solution:**
- Current Marketing = 15% of 50 = 7.5 Cr
- Increase = 20% of 7.5 = 1.5 Cr
- New Marketing = 7.5 + 1.5 = 9 Cr
- New percentage = (9/50) × 100 = 18%

**Answer: 18% or ₹9 Crores**

---

### Problem Set 4: Line Graphs

**Data: Temperature Variation (°C)**

| Time | Day 1 | Day 2 |
|------|-------|-------|
| 6 AM | 18 | 20 |
| 9 AM | 24 | 25 |
| 12 PM | 32 | 35 |
| 3 PM | 36 | 38 |
| 6 PM | 30 | 32 |
| 9 PM | 24 | 26 |

**Q1.** What is the average temperature on Day 1?

**Solution:**
Average = (18 + 24 + 32 + 36 + 30 + 24) / 6 = 164/6 = 27.33°C

**Answer: 27.33°C**

**Q2.** At what time was the temperature difference between Day 1 and Day 2 maximum?

**Solution:**
Differences:
- 6 AM: 20 - 18 = 2
- 9 AM: 25 - 24 = 1
- 12 PM: 35 - 32 = 3
- 3 PM: 38 - 36 = 2
- 6 PM: 32 - 30 = 2
- 9 PM: 26 - 24 = 2

**Answer: 12 PM (difference of 3°C)**

**Q3.** By what percentage did Day 2 temperature increase from 6 AM to 3 PM?

**Solution:**
- Increase = 38 - 20 = 18
- Percentage = (18/20) × 100 = 90%

**Answer: 90%**

**Q4.** What is the ratio of temperature at 9 AM to temperature at 9 PM on Day 1?

**Solution:**
Ratio = 24:24 = 1:1

**Answer: 1:1**

---

### Problem Set 5: Mixed DI / Caselet

**Caselet:**
*A company has 500 employees distributed across three offices: Delhi, Mumbai, and Chennai. The Delhi office has 40% of the employees. The Mumbai office has 50 fewer employees than Delhi. The remaining employees work in Chennai. Male employees in Delhi, Mumbai, and Chennai are 60%, 50%, and 45% respectively.*

**Q1.** How many employees work in the Chennai office?

**Solution:**
- Delhi = 40% of 500 = 200
- Mumbai = 200 - 50 = 150
- Chennai = 500 - 200 - 150 = 150

**Answer: 150 employees**

**Q2.** What is the total number of male employees in the company?

**Solution:**
- Delhi males = 60% of 200 = 120
- Mumbai males = 50% of 150 = 75
- Chennai males = 45% of 150 = 67.5 ≈ 68

**Answer: 263 (or 262.5) male employees**

**Q3.** What is the ratio of female employees in Mumbai to female employees in Chennai?

**Solution:**
- Mumbai females = 150 - 75 = 75
- Chennai females = 150 - 67.5 = 82.5

Ratio = 75 : 82.5 = 750 : 825 = 10:11

**Answer: 10:11**

**Q4.** If Delhi office adds 25 new employees (all female), what will be the new percentage of male employees in Delhi?

**Solution:**
- New Delhi total = 200 + 25 = 225
- Delhi males remain = 120
- New male % = (120/225) × 100 = 53.33%

**Answer: 53.33%**

---

## 16. Quick Reference Formulas

### Percentage Formulas

| Operation | Formula |
|-----------|---------|
| Percentage of a number | (P/100) × N |
| What % is X of Y | (X/Y) × 100 |
| % Increase | ((New - Old)/Old) × 100 |
| % Decrease | ((Old - New)/Old) × 100 |
| Successive % change | a + b + (ab/100) |
| Reverse % (after increase) | (x/(100+x)) × 100 |
| Reverse % (after decrease) | (x/(100-x)) × 100 |

### Ratio & Proportion Formulas

| Operation | Formula |
|-----------|---------|
| Dividing in ratio a:b | First part = (a/(a+b)) × Total |
| Combining ratios | Make common element equal |
| Alligation | (d-m):(m-c) for cheaper:dearer |
| Partnership | Profit ratio = Capital × Time |

### Average Formulas

| Operation | Formula |
|-----------|---------|
| Simple Average | Sum/Count |
| Weighted Average | Σ(Value × Weight)/Σ(Weight) |
| Combined Average | (n₁A₁ + n₂A₂)/(n₁ + n₂) |

### Pie Chart Formulas

| Operation | Formula |
|-----------|---------|
| Degree to % | (Degree/360) × 100 |
| % to Degree | (Percentage/100) × 360 |
| % to Value | (Percentage/100) × Total |

### Growth Rate Formulas

| Operation | Formula |
|-----------|---------|
| CAGR | ((Final/Initial)^(1/n) - 1) × 100 |
| Simple Growth Rate | ((Final - Initial)/Initial) × 100 |
| Average Growth Rate | Total Growth / Number of Periods |

---

## Key Takeaways

### The 5-Second Checklist Before Solving

1. ✓ Read the question carefully - what exactly is asked?
2. ✓ Check units - are they consistent?
3. ✓ Identify the relevant data - ignore the rest
4. ✓ Choose the right method - direct reading vs. calculation
5. ✓ Verify the magnitude - is the answer reasonable?

### The 10 Commandments of DI

1. **Read all questions before starting** - plan your approach
2. **Easy questions first** - build confidence and secure marks
3. **Never spend more than 2 minutes** on any single question
4. **Use approximation wisely** - check if options allow it
5. **Watch for units** - lakhs vs. crores, % vs. percentage points
6. **Mark uncertain answers for review** - if time permits
7. **Don't carry mistakes forward** - verify early calculations
8. **Use options strategically** - elimination and back-calculation
9. **Practice daily** - DI is a skill, not just knowledge
10. **Stay calm** - panic is your biggest enemy

### Recommended Practice Schedule

| Week | Focus Area | Daily Practice |
|------|------------|----------------|
| 1-2 | Tables & Bar Charts | 3 DI sets |
| 3-4 | Pie Charts & Line Graphs | 3 DI sets |
| 5-6 | Mixed DI & Caselets | 3 DI sets |
| 7-8 | Full-length Tests | 1 complete test |
| 9+ | Previous Year Papers | 2 papers/week |

---

## Final Words

Data Interpretation is not about complex calculations—it's about **efficient data processing**. The difference between a top ranker and an average student is not mathematical ability, but the ability to:

1. **Extract** the right information quickly
2. **Ignore** irrelevant data
3. **Calculate** smartly (not necessarily precisely)
4. **Manage** time effectively

**Remember:** Every minute saved in DI is a minute earned for complex topics.

---

**Good luck with your preparation!**

---

**Version:** 1.0  
**Last Updated:** January 2026  
**Target Exams:** GATE | ESE | PSU | BANK (Prelims & Mains)
