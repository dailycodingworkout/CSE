# 📖 Module 12: Quick Reference & Cheat Sheets

## 🎯 Last-Minute Revision Guide

This module contains all formulas, shortcuts, and quick references for exam day. **Print this for revision!**

---

## 12.1 Powers of 2 (MEMORIZE!)

```
2⁰  = 1           2⁸  = 256         2¹⁶ = 65,536
2¹  = 2           2⁹  = 512         2²⁰ = 1,048,576 (≈1M)
2²  = 4           2¹⁰ = 1,024 (1K)  2³⁰ = 1,073,741,824 (≈1G)
2³  = 8           2¹¹ = 2,048       2³² = 4,294,967,296 (≈4G)
2⁴  = 16          2¹² = 4,096 (4K)
2⁵  = 32          2¹³ = 8,192
2⁶  = 64          2¹⁴ = 16,384
2⁷  = 128         2¹⁵ = 32,768
```

---

## 12.2 Hex-Binary Quick Table

```
0 = 0000    4 = 0100    8 = 1000    C = 1100
1 = 0001    5 = 0101    9 = 1001    D = 1101
2 = 0010    6 = 0110    A = 1010    E = 1110
3 = 0011    7 = 0111    B = 1011    F = 1111
```

---

## 12.3 Range Formulas

### Unsigned n-bit:
```
Range: 0 to 2ⁿ - 1
Total values: 2ⁿ
```

### Signed n-bit (2's Complement):
```
Range: -2ⁿ⁻¹ to +2ⁿ⁻¹ - 1
Total values: 2ⁿ
Min: 100...0 (n-1 zeros)
Max: 011...1 (n-1 ones)
```

### Quick Reference:
| Bits | Unsigned Max | Signed Range |
|------|--------------|--------------|
| 4 | 15 | -8 to +7 |
| 8 | 255 | -128 to +127 |
| 16 | 65,535 | -32,768 to +32,767 |
| 32 | 4,294,967,295 | -2,147,483,648 to +2,147,483,647 |

---

## 12.4 Conversion Formulas

### Any Base to Decimal:
```
(dₙdₙ₋₁...d₁d₀)ᵦ = dₙ×bⁿ + dₙ₋₁×bⁿ⁻¹ + ... + d₁×b¹ + d₀×b⁰
```

### Decimal to Any Base:
```
Method: Divide by base, collect remainders bottom-to-top
```

### Fractional Conversion:
```
Decimal to Binary: Multiply by 2, collect integer parts top-to-bottom
Binary to Decimal: Sum of (bit × 2⁻ᵖᵒˢⁱᵗⁱᵒⁿ)
```

### Direct Conversions:
```
Binary ↔ Octal: Group/Expand by 3 bits
Binary ↔ Hex: Group/Expand by 4 bits
```

---

## 12.5 2's Complement Formulas

### To Get -N from +N:
```
Method 1: Invert all bits + 1
Method 2: Keep from right until first 1, flip rest
Method 3: 2ⁿ - N
```

### Value of Negative Number:
```
Method 1: Take 2's complement, add minus sign
Method 2: -2ⁿ⁻¹ + (remaining bits as positive)
```

### Sign Extension:
```
Copy MSB to fill new bits
Example: 1010 (4-bit) → 11111010 (8-bit)
```

---

## 12.6 IEEE 754 Floating Point

### Single Precision (32-bit):
```
|S|   E (8 bits)   |   M (23 bits)   |
| 1 |   01111111    | 00000000...     |

Value = (-1)ˢ × 1.M × 2^(E-127)
Bias = 127
```

### Double Precision (64-bit):
```
|S|   E (11 bits)  |   M (52 bits)   |

Value = (-1)ˢ × 1.M × 2^(E-1023)
Bias = 1023
```

### Special Values:
| E | M | Value |
|---|---|-------|
| 0 | 0 | ±0 |
| 0 | ≠0 | Denormalized |
| 1-254 | any | Normalized |
| 255 | 0 | ±∞ |
| 255 | ≠0 | NaN |

### Key Values:
```
+∞ = 0 11111111 00000000000000000000000 (0x7F800000)
-∞ = 1 11111111 00000000000000000000000 (0xFF800000)
+1 = 0 01111111 00000000000000000000000 (0x3F800000)
-1 = 1 01111111 00000000000000000000000 (0xBF800000)
```

---

## 12.7 Overflow Detection

### 2's Complement Addition:
```
Overflow = (Same sign inputs) AND (Different sign result)

Using Carries:
V = Cₙ₋₁ ⊕ Cₙ (Carry into MSB XOR Carry out of MSB)
```

### Quick Rules:
```
✓ Positive + Negative → NEVER overflow
✗ Positive + Positive = Negative → OVERFLOW
✗ Negative + Negative = Positive → OVERFLOW
```

---

## 12.8 ASCII Values (Key Points)

```
'0' = 48 = 0x30    'A' = 65 = 0x41    'a' = 97 = 0x61
'9' = 57 = 0x39    'Z' = 90 = 0x5A    'z' = 122 = 0x7A
Space = 32 = 0x20

Conversion:
'a' - 'A' = 32 (lowercase to uppercase: subtract 32)
'5' - '0' = 5 (character to digit: subtract 48)
```

---

## 12.9 Gray Code Conversions

### Binary to Gray:
```
G[MSB] = B[MSB]
G[i] = B[i+1] ⊕ B[i]
```

### Gray to Binary:
```
B[MSB] = G[MSB]
B[i] = B[i+1] ⊕ G[i]
```

---

## 12.10 BCD Rules

