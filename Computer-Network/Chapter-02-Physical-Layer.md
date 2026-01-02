# ⚡ Chapter 2: Physical Layer

> **The Atomic Truth:** Convert bits to signals; maximize capacity.

---

## 🎯 Chapter Overview

| Topic | GATE Weightage | Difficulty |
|-------|----------------|------------|
| Shannon's Theorem | High | Medium |
| Nyquist Rate | High | Medium |
| Transmission Media | Low | Easy |
| Multiplexing | Medium | Medium |
| Encoding Schemes | Medium | Medium |

---

## 2.1 Analog vs Digital Signals

### Signal Types

```
ANALOG SIGNAL                    DIGITAL SIGNAL
     ╱╲    ╱╲                    ┌──┐  ┌──┐
    ╱  ╲  ╱  ╲                   │  │  │  │
   ╱    ╲╱    ╲                 ─┘  └──┘  └──
  Continuous amplitude          Discrete levels (0, 1)
```

### Key Definitions

| Term | Definition | Unit |
|------|------------|------|
| **Bandwidth (B)** | Range of frequencies | Hz |
| **Bit Rate (R)** | Bits transmitted per second | bps |
| **Baud Rate** | Signal changes per second | baud |

### ⚠️ GATE TRAP: Bit Rate vs Baud Rate
$$\text{Bit Rate} = \text{Baud Rate} \times \log_2(L)$$

where $L$ = number of discrete signal levels

**Key Insight:** For binary signaling ($L=2$), bit rate = baud rate (since $\log_2(2) = 1$). This is a common source of confusion!

**Example:** If baud rate = 1000 and 4 signal levels:
$$\text{Bit Rate} = 1000 \times \log_2(4) = 1000 \times 2 = 2000 \text{ bps}$$

---

## 2.2 Transmission Impairments

### 2.2.1 Attenuation

**What:** Signal power decreases with distance

$$P_{out} = P_{in} \times e^{-\alpha d}$$

**Decibel (dB) measure:**
$$dB = 10 \log_{10}\left(\frac{P_2}{P_1}\right)$$

**For amplifiers/repeaters:**
$$dB_{total} = dB_1 + dB_2 + dB_3 + \ldots$$

#### 🧮 NAT Practice
**Q:** A signal travels through 3 segments with gains of -10 dB, +20 dB, -5 dB. What is the total gain?

**Solution:** $dB_{total} = -10 + 20 - 5 = +5$ dB

If input power = 100 mW:
$$P_{out} = 100 \times 10^{5/10} = 100 \times 10^{0.5} = 316.23 \text{ mW}$$

### 2.2.2 Distortion

**What:** Signal shape changes due to different frequency components traveling at different speeds

**Cause:** Dispersion in medium

### 2.2.3 Noise

| Type | Description | Formula |
|------|-------------|---------|
| **Thermal** | Random electron motion | $N = kTB$ |
| **Induced** | From external sources | — |
| **Crosstalk** | Signal leakage between wires | — |
| **Impulse** | Spikes (lightning, etc.) | — |

**Signal-to-Noise Ratio (SNR):**
$$SNR = \frac{P_{signal}}{P_{noise}}$$

$$SNR_{dB} = 10 \log_{10}\left(\frac{P_{signal}}{P_{noise}}\right)$$

---

## 2.3 Channel Capacity — The Golden Theorems

### 2.3.1 Nyquist Theorem (Noiseless Channel)

> **For a noiseless channel with bandwidth $B$ Hz and $L$ signal levels:**

$$C_{max} = 2B \log_2(L) \text{ bps}$$

**Derivation Logic:**
1. Bandwidth $B$ limits how fast signal can change
2. Maximum symbol rate = $2B$ symbols/second (Nyquist rate)
3. Each symbol carries $\log_2(L)$ bits
4. Therefore: $C = 2B \times \log_2(L)$

### 2.3.2 Shannon's Theorem (Noisy Channel)

> **For a noisy channel with bandwidth $B$ Hz and SNR ratio:**

$$C_{max} = B \log_2(1 + SNR) \text{ bps}$$

**The Golden Pivot:** SNR is the master switch — it sets the theoretical maximum regardless of encoding!

### ⚠️ GATE TRAP: Which Formula to Use?

