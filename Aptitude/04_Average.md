# Average | GATE ESE PSU - Maximum Difficulty Question Bank

## The Atomic Truth
> **"Weighted Sum divided by Total Weight."**

---

## Question 1 | Weighted Average Trap (NAT)

**Problem:** Class A has 40 students with average marks 75. Class B has 60 students with average marks 65. Find the combined average of both classes.

**Trap Alert:** Simple arithmetic mean (75+65)/2 = 70 is WRONG!

### Solution via Technique:
**Weighted Average Formula:**
$$\bar{x} = \frac{n_1 \bar{x_1} + n_2 \bar{x_2}}{n_1 + n_2}$$

$$\bar{x} = \frac{40 \times 75 + 60 \times 65}{40 + 60} = \frac{3000 + 3900}{100} = \frac{6900}{100} = 69$$

**Answer: 69**

**5-Second Snap-Check:** Combined average should be closer to Class B's average (65) since B has more students. 69 < 70 ✓

---

## Question 2 | Average Change on Addition (NAT)

**Problem:** The average of 10 numbers is 25. If a new number is added, the average becomes 27. Find the new number.

### Solution via Technique:
**Sum of original 10 numbers:** $10 \times 25 = 250$

**Sum of 11 numbers:** $11 \times 27 = 297$

**New number:** $297 - 250 = 47$

**Answer: 47**

**Alternative Quick Method:** 
New number = New average + (Number of original items × Increase in average)
$$= 27 + 10 \times 2 = 27 + 20 = 47$$

---

## Question 3 | Average Change on Removal (NAT)

**Problem:** The average age of 30 students is 15 years. If the teacher's age is included, the average becomes 16 years. Find the teacher's age.

### Solution via Technique:
**Sum of students' ages:** $30 \times 15 = 450$

**Sum including teacher:** $31 \times 16 = 496$

**Teacher's age:** $496 - 450 = 46$

**Answer: 46**

**Quick Formula:** Teacher's age = New average + n × (Increase) = 16 + 30 × 1 = 46 ✓

---

## Question 4 | Replacement Average (NAT)

**Problem:** The average of 8 numbers is 27. One number (23) is replaced by a new number, and the average increases by 3. Find the new number.

**Trap Alert:** The new number is NOT simply 23 + 3!

### Solution via Technique:
**Change in sum = Change in average × n**
$$\Delta S = 3 \times 8 = 24$$

**New number = Old number + Change in sum**
$$= 23 + 24 = 47$$

**Answer: 47**

**Verification:** 
Original sum = 8 × 27 = 216
New sum = 216 - 23 + 47 = 240
New average = 240/8 = 30 = 27 + 3 ✓

---

## Question 5 | Successive Averages (NAT)

**Problem:** A batsman's average after 20 innings is 45. After the 21st innings, his average becomes 47. How many runs did he score in the 21st innings?

### Solution via Technique:
**Runs in 21st innings = New average + (Old innings × Increase)**
$$= 47 + 20 \times 2 = 47 + 40 = 87$$

**Answer: 87**

---

## Question 6 | Average Speed Trap (NAT)

**Problem:** A car travels from A to B at 60 km/h and returns at 40 km/h. Find the average speed for the entire journey. (Answer in km/h)

**Trap Alert:** Average speed ≠ (60 + 40)/2 = 50!

### Solution via Technique:
**For equal distances, use Harmonic Mean:**
$$\bar{v} = \frac{2v_1 v_2}{v_1 + v_2} = \frac{2 \times 60 \times 40}{60 + 40} = \frac{4800}{100} = 48$$

**Answer: 48**

**Why not 50?** 
The car spends MORE TIME at the slower speed (40 km/h), pulling the average down.

**Verification:** Let distance = 120 km each way.
- Time A→B = 120/60 = 2 hours
- Time B→A = 120/40 = 3 hours
- Total time = 5 hours, Total distance = 240 km
- Average speed = 240/5 = 48 km/h ✓

---

## Question 7 | Average of First n Natural Numbers (NAT)

**Problem:** Find the average of first 100 positive integers.

### Solution via Technique:
**Sum of first n natural numbers:** $S = \frac{n(n+1)}{2}$

**Average:** $\bar{x} = \frac{S}{n} = \frac{n+1}{2}$

For n = 100: $\bar{x} = \frac{101}{2} = 50.5$

**Answer: 50.5**

---

## Question 8 | Average of Multiples (NAT)

**Problem:** Find the average of all multiples of 7 between 100 and 500.

### Solution via Technique:
**First multiple ≥ 100:** 105 (since 100/7 = 14.28, so 15×7 = 105)
**Last multiple ≤ 500:** 497 (since 500/7 = 71.43, so 71×7 = 497)

