# Chapter 5: Transport Layer

## 🎯 The Atomic Truth
> **"End-to-end reliable/unreliable data delivery between processes using ports."**

---

## 5.1 Transport Layer Functions

### Core Responsibilities

| Function | Description |
|----------|-------------|
| **Process-to-Process Delivery** | Identify applications using port numbers |
| **Segmentation** | Break large data into segments |
| **Connection Management** | Establish, maintain, terminate connections |
| **Flow Control** | Match sender speed to receiver capacity |
| **Congestion Control** | Prevent network overload |
| **Error Control** | Detect and retransmit lost/corrupted data |

### The "Aha!" Moment 💡
Think of Transport Layer as the **"delivery service department"**:
- **Port** = Apartment number (which app in the host)
- **Socket** = Complete address (IP + Port)
- **TCP** = Registered mail (guaranteed delivery, signature)
- **UDP** = Postcard (fast, no guarantee)
- **Segment** = Package with tracking

### Network vs Transport Layer

| Aspect | Network Layer | Transport Layer |
|--------|---------------|-----------------|
| Addressing | IP (host-to-host) | Port (process-to-process) |
| Reliability | Best effort | TCP: Reliable, UDP: Best effort |
| Unit | Packet | Segment (TCP) / Datagram (UDP) |
| Scope | Router-to-router | End-to-end |

---

## 5.2 Port Numbers ⭐

### Port Number Ranges

| Range | Name | Description | Examples |
|-------|------|-------------|----------|
| 0-1023 | Well-known | Reserved for standard services | HTTP(80), FTP(21) |
| 1024-49151 | Registered | Registered applications | MySQL(3306) |
| 49152-65535 | Dynamic/Private | Ephemeral (client-side) | Auto-assigned |

### Important Port Numbers ⭐⭐

| Port | Protocol | Service |
|------|----------|---------|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (Server/Client) |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 119 | TCP | NNTP |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 161/162 | UDP | SNMP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB/CIFS |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |

**Memory Trick**: "**21F** **22S** **23T** **25S** **53D** **80H** **443H(S)**"
(FTP, SSH, Telnet, SMTP, DNS, HTTP, HTTPS)

### Socket = IP Address + Port Number

```
Socket: 192.168.1.10:80
        └─IP Address─┘ └Port┘

Connection identified by 4-tuple:
(Source IP, Source Port, Dest IP, Dest Port)
```

---

## 5.3 UDP (User Datagram Protocol) ⭐⭐

### 5.3.1 UDP Characteristics

| Aspect | Details |
|--------|---------|
| Connection | Connectionless |
| Reliability | Unreliable (no ACK, no retransmit) |
| Ordering | No guarantee |
| Flow Control | None |
| Congestion Control | None |
| Overhead | Low (8-byte header) |
| Speed | Fast |

### 5.3.2 UDP Header

```
 0      7 8     15 16    23 24    31
┌────────┬────────┬────────┬────────┐
│  Source Port    │   Dest Port     │  (2+2 = 4 bytes)
├─────────────────┼─────────────────┤
│     Length      │    Checksum     │  (2+2 = 4 bytes)
├─────────────────┴─────────────────┤
│              Data                 │
└───────────────────────────────────┘
```

**Header Size**: 8 bytes (fixed)

| Field | Size | Description |
|-------|------|-------------|
| Source Port | 2 bytes | Sender's port |
| Dest Port | 2 bytes | Receiver's port |
| Length | 2 bytes | Total datagram length (header + data) |
| Checksum | 2 bytes | Optional in IPv4, mandatory in IPv6 |

**Minimum UDP Datagram**: 8 bytes (header only)
**Maximum**: 65,535 - 20 (IP) - 8 (UDP) = 65,507 bytes data

### 5.3.3 UDP Checksum

Calculated over:
1. **Pseudo-header** (from IP header): Source IP, Dest IP, Protocol, UDP Length
2. **UDP Header**
3. **UDP Data**

### 5.3.4 When to Use UDP

