# Data Sufficiency | Supreme Architect Question Bank

## Logic Coverage Mandate
This question set exhausts the logic-space for Data Sufficiency problems across GATE, ESE, PSU, and Banking exams. Each question destroys a specific memorized shortcut and introduces unique reasoning patterns.

---

## Question 1: The Illusion of Complete Data

### Best Technique
Never solve completely. Ask: "Can this be solved?" not "What is the answer?" Test if multiple values are possible.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Missing data illusion
- **Secondary Logic Interactions:** Hidden constraint dominance, Assumption poisoning
- **Why This Logic is Rare and Lethal:** Data appears complete but is actually underdetermined.

### 2️⃣ Question
What is the value of x?
Statement I: x² = 16
Statement II: x is a real number

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests recognition that squares have two roots
- Why Top-100 candidates fail: They assume x = 4 without considering -4

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Check what each statement provides
2. Statement I: x² = 16 → x = ±4 (two possible values)
3. Statement II: x is real (doesn't help narrow down)
4. Combined: Still x = 4 or x = -4
5. Answer: (D) Both statements together are not sufficient
- **Rejection of Wrong Paths:** Don't assume positive root only

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (A)
- **Why It Feels Correct:** x² = 16 seems to determine x
- **Exact Point of Failure:** Forgetting negative root

### 6️⃣ Generalization Map
1. Use higher degree polynomials
2. Include complex number possibilities
3. Add absolute value equations
4. Use inequalities instead
5. Include "positive integer" constraint

### 7️⃣ Neural Anchor
**"Square = Two Roots"**

---

## Question 2: The Redundant Statement Trap

### Best Technique
Check if one statement is derivable from the other. Redundant information doesn't add value.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Ghost variable cancellation
- **Secondary Logic Interactions:** Hidden constraint dominance, Overfitting to standard models
- **Why This Logic is Rare and Lethal:** Statements look different but convey the same information.

### 2️⃣ Question
Is x positive?
Statement I: x + 5 > 5
Statement II: 2x > 0

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests recognition of equivalent statements
- Why Top-100 candidates fail: They don't simplify statements

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Simplify each statement
2. Statement I: x + 5 > 5 → x > 0 (x is positive)
3. Statement II: 2x > 0 → x > 0 (x is positive)
4. Both statements say the same thing: x > 0
5. Either alone is sufficient to answer "Is x positive?" → YES
6. Answer: (E) Either statement alone is sufficient
- **Rejection of Wrong Paths:** Don't look for additional information in combination

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Two statements seem to provide more certainty
- **Exact Point of Failure:** Statements are equivalent

### 6️⃣ Generalization Map
1. Use more complex equivalent forms
2. Include trigonometric equivalents
3. Add logarithmic forms
4. Use geometric interpretations
5. Include modular arithmetic equivalents

### 7️⃣ Neural Anchor
**"Simplify First"**

---

## Question 3: The Uniqueness vs Sufficiency

### Best Technique
Sufficiency means "unique answer determinable," not "answer calculable easily."

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Multiple valid methods — only one legal
- **Secondary Logic Interactions:** Conservation vs optimization conflict, Boundary-condition collapse
- **Why This Logic is Rare and Lethal:** Data may be sufficient even if calculation is complex.

### 2️⃣ Question
What is the area of triangle ABC?
Statement I: AB = 5 cm, BC = 7 cm, CA = 8 cm
Statement II: Triangle ABC is right-angled at B

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests understanding that three sides determine area uniquely
- Why Top-100 candidates fail: They think they need height or angles

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** What's needed for area?
2. Statement I: Three sides → Use Heron's formula → Unique area (sufficient)
3. Statement II: Right angle at B, but no sides → Cannot compute (insufficient)
4. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** Don't combine when one is already sufficient

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** More information seems better
- **Exact Point of Failure:** Statement I alone uniquely determines area

### 6️⃣ Generalization Map
1. Use different triangle properties
2. Include circumradius/inradius
3. Add coordinate geometry versions
4. Use two sides plus included angle
5. Include similar triangle problems

### 7️⃣ Neural Anchor
**"Three Sides = Unique"**

---

## Question 4: The Yes/No Question Trap

### Best Technique
For yes/no questions, sufficient means "definitively yes" OR "definitively no" — not "probably."

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Intuition vs formal logic conflict
- **Secondary Logic Interactions:** Limiting-case override, False linearity assumption
- **Why This Logic is Rare and Lethal:** "Always no" is just as sufficient as "always yes."

### 2️⃣ Question
Is n divisible by 6?
Statement I: n is divisible by 3
Statement II: n is divisible by 2

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests LCM concept for divisibility
- Why Top-100 candidates fail: They don't realize 6 = 2 × 3 (coprime)

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** What does divisible by 6 require?
2. 6 = 2 × 3, and gcd(2,3) = 1
3. Statement I alone: n divisible by 3, but maybe not 2 → Insufficient
4. Statement II alone: n divisible by 2, but maybe not 3 → Insufficient
5. Combined: n divisible by both 2 and 3 → n divisible by 6
6. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither statement alone determines divisibility by 6

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** May think factors need to be consecutive
- **Exact Point of Failure:** Coprime factors multiply to LCM

### 6️⃣ Generalization Map
1. Use non-coprime factors
2. Include composite divisibility
3. Add GCD-based questions
4. Use prime factorization
5. Include modular conditions

### 7️⃣ Neural Anchor
**"Coprime Factors Combine"**

---

## Question 5: The Hidden Constraint Discovery

### Best Technique
Look for constraints implied but not stated (like "age must be positive").

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Hidden constraint dominance
- **Secondary Logic Interactions:** Assumption poisoning, Boundary-condition collapse
- **Why This Logic is Rare and Lethal:** Real-world constraints may make otherwise insufficient data sufficient.

### 2️⃣ Question
What is A's age?
Statement I: A's age is a perfect square
Statement II: A's age is between 20 and 30

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests intersection of constraints
- Why Top-100 candidates fail: They don't identify unique value exists

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Find intersection of conditions
2. Statement I: Perfect squares: 1, 4, 9, 16, 25, 36, 49... (multiple values)
3. Statement II: Age between 20 and 30: 21, 22, 23, 24, 25, 26, 27, 28, 29 (multiple values)
4. Combined: Perfect square AND between 20-30: Only 25
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither alone gives unique value

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** Constraints seem loose
- **Exact Point of Failure:** Intersection has only one element

### 6️⃣ Generalization Map
1. Use different number properties
2. Include prime number constraints
3. Add divisibility conditions
4. Use range overlaps
5. Include age-relationship constraints

### 7️⃣ Neural Anchor
**"Intersection = Unique?"**

---

## Question 6: The Geometric Constraint

### Best Technique
In geometry, verify if given data uniquely determines the figure (up to congruence).

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Overfitting to standard models
- **Secondary Logic Interactions:** Symmetry exploitation, Dimensional contradiction
- **Why This Logic is Rare and Lethal:** Some geometric data determines shape but not size.

### 2️⃣ Question
What is the perimeter of rectangle ABCD?
Statement I: Area of ABCD is 24 sq cm
Statement II: Diagonal of ABCD is 10 cm

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests whether two conditions determine rectangle uniquely
- Why Top-100 candidates fail: They don't set up the system of equations

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Set up equations
2. Let length = l, width = w
3. Statement I: l × w = 24 (one equation, two unknowns)
4. Statement II: l² + w² = 100 (one equation, two unknowns)
5. Combined: l × w = 24, l² + w² = 100
6. Perimeter = 2(l + w). Can we find l + w?
7. (l + w)² = l² + 2lw + w² = 100 + 48 = 148
8. l + w = √148, Perimeter = 2√148 (unique value)
9. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither alone gives perimeter

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** Two unknowns with two equations seems underdetermined
- **Exact Point of Failure:** We only need l + w, not individual values

### 6️⃣ Generalization Map
1. Use parallelogram instead
2. Include angle constraints
3. Add ratio conditions
4. Use circle inscribed/circumscribed
5. Include 3D extensions

### 7️⃣ Neural Anchor
**"Sum Without Parts"**

---

## Question 7: The Rate Problem

### Best Technique
Identify if rate × time = work/distance relationship can be uniquely determined.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Ghost variable cancellation
- **Secondary Logic Interactions:** Conservation vs optimization conflict, Order-of-magnitude deception
- **Why This Logic is Rare and Lethal:** Relative rates may determine time even without individual rates.

### 2️⃣ Question
How long does A take to complete a work alone?
Statement I: A and B together complete the work in 6 days
Statement II: B alone completes the work in 12 days

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests work rate calculation
- Why Top-100 candidates fail: They correctly identify that both are needed

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Work rate addition
2. Statement I: A + B rate = 1/6 per day
3. Statement II: B rate = 1/12 per day
4. Combined: A rate = 1/6 - 1/12 = 1/12 per day → A takes 12 days
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Each alone is insufficient

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (A)
- **Why It Feels Correct:** Combined time seems informative
- **Exact Point of Failure:** Can't separate A's contribution without B's rate

### 6️⃣ Generalization Map
1. Add third worker
2. Include efficiency ratios
3. Use alternate working patterns
4. Add work-pause scenarios
5. Include partial completion data

### 7️⃣ Neural Anchor
**"Combined Needs Parts"**

---

## Question 8: The Algebraic Identity

### Best Technique
Use algebraic identities to combine given information (e.g., x + y and xy to find x² + y²).

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Reverse reasoning (answer → question)
- **Secondary Logic Interactions:** Ghost variable cancellation, Symmetry exploitation
- **Why This Logic is Rare and Lethal:** The question asks for something derivable from given but not directly stated.

### 2️⃣ Question
What is the value of x² + y²?
Statement I: x + y = 5
Statement II: xy = 6

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests algebraic identity: (x+y)² = x² + 2xy + y²
- Why Top-100 candidates fail: They try to find x and y individually

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Recognize the identity
2. x² + y² = (x + y)² - 2xy
3. Statement I: x + y = 5, but xy unknown → Insufficient
4. Statement II: xy = 6, but x + y unknown → Insufficient
5. Combined: x² + y² = 25 - 12 = 13
6. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Don't solve for x and y individually

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** Seems like two unknowns
- **Exact Point of Failure:** Identity provides direct calculation

### 6️⃣ Generalization Map
1. Use x³ + y³
2. Include x² - y²
3. Add 1/x + 1/y type questions
4. Use symmetric functions
5. Include three-variable identities

### 7️⃣ Neural Anchor
**"Identity Bypasses"**

---

## Question 9: The Probability Question

### Best Technique
Check if probability can be uniquely determined or if it lies in a range.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** False linearity assumption
- **Secondary Logic Interactions:** Boundary-condition collapse, Limiting-case override
- **Why This Logic is Rare and Lethal:** Probability may be determinable even with seemingly incomplete data.

### 2️⃣ Question
What is the probability of drawing a red ball from a bag?
Statement I: The bag contains only red and blue balls
Statement II: The ratio of red to blue balls is 3:2

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests understanding that ratio determines probability
- Why Top-100 candidates fail: They think they need total count

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** What determines probability?
2. Statement I: Only red and blue → Probability exists but not determined
3. Statement II: Ratio 3:2 → P(red) = 3/(3+2) = 3/5
4. Wait: Statement II alone sufficient if bag has only red and blue (implied)
5. If Statement II implies only these colors exist, then B is sufficient
6. But if other colors possible, need Statement I
7. Typically, ratio statement implies only those items exist
8. Answer: (B) Statement II alone is sufficient
- **Rejection of Wrong Paths:** Ratio gives probability directly

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Both seem necessary
- **Exact Point of Failure:** Ratio directly gives probability fraction

### 6️⃣ Generalization Map
1. Add more colors
2. Include conditional probability
3. Use with/without replacement
4. Add ball-drawing sequences
5. Include independence questions

### 7️⃣ Neural Anchor
**"Ratio = Probability"**

---

## Question 10: The Uniqueness of Average

### Best Technique
Average with count gives sum; average without count needs additional info.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Missing data illusion
- **Secondary Logic Interactions:** Ghost variable cancellation, Order-of-magnitude deception
- **Why This Logic is Rare and Lethal:** Average alone doesn't determine sum without count.

### 2️⃣ Question
What is the sum of 5 numbers?
Statement I: Average of 5 numbers is 20
Statement II: Largest number is 40

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests average-sum relationship
- Why Top-100 candidates fail: They overlook that Statement I directly gives sum

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Sum = Average × Count
2. Statement I: Average = 20, Count = 5 → Sum = 100 (sufficient)
3. Statement II: Largest = 40, no info on others (insufficient)
4. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** Statement II adds no value

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** More data seems helpful
- **Exact Point of Failure:** Average × Count = Sum directly

### 6️⃣ Generalization Map
1. Ask for median instead
2. Include weighted average
3. Add range constraints
4. Use arithmetic vs geometric mean
5. Include variance questions

### 7️⃣ Neural Anchor
**"Average × Count = Sum"**

---

## Question 11: The Profit/Loss Determination

### Best Technique
Profit needs Cost Price and Selling Price. Either both or the relationship between them.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Conservation vs optimization conflict
- **Secondary Logic Interactions:** Order-of-magnitude deception, False linearity assumption
- **Why This Logic is Rare and Lethal:** Percentage profit can be found without knowing actual prices.

### 2️⃣ Question
What is the profit percentage?
Statement I: Selling Price is 1.2 times the Cost Price
Statement II: Cost Price is Rs. 500

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests percentage profit formula
- Why Top-100 candidates fail: They think absolute values are needed

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Profit % = (SP - CP)/CP × 100
2. Statement I: SP = 1.2 × CP → Profit % = (1.2CP - CP)/CP × 100 = 20%
3. Statement II: CP = 500, but SP unknown → Insufficient
4. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** Absolute CP not needed for percentage

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Actual prices seem necessary
- **Exact Point of Failure:** Ratio determines percentage

### 6️⃣ Generalization Map
1. Include discount scenarios
2. Add marked price
3. Use successive discounts
4. Include loss percentage
5. Add cost with overhead

### 7️⃣ Neural Anchor
**"Ratio = Percentage"**

---

## Question 12: The Counting Problem

### Best Technique
For counting, check if constraints uniquely determine the count or leave ambiguity.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Discrete vs continuous trap
- **Secondary Logic Interactions:** Boundary-condition collapse, Overfitting to standard models
- **Why This Logic is Rare and Lethal:** Integer constraints may uniquely determine values.

### 2️⃣ Question
How many students scored above 80?
Statement I: 40% of students scored above 80
Statement II: Total students in class is 25

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests percentage to absolute conversion
- Why Top-100 candidates fail: They might not realize 40% of 25 = 10 is an integer

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Need percentage and total
2. Statement I: 40% scored above 80, but total unknown → Insufficient
3. Statement II: Total = 25, but percentage unknown → Insufficient
4. Combined: 40% of 25 = 10 students
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither alone works

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D) if 40% of 25 seems non-integer
- **Why It Feels Correct:** May think 0.4 × 25 = 10.0 ≠ integer
- **Exact Point of Failure:** 10 is indeed an integer

