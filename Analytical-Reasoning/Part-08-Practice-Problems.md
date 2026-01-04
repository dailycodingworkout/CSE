# Part 8: Practice Problems with Solutions

## The Singularity

**The Atomic Truth:** *Mastery comes through deliberate practice.*

---

## 8.1 How to Use This Section

### Practice Strategy

1. **Attempt** each problem without looking at solutions
2. **Time** yourself (aim for 2-3 minutes per problem)
3. **Check** your answer and methodology
4. **Analyze** mistakes to identify weak areas
5. **Revisit** incorrect problems after a gap

### Problem Categories

| Category | Problems | Focus Areas |
|----------|----------|-------------|
| Syllogisms | 1-10 | Deductive reasoning, Venn diagrams |
| Arrangements | 11-20 | Linear, circular, matrix |
| Critical Reasoning | 21-30 | Assumptions, strengthen, weaken |
| Pattern Recognition | 31-40 | Series, sequences |
| Data Interpretation | 41-50 | Tables, graphs, calculations |
| Mixed/Advanced | 51-60 | Combined concepts |

---

## Section A: Syllogisms (Problems 1-10)

### Problem 1 (Easy)
**Statements:**
- All roses are flowers
- Some flowers are red

**Conclusions:**
I. Some roses are red
II. Some red things are flowers

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
All roses ⊂ flowers
Some flowers ∩ red ≠ ∅

Conclusion I: Some roses are red
- The red flowers might not be roses (roses are a subset of flowers)
- NOT necessarily true ✗

Conclusion II: Some red things are flowers
- Direct conversion of "Some flowers are red"
- I-type statements can be converted ✓
```

**Answer: (B) Only II follows**

</details>

---

### Problem 2 (Easy)
**Statements:**
- No cat is a dog
- All dogs are animals

**Conclusions:**
I. No cat is an animal
II. Some animals are dogs

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
cats ∩ dogs = ∅
dogs ⊂ animals

Conclusion I: No cat is an animal
- Cats could still be animals (just not dogs)
- NOT necessarily true ✗

Conclusion II: Some animals are dogs
- Since all dogs are animals, and dogs exist, some animals are dogs ✓
```

**Answer: (B) Only II follows**

</details>

---

### Problem 3 (Medium)
**Statements:**
- All engineers are graduates
- All graduates are educated
- Some educated people are employed

**Conclusions:**
I. All engineers are educated
II. Some employed people are engineers

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
engineers ⊂ graduates ⊂ educated
educated ∩ employed ≠ ∅

Conclusion I: All engineers are educated
- engineers ⊂ graduates ⊂ educated
- Chain syllogism valid ✓

Conclusion II: Some employed people are engineers
- The employed educated might not be engineers
- NOT necessarily true ✗
```

**Answer: (A) Only I follows**

</details>

---

### Problem 4 (Medium)
**Statements:**
- Only managers can approve budgets
- Some team leads are managers

**Conclusions:**
I. All who approve budgets are managers
II. Some team leads can approve budgets

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
"Only managers can approve budgets"
= "All who approve budgets are managers"
= budget_approvers ⊂ managers

"Some team leads are managers"
= team_leads ∩ managers ≠ ∅

Conclusion I: All who approve budgets are managers
- Direct restatement of first statement ✓

Conclusion II: Some team leads can approve budgets
- Some team leads are managers, but not all managers approve budgets
- Being a manager doesn't mean they approve budgets (necessary, not sufficient)
- NOT necessarily true ✗
```

**Answer: (A) Only I follows**

</details>

---

### Problem 5 (Medium)
**Statements:**
- Some books are novels
- All novels are interesting
- No interesting thing is boring

**Conclusions:**
I. Some books are interesting
II. Some books are not boring

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
books ∩ novels ≠ ∅
novels ⊂ interesting
interesting ∩ boring = ∅

Conclusion I: Some books are interesting
- Some books are novels, and all novels are interesting
- Therefore, those books (that are novels) are interesting ✓

Conclusion II: Some books are not boring
- Some books are interesting (from I)
- Interesting things are not boring
- Therefore, those books are not boring ✓
```

**Answer: (C) Both follow**

</details>

---

### Problem 6 (Medium)
**Statements:**
- All squares are rectangles
- All rectangles are parallelograms
- Some parallelograms are rhombi

**Conclusions:**
I. All squares are parallelograms
II. Some rhombi are squares

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
squares ⊂ rectangles ⊂ parallelograms
parallelograms ∩ rhombi ≠ ∅

Conclusion I: All squares are parallelograms
- Chain: squares ⊂ rectangles ⊂ parallelograms ✓

Conclusion II: Some rhombi are squares
- The rhombi that are parallelograms might not be rectangles (or squares)
- NOT necessarily true ✗
```

**Answer: (A) Only I follows**

