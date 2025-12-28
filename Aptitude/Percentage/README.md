# 📊 Percentage - Complete Mastery Guide for GATE & ESE

> **One-liner**: Percentage = "Per Hundred" = A way to express a number as a fraction of 100.

---

## 🧠 Core Intuition

### What is Percentage?
**Percentage is just a ratio with denominator 100.**

```
x% = x/100 = x per 100
```

**Why 100?** Humans think better in base-10. 100 is easy to visualize (grid of 10×10).

### The Holy Trinity
| Concept | Symbol | Meaning |
|---------|--------|---------|
| **Percentage** | P% | The rate (out of 100) |
| **Base** | B | The reference value (what you're taking % of) |
| **Value** | V | The actual amount |

**Master Formula**: `V = (P/100) × B` or simply `V = P% × B`

---

## 🔑 Essential Formulas

### 1. Basic Conversions

| From → To | Formula | Example |
|-----------|---------|---------|
| Fraction → % | Multiply by 100 | 3/4 = 75% |
| % → Fraction | Divide by 100 | 25% = 1/4 |
| Decimal → % | Multiply by 100 | 0.6 = 60% |
| % → Decimal | Divide by 100 | 45% = 0.45 |

### 2. Percentage of a Number
```
x% of N = (x × N) / 100
```
**Trick**: "of" means multiply → x% of N = (x/100) × N

### 3. What % is A of B?
```
(A/B) × 100 = Answer%
```
**Example**: What % is 15 of 60? → (15/60) × 100 = 25%

### 4. Percentage Change Formula
```
% Change = [(New - Old) / Old] × 100
```
**Memory Hook**: "NOO" - (New minus Old, Over Old) × 100

### 5. Successive Percentage Changes
If value changes by a% then by b%:
```
Net Effect = a + b + (ab/100)
```
**Derivation**: 
- After a%: Value = V(1 + a/100)
- After b%: Value = V(1 + a/100)(1 + b/100)
- Net = V[1 + a/100 + b/100 + ab/10000]
- Net % change = a + b + ab/100

---

## ⚡ Speed Tricks & Mental Math

### Trick 1: The Fraction-Percentage Table (MEMORIZE THIS!)

| Fraction | Percentage | Decimal |
|----------|------------|---------|
| 1/2 | 50% | 0.5 |
| 1/3 | 33.33% | 0.333 |
| 1/4 | 25% | 0.25 |
| 1/5 | 20% | 0.2 |
| 1/6 | 16.67% | 0.167 |
| 1/7 | 14.28% | 0.1428 |
| 1/8 | 12.5% | 0.125 |
| 1/9 | 11.11% | 0.111 |
| 1/10 | 10% | 0.1 |
| 1/11 | 9.09% | 0.0909 |
| 1/12 | 8.33% | 0.083 |

### Trick 2: Splitting for Fast Calculation
```
23% of 500 = (20% + 3%) of 500
           = 100 + 15 
           = 115
```

### Trick 3: Reverse Calculation
```
17% of X = Y 
means 
X of 17% = Y 
means
X% of 17 = Y
```
**Example**: 8% of 25 = 25% of 8 = 2 ✓

### Trick 4: The "Move Decimal" Trick
- 10% → Move decimal one left
- 1% → Move decimal two left
- 5% → Half of 10%

**Example**: 35% of 480
- 10% = 48
- 30% = 144
- 5% = 24
- 35% = 144 + 24 = 168 ✓

### Trick 5: Multiplier Method
Instead of calculating percentage change, use multipliers:
- Increase of 20% → Multiply by 1.2
- Decrease of 25% → Multiply by 0.75

---

## 🎯 Key Patterns in GATE/ESE

### Pattern 1: Successive Percentage Changes

**Example**: Price increases by 10%, then decreases by 10%. Net change?
```
Net = 10 + (-10) + (10 × -10)/100 = 0 - 1 = -1%
```
**Insight**: Equal % up then down always results in NET LOSS!

**General Formula for same % increase then decrease**:
```
Net Loss = -(x²/100)%
```

### Pattern 2: Population/Compound Growth
```
Final = Initial × (1 + r/100)^n
```
Where:
- r = rate of growth per period
- n = number of periods

### Pattern 3: Depreciation
```
Final = Initial × (1 - r/100)^n
```

### Pattern 4: A is X% More/Less Than B
| Statement | Meaning | Formula |
|-----------|---------|---------|
| A is 20% more than B | A = B + 0.2B | A = 1.2B |
| A is 20% less than B | A = B - 0.2B | A = 0.8B |

**Critical Trap**: "A is 25% more than B" ≠ "B is 25% less than A"
- If A = 125, B = 100 → A is 25% more than B ✓
- But B is 20% less than A (not 25%!)

### Pattern 5: Expenditure Problems
```
Expenditure = Price × Quantity

If price changes by p% and quantity changes by q%:
Net change in expenditure = p + q + (pq/100)
```

---

## 🔄 Inverse Relationships

### The Golden Rule
If A is x% more than B, then B is `[x/(100+x)] × 100`% less than A.

| A is more than B by | B is less than A by |
|---------------------|---------------------|
| 10% | 9.09% (1/11) |
| 20% | 16.67% (1/6) |
| 25% | 20% (1/5) |
| 33.33% | 25% (1/4) |
| 50% | 33.33% (1/3) |

**Formula Derivation**:
- Let B = 100
- A = 100 + x% of 100 = 100 + x
- B less than A by = [(A-B)/A] × 100 = [x/(100+x)] × 100

---

## 🧩 Real-World Analogies

### Analogy 1: The Pizza Slice
- 100% = Full pizza
- 50% = Half pizza
- 25% = Quarter pizza

### Analogy 2: The Progress Bar
Your download is at 75% = 3/4 complete = 0.75 of total file.

### Analogy 3: Tax & Discount
- 18% GST means: For every ₹100 price, pay ₹18 extra
- 30% discount means: For every ₹100 price, pay only ₹70

### Analogy 4: Successive Changes = Compound Effect
Like hitting a punching bag:
- First hit pushes it 10% back
- Second hit adds 20% MORE from new position
- Net displacement ≠ simple addition

---

## ⚠️ Common Mistakes & Edge Cases

### Mistake 1: Percentage Point vs Percentage Change
- "Interest rate changed from 5% to 8%"
- **Wrong**: 3% increase
- **Correct**: 3 percentage POINTS increase, which is 60% relative increase!

### Mistake 2: Base Confusion
"A is 25% of B" vs "A is 25% more than B"
- 25% of B → A = 0.25B
- 25% more than B → A = 1.25B

### Mistake 3: Successive % ≠ Simple Addition
- 20% increase then 30% increase ≠ 50% increase
- Correct: 20 + 30 + (20×30)/100 = 56%

### Edge Case 1: 100% Decrease
- 100% decrease = Value becomes 0
- More than 100% decrease is not physically possible for positive quantities

### Edge Case 2: Negative Base
- When dealing with profits/losses, the base might be negative
- 10% of -100 = -10

### Edge Case 3: Very Large Percentages
- 200% of X = 2X (not X + 200)
- 250% increase means final = 3.5X

---

## 📋 Quick Problem-Solving Framework

### Step 1: Identify
- What is the BASE? (Reference value)
- What is being asked? (Value or Percentage)

### Step 2: Setup
- Write the relationship: V = P% × B

### Step 3: Solve
- Plug in known values
- Solve for unknown

### Step 4: Verify
- Does the answer make sense?
- Cross-check with approximation

---

## 🎓 GATE/ESE Level Problems

### Type 1: Basic Calculation
**Q**: If 35% of a number is 70, find 50% of that number.
**Solution**:
- 35% of N = 70
- N = 70 × 100/35 = 200
- 50% of 200 = 100 ✓

### Type 2: Percentage Change
**Q**: A shopkeeper marks up goods by 25% and gives 20% discount. Find net profit%.
**Solution**:
- Let CP = 100
- MP = 125 (25% markup)
- SP = 125 × 0.8 = 100 (20% discount)
- Profit = 0%
- OR use formula: 25 + (-20) + (25×-20)/100 = 25 - 20 - 5 = 0% ✓

### Type 3: Compound Percentage
**Q**: Population of city increases by 10% every year. In how many years will it double?
**Solution**:
- After n years: P(1.1)^n = 2P
- (1.1)^n = 2
- n × log(1.1) = log(2)
- n = 0.301/0.041 ≈ 7.27 years ≈ 8 years (complete years)

### Type 4: Mixture Problems with Percentage
**Q**: Two solutions of 40% and 60% acid are mixed to get 30L of 52% acid. Find quantities.
**Solution**:
- Let x = quantity of 40% solution
- 30-x = quantity of 60% solution
- 0.4x + 0.6(30-x) = 0.52 × 30
- 0.4x + 18 - 0.6x = 15.6
- -0.2x = -2.4
- x = 12L (40% solution)
- 18L (60% solution) ✓

### Type 5: Reverse Percentage
**Q**: After 20% increase, price is ₹600. Find original price.
**Solution**:
- 1.2 × Original = 600
- Original = 600/1.2 = ₹500 ✓

---

## 📊 Cheat Sheet for Quick Revision

```
┌─────────────────────────────────────────────────────────────────┐
│                    PERCENTAGE CHEAT SHEET                       │
├─────────────────────────────────────────────────────────────────┤
│ x% of N = (x × N)/100 = N × (x/100)                             │
│                                                                  │
│ % Change = [(New - Old)/Old] × 100                              │
│                                                                  │
│ Successive Changes: Net = a + b + ab/100                        │
│                                                                  │
│ Same % up then down: Net Loss = -x²/100                         │
│                                                                  │
│ Compound Growth: Final = Initial × (1 + r/100)^n                │
│                                                                  │
│ A is x% more than B → B is [x/(100+x)]×100 % less than A        │
│                                                                  │
│ Key Fractions: 1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%            │
│               1/6=16.67%, 1/8=12.5%, 1/9=11.11%                 │
├─────────────────────────────────────────────────────────────────┤
│ REMEMBER: "of" = multiply | "is" = equals | Base = Denominator  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Pro Tips for Exam

1. **Always identify the BASE first** - Most errors come from wrong base selection
2. **Use multipliers for speed** - 15% increase = ×1.15, not +15%
3. **Round intelligently** - 33.33% ≈ 1/3, 66.67% ≈ 2/3
4. **Check boundary conditions** - Does 0% and 100% give expected results?
5. **When stuck, assume base = 100** - Makes calculations easier
6. **For multiple changes, work left to right** - Apply each change sequentially

---

## 🔗 Related Topics
- **Profit & Loss** - Uses percentage concepts extensively
- **Simple & Compound Interest** - Percentage over time
- **Ratio & Proportion** - Foundation for percentage

---

*Made with ❤️ for GATE & ESE aspirants*
