# Chapter 4: Network Layer

## 🎯 GATE/ESE Weightage: 10-15 marks (Heavy Numericals + Conceptual)

---

## 4.1 Network Layer Functions

The Network Layer is responsible for **host-to-host** delivery across multiple networks (internetworking).

**Core Functions**:
1. **Logical Addressing**: IP addresses
2. **Routing**: Determine best path
3. **Forwarding**: Move packets to next hop
4. **Fragmentation**: Split packets for different MTUs
5. **Packetization**: Encapsulate segments into packets

---

## 4.2 IPv4 Addressing (🎯 MOST IMPORTANT)

### IP Address Structure

```
32 bits = 4 octets = 4 bytes

Binary: 11000000.10101000.00000001.00000001
Dotted Decimal: 192.168.1.1

Each octet: 0-255 (2^8 values)
Total addresses: 2^32 ≈ 4.3 billion
```

### Classful Addressing (Legacy but GATE loves it!)

```
Class A: 0xxxxxxx. xxxxxxxx.xxxxxxxx.xxxxxxxx
         └─ Net ─┘ └────── Host ──────────┘
         1-126 (0 and 127 reserved)
         
Class B: 10xxxxxx.xxxxxxxx. xxxxxxxx.xxxxxxxx
         └──── Network ───┘ └─── Host ────┘
         128-191
         
Class C: 110xxxxx.xxxxxxxx.xxxxxxxx. xxxxxxxx
         └─────── Network ──────────┘ └ Host ┘
         192-223
         
Class D: 1110xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
         224-239 (Multicast)
         
Class E: 1111xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
         240-255 (Reserved/Experimental)
```

### Class Properties (🎯 MEMORIZE)

| Class | First Octet | Networks | Hosts/Network | Default Mask |
|-------|-------------|----------|---------------|--------------|
| A | 1-126 | 126 (2^7-2) | 16,777,214 (2^24-2) | 255.0.0.0 (/8) |
| B | 128-191 | 16,384 (2^14) | 65,534 (2^16-2) | 255.255.0.0 (/16) |
| C | 192-223 | 2,097,152 (2^21) | 254 (2^8-2) | 255.255.255.0 (/24) |
| D | 224-239 | N/A (Multicast) | N/A | N/A |
| E | 240-255 | Reserved | N/A | N/A |

**🧠 Why -2 for hosts?**
- **Network address**: All host bits = 0 (e.g., 192.168.1.0)
- **Broadcast address**: All host bits = 1 (e.g., 192.168.1.255)

### Special IP Addresses (🎯 IMPORTANT)

| Address | Purpose |
|---------|---------|
| 0.0.0.0 | "This host" (source only) |
| 255.255.255.255 | Limited broadcast |
| 127.x.x.x | Loopback (localhost) |
| 10.0.0.0/8 | Private Class A |
| 172.16.0.0/12 | Private Class B (172.16-172.31) |
| 192.168.0.0/16 | Private Class C |
| 169.254.0.0/16 | Link-local (APIPA) |

---

## 4.3 Subnetting (🎯 MOST ASKED)

### Why Subnetting?

- **Reduce broadcast domain** size
- **Efficient IP** allocation
- **Security** boundaries
- **Network organization**

### Subnet Mask

```
IP Address:     192.168.1.50     = 11000000.10101000.00000001.00110010
Subnet Mask:    255.255.255.0    = 11111111.11111111.11111111.00000000
                                   └────── Network ───────────┘└ Host ┘
Network ID:     192.168.1.0      (AND operation)
```

### CIDR Notation

```
/n = n bits for network

192.168.1.0/24 means:
- First 24 bits = Network
- Last 8 bits = Host
- Subnet mask = 255.255.255.0
```

### Subnet Calculation (🎯 CRITICAL)

**Given**: 192.168.1.0/24, need 4 subnets

**Step 1**: Bits needed = ⌈log₂(4)⌉ = 2 bits

**Step 2**: New prefix = /24 + 2 = /26

**Step 3**: Hosts per subnet = 2^(32-26) - 2 = 62 hosts

**Step 4**: Subnet increment = 256 - 192 = 64 (or 2^6 = 64)

