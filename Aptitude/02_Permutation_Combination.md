# Permutation and Combination (PNC) | GATE ESE PSU - Maximum Difficulty Question Bank

## The Atomic Truth
> **"Count arrangements (order matters) vs selections (order doesn't)."**

---

## Question 1 | Circular Arrangement Trap (NAT)

**Problem:** In how many ways can 8 people be seated around a circular table such that 2 specific people (A and B) are never adjacent?

**Trap Alert:** Students forget to subtract adjacent cases from total or wrongly apply linear formula.

### Solution via Technique:
**Step 1:** Total circular arrangements = $(8-1)! = 7! = 5040$

**Step 2:** A and B together (treat as single unit):
- Units = 7, circular arrangements = $(7-1)! = 6! = 720$
- A and B can swap: $720 \times 2 = 1440$

**Step 3:** A and B NOT adjacent = Total - Adjacent
$$= 5040 - 1440 = 3600$$

**Answer: 3600**

**5-Second Snap-Check:** Non-adjacent should be roughly $\frac{5}{7}$ of total (since each person has 2 neighbors out of 7). $5040 \times \frac{5}{7} = 3600$ ✓

---

## Question 2 | Derangement (NAT)

**Problem:** 5 letters are placed in 5 addressed envelopes. Find the number of ways such that exactly 2 letters go to correct envelopes.

**Trap Alert:** This is NOT derangement directly—it's partial derangement!

### Solution via Technique:
**Step 1:** Choose which 2 letters are correct: $\binom{5}{2} = 10$

**Step 2:** Remaining 3 letters must ALL go to wrong envelopes (derangement of 3)

**Derangement formula:** $D_n = n! \left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + ... + \frac{(-1)^n}{n!}\right)$

$$D_3 = 3! \left(1 - 1 + \frac{1}{2} - \frac{1}{6}\right) = 6 \times \frac{1}{3} = 2$$

**Step 3:** Total = $10 \times 2 = 20$

**Answer: 20**

**Alternative Formula:** $D_n = (n-1)(D_{n-1} + D_{n-2})$ with $D_1 = 0, D_2 = 1$
- $D_3 = 2(D_2 + D_1) = 2(1+0) = 2$ ✓

---

## Question 3 | Identical Objects Distribution (NAT)

**Problem:** Find the number of ways to distribute 10 identical balls into 4 distinct boxes such that no box is empty.

**Trap Alert:** Many confuse "at least one" constraint with standard stars and bars.

### Solution via Technique:
**Stars and Bars with Constraint:**
Each box must have ≥ 1 ball. Put 1 ball in each box first: 4 balls used, 6 remaining.

Now distribute 6 identical balls into 4 distinct boxes (can be empty):
$$\binom{6 + 4 - 1}{4 - 1} = \binom{9}{3} = 84$$

**Answer: 84**

**The Golden Formula:** Distributing $n$ identical objects into $r$ distinct boxes with each box having at least 1:
$$\binom{n-1}{r-1}$$

Verification: $\binom{10-1}{4-1} = \binom{9}{3} = 84$ ✓

---

## Question 4 | Word Arrangements with Restrictions (MSQ)

**Problem:** How many arrangements of the word "COMMITTEE" have all vowels together?

A) 30240  
B) 15120  
C) 10080  
D) None of these

**Trap Alert:** COMMITTEE has repeated letters! Also, which letters are vowels matters.

### Solution via Technique:
**COMMITTEE:** C-O-M-M-I-T-T-E-E

**Vowels:** O, I, E, E (4 vowels, E repeats)
**Consonants:** C, M, M, T, T (5 consonants, M and T repeat)

**Step 1:** Treat vowels as single unit: [OIEE]
Total units: [OIEE], C, M, M, T, T = 6 units

**Step 2:** Arrange 6 units with M×2, T×2:
$$\frac{6!}{2! \times 2!} = \frac{720}{4} = 180$$

**Step 3:** Arrange vowels within the unit (E repeats):
$$\frac{4!}{2!} = \frac{24}{2} = 12$$

**Step 4:** Total = $180 \times 12 = 2160$

**Answer: D) None of these**

---

## Question 5 | Selection with Constraints (NAT)

**Problem:** From 5 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?

### Solution via Technique:
**Step 1:** Select consonants: $\binom{5}{3} = 10$

**Step 2:** Select vowels: $\binom{4}{2} = 6$

**Step 3:** Arrange 5 letters: $5! = 120$

**Total:** $10 \times 6 \times 120 = 7200$

**Answer: 7200**

---

## Question 6 | Multinomial Coefficient (NAT)

**Problem:** In how many ways can 12 different books be divided equally among 3 students?

**Trap Alert:** Order of students matters vs doesn't matter—critical distinction!

### Solution via Technique:
**Since students are distinguishable (different people):**

**Step 1:** Choose 4 books for Student 1: $\binom{12}{4}$

**Step 2:** Choose 4 books for Student 2: $\binom{8}{4}$

**Step 3:** Remaining 4 go to Student 3: $\binom{4}{4} = 1$

