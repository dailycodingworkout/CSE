# Chapter 4: Medium Access Control (MAC)
## The Traffic Coordinator | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"MAC protocols decide who talks when on a shared medium."**

---

## 4.1 MAC Problem

### The Challenge
Multiple devices share one channel. How to prevent collisions?

### Classification

```
MAC Protocols
├── Random Access (Contention)
│   ├── ALOHA
│   ├── CSMA
│   ├── CSMA/CD (Ethernet)
│   └── CSMA/CA (WiFi)
├── Controlled Access
│   ├── Reservation
│   ├── Polling
│   └── Token Passing
└── Channelization
    ├── FDMA
    ├── TDMA
    └── CDMA
```

---

## 4.2 ALOHA Protocols

### Pure ALOHA

**Rule:** Transmit whenever you have data. If collision, wait random time and retry.

```
Station A: ──────[Frame]─────────
Station B: ──────────[Frame]─────
                    ↑
                Collision!
```

**Vulnerable Period:** $2 \times T_{frame}$

```
         ←── Vulnerable Period ──→
    ─────[Existing Frame]─────
         [New Frame]
         If new frame starts here, collision!
```

**Throughput:**
$$S = G \cdot e^{-2G}$$

Where:
- S = Successful throughput
- G = Offered load (frames/frame time)

**Maximum Throughput:** At $G = 0.5$
$$S_{max} = \frac{1}{2e} \approx 0.184 = 18.4\%$$

### Slotted ALOHA

**Improvement:** Divide time into slots. Transmit only at slot start.

```
Time slots: |─────|─────|─────|─────|
Station A:  |     |Frame|     |     |
Station B:  |     |Frame|     |     |
                  ↑
             Only here!
```

**Vulnerable Period:** $1 \times T_{frame}$

**Throughput:**
$$S = G \cdot e^{-G}$$

**Maximum Throughput:** At $G = 1$
$$S_{max} = \frac{1}{e} \approx 0.368 = 36.8\%$$

### 🎯 ALOHA Comparison

| Parameter | Pure ALOHA | Slotted ALOHA |
|-----------|------------|---------------|
| Vulnerable time | 2T | T |
| Max throughput | 18.4% | 36.8% |
| Optimal G | 0.5 | 1 |
| Synchronization | Not needed | Required |

---

## 4.3 CSMA Protocols

### CSMA (Carrier Sense Multiple Access)

**Rule:** Listen before transmitting.

"If channel busy, wait. If idle, transmit."

### CSMA Variants

#### 1-Persistent CSMA
```
if (channel == busy) {
    wait until idle;
    transmit immediately;  // Probability 1
}
```
**Problem:** If multiple stations waiting, collision guaranteed!

#### Non-Persistent CSMA
```
if (channel == busy) {
    wait random time;
    sense again;
} else {
    transmit;
}
```
**Better:** Reduces collision probability but may waste channel.

#### p-Persistent CSMA
```
if (channel == idle) {
    transmit with probability p;
    wait one slot with probability (1-p);
} else {
    wait for next slot;
}
```
**Balanced:** Used in slotted channels.

### Why Collisions Still Happen?

**Propagation Delay!**

```
Station A     ──────────────────────    Station B
        └─[Frame]→    ←[Frame]─┘
              Propagation time
              
A senses idle, starts transmitting.
B senses idle (A's signal not yet arrived), also starts.
Collision!
```

---

## 4.4 CSMA/CD (Collision Detection)

### Used in: Ethernet (802.3)

**Rule:** Listen while transmitting. If collision detected, abort and retry.

### Algorithm

```
1. Sense channel
2. If idle, transmit
3. If busy, wait
4. While transmitting, listen for collision
5. If collision detected:
   a. Send JAM signal (48 bits)
   b. Wait random time (backoff)
   c. Retry from step 1
6. If no collision, success!
```

### Minimum Frame Size

To detect collision, frame must be transmitting when collision signal returns.

$$T_{trans} \geq 2 \times T_{prop}$$

$$\frac{L_{min}}{R} \geq 2 \times \frac{d_{max}}{v}$$

$$L_{min} = 2 \times T_{prop} \times R$$

