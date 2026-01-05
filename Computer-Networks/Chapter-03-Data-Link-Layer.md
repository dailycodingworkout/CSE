# Chapter 3: Data Link Layer

## 🎯 The Atomic Truth
> **"Reliable node-to-node delivery through framing, error control, and access control."**

---

## 3.1 Data Link Layer Functions

### Core Responsibilities

| Function | Description |
|----------|-------------|
| **Framing** | Encapsulate network layer packets into frames |
| **Physical Addressing** | Add MAC addresses for local delivery |
| **Error Control** | Detect and possibly correct transmission errors |
| **Flow Control** | Prevent fast sender from overwhelming slow receiver |
| **Access Control** | Manage shared medium access (MAC sublayer) |

### The "Aha!" Moment 💡
Think of DLL as a **"quality postal service within a city"**:
- **Frames** = Sealed envelopes
- **MAC Address** = Street address
- **Error Detection** = "Fragile" sticker + inspection
- **Flow Control** = "Don't send more until I confirm"
- **Access Control** = Turn-taking at a single mailbox

### Sublayers of DLL

```
┌─────────────────────────────────────┐
│          Network Layer              │
├─────────────────────────────────────┤
│    LLC (Logical Link Control)       │  ← Error & Flow Control
├─────────────────────────────────────┤
│    MAC (Medium Access Control)      │  ← Channel Access
├─────────────────────────────────────┤
│         Physical Layer              │
└─────────────────────────────────────┘
```

---

## 3.2 Framing

### 3.2.1 Why Framing?

Physical layer sends bits → Need to identify boundaries of meaningful data units.

### 3.2.2 Framing Methods

#### 1. Character Count
```
Frame: [5|A|B|C|D][4|E|F|G][6|H|I|J|K|L]...
        ↑count     ↑count   ↑count
```

| Aspect | Details |
|--------|---------|
| Method | First byte = frame length |
| Problem | If count corrupted, all subsequent frames lost |
| Use | Rarely used alone |

#### 2. Character Stuffing (Byte Stuffing)

```
FLAG = 01111110 (0x7E)
ESC  = 01111101 (0x7D)

Original Data: ...FLAG...ESC...
Stuffed Data:  [FLAG]...ESC FLAG...ESC ESC...[FLAG]
               ↑Start                          ↑End
```

| Aspect | Details |
|--------|---------|
| Delimiter | Special FLAG character |
| Escape | Special ESC character before data FLAG/ESC |
| Overhead | Variable (depends on data) |
| Protocol | PPP (Point-to-Point Protocol) |

**Rule**: 
- Data contains FLAG → insert ESC before it
- Data contains ESC → insert ESC before it

#### 3. Bit Stuffing ⭐ (GATE Favorite)

Used by HDLC, Frame Relay

**Flag Pattern**: `01111110` (six 1s between two 0s)

**Stuffing Rule**: After **five consecutive 1s** in data, insert a **0**

```
Original:  011111110010111111011
                 ↑ insert 0    ↑ insert 0
Stuffed:   0111110110010111110011
           ↑FLAG                ↑FLAG is preserved
```

**Destuffing Rule**: After five consecutive 1s, remove the next 0

**Example (GATE Style)**:
> Data: `01111111111110`
> Apply bit stuffing.

**Solution**:
```
Original: 0 1 1 1 1 1 1 1 1 1 1 1 1 0
Count:      1 2 3 4 5   1 2 3 4 5
            ↑insert 0     ↑insert 0
Stuffed:  0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0
                      ↑           ↑
```

Wait, let me redo carefully:
```
Original: 0 1 1 1 1 1 | 1 1 1 1 1 | 1 1 0
          After 5 1s   After next 5 1s
Stuffed:  0 1 1 1 1 1 [0] 1 1 1 1 1 [0] 1 1 0
```

**GATE Trap**: Stuffed 0 is counted in transmission but NOT in original message length.

#### 4. Physical Layer Coding Violations

