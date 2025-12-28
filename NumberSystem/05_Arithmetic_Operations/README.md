# 📖 Module 5: Arithmetic Operations in Binary

## 🎯 Learning Objectives

After completing this module, you will:
- Perform binary addition and subtraction
- Understand arithmetic in different signed representations
- Detect and handle overflow conditions
- Master multiplication and division techniques

---

## 5.1 Binary Addition

### Basic Rules:
```
0 + 0 = 0        (no carry)
0 + 1 = 1        (no carry)
1 + 0 = 1        (no carry)
1 + 1 = 10       (0 with carry 1)
1 + 1 + 1 = 11   (1 with carry 1)
```

### Example: Add 1011 + 1101 (Unsigned)
```
    1 1 1 1      ← Carries
      1 0 1 1    (11)
    + 1 1 0 1    (13)
    ─────────
    1 1 0 0 0    (24)
```

### Verification:
11 + 13 = 24 ✓

---

## 5.2 Binary Subtraction

### Method 1: Direct Subtraction (Borrow Method)
```
0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
0 - 1 = 1 (with borrow from next position)
```

### Example: 1101 - 0111
```
      1 1 0 1    (13)
    - 0 1 1 1    (7)
    ─────────
      0 1 1 0    (6)

Working:
Position 0: 1 - 1 = 0
Position 1: 0 - 1 → borrow → 10 - 1 = 1
Position 2: 0 - 1 → borrow → 10 - 1 = 1
Position 3: 0 - 0 = 0
```

### Method 2: Using 2's Complement (Preferred!)
```
A - B = A + (-B) = A + (2's complement of B)
```

### Example: 1101 - 0111 using 2's complement
```
A = 1101 (13)
B = 0111 (7)
-B = 1001 (2's complement of 0111)

  1 1 0 1
+ 1 0 0 1
─────────
1 0 1 1 0  → Discard carry → 0110 (6) ✓
```

---

## 5.3 2's Complement Addition

### Rules:
1. Add numbers as unsigned binary
2. Discard any carry out from MSB
3. Result is correct if no overflow

### Case 1: Both Positive
```
  +5 = 0101
  +3 = 0011
  ─────────
  +8 = 1000  ← Wait! MSB is 1, this looks negative!
  
But we only have 4 bits, so 1000 = -8 in 2's complement
This is OVERFLOW! (Result can't fit in 4 bits for signed)
```

### Case 2: Both Negative
```
  -3 = 1101
  -2 = 1110
  ─────────
1 1011  ← Discard carry
  -5 = 1011 ✓
  
Verify: -8 + 4 + 2 + 1 = -5 ✓
```

### Case 3: Positive + Negative
```
  +5 = 0101
  -3 = 1101
  ─────────
1 0010  ← Discard carry
  +2 = 0010 ✓
```

### Case 4: Negative + Positive
```
  -5 = 1011
  +3 = 0011
  ─────────
  1110 = -2 ✓
  
Verify: -8 + 4 + 2 = -2 ✓
```

---

## 5.4 Overflow Detection ⭐

### When Does Overflow Occur?
```
Overflow happens when:
1. Adding two positive numbers gives negative result
2. Adding two negative numbers gives positive result

Overflow NEVER happens when:
- Adding numbers of different signs
```

### Method 1: Sign Bit Check
```
Overflow = (Sign of A = Sign of B) AND (Sign of Result ≠ Sign of A)
```

### Method 2: Carry Comparison
```
Overflow = Cₙ ⊕ Cₙ₋₁
         = (Carry into MSB) XOR (Carry out of MSB)
```

### Example: Overflow Detection
```
4-bit 2's complement: range -8 to +7

Case 1: 5 + 4 = 9 (overflow!)
  0101  (+5)
+ 0100  (+4)
──────
  1001  (-7 in 2's complement)

Signs: Both positive, result negative → OVERFLOW!
Carries: Cₙ₋₁ = 1, Cₙ = 0 → 1 ⊕ 0 = 1 → OVERFLOW!

Case 2: -6 + -4 = -10 (overflow!)
  1010  (-6)
+ 1100  (-4)
──────
1 0110  (+6, after discarding carry)

Signs: Both negative, result positive → OVERFLOW!
```

---

## 5.5 1's Complement Arithmetic

