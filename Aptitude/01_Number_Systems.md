# Chapter 1: Number Systems

> **The foundation of all computing and competitive math**

---

## 🎯 Why Study Number Systems?

- **GATE CSE/IT**: Directly tested + required for Digital Logic, Computer Organization
- **ESE**: Foundation for numerical ability section
- **Real Application**: Every computer operates on binary arithmetic

---

## 📚 Core Concepts

### 1.1 Types of Number Systems

| System | Base | Digits Used | Prefix | Example |
|--------|------|-------------|--------|---------|
| Binary | 2 | 0, 1 | 0b | 0b1010 = 10 |
| Octal | 8 | 0-7 | 0o | 0o12 = 10 |
| Decimal | 10 | 0-9 | None | 10 |
| Hexadecimal | 16 | 0-9, A-F | 0x | 0xA = 10 |

**💡 Analogy**: Think of bases like counting systems:
- Binary = Light switches (ON/OFF only)
- Octal = Octopus arms (8 options)
- Decimal = Human fingers (10 options)
- Hex = Extended hands (fingers + some letters)

---

### 1.2 Position Value Concept

Every digit's value = `digit × base^position`

**Position numbering**: Right-to-left, starting from 0

```
Example: (1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰
                 = 8 + 0 + 2 + 1 = 11₁₀
```

---

## 🔄 Conversions Master Guide

### 2.1 Any Base → Decimal

**Method**: Multiply each digit by base^position, sum all

```
(372)₈ → Decimal
= 3×8² + 7×8¹ + 2×8⁰
= 192 + 56 + 2
= 250₁₀

(2AF)₁₆ → Decimal
= 2×16² + 10×16¹ + 15×16⁰
= 512 + 160 + 15
= 687₁₀
```

**⚡ Trick for Binary**: Just add the powers of 2 where there's a 1
```
(11011)₂ = 2⁴ + 2³ + 2¹ + 2⁰ = 16 + 8 + 2 + 1 = 27
```

---

### 2.2 Decimal → Any Base

**Method**: Repeated division by target base, read remainders bottom-to-top

```
156₁₀ → Binary

156 ÷ 2 = 78  R 0  ↑
78  ÷ 2 = 39  R 0  │
39  ÷ 2 = 19  R 1  │ Read
19  ÷ 2 = 9   R 1  │ upward
9   ÷ 2 = 4   R 1  │
4   ÷ 2 = 2   R 0  │
2   ÷ 2 = 1   R 0  │
1   ÷ 2 = 0   R 1  │

Answer: 10011100₂
```

**⚡ Quick Trick for Decimal → Binary**:
Find largest power of 2 ≤ number, subtract, repeat
```
156 = 128 + 28 = 128 + 16 + 12 = 128 + 16 + 8 + 4
    = 2⁷ + 2⁴ + 2³ + 2²
    = 10011100₂
```

---

### 2.3 Binary ↔ Octal (⭐ Super Important)

**Secret**: Group binary digits in 3s (right to left)

| Binary Group | Octal |
|--------------|-------|
| 000 | 0 |
| 001 | 1 |
| 010 | 2 |
| 011 | 3 |
| 100 | 4 |
| 101 | 5 |
| 110 | 6 |
| 111 | 7 |

```
Binary → Octal: (10110101)₂
Group: 010 | 110 | 101
       2     6     5
Answer: (265)₈

Octal → Binary: (473)₈
4 → 100, 7 → 111, 3 → 011
Answer: (100111011)₂
```

---

### 2.4 Binary ↔ Hexadecimal (⭐ Super Important)

**Secret**: Group binary digits in 4s (right to left)

| Binary | Hex | Binary | Hex |
|--------|-----|--------|-----|
| 0000 | 0 | 1000 | 8 |
| 0001 | 1 | 1001 | 9 |
| 0010 | 2 | 1010 | A |
| 0011 | 3 | 1011 | B |
| 0100 | 4 | 1100 | C |
| 0101 | 5 | 1101 | D |
| 0110 | 6 | 1110 | E |
| 0111 | 7 | 1111 | F |

**🧠 Memorize**: A=10, B=11, C=12, D=13, E=14, F=15

```
Binary → Hex: (10111011010)₂
Group from right: 0101 | 1101 | 1010
                   5      D      A
Answer: (5DA)₁₆

Hex → Binary: (3CF)₁₆
3 → 0011, C → 1100, F → 1111
Answer: (001111001111)₂
```

---

### 2.5 Octal ↔ Hexadecimal

**Method**: Use Binary as intermediate bridge

```
(573)₈ → Hex
Step 1: Octal → Binary
  5 → 101, 7 → 111, 3 → 011
  Binary: 101111011

Step 2: Binary → Hex (group by 4)
  0001 | 0111 | 1011
   1      7      B
Answer: (17B)₁₆
```

---

## 📐 Fractional Number Conversions

### 3.1 Decimal Fraction → Binary

**Method**: Repeated multiplication by 2, take integer parts (top-to-bottom)

```
0.625₁₀ → Binary

0.625 × 2 = 1.25  → 1 ↓
0.25  × 2 = 0.50  → 0 │ Read
0.50  × 2 = 1.00  → 1 ↓ downward

Answer: 0.101₂
```

**⚠️ Edge Case**: Some decimals never terminate in binary!
```
0.1₁₀ = 0.0001100110011...₂ (repeating)
```

---

### 3.2 Binary Fraction → Decimal

**Method**: Multiply by negative powers of 2

