# Part 3: Analytical Puzzles & Arrangements

## The Singularity

**The Atomic Truth:** *Puzzles are constraint propagation problems.*

---

## 3.1 Understanding Arrangement Problems

### What Are Arrangement Problems?

Arrangement problems require you to:
1. Place entities in specific positions
2. Satisfy multiple constraints simultaneously
3. Deduce valid configurations

### Types of Arrangements

| Type | Description | Visualization |
|------|-------------|---------------|
| Linear | Entities in a row | `A-B-C-D-E` |
| Circular | Entities in a circle | `  A-B  ` with wrap |
| Matrix/Grid | Rows and columns | 2D table |
| Comparative | Ranking/ordering | `A > B > C` |
| Grouping | Entities into groups | Sets/Teams |

---

## 3.2 Linear Arrangement

### The Position Line Model

```
Position:   1     2     3     4     5
            │     │     │     │     │
            ▼     ▼     ▼     ▼     ▼
           ─┴─────┴─────┴─────┴─────┴─
           Left                    Right
           (First)               (Last)
```

### Key Terminology

| Term | Meaning |
|------|---------|
| "A is to the left of B" | Position(A) < Position(B) |
| "A is immediately left of B" | Position(B) = Position(A) + 1 |
| "A and B are adjacent" | |Position(A) - Position(B)| = 1 |
| "A is at one end" | Position(A) = 1 or n |
| "A is in the middle" | Position(A) = (n+1)/2 for odd n |
| "A is 3 places from B" | |Position(A) - Position(B)| = 3 |

### Solving Strategy: The Anchor Method

**Step 1:** Find the "anchor" - the entity with most constraints
**Step 2:** Place the anchor and build around it
**Step 3:** Use elimination to fill remaining positions

### Worked Example

**Problem:** 
Five people A, B, C, D, E sit in a row.
- A is not at either end
- B is to the right of A
- C is at one of the ends
- D is not adjacent to A

**Solution:**

**Step 1: Identify constraints**
```
A: Position ∈ {2, 3, 4}
B: Position > Position(A)
C: Position ∈ {1, 5}
D: |Position(D) - Position(A)| ≠ 1
```

**Step 2: Case Analysis**

*Case 1: A is at position 2*
```
Position:  1    2    3    4    5
           ?    A    ?    ?    ?
           
B must be at 3, 4, or 5
D cannot be at 1 or 3 (adjacent to A)
D ∈ {4, 5}

If C is at 1:
Position:  1    2    3    4    5
           C    A    ?    ?    ?
D ∈ {4, 5}, B ∈ {3, 4, 5}
E fills remaining

Possible: C-A-B-D-E, C-A-B-E-D, C-A-E-B-D, C-A-E-D-B
```

*Continue for other cases...*

**Step 3: Validate each arrangement against ALL constraints**

### Speed Technique: The Elimination Grid

```
         Pos 1  Pos 2  Pos 3  Pos 4  Pos 5
    A      ✗      ?      ?      ?      ✗
    B      ?      ?      ?      ?      ?
    C      ?      ✗      ✗      ✗      ?
    D      ?      ?      ?      ?      ?
    E      ?      ?      ?      ?      ?
```

Fill ✗ for impossible, ✓ for definite, ? for possible.

---

## 3.3 Circular Arrangement

### The Circular Model

```
          ┌───┐
         A│   │B
          │ ○ │
         E│   │C
          └─D─┘
          
Clockwise: A → B → C → D → E → A
```

### Key Differences from Linear

| Aspect | Linear | Circular |
|--------|--------|----------|
| End positions | 2 ends | No ends |
| Total arrangements (n items) | n! | (n-1)! |
| Reference point | Position 1 | Fix one person |
| Neighbors | At most 2 | Exactly 2 |

### Important Insight

**In circular arrangements, one person is FIXED as reference.**

Why? Because rotations are considered identical.

```
A-B-C-D (fixing A)   is same as   B-C-D-A   and   C-D-A-B
```

### Solving Strategy

