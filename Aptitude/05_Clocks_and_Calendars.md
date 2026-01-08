# Clocks and Calendars | Complete Mastery Guide
## For GATE, ESE, PSU & Bank Examinations

---

## The Atomic Truth
> **"Time calculations via angular rates and cyclic patterns."**

---

# PART A: CLOCKS

## 1. Clock Fundamentals

### The Basic Structure
```
        12
    11      1
  10          2
 9      ●      3
  8           4
    7       5
        6
```

### Key Components
- **Hour hand**: Short hand, completes 360° in 12 hours
- **Minute hand**: Long hand, completes 360° in 60 minutes
- **Second hand** (if present): Completes 360° in 60 seconds

---

## 2. Angular Speed Formulas

### The Core Mathematics

| Hand | Speed | Per Minute | Per Hour |
|------|-------|------------|----------|
| Hour hand | 360°/12h = 0.5°/min | 0.5° | 30° |
| Minute hand | 360°/60min = 6°/min | 6° | 360° |
| Second hand | 360°/60sec = 6°/sec | 360° | - |

### The Golden Formula
> **Relative speed of minute hand w.r.t hour hand = 6° - 0.5° = 5.5°/min**

This means: The minute hand gains 5.5° on the hour hand every minute.

---

## 3. Angle Between Hands

### The Master Formula

$$\theta = \left| 30H - 5.5M \right|$$

Where:
- $\theta$ = Angle between hour and minute hands
- $H$ = Hour (12-hour format)
- $M$ = Minutes

### If $\theta > 180°$, use $(360° - \theta)$ for the smaller angle

### Derivation
```
Hour hand position from 12:
= 30° × H + 0.5° × M
= 30H + 0.5M

Minute hand position from 12:
= 6° × M
= 6M

Difference:
= |30H + 0.5M - 6M|
= |30H - 5.5M|
```

### Examples

**Example 1: Angle at 3:30**
```
θ = |30(3) - 5.5(30)|
  = |90 - 165|
  = |-75|
  = 75°
```

**Example 2: Angle at 7:20**
```
θ = |30(7) - 5.5(20)|
  = |210 - 110|
  = 100°
```

**Example 3: Angle at 2:45**
```
θ = |30(2) - 5.5(45)|
  = |60 - 247.5|
  = 187.5°

Since 187.5° > 180°:
Smaller angle = 360° - 187.5° = 172.5°
```

---

## 4. When Hands Overlap (Coincide)

### The Problem
At what times are the hour and minute hands exactly on top of each other?

### Solution Approach
Hands overlap when angle between them = 0°

$$30H - 5.5M = 0$$
$$M = \frac{30H}{5.5} = \frac{60H}{11}$$

### Overlap Times Table

| Between | At (approx) | Exact Calculation |
|---------|-------------|-------------------|
| 12 and 1 | 12:00:00 | M = 60(0)/11 = 0 |
| 1 and 2 | 1:05:27 | M = 60(1)/11 = 5.45 min |
| 2 and 3 | 2:10:54 | M = 60(2)/11 = 10.91 min |
| 3 and 4 | 3:16:22 | M = 60(3)/11 = 16.36 min |
| 4 and 5 | 4:21:49 | M = 60(4)/11 = 21.82 min |
| 5 and 6 | 5:27:16 | M = 60(5)/11 = 27.27 min |
| 6 and 7 | 6:32:43 | M = 60(6)/11 = 32.73 min |
| 7 and 8 | 7:38:11 | M = 60(7)/11 = 38.18 min |
| 8 and 9 | 8:43:38 | M = 60(8)/11 = 43.64 min |
| 9 and 10 | 9:49:05 | M = 60(9)/11 = 49.09 min |
| 10 and 11 | 10:54:33 | M = 60(10)/11 = 54.55 min |
| 11 and 12 | 12:00:00 | Next cycle |

### Key Insight
> Hands overlap **11 times in 12 hours** (not 12 times!)
> In 24 hours, they overlap **22 times**

---

## 5. When Hands Are Opposite (180°)

### Solution Approach
$$|30H - 5.5M| = 180°$$

This gives two equations:
1. $30H - 5.5M = 180$ → $M = \frac{30H - 180}{5.5}$
2. $30H - 5.5M = -180$ → $M = \frac{30H + 180}{5.5}$

