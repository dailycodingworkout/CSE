# Module 7: Transport Layer | The Singularity

> **The Atomic Truth:** *Transport Layer = End-to-end process delivery*

---

## 7.1 Transport Layer Overview

### **Position in Stack**

```
Application Layer (HTTP, FTP, SMTP)
        ↓ Data
┌───────────────────────────────────┐
│       TRANSPORT LAYER             │
│                                   │
│   Process-to-Process Delivery     │
│   Port Numbers                    │
│   TCP (Reliable) / UDP (Fast)     │
│                                   │
└───────────────────────────────────┘
        ↓ Segment/Datagram
Network Layer (IP)
```

### **Core Responsibilities**
1. **Process-to-Process Delivery** — Using port numbers
2. **Segmentation & Reassembly** — Breaking data into segments
3. **Connection Management** — Setup/teardown (TCP)
4. **Flow Control** — Preventing receiver overflow
5. **Congestion Control** — Preventing network overflow
6. **Error Control** — Reliable delivery (TCP)

### **The Analogy 💡**
If Network Layer is the postal system (house address), Transport Layer is the **apartment number** — delivering to the specific person (process).

---

## 7.2 Port Numbers

### **Port Number Ranges**

| Range | Name | Description | Examples |
|-------|------|-------------|----------|
| 0-1023 | **Well-Known** | System/standard services | HTTP(80), FTP(21), SSH(22) |
| 1024-49151 | **Registered** | Application-specific | MySQL(3306), MongoDB(27017) |
| 49152-65535 | **Dynamic/Private** | Ephemeral ports | Client-side ports |

### **Critical Port Numbers (GATE Favorites)**

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
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 161 | UDP | SNMP |
| 443 | TCP | HTTPS |

### **The Mnemonic 🧠**
> **"FTP: 20/21, SSH: 22, SMTP: 25, DNS: 53, HTTP: 80, HTTPS: 443"**

### **Socket = IP Address + Port Number**
$$Socket = (IP, Port)$$
$$Connection = (Source Socket, Destination Socket)$$

---

## 7.3 UDP (User Datagram Protocol)

### **The Atomic Truth:** *UDP = Fast, unreliable, connectionless*

### **UDP Header (8 bytes)**

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│         Source Port            │        Destination Port       │
├─────────────────────────────────┼─────────────────────────────────┤
│            Length              │            Checksum             │
├─────────────────────────────────┴─────────────────────────────────┤
│                          Data (if any)                           │
└───────────────────────────────────────────────────────────────────┘
```

### **UDP Characteristics**

| Feature | UDP |
|---------|-----|
| Connection | Connectionless |
| Reliability | Unreliable (no ACK, retransmission) |
| Ordering | No guarantee |
| Flow Control | None |
| Congestion Control | None |
| Header Size | 8 bytes |
| Speed | Fast (low overhead) |

### **When to Use UDP**

1. ✅ Real-time applications (VoIP, video streaming)
2. ✅ DNS queries (small, quick)
3. ✅ DHCP, TFTP
4. ✅ Online gaming
5. ✅ Multicast/Broadcast

### **UDP Length Field**
- Includes header + data
- Minimum: 8 bytes (header only)
- Maximum: 65,535 bytes (limited by IP)

---

## 7.4 TCP (Transmission Control Protocol)

### **The Atomic Truth:** *TCP = Reliable, ordered, connection-oriented*

### **TCP Header (20-60 bytes)**

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│         Source Port            │        Destination Port       │
├───────────────────────────────────────────────────────────────────┤
│                        Sequence Number                           │
├───────────────────────────────────────────────────────────────────┤
│                    Acknowledgment Number                         │
├───────────────────────────────────────────────────────────────────┤
│ Data  │Reser│ Flags           │                                 │
│Offset │ved  │U A P R S F      │          Window Size            │
│4 bits │3bits│R C S S Y I      │            16 bits              │
│       │     │G K H T N N      │                                 │
├───────────────────────────────────┼───────────────────────────────┤
│          Checksum              │         Urgent Pointer          │
├───────────────────────────────────┴───────────────────────────────┤
│                    Options (if Data Offset > 5)                   │
├───────────────────────────────────────────────────────────────────┤
│                              Data                                 │
└───────────────────────────────────────────────────────────────────┘
```

