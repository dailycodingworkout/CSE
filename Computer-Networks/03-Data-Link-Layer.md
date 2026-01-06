# Chapter 3: Data Link Layer
## The Frame Guardian | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Data Link Layer delivers frames; it handles errors, flow, and access."**

---

## 3.1 Data Link Layer Responsibilities

### Main Functions

1. **Framing:** Bundle bits into frames
2. **Physical Addressing:** MAC addresses
3. **Error Detection/Correction:** Ensure reliability
4. **Flow Control:** Prevent receiver overwhelm
5. **Access Control:** Who transmits when (MAC sublayer)

### Sublayers

```
┌─────────────────────────────────────┐
│ Data Link Layer                     │
├──────────────────┬──────────────────┤
│ LLC (Logical     │ MAC (Media       │
│ Link Control)    │ Access Control)  │
│ - Error control  │ - Physical addr  │
│ - Flow control   │ - Channel access │
└──────────────────┴──────────────────┘
```

---

## 3.2 Framing

### Why Framing?
Divide bit stream into manageable units with boundaries.

### Character Count

```
┌───┬───────────┬───┬───────────┬───┬───────────┐
│ 5 │ a b c d   │ 5 │ e f g h   │ 6 │ i j k l m │
└───┴───────────┴───┴───────────┴───┴───────────┘
  ↑ Count includes count byte itself
```

**Problem:** If count corrupted, all subsequent frames lost.

### Flag Bytes with Byte Stuffing

```
Frame format:
┌──────┬─────────────────────┬──────┐
│ FLAG │        DATA         │ FLAG │
└──────┴─────────────────────┴──────┘
  01111110                      01111110
```

**Byte Stuffing:** If data contains flag pattern, insert escape byte.

```
Data: ... FLAG ...
Transmitted: ... ESC FLAG ...

Data: ... ESC ...
Transmitted: ... ESC ESC ...
```

### Flag Bits with Bit Stuffing

Used in HDLC, PPP.

**Flag:** 01111110

**Bit Stuffing Rule:** After 5 consecutive 1s, insert 0.

```
Original:  011111101111111110
Stuffed:   0111110101111101110
           ↑     ↑        ↑
        Added 0s after 5 ones
```

**At receiver:** Remove 0 after 5 consecutive 1s.

### 🎯 GATE Classic

**Q:** Apply bit stuffing to: 01111110111111011111101

**Solution:**
- Original: 01111110111111011111101
- After 11111, insert 0:
  - 011111**0**1011111**0**1011111**0**01
- Answer: 0111110101111101011111001

---

## 3.3 Error Detection

### Types of Errors

| Type | Description | Example |
|------|-------------|---------|
| Single-bit | One bit flipped | 10101 → 10001 |
| Burst | Multiple adjacent bits | 10101 → 11011 |

### Parity Check

#### Simple Parity (Single Bit)

```
Even Parity: Total 1s should be even
Data: 1011001 (four 1s, already even)
With parity: 10110010

Data: 1011101 (five 1s, odd)
With parity: 10111011 (add 1 to make even)
```

**Limitation:** Detects odd number of errors only, cannot correct.

#### Two-Dimensional Parity

```
Data bits:       Row parity:
1 0 1 1  →  1      (3 ones, add 1)
1 1 0 0  →  0      (2 ones, add 0)
0 1 1 0  →  0      (2 ones, add 0)
1 0 1 1  →  1      (3 ones, add 1)
─────────
Col: 1 0 1 0 → 0   (column parities + corner)
```

- Detects single-bit errors
- Can locate and correct single-bit errors
- Detects burst errors up to n bits (column width)

### Checksum

#### Internet Checksum Algorithm

1. Divide data into 16-bit words
2. Add all words using one's complement
3. Take one's complement of sum
4. Append as checksum

**Example:**
```
Data: 10101001 00111001
      Word 1:  10101001 00111001
      
Sum: Add all 16-bit segments
Complement: Flip all bits
```

**Verification:** Add all words + checksum = all 1s (if no error)

### Cyclic Redundancy Check (CRC)

**Most widely used for error detection.**

#### CRC Algorithm

1. Choose divisor polynomial (generator) G(x)
2. Append (r-1) zeros to data (r = degree of G(x))
3. Divide by G(x) using XOR division
4. Remainder is CRC
5. Transmit data + CRC

#### Example