**For arithmetic progression, Average = (First + Last)/2**
$$\bar{x} = \frac{105 + 497}{2} = \frac{602}{2} = 301$$

**Answer: 301**

---

## Question 9 | Average with Missing Data (NAT)

**Problem:** The average of 11 numbers is 50. The average of first 6 numbers is 49, and the average of last 6 numbers is 52. Find the 6th number (the middle one, counted in both groups).

**Trap Alert:** The 6th number is counted twice!

### Solution via Technique:
**Total sum:** $11 \times 50 = 550$
**Sum of first 6:** $6 \times 49 = 294$
**Sum of last 6:** $6 \times 52 = 312$

**The 6th number is in both sums:**
$$294 + 312 - 550 = 56$$

**Answer: 56**

---

## Question 10 | Running Average (NAT)

**Problem:** The average of 5 consecutive even numbers is 36. Find the largest number.

### Solution via Technique:
**For consecutive (even) numbers, Average = Middle term**

Middle term = 36

Numbers: 32, 34, **36**, 38, 40

**Largest = 40**

**Answer: 40**

---

## Question 11 | Average Age Problem (NAT)

**Problem:** 5 years ago, the average age of a family of 4 was 30 years. A baby was born, and the present average age is 28 years. Find the baby's current age.

### Solution via Technique:
**Sum of ages 5 years ago:** $4 \times 30 = 120$

**Present sum of 4 original members:** $120 + (4 \times 5) = 140$

**Present sum of all 5 members (including baby):** $5 \times 28 = 140$

**Baby's age:** $140 - 140 = 0$

**Interpretation:** The baby was just born (age ≈ 0). This is mathematically consistent—the addition of a newborn (age 0) doesn't change the total sum, but increases the count, which lowers the average from 35 (what 4 members would average now) to 28.

**Verification:** If baby = 0: Sum = 140, Average = 140/5 = 28 ✓

**Answer: 0** (newborn)

---

## Question 12 | Median vs Mean (MSQ)

**Problem:** For the dataset {2, 3, 5, 7, 83}, which statements are TRUE?

A) Mean = 20  
B) Median = 5  
C) Mean > Median  
D) The distribution is right-skewed

### Solution via Technique:
**Mean:** $(2+3+5+7+83)/5 = 100/5 = 20$ ✓ A is TRUE

**Median:** Middle value (3rd of 5) = 5 ✓ B is TRUE

**Mean (20) > Median (5):** ✓ C is TRUE

**Right-skewed:** When mean > median, distribution is right-skewed (tail on right). ✓ D is TRUE

**Answer: A, B, C, D (all TRUE)**

---

## Question 13 | Geometric Mean (NAT)

**Problem:** Find the geometric mean of 4, 8, and 16.

### Solution via Technique:
**Geometric Mean:** $GM = \sqrt[n]{\prod x_i}$

$$GM = \sqrt[3]{4 \times 8 \times 16} = \sqrt[3]{512} = 8$$

**Answer: 8**

**Note:** For numbers in GP, GM = middle term. Here 4, 8, 16 is a GP with ratio 2, so GM = 8 ✓

---

## Question 14 | Harmonic Mean (NAT)

**Problem:** Find the harmonic mean of 2, 4, and 8.

### Solution via Technique:
**Harmonic Mean:** $HM = \frac{n}{\sum \frac{1}{x_i}}$

$$HM = \frac{3}{\frac{1}{2} + \frac{1}{4} + \frac{1}{8}} = \frac{3}{\frac{4+2+1}{8}} = \frac{3 \times 8}{7} = \frac{24}{7} \approx 3.43$$

**Answer: 24/7 or 3.43**

---

## Question 15 | Relationship AM ≥ GM ≥ HM (MSQ)

**Problem:** For positive numbers a and b, which is/are always TRUE?

A) AM ≥ GM  
B) GM ≥ HM  
C) AM × HM = GM²  
D) AM = GM = HM only when a = b

### Solution via Technique:
For two positive numbers a, b:
- AM = (a+b)/2
- GM = √(ab)
- HM = 2ab/(a+b)

**Verify each:**

**A) AM ≥ GM:** 
$(a+b)/2 \geq \sqrt{ab}$
$a + b \geq 2\sqrt{ab}$
$(\sqrt{a} - \sqrt{b})^2 \geq 0$ ✓ Always TRUE

**B) GM ≥ HM:**
$\sqrt{ab} \geq 2ab/(a+b)$
$(a+b)\sqrt{ab} \geq 2ab$
$(a+b) \geq 2\sqrt{ab}$ (same as A) ✓ Always TRUE

