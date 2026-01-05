# Module 3: Data Link Layer | The Singularity

> **The Atomic Truth:** *Data Link = Reliable hop-to-hop delivery*

---

## 3.1 Data Link Layer Overview

### **Position in Protocol Stack**
```
      Transport Layer
            ↓
       Network Layer (IP Packets)
            ↓
    ┌───────────────────────────┐
    │     DATA LINK LAYER       │
    │  ┌─────────────────────┐  │
    │  │      LLC            │  │ ← Logical Link Control
    │  ├─────────────────────┤  │
    │  │      MAC            │  │ ← Media Access Control
    │  └─────────────────────┘  │
    └───────────────────────────┘
            ↓
       Physical Layer (Bits)
```

### **Core Responsibilities**
1. **Framing** — Packaging bits into frames
2. **Physical Addressing** — MAC addresses
3. **Error Detection & Correction**
4. **Flow Control** — Prevent receiver overflow
5. **Access Control** — Who transmits when (MAC sublayer)

### **The Analogy 💡**
Data Link Layer is like a **local postman**:
- Knows your house (MAC address)
- Handles local delivery (hop-to-hop)
- Checks if package is damaged (error detection)
- Waits if your mailbox is full (flow control)

---

## 3.2 Framing

### **Why Framing?**
Physical layer transmits raw bits. We need to identify where one frame ends and another begins.

### **Framing Methods**

#### **1. Character Count**
- Header contains frame length
- **Problem:** If count is corrupted, all subsequent frames are lost

#### **2. Character Stuffing (Byte Stuffing)**
```
Flag = 01111110 (0x7E)
Escape = 01111101 (0x7D)

Original:  ... 0x7E ...
Stuffed:   ... 0x7D 0x5E ...

Original:  ... 0x7D ...
Stuffed:   ... 0x7D 0x5D ...
```

**Used in:** PPP (Point-to-Point Protocol)

#### **3. Bit Stuffing**
```
Flag: 01111110

Rule: After five consecutive 1s in data, insert a 0

Original: 0111111110
Stuffed:  01111101110
          ↑ inserted 0
```

**Used in:** HDLC, Frame Relay

### **GATE Trap Alert ⚠️**

**Question Type:** "After bit stuffing, what is the transmitted sequence?"

**Method:**
1. Scan for 5 consecutive 1s
2. Insert 0 after them
3. Remember: Flag (01111110) is NOT stuffed — it's added at boundaries

---

## 3.3 Error Detection

### **The Atomic Truth:** *Error detection finds errors; Error correction fixes them*

### **3.3.1 Parity Check**

**Simple (1D) Parity:**
- Add 1 bit to make total 1s even (even parity) or odd (odd parity)
- Detects: Single bit errors
- **Cannot detect:** Even number of bit errors

**Two-Dimensional Parity:**
```
Data:        Row Parity:
1 0 1 1      1
0 1 1 0      0
1 1 1 0      1
─────────
0 0 1 1   ← Column Parity
```

- Can detect and **correct single bit errors**
- Can detect (not correct) any combination of 2 errors
- Can detect many burst errors

### **3.3.2 Checksum**

**Process:**
1. Divide data into 16-bit words
2. Add all words using 1's complement addition
3. Take 1's complement of sum = checksum

**Used in:** IP, TCP, UDP headers

**1's Complement Addition:**
- If carry-out occurs, add it back to the result (wrap-around carry)

### **3.3.3 Cyclic Redundancy Check (CRC) 🔑**

**The Most Important Error Detection for GATE**

**The Process:**
1. Append $r$ zeros to data (where $r$ = degree of generator polynomial)
2. Divide by generator polynomial using XOR division
3. Remainder = CRC (FCS - Frame Check Sequence)
4. Transmit: Data + CRC

