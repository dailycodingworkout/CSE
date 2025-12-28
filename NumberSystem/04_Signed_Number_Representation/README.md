# 📖 Module 4: Signed Number Representation

## 🎯 Learning Objectives

After completing this module, you will:
- Understand all methods of representing signed numbers
- Master 2's complement (most important for GATE)
- Calculate ranges for n-bit representations
- Identify the representation method from given data

---

## 4.1 Why Signed Numbers?

### The Need:
- Computers need to represent both positive and negative numbers
- Binary has no inherent "minus sign"
- Different methods have different trade-offs

### Methods Covered:
1. **Sign-Magnitude** (Simple but rarely used)
2. **1's Complement** (Historical importance)
3. **2's Complement** (Most common - GATE favorite!)
4. **Excess-N (Biased)** (Used in IEEE 754 exponent)

---

## 4.2 Sign-Magnitude Representation

### Definition:
The leftmost bit (MSB) indicates sign, remaining bits represent magnitude.

```
n-bit number: [S | Magnitude (n-1 bits)]
S = 0 → Positive
S = 1 → Negative
```

### Example (8-bit):
```
+45 = 0 0101101  (0 for +, then 45 in 7 bits)
-45 = 1 0101101  (1 for -, then 45 in 7 bits)
```

### Range:
```
For n bits:
Minimum: -(2ⁿ⁻¹ - 1)
Maximum: +(2ⁿ⁻¹ - 1)
Total unique values: 2ⁿ - 1 (because of -0 and +0)
```

| Bits | Range | Unique Values |
|------|-------|---------------|
| 4 | -7 to +7 | 15 |
| 8 | -127 to +127 | 255 |
| 16 | -32767 to +32767 | 65535 |

### Problems:
1. **Two representations of zero**: +0 (00...0) and -0 (10...0)
2. **Complex arithmetic**: Addition/subtraction requires extra logic
3. **End-around carry needed** for subtraction

### 4-bit Sign-Magnitude Table:
| Binary | Decimal |
|--------|---------|
| 0000 | +0 |
| 0001 | +1 |
| 0010 | +2 |
| 0011 | +3 |
| 0100 | +4 |
| 0101 | +5 |
| 0110 | +6 |
| 0111 | +7 |
| 1000 | -0 |
| 1001 | -1 |
| 1010 | -2 |
| 1011 | -3 |
| 1100 | -4 |
| 1101 | -5 |
| 1110 | -6 |
| 1111 | -7 |

---

## 4.3 One's Complement Representation

### Definition:
- Positive numbers: Same as unsigned binary
- Negative numbers: Invert all bits of the positive number

```
-N = bitwise NOT(+N) = ~(+N)
```

### Example (8-bit):
```
+45 = 00101101
-45 = 11010010  (flip all bits)
```

### Finding Value of a Negative Number:
```
If MSB = 1 (negative):
  1. Invert all bits
  2. The result is the magnitude
  3. Add negative sign

Example: 11010010 (1's complement)
  Invert: 00101101 = 45
  Answer: -45
```

### Range:
```
For n bits:
Minimum: -(2ⁿ⁻¹ - 1)
Maximum: +(2ⁿ⁻¹ - 1)
Total unique values: 2ⁿ - 1
```

Same range as Sign-Magnitude!

### Problems:
1. **Two zeros**: +0 (00...0) and -0 (11...1)
2. **End-around carry**: Must add carry back to result

### 4-bit 1's Complement Table:
| Binary | Decimal |
|--------|---------|
| 0000 | +0 |
| 0001 | +1 |
| 0010 | +2 |
| 0011 | +3 |
| 0100 | +4 |
| 0101 | +5 |
| 0110 | +6 |
| 0111 | +7 |
| 1000 | -7 |
| 1001 | -6 |
| 1010 | -5 |
| 1011 | -4 |
| 1100 | -3 |
| 1101 | -2 |
| 1110 | -1 |
| 1111 | -0 |

### 1's Complement Addition (with end-around carry):
```
Add +5 and -3 in 4-bit 1's complement:

  +5 = 0101
  -3 = 1100
  ────────
       10001  (5 bits - carry out)
  +       1  (add carry back)
  ────────
       0010 = +2 ✓
```

---

## 4.4 Two's Complement Representation ⭐

### 🚨 MOST IMPORTANT FOR GATE!

### Definition:
- Positive numbers: Same as unsigned binary
- Negative numbers: 1's complement + 1

```
-N = ~(+N) + 1 = 2ⁿ - N
```

### Methods to Find 2's Complement:

#### Method 1: Invert and Add 1
```
+45 = 00101101
~45 = 11010010  (1's complement)
+1  = 11010011  (2's complement = -45)
```

#### Method 2: Shortcut - Flip After First 1
```
Starting from LSB:
1. Keep all bits up to and including the first 1
2. Flip all remaining bits

Example: +45 = 00101101
               └──────┘
Keep:          ___01
Flip:          110____
Result:        11010011 = -45 ✓
```