| Condition | Formula | Notes |
|-----------|---------|-------|
| Given signal levels, noiseless | Nyquist | $C = 2B\log_2(L)$ |
| Given SNR, noisy | Shannon | $C = B\log_2(1 + SNR)$ |
| Given both | Use **minimum** of both | Practical limit |

#### 🧮 NAT Practice — The Classic Combo Question
**Q:** A channel has bandwidth 4 kHz. SNR = 255. If we use 16 signal levels, what is the maximum achievable bit rate?

**Solution:**

**Shannon's Limit:**
$$C_S = 4000 \times \log_2(1 + 255) = 4000 \times \log_2(256) = 4000 \times 8 = 32000 \text{ bps}$$

**Nyquist's Limit:**
$$C_N = 2 \times 4000 \times \log_2(16) = 8000 \times 4 = 32000 \text{ bps}$$

**Answer:** 32 kbps (both agree!)

#### 🧮 NAT Practice — When They Disagree
**Q:** Bandwidth = 3 kHz, SNR = 63, signal levels = 8. Find max bit rate.

**Shannon:**
$$C_S = 3000 \times \log_2(64) = 3000 \times 6 = 18000 \text{ bps}$$

**Nyquist:**
$$C_N = 2 \times 3000 \times \log_2(8) = 6000 \times 3 = 18000 \text{ bps}$$

**Answer:** 18 kbps

---

## 2.4 Transmission Media

### 2.4.1 Guided Media (Wired)

| Medium | Bandwidth | Distance | Cost | Use |
|--------|-----------|----------|------|-----|
| **Twisted Pair** | ~100 MHz | ~100m | Low | LAN, Telephone |
| **Coaxial** | ~500 MHz | ~500m | Medium | Cable TV |
| **Fiber Optic** | ~THz | ~100km | High | WAN, Backbone |

#### Twisted Pair Categories

| Category | Max Frequency | Max Speed | Use |
|----------|---------------|-----------|-----|
| Cat 3 | 16 MHz | 10 Mbps | Voice |
| Cat 5e | 100 MHz | 1 Gbps | Ethernet |
| Cat 6 | 250 MHz | 10 Gbps | Fast Ethernet |
| Cat 7 | 600 MHz | 10 Gbps | Data centers |

#### Fiber Optic Types

| Type | Core Diameter | Modes | Distance | Use |
|------|---------------|-------|----------|-----|
| **Single Mode** | 8-10 μm | 1 | 100+ km | Long-haul |
| **Multi-Mode** | 50-62.5 μm | Multiple | ~2 km | LAN |

**Why Single Mode goes farther:** No modal dispersion (only one path for light)

### 2.4.2 Unguided Media (Wireless)

| Type | Frequency | Range | Use |
|------|-----------|-------|-----|
| **Radio** | 3 kHz - 1 GHz | Long | AM/FM, TV |
| **Microwave** | 1 GHz - 300 GHz | Line-of-sight | Satellite, 5G |
| **Infrared** | 300 GHz - 400 THz | Room | Remote controls |

---

## 2.5 Multiplexing

### 2.5.1 Frequency Division Multiplexing (FDM)

```
Channel 1: ████████░░░░░░░░░░░░░░░░░░░
Channel 2: ░░░░░░░░████████░░░░░░░░░░░
Channel 3: ░░░░░░░░░░░░░░░░████████░░░
           └── Guard Band ──┘
           ◄───────── Frequency ──────►
```

**Characteristics:**
- Analog multiplexing
- Each channel gets a frequency band
- Guard bands prevent interference

**Total Bandwidth:**
$$B_{total} = n \times B_{channel} + (n-1) \times B_{guard}$$

### 2.5.2 Time Division Multiplexing (TDM)

```
Time →
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ C1 │ C2 │ C3 │ C4 │ C1 │ C2 │ C3 │ C4 │
└────┴────┴────┴────┴────┴────┴────┴────┘
├────── Frame 1 ─────┼────── Frame 2 ────┤
```

**Types:**
1. **Synchronous TDM:** Fixed time slots, even if empty
2. **Statistical TDM (Async):** Slots assigned on demand

**Efficiency:**
$$\eta_{sync} = \frac{\text{Used slots}}{\text{Total slots}}$$

