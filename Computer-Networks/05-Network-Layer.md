# Module 5: Network Layer | The Singularity

> **The Atomic Truth:** *Network Layer = Logical addressing + Routing*

---

## 5.1 Network Layer Overview

### **Core Responsibilities**
1. **Logical Addressing** — IP addresses
2. **Routing** — Path selection between networks
3. **Packet Forwarding** — Moving packets hop-by-hop
4. **Fragmentation & Reassembly** — Handling MTU differences

### **The Analogy 💡**
Network Layer is the **GPS navigation system**:
- Knows your destination address (IP)
- Calculates the best route
- Guides you through each junction (router)
- Doesn't care about the local roads (that's Data Link)

---

## 5.2 IPv4 Addressing

### **IPv4 Address Structure**

```
32 bits total
┌─────────────────────┬─────────────────────┐
│   Network ID        │      Host ID         │
│   (Network portion) │   (Host portion)     │
└─────────────────────┴─────────────────────┘

Example: 192.168.1.100
Binary:  11000000.10101000.00000001.01100100
```

### **Dotted Decimal Notation**
- 4 octets separated by dots
- Each octet: 0-255 (8 bits)
- Total: 32 bits = $2^{32}$ ≈ 4.3 billion addresses

### **5.2.1 Classful Addressing (Legacy)**

| Class | First Bits | Range | Default Mask | Networks | Hosts/Network |
|-------|------------|-------|--------------|----------|---------------|
| A | 0xxx | 0-127 | /8 (255.0.0.0) | 128 | 16,777,214 |
| B | 10xx | 128-191 | /16 (255.255.0.0) | 16,384 | 65,534 |
| C | 110x | 192-223 | /24 (255.255.255.0) | 2,097,152 | 254 |
| D | 1110 | 224-239 | N/A | Multicast | N/A |
| E | 1111 | 240-255 | N/A | Reserved | N/A |

### **The Mnemonic 🧠**
> **"All Big Companies Deserve Excellence"**
> A (0-127) → B (128-191) → C (192-223) → D (224-239) → E (240-255)

### **GATE Trap Alert ⚠️**

**Class A Range:**
- Technically 0.0.0.0 to 127.255.255.255
- But 0.x.x.x (default network) and 127.x.x.x (loopback) are reserved
- **Usable Class A networks: 1-126** (126 networks, not 128)

**Hosts per Network Formula:**
$$\text{Usable Hosts} = 2^{h} - 2$$

Where $h$ = host bits
- Subtract 2: Network address (all 0s) and Broadcast address (all 1s)

---

## 5.3 Subnetting | The GATE Goldmine 🔑

### **The Atomic Truth:** *Subnetting = Borrowing host bits for network*

### **Subnet Mask**

| CIDR | Subnet Mask | Host Bits | Usable Hosts |
|------|-------------|-----------|--------------|
| /24 | 255.255.255.0 | 8 | 254 |
| /25 | 255.255.255.128 | 7 | 126 |
| /26 | 255.255.255.192 | 6 | 62 |
| /27 | 255.255.255.224 | 5 | 30 |
| /28 | 255.255.255.240 | 4 | 14 |
| /29 | 255.255.255.248 | 3 | 6 |
| /30 | 255.255.255.252 | 2 | 2 |
| /31 | 255.255.255.254 | 1 | 2* (point-to-point) |
| /32 | 255.255.255.255 | 0 | 1 (host route) |

### **The Magic Number Technique 🧙**

**Magic Number = 256 - Last non-zero octet of subnet mask**

**Example:** Subnet mask 255.255.255.224
- Magic Number = 256 - 224 = 32
- Subnets start at: 0, 32, 64, 96, 128, 160, 192, 224

### **Subnet Calculation Master Formula**

Given IP and subnet mask, find:

1. **Network Address:** IP AND Subnet Mask
2. **Broadcast Address:** Network Address OR (NOT Subnet Mask)
3. **First Host:** Network Address + 1
4. **Last Host:** Broadcast Address - 1
5. **Number of Hosts:** $2^{host\_bits} - 2$

### **Step-by-Step Example**

**Problem:** Find network details for 192.168.10.75/26

**Step 1:** Identify subnet mask
- /26 = 255.255.255.192
- Host bits = 32 - 26 = 6

