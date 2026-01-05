# Chapter 4: Network Layer

## 🎯 The Atomic Truth
> **"Routing packets from source to destination across multiple networks using logical addressing."**

---

## 4.1 Network Layer Functions

### Core Responsibilities

| Function | Description |
|----------|-------------|
| **Logical Addressing** | IP addresses for global identification |
| **Routing** | Determine optimal path for packets |
| **Forwarding** | Move packets from input to output port |
| **Fragmentation** | Break large packets for smaller MTU links |
| **Error Handling** | ICMP for error reporting |

### The "Aha!" Moment 💡
Think of Network Layer as the **"GPS navigation system"**:
- **IP Address** = GPS coordinates (globally unique location)
- **Routing Table** = Road map with directions
- **Router** = Highway intersection with signboards
- **Packet** = Car traveling with destination address
- **TTL** = Fuel limit (prevents infinite loops)

---

## 4.2 IP Addressing & Subnetting ⭐⭐⭐

### 4.2.1 IPv4 Address Structure

```
32 bits = 4 octets
┌────────────┬────────────┬────────────┬────────────┐
│  Octet 1   │  Octet 2   │  Octet 3   │  Octet 4   │
│  8 bits    │  8 bits    │  8 bits    │  8 bits    │
└────────────┴────────────┴────────────┴────────────┘
Example: 192.168.1.100 = 11000000.10101000.00000001.01100100
```

### 4.2.2 Classful Addressing

| Class | First Bits | First Octet Range | Network/Host | Default Mask | Networks | Hosts/Network |
|-------|------------|-------------------|--------------|--------------|----------|---------------|
| A | 0xxx | 1-126 | N.H.H.H | /8 (255.0.0.0) | 126 | 16,777,214 |
| B | 10xx | 128-191 | N.N.H.H | /16 (255.255.0.0) | 16,384 | 65,534 |
| C | 110x | 192-223 | N.N.N.H | /24 (255.255.255.0) | 2,097,152 | 254 |
| D | 1110 | 224-239 | Multicast | - | - | - |
| E | 1111 | 240-255 | Reserved | - | - | - |

**Memory Trick**: "**All Big Companies Don't Experiment**" (A, B, C, D, E)

**Special Addresses**:

| Address | Purpose |
|---------|---------|
| 0.0.0.0 | This host (used during boot) |
| 127.x.x.x | Loopback (127.0.0.1 = localhost) |
| 255.255.255.255 | Limited broadcast (local network) |
| Network.0 | Network address |
| Network.all-1s | Directed broadcast |

### 4.2.3 Private IP Ranges ⭐

| Class | Range | CIDR |
|-------|-------|------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

**APIPA**: 169.254.0.0/16 (Link-local, auto-assigned when DHCP fails)

### 4.2.4 Subnetting ⭐⭐⭐

**The Golden Formulas**:

$$\text{Number of Subnets} = 2^s$$
$$\text{Hosts per Subnet} = 2^h - 2$$
$$\text{Block Size} = 2^h = 256 - \text{(last non-zero octet of mask)}$$

Where:
- $s$ = borrowed bits (from host portion)
- $h$ = remaining host bits
- Subtract 2 for network address and broadcast

**Subnet Mask Conversion Table** ⭐:

| CIDR | Mask | Binary Last Octet | Block Size | Hosts |
|------|------|-------------------|------------|-------|
| /24 | 255.255.255.0 | 00000000 | 256 | 254 |
| /25 | 255.255.255.128 | 10000000 | 128 | 126 |
| /26 | 255.255.255.192 | 11000000 | 64 | 62 |
| /27 | 255.255.255.224 | 11100000 | 32 | 30 |
| /28 | 255.255.255.240 | 11110000 | 16 | 14 |
| /29 | 255.255.255.248 | 11111000 | 8 | 6 |
| /30 | 255.255.255.252 | 11111100 | 4 | 2 |
| /31 | 255.255.255.254 | 11111110 | 2 | 0* |
| /32 | 255.255.255.255 | 11111111 | 1 | 0 |