```
Subnet 1: 192.168.1.0/26    (0-63)    Usable: .1 to .62
Subnet 2: 192.168.1.64/26   (64-127)  Usable: .65 to .126
Subnet 3: 192.168.1.128/26  (128-191) Usable: .129 to .190
Subnet 4: 192.168.1.192/26  (192-255) Usable: .193 to .254
```

### Quick Subnet Reference Table (🎯 MEMORIZE)

| CIDR | Mask | Block Size | Hosts | Subnets (from /24) |
|------|------|------------|-------|-------------------|
| /24 | 255.255.255.0 | 256 | 254 | 1 |
| /25 | 255.255.255.128 | 128 | 126 | 2 |
| /26 | 255.255.255.192 | 64 | 62 | 4 |
| /27 | 255.255.255.224 | 32 | 30 | 8 |
| /28 | 255.255.255.240 | 16 | 14 | 16 |
| /29 | 255.255.255.248 | 8 | 6 | 32 |
| /30 | 255.255.255.252 | 4 | 2 | 64 |
| /31 | 255.255.255.254 | 2 | 0* | 128 |
| /32 | 255.255.255.255 | 1 | 0 | 256 |

**Note**: /30 is used for point-to-point links (2 hosts)
**Note**: /31 is special RFC 3021 for point-to-point (no network/broadcast)

### VLSM (Variable Length Subnet Masks)

**Problem**: Different subnets need different sizes

```
Given: 192.168.1.0/24
Need:
- Subnet A: 50 hosts
- Subnet B: 25 hosts  
- Subnet C: 10 hosts
- Subnet D: 2 hosts (point-to-point)

Solution (allocate largest first):
A: 192.168.1.0/26    (62 hosts) ← Covers 0-63
B: 192.168.1.64/27   (30 hosts) ← Covers 64-95
C: 192.168.1.96/28   (14 hosts) ← Covers 96-111
D: 192.168.1.112/30  (2 hosts)  ← Covers 112-115
```

### 🎯 Finding Network Details from IP

**Given**: 172.16.45.123/20

**Step 1**: Find subnet mask
- /20 = 20 ones = 255.255.240.0

**Step 2**: Find network address (AND operation)
```
172.16.45.123   = 10101100.00010000.00101101.01111011
255.255.240.0   = 11111111.11111111.11110000.00000000
Network         = 10101100.00010000.00100000.00000000
                = 172.16.32.0
```

**Step 3**: Find broadcast (OR with inverted mask)
```
172.16.32.0     = 10101100.00010000.00100000.00000000
~Mask           = 00000000.00000000.00001111.11111111
Broadcast       = 10101100.00010000.00101111.11111111
                = 172.16.47.255
```

**Step 4**: Usable range
- First host: 172.16.32.1
- Last host: 172.16.47.254
- Total hosts: 2^12 - 2 = 4094

---

## 4.4 IPv4 Header (🎯 IMPORTANT)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if IHL > 5)                       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Header Fields

