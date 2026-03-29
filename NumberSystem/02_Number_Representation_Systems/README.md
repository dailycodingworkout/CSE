# 📖 Module 2: Number Representation Systems

## 🎯 Learning Objectives

After completing this module, you will:
- Master all four common number systems (Binary, Octal, Decimal, Hexadecimal)
- Understand weighted and non-weighted codes
- Learn the relationship between different number systems
- Be able to quickly identify and work with any base

---

## 2.1 Binary Number System (Base-2)

### Characteristics:
- **Base**: 2
- **Digits**: 0, 1 (called bits)
- **Used in**: All digital computers and electronic systems

### Place Values:
```
Position:  7    6    5    4    3    2    1    0
Weight:   2⁷   2⁶   2⁵   2⁴   2³   2²   2¹   2⁰
Value:   128   64   32   16   8    4    2    1
```

### Examples:
| Binary | Calculation | Decimal |
|--------|-------------|---------|
| 1011 | 1×8 + 0×4 + 1×2 + 1×1 | 11 |
| 11111111 | 128+64+32+16+8+4+2+1 | 255 |
| 10000000 | 1×128 | 128 |

### Quick Reference - Powers of 2:
```
2⁰ = 1        2⁵ = 32       2¹⁰ = 1024 (1K)
2¹ = 2        2⁶ = 64       2¹¹ = 2048 (2K)
2² = 4        2⁷ = 128      2¹² = 4096 (4K)
2³ = 8        2⁸ = 256      2¹⁶ = 65536 (64K)
2⁴ = 16       2⁹ = 512      2²⁰ = 1048576 (1M)
```

---

## 2.2 Octal Number System (Base-8)

### Characteristics:
- **Base**: 8
- **Digits**: 0, 1, 2, 3, 4, 5, 6, 7
- **Used in**: Compact representation of binary, Unix file permissions

### Place Values:
```
Position:  3      2      1      0
Weight:   8³     8²     8¹     8⁰
Value:   512    64      8      1
```

### Examples:
| Octal | Calculation | Decimal |
|-------|-------------|---------|
| 75 | 7×8 + 5×1 | 61 |
| 123 | 1×64 + 2×8 + 3×1 | 83 |
| 777 | 7×64 + 7×8 + 7×1 | 511 |

### Why Octal?
- **3 binary bits = 1 octal digit**
- Easy grouping: (111 010 001)₂ = (721)₈
- Used in Unix/Linux file permissions: rwxrwxrwx = 777

---

## 2.3 Decimal Number System (Base-10)

### Characteristics:
- **Base**: 10
- **Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Used in**: Human calculations, everyday counting

### Place Values:
```
Position:  3        2        1        0
Weight:   10³      10²      10¹      10⁰
Value:   1000     100       10        1
```

### Significance:
- Most familiar to humans
- All number system problems start or end with decimal
- Conversion reference point

---

## 2.4 Hexadecimal Number System (Base-16)

### Characteristics:
- **Base**: 16
- **Digits**: 0-9, A(10), B(11), C(12), D(13), E(14), F(15)
- **Used in**: Memory addresses, MAC addresses, colors, assembly

### Digit Mapping:
| Decimal | Hex | Binary |
|---------|-----|--------|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

### Place Values:
```
Position:  3        2        1        0
Weight:   16³      16²      16¹      16⁰
Value:   4096     256       16        1
```

### Examples:
| Hex | Calculation | Decimal |
|-----|-------------|---------|
| 2A | 2×16 + 10×1 | 42 |
| FF | 15×16 + 15×1 | 255 |
| 1000 | 1×4096 | 4096 |

### Why Hexadecimal?
- **4 binary bits = 1 hex digit**
- Compact representation of binary
- Memory addresses: 0x7FFE2A3C
- Color codes: #FF5733

---

## 2.5 Relationship Between Number Systems

### Binary ↔ Octal ↔ Hexadecimal:

```
1 Octal digit = 3 Binary bits
1 Hex digit = 4 Binary bits

Example:
Binary:     1 0 1 1 0 1 1 1 0 0 1 0
            \_____/ \_____/ \_____/ \_____/
Octal:         5       5       6       2
            \_______/ \_______/ \_______/
Hex:            B         7         2
```

### Quick Conversion Chart:
```
Binary     Octal    Hex
000        0        -
001        1        -
010        2        -
011        3        -
100        4        -
101        5        -
110        6        -
111        7        -
0000       -        0
0001       -        1
...
1111       -        F
```

---

## 2.6 Weighted vs Non-Weighted Codes

### Weighted Codes:
Each position has a fixed weight (value).

| Code | Weights | Example |
|------|---------|---------|
| **Binary** | 2ⁿ | 8-4-2-1 |
| **BCD (8421)** | 8-4-2-1 | 0101 = 5 |
| **2421 Code** | 2-4-2-1 | 0101 = 5 |
| **5211 Code** | 5-2-1-1 | 0110 = 4 |

### Non-Weighted Codes:
No fixed positional weight.

| Code | Description | Use |
|------|-------------|-----|
| **Gray Code** | Only 1 bit changes between consecutive numbers | Encoders, error minimization |
| **Excess-3** | BCD + 3 | Self-complementing |
| **ASCII** | Character encoding | Text representation |