**/30 is commonly used for point-to-point links** (2 usable IPs)

### 4.2.5 Subnetting Examples ⭐⭐

**Example 1 (GATE Style)**:
> Given: 192.168.10.0/24. Create 4 subnets. Find subnet addresses.

**Solution**:
- Need 4 subnets → $2^s = 4$ → $s = 2$ borrowed bits
- Original: /24 → New: /26
- Block size = $2^{8-2} = 64$

| Subnet | Network | First Host | Last Host | Broadcast |
|--------|---------|------------|-----------|-----------|
| 0 | 192.168.10.0 | .1 | .62 | .63 |
| 1 | 192.168.10.64 | .65 | .126 | .127 |
| 2 | 192.168.10.128 | .129 | .190 | .191 |
| 3 | 192.168.10.192 | .193 | .254 | .255 |

**Example 2 (GATE NAT)**:
> IP: 172.25.100.37/21. Find network address.

**Solution**:
- /21 means 21 bits for network
- In 3rd octet: 5 bits network (21 - 16), 3 bits host
- 100 in binary: 01100100
- Keep first 5 bits: 01100 → 96
- Network: 172.25.96.0

**Quick Method**: 
- Block size = $2^{8-5} = 8$ in 3rd octet
- $100 \div 8 = 12.5$ → Floor = 12 → $12 \times 8 = 96$

**Example 3 (GATE Style)**:
> How many /26 subnets can be created from 192.168.1.0/24?

**Solution**:
- /24 has 8 host bits
- /26 has 6 host bits
- Bits borrowed = $26 - 24 = 2$
- Subnets = $2^2 = 4$

### 4.2.6 VLSM (Variable Length Subnet Masking)

**Concept**: Use different subnet sizes based on need.

**Example**:
> 192.168.1.0/24 - Create subnets for: 100 hosts, 50 hosts, 25 hosts, 2 hosts

**Solution** (allocate largest first):
1. 100 hosts → need 128 ($2^7$) → /25 → 192.168.1.0/25
2. 50 hosts → need 64 ($2^6$) → /26 → 192.168.1.128/26
3. 25 hosts → need 32 ($2^5$) → /27 → 192.168.1.192/27
4. 2 hosts → need 4 ($2^2$) → /30 → 192.168.1.224/30

### 4.2.7 Supernetting (CIDR) ⭐

**Concept**: Combine multiple networks into one larger block.

**Route Aggregation Example**:
> Combine: 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24

**Solution**:
- 4 networks → need 2 bits for networks
- Common bits: 192.168.0-3 → 192.168.000000xx (last 6 bits vary)
- Result: 192.168.0.0/22

**Condition for Supernetting**:
- Networks must be contiguous
- Number of networks must be power of 2
- First network address must be divisible by total size

---

