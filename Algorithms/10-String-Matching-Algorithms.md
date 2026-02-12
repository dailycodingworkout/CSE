# Chapter 10: String Matching Algorithms

## 10.1 The Problem

**Given:** Text T of length n, Pattern P of length m. Find all occurrences of P in T.

> **Analogy:** Like using Ctrl+F to find a word in a document. How efficiently can the computer do this?

---

## 10.2 Naive (Brute Force) String Matching

```
NaiveMatch(T, P):
    n = |T|, m = |P|
    for s = 0 to n-m:
        match = true
        for j = 0 to m-1:
            if T[s+j] ≠ P[j]:
                match = false
                break
        if match:
            print "Pattern found at shift " + s
```

| Metric | Value |
|--------|-------|
| Best Case | O(n) — first character always mismatches |
| Worst Case | **O((n-m+1)×m) = O(nm)** |
| Space | O(1) |

**Worst case example:** T = "AAAAAAAAB", P = "AAAB" — mismatch always at last character.

---

## 10.3 KMP Algorithm (Knuth-Morris-Pratt) ⭐⭐

> **Key Insight:** When a mismatch occurs, we already know some of the characters that match. Don't re-compare them! Use a **prefix function (failure function)** to skip ahead.

### The Prefix Function (LPS Array)

**LPS[i]** = length of the longest **proper prefix** of P[0..i] that is also a **suffix** of P[0..i].

**How to compute:**
```
ComputeLPS(P, m):
    LPS[0] = 0
    len = 0          // length of previous longest prefix suffix
    i = 1
    while i < m:
        if P[i] == P[len]:
            len++
            LPS[i] = len
            i++
        else:
            if len != 0:
                len = LPS[len-1]    // Key: don't increment i!
            else:
                LPS[i] = 0
                i++
    return LPS
```

**Example:** P = "ABCABD"
```
i=0: LPS[0] = 0                          → [0, _, _, _, _, _]
i=1: P[1]='B' ≠ P[0]='A' → LPS[1] = 0   → [0, 0, _, _, _, _]
i=2: P[2]='C' ≠ P[0]='A' → LPS[2] = 0   → [0, 0, 0, _, _, _]
i=3: P[3]='A' = P[0]='A' → LPS[3] = 1   → [0, 0, 0, 1, _, _]
i=4: P[4]='B' = P[1]='B' → LPS[4] = 2   → [0, 0, 0, 1, 2, _]
i=5: P[5]='D' ≠ P[2]='C', len=LPS[1]=0
     P[5]='D' ≠ P[0]='A' → LPS[5] = 0   → [0, 0, 0, 1, 2, 0]
```

### KMP Search

```
KMP(T, P):
    n = |T|, m = |P|
    LPS = ComputeLPS(P, m)
    i = 0    // index in T
    j = 0    // index in P
    while i < n:
        if T[i] == P[j]:
            i++; j++
        if j == m:
            print "Pattern found at index " + (i-j)
            j = LPS[j-1]
        elif i < n and T[i] ≠ P[j]:
            if j != 0:
                j = LPS[j-1]    // Use failure function (don't move i!)
            else:
                i++
```

| Metric | Value |
|--------|-------|
| Preprocessing | O(m) — building LPS array |
| Matching | **O(n)** |
| Total | **O(n + m)** |
| Space | O(m) — for LPS array |

### Why KMP is O(n)?

**Key observation:** In each step, either:
- i advances (happens at most n times), OR
- j decreases (but j can't decrease more than it has increased, which is at most n times)

Total steps ≤ 2n → **O(n)**

> **GATE Favorite Questions:**
> 1. "Build the LPS/failure function array for pattern P" — Very common!
> 2. "How many character comparisons does KMP make?"
> 3. "What is the worst-case number of comparisons?"

---

## 10.4 Rabin-Karp Algorithm ⭐

> **Key Idea:** Use **hashing** to compare pattern with text windows. Only do character-by-character comparison when hashes match.

### Rolling Hash

**Hash function:** Treat string as a number in base d (alphabet size):
```
hash("abc") = a × d² + b × d¹ + c × d⁰
```

**Rolling hash update:** When sliding from T[s..s+m-1] to T[s+1..s+m]:
```
h(s+1) = d × (h(s) - T[s] × dᵐ⁻¹) + T[s+m]
```

**All computations done mod q** (a large prime) to prevent overflow.

```
RabinKarp(T, P, d, q):
    n = |T|, m = |P|
    h = d^(m-1) mod q        // Precompute highest power
    p = hash(P)              // Pattern hash
    t = hash(T[0..m-1])      // First window hash
    
    for s = 0 to n-m:
        if t == p:
            // Verify character by character (avoid spurious hits)
            if T[s..s+m-1] == P[0..m-1]:
                print "Pattern found at shift " + s
        if s < n-m:
            t = (d × (t - T[s] × h) + T[s+m]) mod q
```

| Metric | Value |
|--------|-------|
| Best/Average | **O(n + m)** |
| Worst Case | **O(nm)** — many spurious hash matches |
| Space | O(1) |

**When is worst case?** When hash function has many collisions. Example: all characters same, T = "AAAA...A", P = "AAA".

> **GATE Facts:**
> - Rabin-Karp is great for **multiple pattern search** (compute hash for each pattern)
> - Average case is O(n+m) with a good hash function
> - Used in plagiarism detection (multiple substring matching)
> - The hash function choice significantly affects performance

---

## 10.5 Finite Automaton Based Matching

**Idea:** Build a DFA (Deterministic Finite Automaton) for the pattern, then process text through it.

**State:** Number of characters matched so far.
**Transition function:** δ(state, character) = length of longest proper suffix of P[0..state]+character that is a prefix of P.

| Metric | Value |
|--------|-------|
| Preprocessing | O(m × |Σ|) — building transition table |
| Matching | **O(n)** — single pass through text |
| Space | O(m × |Σ|) |

> **Comparison with KMP:** KMP uses LPS to implicitly handle the same transitions with O(m) space instead of O(m|Σ|).

---

## 10.6 Comparison of String Matching Algorithms

| Algorithm | Preprocessing | Matching | Total | Space |
|-----------|---------------|----------|-------|-------|
| Naive | None | O(nm) | O(nm) | O(1) |
| KMP | O(m) | O(n) | **O(n+m)** | O(m) |
| Rabin-Karp | O(m) | O(n) avg | O(n+m) avg | O(1) |
| Finite Automaton | O(m\|Σ\|) | O(n) | O(n+m\|Σ\|) | O(m\|Σ\|) |

---


---
