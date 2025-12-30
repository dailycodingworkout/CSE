# Chapter 1: Introduction to Computer Networks

## 🎯 GATE/ESE Weightage: 2-4 marks (Conceptual Foundation)

---

## 1.1 What is a Computer Network?

**Definition**: A collection of autonomous computers interconnected by a single technology to exchange data and share resources.

**Key Word Analysis**:
- **Autonomous**: Each computer operates independently (no master-slave)
- **Interconnected**: Physical/wireless connection exists
- **Single Technology**: Common protocol/medium for communication

### Why Networks Exist?
| Purpose | Example |
|---------|---------|
| Resource Sharing | Printers, storage, computational power |
| Communication | Email, video conferencing |
| Reliability | Redundant systems, backup |
| Cost Savings | Share expensive hardware |
| Scalability | Add nodes without redesigning |

---

## 1.2 Network Classification

### By Size (🎯 GATE Favorite)

```
┌─────────────────────────────────────────────────────────────────┐
│  PAN ⊂ LAN ⊂ MAN ⊂ WAN ⊂ Internet                              │
│  (1m)  (1km)  (10km) (1000+km) (Global)                         │
└─────────────────────────────────────────────────────────────────┘
```

| Network | Range | Example | Speed | Owner |
|---------|-------|---------|-------|-------|
| **PAN** | ~1m | Bluetooth headset | 1-3 Mbps | Personal |
| **LAN** | ~1km | Office network | 100 Mbps-10 Gbps | Single org |
| **MAN** | ~10km | City cable TV | 10-100 Mbps | ISP/City |
| **WAN** | 1000+ km | Internet backbone | Variable | Multiple |

**🧠 Trick**: "**P**lease **L**et **M**e **W**ork" = PAN → LAN → MAN → WAN

### By Topology

```
       BUS                    STAR                    RING
    ═══╤═══╤═══╤═══        ┌──────┐              ┌───┐
       │   │   │           │ HUB/ │              │   │
      [A] [B] [C]      [A]─┤SWITCH├─[C]      [A]─┤   ├─[B]
                           └──┬───┘              │   │
                              │                  └─┬─┘
                             [B]                  [C]

       MESH                   TREE                  HYBRID
    [A]───[B]              [ROOT]                (Combination)
     │\ /│                 /    \
     │ X │              [A]    [B]
     │/ \│              / \    / \
    [C]───[D]         [1][2] [3][4]
```

| Topology | Advantages | Disadvantages | Use Case |
|----------|------------|---------------|----------|
| **Bus** | Simple, cheap | Single point of failure, collision | Small LANs |
| **Star** | Easy troubleshoot, isolated failures | Hub failure = total failure | Modern LANs |
| **Ring** | Equal access, no collision | One failure breaks ring | Token Ring |
| **Mesh** | Highly reliable, redundant | Expensive, complex | WANs, Internet |
| **Tree** | Hierarchical, scalable | Root failure critical | Large organizations |

**🎯 GATE Formula**: For **Full Mesh** with n nodes:
- **Links** = n(n-1)/2 (undirected) or n(n-1) (directed)
- **I/O ports per device** = n-1

**Example**: 10 devices in full mesh = 10×9/2 = **45 cables**

---

## 1.3 OSI Reference Model (🎯 MOST IMPORTANT)

### The 7 Layers

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 7: APPLICATION    │ End-user interface               │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 6: PRESENTATION   │ Data formatting, encryption      │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 5: SESSION        │ Session management               │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 4: TRANSPORT      │ End-to-end delivery, reliability │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 3: NETWORK        │ Logical addressing, routing      │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 2: DATA LINK      │ Framing, MAC, error detection    │
├─────────────────────────┼───────────────────────────────────┤
│ Layer 1: PHYSICAL       │ Bits on wire, signaling          │
└─────────────────────────┴───────────────────────────────────┘
```

**🧠 Mnemonic (Top→Down)**: "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"
**🧠 Mnemonic (Bottom→Up)**: "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"

### Layer Details with PDU (Protocol Data Unit)

| Layer | PDU Name | Devices | Protocols | Function |
|-------|----------|---------|-----------|----------|
| 7-Application | Data | - | HTTP, FTP, SMTP, DNS | User interface |
| 6-Presentation | Data | - | JPEG, MPEG, SSL/TLS | Translation, encryption |
| 5-Session | Data | - | NetBIOS, RPC | Dialog control |
| 4-Transport | **Segment** | - | TCP, UDP | Segmentation, flow control |
| 3-Network | **Packet** | Router | IP, ICMP, ARP | Routing, logical addressing |
| 2-Data Link | **Frame** | Switch, Bridge | Ethernet, PPP | Framing, MAC addressing |
| 1-Physical | **Bits** | Hub, Repeater | RS-232, DSL | Physical transmission |

**🎯 PDU Trick**: "**D**o **S**ome **P**eople **F**ear **B**irds?"
- **D**ata → **S**egment → **P**acket → **F**rame → **B**its

### Encapsulation Process

```
APPLICATION DATA
        ↓