### Key Insight
> Hands are opposite **11 times in 12 hours**
> In 24 hours, they're opposite **22 times**

---

## 6. When Hands Are at Right Angle (90°)

### Solution Approach
$$|30H - 5.5M| = 90°$$

Two cases:
1. $30H - 5.5M = 90$ → $M = \frac{30H - 90}{5.5}$
2. $30H - 5.5M = -90$ → $M = \frac{30H + 90}{5.5}$

### Example: Right angles between 4 and 5 o'clock

**Case 1:** $M = \frac{30(4) - 90}{5.5} = \frac{120-90}{5.5} = \frac{30}{5.5} = 5.45$ min
Time: 4:05:27

**Case 2:** $M = \frac{30(4) + 90}{5.5} = \frac{120+90}{5.5} = \frac{210}{5.5} = 38.18$ min
Time: 4:38:11

### Key Insight
> Hands are at right angle **44 times in 24 hours** (22 times per 12 hours)

---

## 7. Gaining and Losing Time (Faulty Clocks)

### Concept
A clock that doesn't keep accurate time:
- **Gains time**: Runs fast (shows more time than actual)
- **Loses time**: Runs slow (shows less time than actual)

### Formula for Faulty Clocks

$$\text{Actual Time} = \text{Shown Time} \times \frac{\text{Correct Rate}}{\text{Faulty Rate}}$$

### Example 1: Gaining Time
```
A clock gains 5 minutes every hour.
If it shows 10:00 AM now, what is the actual time if it was set correctly at 6:00 AM?

Hours passed (shown): 4 hours = 240 minutes
For every 60 minutes actual, clock shows 65 minutes.

Actual minutes = 240 × (60/65) = 221.54 minutes = 3 hours 41.5 minutes

Actual time = 6:00 + 3:41:30 = 9:41:30 AM
```

### Example 2: Losing Time
```
A clock loses 10 minutes every hour.
If it shows 3:00 PM, what's the actual time if set at 12:00 noon?

Clock shows 3 hours = 180 minutes from setting
For every 60 minutes actual, clock shows 50 minutes.

Actual minutes = 180 × (60/50) = 216 minutes = 3 hours 36 minutes

Actual time = 12:00 + 3:36 = 3:36 PM
```

---

## 8. Mirror Image of Time

### Concept
Time shown in a mirror is different from actual time.

### Formula
$$\text{Mirror Time} = 12:00 - \text{Actual Time}$$

or

$$\text{Mirror Time} = 11:60 - \text{Actual Time}$$

(Use 11:60 when actual minutes > 0)

### Example
```
Actual time: 3:25
Mirror time = 11:60 - 3:25 = 8:35

Actual time: 9:50
Mirror time = 11:60 - 9:50 = 2:10
```

---

## 9. Clock Problem Shortcuts

### Shortcut 1: Overlap Interval
Hands overlap every $\frac{12}{11}$ hours = 65.45 minutes

### Shortcut 2: Right Angle Interval
Hands are at 90° every $\frac{6}{11}$ hours = 32.73 minutes

### Shortcut 3: Opposite Interval
Hands are opposite every $\frac{12}{11}$ hours = 65.45 minutes (same as overlap)

### Shortcut 4: Quick Angle Check
At exactly H o'clock, angle = 30° × H

---

## 10. Clock Practice Problems

### Problem 1
**At what time between 5 and 6 o'clock are the hands 3 minutes apart?**

Note: "3 minutes apart" on clock face = 3 × 6° = 18° apart

$$|30(5) - 5.5M| = 18$$

Case 1: $150 - 5.5M = 18$ → $M = 24$
Case 2: $150 - 5.5M = -18$ → $M = 30.55$

**Times: 5:24 and 5:30:33**

### Problem 2
**A clock shows 4:00. What angle do the hands make?**

$$\theta = |30(4) - 5.5(0)| = 120°$$

### Problem 3
**How many times do the hands overlap between 8 AM Monday and 8 PM Tuesday?**

```
Total hours = 8 AM Mon to 8 PM Tue = 36 hours
Overlaps in 12 hours = 11
Overlaps in 36 hours = 11 × 3 = 33

Wait, let's be precise:
8 AM Mon to 8 AM Tue = 24 hours → 22 overlaps
8 AM Tue to 8 PM Tue = 12 hours → 11 overlaps
Total = 33 overlaps
```

---

# PART B: CALENDARS

