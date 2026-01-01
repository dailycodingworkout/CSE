# 📊 Averages and Mixtures | The Singularity

> **The Atomic Truth:** *Average is the balancing point; mixture is weighted combination.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Simple Averages](#simple-averages)
3. [Weighted Averages](#weighted-averages)
4. [Change in Average](#change-in-average)
5. [Mixtures](#mixtures)
6. [Alligation Rule](#alligation-rule)
7. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
8. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
9. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Averages & Mixtures Matter?
This topic appears frequently in:
- Data Interpretation sets
- Age-based problems
- Salary/expenditure problems
- Mixture problems in chemistry context

### Basic Definitions

**Average (Arithmetic Mean):**
$$\text{Average} = \frac{\text{Sum of all observations}}{\text{Number of observations}}$$

**Weighted Average:**
$$\text{Weighted Average} = \frac{\sum (w_i \times x_i)}{\sum w_i}$$

---

## Simple Averages

### The Core Formula

$$\bar{x} = \frac{x_1 + x_2 + x_3 + ... + x_n}{n} = \frac{\sum x_i}{n}$$

### Key Properties

1. **Sum = Average × Count**
   $$\sum x_i = \bar{x} \times n$$

2. **Average of first n natural numbers:**
   $$\text{Average} = \frac{n + 1}{2}$$

3. **Average of first n even numbers:**
   $$\text{Average} = n + 1$$

4. **Average of first n odd numbers:**
   $$\text{Average} = n$$

5. **Average of squares of first n natural numbers:**
   $$\text{Average} = \frac{(n+1)(2n+1)}{6}$$

### Average of Consecutive Numbers

| Type | Average |
|------|---------|
| n consecutive numbers | Middle term or average of two middle terms |
| n consecutive odd/even | Also middle term(s) |
| AP series | $\frac{\text{First term + Last term}}{2}$ |

> **💡 The Golden Pivot:** For any AP, Average = (First + Last)/2 = Middle term

---

## Weighted Averages

### When to Use
Use weighted average when:
- Different groups have different sizes
- Different items have different importance
- Combining two or more groups

### Formula
$$\bar{x}_w = \frac{n_1 x_1 + n_2 x_2 + ... + n_k x_k}{n_1 + n_2 + ... + n_k}$$

### Example 1: Class Average
Class A (30 students) has average marks 60.
Class B (20 students) has average marks 80.
Combined average?

$$\bar{x} = \frac{30 \times 60 + 20 \times 80}{30 + 20} = \frac{1800 + 1600}{50} = \frac{3400}{50} = 68$$

### Example 2: Speed Average

If a person travels:
- Distance $d_1$ at speed $s_1$
- Distance $d_2$ at speed $s_2$

**Average speed (by distance):**
$$\bar{s} = \frac{d_1 + d_2}{\frac{d_1}{s_1} + \frac{d_2}{s_2}}$$

**For equal distances:**
$$\bar{s} = \frac{2 s_1 s_2}{s_1 + s_2}$$ (Harmonic mean)

**For equal times:**
$$\bar{s} = \frac{s_1 + s_2}{2}$$ (Arithmetic mean)

---

## Change in Average

### Adding a New Element

When a new element $x_{n+1}$ is added to n numbers with average $\bar{x}$:

$$\text{New Average} = \frac{n \bar{x} + x_{n+1}}{n + 1}$$

**Change in average:**
$$\Delta \bar{x} = \frac{x_{n+1} - \bar{x}}{n + 1}$$

### Removing an Element

When an element $x_k$ is removed from n numbers with average $\bar{x}$:

$$\text{New Average} = \frac{n \bar{x} - x_k}{n - 1}$$

### Replacing an Element

When $x_{\text{old}}$ is replaced by $x_{\text{new}}$:

$$\text{Change in average} = \frac{x_{\text{new}} - x_{\text{old}}}{n}$$

### Example
Average of 10 numbers is 15. If one number (10) is replaced by 40:
$$\text{Change} = \frac{40 - 10}{10} = 3$$
New average = 15 + 3 = 18

---

## Mixtures

### Type 1: Simple Mixture

Mixing quantities $q_1$ and $q_2$ of ingredients with concentrations $c_1$ and $c_2$:

$$\text{Resultant concentration} = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}$$

### Type 2: Repeated Dilution/Replacement

If a container has $V$ liters of liquid A, and $x$ liters is replaced with liquid B, done $n$ times:

$$\text{Amount of A remaining} = V \left(1 - \frac{x}{V}\right)^n$$

$$\text{Concentration of A} = \left(1 - \frac{x}{V}\right)^n$$

### Example
50L of milk. 5L removed and replaced with water, done 2 times.
$$\text{Milk remaining} = 50 \times \left(1 - \frac{5}{50}\right)^2 = 50 \times (0.9)^2 = 50 \times 0.81 = 40.5L$$

---

## Alligation Rule

### The Powerful Shortcut

For mixing two ingredients at prices/concentrations $C_1$ (cheaper) and $C_2$ (dearer) to get mean $C_m$:

$$\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{C_2 - C_m}{C_m - C_1}$$

### The Cross Diagram

```
    C₁ (Cheaper)              C₂ (Dearer)
              \               /
               \             /
                \           /
                 Cₘ (Mean)
                /           \
               /             \
              /               \
        |C₂ - Cₘ|           |Cₘ - C₁|
```

**Quantity ratio = (C₂ - Cₘ) : (Cₘ - C₁)**

### Example 1: Price Mixing
Rice at ₹20/kg mixed with rice at ₹30/kg to get mixture at ₹23/kg.

Ratio = (30-23) : (23-20) = 7 : 3

So 7 parts of cheaper + 3 parts of dearer

### Example 2: Concentration Problems
40% alcohol solution mixed with 60% alcohol solution to get 48% solution.

Ratio = (60-48) : (48-40) = 12 : 8 = 3 : 2

### Example 3: Finding Cost
Type A (₹x) and Type B (₹15) mixed in ratio 2:3 gives mixture worth ₹12.

Using alligation: 
- (15-12) : (12-x) = 2 : 3
- 3 × 3 = 2 × (12-x)
- 9 = 24 - 2x
- x = ₹7.5

---

## GATE & ESE Problem Patterns

### Pattern 1: Average with Inclusion/Exclusion
> Average age of 30 students is 15 years. When teacher is included, average becomes 16. Find teacher's age.
- Sum of students = 30 × 15 = 450
- New sum = 31 × 16 = 496
- Teacher's age = 496 - 450 = **46 years**

### Pattern 2: Runs/Cricket Average
> A batsman has average of 40 runs in 10 innings. How many runs in 11th innings to have average of 45?
- Current total = 40 × 10 = 400
- Required total = 45 × 11 = 495
- Runs needed = 495 - 400 = **95 runs**

### Pattern 3: False Measurement
> Average weight of 20 students was calculated as 60 kg. Later, it was found that one weight was read as 57 kg instead of 75 kg. Find correct average.
- Error = 75 - 57 = 18 kg
- Correct sum = 20 × 60 + 18 = 1218 kg
- Correct average = 1218/20 = **60.9 kg**

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"Average of 5 consecutive even numbers is 10. Find the largest number."

Wrong approach: Thinking largest = 10 + 4 = 14

**The Elegant Solution:**
- Let numbers be: (n-4), (n-2), n, (n+2), (n+4)
- Average = n = 10
- Largest = 10 + 4 = **14**

Actually, in this case the answer is 14, but let's verify:
Numbers: 6, 8, 10, 12, 14 → Average = 50/5 = 10 ✓

The trap occurs when students confuse consecutive integers with consecutive even/odd.

**MSQ Logic Gate:**
- For consecutive even/odd, gap is 2 (not 1)
- Average of AP is always the middle term
- Weighted average lies between the extremes

**NAT Precision Lock:**
- Average calculations often yield decimals
- Don't round intermediate steps
- Final answer precision as specified

---

## Speed Tricks & Shortcuts

### Trick 1: Deviation Method for Average

Choose an assumed mean $A$. Then:
$$\text{True Average} = A + \frac{\sum d_i}{n}$$

Where $d_i = x_i - A$

**Example:** Average of 98, 102, 97, 103, 100
- Assume A = 100
- Deviations: -2, 2, -3, 3, 0
- Sum of deviations = 0
- Average = 100 + 0/5 = **100**

### Trick 2: Quick Alligation Setup

Always put cheaper on left, dearer on right. The answer naturally comes as:
$$\text{Cheaper : Dearer} = (\text{Dearer} - \text{Mean}) : (\text{Mean} - \text{Cheaper})$$

### Trick 3: Average Speed for Equal Distances

$$\bar{s} = \frac{2 \times s_1 \times s_2}{s_1 + s_2}$$

This is the **harmonic mean**, not arithmetic mean!

### Trick 4: New Average After Addition

If adding $k$ to each number, new average = old average + $k$

If multiplying each number by $k$, new average = old average × $k$

### Trick 5: Combined Average Bounds

When combining two groups:
$$\min(avg_1, avg_2) < \text{Combined Average} < \max(avg_1, avg_2)$$

---

## Permanent Recall

### The Bizarre Mnemonic (Alligation)
*"Think of a see-saw where the cheaper kid sits far from center (more weight = more quantity) and the expensive kid sits close (less weight = less quantity). The fulcrum is the mean price!"*

### The Mental Slider
Visualize a thermometer:
- Bottom = Cheaper/Lower value
- Top = Dearer/Higher value
- Mercury level = Mean
- Distance from bottom tells you how much of dearer you need

### The 5-Second Snap-Check
- Average must lie between min and max values
- In alligation, if mean is closer to cheaper, more of cheaper is used
- Sum of group = Average × Count (quick verification)

---

## Practice Problems

### Level 1: Fundamentals
1. Find the average of first 50 natural numbers.
2. Average of 5 numbers is 20. If one number is excluded, average becomes 18. Find the excluded number.
3. In what ratio should water be mixed with milk costing ₹24/L to get mixture at ₹20/L?

### Level 2: GATE Standard
4. A train travels 360 km at uniform speed. If speed was 5 km/h more, it would have taken 1 hour less. Find original speed.
5. Average marks of 40 students is 70. Later 5 students with marks 60, 65, 70, 75, 80 are found to be of another class. What is the average of remaining 35 students?
6. A vessel contains 60L of solution with 40% acid. How much water must be added to make it 30% acid solution?

### Level 3: IIT Examiner Level
7. The average of 11 observations is 50. The average of first 5 is 52, and average of last 5 is 48. Find the 6th observation.
8. A merchant mixes 3 varieties of rice at ₹20, ₹24, and ₹30 per kg. In what ratio should he mix to get mixture at ₹26 per kg, if first two varieties are in ratio 1:2?
9. From a vessel containing 100L of wine, 10L is taken out and replaced by water. This is done 3 times. What is the ratio of wine to water in final mixture?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Average = (n+1)/2 = 51/2 = **25.5**

2. Sum of 5 = 5 × 20 = 100
   Sum of 4 = 4 × 18 = 72
   Excluded = 100 - 72 = **28**

3. Water (₹0) : Milk (₹24) for mean ₹20
   Ratio = (24-20) : (20-0) = 4 : 20 = **1:5**

4. Let speed = s km/h
   Time = 360/s
   New time = 360/(s+5)
   360/s - 360/(s+5) = 1
   360(s+5) - 360s = s(s+5)
   1800 = s² + 5s
   s² + 5s - 1800 = 0
   s = 40 km/h (taking positive root)
   **Original speed = 40 km/h**

5. Sum of 40 = 40 × 70 = 2800
   Sum of 5 excluded = 60+65+70+75+80 = 350
   Sum of 35 = 2800 - 350 = 2450
   Average = 2450/35 = **70**

6. Acid in 60L = 40% of 60 = 24L
   Let water added = x L
   New concentration: 24/(60+x) = 30/100
   2400 = 30(60+x) = 1800 + 30x
   x = 600/30 = **20L**

7. Sum of 11 = 11 × 50 = 550
   Sum of first 5 = 5 × 52 = 260
   Sum of last 5 = 5 × 48 = 240
   6th observation = 550 - 260 - 240 + (included in both) 
   Wait, 6th is counted separately.
   Actually: Sum(1-5) + x₆ + Sum(7-11) = 550
   260 + x₆ + 240 = 550
   x₆ = **50**

8. Let first:second:third = 1:2:k
   Weighted average: (1×20 + 2×24 + k×30)/(1+2+k) = 26
   (20 + 48 + 30k)/(3+k) = 26
   68 + 30k = 78 + 26k
   4k = 10
   k = 2.5
   Ratio = 1 : 2 : 2.5 = **2:4:5**

9. Wine remaining = 100 × (1 - 10/100)³ = 100 × (0.9)³ = 72.9L
   Water = 100 - 72.9 = 27.1L
   Ratio = 72.9 : 27.1 = 729 : 271 ≈ **729:271**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Averages with Time, Speed & Distance for a Rank-1 simulation?
