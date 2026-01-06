# Chapter 3: Data Link Layer

## 🎯 GATE/ESE Weightage: 8-12 marks (Heavy Numericals)

---

## 3.1 Data Link Layer Functions

The Data Link Layer is responsible for **node-to-node** delivery of frames over a single link.

**Core Functions**:
1. **Framing**: Package bits into frames
2. **Physical Addressing**: MAC address handling
3. **Error Control**: Detection and correction
4. **Flow Control**: Prevent receiver overflow
5. **Access Control**: Who transmits when (MAC sublayer)

### Sublayers

```
┌─────────────────────────────────────┐
│        DATA LINK LAYER              │
├─────────────────────────────────────┤
│  LLC (Logical Link Control)         │  ← Flow/Error control (802.2)
├─────────────────────────────────────┤
│  MAC (Medium Access Control)        │  ← Physical addressing, access (802.3, 802.11)
└─────────────────────────────────────┘
```

---

## 3.2 Framing

### Why Framing?

Physical layer sends streams of bits. Data link layer must:
- Mark beginning and end of frames
- Separate frames from each other
- Enable error detection per frame

### Framing Methods

#### 1. Character Count

```
Frame 1        Frame 2        Frame 3
┌─────────────┬─────────────┬─────────────┐
│ 5 │ A B C D │ 6 │ E F G H I │ ...        │
└───┴─────────┴───┴───────────┴─────────────┘
  ↑             ↑
Count includes  Count = 6 bytes total
itself
```

**Problem**: If count is corrupted, sync is lost forever!
**Status**: Rarely used alone

#### 2. Byte Stuffing (Character Stuffing)

```
FLAG = 01111110 (ESC sequence)

Original: [Data with FLAG pattern]
Stuffed:  [Data with ESC + FLAG pattern]

If data contains ESC: Add another ESC
```

**Example (BSC Protocol)**:
- FLAG = DLE STX (start), DLE ETX (end)
- If DLE in data: Insert extra DLE

#### 3. Bit Stuffing (🎯 GATE FAVORITE)

```
FLAG pattern: 01111110

Rule: After 5 consecutive 1s, insert 0

Original:    011111111110
Stuffed:     0111110111110 0
                   ↑      ↑
              Inserted bits

Receiver: Remove 0 after five 1s
```

**🧠 Why 5 ones?**: FLAG has 6 ones. By stuffing after 5, we prevent data from looking like FLAG.

**Used in**: HDLC, PPP

**🎯 GATE Problem Pattern**:
**Q**: Given 01111110 as flag, stuff: 0111111111110
**A**: After every 5 ones, insert 0:
       01111**0**1111**0**10  → Stuffed output

#### 4. Physical Layer Coding Violations

- Use invalid signal patterns to mark boundaries
- Example: Manchester encoding violations
- Used in Token Ring

---

## 3.3 Error Detection & Correction (🎯 VERY IMPORTANT)

### Types of Errors

```
SINGLE-BIT ERROR:           BURST ERROR:
Sent:    10101010           Sent:    10101010
Received: 10001010          Received: 10011110
              ↑                        ↑↑↑
           One bit flipped          Multiple consecutive bits
```

### Hamming Distance

**Definition**: Number of bit positions where two codewords differ.

```
Codeword 1: 10101
Codeword 2: 10010
XOR:        00111  → Hamming distance = 3
```

**🎯 Key Formulas**:

| Requirement | Minimum Hamming Distance |
|-------------|-------------------------|
| Detect d errors | d_min ≥ d + 1 |
| Correct d errors | d_min ≥ 2d + 1 |
| Detect d, correct c errors | d_min ≥ d + c + 1 |

**Example**: To detect 2-bit and correct 1-bit errors:
- d_min ≥ 2 + 1 + 1 = 4

### Parity Check

```
EVEN PARITY: Number of 1s (including parity) is even
ODD PARITY: Number of 1s (including parity) is odd

Data:    1011001
Even parity: 1011001 1  (4 ones → add 1)
Odd parity:  1011001 0  (4 ones → add 0)
```

**Limitation**: Can detect only **odd number** of errors (Hamming distance = 2)

### Two-Dimensional Parity