### Addition with End-Around Carry:
```
If there's a carry out, add it back to the result.
```

### Example: -3 + 5 in 1's complement
```
-3 = 1100  (1's complement)
+5 = 0101

  1100
+ 0101
──────
1 0001  ← Carry out = 1

Add end-around carry:
  0001
+    1
──────
  0010 = +2 ✓
```

### Example: -3 + -2 in 1's complement
```
-3 = 1100
-2 = 1101

  1100
+ 1101
──────
1 1001  ← Carry out = 1

Add end-around carry:
  1001
+    1
──────
  1010 = -(0101) = -5 ✓
```

---

## 5.6 Binary Multiplication

### Method 1: Repeated Addition
```
5 × 3 = 5 + 5 + 5 = 15
```

### Method 2: Shift and Add (Paper Method)
```
     1011  (multiplicand = 11)
   × 1101  (multiplier = 13)
   ──────
     1011  (1011 × 1)
    0000   (1011 × 0, shifted)
   1011    (1011 × 1, shifted)
  1011     (1011 × 1, shifted)
  ────────
 10001111  (143 = 11 × 13) ✓
```

### Result Size:
```
n-bit × m-bit = (n+m)-bit result maximum
```

### Important for GATE:
```
For n-bit × n-bit unsigned:
- Maximum result: (2ⁿ-1)² ≈ 2²ⁿ
- Needs 2n bits to store

For n-bit × n-bit signed:
- Need 2n bits (or 2n-1 depending on representation)
```

---

## 5.7 Multiplication Algorithms

### Booth's Algorithm (For Signed Multiplication):

Used to handle negative numbers in multiplication efficiently.

**Key Insight**: Examines pairs of bits to decide:
- Add multiplicand
- Subtract multiplicand  
- Do nothing (just shift)

**Booth's Encoding**:
| Bit pair (current, previous) | Action |
|------------------------------|--------|
| 00 | 0 (no operation) |
| 01 | +1 (add multiplicand) |
| 10 | -1 (subtract multiplicand) |
| 11 | 0 (no operation) |

### Example: Multiply -3 × 2 using Booth's Algorithm

```
-3 = 1101 (4-bit 2's complement)
+2 = 0010 (4-bit)

Steps involve examining bit pairs and performing add/subtract/shift operations.
(Detailed algorithm steps shown in advanced sections)

Result: 11111010 = -6 ✓
```

---

## 5.8 Binary Division

### Method: Repeated Subtraction
```
13 ÷ 3:
13 - 3 = 10  (count 1)
10 - 3 = 7   (count 2)
7 - 3 = 4    (count 3)
4 - 3 = 1    (count 4)
1 < 3        (stop)

Quotient = 4, Remainder = 1
13 = 3 × 4 + 1 ✓
```

### Method: Long Division (Shift and Subtract)
```
       0100  ← Quotient
     ──────
11 | 1101   (3 | 13)
     11     (3)
     ───
      001   (1 < 3, bring down)
      00    (0)
      ───
       01   (1 = remainder)
```

### Result Properties:
```
Dividend = Divisor × Quotient + Remainder

For n-bit ÷ m-bit:
- Quotient: at most n bits
- Remainder: at most m bits
```

---

## 5.9 Division Algorithms

### Restoring Division:
1. Subtract divisor from partial remainder
2. If result is negative, restore (add back divisor)
3. Shift and repeat

### Non-Restoring Division:
1. Subtract or add divisor based on sign
2. If partial remainder ≥ 0: quotient bit = 1, next: subtract
3. If partial remainder < 0: quotient bit = 0, next: add

---

## 5.10 Arithmetic with Octal and Hexadecimal

### Octal Addition:
```
Same as decimal, but carry at 8

  536₈
+ 247₈
──────
 1005₈

Working:
6 + 7 = 13 = 8 + 5 → write 5, carry 1
3 + 4 + 1 = 8 = 8 + 0 → write 0, carry 1
5 + 2 + 1 = 8 = 8 + 0 → write 0, carry 1
Carry = 1

Verify: 350 + 167 = 517 (in decimal) = 1005₈ ✓
```

