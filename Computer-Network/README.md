# 🌐 Computer Networks — GATE & ESE Ultimate Study Material

> **The Singularity:** Data moves in packets, governed by layered protocols.

Welcome to the **Computer Networks** section of the CSE repository! This comprehensive study material is specifically designed for **GATE** and **ESE** aspirants aiming for **Rank #1**. Every concept is explained from first principles with mathematical rigor, intuitive analogies, edge cases, traps, and exam-oriented tricks.

---

## 📋 Table of Contents

| Chapter | Topic | Key Focus Areas |
|---------|-------|-----------------|
| [Chapter 1](./Chapter-01-Introduction.md) | **Introduction to Computer Networks** | Network Types, Topologies, OSI/TCP-IP Models |
| [Chapter 2](./Chapter-02-Physical-Layer.md) | **Physical Layer** | Transmission Media, Multiplexing, Switching, Shannon's Theorem |
| [Chapter 3](./Chapter-03-Data-Link-Layer.md) | **Data Link Layer** | Framing, Error Detection/Correction, Flow Control, MAC Protocols |
| [Chapter 4](./Chapter-04-Network-Layer.md) | **Network Layer** | IP Addressing, Subnetting, CIDR, Routing Algorithms |
| [Chapter 5](./Chapter-05-Transport-Layer.md) | **Transport Layer** | TCP, UDP, Congestion Control, Flow Control |
| [Chapter 6](./Chapter-06-Application-Layer.md) | **Application Layer** | DNS, HTTP, FTP, SMTP, DHCP |
| [Chapter 7](./Chapter-07-Network-Security.md) | **Network Security** | Cryptography, Firewalls, SSL/TLS, Digital Signatures |

---

## 🎯 How to Use This Material

1. **Sequential Study:** Follow chapters in order — each builds on the previous
2. **Formula Sheets:** Every chapter ends with a quick-reference formula sheet
3. **Trap Alerts:** Watch for ⚠️ **GATE TRAP** sections — these are common mistakes
4. **Practice NAT:** Numerical Answer Type questions require precision — note the decimal boundaries
5. **MSQ Strategy:** Multi-Select Questions require eliminating partial truths

---

## 📊 GATE Weightage Analysis

| Topic | Average Marks (Last 10 Years) | Question Types |
|-------|-------------------------------|----------------|
| Network Layer (IP, Subnetting, Routing) | 8-12 marks | NAT, MCQ, MSQ |
| Data Link Layer (Flow Control, MAC) | 6-10 marks | NAT, MCQ |
| Transport Layer (TCP/UDP) | 4-8 marks | MCQ, MSQ |
| Application Layer | 2-4 marks | MCQ |
| Physical Layer | 2-4 marks | NAT, MCQ |

---

