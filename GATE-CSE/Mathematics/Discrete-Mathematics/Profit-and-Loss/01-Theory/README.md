# 01-Theory: Exhaustive Profit and Loss Concepts
## GATE 2026 CSE AIR 1 Preparation

### 🎯 Complete Theoretical Foundation

This section provides **exhaustive, meticulously detailed theory** covering all Profit and Loss concepts essential for achieving AIR 1 in GATE 2026 CSE.

---

## 1. Terminologies in Profit & Loss

### 1.1 Fundamental Definitions

#### Cost Price (CP)
**Definition**: The price at which an article is purchased or the cost incurred in manufacturing/producing an article.

**Mathematical Representation**:
```
CP = Purchase Price + Additional Expenses
```

**Components of Cost Price**:
- Purchase/Manufacturing cost
- Transportation charges
- Labor charges
- Overhead expenses
- Storage costs

#### Selling Price (SP)
**Definition**: The price at which an article is sold to the customer.

**Mathematical Representation**:
```
SP = Marked Price - Discount
SP = CP + Profit (if profit)
SP = CP - Loss (if loss)
```

#### Marked Price (MP) / List Price
**Definition**: The price marked on the article, which is usually higher than the selling price.

**Key Relationship**:
```
MP = SP + Discount
MP = CP + Profit + Discount
```

#### Profit (Gain)
**Definition**: When Selling Price > Cost Price, the excess amount is called Profit.

**Mathematical Formulation**:
```
Profit = SP - CP (when SP > CP)
Profit% = (Profit/CP) × 100
Profit% = ((SP - CP)/CP) × 100
```

#### Loss
**Definition**: When Selling Price < Cost Price, the deficit amount is called Loss.

**Mathematical Formulation**:
```
Loss = CP - SP (when CP > SP)
Loss% = (Loss/CP) × 100
Loss% = ((CP - SP)/CP) × 100
```

#### Discount
**Definition**: The reduction given on the Marked Price.

**Mathematical Formulation**:
```
Discount = MP - SP
Discount% = (Discount/MP) × 100
Discount% = ((MP - SP)/MP) × 100
```

### 1.2 Advanced Terminologies

#### Break-Even Point
**Definition**: The point where Cost Price equals Selling Price (No Profit, No Loss).

#### Overhead Expenses
**Definition**: Indirect costs incurred in business operations.
- Fixed Overhead: Rent, Insurance, Salaries
- Variable Overhead: Electricity, Raw materials

#### Gross Profit vs Net Profit
- **Gross Profit**: SP - Direct CP
- **Net Profit**: Gross Profit - All Expenses

---

## 2. Basic Formulae (Mathematical Foundations)

### 2.1 Core Profit-Loss Formulas

#### Formula Set 1: Basic Relationships
```
1. Profit = SP - CP
2. Loss = CP - SP
3. SP = CP + Profit = CP - Loss
4. CP = SP - Profit = SP + Loss
```

#### Formula Set 2: Percentage Calculations
```
1. Profit% = (Profit/CP) × 100
2. Loss% = (Loss/CP) × 100
3. SP = CP × (100 + Profit%)/100
4. SP = CP × (100 - Loss%)/100
5. CP = SP × 100/(100 + Profit%)
6. CP = SP × 100/(100 - Loss%)
```

#### Formula Set 3: Marked Price and Discount
```
1. Discount = MP - SP
2. Discount% = (Discount/MP) × 100
3. SP = MP × (100 - Discount%)/100
4. MP = SP × 100/(100 - Discount%)
```

### 2.2 Advanced Formula Derivations

#### Combined Profit-Discount Formula
**Derivation**:
```
Given: MP, Discount%, and required Profit%
MP × (100 - Discount%)/100 = CP × (100 + Profit%)/100

Therefore:
CP = MP × (100 - Discount%) / (100 + Profit%)
```

#### Successive Profit/Loss Formula
**For two successive transactions**:
```
If first transaction has x% profit/loss and second has y% profit/loss:
Net% = x + y + (xy/100)

Net Profit% = x + y + (xy/100) [if both are profits]
Net Loss% = x + y + (xy/100) [if both are losses]
Mixed = x - y + (xy/100) [if one profit, one loss]
```

#### Mathematical Proof:
```
Let initial CP = 100
After first transaction: 100 × (100 ± x)/100 = 100 ± x
After second transaction: (100 ± x) × (100 ± y)/100
= 100 ± x ± y ± xy/100
Net change = ±x ± y ± xy/100
```

### 2.3 Ratio-Based Formulas

#### Profit Ratio Formula
```
If profit% = p, then:
CP : SP = 100 : (100 + p)
SP : CP = (100 + p) : 100
```

#### Loss Ratio Formula
```
If loss% = l, then:
CP : SP = 100 : (100 - l)
SP : CP = (100 - l) : 100
```

---

## 3. False Weight Concepts

### 3.1 Theoretical Foundation

#### Definition
**False Weight**: When a trader uses incorrect weights (either more or less than standard) while buying or selling goods.

#### Types of False Weight Scenarios
1. **Using less weight while selling** (Gains more profit)
2. **Using more weight while buying** (Gains more quantity)
3. **Combination of both**

### 3.2 Mathematical Framework

#### Scenario 1: False Weight in Selling
**When seller uses weight 'w' instead of '1000g'**:

**Profit% Formula**:
```
Profit% = ((1000 - w)/w) × 100
```

**Derivation**:
- Customer pays for 1000g but gets only 'w' grams
- Effective CP for seller = w × (rate per gram)
- SP = 1000 × (rate per gram)
- Profit = SP - CP = (1000 - w) × (rate per gram)
- Profit% = ((1000 - w)/w) × 100

#### Scenario 2: False Weight in Buying
**When buyer uses weight 'w' instead of '1000g'**:

**Effective Cost Reduction**:
```
Cost Reduction% = ((1000 - w)/1000) × 100
```

#### Scenario 3: Combined False Weight
**Using weight 'w₁' while buying and 'w₂' while selling**:

**Net Profit% Formula**:
```
Net Profit% = ((w₁ - w₂)/w₂) × 100
```

### 3.3 Advanced False Weight Concepts

#### False Weight with Profit/Loss
**When trader has x% profit/loss along with false weight**:

**Combined Formula**:
```
Total Profit% = Normal Profit% + False Weight Profit% + (Product Term)

Total% = x + ((1000-w)/w)×100 + (x×((1000-w)/w)×100)/100
```

---

## 4. Discount Theory

### 4.1 Fundamental Discount Concepts

#### Single Discount
**Basic Formula**:
```
Final Price = Marked Price × (100 - Discount%)/100
```

#### Successive Discounts
**For two successive discounts d₁% and d₂%**:

**Mathematical Derivation**:
```
After first discount: MP × (100 - d₁)/100
After second discount: MP × (100 - d₁)/100 × (100 - d₂)/100
= MP × (100 - d₁)(100 - d₂)/10000
```

**Equivalent Single Discount Formula**:
```
Equivalent Discount% = d₁ + d₂ - (d₁ × d₂)/100
```

#### Proof of Successive Discount Formula:
```
Let MP = 100
After discounts: 100 × (100-d₁)(100-d₂)/10000
= 100 × (10000 - 100d₁ - 100d₂ + d₁d₂)/10000
= 100 - d₁ - d₂ + d₁d₂/100

Therefore, Total Discount = d₁ + d₂ - d₁d₂/100
```

### 4.2 Advanced Discount Strategies

#### Discount with Profit Target
**Problem Type**: Give x% discount and still maintain y% profit

**Formula Derivation**:
```
SP = MP × (100 - x)/100
SP = CP × (100 + y)/100

Therefore:
MP × (100 - x)/100 = CP × (100 + y)/100
MP = CP × (100 + y)/(100 - x)
```

#### Multi-level Discount Chains
**For n successive discounts d₁, d₂, ..., dₙ**:

**General Formula**:
```
Final Price = MP × ∏(100 - dᵢ)/100 for i=1 to n
```

---

## 5. Advanced Theoretical Concepts

### 5.1 Break-Even Analysis

#### Break-Even Point Calculation
**Definition**: Point where Total Revenue = Total Cost

**Mathematical Model**:
```
Break-Even Quantity = Fixed Cost / (Selling Price per unit - Variable Cost per unit)
```

### 5.2 Profit Maximization Theory

#### Marginal Analysis
**Optimal Profit Condition**:
```
Marginal Revenue = Marginal Cost
```

**Practical Application**:
- Increase production until MR = MC
- Beyond this point, profit decreases

### 5.3 Elasticity and Profit

#### Price Elasticity Impact
**Relationship between price change and profit**:
```
If demand is elastic: Price↓ → Quantity↑ → Profit may↑
If demand is inelastic: Price↑ → Quantity↓ slightly → Profit↑
```

---

## 6. Mathematical Proofs and Derivations

### 6.1 Proof: Successive Profit Formula

**Theorem**: For successive profits of x% and y%, net profit = x + y + xy/100

**Proof**:
```
Let initial amount = A
After first profit: A(1 + x/100)
After second profit: A(1 + x/100)(1 + y/100)
= A(1 + x/100 + y/100 + xy/10000)
= A(1 + (x + y + xy/100)/100)

Therefore, Net Profit% = x + y + xy/100
```

### 6.2 Proof: False Weight Profit Formula

**Theorem**: Using weight w instead of 1000g gives profit% = (1000-w)/w × 100

**Proof**:
```
Cost for w grams = C
Revenue for 1000g worth = C × 1000/w
Profit = C × 1000/w - C = C(1000-w)/w
Profit% = [C(1000-w)/w]/C × 100 = (1000-w)/w × 100
```

---

## 7. Real-World Applications

### 7.1 Business Scenarios

#### Inventory Management
- **FIFO Method**: First In, First Out
- **LIFO Method**: Last In, First Out
- **Average Cost Method**: Weighted average

#### Tax Implications
- **GST Impact on Profit Calculations**
- **Income Tax on Business Profits**

### 7.2 Economic Principles

#### Supply-Demand Impact
- **Market Equilibrium and Profit**
- **Competition Effects on Pricing**

---

## 🎯 Key Takeaways for AIR 1

1. **Master all 25+ core formulas** with instant recall
2. **Understand derivations** for complex problem variations
3. **Practice false weight scenarios** extensively
4. **Excel in successive discount calculations**
5. **Apply break-even analysis** for optimization problems

---

**Next**: Proceed to [02-Tips-and-Tricks](../02-Tips-and-Tricks/) for speed calculation techniques and memory aids.