# 📖 Module 9: Special Numbers and Codes

## 🎯 Learning Objectives

After completing this module, you will:
- Understand various binary codes used in digital systems
- Master BCD, Gray Code, ASCII, and Unicode
- Learn error detection and correction codes
- Apply these concepts in GATE-level problems

---

## 9.1 Binary Coded Decimal (BCD)

### Definition:
Each decimal digit (0-9) is represented by its 4-bit binary equivalent.

### BCD (8421) Table:
| Decimal | BCD | Valid? |
|---------|-----|--------|
| 0 | 0000 | ✅ |
| 1 | 0001 | ✅ |
| 2 | 0010 | ✅ |
| 3 | 0011 | ✅ |
| 4 | 0100 | ✅ |
| 5 | 0101 | ✅ |
| 6 | 0110 | ✅ |
| 7 | 0111 | ✅ |
| 8 | 1000 | ✅ |
| 9 | 1001 | ✅ |
| 10 | 1010 | ❌ Invalid |
| 11 | 1011 | ❌ Invalid |
| ... | ... | ❌ Invalid |
| 15 | 1111 | ❌ Invalid |

### BCD vs Binary:
```
Decimal 59:
  Binary: 111011 (6 bits)
  BCD:    0101 1001 (8 bits)
          └─5─┘└─9─┘
```

### BCD Arithmetic:
```
BCD Addition Rules:
1. Add as normal 4-bit binary
2. If result > 9 OR carry out, add 0110 (6)

Example: 7 + 6 = 13
  0111
+ 0110
──────
  1101 (13 in binary, but invalid BCD!)
+ 0110 (add correction)
──────
 10011 → 0001 0011 (BCD 13)
          └─1─┘└─3─┘
```

### Packed vs Unpacked BCD:
```
Packed BCD: Two digits per byte
  59 = 0101 1001 (1 byte)

Unpacked BCD: One digit per byte
  59 = 0000 0101  0000 1001 (2 bytes)
```

---

## 9.2 Other Weighted Codes

### 2421 Code:
```
Weights: 2, 4, 2, 1

| Decimal | 2421 |
|---------|------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 1011 |
| 6 | 1100 |
| 7 | 1101 |
| 8 | 1110 |
| 9 | 1111 |

Self-complementing: 9's complement = bit complement
Example: 3 = 0011, 6 = 1100 (complement bits!) 3 + 6 = 9 ✓
```

### 5211 Code:
```
Weights: 5, 2, 1, 1

| Decimal | 5211 |
|---------|------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0011 |
| 3 | 0101 |
| 4 | 0111 |
| 5 | 1000 |
| 6 | 1010 |
| 7 | 1100 |
| 8 | 1110 |
| 9 | 1111 |
```

---

## 9.3 Gray Code (Reflected Binary Code)

### Property:
Adjacent codes differ by exactly ONE bit.

### 4-bit Gray Code:
| Decimal | Binary | Gray |
|---------|--------|------|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

### Binary to Gray Conversion:
```
G[n-1] = B[n-1]  (MSB stays same)
G[i] = B[i+1] ⊕ B[i]  (XOR adjacent bits)

Example: Binary 1011 → Gray
G[3] = B[3] = 1
G[2] = B[3] ⊕ B[2] = 1 ⊕ 0 = 1
G[1] = B[2] ⊕ B[1] = 0 ⊕ 1 = 1
G[0] = B[1] ⊕ B[0] = 1 ⊕ 1 = 0

Gray = 1110
```

### Gray to Binary Conversion:
```
B[n-1] = G[n-1]  (MSB stays same)
B[i] = B[i+1] ⊕ G[i]  (XOR with previous binary bit)

Example: Gray 1110 → Binary
B[3] = G[3] = 1
B[2] = B[3] ⊕ G[2] = 1 ⊕ 1 = 0
B[1] = B[2] ⊕ G[1] = 0 ⊕ 1 = 1
B[0] = B[1] ⊕ G[0] = 1 ⊕ 0 = 1

Binary = 1011
```

### Applications:
- Rotary encoders (position sensing)
- Karnaugh maps
- Error minimization in A/D conversion

