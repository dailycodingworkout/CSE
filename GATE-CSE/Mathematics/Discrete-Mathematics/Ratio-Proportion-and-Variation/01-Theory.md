# Ratio, Proportion & Variation - Complete Theory
**GATE 2026 CSE | AIR 1 Preparation**

---

## Table of Contents
1. [Ratio - Fundamental Concepts](#ratio-fundamental-concepts)
2. [Proportion - Advanced Applications](#proportion-advanced-applications) 
3. [Variation - Dynamic Relationships](#variation-dynamic-relationships)
4. [Compound Ratio & Partnership](#compound-ratio--partnership)
5. [Mathematical Foundations](#mathematical-foundations)

---

## 1. Ratio - Fundamental Concepts

### 1.1 Definition and Core Principles

**Ratio** is a quantitative relationship between two quantities of the same kind, expressing how many times one quantity contains another.

**Mathematical Definition:**
If a and b are two quantities of the same kind, their ratio is expressed as a:b or a/b, where:
- **a** = Antecedent (first term)
- **b** = Consequent (second term)
- **b ≠ 0** (consequent cannot be zero)

### 1.2 Properties of Ratios

**Property 1: Fundamental Ratio Equality**
```
a:b = c:d ⟺ ad = bc (Cross multiplication property)
```

**Property 2: Scaling Property**
```
a:b = ka:kb for any non-zero constant k
```

**Property 3: Additive Property**
If a:b = c:d, then:
```
(a+c):(b+d) = a:b = c:d (when ratios are equal)
```

### 1.3 Equalities in Ratio

**Adding/Subtracting Same Value:**
If ratio a:b is given, and we add/subtract x to both terms:
- New ratio = (a+x):(b+x) or (a-x):(b-x)
- **Critical Point:** This changes the ratio value unless x = 0

**Mathematical Proof:**
```
Original ratio: a/b
New ratio: (a+x)/(b+x)

For equality: a/b = (a+x)/(b+x)
Cross multiply: a(b+x) = b(a+x)
ab + ax = ba + bx
ax = bx
x(a-b) = 0

Therefore: x = 0 or a = b
```

### 1.4 Ratio as Part of Total Value

If a:b = m:n, and total value is T, then:
- Share of a = (m/(m+n)) × T
- Share of b = (n/(m+n)) × T

**Verification:** (m/(m+n)) × T + (n/(m+n)) × T = T ✓

### 1.5 Types of Ratios

#### 1.5.1 Duplicate Ratio
**Definition:** Square of a given ratio
```
If a:b is given ratio, then a²:b² is duplicate ratio
Mathematical form: (a/b)² = a²/b²
```

#### 1.5.2 Triplicate Ratio  
**Definition:** Cube of a given ratio
```
If a:b is given ratio, then a³:b³ is triplicate ratio
Mathematical form: (a/b)³ = a³/b³
```

#### 1.5.3 Sub-duplicate Ratio
**Definition:** Square root of a given ratio
```
If a:b is given ratio, then √a:√b is sub-duplicate ratio
Mathematical form: √(a/b) = √a/√b
```

#### 1.5.4 Sub-triplicate Ratio
**Definition:** Cube root of a given ratio
```
If a:b is given ratio, then ∛a:∛b is sub-triplicate ratio  
Mathematical form: ∛(a/b) = ∛a/∛b
```

**Relationship Chain:**
```
Sub-triplicate → Sub-duplicate → Original → Duplicate → Triplicate
∛(a:b) → √(a:b) → (a:b) → (a:b)² → (a:b)³
```

---

## 2. Proportion - Advanced Applications

### 2.1 Definition and Fundamental Theorem

**Proportion** is the equality of two ratios.
```
a:b :: c:d or a:b = c:d
Mathematical form: a/b = c/d ⟺ ad = bc
```

**Fundamental Theorem:** In any proportion a:b :: c:d
- **Product of extremes** = **Product of means**
- Extremes: a, d; Means: b, c
- Therefore: a × d = b × c

### 2.2 Types of Proportions

#### 2.2.1 Fourth Proportion
If a:b :: c:x, then x is the fourth proportion.
```
Solution: x = (b × c)/a
Verification: a/b = c/x ⟹ ax = bc ⟹ x = bc/a
```

#### 2.2.2 Third Proportion  
If a:b :: b:x, then x is the third proportion.
```
Solution: x = b²/a
Verification: a/b = b/x ⟹ ax = b² ⟹ x = b²/a
```

#### 2.2.3 Second Proportion (Mean Proportion/Geometric Mean)
If a:x :: x:b, then x is the mean proportion.
```
Solution: x = √(ab)
Verification: a/x = x/b ⟹ x² = ab ⟹ x = √(ab)
```

#### 2.2.4 Continued Proportion
Three quantities a, b, c are in continued proportion if a:b :: b:c
```
Condition: b² = ac
Common ratio: r = b/a = c/b
General form: a, ar, ar²
```

### 2.3 Advanced Proportion Rules

#### 2.3.1 Componendo Rule
If a/b = c/d, then (a+b)/b = (c+d)/d
```
Proof:
a/b = c/d (given)
Adding 1 to both sides: a/b + 1 = c/d + 1
(a+b)/b = (c+d)/d
```

#### 2.3.2 Dividendo Rule  
If a/b = c/d, then (a-b)/b = (c-d)/d
```
Proof:
a/b = c/d (given)
Subtracting 1: a/b - 1 = c/d - 1
(a-b)/b = (c-d)/d
```

#### 2.3.3 Componendo-Dividendo Rule
If a/b = c/d, then (a+b)/(a-b) = (c+d)/(c-d)
```
Proof:
From Componendo: (a+b)/b = (c+d)/d ... (1)
From Dividendo: (a-b)/b = (c-d)/d ... (2)
Dividing (1) by (2): (a+b)/(a-b) = (c+d)/(c-d)
```

#### 2.3.4 Invertendo Rule
If a/b = c/d, then b/a = d/c
```
Proof: Direct reciprocal of given proportion
```

#### 2.3.5 Alternendo Rule  
If a/b = c/d, then a/c = b/d
```
Proof:
a/b = c/d ⟹ ad = bc
Dividing by cd: a/c = b/d
```

### 2.4 Multiple Ratio Equality
If a/b = c/d = e/f = k (constant), then:
```
(a+c+e)/(b+d+f) = k

Proof:
a = bk, c = dk, e = fk
Therefore: (a+c+e)/(b+d+f) = (bk+dk+fk)/(b+d+f) = k(b+d+f)/(b+d+f) = k
```

---

## 3. Variation - Dynamic Relationships

### 3.1 Direct Variation

**Definition:** Two quantities x and y are in direct variation if their ratio remains constant.
```
Mathematical form: y ∝ x or y = kx (k = constant of variation)
```

**Properties:**
1. As x increases, y increases proportionally
2. As x decreases, y decreases proportionally  
3. Graph is a straight line passing through origin
4. y₁/x₁ = y₂/x₂ = k

**Advanced Applications:**
- Time and Distance (at constant speed)
- Work and Workers (for same efficiency)
- Cost and Quantity (at constant rate)

### 3.2 Inverse Variation

**Definition:** Two quantities x and y are in inverse variation if their product remains constant.
```
Mathematical form: y ∝ 1/x or xy = k (k = constant)
```

**Properties:**
1. As x increases, y decreases
2. As x decreases, y increases
3. Graph is a rectangular hyperbola
4. x₁y₁ = x₂y₂ = k

**Advanced Applications:**
- Time and Speed (for fixed distance)
- Workers and Time (for same work)
- Pressure and Volume (Boyle's Law)

### 3.3 Joint Variation
When one quantity varies with multiple other quantities:
```
z ∝ xy ⟹ z = kxy (Direct joint variation)
z ∝ x/y ⟹ z = kx/y (Mixed variation)
```

---

## 4. Compound Ratio & Partnership

### 4.1 Compound Ratio Theory

**Definition:** Product of two or more ratios
```
If ratios are a:b and c:d, then compound ratio = (a×c):(b×d) = ac:bd
```

**Extended Form:** For ratios r₁, r₂, ..., rₙ
```
Compound ratio = r₁ × r₂ × ... × rₙ
```

### 4.2 Partnership Applications

**Fundamental Principle:** Profit division in partnership is based on compound ratio of investment and time.

#### 4.2.1 Case 1: Investment Ratio is Unity (Equal Investment)
When all partners invest equal amounts:
```
Profit ratio = Time ratio
If times are t₁:t₂:t₃, then profit ratio = t₁:t₂:t₃
```

#### 4.2.2 Case 2: Investment Time is Same  
When all partners invest for equal time:
```
Profit ratio = Investment ratio
If investments are I₁:I₂:I₃, then profit ratio = I₁:I₂:I₃
```

#### 4.2.3 Case 3: Variable Investment (General Case)
When both investment and time vary:
```
Profit ratio = (Investment × Time) ratio
Partner A : Partner B = (I₁ × t₁) : (I₂ × t₂)
```

**Effective Investment Concept:**
```
Effective Investment = Actual Investment × Time Period
Total Effective Investment = Σ(Individual Effective Investments)
Individual Share = (Individual Effective Investment / Total Effective Investment) × Total Profit
```

### 4.3 Advanced Partnership Scenarios

#### 4.3.1 Variable Investment Over Time
If partner changes investment during partnership:
```
Effective Investment = Σ(Investment × Time for each period)
Example: ₹1000 for 3 months + ₹1500 for 2 months = 1000×3 + 1500×2 = 6000
```

#### 4.3.2 Partnership with Different Profit Sharing Agreements
- **Salary-based:** Fixed salary + profit share
- **Commission-based:** Commission on sales + profit share
- **Guaranteed minimum:** Minimum guaranteed amount + profit share

---

## 5. Mathematical Foundations

### 5.1 Ratio and Proportion in Number Theory

**GCD and Ratio Simplification:**
```
If a:b = m:n (in simplest form), then gcd(a,b) = gcd(m,n) × k
where k is the scaling factor
```

**LCM and Ratio Applications:**
```
If a:b = m:n, then LCM(a,b) = LCM(m,n) × k
where k = gcd(a,b)
```

### 5.2 Algebraic Identities in Ratios

**Identity 1:** (a+b):(a-b) transformation
```
If a/b = m/n, then (a+b)/(a-b) = (m+n)/(m-n)
```

**Identity 2:** Ratio of sums and differences
```
If a:b:c = x:y:z, then 
(a+b+c):(b+c+a):(c+a+b) = (x+y+z):(y+z+x):(z+x+y) = 1:1:1
```

### 5.3 Calculus Applications

**Rate of Change in Ratios:**
```
If y = kx^n (power law), then dy/dx = nkx^(n-1)
Ratio of rates: (dy₁/dx):(dy₂/dx) at different points
```

**Optimization in Partnership:**
Finding optimal investment ratios for maximum individual returns under constraints.

---

## Key Formulas Summary

### Ratio Formulas
- Basic ratio: a:b = a/b
- Duplicate ratio: a²:b²  
- Sub-duplicate ratio: √a:√b
- Compound ratio: (a:b) × (c:d) = ac:bd

### Proportion Formulas
- Fourth proportion: If a:b::c:x, then x = bc/a
- Mean proportion: If a:x::x:b, then x = √(ab)
- Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)

### Variation Formulas
- Direct: y = kx
- Inverse: xy = k
- Joint: z = kxy

### Partnership Formulas
- Profit ratio = (Investment × Time) ratio
- Individual share = (Effective Investment/Total Effective Investment) × Total Profit

**Total Characters: 8,445**