Use invalid signal patterns as delimiters (works with Manchester encoding).

---

## 3.3 Error Detection and Correction ⭐⭐

### 3.3.1 Types of Errors

| Type | Description | Cause |
|------|-------------|-------|
| **Single-bit** | One bit flipped | Short noise burst |
| **Burst Error** | Multiple consecutive bits affected | Long noise burst |

**Burst Length**: Number of bits from first to last error bit (inclusive)

### 3.3.2 Error Detection Codes

#### Parity Check

**Single Parity (VRC - Vertical Redundancy Check)**

```
Data: 1011001
Even Parity: 1011001[0] (count of 1s = 4, already even)
Odd Parity:  1011001[1] (make count of 1s odd)
```

| Aspect | Details |
|--------|---------|
| Detection | Single-bit errors only |
| Misses | Even number of bit errors |
| Overhead | 1 bit per block |

**Two-Dimensional Parity (LRC + VRC)** ⭐

```
       D1 D2 D3 D4 D5 D6 D7 | VRC
Row 1:  1  0  1  1  0  0  1 | [0]
Row 2:  1  1  0  0  1  1  0 | [0]
Row 3:  0  1  1  0  1  0  1 | [0]
Row 4:  1  1  0  1  0  1  0 | [0]
        ─────────────────────────
LRC:   [1][1][0][0][0][0][0]|[0]
```

| Aspect | Details |
|--------|---------|
| Detection | All single-bit errors |
| Detection | Most 2-bit and 3-bit errors |
| Correction | Can correct single-bit errors |
| Misses | 4-bit errors in rectangle pattern |

#### Checksum

```
Step 1: Divide data into k-bit chunks
Step 2: Add all chunks (one's complement arithmetic)
Step 3: Take one's complement of sum = Checksum
Step 4: Append checksum to data
Step 5: Receiver adds all chunks including checksum
Step 6: Result should be all 1s (or 0 after complement)
```

**Example** (16-bit chunks):
```
Data: 10101001 00111001
      ────────────────
           Sum: (with wraparound)
      Checksum: One's complement of sum
```

| Aspect | Details |
|--------|---------|
| Use | IP, TCP, UDP headers |
| Detection | Reasonable error detection |
| Misses | Reordering errors, some multi-bit |

#### Cyclic Redundancy Check (CRC) ⭐⭐⭐

**The Most Important Error Detection for GATE**

**Concept**: Polynomial division in GF(2) - XOR arithmetic

**Terminology**:
- $D(x)$ = Data polynomial (from data bits)
- $G(x)$ = Generator polynomial (given)
- $R(x)$ = Remainder polynomial (CRC bits)
- $T(x)$ = Transmitted polynomial = $D(x) \cdot x^r + R(x)$

Where $r$ = degree of generator = number of CRC bits

**CRC Calculation Steps** ⭐:

1. Append $r$ zeros to data (where $r$ = degree of $G(x)$)
2. Divide by $G(x)$ using XOR (polynomial division)
3. Remainder = CRC
4. Transmitted data = Original data + CRC

**Verification**: Divide received data by $G(x)$; remainder should be 0.

**Example (GATE Style)**:
> Data: 1001, Generator: 1011 (degree 3). Find CRC.

**Solution**:
```
Step 1: Append 3 zeros → 1001000

Step 2: Divide 1001000 by 1011

        1011 ) 1001000 ( 1110  ← Quotient
               1011
               ────
                010100
                 1011
                 ────
                 01110
                  1011
                  ────
                  01010
                   1011
                   ────
                   0001 ← Remainder = CRC

Step 3: CRC = 001

Step 4: Transmitted = 1001 + 001 = 1001001
```

**Standard Generator Polynomials**:

| Standard | Generator | Degree | Detects |
|----------|-----------|--------|---------|
| CRC-8 | $x^8 + x^2 + x + 1$ | 8 | Up to 8-bit bursts |
| CRC-12 | $x^{12} + x^{11} + x^3 + x^2 + x + 1$ | 12 | Up to 12-bit bursts |
| CRC-16 | $x^{16} + x^{15} + x^2 + 1$ | 16 | Up to 16-bit bursts |
| CRC-32 | $x^{32} + x^{26} + x^{23} + ... + 1$ | 32 | Ethernet, ZIP |

**CRC Detection Capabilities**:

| Error Type | Detection |
|------------|-----------|
| All single-bit | Yes (if $G(x)$ has $x^0$ and $x^1$ terms) |
| All double-bit | Yes (if $G(x)$ is primitive) |
| All odd-bit errors | Yes (if $G(x)$ has $(x+1)$ as factor) |
| All burst ≤ r | Yes |
| Burst > r | Detection probability = $1 - 2^{-r}$ |

**GATE Trap**: CRC can DETECT but NOT CORRECT errors.

### 3.3.3 Error Correction: Hamming Code ⭐⭐

**Concept**: Place check bits at positions that are powers of 2.

**Hamming Distance**: Minimum number of bit positions in which two codewords differ.

$$\text{To detect } d \text{ errors: } d_{min} \geq d + 1$$
$$\text{To correct } t \text{ errors: } d_{min} \geq 2t + 1$$

**Hamming Code (7,4)**:
- 4 data bits → 7 total bits (3 check bits)
- Positions: P1, P2, D1, P4, D2, D3, D4

```
Position:  1   2   3   4   5   6   7
Bit:       P1  P2  D1  P4  D2  D3  D4
                ↓       ↓   ↓   ↓
           Check bits cover specific data bits
```

**Check Bit Coverage**:
- P1 (position 1): covers positions with bit 0 set in binary (1,3,5,7,9,...)
- P2 (position 2): covers positions with bit 1 set (2,3,6,7,10,11,...)
- P4 (position 4): covers positions with bit 2 set (4,5,6,7,12,13,14,15,...)
- P8 (position 8): covers positions with bit 3 set (8-15, 24-31,...)

**Calculation (Even Parity)**:
$$P_1 = D_1 \oplus D_2 \oplus D_4$$
$$P_2 = D_1 \oplus D_3 \oplus D_4$$
$$P_4 = D_2 \oplus D_3 \oplus D_4$$

**Example (GATE Style)**:
> Data bits: 1011 (D1=1, D2=0, D3=1, D4=1). Create Hamming code.

**Solution**:
```
P1 = D1 ⊕ D2 ⊕ D4 = 1 ⊕ 0 ⊕ 1 = 0
P2 = D1 ⊕ D3 ⊕ D4 = 1 ⊕ 1 ⊕ 1 = 1
P4 = D2 ⊕ D3 ⊕ D4 = 0 ⊕ 1 ⊕ 1 = 0

Position:  1   2   3   4   5   6   7
Hamming:   0   1   1   0   0   1   1
          P1  P2  D1  P4  D2  D3  D4
```

**Error Detection/Correction**:
1. Calculate syndrome bits (S1, S2, S4, ...)
2. $S_i = P_i \oplus (\text{XOR of all bits } P_i \text{ covers})$
3. Error position = $S_4 S_2 S_1$ (binary to decimal)
4. If syndrome ≠ 0, flip bit at error position

**Formula for Hamming Code**:
$$2^r \geq m + r + 1$$

Where:
- $m$ = number of data bits
- $r$ = number of check bits
- Total bits = $m + r$

| Data bits (m) | Check bits (r) | Total | Code |
|---------------|----------------|-------|------|
| 4 | 3 | 7 | (7,4) |
| 8 | 4 | 12 | (12,8) |
| 11 | 4 | 15 | (15,11) |
| 26 | 5 | 31 | (31,26) |

---

## 3.4 Flow Control ⭐⭐

### 3.4.1 Why Flow Control?

Prevent sender from overwhelming receiver with data faster than it can process.

### 3.4.2 Stop-and-Wait Protocol