---

## 9.4 Excess-3 Code

### Definition:
Add 3 to each decimal digit, then convert to 4-bit binary.

### Excess-3 Table:
| Decimal | Decimal + 3 | Excess-3 |
|---------|-------------|----------|
| 0 | 3 | 0011 |
| 1 | 4 | 0100 |
| 2 | 5 | 0101 |
| 3 | 6 | 0110 |
| 4 | 7 | 0111 |
| 5 | 8 | 1000 |
| 6 | 9 | 1001 |
| 7 | 10 | 1010 |
| 8 | 11 | 1011 |
| 9 | 12 | 1100 |

### Properties:
1. **Self-Complementing**: 1's complement of a digit = 9's complement
   ```
   5 in Excess-3 = 1000
   4 in Excess-3 = 0111
   1000 complement = 0111 ✓ (5 + 4 = 9)
   ```

2. **No all-zeros or all-ones**: Valid codes are 0011 to 1100

---

## 9.5 ASCII (American Standard Code for Information Interchange)

### Overview:
- 7-bit code (128 characters)
- Extended ASCII: 8-bit (256 characters)

### Key ASCII Values (Memorize These!):

| Character | Decimal | Hex | Binary |
|-----------|---------|-----|--------|
| '0' | 48 | 0x30 | 0110000 |
| '9' | 57 | 0x39 | 0111001 |
| 'A' | 65 | 0x41 | 1000001 |
| 'Z' | 90 | 0x5A | 1011010 |
| 'a' | 97 | 0x61 | 1100001 |
| 'z' | 122 | 0x7A | 1111010 |
| Space | 32 | 0x20 | 0100000 |
| NUL | 0 | 0x00 | 0000000 |

### Important Relationships:
```
'A' to 'a': difference of 32 (0x20)
'A' = 65, 'a' = 97
To convert: lowercase = uppercase | 0x20
            uppercase = lowercase & 0xDF

'0' to 0: subtract 48 (0x30)
'5' - '0' = 53 - 48 = 5
```

### ASCII Categories:
```
0-31: Control characters (non-printable)
32-47: Punctuation and symbols
48-57: Digits 0-9
58-64: More punctuation
65-90: Uppercase A-Z
91-96: More punctuation
97-122: Lowercase a-z
123-127: More punctuation and DEL
```

---

## 9.6 Unicode

### Evolution:
```
ASCII (7-bit) → Extended ASCII (8-bit) → Unicode (16-bit+)
128 chars      256 chars                 1,114,112 code points
```

### Unicode Formats:
| Encoding | Bytes per Character | Use |
|----------|---------------------|-----|
| UTF-8 | 1-4 | Web, most common |
| UTF-16 | 2-4 | Windows, Java |
| UTF-32 | 4 | Fixed width |

### UTF-8 Encoding:
```
Code Point Range    | Byte 1   | Byte 2   | Byte 3   | Byte 4
U+0000 to U+007F   | 0xxxxxxx |          |          |
U+0080 to U+07FF   | 110xxxxx | 10xxxxxx |          |
U+0800 to U+FFFF   | 1110xxxx | 10xxxxxx | 10xxxxxx |
U+10000 to U+10FFFF| 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx
```

### Example:
```
Character: € (Euro sign)
Unicode: U+20AC
Binary: 0010 0000 1010 1100

UTF-8 encoding (3 bytes):
1110 0010 | 10 000010 | 10 101100
    E2       82          AC

UTF-8 = 0xE282AC
```

---

## 9.7 Error Detection Codes

### Parity Bit:
```
Even Parity: Total 1s (including parity) is even
Odd Parity: Total 1s (including parity) is odd

Example (Even Parity):
Data: 1011001 (four 1s, already even)
With parity: 1011001 0 (parity bit = 0)

Data: 1011011 (five 1s, odd)
With parity: 1011011 1 (parity bit = 1)
```

### Limitations:
- Detects odd number of bit errors
- Cannot detect even number of bit errors
- Cannot correct errors

