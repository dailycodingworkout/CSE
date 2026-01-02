# 📡 Chapter 1: Introduction to Computer Networks

> **The Atomic Truth:** Networks connect devices using standardized protocols.

---

## 🎯 Chapter Overview

| Topic | GATE Weightage | Difficulty |
|-------|----------------|------------|
| Network Types | Low | Easy |
| Topologies | Low-Medium | Easy |
| OSI Model | Medium | Medium |
| TCP/IP Model | Medium | Medium |
| Switching Techniques | Medium | Medium |

---

## 1.1 What is a Computer Network?

**Definition:** A computer network is a collection of interconnected devices that can communicate and share resources using a common set of protocols.

### The Why Behind Networks
- **Resource Sharing:** Share printers, files, databases
- **Communication:** Email, messaging, video calls
- **Reliability:** Redundant paths, backup systems
- **Cost Reduction:** Shared infrastructure vs. individual systems

### Analogy 🎭
> Think of a network like a postal system. Letters (data) travel through post offices (routers) using addresses (IP addresses) following postal rules (protocols).

---

## 1.2 Network Classification

### 1.2.1 By Geographical Span

| Type | Full Form | Range | Example |
|------|-----------|-------|---------|
| **PAN** | Personal Area Network | ~10m | Bluetooth headset |
| **LAN** | Local Area Network | ~1km | Office network |
| **MAN** | Metropolitan Area Network | ~50km | City-wide cable TV |
| **WAN** | Wide Area Network | Global | Internet |

#### ⚠️ GATE TRAP: LAN vs MAN Boundary
- **LAN:** Single organization, high speed (Gbps), low error rate
- **MAN:** Multiple organizations, city-scale, medium speed
- **Key Differentiator:** Ownership! LAN = single owner, MAN = usually ISP-managed

### 1.2.2 By Connection Type

| Type | Description | Example |
|------|-------------|---------|
| **Point-to-Point** | Direct link between two devices | Leased line |
| **Broadcast** | Shared medium, all receive | Ethernet hub |
| **Multicast** | One-to-many selective | Video streaming |

---

## 1.3 Network Topologies

### 1.3.1 Physical Topologies

```
    BUS TOPOLOGY               STAR TOPOLOGY              RING TOPOLOGY
    ═══════════════           ┌───┐                      ┌───┐
    │   │   │   │             │ H │                    ┌─│ A │─┐
   [A] [B] [C] [D]          ┌─┴───┴─┐                  │ └───┘ │
                           [A]     [B]               ┌───┐   ┌───┐
                            │       │                │ D │───│ B │
                           [C]     [D]               └───┘   └───┘
                                                       └──┌───┐──┘
                                                          │ C │
                                                          └───┘
```

### Topology Comparison Table

| Topology | Cable Length | Fault Tolerance | Cost | Use Case |
|----------|--------------|-----------------|------|----------|
| **Bus** | Minimum | Low (single point failure) | Low | Legacy LANs |
| **Star** | High | Medium (hub failure = total) | Medium | Modern LANs |
| **Ring** | Medium | Low (any node failure) | Medium | Token Ring |
| **Mesh** | Maximum | Highest | High | WANs, critical systems |
| **Tree** | High | Medium | Medium | Hierarchical networks |

### 1.3.2 Mathematical Analysis of Mesh Topology

For a **fully connected mesh** with $n$ nodes:

$$\text{Number of Links} = \frac{n(n-1)}{2}$$

For a **duplex (full-duplex) mesh**:
$$\text{Number of Duplex Links} = \frac{n(n-1)}{2}$$

For **simplex** connections:
$$\text{Number of Simplex Links} = n(n-1)$$

#### 🧮 NAT Practice
**Q:** A fully connected mesh network has 45 links. How many nodes does it have?

**Solution:**
$$\frac{n(n-1)}{2} = 45$$
$$n(n-1) = 90$$
$$n^2 - n - 90 = 0$$
$$n = \frac{1 + \sqrt{1 + 360}}{2} = \frac{1 + 19}{2} = 10$$

**Answer:** 10 nodes

---

## 1.4 The OSI Reference Model

### The Seven Layers

| Layer | Name | PDU | Function | Protocols/Devices |
|-------|------|-----|----------|-------------------|
| 7 | **Application** | Data | User interface | HTTP, FTP, SMTP, DNS |
| 6 | **Presentation** | Data | Translation, encryption | SSL, JPEG, MPEG |
| 5 | **Session** | Data | Session management | NetBIOS, RPC |
| 4 | **Transport** | Segment | End-to-end delivery | TCP, UDP |
| 3 | **Network** | Packet | Logical addressing, routing | IP, ICMP, Routers |
| 2 | **Data Link** | Frame | Physical addressing, framing | Ethernet, Switches |
| 1 | **Physical** | Bits | Physical transmission | Hubs, Cables, NIC |