```
    1 0 1 1 | 1
    0 1 1 0 | 0
    1 1 0 1 | 1
    --------+--
    0 0 0 0 | 0
         ↑
    Column parity
```

**Advantage**: Can detect AND correct single-bit errors
**Limitation**: Cannot correct burst errors

### Checksum

```
1. Divide data into fixed-size words (e.g., 16 bits)
2. Add all words using 1's complement arithmetic
3. Complement the sum = Checksum
4. Sender appends checksum
5. Receiver adds all words + checksum
6. Result should be all 1s (or 0 after complement)
```

**Example (8-bit checksum)**:
```
Data:    10101001
         00111001
Sum:     11100010
Checksum: 00011101 (complement)

Verification: 10101001 + 00111001 + 00011101 = 11111111 ✓
```

**Used in**: IP, TCP, UDP headers

### CRC (Cyclic Redundancy Check) (🎯 MOST IMPORTANT)

**The most powerful error detection method in Data Link Layer**

```
┌─────────────────────────────────────────────────────────┐
│              CRC ALGORITHM                              │
│                                                         │
│  1. Append n zeros to message (n = degree of polynomial)│
│  2. Divide by generator polynomial using XOR            │
│  3. Remainder = CRC (n bits)                           │
│  4. Append CRC to original message                     │
│  5. Transmitted = Message + CRC                        │
│  6. Receiver divides by same polynomial               │
│  7. If remainder = 0, no error detected               │
└─────────────────────────────────────────────────────────┘
```

#### CRC Step-by-Step (🎯 MUST PRACTICE)

**Problem**: Data = 1101, Generator = 1011 (CRC-3)

**Step 1**: Append 3 zeros (generator degree = 3): **1101000**

**Step 2**: Polynomial division (XOR):
```
        1010  ← Quotient (ignore)
       ─────────
1011 │ 1101000
       1011
       ────
        1100
        1011
        ────
         1110
         1011
         ────
          1010
          1011
          ────
           001  ← Remainder (CRC)
```

**Step 3**: Transmitted message = 1101 + 001 = **1101001**

**Verification**: Divide 1101001 by 1011 → Remainder should be 000 ✓

#### Standard CRC Polynomials

| CRC | Polynomial | Detects |
|-----|------------|---------|
| CRC-8 | x⁸ + x² + x + 1 | 8-bit errors |
| CRC-16 | x¹⁶ + x¹⁵ + x² + 1 | Up to 16-bit burst |
| CRC-32 | x³² + x²⁶ + x²³ + ... | Ethernet, ZIP |
| CRC-CCITT | x¹⁶ + x¹² + x⁵ + 1 | HDLC, X.25 |

**🎯 CRC Detection Capabilities**:
- **All single-bit errors**: If polynomial has ≥ 2 terms
- **All double-bit errors**: Certain polynomials
- **All odd number of errors**: If polynomial has (x+1) as factor
- **Burst errors ≤ n bits**: 100% detection (n = polynomial degree)
- **Burst errors = n+1 bits**: Miss probability = 1/2^(n-1)
- **Burst errors > n+1 bits**: Miss probability = 1/2^n

### Hamming Code (🎯 GATE FAVORITE)

**Purpose**: Error correction (not just detection)

**Structure**:
- Parity bits at positions 2^i (1, 2, 4, 8, 16, ...)
- Data bits at remaining positions
- Each parity covers specific bit positions

```
Position: 1  2  3  4  5  6  7
Type:     P1 P2 D1 P4 D2 D3 D4

P1 checks: 1, 3, 5, 7 (binary: xxx1)
P2 checks: 2, 3, 6, 7 (binary: xx1x)
P4 checks: 4, 5, 6, 7 (binary: x1xx)
```

#### Hamming Code Formula

```
For m data bits, need r parity bits:

2^r ≥ m + r + 1

Number of data bits + parity bits = codeword length
```

| Data bits (m) | Parity bits (r) | Codeword |
|---------------|-----------------|----------|
| 1 | 2 | 3 |
| 4 | 3 | 7 |
| 11 | 4 | 15 |
| 26 | 5 | 31 |

**🎯 GATE Example**:
**Q**: Data = 1011 (4 bits), find Hamming code.

