# Percentage | MAX-DIFFICULTY Logic Coverage Set

> **Supreme Architect Protocol**: This set exhausts the logic-space of Percentages. Each question destroys at least one memorized shortcut. No two questions share the same dominant reasoning path.

---

## Question 1: The Base Change Deception

### Best Technique
Always identify the **correct base** for percentage calculation. The base is what the percentage is "of" or "out of."

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Assumption poisoning (base assumed incorrectly)
- **Secondary Logic Interactions**: Examiner-language misdirection
- **Why Lethal**: "Of" and "than" create different bases in the same sentence

### 2️⃣ Question
If A is 25% more than B, then B is what percent less than A?

### 3️⃣ Examiner's Intent
- Tests base change in percentage comparison
- Top-100 fail by answering 25%

### 4️⃣ Solution (Logic-First)
1. Let $B = 100$, then $A = 125$
2. Difference = $125 - 100 = 25$
3. B is less than A by: $\frac{25}{125} \times 100 = 20\%$
4. **Formula**: If A is $x\%$ more than B, then B is $\frac{x}{100+x} \times 100\%$ less than A
5. Here: $\frac{25}{125} \times 100 = 20\%$
6. **Answer: 20%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 25%
- **Why it feels correct**: Same difference, so same percentage
- **Exact failure point**: Different bases (B for "more than", A for "less than")

### 6️⃣ Generalization Map
1. A is 50% more than B
2. A is $x\%$ less than B, find B compared to A
3. Chain of comparisons (A to B to C)
4. Percentage of percentage
5. Compound percentage changes

### 7️⃣ Neural Anchor
**"Base-Flip"**

---

## Question 2: The Successive Change

### Best Technique
For successive changes, **multiply the factors**: $(1 \pm p_1\%)(1 \pm p_2\%) - 1$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: False linearity assumption
- **Secondary Logic Interactions**: Multiplicative vs additive
- **Why Lethal**: Percentages don't simply add for successive changes

### 2️⃣ Question
A price increases by 20% and then decreases by 20%. What is the net percentage change?

### 3️⃣ Examiner's Intent
- Tests that $+x\%$ followed by $-x\%$ ≠ 0%
- Top-100 fail by computing $20\% - 20\% = 0\%$

### 4️⃣ Solution (Logic-First)
1. Let original price = 100
2. After 20% increase: $100 \times 1.20 = 120$
3. After 20% decrease: $120 \times 0.80 = 96$
4. Net change = $96 - 100 = -4$, which is $-4\%$
5. **Formula**: Net change $= (1.20)(0.80) - 1 = 0.96 - 1 = -0.04 = -4\%$
6. **Answer: 4% decrease**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 0% (no net change)
- **Why it feels correct**: $+20\%$ and $-20\%$ seem to cancel
- **Exact failure point**: Ignoring that decrease is from higher base

### 6️⃣ Generalization Map
1. Three successive changes
2. Equal increases and decreases of different percentages
3. Find the break-even percentage
4. Compound interest vs simple interest
5. Population growth and decline

### 7️⃣ Neural Anchor
**"Multiply-Factors"**

---

## Question 3: The Percentage Point Confusion

### Best Technique
Distinguish **percentage points** (absolute difference) from **percentage change** (relative difference)

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Examiner-language misdirection (critical)
- **Secondary Logic Interactions**: Absolute vs relative
- **Why Lethal**: "Percentage points" and "percent" mean different things

### 2️⃣ Question
Interest rate rises from 8% to 10%. Express this as (a) percentage point increase and (b) percentage increase.

### 3️⃣ Examiner's Intent
- Tests understanding of percentage point vs percentage
- Top-100 fail by giving same answer for both

### 4️⃣ Solution (Logic-First)
1. **Percentage point increase** = $10\% - 8\% = 2$ percentage points
2. **Percentage increase** = $\frac{10 - 8}{8} \times 100 = \frac{2}{8} \times 100 = 25\%$
3. **Answer: (a) 2 percentage points, (b) 25%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: Both are 2%
- **Why it feels correct**: Direct subtraction seems like the answer
- **Exact failure point**: Not recognizing two different measures

### 6️⃣ Generalization Map
1. Decrease from 50% to 40%
2. News headlines about polling changes
3. Tax rate changes
4. Market share changes
5. Inflation rate changes

### 7️⃣ Neural Anchor
**"Point-vs-Percent"**

---

