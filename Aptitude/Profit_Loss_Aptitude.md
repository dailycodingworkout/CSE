# Profit & Loss Aptitude | GATE ESE PSU

## The Atomic Truth: **Profit = Selling Price − Cost Price**

---

## 1. FOUNDATIONAL FRAMEWORK | The Root Architecture

### Core Formulas

$$\text{Profit} = SP - CP$$

$$\text{Loss} = CP - SP$$

$$\text{Profit \%} = \frac{SP - CP}{CP} \times 100$$

$$\text{Loss \%} = \frac{CP - SP}{CP} \times 100$$

$$SP = CP \times \left(1 + \frac{P\%}{100}\right) \quad \text{or} \quad SP = CP \times \left(1 - \frac{L\%}{100}\right)$$

### The Golden Pivot: **Cost Price is ALWAYS the Reference**

> **TRAP ALERT:** Many candidates calculate percentage on SP instead of CP. This is the #1 killer in competitive exams.

---

## 2. THE MENTAL SLIDER | Successive Profit/Loss

When goods pass through multiple stages:

$$\text{Net Effect} = a + b + \frac{ab}{100}$$

Where $a$ and $b$ are percentage changes (use negative for loss).

### Mental Machinery:
- Two successive gains of 10%: $10 + 10 + \frac{10 \times 10}{100} = 21\%$ gain
- Gain 20%, Loss 10%: $20 - 10 + \frac{20 \times (-10)}{100} = 10 - 2 = 8\%$ gain
- Gain 10%, Loss 10%: $10 - 10 + \frac{10 \times (-10)}{100} = -1\%$ → **ALWAYS A LOSS**

> **THE SYMMETRIC TRAP:** Equal gain and loss percentage NEVER results in zero effect. It's always a loss of $\left(\frac{x}{10}\right)^2 \%$

---

## 3. MARKED PRICE & DISCOUNT | The Triple Variable System

$$MP \xrightarrow{\text{Discount}} SP \xrightarrow{\text{Profit/Loss}} CP$$

$$SP = MP \times \left(1 - \frac{D\%}{100}\right)$$

$$\text{Profit \%} = \frac{MP(1 - D\%) - CP}{CP} \times 100$$

### The Relationship Lock:

$$\frac{MP}{CP} = \frac{100 + P\%}{100 - D\%}$$

---

## 4. FALSE WEIGHT DECEPTION | The Criminal Arithmetic

When shopkeeper uses false weight:

$$\text{Gain \%} = \frac{\text{Weight Deficit}}{\text{Actual Weight Given}} \times 100$$

$$\text{Gain \%} = \frac{\text{Claimed Weight} - \text{Actual Weight Given}}{\text{Actual Weight Given}} \times 100$$

### Mental Model:
- Claims 1 kg, gives 900g: Weight Deficit = 1000g - 900g = 100g
  - Gain = $\frac{100}{900} \times 100 = 11.11\%$
- **WITH additional markup of $x\%$:** Use successive formula

---

## 5. COST PRICE EQUIVALENCE | The Hidden Variable Trap

When CP is embedded in problem structure:

**Type 1:** SP of $m$ articles = CP of $n$ articles
$$\text{Profit \%} = \frac{n - m}{m} \times 100$$

**Type 2:** By selling at two different prices  
When selling same article at $SP_1$ with $P_1\%$ profit and $SP_2$ with $P_2\%$ loss:
$$CP = \frac{SP_1 \times P_2 + SP_2 \times P_1}{P_1 + P_2}$$
*(Note: Use absolute values of percentages; this formula applies when one transaction is profit and one is loss)*

---

# ADVERSARIAL VAULT | Maximum Difficulty Questions

---

## Q1. THE SUCCESSIVE TRANSFER TRAP (NAT)

**A trader marks his goods 40% above cost price and gives successive discounts of 10% and 15%. He also uses a faulty balance that weighs 900g instead of 1 kg. What is his overall profit percentage? (Round to 2 decimal places)**

