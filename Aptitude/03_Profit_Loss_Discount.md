# Chapter 3: Profit, Loss & Discount

> **Business mathematics - the language of commerce and competitive exams**

---

## 🎯 Why Study This?

- Directly tested in GATE/ESE (2-3 questions per exam)
- Combines percentage concepts with real-world transactions
- Foundation for data interpretation problems

---

## 📚 Fundamental Definitions

### Key Terms

| Term | Symbol | Definition |
|------|--------|------------|
| **Cost Price (CP)** | C | Price at which item is bought/manufactured |
| **Selling Price (SP)** | S | Price at which item is sold |
| **Marked Price (MP)** | M | Listed/Tag price before discount |
| **Profit (Gain)** | P | SP - CP (when SP > CP) |
| **Loss** | L | CP - SP (when CP > SP) |
| **Discount** | D | MP - SP |

**💡 Analogy**: 
- CP = What you paid
- MP = What the tag says
- Discount = What you bargained off
- SP = What customer pays
- Profit = What you earned

---

## 📐 Core Formulas

### Profit Scenario (SP > CP)

```
Profit = SP - CP
Profit % = (Profit/CP) × 100 = ((SP-CP)/CP) × 100

SP = CP × (1 + P%/100) = CP × (100 + P%)/100
CP = SP × (100/(100 + P%))
```

### Loss Scenario (CP > SP)

```
Loss = CP - SP
Loss % = (Loss/CP) × 100 = ((CP-SP)/CP) × 100

SP = CP × (1 - L%/100) = CP × (100 - L%)/100
CP = SP × (100/(100 - L%))
```

**⚠️ Critical**: Profit% and Loss% are ALWAYS calculated on **Cost Price**!

---

### Discount Calculation

```
Discount = MP - SP
Discount % = (Discount/MP) × 100

SP = MP × (1 - D%/100) = MP × (100 - D%)/100
```

**⚠️ Critical**: Discount% is ALWAYS calculated on **Marked Price**!

---

## 🔗 The Complete Transaction Chain

```
             markup%              discount%
    CP  ──────────────►  MP  ──────────────►  SP
    
SP = CP × (1 + markup%/100) × (1 - discount%/100)
```

**Example**: CP = 100, Markup = 50%, Discount = 20%
```
MP = 100 × 1.5 = 150
SP = 150 × 0.8 = 120
Profit = 120 - 100 = 20 (20% profit)
```

---

## ⚡ Multiplying Factor Method (Master This!)

| Action | Multiplying Factor |
|--------|-------------------|
| Profit of x% | × (100+x)/100 |
| Loss of x% | × (100-x)/100 |
| Markup of x% | × (100+x)/100 |
| Discount of x% | × (100-x)/100 |

**Example**: CP = 800, Profit = 25%
```
SP = 800 × 125/100 = 800 × 1.25 = 1000
```

**Example**: MP = 500, Discount = 15%
```
SP = 500 × 85/100 = 500 × 0.85 = 425
```

---

## 📊 Standard Problem Types

### Type 1: Find Missing Value

**Given CP and Profit%, find SP**
```
CP = 450, Profit = 20%
SP = 450 × 1.2 = 540
```

**Given SP and Loss%, find CP**
```
SP = 720, Loss = 10%
CP = SP × 100/(100-L%) = 720 × 100/90 = 800
```

---

### Type 2: Find Profit/Loss Percentage

**Given CP and SP**
```
CP = 250, SP = 300
Profit = 50
Profit% = (50/250) × 100 = 20%
```

**⚡ Shortcut Formula**:
```
Profit% = ((SP-CP)/CP) × 100 = ((SP/CP) - 1) × 100
Loss% = ((CP-SP)/CP) × 100 = (1 - (SP/CP)) × 100
```

---

### Type 3: Markup and Discount Combined

**To earn x% profit after giving y% discount, markup should be?**

```
Let CP = 100, Required SP = 100 + x (for x% profit)
After y% discount: SP = MP × (100-y)/100
So: 100 + x = MP × (100-y)/100
MP = (100+x) × 100/(100-y)
Markup = MP - 100 = (100+x) × 100/(100-y) - 100
```

**Formula**:
```
Markup% = ((100 + Profit%)/(100 - Discount%) - 1) × 100
        = (Profit% + Discount%)/(100 - Discount%) × 100
```

**Example**: Profit 20%, Discount 10%
```
Markup = (20 + 10)/(100 - 10) × 100 = 30/90 × 100 = 33.33%
```

---

### Type 4: Successive Discounts

Two successive discounts of a% and b% = Single discount of:
```
Equivalent Single Discount = a + b - (ab/100) %
```

**Example**: 20% and 10% successive discounts
```
= 20 + 10 - 200/100 = 28%
```

**Alternative**: Using multipliers
```
(1 - 0.20)(1 - 0.10) = 0.8 × 0.9 = 0.72
Discount = 28%
```

