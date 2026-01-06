# Chapter 6: Transport Layer
## The End-to-End Champion | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Transport layer delivers data process-to-process; TCP guarantees, UDP doesn't."**

---

## 6.1 Transport Layer Functions

1. **Process-to-Process Delivery:** Using port numbers
2. **Segmentation:** Breaking data into segments
3. **Connection Management:** Establish, maintain, terminate (TCP)
4. **Flow Control:** Prevent receiver overwhelm (TCP)
5. **Error Control:** Detect and recover errors (TCP)
6. **Congestion Control:** Prevent network overwhelm (TCP)

---

## 6.2 Port Numbers

### Well-Known Ports (0-1023)

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

### Port Ranges

| Range | Type | Use |
|-------|------|-----|
| 0-1023 | Well-known | System services |
| 1024-49151 | Registered | User applications |
| 49152-65535 | Dynamic/Ephemeral | Client connections |

### Socket

$$\text{Socket} = \text{IP Address} + \text{Port Number}$$

Example: 192.168.1.10:80

---

## 6.3 UDP (User Datagram Protocol)

### Characteristics

- **Connectionless:** No setup required
- **Unreliable:** No guaranteed delivery
- **Unordered:** Packets may arrive out of order
- **Fast:** Low overhead
- **No flow/congestion control**

### UDP Header

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┤
│          Source Port          │       Destination Port        │
├───────────────────────────────┼───────────────────────────────┤
│            Length             │           Checksum            │
└───────────────────────────────┴───────────────────────────────┘
```

**Header Size:** 8 bytes (fixed)

| Field | Size | Description |
|-------|------|-------------|
| Source Port | 16 bits | Sender's port |
| Destination Port | 16 bits | Receiver's port |
| Length | 16 bits | Header + Data (min 8) |
| Checksum | 16 bits | Error detection |

### UDP Checksum Calculation

Uses **pseudo-header** for integrity:
```
┌───────────────────────────────────────────────────────────────┐
│                     Source IP Address                         │
├───────────────────────────────────────────────────────────────┤
│                   Destination IP Address                      │
├───────────────┬───────────────┬───────────────────────────────┤
│   All zeros   │   Protocol=17 │         UDP Length            │
└───────────────┴───────────────┴───────────────────────────────┘
```

### UDP Use Cases

- DNS queries
- DHCP
- Streaming media
- VoIP
- Online gaming
- IoT/Sensors

---

## 6.4 TCP (Transmission Control Protocol)

### Characteristics

- **Connection-oriented:** 3-way handshake
- **Reliable:** Guaranteed delivery
- **Ordered:** In-sequence delivery
- **Flow Control:** Sliding window
- **Congestion Control:** Multiple algorithms
- **Full-duplex:** Both directions simultaneously

### TCP Header

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┤
│          Source Port          │       Destination Port        │
├───────────────────────────────────────────────────────────────┤
│                        Sequence Number                        │
├───────────────────────────────────────────────────────────────┤
│                    Acknowledgment Number                      │
├───────┬───────┬─┬─┬─┬─┬─┬─┬───────────────────────────────────┤
│ Data  │       │U│A│P│R│S│F│                                   │
│Offset │ Rsrvd │R│C│S│S│Y│I│            Window Size            │
│       │       │G│K│H│T│N│N│                                   │
├───────┴───────┴─┴─┴─┴─┴─┴─┴───────────────────────────────────┤
│           Checksum            │         Urgent Pointer        │
├───────────────────────────────────────────────────────────────┤
│                    Options (if any)                           │
└───────────────────────────────────────────────────────────────┘
```

**Header Size:** 20-60 bytes (20 minimum)

### TCP Flags

| Flag | Name | Purpose |
|------|------|---------|
| SYN | Synchronize | Connection setup |
| ACK | Acknowledgment | Confirms receipt |
| FIN | Finish | Connection teardown |
| RST | Reset | Abort connection |
| PSH | Push | Deliver immediately |
| URG | Urgent | Priority data |

---

## 6.5 TCP Connection Management

### 3-Way Handshake (Connection Establishment)

```
Client                                Server
   │                                    │
   │────SYN, seq=x──────────────────→│
   │                                    │ (SYN received)
   │←────SYN+ACK, seq=y, ack=x+1────│
   │ (SYN+ACK received)                │
   │────ACK, seq=x+1, ack=y+1───────→│
   │                                    │ (Connection Established)
   │       ←── Data Transfer ──→       │
```

