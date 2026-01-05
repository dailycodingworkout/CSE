# Chapter 17: Probability

> **The mathematics of uncertainty - quantifying chance and randomness**

---

## 🎯 Why Study This?

- Essential for GATE/ESE aptitude and core subjects
- Foundation for statistics and machine learning
- Real-world: Risk analysis, decision making

---

## 📚 Part 1: Basic Probability

### Fundamental Definitions

**Experiment**: An action with uncertain outcome (rolling a die)
**Sample Space (S)**: Set of all possible outcomes
**Event (E)**: Subset of sample space (getting even number)

---

### Probability Definition

```
P(E) = Number of favorable outcomes / Total number of outcomes
     = n(E) / n(S)
```

**Properties**:
```
0 ≤ P(E) ≤ 1
P(S) = 1 (certain event)
P(∅) = 0 (impossible event)
P(E') = 1 - P(E) (complement)
```

---

### Types of Events

| Type | Definition |
|------|------------|
| **Simple Event** | Single outcome |
| **Compound Event** | Two or more outcomes |
| **Mutually Exclusive** | Cannot occur together: P(A ∩ B) = 0 |
| **Exhaustive Events** | Cover entire sample space |
| **Independent Events** | One doesn't affect the other |
| **Complementary** | E and E' together = S |

---

## 📐 Probability Rules

### Addition Rule

**For any two events**:
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

**For mutually exclusive events** (P(A ∩ B) = 0):
```
P(A ∪ B) = P(A) + P(B)
```

**For three events**:
```
P(A ∪ B ∪ C) = P(A) + P(B) + P(C) 
              - P(A∩B) - P(B∩C) - P(A∩C) 
              + P(A∩B∩C)
```

---

### Multiplication Rule

**For any two events**:
```
P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)
```

**For independent events**:
```
P(A ∩ B) = P(A) × P(B)
```

---

### Conditional Probability

Probability of A given B has occurred:
```
P(A|B) = P(A ∩ B) / P(B), where P(B) > 0
```

**💡 Analogy**: Given that B happened, how does this affect A's probability?

---

## 📊 Bayes' Theorem

```
P(A|B) = P(B|A) × P(A) / P(B)
```

**Generalized (with partitions)**:
```
P(Aᵢ|B) = P(B|Aᵢ) × P(Aᵢ) / Σ[P(B|Aⱼ) × P(Aⱼ)]
```

**💡 Application**: Finding "reverse" conditional probability

---

## 📚 Part 2: Common Probability Scenarios

### Coin Toss

| Scenario | Probability |
|----------|-------------|
| Head | 1/2 |
| Tail | 1/2 |
| At least 1 head in n tosses | 1 - (1/2)ⁿ |
| Exactly k heads in n tosses | ⁿCₖ(1/2)ⁿ |

---

### Dice Roll (Single Fair Die)

| Scenario | Probability |
|----------|-------------|
| Getting specific number | 1/6 |
| Getting even | 3/6 = 1/2 |
| Getting > 4 | 2/6 = 1/3 |

---

### Two Dice

Total outcomes = 36

| Sum | Ways | Probability |
|-----|------|-------------|
| 2 | 1 | 1/36 |
| 3 | 2 | 2/36 |
| 4 | 3 | 3/36 |
| 5 | 4 | 4/36 |
| 6 | 5 | 5/36 |
| 7 | 6 | 6/36 = 1/6 |
| 8 | 5 | 5/36 |
| ... | ... | ... |

**⚡ Pattern**: Ways increase from 2 to 7, then decrease.

---

### Cards (Standard 52-Card Deck)

| Selection | Count |
|-----------|-------|
| Hearts/Diamonds/Clubs/Spades | 13 each |
| Face cards (J, Q, K) | 12 total |
| Aces | 4 |
| Red cards | 26 |
| Black cards | 26 |

**Example**: P(drawing a heart) = 13/52 = 1/4

---

### Balls in Bag/Urn

**Without replacement**: Probabilities change after each draw
**With replacement**: Probabilities remain same

---

## 📚 Part 3: Advanced Concepts

### Total Probability Theorem

If B₁, B₂, ..., Bₙ partition S:
```
P(A) = Σ P(A|Bᵢ) × P(Bᵢ)
```

---

### Binomial Distribution

For n independent trials, each with success probability p:
```
P(X = k) = ⁿCₖ × pᵏ × (1-p)ⁿ⁻ᵏ

Mean (μ) = np
Variance (σ²) = np(1-p)
```

---

### Poisson Distribution

For rare events with average rate λ:
```
P(X = k) = e⁻λ × λᵏ / k!

Mean = Variance = λ
```

---

### Geometric Distribution

Probability of first success on kth trial:
```
P(X = k) = (1-p)ᵏ⁻¹ × p

Mean = 1/p
```

---

### Expected Value