┌──────────────────────────────┐
│ [L4 Header] + DATA = SEGMENT │  ← TCP/UDP adds port numbers
└──────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ [L3 Header] + SEGMENT = PACKET      │  ← IP adds source/dest IP
└─────────────────────────────────────┘
        ↓
┌────────────────────────────────────────────┐
│ [L2 Header] + PACKET + [Trailer] = FRAME   │  ← MAC addresses + CRC
└────────────────────────────────────────────┘
        ↓
┌────────────────────────────────────────────────┐
│ FRAME converted to BITS for transmission       │
└────────────────────────────────────────────────┘
```

### 🎯 GATE Edge Cases

1. **Which layer handles encryption?**
   - Presentation (SSL conceptually) but practically Application layer in TCP/IP

2. **Router vs Switch vs Hub**:
   - Hub: Layer 1 (broadcasts to all)
   - Switch: Layer 2 (uses MAC table)
   - Router: Layer 3 (uses routing table)

3. **Where does error detection happen?**
   - Data Link (CRC) and Transport (Checksum) BOTH!

---

## 1.4 TCP/IP Model (Internet Model)

### Comparison with OSI

```
        OSI Model                    TCP/IP Model
    ┌─────────────┐              ┌─────────────────┐
    │ Application │──────────────│                 │
    ├─────────────┤              │   Application   │
    │Presentation │──────────────│                 │
    ├─────────────┤              ├─────────────────┤
    │   Session   │──────────────│                 │
    ├─────────────┤              ├─────────────────┤
    │  Transport  │──────────────│    Transport    │
    ├─────────────┤              ├─────────────────┤
    │   Network   │──────────────│    Internet     │
    ├─────────────┤              ├─────────────────┤
    │  Data Link  │──────────────│                 │
    ├─────────────┤              │ Network Access  │
    │  Physical   │──────────────│                 │
    └─────────────┘              └─────────────────┘
```

### TCP/IP Protocol Suite

```
┌────────────────────────────────────────────────────────────┐
│ APPLICATION: HTTP, FTP, SMTP, DNS, SNMP, Telnet, SSH       │
├────────────────────────────────────────────────────────────┤
│ TRANSPORT: TCP (reliable) | UDP (fast, unreliable)         │
├────────────────────────────────────────────────────────────┤
│ INTERNET: IP, ICMP, ARP, RARP, IGMP                        │
├────────────────────────────────────────────────────────────┤
│ NETWORK ACCESS: Ethernet, Wi-Fi, Token Ring, FDDI          │
└────────────────────────────────────────────────────────────┘
```

### OSI vs TCP/IP: Key Differences

| Aspect | OSI | TCP/IP |
|--------|-----|--------|
| Layers | 7 | 4 (or 5) |
| Developed by | ISO | DoD/DARPA |
| Approach | Theoretical first | Practical first |
| Session/Presentation | Separate layers | Merged in Application |
| Protocols | Protocol independent | Protocol dependent |
| Usage | Reference model | Actual implementation |

**🎯 GATE Insight**: TCP/IP was "protocols first, model later" while OSI was "model first, protocols later"

---

## 1.5 Transmission Modes

### Simplex, Half-Duplex, Full-Duplex

```
SIMPLEX (Unidirectional):
    [A] ──────────────→ [B]
    Example: Keyboard → Computer, TV broadcast

HALF-DUPLEX (Bidirectional, one at a time):
    [A] ←─────────────→ [B]
    Example: Walkie-talkie, HTTP 1.0

FULL-DUPLEX (Bidirectional, simultaneous):
    [A] ←═════════════→ [B]
    Example: Telephone, Ethernet switch
