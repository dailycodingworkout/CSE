# Chapter 6: Averages & Mixtures

> **Weighted thinking - the key to combining disparate quantities**

---

## 🎯 Why Study This?

- High-frequency topic in GATE/ESE
- Foundation for Data Interpretation
- Alligation method saves massive time in competitive exams

---

## 📚 Part 1: Averages

### What is Average?

**Average** = Sum of all values / Number of values

```
Average (Ā) = (x₁ + x₂ + ... + xₙ) / n = Σx / n
```

**💡 Analogy**: Average is the "balancing point" - if everyone got the same amount, what would each person get?

---

### Core Properties

**Property 1**: Sum = Average × Count
```
Σx = Ā × n
```

**Property 2**: Average lies between minimum and maximum values
```
min(xᵢ) ≤ Ā ≤ max(xᵢ)
```

**Property 3**: If each value changes by k, average changes by k
```
New average = Old average ± k
```

**Property 4**: If each value is multiplied by k, average is multiplied by k
```
New average = k × Old average
```

---

### Standard Problem Types

#### Type 1: Finding Average

**Example**: Find average of 12, 15, 18, 21, 24
```
Sum = 90, Count = 5
Average = 90/5 = 18
```

**⚡ Shortcut for AP series**: Average = (First + Last) / 2
```
Average = (12 + 24)/2 = 18
```

---

#### Type 2: Finding Missing Value

**Example**: Average of 5 numbers is 20. If one number is removed, average becomes 18. Find the removed number.
```
Original sum = 5 × 20 = 100
New sum = 4 × 18 = 72
Removed number = 100 - 72 = 28
```

---

#### Type 3: Combined Average

If group 1 has n₁ items with average A₁, group 2 has n₂ items with average A₂:
```
Combined Average = (n₁×A₁ + n₂×A₂) / (n₁ + n₂)
```

**Example**: 30 students average 60 marks, 20 students average 80 marks
```
Combined = (30×60 + 20×80) / 50 = (1800 + 1600) / 50 = 68
```

---

#### Type 4: New Entry Changes Average

**Person joins**:
```
New person's value = New average + n × (New avg - Old avg)
Where n = new count (after joining)
```

**Person leaves**:
```
Departed person's value = Old average + n × (Old avg - New avg)
Where n = old count (before leaving)
```

**Example**: Average age of 9 people is 28. A new person joins, average becomes 30. Age of new person?
```
Age = 30 + 10 × (30 - 28) = 30 + 20 = 50
OR: Total was 252, now 300, new person = 48... 
Wait, let me recalculate:
New person = 30 + 10×2 = 50 ✓
Check: (252 + 50)/10 = 302/10 ≠ 30
Correct formula: New = New avg × new count - Old avg × old count
= 30×10 - 28×9 = 300 - 252 = 48
```

**⚡ Correct Formula**:
```
New entry = New avg × (n+1) - Old avg × n = New avg + n(New avg - Old avg)
```

---

#### Type 5: Replacement Problems

**One item replaced by another**:
```
New - Old = n × (New avg - Old avg)
Where n = total count
```

**Example**: Average of 10 numbers is 15. One number is replaced by 25, average becomes 17. Replaced number?
```
25 - x = 10 × (17 - 15) = 20
x = 5
```

---

### Weighted Average

When items have different weights/frequencies:
```
Weighted Avg = Σ(wᵢ × xᵢ) / Σwᵢ
```

**Example**: Subject marks with credits
| Subject | Marks | Credits |
|---------|-------|---------|
| Math | 90 | 4 |
| Physics | 80 | 3 |
| English | 70 | 2 |

```
Weighted Avg = (90×4 + 80×3 + 70×2) / (4+3+2)
            = (360 + 240 + 140) / 9 = 82.22
```

---

## 📚 Part 2: Mixtures

### Concept

Mixing different items at different rates/prices to get a mixture.

**Key Principle**: Total value before mixing = Total value after mixing

---

### Type 1: Simple Mixing

**Mixing quantities Q₁ (at rate R₁) and Q₂ (at rate R₂)**:
```
Mixture rate = (Q₁×R₁ + Q₂×R₂) / (Q₁ + Q₂)
```

**Example**: 20L of milk at ₹40/L mixed with 30L at ₹50/L
```
Mixture price = (20×40 + 30×50) / 50 = 2300/50 = ₹46/L
```

---

### Type 2: Finding Mixing Ratio (Alligation)

**The Alligation Rule** - Most powerful technique!

Given mixture price M, and two components at prices P₁ and P₂:
```
Q₁/Q₂ = (P₂ - M) / (M - P₁)
```

**Visual Method (Alligation Diagram)**:
```
        P₁                    P₂
           \                /
            \    M        /
             \          /
              \        /
         (P₂-M)     (M-P₁)

Ratio Q₁:Q₂ = (P₂-M) : (M-P₁)
```

**Example**: In what ratio should rice at ₹32/kg be mixed with rice at ₹40/kg to get mixture at ₹35/kg?
```
        32 ———— 40
            35
        |         |
    40-35=5   35-32=3

Ratio = 5:3
```

---