#### 🧮 NAT Practice
**Q:** 4 channels, each 1 Mbps. TDM frame has 1-bit slots. Find:
(a) Frame size in bits
(b) Frame duration
(c) Link speed

**Solution:**
- (a) Frame size = 4 bits (one from each channel)
- (b) Each channel contributes 1 Mbps, so 1 bit every $10^{-6}$ s per channel
- Frame duration = $4 \times 10^{-6}$ s? **No!**
- Actually: Frame rate = 1M frames/second (each channel sends 1M bits/s)
- (b) Frame duration = $10^{-6}$ s = 1 μs
- (c) Link speed = 4 bits per frame × 1M frames/s = **4 Mbps**

### 2.5.3 Wavelength Division Multiplexing (WDM)

- FDM for optical fiber
- Different wavelengths (colors) of light
- **DWDM:** Dense WDM, many channels

### 2.5.4 Code Division Multiplexing (CDM)

- Each channel has unique code
- All transmit simultaneously on same frequency
- Receiver uses code to extract intended signal
- Used in CDMA cellular

---

## 2.6 Digital Encoding Schemes

### Line Coding

```
Data:     1   0   1   1   0   0   1

NRZ-L:   ─┐   ┌───┐   ┌───────┐
          └───┘   └───┘       └───

NRZ-I:   ─┐   │   ┌───┐       ┌───
          └───┘   └───────────┘

Manchester:
         ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
         │ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ │
         1   0   1   1   0   0   1

Diff Manchester:
         ┌─┐   ┌─┐   ┌───┐   ┌───┐
         │ └───┘ └───┘   └───┘   │
         1   0   1   1   0   0   1
```

### Encoding Comparison

| Scheme | Sync | DC Component | Bandwidth | Use |
|--------|------|--------------|-----------|-----|
| **NRZ-L** | No | Yes | Low | Simple |
| **NRZ-I** | Better | Yes | Low | USB |
| **Manchester** | Yes | No | 2× NRZ | 10BASE-T Ethernet |
| **Diff. Manchester** | Yes | No | 2× NRZ | Token Ring |
| **AMI** | Yes | No | Low | T1 lines |
| **MLT-3** | No | No | Low | 100BASE-TX |

### ⚠️ GATE TRAP: Manchester Bandwidth
- Manchester encoding requires **twice** the bandwidth of NRZ
- Because: 2 signal transitions per bit (clock embedded)
- Minimum bandwidth = 2 × bit rate

### Bandwidth Efficiency

| Encoding | Baud Rate per bps |
|----------|-------------------|
| NRZ | 1 |
| Manchester | 2 |
| 4B/5B + NRZ-I | 1.25 |
| 8B/10B | 1.25 |

---

## 2.7 Block Coding

### 4B/5B Encoding
- 4 data bits → 5 code bits
- Efficiency = 4/5 = 80%
- Ensures no more than 3 consecutive zeros
- Used with NRZ-I in Fast Ethernet

### 8B/10B Encoding
- 8 data bits → 10 code bits
- Efficiency = 80%
- DC balanced
- Used in Gigabit Ethernet

---

## 2.8 Analog-to-Digital Conversion

### Pulse Code Modulation (PCM)

**Steps:**
1. **Sampling:** At Nyquist rate $f_s ≥ 2f_{max}$
2. **Quantization:** Map to discrete levels
3. **Encoding:** Convert to binary

**Bit Rate:**
$$R = f_s \times n = f_s \times \lceil\log_2(L)\rceil$$

where $n$ = bits per sample, $L$ = quantization levels

#### 🧮 NAT Practice
**Q:** Voice signal (0-4 kHz) is sampled at Nyquist rate, quantized to 256 levels. Find bit rate.

**Solution:**
- $f_s = 2 \times 4000 = 8000$ samples/second
- Bits per sample = $\log_2(256) = 8$
- Bit rate = $8000 \times 8 = 64000$ bps = **64 kbps**

This is the standard **DS-0 rate**!

### T-Carrier and E-Carrier Systems

| System | Channels | Bit Rate |
|--------|----------|----------|
| DS-0 | 1 | 64 kbps |
| DS-1 (T1) | 24 | 1.544 Mbps |
| E1 | 30 | 2.048 Mbps |
| DS-3 (T3) | 672 | 44.736 Mbps |