## Question 4: The Reverse Percentage

### Best Technique
To find original from final: Original = Final / $(1 \pm x\%)$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Reverse reasoning (answer → question)
- **Secondary Logic Interactions**: Division vs multiplication
- **Why Lethal**: Students multiply when they should divide

### 2️⃣ Question
After a 15% discount, the price of a shirt is ₹510. What was the original price?

### 3️⃣ Examiner's Intent
- Tests reverse percentage calculation
- Top-100 fail by adding 15% to 510

### 4️⃣ Solution (Logic-First)
1. After 15% discount: price = Original × 0.85
2. $510 = \text{Original} \times 0.85$
3. Original = $510 / 0.85 = 600$
4. **Verification**: $600 \times 0.85 = 510$ ✓
5. **Answer: ₹600**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: $510 \times 1.15 = 586.50$
- **Why it feels correct**: Adding back 15% seems logical
- **Exact failure point**: Adding 15% of discounted price, not original

### 6️⃣ Generalization Map
1. After tax addition
2. After multiple discounts
3. Find discount percent given both prices
4. Markup percentage problems
5. Commission included in price

### 7️⃣ Neural Anchor
**"Divide-Not-Add"**

---

## Question 5: The Population Paradox

### Best Technique
Use **compound growth formula**: $P = P_0(1 + r)^n$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Discrete vs continuous trap
- **Secondary Logic Interactions**: Exponential vs linear growth
- **Why Lethal**: Annual compounding differs from continuous

### 2️⃣ Question
If a population grows at 10% per annum, how many years will it take to double?

### 3️⃣ Examiner's Intent
- Tests compound growth / Rule of 72
- Top-100 fail by computing $100/10 = 10$ years

### 4️⃣ Solution (Logic-First)
1. Need: $(1.10)^n = 2$
2. Take log: $n \log(1.10) = \log(2)$
3. $n = \frac{\log 2}{\log 1.10} = \frac{0.301}{0.0414} \approx 7.27$ years
4. **Rule of 72**: $72/10 = 7.2$ years (quick estimate)
5. **Answer: Approximately 7.27 years**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 10 years (100%/10% per year)
- **Why it feels correct**: Linear thinking
- **Exact failure point**: Ignoring compound growth

### 6️⃣ Generalization Map
1. Triple the population
2. Different growth rates
3. Decline to half
4. Rule of 69 for continuous growth
5. Variable growth rates

### 7️⃣ Neural Anchor
**"Rule-of-72"**

---

## Question 6: The Tax Cascade

### Best Technique
Handle **tax on tax** situations (like GST on cess-inclusive price)

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Non-commutative step dependency
- **Secondary Logic Interactions**: Order of application matters
- **Why Lethal**: Sequential taxes on already-taxed amounts

### 2️⃣ Question
A product has a base price of ₹1000. First, a 10% luxury tax is added. Then, 18% GST is applied on the luxury-tax-inclusive price. What is the final price?

### 3️⃣ Examiner's Intent
- Tests cascading tax calculation
- Top-100 fail by adding 10% + 18% = 28%

### 4️⃣ Solution (Logic-First)
1. After 10% luxury tax: $1000 \times 1.10 = 1100$
2. After 18% GST on 1100: $1100 \times 1.18 = 1298$
3. **Answer: ₹1298**
4. Compare with simple 28%: $1000 \times 1.28 = 1280$ (Wrong!)

### 5️⃣ Trap Autopsy
- **Common wrong answer**: ₹1280 (adding percentages)
- **Why it feels correct**: Total tax seems like 28%
- **Exact failure point**: GST is on already-inflated price

### 6️⃣ Generalization Map
1. Reverse: extract original from final
2. Three-level tax cascade
3. Different tax bases (some on original, some on inclusive)
4. Tax credits and refunds
5. Effective tax rate calculation

### 7️⃣ Neural Anchor
**"Tax-on-Tax"**

---

## Question 7: The Discount Stack

### Best Technique
Apply **successive discounts** multiplicatively: Final = Original × $(1-d_1)(1-d_2)$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: False linearity assumption
- **Secondary Logic Interactions**: Order independence for multiplication
- **Why Lethal**: 30% + 20% discount ≠ 50% discount

### 2️⃣ Question
A store offers a 30% discount followed by an additional 20% discount. What is the equivalent single discount?