**States:**
- Client: CLOSED → SYN_SENT → ESTABLISHED
- Server: CLOSED → LISTEN → SYN_RCVD → ESTABLISHED

### 4-Way Handshake (Connection Termination)

```
Client                                Server
   │                                    │
   │────FIN, seq=u───────────────────→│
   │                                    │
   │←────ACK, ack=u+1─────────────────│
   │                                    │
   │←────FIN, seq=v───────────────────│
   │                                    │
   │────ACK, ack=v+1─────────────────→│
   │                                    │
```

**TIME_WAIT:** Client waits 2×MSL (Maximum Segment Lifetime) before closing.

### TCP State Diagram

```
       CLOSED
          │
    passive open
          ↓
       LISTEN ←───────────────────┐
          │                        │
     SYN received                  │
          ↓                        │
     SYN_RCVD ────→ ESTABLISHED ──┤
          ↑              │         │
     SYN+ACK         data transfer │
          │              ↓         │
    SYN_SENT ────→ ESTABLISHED    │
       (active open)     │         │
                    close │         │
                         ↓         │
                   FIN_WAIT_1      │
                         │         │
                   FIN_WAIT_2      │
                         │         │
                    TIME_WAIT ─────┘
```

---

## 6.6 TCP Reliable Data Transfer

### Sequence Numbers

- Byte-oriented (not segment-oriented)
- Initial Sequence Number (ISN) randomly chosen
- Each byte has a sequence number

**Example:**
- ISN = 1000
- First segment: 500 bytes, seq = 1000
- Second segment: 500 bytes, seq = 1500
- Third segment: 500 bytes, seq = 2000

### Acknowledgment Numbers

- Next expected byte
- Cumulative ACKs

**Example:**
- Received bytes 1000-1499: ACK = 1500
- Received bytes 1500-1999: ACK = 2000

### Retransmission

**Timeout-based:**
$$\text{RTO} = \text{SRTT} + 4 \times \text{RTTVAR}$$

Where:
- SRTT = Smoothed RTT
- RTTVAR = RTT Variance

**Fast Retransmit:**
- 3 duplicate ACKs trigger retransmission
- Don't wait for timeout

```
Sender          Receiver
  │───Seg 1───→│
  │───Seg 2───→│  ← Lost!
  │───Seg 3───→│
  │←──ACK 1────│
  │←──ACK 1────│  (dup 1)
  │───Seg 4───→│
  │←──ACK 1────│  (dup 2)
  │←──ACK 1────│  (dup 3)
  │───Seg 2───→│  ← Retransmit!
```

---

## 6.7 TCP Flow Control

### Sliding Window

Receiver advertises **receive window (rwnd)** in TCP header.

```
Sender's view:
├─────────────┬───────────────────────┬─────────────────┤
│    Sent &   │      Sent but not     │   Not yet sent  │
│    ACKed    │       ACKed           │                 │
└─────────────┴───────────────────────┴─────────────────┘
              ↑                       ↑
          Send base              Send base + window
```

**Window Size:** How much can be sent without ACK

**rwnd = 0:** Receiver says "stop sending!"

### 🎯 Throughput Formula

$$\text{Throughput} = \frac{\text{Window Size}}{\text{RTT}}$$

**Example:**
- Window = 64 KB = 524,288 bits
- RTT = 100 ms
- Throughput = 524,288 / 0.1 = 5.24 Mbps

---

## 6.8 TCP Congestion Control

### Why Congestion Control?
Network can't handle all traffic → dropped packets, delays.

### Congestion Window (cwnd)

Sender maintains cwnd limiting bytes in flight.

$$\text{Effective Window} = \min(\text{cwnd}, \text{rwnd})$$

### Slow Start

```
cwnd doubles each RTT (exponential growth)
Initial cwnd = 1 MSS (Maximum Segment Size)

RTT 1: cwnd = 1 MSS
RTT 2: cwnd = 2 MSS
RTT 3: cwnd = 4 MSS
RTT 4: cwnd = 8 MSS
...
Until cwnd ≥ ssthresh (slow start threshold)
```

### Congestion Avoidance

After ssthresh reached, linear growth:
$$\text{cwnd} = \text{cwnd} + \frac{\text{MSS}^2}{\text{cwnd}}$$

Approximately: cwnd increases by 1 MSS per RTT.

### Congestion Detection

**Timeout (severe):**
- ssthresh = cwnd / 2
- cwnd = 1 MSS
- Enter Slow Start