### 6️⃣ Generalization Map
1. Use non-integer-producing percentages
2. Include "at least" conditions
3. Add multiple groups
4. Use ratios instead of percentages
5. Include exclusion criteria

### 7️⃣ Neural Anchor
**"Check Integer Result"**

---

## Question 13: The Comparison Question

### Best Technique
For "Is A > B?" questions, check if the comparison can be definitively made.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Intuition vs formal logic conflict
- **Secondary Logic Interactions:** Assumption poisoning, Boundary-condition collapse
- **Why This Logic is Rare and Lethal:** Comparison may be determinate even when values aren't.

### 2️⃣ Question
Is x > y?
Statement I: x - y > 0
Statement II: x + y > 0

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests direct inequality interpretation
- Why Top-100 candidates fail: They overcomplicate

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** What does each statement say?
2. Statement I: x - y > 0 → x > y (SUFFICIENT: Answer is YES)
3. Statement II: x + y > 0 → No info on comparison (x=10, y=-5 vs x=-5, y=10)
4. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** Statement II doesn't determine relative values

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Two statements seem better
- **Exact Point of Failure:** Statement I directly answers the question

### 6️⃣ Generalization Map
1. Use product instead of sum
2. Include absolute values
3. Add quadratic conditions
4. Use ratio comparisons
5. Include three-variable comparisons