---

### Type 5: False Weight/Measure Fraud

**Selling at CP but using false weights**:
```
Gain% = (Error/True Value - Error) × 100
      = (Error/(True - Error)) × 100
```

**Example**: Shopkeeper sells 900g instead of 1kg at CP
```
Gain% = (100/900) × 100 = 11.11%
```

**General Formula** (uses x grams less):
```
Gain% = (x/(1000-x)) × 100
```

---

### Type 6: Selling at Cost Price but Gaining

**Using false weights + markup**:
```
Total Gain% = ((True Weight/False Weight) × (100+Markup%)/100 - 1) × 100
```

---

## 🔄 Break-Even Analysis

**Break-even**: When total revenue = total cost (no profit, no loss)

```
Break-even quantity = Fixed Costs / (SP per unit - Variable Cost per unit)
```

---

## 💰 When CP of X = SP of Y

**Classic Problem Type**:
If CP of X articles = SP of Y articles:
```
Profit% = ((X-Y)/Y) × 100   (when X > Y)
Loss% = ((Y-X)/Y) × 100     (when Y > X)
```

**Example**: CP of 15 = SP of 12
```
Profit% = (15-12)/12 × 100 = 25%
```

**⚡ Trick**: X/Y = (100+P%)/100 or (100-L%)/100

---

## 📈 Multiple Transactions

### Same Article Sold to Multiple Buyers

If sold at different profit/loss percentages:
```
Total Revenue = Σ(Quantity × SP per unit)
Total Cost = Σ(Quantity × CP per unit)
Overall Profit% = (Total Revenue - Total Cost)/Total Cost × 100
```

---

### Two Articles, Same SP, One Profit, One Loss

**If profit% = loss% = x%**:
```
There is ALWAYS a net LOSS

Net Loss% = x²/100 %
```

**Example**: Two items sold at ₹100 each, one at 20% profit, one at 20% loss
```
Net Loss% = 20²/100 = 4%
```

**⚡ Why?** 
```
For profit case: CP₁ = 100/1.2 = 83.33
For loss case: CP₂ = 100/0.8 = 125
Total CP = 208.33, Total SP = 200
Loss = 8.33, Loss% = 8.33/208.33 = 4%
```

---

### Two Articles, Same CP, One Profit, One Loss

**If profit% = loss% = x%**:
```
Net = 0 (No profit, No loss)
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Don't confuse the base
```
❌ Profit% calculated on SP
✅ Profit% calculated on CP

❌ Discount% calculated on SP
✅ Discount% calculated on MP
```

### Trap 2: "% above/below cost" vs "% of cost"
```
20% above cost = CP × 1.2
20% of cost = CP × 0.2
```

### Trap 3: Successive discounts ≠ Sum of discounts
```
20% + 20% discount ≠ 40%
= 20 + 20 - 400/100 = 36%
```

### Trap 4: Equal profit% and loss% on same SP = Loss
```
Always remember the x²/100 formula
```

### Edge Case: Negative Profit = Loss
```
If Profit% comes negative, it's a Loss%
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| Profit% | ((SP-CP)/CP) × 100 |
| Loss% | ((CP-SP)/CP) × 100 |
| SP with profit | CP × (100+P)/100 |
| SP with loss | CP × (100-L)/100 |
| SP after discount | MP × (100-D)/100 |
| Successive discounts a%, b% | a + b - ab/100 |
| False weight gain | Error/(True-Error) × 100 |
| CP of X = SP of Y | (X-Y)/Y × 100 profit |
| Same SP, equal P% & L% | Net loss = x²/100 % |
| Markup for P% profit, D% discount | (P+D)/(100-D) × 100 |

---

## 📝 GATE-Level Practice

**Q1**: A shopkeeper marks goods 40% above CP and allows 20% discount. Find profit%.
```
Let CP = 100
MP = 140
SP = 140 × 0.8 = 112
Profit% = 12%

Or directly: (40-20-40×20/100) = 12%
Wait, that formula is for successive: 40 - 20 - 8 = 12% ✓
```

**Q2**: CP of 20 pens = SP of 16 pens. Profit%?
```
Profit% = (20-16)/16 × 100 = 25%
```

**Q3**: Two articles sold at ₹198 each. One at 10% profit, one at 10% loss. Net result?
```
Net Loss% = 10²/100 = 1%
```

**Q4**: To gain 20% after allowing 15% discount, goods must be marked above CP by?
```
Markup = (20 + 15)/(100 - 15) × 100 = 35/85 × 100 = 41.18%
```

**Q5**: A dishonest dealer sells at CP but uses 800g weight instead of 1kg. Gain%?
```
Gain% = (200/800) × 100 = 25%
```

---

*← [Chapter 2 - Percentages](./02_Percentages.md) | [Chapter 4 - Simple & Compound Interest →](./04_Simple_Compound_Interest.md)*