**Solution**:
```
Positions: 1  2  3  4  5  6  7
Type:      P1 P2 D1 P4 D2 D3 D4
Data:      _  _  1  _  0  1  1

P1 (1,3,5,7): P1 ⊕ 1 ⊕ 0 ⊕ 1 = 0 → P1 = 0
P2 (2,3,6,7): P2 ⊕ 1 ⊕ 1 ⊕ 1 = 0 → P2 = 1
P4 (4,5,6,7): P4 ⊕ 0 ⊕ 1 ⊕ 1 = 0 → P4 = 0

Codeword: 0 1 1 0 0 1 1 = 0110011
```

**Error Detection**:
```
Received: 0110111 (bit 5 flipped)

Check P1 (1,3,5,7): 0 ⊕ 1 ⊕ 1 ⊕ 1 = 1 (error)
Check P2 (2,3,6,7): 1 ⊕ 1 ⊕ 1 ⊕ 1 = 0 (ok)
Check P4 (4,5,6,7): 0 ⊕ 1 ⊕ 1 ⊕ 1 = 1 (error)

Error position = P4 P2 P1 = 1 0 1 = 5 ✓
```

---

## 3.4 Flow Control Protocols (🎯 MOST ASKED)

### Why Flow Control?

Prevent **fast sender** from overwhelming **slow receiver**.

### Stop-and-Wait Protocol

```
Sender                              Receiver
  │                                    │
  │────── Frame 0 ────────────────────→│
  │                                    │
  │←──────── ACK 0 ────────────────────│
  │                                    │
  │────── Frame 1 ────────────────────→│
  │                                    │
  │←──────── ACK 1 ────────────────────│
  │                                    │

Send one frame → Wait for ACK → Send next
```

**🎯 Efficiency Formula (CRITICAL)**:

```
η = Tt / (Tt + 2×Tp)
  = 1 / (1 + 2a)

Where:
a = Tp/Tt = Propagation delay / Transmission delay
η = Efficiency (utilization)
```

**Example**:
- L = 1000 bits, B = 1 Mbps, D = 2000 km, V = 2×10⁸ m/s
- Tt = 1000 / 10⁶ = 1 ms
- Tp = 2×10⁶ / (2×10⁸) = 10 ms
- a = 10/1 = 10
- η = 1 / (1 + 2×10) = 1/21 = **4.76%** 😱

**Problem**: Terribly inefficient for high bandwidth-delay product!

### Sliding Window Protocols

**Solution**: Send multiple frames before waiting for ACK

```
Window Size (W) = Number of frames sent before waiting

Sender window:    [0][1][2][3]    (can send 0-3)
                   ↑     ↑
               sent   can send

After ACK 0:      [1][2][3][4]    (window slides)
```

### Go-Back-N (GBN)

```
Sender Window = N, Receiver Window = 1

Sender                              Receiver
  │────── Frame 0 ────────────────────→│
  │────── Frame 1 ────────────────────→│
  │────── Frame 2 ────────────✗        │ (Frame 2 lost)
  │────── Frame 3 ────────────────────→│ (Discarded! Out of order)
  │←──────── ACK 0 ────────────────────│
  │←──────── ACK 1 ────────────────────│
  │        (Timeout for Frame 2)       │
  │────── Frame 2 ────────────────────→│ ← Retransmit from 2
  │────── Frame 3 ────────────────────→│
  │────── Frame 4 ────────────────────→│
  │←──────── ACK 2 ────────────────────│
  ...
```

**Key Points**:
- **Sender window**: N frames
- **Receiver window**: 1 frame (expects specific sequence)
- **Error**: Discard all subsequent frames, retransmit from error
- **ACK**: Cumulative (ACK n means all up to n received)

**🎯 Window Size Constraint**:
```
W ≤ 2^m - 1

Where m = number of bits for sequence number
```

**Why 2^m - 1?** If W = 2^m, receiver can't distinguish retransmission from new frame.

### Selective Repeat (SR)