| Use Case | Why UDP |
|----------|---------|
| DNS queries | Single request/response, speed |
| Streaming | Real-time, can tolerate loss |
| VoIP | Low latency critical |
| Online games | Speed over reliability |
| DHCP | Before IP assigned |
| TFTP | Simple file transfer |
| SNMP | Network management |

---

## 5.4 TCP (Transmission Control Protocol) ⭐⭐⭐

### 5.4.1 TCP Characteristics

| Aspect | Details |
|--------|---------|
| Connection | Connection-oriented (3-way handshake) |
| Reliability | Reliable (ACK, retransmit) |
| Ordering | Guaranteed (sequence numbers) |
| Flow Control | Yes (sliding window) |
| Congestion Control | Yes (multiple algorithms) |
| Overhead | Higher (20+ byte header) |
| Full-duplex | Yes |

### 5.4.2 TCP Header ⭐⭐

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│          Source Port          │       Destination Port        │
├───────────────────────────────┴───────────────────────────────┤
│                        Sequence Number                        │
├───────────────────────────────────────────────────────────────┤
│                    Acknowledgment Number                      │
├───────┬───────┬─┬─┬─┬─┬─┬─┬───────────────────────────────────┤
│  Data │       │U│A│P│R│S│F│                                   │
│Offset │ Res   │R│C│S│S│Y│I│            Window                 │
│       │       │G│K│H│T│N│N│                                   │
├───────┴───────┴─┴─┴─┴─┴─┴─┼───────────────────────────────────┤
│         Checksum          │         Urgent Pointer            │
├───────────────────────────┴───────────────────────────────────┤
│                    Options (if Data Offset > 5)               │
├───────────────────────────────────────────────────────────────┤
│                             Data                              │
└───────────────────────────────────────────────────────────────┘
```

### TCP Header Fields ⭐

| Field | Size | Description |
|-------|------|-------------|
| Source Port | 2 bytes | Sender's port |
| Dest Port | 2 bytes | Receiver's port |
| Sequence Number | 4 bytes | Byte number of first data byte |
| ACK Number | 4 bytes | Next expected byte from sender |
| Data Offset | 4 bits | Header length in 32-bit words (min 5) |
| Reserved | 6 bits | Must be zero |
| Flags | 6 bits | URG, ACK, PSH, RST, SYN, FIN |
| Window | 2 bytes | Receiver's buffer space (flow control) |
| Checksum | 2 bytes | Covers header + data + pseudo-header |
| Urgent Pointer | 2 bytes | Offset to urgent data (if URG set) |
| Options | Variable | MSS, Window Scale, Timestamps, SACK |

**Minimum Header**: 20 bytes (Data Offset = 5)
**Maximum Header**: 60 bytes (Data Offset = 15)

### TCP Flags ⭐⭐

| Flag | Name | Purpose |
|------|------|---------|
| **SYN** | Synchronize | Initiate connection |
| **ACK** | Acknowledge | Acknowledgment field valid |
| **FIN** | Finish | Terminate connection |
| **RST** | Reset | Abort connection |
| **PSH** | Push | Send data immediately (no buffer) |
| **URG** | Urgent | Urgent pointer field valid |

### 5.4.3 TCP Connection Establishment (3-Way Handshake) ⭐⭐⭐

```
Client                                Server
   │                                    │
   │──── SYN (seq=x) ──────────────────►│
   │                                    │
   │◄─── SYN+ACK (seq=y, ack=x+1) ──────│
   │                                    │
   │──── ACK (seq=x+1, ack=y+1) ────────►│
   │                                    │
   │        Connection Established       │