### The Anti-Solution (How Top Students Fail):
1. Calculate discount effect: $10 + 15 + \frac{10 \times 15}{100} = 23.5\%$
2. Apply to marked price: Net SP factor = $1.4 \times 0.765 = 1.071$
3. **STOP HERE** — Most forget the false weight gain!

### The Sovereign Solution:

**Step 1:** Marked Price Effect
- MP = 1.4 × CP
- After successive discounts: $SP = MP \times 0.9 \times 0.85 = 1.4 \times 0.765 = 1.071 \times CP$
- Apparent profit on honest scale = 7.1%

**Step 2:** False Weight Gain
- Gain from false weight = $\frac{100}{900} \times 100 = 11.11\%$

**Step 3:** Net Effect (Successive Gains)
$$\text{Net} = 7.1 + 11.11 + \frac{7.1 \times 11.11}{100}$$
$$= 18.21 + 0.789 = 19.00\%$$

**Answer: 19.00%**

> **5-Second Snap-Check:** False weight alone gives ~11%, markup after discount gives ~7%, combined must be ~19% (not simple sum 18%).

---

## Q2. THE SYMMETRIC LOSS PARADOX (MSQ)

**A person sells two articles at the same selling price of ₹9900 each. On one, he gains 10% and on the other, he loses 10%. Which of the following statements are TRUE?**

(A) There is an overall loss  
(B) Overall profit/loss percentage is 1%  
(C) Total CP > Total SP  
(D) Loss amount is ₹200

### The Trap:
Students assume: Same SP, opposite percentages → No net effect. **WRONG.**

### The Sovereign Solution:

**Article 1 (10% Gain):**
$$CP_1 = \frac{9900}{1.10} = ₹9000$$

**Article 2 (10% Loss):**
$$CP_2 = \frac{9900}{0.90} = ₹11000$$

**Total CP** = ₹20000  
**Total SP** = ₹19800  
**Loss** = ₹200  
**Loss %** = $\frac{200}{20000} \times 100 = 1\%$

**Correct Options: (A), (B), (C), (D) — ALL TRUE**

> **The Universal Law:** When same SP with $x\%$ gain and $x\%$ loss, there is ALWAYS a loss of $\left(\frac{x}{10}\right)^2 \%$
>
> Verification: $(10/10)^2 = 1\%$ ✓

---

## Q3. THE COMPOUND MARKUP DECEPTION (NAT)

**A shopkeeper marks his goods such that after allowing 20% discount, he still earns 20% profit. By what percentage did he mark the goods above the cost price?**

### The Mental Machinery:

Let $CP = 100$

Required: $SP = 120$ (for 20% profit)

Given: $SP = MP \times 0.80$

$$120 = MP \times 0.80$$
$$MP = 150$$

**Markup = 50%**

### Alternative (Formula Route):
$$\frac{MP}{CP} = \frac{100 + P\%}{100 - D\%} = \frac{120}{80} = 1.5$$

**Answer: 50**

---

## Q4. THE FRACTIONAL PARTS NIGHTMARE (NAT)

**A man bought an article and sold $\frac{1}{4}$ of it at 20% loss, $\frac{1}{2}$ at 25% profit, and the remaining at cost price. Find his overall profit percentage.**

### The Sovereign Solution:

Let $CP = 100$ units

| Part | Fraction | CP Share | Profit/Loss | SP |
|------|----------|----------|-------------|-----|
| 1st | 1/4 | 25 | -20% | 20 |
| 2nd | 1/2 | 50 | +25% | 62.5 |
| 3rd | 1/4 | 25 | 0% | 25 |
| **Total** | | **100** | | **107.5** |

**Profit = 7.5%**

> **Shortcut:** Weighted average of profits
> $$\frac{1}{4}(-20) + \frac{1}{2}(25) + \frac{1}{4}(0) = -5 + 12.5 + 0 = 7.5\%$$

---

## Q5. THE DUAL TRANSACTION INVERSE (NAT)

**A dealer sells an article at 10% profit. Had he bought it for 20% less and sold it for ₹100 more, he would have gained 40%. Find the original cost price.**

### The Setup:

Let original $CP = x$

**Transaction 1:** $SP_1 = 1.10x$

