# 📖 Module 8: Overflow and Underflow

## 🎯 Learning Objectives

After completing this module, you will:
- Understand what causes overflow and underflow
- Master detection techniques for different representations
- Handle overflow conditions in different number systems
- Solve GATE-level overflow problems

---

## 8.1 What is Overflow?

### Definition:
**Overflow** occurs when an arithmetic operation produces a result that is too large (or too small for negative numbers) to be represented in the available number of bits.

```
Example: 4-bit unsigned addition
15 + 1 = 16

But 4 bits can only hold 0-15!
1111 + 0001 = 10000 (5 bits needed)
Result stored: 0000 (incorrect!)
```

### Visual Representation:
```
Number line for 4-bit unsigned:
0 ────────────────────────► 15
  └─────────── Range ───────┘

16 is beyond the range → OVERFLOW
```

---

## 8.2 What is Underflow?

### Definition:
**Underflow** occurs when:
1. An arithmetic result is smaller than the smallest representable negative number (integer context)
2. A floating point result is closer to zero than the smallest representable positive number

### Integer Underflow:
```
4-bit signed (2's complement): range -8 to +7

-8 - 1 = -9
But -9 is outside the range!
1000 + 1111 = 10111 → 0111 = +7 (WRONG!)
```

### Floating Point Underflow:
```
When result is too close to zero to represent

Example: 10⁻⁴⁰ × 10⁻⁵ = 10⁻⁴⁵
If smallest representable is 10⁻³⁸, underflow occurs
```

---

## 8.3 Overflow in Unsigned Arithmetic

### Addition:
```
Overflow occurs when: Carry out of MSB = 1

Example (4-bit unsigned):
12 + 5 = 17 > 15 (max for 4 bits)

  1100  (12)
+ 0101  (5)
──────
 10001  ← Carry out = 1 → OVERFLOW!
 
Stored result: 0001 = 1 (incorrect)
```

### Subtraction:
```
Underflow (borrow out) when: Minuend < Subtrahend

Example (4-bit unsigned):
3 - 7 = -4 (negative, can't represent)

  0011  (3)
- 0111  (7)
──────
Borrow out → UNDERFLOW!

Using 2's complement method:
0011 + 1001 = 1100 = 12 (interpreted as unsigned, wrong for signed result)
```

### Detection:
```
Unsigned Addition: Overflow = Carry Out
Unsigned Subtraction: Underflow = Borrow Out
```

---

## 8.4 Overflow in Signed Arithmetic (2's Complement) ⭐

### When Overflow Occurs:
```
1. Positive + Positive = Negative → OVERFLOW
2. Negative + Negative = Positive → OVERFLOW

Overflow NEVER occurs when adding numbers of different signs!
```

### Examples (4-bit 2's complement, range: -8 to +7):

**Case 1: Positive + Positive = Negative**
```
+5 + +4 = +9 (outside range)

  0101  (+5)
+ 0100  (+4)
──────
  1001  = -7 (interpreted as 2's complement)

Both inputs positive, result negative → OVERFLOW!
```

**Case 2: Negative + Negative = Positive**
```
-5 + -4 = -9 (outside range)

  1011  (-5)
+ 1100  (-4)
──────
 10111  → 0111 = +7 (after discarding carry)

Both inputs negative, result positive → OVERFLOW!
```

**Case 3: Different Signs (No Overflow)**
```
+5 + -3 = +2

  0101  (+5)
+ 1101  (-3)
──────
 10010  → 0010 = +2 ✓

No overflow possible when signs differ!
```

---

## 8.5 Overflow Detection Methods

### Method 1: Sign Bit Comparison
```
Overflow = (Sign_A = Sign_B) AND (Sign_Result ≠ Sign_A)

In logic:
V = (A_n-1 ⊙ B_n-1) · (A_n-1 ⊕ S_n-1)

Where:
⊙ = XNOR (same signs check)
⊕ = XOR (different sign check)
· = AND
```

### Method 2: Carry Comparison ⭐ (GATE Favorite)
```
Overflow = Cₙ ⊕ Cₙ₋₁

Where:
Cₙ = Carry OUT of MSB (bit n-1)
Cₙ₋₁ = Carry INTO MSB (from bit n-2)
```