```

| Mode | Direction | Bandwidth Use | Example |
|------|-----------|---------------|---------|
| Simplex | One-way only | Full in one direction | Broadcast TV |
| Half-Duplex | Both ways, not simultaneous | Alternating | Walkie-talkie |
| Full-Duplex | Both ways simultaneously | Full both directions | Phone call |

---

## 1.6 Switching Techniques

### Circuit Switching

```
[A]════════════════════════════════════════[B]
     Dedicated path for entire communication

Phases: 1. Connection Setup → 2. Data Transfer → 3. Teardown
```

**Characteristics**:
- Dedicated path (guaranteed bandwidth)
- Connection-oriented
- Fixed delay
- Wasteful if data is bursty
- Example: PSTN (telephone network)

**🎯 Formula**: Transmission Time = Setup Time + (Message Size / Bandwidth) + Propagation Delay

### Packet Switching

```
     ┌───────┐
[A]──┤Router1├──[Router2]──[B]
     └───┬───┘      │
         └────[Router3]────┘

Packets can take different paths!
```

**Two Types**:

| Aspect | Datagram | Virtual Circuit |
|--------|----------|-----------------|
| Connection | Connectionless | Connection-oriented |
| Path | Different for each packet | Same for all packets |
| Order | May arrive out of order | Arrives in order |
| Overhead | Per-packet header | Setup time |
| Example | IP (Internet) | ATM, MPLS |

### Message Switching (Store-and-Forward)

```
[A]─→[Switch1]─→[Switch2]─→[B]
     (stores     (stores
      entire      entire
      message)    message)
```

- Entire message stored before forwarding
- No real-time communication
- Used in email (historically)

### 🎯 GATE Comparison

| Feature | Circuit | Packet (Datagram) | Packet (VC) |
|---------|---------|-------------------|-------------|
| Setup | Required | Not required | Required |
| Bandwidth | Dedicated | Shared | Shared |
| Congestion | Blocked at setup | Possible during transfer | Possible |
| Reliability | High | Low | Medium |
| Order | Guaranteed | Not guaranteed | Guaranteed |

---

## 1.7 Network Devices

### Device Comparison (🎯 GATE Favorite)

```
Layer 1: Hub, Repeater ──→ Work with BITS
Layer 2: Bridge, Switch ──→ Work with FRAMES (MAC addresses)
Layer 3: Router ──→ Work with PACKETS (IP addresses)
Layer 4+: Gateway ──→ Protocol conversion
```

| Device | Layer | Uses | Function | Collision Domain | Broadcast Domain |
|--------|-------|------|----------|------------------|------------------|
| **Repeater** | 1 | Signal | Amplify/regenerate | Extends | Extends |
| **Hub** | 1 | Signal | Multi-port repeater | Single (shared) | Single |
| **Bridge** | 2 | MAC | Connect 2 LANs | Separates | Single |
| **Switch** | 2 | MAC | Multi-port bridge | Separates (per port) | Single |
| **Router** | 3 | IP | Connect networks | Separates | Separates |
| **Gateway** | 4-7 | All | Protocol converter | Separates | Separates |

### 🎯 Collision Domain vs Broadcast Domain

**Collision Domain**: Area where frame collisions can occur (CSMA/CD)
**Broadcast Domain**: Area where broadcast frames are forwarded

**Example Problem**:
```
        [Router]
           │
    ┌──────┴──────┐
 [Switch1]     [Switch2]
  │  │  │       │  │
  H  H  H       H  H
```

- **Collision Domains**: 5 (each switch port = 1 CD)
- **Broadcast Domains**: 2 (router separates)

---

## 1.8 Types of Casting

```
UNICAST (1:1):        [A] ──────────→ [B]
BROADCAST (1:All):    [A] ══════════→ [All nodes in network]
MULTICAST (1:Many):   [A] ──────────→ [B, C, D] (subscribed group)
ANYCAST (1:Nearest):  [A] ──────────→ [Nearest B] (same IP, multiple locations)
```

| Type | Target | Address Example | Use Case |
|------|--------|-----------------|----------|
| Unicast | Single host | 192.168.1.5 | Normal communication |
| Broadcast | All hosts | 255.255.255.255 | ARP, DHCP discover |
| Multicast | Group | 224.0.0.0 - 239.255.255.255 | Video streaming |
| Anycast | Nearest one | Same IP on multiple servers | DNS root servers, CDN |

---

## 1.9 Delays in Networks (🎯 VERY IMPORTANT)

### Types of Delays

```
Total Delay = Transmission + Propagation + Processing + Queuing