| Field | Bits | Description |
|-------|------|-------------|
| **Version** | 4 | IPv4 = 4 |
| **IHL** | 4 | Header length in 32-bit words (min 5 = 20 bytes) |
| **ToS/DSCP** | 8 | Type of Service / QoS |
| **Total Length** | 16 | Entire packet size (max 65535 bytes) |
| **Identification** | 16 | Fragment identification |
| **Flags** | 3 | DF (Don't Fragment), MF (More Fragments) |
| **Fragment Offset** | 13 | Position in original datagram (×8 bytes) |
| **TTL** | 8 | Hop limit (decremented at each router) |
| **Protocol** | 8 | Upper layer protocol (1=ICMP, 6=TCP, 17=UDP) |
| **Header Checksum** | 16 | Header integrity check |
| **Source IP** | 32 | Sender's IP address |
| **Destination IP** | 32 | Receiver's IP address |

**🎯 Protocol Numbers** (GATE loves these):
| Number | Protocol |
|--------|----------|
| 1 | ICMP |
| 2 | IGMP |
| 6 | TCP |
| 17 | UDP |
| 89 | OSPF |

---

## 4.5 IP Fragmentation (🎯 GATE FAVORITE)

### Why Fragment?

Different networks have different **MTU** (Maximum Transmission Unit).

```
MTU = 1500 bytes (Ethernet)
MTU = 576 bytes (some WANs)

Packet 4000 bytes → Must fragment for 1500 MTU network
```

### Fragmentation Process

```
Original: 4000 bytes (20 header + 3980 data)
MTU: 1500 bytes

Fragment 1: 1500 bytes (20 header + 1480 data)
           Offset = 0, MF = 1
           
Fragment 2: 1500 bytes (20 header + 1480 data)
           Offset = 185 (1480/8), MF = 1
           
Fragment 3: 1040 bytes (20 header + 1020 data)
           Offset = 370 (2960/8), MF = 0
```

### 🎯 Fragmentation Formulas

```
Max Data per Fragment = MTU - Header Size
                      = MTU - 20 (minimum)
                      
Must be multiple of 8 (offset granularity)

Fragment Offset = (Bytes before this fragment) / 8
```

### GATE Problem Pattern

**Q**: 4500-byte packet, 20-byte header, MTU = 1500. Find fragments.

**Solution**:
```
Original data = 4500 - 20 = 4480 bytes
Max data/fragment = 1500 - 20 = 1480 bytes (multiple of 8 ✓)

Fragment 1: 1500 bytes (1480 data), Offset = 0, MF = 1
Fragment 2: 1500 bytes (1480 data), Offset = 185, MF = 1
Fragment 3: 1520 bytes (1520 data), Offset = 370, MF = 0

Wait! 1520 > 1500. Recalculate:
Remaining = 4480 - 2960 = 1520 bytes
Fragment 3: 1500 bytes (1480 data), Offset = 370, MF = 1
Fragment 4: 60 bytes (40 data + 20 header), Offset = 555, MF = 0
```

**🎯 Key Point**: Each fragment gets its **own** IP header (20 bytes overhead each)

---

## 4.6 ICMP (Internet Control Message Protocol)

### Purpose
- **Error reporting** (unreachable, time exceeded)
- **Network diagnostics** (ping, traceroute)

### ICMP Message Types (🎯 MEMORIZE)

| Type | Name | Description |
|------|------|-------------|
| 0 | Echo Reply | Ping response |
| 3 | Destination Unreachable | Can't reach destination |
| 4 | Source Quench | Congestion control (deprecated) |
| 5 | Redirect | Better route available |
| 8 | Echo Request | Ping request |
| 11 | Time Exceeded | TTL = 0 (traceroute uses this) |
| 12 | Parameter Problem | Header error |

### Ping and Traceroute

```
PING: Uses Echo Request (Type 8) and Echo Reply (Type 0)
      Measures RTT, packet loss

TRACEROUTE: Sends packets with increasing TTL
           TTL=1 → First router responds with Time Exceeded
           TTL=2 → Second router responds
           ... until destination reached
```

---

## 4.7 ARP and RARP

### ARP (Address Resolution Protocol)

```
Purpose: IP address → MAC address

Sender knows: 192.168.1.5 (destination IP)
Sender needs: XX:XX:XX:XX:XX:XX (destination MAC)

ARP Request (Broadcast):
"Who has 192.168.1.5? Tell 192.168.1.1"
→ Sent to FF:FF:FF:FF:FF:FF

ARP Reply (Unicast):
"192.168.1.5 is at AA:BB:CC:DD:EE:FF"
→ Sent directly to sender
```

### ARP Cache

```
Stores recent IP→MAC mappings
$ arp -a
192.168.1.1    00:11:22:33:44:55
192.168.1.5    AA:BB:CC:DD:EE:FF
```

**Cache timeout**: Typically 20 minutes

### RARP (Reverse ARP)

```
Purpose: MAC address → IP address
Used by: Diskless workstations at boot
Status: Replaced by BOOTP/DHCP
```

### Proxy ARP

Router answers ARP requests on behalf of hosts on another network.

```
Host A wants to reach Host B on different subnet
Router has both networks connected
Router responds to ARP with its own MAC
Router forwards packets between networks
```

---

## 4.8 Routing Concepts (🎯 CRITICAL)

### Routing Table

```
Destination      Next Hop       Interface    Metric
192.168.1.0/24   Direct         eth0         0
10.0.0.0/8       192.168.1.1    eth0         1
0.0.0.0/0        192.168.1.254  eth0         1  ← Default route
```

### Longest Prefix Match

**When multiple routes match, use the most specific (longest prefix).**

```
Packet to: 192.168.1.100

Routes:
0.0.0.0/0        → Default
192.168.0.0/16   → Router A
192.168.1.0/24   → Router B  ← Longest match, USE THIS
```

### Static vs Dynamic Routing

| Aspect | Static | Dynamic |
|--------|--------|---------|
| Configuration | Manual | Automatic |
| Scalability | Poor | Good |
| Bandwidth | None | Uses bandwidth |
| CPU/Memory | Low | Higher |
| Convergence | N/A | Varies by protocol |
| Use case | Small networks | Large networks |

---

## 4.9 Routing Algorithms (🎯 VERY IMPORTANT)

### Classification

```
Routing Algorithms
├── Non-Adaptive (Static)
│   └── Shortest path, flooding
│
└── Adaptive (Dynamic)
    ├── Distance Vector (RIP)
    │   └── Bellman-Ford algorithm
    │
    ├── Link State (OSPF)
    │   └── Dijkstra's algorithm
    │
    └── Path Vector (BGP)
```

### Distance Vector Routing (🎯 GATE FAVORITE)

**Principle**: Each router knows:
- **Distance** to every destination
- **Vector** (direction/next hop) to reach them

**Algorithm**: Bellman-Ford
```
Dx(y) = min { c(x,v) + Dv(y) }

Where:
Dx(y) = cost from x to y
c(x,v) = cost from x to neighbor v
Dv(y) = neighbor v's cost to y
```

#### Count-to-Infinity Problem

```
       1        1
  A ─────── B ─────── C

Initial: A→C cost = 2 (via B)

If link B-C fails:
- B updates: C unreachable
- A still thinks: C via B, cost 2
- B hears A's route: "C via A, cost 2"
- B updates: C via A, cost 3 (wrong!)
- A updates: C via B, cost 4
- ... counts to infinity
```

#### Solutions to Count-to-Infinity

| Technique | Description |
|-----------|-------------|
| **Split Horizon** | Don't advertise route back to source |
| **Poison Reverse** | Advertise infinite cost back to source |
| **Triggered Updates** | Send updates immediately on change |
| **Hold-down Timer** | Ignore updates for a period after change |
| **Maximum Hop Count** | Define infinity (e.g., 16 in RIP) |

### Link State Routing

**Principle**: Each router knows **complete topology**.

**Process**:
1. **Discover neighbors** (Hello packets)
2. **Measure link costs**
3. **Build Link State Packets (LSP)**
4. **Flood LSPs** to all routers
5. **Compute shortest path** (Dijkstra)

#### Dijkstra's Algorithm (🎯 MUST KNOW)

```
1. Initialize: dist[source] = 0, dist[all others] = ∞
2. Mark source as visited
3. Update distances to all unvisited neighbors
4. Pick unvisited node with minimum distance
5. Mark it visited, repeat from step 3
6. Until all nodes visited
```

**Example**:
```
        2
    A ───── B
    │ \     │
  1 │  \ 4  │ 1
    │   \   │
    C ───── D
        3

From A:
Step 1: dist[A]=0, visit A
Step 2: dist[B]=2, dist[C]=1, dist[D]=4
Step 3: Visit C (min=1), update: dist[D]=min(4, 1+3)=4
Step 4: Visit B (min=2), update: dist[D]=min(4, 2+1)=3
Step 5: Visit D (min=3), done

Shortest paths from A: B=2, C=1, D=3
```

### Distance Vector vs Link State (🎯 MEMORIZE)

| Feature | Distance Vector | Link State |
|---------|-----------------|------------|
| Algorithm | Bellman-Ford | Dijkstra |
| Knowledge | Neighbors only | Full topology |
| Updates | Periodic, entire table | Event-driven, LSPs |
| Convergence | Slow | Fast |
| Bandwidth | Less (local exchange) | More (flooding) |
| CPU/Memory | Less | More |
| Loop problem | Yes (count to infinity) | No |
| Example | RIP, IGRP | OSPF, IS-IS |

---

## 4.10 Interior Gateway Protocols (IGP)

### RIP (Routing Information Protocol)

| Feature | Value |
|---------|-------|
| Type | Distance Vector |
| Metric | Hop count |
| Max hops | 15 (16 = infinity) |
| Updates | Every 30 seconds |
| Port | UDP 520 |
| Convergence | Slow |

### OSPF (Open Shortest Path First) (🎯 IMPORTANT)

| Feature | Value |
|---------|-------|
| Type | Link State |
| Metric | Cost (based on bandwidth) |
| Updates | Event-triggered |
| Port | IP Protocol 89 |
| Convergence | Fast |
| Hierarchy | Areas (Area 0 = backbone) |

**OSPF Packet Types**:
| Type | Name | Function |
|------|------|----------|
| 1 | Hello | Neighbor discovery |
| 2 | DBD | Database Description |
| 3 | LSR | Link State Request |
| 4 | LSU | Link State Update |
| 5 | LSAck | Link State Acknowledgment |

**OSPF Router Types**:
- **Internal Router**: All interfaces in one area
- **ABR** (Area Border Router): Connects areas
- **ASBR** (AS Boundary Router): Connects to external AS
- **Backbone Router**: At least one interface in Area 0

### OSPF Cost Calculation

```
Cost = Reference Bandwidth / Interface Bandwidth

Default Reference = 100 Mbps = 10^8 bps

Examples:
10 Mbps → Cost = 100/10 = 10
100 Mbps → Cost = 100/100 = 1
1 Gbps → Cost = 100/1000 = 0.1 (rounded to 1)
```

---

## 4.11 Exterior Gateway Protocol (EGP)

### BGP (Border Gateway Protocol)

- Used **between** Autonomous Systems
- **Path Vector** protocol
- Uses **TCP port 179**
- Policies over shortest path

### BGP Attributes (🎯 Important)

| Attribute | Type | Description |
|-----------|------|-------------|
| AS_PATH | Mandatory | List of AS traversed |
| NEXT_HOP | Mandatory | Next hop IP |
| LOCAL_PREF | Optional | Prefer routes within AS |
| MED | Optional | Metric for external AS |
| ORIGIN | Mandatory | Origin of route (i, e, ?) |

### BGP Path Selection (🎯 ORDER MATTERS)

1. **Highest LOCAL_PREF**
2. **Shortest AS_PATH**
3. **Lowest ORIGIN** (IGP < EGP < incomplete)
4. **Lowest MED**
5. **eBGP over iBGP**
6. **Lowest router ID**

---

## 4.12 NAT (Network Address Translation)

### Why NAT?

- **IPv4 address exhaustion** - Multiple private IPs → one public IP
- **Security** - Internal IPs hidden from internet

### NAT Types

```
STATIC NAT (1:1):
Private 192.168.1.5 ←→ Public 203.0.113.5

DYNAMIC NAT (Pool):
Private IPs → Pool of Public IPs (first-come basis)

PAT/NAPT (Many:1) - Most common:
192.168.1.5:5000 ←→ 203.0.113.1:50000
192.168.1.6:5000 ←→ 203.0.113.1:50001
```

### NAT Table Example

| Inside Local | Inside Global | Outside Global | Protocol |
|--------------|---------------|----------------|----------|
| 192.168.1.5:1025 | 203.0.113.1:50000 | 8.8.8.8:53 | UDP |
| 192.168.1.6:1026 | 203.0.113.1:50001 | 1.1.1.1:443 | TCP |

---

## 4.13 IPv6

### Why IPv6?

- **128-bit addresses** (vs 32-bit IPv4)
- **Simplified header**
- **No fragmentation by routers** (only end hosts)
- **No checksum** (handled by upper layers)
- **Built-in IPsec support**

### IPv6 Address Format

```
128 bits = 8 groups of 16 bits (4 hex digits each)

Full: 2001:0db8:0000:0000:0000:0000:0000:0001
Compressed: 2001:db8::1

Rules:
- Leading zeros in each group can be omitted
- One sequence of all-zero groups replaced by ::
- :: can only appear once
```

### IPv6 Header (🎯 SIMPLIFIED!)

```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |           Flow Label                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Payload Length        |  Next Header  |   Hop Limit   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                         Source Address                        +
|                            (128 bits)                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                      Destination Address                      +
|                            (128 bits)                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Fixed 40 bytes (vs variable in IPv4)
```

### IPv4 vs IPv6 Header Comparison

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Header Size | 20-60 bytes | Fixed 40 bytes |
| Checksum | Yes | No |
| Fragmentation | Routers can fragment | Only end hosts |
| Options | In header | Extension headers |
| TTL | TTL field | Hop Limit |

### IPv6 Address Types

| Type | Prefix | Description |
|------|--------|-------------|
| Loopback | ::1 | Localhost |
| Link-local | fe80::/10 | Same link only |
| Unique Local | fc00::/7 | Private (like RFC 1918) |
| Global Unicast | 2000::/3 | Routable internet |
| Multicast | ff00::/8 | One-to-many |

---

## 4.14 DHCP (Dynamic Host Configuration Protocol)

### DHCP Process (DORA)

```
         Client                              Server
            │                                   │
            │──────── DISCOVER ────────────────→│ (Broadcast)
            │                                   │
            │←─────── OFFER ───────────────────│ (Unicast/Broadcast)
            │                                   │
            │──────── REQUEST ─────────────────→│ (Broadcast)
            │                                   │
            │←─────── ACK ─────────────────────│ (Unicast/Broadcast)
            │                                   │

DORA = Discover → Offer → Request → Acknowledge
```

### DHCP Provides

- IP address
- Subnet mask
- Default gateway
- DNS servers
- Lease time

### DHCP Ports

- Server: UDP **67**
- Client: UDP **68**

---

## 4.15 Key Formulas Summary

| Concept | Formula |
|---------|---------|
| **Hosts in subnet** | 2^(32-n) - 2 |
| **Subnets from /24** | 2^(n-24) |
| **Block size** | 256 - last octet of mask |
| **Fragment offset** | bytes_before / 8 |
| **Max data per fragment** | MTU - 20 |
| **OSPF cost** | Reference_BW / Interface_BW |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: Subnetting
**Q**: 192.168.1.0/26, how many hosts per subnet?
**A**: 2^(32-26) - 2 = 2^6 - 2 = **62 hosts**

### Pattern 2: Network ID
**Q**: IP = 172.16.45.123/20, find network address.
**A**: Mask 255.255.240.0, AND with IP = **172.16.32.0**

### Pattern 3: Fragmentation
**Q**: 3000-byte packet, MTU = 1000. How many fragments?
**A**: Max data = 1000-20 = 980, round to 976 (×8)
       Fragment 1: 976 data
       Fragment 2: 976 data
       Fragment 3: 1028 data (remaining)
       = **4 fragments** (recalculate if needed)

### Pattern 4: Routing Table
**Q**: Which route for 192.168.5.100?
       Routes: 192.168.0.0/16, 192.168.4.0/22, 192.168.5.0/24
**A**: Longest prefix match = **192.168.5.0/24**

---

## 📝 Quick Revision Checklist

- [ ] Classful addressing: Class A (1-126), B (128-191), C (192-223)
- [ ] Subnetting: Hosts = 2^host_bits - 2
- [ ] CIDR: /n means n network bits
- [ ] IPv4 header: Version, IHL, TTL, Protocol, addresses
- [ ] Fragmentation: Offset = bytes/8, MF flag
- [ ] ARP: IP → MAC (broadcast request, unicast reply)
- [ ] Distance Vector: Bellman-Ford, count-to-infinity problem
- [ ] Link State: Dijkstra, complete topology knowledge
- [ ] RIP: Hop count, max 15, UDP 520
- [ ] OSPF: Cost metric, areas, IP protocol 89
- [ ] BGP: Path vector, TCP 179, AS_PATH
- [ ] NAT: Private → Public translation
- [ ] DHCP: DORA process, UDP 67/68

---

## 🔥 One-Liner Summary

> "Network layer routes packets host-to-host; IP addresses are 32-bit (Class A/B/C), subnetting borrows host bits (hosts=2^n-2); routers use longest prefix match; Distance Vector (RIP, Bellman-Ford) knows neighbors, Link State (OSPF, Dijkstra) knows topology; fragmentation splits packets for smaller MTU; ARP resolves IP→MAC; NAT translates private→public."
