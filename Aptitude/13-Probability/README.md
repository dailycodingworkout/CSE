# 🎲 Probability | The Singularity

> **The Atomic Truth:** *Probability measures likelihood—favorable outcomes over total outcomes.*

---

## 📚 Table of Contents
1. [Fundamental Concepts](#fundamental-concepts)
2. [Basic Probability](#basic-probability)
3. [Probability Rules](#probability-rules)
4. [Conditional Probability](#conditional-probability)
5. [Bayes' Theorem](#bayes-theorem)
6. [Random Variables](#random-variables)
7. [Common Distributions](#common-distributions)
8. [GATE & ESE Problem Patterns](#gate--ese-problem-patterns)
9. [Speed Tricks & Shortcuts](#speed-tricks--shortcuts)
10. [Practice Problems](#practice-problems)

---

## Fundamental Concepts

### Why Probability Matters?
Probability is a **GATE favorite** (2-3 questions guaranteed). It tests:
- Counting principles
- Logical reasoning
- Understanding of randomness
- Engineering reliability concepts

### Basic Terminology

| Term | Definition |
|------|------------|
| **Experiment** | Process with uncertain outcome |
| **Sample Space (S)** | Set of all possible outcomes |
| **Event** | Subset of sample space |
| **Outcome** | Single result of experiment |
| **Favorable Outcome** | Outcome satisfying event condition |

### Types of Events

| Type | Definition |
|------|------------|
| **Certain Event** | P(E) = 1 |
| **Impossible Event** | P(E) = 0 |
| **Mutually Exclusive** | Cannot occur together |
| **Exhaustive** | Cover all possibilities |
| **Independent** | Occurrence doesn't affect other |
| **Complement** | E' = S - E |

> **💡 The Golden Pivot:** $0 \leq P(E) \leq 1$ always!

---

## Basic Probability

### Classical Definition

$$P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}} = \frac{n(E)}{n(S)}$$

### Complement Rule

$$P(E') = 1 - P(E)$$

$$P(\text{at least one}) = 1 - P(\text{none})$$

### Common Sample Spaces

| Experiment | Sample Space | Size |
|------------|--------------|------|
| One coin | {H, T} | 2 |
| Two coins | {HH, HT, TH, TT} | 4 |
| One die | {1,2,3,4,5,6} | 6 |
| Two dice | 36 outcomes | 36 |
| One card | 52 cards | 52 |
| n coins | $2^n$ outcomes | $2^n$ |

---

## Probability Rules

### Addition Rule (OR)

**For any events:**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**For mutually exclusive events:**
$$P(A \cup B) = P(A) + P(B)$$

### Multiplication Rule (AND)

**For any events:**
$$P(A \cap B) = P(A) \times P(B|A) = P(B) \times P(A|B)$$

**For independent events:**
$$P(A \cap B) = P(A) \times P(B)$$

### De Morgan's Laws

$$P(\overline{A \cup B}) = P(\bar{A} \cap \bar{B})$$
$$P(\overline{A \cap B}) = P(\bar{A} \cup \bar{B})$$

---

## Conditional Probability

### Definition

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Interpretation:** Probability of A, given that B has occurred.

### Independence Test

Events A and B are independent iff:
$$P(A|B) = P(A)$$
or equivalently:
$$P(A \cap B) = P(A) \times P(B)$$

### Total Probability Theorem

If $B_1, B_2, ..., B_n$ are mutually exclusive and exhaustive:
$$P(A) = \sum_{i=1}^{n} P(B_i) \times P(A|B_i)$$

---

## Bayes' Theorem

### Formula

$$P(B_i|A) = \frac{P(B_i) \times P(A|B_i)}{\sum_{j=1}^{n} P(B_j) \times P(A|B_j)}$$

### Simpler Form (Two Events)

$$P(B|A) = \frac{P(B) \times P(A|B)}{P(A)}$$

### Application Example

**Medical Testing:**
- Disease prevalence: 1% (P(D) = 0.01)
- Test accuracy: 99% (P(+|D) = 0.99)
- False positive rate: 5% (P(+|D') = 0.05)

If tested positive, probability of having disease:
$$P(D|+) = \frac{0.01 \times 0.99}{0.01 \times 0.99 + 0.99 \times 0.05}$$
$$= \frac{0.0099}{0.0099 + 0.0495} = \frac{0.0099}{0.0594} \approx 0.167$$

> **Insight:** Even with 99% accurate test, positive result means only ~17% chance of disease due to low prevalence!

---

## Random Variables

### Definition
A random variable is a function that assigns a numerical value to each outcome.

### Types

**Discrete:** Takes countable values (dice roll, number of defects)
**Continuous:** Takes any value in range (height, weight, time)

### Expected Value (Mean)

**Discrete:**
$$E(X) = \sum x_i \times P(X = x_i)$$

**Properties:**
- $E(aX + b) = aE(X) + b$
- $E(X + Y) = E(X) + E(Y)$
- For independent X, Y: $E(XY) = E(X) \times E(Y)$

### Variance

$$\text{Var}(X) = E(X^2) - [E(X)]^2$$

**Properties:**
- $\text{Var}(aX + b) = a^2 \text{Var}(X)$
- For independent X, Y: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

### Standard Deviation

$$\sigma = \sqrt{\text{Var}(X)}$$

---

## Common Distributions

### Binomial Distribution

For n independent trials, each with success probability p:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Mean:** $\mu = np$
**Variance:** $\sigma^2 = np(1-p)$

### Poisson Distribution

For rare events with average rate λ:

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$$

**Mean:** $\mu = \lambda$
**Variance:** $\sigma^2 = \lambda$

### Geometric Distribution

First success on k-th trial:

$$P(X = k) = (1-p)^{k-1} p$$

**Mean:** $\mu = \frac{1}{p}$

### Uniform Distribution

Each outcome equally likely:

**Discrete:** $P(X = x) = \frac{1}{n}$ for n outcomes
**Continuous (a,b):** $f(x) = \frac{1}{b-a}$

**Mean:** $\mu = \frac{a+b}{2}$
**Variance:** $\sigma^2 = \frac{(b-a)^2}{12}$

### Normal Distribution

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

**Standard Normal:** $\mu = 0$, $\sigma = 1$

**68-95-99.7 Rule:**
- 68% within 1σ of mean
- 95% within 2σ of mean
- 99.7% within 3σ of mean

---

## GATE & ESE Problem Patterns

### Pattern 1: Dice Problems
> Two dice are thrown. Probability of sum being 7?
- Favorable: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6
- Total = 36
- P = 6/36 = **1/6**

### Pattern 2: Card Problems
> One card drawn from 52 cards. Probability of red king?
- Red kings = 2 (heart K, diamond K)
- P = 2/52 = **1/26**

### Pattern 3: Balls in Urn
> Urn has 4 red and 6 blue balls. Two drawn without replacement. P(both red)?
$$P = \frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15}$$

### Pattern 4: At Least One
> Three coins tossed. P(at least one head)?
- P(no head) = P(TTT) = 1/8
- P(at least one head) = 1 - 1/8 = **7/8**

### Pattern 5: Conditional Probability
> A bag has 5 red and 4 black balls. Two drawn. P(second is red | first is red)?
$$P = \frac{4}{8} = \frac{1}{2}$$

### The 2026 Adversarial Vault

**The Inversion (Common Mistake):**
"Probability of getting at least 2 heads in 3 tosses."

Wrong approach: Adding P(2H) + P(3H) with wrong counting

**The Elegant Solution:**
Using complement:
- P(0H) = 1/8
- P(1H) = 3/8
- P(≥2H) = 1 - 1/8 - 3/8 = **4/8 = 1/2**

Or directly:
- P(2H) = $\binom{3}{2}(1/2)^3 = 3/8$
- P(3H) = $\binom{3}{3}(1/2)^3 = 1/8$
- Total = **4/8 = 1/2**

**MSQ Logic Gate:**
- P(A ∪ B) ≤ P(A) + P(B) (can be less due to overlap)
- P(A ∩ B) ≤ min(P(A), P(B))

**NAT Precision Lock:**
- Express as fraction when exact
- Decimal answers typically to 2-4 decimal places
- Watch for "with replacement" vs "without replacement"

---

## Speed Tricks & Shortcuts

### Trick 1: Complement Method

For "at least one" problems:
$$P(\text{at least one}) = 1 - P(\text{none})$$

### Trick 2: Two Dice Sum Table

| Sum | Combinations | P |
|-----|--------------|---|
| 2 | 1 | 1/36 |
| 3 | 2 | 2/36 |
| 4 | 3 | 3/36 |
| 5 | 4 | 4/36 |
| 6 | 5 | 5/36 |
| 7 | 6 | 6/36 |
| 8 | 5 | 5/36 |
| 9 | 4 | 4/36 |
| 10 | 3 | 3/36 |
| 11 | 2 | 2/36 |
| 12 | 1 | 1/36 |

### Trick 3: Card Deck Quick Facts

- Total cards: 52
- Each suit: 13 cards
- Face cards (J, Q, K): 12 total (3 per suit)
- Red cards: 26, Black cards: 26

### Trick 4: Independence Shortcut

If independent:
$$P(\text{both succeed}) = P(A) \times P(B)$$
$$P(\text{both fail}) = (1-P(A)) \times (1-P(B))$$
$$P(\text{exactly one}) = P(A)(1-P(B)) + P(B)(1-P(A))$$

### Trick 5: Birthday Problem Approximation

For n people, P(at least 2 share birthday) ≈ $1 - e^{-n^2/730}$
- 23 people → ~50%
- 50 people → ~97%

---

## Permanent Recall

### The Bizarre Mnemonic (Bayes)
*"Bayes is backwards thinking: You saw the effect (positive test), now trace back to cause (actual disease). The cause that explains the effect better, wins the probability race!"*

### The Mental Slider
Imagine a Venn diagram:
- Two overlapping circles (A and B)
- P(A ∩ B) is the overlap
- P(A ∪ B) is the total area
- P(A|B) is overlap/B's circle

### The 5-Second Snap-Check
- Probability must be between 0 and 1
- All probabilities in sample space sum to 1
- P(A) + P(A') = 1 always

---

## Practice Problems

### Level 1: Fundamentals
1. A die is thrown twice. Find P(sum = 9).
2. A card is drawn from a deck. Find P(queen or heart).
3. A coin is tossed 4 times. Find P(exactly 2 heads).

### Level 2: GATE Standard
4. Bag A has 3 red and 2 white balls. Bag B has 4 red and 3 white. A bag is chosen at random and a ball drawn. P(ball is red)?
5. A manufacturing process has 5% defective items. If 4 items are selected, find P(at most 1 defective).
6. If P(A) = 0.6, P(B) = 0.4, P(A ∩ B) = 0.3, find P(A ∪ B) and P(A|B).

### Level 3: IIT Examiner Level
7. A box has 5 red, 3 white, 2 blue balls. 3 balls drawn at random. P(1 of each color)?
8. In a class, 60% students study Math, 40% study Physics, 20% study both. If a student studies Math, P(also studies Physics)?
9. A test has 10 questions with 4 options each. A student guesses randomly on all. P(getting at least 3 correct)?

---

### Solutions

<details>
<summary>Click to reveal solutions</summary>

1. Sum = 9: (3,6), (4,5), (5,4), (6,3) = 4 ways
   P = 4/36 = **1/9**

2. P(Queen) = 4/52
   P(Heart) = 13/52
   P(Queen ∩ Heart) = 1/52 (Queen of Hearts)
   P(Q ∪ H) = 4/52 + 13/52 - 1/52 = 16/52 = **4/13**

3. P(2H in 4 tosses) = $\binom{4}{2}(1/2)^4 = 6 \times 1/16 = **3/8**$

4. P(A) = P(B) = 1/2
   P(Red|A) = 3/5, P(Red|B) = 4/7
   P(Red) = 1/2 × 3/5 + 1/2 × 4/7 = 3/10 + 2/7 = 21/70 + 20/70 = **41/70**

5. n = 4, p = 0.05
   P(0 defective) = (0.95)^4 ≈ 0.8145
   P(1 defective) = $\binom{4}{1}(0.05)(0.95)^3 ≈ 0.1715$
   P(≤1) = 0.8145 + 0.1715 = **0.986** (or 98.6%)

6. P(A ∪ B) = 0.6 + 0.4 - 0.3 = **0.7**
   P(A|B) = P(A ∩ B)/P(B) = 0.3/0.4 = **0.75**

7. Total balls = 10
   Total ways = $\binom{10}{3} = 120$
   Favorable = $\binom{5}{1} × \binom{3}{1} × \binom{2}{1} = 5 × 3 × 2 = 30$
   P = 30/120 = **1/4**

8. P(Math) = 0.6, P(Both) = 0.2
   P(Physics|Math) = P(Both)/P(Math) = 0.2/0.6 = **1/3**

9. n = 10, p = 1/4
   P(≥3) = 1 - P(0) - P(1) - P(2)
   
   P(0) = (3/4)^10 ≈ 0.0563
   P(1) = $\binom{10}{1}(1/4)(3/4)^9 ≈ 0.1877$
   P(2) = $\binom{10}{2}(1/4)^2(3/4)^8 ≈ 0.2816$
   
   P(≥3) = 1 - 0.0563 - 0.1877 - 0.2816 = **0.4744** (≈47.4%)

</details>

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining Probability with Permutation and Combination for a Rank-1 simulation?
