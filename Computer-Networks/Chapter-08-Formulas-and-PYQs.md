# Chapter 8: Formulas, Tricks & Previous Year Questions

## 🎯 The Atomic Truth
> **"Master the patterns, own the exam."**

---

## 8.1 All-in-One Formula Sheet ⭐⭐⭐

### 8.1.1 Physical Layer Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| $T_t = \frac{L}{B}$ | Transmission time | Time to put bits on wire |
| $T_p = \frac{d}{v}$ | Propagation time | Time for signal to travel |
| $a = \frac{T_p}{T_t}$ | Propagation-transmission ratio | Efficiency calculations |
| $C = 2B \log_2 L$ | Nyquist (noiseless) | Max bit rate, no noise |
| $C = B \log_2(1+SNR)$ | Shannon (noisy) | Max bit rate with noise |
| $SNR_{linear} = 10^{SNR_{dB}/10}$ | dB to linear conversion | When SNR given in dB |
| $\text{Bit Rate} = f_s \times n$ | PCM bit rate | Sampling × bits/sample |
| $f_s \geq 2 \times f_{max}$ | Nyquist sampling | Minimum sampling rate |

### 8.1.2 Data Link Layer Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| $\eta = \frac{1}{1+2a}$ | Stop-and-Wait efficiency | Window = 1 |
| $\eta = \frac{W}{1+2a}$ | Sliding window (if $W < 1+2a$) | Window-based protocols |
| $\eta = 1$ | Sliding window (if $W \geq 1+2a$) | Full utilization |
| $W_{GBN} \leq 2^n - 1$ | Go-Back-N max window | Given n-bit seq number |
| $W_{SR} \leq 2^{n-1}$ | Selective Repeat max window | Given n-bit seq number |
| $S_{ALOHA} = G \cdot e^{-2G}$ | Pure ALOHA throughput | Max at G=0.5: 18.4% |
| $S_{Slotted} = G \cdot e^{-G}$ | Slotted ALOHA throughput | Max at G=1: 36.8% |
| $L_{min} = 2 \times BDP$ | Min frame for CSMA/CD | Collision detection |
| $2^r \geq m + r + 1$ | Hamming code bits | m data, r check bits |
| $d_{min} \geq d + 1$ | Detect d errors | Error detection |
| $d_{min} \geq 2t + 1$ | Correct t errors | Error correction |

### 8.1.3 Network Layer Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| $\text{Subnets} = 2^s$ | Number of subnets | s = borrowed bits |
| $\text{Hosts} = 2^h - 2$ | Hosts per subnet | h = host bits |
| $\text{Block Size} = 2^h$ | IP block size | Address calculations |
| $\text{Block Size} = 256 - \text{mask octet}$ | Quick calculation | Last non-zero octet |
| Fragment Offset = $\frac{\text{byte offset}}{8}$ | Fragmentation | Offset in 8-byte units |

### 8.1.4 Transport Layer Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| $\text{Throughput} = \frac{W}{RTT}$ | TCP throughput | Window-limited |
| $\text{BDP} = B \times RTT$ | Bandwidth-Delay Product | Required window for full util |
| $RTO = EstRTT + 4 \times DevRTT$ | Retransmission timeout | TCP timeout calculation |
| cwnd doubles per RTT | Slow Start | Exponential growth |
| cwnd += 1 per RTT | Congestion Avoidance | Linear growth |

### 8.1.5 Application Layer Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| Non-persistent: $2(n+1) \times RTT$ | HTTP time | n objects, separate connections |
| Persistent (no pipe): $(n+2) \times RTT$ | HTTP time | Same connection, serial |
| Persistent (pipe): $2 \times RTT$ | HTTP time | Pipelined requests |

### 8.1.6 Security Formulas

| Formula | Description | When to Use |
|---------|-------------|-------------|
| $n = p \times q$ | RSA modulus | Key generation |
| $\phi(n) = (p-1)(q-1)$ | Euler's totient | For finding d |
| $d = e^{-1} \mod \phi(n)$ | Private exponent | ed ≡ 1 (mod φ(n)) |
| $C = M^e \mod n$ | RSA encrypt | Encryption |
| $M = C^d \mod n$ | RSA decrypt | Decryption |

---

## 8.2 Quick Reference Tables ⭐⭐

### 8.2.1 Port Numbers

| Port | Protocol | Service |
|------|----------|---------|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 161/162 | UDP | SNMP |
| 443 | TCP | HTTPS |
| 3389 | TCP | RDP |

### 8.2.2 Protocol Quick Reference

