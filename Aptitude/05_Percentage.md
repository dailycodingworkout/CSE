# Percentage | GATE ESE PSU - Maximum Difficulty Question Bank

## The Atomic Truth
> **"Per Hundred—everything is relative to 100."**

---

## Question 1 | Successive Percentage Change Trap (NAT)

**Problem:** A price is first increased by 20%, then decreased by 20%. Find the net percentage change.

**Trap Alert:** Many think +20% and -20% cancel out. WRONG!

### Solution via Technique:
**Successive Change Formula:**
$$\text{Net \%} = a + b + \frac{ab}{100}$$

Where a = +20, b = -20:
$$= 20 + (-20) + \frac{20 \times (-20)}{100} = 0 - 4 = -4\%$$

**Answer: -4% (decrease)**

**Verification:** 
Start: 100
After 20% increase: 120
After 20% decrease: 120 × 0.8 = 96
Change: 96 - 100 = -4 ✓

**5-Second Snap-Check:** % decrease on a larger base (120) has more absolute effect than same % increase on smaller base (100).

---

## Question 2 | Population Growth (NAT)

**Problem:** A city's population increases by 10% in the first year and 20% in the second year. Find the overall percentage increase over two years.

### Solution via Technique:
**Compound Growth:**
$$\text{Final} = \text{Initial} \times 1.10 \times 1.20 = 1.32 \times \text{Initial}$$

**Net increase = 32%**

**Using formula:** $10 + 20 + \frac{10 \times 20}{100} = 30 + 2 = 32\%$

**Answer: 32%**

---

## Question 3 | Percentage of Percentage (NAT)

**Problem:** What is 40% of 60% of 500?

### Solution via Technique:
$$0.40 \times 0.60 \times 500 = 0.24 \times 500 = 120$$

**Answer: 120**

---

## Question 4 | Reverse Percentage (NAT)

**Problem:** After a 25% discount, the price of a shirt is ₹750. Find the original price.

**Trap Alert:** Don't add 25% to 750!

### Solution via Technique:
**If 25% is discounted, 75% remains:**
$$0.75 \times \text{Original} = 750$$
$$\text{Original} = \frac{750}{0.75} = 1000$$

**Answer: ₹1000**

**Wrong Approach:** 750 + 25% of 750 = 750 + 187.5 = 937.5 ≠ 1000 ✗

---

## Question 5 | Percentage Increase/Decrease (NAT)

**Problem:** If A is 25% more than B, by what percent is B less than A?

**Trap Alert:** It's NOT 25%!

### Solution via Technique:
**Let B = 100, then A = 125**

**B less than A by:**
$$\frac{A - B}{A} \times 100 = \frac{125 - 100}{125} \times 100 = \frac{25}{125} \times 100 = 20\%$$

**Answer: 20%**

**Quick Formula:** If A is r% more than B, then B is $\frac{r}{100+r} \times 100$% less than A.
$$= \frac{25}{125} \times 100 = 20\%$$ ✓

---

## Question 6 | Profit and Loss (NAT)

**Problem:** An article is sold at 20% profit. If the cost price and selling price are both reduced by ₹100, the profit becomes 40/3%. Find the cost price.

### Solution via Technique:
**Let CP = C**

**Original:** SP = 1.2C, Profit = 0.2C

**New:** CP' = C - 100, SP' = 1.2C - 100

