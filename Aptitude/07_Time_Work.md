# Chapter 7: Time & Work

> **Efficiency mathematics - the core of resource allocation problems**

---

## 🎯 Why Study This?

- Very high frequency in GATE/ESE (guaranteed questions)
- Tests logical reasoning with numbers
- Real-world: Project management, resource planning

---

## 📚 Core Concept

**Work** = Rate × Time

```
W = R × T

Or equivalently:
Rate = Work/Time = 1/Time (if total work = 1)
Time = Work/Rate
```

**💡 Analogy**: 
- Work is like filling a tank
- Rate is the tap's flow
- Time is how long the tap runs

---

## 🔧 Fundamental Approach

### The Unity Method

**Total work = 1 unit** (normalized)

If A completes work in n days:
```
A's 1 day work = 1/n (work per day rate)
A's rate = 1/n
```

---

### The LCM Method (⭐ Recommended)

**Total work = LCM of all individual times**

This avoids fractions and speeds up calculations.

**Example**: A takes 12 days, B takes 15 days
```
Total work = LCM(12, 15) = 60 units
A's rate = 60/12 = 5 units/day
B's rate = 60/15 = 4 units/day
Combined = 9 units/day
Time together = 60/9 = 6⅔ days
```

---

## 📐 Core Formulas

### Working Together

If A takes 'a' days, B takes 'b' days alone:
```
Together: 1/a + 1/b = 1/T
T = ab/(a+b) days
```

**For three workers A, B, C**:
```
1/a + 1/b + 1/c = 1/T
```

---

### Alternate Days Work

If A and B work on alternate days, starting with A:
```
Work in 2 days = A's 1 day + B's 1 day
Calculate pairs, then adjust for remaining
```

---

### Work Equivalence

```
M₁ × D₁ × H₁ × E₁ / W₁ = M₂ × D₂ × H₂ × E₂ / W₂

Where:
M = number of men
D = number of days
H = hours per day
E = efficiency
W = work done
```

---

## 📊 Standard Problem Types

### Type 1: Basic Combined Work

**Example**: A does work in 10 days, B in 15 days. Together?
```
Method 1 (Unity):
Combined rate = 1/10 + 1/15 = 5/30 = 1/6
Time = 6 days

Method 2 (LCM):
Work = 30 units
A = 3/day, B = 2/day
Together = 5/day
Time = 30/5 = 6 days
```

---

### Type 2: Work with Leaving/Joining

**Example**: A and B together can do in 12 days. A alone in 20 days. After 4 days A leaves. B finishes in?

```
LCM(12, 20) = 60 units total work
A + B rate = 60/12 = 5/day
A's rate = 60/20 = 3/day
B's rate = 5 - 3 = 2/day

Work in 4 days (together) = 4 × 5 = 20 units
Remaining = 60 - 20 = 40 units
B alone = 40/2 = 20 days
```

---

### Type 3: Negative Work (Destructive)

**Pipes & Cisterns with leak/outlet**

If inlet fills in 'a' hours, outlet empties in 'b' hours:
```
Net rate = 1/a - 1/b (inlet taken positive)
If a < b: Tank fills
If a > b: Tank empties
```

**Example**: Inlet fills in 6 hrs, outlet empties in 8 hrs. Net fill time?
```
Net rate = 1/6 - 1/8 = 4/24 - 3/24 = 1/24
Time = 24 hours
```

---

### Type 4: Efficiency Based

If A is x times as efficient as B:
```
Time ratio = B : A (inverse of efficiency)
If A is 2× efficient: A takes half the time
```

**Example**: A is 50% more efficient than B. B takes 30 days. A takes?
```
A's efficiency = 1.5 × B
A's time = 30/1.5 = 20 days
```

---

### Type 5: Work and Wages

Wages distributed in ratio of work done (or rate × time worked).

```
If work done by A, B, C in ratio a:b:c
Wages split in same ratio a:b:c
```

**Example**: A and B complete work in 10 and 15 days. Together they finish, total wage = ₹600. Distribution?
```
A's work capacity = 1/10
B's work capacity = 1/15
Ratio = 1/10 : 1/15 = 3:2
A gets = 600 × 3/5 = ₹360
B gets = 600 × 2/5 = ₹240
```

---

### Type 6: Men-Days Calculation

```
Man-days = Total work
M₁D₁ = M₂D₂ (for same work)
```

**Example**: 15 men complete work in 20 days. How many men needed for 12 days?
```
15 × 20 = M × 12
M = 25 men
```

---

### Type 7: Alternate Day/Complex Scheduling

**Example**: A works on Day 1, B on Day 2, A on Day 3... A completes in 18 days alone, B in 24 days.

