# 📖 Module 1: Introduction to Number System

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Understand what a number system is and why it's important
- Identify different types of number systems
- Understand the role of number systems in digital computers
- Recognize the significance of this topic for GATE/ESE

---

## 1.1 What is a Number System?

A **Number System** is a mathematical notation for representing numbers using a consistent set of symbols or digits. It provides a systematic way to express and manipulate quantities.

### Definition:
> A number system is a set of symbols (digits) and rules for combining them to represent numerical values.

### Key Components:
1. **Base (Radix)**: The number of unique digits used in the system
2. **Digits**: The symbols used to represent values
3. **Positional Notation**: The value of a digit depends on its position

---

## 1.2 Why Study Number Systems?

### In Digital Systems:
- Computers use **binary (base-2)** internally
- All data, instructions, and addresses are represented in binary
- Understanding number systems is fundamental to:
  - Digital Logic Design
  - Computer Architecture
  - Assembly Programming
  - Memory Addressing

### In GATE/ESE:
- Direct questions on conversions and arithmetic
- Foundation for Digital Logic questions
- Required for Computer Organization topics
- Critical for understanding IEEE 754 floating point

---

## 1.3 Types of Number Systems

### Positional vs Non-Positional:

| Type | Description | Example |
|------|-------------|---------|
| **Positional** | Value depends on position | Decimal (452 ≠ 245) |
| **Non-Positional** | Value doesn't depend on position | Roman Numerals (VI = IV + I) |

### Common Positional Number Systems:

| System | Base | Digits | Usage |
|--------|------|--------|-------|
| **Binary** | 2 | 0, 1 | Digital circuits, computers |
| **Octal** | 8 | 0-7 | Compact binary representation |
| **Decimal** | 10 | 0-9 | Human calculations |
| **Hexadecimal** | 16 | 0-9, A-F | Memory addresses, colors |

---

## 1.4 Positional Notation Explained

In a positional number system with base `b`, a number is represented as:

```
(dₙdₙ₋₁...d₁d₀.d₋₁d₋₂...d₋ₘ)ᵦ

Value = dₙ × bⁿ + dₙ₋₁ × bⁿ⁻¹ + ... + d₁ × b¹ + d₀ × b⁰ + d₋₁ × b⁻¹ + ...
```

### Example: (1010.11)₂
```
= 1×2³ + 0×2² + 1×2¹ + 0×2⁰ + 1×2⁻¹ + 1×2⁻²
= 8 + 0 + 2 + 0 + 0.5 + 0.25
= 10.75₁₀
```

### Example: (2A3)₁₆
```
= 2×16² + 10×16¹ + 3×16⁰
= 512 + 160 + 3
= 675₁₀
```

---

## 1.5 Why Binary in Computers?

### Reasons for Using Binary:
1. **Simplicity**: Only two states (ON/OFF, HIGH/LOW)
2. **Reliability**: Easy to distinguish between two voltage levels
3. **Cost-Effective**: Simple circuitry
4. **Boolean Algebra**: Mathematical foundation (AND, OR, NOT)

### Physical Representation:
| Binary Value | Voltage Level | Physical State |
|--------------|--------------|----------------|
| 0 | Low (0V-0.8V) | OFF, Ground |
| 1 | High (2V-5V) | ON, Vcc |

---

## 1.6 Understanding Bits and Bytes

### Terminology:
| Unit | Definition | Capacity |
|------|------------|----------|
| **Bit** | Single binary digit | 0 or 1 |
| **Nibble** | 4 bits | 2⁴ = 16 values |
| **Byte** | 8 bits | 2⁸ = 256 values |
| **Word** | Architecture dependent | 16/32/64 bits |

### Common Word Sizes:
- **8-bit**: 0 to 255 (unsigned)
- **16-bit**: 0 to 65,535 (unsigned)
- **32-bit**: 0 to 4,294,967,295 (unsigned)
- **64-bit**: 0 to 18,446,744,073,709,551,615 (unsigned)

---

## 1.7 GATE Exam Perspective

### Types of Questions Asked:
1. **Direct Conversion**: Convert between bases
2. **Arithmetic**: Addition, subtraction in different bases
3. **Representation**: Signed numbers, IEEE 754
4. **Conceptual**: Range, overflow, precision

### Marks Distribution (Approximate):
```
Number System Topics in GATE:
├── Base Conversions: 5-10%
├── Signed Representation: 30-40%
├── Arithmetic Operations: 20-30%
├── Floating Point: 20-30%
└── Miscellaneous: 10-15%
```

---

## 1.8 Key Terminology

| Term | Definition |
|------|------------|
| **Base/Radix** | Number of unique digits in a number system |
| **MSB** | Most Significant Bit (leftmost bit) |
| **LSB** | Least Significant Bit (rightmost bit) |
| **Radix Point** | Separator between integer and fractional parts |
| **Weighted Code** | Each position has a specific weight |
| **Positional Value** | Value of a digit based on its position |

---

## 1.9 Summary

✅ Number system is a way to represent numbers using symbols and positions
✅ Digital computers use binary (base-2) system
✅ Common systems: Binary, Octal, Decimal, Hexadecimal
✅ Positional notation: value depends on position
✅ This topic is fundamental for GATE Digital Logic and Computer Organization

---

## 📝 Practice Questions

### Question 1:
What is the base of a number system that uses 8 unique symbols?

<details>
<summary>Answer</summary>
The base is 8 (Octal number system).
</details>

### Question 2:
In the decimal number 753, what is the positional value of digit 5?

<details>
<summary>Answer</summary>
5 × 10¹ = 50 (5 is in the tens position)
</details>

### Question 3:
Why can't we have negative bases in number systems?

<details>
<summary>Answer</summary>
Actually, we CAN have negative bases! Negabinary (base -2) exists. However, it's rarely used in practical systems and not asked in GATE.
</details>

---

## 🔜 Next Module
[Module 2: Number Representation Systems →](../02_Number_Representation_Systems/)
