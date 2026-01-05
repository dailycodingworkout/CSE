# Module 6: Routing Protocols | The Singularity

> **The Atomic Truth:** *Routing = Finding the optimal path*

---

## 6.1 Routing Protocol Classification

### **By Algorithm Type**

```
              ROUTING PROTOCOLS
                     │
         ┌───────────┼───────────┐
         │           │           │
   Distance Vector  Link State   Hybrid
         │           │           │
        RIP        OSPF       EIGRP
       IGRP        IS-IS
```

### **By Scope (AS Relationship)**

| Type | Scope | Examples | Algorithm |
|------|-------|----------|-----------|
| **IGP** (Interior Gateway Protocol) | Within AS | RIP, OSPF, EIGRP, IS-IS | Various |
| **EGP** (Exterior Gateway Protocol) | Between AS | BGP | Path Vector |

### **The Analogy 💡**
- **IGP** = Roads within your city (internal routing)
- **EGP** = Highways between cities (inter-domain routing)

---

## 6.2 Distance Vector Protocols

### **Core Concept**
Each router maintains a table with:
- **Destination**
- **Distance** (cost/metric)
- **Next hop** (direction)

### **How It Works**

```
┌─────────────────────────────────────────────────────────────┐
│              DISTANCE VECTOR OPERATION                       │
├─────────────────────────────────────────────────────────────┤
│  1. Initialize: Distance to self = 0, others = ∞            │
│  2. Send routing table to all neighbors (periodically)       │
│  3. Receive neighbor's tables                                │
│  4. Update own table using Bellman-Ford:                     │
│     D_x(y) = min_v { c(x,v) + D_v(y) }                       │
│  5. Repeat until convergence                                 │
└─────────────────────────────────────────────────────────────┘
```

### **Bellman-Ford Algorithm**

$$D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$$

Where:
- $D_x(y)$ = Cost from x to y
- $c(x,v)$ = Cost from x to neighbor v
- $D_v(y)$ = Cost from neighbor v to y

### **Distance Vector Problems**

#### **1. Count-to-Infinity Problem**

```
Before failure:        After A-B link fails:
   A ─── B ─── C          A    B ─── C
   
B thinks: "I can reach A via C (cost = 3)"
C thinks: "I can reach A via B (cost = 4)"
B updates: "Via C = 1 + 4 = 5"
C updates: "Via B = 1 + 5 = 6"
... continues to infinity
```

#### **Solutions**

