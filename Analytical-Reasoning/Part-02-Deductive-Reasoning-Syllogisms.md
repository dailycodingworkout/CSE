# Part 2: Deductive Reasoning & Syllogisms

## The Singularity

**The Atomic Truth:** *Syllogism is intersection logic of categorical sets.*

---

## 2.1 Understanding Syllogisms

### What is a Syllogism?

A syllogism is a logical argument where a conclusion is inferred from two premises.

**Structure:**
```
Premise 1 (Major): All M are P
Premise 2 (Minor): All S are M
─────────────────────────────
Conclusion:        All S are P
```

**The Three Terms:**
- **Major Term (P):** Predicate of the conclusion
- **Minor Term (S):** Subject of the conclusion  
- **Middle Term (M):** Appears in both premises but NOT in conclusion

---

## 2.2 The Four Standard Forms

### Form A: Universal Affirmative
**Statement:** "All S are P"

**Venn Representation:**
```
      ┌─────────────────┐
      │        P        │
      │    ┌───────┐    │
      │    │   S   │    │
      │    └───────┘    │
      └─────────────────┘
      
S is completely inside P
```

**Examples:**
- All cats are animals
- All squares are rectangles
- All prime numbers greater than 2 are odd

### Form E: Universal Negative
**Statement:** "No S are P"

**Venn Representation:**
```
    ┌───────┐     ┌───────┐
    │   S   │     │   P   │
    │       │     │       │
    └───────┘     └───────┘
    
S and P are completely separate
```

**Examples:**
- No mammals are reptiles
- No even prime is greater than 2
- No parallel lines intersect

### Form I: Particular Affirmative
**Statement:** "Some S are P"

**Venn Representation:**
```
    ┌───────────────────┐
    │   S     ╔═══╗     │
    │         ║ ∩ ║   P │
    │         ╚═══╝     │
    └───────────────────┘
    
At least one element in the intersection
```

**Examples:**
- Some students are toppers
- Some integers are even
- Some rectangles are squares

### Form O: Particular Negative
**Statement:** "Some S are not P"

**Venn Representation:**
```
    ┌───────┐     ┌───────┐
    │ S ████│     │   P   │
    │   ████│     │       │
    └───────┘     └───────┘
    
Some part of S is outside P (shaded region)
```

**Examples:**
- Some animals are not mammals
- Some numbers are not prime
- Some students are not engineers

---

## 2.3 The Distribution Rules

### What is Distribution?

A term is **distributed** if the statement tells us something about **every member** of that class.

### Distribution Table

| Statement Type | Subject | Predicate |
|---------------|---------|-----------|
| A: All S are P | Distributed ✓ | Not Distributed ✗ |
| E: No S are P | Distributed ✓ | Distributed ✓ |
| I: Some S are P | Not Distributed ✗ | Not Distributed ✗ |
| O: Some S are not P | Not Distributed ✗ | Distributed ✓ |

### Memory Trick: "ASEP"
```
A - Subject distributed
S - (same as A)
E - Both distributed
P - Predicate distributed (O type)

Or simply: "All Subjects are distributed, Negative Predicates are distributed"
```

### Why Distribution Matters

**Rule 1:** The middle term must be distributed at least once.

**Example of Violation:**
```
Premise 1: All cats are animals       (M=animals, not distributed)
Premise 2: All dogs are animals       (M=animals, not distributed)
Conclusion: All cats are dogs         ❌ INVALID
```
The middle term "animals" is the predicate in both A-type statements, never distributed.

**Rule 2:** If a term is distributed in the conclusion, it must be distributed in a premise.

---

## 2.4 Valid Syllogism Forms (Figures)

### The Four Figures

**Figure 1:**
```
M ─ P
S ─ M
∴ S ─ P
```

**Figure 2:**
```
P ─ M
S ─ M
∴ S ─ P
```

**Figure 3:**
```
M ─ P
M ─ S
∴ S ─ P
```

**Figure 4:**
```
P ─ M
M ─ S
∴ S ─ P
```

### Valid Moods by Figure

