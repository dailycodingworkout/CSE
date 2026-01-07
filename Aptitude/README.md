# GATE ESE PSU Aptitude Master Guide | Maximum Difficulty Question Bank

## The Omega Protocol | Exam Preparation Framework

This comprehensive question bank is designed to exploit all logical gaps and fill them systematically. Each chapter contains:
- **Maximum difficulty questions** covering vast concepts
- **Traps and pitfalls** where most students make mistakes
- **Elegant techniques** to solve problems quickly
- **5-Second Snap-Checks** for answer verification
- **Mental Machinery** for permanent recall

---

## Chapter Directory

| Chapter | Topic | Questions | Key Traps Covered |
|---------|-------|-----------|-------------------|
| [01](01_Number_System.md) | Number System | 12 | Fermat's theorem on composite, Carmichael numbers, Trailing zeros |
| [02](02_Permutation_Combination.md) | Permutation & Combination | 15 | Circular vs Linear, Derangements, Identical objects |
| [03](03_Probability.md) | Probability | 20 | Bayes' Theorem inversion, Birthday paradox, Independence |
| [04](04_Average.md) | Average | 22 | Weighted vs Simple, Speed (Harmonic Mean), Age problems |
| [05](05_Percentage.md) | Percentage | 25 | Successive changes, Base confusion, Percentage points vs % |

---

## Critical Formulas Quick Reference

### Number System
```
Wilson's Theorem: (p-1)! ≡ -1 (mod p) for prime p
Fermat's Little: a^(p-1) ≡ 1 (mod p) for prime p, gcd(a,p)=1
Euler's Theorem: a^φ(n) ≡ 1 (mod n) for gcd(a,n)=1
Trailing zeros in n!: Σ⌊n/5^k⌋
Sum of divisors: σ(n) = Π[(p^(a+1) - 1)/(p-1)]
```

### PNC
```
nPr = n!/(n-r)!
nCr = n!/[r!(n-r)!]
Circular arrangements: (n-1)!
Derangements: Dn = n![1 - 1/1! + 1/2! - 1/3! + ...]
Catalan: Cn = (2n)!/[(n+1)!n!]
Stars and Bars: C(n+r-1, r-1) for n items, r boxes
```

### Probability
```
Bayes: P(A|B) = P(B|A)·P(A)/P(B)
Binomial: P(X=k) = C(n,k)·p^k·(1-p)^(n-k)
Poisson: P(X=k) = λ^k·e^(-λ)/k!
E[X+Y] = E[X] + E[Y] (always)
Var(X+Y) = Var(X) + Var(Y) (if independent)
```

### Average
```
Weighted Average = Σ(wi·xi)/Σwi
Harmonic Mean = n/Σ(1/xi)
AM ≥ GM ≥ HM
AM × HM = GM² (for two numbers)
Average Speed (equal distance) = 2v1v2/(v1+v2)
```

### Percentage
```
Successive change: a + b + ab/100
A is r% more than B → B is r/(100+r)×100% less than A
A is r% less than B → B is r/(100-r)×100% more than A
CI - SI (2 years) = P(r/100)²
Equivalent discount: a + b - ab/100
```

---

## The Five Fatal Traps (Most Common Mistakes)

### Trap 1: Base Confusion
- **Wrong:** "A is 25% more than B, so B is 25% less than A"
- **Right:** B is 20% less than A (different base!)

### Trap 2: Successive Percentage
- **Wrong:** "+20% then -20% = no change"
- **Right:** Net change = -4% (always a loss!)

### Trap 3: Average Speed
- **Wrong:** "Average of 60 and 40 is 50 km/h"
- **Right:** Harmonic mean = 48 km/h (for equal distances)

### Trap 4: Probability Inversion
- **Wrong:** P(A|B) = P(B|A)
- **Right:** Use Bayes' Theorem for inversion

### Trap 5: Circular Arrangements
- **Wrong:** "n! ways for n people in a circle"
- **Right:** (n-1)! ways (fixing one position)

---

## Exam Strategy

### Time Management
1. **NAT questions:** Verify with snap-check before submitting
2. **MSQ questions:** Eliminate options using edge cases
3. **Complex problems:** Use answer choices to work backward

### Verification Techniques
1. **Dimensional Analysis:** Check if units make sense
2. **Extreme Cases:** Test with n=0, 1, large n
3. **Parity Check:** Odd/even consistency
4. **Magnitude Check:** Is the answer in reasonable range?

### Mental Models
1. **For PNC:** Always ask "Does order matter?"
2. **For Probability:** Draw probability trees for clarity
3. **For Percentage:** Always identify the base (of what?)
4. **For Average:** Picture a balanced seesaw

---

## Practice Roadmap

### Week 1: Foundation
- [ ] Number System (Q1-6)
- [ ] PNC (Q1-7)
- [ ] Basic Probability (Q1-8)

### Week 2: Intermediate
- [ ] Number System (Q7-12)
- [ ] PNC (Q8-15)
- [ ] Probability (Q9-15)
- [ ] Average (Q1-11)
- [ ] Percentage (Q1-12)

### Week 3: Advanced
- [ ] Probability (Q16-20)
- [ ] Average (Q12-22)
- [ ] Percentage (Q13-25)
- [ ] Mixed practice from all chapters

### Week 4: Exam Simulation
- [ ] Timed practice (50 questions in 90 minutes)
- [ ] Identify weak areas
- [ ] Targeted revision

---

## Quick Reference Cards

### Number Theory Primes to 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

### Factorial Values
- 5! = 120
- 6! = 720
- 7! = 5040
- 8! = 40320
- 10! = 3,628,800

### Powers of 2
2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128, 2⁸=256, 2⁹=512, 2¹⁰=1024

### Perfect Squares (11-20)
121, 144, 169, 196, 225, 256, 289, 324, 361, 400

### Percentage-Fraction Conversions
- 1/2 = 50%, 1/3 = 33.33%, 1/4 = 25%, 1/5 = 20%
- 1/6 = 16.67%, 1/7 = 14.29%, 1/8 = 12.5%
- 2/3 = 66.67%, 3/4 = 75%, 4/5 = 80%

---

## Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].

> **"The exam will feel easy when you've seen harder problems here."**

---

*Created for GATE/ESE/PSU aspirants aiming for top ranks.*