| Technique | How It Works |
|-----------|--------------|
| **Split Horizon** | Don't advertise route back to source |
| **Poison Reverse** | Advertise route back as ∞ |
| **Triggered Updates** | Send immediately on change (don't wait) |
| **Hold-down Timer** | Don't accept updates for recently failed routes |
| **Maximum Hop Count** | 16 = infinity in RIP |

---

## 6.3 RIP (Routing Information Protocol)

### **RIP Specifications**

| Feature | RIPv1 | RIPv2 |
|---------|-------|-------|
| Classful/Classless | Classful | Classless (VLSM) |
| Authentication | No | Yes |
| Multicast | Broadcast (255.255.255.255) | 224.0.0.9 |
| Maximum hops | 15 (16 = ∞) | 15 |
| Update interval | 30 seconds | 30 seconds |
| Protocol | UDP port 520 | UDP port 520 |

### **RIP Timers**

| Timer | Default | Purpose |
|-------|---------|---------|
| **Update** | 30 sec | Send full routing table |
| **Invalid** | 180 sec | Mark route invalid if no update |
| **Hold-down** | 180 sec | Ignore updates for marked route |
| **Flush** | 240 sec | Remove route from table |

### **RIP Metric**
- **Hop count** (number of routers to destination)
- Max = 15 (16 = unreachable)
- Simple but ignores bandwidth, delay

### **GATE Trap Alert ⚠️**

**"RIP converges slowly"** — Why?
- 30-second update interval
- Count-to-infinity (even with mitigations)
- Max 15 hops limits network size

---

## 6.4 Link State Protocols

### **Core Concept**
Every router knows the **complete network topology** and calculates shortest paths independently.

### **How It Works**

```
┌─────────────────────────────────────────────────────────────┐
│              LINK STATE OPERATION                            │
├─────────────────────────────────────────────────────────────┤
│  1. Discover neighbors (Hello protocol)                      │
│  2. Measure cost to each neighbor                           │
│  3. Create Link State Advertisement (LSA)                    │
│  4. Flood LSA to all routers                                │
│  5. Build complete topology database (LSDB)                  │
│  6. Run Dijkstra's SPF algorithm                            │
│  7. Build routing table from SPF tree                       │
└─────────────────────────────────────────────────────────────┘
```

### **Dijkstra's Algorithm (SPF)**

```python
def dijkstra(graph, source):
    dist = {v: ∞ for v in graph}
    dist[source] = 0
    unvisited = set(graph)
    
    while unvisited:
        u = min(unvisited, key=lambda v: dist[v])
        unvisited.remove(u)
        
        for v in neighbors(u):
            if dist[u] + cost(u,v) < dist[v]:
                dist[v] = dist[u] + cost(u,v)
    
    return dist
```

### **Dijkstra Example**

```
        2
   A ──────── B
   │         │
 1 │         │ 1
   │    3    │
   C ──────── D ─── E
                  2
```

**From A:**
| Step | Visited | Distance to A,B,C,D,E |
|------|---------|----------------------|
| Init | {} | 0,∞,∞,∞,∞ |
| 1 | {A} | 0,2,1,∞,∞ |
| 2 | {A,C} | 0,2,1,4,∞ |
| 3 | {A,C,B} | 0,2,1,3,∞ |
| 4 | {A,C,B,D} | 0,2,1,3,5 |
| 5 | {A,C,B,D,E} | 0,2,1,3,5 |

---

## 6.5 OSPF (Open Shortest Path First)

### **OSPF Specifications**

| Feature | Value |
|---------|-------|
| Type | Link State (IGP) |
| Algorithm | Dijkstra (SPF) |
| Metric | Cost (based on bandwidth) |
| Transport | IP protocol 89 (directly over IP) |
| Multicast | 224.0.0.5 (AllSPFRouters), 224.0.0.6 (AllDRRouters) |
| Updates | Triggered (event-driven) |
| Convergence | Fast |
| Authentication | Yes |
| VLSM/CIDR | Yes |

### **OSPF Metric (Cost)**

$$Cost = \frac{Reference Bandwidth}{Interface Bandwidth}$$

Default reference = 100 Mbps = 10⁸ bps

| Interface | Bandwidth | Default Cost |
|-----------|-----------|--------------|
| 10 Mbps | 10⁷ | 10 |
| 100 Mbps | 10⁸ | 1 |
| 1 Gbps | 10⁹ | 1* |

*Adjust reference bandwidth for gigabit links

### **OSPF Areas**

```
                    ┌─────────────────┐
                    │    Backbone     │
                    │   Area 0.0.0.0  │
                    └────────┬────────┘
                  ┌──────────┼──────────┐
            ┌─────┴─────┐         ┌─────┴─────┐
            │   Area 1   │         │   Area 2   │
            └───────────┘         └───────────┘
```

**Area Types:**
| Area | Description |
|------|-------------|
| **Backbone (0)** | All areas connect through it |
| **Standard** | Full LSA database |
| **Stub** | No external routes, uses default |
| **Totally Stub** | Only default route |
| **NSSA** | Not-So-Stubby Area |

### **OSPF Router Types**

| Type | Role |
|------|------|
| **Internal Router** | All interfaces in one area |
| **Area Border Router (ABR)** | Interfaces in multiple areas |
| **Backbone Router** | At least one interface in Area 0 |
| **AS Boundary Router (ASBR)** | Connects to external AS |

### **DR/BDR Election**

On multi-access networks (Ethernet):
1. **Designated Router (DR):** Highest priority, then highest Router ID
2. **Backup DR (BDR):** Second highest
3. Others (DROthers) communicate through DR

**Purpose:** Reduce LSA flooding (n routers → n adjacencies, not n²)

### **OSPF Packet Types**

| Type | Name | Purpose |
|------|------|---------|
| 1 | Hello | Discover neighbors, maintain adjacency |
| 2 | DBD (Database Description) | Summary of LSDB |
| 3 | LSR (Link State Request) | Request specific LSAs |
| 4 | LSU (Link State Update) | Send LSAs |
| 5 | LSAck | Acknowledge LSAs |

---

## 6.6 Distance Vector vs Link State

### **Comprehensive Comparison**

| Feature | Distance Vector | Link State |
|---------|-----------------|------------|
| **Knowledge** | Next hop + distance | Full topology |
| **Information shared** | Routing table | Link state |
| **Update trigger** | Periodic | Event-driven |
| **Update scope** | Neighbors only | All routers (flood) |
| **Convergence** | Slow | Fast |
| **Routing loops** | Possible | Rare |
| **CPU usage** | Low | High (SPF) |
| **Memory usage** | Low | High (LSDB) |
| **Bandwidth usage** | Periodic overhead | Initial flood |
| **Algorithm** | Bellman-Ford | Dijkstra |
| **Scalability** | Limited | Good |
| **Examples** | RIP, EIGRP | OSPF, IS-IS |

### **The Mental Model 🧠**

**Distance Vector = "Routing by rumor"**
- "My neighbor says it's 5 hops to X"
- Trust what others tell you

**Link State = "Routing by map"**
- "I have the complete network map"
- Calculate best path myself

---

## 6.7 BGP (Border Gateway Protocol)

### **BGP Overview**

| Feature | Value |
|---------|-------|
| Type | Path Vector (EGP) |
| Transport | TCP port 179 |
| Metric | Path attributes (complex) |
| Purpose | Inter-AS routing |
| Current version | BGP-4 |

### **Why BGP is Different**

- Internet scale (700,000+ routes)
- Policy-based (not just shortest path)
- Business relationships matter
- Incremental updates only

### **BGP Path Attributes**

| Attribute | Type | Description |
|-----------|------|-------------|
| **AS-PATH** | Well-known mandatory | List of ASes traversed |
| **NEXT-HOP** | Well-known mandatory | Next hop IP |
| **ORIGIN** | Well-known mandatory | How route was learned |
| **LOCAL-PREF** | Well-known discretionary | Preference within AS |
| **MED** | Optional non-transitive | Multi-Exit Discriminator |
| **COMMUNITY** | Optional transitive | Route tagging |

### **BGP Path Selection (Simplified)**

1. Highest LOCAL-PREF
2. Shortest AS-PATH
3. Lowest ORIGIN type (IGP < EGP < Incomplete)
4. Lowest MED
5. eBGP over iBGP
6. Lowest IGP cost to next hop
7. Lowest router ID

### **eBGP vs iBGP**

| Feature | eBGP | iBGP |
|---------|------|------|
| Peers | Different AS | Same AS |
| TTL | 1 (direct link) | 255 (any path) |
| Next-hop | Changed | Not changed |
| Full mesh | Not required | Required (or route reflector) |

---

## 6.8 Routing Protocol Summary Table

| Protocol | Type | Algorithm | Metric | Max Hops | Transport |
|----------|------|-----------|--------|----------|-----------|
| **RIPv1** | DV | Bellman-Ford | Hop count | 15 | UDP 520 |
| **RIPv2** | DV | Bellman-Ford | Hop count | 15 | UDP 520 |
| **OSPF** | LS | Dijkstra | Cost | Unlimited | IP 89 |
| **IS-IS** | LS | Dijkstra | Cost | Unlimited | ISO |
| **EIGRP** | Hybrid | DUAL | Composite | 224 | IP 88 |
| **BGP** | Path Vector | Best path | Path attrs | Unlimited | TCP 179 |

---

## 6.9 Solved Examples

### **Example 1: Distance Vector Iteration**

**Problem:** Given the network below, find the routing table at node A after convergence using distance vector.

```
     1       2       1
A ─────── B ─────── C ─────── D
```

**Solution:**

**Initial Tables:**
- A: {A:0, B:1, C:∞, D:∞}
- B: {A:1, B:0, C:2, D:∞}
- C: {A:∞, B:2, C:0, D:1}
- D: {A:∞, B:∞, C:1, D:0}

**After Exchange 1:**
A receives from B: {B:0, C:2}
- A to C via B: 1 + 2 = 3
- A: {A:0, B:1, C:3, D:∞}

**After Exchange 2:**
A receives from B: {C:2, D:3}
- A to D via B: 1 + 3 = 4
- A: {A:0, B:1, C:3, D:4}

**Final Table at A:**
| Dest | Cost | Via |
|------|------|-----|
| A | 0 | - |
| B | 1 | B |
| C | 3 | B |
| D | 4 | B |

---

### **Example 2: Dijkstra's Algorithm**

**Problem:** Find shortest paths from A.

```
        3
   A ──────── B
   │\        │
 2 │ \5     4│
   │  \      │
   C───D─────E
    2     1
```

**Solution:**

| Step | Visited | A | B | C | D | E |
|------|---------|---|---|---|---|---|
| Init | {} | 0 | 3 | 2 | 5 | ∞ |
| 1 | {A} | 0 | 3 | 2 | 5 | ∞ |
| 2 | {A,C} | 0 | 3 | 2 | 4 | ∞ |
| 3 | {A,C,B} | 0 | 3 | 2 | 4 | 7 |
| 4 | {A,C,B,D} | 0 | 3 | 2 | 4 | 5 |
| 5 | {A,C,B,D,E} | 0 | 3 | 2 | 4 | 5 |

**Shortest Paths from A:**
- A→B: 3 (direct)
- A→C: 2 (direct)
- A→D: 4 (via C)
- A→E: 5 (via C,D)

---

### **Example 3: OSPF Cost**

**Problem:** Calculate OSPF cost for a path through interfaces: FastEthernet (100Mbps) → Serial (1.544Mbps) → GigabitEthernet (1Gbps). Reference bandwidth = 100 Mbps.

**Solution:**

Cost = Reference/Bandwidth

- FastEthernet: 100/100 = 1
- Serial: 100/1.544 = 64 (rounded)
- GigabitEthernet: 100/1000 = 1 (minimum is 1)

**Total Path Cost = 1 + 64 + 1 = 66**

---

## 6.10 Practice Problems

**Q1.** RIP uses which of the following?
- (a) Dijkstra's algorithm
- (b) Bellman-Ford algorithm
- (c) Prim's algorithm
- (d) Floyd-Warshall algorithm

<details>
<summary>Answer</summary>
**(b) Bellman-Ford** — RIP is a distance vector protocol
</details>

---

**Q2.** OSPF metric is based on:
- (a) Hop count
- (b) Bandwidth
- (c) Delay
- (d) Both b and c

<details>
<summary>Answer</summary>
**(b) Bandwidth** — Cost = Reference/Bandwidth
</details>

---

**Q3.** [NAT] In RIP, what is the maximum hop count before a destination is considered unreachable?

<details>
<summary>Answer</summary>
$\boxed{16}$ — In RIP, 16 hops means infinity (unreachable)
</details>

---

**Q4.** Which protocol uses TCP for reliable transport?
- (a) RIP
- (b) OSPF
- (c) BGP
- (d) EIGRP

<details>
<summary>Answer</summary>
**(c) BGP** — Uses TCP port 179
</details>

---

**Q5.** In OSPF, what is the purpose of the DR?
- (a) Backup routing
- (b) Reduce flooding overhead
- (c) Faster convergence
- (d) Authentication

<details>
<summary>Answer</summary>
**(b) Reduce flooding overhead** — DR collects and distributes LSAs, reducing n² to n adjacencies
</details>

---

## 6.11 The 5-Second Snap-Check ✅

1. ☐ Distance Vector: Share table with neighbors (RIP = hop count)
2. ☐ Link State: Flood topology, run Dijkstra (OSPF = cost)
3. ☐ RIP: Max 15 hops, UDP 520, 30-sec updates
4. ☐ OSPF: IP protocol 89, areas, DR/BDR on broadcast networks
5. ☐ BGP: TCP 179, AS-PATH, policy-based
6. ☐ Count-to-infinity: Split horizon, poison reverse

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 7: Transport Layer →](./07-Transport-Layer.md)