**Standard Generators:**
| Name | Polynomial | Bits |
|------|------------|------|
| CRC-8 | $x^8 + x^2 + x + 1$ | 9 bits |
| CRC-16 | $x^{16} + x^{15} + x^2 + 1$ | 17 bits |
| CRC-32 | Used in Ethernet | 33 bits |
| CRC-CCITT | $x^{16} + x^{12} + x^5 + 1$ | 17 bits |

### **CRC Calculation Example**

**Problem:** Data = 1101011011, Generator = 10011 (CRC-4, $x^4 + x + 1$)

**Step 1:** Append 4 zeros (degree = 4)
Data = 11010110110000

**Step 2:** XOR Division
```
        1100001010
       ─────────────
10011 │11010110110000
       10011
       ─────
        10011
        10011
        ─────
         00001 0110000
             1 0011
             ──────
               010100
                10011
                ─────
                 01110 ← Remainder (CRC)
```

**Step 3:** Transmitted Frame = 11010110111110

### **CRC Error Detection Capability**

CRC with $r$-bit polynomial can detect:
1. ✅ All single-bit errors
2. ✅ All double-bit errors (if polynomial has at least 3 terms)
3. ✅ All odd number of bit errors (if $(x+1)$ is a factor)
4. ✅ All burst errors of length ≤ r
5. ✅ Most burst errors of length > r

---

## 3.4 Error Correction

### **3.4.1 Hamming Code**

**The Golden Relationship:**
$$2^r \geq m + r + 1$$

Where:
- $m$ = data bits
- $r$ = parity bits
- $n = m + r$ = total bits (codeword length)

**The Hamming Distance**
$$d_{min} = \text{Minimum number of bit differences between any two valid codewords}$$

**Detection & Correction Capability:**
| To Detect | To Correct | Minimum Distance Required |
|-----------|------------|---------------------------|
| d errors | — | $d_{min} \geq d + 1$ |
| — | d errors | $d_{min} \geq 2d + 1$ |
| d errors | t errors | $d_{min} \geq d + t + 1$ |

**Hamming (7,4) Code:**
- 4 data bits, 3 parity bits
- $d_{min} = 3$
- Can detect 2 errors OR correct 1 error

**Parity Bit Positions:**
- Positions that are powers of 2: 1, 2, 4, 8, 16...
- Position 1 checks bits 1, 3, 5, 7, 9, 11...
- Position 2 checks bits 2, 3, 6, 7, 10, 11...
- Position 4 checks bits 4, 5, 6, 7, 12, 13, 14, 15...

### **GATE Favorite: Hamming Code Construction**

**Example:** Encode data bits D = 1011

**Step 1:** Determine positions
- Total bits = 7 (since $2^3 \geq 4 + 3 + 1$)
- Parity positions: 1, 2, 4
- Data positions: 3, 5, 6, 7

```
Position:  1  2  3  4  5  6  7
Content:  P1 P2 D1 P4 D2 D3 D4
          P1 P2  1 P4  0  1  1
```

**Step 2:** Calculate parity bits (even parity)
- P1 checks positions 1,3,5,7: P1⊕1⊕0⊕1 = 0 → P1 = 0
- P2 checks positions 2,3,6,7: P2⊕1⊕1⊕1 = 0 → P2 = 1
- P4 checks positions 4,5,6,7: P4⊕0⊕1⊕1 = 0 → P4 = 0

**Codeword:** 0110011

### **Error Detection with Hamming Code**

If received codeword has error at position X:
1. Check each parity group
2. Syndrome = P4P2P1 (binary) = Position of error
3. Flip that bit

---

## 3.5 Flow Control Protocols

### **The Problem**
Fast sender can overwhelm slow receiver.

### **3.5.1 Stop-and-Wait**

```
Sender                 Receiver
  │                        │
  │──── Frame 0 ──────────>│
  │                        │
  │<──── ACK 0 ────────────│
  │                        │
  │──── Frame 1 ──────────>│
  │                        │
  │<──── ACK 1 ────────────│
```

