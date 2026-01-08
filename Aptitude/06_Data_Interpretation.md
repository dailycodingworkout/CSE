# Data Interpretation | Complete Mastery Guide
## For GATE, ESE, PSU & Bank Examinations

---

## The Atomic Truth
> **"Extract insights from organized visual data formats."**

---

## 1. Foundation: What is Data Interpretation?

### Definition
Data Interpretation (DI) tests your ability to:
- **Read and understand** data presented in various formats
- **Analyze** trends, patterns, and relationships
- **Calculate** specific values from given data
- **Draw conclusions** and make comparisons

### Why It Matters
- High weightage in all competitive exams
- Tests **mathematical accuracy + speed**
- Bank PO/Clerk: 15-20 questions (major section)
- GATE: 5-10 questions
- SSC: 10-15 questions

---

## 2. Types of Data Representations

### Type 1: Tables
```
┌─────────┬────────┬────────┬────────┬────────┐
│  Year   │ Sales  │ Profit │ Expense│ Growth │
├─────────┼────────┼────────┼────────┼────────┤
│  2020   │  1000  │  200   │  800   │   5%   │
│  2021   │  1200  │  240   │  960   │  20%   │
│  2022   │  1500  │  300   │  1200  │  25%   │
│  2023   │  1800  │  360   │  1440  │  20%   │
└─────────┴────────┴────────┴────────┴────────┘
```

### Type 2: Bar Graphs
```
                2023 ████████████████████ 180
                2022 ███████████████ 150
                2021 ████████████ 120
                2020 ██████████ 100
                     0   50  100  150  200
```

### Type 3: Line Graphs
```
    200 ┤                          ╭─●
        │                     ╭───╯
    150 ┤               ╭────╯
        │          ╭───╯
    100 ┤     ●───╯
        │
     50 ┤
        └────┬────┬────┬────┬────┬────
            2019 2020 2021 2022 2023
```

### Type 4: Pie Charts
```
         ╭─────────────╮
        ╱   Sales 40%   ╲
       ╱      ╱╲        ╲
      │   ╱      ╲  20%  │
      │ 15%       ╲Profit│
       ╲  Rent    ╱      ╱
        ╲  25%  ╱       ╱
         ╰────Expenses─╯
```

### Type 5: Combination/Mixed Charts
Bar + Line, Multiple pie charts, Stacked bars, etc.

### Type 6: Radar/Spider Charts
```
              Speed
                │
         ╱─────●─────╲
        ╱      │      ╲
    Cost●──────┼──────●Quality
        ╲      │      ╱
         ╲─────●─────╱
                │
             Durability
```

### Type 7: Caselet (Text-Based)
Data given in paragraph form, requiring extraction before calculation.

---

## 3. Essential Formulas

### Percentage Calculations (Multiplier Method)

> ⚡ **The Multiplier Approach:** Convert percentages to multipliers for faster calculations!

**Core Principle:**
```
x% increase → Multiply by (1 + x/100)
x% decrease → Multiply by (1 - x/100)

Examples:
20% profit  → × 1.20
20% loss    → × 0.80
15% increase → × 1.15
25% decrease → × 0.75
10% profit  → × 1.10
10% loss    → × 0.90
```

**Quick Multiplier Reference Table:**
| % Change | Profit/Increase | Loss/Decrease |
|----------|-----------------|---------------|
| 5% | × 1.05 | × 0.95 |
| 10% | × 1.10 | × 0.90 |
| 12.5% | × 1.125 | × 0.875 |
| 15% | × 1.15 | × 0.85 |
| 20% | × 1.20 | × 0.80 |
| 25% | × 1.25 | × 0.75 |
| 30% | × 1.30 | × 0.70 |
| 33.33% | × 1.333 | × 0.667 |
| 40% | × 1.40 | × 0.60 |
| 50% | × 1.50 | × 0.50 |

**Basic Percentage (Traditional):**
$$\text{Percentage} = \frac{\text{Part}}{\text{Whole}} \times 100$$

**Percentage Change (Traditional):**
$$\text{\% Change} = \frac{\text{New} - \text{Old}}{\text{Old}} \times 100$$

**Percentage Point Difference:**
$$\text{PP Diff} = \text{New \%} - \text{Old \%}$$

---

### Profit & Loss (Multiplier Method)