```

**Explanation**:
1. **Client → Server**: SYN (seq = ISN_client = x)
2. **Server → Client**: SYN+ACK (seq = ISN_server = y, ack = x+1)
3. **Client → Server**: ACK (seq = x+1, ack = y+1)

**Initial Sequence Number (ISN)**: Random for security.

**Why 3-way?** 
- 2-way: Server doesn't know if client received SYN+ACK
- Prevents old duplicate SYNs from creating connections

### 5.4.4 TCP Connection Termination (4-Way Handshake) ⭐⭐

```
Client                                Server
   │                                    │
   │──── FIN (seq=u) ──────────────────►│
   │                                    │
   │◄─── ACK (ack=u+1) ─────────────────│
   │                                    │
   │        (Server may send more data) │
   │                                    │
   │◄─── FIN (seq=v) ───────────────────│
   │                                    │
   │──── ACK (ack=v+1) ────────────────►│
   │                                    │
   │        Connection Closed           │
```

**Why 4-way?**
- Half-close: One side can close while other still sends
- Each direction closes independently

**TIME_WAIT State**: Client waits 2×MSL (Maximum Segment Lifetime) after sending final ACK
- Ensures last ACK reaches server
- Allows old packets to expire

### 5.4.5 TCP State Diagram (Simplified)

```
                    ┌─────────────┐
                    │   CLOSED    │
                    └──────┬──────┘
                           │ (passive open)
                    ┌──────▼──────┐
                    │   LISTEN    │◄──────────────┐
                    └──────┬──────┘               │
           (receive SYN)   │                      │
                    ┌──────▼──────┐               │
                    │  SYN_RCVD   │───────────────┤
                    └──────┬──────┘ (RST)         │
         (receive ACK)     │                      │
                    ┌──────▼──────┐               │
           ┌────────│ ESTABLISHED │               │
           │        └──────┬──────┘               │
           │ (close)       │ (receive FIN)        │
    ┌──────▼──────┐ ┌──────▼──────┐               │
    │  FIN_WAIT_1 │ │ CLOSE_WAIT  │               │
    └──────┬──────┘ └──────┬──────┘               │
           │               │ (close)              │
    ┌──────▼──────┐ ┌──────▼──────┐               │
    │  FIN_WAIT_2 │ │  LAST_ACK   │───────────────┘
    └──────┬──────┘ └─────────────┘
           │ (receive FIN)
    ┌──────▼──────┐
    │  TIME_WAIT  │ (2MSL timeout)
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │   CLOSED    │
    └─────────────┘
```

---

## 5.5 TCP Flow Control ⭐⭐

### 5.5.1 Sliding Window Protocol

**Receiver Window (rwnd)**: Advertised in TCP header (Window field)

```
Sender's View:
┌───────────────────────────────────────────────────────┐
│ Sent & ACKed │ Sent, not ACKed │ Can Send │ Cannot Send│
└──────────────┴─────────────────┴──────────┴────────────┘
               ◄──────── rwnd ────────────►
