# 📖 Module 6: Floating Point Representation (IEEE 754)

## 🎯 Learning Objectives

After completing this module, you will:
- Understand the IEEE 754 standard completely
- Convert between decimal and IEEE 754 format
- Handle special values (infinity, NaN, denormalized)
- Solve GATE-level floating point problems

---

## 6.1 Why Floating Point?

### Limitations of Fixed Point:
- Limited range for a given number of bits
- Can't represent very large or very small numbers
- Trade-off between range and precision

### Floating Point Advantages:
- Wide range of values
- Scientific notation in binary
- Standardized (IEEE 754)

### Scientific Notation Analogy:
```
Decimal: 6.022 × 10²³ (Avogadro's number)
         ↑      ↑  ↑
      Mantissa Base Exponent

Binary: 1.01 × 2⁵
        ↑    ↑ ↑
     Mantissa Base Exponent
```

---

## 6.2 IEEE 754 Standard Overview

### Two Main Formats:

| Property | Single Precision | Double Precision |
|----------|-----------------|------------------|
| Total Bits | 32 | 64 |
| Sign (S) | 1 bit | 1 bit |
| Exponent (E) | 8 bits | 11 bits |
| Mantissa (M) | 23 bits | 52 bits |
| Bias | 127 | 1023 |
| Range | ±3.4 × 10³⁸ | ±1.8 × 10³⁰⁸ |
| Precision | ~7 digits | ~16 digits |

### Bit Layout (Single Precision):
```
┌─────┬──────────────┬─────────────────────────────────────┐
│  S  │   Exponent   │              Mantissa               │
├─────┼──────────────┼─────────────────────────────────────┤
│ 31  │ 30      23   │ 22                              0   │
│ 1   │    8 bits    │             23 bits                 │
└─────┴──────────────┴─────────────────────────────────────┘
```

---

## 6.3 IEEE 754 Single Precision (32-bit)

### Structure:
```
S = Sign bit (0 = positive, 1 = negative)
E = Exponent (8 bits, biased by 127)
M = Mantissa/Significand (23 bits, normalized)
```

### Value Calculation:
```
For normalized numbers (E ≠ 0 and E ≠ 255):

Value = (-1)^S × 1.M × 2^(E-127)

Where:
- 1.M is the "hidden bit" representation
- E-127 gives the true (unbiased) exponent
```

### Bias Explanation:
```
Why bias 127?
- 8-bit exponent: values 0 to 255
- Bias = 127 allows range: -126 to +127 (actual exponents)
- Makes comparison easier (just compare bit patterns)

Actual exponent = Stored exponent - 127
Stored exponent = Actual exponent + 127
```

---

## 6.4 Converting Decimal to IEEE 754

### Step-by-Step Algorithm:

**Step 1**: Determine the sign bit
**Step 2**: Convert to binary
**Step 3**: Normalize (1.xxx × 2ⁿ form)
**Step 4**: Calculate biased exponent
**Step 5**: Extract mantissa (without hidden bit)

### Example 1: Convert -13.625 to IEEE 754 Single Precision

**Step 1**: Sign
```
Negative → S = 1
```

**Step 2**: Convert to Binary
```
13 = 1101₂
0.625 = 0.101₂  (0.625 × 2 = 1.25 → 1
                 0.25 × 2 = 0.5  → 0
                 0.5 × 2 = 1.0   → 1)

13.625 = 1101.101₂
```

**Step 3**: Normalize
```
1101.101 = 1.101101 × 2³
            ↑
        Hidden bit
```

**Step 4**: Calculate Exponent
```
Actual exponent = 3
Biased exponent = 3 + 127 = 130 = 10000010₂
```

**Step 5**: Extract Mantissa
```
1.101101 → Mantissa = 10110100000000000000000 (23 bits)
   └─────────────────────────────────────────────┘
```

**Final Answer**:
```
S = 1
E = 10000010
M = 10110100000000000000000

IEEE 754: 1 10000010 10110100000000000000000
Hex: 0xC15A0000
```