### 7️⃣ Neural Anchor
**"Difference = Comparison"**

---

## Question 14: The Time-Distance Problem

### Best Technique
Verify if speed and distance/time relationships uniquely determine the answer.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Order-of-magnitude deception
- **Secondary Logic Interactions:** Conservation vs optimization conflict, Ghost variable cancellation
- **Why This Logic is Rare and Lethal:** Multiple speed-time combinations can give same distance.

### 2️⃣ Question
What is the speed of the car?
Statement I: Car covers 120 km
Statement II: Car travels for 3 hours

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests basic speed formula
- Why Top-100 candidates fail: They might add complications

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Speed = Distance / Time
2. Statement I: Distance = 120 km, time unknown → Insufficient
3. Statement II: Time = 3 hours, distance unknown → Insufficient
4. Combined: Speed = 120/3 = 40 km/hr
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Both distance and time needed

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D) if assuming uniform speed not stated
- **Why It Feels Correct:** Speed might vary
- **Exact Point of Failure:** Average speed = Total Distance / Total Time

### 6️⃣ Generalization Map
1. Include multiple legs of journey
2. Add relative speed problems
3. Use upstream/downstream
4. Include rest periods
5. Add acceleration considerations

### 7️⃣ Neural Anchor
**"Distance ÷ Time = Speed"**

