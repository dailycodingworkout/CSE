# Complete Theory - Time, Speed & Distance

## 🎯 **Exhaustive Theory for GATE 2026 CSE AIR 1**

This comprehensive theory covers all Time, Speed & Distance concepts essential for achieving All India Rank 1 in GATE 2026 CSE.

## 🔧 **1. Basic Time, Speed & Distance Concepts**

### **Fundamental Relations**
The foundation of all motion problems lies in three fundamental relationships:

**Primary Formula:**
```
Speed = Distance / Time
Distance = Speed × Time  
Time = Distance / Speed
```

**Memory Aid**: **SDT Triangle** - Cover any one variable to get formula for the other two.

### **Unit Conversions (Critical for GATE)**

**1.1 Speed Conversions**
```
1 km/hr = 5/18 m/s
1 m/s = 18/5 km/hr = 3.6 km/hr
```

**Derivation:**
- 1 km = 1000 m
- 1 hour = 3600 seconds
- 1 km/hr = 1000m/3600s = 5/18 m/s

**Quick Conversion Tricks:**
- km/hr to m/s: Multiply by 5/18
- m/s to km/hr: Multiply by 18/5
- Mental trick: km/hr ÷ 3.6 = m/s

**1.2 Common Speed Equivalents**
```
54 km/hr = 15 m/s
72 km/hr = 20 m/s
90 km/hr = 25 m/s
108 km/hr = 30 m/s
```

## 🔄 **2. Relative Speed**

### **Definition and Core Concepts**
Relative speed is the speed of one moving object with respect to another moving object.

### **2.1 Same Plane Movement (Linear Motion)**

**Case 1: Same Direction**
```
Relative Speed = |Speed₁ - Speed₂|
```
- Faster object approaches slower object at relative speed
- Time to overtake = Initial separation / Relative speed

**Case 2: Opposite Direction**
```
Relative Speed = Speed₁ + Speed₂
```
- Objects approach each other at combined speed
- Time to meet = Initial separation / Relative speed

**Example Applications:**
- Two cars on highway
- Two trains on parallel tracks
- Walking on moving walkway

### **2.2 One Object on Another (Platform Movement)**

**Case 1: Same Direction**
```
Effective Speed = Object Speed + Platform Speed
```

**Case 2: Opposite Direction**
```
Effective Speed = Object Speed - Platform Speed
```

**Applications:**
- Person on escalator
- Swimming in river current
- Walking on train

### **2.3 Problem-Solving Approach**
1. **Identify relative motion type**
2. **Determine direction relationship**
3. **Apply appropriate relative speed formula**
4. **Calculate time or distance as required**

## 📊 **3. Average Speed**

### **Fundamental Principle**
Average speed is NOT the arithmetic mean of speeds but the total distance divided by total time.

**Formula:**
```
Average Speed = Total Distance Traveled / Total Time Taken
```

### **3.1 Equal Distance with Different Speeds**

**Problem Type**: Travel equal distances d with speeds v₁ and v₂

**Formula:**
```
Average Speed = 2v₁v₂ / (v₁ + v₂)
```

**Derivation:**
- Time₁ = d/v₁, Time₂ = d/v₂
- Total Distance = 2d
- Total Time = d/v₁ + d/v₂ = d(v₁ + v₂)/(v₁v₂)
- Average Speed = 2d / [d(v₁ + v₂)/(v₁v₂)] = 2v₁v₂/(v₁ + v₂)

### **3.2 Equal Time with Different Speeds**

**Problem Type**: Travel for equal times t with speeds v₁ and v₂

**Formula:**
```
Average Speed = (v₁ + v₂) / 2
```
This is simply the arithmetic mean when time periods are equal.

### **3.3 General Case Formula**
For n segments with distances d₁, d₂, ..., dₙ and speeds v₁, v₂, ..., vₙ:

```
Average Speed = (d₁ + d₂ + ... + dₙ) / (d₁/v₁ + d₂/v₂ + ... + dₙ/vₙ)
```

