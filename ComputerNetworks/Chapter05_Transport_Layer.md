# Chapter 5: Transport Layer

## 🎯 GATE/ESE Weightage: 8-12 marks (Heavy on TCP)

---

## 5.1 Transport Layer Functions

The Transport Layer provides **end-to-end** (process-to-process) communication between applications.

**Core Functions**:
1. **Process-to-process delivery** (using ports)
2. **Segmentation and reassembly**
3. **Connection control** (TCP)
4. **Flow control** (TCP)
5. **Error control** (TCP)
6. **Congestion control** (TCP)

### Network Layer vs Transport Layer

| Layer | Addressing | Delivery | Reliability |
|-------|------------|----------|-------------|
| Network | IP (host-to-host) | Best effort | No |
| Transport | Port (process-to-process) | Depends | TCP: Yes, UDP: No |

---

## 5.2 Port Numbers (🎯 MEMORIZE)

### Port Ranges

| Range | Name | Usage |
|-------|------|-------|
| 0-1023 | Well-known | System services (root) |
| 1024-49151 | Registered | User applications |
| 49152-65535 | Dynamic/Private | Client ephemeral ports |

### Well-Known Ports (🎯 GATE FAVORITES)

| Port | Protocol | Service |
|------|----------|---------|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67 | UDP | DHCP Server |
| 68 | UDP | DHCP Client |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 520 | UDP | RIP |

### Socket = IP + Port

```
Socket: 192.168.1.5:80

Connection identified by 5-tuple:
(Source IP, Source Port, Dest IP, Dest Port, Protocol)
```

---

## 5.3 UDP (User Datagram Protocol)

### Characteristics

- **Connectionless**: No handshake
- **Unreliable**: No ACK, no retransmission
- **Unordered**: Packets may arrive out of order
- **Fast**: Minimal overhead
- **Message-oriented**: Preserves message boundaries

### UDP Header (8 bytes)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Length             |           Checksum            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Field | Size | Description |
|-------|------|-------------|
| Source Port | 16 bits | Sender's port |
| Dest Port | 16 bits | Receiver's port |
| Length | 16 bits | Header + Data (min 8) |
| Checksum | 16 bits | Optional in IPv4, mandatory in IPv6 |

### UDP Use Cases

- **DNS** (quick queries)
- **DHCP** (configuration)
- **SNMP** (monitoring)
- **VoIP/Video** (real-time, tolerates loss)
- **Online gaming**
- **TFTP**

---

## 5.4 TCP (Transmission Control Protocol) (🎯 CRITICAL)

### Characteristics

- **Connection-oriented**: 3-way handshake
- **Reliable**: ACKs, retransmission
- **Ordered**: Sequence numbers
- **Flow control**: Sliding window
- **Congestion control**: AIMD, slow start
- **Full-duplex**: Bidirectional communication
- **Stream-oriented**: No message boundaries

### TCP Header (20-60 bytes)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |       |C|E|U|A|P|R|S|F|                               |
| Offset| Rsrvd |W|C|R|C|S|S|Y|I|            Window             |
|       |       |R|E|G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if data offset > 5)               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### TCP Header Fields

| Field | Bits | Description |
|-------|------|-------------|
| Source Port | 16 | Sender's port |
| Dest Port | 16 | Receiver's port |
| Sequence Number | 32 | Byte number of first data byte |
| ACK Number | 32 | Next expected byte (cumulative) |
| Data Offset | 4 | Header length in 32-bit words |
| Reserved | 4 | Set to zero |
| **Flags** | 8 | Control bits (below) |
| Window | 16 | Receiver's buffer size (flow control) |
| Checksum | 16 | Header + Data + Pseudo-header |
| Urgent Pointer | 16 | Used with URG flag |

### TCP Flags (🎯 MUST MEMORIZE)

| Flag | Name | Purpose |
|------|------|---------|
| **SYN** | Synchronize | Initiate connection |
| **ACK** | Acknowledge | Acknowledgment valid |
| **FIN** | Finish | Terminate connection |
| **RST** | Reset | Abort connection |
| **PSH** | Push | Don't buffer, deliver immediately |
| **URG** | Urgent | Urgent pointer valid |
| CWR | Congestion Window Reduced | ECN response |
| ECE | ECN-Echo | Congestion notification |

