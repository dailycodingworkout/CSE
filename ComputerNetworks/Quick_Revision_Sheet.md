# 🔥 Computer Networks - Quick Revision Sheet

## One-Page Summary for Last-Minute Revision

---

## 1️⃣ OSI Model

```
Layer    Name           PDU        Device      Protocol Examples
─────────────────────────────────────────────────────────────────
  7      Application    Data       -           HTTP, FTP, DNS, SMTP
  6      Presentation   Data       -           SSL/TLS, JPEG, MPEG
  5      Session        Data       -           NetBIOS, RPC
  4      Transport      Segment    -           TCP, UDP
  3      Network        Packet     Router      IP, ICMP, OSPF
  2      Data Link      Frame      Switch      Ethernet, PPP
  1      Physical       Bits       Hub         RS-232, DSL
```

**🧠 Mnemonic**: "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"

---

## 2️⃣ Critical Formulas

### Channel Capacity
```
Nyquist (no noise):   C = 2B × log₂(L)
Shannon (with noise): C = B × log₂(1 + SNR)
Use MINIMUM when both given!

SNR conversion:       SNR_linear = 10^(SNR_dB/10)
```

### Delays
```
Transmission Delay:   Tt = L / B    (L=bits, B=bps)
Propagation Delay:    Tp = D / V    (D=distance, V=velocity)
a = Tp / Tt

Velocity: Copper cable ≈ 2×10⁸ m/s, Light in vacuum ≈ 3×10⁸ m/s, Fiber ≈ 2×10⁸ m/s
```

### Sliding Window Efficiency
```
Stop-and-Wait:        η = 1 / (1 + 2a)
Sliding Window:       η = min(1, W / (1 + 2a))

Window Size Limits:
  GBN:  W ≤ 2^m - 1
  SR:   W ≤ 2^(m-1)
```

### ALOHA Throughput
```
Pure ALOHA:           S = G × e^(-2G), max = 18.4% at G=0.5
Slotted ALOHA:        S = G × e^(-G), max = 36.8% at G=1.0
```

### CSMA/CD
```
Min Frame Size:       L_min = 2 × Tp × B = RTT × B
Ethernet Min:         64 bytes (512 bits)
```

### Subnetting
```
Hosts per subnet:     2^(host bits) - 2 = 2^(32-prefix) - 2
Subnets created:      2^(borrowed bits)
Block size:           256 - mask_last_octet (or 2^host_bits)
```

### TCP Congestion Control
```
Slow Start:           cwnd doubles every RTT (exponential)
Congestion Avoid:     cwnd += 1 MSS per RTT (linear)

On Timeout:           ssthresh = cwnd/2, cwnd = 1 MSS
On 3 Dup ACKs:        ssthresh = cwnd/2, cwnd = ssthresh (Reno)

Throughput:           Window / RTT
BDP:                  Bandwidth × RTT
```

### Fragmentation
```
Max data/fragment:    MTU - 20 (must be multiple of 8)
Fragment offset:      bytes_before / 8
Each fragment adds:   20-byte IP header
```

---

## 3️⃣ Key Comparisons

### GBN vs SR
| Feature | GBN | SR |
|---------|-----|-----|
| Sender Window | N | N |
| Receiver Window | 1 | N |
| Retransmit | From error | Only lost |
| Max W | 2^m - 1 | 2^(m-1) |

### TCP vs UDP
| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Yes (3-way) | No |
| Reliable | Yes | No |
| Header | 20+ bytes | 8 bytes |
| Flow Control | Yes | No |

### Distance Vector vs Link State
| DV (RIP) | LS (OSPF) |
|----------|-----------|
| Bellman-Ford | Dijkstra |
| Knows neighbors | Knows full topology |
| Periodic updates | Event-triggered |
| Count-to-infinity | No loops |

### IPv4 vs IPv6
| IPv4 | IPv6 |
|------|------|
| 32 bits | 128 bits |
| Header: 20-60 bytes | Header: 40 bytes fixed |
| Checksum: Yes | Checksum: No |
| Router fragments | Only end hosts fragment |

---

## 4️⃣ Port Numbers (Must Know)

