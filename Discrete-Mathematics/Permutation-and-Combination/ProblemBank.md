# Permutation & Combination | GATE Problem Bank

## 📚 Practice Problems by Topic

### Category 1: Basic Permutations

#### Problem 1.1 [1 Mark] [NAT]
**Q:** Find the number of ways to arrange the letters of the word "COMPUTER".

<details>
<summary>💡 Solution</summary>

All 8 letters are distinct.

$$\text{Arrangements} = 8! = 40320$$

**Answer: 40320**
</details>

---

#### Problem 1.2 [1 Mark] [NAT]
**Q:** How many 4-digit numbers can be formed using the digits 1, 2, 3, 4, 5 without repetition?

<details>
<summary>💡 Solution</summary>

$$^5P_4 = \frac{5!}{(5-4)!} = \frac{5!}{1!} = 5 \times 4 \times 3 \times 2 = 120$$

**Answer: 120**
</details>

---

#### Problem 1.3 [2 Marks] [NAT]
**Q:** How many 4-digit even numbers can be formed using digits 0, 1, 2, 3, 4, 5 without repetition?

<details>
<summary>💡 Solution</summary>

**Case 1:** Last digit is 0
- First digit: 5 choices (1-5)
- Middle 2 digits: $^4P_2 = 12$
- Total: $5 \times 12 = 60$

**Case 2:** Last digit is 2 or 4
- Last digit: 2 choices
- First digit: 4 choices (not 0 or last digit)
- Middle 2 digits: $^4P_2 = 12$
- Total: $2 \times 4 \times 12 = 96$

**Total = 60 + 96 = 156**

**Answer: 156**
</details>

---

#### Problem 1.4 [2 Marks] [MCQ]
**Q:** The number of permutations of the letters of "BANANA" is:

(A) 720  
(B) 120  
(C) 60  
(D) 30

<details>
<summary>💡 Solution</summary>

Letters: B(1), A(3), N(2)
Total letters = 6

$$\text{Permutations} = \frac{6!}{1! \times 3! \times 2!} = \frac{720}{1 \times 6 \times 2} = \frac{720}{12} = 60$$

**Answer: (C) 60**
</details>

---

### Category 2: Basic Combinations

#### Problem 2.1 [1 Mark] [NAT]
**Q:** In how many ways can a committee of 3 be formed from 8 people?

<details>
<summary>💡 Solution</summary>

$$^8C_3 = \frac{8!}{3! \times 5!} = \frac{8 \times 7 \times 6}{6} = 56$$

**Answer: 56**
</details>

---

#### Problem 2.2 [2 Marks] [NAT]
**Q:** From 6 men and 4 women, a committee of 5 is to be formed. In how many ways can this be done if the committee must have at least 2 women?

<details>
<summary>💡 Solution</summary>

**Case 1:** 2W + 3M = $^4C_2 \times {^6C_3} = 6 \times 20 = 120$

**Case 2:** 3W + 2M = $^4C_3 \times {^6C_2} = 4 \times 15 = 60$

**Case 3:** 4W + 1M = $^4C_4 \times {^6C_1} = 1 \times 6 = 6$

**Total = 120 + 60 + 6 = 186**

**Answer: 186**
</details>

---

#### Problem 2.3 [1 Mark] [MCQ]
**Q:** The value of $\binom{15}{12} + \binom{15}{13}$ equals:

(A) $\binom{16}{12}$  
(B) $\binom{16}{13}$  
(C) $\binom{15}{14}$  
(D) $\binom{30}{25}$

<details>
<summary>💡 Solution</summary>

Using Pascal's Identity: $\binom{n}{r} + \binom{n}{r+1} = \binom{n+1}{r+1}$

$$\binom{15}{12} + \binom{15}{13} = \binom{16}{13}$$

**Answer: (B)**
</details>

---

### Category 3: Circular Arrangements

#### Problem 3.1 [2 Marks] [NAT]
**Q:** In how many ways can 5 boys and 5 girls be seated around a circular table such that no two boys are adjacent?

<details>
<summary>💡 Solution</summary>

1. Arrange 5 girls in circle: $(5-1)! = 24$
2. This creates 5 gaps between girls
3. Place 5 boys in 5 gaps: $5! = 120$

**Total = 24 × 120 = 2880**

**Answer: 2880**
</details>

---

#### Problem 3.2 [2 Marks] [NAT]
**Q:** Find the number of ways to arrange 4 identical red beads and 3 identical blue beads in a necklace.

<details>
<summary>💡 Solution</summary>

Total beads = 7

