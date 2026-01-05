# Module 2: Physical Layer | The Singularity

> **The Atomic Truth:** *Physical Layer = Bits on Wire*

---

## 2.1 Physical Layer Overview

### **Core Responsibility**
The Physical Layer (Layer 1) is responsible for the **transmission and reception of raw bit streams** over a physical medium.

### **Key Functions**
1. **Bit-by-bit delivery** between nodes
2. **Encoding/Decoding** signals
3. **Bit rate control** (transmission rate)
4. **Bit synchronization** (clock synchronization)
5. **Physical topology** definition
6. **Transmission mode** (simplex, half-duplex, full-duplex)

### **The Analogy 💡**
Physical Layer is like the **postal truck** — it doesn't care what's in the envelope (data), it just physically moves it from point A to point B.

---

## 2.2 Transmission Media

### **Classification**

```
                    TRANSMISSION MEDIA
                          │
           ┌──────────────┴──────────────┐
           │                             │
      GUIDED                         UNGUIDED
    (Wired)                        (Wireless)
           │                             │
    ┌──────┼──────┐             ┌────────┼────────┐
    │      │      │             │        │        │
 Twisted  Coax  Fiber        Radio  Microwave  Infrared
  Pair   Cable  Optic        Waves
```

### **2.2.1 Twisted Pair Cable**

| Type | Full Form | Speed | Distance | Use Case |
|------|-----------|-------|----------|----------|
| **UTP** | Unshielded Twisted Pair | Up to 10 Gbps | 100m | LAN, Ethernet |
| **STP** | Shielded Twisted Pair | Up to 10 Gbps | 100m | Noisy environments |

**Categories:**
| Category | Max Speed | Frequency | Application |
|----------|-----------|-----------|-------------|
| Cat 5 | 100 Mbps | 100 MHz | Fast Ethernet |
| Cat 5e | 1 Gbps | 100 MHz | Gigabit Ethernet |
| Cat 6 | 10 Gbps (55m) | 250 MHz | 10GBase-T |
| Cat 6a | 10 Gbps (100m) | 500 MHz | Data Centers |
| Cat 7 | 10 Gbps | 600 MHz | High-speed networks |

**Why Twisted?**
> Twisting reduces **electromagnetic interference (EMI)** by canceling out induced noise signals.

### **2.2.2 Coaxial Cable**

| Component | Function |
|-----------|----------|
| Inner conductor | Carries signal |
| Insulator | Separates conductors |
| Outer conductor (shield) | Reduces EMI |
| Outer jacket | Physical protection |

**Types:**
- **RG-58** (Thinnet): 10Base2, 185m max
- **RG-8** (Thicknet): 10Base5, 500m max
- **RG-59**: Cable TV
- **RG-6**: Digital Cable/Satellite

### **2.2.3 Fiber Optic Cable**

| Type | Core Size | Light Source | Distance | Bandwidth |
|------|-----------|--------------|----------|-----------|
| **Single-Mode (SMF)** | 8-10 μm | Laser | Up to 100+ km | Very High |
| **Multi-Mode (MMF)** | 50-62.5 μm | LED | Up to 2 km | High |

**The Aha Moment 💡**
- **Single-mode** = One light path = No dispersion = Long distance
- **Multi-mode** = Multiple light paths = Modal dispersion = Short distance

**Advantages of Fiber:**
1. ✅ Immune to EMI
2. ✅ Very high bandwidth (Tbps)
3. ✅ Long distances
4. ✅ Secure (hard to tap)
5. ✅ Lightweight

**Disadvantages:**
1. ❌ Expensive
2. ❌ Fragile
3. ❌ Difficult to install

### **2.2.4 Wireless Media Comparison**

| Type | Frequency | Range | Use Case |
|------|-----------|-------|----------|
| **Radio Waves** | 3 KHz - 1 GHz | Long | AM/FM radio, WiFi |
| **Microwaves** | 1 GHz - 300 GHz | Line-of-sight | Satellite, cellular |
| **Infrared** | 300 GHz - 400 THz | Short | TV remote, IrDA |

---

## 2.3 Signal Fundamentals

### **Analog vs Digital Signals**

| Aspect | Analog | Digital |
|--------|--------|---------|
| Form | Continuous wave | Discrete pulses |
| Values | Infinite | Finite (0s and 1s) |
| Noise immunity | Low | High |
| Example | Human voice | Computer data |

### **Signal Parameters**

```
    Amplitude (A)
         │
    A ───┼───────────────────────────
         │    ╱╲      ╱╲      ╱╲
         │   ╱  ╲    ╱  ╲    ╱  ╲
    0 ───┼──╱────╲──╱────╲──╱────╲── Time
         │ ╱      ╲╱      ╲╱      ╲
   -A ───┼─────────────────────────
         │
         │←─ Period (T) ─→│
         │←─────── Wavelength (λ) ─────────→│
```