```
Data: 1101011011
Generator: 10011 (CRC-4, degree 4)

Step 1: Append 4 zeros
        110101101100 00

Step 2: XOR division
        110101101100 00
        10011
        ──────
        0100011
         10011
         ─────
          01001
          10011
          ─────
           1010011
           10011
           ──────
            011100
            10011
            ─────
             11110
             10011
             ─────
              1101 00
              10011
              ─────
               10000
               10011
               ─────
                0011 ← Remainder (CRC)

Step 3: Transmit: 110101101100 11
```

### Standard CRC Polynomials

| Name | Polynomial | Bits |
|------|------------|------|
| CRC-8 | $x^8 + x^2 + x + 1$ | 8 |
| CRC-16 | $x^{16} + x^{15} + x^2 + 1$ | 16 |
| CRC-32 | $x^{32} + x^{26} + ... + 1$ | 32 |
| CRC-CCITT | $x^{16} + x^{12} + x^5 + 1$ | 16 |

### 🎯 CRC Detection Capabilities

- Detects all single-bit errors
- Detects all double-bit errors (if G(x) has ≥3 terms)
- Detects all odd number of bit errors (if G(x) has factor x+1)
- Detects all burst errors ≤ r bits
- Detects most burst errors > r bits

---

## 3.4 Error Correction

### Hamming Code

#### Hamming Distance
Minimum number of bit positions that differ between two codewords.

$$d(code) = \text{minimum Hamming distance between any two codewords}$$

**For detection of d errors:** Need distance ≥ d + 1
**For correction of d errors:** Need distance ≥ 2d + 1

#### Hamming(7,4) Code

4 data bits, 3 parity bits, total 7 bits.

**Parity positions:** Powers of 2 (1, 2, 4, 8, ...)

```
Position: 1  2  3  4  5  6  7
Bit:      P1 P2 D1 P4 D2 D3 D4

P1 covers positions: 1, 3, 5, 7 (bit 0 is 1 in binary)
P2 covers positions: 2, 3, 6, 7 (bit 1 is 1 in binary)
P4 covers positions: 4, 5, 6, 7 (bit 2 is 1 in binary)
```

#### Hamming Code Example

**Encode D1D2D3D4 = 1011:**

```
Position:  1   2   3   4   5   6   7
          P1  P2  D1  P4  D2  D3  D4
              ?   1   ?   0   1   1

P1 covers 1,3,5,7: P1 ⊕ 1 ⊕ 0 ⊕ 1 = 0 → P1 = 0
P2 covers 2,3,6,7: P2 ⊕ 1 ⊕ 1 ⊕ 1 = 0 → P2 = 1
P4 covers 4,5,6,7: P4 ⊕ 0 ⊕ 1 ⊕ 1 = 0 → P4 = 0

Codeword: 0 1 1 0 0 1 1
```

#### Error Detection/Correction

If received word has error at position p:
- Calculate syndrome: check each parity
- Syndrome binary = error position
- Flip that bit

### Hamming Code Parameters

$$n = 2^r - 1 \text{ (total bits)}$$
$$k = n - r \text{ (data bits)}$$

| r | n | k | Code |
|---|---|---|------|
| 3 | 7 | 4 | Hamming(7,4) |
| 4 | 15 | 11 | Hamming(15,11) |
| 5 | 31 | 26 | Hamming(31,26) |

---

## 3.5 Flow Control

### Stop-and-Wait Protocol

```
Sender                    Receiver
  │─────Frame 0──────────→│
  │                        │
  │←────────ACK 0──────────│
  │                        │
  │─────Frame 1──────────→│
  │                        │
  │←────────ACK 1──────────│
```

**Efficiency:**

$$\eta = \frac{T_{trans}}{T_{trans} + 2 \times T_{prop}} = \frac{1}{1 + 2a}$$

Where $a = \frac{T_{prop}}{T_{trans}}$

**Problem:** Very inefficient for high $a$ (high delay-bandwidth product).

### Sliding Window Protocol

Send multiple frames before waiting for ACK.

#### Go-Back-N (GBN)

```
Window size = N
Sender:   [0][1][2][3] → → → Receiver
           └──┬──┴──┘
          Window size N

If Frame 2 lost:
- Receiver discards 3, 4, 5...
- Sender retransmits 2, 3, 4, 5...
```

**Window size:** $N \leq 2^n - 1$ (n = sequence number bits)

**Efficiency:**
$$\eta = \frac{N}{1 + 2a} \text{ if } N < 1 + 2a$$
$$\eta = 1 \text{ if } N \geq 1 + 2a$$

#### Selective Repeat (SR)