</details>

---

### Problem 7 (Hard)
**Statements:**
- All A are B
- No B is C
- Some C are D

**Which of the following is definitely FALSE?**
(A) Some A are not C
(B) No A is C
(C) Some D are C
(D) All A are C

<details>
<summary>Solution</summary>

**Analysis:**
```
A ⊂ B
B ∩ C = ∅
C ∩ D ≠ ∅

Since A ⊂ B and B ∩ C = ∅:
A ∩ C = ∅ (No A is C)

(A) Some A are not C - TRUE (in fact, ALL A are not C)
(B) No A is C - TRUE (derived above)
(C) Some D are C - TRUE (conversion of given statement)
(D) All A are C - FALSE (contradicts "No A is C")
```

**Answer: (D) All A are C** is definitely FALSE

</details>

---

### Problem 8 (Hard)
**Statements:**
- At least some X are Y
- All Y are Z
- Some Z are not W

**Conclusions:**
I. At least some X are Z
II. Some X are not W

**Options:**
(A) Only I follows
(B) Only II follows
(C) Both follow
(D) Neither follows

<details>
<summary>Solution</summary>

**Analysis:**
```
X ∩ Y ≠ ∅ (some X are Y)
Y ⊂ Z
Z \ W ≠ ∅ (some Z are not W)

Conclusion I: At least some X are Z
- Some X are Y, all Y are Z
- Those X (that are Y) are also Z ✓

Conclusion II: Some X are not W
- Some X are Z (from I)
- But we only know "some Z are not W"
- The X's that are Z might be the W ones
- NOT necessarily true ✗
```

**Answer: (A) Only I follows**

</details>

---

### Problem 9 (Hard)
**If "All cats are animals" is true, which of the following is definitely FALSE?**

(A) Some cats are not animals
(B) No cat is an animal
(C) Some animals are cats
(D) Both (A) and (B)

<details>
<summary>Solution</summary>

**Analysis:**
```
"All cats are animals" (A-type: All S are P)

Contradictory: "Some cats are not animals" (O-type)
- If A is TRUE, O is FALSE

Contrary: "No cat is an animal" (E-type)
- If A is TRUE, E is FALSE
- (But E and A can't both be true, both can be false)

(A) Some cats are not animals - FALSE (O contradicts A)
(B) No cat is an animal - FALSE (E is contrary to A)
(C) Some animals are cats - TRUE (valid conversion of A)
(D) Both (A) and (B) - Both are indeed FALSE
```

**Answer: (D) Both (A) and (B)**

</details>

---

### Problem 10 (Hard)
**Statements:**
- 60% of students study Physics
- 70% of students study Chemistry
- 40% of students study both Physics and Chemistry

**What percentage of students study neither?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Using inclusion-exclusion:
P(Physics ∪ Chemistry) = P(Physics) + P(Chemistry) - P(both)
                        = 60% + 70% - 40%
                        = 90%

P(Neither) = 100% - 90% = 10%
```

**Answer: 10%**

</details>

---

## Section B: Arrangements (Problems 11-20)

### Problem 11 (Easy)
**Five people A, B, C, D, E sit in a row. B is to the right of A. C is at one of the ends. How many possible arrangements are there?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Total positions: 5
C is at an end: 2 choices (position 1 or 5)

After fixing C, 4 people (A, B, D, E) in 4 positions.
B must be right of A.

Without constraint: 4! = 24 arrangements
With B right of A: 24/2 = 12 arrangements
(Half have A before B, half have B before A)

Total: 2 × 12 = 24
```

**Answer: 24 arrangements**

</details>

---

### Problem 12 (Easy)
**In a row of 5 students, if Ram is always in the middle, in how many ways can the students be arranged?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Ram is fixed in position 3 (middle of 5).
Remaining 4 students can be arranged in 4! ways.

4! = 24
```

**Answer: 24 ways**

</details>

---

### Problem 13 (Medium)
**Six people P, Q, R, S, T, U sit around a circular table. P and Q want to sit together. In how many ways can they be arranged?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Circular arrangement of n: (n-1)!
Treat P and Q as one unit: 5 units total
Circular arrangements: (5-1)! = 4! = 24

But P and Q can swap within their unit: 2 ways

Total: 24 × 2 = 48
```

**Answer: 48 ways**

</details>

---

### Problem 14 (Medium)
**In a linear arrangement:**
- A is not at either end
- B is two places to the right of A
- C is adjacent to D

**If there are 5 people A, B, C, D, E, how many arrangements are possible?**

<details>
<summary>Solution</summary>

