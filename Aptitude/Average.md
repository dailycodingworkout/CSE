# Average - Supreme Logic Coverage Questions

> **Mission:** Total Logic Coverage with Minimum Questions  
> **Target:** GATE, ESE, PSU, and Banking Exams  
> **Philosophy:** Exhaust the logic-space, not the syllabus

---

## Question 1: The Weighted Mirage

### Best Technique
**Weighted Average Decomposition:** When groups with different sizes are combined, the overall average is a weighted sum, not a simple arithmetic mean. The trap is that weights are often hidden in the problem statement.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Missing data illusion
- **Secondary Logic Interactions:** Hidden constraint dominance, Order-of-magnitude deception
- **Why Lethal:** The problem gives partial averages without sizes. Students assume equal sizes or miss that size information is implicitly derivable.

### 2️⃣ Question
The average salary of officers in a company is ₹12,000 and the average salary of workers is ₹3,000. If the average salary of all employees is ₹4,000, find the ratio of officers to workers.

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you extract the hidden ratio from average constraints?
- **Why Top-100 Fail:** They try to solve with two unknowns but have only one equation, not recognizing the ratio is what's being asked (1 equation suffices for ratio).

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Use weighted average formula and solve for ratio.

1. Let officers = $O$, workers = $W$
2. Total salary = $12000 \cdot O + 3000 \cdot W$
3. Total employees = $O + W$
4. Average: $\frac{12000O + 3000W}{O + W} = 4000$
5. $12000O + 3000W = 4000(O + W)$
6. $12000O + 3000W = 4000O + 4000W$
7. $8000O = 1000W$
8. $\frac{O}{W} = \frac{1000}{8000} = \frac{1}{8}$

**Answer: 1:8**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 1:4 or 1:3 (from wrong arithmetic)
- **Why It Feels Correct:** Students may average the averages: $(12000 + 3000)/2 = 7500$, which doesn't match 4000, causing confusion.
- **Exact Failure Point:** Not setting up the weighted average equation correctly.

### 6️⃣ Generalization Map
1. Three groups with two known ratios
2. Average changes when new members join
3. Finding individual salaries given constraints
4. Median vs mean comparison
5. Average salary with partial information about groups

### 7️⃣ Neural Anchor
**"Alligation-Ratio"**

---

## Question 2: The Entry-Exit Paradox

### Best Technique
**Running Total Maintenance:** When members enter or leave a group, track the running sum, not averages. Averages can be recomputed from sum and count.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Non-commutative step dependency
- **Secondary Logic Interactions:** Local correctness global failure, Ghost variable cancellation
- **Why Lethal:** Order of entry/exit matters when averages are involved. Students often average the changes instead of tracking sums.

### 2️⃣ Question
The average age of 5 members of a family is 24 years. A child is born, reducing the average to 20 years. What is the current age of the youngest member?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you interpret "reducing the average" correctly in the context of a birth?
- **Why Top-100 Fail:** They forget that "current age" of the child is different from the age at birth (which is 0).

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Use sum preservation with new member.

1. Initial: 5 members, average = 24 → Total age = $5 \times 24 = 120$
2. After birth: 6 members, average = 20 → Total age = $6 \times 20 = 120$
3. **Wait:** Total age is same? That would mean child's age = 0
4. **Re-read:** "A child is born, reducing the average to 20"
5. At birth, child's age = 0
6. New total = $120 + 0 = 120$
7. New average = $120 / 6 = 20$ ✓
8. Current age of youngest member (the child) = 0

**Answer: 0 years**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 4 years (computing $120 - 6 \times 20 = 0$ but then adding time)
- **Why It Feels Correct:** The question asks "current age," which some interpret as "after some time has passed."
- **Exact Failure Point:** The question says "is born" (present tense) and "current age" refers to the moment of birth.

### 6️⃣ Generalization Map
1. After 5 years, what is the average?
2. A member leaves instead of joining
3. Replace one member with another
4. Weighted by seniority instead of simple average
5. Two events: one birth, one death

### 7️⃣ Neural Anchor
**"Sum-Before-Average"**

---

## Question 3: The Speed Deception

### Best Technique
**Harmonic Mean for Equal Distances:** When traveling equal distances at different speeds, the average speed is the harmonic mean, not arithmetic mean. For equal times, use arithmetic mean.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** False linearity assumption
- **Secondary Logic Interactions:** Dimensional contradiction, Symmetry/invariance exploitation
- **Why Lethal:** "Average speed" sounds like it should be the arithmetic mean, but it depends on the weighting (by distance vs by time).

### 2️⃣ Question
A person travels from A to B at 40 km/h and returns at 60 km/h. What is the average speed for the entire journey?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you identify that equal distances require harmonic mean?
- **Why Top-100 Fail:** They compute $(40 + 60)/2 = 50$ km/h.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Equal distance → harmonic mean.

1. Let distance A to B = $d$
2. Time for A→B: $t_1 = d/40$
3. Time for B→A: $t_2 = d/60$
4. Total distance = $2d$
5. Total time = $d/40 + d/60 = d \cdot \frac{3 + 2}{120} = \frac{5d}{120} = \frac{d}{24}$
6. Average speed = $\frac{2d}{d/24} = 2d \times \frac{24}{d} = 48$ km/h

**Alternative (Harmonic mean formula):**
$$\text{Average speed} = \frac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100} = 48$$

**Answer: 48 km/h**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 50 km/h (arithmetic mean)
- **Why It Feels Correct:** Average of two numbers "should be" their arithmetic mean.
- **Exact Failure Point:** Not recognizing that time spent at each speed differs.