**Key Formulas:**

$$f = \frac{1}{T} \text{ (Frequency in Hz)}$$

$$\lambda = \frac{v}{f} \text{ (Wavelength)}$$

$$v = \lambda \times f \text{ (Propagation velocity)}$$

### **Bandwidth**

**Analog Bandwidth:** Range of frequencies a medium can carry (Hz)

**Digital Bandwidth:** Bit rate the medium can support (bps)

**Nyquist Theorem (Noiseless Channel):**
$$C = 2B \log_2 L$$

Where:
- $C$ = Maximum bit rate (bps)
- $B$ = Bandwidth (Hz)
- $L$ = Number of signal levels

**Shannon's Theorem (Noisy Channel):**
$$C = B \log_2 (1 + SNR)$$

Where:
- $SNR$ = Signal-to-Noise Ratio (linear, not dB)
- $SNR_{dB} = 10 \log_{10}(SNR)$

### **GATE Trap Alert ⚠️**

**Converting SNR from dB to linear:**
$$SNR = 10^{SNR_{dB}/10}$$

**Example:** SNR = 30 dB means $SNR = 10^{30/10} = 10^3 = 1000$

---

## 2.4 Digital Transmission

### **2.4.1 Line Coding Schemes**

**The Purpose:** Convert binary data to digital signals

```
Binary Data:    1   0   1   1   0   0   1   0

NRZ-L:       ─┐   ┌─┐   ┌───┐   ┌───┐   ┌─
             └───┘ └───┘   └───┘   └───┘

NRZ-I:       ─┐   ┌───────┐       ┌───────┐
             └───┘       └───────┘       └─
             (Transition on 1)

Manchester:   ┌┐ ┌┐┌┐ ┌┐┌┐ ┌┐ ┌┐┌┐ ┌┐ ┌┐
             ─┘└─┘└┘└─┘└┘└─┘└─┘└┘└─┘└─┘└─
             (1=high-to-low, 0=low-to-high)

Differential 
Manchester:   ┌─┐ ┌─┐ ┌─┐   ┌─┐   ┌─┐ ┌─┐
             ─┘ └─┘ └─┘ └───┘ └───┘ └─┘ └─
             (Always mid-bit transition; 
              edge transition = 0)
```

### **Line Coding Comparison**

| Scheme | Self-clocking | DC Component | Bandwidth | GATE Frequency |
|--------|---------------|--------------|-----------|----------------|
| **NRZ-L** | No | Yes | Low | ⭐⭐ |
| **NRZ-I** | Partial | Yes | Low | ⭐⭐ |
| **RZ** | Yes | Yes | High | ⭐ |
| **Manchester** | Yes | No | 2× data rate | ⭐⭐⭐⭐ |
| **Differential Manchester** | Yes | No | 2× data rate | ⭐⭐⭐ |
| **AMI** | Partial | No | Low | ⭐⭐ |
| **B8ZS/HDB3** | Yes | No | Low | ⭐⭐⭐ |

### **The Golden Insight 💡**

**Why Manchester encoding is used in Ethernet:**
1. Self-clocking (transition in every bit)
2. No DC component (can use transformers)
3. Easy error detection

**Trade-off:** Requires 2× bandwidth

### **2.4.2 Block Coding**

**Purpose:** Add redundancy for synchronization and error detection

| Code | Data Bits | Transmitted | Efficiency | Use |
|------|-----------|-------------|------------|-----|
| 4B/5B | 4 | 5 | 80% | Fast Ethernet |
| 8B/10B | 8 | 10 | 80% | Gigabit Ethernet |
| 64B/66B | 64 | 66 | 97% | 10 Gigabit Ethernet |

---

## 2.5 Analog Transmission

### **2.5.1 Digital-to-Analog Conversion**

**The Challenge:** Send digital data over analog medium (like telephone lines)

#### **Amplitude Shift Keying (ASK)**

```
Binary:  1   0   1   1   0   0   1
         ╱╲     ╱╲ ╱╲         ╱╲
Signal: ╱  ╲───╱  ╲  ╲───────╱  ╲
```

- Amplitude changes based on bit value
- Susceptible to noise
- Used in fiber optics (on/off)

**Bandwidth:** $B = (1 + d) \times S$ where $d$ = factor (0-1), $S$ = signal rate

#### **Frequency Shift Keying (FSK)**

```
Binary:  1   0   1   1   0   0   1
        ∿∿∿ ~~~ ∿∿∿ ∿∿∿ ~~~ ~~~ ∿∿∿
        (f1) (f2) (f1)(f1)(f2)(f2)(f1)
```