**Efficiency (Utilization):**

$$\eta = \frac{T_{trans}}{T_{trans} + 2 \times T_{prop}} = \frac{1}{1 + 2a}$$

Where:
$$a = \frac{T_{prop}}{T_{trans}} = \frac{\text{Propagation Delay}}{\text{Transmission Delay}}$$

**The Golden Insight:**
- If $a$ is large (long distance, small frames), efficiency is VERY low
- Stop-and-Wait is good only when $a < 1$

### **3.5.2 Sliding Window Protocol**

**The Core Idea:** Send multiple frames before waiting for ACK

**Window Sizes:**
- **Sender Window ($W_s$):** Max frames that can be outstanding
- **Receiver Window ($W_r$):** Max frames that can be accepted

**For $n$-bit sequence numbers:**
- Total sequences: $2^n$
- Go-Back-N: $W_s \leq 2^n - 1$, $W_r = 1$
- Selective Repeat: $W_s \leq 2^{n-1}$, $W_r \leq 2^{n-1}$

### **Efficiency with Sliding Window:**

$$\eta = \begin{cases} 1 & \text{if } W \geq 1 + 2a \\ \frac{W}{1 + 2a} & \text{if } W < 1 + 2a \end{cases}$$

### **Go-Back-N (GBN) ARQ**

```
Sender Window: N frames
Receiver Window: 1 frame

If error in frame k:
  → Receiver discards frame k and all subsequent frames
  → Sender retransmits frame k and all subsequent frames
```

**Pros:** Simple receiver
**Cons:** Wastes bandwidth on retransmissions

### **Selective Repeat (SR) ARQ**

```
Sender Window: N frames
Receiver Window: N frames

If error in frame k:
  → Receiver buffers out-of-order frames
  → Sender retransmits ONLY frame k
```

**Pros:** Efficient retransmission
**Cons:** Complex receiver, needs buffering

### **GATE Trap Alert ⚠️**

**Window Size Constraint for SR:**
$$W_s + W_r \leq 2^n$$

If $W_s = W_r$, then $W_s \leq 2^{n-1}$

**Why?** To distinguish between new frames and retransmissions.

---

## 3.6 HDLC (High-Level Data Link Control)

### **Frame Format**

```
┌───────┬─────────┬─────────┬─────────────┬─────────┬───────┐
│ Flag  │ Address │ Control │    Data     │   FCS   │ Flag  │
│8 bits │ 8 bits  │ 8/16bits│  Variable   │ 16/32bits│8 bits │
│01111110│         │         │             │   CRC   │01111110│
└───────┴─────────┴─────────┴─────────────┴─────────┴───────┘
```

### **Frame Types**

| Type | Control Field | Purpose |
|------|---------------|---------|
| **I-frame** | 0 xxx xxxx | Information (data) |
| **S-frame** | 10 xx xxxx | Supervisory (ACK, NAK) |
| **U-frame** | 11 xx xxxx | Unnumbered (setup, disconnect) |

---

## 3.7 PPP (Point-to-Point Protocol)

### **Frame Format**

```
┌───────┬─────────┬─────────┬──────────┬─────────────┬─────────┬───────┐
│ Flag  │ Address │ Control │ Protocol │    Data     │   FCS   │ Flag  │
│ 0x7E  │  0xFF   │  0x03   │  2 bytes │  Variable   │ 2 bytes │ 0x7E  │
└───────┴─────────┴─────────┴──────────┴─────────────┴─────────┴───────┘
```

### **PPP vs HDLC**

| Feature | HDLC | PPP |
|---------|------|-----|
| Addressing | Variable | Always 0xFF |
| Protocol Field | No | Yes |
| Authentication | No | PAP, CHAP |
| Byte Stuffing | Bit stuffing | 0x7D escape |

---

## 3.8 MAC (Media Access Control) Sublayer

### **The Problem:** Who transmits on a shared medium?

### **Classification**