#### Method 3: Using 2ⁿ - N
```
For 8 bits: -45 = 2⁸ - 45 = 256 - 45 = 211 = 11010011
```

### Finding Value of a 2's Complement Number:

```
If MSB = 0 → Positive, read as normal
If MSB = 1 → Negative:
  Method 1: Take 2's complement, add negative sign
  Method 2: -2ⁿ⁻¹ + (remaining bits as positive)
```

### Example:
```
Number: 11010011 (8-bit 2's complement)

Method 1:
  Take 2's complement: 00101101 = 45
  Answer: -45

Method 2 (Weighted Sum):
  = -128 + 64 + 0 + 16 + 0 + 0 + 2 + 1
  = -128 + 83
  = -45 ✓
```

### Range:
```
For n bits:
Minimum: -2ⁿ⁻¹
Maximum: +(2ⁿ⁻¹ - 1)
Total unique values: 2ⁿ (NO duplicate zero!)
```

| Bits | Range | Min | Max |
|------|-------|-----|-----|
| 4 | 16 values | -8 | +7 |
| 8 | 256 values | -128 | +127 |
| 16 | 65536 values | -32768 | +32767 |
| 32 | 2³² values | -2³¹ | +2³¹-1 |

### 4-bit 2's Complement Table:
| Binary | Decimal | Notes |
|--------|---------|-------|
| 0000 | 0 | Zero |
| 0001 | +1 | |
| 0010 | +2 | |
| 0011 | +3 | |
| 0100 | +4 | |
| 0101 | +5 | |
| 0110 | +6 | |
| 0111 | +7 | Maximum positive |
| 1000 | -8 | Minimum (special!) |
| 1001 | -7 | |
| 1010 | -6 | |
| 1011 | -5 | |
| 1100 | -4 | |
| 1101 | -3 | |
| 1110 | -2 | |
| 1111 | -1 | |

### Advantages of 2's Complement:
1. **Only one zero** (unique representation)
2. **Simple arithmetic** (add directly, even for subtraction)
3. **Same adder circuit** for both addition and subtraction
4. **No end-around carry** needed

### The Special Case: Most Negative Number
```
In n-bit 2's complement:
  -2ⁿ⁻¹ has NO positive counterpart!
  
Example (4-bit): -8 = 1000
  2's complement of 1000:
  ~1000 = 0111
  +1    = 1000  (back to -8!)
  
This means: -(-8) = -8 in 4-bit 2's complement!
This can cause overflow if not handled properly.
```

---

## 4.5 Comparison of Signed Representations

| Feature | Sign-Magnitude | 1's Complement | 2's Complement |
|---------|---------------|----------------|----------------|
| Zero representations | 2 (+0, -0) | 2 (+0, -0) | 1 |
| Range (n-bit) | -(2ⁿ⁻¹-1) to +(2ⁿ⁻¹-1) | -(2ⁿ⁻¹-1) to +(2ⁿ⁻¹-1) | -2ⁿ⁻¹ to +(2ⁿ⁻¹-1) |
| Unique values | 2ⁿ-1 | 2ⁿ-1 | 2ⁿ |
| Addition complexity | High | Medium | Low |
| Most negative | -(2ⁿ⁻¹-1) | -(2ⁿ⁻¹-1) | -2ⁿ⁻¹ |
| Used in | - | - | Modern computers |

### Visual Comparison (4-bit):
```
             Sign-Mag     1's Comp     2's Comp
Binary  →    Decimal      Decimal      Decimal
0000         +0           +0           0
0001         +1           +1           +1
0010         +2           +2           +2
0011         +3           +3           +3
0100         +4           +4           +4
0101         +5           +5           +5
0110         +6           +6           +6
0111         +7           +7           +7
1000         -0           -7           -8  ← Different!
1001         -1           -6           -7
1010         -2           -5           -6
1011         -3           -4           -5
1100         -4           -3           -4
1101         -5           -2           -3
1110         -6           -1           -2
1111         -7           -0           -1
```

---

## 4.6 Excess-N (Biased) Representation

### Definition:
Add a bias N to the actual value, then store as unsigned.

```
Stored value = Actual value + Bias
Actual value = Stored value - Bias
```

### Common Biases:
- **Excess-128** (for 8-bit): Bias = 128
- **Excess-127** (IEEE 754 single): Bias = 127
- **Excess-1023** (IEEE 754 double): Bias = 1023

### Example: Excess-8 (4-bit)
```
Actual -8 → Stored: -8 + 8 = 0 = 0000
Actual 0  → Stored: 0 + 8 = 8 = 1000
Actual +7 → Stored: 7 + 8 = 15 = 1111
```

### 4-bit Excess-8 Table:
| Binary | Stored | Actual |
|--------|--------|--------|
| 0000 | 0 | -8 |
| 0001 | 1 | -7 |
| ... | ... | ... |
| 0111 | 7 | -1 |
| 1000 | 8 | 0 |
| 1001 | 9 | +1 |
| ... | ... | ... |
| 1111 | 15 | +7 |