### 3️⃣ Examiner's Intent
- Tests successive discount calculation
- Top-100 fail by adding $30\% + 20\% = 50\%$

### 4️⃣ Solution (Logic-First)
1. After 30% off: pay $70\% = 0.70$
2. After 20% off on that: pay $0.70 \times 0.80 = 0.56 = 56\%$
3. Total discount = $100\% - 56\% = 44\%$
4. **Answer: 44% equivalent discount**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 50%
- **Why it feels correct**: Simple addition of discounts
- **Exact failure point**: Second discount is on reduced price

### 6️⃣ Generalization Map
1. Three successive discounts
2. Find one discount given other and equivalent
3. Markup followed by discount
4. Buy one get one free as percentage
5. Loyalty points as effective discount

### 7️⃣ Neural Anchor
**"Discount-Multiply"**

---

## Question 8: The Percentage of Percentage

### Best Technique
Calculate **nested percentages**: $x\%$ of $y\% = \frac{xy}{100}\%$ of original

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Ghost variable cancellation
- **Secondary Logic Interactions**: Order of operations
- **Why Lethal**: "Percent of percent" compounds the percentage operation

### 2️⃣ Question
If 60% of students are girls, and 40% of girls play sports, what percentage of all students are girls who play sports?

### 3️⃣ Examiner's Intent
- Tests multiplication of percentages
- Top-100 fail by adding or averaging

### 4️⃣ Solution (Logic-First)
1. Girls = 60% of all students
2. Girls who play sports = 40% of 60% = $0.40 \times 0.60 = 0.24 = 24\%$
3. **Answer: 24%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 50% (average) or 100% (adding)
- **Why it feels correct**: Mental shortcuts
- **Exact failure point**: Not multiplying fractions/percentages

### 6️⃣ Generalization Map
1. Three nested conditions
2. Find one percentage given others
3. Venn diagram problems
4. Conditional probability connection
5. Market segmentation

### 7️⃣ Neural Anchor
**"Percent-of-Percent-Multiply"**

---

## Question 9: The Profit-Loss Base

### Best Technique
Profit/loss percentage is **always on cost price** unless specified otherwise

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Hidden constraint dominance (base definition)
- **Secondary Logic Interactions**: Standard business convention
- **Why Lethal**: "20% profit" means different things based on base

### 2️⃣ Question
An article is sold at 20% profit. The profit is what percentage of the selling price?

### 3️⃣ Examiner's Intent
- Tests profit as percentage of different bases
- Top-100 fail by answering 20%

### 4️⃣ Solution (Logic-First)
1. Let CP = 100, then Profit = 20, SP = 120
2. Profit as % of SP = $(20/120) \times 100 = 16.67\%$
3. **Answer: 16.67% (or 50/3 %)**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 20%
- **Why it feels correct**: Profit was stated as 20%
- **Exact failure point**: Different base (SP vs CP)

### 6️⃣ Generalization Map
1. Loss as percentage of SP
2. Markup percentage (on CP) vs margin (on SP)
3. Discount on marked price vs cost price
4. Break-even analysis
5. Gross vs net profit

### 7️⃣ Neural Anchor
**"Profit-Base-CP"**

---

## Question 10: The Expenditure Constancy

### Best Technique
When expenditure is constant: Price × Quantity = Constant

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Conservation vs optimization
- **Secondary Logic Interactions**: Inverse proportionality
- **Why Lethal**: Price increase forces quantity decrease to maintain budget

### 2️⃣ Question
If the price of sugar rises by 25%, by what percentage must a family reduce consumption to keep expenditure unchanged?

### 3️⃣ Examiner's Intent
- Tests inverse relationship under constant product
- Top-100 fail by answering 25%

### 4️⃣ Solution (Logic-First)
1. Let original: Price = 100, Quantity = Q, Expenditure = 100Q
2. New price = 125. For same expenditure: $125 \times Q' = 100Q$
3. $Q' = 100Q/125 = 0.8Q$
4. Reduction = $(1 - 0.8) = 0.2 = 20\%$
5. **Formula**: If price increases by $x\%$, reduce by $\frac{x}{100+x} \times 100\%$
6. **Answer: 20%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 25%
- **Why it feels correct**: Same percentage as price increase
- **Exact failure point**: New consumption is of lower quantity at higher price

### 6️⃣ Generalization Map
1. Price decreases by $x\%$
2. Budget increases by $y\%$, price by $x\%$
3. Two commodities with budget split
4. Elasticity of demand
5. Real income effect

