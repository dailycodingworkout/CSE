# 📖 Module 10: Practice Problems - Solved Examples

## 🎯 Learning Objectives

After completing this module, you will:
- Apply all number system concepts to solve problems
- Develop speed and accuracy for GATE
- Learn problem-solving strategies
- Build confidence through practice

---

## 10.1 Base Conversion Problems

### Problem 1: Decimal to Binary
**Convert 156.625 to binary**

**Solution:**
```
Integer part: 156
156 ÷ 2 = 78 R 0
78 ÷ 2 = 39 R 0
39 ÷ 2 = 19 R 1
19 ÷ 2 = 9 R 1
9 ÷ 2 = 4 R 1
4 ÷ 2 = 2 R 0
2 ÷ 2 = 1 R 0
1 ÷ 2 = 0 R 1

Reading bottom to top: 10011100

Fractional part: 0.625
0.625 × 2 = 1.25 → 1
0.25 × 2 = 0.5 → 0
0.5 × 2 = 1.0 → 1

Reading top to bottom: 0.101

Answer: 156.625₁₀ = 10011100.101₂
```

---

### Problem 2: Binary to Hexadecimal
**Convert 1011110010.11011 to hexadecimal**

**Solution:**
```
Group by 4 bits from radix point:
Integer: 10 1111 0010 → 0010 1111 0010
Fraction: 1101 1 → 1101 1000 (pad with zeros)

0010 = 2
1111 = F
0010 = 2
.
1101 = D
1000 = 8

Answer: 2F2.D8₁₆
```

---

### Problem 3: Octal to Binary to Hex
**Convert 7654₈ to hexadecimal**

**Solution:**
```
Step 1: Octal to Binary (expand each digit to 3 bits)
7 → 111
6 → 110
5 → 101
4 → 100

Binary: 111110101100₂

Step 2: Binary to Hex (group by 4 bits from right)
1111 1010 1100
  F    A    C

Answer: 7654₈ = FAC₁₆
```

---

### Problem 4: Find Unknown Base
**If (23)ₓ = (15)₁₀, find x**

**Solution:**
```
(23)ₓ = 2×x + 3×1 = 15
2x + 3 = 15
2x = 12
x = 6

Verify: 2×6 + 3 = 15 ✓

Answer: x = 6
```

---

### Problem 5: Mixed Base Problem
**If (132)ₓ = (30)₁₀, find x**

**Solution:**
```
1×x² + 3×x + 2 = 30
x² + 3x + 2 = 30
x² + 3x - 28 = 0
(x + 7)(x - 4) = 0
x = 4 or x = -7

Since base must be positive and > 3 (largest digit is 3):
x = 4

Verify: 1×16 + 3×4 + 2 = 16 + 12 + 2 = 30 ✓

Answer: x = 4
```

---

## 10.2 Signed Number Problems

### Problem 6: 2's Complement Representation
**Represent -57 in 8-bit 2's complement**

**Solution:**
```
Step 1: Convert 57 to binary
57 = 32 + 16 + 8 + 1 = 00111001

Step 2: Invert all bits
~00111001 = 11000110

Step 3: Add 1
11000110 + 1 = 11000111

Verify: -128 + 64 + 4 + 2 + 1 = -128 + 71 = -57 ✓

Answer: -57 = 11000111₂ (in 8-bit 2's complement)
```

---

### Problem 7: Find Decimal Value
**What decimal number does 10110011 represent in 8-bit 2's complement?**

**Solution:**
```
Method 1: Weighted sum
= -128 + 32 + 16 + 2 + 1
= -128 + 51
= -77

Method 2: 2's complement conversion
10110011 → invert → 01001100 → add 1 → 01001101 = 77
Answer = -77

Answer: -77
```

---

### Problem 8: Sign Extension
**Sign extend 1010 (4-bit) to 8 bits in 2's complement**

**Solution:**
```
Original: 1010 (MSB = 1, so negative)

Sign extend by copying MSB:
4-bit: 1010
8-bit: 11111010

Verify:
4-bit value: -8 + 2 = -6
8-bit value: -128 + 64 + 32 + 16 + 8 + 2 = -128 + 122 = -6 ✓

Answer: 11111010
```

---

### Problem 9: Range Calculation
**What is the range of values in 12-bit 2's complement?**

**Solution:**
```
For n-bit 2's complement:
Minimum = -2^(n-1)
Maximum = 2^(n-1) - 1

For n = 12:
Minimum = -2¹¹ = -2048
Maximum = 2¹¹ - 1 = 2047

Answer: -2048 to +2047
```

---

## 10.3 Arithmetic Problems