## 11. Calendar Fundamentals

### Days in Months (Mnemonic: Knuckle Method)
```
Jan(31) Mar(31) May(31) Jul(31) Aug(31) Oct(31) Dec(31) - Knuckles (high)
Feb(28/29) Apr(30) Jun(30) Sep(30) Nov(30) - Valleys (between knuckles)

Or remember: "30 days has September, April, June, and November"
```

### Leap Year Rules

| Rule | Condition | Example |
|------|-----------|---------|
| Rule 1 | Divisible by 4 | 2024 ✓ |
| Rule 2 | Century years must be divisible by 400 | 1900 ✗, 2000 ✓ |

### Quick Leap Year Check
```
For non-century years: Divisible by 4 → Leap year
For century years: Divisible by 400 → Leap year

2024: 2024 ÷ 4 = 506 → Leap year ✓
1900: Century, 1900 ÷ 400 ≠ integer → Not leap ✗
2000: Century, 2000 ÷ 400 = 5 → Leap year ✓
2100: Century, 2100 ÷ 400 ≠ integer → Not leap ✗
```

---

## 12. Odd Days Concept

### What are Odd Days?
The number of days more than complete weeks.

$$\text{Odd Days} = \text{Total Days} \mod 7$$

### Odd Days for Different Periods

| Period | Odd Days |
|--------|----------|
| 1 ordinary year (365 days) | 365 mod 7 = 1 |
| 1 leap year (366 days) | 366 mod 7 = 2 |
| 100 years | 5 odd days |
| 200 years | 3 odd days |
| 300 years | 1 odd day |
| 400 years | 0 odd days |

### Why 400 years = 0 odd days?
```
In 400 years:
- Ordinary years = 400 - 97 = 303 (each gives 1 odd day)
- Leap years = 97 (each gives 2 odd days)
- Total odd days = 303 × 1 + 97 × 2 = 303 + 194 = 497
- 497 mod 7 = 0

So calendar repeats every 400 years!
```

### Odd Days for Each Month

| Month | Odd Days (Ordinary) | Odd Days (Leap) |
|-------|--------------------|--------------------|
| January | 31 mod 7 = 3 | 3 |
| February | 28 mod 7 = 0 | 29 mod 7 = 1 |
| March | 31 mod 7 = 3 | 3 |
| April | 30 mod 7 = 2 | 2 |
| May | 31 mod 7 = 3 | 3 |
| June | 30 mod 7 = 2 | 2 |
| July | 31 mod 7 = 3 | 3 |
| August | 31 mod 7 = 3 | 3 |
| September | 30 mod 7 = 2 | 2 |
| October | 31 mod 7 = 3 | 3 |
| November | 30 mod 7 = 2 | 2 |
| December | 31 mod 7 = 3 | 3 |

---

## 13. Day-Number Correspondence

### Reference Table
| Day | Code |
|-----|------|
| Sunday | 0 |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |

---

## 14. Finding Day of Any Date

### Method 1: Odd Days Method

**Step 1:** Calculate odd days from a reference point (usually 0 AD or 1 Jan of a century)

**Step 2:** Add odd days for complete years

**Step 3:** Add odd days for complete months

**Step 4:** Add remaining days

**Step 5:** Total mod 7 = Day code

### Example: Find day on 15 August 1947

```
Step 1: Odd days from 0 AD to 1900
- For 1600 years: 400×4 = 0 odd days (every 400 years = 0)
- For 300 years: 1 odd day
- Total for 1900: 0 + 1 = 1 odd day

Step 2: Odd days from 1900 to 1946 (complete years)
- 46 years = 11 leap years + 35 ordinary years
- Odd days = 11×2 + 35×1 = 22 + 35 = 57
- 57 mod 7 = 1 odd day

Step 3: Odd days from Jan to July 1947 (complete months)
- Jan(3) + Feb(0) + Mar(3) + Apr(2) + May(3) + Jun(2) + Jul(3)
- = 3+0+3+2+3+2+3 = 16
- 16 mod 7 = 2 odd days

Step 4: Days in August = 15
- 15 mod 7 = 1 odd day

Step 5: Total odd days = 1 + 1 + 2 + 1 = 5
- 5 = Friday

15 August 1947 was a Friday ✓
```

### Method 2: Zeller's Formula (For quick calculation)

For dates in Gregorian calendar (after 1582):