```
Sender                              Receiver
  │                                    │
  │──────── Frame 0 ──────────────────►│
  │                                    │
  │◄────────── ACK ────────────────────│
  │                                    │
  │──────── Frame 1 ──────────────────►│
  │                                    │
  │◄────────── ACK ────────────────────│
```

**Efficiency Formula** ⭐:

$$\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a}$$

Where: $a = \frac{T_p}{T_t}$

**Throughput**:
$$\text{Throughput} = \eta \times \text{Bandwidth}$$

| Aspect | Details |
|--------|---------|
| Window Size | 1 frame |
| Sequence Numbers | 2 (0 and 1) |
| Good for | High $T_t$, low $T_p$ (short distance, slow links) |
| Bad for | Low $T_t$, high $T_p$ (long distance, fast links) |

**Example (GATE Style)**:
> Link: 1 Mbps, 1000 km, frame = 1000 bits, propagation = $2 \times 10^8$ m/s.
> Find efficiency of Stop-and-Wait.

**Solution**:
$$T_t = \frac{1000}{10^6} = 1 \text{ ms}$$
$$T_p = \frac{1000 \times 10^3}{2 \times 10^8} = 5 \text{ ms}$$
$$a = \frac{5}{1} = 5$$
$$\eta = \frac{1}{1 + 2(5)} = \frac{1}{11} = 9.09\%$$

### 3.4.3 Sliding Window Protocols ⭐⭐⭐

**Key Insight**: Send multiple frames before waiting for ACK.

**Window**: Set of sequence numbers sender can use.

```
Sender Window (size = 4):
[0][1][2][3] 4  5  6  7  0  1  2  3...
 ↑sent,ACKed ↑     ↑can send
             └─window─┘

As ACKs received, window "slides" forward.
```

**Efficiency with Window Size W** ⭐:

If $W \geq 1 + 2a$:
$$\eta = 1 \text{ (100% utilization)}$$

If $W < 1 + 2a$:
$$\eta = \frac{W}{1 + 2a}$$

**Minimum Window Size for 100% Efficiency**:
$$W_{min} = 1 + 2a = 1 + \frac{2 \times T_p}{T_t} = 1 + \frac{2 \times BDP}{L}$$

Where BDP = Bandwidth-Delay Product = $B \times T_p$

**Sequence Number Range**:

| Protocol | Min Sequence Numbers | Window Size |
|----------|---------------------|-------------|
| Stop-and-Wait | 2 | 1 |
| Go-Back-N | $W + 1$ | $W \leq 2^n - 1$ |
| Selective Repeat | $2W$ | $W \leq 2^{n-1}$ |

Where $n$ = number of bits for sequence number.

### 3.4.4 Go-Back-N (GBN) ⭐⭐

**Concept**: On error, retransmit from the errored frame onwards.

```
Sender:    [0][1][2][3][4][5][6][7]...
                  ↑error detected
Retransmit: [2][3][4][5][6][7]...
            All from error point
```

**Rules**:
- Sender window: Up to $2^n - 1$ (where n = bits for seq num)
- Receiver window: 1 (only accepts in-order)
- ACK is cumulative (ACK n means all up to n received)
- Timer for oldest unACKed frame

| Aspect | Details |
|--------|---------|
| Sender Window | $W_s \leq 2^n - 1$ |
| Receiver Window | $W_r = 1$ |
| On Error | Retransmit all from error |
| ACK | Cumulative |
| Overhead | High if error rate high |

**Why $W \leq 2^n - 1$?**
If W = $2^n$, receiver can't distinguish new frames from retransmissions.

**Example**: n = 3 bits → 8 sequence numbers (0-7), max window = 7

### 3.4.5 Selective Repeat (SR) ⭐⭐

**Concept**: Only retransmit the errored frame, not all subsequent.

```
Sender:    [0][1][2][3][4][5][6][7]...
                  ↑error
Retransmit: Only [2]
Receiver buffers: [3][4][5]... while waiting for [2]
```