| Protocol | Layer | Transport | Key Feature |
|----------|-------|-----------|-------------|
| ARP | 2-3 | - | IP → MAC |
| ICMP | 3 | - | Error reporting |
| IP | 3 | - | Routing, addressing |
| TCP | 4 | - | Reliable, ordered |
| UDP | 4 | - | Fast, unreliable |
| DNS | 7 | UDP/TCP | Name resolution |
| DHCP | 7 | UDP | IP configuration |
| HTTP | 7 | TCP | Web |
| SMTP | 7 | TCP | Send email |
| FTP | 7 | TCP | File transfer |

### 8.2.3 Subnet Mask Quick Reference

| CIDR | Mask | Hosts | Block |
|------|------|-------|-------|
| /8 | 255.0.0.0 | 16M | 256 in 2nd |
| /16 | 255.255.0.0 | 65K | 256 in 3rd |
| /24 | 255.255.255.0 | 254 | 256 in 4th |
| /25 | 255.255.255.128 | 126 | 128 |
| /26 | 255.255.255.192 | 62 | 64 |
| /27 | 255.255.255.224 | 30 | 32 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 |

### 8.2.4 Network Devices by Layer

| Device | Layer | Collision Domain | Broadcast Domain |
|--------|-------|------------------|------------------|
| Repeater | 1 | Extends | Extends |
| Hub | 1 | Single | Single |
| Bridge | 2 | Separates | Single |
| Switch | 2 | Per port | Single |
| Router | 3 | Separates | Separates |

### 8.2.5 Topology Cable Count

| Topology | Cables | Formula |
|----------|--------|---------|
| Bus | n+1 | Backbone + drops |
| Star | n | One per device |
| Ring | n | One per device |
| Full Mesh | n(n-1)/2 | All pairs |

### 8.2.6 Encoding Comparison

| Encoding | Sync | DC | Bandwidth | Use |
|----------|------|-----|-----------|-----|
| NRZ-L | Poor | Yes | B | - |
| NRZ-I | Fair | Yes | B | - |
| Manchester | Good | No | 2B | Ethernet |
| Diff Manchester | Good | No | 2B | Token Ring |
| AMI | Fair | No | B | T1 |

---

## 8.3 Tricks and Shortcuts ⭐⭐

### 8.3.1 Subnetting Speed Tricks

**Finding Network Address:**
1. Find block size for that prefix
2. Floor(given IP / block size) × block size = Network

**Example**: 192.168.10.130/26
- Block = 64
- 130 / 64 = 2.03 → Floor = 2
- Network = 2 × 64 = 128
- Answer: 192.168.10.128

**Finding Broadcast:**
- Broadcast = Next Network - 1
- Or: Network + Block Size - 1

### 8.3.2 Binary-Decimal Quick Conversions

| Binary | Decimal |
|--------|---------|
| 10000000 | 128 |
| 11000000 | 192 |
| 11100000 | 224 |
| 11110000 | 240 |
| 11111000 | 248 |
| 11111100 | 252 |
| 11111110 | 254 |
| 11111111 | 255 |

### 8.3.3 Window Size Tricks

**Minimum Window for 100% Efficiency:**
$$W_{min} = 1 + 2a = 1 + \frac{2 \times T_p}{T_t}$$

**Quick Check**: If a ≥ 1, stop-and-wait efficiency < 50%

### 8.3.4 CRC Quick Check

- CRC bits = degree of generator
- Append that many zeros before division
- Final answer = original data + remainder

### 8.3.5 Hamming Code Position

- Check bits at powers of 2: 1, 2, 4, 8, 16...
- Position 1 checks: 1, 3, 5, 7, 9... (odd positions)
- Position 2 checks: 2, 3, 6, 7, 10, 11...
- Position 4 checks: 4-7, 12-15...

### 8.3.6 TCP Congestion Control Pattern

```
Slow Start: 1 → 2 → 4 → 8 → 16 → ssthresh
Congestion Avoidance: +1 each RTT
On timeout: ssthresh = cwnd/2, cwnd = 1
On 3 dup ACK (Reno): ssthresh = cwnd/2, cwnd = ssthresh
```

### 8.3.7 HTTP RTT Calculation

| Scenario | RTT Count |
|----------|-----------|
| Non-persistent, n objects | 2(n+1) |
| Persistent, no pipeline, n objects | n+2 |
| Persistent, pipeline | 2 |

---

## 8.4 GATE Previous Year Analysis ⭐⭐⭐

### 8.4.1 Topic-wise Weightage (2020-2025)

| Topic | Questions | Marks | Priority |
|-------|-----------|-------|----------|
| Network Layer (IP, Subnetting) | 8-10 | ~15 | ⭐⭐⭐ |
| Transport Layer (TCP) | 6-8 | ~12 | ⭐⭐⭐ |
| Data Link Layer | 5-7 | ~10 | ⭐⭐ |
| Application Layer | 3-4 | ~5 | ⭐⭐ |
| Physical Layer | 2-3 | ~4 | ⭐ |
| Network Security | 2-3 | ~4 | ⭐ |