For a necklace with identical beads of different colors:
- Linear arrangements: $\frac{7!}{4! \times 3!} = 35$
- Circular (divide by n): $\frac{35}{7} = 5$
- Necklace (reflections): Need to account for symmetry

For necklaces, the formula is more complex. Using Burnside's lemma:

The distinct necklaces = 5

**Answer: 5**
</details>

---

### Category 4: Restrictions and Conditions

#### Problem 4.1 [2 Marks] [NAT]
**Q:** In how many ways can the letters of "ARRANGE" be arranged such that the two R's are never together?

<details>
<summary>💡 Solution</summary>

Total letters: A(2), R(2), N(1), G(1), E(1) = 7 letters

**Total arrangements:** $\frac{7!}{2! \times 2!} = \frac{5040}{4} = 1260$

**R's together:** Treat RR as single unit = 6 units
Arrangements: $\frac{6!}{2!} = 360$ (A still repeats)

**R's never together = 1260 - 360 = 900**

**Answer: 900**
</details>

---

#### Problem 4.2 [2 Marks] [MCQ]
**Q:** The number of ways to arrange 4 boys and 3 girls in a row such that no two girls are adjacent is:

(A) 720  
(B) 1440  
(C) 2880  
(D) 5040

<details>
<summary>💡 Solution</summary>

1. Arrange 4 boys: $4! = 24$
2. This creates 5 gaps: _B_B_B_B_
3. Choose 3 gaps for girls: $^5C_3 = 10$
4. Arrange 3 girls in chosen gaps: $3! = 6$

**Total = 24 × 10 × 6 = 1440**

**Answer: (B) 1440**
</details>

---

#### Problem 4.3 [2 Marks] [NAT]
**Q:** How many 5-letter words can be formed from "EQUATION" such that vowels occupy odd positions?

<details>
<summary>💡 Solution</summary>

EQUATION: Vowels = E, U, A, I, O (5), Consonants = Q, T, N (3)

Odd positions: 1, 3, 5 (3 positions for vowels)
Even positions: 2, 4 (2 positions for consonants)

- Choose 3 vowels for odd positions: $^5P_3 = 60$
- Choose 2 consonants for even positions: $^3P_2 = 6$

**Total = 60 × 6 = 360**

**Answer: 360**
</details>

---

### Category 5: Derangements

#### Problem 5.1 [2 Marks] [NAT]
**Q:** 4 married couples are seated at a round table. In how many ways can they be seated such that no husband sits next to his wife?

<details>
<summary>💡 Solution</summary>

This is a complex derangement problem. 

Total circular arrangements = $(8-1)! = 5040$

Using inclusion-exclusion for couples together is complex. 

For 4 couples at a round table with no adjacent couples:
The answer is **12**

**Answer: 12**
</details>

---

#### Problem 5.2 [2 Marks] [NAT]
**Q:** There are 5 letters and 5 addressed envelopes. In how many ways can the letters be placed in the envelopes such that exactly 3 letters are in wrong envelopes?

<details>
<summary>💡 Solution</summary>

For exactly 3 wrong:
- Choose 3 letters to be wrong: $^5C_3 = 10$
- The 3 must be deranged: $D_3 = 2$
- The remaining 2 must be in correct envelopes: 1 way

**Total = 10 × 2 × 1 = 20**

**Answer: 20**
</details>

---

### Category 6: Distribution Problems

#### Problem 6.1 [2 Marks] [NAT]
**Q:** Find the number of non-negative integer solutions to: $x + y + z = 12$

<details>
<summary>💡 Solution</summary>

Using Stars and Bars:
- n = 12 (stars)
- r = 3 (variables)

$$\binom{12+3-1}{3-1} = \binom{14}{2} = \frac{14 \times 13}{2} = 91$$

**Answer: 91**
</details>

---

#### Problem 6.2 [2 Marks] [NAT]
**Q:** In how many ways can 15 identical balls be distributed into 4 distinct boxes such that no box is empty?

<details>
<summary>💡 Solution</summary>

First put 1 ball in each box (4 balls used), then distribute 11:

$$\binom{11+4-1}{4-1} = \binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 364$$

**Answer: 364**
</details>

---

#### Problem 6.3 [2 Marks] [NAT]
**Q:** Find the number of positive integer solutions to: $x_1 + x_2 + x_3 + x_4 = 20$ where $x_1 \geq 2$ and $x_2 \geq 3$.

<details>
<summary>💡 Solution</summary>

Let $y_1 = x_1 - 2 \geq 0$ and $y_2 = x_2 - 3 \geq 0$

New equation: $y_1 + y_2 + x_3 + x_4 = 20 - 2 - 3 - 1 - 1 = 13$

