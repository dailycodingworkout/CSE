# Permutation & Combination | One-Page Cheat Sheet

## 🎯 Core Decision Framework

```
                    ┌─────────────────────────┐
                    │   Does ORDER matter?    │
                    └───────────┬─────────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
              ┌─────────┐             ┌─────────────┐
              │   YES   │             │     NO      │
              │PERMUTATION│           │COMBINATION  │
              └────┬────┘             └──────┬──────┘
                   │                         │
         ┌─────────┴─────────┐     ┌─────────┴─────────┐
         ▼                   ▼     ▼                   ▼
    ┌─────────┐        ┌─────────┐ ┌─────────┐   ┌─────────┐
    │Repetition│       │   No    │ │Repetition│  │   No    │
    │ Allowed │        │Repetition│ │ Allowed │  │Repetition│
    └────┬────┘        └────┬────┘ └────┬────┘  └────┬────┘
         │                  │           │            │
         ▼                  ▼           ▼            ▼
       n^r              n!/(n-r)!    C(n+r-1,r)   C(n,r)
```

---

## 📐 Master Formulas

| Scenario | Formula | Example |
|----------|---------|---------|
| **Permutation (no rep.)** | $^nP_r = \frac{n!}{(n-r)!}$ | Arrange 3 from 5: $^5P_3 = 60$ |
| **Permutation (with rep.)** | $n^r$ | 4-digit PIN (0-9): $10^4 = 10000$ |
| **Permutation (identical obj.)** | $\frac{n!}{n_1! \cdot n_2! \cdots}$ | "MISSISSIPPI": $\frac{11!}{4!4!2!1!}$ |
| **Circular Permutation** | $(n-1)!$ | 6 people in circle: $5! = 120$ |
| **Necklace/Bracelet** | $\frac{(n-1)!}{2}$ | 6 beads on ring: $\frac{5!}{2} = 60$ |
| **Combination (no rep.)** | $^nC_r = \frac{n!}{r!(n-r)!}$ | Choose 3 from 5: $^5C_3 = 10$ |
| **Combination (with rep.)** | $^{n+r-1}C_r$ | 5 fruits from 3 types: $^7C_5 = 21$ |
| **Derangement** | $D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$ | $D_4 = 9$ |
| **Catalan Number** | $C_n = \frac{1}{n+1}\binom{2n}{n}$ | $C_4 = 14$ |

---

## ⚡ Quick Identities

$$^nC_r = {^nC_{n-r}} \quad \text{(Symmetry)}$$

$$^nC_r = {^{n-1}C_{r-1}} + {^{n-1}C_r} \quad \text{(Pascal's Rule)}$$

$$\sum_{r=0}^{n} {^nC_r} = 2^n \quad \text{(Total Subsets)}$$

$$^nP_r = {^nC_r} \times r! \quad \text{(Core Relationship)}$$

---

## 🔢 Key Numbers to Remember

| **Factorials** | **Derangements** | **Catalan** |
|----------------|------------------|-------------|
| $5! = 120$ | $D_1 = 0$ | $C_0 = 1$ |
| $6! = 720$ | $D_2 = 1$ | $C_1 = 1$ |
| $7! = 5040$ | $D_3 = 2$ | $C_2 = 2$ |
| $8! = 40320$ | $D_4 = 9$ | $C_3 = 5$ |
| $10! = 3628800$ | $D_5 = 44$ | $C_4 = 14$ |
|  | $D_6 = 265$ | $C_5 = 42$ |

---

## 🎯 Distribution Formulas

| Objects → Boxes | Formula |
|-----------------|---------|
| n **identical** → r **distinct** | $\binom{n+r-1}{r-1}$ |
| n **identical** → r **distinct** (each ≥1) | $\binom{n-1}{r-1}$ |
| n **distinct** → r **distinct** | $r^n$ |
| n **distinct** → r **identical** | $S(n,r)$ (Stirling 2nd) |

---

## ⚠️ Common Traps

| Trap | Wrong | Correct |
|------|-------|---------|
| 4-digit numbers with {0,1,2,3} | $4! = 24$ | $3 \times 3! = 18$ |
| At least one | Direct count | Total - None |
| Circular with n objects | $n!$ | $(n-1)!$ |
| Stars & Bars selection | $\binom{n+r-1}{r-1}$ | $\binom{n+r-1}{r}$ |
| "Together" constraint | Forget internal | Unit × Internal arr. |

---

## 🧮 5-Second Sanity Checks

1. $^nC_r$ must be ≤ $2^n$
2. $^nP_r$ must be ≤ $n!$
3. $^nC_r = {^nC_{n-r}}$ (verify with easier computation)
4. Answer must be positive integer
5. $n=0$ or $r=0$ edge case: usually = 1

---

## 🎓 GATE NAT Precision Rules

- Always **simplify before multiplying**
- Use **smaller r** for $^nC_r$ calculations
- **Double-check division** in factorial problems
- For "at least/at most": **use complement method**

---

*Quick Reference | GATE CSE & ESE 2026*