$$\text{Total} = \binom{12}{4} \times \binom{8}{4} \times \binom{4}{4} = 495 \times 70 \times 1 = 34650$$

**Alternatively:** $\frac{12!}{(4!)^3} = \frac{479001600}{13824} = 34650$

**Answer: 34650**

**If groups were identical (not students):** Divide by $3! = 6$ → $34650/6 = 5775$

---

## Question 7 | Ranking Words (NAT)

**Problem:** Find the rank of the word "MOTHER" in dictionary order among all arrangements of its letters.

### Solution via Technique:
**MOTHER:** M, O, T, H, E, R (all distinct)
**Alphabetical order:** E, H, M, O, R, T

**Words starting with E:** $5! = 120$
**Words starting with H:** $5! = 120$
**Total so far:** 240

**Words starting with M (our letter):**
- ME...: $4! = 24$
- MH...: $4! = 24$
- MO (our next letters):
  - MOE...: $3! = 6$
  - MOH...: $3! = 6$
  - MOR...: $3! = 6$
  - MOT (our letters):
    - MOTE...: $2! = 2$
    - MOTH (our letters):
      - MOTHE...: Next is E, then R
      - MOTHER: Rank = 1

**Calculation:** Words before MOTHER in dictionary order:
1. Starting with E: $5! = 120$
2. Starting with H: $5! = 120$
3. Starting with ME: $4! = 24$
4. Starting with MH: $4! = 24$
5. Starting with MOE: $3! = 6$
6. Starting with MOH: $3! = 6$
7. Starting with MOR: $3! = 6$
8. Starting with MOTE: $2! = 2$
9. Starting with MOTHE: $1! = 1$ (only MOTHER comes after MOTHE_)

**Rank = $120 + 120 + 24 + 24 + 6 + 6 + 6 + 2 + 1 + 1 = 310$**

**Answer: 310**

---

## Question 8 | Partitions (NAT)

**Problem:** In how many ways can 7 be written as an ordered sum of positive integers?

**Trap Alert:** "Ordered" means $1+6 \neq 6+1$. This is composition, not partition!

### Solution via Technique:
**Compositions of n:** There are $2^{n-1}$ compositions.

For $n = 7$: $2^{7-1} = 2^6 = 64$

**Why?** Think of 7 as 7 ones: $1|1|1|1|1|1|1$

Between each pair of 1's, you can place a bar (separate) or not (combine).
6 gaps, 2 choices each = $2^6 = 64$

**Answer: 64**

---

## Question 9 | Committee with Restrictions (NAT)

**Problem:** A committee of 5 is to be formed from 6 men and 4 women. If the committee must have at least 2 women, how many ways can this be done?

### Solution via Technique:
**Method 1: Direct Counting**
- 2W + 3M: $\binom{4}{2} \times \binom{6}{3} = 6 \times 20 = 120$
- 3W + 2M: $\binom{4}{3} \times \binom{6}{2} = 4 \times 15 = 60$
- 4W + 1M: $\binom{4}{4} \times \binom{6}{1} = 1 \times 6 = 6$

**Total = $120 + 60 + 6 = 186$**

**Method 2: Complementary Counting**
Total committees: $\binom{10}{5} = 252$
0W: $\binom{4}{0} \times \binom{6}{5} = 1 \times 6 = 6$
1W: $\binom{4}{1} \times \binom{6}{4} = 4 \times 15 = 60$
At least 2W = $252 - 6 - 60 = 186$ ✓

**Answer: 186**

---

## Question 10 | Chessboard Counting (NAT)

**Problem:** In how many ways can 2 identical rooks be placed on an 8×8 chessboard such that they don't attack each other?

**Trap Alert:** Rooks attack along rows and columns. Also, rooks are IDENTICAL!

### Solution via Technique:
**Rooks don't attack if they're on different rows AND different columns.**

**Step 1:** Choose 2 rows from 8: $\binom{8}{2} = 28$

**Step 2:** Choose 2 columns from 8: $\binom{8}{2} = 28$

**Step 3:** Place rooks (since identical, only 1 way per row-column selection)
Each rook goes to one intersection. But wait—2 rows × 2 columns gives 4 cells, and we place 2 rooks.

**For 2 identical non-attacking rooks:**

**Method:** Choose 2 rows and 2 columns, then place rooks on the diagonal.

- Choose 2 rows: $\binom{8}{2} = 28$
- Choose 2 columns: $\binom{8}{2} = 28$
- For each 2×2 selection, there are 2 diagonal placements (both valid, non-attacking)
- Since rooks are identical, each board configuration is counted exactly once

**Total = $28 \times 28 \times 2 = 1568$**

**Answer: 1568**

---

## Question 11 | Pigeonhole Principle (MSQ)

**Problem:** Among any 27 distinct integers, which of the following MUST be true?

A) At least 2 have the same last digit  
B) At least 3 have the same last digit  
C) At least 3 have the same remainder when divided by 10  
D) At least 2 have the same remainder when divided by 9

**Trap Alert:** Different formulations of the same pigeonhole!

### Solution via Technique:
**A and C are equivalent:** Last digit = remainder mod 10