- Different frequencies for 0 and 1
- More immune to noise than ASK
- Used in modems, Caller ID

**Bandwidth:** $B = (1 + d) \times S + 2\Delta f$

#### **Phase Shift Keying (PSK)**

```
BPSK (2-PSK):
  0 = 0°    1 = 180°

QPSK (4-PSK):
  00 = 45°   01 = 135°   10 = 225°   11 = 315°
```

**Bits per symbol:**
$$\text{Bits/symbol} = \log_2(\text{Number of phases})$$

| Type | Phases | Bits/Symbol | Bandwidth Efficiency |
|------|--------|-------------|---------------------|
| BPSK | 2 | 1 | 1 bps/Hz |
| QPSK | 4 | 2 | 2 bps/Hz |
| 8-PSK | 8 | 3 | 3 bps/Hz |
| 16-PSK | 16 | 4 | 4 bps/Hz |

#### **Quadrature Amplitude Modulation (QAM)**

Combines ASK and PSK — varies both amplitude and phase.

| Type | Points | Bits/Symbol | Use Case |
|------|--------|-------------|----------|
| 16-QAM | 16 | 4 | WiFi, Cable |
| 64-QAM | 64 | 6 | Digital Cable |
| 256-QAM | 256 | 8 | DOCSIS 3.0 |
| 1024-QAM | 1024 | 10 | WiFi 6 |

### **The Master Formula for Bit Rate 🔑**

$$\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Symbol}$$

$$\text{Bit Rate} = \text{Baud Rate} \times \log_2 L$$

Where:
- Baud Rate = Symbols per second
- L = Number of signal levels/symbols

### **GATE Trap Alert ⚠️**

**Baud Rate ≠ Bit Rate**
- **Baud Rate** = Symbol rate (symbols/sec)
- **Bit Rate** = Data rate (bits/sec)
- They are equal ONLY when L = 2 (1 bit per symbol)

---

## 2.6 Multiplexing

### **The Atomic Truth:** *Multiplexing = Many signals, one channel*

### **Types of Multiplexing**

```
         MULTIPLEXING TECHNIQUES
                  │
    ┌─────────────┼─────────────┐
    │             │             │
   FDM           TDM           WDM
(Frequency)    (Time)      (Wavelength)
    │             │             │
    │      ┌──────┴──────┐      │
    │      │             │      │
    │   Sync TDM    Async TDM   │
    │                (StatTDM)  │
```

### **2.6.1 Frequency Division Multiplexing (FDM)**

```
Frequency
    ↑
    │  ┌────┐ ┌────┐ ┌────┐ ┌────┐
    │  │ C1 │ │ C2 │ │ C3 │ │ C4 │
    │  └────┘ └────┘ └────┘ └────┘
    │    f1     f2     f3     f4
    └─────────────────────────────→ Time
```

- Each channel gets a unique frequency band
- Guard bands prevent interference
- **Used in:** Radio, Cable TV, ADSL

**Total Bandwidth = Sum of channel bandwidths + Guard bands**

### **2.6.2 Time Division Multiplexing (TDM)**

```
Time
    │
    │  ┌───┬───┬───┬───┬───┬───┬───┬───┐
    │  │C1 │C2 │C3 │C4 │C1 │C2 │C3 │C4 │
    │  └───┴───┴───┴───┴───┴───┴───┴───┘
    │    Frame 1          Frame 2
    └─────────────────────────────────────→
```

**Synchronous TDM:**
- Fixed time slots for each channel
- Slot wasted if channel has no data
- Example: T1 line (24 channels × 8 bits = 192 bits/frame)

**Statistical (Async) TDM:**
- Slots assigned dynamically based on need
- More efficient but requires addressing overhead
- Example: Packet switching

### **2.6.3 Wavelength Division Multiplexing (WDM)**

- FDM for fiber optic (different wavelengths of light)
- **DWDM** (Dense WDM): 80+ channels
- **CWDM** (Coarse WDM): Fewer channels, cheaper

---

## 2.7 Key Formulas Summary

### **Nyquist & Shannon**

| Theorem | Formula | When to Use |
|---------|---------|-------------|
| Nyquist (Noiseless) | $C = 2B \log_2 L$ | Ideal channel |
| Shannon (Noisy) | $C = B \log_2(1 + SNR)$ | Real channel |

**The Golden Rule:**
> Maximum channel capacity = **min(Nyquist, Shannon)**

### **Transmission Calculations**