### Example:
```
+6 + +5 = +11 (overflow in 4-bit)

    0 1 1  ← Carries
  0 1 1 0  (+6)
+ 0 1 0 1  (+5)
──────────
  1 0 1 1  = -5 (wrong!)

Carry into MSB (Cₙ₋₁) = 1
Carry out of MSB (Cₙ) = 0

Overflow = 1 ⊕ 0 = 1 → OVERFLOW DETECTED!
```

### Truth Table for Overflow Detection:
| Cₙ₋₁ (into) | Cₙ (out) | Overflow |
|-------------|----------|----------|
| 0 | 0 | No |
| 0 | 1 | Yes |
| 1 | 0 | Yes |
| 1 | 1 | No |

---

## 8.6 Overflow in Other Representations

### Sign-Magnitude:
```
Overflow when: |Result| > 2^(n-1) - 1

Example (4-bit): max positive = 7
+5 + +3 = +8 > +7 → OVERFLOW
```

### 1's Complement:
```
Similar to 2's complement, but remember end-around carry!
After adding end-around carry, check for overflow.
```

### Excess-K (Biased):
```
Overflow when: Stored result < 0 or > 2^n - 1

Example (Excess-8, 4-bit):
+6 + +3 = +9
Stored: (6+8) + (3+8) - 8 = 14 + 11 - 8 = 17 > 15 → OVERFLOW
```

---

## 8.7 Overflow in Multiplication

### Unsigned Multiplication:
```
n-bit × n-bit = up to 2n-bit result

If only n bits available for result:
Overflow when result > 2^n - 1
```

### Signed Multiplication:
```
n-bit × n-bit (2's complement)
Maximum: (-2^(n-1)) × (-2^(n-1)) = 2^(2n-2) [positive]
Minimum: (-2^(n-1)) × (2^(n-1) - 1) = -2^(2n-2) + 2^(n-1) [negative]

Need 2n-1 or 2n bits for full result
```

### Special Case:
```
4-bit 2's complement: -8 × -1

-8 = 1000
-1 = 1111

-8 × -1 = +8

But +8 cannot be represented in 4 bits (max is +7)!
OVERFLOW!
```

---

## 8.8 Floating Point Overflow and Underflow

### Overflow:
```
When exponent too large to represent

IEEE 754 Single:
If E > 254 (biased) → Overflow
Result set to: ±Infinity
```

### Underflow:
```
When exponent too small (result too close to zero)

If actual exponent < -126 and can't be denormalized → Underflow
Result set to: 0 or smallest denormalized
```

### Example:
```
Single precision:
Largest: ≈ 3.4 × 10³⁸
Smallest positive normal: ≈ 1.18 × 10⁻³⁸

10⁴⁰ → OVERFLOW (set to +∞)
10⁻⁵⁰ → UNDERFLOW (set to denormal or 0)
```

---

## 8.9 Handling Overflow

### Method 1: Saturation
```
If overflow detected:
  If positive overflow: Result = Maximum value
  If negative overflow: Result = Minimum value

Example (4-bit signed):
+6 + +5 = +11 → saturate to +7
-5 + -6 = -11 → saturate to -8
```

### Method 2: Wraparound (Default)
```
Result wraps around modularly

Example (4-bit unsigned):
14 + 3 = 17 → 17 mod 16 = 1
```

### Method 3: Exception/Trap
```
Hardware generates interrupt/exception
Software handles the error
```

### Method 4: Extended Precision
```
Use more bits for intermediate results
Example: 16-bit operands, 32-bit accumulator
```

---

## 8.10 Range Calculations

### Quick Reference:

| Representation | n-bit Range | Overflow Condition |
|---------------|-------------|-------------------|
| Unsigned | 0 to 2ⁿ-1 | Result > 2ⁿ-1 or < 0 |
| Sign-Magnitude | ±(2ⁿ⁻¹-1) | |Result| > 2ⁿ⁻¹-1 |
| 1's Complement | ±(2ⁿ⁻¹-1) | |Result| > 2ⁿ⁻¹-1 |
| 2's Complement | -2ⁿ⁻¹ to 2ⁿ⁻¹-1 | Result > 2ⁿ⁻¹-1 or < -2ⁿ⁻¹ |

### Examples for 8 bits:
| Representation | Minimum | Maximum |
|---------------|---------|---------|
| Unsigned | 0 | 255 |
| Sign-Magnitude | -127 | +127 |
| 1's Complement | -127 | +127 |
| 2's Complement | -128 | +127 |

---

## 8.11 GATE-Level Problems

