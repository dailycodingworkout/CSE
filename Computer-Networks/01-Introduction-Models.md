# Chapter 1: Introduction & Network Models
## The Foundation | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Networks connect; Models organize; Protocols standardize."**

---

## 1.1 Computer Network Basics

### What is a Computer Network?
A collection of interconnected devices that can exchange data and share resources using defined protocols.

### Network Classifications

#### By Geographic Scope

| Type | Full Form | Range | Speed | Example |
|------|-----------|-------|-------|---------|
| PAN | Personal Area Network | ~10m | Low-Medium | Bluetooth devices |
| LAN | Local Area Network | ~1km | High (1Gbps+) | Office, Home |
| MAN | Metropolitan Area Network | ~50km | Medium-High | City network |
| WAN | Wide Area Network | Global | Variable | Internet |

#### By Topology

```
1. Bus Topology:
   ═══════════════════
     │     │     │
    [A]   [B]   [C]

2. Star Topology:
        [A]
         │
   [B]──[HUB]──[C]
         │
        [D]

3. Ring Topology:
     ┌──[A]──┐
    [D]     [B]
     └──[C]──┘

4. Mesh Topology:
   [A]═══[B]
    ║╲  ╱║
    ║ ╳ ║
    ║╱  ╲║
   [C]═══[D]
```

#### Topology Comparison

| Topology | Cable | Fault Tolerance | Cost | Scalability |
|----------|-------|-----------------|------|-------------|
| Bus | Low | Low | Low | Low |
| Star | Medium | Medium | Medium | High |
| Ring | Medium | Low | Medium | Medium |
| Mesh | High | High | High | Low |
| Tree | Medium | Medium | Medium | High |

---

## 1.2 Network Devices

| Device | Layer | Function |
|--------|-------|----------|
| Hub | Physical (1) | Broadcast to all ports |
| Repeater | Physical (1) | Regenerate signal |
| Bridge | Data Link (2) | Forward based on MAC |
| Switch | Data Link (2) | Forward based on MAC, multiple ports |
| Router | Network (3) | Forward based on IP |
| Gateway | All layers | Protocol conversion |
| Modem | Physical (1) | Digital ↔ Analog conversion |

### 🧠 Hub vs Switch vs Router

```
Hub: "I'll tell everyone!" (Broadcast)
     [A]──┐
     [B]──┼──[HUB]──[D]
     [C]──┘
     Message from A goes to B, C, D

Switch: "I'll tell only the right one!" (Unicast)
     [A]──┐           MAC Table:
     [B]──┼──[SWITCH] A → Port 1
     [C]──┘           B → Port 2
     Message from A to C goes only to C

Router: "Different network? I know the way!" (IP Routing)
     [LAN1]──[ROUTER]──[LAN2]
     Connects different networks
```

---

## 1.3 The OSI Model

### The Seven Layers (Top to Bottom)

```
┌─────────────────────────────────────────────────────────────┐
│ 7. APPLICATION    │ User interface, HTTP, FTP, SMTP        │
├───────────────────┼─────────────────────────────────────────┤
│ 6. PRESENTATION   │ Encryption, Compression, Translation   │
├───────────────────┼─────────────────────────────────────────┤
│ 5. SESSION        │ Dialog control, Synchronization        │
├───────────────────┼─────────────────────────────────────────┤
│ 4. TRANSPORT      │ End-to-end delivery, TCP/UDP           │
├───────────────────┼─────────────────────────────────────────┤
│ 3. NETWORK        │ Routing, IP addressing                 │
├───────────────────┼─────────────────────────────────────────┤
│ 2. DATA LINK      │ MAC addressing, Framing, Error detect  │
├───────────────────┼─────────────────────────────────────────┤
│ 1. PHYSICAL       │ Bits transmission, Cables, Signals     │
└─────────────────────────────────────────────────────────────┘
```

### 🔥 The Mnemonic

**Top-Down:** "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"
**Bottom-Up:** "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"

### Layer Details

#### Layer 7: Application
- Direct interface for user applications
- Protocols: HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, SNMP, Telnet, SSH

#### Layer 6: Presentation
- Data format translation (ASCII ↔ EBCDIC)
- Encryption/Decryption
- Compression
- Protocols: SSL/TLS, JPEG, MPEG, GIF