### Type 3: Repeated Dilution

**After n operations of removing x units and replacing with another liquid**:
```
Final concentration = Initial × (1 - x/V)ⁿ

Where V = total volume
```

**Example**: A 20L container has pure milk. 4L is removed and replaced with water 3 times. Find milk left.
```
Milk = 20 × (1 - 4/20)³ = 20 × (0.8)³ = 20 × 0.512 = 10.24L
```

---

### Type 4: Removal and Replacement

**Single operation**: Remove x from V, replace with water
```
Milk remaining = V - x
Milk concentration = (V-x)/V
```

**Multiple operations** (n times):
```
Milk left = V × (1 - x/V)ⁿ
Water = V - Milk left = V × [1 - (1-x/V)ⁿ]
```

---

### Type 5: Mixing Two Mixtures

Mixture A: a% of substance X
Mixture B: b% of substance X
Mix in ratio m:n

```
Final concentration = (m×a + n×b) / (m+n) %
```

---

## 💡 Advanced Tricks

### Trick 1: Average by Deviation Method

Instead of calculating sum, use deviations from assumed average:
```
Average = Assumed avg + (Σ deviations / n)
```

**Example**: Find average of 47, 52, 48, 53, 50
```
Assume avg = 50
Deviations: -3, +2, -2, +3, 0
Sum of deviations = 0
Average = 50 + 0/5 = 50
```

---

### Trick 2: Alligation for Averages

Works for any weighted average problem!

**Example**: Class A (30 students) avg 60, Class B (20 students) avg 80. Combined avg?
```
     60 ———— 80
         Avg
        |         |
    80-A=30   A-60=20

30:20 = 3:2 gives the split from 80 and 60
Avg = 60 + 20×2/(2+3) = 60 + 8 = 68
OR = 80 - 20×3/(3+2) = 80 - 12 = 68
```

---

### Trick 3: Quick Mean of Arithmetic Progression

```
Average of AP = (First term + Last term) / 2
             = First term + (n-1)d/2
             = Middle term (if n is odd)
```

---

### Trick 4: Average Speed

**If same distance at different speeds**:
```
Average Speed = 2×S₁×S₂ / (S₁+S₂) (for two distances)
             = n / (1/S₁ + 1/S₂ + ... + 1/Sₙ) (Harmonic Mean)
```

**⚠️ NOT (S₁+S₂)/2** unless time is same!

---

### Trick 5: Finding Number of Items Above/Below Average

If total items = n, average = A, and we know:
```
Sum of items above avg = Items above × (their avg)
Sum of items below avg = Items below × (their avg)
Both must balance around the total average
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Average of Averages ≠ Overall Average
```
❌ Avg of (A₁ and A₂) = (A₁ + A₂)/2 (only if counts are equal)
✅ Use weighted average formula
```

### Trap 2: Speed Average
```
❌ Average of 40 km/h and 60 km/h = 50 km/h
✅ For same distance: 2×40×60/(40+60) = 48 km/h
```

### Trap 3: Concentration After Mixing
```
Always maintain mass balance:
Solute before = Solute after
```

### Trap 4: Replacement Reduces Original
```
In repeated replacement, original substance never becomes zero
(it approaches zero asymptotically)
```

### Edge Case: One Component is Zero
```
Mixing pure substance with pure diluent
Use same formulas - concentration of one is 100%, other is 0%
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| Simple Average | Σx/n |
| Combined Average | (n₁A₁ + n₂A₂)/(n₁+n₂) |
| Weighted Average | Σ(wᵢxᵢ)/Σwᵢ |
| Alligation Ratio | (P₂-M):(M-P₁) |
| Repeated Dilution | V(1-x/V)ⁿ |
| New member value | New avg + n(New-Old) |
| Replacement | New-Old = n(New avg - Old avg) |
| Average Speed (same dist) | 2S₁S₂/(S₁+S₂) |

---

## 📝 GATE-Level Practice

**Q1**: Average of 11 numbers is 50. Average of first 6 is 49, last 6 is 52. Find 6th number.
```
Total = 11 × 50 = 550
First 6 sum = 6 × 49 = 294
Last 6 sum = 6 × 52 = 312
6th number = 294 + 312 - 550 = 56
```

**Q2**: In what ratio must water be mixed with milk at ₹60/L to reduce price to ₹48/L?
```
Alligation: Water=0, Milk=60, Mix=48
Ratio = (60-48):(48-0) = 12:48 = 1:4
```

**Q3**: A vessel has 60L of milk. 12L removed, replaced with water, done 3 times. Milk remaining?
```
Milk = 60 × (1 - 12/60)³ = 60 × (0.8)³ = 60 × 0.512 = 30.72L
```

**Q4**: Average of 20 numbers is 35. It was found that two numbers 45 and 55 were read as 25 and 35. Correct average?
```
Error = (45-25) + (55-35) = 20 + 20 = 40
Correct sum = 20×35 + 40 = 740
Correct average = 740/20 = 37
```

---

*← [Chapter 5 - Ratio & Proportion](./05_Ratio_Proportion.md) | [Chapter 7 - Time & Work →](./07_Time_Work.md)*
