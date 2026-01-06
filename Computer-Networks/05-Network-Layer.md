# Chapter 5: Network Layer
## The Routing Engine | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Network layer routes packets across networks using logical addresses."**

---

## 5.1 Network Layer Functions

1. **Logical Addressing:** IP addresses
2. **Routing:** Finding best path
3. **Forwarding:** Moving packet to next hop
4. **Fragmentation:** Breaking large packets
5. **Packetizing:** Encapsulating data

---

## 5.2 IP Addressing

### IPv4 Address

32 bits = 4 octets, dotted decimal notation.

```
Binary:  11000000.10101000.00000001.00001010
Decimal: 192.168.1.10
```

### Classful Addressing

| Class | First Octet | Range | Default Mask | Networks | Hosts/Network |
|-------|-------------|-------|--------------|----------|---------------|
| A | 0xxx | 1-126 | /8 | 128 | 16,777,214 |
| B | 10xx | 128-191 | /16 | 16,384 | 65,534 |
| C | 110x | 192-223 | /24 | 2,097,152 | 254 |
| D | 1110 | 224-239 | - | Multicast | - |
| E | 1111 | 240-255 | - | Reserved | - |

**Note:** 127.x.x.x is loopback (localhost).

### Special Addresses

| Address | Purpose |
|---------|---------|
| 0.0.0.0 | This host |
| 127.0.0.1 | Loopback |
| 255.255.255.255 | Limited broadcast |
| Network.All-1s | Directed broadcast |
| Network.All-0s | Network address |

### Private IP Ranges (RFC 1918)

| Class | Range | CIDR |
|-------|-------|------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

---

## 5.3 Subnetting

### Why Subnet?
- Efficient IP allocation
- Reduce broadcast domain
- Improve security
- Hierarchical addressing

### Subnet Mask

Separates network portion from host portion.

```
IP:      192.168.1.100
Mask:    255.255.255.0   (/24)
         
Binary:  11111111.11111111.11111111.00000000
         ├───── Network (24 bits) ───┤ Host │
         
Network: 192.168.1.0
Host:    100
```

### CIDR Notation

/n = n bits for network

| CIDR | Mask | Hosts |
|------|------|-------|
| /8 | 255.0.0.0 | 16,777,214 |
| /16 | 255.255.0.0 | 65,534 |
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |
| /31 | 255.255.255.254 | 0 (point-to-point) |
| /32 | 255.255.255.255 | 1 (host route) |

### 🔥 Subnetting Formula

$$\text{Usable Hosts} = 2^h - 2$$

Where h = number of host bits.

(-2 for network address and broadcast)

$$\text{Number of Subnets} = 2^s$$

Where s = number of subnet bits borrowed.

### 🎯 Subnetting Example

**Problem:** Divide 192.168.1.0/24 into 4 subnets.

**Solution:**
1. Need 4 subnets → $2^s = 4$ → s = 2 bits
2. New mask: /24 + 2 = /26 (255.255.255.192)
3. Block size: $256 - 192 = 64$
4. Subnets:
   - 192.168.1.0/26 (0-63)
   - 192.168.1.64/26 (64-127)
   - 192.168.1.128/26 (128-191)
   - 192.168.1.192/26 (192-255)

| Subnet | Network | First Host | Last Host | Broadcast |
|--------|---------|------------|-----------|-----------|
| 1 | 192.168.1.0 | 192.168.1.1 | 192.168.1.62 | 192.168.1.63 |
| 2 | 192.168.1.64 | 192.168.1.65 | 192.168.1.126 | 192.168.1.127 |
| 3 | 192.168.1.128 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| 4 | 192.168.1.192 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

### VLSM (Variable Length Subnet Mask)

Divide based on need, not equally.

**Example:** Allocate from 192.168.1.0/24:
- Subnet A: 60 hosts → /26 (62 usable)
- Subnet B: 30 hosts → /27 (30 usable)
- Subnet C: 10 hosts → /28 (14 usable)
- Point-to-point links: /30 (2 usable)

---