**Rules**:
- Sender window: Up to $2^{n-1}$
- Receiver window: Same as sender window
- ACK is individual (each frame ACKed separately)
- Receiver buffers out-of-order frames

| Aspect | Details |
|--------|---------|
| Sender Window | $W_s \leq 2^{n-1}$ |
| Receiver Window | $W_r = W_s$ |
| On Error | Retransmit only errored frame |
| ACK | Individual |
| Buffer | Receiver needs buffer |

**Why $W \leq 2^{n-1}$?**

Scenario: Window = 4, Seq nums = 0,1,2,3 (n=2)
- Sender sends [0,1,2,3]
- All ACKs lost
- Sender retransmits [0,1,2,3]
- Receiver expects [0,1,2,3] as NEW frames (next cycle)
- **Ambiguity!**

Solution: $W \leq 2^{n-1}$ ensures no overlap between old and new.

### Protocol Comparison ⭐

| Aspect | Stop-Wait | Go-Back-N | Selective Repeat |
|--------|-----------|-----------|------------------|
| Sender Window | 1 | $\leq 2^n - 1$ | $\leq 2^{n-1}$ |
| Receiver Window | 1 | 1 | $\leq 2^{n-1}$ |
| Retransmission | 1 frame | All from error | Only errored |
| Receiver Buffer | 1 | 1 | Multiple |
| Complexity | Simple | Moderate | Complex |
| Efficiency (no error) | Low | High | High |
| Efficiency (high error) | Low | Moderate | High |
| ACK Type | Individual | Cumulative | Individual |

### Efficiency Formulas Summary ⭐

**Without errors:**
$$\eta = \min\left(\frac{W}{1+2a}, 1\right)$$

**With frame error probability P:**

Stop-and-Wait:
$$\eta = \frac{(1-P)}{(1+2a)}$$

Go-Back-N:
$$\eta = \frac{(1-P)}{(1+2aP)} \quad \text{if } W \geq 1+2a$$

Selective Repeat:
$$\eta = (1-P) \quad \text{if } W \geq 1+2a$$

---

## 3.5 MAC Sublayer - Medium Access Control ⭐⭐

### 3.5.1 The Channel Allocation Problem

Multiple devices share a single broadcast channel → Need coordination.

### 3.5.2 Random Access Protocols

#### ALOHA

**Pure ALOHA**:
- Transmit whenever data available
- If collision → wait random time → retransmit

**Vulnerability Period**: $2 \times T_t$ (frame from another station can collide)

$$\text{Throughput} = G \cdot e^{-2G}$$

Where G = offered load (average frames per frame time)

$$S_{max} = \frac{1}{2e} \approx 0.184 = 18.4\%$$ at $G = 0.5$

**Slotted ALOHA**:
- Time divided into slots = frame transmission time
- Transmit only at slot beginning

**Vulnerability Period**: $T_t$ (reduced by half)

$$\text{Throughput} = G \cdot e^{-G}$$

$$S_{max} = \frac{1}{e} \approx 0.368 = 36.8\%$$ at $G = 1$

**Comparison**:

| Aspect | Pure ALOHA | Slotted ALOHA |
|--------|------------|---------------|
| Efficiency | 18.4% | 36.8% |
| Synchronization | Not required | Required |
| Vulnerability | 2Tt | Tt |

#### CSMA (Carrier Sense Multiple Access)

**Concept**: Listen before transmit.

**Types**:

| Type | Action when busy | Action when idle | Efficiency |
|------|------------------|------------------|------------|
| **1-Persistent** | Wait, transmit immediately when free | Transmit immediately | Highest collision |
| **Non-persistent** | Wait random time, sense again | Transmit | Lower collision |
| **P-persistent** | Wait for slot, try again | Transmit with probability p | Balanced |

**Vulnerability Time**: Still exists due to propagation delay.

$$\text{Vulnerability} = T_p$$

**CSMA Efficiency** (approximate):
$$\eta \approx \frac{1}{1 + a} = \frac{1}{1 + T_p/T_t}$$