### Checksum:
```
Sum all data bytes, take lower bits

Example:
Data: 0x25, 0x62, 0x3F
Sum: 0x25 + 0x62 + 0x3F = 0xC6
Checksum (8-bit): 0xC6
```

---

## 9.8 Hamming Code

### Purpose:
Single Error Correction, Double Error Detection (SECDED)

### Structure:
```
For m data bits, need r parity bits where 2^r ≥ m + r + 1

Position of parity bits: powers of 2 (1, 2, 4, 8, ...)
```

### Example: Hamming(7,4)
```
4 data bits (D1, D2, D3, D4)
3 parity bits (P1, P2, P4)

Position: 1   2   3   4   5   6   7
Bit:      P1  P2  D1  P4  D2  D3  D4

P1 checks: 1, 3, 5, 7 (positions with bit 0 set)
P2 checks: 2, 3, 6, 7 (positions with bit 1 set)
P4 checks: 4, 5, 6, 7 (positions with bit 2 set)
```

### Error Detection:
```
Recalculate parities
Syndrome = P4 P2 P1
If Syndrome = 0: No error
If Syndrome ≠ 0: Error at position = Syndrome value
```

---

## 9.9 Cyclic Redundancy Check (CRC)

### Overview:
- Powerful error detection
- Used in networks, storage
- Based on polynomial division

### CRC Calculation:
```
1. Append n zeros to message (n = degree of generator)
2. Divide (XOR) by generator polynomial
3. Remainder is CRC
4. Append CRC to message
```

### Example: CRC-4
```
Message: 1101011011
Generator: 10011 (CRC-4)

1. Append 4 zeros: 11010110110000
2. Perform polynomial division (XOR)
3. Remainder = 1110 (CRC)
4. Transmit: 11010110111110
```

### Common CRC Polynomials:
```
CRC-8: x⁸ + x² + x + 1
CRC-16: x¹⁶ + x¹⁵ + x² + 1
CRC-32: x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1
```

---

## 9.10 Alphanumeric Codes

### EBCDIC (Extended Binary Coded Decimal Interchange Code):
- 8-bit code
- Used in IBM mainframes
- Different from ASCII

### EBCDIC vs ASCII:
| Character | ASCII | EBCDIC |
|-----------|-------|--------|
| 'A' | 0x41 | 0xC1 |
| '0' | 0x30 | 0xF0 |

### Considerations:
- File transfer between systems
- Different collating sequences

---

## 9.11 Summary Tables

### Weighted Codes Comparison:
| Code | Weights | Self-Complementing |
|------|---------|-------------------|
| 8421 (BCD) | 8-4-2-1 | No |
| 2421 | 2-4-2-1 | Yes |
| 5211 | 5-2-1-1 | No |
| Excess-3 | - | Yes |

### Character Codes:
| Code | Bits | Characters |
|------|------|------------|
| ASCII | 7 | 128 |
| Extended ASCII | 8 | 256 |
| Unicode | 16-32 | 1M+ |
| EBCDIC | 8 | 256 |

---

## 9.12 GATE Important Points

### Frequently Asked:
1. BCD addition and correction
2. Gray code conversions
3. ASCII value calculations
4. Hamming code parity calculation
5. Properties of self-complementing codes

### Quick Tips:
- '0' = 48, 'A' = 65, 'a' = 97 in ASCII
- Gray code: MSB same, then XOR adjacent
- BCD: add 6 if > 9 or carry
- Excess-3: add 3 to each digit before BCD

---

## 📝 Practice Problems

1. Convert 487 to BCD
2. Convert binary 10111 to Gray code
3. What is the Hamming distance between 1011 and 1110?
4. Calculate even parity bit for 1011010
5. In ASCII, what is 'M' + 32?

<details>
<summary>Answers</summary>

1. 0100 1000 0111 (4-8-7)
2. 10111 → 11100 (Gray)
3. Hamming distance = 2 (two bits differ)
4. 1011010 has 4 ones (even), parity bit = 0
5. 'M' = 77, 77 + 32 = 109 = 'm' (lowercase conversion)

</details>

---

## 🔜 Next Module
[Module 10: Practice Problems →](../10_Practice_Problems/)
