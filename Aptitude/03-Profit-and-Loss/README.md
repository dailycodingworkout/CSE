# 💰 Profit and Loss | The Singularity

> **The Atomic Truth:** *Profit/Loss = Selling Price − Cost Price, expressed as percentage of CP.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Key Formulas](#key-formulas)
3. [Marked Price & Discount](#marked-price--discount)
4. [Dishonest Dealings](#dishonest-dealings)
5. [Partnership Problems](#partnership-problems)
6. [Special Cases](#special-cases)
7. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
8. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Profit & Loss Matters?
This topic tests your understanding of business mathematics—a skill valued in engineering management and real-world applications. It's frequently combined with:
- Percentages
- Ratio and Proportion
- Simple equations

### Basic Terminology

| Term | Symbol | Definition |
|------|--------|------------|
| **Cost Price (CP)** | CP | Price at which an article is purchased |
| **Selling Price (SP)** | SP | Price at which an article is sold |
| **Marked Price (MP)** | MP | Listed/Label price (before discount) |
| **Profit** | P | SP - CP (when SP > CP) |
| **Loss** | L | CP - SP (when CP > SP) |
| **Discount** | D | MP - SP |
| **Overhead Expenses** | OE | Additional costs (transport, tax, etc.) |

### The Fundamental Equation

$$\text{Effective CP} = \text{Actual CP} + \text{Overhead Expenses}$$

$$\text{Profit/Loss} = \text{SP} - \text{Effective CP}$$

---

## Key Formulas

### Profit and Loss Percentage

$$\text{Profit } \% = \frac{\text{Profit}}{\text{CP}} \times 100 = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100$$

$$\text{Loss } \% = \frac{\text{Loss}}{\text{CP}} \times 100 = \frac{\text{CP} - \text{SP}}{\text{CP}} \times 100$$

> **💡 The Golden Pivot:** Percentage is ALWAYS calculated on Cost Price!

### SP in terms of CP

$$\text{SP} = \text{CP} \times \left(1 + \frac{\text{Profit}\%}{100}\right)$$

$$\text{SP} = \text{CP} \times \left(1 - \frac{\text{Loss}\%}{100}\right)$$

### CP in terms of SP

$$\text{CP} = \frac{\text{SP} \times 100}{100 + \text{Profit}\%}$$

$$\text{CP} = \frac{\text{SP} \times 100}{100 - \text{Loss}\%}$$

### The Multiplier Method

| Scenario | Multiplier | Formula |
|----------|------------|---------|
| 20% Profit | 1.20 | SP = 1.20 × CP |
| 25% Profit | 1.25 | SP = 1.25 × CP |
| 10% Loss | 0.90 | SP = 0.90 × CP |
| 20% Loss | 0.80 | SP = 0.80 × CP |

---

## Marked Price & Discount

### The Price Chain

```
CP → MP → SP
(Cost) → (Marked/List) → (Selling)
     ↑                    ↓
  Markup              Discount
```

### Markup Formulas

$$\text{Markup} = \text{MP} - \text{CP}$$

$$\text{Markup } \% = \frac{\text{MP} - \text{CP}}{\text{CP}} \times 100$$

### Discount Formulas

$$\text{Discount} = \text{MP} - \text{SP}$$

$$\text{Discount } \% = \frac{\text{MP} - \text{SP}}{\text{MP}} \times 100$$

### The Grand Connection

$$\text{SP} = \text{MP} \times \left(1 - \frac{d}{100}\right)$$

$$\text{Profit } \% = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100 = \frac{\text{MP}(1-d/100) - \text{CP}}{\text{CP}} \times 100$$

### Successive Discounts

For discounts of $d_1\%$ and $d_2\%$ in succession:

$$\text{Single Equivalent Discount} = d_1 + d_2 - \frac{d_1 \times d_2}{100}$$

**Example:** Successive discounts of 20% and 10%
$$\text{Equivalent} = 20 + 10 - \frac{20 \times 10}{100} = 28\%$$

> **⚠️ Note:** Order of successive discounts doesn't matter!

### False Discount Scenario

If a trader marks up by $x\%$ and gives discount of $d\%$:

$$\text{Net Profit/Loss } \% = \left[\left(1 + \frac{x}{100}\right)\left(1 - \frac{d}{100}\right) - 1\right] \times 100$$

Or using shortcut:
$$\text{Net} \% = x - d - \frac{xd}{100}$$

---

## Dishonest Dealings

### Using False Weights

When a trader uses a faulty weight to cheat:

$$\text{Profit } \% = \frac{\text{True Weight} - \text{False Weight}}{\text{False Weight}} \times 100$$

Or equivalently:
$$\text{Profit } \% = \frac{\text{Error}}{\text{True Value} - \text{Error}} \times 100$$

**Example:** A trader uses 900g weight instead of 1kg
$$\text{Profit} = \frac{1000 - 900}{900} \times 100 = \frac{100}{900} \times 100 = 11.11\%$$

### Combined Cheating

If trader cheats both while buying (uses more weight) and selling (uses less weight):

$$\text{Profit } \% = \frac{\text{Weight used while buying}}{\text{Weight used while selling}} \times \left(1 + \frac{p\%}{100}\right) - 1$$

Where $p\%$ is any additional profit percentage.

---

## Partnership Problems

### Simple Partnership
When all partners invest for the **same duration**:

$$\frac{A's \text{ Share}}{B's \text{ Share}} = \frac{A's \text{ Investment}}{B's \text{ Investment}}$$

### Compound Partnership
When partners invest for **different durations**:

$$\frac{A's \text{ Share}}{B's \text{ Share}} = \frac{A's \text{ Investment} \times A's \text{ Time}}{B's \text{ Investment} \times B's \text{ Time}}$$

**Example:** A invests ₹5000 for 12 months, B invests ₹6000 for 10 months. Profit ratio?
$$\text{Ratio} = \frac{5000 \times 12}{6000 \times 10} = \frac{60000}{60000} = 1:1$$

### Working Partner Salary

If one partner also works (active partner):
1. Deduct the working partner's salary from total profit
2. Divide remaining profit in investment ratio

---

## Special Cases

### Case 1: Selling at Same Price with Profit and Loss

If two articles are sold at the **same SP**, one with $x\%$ profit and other with $x\%$ loss:

$$\text{Net Loss } \% = \frac{x^2}{100}\%$$

**Example:** Two articles sold at ₹100 each, one at 10% profit, other at 10% loss
$$\text{Net Loss} = \frac{10^2}{100} = 1\%$$

> **Why always loss?** The article with profit has lower CP, and article with loss has higher CP. You're losing more on the expensive one!

### Case 2: CP of x articles = SP of y articles

$$\text{Profit } \% = \frac{x - y}{y} \times 100$$

$$\text{Loss } \% = \frac{y - x}{y} \times 100 \text{ (when } y > x \text{)}$$

**Example:** CP of 20 articles = SP of 16 articles
$$\text{Profit} = \frac{20 - 16}{16} \times 100 = 25\%$$

### Case 3: Break-Even Point

$$\text{Break-Even} = \frac{\text{Fixed Costs}}{\text{SP per unit} - \text{Variable CP per unit}}$$

### Case 4: Profit on Cost vs Profit on Sale

If profit is $p\%$ on SP, then profit on CP:
$$\text{Profit on CP} = \frac{100p}{100-p}\%$$

If profit is $p\%$ on CP, then profit on SP:
$$\text{Profit on SP} = \frac{100p}{100+p}\%$$

---

## GATE & ESE Problem Patterns

### Pattern 1: Direct Calculation
> A trader buys goods for ₹450 and sells at ₹540. Find profit %.
- Profit = 540 - 450 = 90
- Profit % = (90/450) × 100 = **20%**

### Pattern 2: Markup-Discount Chain
> MP is 50% above CP. Discount given is 10%. Find profit %.
- Let CP = 100, MP = 150
- SP = 150 × 0.9 = 135
- Profit = 35%

Or using formula: $50 - 10 - \frac{50 \times 10}{100} = 50 - 10 - 5 = 35\%$

### Pattern 3: Cost Recovery
> A man sells an article at 5% loss. If he had sold it for ₹50 more, he would have gained 5%. Find CP.
- SP at 5% loss = 0.95 × CP
- SP at 5% profit = 1.05 × CP
- Difference = 0.10 × CP = 50
- CP = ₹500

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"A shopkeeper marks goods 30% above CP and gives 30% discount. What is the profit/loss %?"

Wrong thinking: 30% - 30% = 0% (no profit, no loss)

**The Elegant Solution:**
$$\text{Net} = 30 - 30 - \frac{30 \times 30}{100} = -9\%$$
There's a **9% loss**.

**MSQ Logic Gate:**
- If markup % = discount %, there's ALWAYS a loss
- Loss = (markup × discount)/100

**NAT Precision Lock:**
- Profit/Loss % may be a fraction (like 11.11%)
- Round to 2 decimal places unless specified otherwise

---

## Speed Tricks & Shortcuts

### Trick 1: The Fraction Method

| Profit/Loss | Fraction for CP→SP |
|-------------|-------------------|
| 10% Profit | ×11/10 |
| 20% Profit | ×6/5 |
| 25% Profit | ×5/4 |
| 33.33% Profit | ×4/3 |
| 10% Loss | ×9/10 |
| 20% Loss | ×4/5 |
| 25% Loss | ×3/4 |

### Trick 2: CP Ratio Shortcut

If SP is same and profit % are $p_1$ and $p_2$:
$$\frac{\text{CP}_1}{\text{CP}_2} = \frac{100 + p_2}{100 + p_1}$$

### Trick 3: The 100 Technique

Always assume CP = 100 (unless CP is given or needs to be found).

### Trick 4: Articles Shortcut

For "CP of m articles = SP of n articles":
- Profit if m > n, Loss if m < n
- Percentage = $\frac{|m-n|}{n} \times 100$

### Trick 5: Successive Discount Quick Calc

For 10% and 20% discounts:
- Think of it as: Pay 90% of 80% = 72%
- Discount = 28%

---

## Permanent Recall

### The Bizarre Mnemonic (Markup-Discount)
*"Mark UP to the sky, Discount DOWN to sell, but they meet in the middle and fight—the product of their fight ($\frac{xy}{100}$) is your loss!"*

### The Mental Slider
Visualize a price thermometer:
- CP at bottom (your investment)
- MP at top (your dreams)
- SP somewhere between (reality after discount)
- Profit = how far SP is above CP

### The 5-Second Snap-Check
- If discount % = markup %, you're at a LOSS
- If selling same item at profit AND loss for same SP, net is ALWAYS LOSS

---

## Practice Problems

### Level 1: Fundamentals
1. A shopkeeper buys an article for ₹400 and sells it for ₹500. Find the profit percentage.
2. If an article is sold at 20% loss, and SP is ₹800, find CP.
3. A trader marks goods 40% above CP and allows 20% discount. Find profit %.

### Level 2: GATE Standard
4. By selling 33 meters of cloth, a trader gains the cost of 11 meters. Find profit %.
5. A dealer sold two cars for ₹1,99,500 each, gaining 5% on one and losing 5% on the other. Find overall profit or loss.
6. If MP:CP = 3:2 and discount = 12.5%, find profit %.

### Level 3: IIT Examiner Level
7. A trader uses 960g weight instead of 1 kg and marks goods 20% above CP. If he gives 5% discount, find his total gain %.
8. A and B start a business with investments in ratio 3:2. After 4 months, A invests 50% more. Profit at year-end is ₹35,000. Find B's share.
9. A shopkeeper cheats both while buying (uses 20% extra weight) and selling (uses 20% less weight). Find total profit %.

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Profit = 500 - 400 = 100
   Profit % = (100/400) × 100 = **25%**

2. SP = CP × (1 - 20/100) = 0.8 × CP
   800 = 0.8 × CP
   CP = **₹1000**

3. Net = 40 - 20 - (40×20)/100 = 40 - 20 - 8 = **12%**

4. CP of 33m = SP of 33m - Profit
   Profit = CP of 11m
   So SP of 33m = CP of (33 + 11) = CP of 44m
   But SP of 33m = CP of 33m + Profit
   This means: Selling 33m gives profit of 11m worth
   Profit % = (11/33) × 100 = **33.33%**

5. Using formula for same SP: Loss = x²/100 = 25/100 = 0.25%
   Net Loss = 0.25% of total CP
   
   CP of car sold at profit = 199500/1.05 = 190000
   CP of car sold at loss = 199500/0.95 = 210000
   Total CP = 400000, Total SP = 399000
   Net Loss = ₹1000, Loss % = 1000/400000 × 100 = **0.25% Loss**

6. MP:CP = 3:2, so MP = 1.5 × CP
   SP = MP × (1 - 12.5/100) = 1.5 × 0.875 × CP = 1.3125 × CP
   Profit = 31.25% or **31.25%**

7. Gain from weight = (1000-960)/960 × 100 = 4.17%
   Effective multiplier from markup & discount = (1.20)(0.95) = 1.14
   Combined = 1.0417 × 1.14 = 1.1875
   Total gain = **18.75%**

8. A:B initial = 3:2
   After 4 months, A = 3 × 1.5 = 4.5
   A's capital-months = 3×4 + 4.5×8 = 12 + 36 = 48
   B's capital-months = 2×12 = 24
   Ratio = 48:24 = 2:1
   B's share = 35000 × 1/3 = **₹11,666.67**

9. While buying: Gets 1.2 kg for price of 1 kg
   While selling: Gives 0.8 kg for price of 1 kg
   Net ratio = 1.2/0.8 = 1.5
   Profit = **50%**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Profit & Loss with Simple & Compound Interest for a Rank-1 simulation?
