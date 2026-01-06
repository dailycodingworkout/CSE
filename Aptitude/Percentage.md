# Percentage - Supreme Logic Coverage Questions

> **Mission:** Total Logic Coverage with Minimum Questions  
> **Target:** GATE, ESE, PSU, and Banking Exams  
> **Philosophy:** Exhaust the logic-space, not the syllabus

---

## Question 1: The Base Shift Deception

### Best Technique
**Base Identification First:** Every percentage is relative to a base. When the base shifts mid-problem, the percentages are not directly comparable. Always identify the base before applying any percentage.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Assumption Poisoning
- **Secondary Logic Interactions:** Examiner-language misdirection, Non-commutative step dependency
- **Why Lethal:** "Increased by 20% then decreased by 20%" sounds like net zero change, but the bases differ.

### 2️⃣ Question
A price is increased by 25%, then decreased by 20%. What is the net percentage change in price?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you track base changes through successive percentage operations?
- **Why Top-100 Fail:** They compute $25 - 20 = 5\%$ increase.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Use multiplicative factors.

1. Let original price = 100 (choose convenient base)
2. After 25% increase: $100 \times 1.25 = 125$
3. After 20% decrease: $125 \times 0.80 = 100$
4. Net change: $100 - 100 = 0$

**Alternative (Factor method):**
$$\text{Net factor} = 1.25 \times 0.80 = 1.00$$
$$\text{Net change} = (1.00 - 1) \times 100\% = 0\%$$

**Answer: 0% (No change)**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 5% increase or 5% decrease
- **Why It Feels Correct:** Additive intuition: $+25 - 20 = +5$.
- **Exact Failure Point:** Not recognizing that the 20% is applied to 125, not 100.

### 6️⃣ Generalization Map
1. Different percentages (30% up, 20% down)
2. Three or more successive changes
3. Find the percentage decrease needed to restore original
4. Compound interest vs simple interest analogy
5. Price and quantity changes in revenue

### 7️⃣ Neural Anchor
**"Multiply-Not-Add"**

---

## Question 2: The Percentage Point Confusion

### Best Technique
**Absolute vs Relative Change:** "Increased from 40% to 50%" can be reported as 10 percentage points (absolute) or 25% (relative). Know which is being asked.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Examiner-language misdirection
- **Secondary Logic Interactions:** Dimensional contradiction, Order-of-magnitude deception
- **Why Lethal:** The phrases "increased by 25%" and "increased by 25 percentage points" mean completely different things.

### 2️⃣ Question
The pass rate in an exam increased from 60% to 75%. What is the percentage increase in the pass rate?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you distinguish between "percentage point change" and "percentage change of percentage"?
- **Why Top-100 Fail:** They answer 15% (the point difference) instead of computing relative increase.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** "Percentage increase" means relative change.

1. Original pass rate: 60%
2. New pass rate: 75%
3. Change: $75 - 60 = 15$ percentage points (absolute)
4. Percentage increase: $\frac{15}{60} \times 100\% = 25\%$

**Answer: 25%**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 15%
- **Why It Feels Correct:** The numbers 75 and 60 are percentages, and their difference is 15.
- **Exact Failure Point:** Not applying the percentage change formula to the original value.

### 6️⃣ Generalization Map
1. Rate decreased (e.g., 40% to 30%)
2. "By what percentage points" explicitly asked
3. Multiple metrics changing simultaneously
4. Year-over-year comparisons
5. Compound changes in rates

### 7️⃣ Neural Anchor
**"Points-vs-Percent"**

---

## Question 3: The Reverse Percentage Trap

### Best Technique
**Inverse Operation Awareness:** If something is "20% less than X," then X is NOT "20% more than something." The percentages are calculated on different bases.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Reverse reasoning (answer → question)
- **Secondary Logic Interactions:** False linearity assumption, Symmetry/invariance exploitation
- **Why Lethal:** Inverse relationships are asymmetric. Students assume if A is 20% more than B, then B is 20% less than A.

### 2️⃣ Question
If A is 25% more than B, then B is what percent less than A?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you correctly compute the inverse percentage relationship?
- **Why Top-100 Fail:** They answer 25% without recalculating the base.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Set up the relationship and solve for the reverse.

