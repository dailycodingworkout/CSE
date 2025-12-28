# 📖 Module 3: Base Conversions - Complete Guide

## 🎯 Learning Objectives

After completing this module, you will:
- Master all types of base conversions
- Learn shortcut methods for quick calculations
- Handle fractional number conversions
- Solve conversion problems in under 30 seconds

---

## 3.1 Overview of Conversion Methods

### Types of Conversions:
```
                    ┌─────────────┐
                    │   DECIMAL   │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  BINARY  │◄──►│  OCTAL   │◄──►│   HEX    │
    └──────────┘    └──────────┘    └──────────┘
```

### Conversion Matrix:
| From↓ To→ | Binary | Octal | Decimal | Hex |
|-----------|--------|-------|---------|-----|
| **Binary** | - | Group 3 | Sum of weights | Group 4 |
| **Octal** | Expand 3 | - | Sum of weights | Via Binary |
| **Decimal** | Divide by 2 | Divide by 8 | - | Divide by 16 |
| **Hex** | Expand 4 | Via Binary | Sum of weights | - |

---

## 3.2 Decimal to Binary Conversion

### Method 1: Repeated Division by 2

**Algorithm:**
1. Divide the number by 2
2. Record the remainder
3. Repeat with quotient until quotient = 0
4. Read remainders bottom to top

**Example: Convert 25₁₀ to Binary**
```
25 ÷ 2 = 12  remainder 1  ← LSB
12 ÷ 2 = 6   remainder 0
6  ÷ 2 = 3   remainder 0
3  ÷ 2 = 1   remainder 1
1  ÷ 2 = 0   remainder 1  ← MSB

Answer: 11001₂
```

### Method 2: Sum of Powers of 2 (Fast Method)

**Algorithm:**
1. Find the largest power of 2 ≤ number
2. Subtract it and put 1 in that position
3. Repeat until number becomes 0

**Example: Convert 45₁₀ to Binary**
```
45 - 32(2⁵) = 13   →  1
13 - 8(2³)  = 5    →  1
5  - 4(2²)  = 1    →  1
1  - 1(2⁰)  = 0    →  1

Position: 5 4 3 2 1 0
Value:    1 0 1 1 0 1

Answer: 101101₂
```

### Method 3: 8-4-2-1 Method (For small numbers)

**Example: Convert 13₁₀ to Binary**
```
8  4  2  1
↓  ↓  ↓  ↓
1  1  0  1   (8+4+1 = 13)

Answer: 1101₂
```

---

## 3.3 Binary to Decimal Conversion

### Method: Weighted Sum

**Formula:**
```
(bₙbₙ₋₁...b₁b₀)₂ = bₙ×2ⁿ + bₙ₋₁×2ⁿ⁻¹ + ... + b₁×2¹ + b₀×2⁰
```

**Example: Convert 110101₂ to Decimal**
```
Position: 5  4  3  2  1  0
Binary:   1  1  0  1  0  1
Weight:   32 16 8  4  2  1

Value = 32 + 16 + 0 + 4 + 0 + 1 = 53₁₀
```

### Shortcut: Doubling Method

**Algorithm:** Start from MSB, double and add
```
110101₂
Start: 1
1×2 + 1 = 3
3×2 + 0 = 6
6×2 + 1 = 13
13×2 + 0 = 26
26×2 + 1 = 53

Answer: 53₁₀
```

---

## 3.4 Decimal to Octal Conversion

### Method: Repeated Division by 8

**Example: Convert 125₁₀ to Octal**
```
125 ÷ 8 = 15  remainder 5  ← LSB
15  ÷ 8 = 1   remainder 7
1   ÷ 8 = 0   remainder 1  ← MSB

Answer: 175₈
```

### Verification:
```
1×64 + 7×8 + 5×1 = 64 + 56 + 5 = 125 ✓
```

---

## 3.5 Octal to Decimal Conversion

### Method: Weighted Sum

**Example: Convert 372₈ to Decimal**
```
3×8² + 7×8¹ + 2×8⁰
= 3×64 + 7×8 + 2×1
= 192 + 56 + 2
= 250₁₀
```

---

## 3.6 Decimal to Hexadecimal Conversion

### Method: Repeated Division by 16

