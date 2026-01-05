# Module 11: Previous Year Questions Analysis | The Singularity

> **The Atomic Truth:** *Past patterns predict future questions*

---

## 11.1 GATE Question Distribution (2015-2024)

### **Topic-wise Analysis**

| Topic | Frequency | Marks | Question Types |
|-------|-----------|-------|----------------|
| **IP Addressing/Subnetting** | ⭐⭐⭐⭐⭐ | 2-4 | NAT, MCQ |
| **TCP/Congestion Control** | ⭐⭐⭐⭐⭐ | 2-4 | NAT, MSQ |
| **Flow Control (Sliding Window)** | ⭐⭐⭐⭐ | 2 | NAT |
| **Error Detection (CRC, Hamming)** | ⭐⭐⭐⭐ | 2 | NAT |
| **CSMA/CD, ALOHA** | ⭐⭐⭐ | 1-2 | MCQ |
| **Routing Algorithms** | ⭐⭐⭐ | 2 | NAT, MCQ |
| **Application Layer** | ⭐⭐ | 1 | MCQ |
| **Network Security** | ⭐⭐ | 1-2 | MCQ |

---

## 11.2 High-Frequency Question Types

### **Type 1: Subnetting & IP Addressing (Almost Every Year)**

#### **Pattern 1: Calculate hosts/subnets**
> "Given IP X.X.X.X/Y, find..."

**Example (GATE 2019):**
An IP router with a Maximum Transmission Unit (MTU) of 1500 bytes has an interface with an IP address of 192.168.10.1 with a subnet mask of 255.255.255.252. The maximum number of hosts that can be connected to this network is ______.

**Solution:**
- Mask 255.255.255.252 = /30
- Host bits = 2
- Hosts = $2^2 - 2 = 2$

---

#### **Pattern 2: Find network/broadcast address**
> "What is the network address for..."

**Example:**
Find the network and broadcast addresses for 172.16.45.123/20

**Solution:**
- /20 means 20 network bits
- Mask = 255.255.240.0
- Magic number = 256 - 240 = 16 (in 2nd octet)
- 45 ÷ 16 = 2.8... → Network at 32
- Network: 172.16.32.0
- Broadcast: 172.16.47.255

---

#### **Pattern 3: Route aggregation/supernetting**
> "Aggregate these routes..."

**Example:**
Aggregate: 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24

**Solution:**
- Find common prefix bits
- 192.168.0.x and 192.168.3.x differ in bits 6-7 of third octet
- Common prefix = 22 bits
- Aggregated: 192.168.0.0/22

---

### **Type 2: TCP Congestion Control (Very High Frequency)**

#### **Pattern 1: Calculate cwnd after N RTTs**
> "Starting with cwnd=1, ssthresh=X, find cwnd after N RTTs"

**Example (GATE 2016 Style):**
TCP connection: Initial cwnd = 1 KB, ssthresh = 32 KB. Find cwnd after 10 RTTs (no loss).

**Solution:**
Slow Start (cwnd < 32):
- RTT 0: 1 → RTT 1: 2 → RTT 2: 4 → RTT 3: 8 → RTT 4: 16 → RTT 5: 32

Congestion Avoidance (cwnd ≥ 32):
- RTT 6: 33 → RTT 7: 34 → RTT 8: 35 → RTT 9: 36 → RTT 10: 37

**Answer: 37 KB**

---

#### **Pattern 2: Behavior after packet loss**
> "After timeout/3 duplicate ACKs, what happens?"

**Key Rules:**
| Event | ssthresh | cwnd | Next Phase |
|-------|----------|------|------------|
| Timeout | cwnd/2 | 1 | Slow Start |
| 3 Dup ACKs (Reno) | cwnd/2 | ssthresh+3 | Fast Recovery |

---

#### **Pattern 3: Calculate throughput**
> "Given window size and RTT, find throughput"

$$\text{Throughput} = \frac{\text{Window Size}}{\text{RTT}}$$

---

### **Type 3: Error Detection (CRC, Hamming)**

#### **Pattern 1: CRC remainder calculation**
> "Find CRC for data D using generator G"

**Example (GATE 2018 Style):**
Data: 1101, Generator: 1011. Find CRC.

**Solution:**
1. Append 3 zeros (degree = 3): 1101000
2. XOR division:
```
      1110
     ─────
1011│1101000
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
         001 ← CRC
```
**Answer: 001**

---

#### **Pattern 2: Hamming code parity bits**
> "How many parity bits for M data bits?"

**Formula:** $2^r \geq m + r + 1$

**Example:** For 11 data bits:
- Try r=3: 8 ≥ 15? No
- Try r=4: 16 ≥ 16? Yes
**Answer: 4 parity bits**

---