**Analysis:**
```
A not at ends: A ∈ {2, 3, 4}
B is 2 places right of A: 
  If A=2, B=4
  If A=3, B=5
  If A=4, B=6 (invalid, only 5 positions)

Case 1: A=2, B=4
Positions: _, A, _, B, _
           1  2  3  4  5
C, D, E in positions 1, 3, 5
C-D adjacent: Must be in (1,3) or (3,5)
  C-D in (1,3): E in 5, C-D can swap: 2 ways
  C-D in (3,5): E in 1, C-D can swap: 2 ways
Total for Case 1: 4

Case 2: A=3, B=5
Positions: _, _, A, _, B
           1  2  3  4  5
C, D, E in positions 1, 2, 4
C-D adjacent: Must be in (1,2) or (2,4)
  C-D in (1,2): E in 4, C-D can swap: 2 ways
  C-D in (2,4): E in 1, C-D can swap: 2 ways
Total for Case 2: 4

Total: 4 + 4 = 8
```

**Answer: 8 arrangements**

</details>

---

### Problem 15 (Medium)
**Eight people sit around a circular table. Three particular people must NOT sit together. In how many ways can they be arranged?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Total circular arrangements: (8-1)! = 7! = 5040

Arrangements where 3 particular people sit together:
Treat 3 as one unit: 6 units in circle
Circular: (6-1)! = 5! = 120
The 3 can arrange among themselves: 3! = 6
Together: 120 × 6 = 720

Arrangements where they DON'T sit together:
5040 - 720 = 4320
```

**Answer: 4320 ways**

</details>

---

### Problem 16 (Medium)
**In a 3×3 grid, 9 people are seated. Person A is in the center. Person B is not in any corner. How many ways can the remaining 7 people be arranged?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Grid positions:
1 2 3
4 5 6
7 8 9

A is in center (position 5).
Corners: 1, 3, 7, 9
Edges: 2, 4, 6, 8
Center: 5 (taken by A)

B is not in corner, so B ∈ {2, 4, 6, 8}: 4 choices

After A (center) and B (edge): 7 people in 7 positions
7! = 5040

Total: 4 × 5040 = 20160
```

**Answer: 20160 ways**

</details>

---

### Problem 17 (Hard)
**Five friends A, B, C, D, E have ranks 1-5 (1 = highest):**
- A has higher rank than B
- C has rank 3
- D has lower rank than B
- E is not ranked 1 or 5

**Who has rank 1?**

<details>
<summary>Solution</summary>

**Analysis:**
```
C = 3 (given)
E ∈ {2, 4} (not 1 or 5)
A > B > D (A better than B better than D)

If E = 2:
A, B, D need ranks from {1, 4, 5}
A > B > D means A=1, B=4, D=5 ✓

If E = 4:
A, B, D need ranks from {1, 2, 5}
A > B > D: A=1, B=2, D=5 ✓

Both cases: A = 1
```

**Answer: A has rank 1**

</details>

---

### Problem 18 (Hard)
**Six people sit in two rows of three (facing each other):**
```
Row 1: _ _ _
Row 2: _ _ _
```
**Conditions:**
- A sits in Row 1
- B sits directly opposite to A
- C does not sit at either end of a row
- D sits next to A

**If E and F take remaining positions, in how many ways can they be arranged?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Row 1 positions: L1, M1, R1
Row 2 positions: L2, M2, R2 (opposite L1, M1, R1)

A in Row 1, B opposite A (Row 2, same column)
D next to A (Row 1)
C not at end: C ∈ {M1, M2}

Case 1: A in L1
  B in L2
  D next to A: D in M1
  C not at end: C in M2 (M1 taken by D)
  Remaining: R1, R2 for E, F: 2! = 2 ways

Case 2: A in M1
  B in M2
  D next to A: D in L1 or R1 (2 choices)
  C not at end: C can't be M1 or M2 (taken), so C at an end? Contradiction!
  Actually, C ∈ {M1, M2} but both taken. Invalid.

Case 3: A in R1
  B in R2
  D next to A: D in M1
  C not at end: C in M2
  Remaining: L1, L2 for E, F: 2! = 2 ways

Total: 2 + 2 = 4
```

**Answer: 4 ways**

</details>

---

### Problem 19 (Hard)
**Seven items are to be arranged in a row. Items X and Y must have exactly two items between them. In how many ways can this be done?**

<details>
<summary>Solution</summary>

**Analysis:**
```
X and Y have exactly 2 items between them.
X _ _ Y or Y _ _ X

Possible position pairs for (X,Y):
(1,4), (2,5), (3,6), (4,7): 4 pairs
Each can be (X,Y) or (Y,X): 4 × 2 = 8

For each fixed (X,Y) placement:
Remaining 5 items in 5 positions: 5! = 120

Total: 8 × 120 = 960
```

**Answer: 960 ways**

</details>

---

### Problem 20 (Hard)
**In a circular arrangement of 8 people, the host sits in a fixed position. The remaining 7 guests are to be seated such that two specific guests never sit adjacent to the host. In how many ways can this be done?**

<details>
<summary>Solution</summary>

**Analysis:**
```
Host is fixed.
7 guests to arrange.
2 specific guests (say G1, G2) cannot be adjacent to host.
Host has 2 neighbors (left and right).