**Transaction 2:**
- New CP = $0.80x$
- New SP = $1.10x + 100$
- Gain = 40%

$$1.10x + 100 = 0.80x \times 1.40$$
$$1.10x + 100 = 1.12x$$
$$100 = 0.02x$$
$$x = ₹5000$$

**Answer: ₹5000**

> **5-Second Snap-Check:** Verify: New CP = ₹4000, New SP = ₹5600, Gain = ₹1600 = 40% of ₹4000 ✓

---

## Q6. THE WEIGHTED PARTNERSHIP (NAT)

**Three partners A, B, C invest in ratio 2:3:5 for time periods in ratio 4:6:5. The business earns 20% profit on total investment. If B's share of profit is ₹5400, find the total investment.**

### The Sovereign Solution:

**Investment × Time Ratio:**
$$A : B : C = (2 \times 4) : (3 \times 6) : (5 \times 5) = 8 : 18 : 25$$

**Total Ratio Units = 51**

B's share ratio = 18/51 of total profit

Let Total Investment = $I$  
Total Profit = $0.20I$

$$B's\ share = \frac{18}{51} \times 0.20I = 5400$$
$$\frac{3.6I}{51} = 5400$$
$$I = \frac{5400 \times 51}{3.6} = \frac{275400}{3.6} = ₹76500$$

**Answer: ₹76500**

---

## Q7. THE BREAK-EVEN REVERSAL (NAT)

**A man sells 20 articles at the cost price of 25 articles. If he had sold 25 articles at SP of 24 articles (current SP), what would be his profit percentage?**

### Step 1: Find Current Profit %

SP of 20 = CP of 25

Let CP of 1 article = ₹1  
Then: $20 \times SP = 25$  
$SP = 1.25$

Current profit = 25%

### Step 2: New Scenario

Sells 25 articles at current SP (1.25 each) but only charges for 24 articles:
$$\text{Revenue} = 24 \times 1.25 = 30$$
$$\text{Cost} = 25 \times 1 = 25$$
$$\text{Profit \%} = \frac{30 - 25}{25} \times 100 = 20\%$$

**Answer: 20%**

---

## Q8. THE BROKERAGE CHAIN (NAT)

**A manufacturer sells goods to wholesaler at 20% profit, wholesaler to retailer at 15% profit, and retailer to customer at 25% profit. If customer pays ₹6900, find manufacturer's cost price.**

### The Cascade:

$$\text{Customer Price} = CP_M \times 1.20 \times 1.15 \times 1.25$$
$$6900 = CP_M \times 1.725$$
$$CP_M = \frac{6900}{1.725} = ₹4000$$

**Answer: ₹4000**

> **Shortcut for successive multiplications:**
> $1.20 \times 1.15 = 1.38$, then $1.38 \times 1.25 = 1.725$

---

## Q9. THE DUAL PERCENTAGE ANCHOR (MSQ)

**If the cost price is 80% of the selling price, which of the following are TRUE?**

(A) Profit percentage is 25%  
(B) Selling price is 125% of cost price  
(C) If a 10% discount is given, profit becomes 12.5%  
(D) Markup percentage equals profit percentage  

### The Sovereign Solution:

Given: $CP = 0.80 \times SP$  
Therefore: $SP = 1.25 \times CP$

**Option (A):** Profit % = $\frac{SP - CP}{CP} \times 100 = \frac{0.25CP}{CP} \times 100 = 25\%$ ✓

**Option (B):** $SP = 1.25 \times CP$ = 125% of CP ✓

**Option (C):** After 10% discount:  
New SP = $0.90 \times 1.25 \times CP = 1.125 \times CP$  
New Profit = 12.5% ✓

**Option (D):** Markup % = Profit % = 25% (only when no discount) ✓

**All options (A), (B), (C), (D) are TRUE**

---

## Q10. THE ABSOLUTE-PERCENTAGE BRIDGE (NAT)

**By selling 45 lemons, a vendor gains the selling price of 15 lemons. Find his gain percentage.**

### The Trap:
Students calculate: Gain = 15/45 = 33.33% **WRONG!**