**T1 Calculation:**
$$\text{T1} = 24 \times 64 \text{ kbps} + 8 \text{ kbps (framing)} = 1.544 \text{ Mbps}$$

**E1 Calculation:**
$$\text{E1} = 32 \times 64 \text{ kbps} = 2.048 \text{ Mbps}$$

(30 voice + 2 signaling/sync)

---

## 2.9 Modulation Techniques

### Digital-to-Analog Modulation

For transmitting digital data over analog channel (e.g., modem):

| Technique | Modifies | Diagram |
|-----------|----------|---------|
| **ASK** | Amplitude | High/Low amplitude for 1/0 |
| **FSK** | Frequency | Different frequencies for 1/0 |
| **PSK** | Phase | Different phases for 1/0 |
| **QAM** | Amplitude + Phase | Combines ASK + PSK |

### QAM Constellation

```
    QPSK (4-QAM)              16-QAM
       Q                        Q
       │   •   •                │ • • • •
       │                        │ • • • •
   ────┼────► I             ────┼────────► I
       │                        │ • • • •
       •   •                    │ • • • •
```

**Bits per symbol:**
$$n = \log_2(M)$$

For 256-QAM: $n = \log_2(256) = 8$ bits/symbol

---

## 2.10 Switching at Physical Layer

### Circuit Switching Components

| Component | Function |
|-----------|----------|
| **Space Division** | Physical switching of wires |
| **Time Division** | Switching time slots |

### Crossbar Switch

For $n$ inputs and $m$ outputs:
- Number of crosspoints = $n \times m$
- Non-blocking: Any input can reach any free output

**Problem:** $n^2$ crosspoints for $n \times n$ switch

### Multi-stage Switches

**Clos Network:** Reduces crosspoints while maintaining non-blocking

$$\text{Crosspoints} = 2nk + k\left(\frac{n}{k}\right)^2$$

---

## 2.11 Performance Metrics

### Throughput vs Bandwidth

- **Bandwidth:** Maximum capacity (theoretical)
- **Throughput:** Actual achieved rate
- **Goodput:** Application-level useful data rate

$$\text{Throughput} ≤ \text{Bandwidth}$$

$$\text{Goodput} ≤ \text{Throughput}$$

### Latency Components

$$T_{total} = T_{transmission} + T_{propagation} + T_{queuing} + T_{processing}$$

Where:
- $T_{transmission} = \frac{L}{B}$ (L = packet size, B = bandwidth)
- $T_{propagation} = \frac{d}{v}$ (d = distance, v = signal speed)

### ⚠️ GATE TRAP: Propagation Speed
- Copper wire: ~$2 \times 10^8$ m/s
- Fiber optic: ~$2 \times 10^8$ m/s
- Air/Vacuum: $3 \times 10^8$ m/s

**Don't assume** $3 \times 10^8$ for wires!

---

## 📝 Quick Revision Formula Sheet

| Concept | Formula |
|---------|---------|
| Nyquist Capacity | $C = 2B\log_2(L)$ |
| Shannon Capacity | $C = B\log_2(1 + SNR)$ |
| SNR in dB | $SNR_{dB} = 10\log_{10}(SNR)$ |
| dB to ratio | $\text{ratio} = 10^{dB/10}$ |
| Bit rate | Baud rate × $\log_2(L)$ |
| PCM bit rate | $f_s \times \log_2(\text{levels})$ |
| Transmission time | $L/B$ |
| Propagation time | $d/v$ |
| T1 rate | 1.544 Mbps |
| E1 rate | 2.048 Mbps |

---

## 🎯 Chapter Summary

1. **Nyquist:** Noiseless channel limit, depends on levels
2. **Shannon:** Noisy channel limit, depends on SNR
3. **Use minimum** of both for practical limit
4. **Transmission media:** Twisted pair < Coax < Fiber
5. **Multiplexing:** FDM (frequency), TDM (time), WDM (wavelength), CDM (code)
6. **Encoding:** NRZ (simple), Manchester (self-clocking, 2× BW)
7. **PCM:** Sample at Nyquist rate, quantize, encode
8. **Modulation:** ASK, FSK, PSK, QAM for analog channels

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining this with **Data Link Layer** for a Rank-1 simulation?