#### Layer 5: Session
- Establishes, manages, terminates sessions
- Synchronization and checkpointing
- Protocols: NetBIOS, RPC, SQL

#### Layer 4: Transport
- End-to-end message delivery
- Segmentation and reassembly
- Flow control, error control
- Protocols: TCP, UDP

#### Layer 3: Network
- Logical addressing (IP)
- Routing between networks
- Protocols: IP, ICMP, IGMP, ARP, RARP
- Devices: Router

#### Layer 2: Data Link
- Physical addressing (MAC)
- Framing, error detection
- Access control to media
- Protocols: Ethernet, PPP, HDLC
- Devices: Switch, Bridge

#### Layer 1: Physical
- Bit transmission
- Physical characteristics
- Transmission media
- Devices: Hub, Repeater, Cables

### Protocol Data Units (PDUs)

| Layer | PDU Name |
|-------|----------|
| Application/Presentation/Session | Data |
| Transport | Segment (TCP) / Datagram (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

### Encapsulation Process

```
Sender:
┌──────────────────────────────────────────────────────────────┐
│ Application  │ [DATA]                                        │
├──────────────┼───────────────────────────────────────────────┤
│ Transport    │ [SEGMENT HEADER][DATA]                        │
├──────────────┼───────────────────────────────────────────────┤
│ Network      │ [IP HEADER][SEGMENT HEADER][DATA]             │
├──────────────┼───────────────────────────────────────────────┤
│ Data Link    │ [FRAME HEADER][IP][SEGMENT][DATA][FCS]        │
├──────────────┼───────────────────────────────────────────────┤
│ Physical     │ 010110110101...                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 1.4 The TCP/IP Model

### Four Layers

```
┌────────────────────────────────────────────────────┐
│ APPLICATION      │ HTTP, FTP, SMTP, DNS, SSH      │
│                  │ (OSI 5, 6, 7 combined)         │
├──────────────────┼─────────────────────────────────┤
│ TRANSPORT        │ TCP, UDP                       │
│                  │ (Same as OSI 4)                │
├──────────────────┼─────────────────────────────────┤
│ INTERNET         │ IP, ICMP, ARP, RARP           │
│                  │ (Same as OSI 3)                │
├──────────────────┼─────────────────────────────────┤
│ NETWORK ACCESS   │ Ethernet, Wi-Fi, PPP          │
│ (Link/Host-to-   │ (OSI 1, 2 combined)           │
│  Network)        │                                │
└────────────────────────────────────────────────────┘
```

### 🎯 OSI vs TCP/IP Comparison

| Aspect | OSI Model | TCP/IP Model |
|--------|-----------|--------------|
| Layers | 7 | 4 |
| Development | ISO | DoD/ARPANET |
| Approach | Theoretical | Practical |
| Protocol-dependent | No | Yes |
| Presentation/Session | Separate | Merged into Application |
| Network Access | Separate | Merged |
| Usage | Reference model | Implemented model |

### 🚨 GATE Trap

**Q:** Which layer is responsible for routing?
- **OSI:** Network Layer (Layer 3)
- **TCP/IP:** Internet Layer

**Q:** Which layer provides end-to-end delivery?
- **Answer:** Transport Layer (both models)

---

## 1.5 Transmission Modes

### Simplex
```
[Sender] ────────→ [Receiver]
Example: Keyboard to Computer, TV broadcast
```

### Half-Duplex
```
[Device A] ←────────→ [Device B]
(One direction at a time)
Example: Walkie-talkie
```

### Full-Duplex
```
[Device A] ⟺ [Device B]
(Both directions simultaneously)
Example: Telephone, TCP connections
```

---

## 1.6 Switching Techniques

### Circuit Switching
```
1. Setup phase: Establish path
2. Data transfer: Use dedicated path
3. Teardown: Release path

[A]──[Switch]──[Switch]──[B]
     Dedicated path
```
- Used in: Traditional telephone
- Pros: Guaranteed bandwidth, no congestion
- Cons: Inefficient (unused bandwidth wasted)

### Packet Switching

#### Datagram Approach
```
Packets may take different routes:
[A]──→[R1]──→[R2]──→[B]
       ↓      ↑
      [R3]───┘
Each packet independent
```
- Used in: Internet (IP)
- Pros: Efficient, fault-tolerant
- Cons: Packets may arrive out of order

#### Virtual Circuit Approach
```
Path established first, all packets follow same path
[A]──→[R1]──→[R2]──→[B]
     VC setup first
```
- Used in: ATM, Frame Relay
- Pros: Ordered delivery, QoS possible
- Cons: Setup delay, less flexible

### Message Switching (Store-and-Forward)
```
Complete message stored at each node
[A]──→[R1]──→[R2]──→[B]
       ↓
    Store full
    message
```
- Pros: No setup, efficient for low-priority
- Cons: High delay, large storage needed

---

## 1.7 Network Performance Metrics

### Bandwidth
Rate of data transfer (bits per second).
$$\text{Bandwidth} = \text{bps, Kbps, Mbps, Gbps}$$

### Latency (Delay)
Time for a bit to travel from source to destination.

$$\text{Total Delay} = T_{proc} + T_{queue} + T_{trans} + T_{prop}$$

| Delay Type | Formula | Description |
|------------|---------|-------------|
| Processing | - | Time to process packet header |
| Queuing | Variable | Time waiting in router queue |
| Transmission | $L/R$ | Time to push bits onto link |
| Propagation | $d/v$ | Time for bit to travel the link |

### 🎯 Key Formulas

**Transmission Delay:**
$$T_{trans} = \frac{L}{R} = \frac{\text{Packet size (bits)}}{\text{Bandwidth (bps)}}$$

**Propagation Delay:**
$$T_{prop} = \frac{d}{v} = \frac{\text{Distance (m)}}{\text{Speed (m/s)}}$$

Speed of light in cable: ~$2 \times 10^8$ m/s

**Round Trip Time (RTT):**
$$RTT = 2 \times T_{prop}$$

### Throughput
Actual rate of data transfer.
$$\text{Throughput} \leq \text{Bandwidth}$$

### Efficiency
$$\eta = \frac{\text{Useful data}}{\text{Total data transmitted}}$$

---

## 🎯 Practice Problems

### Problem 1: Delay Calculation
**Q:** A 1 Mbps link, packet size 1000 bits, distance 100 km, speed $2 \times 10^8$ m/s. Find total delay.

**Solution:**
- $T_{trans} = \frac{1000}{10^6} = 1$ ms
- $T_{prop} = \frac{100 \times 10^3}{2 \times 10^8} = 0.5$ ms
- Total = 1 + 0.5 = **1.5 ms**

### Problem 2: OSI Layer
**Q:** At which layer does the router operate?
**Answer:** Network Layer (Layer 3)

### Problem 3: TCP/IP Mapping
**Q:** Which OSI layers are combined in TCP/IP Application layer?
**Answer:** Session (5), Presentation (6), Application (7)

### Problem 4: Switching
**Q:** Which switching technique does the Internet primarily use?
**Answer:** Packet switching (Datagram approach)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"All People Seem To Need Data Processing"**
(Application, Presentation, Session, Transport, Network, Data Link, Physical)

**"Please Don't Tell Secret Passwords Anyway"**
(Physical, Data Link, Network, Transport, Session, Presentation, Application)

### The Mental Slider
Imagine sending a letter:
- **Application:** Writing the letter
- **Presentation:** Translating to recipient's language
- **Session:** Establishing conversation
- **Transport:** Splitting into multiple envelopes if needed
- **Network:** Determining route (addresses)
- **Data Link:** Selecting mailman for each leg
- **Physical:** Actually walking/driving

### The 5-Second Snap-Check
1. **Layer device operates at?** Hub=1, Switch=2, Router=3
2. **PDU name?** Bits→Frame→Packet→Segment→Data
3. **OSI vs TCP/IP?** 7 vs 4 layers
4. **Switching type?** Internet=Packet, Phone=Circuit
5. **Delay dominant?** High BW=Propagation, Low BW=Transmission

---

## 📈 Key Takeaways

| Concept | Remember |
|---------|----------|
| OSI Layers | 7 layers, theoretical model |
| TCP/IP Layers | 4 layers, practical model |
| Hub vs Switch | Broadcast vs Unicast (MAC table) |
| Circuit vs Packet | Dedicated path vs Shared path |
| Transmission Delay | Packet size / Bandwidth |
| Propagation Delay | Distance / Speed |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[Next Chapter: Physical Layer →](02-Physical-Layer.md)