```
              MAC PROTOCOLS
                   │
     ┌─────────────┼─────────────┐
     │             │             │
  Random        Controlled    Channelization
  Access        Access
     │             │             │
  ALOHA        Polling         FDMA
  CSMA         Token Ring      TDMA
  CSMA/CD      Reservation     CDMA
  CSMA/CA
```

---

## 3.9 Random Access Protocols

### **3.9.1 ALOHA**

#### **Pure ALOHA**

```
Timeline:
  │     │     │     │     │     │     │
──┴─────┴─────┴─────┴─────┴─────┴─────┴──→ Time
    A transmits    ← Vulnerable Period = 2T →
```

**Vulnerable Period = 2T** (where T = frame transmission time)

**Throughput:**
$$S = G \cdot e^{-2G}$$

Where $G$ = offered load (average frames per frame time)

**Maximum Throughput:** At $G = 0.5$
$$S_{max} = \frac{1}{2e} \approx 0.184 = 18.4\%$$

#### **Slotted ALOHA**

- Time divided into slots = frame transmission time
- Transmit only at slot beginning

**Vulnerable Period = T**

**Throughput:**
$$S = G \cdot e^{-G}$$

**Maximum Throughput:** At $G = 1$
$$S_{max} = \frac{1}{e} \approx 0.368 = 36.8\%$$

### **The Mnemonic 🧠**
> **"Pure ALOHA = 18%, Slotted = 36%"**
> Slotted is exactly 2× Pure

### **3.9.2 CSMA (Carrier Sense Multiple Access)**

**"Listen before transmit"**

| Variant | Behavior | Efficiency |
|---------|----------|------------|
| **1-Persistent** | If idle, transmit immediately. If busy, wait and transmit immediately when idle. | High collision, low delay |
| **Non-persistent** | If idle, transmit. If busy, wait random time then repeat. | Low collision, higher delay |
| **p-Persistent** | If idle, transmit with probability p. If busy, wait for next slot. | Configurable trade-off |

### **3.9.3 CSMA/CD (Collision Detection)**

**Used in:** Ethernet (802.3)

**Minimum Frame Size Constraint:**
$$T_{transmission} \geq 2 \times T_{propagation}$$

$$\text{Frame}_{min} = 2 \times \frac{d}{v} \times B$$

Where:
- $d$ = maximum distance
- $v$ = propagation speed
- $B$ = bandwidth

**For Ethernet:**
- Min frame = 64 bytes
- Max segment = 2500m (with repeaters)

**Efficiency:**
$$\eta = \frac{1}{1 + 5a}$$

Where $a = \frac{T_p}{T_t}$

### **3.9.4 CSMA/CA (Collision Avoidance)**

**Used in:** WiFi (802.11)

**Why not CD?**
- Wireless: Hard to detect collisions while transmitting (hidden terminal problem)
- Signal attenuation makes collision detection unreliable

**Mechanism:**
1. Wait for DIFS (Distributed Inter-Frame Space)
2. If idle, wait random backoff
3. Send RTS (Request to Send)
4. Receive CTS (Clear to Send)
5. Transmit data
6. Receive ACK

```
Sender              Medium              Receiver
  │                    │                    │
  │─── Wait DIFS ──────│                    │
  │─── RTS ────────────│───────────────────>│
  │                    │<────── CTS ────────│
  │─── Data ───────────│───────────────────>│
  │                    │<────── ACK ────────│
```

---

## 3.10 Controlled Access Protocols

### **Polling**
- Primary station controls transmission
- Polls secondary stations one by one
- **Pros:** No collision
- **Cons:** Overhead, single point of failure

### **Token Passing**
- Token circulates on ring
- Only token holder can transmit
- **Used in:** Token Ring (802.5), FDDI

---

## 3.11 Summary Formulas

### **Error Detection/Correction**

