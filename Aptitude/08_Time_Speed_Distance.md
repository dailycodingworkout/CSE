# Chapter 8: Time, Speed & Distance

> **Motion mathematics - the physics of competitive aptitude**

---

## 🎯 Why Study This?

- Most frequent topic in GATE/ESE aptitude
- Tests mathematical modeling of real scenarios
- Foundation for relative motion, races, trains, boats problems

---

## 📚 Core Formula

```
Distance = Speed × Time

D = S × T
S = D/T
T = D/S
```

**💡 Analogy**: Like filling a container - Speed is flow rate, Time is duration, Distance is amount filled.

---

## 🔄 Unit Conversions (Memorize!)

```
km/hr to m/s: × 5/18
m/s to km/hr: × 18/5

1 km/hr = 5/18 m/s
1 m/s = 18/5 km/hr = 3.6 km/hr
```

**Quick Reference**:
| km/hr | m/s |
|-------|-----|
| 18 | 5 |
| 36 | 10 |
| 54 | 15 |
| 72 | 20 |
| 90 | 25 |

---

## 📐 Core Concepts

### Average Speed

**⚠️ Not simple average of speeds!**

```
Average Speed = Total Distance / Total Time
```

**Case 1: Same distance at different speeds**
```
Avg Speed = 2S₁S₂/(S₁+S₂) = Harmonic Mean
```

**Case 2: Same time at different speeds**
```
Avg Speed = (S₁+S₂)/2 = Arithmetic Mean
```

---

### Relative Speed

**Objects moving in SAME direction**:
```
Relative Speed = |S₁ - S₂|
```

**Objects moving in OPPOSITE directions**:
```
Relative Speed = S₁ + S₂
```

**💡 Analogy**: 
- Same direction: Like walking on a moving walkway
- Opposite direction: Head-on collision scenario

---

## 🚂 Trains Problems

### Key Principle

Train crossing = Train covers (its length + obstacle length)

```
Time to cross = (Train length + Obstacle length) / Relative Speed
```

---

### Standard Scenarios

**1. Train crossing a pole/person (point object)**:
```
Time = Length of train / Speed of train
```

**2. Train crossing a platform/bridge**:
```
Time = (Train length + Platform length) / Speed of train
```

**3. Two trains crossing each other**:
```
Time = (L₁ + L₂) / Relative Speed

Same direction: Relative Speed = |S₁ - S₂|
Opposite direction: Relative Speed = S₁ + S₂
```

**4. Train crossing a person walking**:
```
Relative Speed = |Train speed ± Person speed|
(+ if opposite, - if same direction)
Time = Train length / Relative Speed
```

---

## ⛵ Boats & Streams

### Core Concepts

```
Downstream (with current): Effective speed = Boat + Stream = u + v
Upstream (against current): Effective speed = Boat - Stream = u - v

Where:
u = Speed of boat in still water
v = Speed of stream/current
```

---

### Finding Boat and Stream Speed

```
Boat speed (u) = (Downstream + Upstream) / 2
Stream speed (v) = (Downstream - Upstream) / 2
```

---

### Time and Distance Relations

**Same distance upstream and downstream**:
```
Time upstream / Time downstream = (u+v)/(u-v)
```

**Average speed for round trip**:
```
Avg Speed = (u²-v²)/u = u - v²/u
```

---

## 🏃 Races Problems

### Terminology

```
A beats B by x meters: When A finishes, B is x meters behind
A beats B by t seconds: A finishes t seconds before B
Dead heat: Both finish together
Head start: B starts ahead of A
Time start: B starts before A
```

---

### Key Formulas

**A beats B by x meters in a race of L meters**:
```
When A runs L, B runs (L-x)
Ratio of speeds = A:B = L:(L-x)
```

**A beats B by t seconds**:
```
A's time = T (say)
B's time = T + t
Ratio of speeds = (T+t):T
```

**A gives B a head start of x meters**:
```
A runs L, B runs (L-x) to tie
If A still wins, he's faster than ratio suggests
```

---

## 🕐 Clocks

### Hour and Minute Hands

```
Speed of minute hand = 6°/min (360°/60 min)
Speed of hour hand = 0.5°/min (30°/60 min)
Relative speed = 5.5°/min
```

---

### Standard Problems

**Angle at time H:M**:
```
Hour hand position = 30H + M/2 degrees from 12
Minute hand position = 6M degrees from 12
Angle = |Hour - Minute|
If > 180°, take 360° - angle
```

**Hands overlap (0° apart)**:
```
Time = 12H × 60/11 minutes past 12
Overlaps occur every 65 5/11 minutes
```

**Hands opposite (180° apart)**:
```
Same frequency as overlap, offset by 32 8/11 minutes
```

**Hands at right angle (90° apart)**:
```
Occurs 22 times in 12 hours (twice between each overlap)
```

---

## 📊 Standard Problem Types

### Type 1: Meeting Point

**Two people start from same point**:
```
They meet when: Distance by A + Distance by B = Total distance
S₁×T + S₂×T = D
T = D/(S₁+S₂)
```