> 🎯 **Key Insight:** Always think in multipliers, not percentages!

**Basic Formulas:**
```
Selling Price (SP) = Cost Price (CP) × Multiplier

For Profit:  SP = CP × (1 + Profit%/100)
For Loss:    SP = CP × (1 - Loss%/100)

Examples:
20% Profit: SP = CP × 1.20
20% Loss:   SP = CP × 0.80
```

**Reverse Calculation:**
```
CP = SP / Multiplier

If SP = 1200 and Profit = 20%:
CP = 1200 / 1.20 = 1000
```

**Successive Profit/Loss (Chain Multiplication):**
```
Multiple transactions? Just multiply all multipliers!

Example: 20% profit followed by 10% loss
Final Multiplier = 1.20 × 0.90 = 1.08
Net Result = 8% Profit

Example: 20% profit followed by 20% loss
Final Multiplier = 1.20 × 0.80 = 0.96
Net Result = 4% Loss (NOT 0%!)
```

**Combined/Average Profit-Loss Problems:**

For finding average or effective rate when buying at different prices:

```
If buying at x% profit (multiplier a) and y% loss (multiplier b):
Combined Multiplier for equal quantities = (a + b) / 2

Example: Buy half at 20% profit, half at 20% loss
Multipliers: 1.20 and 0.80
Average = (1.20 + 0.80) / 2 = 1.00 (Break-even)
```

**Harmonic Mean for Equal Investment:**
```
When SAME AMOUNT is invested at different rates:
Effective Multiplier = 2 / (1/a + 1/b)

Example: Invest ₹1000 each at 20% profit and 20% loss rates
Multipliers: 1.20 and 0.80
Effective = 2 / (1/1.20 + 1/0.80)
          = 2 / (0.833 + 1.25)
          = 2 / 2.083
          = 0.96 (4% Loss overall)
```

**Markup and Discount (Multiplier Chain):**
```
Marked Price = CP × Markup Multiplier
Selling Price = MP × Discount Multiplier
Final SP = CP × Markup Multiplier × Discount Multiplier

Example: 25% markup, then 20% discount
Markup: × 1.25
Discount: × 0.80
Net: 1.25 × 0.80 = 1.00 (Break-even, no profit/loss)
```

**False Weight/Quantity Problems:**
```
Profit% = (Actual - Claimed) / Claimed × 100

Using Multiplier:
If selling 800g as 1000g:
Multiplier = 1000/800 = 1.25 → 25% Profit
```

---

### Ratio Calculations

**Basic Ratio:**
$$\text{Ratio } A:B = \frac{A}{B}$$

**Parts from Ratio:**
If A:B = 3:5 and total = 800
$$A = \frac{3}{3+5} \times 800 = 300$$

### Average Calculations

**Simple Average:**
$$\text{Average} = \frac{\text{Sum of values}}{\text{Number of values}}$$

**Weighted Average:**
$$\text{Weighted Avg} = \frac{\sum (w_i \times x_i)}{\sum w_i}$$

### Growth Rate Calculations

**Simple Growth Rate:**
$$\text{Growth} = \frac{\text{Final} - \text{Initial}}{\text{Initial}} \times 100$$

**CAGR (Compound Annual Growth Rate):**
$$\text{CAGR} = \left(\frac{\text{Final}}{\text{Initial}}\right)^{\frac{1}{n}} - 1$$

---

## 4. Table-Based Problems

### Reading Strategy
1. **Scan headers** - understand what each row/column represents
2. **Note units** - thousand, million, percentage, etc.
3. **Identify relationships** - which values derive from others
4. **Mark key data** - values you'll need for calculations

### Common Question Types

**Type 1: Direct Reading**
"What was the sales in 2021?"
→ Read directly from table

**Type 2: Calculation**
"What was the profit percentage in 2022?"
→ Profit/Sales × 100

**Type 3: Comparison**
"Which year had the highest growth?"
→ Calculate growth for each year, compare

**Type 4: Aggregate**
"What was the total profit from 2020-2023?"
→ Sum of profit values

### Example Problem

**Table:**
| Year | Revenue | Expense | Tax |
|------|---------|---------|-----|
| 2020 | 500 | 400 | 20 |
| 2021 | 600 | 450 | 30 |
| 2022 | 750 | 560 | 38 |
| 2023 | 900 | 680 | 44 |