```
Sender Window = N, Receiver Window = N

Sender                              Receiver
  │────── Frame 0 ────────────────────→│
  │────── Frame 1 ────────────────────→│
  │────── Frame 2 ────────────✗        │ (Frame 2 lost)
  │────── Frame 3 ────────────────────→│ (Buffered!)
  │←──────── ACK 0 ────────────────────│
  │←──────── ACK 1 ────────────────────│
  │←──────── NAK 2 ────────────────────│ (Request retransmission)
  │←──────── ACK 3 ────────────────────│ (Out of order ACK!)
  │────── Frame 2 ────────────────────→│ ← Only retransmit Frame 2
  │←──────── ACK 2 ────────────────────│
```

**Key Points**:
- **Both windows**: N frames
- **Receiver buffers**: Out-of-order frames
- **Retransmit**: Only lost frames (not all subsequent)
- **ACK**: Individual (not cumulative)

**🎯 Window Size Constraint**:
```
W ≤ 2^(m-1) = 2^m / 2

Each window ≤ half of sequence number space
```

**Why half?** Sender and receiver windows combined shouldn't exceed total sequence numbers.

### Protocol Comparison (🎯 MEMORIZE)

| Feature | Stop-Wait | Go-Back-N | Selective Repeat |
|---------|-----------|-----------|------------------|
| Sender Window | 1 | N | N |
| Receiver Window | 1 | 1 | N |
| ACK Type | Individual | Cumulative | Individual |
| Retransmission | Single frame | From error onwards | Only lost frame |
| Receiver Buffer | None | None | Required |
| Max Window Size | 1 | 2^m - 1 | 2^(m-1) |
| Efficiency | Low | Medium | High |
| Complexity | Simplest | Medium | Most complex |

### 🎯 Efficiency Formulas

**Stop-and-Wait**:
```
η = 1 / (1 + 2a)
```

**Sliding Window (GBN/SR)**:
```
If W ≥ 1 + 2a:  η = 1 (100% efficient)
If W < 1 + 2a:  η = W / (1 + 2a)

Where:
W = Window size
a = Tp / Tt
```

**🎯 GATE Problem Pattern**:

**Q**: L = 1000 bits, B = 10 Mbps, RTT = 50 ms, Window = ?

**Solution**:
```
Tt = 1000 / (10 × 10⁶) = 0.1 ms
Tp = RTT/2 = 25 ms
a = 25 / 0.1 = 250

For 100% efficiency: W ≥ 1 + 2a = 1 + 500 = 501 frames
```

---

## 3.5 HDLC (High-Level Data Link Control)

### Frame Format

```
┌───────┬─────────┬─────────┬─────────────────┬───────┬───────┐
│ Flag  │ Address │ Control │      Data       │  FCS  │ Flag  │
│01111110│ 8 bits │ 8/16 bit│   Variable      │16/32bit│01111110│
└───────┴─────────┴─────────┴─────────────────┴───────┴───────┘
```

### Frame Types

| Type | Purpose | Control Field Pattern |
|------|---------|----------------------|
| **I-frame** | Information | 0 X X X X X X X |
| **S-frame** | Supervisory (ACK, NAK) | 1 0 X X X X X X |
| **U-frame** | Unnumbered (control) | 1 1 X X X X X X |

### S-Frame Types

| Frame | Function | Bits |
|-------|----------|------|
| **RR** (Receive Ready) | ACK, ready for more | 00 |
| **RNR** (Receive Not Ready) | ACK, pause sending | 01 |
| **REJ** (Reject) | NAK, retransmit from N | 10 |
| **SREJ** (Selective Reject) | NAK, retransmit N only | 11 |

---

## 3.6 PPP (Point-to-Point Protocol)

### Why PPP?

- Most common WAN protocol
- Used for dial-up, DSL, direct connections
- Supports multiple network protocols
- Authentication (PAP, CHAP)

### PPP Frame Format

```
┌───────┬─────────┬─────────┬──────────┬─────────────┬───────┬───────┐
│ Flag  │ Address │ Control │ Protocol │    Data     │  FCS  │ Flag  │
│  7E   │   FF    │   03    │  2 bytes │  ≤1500      │2 bytes│  7E   │
└───────┴─────────┴─────────┴──────────┴─────────────┴───────┴───────┘
```

**Protocol Field Values**:
| Value | Protocol |
|-------|----------|
| 0x0021 | IP |
| 0x8021 | IPCP (IP Control Protocol) |
| 0xC021 | LCP (Link Control Protocol) |
| 0xC023 | PAP (Authentication) |
| 0xC223 | CHAP (Challenge-Handshake) |