### Why Use Biased Representation?
1. **Comparison is simple**: Just compare as unsigned numbers
2. **No special zero handling**: Zero has a non-zero representation
3. **Used in IEEE 754**: For exponent comparison

---

## 4.7 Sign Extension

### Definition:
Increasing the number of bits while preserving the value and sign.

### For 2's Complement:
```
Extend by copying the sign bit (MSB)

Example: Extend 4-bit to 8-bit
+5 = 0101 → 00000101
-5 = 1011 → 11111011
```

### Why It Works:
```
-5 in 4-bit: 1011 = -8 + 4 + 0 + 1 = -5
-5 in 8-bit: 11111011 = -128 + 64 + 32 + 16 + 8 + 0 + 2 + 1
           = -128 + 123 = -5 ✓
```

### For Sign-Magnitude:
```
Copy sign bit, pad magnitude with zeros

Example: Extend 4-bit to 8-bit
+5 = 0101 → 00000101
-5 = 1101 → 10000101
```

---

## 4.8 Determining the Representation

### Given a binary number, how to find its decimal value?

**Step 1**: Identify the representation system
**Step 2**: Apply the appropriate conversion

### Example: What is 1010 in different systems?

| Representation | Calculation | Value |
|---------------|-------------|-------|
| Unsigned | 8+2 | 10 |
| Sign-Magnitude | -(2) | -2 |
| 1's Complement | -(~1010) = -(0101) | -5 |
| 2's Complement | -8+2 | -6 |

---

## 4.9 Range Calculation Summary

### Quick Reference Table:

| Representation | n-bit Range | Formula |
|---------------|-------------|---------|
| **Unsigned** | 0 to 2ⁿ-1 | [0, 2ⁿ-1] |
| **Sign-Magnitude** | -(2ⁿ⁻¹-1) to +(2ⁿ⁻¹-1) | ±(2ⁿ⁻¹-1) |
| **1's Complement** | -(2ⁿ⁻¹-1) to +(2ⁿ⁻¹-1) | ±(2ⁿ⁻¹-1) |
| **2's Complement** | -2ⁿ⁻¹ to +(2ⁿ⁻¹-1) | [-2ⁿ⁻¹, 2ⁿ⁻¹-1] |
| **Excess-K** | -K to (2ⁿ-1-K) | Shifted by K |

### Memory Aid:
```
2's complement has:
- ONE EXTRA negative number
- ONE FEWER positive number
- Asymmetric range!

Example (8-bit):
Signed: -128 to +127 (256 values)
        |→ 128 negatives, 1 zero, 127 positives
```

---

## 4.10 GATE Important Problems

### Problem 1: Range Question
**Q**: The range of signed integers in 8-bit 2's complement is?

**A**: -128 to +127 = -2⁷ to +(2⁷-1)

### Problem 2: Representation Identification
**Q**: In which representation does 1111 equal -0?

**A**: 1's Complement. 

In 1's complement: 1111 = -(~1111) = -(0000) = -0

Note: In sign-magnitude, 1111 = -(111) = -7, not -0. The sign-magnitude representation of -0 is 1000.

### Problem 3: Finding 2's Complement
**Q**: What is the 2's complement of 01100100 (8-bit)?

**A**: 
```
01100100 = 100
~01100100 = 10011011
+1        = 10011100

Or shortcut: 01100100
Keep from right until first 1: ___00100
Flip rest: 100111__
Answer: 10011100 = -100
```

### Problem 4: Special Case
**Q**: What happens when you negate -128 in 8-bit 2's complement?

**A**: 
```
-128 = 10000000
2's complement: ~10000000 + 1 = 01111111 + 1 = 10000000
Result: Still -128! (Overflow case)
```

---

## 4.11 Summary

### Key Points to Remember:
✅ 2's complement is the most important - used in all modern computers
✅ 2's complement has one extra negative number
✅ Only 2's complement has a unique zero
✅ Sign extension: copy the MSB
✅ Most negative number in 2's complement is its own 2's complement

### Conversion Quick Reference:
```
Positive → Negative (2's Complement):
Method 1: Invert all bits, add 1
Method 2: Keep bits from right until first 1, flip rest
Method 3: 2ⁿ - number

Negative → Value (2's Complement):
Method 1: Invert all bits, add 1, negate
Method 2: -2ⁿ⁻¹ + (remaining bits)
```

---

## 📝 Practice Problems

1. Convert -50 to 8-bit 2's complement
2. What is the decimal value of 10110011 in 2's complement?
3. Find the range of 6-bit 2's complement numbers
4. Sign extend 1010 (4-bit 2's complement) to 8 bits
5. What value has the same 2's complement representation as itself?

<details>
<summary>Answers</summary>

1. 50 = 00110010, -50 = 11001110
2. -128 + 48 + 2 + 1 = -77
3. -32 to +31
4. 11111010
5. 0 (and the most negative number, which equals itself when negated)

</details>

---

## 🔜 Next Module
[Module 5: Arithmetic Operations →](../05_Arithmetic_Operations/)