#### CSMA/CD (Collision Detection) ⭐⭐

**Used in**: Ethernet (wired)

**Concept**: Listen while transmitting, detect collision, abort immediately.

```
Station A starts transmitting
        │
        ▼
    ────●════════════════════●────
        A                    B
        ◄────── distance ───►

If B starts before A's signal reaches B:
    Collision occurs
    Both detect collision (signal jamming)
    Both abort and wait random time
```

**Minimum Frame Size Condition** ⭐⭐:

For collision to be detected, frame must still be transmitting when collision signal returns.

$$T_t \geq 2 \times T_p$$

$$\frac{L_{min}}{B} \geq \frac{2D}{V}$$

$$L_{min} = \frac{2 \times B \times D}{V} = 2 \times BDP$$

**For Ethernet**:
- Max distance: 2500 m (with repeaters)
- Speed: 10 Mbps
- Propagation: $2 \times 10^8$ m/s
- Min frame: 64 bytes (512 bits) including all headers

**Binary Exponential Backoff**:
After collision $k$ (where $k \leq 10$):
- Wait random number of slot times from $[0, 2^k - 1]$
- Slot time = RTT = $2 \times T_p$

After collision 10-15: range stays $[0, 1023]$
After collision 16: give up, report error

#### CSMA/CA (Collision Avoidance) ⭐

**Used in**: WiFi (wireless) - IEEE 802.11

**Why not CD?**
- Wireless: Can't detect collision while transmitting
- Hidden terminal problem
- Exposed terminal problem

**CSMA/CA Methods**:

**1. IFS (Interframe Space)**:
- Wait after channel becomes idle
- Priority: SIFS < PIFS < DIFS
- SIFS: Short IFS (ACK, CTS)
- DIFS: Distributed IFS (data frames)

**2. Contention Window**:
- Random backoff before transmission
- Binary exponential backoff on collision

**3. RTS/CTS (Request to Send / Clear to Send)**:
```
A ──RTS──► AP ──CTS──► All
A ──DATA──► AP
AP ──ACK──► A
```

Solves hidden terminal problem:
- RTS reserves channel
- CTS heard by hidden terminals → they wait

### 3.5.3 Controlled Access Protocols

#### Polling
- Central controller asks each station in turn
- Overhead: poll and acknowledgment messages

#### Token Passing
- Token circulates around ring/bus
- Only token holder can transmit

**Token Ring Timing** ⭐:

$$\text{Ring Latency} = T_p + N \times T_{station}$$

Where:
- $T_p$ = Propagation delay around ring
- $N$ = Number of stations
- $T_{station}$ = Processing delay per station (typically 1 bit time)

**Token Holding Time (THT)**: Max time station can hold token

**Efficiency**:
$$\eta = \frac{T_t}{T_t + T_{ring}}$$

### 3.5.4 Channelization Protocols

| Protocol | Domain | Description |
|----------|--------|-------------|
| FDMA | Frequency | Each station gets frequency band |
| TDMA | Time | Each station gets time slot |
| CDMA | Code | Each station gets unique code |

---

## 3.6 Ethernet (IEEE 802.3) ⭐⭐

### 3.6.1 Ethernet Frame Format

```
┌─────────┬─────────┬───────┬───────┬──────┬─────────┬─────┐
│Preamble │   SFD   │ Dest  │Source │Type/ │  Data   │ FCS │
│ 7 bytes │ 1 byte  │ MAC   │ MAC   │Length│46-1500  │4 byte│
│         │         │6 bytes│6 bytes│2 byte│ bytes   │     │
└─────────┴─────────┴───────┴───────┴──────┴─────────┴─────┘
```

| Field | Size | Purpose |
|-------|------|---------|
| Preamble | 7 bytes | Synchronization (101010...) |
| SFD | 1 byte | Start Frame Delimiter (10101011) |
| Dest MAC | 6 bytes | Destination address |
| Source MAC | 6 bytes | Source address |
| Type/Length | 2 bytes | Protocol type (>1536) or length (≤1500) |
| Data | 46-1500 bytes | Payload (padded if < 46) |
| FCS | 4 bytes | CRC-32 for error detection |