### Valid BCD: 0000 to 1001 (0-9)
### Invalid BCD: 1010 to 1111 (10-15)

### BCD Addition:
```
If digit sum > 9 OR carry out → Add 6 (0110)
```

---

## 12.11 Arithmetic Quick Reference

### Binary Addition:
```
0+0=0, 0+1=1, 1+0=1, 1+1=10
```

### Shift Operations:
```
Left Shift by n = Multiply by 2ⁿ
Right Shift by n = Divide by 2ⁿ
```

### Multiplication:
```
n-bit × n-bit = up to 2n-bit result
```

---

## 12.12 Fixed Point Quick Reference

### Q-Format:
```
Qm.n = m integer bits + n fractional bits

Value = stored_integer × 2⁻ⁿ
Stored = value × 2ⁿ

Resolution = 2⁻ⁿ
Range (signed) = [-2^(m-1), 2^(m-1) - 2^(-n)]
```

---

## 12.13 Number of Bits Formula

### To represent N distinct values:
```
Bits needed = ⌈log₂(N)⌉
```

### To represent number N:
```
Bits needed = ⌊log₂(N)⌋ + 1
```

### Useful Approximations:
```
log₂(10) ≈ 3.32
log₁₀(2) ≈ 0.301
2¹⁰ ≈ 10³ (1024 ≈ 1000)
```

---

## 12.14 Error Detection

### Parity:
```
Even parity: Total 1s is even
Odd parity: Total 1s is odd
Detects: Single bit errors
```

### Hamming Code:
```
Parity bits at positions: 1, 2, 4, 8, ... (powers of 2)
Bits needed: 2ʳ ≥ m + r + 1
```

### Hamming Distance:
```
Number of bit positions where two codes differ
Min distance d → can detect (d-1) errors, correct ⌊(d-1)/2⌋ errors
```

---

## 12.15 One-Page Cheat Sheet

```
╔════════════════════════════════════════════════════════════════╗
║                    NUMBER SYSTEM CHEAT SHEET                   ║
╠════════════════════════════════════════════════════════════════╣
║ BASES:                                                         ║
║   Binary(2), Octal(8), Decimal(10), Hex(16)                   ║
║   Bin↔Oct: group 3 | Bin↔Hex: group 4                         ║
║                                                                ║
║ 2's COMPLEMENT (n-bit):                                        ║
║   Range: -2^(n-1) to 2^(n-1)-1                                ║
║   -N = ~N + 1                                                  ║
║   Value: -2^(n-1) + positive_bits                              ║
║                                                                ║
║ OVERFLOW: V = Cᵢₙ_MSB ⊕ Cₒᵤₜ_MSB                               ║
║                                                                ║
║ IEEE 754 SINGLE: 1|8|23, Bias=127                             ║
║   Value = (-1)^S × 1.M × 2^(E-127)                            ║
║   E=0,M=0: Zero | E=255,M=0: ∞ | E=255,M≠0: NaN               ║
║                                                                ║
║ IEEE 754 DOUBLE: 1|11|52, Bias=1023                           ║
║                                                                ║
║ ASCII: '0'=48, 'A'=65, 'a'=97                                  ║
║                                                                ║
║ GRAY CODE: G[i]=B[i+1]⊕B[i], MSB same                         ║
║                                                                ║
║ BCD: 4 bits per decimal digit, add 6 if >9                    ║
║                                                                ║
║ POWERS OF 2: 2^10=1024≈1K, 2^20≈1M, 2^30≈1G                   ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 12.16 Common Mistakes Checklist

Before submitting answer, verify:

- [ ] Did I use correct bias? (127 for single, 1023 for double)
- [ ] Did I include hidden bit in mantissa calculation?
- [ ] Did I check for overflow?
- [ ] Did I read remainders in correct order? (bottom-to-top for integer)
- [ ] Did I pad with correct zeros when grouping for hex/octal?
- [ ] Did I apply BCD correction when needed?
- [ ] Did I interpret negative correctly in 2's complement?

---

## 12.17 Quick Calculation Tricks

### Multiply by 2ⁿ:
```
Left shift by n positions
```

### Divide by 2ⁿ:
```
Right shift by n positions
```

### Check if power of 2:
```
n & (n-1) == 0
```

### Count bits needed:
```
For N: bits = ⌊log₂(N)⌋ + 1
Quick: N between 2^k and 2^(k+1) needs k+1 bits
```

### 2's complement of itself:
```
-2^(n-1) is its own 2's complement!
```

---

## 12.18 Exam Day Reminders

1. **Read question carefully** - Is it signed or unsigned?
2. **Check the base** - (1010)₂ vs (1010)₁₀ are different!
3. **Verify answers** - Convert back if time permits
4. **Use calculator** - GATE virtual calculator can do base conversions
5. **Watch for special cases** - Zero, infinity, NaN, overflow

---

## 📊 Topic Priority for GATE

```
HIGH PRIORITY (Most Questions):
├── 2's Complement ★★★★★
├── IEEE 754 Floating Point ★★★★★
├── Overflow Detection ★★★★☆
└── Range Calculations ★★★★☆

MEDIUM PRIORITY:
├── Base Conversions ★★★☆☆
├── Signed Representations ★★★☆☆
└── Binary Arithmetic ★★★☆☆

LOWER PRIORITY:
├── BCD ★★☆☆☆
├── Gray Code ★★☆☆☆
├── Fixed Point ★★☆☆☆
└── Error Codes ★★☆☆☆
```

---

**🎯 Good Luck with Your Exam! 🎯**

---

*This cheat sheet covers all essential formulas and concepts for GATE Number System questions. Review this before the exam for last-minute revision.*