### Hexadecimal Addition:
```
Same as decimal, but carry at 16

  A9F₁₆
+ 5B2₁₆
───────
 1051₁₆

Working:
F + 2 = 15 + 2 = 17 = 16 + 1 → write 1, carry 1
9 + B + 1 = 9 + 11 + 1 = 21 = 16 + 5 → write 5, carry 1
A + 5 + 1 = 10 + 5 + 1 = 16 = 16 + 0 → write 0, carry 1
Carry = 1

Verify: 2719 + 1458 = 4177 = 1051₁₆ ✓
```

---

## 5.11 BCD Arithmetic

### BCD Addition:
```
Rules:
1. Add as normal binary
2. If result > 9 or carry out, add 6 (0110) to correct

Example: 25 + 47 = 72

  0010 0101  (BCD 25)
+ 0100 0111  (BCD 47)
───────────
  0110 1100  ← Second nibble = 12 > 9

Correction:
  0110 1100
+      0110  (add 6 to invalid digit)
───────────
  0111 0010  (BCD 72) ✓
```

### Why Add 6?
```
BCD has 16 codes but only 10 valid (0-9)
Gap of 6 between 9 (1001) and next tens digit
```

---

## 5.12 Shift Operations

### Left Shift:
```
Shift all bits left, fill with 0 on right
Effect: Multiply by 2

Example: 0011 << 1 = 0110
         (3 × 2 = 6) ✓
```

### Right Shift:
```
Logical Right Shift: Fill with 0 on left
Arithmetic Right Shift: Fill with sign bit (for signed numbers)

Logical:  1100 >>> 1 = 0110
Arithmetic: 1100 >> 1 = 1110 (preserving sign)
```

### Division and Multiplication by Powers of 2:
```
× 2ⁿ = Left shift by n positions
÷ 2ⁿ = Right shift by n positions (arithmetic for signed)

Example: 
24 × 4 = 24 × 2² = 24 << 2
11000 << 2 = 1100000 = 96 ✓
```

---

## 5.13 GATE Important Questions

### Q1: What is 5 - 7 in 4-bit 2's complement?
```
5 = 0101
7 = 0111 → -7 = 1001

  0101
+ 1001
──────
  1110 = -2 ✓
```

### Q2: Overflow occurs in which case? (4-bit 2's complement)
```
A) 3 + 4 = 7   → 0011 + 0100 = 0111 ✓ (no overflow)
B) 5 + 4 = 9   → 0101 + 0100 = 1001 (-7) OVERFLOW!
C) -3 + 5 = 2  → 1101 + 0101 = 10010 → 0010 ✓ (no overflow)
D) -4 - 5 = -9 → 1100 + 1011 = 10111 → 0111 (+7) OVERFLOW!
```

### Q3: Result of -128 × 2 in 8-bit 2's complement?
```
-128 = 10000000
× 2 = left shift = 00000000 = 0 (OVERFLOW!)

The correct answer is 0 due to overflow.
```

---

## 5.14 Summary

### Addition Rules:
```
2's Complement: Add directly, discard carry out
1's Complement: Add, then add end-around carry
```

### Overflow Detection (2's Complement):
```
Overflow = (same input signs) AND (different result sign)
        = Cₙ₋₁ ⊕ Cₙ (carry into MSB XOR carry out of MSB)
```

### Key Points:
✅ Subtraction = Addition of 2's complement
✅ Overflow only possible with same-sign operands
✅ Left shift = ×2, Right shift = ÷2
✅ BCD addition: add 6 if result > 9

---

## 📝 Practice Problems

1. Add 10110 and 01101 in binary
2. Subtract 01011 from 11001 in 2's complement
3. Detect if 0111 + 0100 causes overflow (4-bit 2's complement)
4. Multiply 1011 × 101 using shift-and-add
5. Divide 10011 by 11 using binary long division

<details>
<summary>Answers</summary>

1. 100011 (22 + 13 = 35)
2. 11001 + 10101 = 101110 → 01110 (14, with carry discarded)
3. 0111 + 0100 = 1011 (-5 in 2's complement) - YES overflow (two positives gave negative)
4. 110111 (55 = 11 × 5)
5. Quotient = 0110 (6), Remainder = 1 (19 = 3 × 6 + 1)

</details>

---

## 🔜 Next Module
[Module 6: Floating Point Representation →](../06_Floating_Point_Representation/)
