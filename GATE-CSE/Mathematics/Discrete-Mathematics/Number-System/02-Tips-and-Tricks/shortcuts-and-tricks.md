# Number System - Tips, Tricks & Shortcuts for GATE 2026 CSE

## 🧠 Memory Techniques & Mental Math Shortcuts

### 🔥 Quick Divisibility Checks

#### Lightning Fast Divisibility by 11
**🎯 The Alternating Sum Trick**
```
For 54769:
5 - 4 + 7 - 6 + 9 = 11 ✓ Divisible by 11

Memory Aid: "See-Saw Pattern" - Up, Down, Up, Down...
```

**⚡ Super Fast Method for Large Numbers**:
1. Split into pairs from right: 54|76|9
2. Sum pairs: 54 + 76 + 9 = 139
3. Check if sum is divisible by 11

#### Divisibility by 7, 11, 13 (Super Trick)
**🎯 The 1001 Method** (since 1001 = 7 × 11 × 13)
```
For 6-digit number abcdef:
Split as abc|def
If |abc - def| is divisible by 7/11/13, then original number is too

Example: 234567
234 - 567 = -333
333 ÷ 3 = 111 ÷ 3 = 37 (not divisible by 7, 11, or 13)
```

#### Divisibility by 6, 12, 15, 18 (Composite Tricks)
**🎯 Factor Combination Method**
- **6**: Must be divisible by both 2 AND 3
- **12**: Must be divisible by both 3 AND 4
- **15**: Must be divisible by both 3 AND 5
- **18**: Must be divisible by both 2 AND 9

### 🚀 HCF & LCM Lightning Calculations

#### The Euclidean Speed Method
```
GCD(1071, 462):
1071 = 2×462 + 147    (Quick: 1071 - 2×462)
462 = 3×147 + 21      (Quick: 462 - 3×147)  
147 = 7×21 + 0        (Quick: 147 ÷ 21 = 7)
Answer: 21
```

#### LCM Without Full Calculation
**🎯 The Prime Factor Shortcut**
```
For 36 and 48:
36 = 2² × 3²
48 = 2⁴ × 3¹
LCM = 2⁴ × 3² = 16 × 9 = 144
```

#### HCF of Fractions (Memory Aid)
**"NuH/DeL"** → **Nu**merator **H**CF / **De**nominator **L**CM

### 🎲 Prime Number Shortcuts

#### Quick Primality Check (6k±1 Rule)
**🎯 Only check numbers of form 6k±1**
```
For checking if 97 is prime:
97 = 6×16 + 1 ✓ (form 6k+1)
Only test divisors: 5, 7, 11 (up to √97 ≈ 10)
97 ÷ 5 = 19.4 ✗
97 ÷ 7 = 13.86 ✗  
97 is prime!
```

#### Prime Generation Pattern
**🎯 Memory**: All primes > 3 are 6k±1
- **6k-1**: 5, 11, 17, 23, 29, 41, 47...
- **6k+1**: 7, 13, 19, 31, 37, 43...

### 📊 Counting Factors Super Fast

#### The Exponent Addition Trick
```
For n = 2³ × 3² × 5¹:
Number of factors = (3+1)(2+1)(1+1) = 4×3×2 = 24

For finding specific type factors:
- Even factors: Fix one power of 2, vary others = 3×3×2 = 18
- Odd factors: Remove all powers of 2 = 3×2 = 6
```

#### Sum of Factors Formula (Quick Calculation)
```
For n = 2² × 3¹:
Sum = [(2³-1)/(2-1)] × [(3²-1)/(3-1)]
    = [(8-1)/1] × [(9-1)/2]  
    = 7 × 4 = 28
```

### 🔄 Cyclicity Super Shortcuts