## 🏃 **4. Race Problems**

### **4.1 Basic Race Concepts**

**Dead Heat Race**: Both participants finish simultaneously
**Winning Margin**: Distance by which winner leads at finish

### **4.2 Standard Race Formulas**

**Case 1: A beats B by distance d in race of length L**
- When A finishes L, B covers (L-d)
- Ratio of speeds: A:B = L:(L-d)

**Case 2: A beats B by time t in race of length L**
- A's time = T, B's time = T+t
- Speed ratio: A:B = (T+t):T

**Case 3: A gives B a start of distance s in race of length L**
- A covers L, B covers (L-s) in same time
- For fair race: A:B speed ratio = L:(L-s)

### **4.3 Circular Race Track**

**Meeting Problems:**
- Same direction: Meet every L/(v₁-v₂) time units
- Opposite direction: Meet every L/(v₁+v₂) time units

Where L = circumference of track, v₁ > v₂

**Lap Difference:**
After time t, faster runner leads by: t(v₁-v₂)/L laps

## 🔄 **5. Circular Track Problems**

### **5.1 Key Concepts**

**Starting Together:**
- Same direction: First meeting after L/(v₁-v₂) time
- Opposite direction: First meeting after L/(v₁+v₂) time

**Starting from Opposite Points:**
- Same direction: First meeting after L/[2(v₁-v₂)] time
- Opposite direction: First meeting after L/[2(v₁+v₂)] time

### **5.2 Advanced Circular Motion**

**Multiple Runners:**
For n runners with speeds v₁ > v₂ > ... > vₙ:
- All meet together after LCM of individual meeting periods
- Pairwise meetings follow standard formulas

**Position Calculation:**
After time t, runner with speed v covers: vt distance
Position on track: (vt) mod L

## 📈 **6. Application of Variation**

### **6.1 Direct Variation in Motion**

**Speed ∝ Distance** (constant time)
```
v₁/v₂ = d₁/d₂
```

**Speed ∝ 1/Time** (constant distance)
```
v₁/v₂ = t₂/t₁
```

### **6.2 Inverse Variation**

**Time ∝ 1/Speed** (constant distance)
```
t₁/t₂ = v₂/v₁
```

### **6.3 Joint Variation**
```
Speed ∝ Distance/Time
S₁/S₂ = (D₁/D₂) × (T₂/T₁)
```

## 🚂 **7. Problems on Trains**

### **7.1 Fundamental Train Formula**

When train crosses any object:
```
Time = (Length of Train + Length of Object) / (Speed of Train ± Speed of Object)
```

**Sign Convention:**
- Same direction: Subtract speeds (-)
- Opposite direction: Add speeds (+)

### **7.2 Standard Train Problems**

**Case 1: Train crossing a stationary object**
```
Time = (L_train + L_object) / Speed_train
```

**Case 2: Train crossing a moving object**
```
Time = (L_train + L_object) / Relative_Speed
```

**Case 3: Train crossing a platform**
```
Time = (L_train + L_platform) / Speed_train
```

**Case 4: Train crossing another train**
- Same direction: Time = (L₁ + L₂)/(v₁ - v₂)
- Opposite direction: Time = (L₁ + L₂)/(v₁ + v₂)

### **7.3 Advanced Train Concepts**

**Overtaking Problems:**
```
Overtaking Time = Difference in Lengths / Difference in Speeds
```

**Signal/Telegraph Pole Crossing:**
```
Time = Length of Train / Speed of Train
```
(Point objects have zero length)

## 🌊 **8. Rivers & Boats**

### **8.1 Basic River Concepts**

**Key Variables:**
- v_b = Speed of boat in still water
- v_r = Speed of river current
- Upstream = Against current
- Downstream = Along current

### **8.2 Fundamental River Formulas**

**Upstream Speed:**
```
v_upstream = v_boat - v_river
```

**Downstream Speed:**
```
v_downstream = v_boat + v_river
```