**Step 1:** Fix one entity as reference (usually the one with most constraints)
**Step 2:** Assign positions relative to fixed entity
**Step 3:** Use clockwise/counter-clockwise relationships

### Worked Example

**Problem:**
Six people P, Q, R, S, T, U sit around a circular table.
- P and Q are opposite to each other
- R is to the immediate right of P
- S is not adjacent to Q

**Solution:**

**Step 1: Fix P as reference**
```
Position:    1(P)   2    3    4    5    6
             
P fixed at 1
Q is opposite → Q at position 4 (for 6 people, opposite = position + 3)
```

**Step 2: Apply constraints**
```
R is immediately right of P → R at position 2

         P
      6     R
    5    ○    3
      Q     
         4
         
S is not adjacent to Q (positions 3 and 5)
S ∈ {5, 6} wait... 3 and 5 are adjacent to Q
S ∈ {1, 2, 6} but 1 is P, 2 is R
S = 6

Remaining: T, U at positions 3, 5
```

**Final Arrangement:**
```
         P
      S     R
    U/T  ○  T/U
      Q     
```

---

## 3.4 Matrix/Grid Arrangement

### The Grid Model

```
           Col 1    Col 2    Col 3
        ┌────────┬────────┬────────┐
Row 1   │  (1,1) │  (1,2) │  (1,3) │
        ├────────┼────────┼────────┤
Row 2   │  (2,1) │  (2,2) │  (2,3) │
        ├────────┼────────┼────────┤
Row 3   │  (3,1) │  (3,2) │  (3,3) │
        └────────┴────────┴────────┘
```

### Adjacency in Grids

**4-connectivity (orthogonal):**
```
        ┌───┐
        │ ↑ │
    ┌───┼───┼───┐
    │ ← │ X │ → │
    └───┼───┼───┘
        │ ↓ │
        └───┘
```

**8-connectivity (including diagonal):**
```
    ┌───┬───┬───┐
    │ ↖ │ ↑ │ ↗ │
    ├───┼───┼───┤
    │ ← │ X │ → │
    ├───┼───┼───┤
    │ ↙ │ ↓ │ ↘ │
    └───┴───┴───┘
```

### Common Constraint Types

| Constraint | Meaning |
|------------|---------|
| "A and B in same row" | row(A) = row(B) |
| "A and B in same column" | col(A) = col(B) |
| "A is directly above B" | col(A) = col(B), row(A) = row(B) - 1 |
| "A is diagonally adjacent to B" | |row(A)-row(B)| = 1 AND |col(A)-col(B)| = 1 |

---

## 3.5 Comparative/Ranking Problems

### The Comparison Chain

```
Tallest ─────────────────────────── Shortest
   A    >    B    >    C    >    D
   
or with positions:

Rank:     1        2        3        4
          A        B        C        D
        (Best)                    (Worst)
```

### Key Operators

| Statement | Mathematical Meaning |
|-----------|---------------------|
| "A is taller than B" | A > B |
| "A is not shorter than B" | A ≥ B |
| "A is as tall as B" | A = B |
| "A is shorter than B but taller than C" | B > A > C |
| "A is 3rd tallest" | Rank(A) = 3 |

### Solving Strategy

**Step 1:** Convert statements to inequality chains
**Step 2:** Merge chains where possible
**Step 3:** Determine relative positions

### Worked Example

**Problem:**
In a race:
- A finished before B
- C finished after D but before E
- B finished immediately after D
- A finished second

**Solution:**

**Step 1: Convert to inequalities (lower position = better)**
```
A < B (A before B)
D < C < E (C after D, before E)
B = D + 1 (B immediately after D)
A = 2
```

