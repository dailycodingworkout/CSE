# Module 4: LAN Technologies | The Singularity

> **The Atomic Truth:** *LAN = Local high-speed shared-medium network*

---

## 4.1 Ethernet Evolution

### **IEEE 802.3 Family Tree**

```
              ETHERNET EVOLUTION
                     │
         ┌───────────┼───────────┐
         │           │           │
    10 Mbps      100 Mbps     1000+ Mbps
         │           │           │
  10Base5 (Thick)    │      1000Base-T
  10Base2 (Thin)  100Base-TX  10GBase-T
  10Base-T        100Base-FX  40/100 GbE
```

### **Naming Convention**
```
<Speed><Signaling><Segment/Type>

Example: 100Base-TX
         │   │  └── Twisted pair, category X
         │   └───── Baseband signaling
         └───────── 100 Mbps
```

### **Common Ethernet Standards**

| Standard | Speed | Medium | Max Distance |
|----------|-------|--------|--------------|
| 10Base5 | 10 Mbps | Thick Coax | 500m |
| 10Base2 | 10 Mbps | Thin Coax | 185m |
| 10Base-T | 10 Mbps | UTP Cat3 | 100m |
| 100Base-TX | 100 Mbps | UTP Cat5 | 100m |
| 100Base-FX | 100 Mbps | Fiber | 2km |
| 1000Base-T | 1 Gbps | UTP Cat5e/6 | 100m |
| 1000Base-SX | 1 Gbps | MMF | 550m |
| 1000Base-LX | 1 Gbps | SMF | 5km |
| 10GBase-T | 10 Gbps | Cat6a/7 | 100m |

---

## 4.2 Ethernet Frame Format

### **IEEE 802.3 Frame**

```
┌──────────┬──────────┬───────┬───────┬──────┬────────┬─────────┬─────┐
│ Preamble │   SFD    │ Dest  │ Source│Length│  Data  │ Padding │ FCS │
│  7 bytes │ 1 byte   │  MAC  │  MAC  │/Type │        │         │     │
│  101010..│10101011  │6 bytes│6 bytes│2bytes│46-1500 │ if <46  │4byte│
└──────────┴──────────┴───────┴───────┴──────┴────────┴─────────┴─────┘
            │
            └── Start Frame Delimiter: 10101011
```

### **Key Frame Parameters**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| **Min frame** | 64 bytes | Collision detection guarantee |
| **Max frame** | 1518 bytes | Shared medium fairness |
| **Min data** | 46 bytes | Pad if smaller |
| **Max data** | 1500 bytes | MTU (Maximum Transmission Unit) |
| **Preamble + SFD** | 8 bytes | Synchronization (not counted in frame size) |

### **GATE Trap Alert ⚠️**

**Frame Size Calculation:**
- **Without preamble:** 64-1518 bytes
- **With preamble:** 72-1526 bytes
- **Data payload:** 46-1500 bytes

**Question variations:**
- "Minimum frame size" = 64 bytes (excluding preamble)
- "Minimum data size" = 46 bytes
- "What gets padded?" = Data < 46 bytes

---

## 4.3 MAC Addressing

### **MAC Address Structure**

```
48 bits (6 bytes)
┌─────────────────────────────────────────────────────────────┐
│ AA : BB : CC : DD : EE : FF                                 │
├───────────────────────┬─────────────────────────────────────┤
│   OUI (24 bits)       │   Device ID (24 bits)               │
│   Vendor/Manufacturer │   Unique per device                 │
└───────────────────────┴─────────────────────────────────────┘
         │
         └── First byte, bit 0: 0 = Unicast, 1 = Multicast
             First byte, bit 1: 0 = Global, 1 = Local
```

### **Special Addresses**

| Address | Type | Purpose |
|---------|------|---------|
| FF:FF:FF:FF:FF:FF | Broadcast | All devices on LAN |
| 01:00:5E:xx:xx:xx | Multicast | IP multicast mapping |
| 00:00:00:00:00:00 | Null | Invalid/Unknown |

### **MAC vs IP Address**

| Feature | MAC Address | IP Address |
|---------|-------------|------------|
| Layer | 2 (Data Link) | 3 (Network) |
| Size | 48 bits | 32 bits (IPv4) |
| Scope | Local LAN | Global/Hierarchical |
| Changes | Fixed (burned-in) | Configurable |
| Example | AA:BB:CC:DD:EE:FF | 192.168.1.1 |

---