### Problem 10: 2's Complement Addition
**Add -25 and 18 in 8-bit 2's complement**

**Solution:**
```
-25 in 2's complement:
25 = 00011001
-25 = 11100111

18 = 00010010

  11100111  (-25)
+ 00010010  (+18)
──────────
  11111001

Result = -128 + 64 + 32 + 16 + 8 + 1 = -128 + 121 = -7

Verify: -25 + 18 = -7 ✓

Answer: -7 (11111001)
```

---

### Problem 11: Overflow Detection
**Does adding 100 and 50 cause overflow in 8-bit 2's complement?**

**Solution:**
```
100 = 01100100
50 = 00110010

  01100100
+ 00110010
──────────
  10010110

Result = 10010110
As signed: -128 + 16 + 4 + 2 = -106

Both inputs positive (MSB = 0)
Result negative (MSB = 1)
→ OVERFLOW!

Carry into MSB = 1, Carry out of MSB = 0
V = 1 ⊕ 0 = 1 → OVERFLOW confirmed

Expected: 100 + 50 = 150, but 8-bit signed max is 127

Answer: YES, overflow occurs
```

---

### Problem 12: Binary Multiplication
**Multiply 1011 × 101 in binary**

**Solution:**
```
        1011  (11)
      ×  101  (5)
      ──────
        1011  (1011 × 1)
       0000   (1011 × 0, shifted left)
      1011    (1011 × 1, shifted left)
     ───────
     110111  (55)

Verify: 11 × 5 = 55 ✓

Answer: 110111₂
```

---

### Problem 13: Octal Subtraction
**Calculate 752₈ - 365₈**

**Solution:**
```
Method: Subtract directly with borrows

  7 5 2
- 3 6 5
───────

Position 0: 2 - 5, need to borrow
  12 - 5 = 5 (12₈ = 10₁₀, 10 - 5 = 5)

Position 1: 4 - 6 (after lending 1), need to borrow
  14 - 6 = 6 (14₈ = 12₁₀, 12 - 6 = 6)

Position 2: 6 - 3 = 3 (after lending 1)

Answer: 752₈ - 365₈ = 365₈

Verify: 
752₈ = 7×64 + 5×8 + 2 = 448 + 40 + 2 = 490
365₈ = 3×64 + 6×8 + 5 = 192 + 48 + 5 = 245
490 - 245 = 245 = 365₈ ✓
```

---

## 10.4 Floating Point Problems

### Problem 14: Decimal to IEEE 754
**Convert -6.75 to IEEE 754 single precision**

**Solution:**
```
Step 1: Sign bit
Negative → S = 1

Step 2: Convert to binary
6 = 110₂
0.75 = 0.11₂
6.75 = 110.11₂

Step 3: Normalize
110.11 = 1.1011 × 2²

Step 4: Exponent (biased)
Actual exponent = 2
Biased = 2 + 127 = 129 = 10000001₂

Step 5: Mantissa (without hidden bit)
1.1011 → M = 10110000000000000000000

Answer:
S = 1
E = 10000001
M = 10110000000000000000000

Full: 1 10000001 10110000000000000000000
Hex: 0xC0D80000
```

---

### Problem 15: IEEE 754 to Decimal
**Convert 0x41C80000 to decimal**

**Solution:**
```
Step 1: Convert to binary
0x41C80000 = 0100 0001 1100 1000 0000 0000 0000 0000

Step 2: Extract fields
S = 0
E = 10000011 = 131
M = 10010000000000000000000

Step 3: Calculate
Sign = positive (S = 0)
Actual exponent = 131 - 127 = 4
Mantissa = 1.1001 (with hidden bit)

Value = 1 × 1.1001₂ × 2⁴
      = 1.5625 × 16
      = 25.0

Answer: 25.0
```

---

### Problem 16: Floating Point Range
**What is the smallest positive normalized number in IEEE 754 single precision?**

**Solution:**
```
Smallest normalized: E = 1 (minimum non-zero), M = 0

E = 00000001 = 1
M = 00000000000000000000000

Value = 1.0 × 2^(1-127)
      = 2^(-126)
      ≈ 1.175 × 10^(-38)

Answer: 2^(-126) ≈ 1.175 × 10^(-38)
```

---

## 10.5 Special Codes Problems

### Problem 17: BCD Addition
**Add 47 and 35 in BCD**

**Solution:**
```
47 in BCD: 0100 0111
35 in BCD: 0011 0101

Add digit by digit:
Ones: 0111 + 0101 = 1100 (12 > 9, need correction)
      1100 + 0110 = 10010 → 0010, carry 1
      
Tens: 0100 + 0011 + 1 = 1000 (8 ≤ 9, no correction)

Result: 1000 0010 = 82 in BCD

Verify: 47 + 35 = 82 ✓

Answer: 1000 0010 (BCD)
```