| Figure | Valid Moods |
|--------|-------------|
| 1 | AAA, EAE, AII, EIO |
| 2 | EAE, AEE, EIO, AOO |
| 3 | IAI, AII, OAO, EIO |
| 4 | AEE, IAI, EIO |

### Mnemonic for Valid Moods

**"Barbara, Celarent, Darii, Ferio" (Figure 1)**
- Barbara = AAA
- Celarent = EAE
- Darii = AII
- Ferio = EIO

---

## 2.5 Quick Validation Techniques

### Technique 1: The Venn Diagram Method

**Step-by-Step:**
1. Draw three overlapping circles for S, M, P
2. Shade out regions that CANNOT have elements (from E and O statements)
3. Mark regions that MUST have elements (from I and A statements using ×)
4. Check if conclusion follows necessarily

**Example:**
```
Premise 1: All M are P
Premise 2: Some S are M
Conclusion: Some S are P

Step 1: Draw circles
           P
        ╭─────╮
       ╱       ╲
      │    M    │
      │  ╭───╮  │
  S ──┼──│   │──┼──
      │  ╰───╯  │
       ╲       ╱
        ╰─────╯

Step 2: "All M are P" - shade M outside P (none exists)
Step 3: "Some S are M" - place × in S∩M region
Step 4: Since M is entirely in P, the × is also in P
        Therefore, Some S are P ✓ VALID
```

### Technique 2: The Rule-Based Method

**Five Rules for Validity:**

| Rule | Statement | Violation Result |
|------|-----------|------------------|
| 1 | Middle term distributed at least once | Fallacy of Undistributed Middle |
| 2 | Term distributed in conclusion must be distributed in premise | Illicit Major/Minor |
| 3 | Two negative premises yield no valid conclusion | Fallacy of Exclusive Premises |
| 4 | Negative premise requires negative conclusion | Fallacy of Drawing Affirmative |
| 5 | Two particular premises yield no valid conclusion | Fallacy of Particular Premises |

### Technique 3: The Counter-Example Method

**When to Use:** For MCQs where you need to quickly invalidate options.

**Method:**
1. Construct a scenario where premises are TRUE but conclusion is FALSE
2. If such scenario exists, the syllogism is INVALID

**Example:**
```
Premise 1: All dogs are animals
Premise 2: All cats are animals
Conclusion: All dogs are cats

Counter-Example:
- Let dogs = {Buddy, Max}
- Let cats = {Whiskers, Mittens}
- Let animals = {Buddy, Max, Whiskers, Mittens}
- Premises are TRUE, but conclusion is FALSE
- Therefore, INVALID ✓
```

---

## 2.6 Immediate Inferences

### Conversion

**Process:** Interchange subject and predicate.

| Original | Conversion | Validity |
|----------|------------|----------|
| A: All S are P | I: Some P are S | Valid ✓ |
| E: No S are P | E: No P are S | Valid ✓ |
| I: Some S are P | I: Some P are S | Valid ✓ |
| O: Some S are not P | (No valid conversion) | Invalid ✗ |

**GATE Trap:** A cannot convert to A!
- "All cats are animals" ✓
- "All animals are cats" ❌

### Obversion

**Process:** Change quality (affirmative ↔ negative) and negate predicate.

| Original | Obversion | Validity |
|----------|-----------|----------|
| A: All S are P | E: No S are non-P | Valid ✓ |
| E: No S are P | A: All S are non-P | Valid ✓ |
| I: Some S are P | O: Some S are not non-P | Valid ✓ |
| O: Some S are not P | I: Some S are non-P | Valid ✓ |

### Contraposition

**Process:** Replace subject with negation of predicate and predicate with negation of subject.

| Original | Contraposition | Validity |
|----------|----------------|----------|
| A: All S are P | A: All non-P are non-S | Valid ✓ |
| E: No S are P | (Partially valid) | Partial |
| I: Some S are P | (No valid contraposition) | Invalid ✗ |
| O: Some S are not P | O: Some non-P are not non-S | Valid ✓ |

---

## 2.7 Syllogism with "Only"

### Understanding "Only" Statements

**"Only S are P"** is equivalent to **"All P are S"**