---

## 5.5 TCP Connection Management (🎯 VERY IMPORTANT)

### Three-Way Handshake (Connection Establishment)

```
       Client                              Server
          │                                   │
          │ ──────── SYN, Seq=x ────────────→ │
          │                                   │
          │ ←─── SYN+ACK, Seq=y, Ack=x+1 ──── │
          │                                   │
          │ ──────── ACK, Ack=y+1 ──────────→ │
          │                                   │
       (ESTABLISHED)                    (ESTABLISHED)
```

**Why 3-way?**
- Synchronize sequence numbers
- Verify both directions work
- Prevent old duplicates from causing issues

### Connection Termination (4-way)

```
       Client                              Server
          │                                   │
          │ ──────── FIN, Seq=x ────────────→ │
          │                                   │
          │ ←─────── ACK, Ack=x+1 ─────────── │
          │                                   │
          │ ←─────── FIN, Seq=y ────────────  │
          │                                   │
          │ ──────── ACK, Ack=y+1 ──────────→ │
          │                                   │
       (CLOSED)                           (CLOSED)
```

**Why 4 segments?**
- Each direction closed independently (half-close)
- Server may have data to send after client's FIN

### TCP State Diagram (🎯 IMPORTANT)

```
                              ┌─────────────────┐
                              │     CLOSED      │
                              └────────┬────────┘
                                       │
              Active open              │              Passive open
              Send SYN                 │              (Listen)
                    ┌──────────────────┼──────────────────┐
                    ▼                  ▼                  ▼
             ┌──────────┐        ┌──────────┐      ┌──────────┐
             │ SYN_SENT │        │  LISTEN  │      │          │
             └────┬─────┘        └────┬─────┘      └──────────┘
                  │                   │
         Rcv SYN+ACK                  │ Rcv SYN
         Send ACK                     │ Send SYN+ACK
                  │                   │
                  ▼                   ▼
             ┌──────────────────────────────┐
             │        ESTABLISHED           │
             └──────────────────────────────┘
                           │
              Close        │         Rcv FIN
              Send FIN     │         Send ACK
                    ┌──────┴──────┐
                    ▼             ▼
             ┌──────────┐   ┌──────────┐
             │ FIN_WAIT1│   │CLOSE_WAIT│
             └────┬─────┘   └────┬─────┘
                  │              │
         Rcv ACK  │              │ Close
                  ▼              │ Send FIN
             ┌──────────┐        ▼
             │ FIN_WAIT2│   ┌──────────┐
             └────┬─────┘   │ LAST_ACK │
                  │         └────┬─────┘
         Rcv FIN  │              │ Rcv ACK
         Send ACK │              │
                  ▼              ▼
             ┌──────────┐   ┌──────────┐
             │TIME_WAIT │   │  CLOSED  │
             └────┬─────┘   └──────────┘
                  │
         2MSL timeout
                  ▼
             ┌──────────┐
             │  CLOSED  │
             └──────────┘
```

### TIME_WAIT State

**Duration**: 2 × MSL (Maximum Segment Lifetime) ≈ 2 × 30s = 60s

**Why TIME_WAIT?**
1. Ensure ACK reaches other end (retransmit if FIN repeated)
2. Allow old duplicates to expire before reusing port

---

## 5.6 TCP Flow Control (🎯 IMPORTANT)

### Sliding Window

```
Sender's view:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
 └─sent─┘ └─────────window──────────────┘
   ACKed     sent, unACKed    can send

Receiver advertises: Window = 5000 bytes
Sender can have 5000 unacknowledged bytes in flight
```

### Receiver Window (rwnd)

- Advertised in TCP header's Window field
- Indicates free buffer space
- Sender cannot exceed rwnd

```
Effective Window = min(cwnd, rwnd)

Where:
cwnd = Congestion window (sender's estimate)
rwnd = Receiver window (advertised by receiver)
```