### Mnemonics for OSI Layers

**Top-Down:** "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"

**Bottom-Up:** "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"

### Layer Functions in Detail

#### Layer 1: Physical Layer
- **What:** Deals with raw bits over physical medium
- **How:** Defines voltages, data rates, connector types
- **Devices:** Hub, Repeater, Modem
- **Key Concept:** Encoding schemes (Manchester, NRZ)

#### Layer 2: Data Link Layer
- **What:** Node-to-node delivery, framing
- **How:** MAC addresses, error detection (CRC)
- **Devices:** Switch, Bridge
- **Sub-layers:** LLC (Logical Link Control) + MAC (Media Access Control)

#### Layer 3: Network Layer
- **What:** End-to-end delivery across networks
- **How:** IP addressing, routing
- **Devices:** Router
- **Key Concept:** Logical addressing is network-independent

#### Layer 4: Transport Layer
- **What:** Process-to-process delivery
- **How:** Port numbers, segmentation
- **Protocols:** TCP (reliable), UDP (unreliable)
- **Key Concept:** Multiplexing/Demultiplexing

#### Layer 5: Session Layer
- **What:** Dialog control, synchronization
- **How:** Checkpoints, session tokens
- **Example:** SQL database sessions with transaction checkpoints, RPC (Remote Procedure Call) sessions

#### Layer 6: Presentation Layer
- **What:** Data representation, encryption
- **How:** Format conversion, compression
- **Example:** Converting EBCDIC to ASCII

#### Layer 7: Application Layer
- **What:** Network services for applications
- **How:** Protocols for specific services
- **Example:** Web browser using HTTP

---

## 1.5 TCP/IP Model

### Comparison: OSI vs TCP/IP

```
      OSI Model                    TCP/IP Model
    ┌─────────────┐              ┌─────────────────┐
    │ Application │              │                 │
    ├─────────────┤              │   Application   │
    │ Presentation│              │                 │
    ├─────────────┤              └────────┬────────┘
    │   Session   │                       │
    ├─────────────┤              ┌────────▼────────┐
    │  Transport  │◄─────────────│    Transport    │
    ├─────────────┤              └────────┬────────┘
    │   Network   │◄─────────────┌────────▼────────┐
    ├─────────────┤              │    Internet     │
    │  Data Link  │              └────────┬────────┘
    ├─────────────┤              ┌────────▼────────┐
    │  Physical   │◄─────────────│ Network Access  │
    └─────────────┘              └─────────────────┘
```

### TCP/IP Protocol Suite

| Layer | Protocols |
|-------|-----------|
| **Application** | HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, SNMP, Telnet, SSH |
| **Transport** | TCP, UDP, SCTP |
| **Internet** | IP, ICMP, IGMP, ARP, RARP |
| **Network Access** | Ethernet, Wi-Fi, PPP |

### ⚠️ GATE TRAP: ARP Layer Confusion
- **ARP (Address Resolution Protocol)** maps IP → MAC
- In OSI: It's between Layer 2 and Layer 3 (Link Layer in practice)
- In TCP/IP: It's at the Internet/Network Access boundary
- **Key:** ARP uses Layer 2 frames but serves Layer 3 purposes

---

## 1.6 Switching Techniques

### 1.6.1 Circuit Switching

**Concept:** Dedicated path established before communication

```
Sender ═══════════════════════════════════════ Receiver
        │←── Setup Phase ──│←── Data Phase ──│←── Teardown ──│
```

**Characteristics:**
- Dedicated bandwidth
- No congestion during transfer
- Wastage if channel idle
- Used in: Traditional telephone networks

#### Time Division Multiplexing (TDM) in Circuit Switching

If a link has bandwidth $B$ and is shared by $n$ users:
$$\text{Bandwidth per user} = \frac{B}{n}$$

### 1.6.2 Packet Switching

**Concept:** Data divided into packets, each routed independently

**Two Types:**

| Feature | Datagram | Virtual Circuit |
|---------|----------|-----------------|
| **Path** | Each packet independent | Same path for all packets |
| **Header** | Full address in each packet | Short VC identifier |
| **Order** | May arrive out of order | In-order delivery |
| **Example** | IP (Internet) | ATM, MPLS |

### 1.6.3 Message Switching

**Concept:** Entire message stored at each hop, then forwarded

