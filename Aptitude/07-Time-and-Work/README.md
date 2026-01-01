# ⏰ Time and Work | The Singularity

> **The Atomic Truth:** *Work = Rate × Time; Efficiency is the rate of doing work.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Basic Formulas](#basic-formulas)
3. [Work Efficiency Method](#work-efficiency-method)
4. [Multiple Workers](#multiple-workers)
5. [Pipes and Cisterns](#pipes-and-cisterns)
6. [Wages Distribution](#wages-distribution)
7. [Alternate Days Work](#alternate-days-work)
8. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
9. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
10. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Time & Work Matters?
This topic is a **GATE favorite** because it tests:
- Understanding of rates and efficiency
- Logical problem decomposition
- Fraction manipulation skills
- Real-world project management analogies

### The Core Principle

$$\text{Work} = \text{Rate} \times \text{Time}$$

Or equivalently:
$$W = R \times T$$

Where:
- Work is usually taken as 1 (unit work)
- Rate is work done per unit time (efficiency)
- Time is duration

### Key Insight

If A can complete work in $n$ days:
$$\text{A's rate (efficiency)} = \frac{1}{n} \text{ (work per day)}$$

> **💡 The Golden Pivot:** Work capacity is INVERSELY proportional to time taken.

---

## Basic Formulas

### One-Day Work
$$\text{One day's work} = \frac{1}{\text{Days to complete}}$$

### Days to Complete
$$\text{Days} = \frac{1}{\text{Daily work rate}}$$

### Combined Work Rate
If A and B work together:
$$\text{Combined rate} = \text{Rate}_A + \text{Rate}_B = \frac{1}{a} + \frac{1}{b}$$

Time when working together:
$$T_{together} = \frac{ab}{a + b}$$

### Three Workers Together
$$T_{A+B+C} = \frac{abc}{ab + bc + ca}$$

Or more generally:
$$\frac{1}{T_{total}} = \frac{1}{a} + \frac{1}{b} + \frac{1}{c}$$

---

## Work Efficiency Method

### The LCM Technique

Instead of working with fractions, assume **Total Work = LCM of all time values**.

**Example:** A completes in 10 days, B in 15 days. Time together?

**Traditional Method:**
$$\frac{1}{10} + \frac{1}{15} = \frac{3 + 2}{30} = \frac{5}{30} = \frac{1}{6}$$
Time = 6 days

**LCM Method:**
- Total work = LCM(10, 15) = 30 units
- A's efficiency = 30/10 = 3 units/day
- B's efficiency = 30/15 = 2 units/day
- Combined = 5 units/day
- Time = 30/5 = **6 days**

> **Advantage:** LCM method avoids fractions and is faster!

### Efficiency Comparison

| Person | Days | If LCM = 60 | Efficiency |
|--------|------|-------------|------------|
| A | 10 | 60/10 | 6 units/day |
| B | 12 | 60/12 | 5 units/day |
| C | 15 | 60/15 | 4 units/day |
| D | 20 | 60/20 | 3 units/day |

---

## Multiple Workers

### When One Leaves/Joins Midway

**Scenario:** A and B start together. After some days, one leaves.

**Method:**
1. Let B leave after $x$ days
2. Work done by A+B in $x$ days
3. Remaining work done by A alone
4. Set up equation and solve

**Example:** A can do in 20 days, B in 30 days. They start together but B leaves 5 days before completion. Total days?

- A's rate = 1/20, B's rate = 1/30
- Let total days = $t$
- A works for $t$ days, B works for $(t-5)$ days
- $\frac{t}{20} + \frac{t-5}{30} = 1$
- $\frac{3t + 2(t-5)}{60} = 1$
- $3t + 2t - 10 = 60$
- $5t = 70$
- $t = 14$ days

### Man-Days Concept

$$\text{Total Work} = \text{Number of Men} \times \text{Days} \times \text{Hours per day}$$

$$M_1 D_1 H_1 = M_2 D_2 H_2$$

**Example:** 10 men complete work in 12 days working 8 hours/day. How many men for 6 days at 10 hours/day?
$$10 \times 12 \times 8 = M \times 6 \times 10$$
$$M = \frac{960}{60} = 16 \text{ men}$$

---

## Pipes and Cisterns

### The Concept
- **Inlet pipe:** Fills the tank (positive work)
- **Outlet pipe/Leak:** Empties the tank (negative work)

### Formulas

If inlet fills in $a$ hours and outlet empties in $b$ hours:

**Both open (inlet stronger, $a < b$):**
$$\text{Time to fill} = \frac{ab}{b - a}$$

**Both open (outlet stronger, $b < a$):**
$$\text{Time to empty} = \frac{ab}{a - b}$$

### Example
Pipe A fills in 10 hours, pipe B empties in 15 hours. Both open, time to fill?

- Combined rate = $\frac{1}{10} - \frac{1}{15} = \frac{3-2}{30} = \frac{1}{30}$
- Time to fill = **30 hours**

### Multiple Pipes

$$\text{Net rate} = \sum(\text{Inlet rates}) - \sum(\text{Outlet rates})$$

---

## Wages Distribution

### The Principle
**Wages are distributed in the ratio of work done.**

$$\frac{\text{A's wage}}{\text{B's wage}} = \frac{\text{A's work}}{\text{B's work}}$$

### When Efficiency Differs

If A is twice as efficient as B and total wages are ₹600:
- Work ratio = 2:1
- A gets ₹400, B gets ₹200

### When Time Differs

If A works for 10 days and B for 15 days (same efficiency):
- Work ratio = 10:15 = 2:3
- Wages in ratio 2:3

### Combined Effect

$$\text{Work done} = \text{Efficiency} \times \text{Time worked}$$

---

## Alternate Days Work

### Type 1: A and B Work on Alternate Days

**A starts:**
- Day 1: A works
- Day 2: B works
- Day 3: A works... and so on

**Approach:**
1. Find work done in 2 days (one cycle)
2. Find complete cycles
3. Handle remaining work

**Example:** A completes in 6 days, B in 12 days. A starts. Total time?

Using LCM = 12 units total:
- A's rate = 2 units/day
- B's rate = 1 unit/day
- Work in 2 days = 2 + 1 = 3 units
- Complete cycles = 12/3 = 4 (exactly)
- Total days = 4 × 2 = **8 days**

### Type 2: A Works for Some Days, Then B

**Example:** A does 1/3 of work, then B finishes rest. A takes 10 days for full work, B takes 15 days.

- A does 1/3 in: (1/3) ÷ (1/10) = 10/3 days
- B does 2/3 in: (2/3) ÷ (1/15) = 10 days
- Total = 10/3 + 10 = **40/3 days ≈ 13.33 days**

---

## GATE & ESE Problem Patterns

### Pattern 1: Basic Combined Work
> A does work in 10 days, B in 15 days. Together in?
$$T = \frac{10 \times 15}{10 + 15} = \frac{150}{25} = 6 \text{ days}$$

### Pattern 2: Three Workers
> A, B, C can do in 10, 12, 15 days. A+B work for 2 days, then C joins. Total time?

LCM(10,12,15) = 60 units
- A = 6 units/day, B = 5 units/day, C = 4 units/day
- A+B in 2 days = 2(6+5) = 22 units
- Remaining = 60 - 22 = 38 units
- A+B+C rate = 15 units/day
- Time for remaining = 38/15 = 2.53 days
- Total = 2 + 2.53 = **4.53 days**

### Pattern 3: Efficiency Ratio
> A is twice as efficient as B. Together they take 12 days. B alone in?

Let B's efficiency = 1, A's efficiency = 2
- Combined efficiency = 3
- Total work = 3 × 12 = 36 units
- B alone = 36/1 = **36 days**

### Pattern 4: Pipes with Leak
> A pipe fills in 8 hours. Due to leak, it takes 10 hours. Leak alone empties in?

- Pipe rate = 1/8
- Combined rate = 1/10
- Leak rate = 1/8 - 1/10 = 2/80 = 1/40
- Leak empties in **40 hours**

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"A and B can do work in 12 and 18 days. They work together for 4 days. A leaves. How many more days for B?"

Wrong approach: Thinking B takes 18 - 4 = 14 more days

**The Elegant Solution:**
- LCM(12, 18) = 36 units
- A = 3 units/day, B = 2 units/day
- Work in 4 days = 4(3+2) = 20 units
- Remaining = 36 - 20 = 16 units
- B alone = 16/2 = **8 more days**

**MSQ Logic Gate:**
- Combined work rate is additive (unless opposing like leak)
- Efficiency and time are inversely related
- "More efficient" means less time, not more

**NAT Precision Lock:**
- Time can be fractional (e.g., 4.5 days)
- Express answer as specified (days, hours, or fraction)

---

## Speed Tricks & Shortcuts

### Trick 1: The LCM Master Method
Always take LCM of all time values as total work. This eliminates all fractions!

### Trick 2: Efficiency Ratio
If A is $k$ times as efficient as B, and A takes $a$ days:
- B takes $ka$ days
- Together: $\frac{ka}{k+1}$ days

### Trick 3: Two Workers Shortcut
$$T_{together} = \frac{T_A \times T_B}{T_A + T_B}$$

This is the formula for **parallel resistance** in circuits!

### Trick 4: Quick Pipe Calculations
- Net rate = |Fill rate - Drain rate|
- Positive net = filling, Negative net = emptying

### Trick 5: Alternate Days Pattern
In 2-day cycles:
- Work per cycle = Work₁ + Work₂
- Number of cycles = Total work ÷ Work per cycle

---

## Permanent Recall

### The Bizarre Mnemonic (Work Rate)
*"Think of workers as water taps filling a bucket. Each tap has its own flow rate. Together, their flows ADD UP. But a leak is a hole at the bottom—it drains at its own rate, SUBTRACTING from the total flow."*

### The Mental Slider
Visualize a progress bar:
- Each worker fills it at different speeds
- Working together = multiple arrows pushing the bar
- Leak = an arrow pulling it back

### The 5-Second Snap-Check
- Combined time < Individual time (always, when helping)
- If A alone takes 10 days, A+B < 10 days
- Pipes: Fill rate > Leak rate for filling

---

## Practice Problems

### Level 1: Fundamentals
1. A can do work in 15 days, B in 20 days. Together in how many days?
2. A pipe fills a tank in 6 hours, another empties in 8 hours. Both open, time to fill?
3. 12 men can do work in 10 days. How many men to do it in 8 days?

### Level 2: GATE Standard
4. A is twice as efficient as B. A alone takes 15 days. A and B together take how many days?
5. A and B can do work in 10 and 15 days. They start together, A leaves after 4 days. B finishes remaining in?
6. Three pipes A, B, C can fill in 6, 9, 12 hours. All open for 2 hours, then C is closed. Time to fill remaining?

### Level 3: IIT Examiner Level
7. 10 men can do work in 10 days. 10 women can do same in 15 days. If 6 men and 8 women work together, how many days?
8. A alone does in 20 days, B in 25 days. They work for 5 days, then A leaves. C finishes remaining in 6 days. C alone?
9. A pipe can fill in 12 hours. Due to leak, it fills in 20 hours. When tank is full, if inlet is closed, how long to empty by leak?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. T = (15 × 20)/(15 + 20) = 300/35 = **60/7 days ≈ 8.57 days**

2. Net rate = 1/6 - 1/8 = (4-3)/24 = 1/24
   Time = **24 hours**

3. M₁D₁ = M₂D₂
   12 × 10 = M × 8
   M = **15 men**

4. B takes 2 × 15 = 30 days
   Together = (15 × 30)/(15 + 30) = 450/45 = **10 days**

5. LCM(10,15) = 30 units
   A = 3 units/day, B = 2 units/day
   4 days together = 4 × 5 = 20 units done
   Remaining = 10 units, B alone = 10/2 = **5 days**

6. LCM(6,9,12) = 36 units
   A = 6, B = 4, C = 3 units/hour
   In 2 hours with all: 2 × 13 = 26 units
   Remaining = 10 units, A+B rate = 10
   Time = 10/10 = 1 hour
   Total = 2 + 1 = **3 hours**

7. 1 man's 1 day = 1/100 work
   1 woman's 1 day = 1/150 work
   6 men + 8 women daily = 6/100 + 8/150 = 9/150 + 8/150 = 17/150
   Days = 150/17 ≈ **8.82 days**

8. LCM(20,25) = 100 units (we'll use this)
   A = 5 units/day, B = 4 units/day
   5 days together = 5 × 9 = 45 units
   Remaining = 55 units
   C does 55 in 6 days → C's rate = 55/6 units/day
   C alone = 100 ÷ (55/6) = 600/55 = **120/11 days ≈ 10.91 days**

9. Inlet rate = 1/12
   Combined rate = 1/20
   Leak rate = 1/12 - 1/20 = (5-3)/60 = 2/60 = 1/30
   Leak empties full tank in **30 hours**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Time & Work with Time, Speed & Distance for a Rank-1 simulation?