**3 Duplicate ACKs (mild):**
- ssthresh = cwnd / 2
- cwnd = ssthresh + 3 MSS
- Enter Fast Recovery

### TCP Tahoe vs Reno vs Cubic

| Event | Tahoe | Reno | Cubic |
|-------|-------|------|-------|
| 3 Dup ACKs | SS | Fast Recovery | Fast Recovery |
| Timeout | SS | SS | SS |
| Advantage | Simple | Better | Best for high BW-delay |

### AIMD (Additive Increase, Multiplicative Decrease)

- **Additive Increase:** cwnd += 1 per RTT (linear)
- **Multiplicative Decrease:** cwnd = cwnd / 2 on loss

Creates sawtooth pattern:

```
cwnd
 ↑
 │    /\      /\      /\
 │   /  \    /  \    /  \
 │  /    \  /    \  /    \
 │ /      \/      \/      \
 └──────────────────────────→ time
```

---

## 6.9 TCP vs UDP Comparison

| Aspect | TCP | UDP |
|--------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed | Best effort |
| Ordering | Ordered | Unordered |
| Speed | Slower | Faster |
| Header Size | 20-60 bytes | 8 bytes |
| Flow Control | Yes | No |
| Congestion Control | Yes | No |
| Use Case | Web, Email, File | Streaming, DNS, Gaming |

---

## 6.10 Bandwidth-Delay Product

$$BDP = \text{Bandwidth} \times \text{RTT}$$

Represents the amount of data "in flight."

**Example:**
- Bandwidth = 100 Mbps
- RTT = 100 ms
- BDP = 100 × 10⁶ × 0.1 / 8 = 1.25 MB

For full utilization, window size should ≥ BDP.

---

## 🎯 Practice Problems

### Problem 1: Window Size
**Q:** RTT = 50 ms, required throughput = 10 Mbps. Find minimum window size.

**Solution:**
- Throughput = Window / RTT
- 10 × 10⁶ = Window / 0.05
- Window = 500,000 bits = **62,500 bytes ≈ 62 KB**

### Problem 2: TCP Sequence
**Q:** ISN = 5000, sends 3 segments of 1000 bytes each. What are sequence numbers?

**Solution:**
- Segment 1: seq = 5000
- Segment 2: seq = 6000
- Segment 3: seq = 7000

### Problem 3: Slow Start
**Q:** Initial cwnd = 1 MSS, ssthresh = 32 MSS. After 5 RTTs in slow start, what's cwnd?

**Solution:**
- RTT 1: cwnd = 1
- RTT 2: cwnd = 2
- RTT 3: cwnd = 4
- RTT 4: cwnd = 8
- RTT 5: cwnd = 16
**Answer: 16 MSS**

### Problem 4: Fast Retransmit
**Q:** What triggers fast retransmit?
**Answer:** 3 duplicate ACKs

### Problem 5: Effective Window
**Q:** cwnd = 32 KB, rwnd = 48 KB. What's effective window?
**Answer:** min(32, 48) = **32 KB**

### Problem 6: Bandwidth-Delay Product
**Q:** Link = 1 Gbps, RTT = 20 ms. Find BDP.
**Solution:**
- BDP = 10⁹ × 0.02 / 8 = 2,500,000 bytes = **2.5 MB**

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"TCP Takes Care Properly, UDP Utterly Doesn't Promise"**

**"SYN → SYN-ACK → ACK = Three-Way Handshake"**

### The Mental Slider
- **Slow Start:** Car accelerating from 0 (exponential)
- **Congestion Avoidance:** Cruise control (linear)
- **Fast Recovery:** Quick tap on brakes, don't stop

### The 5-Second Snap-Check
1. **TCP reliable?** Yes, ACKs + retransmit
2. **UDP header size?** 8 bytes
3. **TCP header size?** 20-60 bytes
4. **Slow start?** Double cwnd each RTT
5. **Fast retransmit?** 3 dup ACKs

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| Throughput = Window / RTT | Flow control throughput |
| Effective Window = min(cwnd, rwnd) | Actual send limit |
| BDP = Bandwidth × RTT | Data in flight |
| Slow Start: cwnd = 2^n after n RTTs | Exponential growth |
| Congestion Avoidance: cwnd += 1/RTT | Linear growth |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Network Layer](05-Network-Layer.md) | [Next: Application Layer →](07-Application-Layer.md)