### PPP Phases

```
1. DEAD (Physical layer not ready)
      ↓
2. ESTABLISH (LCP negotiation)
      ↓
3. AUTHENTICATE (Optional: PAP/CHAP)
      ↓
4. NETWORK (NCP negotiation, IP config)
      ↓
5. OPEN (Data transfer)
      ↓
6. TERMINATE (LCP close)
```

---

## 3.7 Medium Access Control (MAC) (🎯 VERY IMPORTANT)

### Why MAC?

In shared medium (bus, wireless), only ONE station should transmit at a time.

### MAC Protocol Classification

```
MAC Protocols
├── Random Access (Contention)
│   ├── ALOHA (Pure, Slotted)
│   ├── CSMA
│   ├── CSMA/CD (Ethernet)
│   └── CSMA/CA (Wi-Fi)
│
├── Controlled Access
│   ├── Reservation
│   ├── Polling
│   └── Token Passing
│
└── Channelization
    ├── FDMA
    ├── TDMA
    └── CDMA
```

---

## 3.8 ALOHA (🎯 GATE FAVORITE)

### Pure ALOHA

```
Station transmits whenever it has data
    ↓
Collision detected? → Wait random time → Retransmit
    ↓
Success? → Done
```

**Vulnerable Period**: If two frames overlap **at all**, both are corrupted.

```
     Vulnerable Period = 2 × Tt
     ←────────────────────────────→
     │                            │
 ────┼────── Frame A ─────────────┼────
     │       ────── Frame B ──────┤
     │            Collision!      │
```

**🎯 Throughput Formula (CRITICAL)**:

```
S = G × e^(-2G)

Where:
S = Throughput (successful transmissions)
G = Offered load (attempted transmissions)

Maximum throughput: S_max = 1/(2e) ≈ 0.184 = 18.4%
At G = 0.5
```

### Slotted ALOHA

**Improvement**: Time divided into slots. Transmit only at slot boundary.

```
Slot 1     Slot 2     Slot 3     Slot 4
│──────────│──────────│──────────│──────────│
│  Frame A │  Empty   │Collision │  Frame C │
└──────────┴──────────┴──────────┴──────────┘

Vulnerable period = 1 × Tt (reduced to half)
```

**🎯 Throughput Formula**:

```
S = G × e^(-G)

Maximum throughput: S_max = 1/e ≈ 0.368 = 36.8%
At G = 1
```

### ALOHA Comparison

| Feature | Pure ALOHA | Slotted ALOHA |
|---------|------------|---------------|
| Vulnerable Period | 2 × Tt | Tt |
| Max Throughput | 18.4% | 36.8% |
| Optimal Load (G) | 0.5 | 1.0 |
| Synchronization | Not needed | Required |

---

## 3.9 CSMA (Carrier Sense Multiple Access)

**Improvement**: Listen before transmit ("listen before talk")

### CSMA Variants

#### 1-Persistent CSMA
```
If channel busy → Wait until idle → Transmit immediately (prob = 1)
```
**Problem**: If multiple waiting, all transmit simultaneously → collision

#### Non-Persistent CSMA
```
If channel busy → Wait random time → Check again
```
**Advantage**: Fewer collisions
**Disadvantage**: Wasted idle time

#### p-Persistent CSMA (Slotted)
```
If channel idle → Transmit with probability p
                → Wait one slot with probability (1-p)
```
**Compromise**: Balances collision vs idle time

### Vulnerability in CSMA

```
                 ←─ Propagation delay ─→
Station A ────────●────────────────────●──────── Station B
                  │                    │
              A starts            B doesn't hear A yet
              transmitting        B also transmits
                                      ↓
                                  COLLISION!
```

**Key Insight**: Collision still possible during **propagation delay**!

---

## 3.10 CSMA/CD (Ethernet) (🎯 MOST IMPORTANT)

**Carrier Sense Multiple Access with Collision Detection**

### Algorithm

```
1. Prepare frame
2. Sense channel
   └── If busy → Wait
   └── If idle → Start transmitting
3. While transmitting, monitor channel
   └── Collision detected?
       ├── Send JAM signal (48 bits)
       ├── Wait random time (exponential backoff)
       └── Go to step 2
4. Transmission successful
```