---

## Question 15: The Percentage Change

### Best Technique
Percentage change needs original value. Successive changes compound multiplicatively.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** False linearity assumption
- **Secondary Logic Interactions:** Order-of-magnitude deception, Assumption poisoning
- **Why This Logic is Rare and Lethal:** Successive percentage changes don't add linearly.

### 2️⃣ Question
What is the final price after two successive discounts?
Statement I: First discount is 20%, second discount is 30%
Statement II: Original price is Rs. 1000

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests successive discount calculation
- Why Top-100 candidates fail: They may add percentages (50% total)

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Successive discounts multiply
2. Statement I: 20% then 30% → Final = Original × 0.8 × 0.7 = 0.56 × Original
3. Statement II: Original = 1000, but no discount info → Insufficient
4. Combined: Final = 1000 × 0.56 = Rs. 560
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Don't add percentages

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (A)
- **Why It Feels Correct:** Discount percentages known
- **Exact Point of Failure:** Need original price for absolute final price

### 6️⃣ Generalization Map
1. Ask for effective discount percentage
2. Include price increase scenarios
3. Add three successive changes
4. Use different bases for each change
5. Include tax after discount

### 7️⃣ Neural Anchor
**"Absolute Needs Base"**

---

## Question 16: The Either-Sufficient Scenario