### **Type 4: Flow Control Efficiency**

#### **Pattern 1: Stop-and-Wait efficiency**
> "Given propagation delay and transmission time, find efficiency"

$$\eta = \frac{1}{1 + 2a}$$

**Example (GATE Style):**
Link: 1 Mbps, Propagation delay: 5 ms, Frame: 1000 bytes

**Solution:**
- $T_{trans} = \frac{1000 \times 8}{10^6} = 8$ ms
- $a = \frac{5}{8} = 0.625$
- $\eta = \frac{1}{1 + 1.25} = \frac{1}{2.25} = 44.4\%$

---

#### **Pattern 2: Minimum window size for full utilization**
> "What window size is needed?"

**Condition:** $W \geq 1 + 2a$

---

### **Type 5: MAC Protocols**

#### **Pattern 1: ALOHA throughput**
> "Calculate throughput of pure/slotted ALOHA"

- Pure ALOHA max: 18.4%
- Slotted ALOHA max: 36.8%

---

#### **Pattern 2: CSMA/CD minimum frame size**
> "Given network parameters, find minimum frame"

$$Frame_{min} = 2 \times \frac{d}{v} \times B$$

---

### **Type 6: Application Layer**

#### **Pattern 1: HTTP download time**
> "Time to fetch page with multiple objects"

**Non-Persistent:**
$$T = n \times (2 \times RTT + T_{file})$$

**Persistent with Pipelining:**
$$T \approx 2 \times RTT + T_{all\_files}$$

---

#### **Pattern 2: DNS/DHCP process**
> "How many messages/queries?"

- DNS iterative from local: Usually 3 queries
- DHCP: 4 messages (DORA)

---

### **Type 7: Network Security**

#### **Pattern 1: RSA calculation**
> "Given p, q, e, find d or encrypt/decrypt"

**Example:**
$p=5$, $q=11$, $e=3$. Find $d$.

**Solution:**
- $n = 55$
- $\phi(n) = 4 \times 10 = 40$
- $3d \equiv 1 \pmod{40}$
- $d = 27$ (since $3 \times 27 = 81 = 2 \times 40 + 1$)

---

#### **Pattern 2: Keys required**
> "For N users, how many keys needed?"

- Symmetric: $\frac{n(n-1)}{2}$
- Asymmetric: $2n$

---

## 11.3 Common Traps and How to Avoid Them

### **Trap 1: Unit Confusion**

| Common Mistake | Correct Approach |
|----------------|------------------|
| Mixing Kbps and KBps | 1 Byte = 8 bits |
| Mixing ms and s | Convert consistently |
| Using 1024 instead of 1000 | Networking uses 1000 (1 Kbps = 1000 bps) |

---

### **Trap 2: Forgetting -2 in Host Calculation**

**Wrong:** Hosts = $2^h$
**Correct:** Hosts = $2^h - 2$ (subtract network and broadcast)

---

### **Trap 3: Window Size Constraints**

| Protocol | Constraint |
|----------|------------|
| Go-Back-N | $W \leq 2^n - 1$ |
| Selective Repeat | $W \leq 2^{n-1}$ |

**Trap:** Using wrong constraint for protocol

---

### **Trap 4: Fragment Offset Units**

**Wrong:** Offset in bytes
**Correct:** Offset in 8-byte units

**To convert:** Divide bytes by 8

---

### **Trap 5: Slow Start vs Congestion Avoidance**

**In Slow Start:** cwnd doubles each RTT
**In CA:** cwnd increases by 1 each RTT

**Trap:** Continuing exponential growth after ssthresh

---

### **Trap 6: Ethernet Frame Size**

| What they ask | What to answer |
|---------------|----------------|
| Minimum frame size | 64 bytes |
| Minimum data size | 46 bytes |
| Maximum frame size | 1518 bytes |
| Maximum data (MTU) | 1500 bytes |

**Trap:** Confusing frame size with data size

---

### **Trap 7: Shannon's SNR**

**Trap:** Using dB value directly
**Correct:** Convert to linear first

$$SNR_{linear} = 10^{SNR_{dB}/10}$$

---

### **Trap 8: CRC Generator Polynomial Degree**

**Trap:** Counting terms instead of highest power
**Correct:** Degree = highest power of polynomial

Example: $x^4 + x + 1$ → Degree = 4 → Append 4 zeros

---

## 11.4 Solved GATE Questions

### **Question 1 (GATE 2023 Style)**

A TCP connection is established with cwnd = 1 MSS and ssthresh = 64 MSS. After a timeout occurs when cwnd = 48 MSS, what is the value of cwnd and ssthresh?

**Solution:**
On Timeout:
- New ssthresh = cwnd/2 = 48/2 = 24 MSS
- New cwnd = 1 MSS