**Starting from opposite ends**:
```
Same formula for first meeting
For subsequent meetings, they travel 3D, 5D, 7D... total
```

---

### Type 2: Catching Up

**A starts, B follows after time t**:
```
When B catches up: 
B's distance = A's distance + A's head start
S_B × T = S_A × (T + t)
```

---

### Type 3: Round Trip

**Outward at S₁, return at S₂**:
```
Total time = D/S₁ + D/S₂ = D(S₁+S₂)/(S₁S₂)
Average speed = 2S₁S₂/(S₁+S₂)
```

---

### Type 4: Late/Early Problems

**Normal speed vs changed speed**:
```
If speed changes by x%, time changes in inverse proportion
D = S₁T₁ = S₂T₂
```

**Example**: Walking at 4 km/hr, late by 10 min. At 5 km/hr, early by 10 min. Find distance.
```
Let distance = D, normal time = T
D/4 = T + 10/60
D/5 = T - 10/60

Subtracting: D/4 - D/5 = 20/60
D(5-4)/20 = 1/3
D = 20/3 km
```

---

### Type 5: Circular Motion

**Two runners on circular track**:
```
Same direction: Meet when relative distance = Track length
Time between meetings = L/(S₁-S₂)

Opposite direction:
Time between meetings = L/(S₁+S₂)
```

---

## 💡 Advanced Tricks

### Trick 1: Constant Distance Ratio

If distance is constant:
```
Speed ratio = Inverse of Time ratio
S₁:S₂ = T₂:T₁
```

---

### Trick 2: The Escalator Problem

```
Let escalator speed = E steps/sec
Person speed = P steps/sec
Visible steps = N

Going with escalator: Steps climbed = N/(1+E/P)
Going against: Steps climbed = N/(1-E/P)

Stationary visible steps = N
```

---

### Trick 3: Multiple Meeting Points

**First meeting**: Total distance covered = D
**Second meeting**: Total distance covered = 3D
**nth meeting**: Total distance covered = (2n-1)D

---

### Trick 4: Man and Train at Bridge

If man is on bridge when train approaches:
```
Calculate safe directions based on:
- Train distance from bridge
- Man's position on bridge
- Relative speeds
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Average Speed ≠ Average of Speeds
```
❌ (40+60)/2 = 50 km/hr
✅ 2×40×60/(40+60) = 48 km/hr (for same distance)
```

### Trap 2: Relative Speed Sign
```
Same direction: |difference| (always positive)
Opposite direction: sum
```

### Trap 3: Train Length Matters
```
Train completely crosses = Train clears the object
Time is for entire train, not front of train
```

### Trap 4: Upstream Time > Downstream Time
```
Always! (for same distance)
Be suspicious if calculations show otherwise
```

### Edge Case: Stream Faster than Boat
```
If v > u, boat cannot go upstream
Boat drifts downstream even when trying to go up
```

---

## 🚀 Formula Cheat Sheet

| Scenario | Formula |
|----------|---------|
| D = S × T | Basic relation |
| km/hr to m/s | × 5/18 |
| m/s to km/hr | × 18/5 |
| Avg speed (same dist) | 2S₁S₂/(S₁+S₂) |
| Relative (same dir) | S₁ - S₂ |
| Relative (opp dir) | S₁ + S₂ |
| Train crosses platform | (L_train + L_platform)/S |
| Two trains cross | (L₁+L₂)/(S₁±S₂) |
| Downstream speed | u + v |
| Upstream speed | u - v |
| Boat speed | (D+U)/2 |
| Stream speed | (D-U)/2 |
| Clock angle at H:M | |30H + M/2 - 6M| |
| Hands overlap | Every 65 5/11 min |

---

## 📝 GATE-Level Practice

**Q1**: A train 150m long crosses a platform of 250m in 20s. Speed?
```
Total distance = 150 + 250 = 400m
Speed = 400/20 = 20 m/s = 72 km/hr
```

**Q2**: Boat goes 24km downstream in 2 hrs, returns in 3 hrs. Stream speed?
```
Downstream = 24/2 = 12 km/hr
Upstream = 24/3 = 8 km/hr
Stream = (12-8)/2 = 2 km/hr
```

**Q3**: A and B start from P and Q (200km apart) towards each other at 40 and 60 km/hr. Where do they meet?
```
Time = 200/(40+60) = 2 hrs
Distance from P = 40 × 2 = 80 km
```

**Q4**: At what time between 3 and 4 do clock hands overlap?
```
At 3:00, hour hand at 90°, minute at 0°
Minute gains 5.5°/min
Time to gain 90° = 90/5.5 = 180/11 = 16 4/11 min
Time = 3:16 4/11
```

**Q5**: Two trains 100m and 150m long approach each other at 30 and 20 m/s. Time to cross?
```
Relative speed = 30 + 20 = 50 m/s
Total distance = 100 + 150 = 250m
Time = 250/50 = 5 seconds
```

---

*← [Chapter 7 - Time & Work](./07_Time_Work.md) | [Chapter 9 - Algebra →](./09_Algebra.md)*