#### Unit Digit Power Patterns (Memory Palace)
**🎯 Visual Memory Aid**:
```
2: "2→4→8→6" (Remember: "24 ate 6")
3: "3→9→7→1" (Remember: "39 to 71")  
4: "4→6" (Remember: "4 sick 6")
7: "7→9→3→1" (Remember: "79 through 31")
8: "8→4→2→6" (Remember: "84 to 26")
9: "9→1" (Remember: "9 won 1")
```

#### Finding Last Digit of Large Powers
**🎯 The Modular Shortcut**
```
Find last digit of 3^47:
47 ÷ 4 = 11 remainder 3
So 3^47 has same last digit as 3³ = 27
Last digit = 7
```

### 🎯 Base Conversion Speed Techniques

#### Binary to Decimal (Mental Math)
**🎯 The Doubling Method**
```
(1011)₂:
Start from left: 1
1×2 + 0 = 2
2×2 + 1 = 5  
5×2 + 1 = 11
Answer: 11
```

#### Decimal to Binary (Quick Division)
**🎯 The Power of 2 Subtraction**
```
Convert 45 to binary:
45 - 32(2⁵) = 13
13 - 8(2³) = 5
5 - 4(2²) = 1  
1 - 1(2⁰) = 0
Binary: 101101
```

#### Hex to Decimal (Group Method)
**🎯 16^n Multipliers Memory**
- 16⁰ = 1
- 16¹ = 16  
- 16² = 256
- 16³ = 4096

### 🧮 Remainder Theorem Shortcuts

#### Fermat's Little Theorem Applications
**🎯 For finding a^(large) mod p (where p is prime)**
```
Find 2^100 mod 7:
By Fermat: 2⁶ ≡ 1 (mod 7)
100 = 6×16 + 4
So 2^100 ≡ 2⁴ ≡ 16 ≡ 2 (mod 7)
```

#### Chinese Remainder Theorem Shortcut
**🎯 For systems with small moduli**
```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)  
x ≡ 1 (mod 7)

Quick method:
x = 2×35×k₁ + 3×21×k₂ + 1×15×k₃ (mod 105)
Where 35k₁ ≡ 1 (mod 3), 21k₂ ≡ 1 (mod 5), 15k₃ ≡ 1 (mod 7)
```

### 🎪 Algebraic Identity Speed Tricks

#### Quick Squaring for Numbers near Multiples of 10
**🎯 The (a±b)² Expansion**
```
97² = (100-3)² = 100² - 2×100×3 + 3² = 10000 - 600 + 9 = 9409
103² = (100+3)² = 100² + 2×100×3 + 3² = 10000 + 600 + 9 = 10609
```

#### Factorization Shortcuts
**🎯 Recognition Patterns**
```
a² - b² = (a+b)(a-b)          [Difference of squares]
a³ + b³ = (a+b)(a²-ab+b²)     [Sum of cubes]
a³ - b³ = (a-b)(a²+ab+b²)     [Difference of cubes]

Quick check: If a + b + c = 0, then a³ + b³ + c³ = 3abc
```

### 🎯 Problem-Solving Strategies

#### The "Factor Tree" Visualization
```
For finding all factors systematically:
24 = 2³ × 3¹

Draw tree:
        24
      /    \
     2      12
           /  \
          3    4
              / \
             2   2

Factors: 1, 2, 3, 4, 6, 8, 12, 24
```

#### The "Divisibility Chain" Method
**🎯 For checking multiple divisibilities**
```
To check if 2730 is divisible by 2, 3, 5, 6, 9, 10:

2: Last digit = 0 ✓
5: Last digit = 0 ✓  
10: Ends in 0 ✓
3: Sum = 2+7+3+0 = 12, 12÷3 = 4 ✓
9: Sum = 12, 12÷9 ≠ integer ✗
6: Divisible by both 2 and 3 ✓
```

### 🧠 Memory Aids for Key Facts

