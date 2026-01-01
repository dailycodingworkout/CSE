# 🚗 Time, Speed and Distance | The Singularity

> **The Atomic Truth:** *Distance = Speed × Time; all motion problems reduce to this.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Unit Conversions](#unit-conversions)
3. [Average Speed](#average-speed)
4. [Relative Speed](#relative-speed)
5. [Trains Problems](#trains-problems)
6. [Boats and Streams](#boats-and-streams)
7. [Races and Circular Tracks](#races-and-circular-tracks)
8. [Clocks](#clocks)
9. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
10. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
11. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### The Core Equation

$$\text{Distance} = \text{Speed} \times \text{Time}$$

$$D = S \times T$$

**Derived Formulas:**
$$S = \frac{D}{T}, \quad T = \frac{D}{S}$$

### Understanding the Relationship

| If | And | Then |
|----|-----|------|
| Speed ↑ | Distance constant | Time ↓ |
| Speed ↓ | Distance constant | Time ↑ |
| Time constant | Speed ↑ | Distance ↑ |
| Speed constant | Time ↑ | Distance ↑ |

> **💡 The Golden Pivot:** Speed and Time are inversely proportional for constant distance.

---

## Unit Conversions

### Essential Conversions

**km/h to m/s:**
$$1 \text{ km/h} = \frac{5}{18} \text{ m/s}$$

**m/s to km/h:**
$$1 \text{ m/s} = \frac{18}{5} \text{ km/h}$$

### Conversion Table

| km/h | m/s |
|------|-----|
| 18 | 5 |
| 36 | 10 |
| 54 | 15 |
| 72 | 20 |
| 90 | 25 |
| 108 | 30 |

### Quick Mental Trick
- km/h to m/s: Multiply by 5, divide by 18
- m/s to km/h: Multiply by 18, divide by 5

**Example:** 72 km/h = 72 × 5/18 = 20 m/s

---

## Average Speed

### Definition
$$\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}$$

### Case 1: Different Speeds for Different Distances

$$\bar{S} = \frac{d_1 + d_2}{\frac{d_1}{s_1} + \frac{d_2}{s_2}}$$

**For Equal Distances (Harmonic Mean):**
$$\bar{S} = \frac{2 s_1 s_2}{s_1 + s_2}$$

### Case 2: Different Speeds for Different Times

$$\bar{S} = \frac{s_1 t_1 + s_2 t_2}{t_1 + t_2}$$

**For Equal Times (Arithmetic Mean):**
$$\bar{S} = \frac{s_1 + s_2}{2}$$

### Example
A car travels first half at 40 km/h and second half at 60 km/h.
$$\bar{S} = \frac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100} = 48 \text{ km/h}$$

> **⚠️ Common Trap:** Average speed ≠ (40 + 60)/2 = 50 km/h

---

## Relative Speed

### Same Direction
When two objects move in the **same direction**:
$$\text{Relative Speed} = |S_1 - S_2|$$

### Opposite Direction
When two objects move in **opposite directions**:
$$\text{Relative Speed} = S_1 + S_2$$

### Applications

**Meeting Point:**
$$\text{Time to meet} = \frac{\text{Initial Distance}}{\text{Relative Speed}}$$

**Catching Up:**
$$\text{Time to catch} = \frac{\text{Lead Distance}}{|\text{Speed difference}|}$$

---

## Trains Problems

### Crossing a Stationary Object (Pole, Person)

$$\text{Time} = \frac{\text{Length of Train}}{\text{Speed of Train}}$$

### Crossing a Platform/Bridge

$$\text{Time} = \frac{\text{Length of Train + Length of Platform}}{\text{Speed of Train}}$$

### Two Trains Crossing Each Other

**Moving in Opposite Directions:**
$$\text{Time} = \frac{L_1 + L_2}{S_1 + S_2}$$

**Moving in Same Direction:**
$$\text{Time} = \frac{L_1 + L_2}{|S_1 - S_2|}$$

### Train Passing a Moving Person

**Same direction:**
$$\text{Time} = \frac{L_{\text{train}}}{S_{\text{train}} - S_{\text{person}}}$$

**Opposite direction:**
$$\text{Time} = \frac{L_{\text{train}}}{S_{\text{train}} + S_{\text{person}}}$$

### Example
Train 200m long at 60 km/h crosses a platform of 300m. Time?
- Total distance = 200 + 300 = 500m
- Speed = 60 × 5/18 = 50/3 m/s
- Time = 500 ÷ (50/3) = 30 seconds

---

## Boats and Streams

### Key Concepts

- **Still Water Speed:** Speed of boat in calm water ($B$)
- **Stream Speed:** Speed of current ($S$)
- **Downstream:** Boat moves with current ($B + S$)
- **Upstream:** Boat moves against current ($B - S$)

### Formulas

$$\text{Downstream Speed} = B + S$$
$$\text{Upstream Speed} = B - S$$

**Finding Boat Speed:**
$$B = \frac{\text{Downstream} + \text{Upstream}}{2}$$

**Finding Stream Speed:**
$$S = \frac{\text{Downstream} - \text{Upstream}}{2}$$

### Example
A boat goes 20 km downstream in 2 hours and returns in 4 hours.
- Downstream speed = 20/2 = 10 km/h
- Upstream speed = 20/4 = 5 km/h
- Boat speed = (10+5)/2 = 7.5 km/h
- Stream speed = (10-5)/2 = 2.5 km/h

### Round Trip

For a round trip of distance $d$ each way:
$$\text{Total Time} = \frac{d}{B+S} + \frac{d}{B-S} = \frac{2dB}{B^2 - S^2}$$

---

## Races and Circular Tracks

### Linear Race

**Terms:**
- A gives B a start of 20m: A starts 20m behind B
- A beats B by 30m: When A finishes, B is 30m behind
- A beats B by 5 seconds: A finishes 5 seconds before B

**Key Formula:**
If A beats B by $x$ meters in a race of $d$ meters:
$$\text{Speed ratio} = \frac{d}{d-x}$$

### Circular Track

**Meeting on Circular Track:**

If two people start from same point:

**Same direction:**
$$\text{Time to first meet} = \frac{\text{Track Length}}{|S_1 - S_2|}$$

**Opposite direction:**
$$\text{Time to first meet} = \frac{\text{Track Length}}{S_1 + S_2}$$

**Meeting at Starting Point:**
$$\text{Time} = \text{LCM}\left(\frac{L}{S_1}, \frac{L}{S_2}\right)$$

### Example
Track = 400m. A's speed = 4 m/s, B's speed = 3 m/s. Starting together in same direction, when do they first meet?
$$\text{Time} = \frac{400}{4-3} = 400 \text{ seconds}$$

---

## Clocks

### Basic Concepts

**Speed of minute hand:** 360°/60 min = 6° per minute
**Speed of hour hand:** 360°/12 hours = 0.5° per minute
**Relative speed:** 6 - 0.5 = 5.5° per minute

### Angle Between Hands

At $h$ hours and $m$ minutes:
$$\theta = \left|30h - \frac{11m}{2}\right|$$

Or:
$$\theta = \left|\frac{11m}{2} - 30h\right|$$

If $\theta > 180°$, take $360° - \theta$

### Hands Coinciding

Hands coincide every $\frac{720}{11}$ ≈ 65.45 minutes

In 12 hours: 11 times (not 12!)

### Hands at Right Angle (90°)

Occurs 44 times in 24 hours (22 times in 12 hours)

### Hands Opposite (180°)

Occurs 22 times in 24 hours (11 times in 12 hours)

### Example
Find angle at 3:30.
$$\theta = |30(3) - \frac{11(30)}{2}| = |90 - 165| = 75°$$

---

## GATE & ESE Problem Patterns

### Pattern 1: Basic Speed-Distance
> A car covers 360 km in 5 hours. Speed?
$$S = \frac{360}{5} = 72 \text{ km/h}$$

### Pattern 2: Late/Early Problems
> Walking at 3/4 of usual speed, a person is 20 min late. Usual time?

Let usual time = $t$
$$\frac{t}{3/4} - t = 20$$
$$\frac{4t}{3} - t = 20$$
$$\frac{t}{3} = 20$$
$$t = 60 \text{ minutes}$$

### Pattern 3: Meet & Catch
> A and B start from P and Q (100 km apart) towards each other at 25 km/h and 15 km/h. Where do they meet?

- Relative speed = 40 km/h
- Time to meet = 100/40 = 2.5 hours
- A travels = 25 × 2.5 = 62.5 km from P

### Pattern 4: Head Start
> A starts 2 hours before B. A's speed is 30 km/h, B's is 50 km/h. When does B catch A?

- A's head start = 30 × 2 = 60 km
- Relative speed = 50 - 30 = 20 km/h
- Time for B to catch = 60/20 = 3 hours (after B starts)

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"A person travels to office at 40 km/h and returns at 60 km/h. Average speed?"

Wrong answer: (40 + 60)/2 = 50 km/h

**The Elegant Solution:**
For equal distances, use Harmonic Mean:
$$\bar{S} = \frac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100} = 48 \text{ km/h}$$

**MSQ Logic Gate:**
- Average speed ≠ Average of speeds (unless equal times)
- Relative speed concept must be clear (same vs opposite direction)

**NAT Precision Lock:**
- Convert all units to same system before calculating
- Time can be fractional; express in proper form

---

## Speed Tricks & Shortcuts

### Trick 1: Time Ratio Inverse of Speed Ratio

If distance is constant:
$$\frac{T_1}{T_2} = \frac{S_2}{S_1}$$

### Trick 2: The Fraction Method for Late/Early

If at $\frac{a}{b}$ of usual speed, person is $t$ minutes late/early:
$$\text{Usual Time} = \frac{b \cdot t}{|a-b|}$$

### Trick 3: Two-Train Meeting Point

Meeting point from A = $\frac{d \times S_A}{S_A + S_B}$

### Trick 4: Circular Track First Meeting

Same direction: Time = $\frac{L}{\text{Speed difference}}$
Opposite direction: Time = $\frac{L}{\text{Speed sum}}$

### Trick 5: Clock Angle Quick Formula

At H:M → Angle = $|30H - 5.5M|$
(If > 180, subtract from 360)

---

## Permanent Recall

### The Bizarre Mnemonic (Average Speed)
*"For equal distances, speeds don't add—they shake hands harmonically (2ab/(a+b)). Only when time is shared equally do they split the check arithmetically ((a+b)/2)."*

### The Mental Slider
Imagine a car dashboard:
- Speedometer needle position = current speed
- Distance accumulates with area under speed curve
- Average speed = total distance / total time (not average of readings!)

### The 5-Second Snap-Check
- Relative speed same direction: SUBTRACT
- Relative speed opposite direction: ADD
- Train crossing: Add lengths, use appropriate relative speed

---

## Practice Problems

### Level 1: Fundamentals
1. A train 150m long passes a pole in 15 seconds. Find its speed in km/h.
2. A boat's speed in still water is 12 km/h. Stream speed is 2 km/h. Time to go 28 km downstream?
3. At 4:00, what is the angle between clock hands?

### Level 2: GATE Standard
4. A person walks from A to B at 5 km/h and returns at 3 km/h. If AB = 15 km, find average speed.
5. Two trains 100m and 150m long run in same direction at 60 km/h and 45 km/h. Time for faster train to cross slower?
6. A car leaves city A at 6 AM at 40 km/h. Another leaves at 7 AM at 50 km/h. When does the second catch the first?

### Level 3: IIT Examiner Level
7. A circular track has circumference 400m. A and B start together in same direction at 4 m/s and 3 m/s. When do they first meet at starting point together again?
8. A train traveling at 72 km/h crosses a platform in 30 seconds and a person on platform in 18 seconds. Find length of platform.
9. Between 4 and 5 o'clock, at what time are the hands of clock at right angle?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Speed = 150/15 = 10 m/s = 10 × 18/5 = **36 km/h**

2. Downstream speed = 12 + 2 = 14 km/h
   Time = 28/14 = **2 hours**

3. At 4:00, angle = |30(4) - 5.5(0)| = **120°**

4. Total distance = 30 km
   Time = 15/5 + 15/3 = 3 + 5 = 8 hours
   Average speed = 30/8 = **3.75 km/h**
   
   Or: 2×5×3/(5+3) = 30/8 = 3.75 km/h

5. Relative speed = 60 - 45 = 15 km/h = 15 × 5/18 = 25/6 m/s
   Total length = 100 + 150 = 250m
   Time = 250 ÷ (25/6) = 250 × 6/25 = **60 seconds**

6. First car's head start = 40 × 1 = 40 km
   Relative speed = 50 - 40 = 10 km/h
   Time to catch = 40/10 = 4 hours after 7 AM = **11 AM**

7. A completes one lap in 400/4 = 100 sec
   B completes one lap in 400/3 = 133.33 sec
   LCM(100, 400/3) = LCM(100, 133.33)
   Converting to fractions: LCM of 100 and 400/3
   = 400 seconds
   Answer: **400 seconds**

8. Let train length = L, platform length = P
   Speed = 72 × 5/18 = 20 m/s
   L = 20 × 18 = 360m (crossing person)
   L + P = 20 × 30 = 600m (crossing platform)
   P = 600 - 360 = **240m**

9. At 4:00, angle = 120°
   Hands move at relative 5.5°/min
   For 90°: Need to reduce angle by 30° OR increase to 90° from opposite side
   
   First right angle: 120 - 90 = 30° to cover
   Time = 30/5.5 = 60/11 min after 4:00
   
   Second right angle: Need total 210° (120 + 90)
   Time = 210/5.5 = 420/11 min after 4:00
   
   Answers: **4:60/11 (≈4:05:27)** and **4:420/11 (≈4:38:11)**

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Speed-Distance with Algebra for a Rank-1 simulation?