### 🎯 Minimum Frame Size (CRITICAL)

**Why minimum frame size?**
- Sender must still be transmitting when collision signal returns
- Otherwise, sender thinks transmission was successful

```
Minimum Frame Size ≥ 2 × Propagation Delay × Bandwidth
                    = 2 × Tp × B
                    = RTT × B
```

**Ethernet Example**:
- Maximum cable length: 2500 m
- Speed: 10 Mbps
- V = 2 × 10⁸ m/s
- RTT = 2 × 2500 / (2 × 10⁸) = 25 μs (worst case ~51.2 μs with repeaters)
- Min frame = 51.2 μs × 10 Mbps = 512 bits = **64 bytes** ✓

### Exponential Backoff

```
After collision i (i = 1 to 10):
  K = random integer from [0, 2^i - 1]
  Wait time = K × slot time

After 10 collisions: Use [0, 1023]
After 16 collisions: Give up, report error
```

**Slot Time**: 51.2 μs (for 10 Mbps Ethernet)

**Example**:
```
Collision 1: K ∈ [0, 1] → Wait 0 or 1 slot
Collision 2: K ∈ [0, 3] → Wait 0, 1, 2, or 3 slots
Collision 3: K ∈ [0, 7] → Wait 0-7 slots
...
```

### CSMA/CD Efficiency

```
η = 1 / (1 + 6.44a)    (approximate)

Where a = Tp / Tt
```

---

## 3.11 CSMA/CA (Wi-Fi - 802.11)

**Carrier Sense Multiple Access with Collision Avoidance**

### Why CA instead of CD?

- **Wireless can't detect collision while transmitting** (near-far problem)
- Listening while transmitting is impractical
- **Hidden terminal problem**

### Hidden Terminal Problem

```
     A ──────── B ──────── C

A cannot hear C (they're hidden from each other)
A and C can both transmit to B simultaneously → Collision at B!
```

### CSMA/CA Mechanism

```
1. Wait for DIFS (DCF Interframe Space)
2. Sense channel
3. If idle for DIFS → Transmit
4. If busy → Random backoff
5. After transmission → Wait for ACK
6. No ACK → Collision assumed → Retransmit
```

### RTS/CTS (Request to Send / Clear to Send)

```
       A                    B                    C
       │                    │                    │
       │─── RTS ───────────→│                    │
       │                    │←── CTS ────────────│
       │←────── CTS ────────│─── CTS ───────────→│
       │                    │                    │
       │─── DATA ──────────→│     (C stays quiet)│
       │                    │                    │
       │←────── ACK ────────│                    │
```

**RTS/CTS solves hidden terminal problem!**

### Interframe Spacing

```
SIFS < PIFS < DIFS

SIFS (Short IFS): 10 μs - ACK, CTS (highest priority)
PIFS (Point IFS): Used by Point Coordinator
DIFS (DCF IFS): 50 μs - Normal data (lowest priority)
```

---

## 3.12 Ethernet (IEEE 802.3)

### Frame Format

```
┌──────────┬───────┬─────────┬─────────┬──────────┬─────────┬───────┐
│ Preamble │  SFD  │  Dest   │ Source  │Type/Len  │  Data   │  FCS  │
│ 7 bytes  │1 byte │ MAC 6B  │ MAC 6B  │ 2 bytes  │46-1500  │4 bytes│
└──────────┴───────┴─────────┴─────────┴──────────┴─────────┴───────┘
     └─────────┘
     10101010...10101011
     Synchronization
```

**Key Points**:
- **Preamble**: 7 bytes of 10101010 (sync)
- **SFD**: 10101011 (Start Frame Delimiter)
- **MAC addresses**: 6 bytes each (48 bits)
- **Type/Length**: Ethernet II uses type, 802.3 uses length
- **Data**: 46-1500 bytes (padded if < 46)
- **FCS**: CRC-32

### MAC Address Format

```
48 bits = 6 bytes = 12 hex digits

AA:BB:CC:DD:EE:FF
└──┬──┘ └────┬────┘
  OUI    NIC specific
(Vendor) (Unique)

Bit 0 of first byte:
  0 = Unicast
  1 = Multicast

Bit 1 of first byte:
  0 = Globally unique (OUI)
  1 = Locally administered
```