### 6️⃣ Generalization Map
1. Three legs with three different speeds
2. Equal time at each speed (then AM applies)
3. One leg is twice the distance of the other
4. Speed varies continuously
5. Factor in rest stops

### 7️⃣ Neural Anchor
**"Equal-Distance-Harmonic"**

---

## Question 4: The Moving Average Trap

### Best Technique
**Incremental Sum Tracking:** When average changes with addition/removal, track the incremental effect on sum, not the average change directly.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Boundary-condition collapse
- **Secondary Logic Interactions:** Order-of-magnitude deception, Assumption poisoning
- **Why Lethal:** Small average changes mask large sum changes when the group is large.

### 2️⃣ Question
The average of 50 numbers is 38. Later, it was found that two numbers 45 and 55 were read as 35 and 40 respectively. Find the correct average.

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you compute the net error and adjust?
- **Why Top-100 Fail:** They get confused about whether to add or subtract the errors.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Compute sum error, then correct.

1. Original (wrong) sum = $50 \times 38 = 1900$
2. Error: 45 was read as 35 → under by 10
3. Error: 55 was read as 40 → under by 15
4. Total undercount = $10 + 15 = 25$
5. Correct sum = $1900 + 25 = 1925$
6. Correct average = $1925 / 50 = 38.5$

**Answer: 38.5**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 37.5 (subtracting instead of adding)
- **Why It Feels Correct:** "Read as less" might be interpreted as "originally more, so subtract."
- **Exact Failure Point:** Sign confusion in the correction.

### 6️⃣ Generalization Map
1. More than two errors
2. Some positive, some negative errors
3. Error in count (51 numbers instead of 50)
4. Percentage error in readings
5. Cascading errors (error in error correction)

### 7️⃣ Neural Anchor
**"Sum-Error-Correct"**

---

## Question 5: The Median Switcheroo

### Best Technique
**Position Tracking for Median:** Median depends on position, not value. When values change, track whether the middle position's value changes.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Intuition vs formal logic conflict
- **Secondary Logic Interactions:** Discrete vs continuous trap, Degenerate/singular cases
- **Why Lethal:** Students conflate median with mean behavior, expecting proportional changes.

### 2️⃣ Question
The median of 7, 12, 15, 19, 21 is 15. If 21 is replaced by 8, what is the new median?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you re-sort and find the new middle element?
- **Why Top-100 Fail:** They assume median stays at 15 or changes by a formula.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Insert new value, re-sort, find middle.

1. Original: 7, 12, 15, 19, 21 (sorted)
2. Replace 21 with 8: 7, 12, 15, 19, 8 (unsorted)
3. Sort: 7, 8, 12, 15, 19
4. Median (middle of 5) = 3rd element = 12

**Answer: 12**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 15 (unchanged) or 14 (some average)
- **Why It Feels Correct:** "Only the largest changed" suggests median shouldn't change much.
- **Exact Failure Point:** Not re-sorting after the replacement.

### 6️⃣ Generalization Map
1. Even number of elements (median is average of two middle)
2. Replace multiple values
3. Add new values instead of replace
4. Find the value that keeps median unchanged
5. Weighted median

### 7️⃣ Neural Anchor
**"Resort-Then-Middle"**

---

## Question 6: The Inclusion Illusion

### Best Technique
**Self-Referential Average Equations:** When a new member's value equals the average, the average may or may not change. This requires algebraic setup.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Conservation vs optimization conflict
- **Secondary Logic Interactions:** Ghost variable cancellation, Limiting-case override
- **Why Lethal:** Circular definitions appear: "new member's score equals the average" but which average?

### 2️⃣ Question
The average of 10 numbers is 50. An 11th number is added such that the new average equals this 11th number. What is the 11th number?

### 3️⃣ Examiner's Intent
- **Secret Test:** Can you handle self-referential constraints?
- **Why Top-100 Fail:** They get stuck in circular reasoning.

### 4️⃣ Solution (Logic-First)
**Entry Decision:** Let the 11th number be $x$, set up equation.

1. Original sum = $10 \times 50 = 500$
2. New sum = $500 + x$
3. New average = $\frac{500 + x}{11}$
4. Condition: New average = $x$
5. $\frac{500 + x}{11} = x$
6. $500 + x = 11x$
7. $500 = 10x$
8. $x = 50$

**Answer: 50**

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** 55 or 45.45 (from wrong equation setup)
- **Why It Feels Correct:** The number "should be different from 50 to change something."
- **Exact Failure Point:** The elegant answer—adding a number equal to the old average keeps the new average equal to that number—surprises students.

### 6️⃣ Generalization Map
1. New average is twice the new number
2. New average is old average plus new number
3. Multiple self-referential additions
4. Geometric mean instead of arithmetic
5. Weighted average with self-referential weight

### 7️⃣ Neural Anchor
**"Self-Reference-Algebra"**

---

## Summary: Logic Traps Covered

| Q# | Dominant Trap | Key Insight |
|----|---------------|-------------|
| 1 | Missing data illusion | Ratio extractable from single equation |
| 2 | Non-commutative step dependency | Birth adds age 0 at that moment |
| 3 | False linearity assumption | Equal distance requires harmonic mean |
| 4 | Boundary-condition collapse | Track sum error, not average error |
| 5 | Intuition vs formal logic conflict | Re-sort after value change |
| 6 | Conservation vs optimization conflict | Self-referential equations have solutions |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