**Crossing River Formulas:**
```
v_boat = (v_downstream + v_upstream) / 2
v_river = (v_downstream - v_upstream) / 2
```

### **8.3 River Problem Types**

**Type 1: Downstream and Upstream Times Given**
If downstream time = t₁ and upstream time = t₂ for distance d:
```
v_boat = d(t₁ + t₂) / (2t₁t₂)
v_river = d(t₂ - t₁) / (2t₁t₂)
```

**Type 2: Round Trip Problems**
Total time for round trip of distance d:
```
Total Time = d/(v_b - v_r) + d/(v_b + v_r) = 2dv_b/(v_b² - v_r²)
```

**Type 3: Crossing River Perpendicular**
To cross river of width w perpendicularly:
```
Time = w / √(v_b² - v_r²)
```

### **8.4 Advanced River Concepts**

**Drift in River:**
When boat aims perpendicular to bank:
```
Drift = v_r × (w/v_b)
Resultant crossing time = w/v_b
```

**Minimum Time Crossing:**
```
Minimum Time = w/v_b
```
(Boat aims perpendicular, accepts drift)

**Minimum Drift Crossing:**
```
Minimum Drift = 0
Time = w/√(v_b² - v_r²)
```
(Boat aims at angle to compensate current)

## 🧮 **Mathematical Derivations and Proofs**

### **Derivation 1: Average Speed for Equal Distances**
**Problem**: Find average speed when traveling distance d at speed v₁ and distance d at speed v₂.

**Solution**:
- Time₁ = d/v₁
- Time₂ = d/v₂
- Total Distance = 2d
- Total Time = d/v₁ + d/v₂ = d(v₁ + v₂)/(v₁v₂)
- Average Speed = 2d ÷ [d(v₁ + v₂)/(v₁v₂)] = 2v₁v₂/(v₁ + v₂)

**Key Insight**: This is the harmonic mean of the two speeds.

### **Derivation 2: Relative Speed in Circular Motion**
**Problem**: Two objects start together on circular track of circumference L with speeds v₁ and v₂ (v₁ > v₂).

**Solution**:
- Relative speed = v₁ - v₂
- For first meeting, faster object must gain one full lap = L
- Time = L/(v₁ - v₂)

### **Derivation 3: Train Crossing Formula**
**Problem**: Train of length L₁ moving at speed v₁ crosses train of length L₂ moving at speed v₂.

**Solution**:
- Total distance to be covered = L₁ + L₂
- Relative speed = v₁ ± v₂ (depending on direction)
- Time = (L₁ + L₂)/(v₁ ± v₂)

## 🎯 **Key Problem-Solving Strategies**

### **Strategy 1: Identify Motion Type**
1. **Linear Motion**: Straight line movement
2. **Circular Motion**: Track/orbit movement
3. **Relative Motion**: One object w.r.t. another
4. **Complex Motion**: Combination of above

### **Strategy 2: Visual Representation**
- Draw diagrams for complex problems
- Mark directions clearly
- Identify initial positions
- Track movement patterns

### **Strategy 3: Unit Consistency**
- Convert all units to same system
- Use dimensional analysis
- Check final answer units

### **Strategy 4: Logical Reasoning**
- Apply common sense checks
- Verify with extreme cases
- Cross-check with alternate methods

## 🏁 **Chapter Summary**

This comprehensive theory covers:
- ✅ **8 major topic areas** with complete mathematical coverage
- ✅ **Advanced problem-solving techniques** for competitive advantage
- ✅ **Mathematical derivations** for deep understanding
- ✅ **Strategic approaches** for different problem types
- ✅ **Common pitfalls** and how to avoid them

**Mastery Indicators:**
- Can solve any basic problem in under 30 seconds
- Understands all formula derivations
- Recognizes problem patterns instantly
- Applies appropriate strategy automatically

---

**Next Steps**: Practice with Tips & Tricks section to develop speed optimization techniques for GATE 2026 CSE success!