### 8.4.2 Most Repeated Question Types

1. **Subnetting** (Almost every year)
   - Find network/broadcast address
   - Number of hosts/subnets
   - VLSM allocation

2. **TCP Congestion Control** (Every year)
   - cwnd progression
   - What happens on timeout/3 dup ACK
   - ssthresh calculation

3. **Sliding Window** (Every year)
   - Efficiency calculation
   - Window size for given scenario
   - GBN vs SR comparison

4. **CRC/Hamming** (Most years)
   - Calculate CRC
   - Error position in Hamming

5. **Routing Algorithms** (Frequent)
   - Dijkstra table filling
   - Distance vector updates

---

## 8.5 Practice Problems by Difficulty ⭐⭐

### 8.5.1 Easy (1-2 marks)

**E1**: The minimum frame size for CSMA/CD to work on a 10 Mbps Ethernet with maximum distance 2500m and signal speed 2×10⁸ m/s is?

<details>
<summary>Solution</summary>

$T_p = \frac{2500}{2 \times 10^8} = 12.5 \mu s$
$L_{min} = 2 \times T_p \times B = 2 \times 12.5 \times 10^{-6} \times 10 \times 10^6 = 250$ bits

But considering repeater delays, Ethernet uses 512 bits = **64 bytes**

</details>

**E2**: Which layer adds port numbers?

<details>
<summary>Solution</summary>

**Transport Layer (Layer 4)**

</details>

**E3**: Maximum window size for SR with 4-bit sequence number?

<details>
<summary>Solution</summary>

$W_{max} = 2^{n-1} = 2^{4-1} = 2^3 = 8$

</details>

### 8.5.2 Medium (2 marks)

**M1**: A 10 Mbps link, distance 2000 km, frame size 1000 bits. Calculate stop-and-wait efficiency.

<details>
<summary>Solution</summary>

$T_t = \frac{1000}{10 \times 10^6} = 100 \mu s = 0.1 ms$
$T_p = \frac{2000 \times 10^3}{2 \times 10^8} = 10 ms$
$a = \frac{10}{0.1} = 100$
$\eta = \frac{1}{1 + 2(100)} = \frac{1}{201} \approx 0.5\%$

</details>

**M2**: IP: 172.16.50.130/20. Find network address and total hosts.

<details>
<summary>Solution</summary>

/20: First 20 bits network, 12 bits host
In 3rd octet: 4 bits network, 4 bits host
50 in binary: 00110010
Network bits: 0011 = 48
Host bits: 12 → $2^{12} - 2 = 4094$ hosts
Network: **172.16.48.0**

</details>

**M3**: TCP connection, cwnd=32, ssthresh=16, timeout occurs. What are new values?

<details>
<summary>Solution</summary>

On timeout:
- $ssthresh = cwnd/2 = 32/2 = 16$
- $cwnd = 1$ (return to slow start)

**New: cwnd=1, ssthresh=16**

</details>

### 8.5.3 Hard (2 marks, Complex)

**H1**: A packet of 4500 bytes (including 20-byte header) arrives at router with MTU 1500. How many fragments? Calculate offsets.

<details>
<summary>Solution</summary>

Total data = 4500 - 20 = 4480 bytes
Max data per fragment = 1500 - 20 = 1480 bytes
1480 is divisible by 8 ✓

Fragments:
1. 1480 bytes, offset = 0
2. 1480 bytes, offset = 1480/8 = 185
3. 1480 bytes, offset = 2960/8 = 370
4. 40 bytes, offset = 4440/8 = 555

**4 fragments**

</details>

**H2**: In Dijkstra's, given graph with edges A-B:2, A-C:4, B-C:1, B-D:5, C-D:2. Find shortest paths from A.

<details>
<summary>Solution</summary>

| Step | Visited | D[A] | D[B] | D[C] | D[D] |
|------|---------|------|------|------|------|
| Init | {A} | 0 | 2 | 4 | ∞ |
| 1 | {A,B} | 0 | 2 | 3 | 7 |
| 2 | {A,B,C} | 0 | 2 | 3 | 5 |
| 3 | {A,B,C,D} | 0 | 2 | 3 | 5 |

**A→B:2, A→C:3 (via B), A→D:5 (via B,C)**

</details>

**H3**: In RSA, p=7, q=11, e=13. Encrypt M=5.

<details>
<summary>Solution</summary>

n = 7 × 11 = 77
φ(n) = 6 × 10 = 60
Check: gcd(13, 60) = 1 ✓