## 5.4 IPv4 Header

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤
│Version│  IHL  │Type of Service│          Total Length         │
├───────────────┼───────────────┼───────────────────────────────┤
│         Identification        │Flags│      Fragment Offset    │
├───────────────┼───────────────┼─────┴─────────────────────────┤
│  Time to Live │    Protocol   │         Header Checksum       │
├───────────────┴───────────────┼───────────────────────────────┤
│                       Source Address                          │
├───────────────────────────────────────────────────────────────┤
│                    Destination Address                        │
├───────────────────────────────────────────────────────────────┤
│                    Options (if IHL > 5)                       │
└───────────────────────────────────────────────────────────────┘
```

### Key Fields

| Field | Size | Description |
|-------|------|-------------|
| Version | 4 bits | 4 for IPv4 |
| IHL | 4 bits | Header length in 32-bit words (min 5) |
| Total Length | 16 bits | Entire packet size (max 65535) |
| TTL | 8 bits | Hop limit (decremented each hop) |
| Protocol | 8 bits | ICMP=1, TCP=6, UDP=17 |
| Flags | 3 bits | DF (Don't Fragment), MF (More Fragments) |
| Fragment Offset | 13 bits | Position in original packet |

### Fragmentation

When packet > MTU (Maximum Transmission Unit).

**MTU of Ethernet:** 1500 bytes

**Fragmentation Example:**
- Original packet: 4000 bytes data
- MTU: 1500 bytes
- Header: 20 bytes
- Max data per fragment: 1480 bytes

| Fragment | Size | Offset | MF |
|----------|------|--------|-----|
| 1 | 1500 | 0 | 1 |
| 2 | 1500 | 185 | 1 |
| 3 | 1040 | 370 | 0 |

**Note:** Offset in units of 8 bytes. 1480/8 = 185.

---

## 5.5 Routing Concepts

### Forwarding Table

| Destination | Mask | Next Hop | Interface |
|-------------|------|----------|-----------|
| 192.168.1.0 | /24 | - | eth0 |
| 192.168.2.0 | /24 | 10.0.0.2 | eth1 |
| 0.0.0.0 | /0 | 10.0.0.1 | eth1 |

### Longest Prefix Match

Choose route with longest matching prefix.

**Example:** Destination 192.168.1.100
- 192.168.0.0/16 matches → 16 bits
- 192.168.1.0/24 matches → 24 bits ✓ (longer, chosen)
- 0.0.0.0/0 matches → 0 bits (default)

---

## 5.6 Routing Algorithms

### Distance Vector (Bellman-Ford)

**Principle:** "Tell neighbors about the world"

Each router:
1. Knows distance to neighbors
2. Shares routing table with neighbors
3. Updates based on neighbor info

**Bellman-Ford Equation:**
$$D_x(y) = \min_v \{c(x,v) + D_v(y)\}$$

**Count-to-Infinity Problem:**

```
Before:    A ──1── B ──1── C
After C fails:
A thinks: Distance to C via B = 2
B thinks: Distance to C via A = 3
A thinks: Distance to C via B = 4
... continues to infinity!
```

**Solutions:**
- Split Horizon
- Poison Reverse
- Triggered Updates

**Protocol:** RIP (Routing Information Protocol)

### Link State (Dijkstra)

**Principle:** "Tell the world about neighbors"

Each router:
1. Discovers neighbors
2. Measures link cost
3. Builds Link State Packet (LSP)
4. Floods LSP to all routers
5. Runs Dijkstra to compute shortest paths

**Dijkstra's Algorithm:**

```
1. Initialize: dist[source] = 0, others = ∞
2. Add source to visited
3. For each neighbor of current:
   if dist[current] + edge < dist[neighbor]:
       dist[neighbor] = dist[current] + edge