**Step 2: Build the chain**
```
A = 2
A < B → B > 2, so B ≥ 3
B = D + 1 → D = B - 1

If B = 3: D = 2, but A = 2 (conflict!)
If B = 4: D = 3
If B = 5: D = 4

Let's try B = 4, D = 3:
D < C < E → 3 < C < E
C > 3, so C ≥ 4, but B = 4
So C = 5, E = 6? But only 5 positions if 5 people.

Actually: C can be 4 if B ≠ 4 in that position
Wait, let's reconsider with 5 people.

Rank: 1  2  3  4  5
      ?  A  ?  ?  ?
      
A = 2 (given)
A < B → B ∈ {3, 4, 5}
B = D + 1 → D = B - 1

If B = 3: D = 2 (but A = 2) ✗
If B = 4: D = 3 → D at rank 3
If B = 5: D = 4 → D at rank 4

Case: B = 4, D = 3
D < C < E → C, E ∈ {4, 5} but B = 4
So C = 5, E after 5? Not possible with 5 people.

Case: B = 5, D = 4
D < C < E → 4 < C < E
C = 5, E = 6? No, only 5 ranks.

Hmm, we need more people or reconsider.

Let's assume 6 people with someone at rank 1:
Rank: 1  2  3  4  5  6
      ?  A  ?  ?  ?  ?

B = 4, D = 3: D < C < E with C, E > 3
C ∈ {5, 6}, E > C, so C = 5, E = 6
Remaining: F at position 1

Final: F(1) - A(2) - D(3) - B(4) - C(5) - E(6)
```

---

## 3.6 Grouping/Distribution Problems

### The Grouping Model

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Group 1   │  │   Group 2   │  │   Group 3   │
│             │  │             │  │             │
│  A, D, E    │  │    B, F     │  │    C, G     │
│             │  │             │  │             │
└─────────────┘  └─────────────┘  └─────────────┘
```

### Types of Grouping Constraints

| Constraint | Meaning |
|------------|---------|
| "A and B are in same group" | group(A) = group(B) |
| "A and B are in different groups" | group(A) ≠ group(B) |
| "Group 1 has exactly 3 members" | |Group 1| = 3 |
| "A is in Group 1 if B is in Group 2" | Conditional |

### Solving Strategy

**Step 1:** Identify fixed assignments first
**Step 2:** Build "must be together" and "cannot be together" lists
**Step 3:** Use constraint propagation

### The Constraint Graph

Visualize relationships:
```
    A ─────── B     (A and B together)
    │
    │╲
    │ ╲
    C   D ═══ E     (D and E cannot be together)
    
Solid line: Must be together
Double line: Cannot be together
```

---

## 3.7 Scheduling Problems

### The Timeline Model

```
Time:   9:00   10:00   11:00   12:00   13:00   14:00
         │       │       │       │       │       │
         ├───────┼───────┼───────┼───────┼───────┤
Slot 1   │  T1   │  T2   │  T3   │ Lunch │  T4   │
         └───────┴───────┴───────┴───────┴───────┘
```

### Common Scheduling Constraints

| Constraint | Meaning |
|------------|---------|
| "T1 before T2" | start(T1) < start(T2) |
| "T1 immediately before T2" | end(T1) = start(T2) |
| "T1 and T2 cannot overlap" | end(T1) ≤ start(T2) OR end(T2) ≤ start(T1) |
| "T1 takes 2 hours" | duration(T1) = 2 |
| "T1 must be in morning" | start(T1) < 12:00 |

### Solving Strategy

**Step 1:** Identify fixed time slots
**Step 2:** Apply duration constraints
**Step 3:** Use precedence constraints to order
**Step 4:** Check for conflicts

---

## 3.8 Common Trap Patterns

### Trap 1: Assuming Uniqueness

**Wrong Assumption:** There's only one valid arrangement.

**Reality:** Multiple arrangements may satisfy constraints.

**Solution:** The question asks "which MUST be true" vs "which COULD be true"

### Trap 2: Forgetting Transitivity

**Given:**
- A is to the left of B
- B is to the left of C

**Implicit:** A is to the left of C (transitivity!)

### Trap 3: Misinterpreting "Immediately"

- "A is left of B" → Any position to the left
- "A is immediately left of B" → Directly adjacent, no gap

### Trap 4: Circular vs Linear Confusion

**Trap:** Treating circular arrangement like linear.

**Key Difference:** In circular, the "last" position is adjacent to the "first."

### Trap 5: Inclusive vs Exclusive Counting

**"Between A and B there are 3 people"**
- Does NOT include A and B
- Total in segment: A + 3 + B = 5 positions

---

## 3.9 Speed Techniques

### Technique 1: The Anchor-and-Build

1. Find the most constrained entity
2. Fix it as anchor
3. Build outward

### Technique 2: The Contradiction Method

For "Must be True" questions:
1. Assume the statement is FALSE
2. Check if this leads to contradiction
3. If contradiction → Statement MUST be true

### Technique 3: The Quick Scan

For "Could be True" questions:
1. Find ONE valid arrangement where statement holds
2. Statement COULD be true

### Technique 4: The Slot Count

Before diving in:
1. Count entities: n
2. Count slots: m
3. If n > m: Some slot has multiple entities (or impossible)
4. If n < m: Some slots are empty

### Technique 5: Bipartite Matching

For assignment problems:
```
Entities:    A   B   C   D
             │╲ │╱  │   │
             │ ╳    │   │
             │╱ │╲  │   │