### Best Technique
When both statements independently give the answer, check if they give the SAME answer.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Multiple valid methods — only one legal
- **Secondary Logic Interactions:** Symmetry exploitation, Local correctness global failure
- **Why This Logic is Rare and Lethal:** Both may be sufficient individually but give different answers (contradiction).

### 2️⃣ Question
What is the value of |x|?
Statement I: x² = 25
Statement II: x³ = 125

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests absolute value with different powers
- Why Top-100 candidates fail: They may not realize both work independently

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** |x| is always non-negative
2. Statement I: x² = 25 → x = ±5 → |x| = 5 (sufficient)
3. Statement II: x³ = 125 → x = 5 → |x| = 5 (sufficient)
4. Both give |x| = 5
5. Answer: (E) Either statement alone is sufficient
- **Rejection of Wrong Paths:** Don't combine when both work independently

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Using both seems thorough
- **Exact Point of Failure:** Absolute value resolves x² ambiguity

### 6️⃣ Generalization Map
1. Use conflicting values
2. Include even/odd power comparisons
3. Add modular arithmetic
4. Use logarithmic forms
5. Include complex number extensions

### 7️⃣ Neural Anchor
**"|x| Absorbs Sign"**

---

## Question 17: The Geometric Angle

### Best Technique
In geometry, angle relationships (supplementary, complementary, triangle sum) provide constraints.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Hidden constraint dominance
- **Secondary Logic Interactions:** Symmetry exploitation, Overfitting to standard models
- **Why This Logic is Rare and Lethal:** Standard angle relationships often provide hidden constraints.

### 2️⃣ Question
What is angle A in triangle ABC?
Statement I: Angle B = 60°
Statement II: Triangle ABC is isosceles with AB = AC

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests isosceles triangle angle properties
- Why Top-100 candidates fail: They may not connect equal sides to equal angles

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Apply triangle properties
2. Statement I: Angle B = 60°, but A and C unknown → Insufficient
3. Statement II: AB = AC → Angles B = C, but values unknown → Insufficient
4. Combined: B = 60°, and B = C → C = 60°, so A = 180 - 60 - 60 = 60°
5. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither alone determines A

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (B)
- **Why It Feels Correct:** Isosceles seems to determine shape
- **Exact Point of Failure:** Isosceles only says two angles equal, not their values