## 4.3 IPv4 Header ⭐⭐

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│Version│  IHL  │    ToS/DSCP   │         Total Length          │
├───────┴───────┼───────────────┼───────────────────────────────┤
│         Identification        │Flags│    Fragment Offset      │
├───────────────┼───────────────┼─────┴─────────────────────────┤
│      TTL      │   Protocol    │       Header Checksum         │
├───────────────┴───────────────┴───────────────────────────────┤
│                       Source IP Address                       │
├───────────────────────────────────────────────────────────────┤
│                    Destination IP Address                     │
├───────────────────────────────────────────────────────────────┤
│                    Options (if IHL > 5)                       │
└───────────────────────────────────────────────────────────────┘
```

### Header Fields ⭐

| Field | Size | Description |
|-------|------|-------------|
| **Version** | 4 bits | IP version (4 for IPv4) |
| **IHL** | 4 bits | Header length in 32-bit words (min 5 = 20 bytes) |
| **ToS/DSCP** | 8 bits | Type of Service / QoS marking |
| **Total Length** | 16 bits | Total packet size (header + data), max 65535 |
| **Identification** | 16 bits | Unique ID for fragmentation |
| **Flags** | 3 bits | DF (Don't Fragment), MF (More Fragments) |
| **Fragment Offset** | 13 bits | Position in original (in 8-byte units) |
| **TTL** | 8 bits | Hop limit (decremented at each router) |
| **Protocol** | 8 bits | Upper layer protocol (TCP=6, UDP=17, ICMP=1) |
| **Checksum** | 16 bits | Header checksum only |
| **Source IP** | 32 bits | Sender's IP address |
| **Dest IP** | 32 bits | Receiver's IP address |
| **Options** | Variable | Rarely used (increases IHL) |

**Minimum Header**: 20 bytes (IHL = 5)
**Maximum Header**: 60 bytes (IHL = 15)

### 4.3.1 Fragmentation ⭐⭐

**When**: Packet size > MTU of next link

**Key Concepts**:
- **Identification**: Same for all fragments of original
- **MF Flag**: 1 for all except last fragment
- **DF Flag**: 1 means don't fragment (drop if too large)
- **Fragment Offset**: In units of 8 bytes

**Fragmentation Example (GATE Style)**:
> Original packet: 4000 bytes total (3980 data + 20 header)
> MTU: 1500 bytes
> Calculate fragments.

**Solution**:
- Max data per fragment = MTU - 20 = 1480 bytes
- 1480 must be multiple of 8 → 1480 ✓
- Total data = 3980 bytes

| Fragment | Data Size | Offset (bytes) | Offset (field) | MF |
|----------|-----------|----------------|----------------|-----|
| 1 | 1480 | 0 | 0 | 1 |
| 2 | 1480 | 1480 | 185 | 1 |
| 3 | 1020 | 2960 | 370 | 0 |

**Total bytes sent** = $3 \times 20 + 3980 = 4040$ bytes (60 bytes overhead)

**GATE Trap**: Fragment offset is in 8-byte units, not bytes!

### 4.3.2 TTL (Time to Live)

- Decremented by 1 at each router
- If TTL = 0, packet dropped and ICMP error sent
- Prevents infinite loops
- Typical values: 64, 128, 255

---

## 4.4 ICMP (Internet Control Message Protocol) ⭐

### ICMP Message Types

| Type | Code | Description |
|------|------|-------------|
| 0 | 0 | Echo Reply (ping response) |
| 3 | 0 | Destination Unreachable - Network |
| 3 | 1 | Destination Unreachable - Host |
| 3 | 3 | Destination Unreachable - Port |
| 3 | 4 | Fragmentation needed but DF set |
| 4 | 0 | Source Quench (deprecated) |
| 5 | x | Redirect |
| 8 | 0 | Echo Request (ping) |
| 11 | 0 | TTL Exceeded (used by traceroute) |
| 11 | 1 | Fragment reassembly time exceeded |

### Ping and Traceroute

**Ping**: Uses Echo Request (Type 8) and Echo Reply (Type 0)

**Traceroute**: 
- Sends packets with TTL = 1, 2, 3, ...
- Each router returns ICMP TTL Exceeded
- Reveals path to destination

---

## 4.5 ARP (Address Resolution Protocol) ⭐⭐

### Purpose
Map IP address → MAC address (for local delivery)

### How ARP Works

```
1. Host A wants to send to 192.168.1.5
2. A checks ARP cache - not found
3. A broadcasts: "Who has 192.168.1.5? Tell 192.168.1.1"
   Ethernet: Dest = FF:FF:FF:FF:FF:FF
4. Host with 192.168.1.5 responds:
   "192.168.1.5 is at AA:BB:CC:DD:EE:FF"