#### Prime Numbers < 100 (Grouping Technique)
**🎯 Memory Groups**:
- **Teens**: 11, 13, 17, 19
- **Twenties**: 23, 29  
- **Thirties**: 31, 37
- **Forties**: 41, 43, 47
- **Up to 100**: 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

#### Perfect Squares (Visual Pattern)
**🎯 Unit Digit Pattern**: 0,1,4,5,6,9 only
```
Squares ending in:
1: 1², 9², 11², 19², 21², 29²...
4: 2², 8², 12², 18², 22², 28²...
5: 5², 15², 25², 35², 45²...
6: 4², 6², 14², 16², 24², 26²...
9: 3², 7², 13², 17², 23², 27²...
0: 10², 20², 30², 40²...
```

### ⚡ Speed Calculation Techniques

#### Multiplication by 11 (Mental Math)
```
For 2-digit: 47 × 11
Add digits: 4 + 7 = 11
Result: 4|11|7 = 4|(1+1)|7 = 517

For 3-digit: 234 × 11  
2|2+3|3+4|4 = 2|5|7|4 = 2574
```

#### Squaring Numbers Ending in 5
```
25² = (2×3)|25 = 6|25 = 625
35² = (3×4)|25 = 12|25 = 1225  
85² = (8×9)|25 = 72|25 = 7225
```

#### Percentage to Fraction (Quick Conversion)
**🎯 Common Percentages**:
- 25% = 1/4, 50% = 1/2, 75% = 3/4
- 33⅓% = 1/3, 66⅔% = 2/3
- 12.5% = 1/8, 37.5% = 3/8, 62.5% = 5/8, 87.5% = 7/8
- 20% = 1/5, 40% = 2/5, 60% = 3/5, 80% = 4/5

### 🎲 Examination Strategies

#### Time Management for Number System Questions
1. **Divisibility (30 sec)**: Use direct rules
2. **HCF/LCM (1 min)**: Euclidean or factorization
3. **Prime checking (1 min)**: 6k±1 rule
4. **Base conversion (1 min)**: Practice standard algorithms
5. **Remainder problems (2 min)**: Apply theorems

#### Common Trap Avoidance
- **0 is even**: Remember 0 = 2×0
- **1 is neither prime nor composite**
- **Negative numbers**: Follow definition carefully
- **Rational vs Irrational**: π ≠ 22/7 (22/7 is rational approximation)

### 🏆 Advanced Shortcuts for AIR 1

#### Modular Arithmetic Speed Rules
```
(a + b) mod n = ((a mod n) + (b mod n)) mod n
(a × b) mod n = ((a mod n) × (b mod n)) mod n
a^(b) mod n: Use repeated squaring for large b
```

#### Wilson's Theorem Application
**For checking primality**: (p-1)! ≡ -1 (mod p) iff p is prime
```
Check if 7 is prime:
6! = 720
720 ÷ 7 = 102 remainder 6 ≡ -1 (mod 7) ✓
```

#### Carmichael Numbers (Composite but pass Fermat test)
**Know these exceptions**: 561, 1105, 1729, 2465, 2821...

---

## 🎯 Quick Reference Card

### Essential Formulas for Speed
- **Divisibility**: Use sum patterns (3,9), alternating (11), last digits (2,4,5,8,10)
- **HCF/LCM**: ab = HCF×LCM, use Euclidean algorithm
- **Factors**: (a+1)(b+1)... for p^a × q^b...
- **Trailing zeros in n!**: ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋...
- **Cyclicity**: Power mod cycle_length
- **Base conversion**: Positional notation, repeated division

### Memory Mnemonics
- **Divisibility by 11**: "Alternating current" (+ - + - ...)
- **Primes form**: "Six plus-minus one" (6k±1)
- **Perfect squares end**: "Only 0,1,4,5,6,9"
- **HCF of fractions**: "NuH/DeL" (Numerator HCF/Denominator LCM)

---

**Next**: [Practice Questions](../03-Practice-Questions/) - 100 carefully selected problems!