| Topic | Formula |
|-------|---------|
| Hamming Code | $2^r \geq m + r + 1$ |
| Detection capability | $d_{min} \geq d + 1$ |
| Correction capability | $d_{min} \geq 2d + 1$ |
| Both (d detect, t correct) | $d_{min} \geq d + t + 1$ |

### **Flow Control**

| Protocol | Efficiency |
|----------|------------|
| Stop-and-Wait | $\frac{1}{1 + 2a}$ |
| Sliding Window | $\min(1, \frac{W}{1 + 2a})$ |
| GBN Window | $W \leq 2^n - 1$ |
| SR Window | $W \leq 2^{n-1}$ |

### **MAC Protocols**

| Protocol | Max Throughput |
|----------|----------------|
| Pure ALOHA | $\frac{1}{2e} = 18.4\%$ |
| Slotted ALOHA | $\frac{1}{e} = 36.8\%$ |
| CSMA/CD | $\frac{1}{1 + 5a}$ (approx) |

---

## 3.12 Solved Examples

### **Example 1: CRC Calculation**

**Problem:** Find CRC for data 1001 using generator 1011.

**Solution:**
Degree of generator = 3, so append 3 zeros.
Data = 1001000

```
      1010
     ─────
1011│1001000
     1011
     ────
      010000
       1011
       ────
        1110
        1011
        ────
         101 ← CRC
```

Transmitted: 1001101

---

### **Example 2: Hamming Code**

**Problem:** How many parity bits are needed for 16 data bits?

**Solution:**
$2^r \geq m + r + 1$
$2^r \geq 16 + r + 1$

Try $r = 5$: $32 \geq 22$ ✓

Answer: **5 parity bits**

---

### **Example 3: Stop-and-Wait Efficiency**

**Problem:** Link of 1 Mbps, propagation delay = 10 ms, frame size = 1000 bytes. Find efficiency.

**Solution:**
$T_{trans} = \frac{1000 \times 8}{10^6} = 8$ ms

$a = \frac{T_{prop}}{T_{trans}} = \frac{10}{8} = 1.25$

$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2.5} = \frac{1}{3.5} = \boxed{28.57\%}$

---

### **Example 4: Sliding Window**

**Problem:** If sequence numbers use 3 bits, what is the maximum window size for:
(a) Go-Back-N
(b) Selective Repeat

**Solution:**
$n = 3$ bits, so $2^n = 8$ sequences

(a) GBN: $W_{max} = 2^n - 1 = 7$

(b) SR: $W_{max} = 2^{n-1} = 4$

---

## 3.13 Practice Problems

**Q1.** The vulnerable period of slotted ALOHA is:
- (a) T
- (b) 2T
- (c) T/2
- (d) 4T

<details>
<summary>Answer</summary>
**(a) T** — In slotted ALOHA, collisions only occur within the same slot.
</details>

---

**Q2.** For a Hamming code with m=11 data bits, minimum parity bits required is:
- (a) 3
- (b) 4
- (c) 5
- (d) 6

<details>
<summary>Answer</summary>
**(b) 4** — $2^4 = 16 \geq 11 + 4 + 1 = 16$ ✓
</details>

---

**Q3.** [NAT] Maximum throughput of pure ALOHA (as percentage, round to one decimal):

<details>
<summary>Answer</summary>
$S_{max} = \frac{1}{2e} = \boxed{18.4}\%$
</details>

---

## 3.14 The 5-Second Snap-Check ✅

1. ☐ Bit stuffing: Insert 0 after five 1s
2. ☐ CRC: Append r zeros, XOR divide, remainder = CRC
3. ☐ Hamming: $2^r \geq m + r + 1$
4. ☐ Stop-Wait efficiency: $\frac{1}{1+2a}$
5. ☐ ALOHA throughput: Pure=18.4%, Slotted=36.8%
6. ☐ Window constraints: GBN = $2^n-1$, SR = $2^{n-1}$

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 4: LAN Technologies →](./04-LAN-Technologies.md)