## 4.4 CSMA/CD in Ethernet

### **Algorithm**

```
┌─────────────────────────────────────────────────────────────┐
│                    CSMA/CD ALGORITHM                         │
├─────────────────────────────────────────────────────────────┤
│  1. Frame ready → Sense channel                              │
│  2. If channel busy → Wait until idle                        │
│  3. If channel idle → Transmit immediately (1-persistent)    │
│  4. While transmitting → Monitor for collision               │
│  5. If collision detected:                                   │
│     a. Stop transmission                                     │
│     b. Send jam signal (48 bits)                            │
│     c. Wait random time (Binary Exponential Backoff)        │
│     d. Go to step 1                                         │
│  6. If no collision → Success!                               │
└─────────────────────────────────────────────────────────────┘
```

### **Binary Exponential Backoff (BEB)**

After $k$ collisions:
- Wait random time in range $[0, 2^k - 1]$ slot times
- $k$ capped at 10 (max wait = 1023 slots)
- After 16 collisions → Abort and report error

**Slot Time = 51.2 μs** (for 10 Mbps Ethernet)

### **Minimum Frame Size Derivation 🔑**

**Requirement:** Sender must be transmitting when collision signal returns

$$T_{transmission} \geq 2 \times T_{propagation}$$

$$\frac{Frame_{min}}{Bandwidth} \geq 2 \times \frac{d_{max}}{v}$$

**For 10 Mbps Ethernet:**
- $d_{max}$ = 2500m (with repeaters)
- $v$ = 2 × 10⁸ m/s
- $RTT$ = 51.2 μs (Round Trip Time)

$$Frame_{min} = 10 \times 10^6 \times 51.2 \times 10^{-6} = 512 \text{ bits} = 64 \text{ bytes}$$

### **GATE NAT Precision Lock 🔒**

**Given:** Network length, bandwidth, propagation speed
**Find:** Minimum frame size

$$Frame_{min} = 2 \times \frac{d}{v} \times B$$

**Example:** d = 2 km, v = 2×10⁸ m/s, B = 100 Mbps
$$Frame_{min} = 2 \times \frac{2000}{2 \times 10^8} \times 100 \times 10^6 = 2000 \text{ bits} = 250 \text{ bytes}$$

---

## 4.5 Ethernet Efficiency

### **Theoretical Maximum Efficiency**

$$\eta = \frac{1}{1 + \frac{5T_p}{T_t}} = \frac{1}{1 + 5a}$$

Where $a = \frac{T_p}{T_t}$

**For optimal (large frames, short distance):** η → 100%
**For worst case (small frames, long distance):** η → very low

### **Practical Factors Affecting Efficiency**
1. Collision overhead
2. Inter-frame gap (96 bit times)
3. Preamble and SFD (64 bits)
4. Exponential backoff delays

---

## 4.6 Ethernet Devices

### **Layer 1: Hub (Repeater)**

```
        ┌─────────────────┐
     ───┤                 ├───
        │      HUB        │     All ports in ONE
     ───┤                 ├───  collision domain
        │  (Broadcasts)   │
     ───┤                 ├───
        └─────────────────┘
```