---

## 2.7 BCD (Binary Coded Decimal)

### Definition:
Each decimal digit is represented by its 4-bit binary equivalent.

### Conversion:
```
Decimal:    3    5    7
BCD:      0011  0101  0111

(357)₁₀ = (0011 0101 0111)ᵦ꜀ᴅ
```

### Important Note:
- BCD is **NOT** the same as binary!
- BCD uses 4 bits per decimal digit
- Invalid BCD codes: 1010 to 1111 (10-15)

### Example Comparison:
| Decimal | Binary | BCD |
|---------|--------|-----|
| 15 | 1111 | 0001 0101 |
| 99 | 1100011 | 1001 1001 |
| 127 | 1111111 | 0001 0010 0111 |

---

## 2.8 Gray Code

### Definition:
A binary numeral system where two successive values differ in only one bit.

### Binary to Gray Conversion:
```
Gray[i] = Binary[i] XOR Binary[i+1]
(MSB remains same)

Binary: 1 0 1 1
         ↓ ↓ ↓ ↓
Gray:   1 1 1 0
```

### Gray to Binary Conversion:
```
Binary[MSB] = Gray[MSB]
Binary[i] = Gray[i] XOR Binary[i+1]

Gray:   1 1 1 0
         ↓ ↓ ↓ ↓
Binary: 1 0 1 1
```

### 3-bit Gray Code Table:
| Decimal | Binary | Gray |
|---------|--------|------|
| 0 | 000 | 000 |
| 1 | 001 | 001 |
| 2 | 010 | 011 |
| 3 | 011 | 010 |
| 4 | 100 | 110 |
| 5 | 101 | 111 |
| 6 | 110 | 101 |
| 7 | 111 | 100 |

### Applications:
- Rotary encoders
- Karnaugh maps
- Error prevention in analog-to-digital conversion

---

## 2.9 Excess-3 Code

### Definition:
Each decimal digit is represented by adding 3 to it, then converting to binary.

### Conversion:
```
Decimal digit + 3 → 4-bit binary

Example: 
Decimal: 5
Excess-3: 5 + 3 = 8 = 1000

Decimal: 0
Excess-3: 0 + 3 = 3 = 0011
```

### Excess-3 Table:
| Decimal | Excess-3 |
|---------|----------|
| 0 | 0011 |
| 1 | 0100 |
| 2 | 0101 |
| 3 | 0110 |
| 4 | 0111 |
| 5 | 1000 |
| 6 | 1001 |
| 7 | 1010 |
| 8 | 1011 |
| 9 | 1100 |

### Property - Self-Complementing:
9's complement of a number = 1's complement of Excess-3 code
```
5 → 1000 → complement → 0111 → 4 (which is 9-5=4) ✓
```

---

## 2.10 Number System Notations

### Different ways to represent base:
```
Binary:      (1010)₂, 1010b, 0b1010
Octal:       (52)₈, 52o, 052 (C notation)
Decimal:     (42)₁₀, 42d, 42
Hexadecimal: (2A)₁₆, 2Ah, 0x2A, #2A
```

### In GATE:
- Usually subscript notation: (1010)₂
- Sometimes just stated: "binary 1010"
- Read carefully for the base!

---

## 2.11 Summary Table

| Property | Binary | Octal | Decimal | Hex |
|----------|--------|-------|---------|-----|
| Base | 2 | 8 | 10 | 16 |
| Digits | 0-1 | 0-7 | 0-9 | 0-F |
| Bits per digit | 1 | 3 | ~3.32 | 4 |
| Use | Computers | Permissions | Humans | Addresses |

---

## 2.12 GATE Important Points

⚠️ **Common Mistakes to Avoid:**
1. Confusing BCD with Binary
2. Using invalid BCD codes (10-15)
3. Wrong grouping for Octal/Hex conversion
4. Forgetting leading zeros in grouping

✅ **Key Takeaways:**
1. 3 bits = 1 octal digit, 4 bits = 1 hex digit
2. BCD is NOT binary - it's decimal in binary costume
3. Gray code differs by only 1 bit between consecutive numbers
4. Memorize hex digits A=10, B=11, ..., F=15

---

## 📝 Practice Questions

### Question 1:
Convert (ABC)₁₆ to binary.

<details>
<summary>Answer</summary>

A = 1010, B = 1011, C = 1100  
Answer: (1010 1011 1100)₂
</details>

### Question 2:
What is the BCD representation of 95?

<details>
<summary>Answer</summary>

9 = 1001, 5 = 0101  
Answer: (1001 0101)BCD
</details>

### Question 3:
Convert binary 1011 to Gray code.

<details>
<summary>Answer</summary>

1011 → 1 (1⊕0) (0⊕1) (1⊕1)  
Answer: 1110 (Gray)
</details>

### Question 4 (GATE 2015):
The number of bits required to represent the decimal number 1025 in binary is:

<details>
<summary>Answer</summary>

2¹⁰ = 1024, 2¹¹ = 2048  
1025 > 1024, so we need 11 bits  
1025 = 10000000001₂  
Answer: 11 bits
</details>

---

## 🔜 Next Module
[Module 3: Base Conversions →](../03_Base_Conversions/)
