# Chapter 11: Complexity Classes & NP-Completeness

## 11.1 Why This Matters

> **The Biggest Open Question in Computer Science:** Is **P = NP**? This $1 million Millennium Prize Problem asks whether every problem whose solution can be verified quickly can also be solved quickly.

Understanding complexity classes helps you:
1. Know when to stop searching for an efficient algorithm (the problem is hard!)
2. Recognize NP-Complete problems in exams and in practice
3. Use approximation or heuristic algorithms instead

---

## 11.2 Decision Problems

A **decision problem** is one with a yes/no answer. Every optimization problem can be converted to a decision version.

| Optimization | Decision Version |
|-------------|-----------------|
| Shortest path from s to t | Is there a path from s to t with length ≤ k? |
| Minimum vertex cover | Is there a vertex cover of size ≤ k? |
| Maximum clique | Is there a clique of size ≥ k? |

---

## 11.3 Complexity Classes — Definitions

### Class P (Polynomial Time)

**P** = Set of decision problems solvable by a **deterministic** Turing machine in **polynomial time** O(nᵏ) for some constant k.

**Examples in P:**
- Sorting (O(n log n))
- Shortest path (O(V² or (V+E)log V))
- MST (O(E log V))
- 2-SAT, 2-coloring
- Matching in bipartite graphs
- Linear programming

> **Intuition:** "Problems we can SOLVE efficiently."

### Class NP (Nondeterministic Polynomial Time)

**NP** = Set of decision problems where a YES answer can be **verified** by a deterministic Turing machine in polynomial time, given a **certificate** (witness/proof).

**Alternative definition:** Problems solvable by a **nondeterministic** Turing machine in polynomial time.

**Examples in NP:**
- All problems in P (trivially — if you can solve it, you can verify it)
- SAT, 3-SAT
- Hamiltonian cycle (certificate: the cycle itself — verify in O(V))
- Graph coloring (certificate: the coloring — verify in O(V+E))
- Subset sum (certificate: the subset — verify in O(n))
- Travelling Salesman (decision version)

> **Intuition:** "Problems where we can VERIFY a solution efficiently."

> **GATE Critical:** **P ⊆ NP** always holds. The open question is whether **P = NP** or **P ⊂ NP** (strict subset).

### Class co-NP

**co-NP** = Set of decision problems where a NO answer can be verified in polynomial time.

**Example:** "Is this number composite?" is in NP (certificate: a factor). "Is this number prime?" is in co-NP (and also in P — AKS primality test).

---

### Class NP-Hard

**NP-Hard** = A problem H is NP-Hard if every problem in NP can be **polynomial-time reduced** to H.

In other words: H is "at least as hard as" the hardest problems in NP.

> **NP-Hard problems are NOT necessarily in NP!** They could be even harder (undecidable, for example).

**Examples:** Halting problem (undecidable, NP-Hard but not in NP), TSP optimization version.

### Class NP-Complete

**NP-Complete** = NP ∩ NP-Hard

A problem L is NP-Complete if:
1. L ∈ NP (solutions can be verified in polynomial time)
2. L is NP-Hard (every NP problem reduces to L)

> **Intuition:** "The hardest problems in NP."

```
         ┌─────────────────────────┐
         │           NP-Hard       │
         │    ┌──────────────┐     │
         │    │  NP-Complete │     │
         │    │   ┌──────┐   │     │
         │    │   │  P   │   │     │
         │    │   └──────┘   │     │
         │    └──────────────┘     │
         │          NP             │
         └─────────────────────────┘
```

(Assuming P ≠ NP)

---

## 11.4 Polynomial-Time Reductions

**Definition:** Problem A reduces to problem B (written A ≤ₚ B) if there exists a polynomial-time function f such that:
- x is a YES instance of A ⟺ f(x) is a YES instance of B

**What this means:** If we can solve B, we can solve A (by transforming A's input to B's format).

**Key implication:** If A ≤ₚ B and A is NP-Hard → B is NP-Hard too!

> **Analogy:** "If I can't climb a 100m wall (A), and a 200m wall (B) is definitely not easier, then I can't climb B either."

**Direction of reduction (GATE TRAP):**

To prove X is NP-Complete:
1. Show X ∈ NP
2. Take a **known NP-Complete** problem Y
3. Show Y ≤ₚ X (reduce FROM the known hard problem TO the new problem)

> **Common mistake:** Students reduce in the wrong direction! Always reduce FROM the known NP-Complete problem TO the one you're trying to prove NP-Complete.

---

## 11.5 Cook's Theorem (SAT is NP-Complete) — The First NP-Complete Problem

**SAT (Boolean Satisfiability):** Given a Boolean formula, is there an assignment of variables that makes it TRUE?