```

**Window Size**: 16 bits = max 65,535 bytes

**Window Scaling** (Option): Scale factor 0-14
$$\text{Actual Window} = \text{Window Field} \times 2^{\text{Scale Factor}}$$

Max with scaling: $65535 \times 2^{14} = 1$ GB

### 5.5.2 Silly Window Syndrome

**Problem**: Sender sends tiny segments due to small window advertisements.

**Solutions**:

| Side | Solution | Description |
|------|----------|-------------|
| Receiver | Clark's Solution | Only advertise window when ≥ MSS or half buffer |
| Sender | Nagle's Algorithm | Wait to collect more data before sending small segments |

**Nagle's Algorithm**:
- If pending data < MSS and there's unACKed data → wait
- Send when: MSS of data OR all previous data ACKed

---

## 5.6 TCP Congestion Control ⭐⭐⭐

### 5.6.1 Why Congestion Control?

Network can be overloaded → Packet drops → Retransmissions → More congestion

**Congestion Window (cwnd)**: Sender-side limit on data in flight

**Effective Window**:
$$\text{Effective Window} = \min(\text{cwnd}, \text{rwnd})$$

### 5.6.2 TCP Congestion Control Algorithms

#### Slow Start ⭐⭐

**Initial cwnd**: 1 MSS (or 10 MSS in modern TCP)

**Growth**: Exponential (doubles every RTT)
- For each ACK: $\text{cwnd} = \text{cwnd} + 1$ MSS
- After 1 RTT: cwnd doubles

```
RTT 1: cwnd = 1, send 1 segment
RTT 2: cwnd = 2, send 2 segments
RTT 3: cwnd = 4, send 4 segments
RTT 4: cwnd = 8, send 8 segments
...
```

**Slow Start Threshold (ssthresh)**: When cwnd reaches ssthresh, switch to Congestion Avoidance.

#### Congestion Avoidance ⭐⭐

**Growth**: Linear (additive increase)
- For each ACK: $\text{cwnd} = \text{cwnd} + \frac{1}{\text{cwnd}}$ MSS
- After 1 RTT: cwnd increases by 1 MSS

```
RTT n:   cwnd = 8
RTT n+1: cwnd = 9
RTT n+2: cwnd = 10
...
```

#### On Packet Loss

**Timeout (severe congestion)**:
- $\text{ssthresh} = \frac{\text{cwnd}}{2}$
- $\text{cwnd} = 1$ MSS
- Return to Slow Start

**3 Duplicate ACKs (mild congestion - Fast Retransmit/Recovery)** ⭐:
- $\text{ssthresh} = \frac{\text{cwnd}}{2}$
- $\text{cwnd} = \text{ssthresh} + 3$ MSS (Fast Recovery)
- Enter Congestion Avoidance

### 5.6.3 TCP Tahoe vs Reno ⭐⭐

| Event | TCP Tahoe | TCP Reno |
|-------|-----------|----------|
| 3 Dup ACKs | ssthresh = cwnd/2, cwnd = 1, Slow Start | ssthresh = cwnd/2, cwnd = ssthresh, Congestion Avoidance |
| Timeout | ssthresh = cwnd/2, cwnd = 1, Slow Start | ssthresh = cwnd/2, cwnd = 1, Slow Start |

**Key Difference**: Reno uses Fast Recovery on 3 dup ACKs (doesn't go to cwnd=1).

### 5.6.4 Congestion Control Diagram ⭐

```
cwnd
  │
  │                    ╱─────── Congestion Avoidance (linear)
  │                  ╱
  │      ssthresh ──╱ ─ ─ ─ ─ ─ ─ ─ ─ ─ 
  │              ╱│
  │            ╱  │
  │          ╱    │    Slow Start (exponential)
  │        ╱      │
  │      ╱        │
  │    ╱          │
  │  ╱            │
  │╱              │
  └───────────────┴──────────────────────► Time/RTT