**Pigeonhole:** 27 integers, 10 possible last digits
$\lceil 27/10 \rceil = 3$

So at least 3 integers share the same last digit.

**For D:** 27 integers, 9 possible remainders (0-8) when divided by 9
$\lceil 27/9 \rceil = 3$

At least 3 share the same remainder mod 9.

**Answer: A, B, C, D (all are true!)**

But wait, let's verify:
- A: At least 2 same last digit? If at least 3, then certainly at least 2. ✓
- B: At least 3 same last digit? Yes, by pigeonhole. ✓
- C: Same as B (remainder mod 10 = last digit). ✓
- D: At least 2 same remainder mod 9? If at least 3, then yes. Actually, $\lceil 27/9 \rceil = 3$, so at least 3, hence at least 2. ✓

**Answer: All A, B, C, D**

---

## Question 12 | Staircase Paths (NAT)

**Problem:** Find the number of ways to go from $(0,0)$ to $(7,4)$ if you can only move right (R) or up (U), and you must pass through $(3,2)$.

### Solution via Technique:
**Paths = Paths to (3,2) × Paths from (3,2) to (7,4)**

**To (3,2):** Need 3R and 2U
$$\binom{3+2}{2} = \binom{5}{2} = 10$$

**From (3,2) to (7,4):** Need 4R and 2U
$$\binom{4+2}{2} = \binom{6}{2} = 15$$

**Total = $10 \times 15 = 150$**

**Answer: 150**

---

## Question 13 | Generating Functions Approach (NAT)

**Problem:** Find the coefficient of $x^{10}$ in $(1+x+x^2+...+x^{10})^3$.

**Trap Alert:** This represents the number of ways to select from 3 groups.

### Solution via Technique:
**Each factor:** $\frac{1-x^{11}}{1-x}$

**Product:** $\left(\frac{1-x^{11}}{1-x}\right)^3 = (1-x^{11})^3 \cdot (1-x)^{-3}$

**Coefficient of $x^{10}$:**
$(1-x^{11})^3 = 1 - 3x^{11} + 3x^{22} - x^{33}$

For $x^{10}$, we only need the "1" term from $(1-x^{11})^3$.

**Coefficient of $x^{10}$ in $(1-x)^{-3}$:**
$$\binom{-3}{10}(-1)^{10} = \binom{10+3-1}{10} = \binom{12}{10} = \binom{12}{2} = 66$$

**Answer: 66**

---

## Question 14 | Catalan Number Application (NAT)

**Problem:** In how many ways can 6 pairs of parentheses be validly matched?

**Trap Alert:** This is a classic Catalan number problem!

### Solution via Technique:
**The Catalan Number:**
$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)! \cdot n!}$$

For $n = 6$:
$$C_6 = \frac{1}{7}\binom{12}{6} = \frac{1}{7} \times 924 = 132$$

**Answer: 132**

**Other Catalan Applications:**
- Valid parentheses matching
- Binary trees with n nodes
- Triangulations of (n+2)-gon
- Dyck paths
- Non-crossing partitions

---

## Question 15 | Inclusion-Exclusion Deep (NAT)

**Problem:** How many integers from 1 to 1000 are divisible by 2, 3, or 5?

### Solution via Technique:
**Let:**
- $A$ = divisible by 2
- $B$ = divisible by 3
- $C$ = divisible by 5

**Inclusion-Exclusion:**
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

**Calculate:**
- $|A| = \lfloor 1000/2 \rfloor = 500$
- $|B| = \lfloor 1000/3 \rfloor = 333$
- $|C| = \lfloor 1000/5 \rfloor = 200$
- $|A \cap B| = \lfloor 1000/6 \rfloor = 166$
- $|B \cap C| = \lfloor 1000/15 \rfloor = 66$
- $|A \cap C| = \lfloor 1000/10 \rfloor = 100$
- $|A \cap B \cap C| = \lfloor 1000/30 \rfloor = 33$

$$|A \cup B \cup C| = 500 + 333 + 200 - 166 - 66 - 100 + 33 = 734$$

**Answer: 734**

---

## Mental Machinery

### The Bizarre Mnemonic for PNC:
**"PERM = Position Matters, COMB = Collection Only"**

Imagine a **PERM**anent tattoo artist who cares WHERE each design goes vs a **COMB** collector who just grabs items into a basket.

### The Mental Slider for Arrangements:
Visualize n objects on a **conveyor belt**. 
- **Permutation:** Objects slide into n distinct slots. Order = which slot.
- **Combination:** Objects fall into a bag. Bag doesn't care about order.
- **Circular:** Belt is a loop—first position is arbitrary.

### The 5-Second Snap-Check:
- **$n!$ grows FAST:** $10! > 3$ million
- **$\binom{n}{r} = \binom{n}{n-r}$:** Symmetry check
- **Combination ≤ Permutation:** Always true

---

## Mastery Checkpoint

**You have completed the Permutation & Combination module.** These counting principles form the foundation for probability problems and appear frequently in GATE/ESE/PSU exams.

**Next Steps:** Practice the Probability module to see how PNC concepts apply to real-world scenarios and conditional problems.