**Question:** What was the profit (Revenue - Expense - Tax) in 2022?

**Solution:**
Profit = 750 - 560 - 38 = 152

---

## 5. Bar Graph Analysis

### Reading Techniques

**Single Bar Graph:**
- Each bar represents one category/time period
- Height/length = value
- Compare bars visually for trends

**Grouped Bar Graph:**
- Multiple bars per category
- Compare within groups and across groups

**Stacked Bar Graph:**
- Total = full bar height
- Segments = components
- Read segment sizes carefully

### Common Calculations

**From Single Bar:**
```
Value of bar = Read from scale
Difference = Bar₁ height - Bar₂ height
Percentage = (Bar₁/Bar₂) × 100
```

**From Stacked Bar:**
```
Total = Full bar height
Component = Segment height
Component % = (Segment/Total) × 100
```

### Example
```
         2023 ████████ 80
Component A  ████ 40
Component B  ████ 40

What % of 2023 total is Component A?
= (40/80) × 100 = 50%
```

---

## 6. Line Graph Analysis

### Reading Techniques

**Single Line:**
- X-axis typically time/categories
- Y-axis is the measured value
- Slope indicates rate of change

**Multiple Lines:**
- Compare trends between different series
- Note crossover points (where lines intersect)

### Key Observations

**Slope Analysis:**
```
Steep upward slope = Rapid growth
Steep downward slope = Rapid decline
Flat line = No change
Fluctuating = Variable/unstable
```

**Trend Analysis:**
```
Consistent increase = Positive trend
Consistent decrease = Negative trend
Peak and trough = Cyclical pattern
```

### Calculating from Line Graph

**Growth Rate:**
$$\text{Growth} = \frac{Y_2 - Y_1}{Y_1} \times 100$$

**Average Rate of Change:**
$$\text{Avg Rate} = \frac{\text{Final Value} - \text{Initial Value}}{\text{Number of Periods}}$$

---

## 7. Pie Chart Analysis

### Fundamental Concepts

**Degree-Percentage Relationship:**
$$\text{Degrees} = \frac{\text{Percentage}}{100} \times 360°$$
$$\text{Percentage} = \frac{\text{Degrees}}{360°} \times 100$$

### Key Formulas

**Value from Percentage:**
$$\text{Value} = \frac{\text{Percentage}}{100} \times \text{Total}$$

**Percentage from Value:**
$$\text{Percentage} = \frac{\text{Value}}{\text{Total}} \times 100$$

**Ratio of Two Sectors:**
$$\text{Ratio} = \frac{\text{Sector 1 \%}}{\text{Sector 2 \%}} = \frac{\text{Sector 1 Degrees}}{\text{Sector 2 Degrees}}$$

### Common Question Types

**Type 1: Find value from percentage**
"If total revenue is 1000 and Sales is 40%, find Sales value."
Sales = 40% × 1000 = 400

**Type 2: Find percentage from degrees**
"If a sector has 72°, what percentage does it represent?"
Percentage = (72/360) × 100 = 20%

**Type 3: Compare sectors**
"Sector A is 30%, Sector B is 20%. What is the ratio?"
Ratio = 30:20 = 3:2

### Example Problem

**Pie Chart Data:** Total = 5000
- A: 20%
- B: 25%
- C: 30%
- D: 15%
- E: 10%

**Question:** What is the difference between B and E?

**Solution:**
B = 25% × 5000 = 1250
E = 10% × 5000 = 500
Difference = 1250 - 500 = 750

---

## 8. Combination Charts

### Bar + Line Combination

**Reading Strategy:**
- Bar typically shows absolute values (left Y-axis)
- Line typically shows trend/percentage (right Y-axis)
- Read each from appropriate scale

### Multiple Pie Charts

**Comparison Strategy:**
- Note if totals are same or different
- Convert to actual values for accurate comparison
- Percentage comparison only works if totals are equal

### Stacked Area Charts

**Reading:**
- Like stacked bar but continuous
- Each band represents a component
- Total = top edge of topmost band

---

## 9. Caselet (Text-Based) Problems

### What is Caselet?
Data given in paragraph form instead of tables/charts.

### Strategy

**Step 1: Extract Data**
Read paragraph and create your own table/structure