### **TCP Flags (6 bits)**

| Flag | Name | Purpose |
|------|------|---------|
| **URG** | Urgent | Urgent pointer is valid |
| **ACK** | Acknowledgment | ACK number is valid |
| **PSH** | Push | Push data immediately to application |
| **RST** | Reset | Reset connection (error) |
| **SYN** | Synchronize | Initiate connection |
| **FIN** | Finish | Terminate connection |

### **TCP Characteristics**

| Feature | TCP |
|---------|-----|
| Connection | Connection-oriented |
| Reliability | Reliable (ACKs, retransmission) |
| Ordering | Guaranteed (sequence numbers) |
| Flow Control | Yes (sliding window) |
| Congestion Control | Yes |
| Header Size | 20-60 bytes |
| Speed | Slower (more overhead) |

---

## 7.5 TCP Connection Management

### **Three-Way Handshake (Connection Establishment)**

```
    Client                              Server
       │                                   │
       │ ──── SYN (seq=x) ───────────────>│
       │                                   │
       │ <─── SYN+ACK (seq=y, ack=x+1) ───│
       │                                   │
       │ ──── ACK (ack=y+1) ─────────────>│
       │                                   │
    ESTABLISHED                       ESTABLISHED
```

**Why 3-way?**
- Synchronizes sequence numbers
- Confirms both sides are ready
- Prevents old duplicate connections

### **Four-Way Termination (Connection Teardown)**

```
    Client                              Server
       │                                   │
       │ ──── FIN (seq=u) ───────────────>│  (Client wants to close)
       │                                   │
       │ <─── ACK (ack=u+1) ──────────────│  (Server acknowledges)
       │                                   │
       │ <─── FIN (seq=v) ────────────────│  (Server also wants to close)
       │                                   │
       │ ──── ACK (ack=v+1) ─────────────>│  (Client acknowledges)
       │                                   │
    CLOSED                            CLOSED
```

**TIME-WAIT State:**
- Client waits 2×MSL (Maximum Segment Lifetime) before closing
- Ensures all segments are received/expired
- MSL typically = 2 minutes, so TIME-WAIT = 4 minutes

### **TCP State Diagram (Simplified)**

```
                    CLOSED
                       │
            ┌──────────┴──────────┐
            │ (Active Open)       │ (Passive Open)
            ↓                     ↓
         SYN_SENT            LISTEN
            │                     │
            │ (Receive SYN+ACK)   │ (Receive SYN)
            ↓                     ↓
       ESTABLISHED ←──────── SYN_RCVD
            │
       (Application closes)
            ↓
        FIN_WAIT_1
            │
            ↓
        FIN_WAIT_2
            │
        TIME_WAIT
            │
         CLOSED
```

---

## 7.6 TCP Flow Control

### **The Problem**
Fast sender can overwhelm slow receiver

### **Solution: Sliding Window**

```
┌───────────────────────────────────────────────────────────────────┐
│                        SENDER'S WINDOW                             │
├─────────┬─────────────────────────────────┬───────────────────────┤
│  Sent   │           Window                │    Not yet usable     │
│  & ACKed│   (can send without ACK)        │   (beyond window)     │
├─────────┼─────────────────────────────────┼───────────────────────┤
│ 1 2 3 4 │ 5  6  7  8  9  10  11  12       │ 13 14 15 16 ...       │
└─────────┴─────────────────────────────────┴───────────────────────┘
           ↑                            ↑
        Last ACKed              Window Size (rwnd)
```

### **Window Size**
- **rwnd (Receiver Window):** Receiver's buffer space
- **cwnd (Congestion Window):** Sender's congestion control
- **Effective Window = min(rwnd, cwnd)**

### **Zero Window**
- Receiver sends window = 0 when buffer full
- Sender stops and starts **persist timer**
- Sender sends **window probe** (1 byte) periodically

---

## 7.7 TCP Congestion Control | The GATE Goldmine 🔑

### **The Four Phases**

```
cwnd
  ↑
  │                    ┌──────────────────────────
  │                   /   Congestion Avoidance
  │                  /     (linear increase)
  │                 /
  │                /──────────────────────────────
  │               /  ssthresh
  │              ╱
  │            ╱╱   Slow Start
  │          ╱╱     (exponential)
  │        ╱╱
  │      ╱╱
  │    ╱╱
  │  ╱╱
  │╱
  └────────────────────────────────────────────────→ Time
```