```

### 5.6.5 AIMD (Additive Increase, Multiplicative Decrease)

- **Additive Increase**: cwnd += 1 per RTT (in Congestion Avoidance)
- **Multiplicative Decrease**: cwnd = cwnd/2 on loss

**AIMD leads to fairness** among TCP flows sharing a link.

### 5.6.6 Example (GATE Style) ⭐⭐

> Initial cwnd = 1, ssthresh = 32. 
> Show cwnd progression until RTT 12, assuming no loss.

| RTT | cwnd | Phase |
|-----|------|-------|
| 1 | 1 | Slow Start |
| 2 | 2 | Slow Start |
| 3 | 4 | Slow Start |
| 4 | 8 | Slow Start |
| 5 | 16 | Slow Start |
| 6 | 32 | Slow Start (= ssthresh) |
| 7 | 33 | Congestion Avoidance |
| 8 | 34 | Congestion Avoidance |
| 9 | 35 | Congestion Avoidance |
| 10 | 36 | Congestion Avoidance |
| 11 | 37 | Congestion Avoidance |
| 12 | 38 | Congestion Avoidance |

**GATE Trap**: Slow Start ends when cwnd ≥ ssthresh, not after!

---

## 5.7 TCP Timers ⭐

### 5.7.1 Retransmission Timer (RTO)

If ACK not received within RTO → Retransmit

**RTO Calculation**:
$$\text{EstimatedRTT} = (1-\alpha) \times \text{EstimatedRTT} + \alpha \times \text{SampleRTT}$$
$$\text{DevRTT} = (1-\beta) \times \text{DevRTT} + \beta \times |\text{SampleRTT} - \text{EstimatedRTT}|$$
$$\text{RTO} = \text{EstimatedRTT} + 4 \times \text{DevRTT}$$

Typical values: $\alpha = 0.125$, $\beta = 0.25$

### 5.7.2 Persistence Timer

When receiver advertises window = 0:
- Sender starts persistence timer
- On expiry, sends 1-byte probe
- Prevents deadlock

### 5.7.3 Keep-Alive Timer

Detect dead connections:
- Send probe after idle period (typically 2 hours)
- No response → Close connection

### 5.7.4 TIME_WAIT Timer

- Duration: 2 × MSL (Maximum Segment Lifetime)
- MSL typically 2 minutes → TIME_WAIT = 4 minutes
- Purpose: Ensure last ACK delivered, old packets expire

---

## 5.8 TCP Options

| Option | Length | Purpose |
|--------|--------|---------|
| **MSS** | 4 bytes | Maximum Segment Size negotiation |
| **Window Scale** | 3 bytes | Window size multiplication factor |
| **Timestamp** | 10 bytes | RTT measurement, PAWS |
| **SACK** | Variable | Selective Acknowledgment |
| **SACK Permitted** | 2 bytes | Indicates SACK support |

### MSS (Maximum Segment Size)

$$\text{MSS} = \text{MTU} - \text{IP Header} - \text{TCP Header}$$
$$\text{Default MSS} = 1500 - 20 - 20 = 1460 \text{ bytes}$$

Negotiated during handshake (SYN packets).

### SACK (Selective ACK)

Reports non-contiguous received blocks:
```
ACK 1000, SACK 2000-3000, 4000-5000
(means: received 1-999, 2000-2999, 4000-4999)
```

Allows sender to retransmit only missing segments.

---

## 5.9 TCP vs UDP Comparison ⭐⭐

| Aspect | TCP | UDP |
|--------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Unreliable |
| Ordering | Guaranteed | Not guaranteed |
| Flow Control | Yes (sliding window) | No |
| Congestion Control | Yes (AIMD) | No |
| Header Size | 20-60 bytes | 8 bytes |
| Speed | Slower | Faster |
| Overhead | Higher | Lower |
| Streaming | Byte stream | Message-based |
| Broadcast/Multicast | No | Yes |
| Use Cases | HTTP, FTP, SMTP | DNS, VoIP, Gaming |

---

## 5.10 Throughput and Efficiency ⭐⭐

### 5.10.1 TCP Throughput

**Maximum throughput limited by**:
1. Bandwidth
2. Receiver Window (rwnd)
3. Congestion Window (cwnd)
4. RTT

**Throughput Formula**:
$$\text{Throughput} = \frac{\text{Window Size}}{\text{RTT}}$$

**Maximum for long-fat network (LFN)**:
$$\text{Bandwidth-Delay Product} = \text{Bandwidth} \times \text{RTT}$$

If Window < BDP → Underutilization

### 5.10.2 Example (GATE Style)

> Link: 1 Gbps, RTT = 100 ms, Window = 64 KB.
> Calculate throughput.

**Solution**:
$$\text{BDP} = 10^9 \times 0.1 = 10^8 \text{ bits} = 12.5 \text{ MB}$$
$$\text{Window} = 64 \text{ KB} = 0.0625 \text{ MB}$$

Since Window << BDP:
$$\text{Throughput} = \frac{64 \times 1024 \times 8}{0.1} = 5.24 \text{ Mbps}$$

**Efficiency**: $\frac{5.24}{1000} = 0.52\%$ (very low!)

**Need window scaling** to increase window beyond 64 KB.

---

## 5.11 SCTP (Stream Control Transmission Protocol)

| Aspect | Details |
|--------|---------|
| Features | TCP reliability + UDP message-based |
| Multi-homing | Multiple IP addresses per endpoint |
| Multi-streaming | Multiple independent streams |
| Use Case | Telecom signaling (SS7 over IP) |
| Protection | Cookie-based 4-way handshake (against SYN flood) |

---

## 5.12 Edge Cases & GATE Traps

### Trap 1: Sequence Number vs ACK Number
- **Sequence Number**: Byte number of FIRST byte in this segment
- **ACK Number**: NEXT byte expected from other side
- ACK 5000 means "received up to 4999, send 5000 next"

### Trap 2: Slow Start is NOT Slow
- Name is misleading
- Slow Start has exponential growth
- Congestion Avoidance is linear (slower)

### Trap 3: 3 Duplicate ACKs = 4 Same ACKs
- Original ACK + 3 duplicates = 4 identical ACKs
- This triggers Fast Retransmit

### Trap 4: MSS vs MTU
- MTU = Max frame size at Network layer (includes IP header)
- MSS = Max TCP data size (excludes TCP/IP headers)
- MSS = MTU - 40 (typically)

### Trap 5: cwnd Units
- cwnd is in bytes or MSS depending on context
- GATE often uses MSS units
- "cwnd = 4" usually means 4 MSS

### Trap 6: ssthresh After Timeout
- ssthresh = cwnd/2 (at time of timeout)
- NOT ssthresh/2

### Trap 7: Window = 0 Deadlock
- Receiver advertises 0 → Sender stops
- If "window update" packet lost → Deadlock
- Solution: Persistence timer with probe

---

## 📝 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Well-known Ports | 0-1023 |
| UDP Header | 8 bytes, connectionless |
| TCP Header | 20-60 bytes, connection-oriented |
| 3-Way Handshake | SYN → SYN+ACK → ACK |
| 4-Way Termination | FIN → ACK → FIN → ACK |
| Flow Control | rwnd in TCP header |
| Slow Start | cwnd doubles each RTT |
| Congestion Avoidance | cwnd += 1 per RTT |
| Tahoe (loss) | cwnd = 1 |
| Reno (3 dup ACK) | cwnd = ssthresh |
| RTO | EstRTT + 4×DevRTT |
| Throughput | Window/RTT |

---

## 🧪 Practice Problems

### Problem 1 (GATE Style)
A TCP connection has initial cwnd = 1 MSS, ssthresh = 16 MSS. After 8 RTTs without loss, what is cwnd?

<details>
<summary>Solution</summary>

RTT 1: cwnd = 1 (Slow Start)
RTT 2: cwnd = 2
RTT 3: cwnd = 4
RTT 4: cwnd = 8
RTT 5: cwnd = 16 (= ssthresh, switch to CA)
RTT 6: cwnd = 17
RTT 7: cwnd = 18
RTT 8: cwnd = 19

**Answer: 19 MSS**

</details>

### Problem 2 (GATE Style)
TCP Reno: cwnd = 40 MSS, ssthresh = 32 MSS. Three duplicate ACKs received. What happens?

<details>
<summary>Solution</summary>

On 3 duplicate ACKs (Reno - Fast Recovery):
- ssthresh = cwnd/2 = 40/2 = 20 MSS
- cwnd = ssthresh + 3 = 20 + 3 = 23 MSS
- Enter Congestion Avoidance

**Answer: ssthresh = 20, cwnd = 23 MSS**

</details>

### Problem 3 (GATE NAT)
Link bandwidth = 100 Mbps, RTT = 50 ms. What window size is needed for 100% utilization?

<details>
<summary>Solution</summary>

BDP = Bandwidth × RTT
BDP = 100 × 10^6 × 0.05 = 5 × 10^6 bits = 625,000 bytes

**Answer: 625,000 bytes (or ~610 KB)**

</details>

### Problem 4 (GATE Style)
During TCP connection setup, client sends SYN with seq = 100. Server responds with SYN+ACK with seq = 300. What ACK number does server send?

<details>
<summary>Solution</summary>

Server ACK = Client's seq + 1 = 100 + 1 = 101

**Answer: ACK = 101**

</details>

---

**Previous Chapter**: [← Chapter 4: Network Layer](./Chapter-04-Network-Layer.md)

**Next Chapter**: [Chapter 6: Application Layer →](./Chapter-06-Application-Layer.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]*