### 6️⃣ Generalization Map
1. Use equilateral conditions
2. Include exterior angles
3. Add right angle conditions
4. Use similar triangles
5. Include inscribed angle scenarios

### 7️⃣ Neural Anchor
**"Equal Sides = Equal Angles"**

---

## Question 18: The Digit Problem

### Best Technique
Use place value constraints and divisibility rules for digit problems.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Boundary-condition collapse
- **Secondary Logic Interactions:** Discrete vs continuous trap, Order-of-magnitude deception
- **Why This Logic is Rare and Lethal:** Digit constraints are inherently discrete (0-9).

### 2️⃣ Question
What is the two-digit number?
Statement I: Sum of digits is 9
Statement II: Number is divisible by 9

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests that Statement II implies Statement I for two-digit numbers
- Why Top-100 candidates fail: They don't see the redundancy

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Divisibility by 9 means digit sum divisible by 9
2. Statement I: Digit sum = 9 → Numbers: 18, 27, 36, 45, 54, 63, 72, 81, 90 (multiple)
3. Statement II: Divisible by 9 → Numbers: 18, 27, 36, ... 99 (multiple)
4. Combined: Same as Statement I (all numbers in I are divisible by 9)
5. Still multiple possibilities
6. Answer: (D) Both statements together are not sufficient
- **Rejection of Wrong Paths:** Statements are effectively equivalent

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Two conditions seem to narrow down
- **Exact Point of Failure:** Both conditions describe same set

### 6️⃣ Generalization Map
1. Use different digit sums
2. Include three-digit numbers
3. Add product of digits
4. Use alternating digit sums
5. Include palindrome conditions

### 7️⃣ Neural Anchor
**"Check Redundancy"**

---

## Question 19: The Sequence Question

### Best Technique
Identify sequence type (AP, GP, etc.) and what's needed to find a specific term.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Overfitting to standard models
- **Secondary Logic Interactions:** Ghost variable cancellation, False linearity assumption
- **Why This Logic is Rare and Lethal:** Sequence type must be verified, not assumed.

### 2️⃣ Question
What is the 10th term of an AP?
Statement I: First term is 5
Statement II: Sum of first 10 terms is 100

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests AP sum and term relationship
- Why Top-100 candidates fail: They may think they need common difference explicitly

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Use AP formulas
2. S_n = n/2 × (2a + (n-1)d) or n/2 × (first + last)
3. Statement I: a = 5, but d unknown → Insufficient
4. Statement II: S_10 = 100 → 10/2 × (a + a_10) = 100 → a + a_10 = 20
5. Still need a or a_10 individually → Insufficient
6. Combined: a = 5, and a + a_10 = 20 → a_10 = 15
7. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Sum alone doesn't give 10th term without first term

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (B)
- **Why It Feels Correct:** Sum of 10 terms seems complete
- **Exact Point of Failure:** Need first term to find specific term

### 6️⃣ Generalization Map
1. Use GP instead
2. Ask for common difference
3. Include negative terms
4. Add boundary term questions
5. Use sum of n terms formula variations

### 7️⃣ Neural Anchor
**"AP Needs Two Constants"**

---

## Question 20: The Logical Negation

### Best Technique
Sometimes proving "No" is just as valid as proving "Yes" for sufficiency.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Intuition vs formal logic conflict
- **Secondary Logic Interactions:** Reverse reasoning, Assumption poisoning
- **Why This Logic is Rare and Lethal:** Definite "No" counts as sufficient answer.

### 2️⃣ Question
Is n prime?
Statement I: n is divisible by 6
Statement II: n > 10

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests that divisibility by 6 implies "not prime"
- Why Top-100 candidates fail: They think sufficiency requires "Yes" answer

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Prime has only two factors: 1 and itself
2. Statement I: n divisible by 6 → n ≥ 6 and has factors 2 and 3
3. If n = 6, factors are 1, 2, 3, 6 → Not prime
4. Any n divisible by 6 is NOT prime (answer is definite NO)
5. Statement I is sufficient (answer is NO)
6. Statement II: n > 10 doesn't determine primality (11 is prime, 12 is not)
7. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** "No" is a valid sufficient answer

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** Need to determine the number itself
- **Exact Point of Failure:** We only need Yes/No, not the value