| Parameter | Formula |
|-----------|---------|
| Bit Rate | $\text{Baud Rate} \times \log_2 L$ |
| Propagation Delay | $\frac{\text{Distance}}{\text{Speed}}$ |
| Transmission Delay | $\frac{\text{Data Size}}{\text{Bandwidth}}$ |

### **Propagation Speeds**

| Medium | Speed |
|--------|-------|
| Vacuum/Air | $3 \times 10^8$ m/s |
| Copper | $2 \times 10^8$ m/s (approx. $\frac{2}{3}c$) |
| Fiber | $2 \times 10^8$ m/s |

---

## 2.8 Solved Examples

### **Example 1: Nyquist Theorem**

**Problem:** A noiseless channel has a bandwidth of 4000 Hz. If we use 8 signal levels, what is the maximum bit rate?

**Solution:**
$C = 2B \log_2 L = 2 \times 4000 \times \log_2 8 = 8000 \times 3 = \boxed{24000 \text{ bps}}$

---

### **Example 2: Shannon's Theorem**

**Problem:** A channel has bandwidth of 3 kHz and SNR of 30 dB. Find the maximum capacity.

**Solution:**
First, convert SNR from dB to linear:
$SNR = 10^{30/10} = 10^3 = 1000$

$C = B \log_2(1 + SNR) = 3000 \times \log_2(1001)$

$\log_2(1001) \approx \log_2(1024) \approx 10$

$C \approx 3000 \times 10 = \boxed{30000 \text{ bps}}$

---

### **Example 3: Baud Rate vs Bit Rate**

**Problem:** A QPSK system has a baud rate of 4000. What is the bit rate?

**Solution:**
QPSK uses 4 signal levels (phases), so each symbol carries $\log_2 4 = 2$ bits.

Bit Rate = Baud Rate × Bits per symbol = $4000 \times 2 = \boxed{8000 \text{ bps}}$

---

### **Example 4: Channel Capacity Comparison**

**Problem:** A channel has B = 4 kHz and SNR = 30 dB. If we use 256 signal levels, what is the achievable bit rate?

**Solution:**
**Nyquist:** $C_N = 2 \times 4000 \times \log_2 256 = 8000 \times 8 = 64000$ bps

**Shannon:** $C_S = 4000 \times \log_2(1 + 1000) \approx 4000 \times 10 = 40000$ bps

**Actual Maximum = min(64000, 40000) = $\boxed{40000 \text{ bps}}$**

**Insight:** Even though we can theoretically send 64 kbps with 256 levels, the noise limits us to 40 kbps.

---

## 2.9 Practice Problems

### **NAT Type Questions**

**Q1.** A channel has bandwidth 10 MHz and SNR = 63. Calculate the maximum channel capacity in Mbps.

<details>
<summary>Answer</summary>

$C = B \log_2(1 + SNR) = 10 \times 10^6 \times \log_2(64) = 10 \times 10^6 \times 6 = \boxed{60}$ Mbps
</details>

---

**Q2.** In Manchester encoding, if the data rate is 10 Mbps, what is the minimum required bandwidth in MHz?

<details>
<summary>Answer</summary>

Manchester encoding requires twice the bandwidth of the data rate.
Minimum Bandwidth = $\boxed{10}$ MHz (or 20 MHz for full spectrum)
</details>

---

**Q3.** A modem uses 16-QAM and operates at 9600 baud. What is the data rate in bps?

<details>
<summary>Answer</summary>

16-QAM → 4 bits per symbol
Data rate = $9600 \times 4 = \boxed{38400}$ bps
</details>

---

### **MCQ Questions**

**Q4.** Which encoding scheme provides self-clocking?
- (a) NRZ-L
- (b) NRZ-I
- (c) Manchester
- (d) RZ with AMI

<details>
<summary>Answer</summary>

**(c) Manchester** - Has a transition in the middle of every bit, providing clock information.
</details>

---

**Q5.** Which multiplexing technique is used in optical fiber communication?
- (a) FDM
- (b) TDM
- (c) WDM
- (d) CDM

<details>
<summary>Answer</summary>

**(c) WDM** - Wavelength Division Multiplexing uses different wavelengths of light.
</details>

---

## 2.10 The 5-Second Snap-Check ✅

Before moving to the next module, verify you can:

1. ☐ Compare twisted pair, coax, and fiber optic
2. ☐ Apply Nyquist: $C = 2B \log_2 L$
3. ☐ Apply Shannon: $C = B \log_2(1 + SNR)$
4. ☐ Convert SNR from dB: $SNR = 10^{dB/10}$
5. ☐ Calculate bit rate from baud rate
6. ☐ Draw Manchester encoding for a given bit sequence
7. ☐ Differentiate FDM, TDM, WDM

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 3: Data Link Layer →](./03-Data-Link-Layer.md)
