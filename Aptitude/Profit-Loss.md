# Profit & Loss: Complete Study Material for GATE & ESE
> Concise, genius-level notes with zero redundancy

---

## Table of Contents
1. [Core Concepts](#1-core-concepts)
2. [Master Formulas](#2-master-formulas)
3. [Mental Math Tricks](#3-mental-math-tricks)
4. [Worked Examples](#4-worked-examples)
5. [Edge Cases & Traps](#5-edge-cases--traps)
6. [Quick Reference Card](#6-quick-reference-card)

---

## 1. Core Concepts

### The Foundation: What is Profit & Loss?

**The One-Line Definition:**
> Profit/Loss = Selling Price − Cost Price

**Real-World Analogy:**
Think of yourself as a trader. You **buy** something (Cost Price), add your **effort/margin** (Profit), and **sell** it (Selling Price). If SP > CP → Profit. If SP < CP → Loss.

### Key Terms (The Building Blocks)

| Term | Symbol | Meaning | Real-World Example |
|------|--------|---------|-------------------|
| **Cost Price (CP)** | C | What you pay to acquire | ₹100 to buy a book |
| **Selling Price (SP)** | S | What you receive when selling | ₹120 when you sell the book |
| **Marked Price (MP)** | M | Listed/sticker price (before discount) | ₹150 printed on the book |
| **Discount** | D | Reduction from marked price | 20% off → you pay ₹120 |
| **Profit/Gain** | P | SP − CP (when positive) | ₹120 − ₹100 = ₹20 profit |
| **Loss** | L | CP − SP (when positive) | Sold at ₹80, loss = ₹20 |

### Why Percentages Matter

**Key Insight:** Profit/Loss percentages are ALWAYS calculated on **Cost Price** (what you invested), not Selling Price.

**Why?** Because profit is about "return on investment." You invested CP, so profit percentage tells you how much you earned relative to your investment.

```
Profit % = (Profit / CP) × 100
Loss % = (Loss / CP) × 100
```

**Analogy:** If you deposit ₹1000 in a bank and earn ₹50 interest, you say "5% return" (50/1000), not based on ₹1050.

---

## 2. Master Formulas

### Tier 1: Essential Formulas

| Formula | When to Use |
|---------|-------------|
| **SP = CP + Profit** | Finding SP when CP and Profit known |
| **SP = CP − Loss** | Finding SP when CP and Loss known |
| **Profit = SP − CP** | Finding absolute profit |
| **Profit % = (Profit/CP) × 100** | Finding percentage profit |
| **SP = CP × (100 + P%)/100** | Direct SP calculation with profit % |
| **SP = CP × (100 − L%)/100** | Direct SP calculation with loss % |
| **CP = SP × 100/(100 + P%)** | Finding CP when SP and P% known |
| **CP = SP × 100/(100 − L%)** | Finding CP when SP and L% known |

### Tier 2: Discount Formulas

| Formula | When to Use |
|---------|-------------|
| **SP = MP × (100 − D%)/100** | Finding SP after discount |
| **MP = SP × 100/(100 − D%)** | Finding MP when SP and discount known |
| **Discount = MP − SP** | Finding absolute discount |
| **D% = (Discount/MP) × 100** | Finding discount percentage |

### Tier 3: Advanced Relationships

**The Golden Chain:** CP → MP → SP

```
MP = CP × (100 + Markup%)/100
SP = MP × (100 − Discount%)/100
```

**Combined Formula (Markup + Discount → Profit):**
```
If Markup = m% and Discount = d%, then:
Net Effect = m − d − (m × d)/100
```

**Derivation:** 
- Let CP = 100
- MP = 100 + m = 100(1 + m/100)
- SP = MP × (1 − d/100) = 100(1 + m/100)(1 − d/100)
- SP = 100 + m − d − md/100
- Profit % = SP − 100 = m − d − md/100 ✓

### Tier 4: Successive Operations

**Two Successive Discounts of a% and b%:**
```
Equivalent Single Discount = a + b − (ab/100)
```

**Two Successive Profits of a% and b%:**
```
Equivalent Single Profit = a + b + (ab/100)
```

**Memory Trick:** 
- Discounts "reduce" → use **minus** (−ab/100)
- Profits "add up" → use **plus** (+ab/100)

---

## 3. Mental Math Tricks

### Trick 1: The Fraction Method (Fastest for Common Percentages)

| Profit/Loss % | Multiplier Fraction | Mental Calculation |
|---------------|--------------------|--------------------|
| 10% profit | × 11/10 | SP = CP × 1.1 |
| 20% profit | × 6/5 | SP = CP × 6/5 |
| 25% profit | × 5/4 | SP = CP × 1.25 |
| 33.33% profit | × 4/3 | SP = CP × 4/3 |
| 50% profit | × 3/2 | SP = CP × 1.5 |
| 10% loss | × 9/10 | SP = CP × 0.9 |
| 20% loss | × 4/5 | SP = CP × 4/5 |
| 25% loss | × 3/4 | SP = CP × 0.75 |

**Example:** CP = ₹240, Profit = 25%
- SP = 240 × 5/4 = 240 × 1.25 = **₹300** ✓

### Trick 2: Profit & Loss Cancel-Out Rule

If an article is sold at **x% profit** and then **x% loss** (or vice versa), there's always a **net loss**.

```
Net Loss % = x²/100
```

**Why?** Proof with x = 20%:
- CP = 100, after 20% profit SP₁ = 120
- Sold at 20% loss: SP₂ = 120 × 0.8 = 96
- Net Loss = 100 − 96 = 4 = 20²/100 = 4% ✓

**Analogy:** Like taking 2 steps forward and 2 steps back on an escalator going down — you end up lower!

### Trick 3: False Weight (Cheating Shopkeeper)

If a shopkeeper uses **false weight** while claiming to sell at CP:
```
Profit % = (Error / True Weight − Error) × 100
         = (Error / Actual Weight Given) × 100
```

**Example:** Sells 900g instead of 1kg at ₹100/kg
- Error = 1000 − 900 = 100g
- Profit % = (100/900) × 100 = **11.11%**

**Quick Formula:** If selling x grams less per kg:
```
Profit % = x/(1000 − x) × 100
```

### Trick 4: Same SP, Different Profit/Loss

When two articles are sold at **same SP** with one at **x% profit** and other at **x% loss**:
```
Net Result = Always LOSS
Net Loss % = x²/100
```

**Why Net Loss?** The loss is calculated on a higher CP than the profit, so loss amount > profit amount.

### Trick 5: CP Ratio Method

If **Profit % = Loss %** and we need to find the ratio:
- When same SP: CP₁ : CP₂ = (100 − x) : (100 + x)

**Example:** Two items sold at ₹480 each, one at 20% profit, one at 20% loss
- CP₁ (profit) = 480 × 100/120 = ₹400
- CP₂ (loss) = 480 × 100/80 = ₹600
- Total CP = ₹1000, Total SP = ₹960
- Net Loss = ₹40 = 4% of 1000 = 20²/100 % ✓

### Trick 6: Break-Even Point

When some items sold at profit and some at loss:
```
For break-even (no profit, no loss):
Ratio of quantities = Loss% : Profit%
```

---

## 4. Worked Examples

### Level 1: Basic Application

**Q1:** A shopkeeper buys 100 pens at ₹10 each and sells at ₹12 each. Find profit %.

**Solution:**
- CP per pen = ₹10, SP per pen = ₹12
- Profit per pen = ₹2
- Profit % = (2/10) × 100 = **20%**

---

**Q2:** An article is sold for ₹1380 at 15% profit. Find CP.

**Solution:**
- SP = CP × (100 + 15)/100 = CP × 1.15
- 1380 = CP × 1.15
- CP = 1380/1.15 = **₹1200**

---

### Level 2: Discount + Markup

**Q3:** A trader marks goods 40% above CP and gives 25% discount. Find profit %.

**Solution (Using Formula):**
```
Net = m − d − md/100 = 40 − 25 − (40 × 25)/100
    = 40 − 25 − 10 = 5%
```
**Answer: 5% Profit** ✓

**Alternative (Assume CP = 100):**
- MP = 140
- SP = 140 × 0.75 = 105
- Profit = 5% ✓

---

**Q4:** After giving two successive discounts of 10% and 20%, the SP is ₹360. Find MP.

**Solution:**
- Equivalent discount = 10 + 20 − (10 × 20)/100 = 28%
- SP = MP × (1 − 0.28) = MP × 0.72
- 360 = MP × 0.72
- MP = 360/0.72 = **₹500**

---

### Level 3: False Weight & Cheating

**Q5:** A dishonest dealer sells at CP but uses 800g weight instead of 1kg. Find profit %.

**Solution:**
```
Profit % = (Error / Actual Weight) × 100
         = (200 / 800) × 100 = 25%
```
**Answer: 25% Profit** ✓

---

**Q6:** A trader uses 20% less weight and also marks up by 20%. Find total profit %.

**Solution:**
- False weight profit = 20/(100 − 20) × 100 = 25%
- Markup profit = 20%
- Combined = 25 + 20 + (25 × 20)/100 = 45 + 5 = **50%**

---

### Level 4: Complex Scenarios

**Q7:** A man sells two watches at ₹1980 each. On one he gains 10% and on the other loses 10%. Find overall result.

**Solution:**
- Net Loss % = x²/100 = 10²/100 = 1%
- CP₁ = 1980 × 100/110 = ₹1800
- CP₂ = 1980 × 100/90 = ₹2200
- Total CP = ₹4000, Total SP = ₹3960
- Loss = ₹40 = 1% of 4000 ✓

**Answer: 1% Loss (or ₹40 loss)**

---

**Q8:** By selling 45 lemons, a vendor gains the SP of 15 lemons. Find profit %.

**Solution:**
Let SP of 1 lemon = ₹1
- SP of 45 lemons = ₹45
- Profit = SP of 15 lemons = ₹15
- CP = SP − Profit = 45 − 15 = ₹30
- Profit % = (15/30) × 100 = **50%**

**Shortcut:** Profit = SP of 15 out of 45 sold
- Ratio = 15:45 = 1:3
- If Profit : SP = 1 : 3, then Profit : CP = 1 : 2
- Profit % = 50%

---

**Q9:** The CP of 15 articles equals SP of 12 articles. Find profit/loss %.

**Solution:**
Let CP of 1 article = ₹1
- CP of 15 = 15 = SP of 12
- SP of 1 = 15/12 = 1.25
- Profit % = (1.25 − 1)/1 × 100 = **25% Profit**

**Quick Formula:** When CP of m = SP of n:
```
If m > n: Profit % = (m − n)/n × 100
If m < n: Loss % = (n − m)/n × 100
```

---

### Level 5: GATE/ESE Standard

**Q10:** A trader marks an item 50% above CP. He allows two successive discounts of 20% and d%. He still makes 8% profit. Find d.

**Solution:**
- Let CP = 100, then MP = 150
- Required SP = 108 (for 8% profit)
- After 20% discount: Price = 150 × 0.8 = 120
- After d% discount: 120 × (100 − d)/100 = 108
- (100 − d) = 108 × 100/120 = 90
- d = **10%**

---

**Q11:** A shopkeeper buys goods at 25% discount on MP. If he sells at MP, find his profit %.

**Solution:**
- CP = MP × 0.75 = 0.75M
- SP = MP = M
- Profit = M − 0.75M = 0.25M
- Profit % = (0.25M / 0.75M) × 100 = 100/3 = **33.33%**

---

## 5. Edge Cases & Traps

### Trap 1: Percentage on Wrong Base

❌ **Wrong:** Calculating profit % on SP instead of CP

**Example:** CP = ₹80, SP = ₹100
- ❌ Wrong: (20/100) × 100 = 20%
- ✅ Right: (20/80) × 100 = **25%**

---

### Trap 2: Successive Discounts ≠ Sum

❌ **Wrong:** Two 10% discounts = 20% discount

**Truth:** 10% + 10% = 10 + 10 − 1 = **19%**

---

### Trap 3: Same % Profit and Loss Always Results in Loss

When selling two items at same SP with equal profit % and loss %:
- **Always a NET LOSS** (because loss is on higher base)

---

### Trap 4: Confusing MP with CP

- **Discount** is always on MP
- **Profit/Loss** is always on CP
- Never mix them!

---

### Trap 5: False Weight – Using Total Weight

❌ **Wrong:** Profit = (Error/1000) × 100

✅ **Right:** Profit = (Error/Actual Weight Given) × 100

**Example:** 900g sold as 1kg
- ❌ Wrong: 100/1000 = 10%
- ✅ Right: 100/900 = **11.11%**

---

### Edge Case 1: Zero Profit Scenario

When a trader gives d% discount and uses false weights of (100-d)% of actual:
```
Net effect can be zero profit OR positive
Depends on the combination
```

---

### Edge Case 2: Negative Markup (Selling Below CP)

If marked below CP (negative markup), use the same formulas but expect negative values indicating loss.

---

### Edge Case 3: Multiple Articles with Different Profits

When n₁ items at P₁% and n₂ items at P₂%:
```
Overall Profit % = (n₁ × P₁ + n₂ × P₂)/(n₁ + n₂)
```
*Only valid when all CPs are equal!*

---

## 6. Quick Reference Card

### Formula Speed Sheet

```
┌─────────────────────────────────────────────────────────────┐
│  CORE RELATIONSHIPS                                          │
├─────────────────────────────────────────────────────────────┤
│  Profit = SP − CP           │  Loss = CP − SP               │
│  P% = (P/CP) × 100          │  L% = (L/CP) × 100            │
│  SP = CP(1 + P/100)         │  SP = CP(1 − L/100)           │
│  CP = SP × 100/(100 + P)    │  CP = SP × 100/(100 − L)      │
├─────────────────────────────────────────────────────────────┤
│  DISCOUNT                                                    │
├─────────────────────────────────────────────────────────────┤
│  SP = MP(1 − D/100)         │  D% = [(MP − SP)/MP] × 100    │
│  Successive D: a + b − ab/100                                │
├─────────────────────────────────────────────────────────────┤
│  SPECIAL CASES                                               │
├─────────────────────────────────────────────────────────────┤
│  False Weight: P% = Error/(True − Error) × 100              │
│  Same SP, ±x%: Loss = x²/100                                │
│  CP of m = SP of n: P% = (m−n)/n × 100 (when m > n)         │
│  Markup m%, Discount d%: Net = m − d − md/100               │
└─────────────────────────────────────────────────────────────┘
```

### Common Percentage Shortcuts

| % | Fraction | Multiply/Divide |
|---|----------|-----------------|
| 5% | 1/20 | ÷ 20 |
| 10% | 1/10 | ÷ 10 |
| 12.5% | 1/8 | ÷ 8 |
| 15% | 3/20 | × 3, ÷ 20 |
| 16.67% | 1/6 | ÷ 6 |
| 20% | 1/5 | ÷ 5 |
| 25% | 1/4 | ÷ 4 |
| 33.33% | 1/3 | ÷ 3 |
| 40% | 2/5 | × 2, ÷ 5 |
| 50% | 1/2 | ÷ 2 |
| 66.67% | 2/3 | × 2, ÷ 3 |
| 75% | 3/4 | × 3, ÷ 4 |

### Golden Rules (Memorize!)

1. **Profit/Loss % → Always on CP**
2. **Discount % → Always on MP**
3. **Successive ±x% on same SP → Net Loss = x²/100**
4. **False weight profit → Error/(True Weight − Error)**
5. **CP of m = SP of n → Profit if m > n**

---

## Practice Problems (Self-Test)

1. A sold an article to B at 20% profit. B sold it to C at 25% profit. If C paid ₹1500, find A's CP.

2. A shopkeeper marks goods 35% above CP and gives 20% discount. He also cheats 10% on weight. Find overall profit %.

3. Two-thirds of goods are sold at 15% profit and rest at 12% loss. Find overall profit/loss %.

4. After two successive discounts of 20% and 25%, an article is sold for ₹480. If the trader still makes 20% profit, find CP.

5. A sells to B at 10% profit, B sells to C at 20% profit, C sells to D at 25% loss. If D pays ₹990, find A's CP.

<details>
<summary>Answers</summary>

1. **₹1000** — Work backward: B's SP = 1500, B's CP = 1500/1.25 = 1200 = A's SP, A's CP = 1200/1.2 = 1000

2. **20% Profit** — Let CP = ₹100/kg. MP = 135, SP after 20% discount = 135 × 0.8 = ₹108. Customer gets only 900g (10% less), so actual cost of goods sold = ₹90. Profit = 108 − 90 = ₹18. Profit % = (18/90) × 100 = **20%**

3. **6% Profit** — Let total goods = 3 units. Profit from 2 units = 2 × 15 = 30%, Loss from 1 unit = 1 × 12 = 12%. Net = (30 − 12)/3 = **6% profit**

4. **₹400** — Equivalent discount = 20 + 25 − 5 = 40%. MP = 480/0.6 = 800. SP = 480 = 1.2 × CP, CP = 400

5. **₹1000** — D = 990, C = 990/0.75 = 1320, B = 1320/1.2 = 1100, A = 1100/1.1 = 1000

</details>

---

*Last Updated: 2025 | Curated for GATE & ESE Aspirants*