**For Ethernet:**
- Max segment length: 2500 m
- Propagation speed: $2 \times 10^8$ m/s
- Bandwidth: 10 Mbps
- $T_{prop} = \frac{2500 \times 4 \text{ (repeaters)}}{2 \times 10^8} = 51.2 \mu s$
- $L_{min} = 2 \times 51.2 \times 10^{-6} \times 10 \times 10^6 = 512$ bits = **64 bytes**

### Binary Exponential Backoff

After collision $n$:
1. Choose $K$ randomly from $\{0, 1, 2, ..., 2^n - 1\}$
2. Wait $K \times$ slot time (51.2 μs for Ethernet)
3. Retry

**Maximum retries:** 16 (then give up)

| Collision # | Range of K | Max Wait |
|-------------|------------|----------|
| 1 | 0-1 | 1 slot |
| 2 | 0-3 | 3 slots |
| 3 | 0-7 | 7 slots |
| ... | ... | ... |
| 10+ | 0-1023 | 1023 slots |

### CSMA/CD Efficiency

$$\eta = \frac{1}{1 + 5a}$$

Where $a = \frac{T_{prop}}{T_{trans}}$

---

## 4.5 CSMA/CA (Collision Avoidance)

### Used in: WiFi (802.11)

**Why not CD?**
- Wireless: Can't detect collision while transmitting
- Hidden terminal problem
- Exposed terminal problem

### Hidden Terminal Problem

```
    A ─────(range)─────> AP <─────(range)───── B
    
    A cannot hear B.
    Both may transmit to AP simultaneously.
    Collision at AP!
```

### CSMA/CA Algorithm

```
1. Sense channel (DIFS = DCF Interframe Space)
2. If idle for DIFS, transmit
3. If busy, wait until idle + DIFS + random backoff
4. Receiver sends ACK after SIFS (Short IFS)
5. If no ACK, assume collision, retry
```

### RTS/CTS Mechanism (Virtual Carrier Sensing)

```
Sender      Receiver        Others
   │            │              │
   │───RTS─────→│              │
   │            │              │
   │←───CTS─────│──CTS heard──→│
   │            │              │ (NAV set - can't transmit)
   │───DATA────→│              │
   │            │              │
   │←───ACK─────│              │
```

**NAV (Network Allocation Vector):** Virtual timer indicating channel busy.

### Frame Spacing (WiFi Priority)

| Type | Duration | Purpose |
|------|----------|---------|
| SIFS | Shortest | ACK, CTS |
| PIFS | Medium | Polling |
| DIFS | Longest | Normal data |

---

## 4.6 Ethernet (IEEE 802.3)

### Ethernet Frame Format

```
┌──────────┬───────┬──────────┬──────────┬──────┬──────────┬───────┐
│ Preamble │  SFD  │ Dest MAC │ Src MAC  │ Type │   Data   │  FCS  │
│ 7 bytes  │1 byte │ 6 bytes  │ 6 bytes  │2 byte│46-1500 B │4 bytes│
└──────────┴───────┴──────────┴──────────┴──────┴──────────┴───────┘
```

**Preamble:** 10101010... (7 bytes) for synchronization
**SFD:** 10101011 (Start Frame Delimiter)
**Type:** Protocol (0x0800 = IPv4)
**FCS:** CRC-32

### MAC Address

48 bits = 6 bytes, written as XX:XX:XX:XX:XX:XX

```
┌───────────────────┬───────────────────┐
│   OUI (24 bits)   │  Device ID (24)   │
│   Manufacturer    │   Unique ID       │
└───────────────────┴───────────────────┘

First byte, LSB:
- 0 = Unicast
- 1 = Multicast

First byte, 2nd LSB:
- 0 = Global (OUI)
- 1 = Local
```

**Broadcast MAC:** FF:FF:FF:FF:FF:FF

### Ethernet Versions

| Standard | Speed | Name | Medium |
|----------|-------|------|--------|
| 802.3 | 10 Mbps | Ethernet | Coax, UTP |
| 802.3u | 100 Mbps | Fast Ethernet | UTP |
| 802.3z | 1 Gbps | Gigabit Ethernet | Fiber |
| 802.3ab | 1 Gbps | Gigabit Ethernet | UTP Cat5 |
| 802.3ae | 10 Gbps | 10G Ethernet | Fiber |