### **Phase 1: Slow Start**
- Initial: cwnd = 1 MSS (Maximum Segment Size)
- After each ACK: cwnd = cwnd + 1 MSS
- After each RTT: cwnd doubles (exponential growth)
- **Continue until:** cwnd ≥ ssthresh (slow start threshold)

### **Phase 2: Congestion Avoidance**
- After each RTT: cwnd = cwnd + 1 MSS (linear growth)
- Or: cwnd = cwnd + MSS × (MSS/cwnd) per ACK
- **Continue until:** Packet loss detected

### **Phase 3: Fast Retransmit**
- On receiving 3 duplicate ACKs:
  - Retransmit lost segment immediately
  - Don't wait for timeout

### **Phase 4: Fast Recovery**
- After fast retransmit (3 dup ACKs):
  - ssthresh = cwnd/2
  - cwnd = ssthresh + 3 MSS
  - Continue congestion avoidance

### **On Timeout:**
- ssthresh = cwnd/2
- cwnd = 1 MSS
- Restart slow start

### **Congestion Control Summary**

| Event | ssthresh | cwnd |
|-------|----------|------|
| **Initial** | 65535 bytes | 1 MSS |
| **Each ACK (SS)** | unchanged | cwnd + 1 |
| **Each RTT (SS)** | unchanged | cwnd × 2 |
| **cwnd ≥ ssthresh** | unchanged | Enter CA |
| **Each RTT (CA)** | unchanged | cwnd + 1 |
| **3 Dup ACKs** | cwnd/2 | ssthresh + 3 |
| **Timeout** | cwnd/2 | 1 MSS |

### **Tahoe vs Reno vs New Reno**

| Algorithm | On 3 Dup ACKs | On Timeout |
|-----------|---------------|------------|
| **Tahoe** | cwnd = 1, slow start | cwnd = 1, slow start |
| **Reno** | cwnd = ssthresh (fast recovery) | cwnd = 1, slow start |
| **New Reno** | Improved fast recovery | cwnd = 1, slow start |

### **GATE Trap Alert ⚠️**

**Common Question:** "After how many RTTs will cwnd reach X?"

**Slow Start:**
After RTT 0: cwnd = 1
After RTT 1: cwnd = 2
After RTT 2: cwnd = 4
After RTT n: cwnd = $2^n$

To reach cwnd = 32: $2^n = 32$, so $n = 5$ RTTs

---

## 7.8 TCP Timers

| Timer | Purpose | Action on Expiry |
|-------|---------|------------------|
| **Retransmission (RTO)** | Detect lost segment | Retransmit |
| **Persist** | Probe zero window | Send window probe |
| **Keepalive** | Check idle connection | Send probe segment |
| **TIME-WAIT** | Ensure all segments expire | Close connection |

### **RTO Calculation (Jacobson's Algorithm)**

$$SRTT = (1-\alpha) \times SRTT + \alpha \times RTT$$
$$RTTVAR = (1-\beta) \times RTTVAR + \beta \times |SRTT - RTT|$$
$$RTO = SRTT + 4 \times RTTVAR$$

Typically: $\alpha = 1/8$, $\beta = 1/4$

---

## 7.9 TCP vs UDP Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| **Connection** | Connection-oriented | Connectionless |
| **Reliability** | Reliable | Unreliable |
| **Ordering** | Ordered | Unordered |
| **Flow Control** | Yes | No |
| **Congestion Control** | Yes | No |
| **Header Size** | 20-60 bytes | 8 bytes |
| **Speed** | Slower | Faster |
| **Overhead** | High | Low |
| **Use Case** | File transfer, web, email | Streaming, DNS, gaming |

---

## 7.10 Throughput Calculations

### **Maximum Throughput**

$$Throughput = \frac{Window Size}{RTT}$$

### **Bandwidth-Delay Product**

$$BDP = Bandwidth \times RTT$$

This is the optimal window size for full utilization.

### **TCP Throughput with Loss**

$$Throughput \approx \frac{MSS}{RTT \times \sqrt{p}}$$