**Example: Convert 500₁₀ to Hexadecimal**
```
500 ÷ 16 = 31  remainder 4  (4)    ← LSB
31  ÷ 16 = 1   remainder 15 (F)
1   ÷ 16 = 0   remainder 1  (1)    ← MSB

Answer: 1F4₁₆
```

### Verification:
```
1×256 + 15×16 + 4×1 = 256 + 240 + 4 = 500 ✓
```

---

## 3.7 Hexadecimal to Decimal Conversion

### Method: Weighted Sum

**Example: Convert 2AF₁₆ to Decimal**
```
2×16² + A×16¹ + F×16⁰
= 2×256 + 10×16 + 15×1
= 512 + 160 + 15
= 687₁₀
```

---

## 3.8 Binary ↔ Octal Conversion (Direct Method)

### Binary to Octal:
Group binary digits in sets of 3 (from right), convert each group.

**Example: Convert 10110111₂ to Octal**
```
Binary:  010  110  111  (pad with 0 on left)
Octal:    2    6    7

Answer: 267₈
```

### Octal to Binary:
Convert each octal digit to 3-bit binary.

**Example: Convert 457₈ to Binary**
```
Octal:   4     5     7
Binary: 100   101   111

Answer: 100101111₂
```

---

## 3.9 Binary ↔ Hexadecimal Conversion (Direct Method)

### Binary to Hexadecimal:
Group binary digits in sets of 4 (from right), convert each group.

**Example: Convert 1101011110₂ to Hex**
```
Binary: 0011  0101  1110  (pad with 0s on left)
Hex:      3     5     E

Answer: 35E₁₆
```

### Hexadecimal to Binary:
Convert each hex digit to 4-bit binary.

**Example: Convert B7C₁₆ to Binary**
```
Hex:      B      7      C
Binary: 1011   0111   1100

Answer: 101101111100₂
```

---

## 3.10 Octal ↔ Hexadecimal Conversion

### Method: Via Binary (Most Efficient)

**Example: Convert 752₈ to Hex**
```
Step 1: Octal to Binary
  7     5     2
 111   101   010
 
Binary: 111101010₂

Step 2: Binary to Hex
 0001  1110  1010  (group by 4 from right)
   1     E     A

Answer: 1EA₁₆
```

**Example: Convert A3F₁₆ to Octal**
```
Step 1: Hex to Binary
   A      3      F
  1010   0011   1111

Binary: 101000111111₂

Step 2: Binary to Octal
  101   000   111   111  (group by 3 from right)
   5     0     7     7

Answer: 5077₈
```

---

## 3.11 Fractional Number Conversions

### Decimal Fraction to Binary:

**Method: Repeated Multiplication by 2**

**Example: Convert 0.625₁₀ to Binary**
```
0.625 × 2 = 1.25  → 1  (MSB of fraction)
0.25  × 2 = 0.5   → 0
0.5   × 2 = 1.0   → 1  (LSB of fraction)

Answer: 0.101₂
```

**Verification:**
```
1×2⁻¹ + 0×2⁻² + 1×2⁻³
= 0.5 + 0 + 0.125 = 0.625 ✓
```

### Non-Terminating Fractions:

**Example: Convert 0.1₁₀ to Binary**
```
0.1 × 2 = 0.2 → 0
0.2 × 2 = 0.4 → 0
0.4 × 2 = 0.8 → 0
0.8 × 2 = 1.6 → 1
0.6 × 2 = 1.2 → 1
0.2 × 2 = 0.4 → 0  (repeating pattern)

Answer: 0.000110011001100...₂ = 0.(0011)₂
```

### Binary Fraction to Decimal:

**Example: Convert 0.1101₂ to Decimal**
```
1×2⁻¹ + 1×2⁻² + 0×2⁻³ + 1×2⁻⁴
= 0.5 + 0.25 + 0 + 0.0625
= 0.8125₁₀
```

---

## 3.12 Mixed Number Conversions

### Integer + Fractional Part:

**Example: Convert 25.375₁₀ to Binary**

**Step 1: Convert integer part (25)**
```
25 = 11001₂
```

**Step 2: Convert fractional part (0.375)**
```
0.375 × 2 = 0.75 → 0
0.75  × 2 = 1.5  → 1
0.5   × 2 = 1.0  → 1

0.375 = 0.011₂
```