5. A caches mapping, sends frame to that MAC
```

### ARP Packet

| Field | Size | Description |
|-------|------|-------------|
| Hardware Type | 2 bytes | 1 = Ethernet |
| Protocol Type | 2 bytes | 0x0800 = IPv4 |
| HLEN | 1 byte | 6 (MAC length) |
| PLEN | 1 byte | 4 (IP length) |
| Operation | 2 bytes | 1 = Request, 2 = Reply |
| Sender MAC | 6 bytes | |
| Sender IP | 4 bytes | |
| Target MAC | 6 bytes | Unknown in request |
| Target IP | 4 bytes | |

### Related Protocols

| Protocol | Purpose |
|----------|---------|
| **ARP** | IP → MAC |
| **RARP** | MAC → IP (obsolete, replaced by DHCP) |
| **Proxy ARP** | Router answers ARP for remote network |
| **Gratuitous ARP** | Announce own IP-MAC mapping |

### ARP Cache Poisoning (Security)
Attacker sends fake ARP replies → Man-in-the-middle attack

---

## 4.6 Routing Algorithms ⭐⭐⭐

### 4.6.1 Classification

```
                    Routing Algorithms
                          │
          ┌───────────────┴───────────────┐
      Static                           Dynamic
   (Manual config)                        │
                          ┌───────────────┴───────────────┐
                    Distance Vector              Link State
                    (Bellman-Ford)              (Dijkstra)
                          │                         │
                    ┌─────┴─────┐              ┌────┴────┐
                   RIP        IGRP           OSPF     IS-IS
```

### 4.6.2 Distance Vector Routing ⭐⭐

**Algorithm**: Bellman-Ford / Distributed Bellman-Ford

**Concept**: Each router shares its distance table with neighbors.

**Distance Table Entry**: (Destination, Cost, Next-Hop)

```
Router A's table:
┌─────────────┬──────┬──────────┐
│ Destination │ Cost │ Next-Hop │
├─────────────┼──────┼──────────┤
│      A      │  0   │    -     │
│      B      │  1   │    B     │
│      C      │  2   │    B     │
│      D      │  3   │    B     │
└─────────────┴──────┴──────────┘
```

**Update Process**:
1. Receive neighbor's distance vector
2. For each destination: $d_{new} = \min(d_{current}, d_{neighbor} + cost_{to\_neighbor})$

**Problems**:

| Problem | Description | Solution |
|---------|-------------|----------|
| **Count to Infinity** | Failed link causes slow convergence | Split horizon, Poison reverse |
| **Routing Loops** | Packets circulate indefinitely | TTL, Hold-down timers |
| **Slow Convergence** | Takes time to propagate changes | Triggered updates |

**Count to Infinity Example**:
```
A ── B ── C (cost 1 each)

If A-B link fails:
- B thinks: can reach A via C (cost 2+1 = 3)
- C thinks: can reach A via B (cost 3+1 = 4)
- This continues: 5, 6, 7... until infinity (16 in RIP)
```

**Solutions**:

| Technique | Description |
|-----------|-------------|
| **Split Horizon** | Don't advertise route back to where learned |
| **Poison Reverse** | Advertise infinity (16) back to source |
| **Hold-down Timer** | Ignore updates for failed destination for a period |
| **Triggered Updates** | Send update immediately on change |

### 4.6.3 Link State Routing ⭐⭐

**Algorithm**: Dijkstra's Shortest Path First

**Concept**: Each router knows entire network topology.

**Steps**:
1. Discover neighbors (Hello packets)
2. Measure link cost
3. Build Link State Packet (LSP)
4. Flood LSP to all routers
5. Build complete topology map
6. Run Dijkstra's algorithm

**Dijkstra's Algorithm** ⭐⭐:

```
Initialize:
  S = {source}
  D[source] = 0
  D[v] = ∞ for all v ≠ source

While S ≠ all nodes:
  Find u ∉ S with minimum D[u]
  Add u to S
  For each neighbor v of u:
    D[v] = min(D[v], D[u] + cost(u,v))
```

**Example (GATE Style)**:
```
Network:
    A ──2── B
    │       │
    1       3
    │       │
    C ──1── D
    