**Total Frame Size**: 64-1518 bytes (not counting preamble/SFD)
**Minimum Data**: 46 bytes (padded if less)
**Maximum Data**: 1500 bytes (MTU)

### 3.6.2 MAC Address

```
XX:XX:XX:XX:XX:XX  (6 bytes = 48 bits)
│         │
└─OUI─────┴─Device Identifier
(Vendor)
```

| Bit | Meaning |
|-----|---------|
| LSB of first byte = 0 | Unicast |
| LSB of first byte = 1 | Multicast |
| All 1s | Broadcast (FF:FF:FF:FF:FF:FF) |
| Second LSB of first byte | Locally/Globally administered |

### 3.6.3 Ethernet Standards

| Standard | Speed | Medium | Distance |
|----------|-------|--------|----------|
| 10BASE-T | 10 Mbps | Cat 3 UTP | 100 m |
| 10BASE-5 | 10 Mbps | Thick coax | 500 m |
| 10BASE-2 | 10 Mbps | Thin coax | 185 m |
| 100BASE-TX | 100 Mbps | Cat 5 UTP | 100 m |
| 100BASE-FX | 100 Mbps | Fiber | 2 km |
| 1000BASE-T | 1 Gbps | Cat 5e/6 | 100 m |
| 1000BASE-SX | 1 Gbps | MMF | 550 m |
| 1000BASE-LX | 1 Gbps | SMF | 5 km |
| 10GBASE-T | 10 Gbps | Cat 6a | 100 m |

**Naming Convention**: Speed (Mbps) + Signaling + Segment type

---

## 3.7 PPP (Point-to-Point Protocol)

### Frame Format

```
┌──────┬─────────┬─────────┬──────────┬─────────┬──────┬──────┐
│ Flag │ Address │ Control │ Protocol │ Payload │ FCS  │ Flag │
│1 byte│ 1 byte  │ 1 byte  │ 2 bytes  │Variable │2 byte│1 byte│
│0x7E  │  0xFF   │  0x03   │          │≤1500 B  │      │0x7E  │
└──────┴─────────┴─────────┴──────────┴─────────┴──────┴──────┘
```

**Key Features**:
- Point-to-point links (dial-up, DSL)
- Byte stuffing (0x7E → 0x7D 0x5E)
- No sequence numbers (no sliding window)
- Uses LCP for link setup, NCP for network protocols

---

## 3.8 Switching at Data Link Layer

### 3.8.1 Learning Bridge/Switch

**MAC Address Table**: Maps MAC address to port

**Learning Process**:
1. Frame arrives on port
2. Learn: Source MAC → port
3. Forward based on destination MAC

**Forwarding Logic**:
- Destination in table → Forward to that port
- Destination NOT in table → Flood to all ports (except source)
- Destination is source port → Drop (same segment)

### 3.8.2 Spanning Tree Protocol (STP) ⭐

**Problem**: Loops in switched network cause broadcast storms.

**Solution**: Build loop-free logical topology.

**Algorithm**:
1. Elect Root Bridge (lowest Bridge ID)
2. Each non-root selects Root Port (best path to root)
3. Each segment selects Designated Port
4. Block other ports

**Bridge ID**: Priority (2 bytes) + MAC (6 bytes)

**Path Cost**: Lower = better (based on bandwidth)

| Speed | Cost (Original) | Cost (Revised) |
|-------|-----------------|----------------|
| 10 Mbps | 100 | 100 |
| 100 Mbps | 10 | 19 |
| 1 Gbps | 1 | 4 |
| 10 Gbps | 1 | 2 |

---

## 3.9 VLAN (Virtual LAN)

**Concept**: Logical grouping of devices regardless of physical location.

**Benefits**:
- Reduced broadcast domain
- Improved security
- Flexible organization