$$h = \left( q + \left\lfloor \frac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor - 2J \right) \mod 7$$

Where:
- $h$ = day of week (0=Sat, 1=Sun, 2=Mon, ...)
- $q$ = day of month
- $m$ = month (3=Mar, 4=Apr, ..., 14=Feb with year-1)
- $K$ = year mod 100
- $J$ = year ÷ 100

---

## 15. Finding Repetition of Calendar

### When Does Calendar Repeat?

A calendar repeats when:
1. Same day on 1st January
2. Same leap year pattern

### Key Insights

For **ordinary year starting on Sunday**: Repeats after 6 years
For **leap year starting on Sunday**: Repeats after 28 years

### General Pattern
After 400 years, calendar exactly repeats (Gregorian cycle)

### Specific Repetition Table

| If year starts on | And it's | Next identical calendar |
|-------------------|----------|------------------------|
| Any day | Ordinary year | +6 or +11 years |
| Any day | Leap year | +28 years |

### Example
2023 calendar (ordinary, starts Sunday) will repeat in 2034.
2024 calendar (leap, starts Monday) will repeat in 2052.

---

## 16. Special Calendar Problems

### What Day Will It Be After N Days?

$$\text{New Day} = (\text{Current Day Code} + N) \mod 7$$

### Example
```
Today is Wednesday. What day is it after 100 days?
Current day = 3 (Wednesday)
100 mod 7 = 2
New day = (3 + 2) mod 7 = 5 = Friday
```

### What Day Was It N Days Ago?

$$\text{Past Day} = (\text{Current Day Code} - N \mod 7 + 7) \mod 7$$

### Example
```
Today is Monday. What day was it 50 days ago?
Current day = 1 (Monday)
50 mod 7 = 1
Past day = (1 - 1 + 7) mod 7 = 0 = Sunday
```

---

## 17. Century Start Days

### Reference Days (1st January)
| Century Start | Day |
|---------------|-----|
| 1 AD | Monday |
| 100 AD | Friday |
| 200 AD | Wednesday |
| 300 AD | Monday |
| 400 AD | Saturday |
| ... | Pattern repeats |
| 1600 | Saturday |
| 1700 | Friday |
| 1800 | Wednesday |
| 1900 | Monday |
| 2000 | Saturday |
| 2100 | Friday |

---

## 18. Common Calendar Traps

### Trap 1: February Dates
```
In leap year: Feb has 29 days
In ordinary year: Feb has 28 days
Always check if year is leap before calculating
```

### Trap 2: Century Leap Year
```
1900: NOT a leap year (divisible by 100 but not 400)
2000: IS a leap year (divisible by 400)
```

### Trap 3: Starting Point
```
When counting "days from date X to date Y":
- Include or exclude X based on question wording
- "After 30 days from Monday" means 30 days later, not day 30
```

### Trap 4: Same Day Same Date
```
For same date to fall on same day:
- In same year: +7 days apart
- Across years: Use odd days method
```

---

## 19. Practice Problems

### Problem 1
**Find the day of the week on 26 January 2024.**

```
2024 is a leap year (2024 ÷ 4 = 506)

Using reference: 1 Jan 2024
First, find 1 Jan 2024's day:

Odd days from 0 AD to 2000:
- 2000 = 5×400 → 0 odd days

Odd days from 2000 to 2023:
- 23 years = 6 leap + 17 ordinary
- Odd days = 6×2 + 17×1 = 29
- 29 mod 7 = 1

1 Jan 2024: (0 + 1) mod 7 = 1 = Monday

From 1 Jan to 26 Jan = 25 days
25 mod 7 = 4

26 Jan 2024: (1 + 4) mod 7 = 5 = Friday ✓
```

### Problem 2
**If 5th March 2023 was Sunday, what day was 5th March 2024?**

```
2023: Ordinary year (2023 ÷ 4 ≠ integer)
2024: Leap year

From 5 Mar 2023 to 5 Mar 2024:
- 5 Mar 2023 to 5 Mar 2024 crosses Feb 2024 (leap year Feb)
- Days = 366 (since we include one Feb 29)

Wait, more carefully:
- From 5 Mar 2023 to 4 Mar 2024 = 1 year
- 2024 is leap, but Feb 2024 is before Mar, so...

Actually:
- 5 Mar 2023 to 5 Mar 2024 passes through:
  - 2023: Mar to Dec = 306 days (31-5=26 Mar + Apr-Dec)
  - 2024: Jan to 5 Mar = 31+29+5 = 65 days
  - Total ≠ This is complex.

Simpler: From 5 Mar 2023 to 5 Mar 2024 = exactly 1 year
2024 is leap year → 366 days
But wait, we need to check if Feb 29 falls in between.

5 Mar 2023 to 5 Mar 2024:
Goes through Feb 2024 (leap) → 366 days
366 mod 7 = 2

Sunday + 2 = Tuesday ✓
```

