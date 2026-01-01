# 📚 Discrete Mathematics: Permutation and Combination

Welcome to the **Permutation and Combination** section of the Discrete Mathematics repository! This section covers key concepts and problem-solving methods related to counting techniques, arrangements, and selections.

---

## ✅ Topics Covered

### 🔹 Permutation
- Definition and explanation
- Formula: \( P(n, r) = \frac{n!}{(n-r)!} \)
- Examples and practice problems

### 🔹 Combination
- Definition and explanation
- Formula: \( C(n, r) = \frac{n!}{r!(n-r)!} \)
- Examples and practice problems

### 🔹 Inclusion-Exclusion Principle

The **Inclusion-Exclusion Principle** is used to compute the number of elements in the union of multiple sets.

#### ✅ General Formula (for 2 sets)
\[
|A \cup B| = |A| + |B| - |A \cap B|
\]

#### ✅ General Formula (for 3 sets)
\[
|A \cup B \cup C| = |A| + |B| + |C| 
- |A \cap B| - |A \cap C| - |B \cap C| 
+ |A \cap B \cap C|
\]

#### ✅ General Formula (for n sets)
\[
\left|\bigcup_{i=1}^{n} A_i\right|
= \sum_{i=1}^{n} |A_i|
- \sum_{1 \le i < j \le n} |A_i \cap A_j|
+ \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k|
- \cdots
+ (-1)^{k+1} \sum_{1 \le i_1 < \cdots < i_k \le n} \left|\bigcap_{t=1}^{k} A_{i_t}\right|
+ \cdots
+ (-1)^{n+1} \left|\bigcap_{i=1}^{n} A_i\right|
\]

---

✍️ Feel free to contribute more examples or practice exercises to this section!