**New Profit%:**
$$\frac{\text{SP'} - \text{CP'}}{\text{CP'}} \times 100 = \frac{40}{3}\%$$

$$\frac{(1.2C - 100) - (C - 100)}{C - 100} \times 100 = \frac{40}{3}$$

$$\frac{0.2C}{C - 100} \times 100 = \frac{40}{3}$$

$$\frac{20C}{C - 100} = \frac{40}{3}$$

**Cross-multiplying:** $60C = 40(C - 100)$
$$60C = 40C - 4000$$
$$20C = -4000$$

**Note:** This gives a negative value, indicating the problem as stated has inconsistent parameters. When both CP and SP are reduced by the same amount, the profit PERCENTAGE always INCREASES (not decreases to 40/3 = 13.33% from 20%).

**Corrected Problem Interpretation:** If the new profit is 40% (not 40/3%), then:
$$\frac{0.2C}{C - 100} = 0.4$$
$$0.2C = 0.4C - 40$$
$$0.2C = 40$$
$$C = 200$$

**Answer: ₹200** (with corrected interpretation)

**Verification:** CP = 200, SP = 240
New CP = 100, New SP = 140
New Profit = 40, New Profit% = 40%

---

## Question 7 | Compound Interest vs Simple Interest (NAT)

**Problem:** The difference between CI and SI on a sum at 10% per annum for 2 years is ₹50. Find the principal.

### Solution via Technique:
**For 2 years:**
$$CI - SI = P \times \left(\frac{r}{100}\right)^2$$

$$50 = P \times (0.10)^2 = P \times 0.01$$

$$P = 5000$$

**Answer: ₹5000**

**Verification:**
SI = 5000 × 0.10 × 2 = 1000
CI = 5000 × (1.1)² - 5000 = 5000 × 1.21 - 5000 = 1050
Difference = 1050 - 1000 = 50 ✓

---

## Question 8 | Discount Chain (NAT)

**Problem:** A shopkeeper offers successive discounts of 20% and 10%. What single discount is equivalent?

### Solution via Technique:
**Equivalent Discount:**
$$d_{eq} = a + b - \frac{ab}{100}$$

Wait, for discounts (both reducing):
$$1 - d_{eq} = (1 - 0.20)(1 - 0.10) = 0.80 \times 0.90 = 0.72$$
$$d_{eq} = 1 - 0.72 = 0.28 = 28\%$$

**Or using formula:** $20 + 10 - \frac{20 \times 10}{100} = 30 - 2 = 28\%$

**Answer: 28%**

---

## Question 9 | Percentage Change in Area (NAT)

**Problem:** If the length and breadth of a rectangle are each increased by 10%, find the percentage increase in area.

### Solution via Technique:
**If both dimensions change by r%:**
$$\text{Area change \%} = r + r + \frac{r^2}{100} = 2r + \frac{r^2}{100}$$

For r = 10:
$$= 20 + 1 = 21\%$$

**Answer: 21%**

---

## Question 10 | Vote Percentage (NAT)

**Problem:** In an election between two candidates, 15% of votes were invalid. The winner got 60% of valid votes and won by 1200 votes. Find the total number of votes.

### Solution via Technique:
**Valid votes = 85% of total**

**Winner: 60% of valid, Loser: 40% of valid**
**Difference = 20% of valid votes = 1200**

**Valid votes = 1200 / 0.20 = 6000**

**Total votes = 6000 / 0.85 ≈ 7058.82**

Hmm, not a round number. Let me recheck:

If total = T, valid = 0.85T
Difference = 0.20 × 0.85T = 0.17T = 1200
T = 1200/0.17 ≈ 7058.82

For clean answer, let's verify: 7059 × 0.85 = 6000.15 (approximately 6000)
0.20 × 6000 = 1200 ✓

**Answer: 7059** (or approximately 7058.82)

Actually, let's use exact math:
0.17T = 1200
T = 1200/0.17 = 120000/17 ≈ 7058.82

**Answer: 120000/17 ≈ 7059**

---

## Question 11 | Salary Percentage (NAT)

**Problem:** A's salary is 20% less than B's salary. By what percent is B's salary more than A's?

### Solution via Technique:
**Let B's salary = 100, then A's = 80**

**B more than A by:**
$$\frac{100 - 80}{80} \times 100 = \frac{20}{80} \times 100 = 25\%$$

**Answer: 25%**

**Quick Formula:** If A is r% less than B, then B is $\frac{r}{100-r} \times 100$% more than A.
$$= \frac{20}{80} \times 100 = 25\%$$ ✓

---

## Question 12 | Markup and Discount (NAT)

**Problem:** A trader marks his goods 40% above cost price and gives 25% discount. Find his profit percentage.

### Solution via Technique:
**Let CP = 100**
**MP (Marked Price) = 140**
**SP = MP - 25% of MP = 140 × 0.75 = 105**

**Profit = 105 - 100 = 5**
**Profit % = 5%**

**Answer: 5%**

**Using Formula:** 
$$\text{Profit \%} = \text{Markup \%} - \text{Discount \%} - \frac{\text{Markup} \times \text{Discount}}{100}$$
$$= 40 - 25 - 10 = 5\%$$

---

## Question 13 | Expenditure Change (NAT)

**Problem:** If the price of sugar increases by 25%, by what percent should consumption be reduced to keep expenditure the same?

### Solution via Technique:
**Expenditure = Price × Consumption = constant**

If price increases by r%, consumption must decrease by $\frac{r}{100+r} \times 100$%

$$= \frac{25}{125} \times 100 = 20\%$$

**Answer: 20%**

---

## Question 14 | Percentage Error (NAT)

**Problem:** In measuring a rectangle, the length is overestimated by 5% and breadth is underestimated by 4%. Find the percentage error in calculated area.

### Solution via Technique:
**Area change:** 
$$= 5 + (-4) + \frac{5 \times (-4)}{100}$$
$$= 5 - 4 - 0.2 = 0.8\%$$

**Answer: +0.8% (overestimate)**

---

## Question 15 | Three Successive Changes (NAT)

**Problem:** A number is successively increased by 10%, 20%, and 25%. Find the overall percentage increase.

### Solution via Technique:
**Compound Factor:**
$$1.10 \times 1.20 \times 1.25 = 1.65$$

**Overall increase = 65%**

**Answer: 65%**

---

## Question 16 | Percentage of Total (MSQ)

**Problem:** In a mixture, A and B are in ratio 3:2. Which statements are TRUE?

A) A is 60% of the mixture  
B) B is 40% of the mixture  
C) A is 150% of B  
D) B is 66.67% of A