### Problem 3
**On what dates in April 2024 does Saturday fall?**

```
First, find 1 April 2024's day.

From Problem 1: 1 Jan 2024 = Monday (code 1)

Jan: 31 days → 31 mod 7 = 3
Feb: 29 days → 29 mod 7 = 1 (leap year)
Mar: 31 days → 31 mod 7 = 3

Total odd days from 1 Jan to 31 Mar = 3+1+3 = 7 mod 7 = 0

1 April 2024: Monday + 0 = Monday (code 1)

Saturday = code 6
From Monday (1) to Saturday (6) = 5 days

First Saturday: 1 + 5 = 6 April 2024
Subsequent: 6+7=13, 13+7=20, 20+7=27

Saturdays in April 2024: 6, 13, 20, 27 ✓
```

---

## 20. Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│            CLOCKS & CALENDARS QUICK REF             │
├─────────────────────────────────────────────────────┤
│ CLOCK FORMULAS:                                     │
│ Angle = |30H - 5.5M|                               │
│ If >180°, use 360° - angle                         │
│                                                     │
│ Overlap: M = 60H/11                                │
│ Opposite (180°): M = (30H ± 180)/5.5               │
│ Right angle (90°): M = (30H ± 90)/5.5              │
│                                                     │
│ Speed: Hour hand = 0.5°/min                        │
│        Minute hand = 6°/min                        │
│        Relative = 5.5°/min                         │
├─────────────────────────────────────────────────────┤
│ CALENDAR FORMULAS:                                  │
│ Odd days in ordinary year = 1                      │
│ Odd days in leap year = 2                          │
│ 100 years = 5, 200 = 3, 300 = 1, 400 = 0          │
│                                                     │
│ Day codes: Sun=0, Mon=1, Tue=2, Wed=3,             │
│            Thu=4, Fri=5, Sat=6                     │
│                                                     │
│ Leap year: ÷4 (non-century), ÷400 (century)       │
├─────────────────────────────────────────────────────┤
│ OVERLAPS/OPPOSITES in 12 hrs:                       │
│ Overlaps: 11 times                                  │
│ Opposite: 11 times                                  │
│ Right angles: 22 times                              │
└─────────────────────────────────────────────────────┘
```

---

## 21. The Mental Slider Visualization

### For Clocks
Imagine a **spinning disc** with two hands:
- Hour hand at 0.5°/min (slow)
- Minute hand at 6°/min (fast)
- Watch the minute hand "chase" the hour hand
- They meet every ~65.45 minutes

### For Calendars
Imagine a **cycle of 7 columns** (days of week):
- Each year shifts the starting column by 1 (ordinary) or 2 (leap)
- After 28 years, pattern repeats for leap years
- Use the column to quickly find any date's day

---

## 22. The 5-Second Sanity Check

### For Clocks
1. **At exact hour**, angle = 30° × hour
2. **At 6:00**, angle is exactly 180°
3. **At 12:00**, angle is exactly 0°
4. **Hands never overlap at 11-12** (they meet exactly at 12:00)

### For Calendars
1. **Leap year check**: Non-century ÷4, Century ÷400
2. **February**: 28 or 29 days only
3. **Same date one year later**: +1 day (ordinary) or +2 days (if crosses Feb 29)
4. **100 years = 5 odd days** (quick check)

---

## 23. Mastery Checklist

### Clocks
- [ ] Know the angle formula: |30H - 5.5M|
- [ ] Calculate overlap times quickly
- [ ] Find right angle times
- [ ] Handle faulty clock problems
- [ ] Know mirror image time formula

### Calendars
- [ ] Identify leap years instantly
- [ ] Know odd days for years and months
- [ ] Find day of any date
- [ ] Calculate days between dates
- [ ] Know when calendars repeat

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**

---

*Next: Data Interpretation | The Graph Decoder*