### Silly Window Syndrome

**Problem**: Small segments waste bandwidth

```
Receiver has 1 byte free → Advertises window = 1
Sender sends 1 byte + 40 bytes headers = INEFFICIENT!
```

**Solutions**:
- **Nagle's Algorithm** (Sender): Buffer small data, send when ACK received or buffer full
- **Clark's Solution** (Receiver): Don't advertise tiny windows

---

## 5.7 TCP Congestion Control (🎯 MOST ASKED)

### Why Congestion Control?

- Prevent network overload
- Fair share of bandwidth
- Avoid congestion collapse

### Key Variables

| Variable | Description |
|----------|-------------|
| **cwnd** | Congestion window (sender-controlled) |
| **rwnd** | Receiver window (receiver-advertised) |
| **ssthresh** | Slow start threshold |
| **MSS** | Maximum Segment Size |

### Congestion Control Phases

```
┌─────────────────────────────────────────────────────────────────┐
│                    TCP CONGESTION CONTROL                       │
│                                                                 │
│  SLOW START                    CONGESTION AVOIDANCE            │
│  (Exponential growth)          (Linear growth - AIMD)          │
│                                                                 │
│  cwnd < ssthresh               cwnd ≥ ssthresh                 │
│  cwnd = cwnd + MSS             cwnd = cwnd + MSS²/cwnd         │
│  (per ACK)                     (approximately +1 MSS per RTT)  │
│                                                                 │
│  Doubles every RTT             Increases by 1 MSS every RTT    │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 1: Slow Start

```
Initial: cwnd = 1 MSS, ssthresh = 65535 (or large)

cwnd
 │
 │                      ○ ssthresh
 │                    ○
 │                  ○
 │               ○
 │            ○
 │         ○
 │      ○
 │   ○
 │ ○
 └─○───────────────────────→ RTT
   1  2  4  8  16  32

Exponential growth: 1 → 2 → 4 → 8 → 16...
```

**Slow Start Algorithm**:
```
For each ACK received:
    cwnd = cwnd + 1 MSS

Effect: cwnd doubles every RTT
```

### Phase 2: Congestion Avoidance (AIMD)

```
When cwnd ≥ ssthresh:

Additive Increase:
    For each RTT: cwnd = cwnd + 1 MSS
    
    (Actually: cwnd = cwnd + MSS × MSS / cwnd per ACK)

cwnd
 │            ╱╲
 │           ╱  ╲
 │          ╱    ╲ Multiplicative
 │         ╱      ╲ Decrease
 │        ╱        ╲
 │       ╱          ╲
 │      ╱ Additive   ╲
 │     ╱  Increase    ╲
 │    ╱                ╲
 └───────────────────────────→ Time
```

### Detecting Congestion

| Event | Indicates | Action |
|-------|-----------|--------|
| **3 Duplicate ACKs** | Mild congestion | Fast Retransmit + Fast Recovery |
| **Timeout** | Severe congestion | Slow Start from cwnd = 1 |

### Fast Retransmit

```
Sender receives: ACK 1000, ACK 1000, ACK 1000, ACK 1000
                         (3 duplicates)
                         
Interpretation: Segment 1000 lost but later ones arrived