### Problem 1:
In 8-bit 2's complement, does 100 + 30 cause overflow?

**Solution:**
```
Range: -128 to +127
100 + 30 = 130 > 127 → YES, OVERFLOW!

Verification:
100 = 01100100
30  = 00011110
Sum = 10000010 = -126 (interpreted as 2's complement)

Both positive, result negative → OVERFLOW confirmed!
```

### Problem 2:
What is the carry-based overflow for: 1110 + 0011 (4-bit 2's complement)?

**Solution:**
```
  1110  (-2)
+ 0011  (+3)
──────

Working with carries:
Position 0: 0 + 1 = 1, C = 0
Position 1: 1 + 1 = 10, C = 1
Position 2: 1 + 0 + 1 = 10, C = 1  ← Carry into MSB
Position 3: 1 + 0 + 1 = 10, C = 1  ← Carry out of MSB

Cₙ₋₁ = 1 (carry into MSB)
Cₙ = 1 (carry out of MSB)

Overflow = 1 ⊕ 1 = 0 → NO OVERFLOW!

Result: 10001 → 0001 = +1
-2 + 3 = +1 ✓
```

### Problem 3:
In IEEE 754 single precision, what happens when computing 2¹²⁸?

**Solution:**
```
Maximum exponent (biased) = 254
Actual max exponent = 254 - 127 = 127
2¹²⁷ is representable, 2¹²⁸ is not.

2¹²⁸ → OVERFLOW → +Infinity
```

---

## 8.12 The Most Negative Number Problem

### In 2's Complement:
```
-2^(n-1) has no positive counterpart in n bits!

Example (4-bit): -8 = 1000
Negate: ~1000 + 1 = 0111 + 1 = 1000 = -8

So: -(-8) = -8 (still negative!)
This can cause overflow in certain operations.
```

### Practical Implications:
```
abs(-128) in 8-bit 2's complement:
Result should be +128, but max is +127
→ Overflow!

Many languages: abs(INT_MIN) is undefined behavior!
```

---

## 8.13 Preventing Overflow

### Compile-Time Checks:
```c
// Check before operation
if (a > INT_MAX - b) {
    // Overflow would occur
    handle_error();
} else {
    result = a + b;
}
```

### Using Wider Types:
```c
int a, b;
long long result = (long long)a + (long long)b;
// Check if result fits in int
```

### Saturating Arithmetic:
```c
// Hardware or library support
result = sat_add(a, b);  // Returns MAX if overflow
```

---

## 8.14 Summary

### Key Points:
✅ Overflow = result too large for representation
✅ Underflow = result too small (or too close to zero)
✅ 2's complement overflow: same-sign inputs, different-sign result
✅ Detection: V = Cₙ ⊕ Cₙ₋₁ (XOR of carries)

### Overflow Detection Quick Reference:
```
Unsigned: Carry out = 1
Signed (2's complement): Cₙ ⊕ Cₙ₋₁ = 1
                         OR (same input signs AND different result sign)
```

### Handling Options:
1. Saturation (clamp to max/min)
2. Wraparound (modular arithmetic)
3. Exception (interrupt/trap)
4. Extended precision

---

## 📝 Practice Problems

1. Does 70 + 80 overflow in 8-bit 2's complement?
2. Calculate the overflow flag for: 0110 + 0111 (4-bit 2's complement)
3. In 4-bit unsigned, what is 13 + 5?
4. What happens to -128 ÷ -1 in 8-bit 2's complement?
5. Detect overflow: 1000 + 1001 (4-bit 2's complement)

<details>
<summary>Answers</summary>

1. YES. 70 + 80 = 150 > 127. Result = 01000110 + 01010000 = 10010110 = -106
2. 0110 + 0111 = 1101. Carry into MSB = 1, Carry out = 0. V = 1 ⊕ 0 = 1 (OVERFLOW)
3. 13 + 5 = 18. 1101 + 0101 = 10010 → 0010 = 2 (with carry out = 1, overflow)
4. -128 ÷ -1 should = +128, but max is +127. OVERFLOW!
5. 1000 + 1001 = 10001 → 0001. Carry into MSB = 0, Carry out = 1. V = 0 ⊕ 1 = 1 (OVERFLOW). -8 + -7 = -15 (but shows as +1)

</details>

---

## 🔜 Next Module
[Module 9: Special Numbers and Codes →](../09_Special_Numbers/)