**Cook-Levin Theorem (1971):** SAT is NP-Complete.

**Proof idea:** Any NP problem can be expressed as a polynomial-time verification by a Turing machine. The TM's computation can be encoded as a Boolean formula that is satisfiable iff the TM accepts.

> **Significance:** This was the FIRST problem proved NP-Complete. All subsequent proofs reduce from SAT (or from other known NP-Complete problems).

---

## 11.6 Famous NP-Complete Problems ⭐

| Problem | Description |
|---------|-------------|
| **SAT** | Is a Boolean formula satisfiable? |
| **3-SAT** | SAT with each clause having exactly 3 literals |
| **Vertex Cover** | Is there a vertex cover of size ≤ k? |
| **Independent Set** | Is there an independent set of size ≥ k? |
| **Clique** | Is there a clique of size ≥ k? |
| **Hamiltonian Cycle** | Does a Hamiltonian cycle exist? |
| **TSP (decision)** | Is there a tour of cost ≤ k? |
| **Subset Sum** | Is there a subset summing to T? |
| **Graph Coloring (≥3)** | Can the graph be colored with ≤ k colors (k≥3)? |
| **3D Matching** | Does a perfect 3D matching exist? |
| **Set Cover** | Can the universe be covered with ≤ k sets? |
| **Partition** | Can a set be split into two equal-sum subsets? |
| **0/1 Knapsack (decision)** | Is there a subset with weight ≤ W and value ≥ V? |

### Standard Reduction Chain

```
SAT → 3-SAT → Clique → Vertex Cover → Independent Set
                  ↓
            Hamiltonian Cycle → TSP
                  ↓
            Subset Sum → Partition → Knapsack
                  ↓
            3-Coloring → k-Coloring
```

---

## 11.7 Key Relationships for GATE

### Problems in P (polynomial time solvable)

| Problem | Time |
|---------|------|
| 2-SAT | O(V+E) |
| 2-Coloring (Bipartite check) | O(V+E) |
| Shortest Path | O(V² or (V+E)logV) |
| MST | O(E log V) |
| Maximum Bipartite Matching | O(V·E) |
| Euler Circuit | O(E) |
| Topological Sort | O(V+E) |

### NP-Complete (no known polynomial solution)

| Problem | NP-Complete? |
|---------|-------------|
| 3-SAT | ✅ |
| 2-SAT | ❌ (in P!) |
| 3-Coloring | ✅ |
| 2-Coloring | ❌ (in P!) |
| Hamiltonian Path | ✅ |
| Euler Path | ❌ (in P!) |
| 0/1 Knapsack | ✅ |
| Fractional Knapsack | ❌ (in P!) |

> **GATE Pattern:** Often "2 vs 3" determines complexity:
> - 2-SAT (P) vs 3-SAT (NPC)
> - 2-Coloring (P) vs 3-Coloring (NPC)
> - 2-Partition (P for some variants) vs 3-Partition (NPC)

---

## 11.8 Important Theorems for GATE

1. **If any NP-Complete problem has a polynomial-time algorithm, then P = NP**
2. **If P ≠ NP, no NP-Complete problem has a polynomial-time algorithm**
3. **Complement:** If L is NP-Complete and L's complement is in NP, and if P = NP, then NP = co-NP
4. **Vertex Cover + Independent Set + Clique:** These are related:
   - S is a vertex cover ⟺ V-S is an independent set
   - G has a clique of size k ⟺ complement graph G̅ has an independent set of size k

5. **Transitivity of reductions:** If A ≤ₚ B and B ≤ₚ C, then A ≤ₚ C

---

## 11.9 Pseudo-Polynomial and Approximation

### Pseudo-Polynomial Algorithms

Some NP-Complete problems have algorithms that are polynomial in the **numeric value** of input but exponential in the **size (bits)** of input.

**Example:** 0/1 Knapsack O(nW) — polynomial in n and W, but W could need log W bits to represent. If W = 2ⁿ, this is O(n·2ⁿ) = exponential.

> **GATE Fact:** Problems that are NP-Complete but have pseudo-polynomial algorithms are called **weakly NP-Complete** (e.g., Subset Sum, Knapsack, Partition).

> Problems that remain NP-Complete even with unary input are **strongly NP-Complete** (e.g., 3-SAT, 3-Coloring, TSP).

### Approximation Algorithms

When exact solutions are too slow, use approximation:

| Problem | Best Approximation Ratio |
|---------|-------------------------|
| Vertex Cover | 2-approximation (always within factor 2 of optimal) |
| TSP (metric) | 3/2-approximation (Christofides) |
| Set Cover | O(log n)-approximation |
| MAX-SAT | 3/4-approximation |
| General TSP | No constant-factor approximation (unless P=NP) |

---


---
