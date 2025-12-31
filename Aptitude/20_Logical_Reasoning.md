# Chapter 20: Logical Reasoning

> **The art of valid inference - drawing correct conclusions from given information**

---

## 🎯 Why Study This?

- High-frequency topic in GATE/ESE aptitude
- Tests critical thinking and analytical skills
- Essential for programming logic and algorithms

---

## 📚 Part 1: Propositional Logic

### Basic Propositions

**Proposition**: A statement that is either TRUE (T) or FALSE (F)

**Examples**:
- "The sun rises in the east" (True proposition)
- "2 + 2 = 5" (False proposition)
- "Is it raining?" (NOT a proposition - it's a question)

---

### Logical Connectives

| Symbol | Name | Meaning | Example |
|--------|------|---------|---------|
| ¬ or ~ | Negation | NOT p | ¬p |
| ∧ | Conjunction | p AND q | p ∧ q |
| ∨ | Disjunction | p OR q | p ∨ q |
| → | Implication | If p then q | p → q |
| ↔ | Biconditional | p if and only if q | p ↔ q |
| ⊕ | XOR | Exclusive OR | p ⊕ q |

---

### Truth Tables

**Negation (¬p)**:
| p | ¬p |
|---|-----|
| T | F |
| F | T |

**Conjunction (p ∧ q)**:
| p | q | p ∧ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Disjunction (p ∨ q)**:
| p | q | p ∨ q |
|---|---|-------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**Implication (p → q)**:
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**💡 Key**: Implication is FALSE only when p is True and q is False

**Biconditional (p ↔ q)**:
| p | q | p ↔ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

---

### Important Equivalences

```
p → q ≡ ¬p ∨ q
¬(p → q) ≡ p ∧ ¬q
p ↔ q ≡ (p → q) ∧ (q → p)
p ⊕ q ≡ (p ∨ q) ∧ ¬(p ∧ q)
```

---

### De Morgan's Laws

```
¬(p ∧ q) ≡ ¬p ∨ ¬q
¬(p ∨ q) ≡ ¬p ∧ ¬q
```

---

### Implications and Their Forms

Given: p → q (If p then q)

| Form | Statement | Notation |
|------|-----------|----------|
| Original | If p then q | p → q |
| Converse | If q then p | q → p |
| Inverse | If not p then not q | ¬p → ¬q |
| Contrapositive | If not q then not p | ¬q → ¬p |

**Key**: Original ≡ Contrapositive, Converse ≡ Inverse

---

## 📚 Part 2: Syllogisms

### What is a Syllogism?

A logical argument with two premises and a conclusion.

**Standard Form**:
```
Premise 1: All A are B
Premise 2: All B are C
Conclusion: All A are C
```

---

### Types of Categorical Propositions

| Type | Form | Example |
|------|------|---------|
| A (Universal Affirmative) | All S are P | All dogs are mammals |
| E (Universal Negative) | No S are P | No reptiles are mammals |
| I (Particular Affirmative) | Some S are P | Some birds are pets |
| O (Particular Negative) | Some S are not P | Some students are not athletes |

---

### Rules for Valid Syllogisms

1. **Three terms only**: Major, Minor, Middle
2. **Middle term distributed at least once**
3. **Term distributed in conclusion must be distributed in premise**
4. **No negative conclusion from two affirmative premises**
5. **At least one premise must be universal if conclusion is universal**

---

### Common Valid Syllogism Patterns

**Pattern 1 (Barbara)**:
```
All M are P
All S are M
∴ All S are P
```

**Pattern 2 (Celarent)**:
```
No M are P
All S are M
∴ No S are P
```

**Pattern 3 (Darii)**:
```
All M are P
Some S are M
∴ Some S are P
```

---

### Venn Diagram Method for Syllogisms

1. Draw three overlapping circles for S, M, P
2. Shade out areas that don't exist (from E or O statements)
3. Mark areas that must have members (from I or A statements)
4. Check if conclusion is valid

---

## 📚 Part 3: Logical Reasoning Patterns

### Deductive Reasoning

From general to specific - conclusion follows necessarily.

```
Premise: All humans are mortal
Premise: Socrates is human
Conclusion: Socrates is mortal ✓
```

---

### Inductive Reasoning

From specific to general - conclusion is probable, not certain.

```
Observation: Swan 1 is white, Swan 2 is white, ...
Conclusion: All swans are white (probable, not certain)
```

---

### Modus Ponens (Affirming the Antecedent)

```
If P then Q
P is true
∴ Q is true
```

**Example**:
```
If it rains, the ground is wet
It is raining
∴ The ground is wet ✓
```

---

### Modus Tollens (Denying the Consequent)

```
If P then Q
Q is false
∴ P is false
```

**Example**:
```
If it rains, the ground is wet
The ground is not wet
∴ It is not raining ✓
```

---

### Fallacies (Invalid Reasoning)

**Affirming the Consequent** (Invalid!):
```
If P then Q
Q is true
∴ P is true ✗
```

**Denying the Antecedent** (Invalid!):
```
If P then Q
P is false
∴ Q is false ✗
```

---

## 📚 Part 4: Common Problem Types

### Blood Relations

**Key Relations**:
- Father/Mother → Parents
- Son/Daughter → Children
- Brother/Sister → Siblings
- Uncle/Aunt → Parent's siblings
- Nephew/Niece → Sibling's children
- Cousin → Uncle/Aunt's children

**Tip**: Draw a family tree diagram

---

### Direction Sense

**Standard Compass**:
```
         N
         |
    W ───┼─── E
         |
         S
```

**Tips**:
- Right turn clockwise, Left turn counter-clockwise
- Track cumulative direction changes
- Use coordinate system when helpful

---

### Coding-Decoding

**Types**:
1. **Letter substitution**: A→Z, B→Y (position 27 - original)
2. **Number coding**: A=1, B=2, or custom patterns
3. **Symbolic coding**: GATE→@#$%
4. **Mixed**: Combinations of above

**Approach**: Find the pattern from given examples, apply to solve.

---

### Seating Arrangement

**Linear**: People in a row/line
**Circular**: People around a table

**Tips**:
- Start with fixed positions
- Mark directions (left/right, clockwise/anticlockwise)
- Use elimination for complex problems

---

### Ranking/Order

**Key Relationships**:
```
If A > B and B > C, then A > C (transitivity)
Total = Above + 1 (person) + Below
```

---

### Puzzles

**Approach**:
1. List all variables and constraints
2. Create a grid/table if needed
3. Fill in definite information first
4. Use elimination and deduction
5. Verify final answer against all constraints

---

## 💡 Advanced Tricks

### Trick 1: Contrapositive for "If-Then"

Always check contrapositive when solving:
```
"If A then B" ≡ "If not B then not A"
```

---

### Trick 2: "Only" and "Unless"

```
"Only A can B" = "If B then A"
"A unless B" = "If not B then A" = "A or B"
```

---

### Trick 3: Blood Relation Shortcuts

```
Father's father = Grandfather
Mother's brother = Uncle
Sister's son = Nephew
```

---

### Trick 4: Direction Net Displacement

```
N = +y, S = -y, E = +x, W = -x
Calculate final (x, y) position
Distance = √(x² + y²)
```

---

## ⚠️ Edge Cases & Traps

### Trap 1: Some ≠ All
```
"Some A are B" doesn't mean "All A are B"
"Some" could be "few" or "all"
```

### Trap 2: Implication False Only in One Case
```
"If P then Q" is false ONLY when P=T and Q=F
All other combinations are TRUE
```

### Trap 3: Converse ≠ Original
```
"If A then B" ≠ "If B then A"
Don't assume converse is true
```

### Trap 4: Negation of "All"
```
Negation of "All A are B" is "Some A are not B" (NOT "No A are B")
```

### Trap 5: "Either...or" Ambiguity
```
In logic, "or" is typically inclusive
In everyday speech, may be exclusive
```

---

## 🚀 Formula Cheat Sheet

| Concept | Formula/Rule |
|---------|--------------|
| p → q | ≡ ¬p ∨ q |
| Contrapositive | p → q ≡ ¬q → ¬p |
| De Morgan | ¬(p ∧ q) ≡ ¬p ∨ ¬q |
| Modus Ponens | p, p→q ⊢ q |
| Modus Tollens | ¬q, p→q ⊢ ¬p |
| "Only if" | "A only if B" = A → B |
| "Unless" | "A unless B" = ¬B → A |
| Negation of "All A are B" | "Some A are not B" |

---

## 📝 GATE-Level Practice

**Q1**: If "All cats are animals" and "Some animals are pets", can we conclude "Some cats are pets"?
```
No! The middle term (animals) may not connect cats to pets.
The animals that are pets may not include cats.
```

**Q2**: If P → Q is true and Q is false, what can we conclude about P?
```
By Modus Tollens: P must be false
If P were true and Q false, P → Q would be false (contradiction)
```

**Q3**: A is B's son. C is A's sister. D is C's mother. What is D to B?
```
A is B's son → B is A's father or mother
C is A's sister → C is also B's child
D is C's mother → D is the mother of B's child
Therefore, D is B's wife (or D = B if B is the mother)
Most likely: D is B's wife
```

**Q4**: "Only if it rains, the match is cancelled" - Which is true if match is cancelled?
```
"Only if A, B" = "B only if A" = B → A
If match cancelled (B), then it rained (A)
So: It rained
```

**Q5**: What is the contrapositive of "If it is sunny, I will go to the beach"?
```
Original: Sunny → Beach
Contrapositive: ¬Beach → ¬Sunny
"If I don't go to the beach, it is not sunny"
```

---

*← [Chapter 19 - Set Theory & Venn Diagrams](./19_Set_Theory_Venn.md) | [Chapter 21 - Data Interpretation →](./21_Data_Interpretation.md)*