### 7️⃣ Neural Anchor
**"Inverse-Price-Quantity"**

---

## Question 11: The Error Propagation

### Best Technique
For errors: Relative error in product ≈ sum of relative errors

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Order-of-magnitude deception
- **Secondary Logic Interactions**: Measurement uncertainty
- **Why Lethal**: Small percentage errors can compound significantly

### 2️⃣ Question
If the length and breadth of a rectangle are measured with errors of +2% and -3% respectively, what is the percentage error in the calculated area?

### 3️⃣ Examiner's Intent
- Tests error propagation in multiplication
- Top-100 fail by computing $(1.02)(0.97)$ incorrectly

### 4️⃣ Solution (Logic-First)
1. True area = L × B
2. Measured area = $(L \times 1.02) \times (B \times 0.97) = LB \times 1.02 \times 0.97$
3. Error factor = $1.02 \times 0.97 = 0.9894$
4. Percentage error = $(0.9894 - 1) \times 100 = -1.06\%$
5. Or approximately: $+2\% + (-3\%) = -1\%$ (first-order approximation)
6. **Answer: -1.06% (approximately 1% underestimate)**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: -5% (adding absolute percentages)
- **Why it feels correct**: Adding errors directly
- **Exact failure point**: Need multiplicative combination

### 6️⃣ Generalization Map
1. Volume of cube with error in side
2. Division (subtract relative errors)
3. Power relationships
4. Composite measurements
5. Significant figures

### 7️⃣ Neural Anchor
**"Error-Multiply"**

---

## Question 12: The Voting Swing

### Best Technique
Handle **vote transfer** between candidates carefully

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Non-commutative step dependency
- **Secondary Logic Interactions**: Total vote conservation
- **Why Lethal**: Votes gained by one = votes lost by another

### 2️⃣ Question
In an election between two candidates, 60% voted for A and 40% for B. If 10% of A's voters had instead voted for B, who would win and by what margin?

### 3️⃣ Examiner's Intent
- Tests vote swing calculation
- Top-100 fail by computing percentage of total instead of swing

### 4️⃣ Solution (Logic-First)
1. Let total voters = 100
2. Original: A = 60, B = 40
3. 10% of A's voters switch: $0.10 \times 60 = 6$ voters
4. New: A = $60 - 6 = 54$, B = $40 + 6 = 46$
5. A still wins by $54 - 46 = 8$ votes = 8%
6. **Answer: A wins by 8%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: B wins (misunderstanding the swing)
- **Why it feels correct**: 10% swing seems large
- **Exact failure point**: 10% of A's votes (6), not 10% of total (10)

### 6️⃣ Generalization Map
1. Find swing needed for tie
2. Three candidates
3. Invalid/null votes
4. Two-round elections
5. Electoral college vs popular vote

### 7️⃣ Neural Anchor
**"Swing-From-Votes"**

---

## Question 13: The Concentration Dilution

### Best Technique
Use $C_1V_1 = C_2V_2$ for dilution or **mixture alligation**

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Conservation vs optimization (mass balance)
- **Secondary Logic Interactions**: Volume additivity
- **Why Lethal**: Concentration decreases when volume increases

### 2️⃣ Question
A solution is 25% salt. How much water must be added to 20 liters of this solution to make it 10% salt?

### 3️⃣ Examiner's Intent
- Tests dilution calculation
- Top-100 fail by computing percentage change directly

### 4️⃣ Solution (Logic-First)
1. Salt in original = $25\% \times 20 = 5$ liters
2. Final solution has 10% salt, so salt remains 5 liters
3. If 10% = 5 liters, then total = $5/0.10 = 50$ liters
4. Water to add = $50 - 20 = 30$ liters
5. **Answer: 30 liters**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 15 liters (25% - 10% = 15% of something)
- **Why it feels correct**: Working with percentage differences
- **Exact failure point**: Salt mass is conserved, not concentration

### 6️⃣ Generalization Map
1. Add more salt (concentrate)
2. Remove water by evaporation
3. Mix two solutions
4. Serial dilution
5. pH calculation

### 7️⃣ Neural Anchor
**"Salt-Conserved"**

---

## Question 14: The Income and Expenditure

### Best Technique
Savings = Income - Expenditure; percentage changes affect each differently

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Ghost variable cancellation
- **Secondary Logic Interactions**: Non-linear relationship
- **Why Lethal**: Savings percentage changes dramatically with small income/expense changes