### Full-Duplex Ethernet

- Separate wires for send and receive
- No collision possible
- No CSMA/CD needed
- Point-to-point (switch ports)

---

## 4.7 Controlled Access Protocols

### Polling

```
Primary (Controller):  ──Poll A──→
Station A:             ←──Data───
Primary:               ──Poll B──→
Station B:             ←──NAK────
Primary:               ──Poll C──→
Station C:             ←──Data───
```

**Pros:** No collision
**Cons:** Polling overhead, single point of failure

### Token Passing

```
Token Ring:
    ┌──[A]──[T]──[B]──┐
    │                 │
    └──[D]─────[C]───┘
    
T = Token (special frame)
Only token holder can transmit.
```

**Token Ring (802.5):**
- Data rate: 4 or 16 Mbps
- Token released after transmission complete

**FDDI (Fiber Distributed Data Interface):**
- Data rate: 100 Mbps
- Dual ring for fault tolerance

---

## 4.8 Channelization Protocols

### FDMA (Frequency Division)

Each station gets a frequency band.
- Used in: Radio, old cellular
- Simple but fixed allocation

### TDMA (Time Division)

Each station gets time slots.
- Used in: GSM cellular
- Requires synchronization

### CDMA (Code Division)

Each station uses unique code.
- All transmit simultaneously at same frequency
- Receiver filters using code
- Used in: 3G cellular, GPS

---

## 🎯 Practice Problems

### Problem 1: Pure ALOHA
**Q:** Pure ALOHA with G = 0.5. Find throughput.
**Solution:** $S = 0.5 \times e^{-1} = 0.184 = 18.4\%$

### Problem 2: Slotted ALOHA
**Q:** Slotted ALOHA with G = 2. Find throughput.
**Solution:** $S = 2 \times e^{-2} = 0.27 = 27\%$

### Problem 3: Minimum Frame Size
**Q:** Ethernet at 100 Mbps, max distance 1 km, speed $2 \times 10^8$ m/s. Min frame size?
**Solution:**
- $T_{prop} = \frac{1000}{2 \times 10^8} = 5 \mu s$
- $L_{min} = 2 \times 5 \times 10^{-6} \times 100 \times 10^6 = 1000$ bits = **125 bytes**

### Problem 4: CSMA/CD Efficiency
**Q:** $T_{prop} = 10 \mu s$, $T_{trans} = 50 \mu s$. Find CSMA/CD efficiency.
**Solution:**
- $a = \frac{10}{50} = 0.2$
- $\eta = \frac{1}{1 + 5 \times 0.2} = \frac{1}{2} = 50\%$

### Problem 5: Backoff
**Q:** After 3rd collision in CSMA/CD, what's the maximum wait time?
**Solution:** $K \in \{0, 1, ..., 7\}$, max = 7 slot times

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"ALOHA Always Loses Half of All"** (18% efficiency)
**"Slotted ALOHA Saves Some - 36%"**
**"CSMA - Carrier Sense, Manner Acquired"**

### The Mental Slider
- **Pure ALOHA:** Shout whenever you want
- **Slotted ALOHA:** Shout only when bell rings
- **CSMA:** Listen before speaking
- **CSMA/CD:** Stop if interrupted
- **CSMA/CA:** Ask permission first (RTS/CTS)

### The 5-Second Snap-Check
1. **Pure ALOHA max?** 18.4% at G=0.5
2. **Slotted ALOHA max?** 36.8% at G=1
3. **Ethernet min frame?** 64 bytes
4. **CSMA/CD efficiency?** 1/(1+5a)
5. **WiFi protocol?** CSMA/CA

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| $S = G \cdot e^{-2G}$ | Pure ALOHA throughput |
| $S = G \cdot e^{-G}$ | Slotted ALOHA throughput |
| $L_{min} = 2 \times T_{prop} \times R$ | Minimum frame size |
| $\eta = \frac{1}{1+5a}$ | CSMA/CD efficiency |
| Backoff: $K \in [0, 2^n-1]$ | After n collisions |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Data Link Layer](03-Data-Link-Layer.md) | [Next: Network Layer →](05-Network-Layer.md)