Find shortest paths from A.
```

**Solution**:
| Iteration | S | D[A] | D[B] | D[C] | D[D] |
|-----------|---|------|------|------|------|
| Init | {A} | 0 | 2 | 1 | ∞ |
| 1 | {A,C} | 0 | 2 | 1 | 2 |
| 2 | {A,C,B} | 0 | 2 | 1 | 2 |
| 3 | {A,C,B,D} | 0 | 2 | 1 | 2 |

**Shortest paths**: A→A=0, A→B=2, A→C=1, A→D=2

### 4.6.4 Comparison ⭐

| Aspect | Distance Vector | Link State |
|--------|-----------------|------------|
| Algorithm | Bellman-Ford | Dijkstra |
| Knowledge | Only neighbors | Entire topology |
| Updates | Periodic + triggered | On change |
| Convergence | Slow | Fast |
| Bandwidth | Lower (send to neighbors) | Higher (flood all) |
| CPU/Memory | Lower | Higher |
| Scalability | Limited | Better |
| Example | RIP, IGRP | OSPF, IS-IS |

### 4.6.5 Path Vector Routing

**Used by**: BGP (Border Gateway Protocol)

**Concept**: Like distance vector but shares entire path to prevent loops.

**Loop Prevention**: If own AS in path, reject route.

---

## 4.7 Routing Protocols ⭐⭐

### 4.7.1 Interior vs Exterior

| Type | Scope | Protocols |
|------|-------|-----------|
| **IGP** (Interior) | Within AS | RIP, OSPF, EIGRP, IS-IS |
| **EGP** (Exterior) | Between AS | BGP |

### 4.7.2 RIP (Routing Information Protocol)

| Aspect | RIPv1 | RIPv2 |
|--------|-------|-------|
| Type | Distance Vector | Distance Vector |
| Metric | Hop count | Hop count |
| Max hops | 15 (16 = infinity) | 15 |
| Updates | Every 30 seconds | Every 30 seconds |
| Classless | No | Yes (VLSM support) |
| Multicast | Broadcast | 224.0.0.9 |
| Authentication | No | Yes |

### 4.7.3 OSPF (Open Shortest Path First) ⭐⭐

| Aspect | Details |
|--------|---------|
| Type | Link State |
| Metric | Cost (based on bandwidth) |
| Areas | Hierarchical (Area 0 = backbone) |
| Updates | On change (LSAs) |
| Multicast | 224.0.0.5 (all OSPF), 224.0.0.6 (DR) |
| Convergence | Fast |
| Authentication | Yes |

**OSPF Areas**:
```
        ┌───────────────────────────────┐
        │         Area 0 (Backbone)     │
        │    ┌───┐     ┌───┐    ┌───┐   │
        │    │ABR│     │ABR│    │ABR│   │
        └────┴─┬─┴─────┴─┬─┴────┴─┬─┴───┘
               │         │        │
           ┌───┴───┐ ┌───┴───┐ ┌──┴────┐
           │Area 1 │ │Area 2 │ │Area 3 │
           └───────┘ └───────┘ └───────┘
```

**Router Types**:
- **Internal**: All interfaces in one area
- **ABR**: Area Border Router (connects areas)
- **ASBR**: Autonomous System Boundary Router (connects to other AS)
- **Backbone**: At least one interface in Area 0

**Cost Calculation**:
$$\text{Cost} = \frac{\text{Reference Bandwidth}}{\text{Interface Bandwidth}}$$

Default reference = 100 Mbps

### 4.7.4 BGP (Border Gateway Protocol)

| Aspect | Details |
|--------|---------|
| Type | Path Vector (advanced distance vector) |
| Port | TCP 179 |
| Metric | AS Path, policies |
| eBGP | Between AS (TTL = 1) |
| iBGP | Within AS |
| Path Selection | Shortest AS path, policies |

**BGP Path Selection (simplified)**:
1. Highest Local Preference
2. Shortest AS Path
3. Lowest Origin type (IGP < EGP < Incomplete)
4. Lowest MED
5. eBGP over iBGP
6. Lowest router ID

---

## 4.8 IPv6 ⭐

### 4.8.1 IPv6 Address

```
128 bits = 8 groups of 16 bits (hex)