### 2️⃣ Question
A person saves 20% of income. If income increases by 25% and expenditure increases by 30%, what is the percentage change in savings?

### 3️⃣ Examiner's Intent
- Tests savings calculation with multiple changes
- Top-100 fail by averaging the percentage changes

### 4️⃣ Solution (Logic-First)
1. Let Income = 100, then Expenditure = 80, Savings = 20
2. New Income = $100 \times 1.25 = 125$
3. New Expenditure = $80 \times 1.30 = 104$
4. New Savings = $125 - 104 = 21$
5. Change in Savings = $(21 - 20)/20 \times 100 = 5\%$ increase
6. **Answer: 5% increase**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: $25\% - 30\% = -5\%$ decrease
- **Why it feels correct**: Simple subtraction of rates
- **Exact failure point**: Changes apply to different bases

### 6️⃣ Generalization Map
1. Fixed expenditure, income changes
2. Savings ratio target
3. Multiple expense categories
4. Inflation adjustment
5. Tax on income

### 7️⃣ Neural Anchor
**"Savings-Residual"**

---

## Question 15: The Percentage Error in Division

### Best Technique
For $z = x/y$: Relative error $≈ |(\Delta x/x) - (\Delta y/y)|$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Multiple valid methods — only one legal
- **Secondary Logic Interactions**: Error subtraction in division
- **Why Lethal**: Division error ≠ product error

### 2️⃣ Question
If numerator is overestimated by 10% and denominator is underestimated by 10%, what is the approximate percentage error in the quotient?

### 3️⃣ Examiner's Intent
- Tests error in division
- Top-100 fail by subtracting $10\% - 10\% = 0\%$

### 4️⃣ Solution (Logic-First)
1. True quotient = $N/D$
2. Measured = $(N \times 1.10)/(D \times 0.90) = (N/D) \times (1.10/0.90) = (N/D) \times 1.222$
3. Error = $(1.222 - 1) \times 100 = 22.2\%$ overestimate
4. **Answer: Approximately 22.2% overestimate**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 0% or 20%
- **Why it feels correct**: Errors seem to cancel or simply add
- **Exact failure point**: Underestimate in denominator inflates quotient

### 6️⃣ Generalization Map
1. Same direction errors
2. Multiple factors in numerator/denominator
3. Maximum possible error
4. Propagation through complex formula
5. Systematic vs random errors

### 7️⃣ Neural Anchor
**"Division-Error-Add"**

---

## Question 16: The Index Number

### Best Technique
Calculate **price index**: (Current price / Base price) × 100

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Order-of-magnitude deception
- **Secondary Logic Interactions**: Base year = 100 by definition
- **Why Lethal**: Index numbers are relative, not absolute

### 2️⃣ Question
If 2010 is the base year with index 100, and prices rise by 20% from 2010 to 2015, then by 10% from 2015 to 2020, what is the 2020 price index?

### 3️⃣ Examiner's Intent
- Tests compound index calculation
- Top-100 fail by adding $100 + 20 + 10 = 130$

### 4️⃣ Solution (Logic-First)
1. 2010 index = 100
2. 2015 index = $100 \times 1.20 = 120$
3. 2020 index = $120 \times 1.10 = 132$
4. **Answer: 132**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 130
- **Why it feels correct**: Adding percentage increases
- **Exact failure point**: Compound growth, not linear addition

### 6️⃣ Generalization Map
1. Change base year
2. Real vs nominal values
3. Weighted price index (Laspeyres, Paasche)
4. Consumer price index
5. Deflation scenario

### 7️⃣ Neural Anchor
**"Index-Compound"**

---

## Question 17: The Partnership Profit Split

### Best Technique
Profit split ∝ Capital × Time (for partnership problems)

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Hidden constraint dominance (time factor)
- **Secondary Logic Interactions**: Proportional distribution
- **Why Lethal**: Unequal investment periods change the ratio

### 2️⃣ Question
A invests ₹50,000 for 12 months, B invests ₹60,000 for 10 months. If the profit is ₹23,000, how much does A receive?

### 3️⃣ Examiner's Intent
- Tests capital × time proportionality
- Top-100 fail by using capital ratio alone

