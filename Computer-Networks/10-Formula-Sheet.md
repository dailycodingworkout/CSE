# Module 10: Formula Sheet & Quick Revision | The Singularity

> **The Atomic Truth:** *Formulas are your weapons; deploy them with precision*

---

## 📊 Complete Formula Reference

### **Physical Layer Formulas**

#### **Nyquist Theorem (Noiseless Channel)**
$$C = 2B \log_2 L$$

| Variable | Meaning |
|----------|---------|
| $C$ | Maximum bit rate (bps) |
| $B$ | Bandwidth (Hz) |
| $L$ | Number of signal levels |

#### **Shannon's Theorem (Noisy Channel)**
$$C = B \log_2 (1 + SNR)$$

| Variable | Meaning |
|----------|---------|
| $C$ | Maximum capacity (bps) |
| $B$ | Bandwidth (Hz) |
| $SNR$ | Signal-to-Noise Ratio (linear) |

#### **SNR Conversion**
$$SNR_{linear} = 10^{SNR_{dB}/10}$$
$$SNR_{dB} = 10 \log_{10}(SNR_{linear})$$

#### **Bit Rate and Baud Rate**
$$\text{Bit Rate} = \text{Baud Rate} \times \log_2 L$$

#### **Propagation Speed**
| Medium | Speed |
|--------|-------|
| Vacuum/Air | $3 \times 10^8$ m/s |
| Copper/Fiber | $2 \times 10^8$ m/s |

---

### **Data Link Layer Formulas**

#### **Error Detection/Correction**

**Hamming Code:**
$$2^r \geq m + r + 1$$

| Variable | Meaning |
|----------|---------|
| $r$ | Parity (check) bits |
| $m$ | Data bits |

**Detection Capability:**
$$d_{min} \geq d + 1$$ (to detect $d$ errors)

**Correction Capability:**
$$d_{min} \geq 2t + 1$$ (to correct $t$ errors)

**Both:**
$$d_{min} \geq d + t + 1$$ (detect $d$, correct $t$)

#### **Flow Control Efficiency**

**Stop-and-Wait:**
$$\eta = \frac{1}{1 + 2a}$$

Where:
$$a = \frac{T_{prop}}{T_{trans}}$$

**Sliding Window:**
$$\eta = \begin{cases} 1 & \text{if } W \geq 1 + 2a \\ \frac{W}{1 + 2a} & \text{if } W < 1 + 2a \end{cases}$$

**Window Size Constraints:**
| Protocol | Maximum Window |
|----------|----------------|
| Go-Back-N | $W \leq 2^n - 1$ |
| Selective Repeat | $W \leq 2^{n-1}$ |

#### **ALOHA Throughput**

**Pure ALOHA:**
$$S = G \cdot e^{-2G}$$
$$S_{max} = \frac{1}{2e} \approx 0.184 = 18.4\%$$ at $G = 0.5$

**Slotted ALOHA:**
$$S = G \cdot e^{-G}$$
$$S_{max} = \frac{1}{e} \approx 0.368 = 36.8\%$$ at $G = 1$

#### **CSMA/CD Efficiency**
$$\eta = \frac{1}{1 + 5a}$$ (approximation)

#### **Minimum Frame Size (Ethernet)**
$$Frame_{min} = 2 \times \frac{d}{v} \times B$$

| Variable | Meaning |
|----------|---------|
| $d$ | Maximum distance |
| $v$ | Propagation speed |
| $B$ | Bandwidth |

---

### **Network Layer Formulas**

#### **Subnetting**

**Usable Hosts:**
$$\text{Hosts} = 2^h - 2$$

Where $h$ = host bits

**Number of Subnets:**
$$\text{Subnets} = 2^s$$

Where $s$ = subnet bits borrowed

**Magic Number:**
$$\text{Magic} = 256 - \text{Last non-zero octet of mask}$$

**Network Address:**
$$\text{Network} = \text{IP AND Mask}$$

**Broadcast Address:**
$$\text{Broadcast} = \text{Network OR (NOT Mask)}$$

#### **IP Header Size**
- Minimum: $5 \times 4 = 20$ bytes
- Maximum: $15 \times 4 = 60$ bytes

#### **Fragmentation**