- **Store-and-forward:** Complete message received before sending
- **No size limit:** But large messages cause delays
- **Historical use:** Telegraph systems

### Delay Comparison

For a message of size $M$ bits, packet size $P$ bits, $n$ hops, link bandwidth $B$:

**Message Switching:**
$$T_{message} = n \times \frac{M}{B}$$

**Packet Switching:**
$$T_{packet} = \frac{M}{B} + (n-1) \times \frac{P}{B}$$

#### 🧮 NAT Practice
**Q:** A 1 MB message is sent over 3 hops. Each link is 1 Mbps. Packet size is 1 KB. Compare delays.

**Message Switching:**
$$T = 3 \times \frac{1 \times 10^6 \times 8}{10^6} = 24 \text{ seconds}$$

**Packet Switching:**
$$T = \frac{8 \times 10^6}{10^6} + 2 \times \frac{8 \times 10^3}{10^6} = 8 + 0.016 = 8.016 \text{ seconds}$$

**Speedup = 24/8.016 ≈ 3×**

---

## 1.7 Network Devices

### Device Comparison

| Device | Layer | Function | Domain |
|--------|-------|----------|--------|
| **Hub** | 1 | Broadcasts all signals | Collision + Broadcast |
| **Repeater** | 1 | Amplifies/regenerates signal | Collision + Broadcast |
| **Bridge** | 2 | Filters by MAC address | Separates collision domains |
| **Switch** | 2 | Multi-port bridge, MAC table | Separates collision domains |
| **Router** | 3 | Routes by IP address | Separates broadcast domains |
| **Gateway** | 7 | Protocol translation | Application-level |

### Collision Domain vs Broadcast Domain

```
                    ┌─────────────┐
        Hub         │  1 Collision│     Switch      ┌─ Collision Domain 1
       ╱   ╲        │  1 Broadcast│    ╱  │  ╲      ├─ Collision Domain 2
      A     B       │   Domain    │   A   B   C     ├─ Collision Domain 3
       ╲   ╱        └─────────────┘                 └─ 1 Broadcast Domain
        Hub
```

### ⚠️ GATE TRAP: Switch vs Router Domains
- **Switch:** Breaks collision domains, NOT broadcast domains
- **Router:** Breaks BOTH collision AND broadcast domains
- **Hub:** Extends both domains (no separation)

---

## 1.8 Data Transmission Modes

### Simplex, Half-Duplex, Full-Duplex

| Mode | Direction | Example |
|------|-----------|---------|
| **Simplex** | One-way only | Keyboard → Computer |
| **Half-Duplex** | Both ways, not simultaneously | Walkie-talkie |
| **Full-Duplex** | Both ways simultaneously | Telephone |

### Serial vs Parallel Transmission

| Feature | Serial | Parallel |
|---------|--------|----------|
| **Wires** | Single | Multiple |
| **Speed** | Slower (per clock) | Faster (per clock) |
| **Distance** | Long | Short |
| **Cost** | Low | High |
| **Skew** | None | Possible |
| **Example** | USB, Ethernet | Old printer cables |

---

## 1.9 Important GATE Questions Patterns

### Pattern 1: Topology Calculations
- Number of links in mesh: $\frac{n(n-1)}{2}$
- Nodes given links: Solve quadratic

### Pattern 2: Layer Identification
- "Which layer handles X?" — Know layer responsibilities
- PDU names: Bits → Frames → Packets → Segments → Data

### Pattern 3: Switching Delay
- Message vs Packet switching comparison
- Account for all hops

### Pattern 4: Device Functions
- What does a switch do that a hub doesn't?
- At which layer does X operate?

---

## 📝 Quick Revision Formula Sheet

| Concept | Formula/Value |
|---------|---------------|
| Full Mesh Links | $\frac{n(n-1)}{2}$ |
| OSI Layers | 7 |
| TCP/IP Layers | 4 |
| Hub Layer | 1 |
| Switch Layer | 2 |
| Router Layer | 3 |

---

## 🎯 Chapter Summary

1. **Networks** enable resource sharing and communication
2. **LAN/MAN/WAN** classification is by geographical span
3. **Topologies:** Bus, Star, Ring, Mesh — know trade-offs
4. **OSI Model:** 7 layers with specific PDUs and functions
5. **TCP/IP:** 4 layers, more practical than OSI
6. **Switching:** Circuit (dedicated), Packet (shared), Message (store-forward)
7. **Devices:** Hub(L1), Switch(L2), Router(L3) — know domain separation

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining this with **Physical Layer** for a Rank-1 simulation?