┌────────────┐   Transmission   ┌────────────┐  Propagation   ┌────────────┐
│   Sender   │ ═══════════════> │   Medium   │ ─────────────> │  Receiver  │
└────────────┘                  └────────────┘                └────────────┘
      ↑                               ↑                             ↑
   Processing                      Queuing                      Processing
```

### Formulas (🎯 MEMORIZE)

| Delay Type | Formula | Depends On |
|------------|---------|------------|
| **Transmission Delay (Tt)** | L / B | Packet size (L), Bandwidth (B) |
| **Propagation Delay (Tp)** | D / V | Distance (D), Medium velocity (V) |
| **Processing Delay** | ~constant | Router/switch processing |
| **Queuing Delay** | Variable | Network congestion |

**Where**:
- L = Packet length (bits)
- B = Bandwidth (bits/second)
- D = Distance (meters)
- V = Propagation speed (~2×10⁸ m/s for copper, ~3×10⁸ m/s for fiber/air)

### 🎯 Key Insight: Tt vs Tp

**Transmission Delay**: Time to push all bits onto the wire (like filling a pipe)
**Propagation Delay**: Time for first bit to reach destination (like water speed in pipe)

**Analogy**: 
- Transmission = Time to put all cars on highway
- Propagation = Time for first car to reach destination

### Efficiency & Utilization

```
Efficiency (η) = Useful time / Total cycle time
               = Tt / (Tt + 2×Tp)     [for Stop-and-Wait]

Bandwidth-Delay Product = Bandwidth × Propagation Delay
                        = Amount of data "in flight"
```

### 🎯 Classic GATE Problem Pattern

**Given**: L = 1000 bits, B = 1 Mbps, D = 2000 km, V = 2×10⁸ m/s

**Solution**:
- Tt = 1000 / 10⁶ = 1 ms (time to put packet on wire)
- Tp = 2×10⁶ / (2×10⁸) = 10 ms (time for signal to travel)
- If RTT needed: RTT = 2 × Tp = 20 ms

---

## 1.10 Throughput vs Bandwidth

| Term | Definition | Unit | Analogy |
|------|------------|------|---------|
| **Bandwidth** | Maximum theoretical capacity | bps | Highway lanes |
| **Throughput** | Actual data transfer rate | bps | Cars actually passing |
| **Latency** | Time for data to travel | seconds | Time per car |
| **Jitter** | Variation in latency | seconds | Variance in travel time |

**Relationship**: Throughput ≤ Bandwidth (always)

---

## 1.11 Standards Organizations

| Organization | Full Form | Standards |
|--------------|-----------|-----------|
| **IEEE** | Institute of Electrical and Electronics Engineers | 802.3 (Ethernet), 802.11 (Wi-Fi) |
| **IETF** | Internet Engineering Task Force | TCP/IP, HTTP, SMTP (RFCs) |
| **ISO** | International Organization for Standardization | OSI Model |
| **ITU** | International Telecommunication Union | H.323 (VoIP), G.7xx (codecs) |
| **W3C** | World Wide Web Consortium | HTML, CSS, XML |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: Layer Identification
**Q**: Which layer handles end-to-end error recovery?
**A**: Transport Layer (uses ACK/NAK, retransmission)

### Pattern 2: Device vs Layer
**Q**: At which layer does a switch operate?
**A**: Layer 2 (Data Link) - uses MAC addresses

### Pattern 3: Delay Calculations
**Q**: Calculate time to send 1000-bit packet over 100 Mbps link
**A**: Tt = 1000 / 100×10⁶ = 10 μs

### Pattern 4: Mesh Topology
**Q**: Links needed for 20-node full mesh?
**A**: 20×19/2 = 190 links

---

## 📝 Quick Revision Checklist

- [ ] OSI 7 layers with PDUs and devices
- [ ] TCP/IP vs OSI comparison
- [ ] Transmission delay vs Propagation delay formulas
- [ ] Network topologies and their properties
- [ ] Switching techniques (Circuit vs Packet)
- [ ] Network devices and their layer of operation
- [ ] Collision domain vs Broadcast domain counting

---

## 🔥 One-Liner Summary

> "Networks connect autonomous computers using shared protocols; OSI has 7 layers (theoretical), TCP/IP has 4 (practical); Switches work at L2 with MACs, Routers at L3 with IPs; Tt = L/B (pushing bits), Tp = D/V (traveling bits)."