**Number of Fragments:**
$$n = \left\lceil \frac{\text{Data Size}}{\text{MTU} - \text{Header Size}} \right\rceil$$

**Fragment Offset (in 8-byte units):**
$$\text{Offset} = \frac{\text{Bytes sent so far}}{8}$$

---

### **Transport Layer Formulas**

#### **Throughput**
$$\text{Throughput} = \frac{\text{Window Size}}{\text{RTT}}$$

#### **Bandwidth-Delay Product**
$$BDP = \text{Bandwidth} \times \text{RTT}$$

#### **TCP Congestion Control**

**Slow Start:**
After $n$ RTTs: $cwnd = 2^n \times \text{MSS}$

**Congestion Avoidance:**
After each RTT: $cwnd = cwnd + 1$

**On 3 Duplicate ACKs (Reno):**
- $ssthresh = \frac{cwnd}{2}$
- $cwnd = ssthresh + 3$

**On Timeout:**
- $ssthresh = \frac{cwnd}{2}$
- $cwnd = 1$ MSS

#### **TCP Throughput with Loss**
$$\text{Throughput} \approx \frac{MSS}{RTT \times \sqrt{p}}$$

Where $p$ = packet loss probability

---

### **Application Layer Formulas**

#### **HTTP Download Time**

**Non-Persistent (Sequential):**
$$T = n \times (2 \times RTT + T_{trans})$$

**Persistent (No Pipelining):**
$$T = 2 \times RTT + n \times (RTT + T_{trans})$$

**Persistent (With Pipelining):**
$$T \approx 2 \times RTT + RTT + n \times T_{trans}$$

---

### **Network Security Formulas**

#### **RSA Key Generation**

| Step | Formula |
|------|---------|
| $n$ | $p \times q$ |
| $\phi(n)$ | $(p-1)(q-1)$ |
| $e$ | $1 < e < \phi(n)$, $\gcd(e, \phi(n)) = 1$ |
| $d$ | $e \times d \equiv 1 \pmod{\phi(n)}$ |

#### **RSA Operations**
$$\text{Encrypt: } C = M^e \mod n$$
$$\text{Decrypt: } M = C^d \mod n$$

#### **Keys Required**

| System | Keys |
|--------|------|
| Symmetric | $\frac{n(n-1)}{2}$ |
| Asymmetric | $2n$ |

---

## 📋 Quick Reference Tables

### **Delay Calculations**

$$\text{Total Delay} = T_{prop} + T_{trans} + T_{queue} + T_{proc}$$

| Delay | Formula |
|-------|---------|
| Propagation | $\frac{\text{Distance}}{\text{Propagation Speed}}$ |
| Transmission | $\frac{\text{Data Size}}{\text{Bandwidth}}$ |

### **Protocol Ports**

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

### **IP Classes**

| Class | First Octet | Default Mask | Networks | Hosts/Net |
|-------|-------------|--------------|----------|-----------|
| A | 0-127 | /8 | 126 | 16,777,214 |
| B | 128-191 | /16 | 16,384 | 65,534 |
| C | 192-223 | /24 | 2,097,152 | 254 |
| D | 224-239 | N/A | Multicast | N/A |
| E | 240-255 | N/A | Reserved | N/A |

### **Private IP Ranges**

| Class | Range | CIDR |
|-------|-------|------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

### **Subnet Mask Reference**

| CIDR | Mask | Hosts |
|------|------|-------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

### **ICMP Types**

| Type | Message |
|------|---------|
| 0 | Echo Reply |
| 3 | Destination Unreachable |
| 5 | Redirect |
| 8 | Echo Request |
| 11 | Time Exceeded |

### **OSI Layers and PDUs**

| Layer | Name | PDU | Devices |
|-------|------|-----|---------|
| 7 | Application | Data | Gateway |
| 6 | Presentation | Data | Gateway |
| 5 | Session | Data | Gateway |
| 4 | Transport | Segment | Gateway |
| 3 | Network | Packet | Router |
| 2 | Data Link | Frame | Switch, Bridge |
| 1 | Physical | Bits | Hub, Repeater |

### **Routing Protocol Comparison**