4. Select unvisited with smallest distance
5. Repeat from step 3 until all visited
```

**Protocol:** OSPF (Open Shortest Path First)

### 🎯 Distance Vector vs Link State

| Aspect | Distance Vector | Link State |
|--------|-----------------|------------|
| Knowledge | Local (neighbors) | Global (full topology) |
| Updates | Periodic, to neighbors | Event-driven, flooded |
| Algorithm | Bellman-Ford | Dijkstra |
| Convergence | Slow | Fast |
| Memory | Low | High |
| Protocol | RIP | OSPF, IS-IS |

---

## 5.7 Routing Protocols

### Interior Gateway Protocols (IGP)

Within an Autonomous System (AS).

#### RIP (Routing Information Protocol)

- Distance vector
- Metric: Hop count (max 15)
- Updates: Every 30 seconds
- Port: UDP 520

#### OSPF (Open Shortest Path First)

- Link state
- Metric: Cost (bandwidth-based)
- Hierarchical (Areas)
- Protocol: IP (89)

### Exterior Gateway Protocol (EGP)

Between Autonomous Systems.

#### BGP (Border Gateway Protocol)

- Path vector
- Metric: AS path, policies
- Port: TCP 179
- Used for Internet routing

---

## 5.8 ARP and ICMP

### ARP (Address Resolution Protocol)

Maps IP → MAC address.

```
Host A wants to send to 192.168.1.5
1. A broadcasts: "Who has 192.168.1.5?"
2. 192.168.1.5 replies: "I have it, my MAC is XX:XX:XX"
3. A caches the mapping
```

**ARP Packet:**

| Field | Value |
|-------|-------|
| Hardware Type | 1 (Ethernet) |
| Protocol Type | 0x0800 (IP) |
| Operation | 1 (Request) or 2 (Reply) |
| Sender MAC/IP | Filled by sender |
| Target MAC/IP | Filled by target |

**RARP:** Reverse ARP (MAC → IP, obsolete)

### ICMP (Internet Control Message Protocol)

Error reporting and diagnostics.

| Type | Code | Message |
|------|------|---------|
| 0 | 0 | Echo Reply (ping response) |
| 3 | 0 | Destination Unreachable - Network |
| 3 | 1 | Destination Unreachable - Host |
| 3 | 3 | Destination Unreachable - Port |
| 8 | 0 | Echo Request (ping) |
| 11 | 0 | Time Exceeded (TTL=0) |
| 5 | - | Redirect |

**ping:** Uses ICMP Echo Request/Reply
**traceroute:** Uses ICMP Time Exceeded

---

## 5.9 NAT (Network Address Translation)

### Why NAT?
- IPv4 address exhaustion
- Private networks use private IPs
- NAT translates private ↔ public

### NAT Types

**Static NAT:** One-to-one mapping
**Dynamic NAT:** Pool of public IPs
**PAT/NAPT:** Many-to-one using ports (most common)

### PAT Example

```
Inside:                    NAT Router:                Outside:
192.168.1.10:5000 ────→   203.0.113.1:10001 ────→    Server
192.168.1.20:5000 ────→   203.0.113.1:10002 ────→    Server
```

**NAT Table:**

| Inside | Outside |
|--------|---------|
| 192.168.1.10:5000 | 203.0.113.1:10001 |
| 192.168.1.20:5000 | 203.0.113.1:10002 |

---

## 5.10 IPv6

### Why IPv6?
- 32-bit IPv4 exhausted
- 128-bit addresses = $2^{128}$ addresses

### IPv6 Address Format

```
2001:0db8:0000:0000:0000:0000:0000:0001
Can be shortened:
2001:db8::1
```

**Rules:**
- Leading zeros removable: 0db8 → db8
- Consecutive zero groups → :: (once)

### IPv6 Header (Simplified)

```
┌─────────────┬────────────┬─────────────────────┐
│ Version (4) │ Traffic    │     Flow Label      │
│             │ Class (8)  │        (20)         │
├─────────────┴────────────┴─────────────────────┤
│ Payload Length (16)  │ Next Header │ Hop Limit │
├────────────────────────────────────────────────┤
│               Source Address (128)             │
├────────────────────────────────────────────────┤
│            Destination Address (128)           │
└────────────────────────────────────────────────┘
```

**Fixed 40 bytes** (vs variable IPv4 header)
**No fragmentation** by intermediate routers
**No checksum** (handled by upper layers)

---

## 🎯 Practice Problems

### Problem 1: Subnetting
**Q:** How many /28 subnets from 192.168.1.0/24?
**Solution:** 24 → 28 means 4 bits borrowed. $2^4 = 16$ subnets.

### Problem 2: Hosts
**Q:** Usable hosts in /26 network?
**Solution:** Host bits = 32 - 26 = 6. Hosts = $2^6 - 2 = 62$

### Problem 3: Network Address
**Q:** IP = 172.16.45.129, Mask = /26. Find network address.
**Solution:**
- /26 → last octet mask = 192 (11000000)
- 129 AND 192 = 128
- Network: 172.16.45.128

### Problem 4: Broadcast Address
**Q:** Network 192.168.1.64/27. Find broadcast.
**Solution:**
- /27 → 32 hosts per block
- Broadcast = 192.168.1.64 + 31 = 192.168.1.95

### Problem 5: Fragmentation
**Q:** 4500 byte datagram, MTU = 1500, header = 20. How many fragments?
**Solution:**
- Data = 4500 - 20 = 4480 bytes
- Per fragment = 1500 - 20 = 1480 bytes
- Fragments = ⌈4480/1480⌉ = 4

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Class A is for All (huge), B is for Big, C is for Compact (small)"**

### The Mental Slider
- **/24:** 256 addresses, 254 usable
- Each bit borrowed halves the hosts, doubles subnets
- Slide from /24 to /32: 254 → 126 → 62 → 30 → 14 → 6 → 2 → 1

### The 5-Second Snap-Check
1. **Class from first octet?** 1-126=A, 128-191=B, 192-223=C
2. **Hosts = $2^{32-mask} - 2$**
3. **Block size = 256 - last octet of mask**
4. **TTL=0?** ICMP Time Exceeded
5. **ARP broadcast?** FF:FF:FF:FF:FF:FF

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| Hosts = $2^h - 2$ | Usable hosts (h = host bits) |
| Subnets = $2^s$ | Number of subnets (s = subnet bits) |
| Block size = $256 - \text{mask octet}$ | Subnet increment |
| Network = IP AND Mask | Find network address |
| Broadcast = Network OR NOT Mask | Find broadcast |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: MAC Layer](04-MAC-Layer.md) | [Next: Transport Layer →](06-Transport-Layer.md)