```
Window size = N
Sender:   [0][1][2][3] → → → Receiver
           └──────┘
          
If Frame 2 lost:
- Receiver accepts 3, 4, 5... (buffers them)
- Only Frame 2 retransmitted
```

**Window size:** $N \leq 2^{n-1}$ (half of sequence space)

### 🎯 Window Size Comparison

| Protocol | Max Window Size | Receiver Buffer |
|----------|-----------------|-----------------|
| Stop-and-Wait | 1 | 1 |
| Go-Back-N | $2^n - 1$ | 1 |
| Selective Repeat | $2^{n-1}$ | $2^{n-1}$ |

---

## 3.6 HDLC and PPP

### HDLC (High-level Data Link Control)

```
┌───────┬─────────┬─────────┬──────────┬─────────┬───────┐
│ Flag  │ Address │ Control │   Data   │   FCS   │ Flag  │
│ 8 bits│ 8 bits  │ 8/16 bits│ Variable │ 16/32 b │ 8 bits│
└───────┴─────────┴─────────┴──────────┴─────────┴───────┘
```

**Frame Types:**
- **I-frames:** Information (data)
- **S-frames:** Supervisory (flow control, error control)
- **U-frames:** Unnumbered (link management)

### PPP (Point-to-Point Protocol)

Used for dial-up, DSL.

```
┌───────┬─────────┬─────────┬────────┬──────────┬─────────┬───────┐
│ Flag  │ Address │ Control │Protocol│   Data   │   FCS   │ Flag  │
│ 1 byte│ 1 byte  │ 1 byte  │ 2 bytes│ Variable │ 2/4 byte│ 1 byte│
└───────┴─────────┴─────────┴────────┴──────────┴─────────┴───────┘
```

**Features:**
- Byte stuffing (0x7E flag, 0x7D escape)
- LCP (Link Control Protocol) for setup
- NCP (Network Control Protocol) for network layer
- Authentication (PAP, CHAP)

---

## 🎯 Practice Problems

### Problem 1: Bit Stuffing
**Q:** Apply bit stuffing: 0111111111110110

**Solution:**
- After 11111, insert 0
- 011111**0**1111**0**10110
- **Answer:** 01111101111010110

### Problem 2: CRC
**Q:** Data = 1001, Generator = 1011. Find CRC.

**Solution:**
```
1001000 ÷ 1011
1011
────
 0100
 0000
 ────
  1000
  1011
  ────
   011 ← CRC

Transmitted: 1001011
```

### Problem 3: Hamming Distance
**Q:** How many errors can be detected with Hamming distance 5?
**Answer:** $d - 1 = 4$ errors

### Problem 4: Stop-and-Wait Efficiency
**Q:** Bandwidth = 1 Mbps, RTT = 50 ms, Frame size = 1000 bits. Find efficiency.

**Solution:**
- $T_{trans} = \frac{1000}{10^6} = 1$ ms
- $a = \frac{T_{prop}}{T_{trans}} = \frac{25}{1} = 25$
- $\eta = \frac{1}{1 + 2 \times 25} = \frac{1}{51} = 1.96\%$

### Problem 5: Window Size
**Q:** GBN with 4-bit sequence number. Max window size?
**Answer:** $2^4 - 1 = 15$

### Problem 6: Selective Repeat
**Q:** SR with 4-bit sequence number. Max window size?
**Answer:** $2^3 = 8$

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"CRC Catches Really Corrupted data"**
**"Hamming Helps Heal single Hits"**

### The Mental Slider
- **Stop-and-Wait:** Polite conversation (wait for response)
- **Go-Back-N:** "I'll repeat everything from where you missed"
- **Selective Repeat:** "Just tell me what you missed"

### The 5-Second Snap-Check
1. **Bit stuffing?** Insert 0 after 11111
2. **CRC remainder?** That's the FCS
3. **Hamming parity positions?** Powers of 2
4. **GBN window?** $2^n - 1$
5. **SR window?** $2^{n-1}$

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| $\eta = \frac{1}{1+2a}$ | Stop-and-Wait efficiency |
| $a = \frac{T_{prop}}{T_{trans}}$ | Efficiency parameter |
| $N_{GBN} \leq 2^n - 1$ | Go-Back-N max window |
| $N_{SR} \leq 2^{n-1}$ | Selective Repeat max window |
| $d_{min} \geq 2t + 1$ | Correct t errors |
| $d_{min} \geq t + 1$ | Detect t errors |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Physical Layer](02-Physical-Layer.md) | [Next: MAC Layer →](04-MAC-Layer.md)