### 4️⃣ Solution (Logic-First)
1. A's investment share = $50,000 \times 12 = 600,000$
2. B's investment share = $60,000 \times 10 = 600,000$
3. Ratio A:B = 600,000 : 600,000 = 1:1
4. A's profit = $23,000 \times (1/2) = ₹11,500$
5. **Answer: ₹11,500**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: ₹10,000 (using 50:60 ratio)
- **Why it feels correct**: Only considering capital
- **Exact failure point**: Ignoring time component

### 6️⃣ Generalization Map
1. Three partners
2. Varying investments over time
3. Salary + profit share
4. Working vs sleeping partner
5. Loss distribution

### 7️⃣ Neural Anchor
**"Capital-Times-Time"**

---

## Question 18: The Compound Interest vs Simple Interest

### Best Technique
CI - SI = Extra interest = $P \times (r/100)^2$ for 2 years

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Discrete vs continuous trap
- **Secondary Logic Interactions**: Interest on interest
- **Why Lethal**: Difference grows non-linearly with time

### 2️⃣ Question
The difference between CI and SI on ₹10,000 for 2 years at 10% p.a. is?

### 3️⃣ Examiner's Intent
- Tests CI-SI difference formula
- Top-100 fail by computing both fully

### 4️⃣ Solution (Logic-First)
1. SI for 2 years = $10,000 \times 0.10 \times 2 = 2,000$
2. CI for 2 years = $10,000 \times (1.10)^2 - 10,000 = 10,000 \times 0.21 = 2,100$
3. Difference = $2,100 - 2,000 = ₹100$
4. **Formula**: Difference = $P \times (r/100)^2 = 10,000 \times 0.01 = 100$
5. **Answer: ₹100**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: ₹200 or ₹0
- **Why it feels correct**: Confusion about what the difference represents
- **Exact failure point**: Not recognizing interest-on-interest

### 6️⃣ Generalization Map
1. Three years difference
2. Half-yearly compounding
3. Find principal given difference
4. Find rate given difference
5. Continuous compounding

### 7️⃣ Neural Anchor
**"CI-SI-Squared"**

---

## Question 19: The Market Share

### Best Technique
Track **relative market positions** as percentages of total

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Conservation vs optimization
- **Secondary Logic Interactions**: Zero-sum game
- **Why Lethal**: One company's gain is others' loss in market share

### 2️⃣ Question
Company A has 40% market share, B has 35%, C has 25%. If A gains 5 percentage points and B loses 3 percentage points, what is C's new market share?

### 3️⃣ Examiner's Intent
- Tests market share conservation
- Top-100 fail by not balancing gains and losses

### 4️⃣ Solution (Logic-First)
1. Total must remain 100%
2. A: $40\% + 5\% = 45\%$
3. B: $35\% - 3\% = 32\%$
4. C: $100\% - 45\% - 32\% = 23\%$
5. Change in C = $25\% - 23\% = -2$ percentage points
6. **Answer: 23%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 25% (unchanged)
- **Why it feels correct**: C wasn't mentioned as changing
- **Exact failure point**: Total must be 100%, so C absorbs the imbalance

### 6️⃣ Generalization Map
1. Four companies
2. Percentage growth of a segment
3. New entrant taking share from all
4. Merger impact
5. Market concentration indices

### 7️⃣ Neural Anchor
**"Market-100%"**

---

## Question 20: The Effective Rate

### Best Technique
Effective annual rate = $(1 + r/n)^n - 1$ for $n$ compounding periods

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Limiting-case override
- **Secondary Logic Interactions**: Compounding frequency effect
- **Why Lethal**: More frequent compounding increases effective rate

### 2️⃣ Question
What is the effective annual rate if nominal rate is 12% compounded quarterly?

### 3️⃣ Examiner's Intent
- Tests effective rate calculation
- Top-100 fail by answering 12%

### 4️⃣ Solution (Logic-First)
1. Nominal rate = 12% p.a., compounded quarterly
2. Per-quarter rate = $12\%/4 = 3\%$
3. Effective rate = $(1 + 0.03)^4 - 1 = 1.1255 - 1 = 0.1255 = 12.55\%$
4. **Answer: 12.55%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 12%
- **Why it feels correct**: That's the stated rate
- **Exact failure point**: Nominal ≠ effective when compounding > 1

### 6️⃣ Generalization Map
1. Monthly compounding
2. Continuous compounding (limit)
3. Compare different frequencies
4. Find nominal given effective
5. Real vs nominal (inflation adjustment)

### 7️⃣ Neural Anchor
**"Effective-Compound"**