### Solution via Technique:
**Total = 3 + 2 = 5 parts**

**A:** 3/5 = 60% ✓ (A is TRUE)
**B:** 2/5 = 40% ✓ (B is TRUE)

**A as % of B:** (3/2) × 100 = 150% ✓ (C is TRUE)
**B as % of A:** (2/3) × 100 = 66.67% ✓ (D is TRUE)

**Answer: A, B, C, D (all TRUE)**

---

## Question 17 | Tax Calculation (NAT)

**Problem:** An item's listed price is ₹5000. A discount of 10% is given, then 18% GST is applied. Find the final price.

### Solution via Technique:
**After discount:** 5000 × 0.90 = 4500
**After GST:** 4500 × 1.18 = 5310

**Answer: ₹5310**

**Trap Alert:** GST is applied AFTER discount, not on MRP!

---

## Question 18 | Percentage in Mixtures (NAT)

**Problem:** 40 liters of 30% alcohol solution is mixed with 60 liters of 50% alcohol solution. Find the concentration of the resulting mixture.

### Solution via Technique:
**Alcohol from 1st:** 40 × 0.30 = 12 liters
**Alcohol from 2nd:** 60 × 0.50 = 30 liters
**Total alcohol:** 12 + 30 = 42 liters
**Total mixture:** 40 + 60 = 100 liters

**Concentration:** 42/100 = 42%

**Answer: 42%**

---

## Question 19 | Growth and Decay (NAT)

**Problem:** A machine depreciates 10% each year. After how many complete years will its value be less than half the original?

### Solution via Technique:
**After n years:** Value = Original × $(0.9)^n$

We need: $(0.9)^n < 0.5$

Taking log: $n \times \log(0.9) < \log(0.5)$
$n > \frac{\log(0.5)}{\log(0.9)} = \frac{-0.301}{-0.046} ≈ 6.5$

**After 7 complete years:** $(0.9)^7 ≈ 0.478 < 0.5$ ✓

**Answer: 7 years**

---

## Question 20 | Fraction to Percentage Conversions (Reference)

| Fraction | Percentage |
|----------|------------|
| 1/2 | 50% |
| 1/3 | 33.33% |
| 1/4 | 25% |
| 1/5 | 20% |
| 1/6 | 16.67% |
| 1/7 | 14.29% |
| 1/8 | 12.5% |
| 1/9 | 11.11% |
| 1/10 | 10% |
| 1/11 | 9.09% |
| 1/12 | 8.33% |
| 2/3 | 66.67% |
| 3/4 | 75% |
| 2/5 | 40% |
| 3/5 | 60% |
| 4/5 | 80% |