2001:0db8:0000:0000:0000:ff00:0042:8329
     │
     Can be compressed to:
2001:db8::ff00:42:8329
```

**Compression Rules**:
1. Leading zeros in group can be omitted
2. One sequence of all-zero groups can be replaced with `::`

### 4.8.2 IPv6 vs IPv4

| Aspect | IPv4 | IPv6 |
|--------|------|------|
| Address Size | 32 bits | 128 bits |
| Addresses | ~4.3 billion | 3.4 × 10^38 |
| Header Size | Variable (20-60) | Fixed 40 bytes |
| Fragmentation | Routers can fragment | Only source fragments |
| Checksum | Yes | No (relies on upper layers) |
| Broadcast | Yes | No (use multicast) |
| ARP | Yes | Replaced by NDP |
| DHCP | Yes | DHCPv6 or SLAAC |

### 4.8.3 IPv6 Header

```
┌───────────────────────────────────────────────────────────────┐
│Version│Traffic Class│            Flow Label                  │
├───────┴──────────────┼────────────────┬───────────────────────┤
│    Payload Length    │  Next Header   │      Hop Limit        │
├──────────────────────┴────────────────┴───────────────────────┤
│                     Source Address (128 bits)                 │
├───────────────────────────────────────────────────────────────┤
│                   Destination Address (128 bits)              │
└───────────────────────────────────────────────────────────────┘
```

**Simplified**: No checksum, no fragmentation fields (handled separately)

### 4.8.4 IPv6 Address Types

| Type | Prefix | Description |
|------|--------|-------------|
| Link-local | fe80::/10 | Local subnet only |
| Unique Local | fc00::/7 | Private (like 10.x.x.x) |
| Global Unicast | 2000::/3 | Public, routable |
| Multicast | ff00::/8 | One-to-many |
| Loopback | ::1 | Like 127.0.0.1 |
| Unspecified | :: | Like 0.0.0.0 |

---

## 4.9 NAT (Network Address Translation) ⭐⭐

### 4.9.1 Purpose
- Conserve IPv4 addresses
- Hide internal network
- Allow private IPs to access internet

### 4.9.2 NAT Types

| Type | Description |
|------|-------------|
| **Static NAT** | 1:1 mapping (private → public) |
| **Dynamic NAT** | Pool of public IPs |
| **PAT/NAPT** | Many:1 using port numbers |

### 4.9.3 PAT (Port Address Translation) ⭐

Most common type (also called NAPT, NAT Overload)

```
Internal:                NAT Router:              External:
192.168.1.10:5000  →    203.0.113.1:10001   →    Web Server
192.168.1.11:5000  →    203.0.113.1:10002   →    Web Server
192.168.1.12:6000  →    203.0.113.1:10003   →    Web Server
           └─different internal─┘  └─same public IP, diff ports─┘
```

**NAT Table Entry**: (Internal IP, Internal Port) ↔ (External IP, External Port)

### 4.9.4 NAT Issues

| Issue | Description |
|-------|-------------|
| End-to-end breaks | Hosts behind NAT not directly reachable |
| Application issues | Some protocols embed IP in data (FTP, SIP) |
| IPSec | NAT modifies headers, breaks integrity |
| Performance | Translation adds latency |

---

## 4.10 DHCP (Dynamic Host Configuration Protocol) ⭐

### 4.10.1 Purpose
Automatically assign IP configuration to hosts.

### 4.10.2 DORA Process ⭐

```
Client                           Server
   │                               │
   │──── DISCOVER (broadcast) ────►│
   │                               │
   │◄──── OFFER (unicast/bcast) ───│
   │                               │
   │──── REQUEST (broadcast) ─────►│
   │                               │
   │◄──── ACK (unicast/bcast) ─────│
   │                               │