---

### Problem 18: Gray Code Conversion
**Convert 13 to Gray code**

**Solution:**
```
Step 1: Convert 13 to binary
13 = 1101₂

Step 2: Binary to Gray
G[3] = B[3] = 1
G[2] = B[3] ⊕ B[2] = 1 ⊕ 1 = 0
G[1] = B[2] ⊕ B[1] = 1 ⊕ 0 = 1
G[0] = B[1] ⊕ B[0] = 0 ⊕ 1 = 1

Gray code: 1011

Answer: 1011 (Gray)
```

---

### Problem 19: Hamming Code
**Calculate parity bits for data 1011 using Hamming(7,4)**

**Solution:**
```
Position: 1   2   3   4   5   6   7
Type:     P1  P2  D1  P4  D2  D3  D4
Data:     ?   ?   1   ?   0   1   1

P1 covers positions 1,3,5,7: P1,1,0,1
P1 = 1 ⊕ 0 ⊕ 1 = 0

P2 covers positions 2,3,6,7: P2,1,1,1
P2 = 1 ⊕ 1 ⊕ 1 = 1

P4 covers positions 4,5,6,7: P4,0,1,1
P4 = 0 ⊕ 1 ⊕ 1 = 0

Final code: 0 1 1 0 0 1 1

Answer: 0110011 (Hamming code)
```

---

### Problem 20: ASCII Calculation
**What is the ASCII value of 'e' if 'A' = 65?**

**Solution:**
```
'A' = 65
'a' = 'A' + 32 = 97

'a' = 97
'e' = 'a' + 4 = 101

Or directly:
'e' is the 5th lowercase letter
'a' = 97
'e' = 97 + 4 = 101

Answer: 101 (0x65)
```

---

## 10.6 Mixed Problems

### Problem 21: Number of Bits
**How many bits are needed to represent 1000 distinct values?**

**Solution:**
```
Need: n bits such that 2ⁿ ≥ 1000

2⁹ = 512 < 1000
2¹⁰ = 1024 ≥ 1000

Answer: 10 bits
```

---

### Problem 22: Complement Comparison
**What is 1010 in unsigned, sign-magnitude, 1's comp, and 2's comp (4-bit)?**

**Solution:**
```
Binary: 1010

Unsigned: 8 + 2 = 10

Sign-Magnitude: 
  MSB = 1 (negative)
  Magnitude = 010 = 2
  Value = -2

1's Complement:
  MSB = 1 (negative)
  Complement: 0101 = 5
  Value = -5

2's Complement:
  MSB = 1 (negative)
  Value = -8 + 2 = -6
  Or: complement + 1 = 0101 + 1 = 0110 = 6, so -6

Answer:
- Unsigned: 10
- Sign-Magnitude: -2
- 1's Complement: -5
- 2's Complement: -6
```

---

### Problem 23: Floating Point Precision
**How many bits of precision does IEEE 754 single precision provide?**

**Solution:**
```
Single precision:
- Mantissa: 23 bits
- Hidden bit: 1 bit
- Total precision: 24 bits

Decimal equivalent:
log₁₀(2²⁴) = 24 × log₁₀(2) = 24 × 0.301 ≈ 7.2 digits

Answer: 24 binary bits ≈ 7 decimal digits
```

---

### Problem 24: Overflow in Multiplication
**Can 127 × 2 be represented in 8-bit 2's complement?**

**Solution:**
```
127 × 2 = 254

8-bit 2's complement range: -128 to +127
254 > 127

Answer: NO, overflow occurs (254 > 127)
```

---

## 10.7 Quick Practice Set

Solve these without looking at answers:

1. (1101.101)₂ = ?₁₀
2. (255)₁₀ = ?₁₆
3. -34 in 8-bit 2's complement = ?
4. What is the range of 5-bit 2's complement?
5. Does 60 + 70 overflow in 8-bit 2's complement?
6. Convert 0x3F800000 to decimal (IEEE 754 single)
7. (567)₈ + (234)₈ = ?₈
8. BCD of 79 = ?
9. Gray code of 9 = ?
10. Even parity of 1010101 = ?

<details>
<summary>Quick Answers</summary>

1. 13.625
2. FF
3. 11011110
4. -16 to +15
5. YES (130 > 127)
6. 1.0
7. 1023₈
8. 0111 1001
9. 1101 (9 = 1001, Gray = 1101)
10. 0 (already 4 ones, even)

</details>

---

## 🔜 Next Module
[Module 11: Previous Year Questions →](../11_Previous_Year_Questions/)