**Special Addresses**:
- **FF:FF:FF:FF:FF:FF** = Broadcast
- **01:xx:xx:xx:xx:xx** = Multicast

### Ethernet Evolution

| Standard | Speed | Medium | Max Distance |
|----------|-------|--------|--------------|
| 10BASE-5 | 10 Mbps | Thick coax | 500 m |
| 10BASE-2 | 10 Mbps | Thin coax | 185 m |
| 10BASE-T | 10 Mbps | Cat 3 UTP | 100 m |
| 100BASE-TX | 100 Mbps | Cat 5 UTP | 100 m |
| 1000BASE-T | 1 Gbps | Cat 5e UTP | 100 m |
| 10GBASE-T | 10 Gbps | Cat 6a/7 | 100 m |

### Switching vs Hub

```
HUB (Shared collision domain):         SWITCH (Separate collision domains):
    ┌─────┐                                 ┌─────┐
 ───┤     ├───                           ───┤     ├───
 ───┤ HUB ├───  (All see all traffic)    ───┤ SW  ├───  (Only destination sees)
 ───┤     ├───                           ───┤     ├───
    └─────┘                                 └─────┘
```

### Switch Learning

```
1. Frame arrives on port P
2. Learn: Source MAC → Port P (store in MAC table)
3. Lookup: Destination MAC
   - Found in table → Forward to specific port
   - Not found → Flood to all ports (except source)
```

---

## 3.13 Key Formulas Summary

| Concept | Formula |
|---------|---------|
| **Stop-Wait Efficiency** | η = 1 / (1 + 2a) |
| **Sliding Window Efficiency** | η = min(1, W / (1 + 2a)) |
| **GBN Max Window** | W ≤ 2^m - 1 |
| **SR Max Window** | W ≤ 2^(m-1) |
| **Pure ALOHA Throughput** | S = G × e^(-2G), max = 18.4% |
| **Slotted ALOHA Throughput** | S = G × e^(-G), max = 36.8% |
| **Min Frame Size (CSMA/CD)** | L_min = 2 × Tp × B |
| **CSMA/CD Efficiency** | η ≈ 1 / (1 + 6.44a) |
| **Hamming Redundancy** | 2^r ≥ m + r + 1 |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: Efficiency
**Q**: Tt = 2 ms, Tp = 20 ms, find Stop-Wait efficiency.
**A**: a = 20/2 = 10, η = 1/(1+20) = **4.76%**

### Pattern 2: Window Size
**Q**: 3-bit sequence number, GBN max window?
**A**: 2³ - 1 = **7 frames**

### Pattern 3: ALOHA
**Q**: Pure ALOHA, G = 0.5. Throughput?
**A**: S = 0.5 × e^(-1) = **0.184 or 18.4%**

### Pattern 4: Min Frame
**Q**: 1 Gbps, 4 km cable, v = 2×10⁸. Min frame?
**A**: RTT = 2×4000/(2×10⁸) = 40 μs
       Min = 40 μs × 10⁹ = 40,000 bits = **5000 bytes**

---

## 📝 Quick Revision Checklist

- [ ] Bit stuffing: Insert 0 after five 1s
- [ ] CRC: Append n zeros, divide, remainder is CRC
- [ ] Hamming: Parity at 2^i positions, detect error position
- [ ] Stop-Wait: η = 1/(1+2a)
- [ ] GBN: Sender W = N, Receiver W = 1, retransmit from error
- [ ] SR: Both W = N, retransmit only lost frame
- [ ] Pure ALOHA: 18.4% max, Slotted: 36.8% max
- [ ] CSMA/CD: Min frame = RTT × Bandwidth
- [ ] Ethernet: 64-1518 bytes, CRC-32, 6-byte MACs

---

## 🔥 One-Liner Summary

> "DLL frames bits, detects errors (CRC), controls flow (sliding window); GBN retransmits all from error (W≤2^m-1), SR retransmits only lost (W≤2^(m-1)); ALOHA max 18.4%/36.8%, CSMA listens first; Ethernet min 64 bytes ensures collision detection within RTT."