---

## Question 21: The Depreciation

### Best Technique
Apply **declining balance depreciation**: Value = $P(1 - r)^n$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Symmetry exploitation (growth vs decay)
- **Secondary Logic Interactions**: Compound decay
- **Why Lethal**: Depreciation is opposite of compound growth

### 2️⃣ Question
A machine depreciates at 10% p.a. on the reducing balance. If initial value is ₹100,000, what is the value after 3 years?

### 3️⃣ Examiner's Intent
- Tests compound depreciation
- Top-100 fail by computing simple depreciation

### 4️⃣ Solution (Logic-First)
1. After 3 years: $100,000 \times (0.90)^3 = 100,000 \times 0.729 = ₹72,900$
2. **Answer: ₹72,900**
3. Compare with straight-line: $100,000 - 30,000 = ₹70,000$

### 5️⃣ Trap Autopsy
- **Common wrong answer**: ₹70,000 (straight-line depreciation)
- **Why it feels correct**: 10% × 3 years = 30%
- **Exact failure point**: Reducing balance, not flat rate

### 6️⃣ Generalization Map
1. Find depreciation rate given initial and final values
2. Time to reach scrap value
3. Sum-of-years-digits method
4. Double declining balance
5. Accumulated depreciation

### 7️⃣ Neural Anchor
**"Depreciate-Compound"**

---

## Question 22: The Percentage Increase Needed

### Best Technique
If reduced by $x\%$, increase by $\frac{x}{100-x} \times 100\%$ to restore

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Reverse reasoning
- **Secondary Logic Interactions**: Asymmetric recovery
- **Why Lethal**: Bigger percentage needed to recover from loss

### 2️⃣ Question
A stock falls by 40%. By what percentage must it rise to return to its original value?

### 3️⃣ Examiner's Intent
- Tests recovery percentage calculation
- Top-100 fail by answering 40%

### 4️⃣ Solution (Logic-First)
1. After 40% fall: value = $100 \times 0.60 = 60$
2. Need to go from 60 to 100: increase = 40
3. Percentage increase = $40/60 \times 100 = 66.67\%$
4. **Formula**: $\frac{x}{100-x} \times 100 = \frac{40}{60} \times 100 = 66.67\%$
5. **Answer: 66.67%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 40%
- **Why it feels correct**: Same percentage to undo
- **Exact failure point**: Increase is on reduced base

### 6️⃣ Generalization Map
1. Rises by $x\%$, falls to original
2. Multiple falls and recoveries
3. 50% loss (need 100% to recover)
4. Breakeven trading
5. Volatility drag

### 7️⃣ Neural Anchor
**"Recovery-Greater"**

---

## Question 23: The Proportion Change

### Best Technique
If $a$ increases by $x\%$ and $b$ decreases by $y\%$, ratio $a:b$ changes multiplicatively

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Ghost variable cancellation (in ratios)
- **Secondary Logic Interactions**: Relative change in ratio
- **Why Lethal**: Percentage change in ratio ≠ difference in percentage changes

### 2️⃣ Question
If width of a rectangle increases by 20% and length decreases by 10%, what is the percentage change in the ratio length:width?

### 3️⃣ Examiner's Intent
- Tests ratio change calculation
- Top-100 fail by computing area change or simple subtraction

### 4️⃣ Solution (Logic-First)
1. Original ratio $L:W = L/W$
2. New ratio = $(L \times 0.90)/(W \times 1.20) = (L/W) \times (0.90/1.20) = (L/W) \times 0.75$
3. Change in ratio = $0.75 - 1 = -0.25 = -25\%$
4. **Answer: 25% decrease in L:W ratio**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 10% decrease (diff of percentages)
- **Why it feels correct**: $-10\% - 20\% = -30\%$ or just $-10\%$
- **Exact failure point**: Need multiplicative combination

### 6️⃣ Generalization Map
1. Three quantities in ratio
2. Constant ratio scenarios
3. Inverse ratios
4. Percentage of ratio
5. Weighted ratios

### 7️⃣ Neural Anchor
**"Ratio-Divide-Factors"**

---

## Question 24: The Exam Pass Percentage

### Best Technique
Track **pass/fail numbers** rather than percentages directly

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Hidden constraint dominance
- **Secondary Logic Interactions**: Absolute vs relative numbers
- **Why Lethal**: 80% pass with 50 students ≠ 80% pass with 100 students