```

**DORA**: Discover, Offer, Request, Acknowledge

### 4.10.3 DHCP Message Contents

| Message | Contains |
|---------|----------|
| Offer | IP, subnet mask, gateway, DNS, lease time |
| ACK | Confirms all parameters |
| NAK | Decline (IP not available) |
| Release | Client releases IP |

**Lease Time**: How long client can use IP before renewal.

### 4.10.4 DHCP Relay

When DHCP server is on different subnet:
- Router acts as relay agent
- Converts broadcast to unicast
- Adds client's subnet info

---

## 4.11 Edge Cases & GATE Traps

### Trap 1: Subnet vs Broadcast Address
- Network address: All host bits = 0
- Broadcast address: All host bits = 1
- These are NOT usable for hosts!

### Trap 2: /31 Subnets
- 0 usable hosts mathematically
- But RFC 3021 allows for point-to-point links
- No network/broadcast needed on point-to-point

### Trap 3: Fragment Offset Units
- Fragment offset is in 8-byte units
- NOT bytes or bits!
- Offset 185 means byte 1480

### Trap 4: Classful Default Masks
- Don't apply classful mask to CIDR address
- 172.16.0.0/12 has mask /12, not /16!

### Trap 5: Distance Vector - Who Updates Whom
- Each router sends ITS OWN table to neighbors
- NOT the reverse

### Trap 6: OSPF Cost
- Lower cost = better
- Cost = Reference BW / Interface BW
- Default reference = 100 Mbps

---

## 📝 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Class A | 1-126, /8, huge networks |
| Class B | 128-191, /16 |
| Class C | 192-223, /24 |
| Subnets | $2^s$ subnets, $2^h - 2$ hosts |
| CIDR | Block size = $2^{32-prefix}$ |
| IPv4 Header | Min 20 bytes, TTL decrements |
| Fragmentation | Offset in 8-byte units |
| ARP | IP → MAC resolution |
| RIP | Max 15 hops, 30s updates |
| OSPF | Link state, cost-based |
| BGP | Path vector, AS-level |
| NAT/PAT | Private → Public translation |
| DHCP | DORA process |

---

## 🧪 Practice Problems

### Problem 1 (GATE NAT)
IP address 192.168.1.130/26. Find the broadcast address.

<details>
<summary>Solution</summary>

/26 means block size = 64
Network ranges: 0-63, 64-127, 128-191, 192-255
130 is in 128-191 range
Broadcast = 192.168.1.191

</details>

### Problem 2 (GATE Style)
A 5000-byte datagram (including 20-byte IP header) arrives at a router with MTU 1500. How many fragments? What are their offsets?

<details>
<summary>Solution</summary>

Data = 5000 - 20 = 4980 bytes
Max data per fragment = 1500 - 20 = 1480 bytes

Fragment 1: 1480 bytes, offset = 0
Fragment 2: 1480 bytes, offset = 185 (1480/8)
Fragment 3: 1480 bytes, offset = 370 (2960/8)
Fragment 4: 540 bytes, offset = 555 (4440/8)

4 fragments total

</details>

### Problem 3 (GATE Style)
Using Dijkstra's algorithm, find shortest path from A to D in:
A-B: 2, A-C: 5, B-C: 1, B-D: 4, C-D: 1

<details>
<summary>Solution</summary>

Init: D[A]=0, D[B]=∞, D[C]=∞, D[D]=∞

Step 1: Select A
  D[B] = min(∞, 0+2) = 2
  D[C] = min(∞, 0+5) = 5

Step 2: Select B (smallest)
  D[C] = min(5, 2+1) = 3
  D[D] = min(∞, 2+4) = 6

Step 3: Select C
  D[D] = min(6, 3+1) = 4

Shortest path A→D = 4 (via A→B→C→D)

</details>

---

**Previous Chapter**: [← Chapter 3: Data Link Layer](./Chapter-03-Data-Link-Layer.md)

**Next Chapter**: [Chapter 5: Transport Layer →](./Chapter-05-Transport-Layer.md)

---

*Happy Learning!*