**Step 3: Combine**
```
Answer: 11001.011₂
```

---

## 3.13 Shortcut Methods for GATE

### Shortcut 1: Using Powers of 2

```
Memorize: 2¹⁰ = 1024 ≈ 1000
          2²⁰ = 1,048,576 ≈ 10⁶

For 2ⁿ where n > 10:
2ⁿ = 2¹⁰ × 2ⁿ⁻¹⁰ = 1024 × 2ⁿ⁻¹⁰
```

### Shortcut 2: Two's Complement Negation
```
-N in binary = Flip all bits + 1
             = (2ⁿ - N) for n-bit system
```

### Shortcut 3: Quick Division
```
÷2 in binary = Right shift by 1
÷4 in binary = Right shift by 2
÷8 in binary = Right shift by 3
```

### Shortcut 4: Quick Multiplication
```
×2 in binary = Left shift by 1
×4 in binary = Left shift by 2
×8 in binary = Left shift by 3
```

### Shortcut 5: Finding Number of Bits
```
For decimal number N:
Bits needed = ⌊log₂(N)⌋ + 1
            = ceil(log₂(N+1))

Example: N = 100
log₂(100) ≈ 6.64
Bits needed = 7
```

---

## 3.14 Common Conversion Table (Must Memorize!)

| Decimal | Binary | Octal | Hex |
|---------|--------|-------|-----|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

---

## 3.15 GATE-Style Conversion Problems

### Problem Types:
1. **Direct Conversion**: Convert X base to Y base
2. **Operations**: Add/Subtract in different bases
3. **Comparison**: Which is larger?
4. **Finding Unknown Digit**: Solve for x in (x32)₈ = (1A)₁₆

---

## 3.16 Solved GATE Problems

### Problem 1 (GATE 2019):
The decimal value of (1.1)₂ × (1.1)₂ is ___

**Solution:**
```
(1.1)₂ = 1 + 0.5 = 1.5₁₀
(1.1)₂ × (1.1)₂ = 1.5 × 1.5 = 2.25₁₀

Answer: 2.25
```

### Problem 2 (GATE 2017):
If (11X)₁₆ = (0001 0001 0101)₂, find X.

**Solution:**
```
(11X)₁₆ in binary = 0001 0001 XXXX
Given: 0001 0001 0101
So X = 0101₂ = 5₁₆

Answer: X = 5
```

### Problem 3 (GATE 2016):
Convert (2.3)₁₀ to binary (3 decimal places).

**Solution:**
```
Integer: 2 = 10₂
Fraction: 0.3
  0.3 × 2 = 0.6 → 0
  0.6 × 2 = 1.2 → 1
  0.2 × 2 = 0.4 → 0
  
Answer: 10.010₂ (approx)
```

---

## 3.17 Summary

### Conversion Flowchart:
```
ANY BASE ──→ DECIMAL ──→ ANY BASE
     ↓                       ↓
   (Weighted Sum)    (Repeated Division)

BINARY ◄─────────────────► OCTAL/HEX
            (Direct Grouping)
```

### Key Points:
✅ Decimal to Base-r: Repeated division, read remainders bottom-up
✅ Base-r to Decimal: Weighted sum of digits
✅ Binary ↔ Octal: Group/expand by 3 bits
✅ Binary ↔ Hex: Group/expand by 4 bits
✅ Fractional: Multiply by base, read integer parts top-down

---

## 📝 Practice Problems

### Easy:
1. Convert 156₁₀ to binary
2. Convert 10110111₂ to decimal
3. Convert 3AF₁₆ to octal

### Medium:
4. Convert 0.4₁₀ to binary (5 bits after point)
5. Convert 65.25₁₀ to hexadecimal
6. If (72)ₓ = (58)₁₀, find x

### Hard:
7. Find the smallest n such that (11...1)₂ (n ones) > (999)₁₀
8. Convert (0.101)₂ recurring to decimal fraction

<details>
<summary>Answers</summary>

1. 10011100₂
2. 183₁₀
3. 1657₈
4. 0.01100...₂
5. 41.4₁₆
6. x = 9
7. n = 10 (1023 > 999)
8. 5/7 or 0.714285...

</details>

---

## 🔜 Next Module
[Module 4: Signed Number Representation →](../04_Signed_Number_Representation/)