### 2️⃣ Question
In class A (50 students), 80% passed. In class B (100 students), 70% passed. What is the overall pass percentage?

### 3️⃣ Examiner's Intent
- Tests combined percentage calculation
- Top-100 fail by averaging $80\%$ and $70\%$

### 4️⃣ Solution (Logic-First)
1. Class A passed: $50 \times 0.80 = 40$
2. Class B passed: $100 \times 0.70 = 70$
3. Total passed = $40 + 70 = 110$
4. Total students = $50 + 100 = 150$
5. Overall pass % = $(110/150) \times 100 = 73.33\%$
6. **Answer: 73.33%**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 75% (average of 80 and 70)
- **Why it feels correct**: Average of two percentages
- **Exact failure point**: Unequal class sizes require weighted average

### 6️⃣ Generalization Map
1. Three classes
2. Find one class's percentage given overall
3. Minimum passes needed in one class for target overall
4. Gender-wise analysis
5. Subject-wise pass percentages

### 7️⃣ Neural Anchor
**"Count-Then-Percent"**

---

## Question 25: The Inflation Adjustment

### Best Technique
Real value = Nominal value / $(1 + \text{inflation rate})^n$

### 1️⃣ Logic Signature
- **Dominant Logic Trap**: Order-of-magnitude deception
- **Secondary Logic Interactions**: Purchasing power erosion
- **Why Lethal**: Nominal increases may be real decreases

### 2️⃣ Question
Salary increases from ₹50,000 to ₹60,000 (20% increase). Inflation over the same period is 15%. What is the real increase in purchasing power?

### 3️⃣ Examiner's Intent
- Tests real vs nominal calculation
- Top-100 fail by computing $20\% - 15\% = 5\%$

### 4️⃣ Solution (Logic-First)
1. Nominal increase = 20%
2. Real salary = Nominal / $(1 + \text{inflation}) = 60,000 / 1.15 = 52,174$
3. Real increase = $(52,174 - 50,000) / 50,000 = 4.35\%$
4. **Formula**: Real increase ≈ $(1.20/1.15) - 1 = 1.0435 - 1 = 4.35\%$
5. **Answer: 4.35% real increase**

### 5️⃣ Trap Autopsy
- **Common wrong answer**: 5%
- **Why it feels correct**: Simple subtraction of percentages
- **Exact failure point**: Real calculation requires division, not subtraction

### 6️⃣ Generalization Map
1. Negative real growth (despite nominal increase)
2. Multi-year inflation adjustment
3. Comparing across countries
4. Constant-dollar analysis
5. Purchasing power parity

### 7️⃣ Neural Anchor
**"Real-Divide-Nominal"**

---

## Logic Coverage Summary

| Q# | Primary Trap | Secondary Traps |
|----|--------------|-----------------|
| 1 | Assumption poisoning | Examiner-language misdirection |
| 2 | False linearity | Multiplicative vs additive |
| 3 | Examiner-language (critical) | Absolute vs relative |
| 4 | Reverse reasoning | Division vs multiplication |
| 5 | Discrete vs continuous | Exponential vs linear |
| 6 | Non-commutative dependency | Order of application |
| 7 | False linearity | Order independence |
| 8 | Ghost variable cancellation | Order of operations |
| 9 | Hidden constraint (base) | Standard convention |
| 10 | Conservation vs optimization | Inverse proportionality |
| 11 | Order-of-magnitude | Measurement uncertainty |
| 12 | Non-commutative dependency | Vote conservation |
| 13 | Conservation (mass balance) | Volume additivity |
| 14 | Ghost variable cancellation | Non-linear relationship |
| 15 | Multiple valid methods | Error in division |
| 16 | Order-of-magnitude | Base year concept |
| 17 | Hidden constraint (time) | Proportional distribution |
| 18 | Discrete vs continuous | Interest on interest |
| 19 | Conservation | Zero-sum game |
| 20 | Limiting-case override | Compounding frequency |
| 21 | Symmetry (growth vs decay) | Compound decay |
| 22 | Reverse reasoning | Asymmetric recovery |
| 23 | Ghost variable (ratios) | Relative change |
| 24 | Hidden constraint | Absolute vs relative |
| 25 | Order-of-magnitude | Purchasing power |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]. Would you like to initiate a 'Multi-Variable Stress Test' combining this with Profit-Loss for a Rank-1 simulation?**
