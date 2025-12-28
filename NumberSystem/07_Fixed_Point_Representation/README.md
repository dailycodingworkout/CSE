# 📖 Module 7: Fixed Point Representation

## 🎯 Learning Objectives

After completing this module, you will:
- Understand fixed point number representation
- Master Q-format and scaling
- Compare fixed point with floating point
- Apply fixed point in embedded systems context

---

## 7.1 What is Fixed Point?

### Definition:
A fixed point number has a fixed number of digits before and after the radix point.

```
Fixed Point Format: IIII.FFFF
                    └──┘ └──┘
            Integer part  Fractional part
```

### Comparison with Floating Point:
| Feature | Fixed Point | Floating Point |
|---------|-------------|----------------|
| Radix point | Fixed position | Variable position |
| Range | Limited | Large |
| Precision | Uniform | Variable |
| Hardware | Simple | Complex |
| Speed | Fast | Slower |
| Use cases | DSP, embedded | General computing |

---

## 7.2 Fixed Point Notation

### General Format:
```
Qm.n or Qn

Where:
- m = number of integer bits (including sign)
- n = number of fractional bits
- Total bits = m + n (or m + n + 1 if sign is separate)
```

### Common Notations:

| Notation | Meaning | Example |
|----------|---------|---------|
| Q15 | 1 sign + 15 fractional bits | 16-bit, range: -1 to 0.99997 |
| Q7.8 | 7 integer + 8 fractional | 15-bit, range: -64 to 63.996 |
| Q0.15 | 0 integer + 15 fractional | Same as Q15 |

---

## 7.3 Fixed Point Representation

### Unsigned Fixed Point:

For an n-bit unsigned number with f fractional bits:
```
Value = Integer Value × 2^(-f)

Example: 8-bit number with 4 fractional bits (Q4.4)
Binary: 0101.1100
Value: 01011100₂ × 2⁻⁴
     = 92 × 0.0625
     = 5.75

Alternative: 4 + 1 + 0.5 + 0.25 = 5.75
```

### Signed Fixed Point (2's Complement):

```
Range for Qm.n format:
Min: -2^(m-1)
Max: 2^(m-1) - 2^(-n)

Example: Q3.4 (3 integer bits including sign, 4 fractional bits)
Total: 7 bits
Range: -4 to 3.9375
Resolution: 2⁻⁴ = 0.0625
```

---

## 7.4 Q-Format Deep Dive

### Q15 Format (Most Common in DSP):
```
Format: sfffffffffff (1 sign + 15 fractional bits)
Total: 16 bits
Range: -1 to (1 - 2⁻¹⁵) ≈ -1 to 0.99997

Value = stored_integer × 2⁻¹⁵
```

### Q7.8 Format:
```
Format: siiiiiii.ffffffff (1 sign + 7 integer + 8 fractional)
Total: 16 bits
Range: -128 to 127.99609375
Resolution: 2⁻⁸ = 0.00390625
```

### Conversion Formula:
```
To store value v in Qm.n format:
stored = round(v × 2^n)

To retrieve value from Qm.n:
actual = stored × 2^(-n)
```

### Example: Store 3.14159 in Q7.8
```
stored = round(3.14159 × 256)
       = round(804.24704)
       = 804
       = 0000001100100100₂

Retrieve: 804 × 2⁻⁸ = 3.140625
Error: 3.14159 - 3.140625 = 0.000965
```

---

## 7.5 Fixed Point Arithmetic

### Addition and Subtraction:
```
Rule: Same Q-format required, add/subtract directly

Example: Q7.8 + Q7.8
A = 3.5 = 896 (3.5 × 256)
B = 2.25 = 576 (2.25 × 256)
Sum = 896 + 576 = 1472
Result = 1472 × 2⁻⁸ = 5.75 ✓
```

### Different Q-Formats:
```
Before adding, align decimal points by shifting

Q7.8 + Q3.12:
Convert Q7.8 to Q3.12: left shift by 4
Or convert Q3.12 to Q7.8: right shift by 4
```

### Multiplication:
```
Rule: Q(m1.n1) × Q(m2.n2) = Q(m1+m2).(n1+n2)

Example: Q7.8 × Q7.8 = Q14.16 (30 bits needed!)

A = 3.5 (stored as 896 in Q7.8)
B = 2.0 (stored as 512 in Q7.8)
Product = 896 × 512 = 458752

This is in Q14.16 format
To convert back to Q7.8: right shift by 8
Result = 458752 >> 8 = 1792
Value = 1792 × 2⁻⁸ = 7.0 ✓
```

### Division:
```
Rule: Pre-shift dividend to maintain precision

Q7.8 ÷ Q7.8:
A = 7.0 (stored as 1792 in Q7.8)
B = 2.0 (stored as 512 in Q7.8)

To maintain Q7.8 result:
Result = (A << 8) / B
       = (1792 << 8) / 512
       = 458752 / 512
       = 896
Value = 896 × 2⁻⁸ = 3.5 ✓
```

---

## 7.6 Scaling and Overflow

### Scaling:
When result exceeds range, scale the values.

```
Problem: Q15 can only hold -1 to 1
Solution: Scale inputs by dividing

Example: Multiply 0.8 × 0.9 in Q15
Normal: 0.8 × 0.9 = 0.72 (fits in Q15)

Example: Add 0.8 + 0.9 in Q15
Normal: 0.8 + 0.9 = 1.7 (OVERFLOW!)
Solution: Scale both by 0.5 first
(0.4 + 0.45) × 2 = 0.85 × 2 = 1.7
Store 0.85, remember scale factor of 2
```