```
(0.1011)₂ → Decimal
= 1×2⁻¹ + 0×2⁻² + 1×2⁻³ + 1×2⁻⁴
= 0.5 + 0 + 0.125 + 0.0625
= 0.6875₁₀
```

---

## ➕➖ Binary Arithmetic

### 4.1 Binary Addition

```
Rules:  0+0=0, 0+1=1, 1+0=1, 1+1=10 (carry 1)

    1 0 1 1
  +   1 1 0
  ---------
  1 0 0 0 1

Carry: 1 1 1
```

---

### 4.2 Binary Subtraction

```
Rules: 0-0=0, 1-0=1, 1-1=0, 0-1=1 (borrow 1)

    1 0 1 1   (11)
  -   1 1 0   (6)
  ---------
      1 0 1   (5)
```

---

### 4.3 Binary Multiplication

```
Same as decimal, but simpler (only 0 and 1)

      1 0 1 1
    ×     1 0 1
    -----------
      1 0 1 1     (×1)
    0 0 0 0       (×0, shifted)
  1 0 1 1         (×1, shifted)
  ---------------
  1 1 0 1 1 1
```

---

## ➖ Signed Number Representation

### 5.1 Sign-Magnitude

- MSB = Sign bit (0 = positive, 1 = negative)
- Remaining bits = Magnitude

```
+5 in 4 bits: 0101
-5 in 4 bits: 1101
```

**⚠️ Problem**: Two representations of zero (+0, -0)

---

### 5.2 1's Complement

**Negative number** = Flip all bits of positive number

```
+5 = 0101
-5 = 1010 (flip each bit)
```

**⚠️ Problem**: Still two zeros, complex addition

---

### 5.3 2's Complement (⭐ Most Important)

**Negative number** = 1's complement + 1 = Flip all bits, then add 1

```
+5 = 0101
1's complement of 5 = 1010
2's complement of 5 = 1010 + 1 = 1011

So -5 = 1011 in 2's complement
```

**⚡ Shortcut**: From right, keep all bits until first 1 (inclusive), then flip rest
```
+6 = 0110
     ↓  ↓
-6 = 1010
```

**Range in n bits**: -2^(n-1) to 2^(n-1) - 1
- 8 bits: -128 to +127
- 16 bits: -32768 to +32767

---

### 5.4 Finding Decimal Value of Negative 2's Complement

```
Given: 1011 (4-bit 2's complement)
MSB = 1, so negative

Method 1: Take 2's complement again
  1011 → flip → 0100 → add 1 → 0101 = 5
  Answer: -5

Method 2: -2³ + 0 + 2¹ + 2⁰ = -8 + 2 + 1 = -5
```

---

## 🔥 Important Properties & Tricks

### Number of Digits Formula

Number of digits in base b for number N:
```
d = ⌊log_b(N)⌋ + 1
```

Example: How many binary digits for 1000?
```
d = ⌊log₂(1000)⌋ + 1 = ⌊9.97⌋ + 1 = 10 digits
```

---

### Quick Mental Math

**Powers of 2** (Memorize!):
```
2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128
2⁸=256, 2⁹=512, 2¹⁰=1024, 2¹¹=2048, 2¹²=4096
```

**Hex to Decimal Quick**: Break down
```
(3E8)₁₆ = 3×256 + 14×16 + 8 = 768 + 224 + 8 = 1000
```

---

## ⚠️ Common Edge Cases & Traps

1. **Don't forget padding zeros** when grouping for octal/hex conversion
   - (11010)₂ for octal: 011 | 010 (not 11 | 010)

2. **MSB matters** in signed numbers
   - Same bits = different values based on interpretation

3. **Overflow in 2's complement**
   - Adding two positives gives negative? Overflow!
   - Adding two negatives gives positive? Overflow!

4. **Repeating fractions**: 1/3, 1/5, 1/10 don't terminate in binary

5. **Range check**: -8 to +7 in 4-bit 2's complement, not -7 to +7

---

## 🚀 Formula Cheat Sheet

| Conversion | Method |
|------------|--------|
| Any → Decimal | Σ(digit × base^position) |
| Decimal → Any | Divide repeatedly, read remainders upward |
| Binary ↔ Octal | Group by 3 bits |
| Binary ↔ Hex | Group by 4 bits |
| 2's Complement | Flip bits + 1 |
| n-bit 2's range | -2^(n-1) to 2^(n-1)-1 |
| Digits needed | ⌊log_b(N)⌋ + 1 |

---

## 📝 GATE-Level Practice Problems

**Q1**: Convert (10110.101)₂ to decimal
```
Answer: 1×2⁴ + 0 + 1×2² + 1×2¹ + 0 + 1×2⁻¹ + 0 + 1×2⁻³
      = 16 + 4 + 2 + 0.5 + 0.125 = 22.625
```

**Q2**: What is -45 in 8-bit 2's complement?
```
45 = 00101101
1's complement = 11010010
2's complement = 11010011
Answer: 11010011
```

**Q3**: Convert (ABC)₁₆ to octal
```
Hex → Binary: A=1010, B=1011, C=1100 → 101010111100
Binary → Octal: 101 | 010 | 111 | 100 → 5274
Answer: (5274)₈
```

**Q4**: Range of values in 6-bit 2's complement?
```
Answer: -2⁵ to 2⁵-1 = -32 to 31
```

---

*Next: [Chapter 2 - Percentages →](./02_Percentages.md)*