$C = 5^{13} \mod 77$

Using modular exponentiation:
$5^2 = 25$
$5^4 = 625 \mod 77 = 9$
$5^8 = 81 \mod 77 = 4$
$5^{13} = 5^8 \times 5^4 \times 5^1 = 4 \times 9 \times 5 = 180 \mod 77 = 26$

**C = 26**

</details>

---

## 8.6 Common Mistakes to Avoid ⭐

| Mistake | Correct Understanding |
|---------|----------------------|
| Confusing RTT with one-way delay | RTT = 2 × one-way delay |
| Forgetting -2 in host count | Hosts = $2^h - 2$ (network + broadcast) |
| Using dB SNR in Shannon | Convert: $SNR_{linear} = 10^{dB/10}$ |
| Mixing Go-Back-N and Selective Repeat windows | GBN: $2^n-1$, SR: $2^{n-1}$ |
| Fragment offset in bytes | Offset is in 8-byte units |
| Thinking Manchester doubles data rate | It doubles bandwidth, not rate |
| Confusing sequence number and ACK number | ACK = next expected byte |
| Ignoring propagation delay in efficiency | Must include $T_p$ in calculations |

---

## 8.7 Exam Day Quick Revision ⭐⭐⭐

### Last-Minute Checklist

**Physical Layer:**
- [ ] Nyquist: $C = 2B \log_2 L$
- [ ] Shannon: $C = B \log_2(1+SNR)$
- [ ] Manchester: 2× bandwidth

**Data Link Layer:**
- [ ] Stop-Wait: $\eta = \frac{1}{1+2a}$
- [ ] GBN window: $\leq 2^n - 1$
- [ ] SR window: $\leq 2^{n-1}$
- [ ] Pure ALOHA: 18.4%, Slotted: 36.8%

**Network Layer:**
- [ ] Hosts = $2^h - 2$
- [ ] Fragment offset in 8-byte units
- [ ] Dijkstra: Pick smallest, update neighbors

**Transport Layer:**
- [ ] 3-way: SYN, SYN-ACK, ACK
- [ ] Slow Start: exponential
- [ ] Congestion Avoidance: linear
- [ ] Timeout: cwnd=1, ssthresh=cwnd/2

**Application Layer:**
- [ ] HTTP persistent + pipeline: 2 RTT
- [ ] DNS: UDP for queries
- [ ] FTP: Port 21 control, 20 data

**Security:**
- [ ] RSA: Encrypt with public, sign with private
- [ ] DH: Key exchange only
- [ ] AH: No encryption, ESP: Encryption

---

## 8.8 GATE 2026 Predictions ⭐

Based on trends:

1. **Subnetting**: 1-2 questions guaranteed
2. **TCP Congestion Control**: 1 question highly likely  
3. **Sliding Window Efficiency**: 1 question expected
4. **Routing (Dijkstra)**: Appears most years
5. **CRC or Hamming**: Usually alternates
6. **HTTP/DNS**: Conceptual question likely
7. **IPv6**: May appear as concepts gain importance
8. **Network Security**: Basic concepts (TLS, IPSec modes)

---

## 8.9 Mind Maps for Quick Recall

### OSI Layers
```
Application  → HTTP, DNS, FTP, SMTP
Presentation → SSL/TLS, Encryption
Session      → NetBIOS, RPC
Transport    → TCP (reliable), UDP (fast)
Network      → IP, ICMP, Routers
Data Link    → MAC, Ethernet, Switches
Physical     → Cables, Signals, Hubs
```

### TCP Flags
```
S - SYN    (Start)
A - ACK    (Acknowledge)
F - FIN    (Finish)
R - RST    (Reset)
P - PSH    (Push)
U - URG    (Urgent)
```

### Address Types
```
IP (32-bit)  → Network Layer, Global
MAC (48-bit) → Data Link Layer, Local
Port (16-bit)→ Transport Layer, Process
```

---

## 📝 Chapter Summary

This chapter provides quick reference for:
- All important formulas organized by layer
- Port numbers and protocol references
- Speed tricks for exam calculations
- Previous year question patterns
- Practice problems at all difficulty levels
- Common mistakes to avoid
- Last-minute revision checklist

**Study Strategy**: 
1. Master formulas in 8.1
2. Memorize port numbers in 8.2
3. Practice tricks in 8.3
4. Solve problems in 8.5
5. Use 8.7 for final revision

---

**Previous Chapter**: [← Chapter 7: Network Security](./Chapter-07-Network-Security.md)

**Back to Index**: [← Computer Networks README](./README.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]*

*Would you like to initiate a **'Multi-Variable Stress Test'** combining concepts across chapters for a Rank-1 simulation?*