**Why?**
```
"Only engineers can apply" 
= "Only engineers are eligible applicants"
= "All eligible applicants are engineers"
= "If you are an eligible applicant, you are an engineer"
```

### Common Transformations

| Original Statement | Equivalent Form |
|-------------------|-----------------|
| Only S are P | All P are S |
| S is the only P | All P are S |
| None but S are P | All P are S |
| S alone is P | All P are S |
| None except S are P | All P are S |

### GATE Trap Example

**Problem:**
- Premise 1: Only graduates are selected
- Premise 2: Some engineers are selected
- Conclusion: ?

**Transformation:**
- Premise 1: All selected are graduates
- Premise 2: Some engineers are selected

**Valid Conclusion:** Some engineers are graduates ✓

---

## 2.8 Syllogism with "If-Then"

### Conditional Statements in Syllogisms

**"If P, then Q"** is equivalent to **"All P are Q"**

### Chain Reasoning (Hypothetical Syllogism)

```
Premise 1: If A then B
Premise 2: If B then C
Conclusion: If A then C ✓ VALID
```

### Modus Ponens

```
Premise 1: If P then Q
Premise 2: P is true
Conclusion: Q is true ✓ VALID
```

### Modus Tollens

```
Premise 1: If P then Q
Premise 2: Q is false
Conclusion: P is false ✓ VALID
```

### Invalid Forms (Fallacies)

**Affirming the Consequent:**
```
Premise 1: If P then Q
Premise 2: Q is true
Conclusion: P is true ❌ INVALID
```

**Denying the Antecedent:**
```
Premise 1: If P then Q
Premise 2: P is false
Conclusion: Q is false ❌ INVALID
```

---

## 2.9 Complex Syllogism Structures

### Sorites (Chain Syllogisms)

**Structure:**
```
All A are B
All B are C
All C are D
All D are E
∴ All A are E ✓
```

**Solving Strategy:**
1. Connect the chain: A → B → C → D → E
2. Conclusion links first subject to last predicate
3. Valid if all links are in same direction

### Disjunctive Syllogism

```
Premise 1: Either P or Q (inclusive or exclusive)
Premise 2: Not P
Conclusion: Q ✓ VALID
```

**GATE Application:**
```
Either the code has a bug OR the input is invalid.
The input is valid.
∴ The code has a bug.
```

---

## 2.10 GATE-Specific Problem Patterns

### Pattern 1: "Some" to "Some not" Inference

**Common Trap:**
- "Some S are P" does NOT imply "Some S are not P"
- The sets might be identical!