### Example 2: Convert 0.15625 to IEEE 754

**Step 1**: Sign = 0 (positive)

**Step 2**: Convert to Binary
```
0.15625 × 2 = 0.3125 → 0
0.3125 × 2 = 0.625  → 0
0.625 × 2 = 1.25    → 1
0.25 × 2 = 0.5      → 0
0.5 × 2 = 1.0       → 1

0.15625 = 0.00101₂
```

**Step 3**: Normalize
```
0.00101 = 1.01 × 2⁻³
```

**Step 4**: Exponent
```
Actual = -3
Biased = -3 + 127 = 124 = 01111100₂
```

**Step 5**: Mantissa
```
1.01 → M = 01000000000000000000000
```

**Final Answer**:
```
0 01111100 01000000000000000000000
Hex: 0x3E200000
```

---

## 6.5 Converting IEEE 754 to Decimal

### Algorithm:
```
1. Extract S, E, M
2. If E = 0 and M = 0 → Zero
3. If E = 255 and M = 0 → Infinity
4. If E = 255 and M ≠ 0 → NaN
5. Otherwise: Value = (-1)^S × 1.M × 2^(E-127)
```

### Example: Convert 0x42480000 to Decimal

**Step 1**: Convert to Binary
```
0x42480000 = 0100 0010 0100 1000 0000 0000 0000 0000
```

**Step 2**: Extract Components
```
S = 0
E = 10000100 = 132
M = 10010000000000000000000
```

**Step 3**: Calculate Value
```
Actual exponent = 132 - 127 = 5
Mantissa with hidden bit = 1.1001

Value = (-1)⁰ × 1.1001₂ × 2⁵
      = 1 × 1.5625 × 32
      = 50.0
```

**Answer**: 50.0

---

## 6.6 Special Values in IEEE 754

### Summary Table:

| Exponent (E) | Mantissa (M) | Value |
|--------------|--------------|-------|
| 0 | 0 | ±0 (signed zero) |
| 0 | ≠ 0 | Denormalized number |
| 1 to 254 | Any | Normalized number |
| 255 | 0 | ±Infinity |
| 255 | ≠ 0 | NaN (Not a Number) |

### Representations:

**Positive Zero**:
```
0 00000000 00000000000000000000000
```

**Negative Zero**:
```
1 00000000 00000000000000000000000
```

**Positive Infinity**:
```
0 11111111 00000000000000000000000
Hex: 0x7F800000
```

**Negative Infinity**:
```
1 11111111 00000000000000000000000
Hex: 0xFF800000
```

**NaN (one example)**:
```
0 11111111 10000000000000000000000
Hex: 0x7FC00000 (quiet NaN)
```

---

## 6.7 Denormalized Numbers

### Purpose:
Fill the gap between zero and smallest normalized number (gradual underflow).

### Format:
```
When E = 0:
Value = (-1)^S × 0.M × 2^(-126)
        ↑
    No hidden bit!
```

### Range:
```
Smallest denormalized (positive):
0 00000000 00000000000000000000001
= 2⁻²³ × 2⁻¹²⁶ = 2⁻¹⁴⁹ ≈ 1.4 × 10⁻⁴⁵

Largest denormalized (positive):
0 00000000 11111111111111111111111
= (1 - 2⁻²³) × 2⁻¹²⁶ ≈ 1.2 × 10⁻³⁸
```

### Smallest Normalized:
```
0 00000001 00000000000000000000000
= 1.0 × 2⁻¹²⁶ ≈ 1.18 × 10⁻³⁸
```

---

## 6.8 Range and Precision

### Single Precision Range:
```
Largest positive: 
  0 11111110 11111111111111111111111
  = (2 - 2⁻²³) × 2¹²⁷ ≈ 3.4 × 10³⁸

Smallest positive (normalized):
  0 00000001 00000000000000000000000
  = 1.0 × 2⁻¹²⁶ ≈ 1.18 × 10⁻³⁸
```