**C) AM × HM = GM²:**
$\frac{a+b}{2} \times \frac{2ab}{a+b} = ab = (\sqrt{ab})^2 = GM^2$ ✓ TRUE

**D) Equality iff a = b:** The inequality becomes equality only when $(\sqrt{a} - \sqrt{b})^2 = 0$, i.e., a = b ✓ TRUE

**Answer: A, B, C, D (all TRUE)**

---

## Question 16 | Deviation from Mean (NAT)

**Problem:** The average of 10 numbers is 20. If each number is increased by 15%, find the new average.

### Solution via Technique:
**If each number is scaled by factor k, the average is also scaled by k.**

$$\text{New average} = 20 \times 1.15 = 23$$

**Answer: 23**

---

## Question 17 | Combining Unequal Groups (NAT)

**Problem:** Three sections A, B, C have average marks 70, 80, 90 with students in ratio 3:4:5. Find the overall average.

### Solution via Technique:
**Weighted Average:**
$$\bar{x} = \frac{3 \times 70 + 4 \times 80 + 5 \times 90}{3 + 4 + 5}$$
$$= \frac{210 + 320 + 450}{12} = \frac{980}{12} = 81.67$$

**Answer: 81.67**

---

## Question 18 | Average of Squares (NAT)

**Problem:** Find the average of squares of first 10 natural numbers.

### Solution via Technique:
**Sum of squares:** $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$

For n = 10:
$$\sum = \frac{10 \times 11 \times 21}{6} = \frac{2310}{6} = 385$$

**Average:** $385/10 = 38.5$

**Answer: 38.5**

---

## Question 19 | Wrong Entry Correction (NAT)

**Problem:** The average of 20 numbers was calculated as 35, but later it was found that one number was wrongly read as 48 instead of 84. Find the correct average.

### Solution via Technique:
**Incorrect sum:** $20 \times 35 = 700$

**Correct sum:** $700 - 48 + 84 = 736$

**Correct average:** $736/20 = 36.8$

**Answer: 36.8**

---

## Question 20 | Algebraic Average (NAT)

**Problem:** If the average of $x, 2x+1, 3x+2, 4x+3, 5x+4$ is 25, find $x$.

### Solution via Technique:
**Sum = 5 × Average**
$$x + (2x+1) + (3x+2) + (4x+3) + (5x+4) = 5 \times 25$$
$$15x + 10 = 125$$
$$15x = 115$$
$$x = 115/15 = 23/3 \approx 7.67$$

**Answer: 23/3 or 7.67**

---

## Question 21 | Average Cricket Problem (NAT)

**Problem:** A cricketer's average increases by 4 after scoring 92 in his 18th innings. What is his new average?

### Solution via Technique:
Let old average = A

**After 17 innings:** Sum = 17A
**After 18 innings:** Sum = 17A + 92
**New average:** $(17A + 92)/18 = A + 4$

$$17A + 92 = 18A + 72$$
$$92 - 72 = 18A - 17A$$
$$A = 20$$

**New average = 20 + 4 = 24**

**Answer: 24**

---

## Question 22 | Temperature Average (NAT)

**Problem:** The average temperature for Monday to Wednesday was 37°C. The average for Tuesday to Thursday was 38°C. If Thursday's temperature was 40°C, find Monday's temperature.

### Solution via Technique:
Let M, T, W, Th = temperatures for respective days.

**Equation 1:** $(M + T + W)/3 = 37 \Rightarrow M + T + W = 111$
**Equation 2:** $(T + W + Th)/3 = 38 \Rightarrow T + W + Th = 114$
**Given:** $Th = 40$

From Eq 2: $T + W = 114 - 40 = 74$

Substitute in Eq 1: $M + 74 = 111 \Rightarrow M = 37$

**Answer: 37°C**

---

## Mental Machinery

### The Bizarre Mnemonic for Averages:
**"Average is the BALANCER on a seesaw!"**

Imagine all numbers as kids on a seesaw. The average is where you'd place the fulcrum to balance perfectly. Heavier kids (larger numbers) pull the average toward them.

### The Mental Slider for Speed Problems:
**"Time is the ENEMY of high speed!"**

At slower speeds, you spend MORE time, which dominates the average:
- Harmonic mean < Arithmetic mean
- More time at slow speed → lower average

### The 5-Second Snap-Checks:
- **Average of consecutive numbers = middle value**
- **Adding a number above average → average increases**
- **For equal distances: Use Harmonic Mean for average speed**
- **For equal times: Use Arithmetic Mean for average speed**
- **AM ≥ GM ≥ HM** (equality only when all numbers equal)

---

## Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]. 

Would you like to initiate a **'Multi-Variable Stress Test'** combining Average with Percentage for a Rank-1 simulation?