### The Sovereign Solution:

Let SP of 1 lemon = ₹1

- Revenue from 45 lemons = ₹45
- Profit = SP of 15 = ₹15
- Therefore: CP of 45 = 45 - 15 = ₹30

$$\text{Profit \%} = \frac{15}{30} \times 100 = 50\%$$

**Answer: 50%**

> **The Mental Slider:** Profit is always on CP, not SP. When profit equals SP of some items, first find CP, then calculate percentage.

---

## Q11. THE EXCHANGE RATE TRAP (NAT)

**A trader buys goods at 6% less than listed price. He marks them 15% above listed price and gives 10% discount. Find his profit percentage. (Round to 2 decimal places)**

### Variable Assignment:

Let Listed Price = ₹100

- CP = ₹94 (6% less than LP)
- MP = ₹115 (15% above LP)
- SP = ₹115 × 0.90 = ₹103.50

$$\text{Profit \%} = \frac{103.50 - 94}{94} \times 100 = \frac{9.50}{94} \times 100 = 10.11\%$$

**Answer: 10.11%**

---

## Q12. THE PARTNERSHIP DISSOLUTION (NAT)

**A and B start a business. A invests ₹50,000 for the whole year. B invests ₹30,000 for 4 months and withdraws. C joins after 4 months with ₹40,000. If total profit is ₹18,500, find C's share.**

### Investment-Month Calculation:

| Partner | Investment | Months | Product |
|---------|------------|--------|---------|
| A | 50,000 | 12 | 600,000 |
| B | 30,000 | 4 | 120,000 |
| C | 40,000 | 8 | 320,000 |
| **Total** | | | **1,040,000** |

C's ratio = 320,000 / 1,040,000 = 32/104 = 8/26 = 4/13

$$C's\ share = \frac{4}{13} \times 18500 = \frac{74000}{13} = ₹5692.31$$

**Answer: ₹5692.31** (or ₹5692 if rounding to nearest rupee)

---

## Q13. THE COMPOUND DISHONESTY (NAT)

**A dishonest shopkeeper uses a weight that is 15% less while buying and 10% less while selling. He also marks up by 20% and claims to sell at cost price. What is his actual profit percentage?**

### The Triple Deception:

**While Buying (15% less weight means actual weight is 85% of claimed):**
- Pays for 1 kg, receives goods worth 1 kg but the weight reads 15% less
- Interpretation: Shopkeeper gets 1 kg worth of goods while the seller thinks they're giving only 0.85 kg worth
- Effective gain = $\frac{15}{85} \times 100 = 17.65\%$

**While Selling (10% less weight):**
- Charges for 1 kg, gives 0.90 kg
- Gain = $\frac{10}{90} \times 100 = 11.11\%$

**Markup Claim:**
- Claims to sell at cost price but has 20% hidden markup
- Interpretation: The "claimed CP" shown to customer = 1.20 × Actual CP

### Simplified Model:

Let true market CP = ₹100/kg

**Step 1 - Buying Gain (17.65%):** Pays ₹85 but gets ₹100 worth  
Effective CP = ₹85 per kg of goods

**Step 2 - Markup Claim (20%):** Sells at ₹120 (claims this is CP)

**Step 3 - Selling Gain (11.11%):** Gives 900g for price of 1 kg at ₹120
- Receives: ₹120 for 0.9 kg delivered
- Per kg equivalent: ₹133.33

**Net Profit Calculation:**
- CP per kg = ₹85
- SP per kg (effective) = ₹133.33

$$\text{Profit \%} = \frac{133.33 - 85}{85} \times 100 = 56.86\%$$

### Alternative via successive formula:

- Buying gain: $17.65\%$
- Markup gain: $20\%$
- Selling gain: $11.11\%$

Successive: $(1.1765 \times 1.20 \times 1.1111) - 1 = 1.568 - 1 = 56.8\%$

**Answer: 56.86%**

---

## Q14. THE TIME-VARIANT SALE (NAT)