**Step 2:** Find Magic Number
- Magic = 256 - 192 = 64
- Subnets: 0, 64, 128, 192

**Step 3:** Identify subnet for 75
- 75 falls in range 64-127 (subnet starting at 64)

**Step 4:** Calculate addresses
- **Network:** 192.168.10.64
- **Broadcast:** 192.168.10.127 (64 + 64 - 1)
- **First Host:** 192.168.10.65
- **Last Host:** 192.168.10.126
- **Usable Hosts:** $2^6 - 2 = 62$

### **Binary AND Method (For Complex Cases)**

```
IP:        192.168.10.75  = 11000000.10101000.00001010.01001011
Mask:      255.255.255.192 = 11111111.11111111.11111111.11000000
           ────────────────────────────────────────────────────
Network:   192.168.10.64  = 11000000.10101000.00001010.01000000
```

---

## 5.4 CIDR (Classless Inter-Domain Routing)

### **The Concept**
- Abolishes class boundaries
- Variable-length subnet masks (VLSM)
- Enables route aggregation (supernetting)

### **Supernetting (Route Aggregation)**

**Problem:** Combine multiple networks into one route

**Example:** Aggregate these networks:
- 192.168.0.0/24
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

**Solution:**
```
192.168.0.0  = 11000000.10101000.00000000.00000000
192.168.1.0  = 11000000.10101000.00000001.00000000
192.168.2.0  = 11000000.10101000.00000010.00000000
192.168.3.0  = 11000000.10101000.00000011.00000000
                                 ^^^^^^^^
                           Common prefix: 22 bits
```

**Aggregated Route:** 192.168.0.0/22

### **CIDR Notation Examples**

| CIDR | Addresses | Use Case |
|------|-----------|----------|
| /32 | 1 | Host route |
| /30 | 4 (2 usable) | Point-to-point link |
| /24 | 256 | Small network |
| /16 | 65,536 | Medium org |
| /8 | 16,777,216 | Large org/ISP |
| /0 | All (default) | Default route |

---

## 5.5 Special IP Addresses

### **Reserved Addresses**

| Address/Range | Purpose |
|---------------|---------|
| 0.0.0.0/8 | "This" network |
| 10.0.0.0/8 | Private (Class A) |
| 127.0.0.0/8 | Loopback |
| 169.254.0.0/16 | Link-local (APIPA) |
| 172.16.0.0/12 | Private (Class B range) |
| 192.168.0.0/16 | Private (Class C range) |
| 224.0.0.0/4 | Multicast |
| 255.255.255.255 | Limited broadcast |

### **Private Address Ranges (RFC 1918)**

| Class | Range | CIDR | Addresses |
|-------|-------|------|-----------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 | 16,777,216 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 | 1,048,576 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 | 65,536 |

### **GATE Trap Alert ⚠️**