Where $p$ = packet loss probability

### **Efficiency with Stop-and-Wait**

$$\eta = \frac{T_{trans}}{T_{trans} + 2T_{prop}} = \frac{1}{1 + 2a}$$

### **Efficiency with Pipelining**

$$\eta = \begin{cases} 1 & \text{if } W \geq 1 + 2a \\ \frac{W}{1 + 2a} & \text{if } W < 1 + 2a \end{cases}$$

---

## 7.11 Solved Examples

### **Example 1: TCP Connection**

**Problem:** How many segments are exchanged in establishing and closing a TCP connection (normal case)?

**Solution:**
- Establishment: 3 (SYN, SYN+ACK, ACK)
- Termination: 4 (FIN, ACK, FIN, ACK)
- **Total: 7 segments**

---

### **Example 2: Congestion Window Growth**

**Problem:** Initial cwnd = 1 KB, ssthresh = 16 KB, MSS = 1 KB. Find cwnd after 8 RTTs (no loss).

**Solution:**

**Slow Start (cwnd < 16):**
- RTT 0: cwnd = 1
- RTT 1: cwnd = 2
- RTT 2: cwnd = 4
- RTT 3: cwnd = 8
- RTT 4: cwnd = 16 → hits ssthresh

**Congestion Avoidance (cwnd ≥ 16):**
- RTT 5: cwnd = 17
- RTT 6: cwnd = 18
- RTT 7: cwnd = 19
- RTT 8: cwnd = 20

**Answer: cwnd = 20 KB**

---

### **Example 3: Throughput Calculation**

**Problem:** A TCP connection has window size 64 KB, RTT = 100 ms. Calculate maximum throughput.

**Solution:**
$$Throughput = \frac{Window}{RTT} = \frac{64 \times 8 \times 1000}{0.1} = \frac{512000}{0.1} = 5.12 \text{ Mbps}$$

---

### **Example 4: Bandwidth-Delay Product**

**Problem:** A link has bandwidth 10 Mbps and RTT 50 ms. What window size is needed for full utilization?

**Solution:**
$$BDP = 10 \times 10^6 \times 0.05 = 500,000 \text{ bits} = 62.5 \text{ KB}$$

Window should be at least 62.5 KB for full link utilization.

---

## 7.12 Practice Problems

**Q1.** TCP header minimum size is:
- (a) 8 bytes
- (b) 16 bytes
- (c) 20 bytes
- (d) 32 bytes

<details>
<summary>Answer</summary>
**(c) 20 bytes** — Minimum TCP header (no options)
</details>

---

**Q2.** Which flag is used to initiate a TCP connection?
- (a) FIN
- (b) ACK
- (c) SYN
- (d) RST

<details>
<summary>Answer</summary>
**(c) SYN** — SYN flag initiates connection
</details>

---

**Q3.** [NAT] In TCP slow start, if initial cwnd = 1 MSS, what is cwnd after 6 RTTs?

<details>
<summary>Answer</summary>
cwnd = $2^6 = \boxed{64}$ MSS
(Assuming ssthresh > 64)
</details>

---

**Q4.** UDP uses port 53 for:
- (a) HTTP
- (b) FTP
- (c) DNS
- (d) SMTP

<details>
<summary>Answer</summary>
**(c) DNS** — DNS uses port 53 (both TCP and UDP)
</details>

---

**Q5.** [NAT] How many segments are exchanged in TCP 3-way handshake?

<details>
<summary>Answer</summary>
$\boxed{3}$ — SYN, SYN+ACK, ACK
</details>

---

## 7.13 The 5-Second Snap-Check ✅

1. ☐ TCP header = 20 bytes min; UDP header = 8 bytes
2. ☐ Well-known ports: 0-1023
3. ☐ TCP connection: 3-way handshake (SYN, SYN+ACK, ACK)
4. ☐ TCP termination: 4 segments (FIN, ACK, FIN, ACK)
5. ☐ Slow start: cwnd doubles each RTT
6. ☐ Congestion avoidance: cwnd + 1 each RTT
7. ☐ 3 dup ACKs → fast retransmit + fast recovery
8. ☐ Timeout → cwnd = 1, restart slow start

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 8: Application Layer →](./08-Application-Layer.md)