## 🧠 The OSI Model at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 7: APPLICATION    │ HTTP, FTP, SMTP, DNS, DHCP      │
├─────────────────────────────────────────────────────────────┤
│  Layer 6: PRESENTATION   │ Encryption, Compression, Format │
├─────────────────────────────────────────────────────────────┤
│  Layer 5: SESSION        │ Session Management, Sync        │
├─────────────────────────────────────────────────────────────┤
│  Layer 4: TRANSPORT      │ TCP, UDP, Ports, Segments       │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: NETWORK        │ IP, Routing, Packets            │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: DATA LINK      │ MAC, Frames, Error Detection    │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: PHYSICAL       │ Bits, Cables, Signals           │
└─────────────────────────────────────────────────────────────┘
```

**Mnemonic:** "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way" (Physical → Application)

---

## 🔑 Master Formulas Quick Reference

### Transmission Time & Delays
$$T_{transmission} = \frac{L}{B}$$
$$T_{propagation} = \frac{d}{v}$$
$$T_{total} = T_{transmission} + T_{propagation} + T_{queuing} + T_{processing}$$

### Efficiency & Throughput
$$\eta = \frac{T_{transmission}}{T_{transmission} + 2 \times T_{propagation}} = \frac{1}{1 + 2a}$$

where $a = \frac{T_p}{T_t}$

### Shannon's Capacity Theorem
$$C = B \cdot \log_2(1 + SNR)$$

### Nyquist Rate
$$C = 2B \cdot \log_2(L)$$ (for $L$ signal levels, noiseless channel)

---

## ⚡ Quick Success Tips

1. **Always convert units first** — Most NAT errors come from unit mismatches
2. **Draw timing diagrams** — Essential for flow control and RTT problems
3. **Memorize port numbers** — HTTP(80), HTTPS(443), FTP(20,21), SSH(22), DNS(53), SMTP(25)
4. **Subnetting shortcuts** — Know powers of 2 up to $2^{16}$
5. **TCP vs UDP** — Know when each is used and why

---

## 📚 Recommended Practice Order

1. Start with **Chapter 4 (Network Layer)** — Highest weightage
2. Then **Chapter 3 (Data Link Layer)** — Second highest
3. Follow with **Chapter 5 (Transport Layer)**
4. Cover **Chapter 2 (Physical Layer)** for NAT questions
5. Complete **Chapter 1, 6, 7** for conceptual MCQs

---

## 🛠️ Problem Solving Techniques

### Technique 1: Unit Conversion First (The Golden Rule)

**Always convert all values to base units before calculation!**

| Given | Convert To |
|-------|------------|
| Kbps, Mbps, Gbps | bps (×10³, ×10⁶, ×10⁹) |
| KB, MB, GB | Bytes or Bits |
| km, m | meters |
| ms, μs | seconds |

**Example:**
```
Given: Bandwidth = 10 Mbps, Packet = 1 KB
Step 1: B = 10 × 10⁶ bps
Step 2: L = 1 × 10³ × 8 = 8000 bits
Step 3: Tₜ = L/B = 8000/(10×10⁶) = 0.8 ms
```

---

### Technique 2: The Delay Breakdown Method

For any transmission problem, break into components:

$$T_{total} = T_t + T_p + T_q + T_{proc}$$

| Delay | Formula | When to Use |
|-------|---------|-------------|
| Transmission ($T_t$) | $L/B$ | Always |
| Propagation ($T_p$) | $d/v$ | When distance given |
| Queuing ($T_q$) | Given/Assumed | Traffic analysis |
| Processing ($T_{proc}$) | Given/Assumed | Usually negligible |

**Pro Tip:** If propagation speed not given, assume:
- Copper/Fiber: $2 \times 10^8$ m/s
- Air/Satellite: $3 \times 10^8$ m/s

---

### Technique 3: Subnetting with Block Size

**Never do binary conversion for simple subnetting!**

**Step-by-Step:**
1. Find block size: $2^{32-prefix}$
2. List subnet boundaries: 0, block, 2×block, 3×block...
3. Find which block contains the IP

**Example:** Find network for 192.168.45.137/26
```
Block size = 2^(32-26) = 2^6 = 64
Boundaries in 4th octet: 0, 64, 128, 192
137 is between 128 and 192
Network: 192.168.45.128/26
Broadcast: 192.168.45.191 (128 + 64 - 1)
```

---

### Technique 4: Efficiency Formula Selection

| Protocol | Efficiency Formula |
|----------|-------------------|
| Stop-and-Wait | $\eta = \frac{1}{1 + 2a}$ |
| Sliding Window (W < 1+2a) | $\eta = \frac{W}{1 + 2a}$ |
| Sliding Window (W ≥ 1+2a) | $\eta = 1$ (100%) |
| Pure ALOHA | $S = Ge^{-2G}$, max 18.4% at G=0.5 |
| Slotted ALOHA | $S = Ge^{-G}$, max 36.8% at G=1 |
| CSMA/CD | $\eta \approx \frac{1}{1 + 5a}$ |

**Where:** $a = T_p/T_t$

---

### Technique 5: TCP Congestion Control State Tracking

**Draw a table to track cwnd over RTTs:**

| RTT | Event | ssthresh | cwnd | Phase |
|-----|-------|----------|------|-------|
| 0 | Start | 64 | 1 | Slow Start |
| 1 | - | 64 | 2 | Slow Start |
| 2 | - | 64 | 4 | Slow Start |
| ... | Timeout | cwnd/2 | 1 | Slow Start |
| ... | 3 Dup ACK | cwnd/2 | ssthresh+3 | Fast Recovery |

**Key Rules:**
- Slow Start: cwnd doubles each RTT
- Congestion Avoidance: cwnd += 1 each RTT
- Timeout: ssthresh = cwnd/2, cwnd = 1
- 3 Dup ACKs (Reno): ssthresh = cwnd/2, cwnd = ssthresh + 3

---

### Technique 6: CRC Calculation Shortcut

**Steps:**
1. Count generator bits → degree $r$ = bits - 1
2. Append $r$ zeros to data
3. XOR divide (no borrows!)
4. Remainder = CRC

**Verification:** (Data + CRC) ÷ Generator = Remainder 0

**Quick Check:** Generator with $(x+1)$ factor detects all odd-bit errors

---

### Technique 7: Hamming Code Position Trick

**Parity bit positions:** Powers of 2 (1, 2, 4, 8, 16...)

**Which positions does parity bit $P_i$ cover?**
- $P_1$: All positions with bit 0 set in binary (1, 3, 5, 7, 9...)
- $P_2$: All positions with bit 1 set in binary (2, 3, 6, 7, 10...)
- $P_4$: All positions with bit 2 set in binary (4, 5, 6, 7, 12...)

**Error Position:** Syndrome bits read as binary give error position!

---

### Technique 8: IP Fragmentation Calculation

**Given:** Packet size $P$, MTU, Header = 20 bytes

**Steps:**
1. Max data per fragment = MTU - 20
2. Data must be multiple of 8 (except last)
3. Number of fragments = $\lceil \frac{P-20}{MTU-20} \rceil$
4. Offset = (previous data bytes) / 8

**Example:** P = 4000 bytes, MTU = 1500
```
Data = 4000 - 20 = 3980 bytes
Max per fragment = 1500 - 20 = 1480 bytes
Fragment 1: 1480 bytes, offset = 0
Fragment 2: 1480 bytes, offset = 185 (1480/8)
Fragment 3: 1020 bytes, offset = 370 (2960/8)
```

---

### Technique 9: Window Size Determination

**For Go-Back-N:**
$$W_{max} = 2^n - 1$$

**For Selective Repeat:**
$$W_{max} = 2^{n-1}$$

Where $n$ = number of sequence number bits

**Minimum window for 100% efficiency:**
$$W_{min} = 1 + 2a = 1 + \frac{2 \times T_p}{T_t}$$

---

### Technique 10: The Elimination Strategy for MCQs

**For Multi-Select Questions (MSQs):**

1. **Eliminate extreme statements** — "always", "never" are often wrong
2. **Check layer boundaries** — Ensure protocol matches correct layer
3. **Verify port numbers** — Common trap with well-known ports
4. **Cross-check formulas** — Especially for efficiency and throughput

**Common Traps:**
- Confusing bit rate vs baud rate
- Forgetting -2 for usable hosts in subnetting
- Using wrong propagation speed (3×10⁸ vs 2×10⁸)
- Mixing up Go-Back-N and Selective Repeat window limits

---

### Technique 11: Drawing Timing Diagrams

For flow control and RTT problems, always draw:

```
Sender                                    Receiver
  │                                          │
  │─────── Packet 1 ────────────────────────►│
  │         (Tₜ)           (Tₚ)              │
  │                                          │
  │◄─────────── ACK 1 ───────────────────────│
  │                                          │
  ├─── RTT = 2×Tₚ + Tₜ(ack) ────────────────►│
```

**This helps visualize:**
- When ACK arrives
- Overlap of transmissions
- Pipeline effects

---

### Technique 12: Quick Sanity Checks

Before submitting any NAT answer:

| Check | What to Verify |
|-------|----------------|
| Units | Is answer in correct units (bps, ms, bytes)? |
| Magnitude | Does the number make sense? (e.g., efficiency ≤ 100%) |
| Boundary | Is it within valid range? (e.g., hosts = 2ⁿ - 2) |
| Precision | Correct decimal places for NAT? |

**Common Magnitude Checks:**
- Efficiency: 0 < η ≤ 1
- Throughput ≤ Bandwidth
- Propagation delay: typically ms for LAN, 10s of ms for WAN
- Window size: reasonable for given sequence bits

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**

✍️ *This material is continuously updated. Contributions are welcome!*