**Example:**
- "Some prime numbers are odd" ✓
- Does this mean "Some prime numbers are not odd"?
- Answer: We CANNOT conclude this (only 2 is even prime, but we can't infer from the first statement alone)

### Pattern 2: Double Negation

**Statement:** "It is not true that no S are P"
**Equivalent:** "Some S are P"

**Logic:** ¬(¬∃) = ∃

### Pattern 3: Complementary Conclusions

When asked "Which conclusion follows?", check for:
1. Direct inference
2. Contrapositive
3. Combined premises

### Pattern 4: Multiple Conclusions

**Strategy:**
1. Test each conclusion independently
2. Both "Some A are B" and "Some B are A" can be simultaneously true
3. Use elimination for MCQs

---

## 2.11 Advanced: Syllogisms with Numbers

### Quantified Premises

**Example:**
- Premise 1: At least 60% of students are graduates
- Premise 2: At least 60% of students are employed
- Conclusion: At least 20% of students are employed graduates

**Logic:**
```
Let total students = 100
Graduates ≥ 60
Employed ≥ 60
Non-graduates ≤ 40
Non-employed ≤ 40

Minimum overlap = 60 + 60 - 100 = 20
Therefore, at least 20 are both ✓
```

### The Overlap Formula

$$\text{Minimum}(A \cap B) = \max(0, |A| + |B| - |U|)$$

Where $|U|$ is the universal set size.

---

## 2.12 Practice Problems

### Problem 1: Basic Syllogism
**Premises:**
- All roses are flowers
- All flowers are plants

**Which conclusions are valid?**
- (A) All roses are plants
- (B) Some plants are roses
- (C) All plants are flowers
- (D) Some flowers are roses

**Solution:**
```
roses → flowers → plants

(A) All roses are plants → Following the chain ✓ VALID
(B) Some plants are roses → Conversion of (A) ✓ VALID
(C) All plants are flowers → Converse of premise 2 ❌ INVALID
(D) Some flowers are roses → Conversion of premise 1 ✓ VALID

Answer: A, B, D
```

### Problem 2: Negative Premises
**Premises:**
- No fish are mammals
- Some aquatic animals are fish

**Conclusion:**
**Solution:**
```
No fish are mammals (E-type)
Some aquatic animals are fish (I-type)

Middle term: fish (distributed in E-type)
Valid conclusion must be negative (Rule 4)

From "Some aquatic animals are fish" and "No fish are mammals":
Some aquatic animals are not mammals ✓ VALID
```

### Problem 3: "Only" Statement
**Premises:**
- Only winners receive medals
- Some athletes are winners

**What follows?**
**Solution:**
```
Transform: All who receive medals are winners
Some athletes are winners

Chain: Some athletes are winners, All medal-receivers are winners
This doesn't give direct chain.

But: Some athletes are winners ∩ All medal-receivers ⊆ winners
We can conclude: Some athletes might receive medals (but not necessarily)

Actually: The conclusion "Some athletes may receive medals" is possible but not necessary.
From given premises, we can ONLY say: Some athletes are winners ✓
```

### Problem 4: Conditional Chain
**Premises:**
- If it rains, the match is cancelled
- If the match is cancelled, tickets are refunded
- Tickets were not refunded

**Conclusion?**
**Solution:**
```
Let R = rains, M = match cancelled, T = tickets refunded

R → M → T

Contrapositive chain: ¬T → ¬M → ¬R

Given: ¬T (tickets not refunded)
Conclusion: ¬R (it did not rain) ✓ VALID
```

### Problem 5: Numerical Syllogism
**Given:**
- In a class of 100 students:
- 75 students passed Mathematics
- 65 students passed Physics

**Minimum students who passed both?**
**Solution:**
$$\text{Minimum overlap} = 75 + 65 - 100 = 40$$

**Answer: 40 students**

---

## 2.13 Quick Reference Tables

### Statement Conversion Quick Reference

| Given | Can Conclude |
|-------|--------------|
| All S are P | Some P are S |
| No S are P | No P are S |
| Some S are P | Some P are S |
| Some S are not P | (Nothing definite about P) |

### Common Wrong Inferences

| From | CANNOT Conclude |
|------|-----------------|
| All S are P | All P are S |
| Some S are P | Some S are not P |
| Some S are not P | No S are P |
| No S are P | No P are S (this IS valid!) |

### The Validity Checklist

1. ☐ Is middle term distributed at least once?
2. ☐ Are terms distributed in conclusion also distributed in premises?
3. ☐ Are there two negative premises? (If yes, INVALID)
4. ☐ Is there a negative premise with affirmative conclusion? (If yes, INVALID)
5. ☐ Are there two particular premises? (If yes, INVALID)

---

## 2.14 Memory Palace for Syllogisms

### The Bizarre Mnemonic

**Visualize a courtroom:**
- The **JUDGE (Major Premise)** makes universal declarations
- The **LAWYER (Minor Premise)** argues specific cases
- The **VERDICT (Conclusion)** combines both

**For Distribution:**
- Picture **ASEP** as a security guard:
  - **A**ll **S**ubjects must show ID (distributed)
  - **E**veryone (both terms) shows ID
  - **P**redicate in **O** must show ID

### The Mental Slider

**Imagine a 3D Venn diagram you can manipulate:**
- **Slider 1:** Move set S left/right within P
- **Slider 2:** Adjust overlap between S and M
- **Slider 3:** Grow/shrink the middle term M

As you move sliders, watch how conclusions change!

---

## Navigation

[◀ Previous: Foundation](Part-01-Foundation-Mental-Models.md) | [Contents](README.md) | [Next: Analytical Puzzles ▶](Part-03-Analytical-Puzzles-Arrangements.md)
