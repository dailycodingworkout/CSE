# 🔗 Chapter 2: Logical Reasoning

## The Atomic Truth
> **"All logic reduces to: If P, then Q. Master the inference, master the exam."**

---

## 📋 Topics Covered

1. [Syllogisms](#1-syllogisms)
2. [Logical Deductions](#2-logical-deductions)
3. [Venn Diagrams](#3-venn-diagrams)
4. [Statements & Conclusions](#4-statements--conclusions)
5. [Statements & Assumptions](#5-statements--assumptions)
6. [Logical Connectives](#6-logical-connectives)
7. [Logical Puzzles](#7-logical-puzzles)

---

## 1. Syllogisms

### The Singularity
> **"Two premises, one conclusion. The middle term is the bridge."**

### The Root Architecture

A syllogism consists of:
- **Major Premise:** A general statement
- **Minor Premise:** A specific statement  
- **Conclusion:** Derived from both premises

$$\text{Major Premise} + \text{Minor Premise} \rightarrow \text{Conclusion}$$

---

### 🔑 The Four Categorical Propositions

| Type | Name | Form | Example | Symbol |
|------|------|------|---------|--------|
| A | Universal Affirmative | All S are P | All dogs are animals | $\forall x: S(x) \rightarrow P(x)$ |
| E | Universal Negative | No S are P | No cats are dogs | $\forall x: S(x) \rightarrow \neg P(x)$ |
| I | Particular Affirmative | Some S are P | Some birds can fly | $\exists x: S(x) \land P(x)$ |
| O | Particular Negative | Some S are not P | Some animals are not mammals | $\exists x: S(x) \land \neg P(x)$ |

---

### 🎨 Venn Diagram Representation

#### Type A: All S are P
```
    ┌─────────────────────────┐
    │           P             │
    │    ┌───────────┐        │
    │    │     S     │        │
    │    │  (shaded) │        │
    │    └───────────┘        │
    └─────────────────────────┘
```
S is completely inside P.

#### Type E: No S are P
```
    ┌──────────┐    ┌──────────┐
    │    S     │    │     P    │
    │          │    │          │
    └──────────┘    └──────────┘
```
S and P are disjoint (no overlap).

#### Type I: Some S are P
```
    ┌──────────────────────┐
    │    S    ┌────────────┼──────┐
    │         │  ★ (some)  │      │
    │         │            │   P  │
    └─────────┼────────────┘      │
              └───────────────────┘
```
S and P overlap (★ represents "some").

#### Type O: Some S are not P
```
    ┌──────────────────────┐
    │  ★ S    ┌────────────┼──────┐
    │(some not│            │      │
    │   in P) │            │   P  │
    └─────────┼────────────┘      │
              └───────────────────┘
```
Part of S exists outside P.

---

### 🔑 The Syllogistic Rules (The Iron Laws)

#### Rule 1: Distribution Rule
A term is **distributed** if the statement refers to ALL members of that term.

| Proposition | Subject | Predicate |
|-------------|---------|-----------|
| A (All S are P) | Distributed | Not Distributed |
| E (No S are P) | Distributed | Distributed |
| I (Some S are P) | Not Distributed | Not Distributed |
| O (Some S are not P) | Not Distributed | Distributed |

#### Rule 2: Middle Term Rule
The **middle term** must be distributed at least once in the premises.

#### Rule 3: Negative Premise Rule
- If one premise is negative, conclusion must be negative
- If both premises are negative, no valid conclusion

#### Rule 4: Particular Premise Rule
- If one premise is particular, conclusion must be particular
- If both premises are particular, no definite conclusion

---

### 🎯 The Syllogism Solving Algorithm

```
Step 1: Identify all propositions (A, E, I, O)
Step 2: Draw Venn diagrams for ALL possible interpretations
Step 3: Check what DEFINITELY follows (true in ALL diagrams)
Step 4: Apply conversion and complement rules if needed
Step 5: Eliminate options that are only SOMETIMES true
```

### 🛠️ Detailed Solving Techniques for Syllogisms

#### Technique 1: The 3-Circle Venn Diagram Method
**When:** Standard syllogism with two premises

```
Step 1: Draw three overlapping circles for all terms
Step 2: Shade regions that CANNOT contain elements
Step 3: Place ★ in regions that MUST contain at least one element
Step 4: Check if conclusion is true in ALL valid regions

Example:
Premises: All A are B. Some B are C.
- Shade A outside B (no A exists outside B)
- Place ★ in B∩C overlap (some B are C)
- Conclusion "Some A are C"? → ★ might be in B-only, not A∩C → NOT VALID
```

#### Technique 2: The Rule-Based Quick Check
**When:** Need fast verification without drawing

```
Quick Rules:
1. A + A → A (valid) | Example: All A are B + All B are C → All A are C ✓
2. A + E → E (valid) | Example: All A are B + No B are C → No A are C ✓
3. E + A → O* (valid) | Some C are not A (with proper order)
4. I + A → I (valid) | Example: Some A are B + All B are C → Some A are C ✓
5. E + E → Invalid (no definite conclusion)
6. I + I → Invalid (no definite conclusion)

Apply: Check if your conclusion matches the expected output type.
```

#### Technique 3: The Possibility Check
**When:** Question asks "Can this conclusion be true?"

```
Step 1: A conclusion "can be true" if at least ONE valid diagram supports it
Step 2: Unlike definite conclusions, possibilities need only one valid case
Step 3: Draw the MOST INCLUSIVE interpretation first

Example:
Premise: Some A are B.
Can "All A are B" be true? 
→ Yes! "Some" means "at least one" which includes "all"
```

#### Technique 4: The Complementary Pair Method
**When:** Two conclusions are complementary (one must be true)

```
Complementary pairs:
- "All A are B" and "Some A are not B" → One must be true
- "No A are B" and "Some A are B" → One must be true

If neither conclusion follows individually, check if they form a complementary pair.
Then at least one of them follows.
```

---

### 📐 Conversion Rules

| Original | Conversion | Valid? |
|----------|------------|--------|
| All S are P | Some P are S | ✅ Yes |
| No S are P | No P are S | ✅ Yes |
| Some S are P | Some P are S | ✅ Yes |
| Some S are not P | Some P are not S | ❌ No |

**The Golden Rule:** You cannot convert an O-type proposition!

---

### ⚠️ The Genius Trap

**Trap 1: Assuming the Converse**
```
Premise: All engineers are smart.
Wrong conclusion: All smart people are engineers.
Correct inference: Some smart people are engineers.
```

**Trap 2: Ignoring "Some" means "At least one"**
```
Premise: Some A are B.
This means: At least one A is B (could be all).
```

**Trap 3: Double Negative Confusion**
```
Premises: No A are B. No B are C.
Wrong: No A are C.
Truth: No valid conclusion (A and C relationship is undefined).
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
Premises:
1. All roses are flowers.
2. Some flowers are red.

Conclusions:
I. Some roses are red.
II. Some red things are roses.

Which conclusion(s) follow?
(A) Only I  (B) Only II  (C) Both I and II  (D) Neither I nor II
```

**Solution:**
- Draw Venn diagram with Roses ⊂ Flowers, and Red overlapping Flowers
- The overlap between Flowers and Red need NOT include Roses
- Neither conclusion definitely follows
- **Answer: (D) Neither I nor II**

**Problem 2:** (GATE 2022 Pattern)
```
Premises:
1. All managers are employees.
2. All employees are hardworking.

Conclusions:
I. All managers are hardworking.
II. Some hardworking people are managers.

(A) Only I  (B) Only II  (C) Both  (D) Neither
```

**Solution:**
- Managers ⊂ Employees ⊂ Hardworking
- Conclusion I: Managers ⊂ Hardworking ✅ (transitive)
- Conclusion II: Some hardworking = Managers ✅ (valid conversion of A-type)
- **Answer: (C) Both**

---

## 2. Logical Deductions

### The Singularity
> **"Chain the implications; break one link, break the chain."**

### The Root Architecture

Logical deductions use **propositional logic** rules:

| Rule | Symbolic Form | Name |
|------|--------------|------|
| If P then Q; P is true | $P \rightarrow Q, P \vdash Q$ | Modus Ponens |
| If P then Q; Q is false | $P \rightarrow Q, \neg Q \vdash \neg P$ | Modus Tollens |
| If P then Q; If Q then R | $P \rightarrow Q, Q \rightarrow R \vdash P \rightarrow R$ | Hypothetical Syllogism |
| P or Q; P is false | $P \lor Q, \neg P \vdash Q$ | Disjunctive Syllogism |

---

### 🔑 The Truth Table Foundation

| $P$ | $Q$ | $P \land Q$ | $P \lor Q$ | $P \rightarrow Q$ | $P \leftrightarrow Q$ |
|-----|-----|-------------|------------|-------------------|----------------------|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | F | T | T | F |
| F | F | F | F | T | T |

**Critical Insight:** $P \rightarrow Q$ is FALSE **only** when P is TRUE and Q is FALSE.

---

### ⚠️ The Genius Trap

**Trap: Affirming the Consequent**
```
Given: If it rains, the ground is wet.
Observation: The ground is wet.
Wrong conclusion: It rained.
Truth: The ground could be wet for other reasons!
```

**Trap: Denying the Antecedent**
```
Given: If you study, you pass.
Observation: You didn't study.
Wrong conclusion: You won't pass.
Truth: You might still pass!
```

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
Statement: If a student works hard, he will pass.
Given: The student did not pass.
What can we conclude?

(A) The student worked hard
(B) The student did not work hard
(C) Nothing can be concluded
(D) The student will work hard next time
```

**Solution:**
- Let P = works hard, Q = pass
- Given: $P \rightarrow Q$ and $\neg Q$
- By Modus Tollens: $\neg P$
- **Answer: (B) The student did not work hard**

---

## 3. Venn Diagrams

### The Singularity
> **"Venn diagrams make abstract logic visual and verifiable."**

### 🔑 The Three-Circle Master Template

```
                    ┌───────────────────────────────────────┐
                    │                                       │
                    │       ┌───────────────┐               │
                    │       │       A       │               │
                    │       │   ┌───────┐   │               │
                    │   ┌───┼───┤  ABC  ├───┼───┐           │
                    │   │   │   └───────┘   │   │           │
                    │   │ B │      AB       │ C │           │
                    │   │   │               │   │           │
                    │   │   └───────┬───────┘   │           │
                    │   │      BC   │    AC     │           │
                    │   └───────────┴───────────┘           │
                    │                                       │
                    │               Universal Set (U)       │
                    └───────────────────────────────────────┘
```

### Region Formulas

For three sets A, B, C:

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

**Only A (exclusively):**
$$|A \text{ only}| = |A| - |A \cap B| - |A \cap C| + |A \cap B \cap C|$$

---

### 📝 Practice Problems

**Problem 1:** (GATE 2019)
```
In a class of 120 students:
- 50 study Mathematics
- 40 study Physics  
- 30 study Chemistry
- 15 study both Mathematics and Physics
- 10 study both Physics and Chemistry
- 5 study both Mathematics and Chemistry
- 3 study all three subjects

How many students study none of these subjects?
```

**Solution:**
Using inclusion-exclusion:
$$|M \cup P \cup C| = 50 + 40 + 30 - 15 - 10 - 5 + 3 = 93$$

Students studying none = $120 - 93 = \mathbf{27}$

---

## 4. Statements & Conclusions

### The Singularity
> **"A conclusion follows only if it is NECESSARILY true, not possibly true."**

### The Root Architecture

Given statements, determine which conclusions **definitely** follow.

### 🔑 The Three-Level Test

| Level | Question | If Answer is NO |
|-------|----------|-----------------|
| 1 | Is the conclusion grammatically derived from premises? | Doesn't follow |
| 2 | Does the conclusion require external knowledge? | Doesn't follow |
| 3 | Is the conclusion true in ALL interpretations of premises? | Doesn't follow |

---

### ⚠️ The Genius Trap

**Trap: Using Real-World Knowledge**
```
Statement: Birds can fly.
Conclusion: Penguins can fly.

Wrong reasoning: Penguins are birds, so they fly.
Correct: We cannot conclude this from the given statement alone.
(The statement doesn't say ALL birds can fly)
```

---

## 5. Statements & Assumptions

### The Singularity
> **"An assumption is what the statement takes for granted without saying."**

### The Root Architecture

An **assumption** is an unstated premise that MUST be true for the statement/argument to be valid.

### 🔑 The Assumption Test

**The Negation Test:** If negating the assumption destroys the argument, it IS an assumption.

```
Statement: "Buy our product for guaranteed weight loss."

Potential Assumption: The product is safe.

Negation Test: "The product is NOT safe."
→ This destroys the argument (no one would buy unsafe products)
→ Therefore, safety IS an assumption ✅
```

---

### 📝 Practice Problems

**Problem 1:**
```
Statement: "The government should increase taxes to fund healthcare."

Assumptions:
I. The government has the authority to increase taxes.
II. Increased taxes will definitely improve healthcare.
III. Healthcare needs more funding.

Which assumptions are implicit?
```

**Solution:**
- I: Without authority, statement is meaningless → Implicit ✅
- II: "Definitely improve" is too strong; the statement only says "fund" → Not implicit ❌
- III: If healthcare didn't need funding, why suggest this? → Implicit ✅

**Answer: I and III only**

---

## 6. Logical Connectives

### The Singularity
> **"AND, OR, NOT, IF-THEN are the DNA of all reasoning."**

### 🔑 The Connective Truth Tables

#### Negation (NOT)
$$\neg P = \text{opposite of } P$$

| $P$ | $\neg P$ |
|-----|----------|
| T | F |
| F | T |

#### Conjunction (AND)
$$P \land Q = \text{true only when BOTH are true}$$

#### Disjunction (OR)
$$P \lor Q = \text{true when AT LEAST ONE is true}$$

#### Implication (IF-THEN)
$$P \rightarrow Q \equiv \neg P \lor Q$$

**Key Insight:** "If P then Q" is equivalent to "Not P or Q"

#### Biconditional (IF AND ONLY IF)
$$P \leftrightarrow Q \equiv (P \rightarrow Q) \land (Q \rightarrow P)$$

---

### 🔑 Logical Equivalences (The Power Laws)

| Law | Expression | Equivalent |
|-----|------------|------------|
| De Morgan's 1 | $\neg(P \land Q)$ | $\neg P \lor \neg Q$ |
| De Morgan's 2 | $\neg(P \lor Q)$ | $\neg P \land \neg Q$ |
| Contrapositive | $P \rightarrow Q$ | $\neg Q \rightarrow \neg P$ |
| Double Negation | $\neg(\neg P)$ | $P$ |
| Distributive | $P \land (Q \lor R)$ | $(P \land Q) \lor (P \land R)$ |
| Distributive | $P \lor (Q \land R)$ | $(P \lor Q) \land (P \lor R)$ |

---

### 📝 Practice Problems

**Problem 1:** (GATE Pattern)
```
Which of the following is logically equivalent to: 
"If it rains, the match will be cancelled"?

(A) If the match is cancelled, it rained.
(B) If the match is not cancelled, it did not rain.
(C) If it does not rain, the match will not be cancelled.
(D) The match will be cancelled only if it rains.
```

**Solution:**
- Let R = rains, C = cancelled
- Given: $R \rightarrow C$
- (A) $C \rightarrow R$ - Converse (NOT equivalent)
- (B) $\neg C \rightarrow \neg R$ - Contrapositive (EQUIVALENT ✅)
- (C) $\neg R \rightarrow \neg C$ - Inverse (NOT equivalent)
- (D) $C \rightarrow R$ - Converse (NOT equivalent)

**Answer: (B)**

---

## 7. Logical Puzzles

### The Singularity
> **"Puzzles are constraint satisfaction problems. Find all constraints, satisfy them all."**

### 🔑 Types of Logical Puzzles

#### Type 1: Truth-Teller and Liar Puzzles

**Setup:** Some people always tell truth, some always lie.

**Strategy:**
1. Assume one person is telling truth
2. Check if all statements are consistent
3. If contradiction found, flip the assumption

**Example:**
```
A says: "B is a liar."
B says: "A and I are both truth-tellers."

Analysis:
- If A is truth-teller: B is liar → B's statement is false
  - B says both are truth-tellers → False means at least one is liar
  - Since B is liar, this is consistent ✅
- If A is liar: B is truth-teller → B says both are truth-tellers
  - But A is liar → Contradiction ❌

Answer: A tells truth, B lies.
```

#### Type 2: Ordering/Ranking Puzzles

**Strategy:**
1. Create a visual timeline or ranking
2. Place definite positions first
3. Use process of elimination

**Example:**
```
Five people A, B, C, D, E are ranked 1-5.
- A is ranked higher than B
- C is ranked just below D
- B is ranked 3rd

Analysis:
- B is 3rd (fixed)
- A > B means A is 1st or 2nd
- C is just below D means D-C are consecutive
- Positions: 1, 2, _, 4, 5 remaining for A, D, C, E
- If D=4, C=5; A can be 1 or 2
```

#### Type 3: Seating Arrangements
(Detailed in Analytical Reasoning chapter)

---

## 🧠 The Logic Master Mnemonic: "VALID"

- **V**erify the proposition types (A, E, I, O)
- **A**pply Venn diagrams for visual verification  
- **L**ook for distribution of terms
- **I**dentify the middle term
- **D**erive conclusions using rules only

---

## 📊 Quick Reference Card

### Immediate Inferences

| From | Can Derive | Cannot Derive |
|------|-----------|---------------|
| All A are B | Some B are A | All B are A |
| No A are B | No B are A | Some A are B |
| Some A are B | Some B are A | All A are B |
| Some A are not B | Nothing definite | Some B are not A |

### Logical Equivalence Quick Check

| Statement | Equivalent To |
|-----------|---------------|
| If P then Q | If not Q then not P |
| Not (P and Q) | (Not P) or (Not Q) |
| Not (P or Q) | (Not P) and (Not Q) |
| P unless Q | If not Q then P |
| P only if Q | If P then Q |

---

## 🎯 Mastery Checklist

- [ ] Can identify A, E, I, O propositions instantly
- [ ] Can draw Venn diagrams for any syllogism
- [ ] Know all distribution rules by heart
- [ ] Can apply Modus Ponens and Modus Tollens correctly
- [ ] Can identify all logical equivalences
- [ ] Can solve truth-teller puzzles in under 2 minutes
- [ ] Never confuse converse with contrapositive

---

## ⏱️ The 5-Second Snap-Check for Syllogisms

| Check | What to Verify |
|-------|---------------|
| ✅ Middle Term | Is it distributed at least once? |
| ✅ Negative Rules | Two negatives = no conclusion |
| ✅ Particular Rules | Two particulars = no definite conclusion |
| ✅ Conclusion Type | Matches premise constraints? |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

[← Back to Main Index](../README.md) | [Previous: Verbal Reasoning](../Verbal-Reasoning/README.md) | [Next: Non-Verbal Reasoning →](../Non-Verbal-Reasoning/README.md)