1. Let $B = 100$ (convenient base)
2. $A = B + 25\% \text{ of } B = 100 + 25 = 125$
3. Now: B is how much less than A?
4. Difference: $A - B = 125 - 100 = 25$
5. Percentage: $\frac{25}{125} \times 100\% = 20\%$

**Answer: 20%**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 25%
- **Why It Feels Correct:** "25% more" should reverse to "25% less."
- **Exact Failure Point:** The base for "less than A" is A = 125, not B = 100.

### 6️⃣ Generalization Map
1. Different percentages (33⅓% more → 25% less)
2. Chain of comparisons (A > B > C)
3. "20% of A is 25% of B, find relation"
4. Iterative percentage changes
5. Geometric interpretation

### 7️⃣ Neural Anchor
**"Base-Shifts-In-Reverse"**

---

## Question 4: The Expenditure Illusion

### Best Technique
**Two-Variable Product Analysis:** When expenditure = price × quantity, a percentage change in one affects total expenditure differently depending on what stays constant.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Hidden constraint dominance
- **Secondary Logic Interactions:** Conservation vs optimization conflict, Ghost variable cancellation
- **Why Lethal:** Students forget to specify whether price, quantity, or expenditure is held constant.

### 2️⃣ Question
If the price of a commodity increases by 40%, by how much percent must a consumer reduce consumption so that expenditure increases by only 12%?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you set up the product equation with three unknowns and one constraint?
- **Why Top-100 Fail:** They use wrong formulas or don't correctly interpret "increases by only 12%."

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Set up product relationship with percentage changes.

1. Let original: Price = $P$, Quantity = $Q$, Expenditure = $E = PQ$
2. New price: $P' = 1.40P$
3. New expenditure: $E' = 1.12E = 1.12PQ$
4. Let new quantity: $Q' = Q \times (1 - r)$ where $r$ is reduction fraction
5. $P' \times Q' = E'$
6. $1.40P \times Q(1 - r) = 1.12PQ$
7. $1.40(1 - r) = 1.12$
8. $1 - r = \frac{1.12}{1.40} = 0.8$
9. $r = 0.2 = 20\%$

**Answer: 20%**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 28% (from $40 - 12$) or 40%
- **Why It Feels Correct:** Subtractive intuition seems simpler.
- **Exact Failure Point:** Not setting up the multiplicative relationship correctly.

### 6️⃣ Generalization Map
1. Expenditure must stay same (12% becomes 0%)
2. Expenditure must decrease by some percentage
3. Both price and quantity change by known amounts
4. Three commodities with budget constraint
5. Tax included in price

### 7️⃣ Neural Anchor
**"Product-Percentage-Split"**

---

## Question 5: The Population Growth Paradox

### Best Technique
**Compound Growth Recognition:** Repeated percentage changes compound. For small percentages over many periods, approximate or use exact compound formulas.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Order-of-magnitude deception
- **Secondary Logic Interactions:** Discrete vs continuous trap, Limiting-case override
- **Why Lethal:** Students use simple interest mentality for compound growth, severely underestimating long-term effects.

### 2️⃣ Question
A population grows at 10% per year. In how many years will it double? (Use $\log 2 = 0.301$, $\log 1.1 = 0.0414$)

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you set up and solve the compound growth equation?
- **Why Top-100 Fail:** They compute $100\% / 10\% = 10$ years (simple growth).

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Use compound growth formula.

1. Let initial population = $P_0$
2. After $n$ years: $P_n = P_0 \times (1.1)^n$
3. Doubling condition: $P_n = 2P_0$
4. $(1.1)^n = 2$
5. $n \log(1.1) = \log 2$
6. $n = \frac{\log 2}{\log 1.1} = \frac{0.301}{0.0414} \approx 7.27$
7. Since we need whole years to double: approximately 7-8 years

**Answer: Approximately 7.27 years (or 8 years for complete doubling)**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 10 years
- **Why It Feels Correct:** 10% per year × 10 years = 100% growth = doubling.
- **Exact Failure Point:** Simple vs compound growth confusion.

### 6️⃣ Generalization Map
1. Different growth rates (5%, 15%)
2. Decay instead of growth
3. Tripling instead of doubling
4. Half-life problems (radioactive decay)
5. Rule of 72 estimation

### 7️⃣ Neural Anchor
**"Compound-Not-Simple"**

---

## Question 6: The Markup-Discount Chain