### 6️⃣ Generalization Map
1. Use divisibility by other numbers
2. Include "n is odd" conditions
3. Add perfect square conditions
4. Use factorial divisibility
5. Include coprimality questions

### 7️⃣ Neural Anchor
**"No = Sufficient"**

---

## Question 21: The Inequality Range

### Best Technique
Check if statement gives definite range or leaves options open.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Boundary-condition collapse
- **Secondary Logic Interactions:** Limiting-case override, False linearity assumption
- **Why This Logic is Rare and Lethal:** Open vs closed boundaries matter for sufficiency.

### 2️⃣ Question
Is x between 0 and 10?
Statement I: x > -5
Statement II: x < 15

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests range intersection
- Why Top-100 candidates fail: They think combined range determines the answer

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Check if x ∈ (0, 10) can be determined
2. Statement I: x > -5 (includes 0-10 but also -4, -3, ...)
3. Statement II: x < 15 (includes 0-10 but also 11, 12, ...)
4. Combined: -5 < x < 15 (includes 0-10, but also -4, 11, 12, ...)
5. Cannot definitively say Yes or No to "x between 0 and 10"
6. Answer: (D) Both statements together are not sufficient
- **Rejection of Wrong Paths:** Range (-5, 15) doesn't confirm or deny (0, 10)

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (C)
- **Why It Feels Correct:** Combined range seems narrow
- **Exact Point of Failure:** Range doesn't fall entirely within or outside (0, 10)

### 6️⃣ Generalization Map
1. Use overlapping ranges
2. Include equality boundaries
3. Add absolute value ranges
4. Use modular constraints
5. Include multiple variable ranges

### 7️⃣ Neural Anchor
**"Overlap ≠ Contained"**

---

## Question 22: The Function Value

### Best Technique
Check if function and input are both determined.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Ghost variable cancellation
- **Secondary Logic Interactions:** Missing data illusion, Hidden constraint dominance
- **Why This Logic is Rare and Lethal:** Function type matters as much as input values.