```
Work = LCM(18, 24) = 72 units
A = 4 units/day, B = 3 units/day
Per 2-day cycle = 4 + 3 = 7 units
Full cycles = 72/7 = 10 cycles + 2 remaining
After 20 days = 70 units done
Day 21 (A works) = 4 units → 74 > 72
So on Day 21, A needs only 2 units = 2/4 = 0.5 day
Total = 20.5 days
```

---

## 🚰 Pipes & Cisterns

### Core Concept

Same as Time & Work, but with liquids.

```
Inlet pipe → Positive work (filling)
Outlet pipe/Leak → Negative work (emptying)
```

---

### Standard Formulas

**Two inlets, one outlet**:
```
Net rate = 1/a + 1/b - 1/c
```

**One inlet, one outlet**:
```
Net rate = 1/a - 1/b
```

---

### Finding Leak Rate

If tank fills in 'a' hours without leak, but takes 'b' hours with leak:
```
Leak rate = 1/a - 1/b = (b-a)/(ab)
Leak empties full tank in = ab/(b-a) hours
```

---

## 💡 Advanced Tricks

### Trick 1: Part Work, Part Time

If A can do 1/3 of work, and A+B do remaining, find time.

```
Step 1: Calculate time for A to do 1/3 work
Step 2: Calculate time for A+B to do 2/3 work
Step 3: Add
```

---

### Trick 2: Efficiency Percentage

```
If B is x% less efficient than A:
B's time = A's time × 100/(100-x)

If B is x% more efficient than A:
B's time = A's time × 100/(100+x)
```

---

### Trick 3: Work-Time Inverse Relationship

```
Workers × Days = Constant (for same work)
Doubling workers = Halving time
```

---

### Trick 4: Multiple Pipes Opening Sequentially

Calculate work done in each phase separately, sum must equal total work.

---

### Trick 5: Starting and Stopping Pattern

If work pattern is complex (e.g., 1 hr on, 30 min off):
```
Calculate effective rate per cycle
Find number of complete cycles
Handle remainder separately
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Don't Add Times
```
❌ A (10 days) + B (15 days) = 25 days together
✅ Add RATES, not times: 1/10 + 1/15
```

### Trap 2: Negative Efficiency
```
If someone destroys work, their rate is NEGATIVE
Net rate = Positive workers - Negative workers
```

### Trap 3: Partial Days
```
0.5 day of work is valid
Don't round prematurely
```

### Trap 4: Efficiency vs Time
```
Higher efficiency = Less time (inverse relationship)
2× efficient = 1/2 time
```

### Edge Case: Zero or Negative Net Rate
```
If outlet rate ≥ inlet rate, tank never fills
Problem might ask when tank empties instead
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| Combined work (A, B) | ab/(a+b) |
| Combined work (A, B, C) | 1/(1/a + 1/b + 1/c) |
| A alone from A+B | Time = (A+B) × B / (B - (A+B)) |
| Inlet - Outlet | 1/a - 1/b |
| Efficiency relation | Time ∝ 1/Efficiency |
| Man-Days constant | M₁D₁ = M₂D₂ |
| Work equivalence | M₁D₁H₁/W₁ = M₂D₂H₂/W₂ |
| Wages ratio | Same as work done ratio |
| x% more efficient | Time = Original × 100/(100+x) |

---

## 📝 GATE-Level Practice

**Q1**: A can do in 12 days, B in 18 days, C in 24 days. All start, A leaves after 4 days. Remaining done by B & C in?
```
Work = LCM(12,18,24) = 72 units
A = 6/day, B = 4/day, C = 3/day
4 days together = 4 × 13 = 52 units done
Remaining = 20 units
B + C = 7/day
Time = 20/7 = 2 6/7 days
```

**Q2**: Pipe A fills in 12 min, B empties in 18 min. If both open, time to fill?
```
Net rate = 1/12 - 1/18 = 3/36 - 2/36 = 1/36
Time = 36 minutes
```

**Q3**: 12 men finish work in 16 days. After 8 days, 4 more men join. Remaining work finished in?
```
Total work = 12 × 16 = 192 man-days
Work done in 8 days = 12 × 8 = 96
Remaining = 96 man-days
Men now = 16
Days = 96/16 = 6 days
```

**Q4**: A is twice as good as B. Together finish in 14 days. A alone?
```
Let B's rate = 1, A's rate = 2
Together = 3 (in same unit)
A alone = 3/2 of 14 = 21 days
```

**Q5**: Inlet fills empty tank in 4 hrs. Outlet empties full tank in 8 hrs. If both open, how long to fill half tank?
```
Net rate = 1/4 - 1/8 = 1/8 per hour
Half tank = 0.5
Time = 0.5/(1/8) = 4 hours
```

---

*← [Chapter 6 - Averages & Mixtures](./06_Averages_Mixtures.md) | [Chapter 8 - Time, Speed & Distance →](./08_Time_Speed_Distance.md)*