### Saturation Arithmetic:
```
Instead of wrapping on overflow, clamp to max/min

If result > MAX: result = MAX
If result < MIN: result = MIN

Example in Q15:
0.9 + 0.5 = 1.4 → saturate to 0.99997
```

---

## 7.7 Resolution and Precision

### Resolution:
```
Resolution = 2^(-n) for n fractional bits

Example:
Q15: resolution = 2⁻¹⁵ ≈ 0.00003
Q7.8: resolution = 2⁻⁸ = 0.00390625
```

### Quantization Error:
```
Maximum error = Resolution / 2

Example in Q7.8:
Max error = 0.00390625 / 2 = 0.001953125
```

### Choosing Q-Format:
```
For range R and precision P:
- Integer bits ≥ ceil(log₂(R)) + 1 (for sign)
- Fractional bits ≥ -log₂(P)

Example: Need range -10 to 10, precision 0.01
Integer bits: ceil(log₂(10)) + 1 = 4 + 1 = 5
Fractional bits: -log₂(0.01) ≈ 7
Total: Q5.7 (12 bits minimum)
```

---

## 7.8 Binary Point Placement

### Explicit vs Implicit:
```
Implicit (most common):
- No actual binary point in hardware
- Programmer tracks position
- Integer arithmetic used

Explicit:
- Special data types in some languages
- Hardware support in some DSPs
```

### Example: Representing 6.75 in 8 bits

**Q4.4 (4 integer, 4 fractional)**:
```
6.75 = 0110.1100₂
Stored: 01101100 = 108
Retrieve: 108 × 2⁻⁴ = 6.75 ✓
```

**Q3.5 (3 integer, 5 fractional)**:
```
6.75 × 32 = 216 = 11011000₂
But 216 > 127 (max for signed 8-bit)
OVERFLOW! Q3.5 can't hold 6.75
```

---

## 7.9 Fixed Point in Embedded Systems

### Why Use Fixed Point?
1. **No FPU**: Many microcontrollers lack floating point hardware
2. **Speed**: Integer operations are faster
3. **Power**: Less energy consumption
4. **Determinism**: Predictable timing

### Common Applications:
- Digital Signal Processing (DSP)
- Audio/Video processing
- Control systems
- Sensor data processing

### Example: Temperature Sensor
```
Sensor outputs 0-1023 (10-bit ADC)
Temperature range: -40°C to 85°C

Conversion to Q7.8:
temp_raw = adc_value
temp_celsius = (temp_raw - offset) × scale

Using fixed point:
scale_Q8 = ((85 - (-40)) × 256) / 1023 = 31.25
offset = value at -40°C
```

---

## 7.10 Comparison: Fixed vs Floating Point

### When to Use Fixed Point:
✅ Embedded systems without FPU
✅ Real-time systems requiring deterministic timing
✅ High-throughput signal processing
✅ Power-constrained applications

### When to Use Floating Point:
✅ Wide dynamic range needed
✅ Scientific computing
✅ When convenience is more important than performance
✅ Systems with FPU hardware

### Performance Comparison:
| Operation | Fixed (cycles) | Float (cycles) |
|-----------|----------------|----------------|
| Addition | 1 | 10-20 |
| Multiplication | 1-3 | 20-50 |
| Division | 10-20 | 50-100 |

*Approximate, varies by architecture*

---

## 7.11 GATE Relevance

### Types of Questions:
1. Convert decimal to fixed point format
2. Determine range and precision
3. Fixed point arithmetic
4. Choose appropriate Q-format for given requirements

### Example GATE Problem:
**Q**: In a Q3.4 format, what is the decimal equivalent of 1010110?

**Solution**:
```
Q3.4 = 3 integer bits + 4 fractional bits = 7 bits
1010110 = 1010.110₂ (place binary point after 3 bits)

But wait - is this signed?
If signed (2's complement): MSB = 1 means negative
1010.110 → signed value = -8 + 2 + 0.5 + 0.25 = -5.25

If unsigned: 1010.110 = 10 + 0.5 + 0.25 = 10.75

Answer depends on whether signed interpretation is used.
```

---

## 7.12 Summary

### Key Formulas:
```
Value = stored_integer × 2^(-fractional_bits)

Stored = round(value × 2^fractional_bits)

Range (signed Qm.n): [-2^(m-1), 2^(m-1) - 2^(-n)]

Resolution: 2^(-n)
```

### Key Points:
✅ Fixed point = integer representation with implied decimal point
✅ Q-format specifies bit allocation
✅ Addition: same format, add directly
✅ Multiplication: formats combine, may need right shift
✅ Watch for overflow - use saturation or scaling

---

## 📝 Practice Problems

1. Convert 5.625 to Q4.4 format (8 bits)
2. What is the range of Q3.12 format?
3. Multiply 2.5 × 1.5 in Q3.4 format
4. What Q-format is needed for range [-100, 100] with precision 0.001?
5. In Q7.8 format, what is stored for the value -3.5?

<details>
<summary>Answers</summary>

1. 5.625 × 16 = 90 = 01011010₂
2. Q3.12: range = [-4, 4 - 2⁻¹²] ≈ [-4, 3.99976]
3. 2.5 = 40 (Q3.4), 1.5 = 24 (Q3.4), product = 960 (Q6.8), shift right by 4 = 60 (Q3.4) = 3.75 ✓
4. Range needs 8 integer bits (7 + sign), precision needs 10 fractional bits → Q8.10 (18 bits)
5. -3.5 × 256 = -896 = 1111110010000000₂ (16-bit 2's complement)

</details>

---

## 🔜 Next Module
[Module 8: Overflow and Underflow →](../08_Overflow_Underflow/)