**Characteristics:**
- Physical layer device
- Regenerates signals
- All ports = ONE collision domain
- All ports = ONE broadcast domain
- No intelligence (doesn't read MAC)

### **Layer 2: Bridge/Switch**

```
        ┌─────────────────┐
     ───┤                 ├───
        │     SWITCH      │     Each port is
     ───┤                 ├───  SEPARATE collision
        │  (Learns MACs)  │     domain
     ───┤                 ├───
        └─────────────────┘
```

**Characteristics:**
- Data Link layer device
- Learns MAC addresses (MAC table)
- Each port = SEPARATE collision domain
- All ports = SAME broadcast domain
- Filters and forwards based on MAC

### **Layer 3: Router**

```
        ┌─────────────────┐
     ───┤                 ├───
        │     ROUTER      │     Each port is
     ───┤                 ├───  SEPARATE broadcast
        │  (Routes IP)    │     domain
     ───┤                 ├───
        └─────────────────┘
```

**Characteristics:**
- Network layer device
- Routes based on IP address
- Each interface = SEPARATE broadcast domain
- Blocks broadcast by default

### **Domain Summary**

| Device | Collision Domains | Broadcast Domains |
|--------|-------------------|-------------------|
| Hub (N ports) | 1 | 1 |
| Switch (N ports) | N | 1 |
| Router (N ports) | N | N |

### **GATE Trap Alert ⚠️**

**Calculating domains in a network:**

Given: 2 routers, 3 switches (8 ports each), 2 hubs (4 ports each)

**Broadcast Domains:**
- Each router interface = separate broadcast domain
- Count router interfaces connecting different networks

**Collision Domains:**
- Each switch port = 1 collision domain
- Hub with all connected = 1 collision domain
- Each router port = 1 collision domain

---

## 4.7 Switching in Bridges/Switches

### **Learning Process**

```
1. Frame arrives on Port 1 from MAC A
   → Learn: A is on Port 1

2. Frame destination is MAC B
   → If B known → Forward to B's port
   → If B unknown → Flood to all ports (except 1)

3. When B replies → Learn: B is on Port 2
```

### **Switching Methods**

| Method | Latency | Error Checking | Use Case |
|--------|---------|----------------|----------|
| **Store-and-Forward** | Highest | Full (CRC) | Reliable |
| **Cut-Through** | Lowest | None | Speed-critical |
| **Fragment-Free** | Medium | First 64 bytes | Balanced |

### **Spanning Tree Protocol (STP)**

**Problem:** Loops in switched network → Broadcast storms

**Solution:** STP (IEEE 802.1D) creates loop-free logical topology

**Process:**
1. Elect Root Bridge (lowest Bridge ID)
2. Calculate Root Path Cost
3. Select Root Port (best path to root)
4. Select Designated Port (one per segment)
5. Block other ports

---

## 4.8 Virtual LANs (VLANs)

### **The Concept**

```
Physical Network:          Logical VLANs:
                          
 [PC1]──┐                  VLAN 10: [PC1] [PC3]
        ├──[Switch]        VLAN 20: [PC2] [PC4]
 [PC2]──┤    │
        │    │             Different broadcast domains
 [PC3]──┤    │             on same physical switch
        ├────┘
 [PC4]──┘
```

### **VLAN Benefits**
1. ✅ Logical grouping (by dept, function)
2. ✅ Broadcast control
3. ✅ Security (isolation)
4. ✅ Flexibility (move without rewiring)

### **VLAN Tagging (802.1Q)**

```
Standard Frame:
┌──────┬──────┬──────┬──────┬──────┬─────┐
│ Dest │ Src  │ Type │ Data │ Pad  │ FCS │
└──────┴──────┴──────┴──────┴──────┴─────┘

802.1Q Tagged Frame:
┌──────┬──────┬─────────────┬──────┬──────┬─────┬─────┐
│ Dest │ Src  │ 802.1Q Tag  │ Type │ Data │ Pad │ FCS │
│      │      │   (4 bytes) │      │      │     │     │
└──────┴──────┴─────────────┴──────┴──────┴─────┴─────┘
                    │
         ┌──────────┴──────────┐
         │ TPID (0x8100) │ TCI │
         │   2 bytes    │2 bytes│
         └───────────────┴──────┘
                          │
              ┌───────────┴───────────┐
              │ PRI │ CFI │   VID     │
              │ 3b  │ 1b  │   12 bits │
              └─────┴─────┴───────────┘

VID = VLAN ID (1-4094)
```

**Maximum VLANs:** $2^{12} = 4096$ (0 and 4095 reserved, so 4094 usable)

---

## 4.9 Wireless LAN (802.11)

### **Architecture**

```
      Infrastructure Mode:              Ad-Hoc Mode:
      
         ┌─────┐                         [STA1]
         │ AP  │                            │
         └──┬──┘                         [STA2]
        ╱   │   ╲                           │
    [STA] [STA] [STA]                    [STA3]
    
    BSS (Basic Service Set)          IBSS (Independent BSS)
```

### **802.11 Standards Comparison**

| Standard | Frequency | Max Speed | Channel Width |
|----------|-----------|-----------|---------------|
| 802.11a | 5 GHz | 54 Mbps | 20 MHz |
| 802.11b | 2.4 GHz | 11 Mbps | 22 MHz |
| 802.11g | 2.4 GHz | 54 Mbps | 20 MHz |
| 802.11n | 2.4/5 GHz | 600 Mbps | 20/40 MHz |
| 802.11ac | 5 GHz | 6.93 Gbps | 80/160 MHz |
| 802.11ax | 2.4/5/6 GHz | 9.6 Gbps | 20-160 MHz |

### **CSMA/CA in WiFi**

**Why CSMA/CD won't work:**
1. **Hidden Terminal Problem:** A can't hear C, but both reach B
2. **Exposed Terminal Problem:** B hears A, thinks busy, but could send to C

**Solution: RTS/CTS**

```
Time →
A: ─────[RTS]─────────────────────[DATA]──────────
B: ──────────[CTS]─────────────────────────[ACK]──
             │
             └── NAV (Network Allocation Vector)
                 Others defer for this duration
```

### **Hidden Terminal Problem**

```
    [A] ─────────── [B] ─────────── [C]
         Radio          Radio
         Range          Range
         
A and C cannot hear each other
Both try to send to B → Collision at B
```

**Solution:** RTS/CTS mechanism ensures B broadcasts availability

---

## 4.10 Key Formulas Summary

| Topic | Formula |
|-------|---------|
| Min frame size | $2 \times \frac{d}{v} \times B$ |
| Ethernet efficiency | $\frac{1}{1 + 5a}$ |
| Collision domains (N-port switch) | N |
| Broadcast domains (switch) | 1 |
| Max VLANs (802.1Q) | 4094 |

---

## 4.11 Solved Examples

### **Example 1: Minimum Frame Size**

**Problem:** A 10 Mbps Ethernet has maximum distance 2 km with propagation speed 2×10⁸ m/s. Find minimum frame size.

**Solution:**
$$Frame_{min} = 2 \times \frac{d}{v} \times B$$
$$= 2 \times \frac{2000}{2 \times 10^8} \times 10 \times 10^6$$
$$= 2 \times 10^{-5} \times 10^7 = 200 \text{ bits} = \boxed{25 \text{ bytes}}$$

---

### **Example 2: Domain Counting**

**Problem:** A network has 1 router with 3 interfaces, 2 switches (10 ports each), and 1 hub (4 ports). Find:
(a) Collision domains
(b) Broadcast domains

**Solution:**
(a) **Collision domains:**
- Router: 3 (one per interface)
- Switches: 10 + 10 = 20 (one per port)
- Hub: 1 (all ports share)
- Total: 3 + 20 + 1 = **24** (but subtract connections between devices)

(b) **Broadcast domains:**
- Router separates: 3 broadcast domains (one per interface)

---

### **Example 3: Ethernet Efficiency**

**Problem:** Calculate efficiency for 1 Gbps Ethernet with:
- Frame size = 1500 bytes
- Propagation delay = 25 μs

**Solution:**
$T_t = \frac{1500 \times 8}{10^9} = 12$ μs

$a = \frac{T_p}{T_t} = \frac{25}{12} = 2.08$

$\eta = \frac{1}{1 + 5a} = \frac{1}{1 + 10.4} = \boxed{8.77\%}$

This shows why Gigabit Ethernet uses full-duplex (no CSMA/CD needed)!

---

## 4.12 Practice Problems

**Q1.** The minimum frame size in Ethernet is:
- (a) 46 bytes
- (b) 64 bytes
- (c) 72 bytes
- (d) 1518 bytes

<details>
<summary>Answer</summary>
**(b) 64 bytes** — Minimum frame size (excluding preamble/SFD)
</details>

---

**Q2.** How many broadcast domains are created by a 24-port switch?
- (a) 24
- (b) 1
- (c) 0
- (d) 23

<details>
<summary>Answer</summary>
**(b) 1** — A switch does not separate broadcast domains (without VLANs)
</details>

---

**Q3.** [NAT] With 3-bit VLAN ID, maximum VLANs possible is:

<details>
<summary>Answer</summary>
$2^3 = \boxed{8}$ (but 802.1Q uses 12 bits = 4096)
</details>

---

**Q4.** Which problem does RTS/CTS solve?
- (a) Collision detection
- (b) Hidden terminal
- (c) Frame fragmentation
- (d) IP addressing

<details>
<summary>Answer</summary>
**(b) Hidden terminal** — RTS/CTS ensures medium reservation is broadcast
</details>

---

## 4.13 The 5-Second Snap-Check ✅

1. ☐ Ethernet min frame = 64 bytes (data min = 46)
2. ☐ MAC address = 48 bits (6 bytes)
3. ☐ Hub = 1 collision domain; Switch = N collision domains
4. ☐ VLAN tag (802.1Q) = 4 bytes, VID = 12 bits
5. ☐ WiFi uses CSMA/CA (not CD)
6. ☐ RTS/CTS solves hidden terminal problem

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 5: Network Layer →](./05-Network-Layer.md)