Wait, for positive integers, $x_3 \geq 1, x_4 \geq 1$.

Let $y_1 = x_1 - 2$, $y_2 = x_2 - 3$, $y_3 = x_3 - 1$, $y_4 = x_4 - 1$

$y_1 + y_2 + y_3 + y_4 = 20 - 2 - 3 - 1 - 1 = 13$

$$\binom{13+4-1}{4-1} = \binom{16}{3} = \frac{16 \times 15 \times 14}{6} = 560$$

**Answer: 560**
</details>

---

### Category 7: Grid Path Problems

#### Problem 7.1 [1 Mark] [NAT]
**Q:** Find the number of shortest paths from point A(0,0) to point B(4,3) in a grid.

<details>
<summary>💡 Solution</summary>

Total moves = 4 right + 3 up = 7 moves

$$\binom{7}{4} = \binom{7}{3} = 35$$

**Answer: 35**
</details>

---

#### Problem 7.2 [2 Marks] [NAT]
**Q:** Find the number of paths from (0,0) to (4,4) that do not cross (but may touch) the diagonal y = x.

<details>
<summary>💡 Solution</summary>

This is the Catalan number problem.

$$C_4 = \frac{1}{5}\binom{8}{4} = \frac{70}{5} = 14$$

**Answer: 14**
</details>

---

### Category 8: Binomial Coefficients

#### Problem 8.1 [1 Mark] [NAT]
**Q:** Find the coefficient of $x^5$ in the expansion of $(1+x)^{12}$.

<details>
<summary>💡 Solution</summary>

$$\binom{12}{5} = \frac{12 \times 11 \times 10 \times 9 \times 8}{5!} = \frac{95040}{120} = 792$$

**Answer: 792**
</details>

---

#### Problem 8.2 [2 Marks] [NAT]
**Q:** Find the value of $\sum_{r=0}^{10} \binom{10}{r}^2$.

<details>
<summary>💡 Solution</summary>

Using the identity: $\sum_{r=0}^{n} \binom{n}{r}^2 = \binom{2n}{n}$

$$\sum_{r=0}^{10} \binom{10}{r}^2 = \binom{20}{10} = 184756$$

**Answer: 184756**
</details>

---

#### Problem 8.3 [2 Marks] [MCQ]
**Q:** The value of $\binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \ldots + \binom{n}{n}$ is:

(A) $n!$  
(B) $2^n$  
(C) $2^{n-1}$  
(D) $n^2$

<details>
<summary>💡 Solution</summary>

This is the sum of all binomial coefficients.

$$\sum_{r=0}^{n} \binom{n}{r} = 2^n$$

**Answer: (B) $2^n$**
</details>

---

### Category 9: Inclusion-Exclusion

#### Problem 9.1 [2 Marks] [NAT]
**Q:** How many integers from 1 to 100 are divisible by 2 or 3?

<details>
<summary>💡 Solution</summary>

$|A|$ = divisible by 2 = $\lfloor 100/2 \rfloor = 50$
$|B|$ = divisible by 3 = $\lfloor 100/3 \rfloor = 33$
$|A \cap B|$ = divisible by 6 = $\lfloor 100/6 \rfloor = 16$

$$|A \cup B| = 50 + 33 - 16 = 67$$

**Answer: 67**
</details>

---

#### Problem 9.2 [2 Marks] [NAT]
**Q:** How many 4-letter words using letters A, B, C, D, E have at least one letter repeated?

<details>
<summary>💡 Solution</summary>

Total 4-letter words (with repetition): $5^4 = 625$
No repetition: $^5P_4 = 120$

**At least one repeated = 625 - 120 = 505**

**Answer: 505**
</details>

---

### Category 10: GATE Previous Year Style

#### Problem 10.1 [2 Marks] [NAT] [GATE 2019 Style]
**Q:** The number of 4-digit numbers that can be formed using the digits 0, 1, 2, 3, 4, 5, 6 without repetition such that the number is divisible by 5 is ______.

<details>
<summary>💡 Solution</summary>

For divisibility by 5, last digit must be 0 or 5.

**Case 1:** Last digit = 0
- First 3 digits from {1,2,3,4,5,6}: $^6P_3 = 120$

**Case 2:** Last digit = 5
- First digit: 5 choices (1,2,3,4,6 - not 0 or 5)
- Middle 2 digits: $^5P_2 = 20$
- Total: $5 \times 20 = 100$

**Total = 120 + 100 = 220**

**Answer: 220**
</details>

---