**Answer:** cwnd = 1 MSS, ssthresh = 24 MSS

---

### **Question 2 (GATE 2022 Style)**

A channel has bandwidth 10 MHz. If signal levels = 4 and SNR = 1023, find the maximum bit rate.

**Solution:**
Nyquist: $C = 2 \times 10 \times 10^6 \times \log_2 4 = 40$ Mbps

Shannon: $C = 10 \times 10^6 \times \log_2(1024) = 100$ Mbps

**Maximum = min(40, 100) = 40 Mbps**

---

### **Question 3 (GATE 2021 Style)**

In a /28 network, how many usable host addresses are available?

**Solution:**
/28 → 32 - 28 = 4 host bits
Usable hosts = $2^4 - 2 = 14$

**Answer: 14**

---

### **Question 4 (GATE 2020 Style)**

A router receives an IP packet of size 4000 bytes. The MTU of outgoing interface is 1500 bytes. How many fragments are created?

**Solution:**
Original data = 4000 - 20 = 3980 bytes
Per fragment = 1500 - 20 = 1480 bytes

Fragments = ⌈3980/1480⌉ = ⌈2.69⌉ = 3

**Answer: 3 fragments**

---

### **Question 5 (GATE 2019 Style)**

In ALOHA, if G = 0.5, what is the throughput of:
(a) Pure ALOHA
(b) Slotted ALOHA

**Solution:**
(a) Pure: $S = 0.5 \times e^{-1} = 0.5/e ≈ 0.184$ → 18.4%
(b) Slotted: $S = 0.5 \times e^{-0.5} = 0.5/\sqrt{e} ≈ 0.303$ → 30.3%

---

### **Question 6 (GATE 2018 Style)**

For RSA, if p=3, q=11, e=7, encrypt message M=5.

**Solution:**
- $n = 33$
- $\phi(n) = 2 \times 10 = 20$
- Verify: gcd(7, 20) = 1 ✓
- $C = 5^7 \mod 33$
- $5^2 = 25$, $5^4 = 625 \mod 33 = 625 - 18×33 = 31$
- $5^7 = 5^4 × 5^2 × 5 = 31 × 25 × 5 \mod 33$
- $= 775 × 5 \mod 33 = 13 × 5 = 65 \mod 33 = 32$

**Answer: C = 32**

---

## 11.5 MSQ Strategy (Multiple Select Questions)

### **Elimination Approach**

1. **Read all options first**
2. **Identify definitely wrong options** (eliminate)
3. **Identify definitely correct options** (include)
4. **Analyze remaining carefully**

### **Common MSQ Traps**

| Trap | Example |
|------|---------|
| "All of the above" disguised | When 3 options seem correct |
| Slight incorrectness | Almost correct but one word wrong |
| Scope confusion | Answer correct but not for this context |

---

## 11.6 NAT Answer Precision

### **When to Round**

| Context | Action |
|---------|--------|
| Efficiency percentage | Round to 2 decimal places |
| Integer counts | No rounding (exact) |
| Time calculations | Match question's precision |

### **Common NAT Answer Ranges**

| Topic | Typical Range |
|-------|---------------|
| Hosts in subnet | 2, 6, 14, 30, 62, 126, 254 |
| Hamming parity bits | 3, 4, 5, 6, 7 |
| ALOHA throughput | 0.18-0.37 |
| TCP cwnd values | Powers of 2, then linear |

---

## 11.7 Last-Minute Revision Checklist

### **Physical Layer**
- [ ] Nyquist: $C = 2B \log_2 L$
- [ ] Shannon: $C = B \log_2(1 + SNR)$
- [ ] SNR conversion: $10^{dB/10}$

### **Data Link Layer**
- [ ] Stop-Wait efficiency: $\frac{1}{1+2a}$
- [ ] Hamming: $2^r \geq m + r + 1$
- [ ] ALOHA: Pure 18.4%, Slotted 36.8%

### **Network Layer**
- [ ] Hosts: $2^h - 2$
- [ ] Fragment offset in 8-byte units
- [ ] Longest prefix match for routing

### **Transport Layer**
- [ ] TCP 3-way handshake
- [ ] Slow Start: doubles; CA: +1 per RTT
- [ ] Timeout: cwnd = 1

### **Application Layer**
- [ ] Port numbers (FTP: 20/21, HTTP: 80, DNS: 53)
- [ ] DHCP: DORA

### **Security**
- [ ] RSA: $n = pq$, $\phi = (p-1)(q-1)$
- [ ] Symmetric keys: $n(n-1)/2$

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**You are now equipped for Rank-1. Execute with precision.**

---

*"In the kingdom of networks, those who understand the protocols rule."*

**← Return to [Index](./README.md)**