Total arrangements without restriction: 7! = 5040

Subtract: At least one of G1, G2 adjacent to host.

Using inclusion-exclusion:
A = G1 adjacent to host
B = G2 adjacent to host

|A| = 2 × 6! = 1440 (G1 in left or right, others arrange)
|B| = 2 × 6! = 1440
|A ∩ B| = 2! × 5! = 240 (G1, G2 in both adjacent spots, others arrange)

|A ∪ B| = 1440 + 1440 - 240 = 2640

Valid = 5040 - 2640 = 2400
```

**Answer: 2400 ways**

</details>

---

## Section C: Critical Reasoning (Problems 21-30)

### Problem 21 (Easy)
**Statement:** "Employees who take regular breaks are more productive. Therefore, we should mandate hourly breaks for all staff."

**Which assumption is necessary for this argument?**

(A) All employees want to take breaks
(B) Productivity increase from breaks outweighs time lost
(C) Breaks should be exactly one hour long
(D) Other companies have similar policies

<details>
<summary>Solution</summary>

**Analysis:**
The argument concludes mandating breaks will be beneficial.
For this to hold, the benefit (productivity) must exceed the cost (break time).

(A) Employee preference is irrelevant to productivity
(B) This is the necessary assumption for the policy to make sense ✓
(C) "Hourly breaks" means breaks every hour, not one-hour breaks
(D) Irrelevant to this company's decision

**Answer: (B)**

</details>

---

### Problem 22 (Easy)
**Statement:** "Sales of winter jackets increased after the temperature dropped. The cold weather must have caused the sales increase."

**Which weakens this argument?**

(A) The jackets were also on sale at a 50% discount
(B) Cold weather makes people stay indoors
(C) Winter jackets are essential in cold weather
(D) The store had low inventory before the temperature drop

<details>
<summary>Solution</summary>

**Analysis:**
The argument claims: Cold weather → Sales increase.
To weaken: Show alternative cause.

(A) Alternative cause (discount) explains the increase ✓
(B) Would actually strengthen (people buy jackets)
(C) Strengthens the causal link
(D) Low inventory would decrease sales, not increase

**Answer: (A)**

</details>

---

### Problem 23 (Medium)
**Statement:** "University X produces the most successful entrepreneurs. A survey shows that 40% of billionaire entrepreneurs attended University X. Therefore, attending University X increases your chances of becoming a billionaire entrepreneur."

**What is the flaw in this reasoning?**

(A) The survey sample is too small
(B) It doesn't account for the total number of University X graduates
(C) Not all billionaires are entrepreneurs
(D) University X may have changed its curriculum

<details>
<summary>Solution</summary>

**Analysis:**
The argument commits the base rate fallacy.
40% of billionaires went to X, but if 80% of all students go to X, X actually underperforms.
We need to compare success rate, not absolute numbers.

(B) correctly identifies the missing base rate ✓

**Answer: (B)**

</details>

---

### Problem 24 (Medium)
**Statement:** "Crime rates have decreased every year since the new police chief was appointed. Clearly, the new chief's strategies are effective."

**Which strengthens this argument?**

(A) The previous chief also saw declining crime rates
(B) The new chief implemented data-driven policing methods
(C) Crime rates decreased in neighboring cities too
(D) There were no other significant changes in the city

<details>
<summary>Solution</summary>

**Analysis:**
To strengthen: Eliminate alternative explanations or add supporting evidence.

(A) Weakens (decline might be a trend, not due to new chief)
(B) Adds possible mechanism, but doesn't eliminate alternatives
(C) Weakens (suggests external factors)
(D) Eliminates confounding variables ✓

**Answer: (D)**

</details>

---

### Problem 25 (Medium)
**Passage:** "A study found that children who play video games for more than 4 hours daily have lower grades. Researchers concluded that video games impair academic performance."

**Which of the following, if true, would most seriously undermine the researchers' conclusion?**

(A) Children with lower grades tend to escape into video games
(B) Video games improve hand-eye coordination
(C) Some high-achieving students also play video games
(D) The study was conducted over several years

<details>
<summary>Solution</summary>

**Analysis:**
Researchers assume: Video games → Lower grades (causation).
To undermine: Show reverse causation or third variable.

(A) Reverse causation: Lower grades → Video games ✓
(B) Irrelevant to academic performance
(C) Exception doesn't undermine the general trend
(D) Actually strengthens the study's reliability

**Answer: (A)**

</details>

---

### Problem 26 (Medium)
**Statements:**
- If the economy grows, employment increases.
- If employment increases, consumer spending rises.
- Consumer spending did not rise.

**What can be concluded?**

(A) The economy did not grow
(B) Employment did not increase
(C) Both (A) and (B)
(D) Neither (A) nor (B)

<details>
<summary>Solution</summary>

**Analysis:**
```
Economy grows → Employment increases → Consumer spending rises