---

## Question 21 | Percentage Points vs Percentage Change (MSQ)

**Problem:** Pass percentage increased from 60% to 72%. Which statements are correct?

A) Increase is 12 percentage points  
B) Increase is 20%  
C) Increase is 12%  
D) The pass rate increased by 12 percentage points

**Trap Alert:** "Percentage points" ≠ "Percent increase"!

### Solution via Technique:
**Percentage Points:** 72 - 60 = 12 pp ✓ (A and D are TRUE)

**Percent Increase:** $\frac{72-60}{60} \times 100 = \frac{12}{60} \times 100 = 20\%$ ✓ (B is TRUE)

**C says "12%" which would be the percentage points misnamed. It's technically wrong terminology.**

**Answer: A, B, D**

---

## Question 22 | Compound Percentage Application (NAT)

**Problem:** In a town, 40% are men. 30% of men and 40% of women are literate. Find the overall literacy rate.

### Solution via Technique:
**Men = 40%, Women = 60%**

**Literate men:** 0.30 × 0.40 = 0.12 = 12%
**Literate women:** 0.40 × 0.60 = 0.24 = 24%

**Total literacy:** 12% + 24% = 36%

**Answer: 36%**

---

## Question 23 | Percentage Decrease Trap (NAT)

**Problem:** A shopkeeper loses 20%. If he increases the SP by 30%, what is his new profit or loss percentage on CP?

### Solution via Technique:
**Original:** CP = 100, SP = 80 (20% loss)

**New SP:** 80 × 1.30 = 104

**New Profit:** 104 - 100 = 4

**Profit %:** 4%

**Answer: 4% profit**

---

## Question 24 | Bonus Multiplier Effect (NAT)

**Problem:** If a worker's efficiency increases by 25%, by what percent should his working hours be reduced to produce the same output?

### Solution via Technique:
**Output = Efficiency × Time = constant**

If efficiency increases by r%, time decreases by $\frac{r}{100+r} \times 100$%

$$= \frac{25}{125} \times 100 = 20\%$$

**Answer: 20%**

---

## Question 25 | Exam Marks Percentage (NAT)

**Problem:** A student needs 40% to pass. He gets 180 marks and fails by 20 marks. Find the maximum marks.

### Solution via Technique:
**Passing marks = 180 + 20 = 200**

**40% of Maximum = 200**

**Maximum = 200/0.40 = 500**

**Answer: 500**

---

## Mental Machinery

### The Bizarre Mnemonic for Percentages:
**"Percent = Per Century = Per 100"**

Imagine 100 soldiers (a century). 25% means 25 soldiers. If 20 out of 50 soldiers are injured, that's 20/50 = 40% (scale to 100 → 40/100).

### The Mental Slider for Successive Changes:
Visualize a **rubber band**:
- Stretch 20% → length = 1.2
- Shrink 20% of NEW length → 1.2 × 0.8 = 0.96
- Net: Band is slightly shorter than original!

### The 5-Second Snap-Checks:
- **Opposite changes don't cancel:** +r% then -r% gives net LOSS
- **Percentage of = Multiply, Percentage more/less = Add/Subtract**
- **On what base?** Always identify the reference (CP, SP, original, new)
- **Points vs Percent:** 60→72 is 12 points but 20% increase
- **Quick fractions:** 1/4 = 25%, 1/5 = 20%, 1/8 = 12.5%

---

## Common Traps Summary

| Trap | Wrong Answer | Correct Approach |
|------|--------------|------------------|
| +20% then -20% | 0% change | Use formula: -4% |
| A is 25% more than B, B is ___% less than A | 25% | 20% (different base) |
| After 25% discount, find original | Add 25% to discounted | Divide by 0.75 |
| Price up 25%, reduce consumption by | 25% | 20% (100/125) |
| CI - SI for 2 years | Complex | P × (r/100)² |

---

## Mastery Checkpoint

**You have completed the Percentage module.** Percentage calculations appear in almost every quantitative section and combine with profit/loss, SI/CI, and data interpretation problems.

**Congratulations!** You have completed all five core aptitude modules. Review the master README for quick reference formulas and use the 4-week practice roadmap to consolidate your preparation.