### 2️⃣ Question
What is f(5)?
Statement I: f(x) = x² + x
Statement II: f(3) = 12

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests function evaluation
- Why Top-100 candidates fail: They may think Statement II provides pattern

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Function definition needed
2. Statement I: f(x) = x² + x → f(5) = 25 + 5 = 30 (sufficient)
3. Statement II: f(3) = 12 (doesn't define f(x) uniquely)
4. Statement II: Many functions satisfy f(3) = 12
5. Answer: (A) Statement I alone is sufficient
- **Rejection of Wrong Paths:** One function value doesn't define the function

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (E)
- **Why It Feels Correct:** Statement II might seem to give pattern
- **Exact Point of Failure:** Infinite functions pass through (3, 12)

### 6️⃣ Generalization Map
1. Use multiple function values
2. Include inverse function
3. Add derivative information
4. Use recursive definitions
5. Include domain restrictions

### 7️⃣ Neural Anchor
**"Function Needs Definition"**

---

## Question 23: The Remainder Problem

### Best Technique
Use modular arithmetic: if you know n mod a and n mod b, you may determine n mod lcm(a,b).

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Discrete vs continuous trap
- **Secondary Logic Interactions:** Symmetry exploitation, Ghost variable cancellation
- **Why This Logic is Rare and Lethal:** Remainder can be determined without knowing the number.

### 2️⃣ Question
What is the remainder when n is divided by 6?
Statement I: Remainder when n is divided by 2 is 1
Statement II: Remainder when n is divided by 3 is 2

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests Chinese Remainder Theorem concept
- Why Top-100 candidates fail: They don't combine mod conditions

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Use CRT or enumeration
2. Statement I: n ≡ 1 (mod 2) → n is odd: 1, 3, 5, 7, 9, 11... (various remainders mod 6)
3. Statement II: n ≡ 2 (mod 3) → n = 2, 5, 8, 11, 14... (various remainders mod 6)
4. Combined: n ≡ 1 (mod 2) AND n ≡ 2 (mod 3)
5. Since gcd(2,3) = 1, unique solution mod 6 exists
6. n = 5 satisfies both: 5 mod 2 = 1 ✓, 5 mod 3 = 2 ✓
7. n mod 6 = 5 (unique)
8. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Neither alone gives unique mod 6

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** Seems like we need n's value
- **Exact Point of Failure:** CRT gives unique remainder

### 6️⃣ Generalization Map
1. Use non-coprime divisors
2. Include three conditions
3. Add explicit CRT problems
4. Use larger moduli
5. Include negative remainders

### 7️⃣ Neural Anchor
**"CRT Combines Mods"**

---

## Question 24: The Set Membership

### Best Technique
Check if element's set membership can be determined from given conditions.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Examiner-language misdirection
- **Secondary Logic Interactions:** Assumption poisoning, Overfitting to standard models
- **Why This Logic is Rare and Lethal:** Set definitions may overlap or conflict.

### 2️⃣ Question
Is x a member of set A?
Statement I: A = {1, 2, 3, 4, 5}
Statement II: x is a prime number less than 6

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests set intersection logic
- Why Top-100 candidates fail: They may not enumerate Statement II

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Identify what each tells us
2. Statement I: A = {1, 2, 3, 4, 5}, but x unknown → Insufficient
3. Statement II: x ∈ {2, 3, 5} (primes < 6), but A unknown → Insufficient
4. Combined: x ∈ {2, 3, 5} and A = {1, 2, 3, 4, 5}
5. All of {2, 3, 5} are in A → x is definitely in A
6. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Need both set and element definition

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (D)
- **Why It Feels Correct:** x could be 2, 3, or 5 (multiple values)
- **Exact Point of Failure:** ALL possible x values are in A

### 6️⃣ Generalization Map
1. Use overlapping but not subset sets
2. Include infinite sets
3. Add set operations
4. Use complement sets
5. Include conditional membership

### 7️⃣ Neural Anchor
**"All Possibilities In → Sufficient"**

---

## Question 25: The Optimization Question

### Best Technique
Maximum/minimum questions need constraints that fix the optimal point.

### 1️⃣ Logic Signature
- **Dominant Logic Trap:** Conservation vs optimization conflict
- **Secondary Logic Interactions:** Limiting-case override, Boundary-condition collapse
- **Why This Logic is Rare and Lethal:** Constraints may not be tight enough to determine optimum.

### 2️⃣ Question
What is the maximum value of xy?
Statement I: x + y = 10
Statement II: x > 0 and y > 0

(A) Statement I alone is sufficient
(B) Statement II alone is sufficient
(C) Both statements together are sufficient
(D) Both statements together are not sufficient
(E) Either statement alone is sufficient

### 3️⃣ Examiner's Intent
- Tests AM-GM or calculus optimization
- Why Top-100 candidates fail: They may not realize integer constraint isn't present

### 4️⃣ Solution (Logic-First)
1. **Entry Decision:** Optimize xy given x + y = 10, x,y > 0
2. Statement I alone: x + y = 10, but x or y could be negative → xy not maximized uniquely
3. Wait: if x = 100, y = -90, x + y = 10, xy = -9000
4. Statement II alone: x, y > 0 but no relation → xy unbounded
5. Combined: x + y = 10, x > 0, y > 0
6. By AM-GM: xy ≤ ((x+y)/2)² = 25, max when x = y = 5
7. Maximum xy = 25
8. Answer: (C) Both statements together are sufficient
- **Rejection of Wrong Paths:** Need positive constraint for maximum

### 5️⃣ Trap Autopsy
- **Common Wrong Answer:** (A)
- **Why It Feels Correct:** Constraint seems complete
- **Exact Point of Failure:** Negative values can make xy arbitrarily large or small

### 6️⃣ Generalization Map
1. Use minimum instead
2. Include integer constraints
3. Add three-variable problems
4. Use constrained optimization
5. Include inequality constraints

### 7️⃣ Neural Anchor
**"Sign Constraints Matter"**

---

## Success Verification

If a candidate masters this set:
- ✅ They recognize what's asked: unique value vs. yes/no
- ✅ They check if statements are independent or redundant
- ✅ They use algebraic identities for indirect calculation
- ✅ They understand "sufficient" means definite, not calculated
- ✅ They combine constraints correctly

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*

Would you like to initiate a **'Multi-Variable Stress Test'** combining Data Sufficiency with **Number System** for a Rank-1 simulation?