Contrapositive chain:
¬Consumer spending → ¬Employment → ¬Economy grows

Given: ¬Consumer spending
Conclude: ¬Employment (by contrapositive)
Conclude: ¬Economy grows (by contrapositive)

Both (A) and (B) follow.
```

**Answer: (C) Both (A) and (B)**

</details>

---

### Problem 27 (Hard)
**Statement:** "None of the candidates who scored below 60 in the written test were selected for the interview. Some candidates who scored above 80 were not selected for the interview. All candidates selected for interview were graduates."

**Which must be true?**

(A) All graduates who scored above 60 were selected
(B) Some graduates scored above 80
(C) All candidates selected for interview scored at least 60
(D) No candidate scoring above 80 was a graduate

<details>
<summary>Solution</summary>

**Analysis:**
```
Below 60 → Not selected for interview (contrapositive: selected → ≥60)
Some above 80 → not selected (at least one above 80 not selected)
Selected → Graduate

(A) Not necessarily; could be selective within ≥60
(B) We know some were selected, and selected are graduates; those selected scored ≥60, not necessarily >80
(C) Selected → ≥60 (from contrapositive) ✓
(D) Some above 80 could be graduates and not selected
```

**Answer: (C)**

</details>

---

### Problem 28 (Hard)
**A city plans to reduce traffic by implementing congestion pricing (charging vehicles to enter busy areas during peak hours). Critics argue this will only shift traffic to other areas.**

**Which, if true, would best support implementing the plan despite critics' concerns?**

(A) Other cities have successfully implemented congestion pricing
(B) The revenue from pricing will fund public transportation
(C) Studies show overall traffic decreases, not just shifts location
(D) Most drivers will simply pay the fee

<details>
<summary>Solution</summary>

**Analysis:**
Critics say: Traffic will shift (not reduce).
To address: Show traffic actually reduces overall.

(A) Precedent helps but doesn't address the specific concern
(B) Addresses outcome but not the traffic shifting concern
(C) Directly refutes the shifting argument ✓
(D) Would mean no reduction (people pay and drive)

**Answer: (C)**

</details>

---

### Problem 29 (Hard)
**Which of the following contains a logical fallacy?**

(A) All mammals are warm-blooded. Whales are mammals. Therefore, whales are warm-blooded.
(B) Every time I wash my car, it rains. Therefore, washing my car causes rain.
(C) 90% of doctors recommend this medicine. You should take it.
(D) Both (B) and (C)

<details>
<summary>Solution</summary>

**Analysis:**
(A) Valid syllogism (AAA in Figure 1: Barbara) ✓ No fallacy
(B) Post hoc fallacy (correlation ≠ causation) ✗ Fallacy!
(C) Appeal to authority / popularity ✗ Fallacy!

**Answer: (D) Both (B) and (C)**

</details>

---

### Problem 30 (Hard)
**A company's profits increased by 25% while employee count decreased by 10%.**

**Which conclusion is best supported?**

(A) Firing employees increased profits
(B) Profit per employee increased
(C) Revenue increased
(D) Remaining employees worked harder

<details>
<summary>Solution</summary>

**Analysis:**
Given: Profit ↑25%, Employees ↓10%

(A) Assumes causation from correlation - not supported
(B) Profit per employee = Profit/Employees
    Original: P/E
    New: 1.25P/0.9E = 1.389P/E (38.9% increase) ✓ Mathematically true
(C) Revenue might have increased or costs decreased - not directly supported
(D) Assumes work hours/efficiency changed - not supported

**Answer: (B)** (This is a mathematical certainty, not an inference)

</details>

---

## Section D: Pattern Recognition (Problems 31-40)

### Problem 31 (Easy)
**Series:** 2, 6, 12, 20, 30, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Differences: 4, 6, 8, 10, ?
Second differences: 2, 2, 2
Next first difference: 12
Answer: 30 + 12 = 42
```

**Answer: 42**

</details>

---

### Problem 32 (Easy)
**Series:** A, C, F, J, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Positions: 1, 3, 6, 10, ?
Differences: 2, 3, 4, 5
Pattern: Triangular numbers
Next position: 10 + 5 = 15
15th letter: O
```

**Answer: O**

</details>

---

### Problem 33 (Medium)
**Series:** 1, 4, 9, 16, 25, 36, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Pattern: 1², 2², 3², 4², 5², 6², 7²
Next: 49
```

**Answer: 49**

</details>

---