Action: Retransmit segment 1000 immediately
        (Don't wait for timeout)
```

### Fast Recovery (TCP Reno)

```
On 3 duplicate ACKs:
    ssthresh = cwnd / 2
    cwnd = ssthresh + 3 MSS
    Retransmit lost segment
    For each additional duplicate ACK: cwnd += 1 MSS
    When new ACK arrives: cwnd = ssthresh (exit fast recovery)
```

### TCP Tahoe vs Reno vs New Reno

| Event | Tahoe | Reno | New Reno |
|-------|-------|------|----------|
| Timeout | ssthresh = cwnd/2, cwnd = 1, Slow Start | Same as Tahoe | Same |
| 3 Dup ACKs | ssthresh = cwnd/2, cwnd = 1, Slow Start | ssthresh = cwnd/2, cwnd = ssthresh, Fast Recovery | Same + Partial ACK handling |

### Congestion Control Graph (🎯 GATE FAVORITE)

```
cwnd (MSS)
  ^
64│                          ╱╲
  │                        ╱    ╲
32│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╱─ ─ ─ ╲─ ─ ssthresh
  │                    ╱         ╲
16│              ○○○○○          ╱╲╲
  │            ○              ╱    ╲
 8│─ ─ ─ ─ ○ ─ ─ ─ ─ ─ ─ ─ ─╱─ ─ ─ ╲─ new ssthresh
  │       ○                       ╱╲
 4│     ○                       ╱
  │    ○   Slow    Congestion  ╱  
 2│   ○   Start    Avoidance  ╱
 1│  ○                       ╱
  └──●─────────────────────────────→ RTT
      ↑        ↑    ↑
    Start   ssthresh  Timeout/3 dup ACK
             reached
```

### 🎯 GATE Calculation Pattern

**Q**: Initial cwnd = 1, ssthresh = 8, find cwnd after 10 RTTs.

**Solution**:
```
RTT 1: cwnd = 1 (Slow Start begins)
RTT 2: cwnd = 2 (doubled)
RTT 3: cwnd = 4
RTT 4: cwnd = 8 (= ssthresh, switch to CA)
RTT 5: cwnd = 9 (Congestion Avoidance: +1)
RTT 6: cwnd = 10
RTT 7: cwnd = 11
RTT 8: cwnd = 12
RTT 9: cwnd = 13
RTT 10: cwnd = 14

Answer: cwnd = 14 MSS
```

**If timeout at RTT 7**:
```
RTT 7: Timeout! ssthresh = 11/2 = 5, cwnd = 1
RTT 8: cwnd = 2 (Slow Start)
RTT 9: cwnd = 4
RTT 10: cwnd = 5 (= ssthresh, switch to CA)
...
```

---

## 5.8 TCP Timer Management

### Types of Timers

| Timer | Purpose | Typical Value |
|-------|---------|---------------|
| **Retransmission** | Detect lost segments | RTO (calculated) |
| **Persistence** | Probe zero window | 60 seconds |
| **Keepalive** | Check dead connections | 2 hours |
| **TIME_WAIT** | Ensure connection closure | 2 × MSL |

### Retransmission Timeout (RTO)

```
RTO = Estimated RTT + 4 × Deviation

Where:
SRTT (Smoothed RTT) = (1-α) × SRTT + α × SampleRTT
DevRTT = (1-β) × DevRTT + β × |SampleRTT - SRTT|

Typical: α = 1/8, β = 1/4
```

### Karn's Algorithm

**Problem**: Can't sample RTT for retransmitted segments (ambiguity)

**Solution**: Don't update RTT estimate for retransmissions

### Exponential Backoff

```
After each timeout:
    RTO = 2 × RTO (doubled)
    
Until successful transmission, then recalculate normally
```

---

## 5.9 TCP vs UDP Comparison (🎯 MEMORIZE)

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable (ACK, retransmit) | Unreliable |
| Ordering | Ordered | Unordered |
| Flow Control | Yes (sliding window) | No |
| Congestion Control | Yes (AIMD) | No |
| Header Size | 20-60 bytes | 8 bytes |
| Speed | Slower | Faster |
| Message Boundary | Stream (no boundaries) | Preserved |
| Overhead | High | Low |
| Use Cases | HTTP, FTP, SMTP, SSH | DNS, DHCP, VoIP, Gaming |

---

## 5.10 Advanced TCP Concepts

### TCP Selective Acknowledgment (SACK)

```
Standard TCP: Cumulative ACK only
    "I received bytes 1-1000"

SACK: Report gaps
    "I received 1-1000, also 2001-3000"
    
Sender knows: 1001-2000 is missing
              Don't retransmit 2001-3000
```

### TCP Window Scaling

```
Default window: 16-bit field = max 65535 bytes
Problem: Not enough for high BDP (Bandwidth × Delay)

Window Scaling Option:
    Window = Window field × 2^(scale factor)
    
Scale factor negotiated in SYN (max 14)
Max window = 65535 × 2^14 = 1 GB
```

### TCP Timestamp

- Accurate RTT measurement
- Protection against sequence number wraparound (PAWS)

### Explicit Congestion Notification (ECN)

- Router marks packets instead of dropping
- Uses IP header and TCP flags (ECE, CWR)
- Reduces retransmissions

---

## 5.11 Throughput Calculations (🎯 IMPORTANT)

### Maximum TCP Throughput

```
Throughput = Window Size / RTT

Max throughput = rwnd / RTT (limited by receiver)
OR
Max throughput = cwnd / RTT (limited by congestion)
```

### Bandwidth-Delay Product (BDP)

```
BDP = Bandwidth × RTT

This is the amount of data "in flight"
Window should be ≥ BDP for full utilization
```

**Example**:
```
B = 100 Mbps, RTT = 100 ms
BDP = 100 × 10^6 × 0.1 = 10 × 10^6 bits = 1.25 MB

Need window ≥ 1.25 MB for full utilization
```

### Efficiency with Packet Loss

```
Throughput ≈ (MSS / RTT) × (1 / √p)

Where p = packet loss probability

For small p, throughput decreases significantly
```

---

## 5.12 Key Formulas Summary

| Concept | Formula |
|---------|---------|
| **Slow Start cwnd** | Doubles every RTT |
| **Congestion Avoidance cwnd** | +1 MSS per RTT |
| **On Timeout** | ssthresh = cwnd/2, cwnd = 1 |
| **On 3 Dup ACKs (Reno)** | ssthresh = cwnd/2, cwnd = ssthresh |
| **Throughput** | Window / RTT |
| **BDP** | Bandwidth × RTT |
| **RTO** | SRTT + 4 × DevRTT |
| **Effective Window** | min(cwnd, rwnd) |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: Congestion Window Evolution
**Q**: ssthresh = 16, trace cwnd for 10 RTTs.
**A**: 1→2→4→8→16→17→18→19→20→21 (Slow Start then CA)

### Pattern 2: After Timeout
**Q**: cwnd = 32, timeout occurs. New ssthresh and cwnd?
**A**: ssthresh = 32/2 = 16, cwnd = 1

### Pattern 3: Throughput
**Q**: Window = 64 KB, RTT = 100 ms. Throughput?
**A**: 64 × 8 / 0.1 = 5.12 Mbps

### Pattern 4: 3-Way Handshake
**Q**: How many RTTs for connection + one request-response?
**A**: 1 RTT (SYN, SYN-ACK) + 0.5 RTT (ACK+data) + 0.5 RTT (response)
       = 2 RTTs (approximately)

### Pattern 5: Port Numbers
**Q**: Which port does HTTP use?
**A**: TCP port 80

---

## 📝 Quick Revision Checklist

- [ ] UDP: 8-byte header, connectionless, unreliable
- [ ] TCP: 20+ byte header, connection-oriented, reliable
- [ ] 3-way handshake: SYN → SYN+ACK → ACK
- [ ] 4-way termination: FIN → ACK → FIN → ACK
- [ ] TIME_WAIT: 2 × MSL duration
- [ ] Slow Start: cwnd doubles every RTT until ssthresh
- [ ] Congestion Avoidance: cwnd +1 per RTT (AIMD)
- [ ] Timeout: ssthresh = cwnd/2, cwnd = 1
- [ ] 3 Dup ACKs (Reno): ssthresh = cwnd/2, cwnd = ssthresh
- [ ] Throughput = Window / RTT
- [ ] Well-known ports: HTTP(80), HTTPS(443), FTP(21), SSH(22), DNS(53)

---

## 🔥 One-Liner Summary

> "Transport layer provides process-to-process delivery using ports; UDP is fast but unreliable (8B header, no handshake); TCP is reliable with 3-way handshake (SYN-SYNACK-ACK), sliding window for flow control, and AIMD congestion control (slow start doubles cwnd, CA adds 1 per RTT); timeout resets cwnd=1, 3 dup ACKs halve cwnd (Reno); throughput = window/RTT."