**VLAN Tagging (802.1Q)**:
```
┌───────┬───────┬──────┬───────┬─────────┬─────┐
│Dest MA│Src MAC│802.1Q│Type/  │  Data   │ FCS │
│       │       │ Tag  │Length │         │     │
└───────┴───────┴──────┴───────┴─────────┴─────┘
                  │
                  ▼
            4 bytes: TPID(2) + TCI(2)
            TCI = Priority(3) + DEI(1) + VLAN ID(12)
```

**VLAN ID Range**: 0-4095 (12 bits)
- 0, 4095: Reserved
- 1: Default VLAN
- 2-1001: Normal range
- 1002-4094: Extended range

---

## 3.10 Edge Cases & GATE Traps

### Trap 1: Go-Back-N vs Selective Repeat Window Size
- GBN: $W \leq 2^n - 1$ (NOT $2^n$)
- SR: $W \leq 2^{n-1}$

### Trap 2: CRC Remainder
- Remainder after division = CRC
- NOT the quotient!

### Trap 3: Bit Stuffing Count
- After 5 ones, insert 0
- Don't count the inserted 0 when looking for next 5

### Trap 4: Minimum Frame Size
- Includes ALL headers (not just data)
- For CSMA/CD: $L_{min} = 2 \times BDP$

### Trap 5: ALOHA Efficiency
- Pure: 18.4% (max at G = 0.5)
- Slotted: 36.8% (max at G = 1)
- NOT 50% or 100%!

### Trap 6: Efficiency Formula
- Include ACK time if asked
- $\eta = \frac{T_t}{T_t + 2T_p + T_{ACK}}$ for complete cycle

---

## 📝 Chapter Summary

| Concept | Key Formula/Point |
|---------|-------------------|
| Bit Stuffing | Insert 0 after five 1s |
| CRC | Append r zeros, divide by G(x), remainder = CRC |
| Hamming | $2^r \geq m + r + 1$; detect d: $d_{min} \geq d+1$; correct t: $d_{min} \geq 2t+1$ |
| Stop-Wait η | $\frac{1}{1+2a}$ |
| Sliding Window η | $\frac{W}{1+2a}$ (if $W < 1+2a$) |
| GBN Window | $\leq 2^n - 1$ |
| SR Window | $\leq 2^{n-1}$ |
| Pure ALOHA | 18.4% max |
| Slotted ALOHA | 36.8% max |
| CSMA/CD Min Frame | $2 \times BDP$ |
| Ethernet Frame | 64-1518 bytes |

---

## 🧪 Practice Problems

### Problem 1 (GATE Style)
For a 3-bit sequence number, what is the maximum window size for Go-Back-N and Selective Repeat?

<details>
<summary>Solution</summary>

GBN: $W_{max} = 2^3 - 1 = 7$
SR: $W_{max} = 2^{3-1} = 4$

</details>

### Problem 2 (GATE NAT)
Data = 110101, Generator = 1001. Find CRC.

<details>
<summary>Solution</summary>

Degree of generator = 3, so append 3 zeros.
Divide 110101000 by 1001:

```
        1001 ) 110101000
               1001
               ─────
                1001
                1001
                ─────
                 0001000
                    1001
                    ─────
                     0010 ← Remainder
```

CRC = 010

</details>

### Problem 3 (GATE Style)
A 10 Mbps link has propagation delay of 20 ms. Frame size is 1000 bits. Find minimum window size for 100% efficiency.

<details>
<summary>Solution</summary>

$T_t = \frac{1000}{10 \times 10^6} = 0.1 \text{ ms}$
$a = \frac{T_p}{T_t} = \frac{20}{0.1} = 200$
$W_{min} = 1 + 2a = 1 + 400 = 401$ frames

</details>

---

**Previous Chapter**: [← Chapter 2: Physical Layer](./Chapter-02-Physical-Layer.md)

**Next Chapter**: [Chapter 4: Network Layer →](./Chapter-04-Network-Layer.md)

---

*Happy Learning!*