**Step 2: Identify Relationships**
Note formulas/connections between variables

**Step 3: Organize**
Create a clean table before solving

### Example Caselet

**Paragraph:**
"A company had 500 employees in 2020. The number increased by 20% in 2021. In 2022, 50 employees left and 80 new employees joined. The company's revenue was ₹10 million per 100 employees in 2022."

**Extract:**
| Year | Employees |
|------|-----------|
| 2020 | 500 |
| 2021 | 500 × 1.2 = 600 |
| 2022 | 600 - 50 + 80 = 630 |

Revenue in 2022 = (630/100) × 10 = ₹63 million

---

## 10. Quick Calculation Techniques

### Technique 1: Percentage Approximation

**Key Percentages to Memorize:**
```
1% = 0.01
5% = 0.05
10% = 0.1
12.5% = 1/8
20% = 1/5
25% = 1/4
33.33% = 1/3
50% = 1/2
66.67% = 2/3
75% = 3/4
```

**Quick Calculation:**
```
17% of 500:
= 10% + 5% + 2%
= 50 + 25 + 10
= 85
```

### Technique 2: Fraction Shortcuts

```
Multiply by 0.5 = Divide by 2
Multiply by 0.25 = Divide by 4
Multiply by 0.125 = Divide by 8
Multiply by 0.2 = Divide by 5
Multiply by 1.5 = Add half
Multiply by 1.25 = Add quarter
```

### Technique 3: Percentage Change Shortcuts (Multiplier Method)

**Successive Percentage Change - The Easy Way:**
```
Just multiply the multipliers!

20% increase then 10% increase:
= 1.20 × 1.10 = 1.32 → 32% increase ✓

Traditional Formula (for reference):
Net Change = x + y + xy/100
= 20 + 10 + (20×10)/100 = 32%
```

**Successive Profit/Loss Examples:**
```
20% profit then 20% loss:
= 1.20 × 0.80 = 0.96 → 4% loss

30% profit then 10% profit:
= 1.30 × 1.10 = 1.43 → 43% profit

25% loss then 25% loss:
= 0.75 × 0.75 = 0.5625 → 43.75% loss
```

**Finding Unknown Percentage:**
```
If net result is 8% profit after 20% profit and x% loss:
1.20 × (1 - x/100) = 1.08
(1 - x/100) = 1.08/1.20 = 0.90
x = 10% loss
```

### Technique 4: Ratio Simplification

When comparing two ratios:
```
A:B = 3:4
C:D = 5:6

To compare A/B with C/D:
Cross multiply: 3×6 = 18, 4×5 = 20
Since 18 < 20, A/B < C/D
```

---

## 11. Common DI Question Patterns

### Pattern 1: Find the Maximum/Minimum
"Which year had the highest profit margin?"
→ Calculate for all years, compare

### Pattern 2: Average Over Period
"What was the average sales from 2019-2023?"
→ Sum all values, divide by number of years