Positions:   1   2   3   4

Draw lines for valid assignments
Count to ensure feasibility
```

---

## 3.10 Practice Problems

### Problem 1: Linear Arrangement

**Seven people A, B, C, D, E, F, G sit in a row facing north.**
- C sits at one of the ends
- B sits third to the right of C
- A sits exactly in the middle
- D is not adjacent to B or C
- E sits to the immediate right of A
- F and G sit adjacent to each other

**Questions:**
1. Who sits at the other end?
2. Who sits between C and A?

**Solution:**
```
Positions: 1 - 2 - 3 - 4 - 5 - 6 - 7
Middle = 4, so A at 4
E is immediately right of A → E at 5

C at one end (1 or 7)
B is third to right of C

If C at 1: B at 4, but A at 4 ✗
If C at 7: B would be at 10 ✗ (out of range)

Wait, "third to the right" means:
C at position X, B at position X + 3

If C at 1: B at 1 + 3 = 4, but A at 4 ✗
If C at 7: No position 10

Hmm, let me reconsider. "Third to the right" might mean 3 positions to right.

Actually, if C is at position 7, and we're facing north, "right" might wrap?
No, in linear arrangement, no wrapping.

Let's try: C at 1, B at 4
But A must be at 4 (middle of 7 is position 4)
Conflict!

Alternative interpretation: C at end, B three positions from C
If C at 1, B at 4 conflicts with A.
If C at 7, B at 4 (7 - 3 = 4) conflicts with A.

There might be an error in the problem or my interpretation.

Let's assume the middle is calculated differently or constraints allow flexibility.

Alternative: If "middle" means one of {3, 4, 5} for 7 people...
If A at 3: C at 1, B at 4 → No conflict!

C - ? - A - B - E - ? - ?
   1   2   3   4   5   6   7
   C       A   B   E       

D is not adjacent to B or C
D ≠ position 2 (adjacent to C at 1)
D ≠ positions 3 or 5 (adjacent to B at 4)
D ∈ {6, 7}

F and G are adjacent: {6,7} or {2} with something else
Since D ∈ {6,7}, and F-G must be adjacent:
If D at 6: F-G at {2, 7}? But 2 and 7 not adjacent. So F at 2, G at 7 OR F at 7 but D at 6.
If D at 7: F-G at {2, 6} - not adjacent!

So D at 6, remaining {2, 7} for F-G
F-G must be adjacent, but 2 and 7 are not adjacent in linear!

Contradiction suggests my interpretation is wrong.

Let me re-read: Perhaps C at 7, B at 4 (third to the LEFT of C)?
"Third to the right" from C at position 7 makes no sense.

If problem means "third from the right of C" meaning 3 positions to left:
C at 7, B at 4 → conflict with A.

Or perhaps A being "exactly in the middle" for 7 people means position 4.

New try with A at 4, but B not at 4:
Can C be in a non-end position? No, problem says end.

