---
layout: default
title: "Algorithms — Manim Video Animations"
description: "Manim Community Edition animation scripts for all 14 Algorithm chapters"
---

# Algorithms — Manim Video Animations

Animated video explanations for every chapter of the Algorithms study material, built with [Manim Community Edition](https://www.manim.community/).

---

## Setup

```bash
# Install system dependencies
sudo apt-get install libpango1.0-dev libcairo2-dev pkg-config \
    texlive texlive-latex-extra texlive-fonts-extra dvisvgm

# Install Manim CE
pip install manim
```

## Rendering

```bash
# Render a specific scene in high quality
manim -pqh scene_01_algorithm_analysis.py Scene03_BigONotation

# Render all scenes in a file (low quality for preview)
manim -pql scene_01_algorithm_analysis.py

# Render all scenes in a file (high quality)
manim -qh scene_01_algorithm_analysis.py
```

---

## Colour Palette

All animations use a consistent colour scheme matching the website design:

| Colour | Hex | Usage |
|--------|-----|-------|
| Teal | `#1a8a8a` | Titles, main headings |
| Coral | `#d94f4f` | Warnings, traps, key alerts |
| Amber | `#e8a317` | Highlights, analogies |
| Indigo | `#4a5da8` | Secondary info, properties |
| Green | `#2e8b57` | Results, proofs, correct answers |

---

## Scene Index

### Chapter 1: Algorithm Analysis & Asymptotic Notations
**File:** `scene_01_algorithm_analysis.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_WhatIsAnAlgorithm` | Knuth's 5 properties, recipe analogy |
| 2 | `Scene02_WhyAnalyze` | Time vs space complexity dimensions |
| 3 | `Scene03_BigONotation` | Big-O definition, visual proof, limit test |
| 4 | `Scene04_BigOmegaAndTheta` | Lower bound (Ω) and tight bound (Θ) with sandwich graph |
| 5 | `Scene05_LittleOAndOmega` | Strict bounds comparison table |
| 6 | `Scene06_GrowthRatesRace` | Animated race of growth functions |
| 7 | `Scene07_BestWorstAverage` | Best/worst/average case on linear search |
| 8 | `Scene08_CodeAnalysisPatterns` | 7 loop patterns commonly tested in GATE |
| 9 | `Scene09_SpaceComplexity` | Space complexity comparison of sorting algorithms |
| 10 | `Scene10_PropertiesOfNotations` | Reflexive, symmetric, transitive, transpose-symmetric |

### Chapter 2: Recurrence Relations
**File:** `scene_02_recurrence_relations.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_WhatIsRecurrence` | Russian-doll analogy, merge sort recurrence |
| 2 | `Scene02_SubstitutionMethod` | Guess & prove by induction |
| 3 | `Scene03_RecursionTree` | Build tree for T(n)=2T(n/2)+n, sum levels |
| 4 | `Scene04_MasterTheorem` | Three cases with battle analogy |
| 5 | `Scene05_MasterTheoremExamples` | Three worked examples |
| 6 | `Scene06_SpecialRecurrences` | Must-memorise recurrence table |
| 7 | `Scene07_CharacteristicEquation` | Fibonacci via characteristic roots |
| 8 | `Scene08_WhenMasterFails` | Four failure cases |

### Chapter 3: Searching Algorithms
**File:** `scene_03_searching.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_LinearSearch` | Step-by-step linear search animation |
| 2 | `Scene02_BinarySearch` | Binary search with halving visualisation |
| 3 | `Scene03_BinaryVsTernary` | Why binary beats ternary (comparison count) |
| 4 | `Scene04_InterpolationSearch` | Value-based position estimation |
| 5 | `Scene05_JumpSearch` | Block search with optimal block size derivation |
| 6 | `Scene06_ExponentialSearch` | Doubling jumps on number line |
| 7 | `Scene07_SearchComparison` | Master comparison table |

### Chapter 4: Sorting Algorithms
**File:** `scene_04_sorting.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_WhySorting` | Motivation and paradigms |
| 2 | `Scene02_BubbleSort` | Animated bubble pass with swap |
| 3 | `Scene03_SelectionSort` | Properties, minimum swaps, instability |
| 4 | `Scene04_InsertionSort` | Card analogy, adaptivity, online |
| 5 | `Scene05_MergeSort` | Split-merge tree visualisation |
| 6 | `Scene06_QuickSort` | Partition concept and worst case |
| 7 | `Scene07_HeapSort` | Build heap O(n) proof |
| 8 | `Scene08_CountingRadixBucket` | Non-comparison sorts overview |
| 9 | `Scene09_LowerBound` | Decision tree Ω(n log n) proof |
| 10 | `Scene10_MasterComparison` | Master comparison table |

### Chapter 5: Divide and Conquer
**File:** `scene_05_divide_and_conquer.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_DCParadigm` | Divide-Conquer-Combine three steps |
| 2 | `Scene02_MaxSubarray` | D&C approach with crossing subarray |
| 3 | `Scene03_Strassen` | 7 multiplications, complexity derivation |
| 4 | `Scene04_Karatsuba` | Fast integer multiplication trick |
| 5 | `Scene05_ClosestPair` | O(n log n) closest pair with strip |
| 6 | `Scene06_MedianOfMedians` | O(n) worst-case selection |

### Chapter 6: Greedy Algorithms
**File:** `scene_06_greedy.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_GreedyParadigm` | Greedy choice + optimal substructure |
| 2 | `Scene02_ActivitySelection` | Timeline with earliest finish time |
| 3 | `Scene03_FractionalKnapsack` | Value/weight ratio greedy |
| 4 | `Scene04_HuffmanCoding` | Step-by-step tree building |
| 5 | `Scene05_JobSequencing` | Slot-based scheduling |
| 6 | `Scene06_KruskalMST` | Sort edges, union-find, MST properties |
| 7 | `Scene07_PrimAndDijkstra` | Kruskal vs Prim vs Dijkstra comparison |
| 8 | `Scene08_GreedyVsDP` | When to use which paradigm |

### Chapter 7: Dynamic Programming
**File:** `scene_07_dynamic_programming.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_DPParadigm` | Two key properties, top-down vs bottom-up |
| 2 | `Scene02_FibonacciDP` | Recursion tree vs DP table |
| 3 | `Scene03_LCS` | Recurrence and GATE tricks |
| 4 | `Scene04_LIS` | O(n²) and O(n log n) approaches |
| 5 | `Scene05_MCM` | Parenthesisation with order-matters example |
| 6 | `Scene06_Knapsack01` | DP table and pseudo-polynomial note |
| 7 | `Scene07_FloydWarshall` | All-pairs shortest paths recurrence |
| 8 | `Scene08_BellmanFord` | V-1 relaxations and negative cycle detection |
| 9 | `Scene09_EditDistance` | kitten->sitting example |
| 10 | `Scene10_CoinChange` | Minimum coins and number of ways |
| 11 | `Scene11_DPStrategy` | 6-step problem-solving framework |

### Chapter 8: Graph Algorithms
**File:** `scene_08_graph_algorithms.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_GraphRepresentations` | Matrix vs list comparison |
| 2 | `Scene02_BFS` | Level-by-level with graph animation |
| 3 | `Scene03_DFS` | Edge classification table |
| 4 | `Scene04_TopologicalSort` | DFS vs Kahn's BFS methods |
| 5 | `Scene05_SCC` | Kosaraju and Tarjan algorithms |
| 6 | `Scene06_ShortestPathSummary` | Master comparison with decision tree |
| 7 | `Scene07_ArticulationBridges` | Low-link based detection rules |
| 8 | `Scene08_Bipartite` | 2-coloring and odd-cycle theorem |

### Chapter 9: Backtracking & Branch and Bound
**File:** `scene_09_backtracking.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_BacktrackingParadigm` | Template with pruning |
| 2 | `Scene02_NQueens` | 4-Queens board animation |
| 3 | `Scene03_SubsetSum` | Include/exclude with pruning |
| 4 | `Scene04_GraphColoring` | Chromatic number facts |
| 5 | `Scene05_HamiltonianVsEuler` | NP-Complete vs polynomial comparison |
| 6 | `Scene06_BranchAndBound` | Bound-based pruning for optimisation |
| 7 | `Scene07_BacktrackVsBBVsDP` | Three paradigms comparison table |

### Chapter 10: String Matching Algorithms
**File:** `scene_10_string_matching.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_NaiveMatching` | Sliding window animation |
| 2 | `Scene02_KMP_LPS` | LPS array construction step by step |
| 3 | `Scene03_KMP_Search` | O(n+m) proof and skip mechanism |
| 4 | `Scene04_RabinKarp` | Rolling hash formula and collisions |
| 5 | `Scene05_FiniteAutomaton` | DFA matching overview |
| 6 | `Scene06_StringMatchingComparison` | Comparison table |

### Chapter 11: Complexity Classes & NP-Completeness
**File:** `scene_11_complexity_classes.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_WhyThisMatters` | P vs NP million dollar question |
| 2 | `Scene02_PAndNP` | Class P and NP definitions |
| 3 | `Scene03_NPHardComplete` | Venn diagram of complexity classes |
| 4 | `Scene04_Reductions` | How to prove NP-Complete |
| 5 | `Scene05_FamousNPC` | Famous problems and reduction chain |
| 6 | `Scene06_PvsNPC` | The 2-vs-3 pattern |
| 7 | `Scene07_PseudoPolynomial` | Pseudo-polynomial and approximation |

### Chapter 12: Amortized Analysis
**File:** `scene_12_amortized_analysis.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_WhatIsAmortized` | Piggy bank analogy, three methods |
| 2 | `Scene02_AggregateMethod` | Stack with Multipop |
| 3 | `Scene03_AccountingMethod` | Overcharge cheap, subsidise expensive |
| 4 | `Scene04_PotentialMethod` | Φ function with stack example |
| 5 | `Scene05_DynamicArray` | Doubling array amortised O(1) |
| 6 | `Scene06_UnionFindSplay` | α(n) and O(log n) amortised |
| 7 | `Scene07_WhichMethod` | Method selection guide |

### Chapter 13: Miscellaneous & Advanced Topics
**File:** `scene_13_miscellaneous.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_HashTableBasics` | Hash functions and collision types |
| 2 | `Scene02_OpenAddressing` | Linear, quadratic, double hashing |
| 3 | `Scene03_RandomizedAlgorithms` | Las Vegas vs Monte Carlo |
| 4 | `Scene04_LowerBounds` | Comparison-based lower bounds table |
| 5 | `Scene05_Approximation` | Approximation ratios for NP-Hard |
| 6 | `Scene06_CatalanAndIdentities` | Catalan numbers and GATE identities |

### Chapter 14: GATE Exam Strategy & PYQ Patterns
**File:** `scene_14_gate_strategy.py`

| # | Scene | Content |
|---|-------|---------|
| 1 | `Scene01_TopicWeightage` | Animated bar chart of marks distribution |
| 2 | `Scene02_QuestionPatterns` | Five common GATE question types |
| 3 | `Scene03_TimeManagement` | Time allocation per question type |
| 4 | `Scene04_CommonMistakes` | Top 10 mistakes to avoid |
| 5 | `Scene05_SortingQuickRef` | Sorting algorithms quick reference |
| 6 | `Scene06_GraphQuickRef` | Graph algorithms quick reference |
| 7 | `Scene07_DPQuickRef` | DP problems quick reference |
| 8 | `Scene08_FinalChecklist` | Animated exam readiness checklist |

---

## Total Scenes: 104

Each scene is self-contained and can be rendered independently. Scenes cover every concept from the corresponding chapter markdown file with visual explanations, animated proofs, comparison tables, and GATE-specific tips.