### Pattern 3: Percentage Contribution
"What percentage of total exports was from India?"
→ (India's value / Total) × 100

### Pattern 4: Year-over-Year Change
"What was the growth rate from 2021 to 2022?"
→ ((2022 - 2021) / 2021) × 100

### Pattern 5: Ratio Questions
"What is the ratio of Sales to Expenses in 2023?"
→ Sales : Expenses = Value₁ : Value₂

### Pattern 6: Combined/Aggregate
"What was the total revenue across all regions?"
→ Sum of all regional revenues

### Pattern 7: Difference Questions
"By how much did profits exceed expenses in 2022?"
→ Profit - Expenses

### Pattern 8: Missing Data
"If total is 500 and three categories are 100, 150, 120, find fourth."
→ Fourth = 500 - 100 - 150 - 120 = 130

---

## 12. Speed-Building Strategies

### Strategy 1: Pre-Calculate Common Values
Before answering questions, note:
- Row/column totals
- Obvious patterns
- Key ratios

### Strategy 2: Approximate First
For complex calculations:
1. Round numbers
2. Get approximate answer
3. Eliminate wrong options
4. Calculate precisely only if needed

### Strategy 3: Use Options
In MCQs:
- Options are clues
- If options are spread apart, approximation works
- If options are close, calculate carefully

### Strategy 4: Visual Estimation (for graphs)
- For bar graphs: estimate bar heights
- For pie charts: estimate sector sizes
- For line graphs: note relative positions

---

## 13. Error Avoidance

### Error 1: Unit Confusion
```
Data in thousands, answer in actual
1500 (in thousands) = 1,500,000 actual
Always note: "All values in lakhs/crores/thousands"
```

### Error 2: Misreading Scale
```
For graphs: check axis intervals
If axis shows: 0, 50, 100, 150...
Then each unit = 50, not 10
```

### Error 3: Wrong Base for Percentage
```
Percentage increase OF what?
"% increase in sales" uses OLD sales as base
"Sales as % of revenue" uses REVENUE as base
```

### Error 4: Missing Data Points
```
In line graphs, note all points
Don't interpolate between points for exact questions
```

### Error 5: Assuming Linear Distribution
```
In pie charts, values are proportional to percentages
Don't assume equal segments
```

---

## 14. Practice Problems

### Problem Set: Profit & Loss (Multiplier Method)

**Q1:** A shopkeeper marks up goods by 25% and then offers a 20% discount. What is the profit or loss percentage?

**Solution (Multiplier Method):**
```
Markup: × 1.25
Discount: × 0.80
Net = 1.25 × 0.80 = 1.00 → No profit, No loss (Break-even)
```

**Q2:** A trader makes 20% profit on first item and 20% loss on second item. If both items have the same cost price, find net result.

**Solution:**
```
For equal CP with equal quantity:
First item: × 1.20
Second item: × 0.80
Average multiplier = (1.20 + 0.80) / 2 = 1.00 → Break-even
```

**Q3:** A merchant invests equal amounts in two items. One gives 20% profit, other gives 20% loss. Find net result.

**Solution (Harmonic Mean for Equal Investment):**
```
Multipliers: 1.20 and 0.80
Effective = 2 / (1/1.20 + 1/0.80)
          = 2 / (0.833 + 1.25)
          = 2 / 2.083
          = 0.96 → 4% Loss
```

**Q4:** An article is sold at 20% profit. If cost price is ₹1000, find selling price.

**Solution:**
```
SP = CP × Multiplier
SP = 1000 × 1.20 = ₹1200
```

**Q5:** After successive discounts of 20% and 10%, the selling price is ₹720. Find the marked price.

**Solution:**
```
Discount chain: × 0.80 × 0.90 = × 0.72
MP × 0.72 = 720
MP = 720 / 0.72 = ₹1000
```

**Q6:** A dealer offers 10% discount and still makes 20% profit. Find the markup percentage if CP is ₹1000.

**Solution:**
```
SP = CP × Profit Multiplier = 1000 × 1.20 = ₹1200
SP = MP × Discount Multiplier
1200 = MP × 0.90
MP = 1200 / 0.90 = ₹1333.33
Markup = (1333.33 - 1000) / 1000 × 100 = 33.33%
Or: Markup Multiplier = 1333.33/1000 = 1.333 → 33.33%
```

**Q7:** Successive profits of 10%, 20%, and 25% on an item. Find overall profit%.

**Solution:**
```
Net Multiplier = 1.10 × 1.20 × 1.25 = 1.65 → 65% Profit
```

---

### Problem Set: Table

**Data:**
| Company | 2020 | 2021 | 2022 | 2023 |
|---------|------|------|------|------|
| A | 120 | 150 | 180 | 200 |
| B | 100 | 110 | 130 | 170 |
| C | 80 | 100 | 120 | 140 |
| D | 150 | 160 | 175 | 190 |
(Values in crores)

**Q1:** What was the total sales of all companies in 2022?
**Solution:** 180 + 130 + 120 + 175 = 605 crores

**Q2:** Which company showed the highest percentage growth from 2020 to 2023?
**Solution:**
- A: (200-120)/120 × 100 = 66.67%
- B: (170-100)/100 × 100 = 70%
- C: (140-80)/80 × 100 = 75%
- D: (190-150)/150 × 100 = 26.67%

**Answer:** Company C with 75%

**Q3:** What is the ratio of Company A's sales to Company D's sales in 2021?
**Solution:** A:D = 150:160 = 15:16

---

### Problem Set: Pie Chart

**Data:** Total Budget = ₹500 crores
- Education: 25%
- Healthcare: 20%
- Defense: 30%
- Infrastructure: 15%
- Others: 10%

**Q1:** What is the budget allocation for Defense?
**Solution:** 30% × 500 = ₹150 crores

**Q2:** What is the difference between Education and Others?
**Solution:** 
Education = 25% × 500 = 125
Others = 10% × 500 = 50
Difference = 125 - 50 = ₹75 crores

**Q3:** If Defense budget increases by 20% and total budget remains same, what would be new Defense allocation as percentage?
**Solution:**
New Defense = 150 × 1.2 = 180
New % = 180/500 × 100 = 36%

---

### Problem Set: Line Graph

**Data:** Company profit (in lakhs) over years
```
Year:   2019  2020  2021  2022  2023
Profit:  100   80   120   150   180
```

**Q1:** In which year was the profit growth rate highest?
**Solution:**
- 2020: (80-100)/100 = -20% (decline)
- 2021: (120-80)/80 = 50%
- 2022: (150-120)/120 = 25%
- 2023: (180-150)/150 = 20%

**Answer:** 2021 with 50%

**Q2:** What was the CAGR from 2019 to 2023?
**Solution:**
CAGR = (180/100)^(1/4) - 1 = (1.8)^0.25 - 1 ≈ 0.158 = 15.8%

---

## 15. Exam-Specific Strategies

### For Bank PO/Clerk
- 15-20 questions from 3-4 sets
- Time: 20-25 minutes total
- Focus on speed with accuracy
- Practice elimination using approximation

### For GATE/ESE
- 5-10 questions
- More analytical, less calculation
- Focus on understanding data relationships
- Time: 2-3 minutes per question

### For SSC
- 10-15 questions
- Mixed difficulty
- Practice quick mental math
- Time: 1.5 minutes per question

---

## 16. Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│           DATA INTERPRETATION QUICK REF             │
├─────────────────────────────────────────────────────┤
│ MULTIPLIER METHOD (KEY!):                           │
│ x% profit → × (1 + x/100)  e.g. 20% → × 1.20       │
│ x% loss   → × (1 - x/100)  e.g. 20% → × 0.80       │
│ Successive: Multiply all multipliers               │
│ e.g. 20% profit + 20% loss = 1.20 × 0.80 = 0.96   │
├─────────────────────────────────────────────────────┤
│ PROFIT & LOSS:                                      │
│ SP = CP × Multiplier                               │
│ CP = SP / Multiplier                               │
│ Equal quantity: (a + b) / 2                        │
│ Equal investment: 2 / (1/a + 1/b)                  │
├─────────────────────────────────────────────────────┤
│ QUICK MULTIPLIERS:                                  │
│ 10%: 1.10/0.90   20%: 1.20/0.80   25%: 1.25/0.75  │
│ 15%: 1.15/0.85   30%: 1.30/0.70   50%: 1.50/0.50  │
├─────────────────────────────────────────────────────┤
│ PIE CHART:                                          │
│ Degrees = (%) × 3.6                                │
│ Value = (%) × Total / 100                          │
│ 360° = 100%                                        │
├─────────────────────────────────────────────────────┤
│ GROWTH RATE:                                        │
│ Simple: (Final-Initial)/Initial × 100              │
│ CAGR: (Final/Initial)^(1/n) - 1                    │
├─────────────────────────────────────────────────────┤
│ STRATEGY:                                           │
│ 1. Read all data first                             │
│ 2. Note units and scale                            │
│ 3. Pre-calculate totals                            │
│ 4. Approximate, then verify                        │
└─────────────────────────────────────────────────────┘
```

---

## 17. The 5-Second Sanity Check

Before marking answer:
1. **Unit check** - Is answer in right units?
2. **Magnitude check** - Does answer make sense given data?
3. **Option elimination** - Did you use approximation wisely?
4. **Base check** - Did you use correct base for percentage?
5. **Sign check** - Growth/decline direction correct?

---

## 18. Mastery Checklist

- [ ] Read all data representation types fluently
- [ ] Calculate percentages mentally (common fractions)
- [ ] Know all basic DI formulas
- [ ] Can approximate quickly
- [ ] Handle combination charts
- [ ] Solve caselet problems systematically
- [ ] Complete 5-question set in <8 minutes
- [ ] Accuracy >90% in practice

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**

---

*Next: Data Sufficiency | The Minimalist Solver*