This problem has contradictory constraints as stated. 
In exam, such problems sometimes have "None of these" as an option.
```

### Problem 2: Circular Arrangement

**Eight people P, Q, R, S, T, U, V, W sit around a circular table.**
- P and R are opposite each other
- Q sits second to the left of P
- S is not adjacent to P or R
- T sits to the immediate right of R

**Find all possible positions of S.**

**Solution:**
```
Fix P at position 1 (12 o'clock)
Opposite in 8-person circle: position 1 + 4 = 5
So R at position 5

Q is second to left of P:
Positions (clockwise): 1, 2, 3, 4, 5, 6, 7, 8
Left of 1 (counterclockwise): 8, 7, 6...
Second to left of 1: position 7
Q at position 7

T is immediately right of R:
R at 5, right of R (clockwise) is position 6
T at position 6

Current state:
Position:  1  2  3  4  5  6  7  8
Person:    P  ?  ?  ?  R  T  Q  ?

S not adjacent to P (positions 2, 8) or R (positions 4, 6)
S ≠ {2, 4, 6, 8}
S ∈ {3}  (positions 1, 5, 7 are taken)

So S at position 3.

Remaining U, V, W at positions 2, 4, 8.
```

**Answer:** S sits at position 3 (two seats clockwise from P).

### Problem 3: Grouping

**10 students are divided into 3 groups for a project.**
- Group A has at least 2 students
- Group B has exactly 3 students
- Group C has at most 4 students
- Student X and Y must be in same group
- Student Z cannot be in Group A
- Student W must be in Group C

**If X is in Group B, where can Y and Z be?**

**Solution:**
```
Constraints:
|A| ≥ 2
|B| = 3
|C| ≤ 4
Total: |A| + |B| + |C| = 10
So: |A| + |C| = 7, with |A| ≥ 2, |C| ≤ 4
Therefore: |A| ∈ {3, 4, 5}, |C| = 7 - |A|

X in B → Y in B (same group constraint)
B has exactly 3, so X, Y + 1 more person in B

Z not in A → Z in B or C
If Z in B: B has X, Y, Z = 3 ✓
If Z in C: Valid too

W in C (given)

If X is in Group B:
- Y must be in Group B (same group as X)
- Z can be in Group B or Group C
```

**Answer:** Y must be in Group B. Z can be in Group B or Group C.

---

## 3.11 Advanced: Constraint Propagation Algorithm

### The AC-3 Algorithm (Mental Version)

**Arc Consistency:** Every constraint between two variables should be satisfiable.

**Steps:**
1. Make a queue of all constraints
2. For each constraint, eliminate impossible values
3. If any domain becomes empty, no solution exists
4. If a domain is reduced, add related constraints back to queue
5. Repeat until queue is empty

### Example Application

```
Variables: A, B, C (positions 1, 2, 3)
Constraints: A < B, B ≠ 2, C = 3

Initial domains:
A: {1, 2, 3}
B: {1, 2, 3}
C: {1, 2, 3}

Step 1: C = 3 → C: {3}
        Update: A ≠ 3, B ≠ 3 (since C = 3)
        A: {1, 2}, B: {1, 2}

Step 2: B ≠ 2 → B: {1}

Step 3: A < B → A < 1 → A: {} 
        Empty domain! No solution.
```

---

## 3.12 Key Takeaways

### The 5-Second Snap-Check

Before finalizing:
1. ✓ Count: Right number of entities in right number of slots?
2. ✓ Constraints: All constraints satisfied?
3. ✓ Question: Did I answer what was asked?
4. ✓ Unique: Is this the only solution or are there alternatives?

### Memory Anchors

**For Linear Arrangement:**
> "Position is Power" - Fix the most constrained entity first.

**For Circular Arrangement:**
> "Fix One, Free the Rest" - One person is always the reference point.

**For Grouping:**
> "Together and Apart" - First map who must/cannot be together.

### The Mental Slider

**Imagine a sorting hat:**
- Each entity is a card
- Slots are positions in your hand
- Constraints are rules about which cards can be adjacent
- Slide cards around until all rules are satisfied

---

## Navigation

[◀ Previous: Syllogisms](Part-02-Deductive-Reasoning-Syllogisms.md) | [Contents](README.md) | [Next: Data Interpretation ▶](Part-04-Data-Interpretation-Logical-Analysis.md)
