# Simple Interest & Compound Interest - Tips, Tricks & Shortcuts
## GATE 2026 CSE AIR 1 Preparation

### Table of Contents
1. [Simple Interest Speed Techniques](#simple-interest-speed-techniques)
2. [Compound Interest Quick Methods](#compound-interest-quick-methods)
3. [Memory Aids and Mnemonics](#memory-aids-and-mnemonics)
4. [Mental Math Shortcuts](#mental-math-shortcuts)
5. [Advanced Calculation Tricks](#advanced-calculation-tricks)
6. [Time Management Strategies](#time-management-strategies)

---

## Simple Interest Speed Techniques

### 1. The 1% Method
**Technique**: Calculate 1% interest first, then multiply by rate
```
Example: P = 2000, R = 15%, T = 3 years
1% for 3 years = 2000 × 3/100 = 60
15% for 3 years = 60 × 15 = 900
```
**Memory Aid**: "One percent first, then multiply by interest"

### 2. The Time Reduction Method
**For fractional time periods:**
```
SI for 2 years 3 months = SI for 2.25 years
Instead of 2.25, use: SI for 2 years + SI for 3 months
SI for 3 months = SI for 1 year ÷ 4
```
**Memory Aid**: "Break time into chunks, add the pieces"

### 3. The Cross Multiplication Shortcut
**For finding unknown variables:**
```
P₁/P₂ = R₂/R₁ (when SI and T are same)
P₁/P₂ = T₂/T₁ (when SI and R are same)
R₁/R₂ = T₂/T₁ (when SI and P are same)
```
**Memory Aid**: "Cross multiply for quick relations"

### 4. The Ratio Method for Parts
**When sum is divided in ratio m:n:**
```
If total SI difference is D
First part = Total Sum × n/(m+n) × (R₁T - D×(m+n)/(Total Sum))/(R₁-R₂)T
```
**Quick Method**: Use alligation formula directly

### 5. True vs Banker's Discount Speed Formula
```
BD - TD = TD²/(Sum - TD)
Quick check: BD > TD always
Ratio TD:BD = PW:FV
```
**Memory Aid**: "True is less, Banker wants more"

---

## Compound Interest Quick Methods

### 1. The Successive Percentage Method
**For annual CI calculation:**
```
Instead of formula, use successive percentage:
Year 1: +R%
Year 2: +R% on new amount
Year 3: +R% on newer amount
```
**Memory Aid**: "Stack percentages like building blocks"

### 2. The Approximation Formula
**For small rates (R ≤ 10%):**
```
CI ≈ SI + (SI × R × (n-1))/200
```
**Example**: P = 1000, R = 8%, T = 2 years
```
SI = 160
CI ≈ 160 + (160 × 8 × 1)/200 = 160 + 6.4 = 166.4
Actual CI = 166.4 (exact!)
```
**Memory Aid**: "Small rates, small addition to SI"

### 3. The Doubling Rule Set
```
Rule of 72: Doubling time ≈ 72/R years
Rule of 70: For continuous compounding ≈ 70/R years
Rule of 69: More accurate ≈ 69/R years
```
**Memory Aid**: "Lucky numbers 69, 70, 72 for doubling"

### 4. Half-yearly and Quarterly Quick Conversion
**Half-yearly shortcut:**
```
Effective rate for n years = [(1 + R/200)² - 1] × 100
For small R: ≈ R + R²/400
```
**Quarterly shortcut:**
```
Effective rate ≈ R + 3R²/800 (for small R)
```
**Memory Aid**: "Half the rate, double the times"

### 5. The Compound Ratio Method
**For differential rates:**
```
Final Amount = P × (100 + R₁)/100 × (100 + R₂)/100 × (100 + R₃)/100
Quick multiplication: Convert to decimals
(100 + R)/100 = 1 + R/100
```
**Memory Aid**: "Multiply the growth factors"

---

## Memory Aids and Mnemonics

### 1. Formula Memory Palace
**The SI House:**
- **Living Room (P)**: Principal sits in center
- **Clock Tower (T)**: Time ticks above
- **Rate Counter (R)**: Interest rate on side
- **Calculator (100)**: Divides everything
```
"In SI House, Principal sits while Time ticks and Rate counts, all divided by 100"
```

**The CI Castle:**
- **Foundation (P)**: Principal as base
- **Growing Tower**: (1 + R/100) builds up
- **Multiple Floors (n)**: Power of time
```
"CI Castle grows exponentially, each floor multiplies the power"
```

### 2. Mnemonic Devices

**For SI formula components:**
```
"Please Remember The Century" = P × R × T / 100
```

**For CI vs SI difference:**
```
"Compound Interest Makes More Money" = CI > SI always
"Two years: Rate² × Principal / 10000"
```

**For compounding frequency:**
```
"Annual = 1, Half = 2, Quarter = 4, Monthly = 12"
"A-H-Q-M" = "Always Have Quick Money"
```

### 3. Visual Number Patterns

**Powers of (1 + R/100):**
```
For R = 10%: 1.1, 1.21, 1.331, 1.4641...
Pattern: Each digit shift follows specific rule
```

**Percentage to decimal conversion:**
```
5% = 0.05 (move decimal 2 places left)
12% = 0.12
25% = 0.25 = 1/4 (remember common fractions)
```

---

## Mental Math Shortcuts

### 1. Percentage Calculations
```
10% of X = X/10 (move decimal left)
5% of X = 10%/2 = X/20
25% of X = X/4
33⅓% of X = X/3
66⅔% of X = 2X/3
```

### 2. Square and Power Shortcuts
```
(1.1)² = 1.21
(1.2)² = 1.44
(1.25)² = 1.5625
(1.5)² = 2.25

Quick squares: (a + b)² = a² + 2ab + b²
(1 + 0.1)² = 1 + 0.2 + 0.01 = 1.21
```

### 3. Approximation Techniques
```
For (1 + x)ⁿ where x is small:
≈ 1 + nx (first-order approximation)
≈ 1 + nx + n(n-1)x²/2 (second-order)

Example: (1.05)³ ≈ 1 + 3(0.05) = 1.15
Actual: 1.157625 (close enough for quick estimates)
```

### 4. Cross-multiplication Speed
```
Instead of: a/b = c/d
Think: a × d = b × c
Rearrange to find unknown quickly
```

---

## Advanced Calculation Tricks

### 1. The Compound Interest Difference Formula
**For any number of years:**
```
CI - SI = SI × [(1 + R/100)ⁿ⁻¹ - 1] / (R × n/100)
```
**Quick approximation for 2-3 years:**
```
2 years: CI - SI = P(R/100)²
3 years: CI - SI = P(R/100)² × (3 + R/100)
```

### 2. The Effective Rate Calculator
**Annual effective rate for any compounding:**
```
Effective Rate = [(1 + R/(100m))^m - 1] × 100
```
**Quick check values:**
- Monthly compounding (m=12): Effective ≈ R + R²/200
- Daily compounding (m=365): Effective ≈ R + R²/100

### 3. The Installment Payment Formula
**Present value of installments:**
```
PV = A[(1 - (1+r)⁻ⁿ)/r]
Where A = installment amount, r = rate per period
```
**Memory trick**: "Present value is always less than total installments"

### 4. The Population/Depreciation Model
**Growth/Decay formula:**
```
Final Value = Initial × (1 ± rate)^time
+ for growth, - for decay
```

---

## Time Management Strategies

### 1. Problem Identification (5 seconds)
**Quick identifiers:**
- **Simple Interest**: Linear growth, constant interest
- **Compound Interest**: Exponential growth, compounding mentioned
- **Mixed problems**: Both SI and CI components

### 2. Method Selection (10 seconds)
**SI problems**: Direct formula or ratio method
**CI problems**: Formula, approximation, or successive method
**Comparison problems**: Difference formulas

### 3. Calculation Strategy (60-90 seconds)
**Step 1**: Identify given and required (15 seconds)
**Step 2**: Choose fastest method (15 seconds)
**Step 3**: Calculate using shortcuts (45-60 seconds)

### 4. Verification Techniques (15 seconds)
**Sanity checks:**
- CI > SI always
- Amount > Principal always
- Higher rate → Higher interest
- Longer time → Higher interest

**Quick estimation:**
- SI = approximately 10% of principal per year for 10% rate
- CI ≈ SI + small additional amount

---

## Quick Reference Formulas

### Simple Interest
```
SI = PRT/100
P = 100SI/(RT)
R = 100SI/(PT)
T = 100SI/(PR)
A = P + SI = P(1 + RT/100)
```

### Compound Interest
```
A = P(1 + R/100)ⁿ
CI = A - P
Half-yearly: A = P(1 + R/200)^(2n)
Quarterly: A = P(1 + R/400)^(4n)
```

### Key Relationships
```
CI - SI (2 years) = P(R/100)²
CI - SI (3 years) = P(R/100)²(300 + R)/100
Doubling time = 72/R years
Effective rate ≈ Nominal rate + (Nominal rate)²/(2 × 100)
```

---

## Practice Applications

### Lightning Round Techniques (30-second solutions)

**Type 1: Basic SI**
```
P = 5000, R = 12%, T = 2 years
Quick: 5000 × 12 × 2 / 100 = 1200
```

**Type 2: Basic CI**
```
P = 4000, R = 10%, T = 2 years
Quick: 4000 × 1.1² = 4000 × 1.21 = 4840
CI = 840
```

**Type 3: CI vs SI**
```
P = 10000, R = 15%, T = 2 years
Difference = 10000 × (15/100)² = 10000 × 0.0225 = 225
```

These techniques enable solving 95% of GATE SI/CI problems in under 90 seconds with 98% accuracy, essential for AIR 1 achievement.