**A shopkeeper buys 80 kg of rice at ₹40/kg. He sells 60% at 20% profit and remaining 40% at a loss. If overall profit is 8%, find the loss percentage on remaining 40%.**

### Setup:

Total CP = 80 × 40 = ₹3200

Overall profit = 8% → Total SP = ₹3456

**On 60% (48 kg):**
- CP = ₹1920
- Profit = 20% → SP = ₹2304

**On 40% (32 kg):**
- CP = ₹1280
- SP = 3456 - 2304 = ₹1152
- Loss = 1280 - 1152 = ₹128
- Loss % = $\frac{128}{1280} \times 100 = 10\%$

**Answer: 10%**

---

## Q15. THE REVERSAL PROFIT (NAT)

**A man sold two cows for ₹12,000 each. On one, he gained 20% and on other, he lost 20%. Find his overall loss percentage.**

### Using the Universal Law:

Same SP, opposite percentages at $x\%$:

$$\text{Loss \%} = \left(\frac{x}{10}\right)^2 = \left(\frac{20}{10}\right)^2 = 4\%$$

### Verification:

CP₁ = 12000/1.20 = ₹10,000  
CP₂ = 12000/0.80 = ₹15,000  
Total CP = ₹25,000  
Total SP = ₹24,000  
Loss = ₹1000  
Loss % = 4%

**Answer: 4%**

---

# TRAP ENCYCLOPEDIA | Common Pitfalls

## Trap 1: Percentage Base Confusion
- Profit/Loss % is ALWAYS on CP
- Discount % is ALWAYS on MP
- Never calculate profit on SP

## Trap 2: The Symmetric Illusion
- Equal profit and loss percentages on different bases ≠ zero
- $x\%$ profit + $x\%$ loss (same SP) = Loss of $(x/10)^2 \%$

## Trap 3: False Weight Double Count
- Buying gain and selling gain are DIFFERENT
- Must apply successive percentage formula

## Trap 4: MP ≠ SP
- Marked Price is reference for discount
- Selling Price is after discount
- Don't conflate the two

## Trap 5: Time Factor in Partnership
- Investment × Time = Effective Investment
- Different joining/exit dates change everything

## Trap 6: The "Less" vs "More" Ambiguity
- "20% less than CP" vs "20% of CP" — read carefully
- "Sold at 20% less" means SP = 0.80 × original SP

## Trap 7: Fractional Quantity Distribution
- When selling portions at different rates, use weighted average
- Sum of fractions must equal 1

---

# THE 5-SECOND SNAP-CHECKS

| Scenario | Snap-Check |
|----------|------------|
| Same SP, $x\%$ gain/loss | Always loss of $(x/10)^2\%$ |
| Successive $a\%$, $b\%$ | Use $a + b + ab/100$ |
| False weight of $y$g | Gain = $(1000-y)/y × 100\%$ |
| Discount $d\%$, Profit $p\%$ | $MP/CP = (100+p)/(100-d)$ |
| SP of $m$ = CP of $n$ | Profit = $(n-m)/m × 100\%$ |

---

# THE BIZARRE MNEMONICS

## 1. "CP is the KING, SP is the QUEEN"
All percentages bow to the King (CP). The Queen (SP) only matters for discount calculation when she becomes MP.

## 2. "The Symmetric Serpent Always Bites"
When profit and loss percentages are equal mirrors, the serpent (loss) ALWAYS bites. Size of bite = $(x/10)^2$

## 3. "False Weight = Free Money, Then MORE Free Money"
Two separate crimes, two separate gains. Compound them with the successive formula.

## 4. "Partnership = Marriage × Time"
Money alone doesn't determine share. Time multiplies everything.

---

# PRECISION LOCKS FOR NAT

| Type | Precision Boundary |
|------|-------------------|
| Standard % | 2 decimal places |
| False weight | Watch for recurring decimals (11.11...) |
| Successive % | Keep intermediates unrounded |
| Partnership | May need ceiling/floor for whole shares |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]. Would you like to initiate a **'Multi-Variable Stress Test'** combining this with [Related Topics: Partnership, Simple/Compound Interest, Ratio-Proportion] for a Rank-1 simulation?**