### Problem 34 (Medium)
**Series:** 2, 3, 5, 7, 11, 13, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Pattern: Prime numbers
Next prime after 13: 17
```

**Answer: 17**

</details>

---

### Problem 35 (Medium)
**Series:** 1, 1, 2, 3, 5, 8, 13, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Pattern: Fibonacci (each term = sum of two previous)
8 + 13 = 21
```

**Answer: 21**

</details>

---

### Problem 36 (Medium)
**Matrix:**
```
┌───┬───┬───┐
│ 2 │ 3 │ 4 │
├───┼───┼───┤
│ 5 │ 6 │ 7 │
├───┼───┼───┤
│ 8 │ 9 │ ? │
└───┴───┴───┘
```

<details>
<summary>Solution</summary>

**Analysis:**
```
Reading order: 2, 3, 4, 5, 6, 7, 8, 9, 10
Pattern: Consecutive integers
Answer: 10
```

**Answer: 10**

</details>

---

### Problem 37 (Hard)
**Series:** 1, 2, 2, 4, 8, 32, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Pattern: Each term = product of previous two
1 × 2 = 2
2 × 2 = 4
2 × 4 = 8
4 × 8 = 32
8 × 32 = 256
```

**Answer: 256**

</details>

---

### Problem 38 (Hard)
**Find the odd one out:** 125, 343, 512, 729, 1000

<details>
<summary>Solution</summary>

**Analysis:**
```
125 = 5³
343 = 7³
512 = 8³
729 = 9³
1000 = 10³

All are cubes. But:
5, 7, 8, 9, 10
5, 7 are prime; 8, 9, 10 are not.
Or: 5, 7, 9 are odd; 8, 10 are even.

Actually, check: 5, 7 are prime, 8 = 2³, 9 = 3², 10 = 2×5

512 = 8³ = (2³)³ = 2⁹ (only power of 2)