```
20/21 - FTP (Data/Control)    110 - POP3
22    - SSH                    143 - IMAP
23    - Telnet                 443 - HTTPS
25    - SMTP                   520 - RIP (UDP)
53    - DNS (TCP/UDP)
67/68 - DHCP (Server/Client)
80    - HTTP
```

---

## 5️⃣ Protocol Numbers (IP Header)

```
1  - ICMP        17 - UDP
6  - TCP         89 - OSPF
```

---

## 6️⃣ Classful IP Ranges

```
Class A: 1-126     (0 and 127 reserved)    /8
Class B: 128-191                            /16
Class C: 192-223                            /24
Class D: 224-239   (Multicast)
Class E: 240-255   (Reserved)

Private Ranges:
10.0.0.0/8      172.16.0.0/12     192.168.0.0/16
```

---

## 7️⃣ Subnet Quick Reference

```
/24 → 256 IPs, 254 hosts     /28 → 16 IPs, 14 hosts
/25 → 128 IPs, 126 hosts     /29 → 8 IPs, 6 hosts
/26 → 64 IPs, 62 hosts       /30 → 4 IPs, 2 hosts
/27 → 32 IPs, 30 hosts       /31 → 2 IPs, 0 hosts (P2P)
```

---

## 8️⃣ Key Processes

### TCP 3-Way Handshake
```
Client → SYN, Seq=x         → Server
Client ← SYN+ACK, Seq=y, Ack=x+1 ← Server
Client → ACK, Ack=y+1       → Server
```

### DHCP (DORA)
```
Client → DISCOVER (broadcast)
Client ← OFFER
Client → REQUEST (broadcast)
Client ← ACK
```

### DNS Resolution
```
Client → Local DNS → Root → TLD → Authoritative
```

---

## 9️⃣ Line Coding Quick Ref

```
Manchester: Transition in MIDDLE of every bit
            1 = High→Low, 0 = Low→High
            Self-clocking, used in Ethernet
            Bandwidth = 2 × NRZ

NRZ-L:      1 = High, 0 = Low
NRZ-I:      Transition on 1, no change on 0
```

---

## 🔟 Security Essentials

### RSA
```
n = p × q
φ(n) = (p-1)(q-1)
e × d ≡ 1 (mod φ(n))

Encrypt: C = M^e mod n
Decrypt: M = C^d mod n
```

### Digital Signature
```
Sign:   Hash → Encrypt with PRIVATE key
Verify: Decrypt with PUBLIC key → Compare hash
```

### TLS Handshake (Simplified)
```
ClientHello → ServerHello + Certificate
→ KeyExchange → ChangeCipherSpec → Finished
```

---

## ⚡ Common Mistakes to Avoid

1. **Subnetting**: Don't forget -2 for network and broadcast
2. **Efficiency**: a = Tp/Tt (not Tt/Tp)
3. **Window Size**: GBN = 2^m - 1, SR = 2^(m-1) (not same!)
4. **Shannon**: Use linear SNR, not dB directly
5. **Fragmentation**: Each fragment gets new header (20 bytes)
6. **ALOHA**: Pure max = 18.4%, Slotted = 36.8%
7. **TCP**: Slow start doubles, CA adds 1
8. **RSA**: φ(n) = (p-1)(q-1), not p×q

---

## 📊 Numerical Problem Patterns

### Pattern 1: Channel Capacity
```
Given: B = 4 MHz, SNR = 255
C = 4×10⁶ × log₂(256) = 4×10⁶ × 8 = 32 Mbps
```

### Pattern 2: Sliding Window
```
Given: Tt = 1ms, Tp = 10ms, find efficiency for W = 7
a = 10/1 = 10
η = 7 / (1 + 20) = 7/21 = 33.3%
```

### Pattern 3: Subnetting
```
Given: 192.168.1.0/26
Hosts = 2^6 - 2 = 62
Block size = 64
Subnets: .0, .64, .128, .192
```

### Pattern 4: TCP cwnd
```
Given: ssthresh = 8, trace cwnd
RTT: 1→2→4→8(SS)→9→10→11(CA)...
```

---

## 🎯 Last-Minute Tips

1. **Read questions carefully** - units matter!
2. **Draw diagrams** for sliding window problems
3. **Double-check** subnet calculations
4. **Remember edge cases** in protocols
5. **Time management** - don't spend too long on one question

---

**Good luck! You've got this! 🚀**