### Best Technique
**Sequential Multiplier Composition:** When multiple markups and discounts are applied, multiply the factors. The order can matter when different bases are used.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Non-commutative step dependency
- **Secondary Logic Interactions:** Local correctness global failure, Multiple valid methods — only one legal
- **Why Lethal:** "Markup on cost" and "discount on marked price" use different bases, making the chain non-obvious.

### 2️⃣ Question
A shopkeeper marks goods 40% above cost price and offers a 25% discount. What is the profit percentage?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you track through cost → marked → selling correctly?
- **Why Top-100 Fail:** They compute $40 - 25 = 15\%$ profit.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Track each price step explicitly.

1. Let Cost Price (CP) = 100
2. Marked Price (MP) = CP + 40% of CP = $100 \times 1.40 = 140$
3. Selling Price (SP) = MP − 25% of MP = $140 \times 0.75 = 105$
4. Profit = SP − CP = $105 - 100 = 5$
5. Profit % = $\frac{5}{100} \times 100\% = 5\%$

**Answer: 5%**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 15% (from $40 - 25$)
- **Why It Feels Correct:** Markup minus discount seems like net profit.
- **Exact Failure Point:** The discount is on the marked price, not the cost price.

### 6️⃣ Generalization Map
1. Two successive discounts
2. Markup on SP instead of CP
3. Find required markup for given profit after discount
4. Include tax (GST) in the chain
5. Wholesale and retail markups

### 7️⃣ Neural Anchor
**"Track-Every-Base"**

---

## Question 7: The Election Percentage Puzzle

### Best Technique
**Total vs Part Percentage Resolution:** When percentages of a whole must sum correctly, set up equations ensuring all parts are accounted for.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Ghost variable cancellation
- **Secondary Logic Interactions:** Boundary-condition collapse, Missing data illusion
- **Why Lethal:** Invalid votes, abstentions, or multi-candidate splits create hidden constraints students miss.

### 2️⃣ Question
In an election between two candidates, 10% of votes were invalid. The winning candidate got 54% of valid votes and won by 4800 votes. How many people voted?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you correctly parse "54% of valid votes" vs "54% of total votes"?
- **Why Top-100 Fail:** They apply 54% to total votes, not valid votes.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Define total and valid votes separately.

1. Let total votes = $T$
2. Invalid = 10% of $T$ = $0.10T$
3. Valid = 90% of $T$ = $0.90T$
4. Winner gets 54% of valid = $0.54 \times 0.90T = 0.486T$
5. Loser gets 46% of valid = $0.46 \times 0.90T = 0.414T$
6. Margin = $0.486T - 0.414T = 0.072T$
7. $0.072T = 4800$
8. $T = \frac{4800}{0.072} = \frac{4800 \times 1000}{72} = \frac{4800000}{72} = 66666.\overline{6}$
9. Expressing as a fraction: $T = \frac{200000}{3}$
10. In practical terms, if the question expects integer total votes, round to **66,667**

**Note:** The non-integer result indicates this is a constructed problem where the margin and percentages don't yield a whole number. The mathematical answer is $\frac{200000}{3} \approx 66667$.

**Answer: 66,667 (or exactly $\frac{200000}{3}$)**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 60,000 (from applying 54% to total directly)
- **Why It Feels Correct:** "Won by 54% vs 46%" applied to total is simpler.
- **Exact Failure Point:** Not accounting for the 10% invalid votes affecting the base.

### 6️⃣ Generalization Map
1. Three candidates with vote splits
2. Different invalid percentages
3. Threshold requirements (e.g., must exceed 50% of total)
4. Minimum vote count constraints
5. Regional voting with different turnouts

### 7️⃣ Neural Anchor
**"Valid-Base-First"**

---

## Summary: Logic Traps Covered

| Q# | Dominant Trap | Key Insight |
|----|---------------|-------------|
| 1 | Assumption Poisoning | Percentages multiply, not add |
| 2 | Examiner-language misdirection | Points vs percentage change |
| 3 | Reverse reasoning | Inverse percentages have different bases |
| 4 | Hidden constraint dominance | Price × Quantity = Expenditure relationship |
| 5 | Order-of-magnitude deception | Compound growth is exponential |
| 6 | Non-commutative step dependency | Markup on cost, discount on marked price |
| 7 | Ghost variable cancellation | Valid votes ≠ total votes |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