Answer: 512 (it's a power of 2, others are not)
```

**Answer: 512**

</details>

---

### Problem 39 (Hard)
**Series:** 2, 12, 36, 80, 150, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Pattern: n(n+1)²
n=1: 1×4 = 4? No.

Let me try: n²(n+1)
n=1: 1×2 = 2 ✓
n=2: 4×3 = 12 ✓
n=3: 9×4 = 36 ✓
n=4: 16×5 = 80 ✓
n=5: 25×6 = 150 ✓
n=6: 36×7 = 252
```

**Answer: 252**

</details>

---

### Problem 40 (Hard)
**Alphanumeric:** A1, B4, C9, D16, ?

<details>
<summary>Solution</summary>

**Analysis:**
```
Letter pattern: A, B, C, D, E (consecutive)
Number pattern: 1, 4, 9, 16, 25 (perfect squares: 1², 2², 3², 4², 5²)
```

**Answer: E25**

</details>

---

## Section E: Data Interpretation (Problems 41-50)

### Problem 41 (Easy)
**Table: Monthly Sales (in lakhs)**

| Month | Product A | Product B |
|-------|-----------|-----------|
| Jan | 20 | 15 |
| Feb | 25 | 20 |
| Mar | 30 | 18 |
| Apr | 22 | 25 |

**What is the total sales of Product B for all months?**

<details>
<summary>Solution</summary>

15 + 20 + 18 + 25 = 78 lakhs

**Answer: 78 lakhs**

</details>

---

### Problem 42 (Easy)
**Using the table from Problem 41, what is the percentage increase in Product A sales from Jan to Mar?**

<details>
<summary>Solution</summary>

Increase = ((30 - 20) / 20) × 100 = 50%

**Answer: 50%**

</details>

---

### Problem 43 (Medium)
**A pie chart shows department-wise distribution of 240 employees:**
- HR: 60°
- Finance: 90°
- IT: 120°
- Operations: 90°

**How many employees are in IT?**

<details>
<summary>Solution</summary>

IT angle = 120°
Percentage = (120/360) × 100 = 33.33%
Employees = 0.3333 × 240 = 80

**Answer: 80 employees**

</details>

---

### Problem 44 (Medium)
**Table: Exam Scores**

| Student | Math | Science | English |
|---------|------|---------|---------|
| A | 85 | 90 | 78 |
| B | 72 | 88 | 92 |
| C | 95 | 75 | 85 |
| D | 68 | 82 | 88 |

**Who has the highest average score?**

<details>
<summary>Solution</summary>

```
A: (85+90+78)/3 = 253/3 = 84.33
B: (72+88+92)/3 = 252/3 = 84
C: (95+75+85)/3 = 255/3 = 85
D: (68+82+88)/3 = 238/3 = 79.33
```

**Answer: C with average 85**

</details>

---

### Problem 45 (Medium)
**Compound Growth: A company's revenue was 100 crores in 2020. It grew at 10% in 2021 and 20% in 2022. What was the revenue in 2022?**

<details>
<summary>Solution</summary>

2020: 100 crores
2021: 100 × 1.10 = 110 crores
2022: 110 × 1.20 = 132 crores

**Answer: 132 crores**

</details>

---

### Problem 46 (Medium)
**A bar graph shows production (in 1000 units):**
- Factory A: 40
- Factory B: 55
- Factory C: 35
- Factory D: 50

**What percentage of total production is from Factory B?**

<details>
<summary>Solution</summary>

Total = 40 + 55 + 35 + 50 = 180 (in 1000 units)
Factory B percentage = (55/180) × 100 = 30.56%

**Answer: 30.56% (or approximately 31%)**

</details>

---

### Problem 47 (Hard)
**Table: Profit Margins**

| Year | Revenue (Cr) | Profit Margin (%) |
|------|--------------|-------------------|
| 2019 | 500 | 8% |
| 2020 | 450 | 12% |
| 2021 | 550 | 10% |
| 2022 | 600 | 15% |

**In which year was the absolute profit maximum?**

<details>
<summary>Solution</summary>

```
2019: 500 × 0.08 = 40 Cr
2020: 450 × 0.12 = 54 Cr
2021: 550 × 0.10 = 55 Cr
2022: 600 × 0.15 = 90 Cr
```

**Answer: 2022 with 90 Cr profit**

</details>

---

### Problem 48 (Hard)
**Line Graph Data (Sales in millions):**

| Quarter | 2021 | 2022 |
|---------|------|------|
| Q1 | 100 | 120 |
| Q2 | 110 | 140 |
| Q3 | 130 | 150 |
| Q4 | 150 | 180 |

**What is the percentage increase in total annual sales from 2021 to 2022?**

<details>
<summary>Solution</summary>

```
2021 Total: 100 + 110 + 130 + 150 = 490 million
2022 Total: 120 + 140 + 150 + 180 = 590 million
Increase: ((590 - 490) / 490) × 100 = 20.41%
```

**Answer: 20.41%**

</details>

---

### Problem 49 (Hard)
**Mixed Data:**
- Pie Chart shows: Product A (25%), Product B (35%), Product C (40%)
- Total Revenue: 800 lakhs
- Product A's profit margin: 20%
- Product B's profit margin: 15%

**What is the combined profit from Products A and B?**

<details>
<summary>Solution</summary>

```
Product A revenue: 800 × 0.25 = 200 lakhs
Product A profit: 200 × 0.20 = 40 lakhs

Product B revenue: 800 × 0.35 = 280 lakhs
Product B profit: 280 × 0.15 = 42 lakhs

Combined profit: 40 + 42 = 82 lakhs
```

**Answer: 82 lakhs**

</details>

---

### Problem 50 (Hard)
**The ratio of boys to girls in a school is 3:2. If the number of boys increases by 20% and girls by 10%, what is the new ratio?**

<details>
<summary>Solution</summary>

```
Original: Boys = 3x, Girls = 2x
New Boys: 3x × 1.20 = 3.6x
New Girls: 2x × 1.10 = 2.2x
New Ratio: 3.6x : 2.2x = 36 : 22 = 18 : 11
```

**Answer: 18:11**

</details>

---

## Section F: Mixed/Advanced (Problems 51-60)

### Problem 51
**Eight people A-H sit in a circle. Given:**
- A is opposite to E
- B is to the immediate right of A
- C is to the immediate right of E
- D is not adjacent to A or E

**Who is opposite to B?**

<details>
<summary>Solution</summary>

```
8-person circle. Opposite = 4 positions apart.
Fix A at position 1. E at position 5.
B is immediately right of A: B at position 2.
C is immediately right of E: C at position 6.
D not adjacent to A (pos 8, 2) or E (pos 4, 6).
D ∈ {3, 7}

Opposite to B (position 2) = position 6 = C
```

**Answer: C**

</details>

---

### Problem 52
**Statement:** "Some doctors are teachers. All teachers are researchers."

**Conclusion:** "Some doctors are researchers."

**Is the conclusion valid?**

<details>
<summary>Solution</summary>

```
doctors ∩ teachers ≠ ∅
teachers ⊂ researchers

The doctors who are teachers are also researchers (since all teachers are researchers).
Therefore, some doctors are researchers. ✓
```

**Answer: Yes, the conclusion is valid**

</details>

---

### Problem 53
**Series:** 3, 8, 15, 24, 35, ?

<details>
<summary>Solution</summary>

```
Differences: 5, 7, 9, 11, ?
Second differences: 2, 2, 2
Next first difference: 13
Answer: 35 + 13 = 48
```

**Answer: 48**

</details>

---

### Problem 54
**A train travels from A to B at 60 km/h and returns at 40 km/h. What is the average speed for the round trip?**

<details>
<summary>Solution</summary>

```
Average speed = 2 × v₁ × v₂ / (v₁ + v₂)
              = 2 × 60 × 40 / (60 + 40)
              = 4800 / 100
              = 48 km/h
```

**Answer: 48 km/h**

</details>

---

### Problem 55
**In a class of 60 students:**
- 35 study Mathematics
- 30 study Physics
- 10 study both

**How many study neither?**

<details>
<summary>Solution</summary>

```
|M ∪ P| = |M| + |P| - |M ∩ P|
        = 35 + 30 - 10 = 55

Neither = 60 - 55 = 5
```

**Answer: 5 students**

</details>

---

### Problem 56
**If COMPUTER = 111 (C+O+M+P+U+T+E+R = 3+15+13+16+21+20+5+18 = 111), find GATE = ?**

<details>
<summary>Solution</summary>

```
G = 7
A = 1
T = 20
E = 5
Sum = 7 + 1 + 20 + 5 = 33
```

**Answer: 33**

</details>

---

### Problem 57
**A shop offers 20% discount on marked price. After discount, 10% GST is added. If final price is 792, what was the marked price?**

<details>
<summary>Solution</summary>

```
Let marked price = M
After 20% discount: M × 0.80
After 10% GST: M × 0.80 × 1.10 = M × 0.88 = 792
M = 792 / 0.88 = 900
```

**Answer: ₹900**

</details>

---

### Problem 58
**In how many ways can letters of MISSISSIPPI be arranged?**

<details>
<summary>Solution</summary>

```
M = 1, I = 4, S = 4, P = 2
Total letters = 11
Arrangements = 11! / (1! × 4! × 4! × 2!)
             = 39916800 / (1 × 24 × 24 × 2)
             = 39916800 / 1152
             = 34650
```

**Answer: 34650**

</details>

---

### Problem 59
**A statement: "If it is Monday, then the museum is closed."**

**Which is logically equivalent?**
(A) If the museum is open, it is not Monday
(B) If it is not Monday, the museum is open
(C) The museum is closed only on Monday
(D) If the museum is closed, it is Monday

<details>
<summary>Solution</summary>

```
Original: Monday → Museum Closed
Contrapositive: Museum Open → Not Monday

(A) Museum Open → Not Monday ✓ (Contrapositive)
(B) Not Monday → Museum Open (Inverse - not equivalent)
(C) Claims Monday is the only closed day (not stated)
(D) Museum Closed → Monday (Converse - not equivalent)
```

**Answer: (A)**

</details>

---

### Problem 60
**Five boxes are labeled 1-5. Each contains one ball (red, blue, green, yellow, white). Given:**
- Red ball is in an odd-numbered box
- Blue ball is in box 2 or 3
- Green ball is in a box next to the red ball
- Yellow ball is in box 5
- White ball is not adjacent to yellow ball

**In which box is the red ball?**

<details>
<summary>Solution</summary>

```
Yellow in box 5.
Red in odd box: 1, 3, or 5. Since 5 has yellow, red ∈ {1, 3}.
Green is next to red.
  If red = 1, green = 2
  If red = 3, green = 2 or 4
Blue in box 2 or 3.

Case 1: Red = 1
  Green = 2. But blue must be in 2 or 3.
  If green = 2, blue = 3.
  Remaining: white in box 4.
  Check: White (box 4) adjacent to yellow (box 5)? Yes! Violation. ✗

Case 2: Red = 3
  Green = 2 or 4. Blue in 2 or 3.
  If green = 2, blue = 3. But red = 3. Conflict! ✗
  If green = 4, blue = 2 or 3.
    Blue can be 2 (since red = 3).
    Remaining: white in box 1.
    Check: White (box 1) adjacent to yellow (box 5)? No. ✓
    
Arrangement: White(1), Blue(2), Red(3), Green(4), Yellow(5)
```

**Answer: Box 3**

</details>

---

## Key Takeaways

### Performance Analysis

After completing all problems, calculate:
- **Total Correct:** ___/60
- **Syllogisms:** ___/10
- **Arrangements:** ___/10
- **Critical Reasoning:** ___/10
- **Pattern Recognition:** ___/10
- **Data Interpretation:** ___/10
- **Mixed/Advanced:** ___/10

### Weak Area Identification

If score < 6 in any section, revisit the corresponding part:
- Syllogisms → Part 2
- Arrangements → Part 3
- Critical Reasoning → Part 5
- Patterns → Part 6
- Data → Part 4

### Time Analysis

Target times:
- Easy problems: < 1 minute
- Medium problems: 1-2 minutes
- Hard problems: 2-3 minutes

---

## Navigation

[◀ Previous: Advanced Problem-Solving](Part-07-Advanced-Problem-Solving.md) | [Contents](README.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]. Would you like to initiate a **'Multi-Variable Stress Test'** combining this with related topics for a Rank-1 simulation?*