| Protocol | Type | Algorithm | Metric | Transport |
|----------|------|-----------|--------|-----------|
| RIP | DV | Bellman-Ford | Hop (max 15) | UDP 520 |
| OSPF | LS | Dijkstra | Cost | IP 89 |
| BGP | PV | Best Path | Path attrs | TCP 179 |

### **Ethernet Parameters**

| Parameter | Value |
|-----------|-------|
| Min frame size | 64 bytes |
| Max frame size | 1518 bytes |
| Min data size | 46 bytes |
| Max data size (MTU) | 1500 bytes |
| MAC address size | 48 bits (6 bytes) |
| Preamble + SFD | 8 bytes |

---

## 🧠 Mnemonics Collection

### **OSI Layers**
- **Top-down:** "All People Seem To Need Data Processing"
- **Bottom-up:** "Please Do Not Throw Sausage Pizza Away"

### **Class A Range**
- "All Big Companies Deserve Excellence" (A, B, C, D, E)

### **DHCP Process**
- "DORA the Explorer" (Discover, Offer, Request, Acknowledge)

### **HTTP Status Codes**
- "1-Info, 2-Success, 3-Redirect, 4-Client Error, 5-Server Error"

### **ALOHA Throughput**
- "Pure = 18%, Slotted = 36% (double)"

### **Network Expansion (PAN to WAN)**
- "Please Let Me Win" (PAN, LAN, MAN, WAN)

---

## ⚡ Quick Calculation Shortcuts

### **Powers of 2**
| $2^n$ | Value |
|-------|-------|
| $2^0$ | 1 |
| $2^5$ | 32 |
| $2^6$ | 64 |
| $2^7$ | 128 |
| $2^8$ | 256 |
| $2^{10}$ | 1024 (≈1K) |
| $2^{16}$ | 65,536 |
| $2^{20}$ | ≈1M |
| $2^{32}$ | ≈4.3B |

### **Log Base 2**
| $\log_2 x$ | Value |
|------------|-------|
| $\log_2 2$ | 1 |
| $\log_2 4$ | 2 |
| $\log_2 8$ | 3 |
| $\log_2 16$ | 4 |
| $\log_2 32$ | 5 |
| $\log_2 64$ | 6 |
| $\log_2 128$ | 7 |
| $\log_2 256$ | 8 |
| $\log_2 1024$ | 10 |

### **Data Size Conversions**
| Unit | Bits | Bytes |
|------|------|-------|
| 1 Byte | 8 | 1 |
| 1 KB | 8,000 | 1,000 |
| 1 KiB | 8,192 | 1,024 |
| 1 MB | 8 × 10⁶ | 10⁶ |
| 1 Gb | 10⁹ | 1.25 × 10⁸ |

### **Time Conversions**
| Unit | Seconds |
|------|---------|
| 1 ms | 10⁻³ |
| 1 μs | 10⁻⁶ |
| 1 ns | 10⁻⁹ |

---

## 📝 Formula Application Checklist

Before solving any problem, ask:

1. ☐ **Units correct?** (bps vs Bps, ms vs s, km vs m)
2. ☐ **Which formula applies?** (Nyquist vs Shannon)
3. ☐ **Edge cases?** (n=0, n=1, maximum values)
4. ☐ **Ceiling/Floor needed?** (Fragmentation, subnets)
5. ☐ **Subtraction for reserved?** (Hosts: $2^h - 2$)

---

## 🎯 Topic-wise Formula Quick Reference

### **For Throughput/Efficiency Questions**
1. Calculate $T_{trans}$ and $T_{prop}$
2. Calculate $a = T_{prop}/T_{trans}$
3. Apply efficiency formula based on protocol

### **For Subnetting Questions**
1. Identify required hosts or subnets
2. Calculate bits needed: $2^h \geq \text{hosts} + 2$
3. Apply magic number technique

### **For Congestion Control Questions**
1. Track cwnd values RTT by RTT
2. Remember: Slow start doubles, CA adds 1
3. Apply event rules (3 dup ACKs, timeout)

### **For Security Questions**
1. For RSA: Calculate $n$, $\phi(n)$, then find $d$
2. For keys needed: Use appropriate formula
3. Remember encryption/decryption with correct key

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 11: Previous Year Questions Analysis →](./11-PYQ-Analysis.md)