### Double Precision Range:
```
Largest: ≈ 1.8 × 10³⁰⁸
Smallest normalized: ≈ 2.2 × 10⁻³⁰⁸
```

### Precision:
```
Single: 23 + 1 = 24 significant bits ≈ 7 decimal digits
Double: 52 + 1 = 53 significant bits ≈ 16 decimal digits
```

---

## 6.9 Floating Point Arithmetic

### Addition/Subtraction Algorithm:
1. Align exponents (shift smaller number's mantissa right)
2. Add/subtract mantissas
3. Normalize result
4. Round if necessary
5. Check for overflow/underflow

### Example: Add 1.5 × 2³ + 1.25 × 2¹

**Step 1**: Align exponents
```
1.25 × 2¹ = 0.0125 × 2³  (shift right by 2)
Actually: 1.25₁₀ = 1.01₂
1.01 × 2¹ → 0.0101 × 2³
```

**Step 2**: Add mantissas
```
1.1000 (1.5₂ × 2³)
+ 0.0101 (shifted)
────────
1.1101 × 2³
```

**Step 3**: Normalize
```
Already normalized (1.xxx form)
Result: 1.1101 × 2³ = 14.5₁₀
```

**Verification**: 
```
1.5 × 2³ = 1.5 × 8 = 12
1.25 × 2¹ = 1.25 × 2 = 2.5
Sum = 12 + 2.5 = 14.5
Binary: 1110.1₂ = 14.5 ✓
```

### Multiplication:
```
(M1 × 2^E1) × (M2 × 2^E2) = (M1 × M2) × 2^(E1+E2)
```

### Division:
```
(M1 × 2^E1) ÷ (M2 × 2^E2) = (M1 ÷ M2) × 2^(E1-E2)
```

---

## 6.10 Rounding Modes

### IEEE 754 Rounding Modes:
1. **Round to Nearest, ties to Even** (default)
2. **Round toward Zero** (truncate)
3. **Round toward +∞** (ceiling)
4. **Round toward -∞** (floor)

### Round to Nearest (Banker's Rounding):
```
If the value is exactly halfway, round to even.

Examples:
2.5 → 2 (round to even)
3.5 → 4 (round to even)
2.6 → 3
2.4 → 2
```

---

## 6.11 Floating Point Issues

### Representation Error:
```
0.1₁₀ cannot be exactly represented in binary!
0.1 = 0.000110011001100110011...₂ (repeating)
```

### Comparison Issues:
```
Never compare floats with ==
Use: |a - b| < epsilon
```

### Associativity Loss:
```
(a + b) + c ≠ a + (b + c) in floating point
Example with very different magnitudes
```

### Catastrophic Cancellation:
```
Subtracting nearly equal numbers loses precision
1.00000001 - 1.00000000 → significant digits lost
```

---

## 6.12 IEEE 754 Double Precision (64-bit)

### Structure:
```
┌───┬─────────────────┬──────────────────────────────────────────────────────┐
│ S │    Exponent     │                    Mantissa                          │
├───┼─────────────────┼──────────────────────────────────────────────────────┤
│ 63│ 62          52  │ 51                                               0   │
│ 1 │    11 bits      │                    52 bits                           │
└───┴─────────────────┴──────────────────────────────────────────────────────┘
```

### Calculations:
```
Value = (-1)^S × 1.M × 2^(E-1023)

Bias = 1023
Exponent range: -1022 to +1023
```

---

## 6.13 Quick Reference Formulas

### Single Precision (32-bit):
```
Value = (-1)^S × 1.M × 2^(E-127)

Bias = 127 = 2⁷ - 1
Exponent bits = 8
Mantissa bits = 23
```

### Double Precision (64-bit):
```
Value = (-1)^S × 1.M × 2^(E-1023)

Bias = 1023 = 2¹⁰ - 1
Exponent bits = 11
Mantissa bits = 52
```

### General Formula (for any precision):
```
Bias = 2^(k-1) - 1, where k = exponent bits
```

---

## 6.14 GATE-Level Problems

### Problem 1:
What is the IEEE 754 single precision representation of -12.5?

**Solution**:
```
Sign: 1 (negative)
12.5 = 1100.1₂ = 1.1001 × 2³
Exponent: 3 + 127 = 130 = 10000010
Mantissa: 10010000000000000000000

Answer: 1 10000010 10010000000000000000000
Hex: 0xC1480000
```

### Problem 2:
What decimal number does 0x3FC00000 represent?

**Solution**:
```
0x3FC00000 = 0011 1111 1100 0000 ... 0000
S = 0
E = 01111111 = 127
M = 10000000000000000000000

Value = 1 × 1.1₂ × 2^(127-127)
      = 1.1₂ × 2⁰
      = 1.5₁₀

Answer: 1.5
```

### Problem 3:
What is the smallest positive normalized single precision number?

**Solution**:
```
E = 00000001 = 1 (minimum non-zero)
M = 00000000000000000000000

Value = 1.0 × 2^(1-127) = 2⁻¹²⁶
      ≈ 1.175 × 10⁻³⁸

Answer: 2⁻¹²⁶
```

### Problem 4:
How many distinct values can be represented in IEEE 754 single precision?

**Solution**:
```
Total bit patterns: 2³²
Unique numbers (excluding NaN): 2³² - 2²⁴ + 1
(Subtracting NaN representations, adding back one for "NaN")

Actually counting distinct numeric values:
- 2 zeros (+0, -0)
- Normalized: 2 × 254 × 2²³ = 2 × 254 × 2²³
- Denormalized: 2 × (2²³ - 1)
- 2 infinities

Total finite values ≈ 2³² - 2²⁴ - 2 + 2 = 2³² - 2²⁴
```

---

## 6.15 Common Mistakes to Avoid

❌ Forgetting the hidden bit in normalized numbers
❌ Using wrong bias (127 for single, 1023 for double)
❌ Confusing E=0 (denormalized) with E=255 (infinity/NaN)
❌ Not normalizing after calculations
❌ Ignoring the sign bit for zero

---

## 6.16 Summary

### Key Points:
✅ IEEE 754 = Sign + Biased Exponent + Mantissa
✅ Single: 1-8-23, Bias 127
✅ Double: 1-11-52, Bias 1023
✅ Normalized: E ∈ [1, 254], hidden bit = 1
✅ Denormalized: E = 0, hidden bit = 0
✅ Special: E = 255 → ∞ or NaN

### Conversion Checklist:
```
Decimal → IEEE 754:
1. Sign bit
2. Convert to binary
3. Normalize (1.xxx × 2^n)
4. Add bias to exponent
5. Write mantissa (drop leading 1)

IEEE 754 → Decimal:
1. Extract S, E, M
2. Check for special values
3. Apply formula: (-1)^S × 1.M × 2^(E-Bias)
```

---

## 📝 Practice Problems

1. Convert 5.5 to IEEE 754 single precision
2. What does 0x40400000 represent in decimal?
3. Find the IEEE 754 representation of -0.125
4. What is the next floating point number after 1.0?
5. Calculate 0.1 + 0.2 in binary (explain the famous issue)

<details>
<summary>Answers</summary>

1. 0 10000001 01100000000000000000000 (0x40B00000)
2. 3.0 (E=128, M=1.1 = 1.5 × 2 = 3)
3. 1 01111100 00000000000000000000000 (0xBE000000)
4. 1.0 + 2⁻²³ = 1.00000011920928955078125
5. 0.1 + 0.2 ≈ 0.30000000000000004 due to binary representation errors

</details>

---

## 🔜 Next Module
[Module 7: Fixed Point Representation →](../07_Fixed_Point_Representation/)