**172.16.0.0/12 covers 172.16.0.0 to 172.31.255.255**
- NOT 172.16.0.0/16 (that's only 172.16.x.x)
- The /12 means first 12 bits fixed: 10101100.0001xxxx

---

## 5.6 IPv4 Header

### **Header Format**

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│Version│  IHL  │    ToS/DSCP   │         Total Length          │
├───────────────┼───────────────┼───────────────────────────────┤
│         Identification        │Flags│    Fragment Offset      │
├───────────────┼───────────────┼───────────────────────────────┤
│      TTL      │   Protocol    │       Header Checksum         │
├───────────────┴───────────────┴───────────────────────────────┤
│                     Source IP Address                         │
├───────────────────────────────────────────────────────────────┤
│                   Destination IP Address                      │
├───────────────────────────────────────────────────────────────┤
│                    Options (if IHL > 5)                       │
└───────────────────────────────────────────────────────────────┘
```

### **Key Fields**

| Field | Size | Purpose |
|-------|------|---------|
| Version | 4 bits | 4 for IPv4 |
| IHL | 4 bits | Header length in 32-bit words (min 5, max 15) |
| Total Length | 16 bits | Total packet size (header + data) |
| TTL | 8 bits | Hop limit (decrements at each router) |
| Protocol | 8 bits | Upper layer protocol (TCP=6, UDP=17, ICMP=1) |
| Identification | 16 bits | Fragment identification |
| Flags | 3 bits | DF (Don't Fragment), MF (More Fragments) |
| Fragment Offset | 13 bits | Position in original datagram (in 8-byte units) |

### **Header Size Calculation**

- **Minimum header:** 5 × 4 = 20 bytes
- **Maximum header:** 15 × 4 = 60 bytes
- **Maximum options:** 40 bytes

### **Maximum Packet Size**
- Total Length field = 16 bits
- Max size = $2^{16} - 1 = 65,535$ bytes

---

## 5.7 IP Fragmentation

### **When Fragmentation Occurs**
- Packet size > MTU (Maximum Transmission Unit) of next link
- Router fragments; destination reassembles

### **Fragmentation Fields**

| Field | Purpose |
|-------|---------|
| **Identification** | Same for all fragments of original packet |
| **DF flag** | If set, don't fragment (send ICMP error instead) |
| **MF flag** | More fragments follow (0 for last fragment) |
| **Fragment Offset** | Position in 8-byte units |

### **Fragmentation Example**

**Problem:** A 4000-byte IP packet (20 byte header, 3980 data) must traverse a link with MTU = 1500 bytes.

**Solution:**

Each fragment can carry: 1500 - 20 = 1480 bytes of data
1480 ÷ 8 = 185 (divisible by 8 ✓)

| Fragment | Data Size | Offset | MF |
|----------|-----------|--------|-----|
| 1 | 1480 | 0 | 1 |
| 2 | 1480 | 185 (1480/8) | 1 |
| 3 | 1020 | 370 (2960/8) | 0 |

Total fragments: 3

### **GATE NAT Precision Lock 🔒**

**Fragment Offset Calculation:**
- Measured in 8-byte units
- Offset = (bytes sent so far) ÷ 8

**Finding Number of Fragments:**
$$n = \lceil \frac{\text{Data Size}}{\text{MTU} - \text{Header}} \rceil$$

**Constraint:** Each fragment (except last) must have data size divisible by 8

---

## 5.8 ICMP (Internet Control Message Protocol)

### **Purpose**
- Error reporting
- Network diagnostics
- NOT for data transfer

### **ICMP Message Types**

| Type | Code | Message | Use |
|------|------|---------|-----|
| 0 | 0 | Echo Reply | Ping response |
| 3 | 0 | Dest Unreachable (Network) | No route |
| 3 | 1 | Dest Unreachable (Host) | Host down |
| 3 | 3 | Dest Unreachable (Port) | Port closed |
| 3 | 4 | Fragmentation Needed | DF set, MTU exceeded |
| 4 | 0 | Source Quench | Congestion (deprecated) |
| 5 | 0-3 | Redirect | Better route available |
| 8 | 0 | Echo Request | Ping |
| 11 | 0 | Time Exceeded (TTL) | Traceroute |
| 11 | 1 | Fragment Reassembly Timeout | |

### **Common ICMP Uses**

| Tool | ICMP Messages Used |
|------|-------------------|
| **ping** | Echo Request (8) / Echo Reply (0) |
| **traceroute** | Echo Request + Time Exceeded (11) |
| **Path MTU Discovery** | Dest Unreachable - Fragmentation Needed (3,4) |

---

## 5.9 NAT (Network Address Translation)

### **Types of NAT**

| Type | Description | Port Translation |
|------|-------------|------------------|
| **Static NAT** | 1:1 mapping (public to private) | No |
| **Dynamic NAT** | Pool of public IPs | No |
| **PAT/NAPT** | Many:1 using ports | Yes |

### **PAT (Port Address Translation)**

```
Internal                        NAT Router                    External
─────────                       ──────────                    ────────
10.0.0.1:5000 ────┐         ┌──────────────┐
                  ├────────>│ 203.0.113.1  │──────────────> Internet
10.0.0.2:6000 ────┘         │    :10001    │
                            │    :10002    │
                            └──────────────┘

NAT Table:
┌──────────────┬───────────────────┐
│ Internal      │ External          │
├──────────────┼───────────────────┤
│ 10.0.0.1:5000 │ 203.0.113.1:10001 │
│ 10.0.0.2:6000 │ 203.0.113.1:10002 │
└──────────────┴───────────────────┘
```

### **NAT Advantages & Disadvantages**

**Advantages:**
- ✅ Conserves public IP addresses
- ✅ Provides security (hides internal structure)
- ✅ Allows network renumbering without external changes

**Disadvantages:**
- ❌ Breaks end-to-end connectivity
- ❌ Complicates peer-to-peer applications
- ❌ Issues with protocols embedding IP in data (FTP, SIP)

---

## 5.10 ARP (Address Resolution Protocol)

### **Purpose**
Maps IP addresses to MAC addresses (Layer 3 → Layer 2)

### **ARP Process**

```
1. Host A wants to send to IP 192.168.1.5
2. A checks ARP cache - not found
3. A broadcasts ARP Request: "Who has 192.168.1.5?"
4. Host B (192.168.1.5) responds: "192.168.1.5 is at AA:BB:CC:DD:EE:FF"
5. A caches mapping and sends frame to that MAC
```

### **ARP Packet Fields**

| Field | Size | Description |
|-------|------|-------------|
| Hardware Type | 2 bytes | 1 = Ethernet |
| Protocol Type | 2 bytes | 0x0800 = IPv4 |
| Hardware Len | 1 byte | 6 (MAC length) |
| Protocol Len | 1 byte | 4 (IPv4 length) |
| Operation | 2 bytes | 1 = Request, 2 = Reply |
| Sender MAC | 6 bytes | |
| Sender IP | 4 bytes | |
| Target MAC | 6 bytes | (0 in request) |
| Target IP | 4 bytes | |

### **Related Protocols**

| Protocol | Direction | Purpose |
|----------|-----------|---------|
| ARP | IP → MAC | Normal resolution |
| RARP | MAC → IP | Diskless workstations (obsolete) |
| Proxy ARP | Router answers for other network | |
| Gratuitous ARP | Self-announcement | Duplicate IP detection |

---

## 5.11 Routing Fundamentals

### **Routing Table Structure**

| Destination | Mask | Next Hop | Interface | Metric |
|-------------|------|----------|-----------|--------|
| 10.0.0.0 | /8 | 192.168.1.1 | eth0 | 1 |
| 0.0.0.0 | /0 | 192.168.1.254 | eth0 | 10 |

### **Longest Prefix Match**

When multiple routes match, use the one with the **longest prefix** (most specific).

**Example:** Destination = 10.1.2.3
- Route 1: 10.0.0.0/8 (matches 8 bits)
- Route 2: 10.1.0.0/16 (matches 16 bits)
- Route 3: 10.1.2.0/24 (matches 24 bits) ← **Selected**

### **Static vs Dynamic Routing**

| Aspect | Static | Dynamic |
|--------|--------|---------|
| Configuration | Manual | Automatic |
| Scalability | Poor | Good |
| Convergence | Instant | Protocol-dependent |
| Overhead | None | CPU, bandwidth |
| Use case | Small networks | Enterprise/Internet |

---

## 5.12 Routing Algorithms

### **Distance Vector (Bellman-Ford)**

**Concept:** Share routing table with neighbors periodically

**Characteristics:**
- Each router knows only neighbors
- Slow convergence
- Count-to-infinity problem
- Examples: RIP, IGRP

**Bellman-Ford Equation:**
$$D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$$

### **Link State (Dijkstra)**

**Concept:** Each router knows entire topology

**Characteristics:**
- Floods link-state advertisements (LSAs)
- Fast convergence
- More CPU/memory intensive
- Examples: OSPF, IS-IS

**Dijkstra's Algorithm:**
1. Start at source, set distance = 0
2. Mark unvisited neighbors
3. Update distances via current node
4. Move to unvisited node with smallest distance
5. Repeat until all visited

### **Comparison**

| Feature | Distance Vector | Link State |
|---------|-----------------|------------|
| Knowledge | Neighbors only | Full topology |
| Updates | Periodic + triggered | Event-driven |
| Convergence | Slow | Fast |
| Loop prevention | Split horizon, poison reverse | SPF algorithm |
| CPU | Low | High |
| Memory | Low | High |
| Examples | RIP, EIGRP | OSPF, IS-IS |

---

## 5.13 Key Formulas Summary

### **Subnetting**

| Calculation | Formula |
|-------------|---------|
| Usable hosts | $2^h - 2$ |
| Subnets | $2^s$ |
| Magic number | $256 - \text{last octet of mask}$ |
| Network address | IP AND Mask |
| Broadcast | Network OR (NOT Mask) |

### **Fragmentation**

| Calculation | Formula |
|-------------|---------|
| Fragments needed | $\lceil \frac{\text{Data}}{MTU - Header} \rceil$ |
| Fragment offset | $\frac{\text{bytes sent so far}}{8}$ |

---

## 5.14 Solved Examples

### **Example 1: Subnetting**

**Problem:** An organization has 192.168.1.0/24 and needs 6 subnets with at least 20 hosts each. Design the subnets.

**Solution:**

Need 6 subnets → borrow 3 bits (2³ = 8 subnets)
Need 20 hosts → need 5 host bits (2⁵ - 2 = 30 hosts)

Verification: 3 + 5 = 8 bits in last octet ✓

New mask: /27 (255.255.255.224)
Magic number: 256 - 224 = 32

Subnets:
| Subnet | Network | First Host | Last Host | Broadcast |
|--------|---------|------------|-----------|-----------|
| 0 | .0 | .1 | .30 | .31 |
| 1 | .32 | .33 | .62 | .63 |
| 2 | .64 | .65 | .94 | .95 |
| 3 | .96 | .97 | .126 | .127 |
| 4 | .128 | .129 | .158 | .159 |
| 5 | .160 | .161 | .190 | .191 |

---

### **Example 2: Fragmentation**

**Problem:** An IP datagram of 4500 bytes (including 20-byte header) needs fragmentation. MTU = 1500 bytes. Calculate the details of each fragment.

**Solution:**

Original data = 4500 - 20 = 4480 bytes
Max data per fragment = 1500 - 20 = 1480 bytes

Fragments needed = ⌈4480/1480⌉ = 4

| Fragment | Data | Offset (bytes) | Offset (units) | MF |
|----------|------|----------------|----------------|-----|
| 1 | 1480 | 0 | 0 | 1 |
| 2 | 1480 | 1480 | 185 | 1 |
| 3 | 1480 | 2960 | 370 | 1 |
| 4 | 40 | 4440 | 555 | 0 |

Each fragment total: 1480 + 20 = 1500 bytes (except last: 60 bytes)

---

### **Example 3: Route Aggregation**

**Problem:** Aggregate these routes:
- 200.20.0.0/24
- 200.20.1.0/24
- 200.20.2.0/24
- 200.20.3.0/24

**Solution:**
```
200.20.0.0 = 11001000.00010100.000000|00.00000000
200.20.1.0 = 11001000.00010100.000000|01.00000000
200.20.2.0 = 11001000.00010100.000000|10.00000000
200.20.3.0 = 11001000.00010100.000000|11.00000000
                                    ↑
                          Common: 22 bits
```

**Aggregated: 200.20.0.0/22**

---

## 5.15 Practice Problems

**Q1.** [NAT] How many hosts can be addressed in a /26 network?

<details>
<summary>Answer</summary>
Host bits = 32 - 26 = 6
Usable hosts = $2^6 - 2 = \boxed{62}$
</details>

---

**Q2.** What is the broadcast address for 172.16.45.123/20?

<details>
<summary>Answer</summary>
Magic = 256 - 240 = 16 (in 2nd octet)
Network = 172.16.32.0
Broadcast = 172.16.47.255

Answer: **172.16.47.255**
</details>

---

**Q3.** How many fragments for a 5000-byte IP packet with MTU 1500?

<details>
<summary>Answer</summary>
Data = 5000 - 20 = 4980 bytes
Per fragment = 1500 - 20 = 1480 bytes
Fragments = ⌈4980/1480⌉ = $\boxed{4}$
</details>

---

## 5.16 The 5-Second Snap-Check ✅

1. ☐ Class A: 0-127, Class B: 128-191, Class C: 192-223
2. ☐ Usable hosts = $2^h - 2$
3. ☐ Longest prefix match for routing
4. ☐ Fragment offset in 8-byte units
5. ☐ ARP: IP → MAC, RARP: MAC → IP
6. ☐ TTL decrements at each router

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 6: Routing Protocols →](./06-Routing-Protocols.md)