```
E(X) = Σ xᵢ × P(xᵢ)
```

**Properties**:
```
E(aX + b) = a × E(X) + b
E(X + Y) = E(X) + E(Y)
E(XY) = E(X) × E(Y) (if independent)
```

---

### Variance

```
Var(X) = E(X²) - [E(X)]²
       = Σ (xᵢ - μ)² × P(xᵢ)
```

**Properties**:
```
Var(aX + b) = a² × Var(X)
Var(X + Y) = Var(X) + Var(Y) (if independent)
```

---

## 💡 Advanced Tricks

### Trick 1: Complementary Probability

"At least one" problems:
```
P(at least one) = 1 - P(none)
```

**Example**: P(at least one head in 3 tosses)
```
= 1 - P(no heads) = 1 - (1/2)³ = 7/8
```

---

### Trick 2: Sequential Without Replacement

Multiply decreasing probabilities:
```
P(2 aces in row, no replacement) = (4/52) × (3/51)
```

---

### Trick 3: "Or" for Mutually Exclusive

If events can't happen together:
```
P(A or B) = P(A) + P(B)
```

---

### Trick 4: Conditional Independence

A and B are conditionally independent given C if:
```
P(A ∩ B|C) = P(A|C) × P(B|C)
```

---

### Trick 5: Birthday Problem

Probability that in n people, at least 2 share birthday:
```
P = 1 - (365/365)(364/365)(363/365)...((365-n+1)/365)
≈ 50% for n ≈ 23
```

---

## 📊 Problem Patterns

### Pattern 1: Multiple Draws

**With replacement**: Independent trials
```
P(both red) = P(red) × P(red)
```

**Without replacement**: Dependent
```
P(both red) = P(1st red) × P(2nd red | 1st red)
```

---

### Pattern 2: Success in Trials

**Exactly k successes in n trials**: Binomial
**At least k successes**: Sum from k to n
**First success on kth trial**: Geometric

---

### Pattern 3: Conditional Selection

Use tree diagrams and multiply along paths.

---

## ⚠️ Edge Cases & Traps

### Trap 1: Forgetting "Without Replacement"
```
After drawing, total changes from 52 to 51, etc.
```

### Trap 2: "At Least" vs "Exactly"
```
At least 2 ≠ Exactly 2
At least 2 = P(2) + P(3) + P(4) + ...
```

### Trap 3: Independence Assumption
```
Don't assume events are independent
Check if outcome of one affects the other
```

### Trap 4: Ordered vs Unordered
```
For cards: AB and BA may be same selection but different arrangements
```

### Trap 5: Conditional Changes Sample Space
```
P(A|B) means B has happened, new sample space is B
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Basic probability | P(E) = n(E)/n(S) |
| Complement | P(E') = 1 - P(E) |
| Addition | P(A∪B) = P(A) + P(B) - P(A∩B) |
| Multiplication | P(A∩B) = P(A) × P(B\|A) |
| Independent | P(A∩B) = P(A) × P(B) |
| Conditional | P(A\|B) = P(A∩B)/P(B) |
| Bayes | P(A\|B) = P(B\|A)P(A)/P(B) |
| Binomial P(X=k) | ⁿCₖpᵏ(1-p)ⁿ⁻ᵏ |
| Expected value | Σ xᵢP(xᵢ) |
| Variance | E(X²) - [E(X)]² |

---

## 📝 GATE-Level Practice

**Q1**: A bag has 5 red, 3 blue balls. Two drawn without replacement. P(both red)?
```
P = (5/8) × (4/7) = 20/56 = 5/14
```

**Q2**: P(sum = 9 when two dice thrown)?
```
Favorable: (3,6), (4,5), (5,4), (6,3) = 4 ways
P = 4/36 = 1/9
```

**Q3**: A coin is tossed 4 times. P(exactly 2 heads)?
```
P = ⁴C₂ × (1/2)² × (1/2)² = 6 × 1/16 = 6/16 = 3/8
```

**Q4**: Box A: 3 white, 2 black. Box B: 2 white, 3 black. Box chosen randomly, then ball drawn. P(white)?
```
P = P(A)P(W|A) + P(B)P(W|B)
  = (1/2)(3/5) + (1/2)(2/5)
  = 3/10 + 2/10 = 1/2
```

**Q5**: If P(A) = 0.4, P(B) = 0.3, P(A∩B) = 0.12. Are A and B independent?
```
If independent: P(A∩B) = P(A)P(B) = 0.4 × 0.3 = 0.12
Yes, they are independent.
```

**Q6**: Expected value when a die is rolled?
```
E(X) = (1+2+3+4+5+6)/6 = 21/6 = 3.5
```

---

*← [Chapter 16 - Permutations & Combinations](./16_Permutations_Combinations.md) | [Chapter 18 - Statistics →](./18_Statistics.md)*