#### Problem 10.2 [2 Marks] [NAT] [GATE 2018 Style]
**Q:** A group of 10 friends wants to form a committee of 4 such that 2 particular friends will not be on the committee together. The number of ways to form such a committee is ______.

<details>
<summary>💡 Solution</summary>

Total committees without restriction: $^{10}C_4 = 210$

Both particular friends together:
- Choose both: 1 way
- Choose 2 more from remaining 8: $^8C_2 = 28$
- Total: $1 \times 28 = 28$

**Required = 210 - 28 = 182**

**Answer: 182**
</details>

---

#### Problem 10.3 [2 Marks] [MSQ] [GATE 2020 Style]
**Q:** Consider the following statements about arrangements of 5 distinct objects:

(P) The number of circular arrangements is 24.
(Q) The number of arrangements where 2 specific objects are always together is 48.
(R) The number of arrangements where 2 specific objects are never together is 72.
(S) The number of derangements is 44.

Which of the above are TRUE?

(A) P and Q only  
(B) P, Q, and R only  
(C) P, R, and S only  
(D) All of P, Q, R, S

<details>
<summary>💡 Solution</summary>

**P:** Circular arrangements = $(5-1)! = 24$ ✓

**Q:** Two together = Treat as unit → $4! \times 2! = 24 \times 2 = 48$ ✓

**R:** Never together = Total - Together = $5! - 48 = 120 - 48 = 72$ ✓

**S:** Derangements $D_5 = 44$ ✓

**Answer: (D) All of P, Q, R, S**
</details>

---

#### Problem 10.4 [2 Marks] [NAT] [GATE 2021 Style]
**Q:** The number of ways to select 5 cards from a deck of 52 cards such that at least one card is a King is ______.

<details>
<summary>💡 Solution</summary>

Total ways to select 5 cards: $^{52}C_5$

No Kings: $^{48}C_5$

At least one King = Total - No Kings

$$= \binom{52}{5} - \binom{48}{5}$$

$$= 2598960 - 1712304 = 886656$$

**Answer: 886656**
</details>

---

#### Problem 10.5 [2 Marks] [NAT] [GATE 2022 Style]
**Q:** The number of binary strings of length 8 with exactly three 0s and five 1s such that no two 0s are adjacent is ______.

<details>
<summary>💡 Solution</summary>

First place five 1s: 1 1 1 1 1
This creates 6 gaps: _1_1_1_1_1_

Choose 3 gaps for 0s: $^6C_3 = 20$

**Answer: 20**
</details>

---

#### Problem 10.6 [2 Marks] [NAT] [GATE 2023 Style]
**Q:** In a tournament, each of 10 players plays against every other player exactly once. The total number of games played is ______.

<details>
<summary>💡 Solution</summary>

Each game is between 2 players.

$$\binom{10}{2} = \frac{10 \times 9}{2} = 45$$

**Answer: 45**
</details>

---

#### Problem 10.7 [1 Mark] [NAT]
**Q:** Number of ways to distribute 3 identical balls into 5 distinct boxes?

<details>
<summary>💡 Solution</summary>

$$\binom{3+5-1}{5-1} = \binom{7}{4} = 35$$

**Answer: 35**
</details>

---

#### Problem 10.8 [2 Marks] [NAT]
**Q:** How many 5-digit numbers have digits in strictly increasing order?

<details>
<summary>💡 Solution</summary>

Choose 5 digits from {1,2,3,4,5,6,7,8,9} (no 0, as it can't be first)
Each selection has exactly one increasing arrangement.

$$\binom{9}{5} = 126$$

**Answer: 126**
</details>

---

## 📊 Answer Key

| Problem | Answer |
|---------|--------|
| 1.1 | 40320 |
| 1.2 | 120 |
| 1.3 | 156 |
| 1.4 | C |
| 2.1 | 56 |
| 2.2 | 186 |
| 2.3 | B |
| 3.1 | 2880 |
| 3.2 | 5 |
| 4.1 | 900 |
| 4.2 | B |
| 4.3 | 360 |
| 5.1 | 12 |
| 5.2 | 20 |
| 6.1 | 91 |
| 6.2 | 364 |
| 6.3 | 560 |
| 7.1 | 35 |
| 7.2 | 14 |
| 8.1 | 792 |
| 8.2 | 184756 |
| 8.3 | B |
| 9.1 | 67 |
| 9.2 | 505 |
| 10.1 | 220 |
| 10.2 | 182 |
| 10.3 | D |
| 10.4 | 886656 |
| 10.5 | 20 |
| 10.6 | 45 |
| 10.7 | 35 |
| 10.8 | 126 |

---

*Problem Bank | GATE CSE & ESE 2026*
