# Chapter 2: Physical Layer

## 🎯 GATE/ESE Weightage: 4-6 marks (Numerical + Conceptual)

---

## 2.1 Physical Layer Functions

The Physical Layer deals with the **mechanical, electrical, and procedural** interface to the transmission medium.

**Core Functions**:
1. **Bit-by-bit delivery** between devices
2. **Encoding/Decoding** data into signals
3. **Transmission rate** (bit rate) definition
4. **Synchronization** of bits
5. **Line configuration** (point-to-point, multipoint)
6. **Physical topology** (mesh, star, bus, ring)

---

## 2.2 Signals: Analog vs Digital

### Signal Types

```
ANALOG SIGNAL (Continuous):              DIGITAL SIGNAL (Discrete):
    ╱╲    ╱╲    ╱╲                         ┌──┐  ┌──┐
   ╱  ╲  ╱  ╲  ╱  ╲                        │  │  │  │
  ╱    ╲╱    ╲╱    ╲                    ───┘  └──┘  └──
Varies continuously over time          Only specific values (0,1)
```

### Signal Parameters (🎯 IMPORTANT)

| Parameter | Symbol | Definition | Unit |
|-----------|--------|------------|------|
| **Amplitude** | A | Signal strength | Volts (V) |
| **Frequency** | f | Cycles per second | Hertz (Hz) |
| **Period** | T | Time for one cycle | Seconds (s) |
| **Phase** | φ | Position in cycle | Degrees/Radians |
| **Wavelength** | λ | Distance per cycle | Meters (m) |

**🎯 Key Relationships**:
```
f = 1/T                    (Frequency and Period)
λ = c/f = c × T            (Wavelength, speed, frequency)
c = λ × f                  (Speed of wave)
```

Where c = 3×10⁸ m/s (speed of light in vacuum)

### Bandwidth vs Data Rate

| Term | Definition | Unit |
|------|------------|------|
| **Bandwidth (Analog)** | Range of frequencies | Hz |
| **Bandwidth (Digital)** | Data transfer capacity | bps |
| **Bit Rate** | Bits transmitted per second | bps |
| **Baud Rate** | Signal changes per second | baud |

**🎯 Critical Relationship**:
```
Bit Rate = Baud Rate × log₂(L)

Where L = number of signal levels
```

**Example**: 
- 1000 baud with 16 levels = 1000 × log₂(16) = 1000 × 4 = **4000 bps**

---

## 2.3 Channel Capacity Theorems (🎯 MOST ASKED)

### Nyquist Theorem (Noiseless Channel)

```
C = 2 × B × log₂(L)

Where:
C = Maximum bit rate (bps)
B = Bandwidth (Hz)
L = Number of signal levels
```

**🧠 Why 2B?**: Sampling at 2× bandwidth captures all information (Nyquist rate)

**Example**: Bandwidth = 3000 Hz, 4 signal levels
- C = 2 × 3000 × log₂(4) = 6000 × 2 = **12,000 bps**

### Shannon's Theorem (Noisy Channel)

```
C = B × log₂(1 + SNR)

Where:
C = Channel capacity (bps)
B = Bandwidth (Hz)
SNR = Signal-to-Noise Ratio (linear, not dB)
```

**🎯 Converting SNR from dB**:
```
SNR(dB) = 10 × log₁₀(SNR_linear)
SNR_linear = 10^(SNR(dB)/10)
```

**Example**: B = 3000 Hz, SNR = 30 dB
- SNR_linear = 10^(30/10) = 1000
- C = 3000 × log₂(1001) ≈ 3000 × 10 = **30,000 bps**

### 🎯 When to Use Which?

| Condition | Use | Formula |
|-----------|-----|---------|
| Given signal levels, no noise | Nyquist | C = 2B × log₂(L) |
| Given SNR | Shannon | C = B × log₂(1 + SNR) |
| Given both | **Minimum** of both | Take lower value |

**🧠 Key Insight**: 
- Nyquist gives **theoretical max** based on sampling
- Shannon gives **practical max** based on noise
- Actual capacity = min(Nyquist, Shannon)

### Classic GATE Problem

**Q**: Channel bandwidth = 4 kHz, SNR = 31, and 8 signal levels. Find max data rate.

**Solution**:
```
Nyquist: C = 2 × 4000 × log₂(8) = 8000 × 3 = 24,000 bps
Shannon: C = 4000 × log₂(1 + 31) = 4000 × 5 = 20,000 bps

Answer: min(24000, 20000) = 20,000 bps ✓
```

---

## 2.4 Transmission Media

### Classification

```
Transmission Media
├── Guided (Wired)
│   ├── Twisted Pair
│   │   ├── UTP (Unshielded)
│   │   └── STP (Shielded)
│   ├── Coaxial Cable
│   │   ├── Thinnet (10Base2)
│   │   └── Thicknet (10Base5)
│   └── Fiber Optic
│       ├── Single-mode (SMF)
│       └── Multi-mode (MMF)
│
└── Unguided (Wireless)
    ├── Radio Waves (3 kHz - 1 GHz)
    ├── Microwaves (1 - 300 GHz)
    └── Infrared (300 GHz - 400 THz)
```

### Guided Media Comparison (🎯 GATE Favorite)

| Property | Twisted Pair | Coaxial | Fiber Optic |
|----------|--------------|---------|-------------|
| **Bandwidth** | Low-Medium | Medium | Very High |
| **Attenuation** | High | Medium | Very Low |
| **EMI Immunity** | Low | Medium | **Complete** |
| **Cost** | Lowest | Medium | Highest |
| **Installation** | Easy | Medium | Difficult |
| **Security** | Low | Medium | High |
| **Distance** | ~100m | ~500m | ~100+ km |
| **Use** | LAN, Phone | Cable TV | Backbone, WAN |

### Twisted Pair Categories

| Category | Bandwidth | Speed | Application |
|----------|-----------|-------|-------------|
| Cat 3 | 16 MHz | 10 Mbps | 10BASE-T |
| Cat 5 | 100 MHz | 100 Mbps | 100BASE-TX |
| Cat 5e | 100 MHz | 1 Gbps | Gigabit Ethernet |
| Cat 6 | 250 MHz | 10 Gbps | 10GBASE-T |
| Cat 6a | 500 MHz | 10 Gbps | 10GBASE-T (100m) |
| Cat 7 | 600 MHz | 10+ Gbps | Data centers |

**🧠 Why Twisted?**: Twisting reduces **crosstalk** and **EMI** by canceling out interference

### Fiber Optic Types (🎯 IMPORTANT)

```
SINGLE-MODE FIBER (SMF):           MULTI-MODE FIBER (MMF):
    ┌────────────────────┐           ┌────────────────────┐
    │→→→→→→→→→→→→→→→→→→→│           │→→→→→→→→→→→→→→→→→→→│
    │    Single ray      │           │ ↗→→→→→→→→↘        │
    │    travels         │           │→→→→→→→→→→→→→→→→→→→│
    │    straight        │           │ ↘→→→→→→→→↗ Modal  │
    └────────────────────┘           └────────dispersion─┘
    Core: 8-10 μm                    Core: 50-62.5 μm
    Long distance, high speed        Short distance, cheaper
```

| Feature | Single-Mode | Multi-Mode |
|---------|-------------|------------|
| Core Diameter | 8-10 μm | 50-62.5 μm |
| Light Source | Laser | LED |
| Distance | Up to 100 km | Up to 2 km |
| Bandwidth | Very high | Lower |
| Cost | Higher | Lower |
| Dispersion | Minimal | Modal dispersion |

### Unguided Media

| Type | Frequency | Propagation | Use Case |
|------|-----------|-------------|----------|
| **Radio** | 3 kHz - 1 GHz | Omnidirectional | AM/FM, Wi-Fi |
| **Microwave** | 1 - 300 GHz | Line-of-sight | Satellite, cellular |
| **Infrared** | 300 GHz - 400 THz | Line-of-sight | TV remote, short range |

**🎯 Propagation Modes**:
- **Ground wave**: Follows Earth's curvature (< 2 MHz)
- **Sky wave**: Reflects off ionosphere (2-30 MHz)
- **Line of sight**: Straight path (> 30 MHz)

---

## 2.5 Digital Transmission (Line Coding)

### Why Line Coding?

1. **DC component elimination** (for AC-coupled lines)
2. **Synchronization** (clock recovery)
3. **Error detection** capability
4. **Bandwidth efficiency**

### Line Coding Schemes

```
Signal for: 0 1 0 1 1 0 0 1

UNIPOLAR NRZ:
 ┌─┐ ┌─┐ ┌─┐   ┌─┐
 │ │ │ │ │ │   │ │
─┘ └─┘ └─┘ └───┘ └─  (1=High, 0=Low)

POLAR NRZ-L (Level):
 ┌─┐   ┌─┬─┐     ┌─┐
 │ │   │ │ │     │ │
─┘ └───┘ └ └─────┘ └  (1=High, 0=Low)

POLAR NRZ-I (Invert on 1):
 ─┬─┐ ┌─┬─┐   ┌───┐
   │ │ │ │ │   │   │
   └─┘ └─┘ └───┘   └  (Transition on 1)

POLAR RZ (Return to Zero):
 ┌┐ ┌┐ ┌┐┌┐   ┌┐
 ││ ││ ││││   ││
─┘└─┘└─┘└┘└───┘└─  (Returns to 0 in each bit)

MANCHESTER (Biphase):
 ┌┐ ┌┐ ┌┐┌┐   ┌┐
 │└┐│└┐│└│└┐┌┐│└┐
 └ └┘ └┘ └ └┘└┘ └  (Transition in MIDDLE of each bit)
                    High-Low = 1, Low-High = 0 (IEEE)

DIFFERENTIAL MANCHESTER:
 ┌┐ ┌┐ ┌┐┌┐   ┌┐
 │└┐│ └│└│ ┐┌┐│ └
 └ └┘  └ └ └┘└┘   (Transition at start = 0, no trans = 1)
                   Always transition in middle
```

### Line Coding Comparison (🎯 MUST MEMORIZE)

| Scheme | Sync | DC Component | Bandwidth | Use |
|--------|------|--------------|-----------|-----|
| **NRZ-L** | Poor | Yes | B = R/2 | Simple |
| **NRZ-I** | Better | Less | B = R/2 | USB |
| **RZ** | Good | Yes | B = R | - |
| **Manchester** | **Excellent** | **None** | B = R | Ethernet (802.3) |
| **Diff Manchester** | **Excellent** | **None** | B = R | Token Ring (802.5) |
| **AMI** | Good | **None** | B = R/2 | T1/E1 |
| **B8ZS** | **Excellent** | **None** | B = R/2 | T1 (North America) |
| **HDB3** | **Excellent** | **None** | B = R/2 | E1 (Europe) |

**Where R = Bit Rate (bps), B = Bandwidth (Hz)**

### 🎯 Manchester Encoding Details

```
Manchester (IEEE 802.3):
- Transition in MIDDLE of every bit period
- 1 = High → Low (falling edge in middle)
- 0 = Low → High (rising edge in middle)

Advantage: Self-clocking (clock embedded in signal)
Disadvantage: Bandwidth = 2 × NRZ (50% efficiency)
```

**🧠 Trick for Manchester**:
- "1 goes DOWN in the middle" (High→Low)
- "0 goes UP in the middle" (Low→High)

### Bipolar Schemes (AMI, B8ZS, HDB3)

```
AMI (Alternate Mark Inversion):
Data:    1   0   1   0   0   1   1   0
Signal: +V   0  -V   0   0  +V  -V   0
         └──────────────────────────┘
         Alternating polarity for 1s

Problem: Long string of 0s = no transitions = sync loss

Solution: B8ZS and HDB3 add violations for long zeros
```

**B8ZS (Bipolar with 8-Zero Substitution)**:
- Replaces 8 consecutive 0s with: 000VB0VB
- V = Violation (same polarity as previous pulse)
- B = Bipolar (opposite polarity)

**HDB3 (High Density Bipolar 3)**:
- Replaces 4 consecutive 0s
- Pattern depends on count of 1s since last substitution

---

## 2.6 Block Coding

### Purpose
Convert m-bit blocks to n-bit blocks (n > m) for:
- Error detection
- Synchronization
- DC balance

### Common Schemes

| Scheme | Input | Output | Efficiency | Use |
|--------|-------|--------|------------|-----|
| **4B/5B** | 4 bits | 5 bits | 80% | 100BASE-TX, FDDI |
| **8B/10B** | 8 bits | 10 bits | 80% | Gigabit Ethernet |
| **8B/6T** | 8 bits | 6 ternary | - | 100BASE-T4 |

**4B/5B + MLT-3** combination used in 100BASE-TX:
```
Data (4 bits) → 4B/5B encoding (5 bits) → MLT-3 signaling

Why? Reduces required bandwidth:
- 100 Mbps with NRZ needs 100 MHz
- 4B/5B makes it 125 Mbps
- MLT-3 reduces effective frequency: 125/4 = 31.25 MHz
```

---

## 2.7 Analog-to-Digital Conversion

### Pulse Code Modulation (PCM) (🎯 VERY IMPORTANT)

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐
│   Analog    │───→│   Sampling   │───→│ Quantizing │───→ Digital
│   Signal    │    │  (PAM pulses)│    │   Encoding │     Output
└─────────────┘    └──────────────┘    └────────────┘
```

**Three Steps**:

1. **Sampling**: Convert continuous signal to discrete samples
2. **Quantization**: Round samples to nearest level
3. **Encoding**: Convert to binary

### Nyquist Sampling Theorem (🎯 CRITICAL)

```
fs ≥ 2 × fmax

Where:
fs = Sampling frequency
fmax = Maximum frequency in signal
```

**Example**: Voice signal (300-3400 Hz)
- fmax = 3400 Hz
- fs ≥ 2 × 3400 = 6800 Hz
- In practice, **8000 Hz** used (for margin)

### PCM Calculations (🎯 GATE FAVORITE)

**Given**: Sampling rate, number of quantization levels

```
Bit Rate = Sampling Rate × Bits per Sample
         = fs × n
         = fs × log₂(L)

Where:
L = Number of quantization levels
n = Number of bits per sample
```

**Standard Voice PCM**:
- Sampling rate: 8000 Hz
- Quantization levels: 256 (8 bits)
- **Bit rate = 8000 × 8 = 64 kbps** (DS0 channel)

**🎯 T1/E1 Systems**:

| System | Channels | Voice Rate | Total Rate |
|--------|----------|------------|------------|
| **T1** | 24 voice channels + framing bits | 64 kbps each | 1.544 Mbps |
| **E1** | 30 voice + 2 signaling channels | 64 kbps each | 2.048 Mbps |

```
T1 = 24 channels × 8 bits × 8000 frames/sec + 8000 framing bits = 1.544 Mbps
   = (24 × 8 + 1) × 8000 = 193 × 8000 = 1.544 Mbps
E1 = 32 × 64 kbps = 2.048 Mbps (30 voice + 2 signaling/sync channels)
```

### Quantization Error

```
SNR (for PCM) = 6.02n + 1.76 dB

Where n = bits per sample
```

**Example**: 8-bit PCM → SNR = 6.02(8) + 1.76 = 49.92 dB

**🧠 Insight**: Each additional bit → ~6 dB improvement

---

## 2.8 Analog-to-Analog Modulation

### Why Modulation?

1. **Antenna size**: λ/4 antenna impractical for low frequencies
2. **Frequency division multiplexing**: Multiple signals share medium
3. **Reduce noise/interference**: Higher frequencies less susceptible

### Modulation Types

```
CARRIER SIGNAL: ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿

AM (Amplitude):    ∿∿∿∿∿∿∿     (Amplitude varies)
                  (small) (large)

FM (Frequency):    ∿∿∿∿∿∿∿∿∿∿∿∿∿  (Frequency varies)
                   (sparse) (dense)

PM (Phase):        ∿∿∿|∿∿∿|∿∿∿   (Phase shifts)
                      ↑   ↑
                   Phase changes
```

### Comparison

| Property | AM | FM | PM |
|----------|-----|-----|-----|
| Varies | Amplitude | Frequency | Phase |
| Noise immunity | Low | High | High |
| Bandwidth | Low (2×fm) | High (Carson's rule) | High |
| Complexity | Simple | Complex | Complex |
| Application | AM radio | FM radio | Digital |

**🎯 Carson's Rule (FM Bandwidth)**:
```
BW = 2(Δf + fm)

Where:
Δf = Maximum frequency deviation
fm = Maximum modulating frequency
```

---

## 2.9 Digital-to-Analog Modulation (🎯 IMPORTANT)

### ASK (Amplitude Shift Keying)

```
Binary: 1   0   1   1   0
        ∿∿∿     ∿∿∿∿∿∿
Signal: (A)  0  (A)  (A)  0
```

- **1 = Carrier present**, **0 = No carrier** (OOK variant)
- Simple but susceptible to noise
- Used in optical fiber (on-off)

### FSK (Frequency Shift Keying)

```
Binary: 1   0   1   1   0
        ∿∿∿ ∿∿∿ ∿∿∿∿∿∿ ∿∿∿
Signal: f1  f2  f1  f1  f2
        (high)(low)
```

- Different frequencies for 0 and 1
- Better noise immunity than ASK
- Used in modems, caller ID

**🎯 FSK Bandwidth**:
```
BW = (f1 - f2) + Baud rate
   = 2Δf + Baud
```

### PSK (Phase Shift Keying)

```
BPSK (Binary PSK):
Binary: 1       0       1       0
Phase:  0°     180°     0°     180°
        ∿∿∿∿∿  ∿∿∿∿∿  ∿∿∿∿∿  ∿∿∿∿∿
             ↑      ↑      ↑
          Phase shifts
```

### QPSK (Quadrature PSK)

```
4 phases = 2 bits per symbol

Dibits:   00    01    10    11
Phase:    0°    90°   180°  270°

          90°(01)
             │
  180°(10) ──┼── 0°(00)
             │
          270°(11)
```

**QPSK Advantage**: Same bandwidth as BPSK, double the bit rate!

### QAM (Quadrature Amplitude Modulation) (🎯 MOST EFFICIENT)

Combines **amplitude** and **phase** modulation.

```
16-QAM: 4 amplitudes × 4 phases = 16 combinations = 4 bits/symbol

Constellation Diagram:
    ●  ●  ●  ●
    ●  ●  ●  ●
    ●  ●  ●  ●
    ●  ●  ●  ●
```

| Modulation | Bits per Symbol | Levels (L) |
|------------|-----------------|------------|
| BPSK | 1 | 2 |
| QPSK | 2 | 4 |
| 8-PSK | 3 | 8 |
| 16-QAM | 4 | 16 |
| 64-QAM | 6 | 64 |
| 256-QAM | 8 | 256 |

**🎯 Formula**:
```
Bits per symbol = log₂(L)
Bit rate = Baud rate × log₂(L)
```

**Example**: 1000 baud, 16-QAM
- Bit rate = 1000 × log₂(16) = 1000 × 4 = **4000 bps**

---

## 2.10 Multiplexing (🎯 VERY IMPORTANT)

### What is Multiplexing?

```
Multiple signals → ONE shared medium → Separate at destination

     ┌───────────┐                    ┌─────────────┐
[A]──┤           │   Single           │             │──[A]
[B]──┤    MUX    ├═══Medium═══════════┤   DEMUX     │──[B]
[C]──┤           │                    │             │──[C]
     └───────────┘                    └─────────────┘
```

### Types of Multiplexing

```
Multiplexing
├── Frequency Division (FDM)    - Analog
├── Wavelength Division (WDM)   - Optical
├── Time Division (TDM)         - Digital
│   ├── Synchronous TDM
│   └── Statistical TDM
└── Code Division (CDM)         - Spread Spectrum
```

### FDM (Frequency Division Multiplexing)

```
Frequency ↑
          │   ┌───────┐
          │   │   C   │  Guard band between channels
          │   ├───────┤  ↔
          │   │   B   │
          │   ├───────┤
          │   │   A   │
          └───┴───────┴──────→ Time

Each channel gets a frequency band (slice of spectrum)
```

**Characteristics**:
- Used with analog signals
- Channels separated by **guard bands** (prevent interference)
- Example: FM radio stations (each at different frequency)

### TDM (Time Division Multiplexing)

```
Time →
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ A │ B │ C │ A │ B │
└───┴───┴───┴───┴───┴───┴───┴───┘
     Frame 1     │     Frame 2
                 ↓
Each channel gets a time slot (round-robin)
```

**Synchronous TDM**:
- Fixed time slots (even if source has no data)
- Wasteful if sources are idle
- Used in T1/E1 systems

**Statistical TDM (Async)**:
- Slots assigned on demand
- More efficient
- Needs addressing in each slot

### 🎯 TDM Calculations

**Given**: n channels, each at R bps

```
Link Rate = n × R bps (for Synchronous TDM)

Frame duration = 1 / Frame rate
Slot duration = Frame duration / n
```

**Example**: 4 channels × 250 kbps each = **1 Mbps link**

### WDM (Wavelength Division Multiplexing)

- **Same as FDM but for optical fiber**
- Different wavelengths (colors) of light
- DWDM (Dense WDM): 160+ channels on single fiber

### CDM/CDMA (Code Division Multiplexing)

```
Each station has unique CODE (chip sequence)
All stations transmit simultaneously on SAME frequency
Receiver uses code to extract correct signal

Station A: Code = [1, 1, 1, -1]
Station B: Code = [1, -1, 1, 1]
Station C: Code = [1, 1, -1, 1]

Codes are ORTHOGONAL (dot product = 0)
```

**Used in**: 3G cellular, GPS

---

## 2.11 Spread Spectrum

### Purpose
- Avoid interference and jamming
- Provide secure communication
- Share bandwidth among multiple users

### FHSS (Frequency Hopping Spread Spectrum)

```
Frequency ↑
   f4  │     ●           ●
   f3  │        ●              ●
   f2  │  ●           ●
   f1  │           ●        ●
       └──────────────────────→ Time

Signal hops between frequencies using pseudo-random sequence
```

### DSSS (Direct Sequence Spread Spectrum)

```
Original bit: 1
Chip code:    1 0 1 1 0 1 0 1 (8 chips)
Transmitted:  1 0 1 1 0 1 0 1

Chip rate >> Bit rate
Spreads signal over wider bandwidth
```

**Processing Gain**: 
```
GP = Chip rate / Bit rate = 10 log₁₀(Chip rate / Bit rate) dB
```

---

## 2.12 Circuit Switching: Time-Space-Time

### Crossbar Switch

```
     Outputs
      1  2  3
    ┌──┬──┬──┐
  1 │× │  │  │
Inputs├──┼──┼──┤
  2 │  │× │  │
    ├──┼──┼──┤
  3 │  │  │× │
    └──┴──┴──┘

N×N crossbar: N² crosspoints
Problem: N² grows quickly, non-blocking but expensive
```

### Multi-Stage Switching

**Clos Network**: Rearrangeably non-blocking
**Benes Network**: Rearrangeably non-blocking with minimum switches

---

## 2.13 Key Formulas Summary

| Concept | Formula |
|---------|---------|
| **Nyquist (noiseless)** | C = 2B × log₂(L) |
| **Shannon (noisy)** | C = B × log₂(1 + SNR) |
| **SNR conversion** | SNR_linear = 10^(SNR_dB/10) |
| **Bit rate vs Baud** | Bit rate = Baud × log₂(L) |
| **Sampling theorem** | fs ≥ 2 × fmax |
| **PCM bit rate** | fs × log₂(L) |
| **Wavelength** | λ = c/f |
| **T1 rate** | 24 × 64k + 8k = 1.544 Mbps |
| **E1 rate** | 32 × 64k = 2.048 Mbps |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: Channel Capacity
**Q**: B = 10 MHz, SNR = 63. Find capacity.
**A**: C = 10×10⁶ × log₂(64) = 10×10⁶ × 6 = **60 Mbps**

### Pattern 2: PCM Rate
**Q**: Voice signal 4 kHz, 128 levels. Find bit rate.
**A**: fs = 2×4k = 8k Hz, bits = log₂(128) = 7
       Rate = 8000 × 7 = **56 kbps**

### Pattern 3: Modulation
**Q**: 64-QAM at 5000 baud. Find bit rate.
**A**: log₂(64) = 6 bits/symbol
       Rate = 5000 × 6 = **30,000 bps**

### Pattern 4: TDM
**Q**: 20 channels, 1 Mbps each. Link rate?
**A**: 20 × 1 = **20 Mbps**

---

## 📝 Quick Revision Checklist

- [ ] Nyquist vs Shannon theorems and when to use each
- [ ] Line coding: NRZ-L, NRZ-I, Manchester, AMI differences
- [ ] Manchester: transition in middle, 1=High→Low
- [ ] PCM: Sampling rate ≥ 2×fmax, Bit rate = fs × log₂(L)
- [ ] T1 = 1.544 Mbps (24 channels), E1 = 2.048 Mbps (32 channels)
- [ ] ASK, FSK, PSK, QAM characteristics
- [ ] FDM (frequency), TDM (time), CDM (code) multiplexing
- [ ] Fiber: Single-mode (laser, long), Multi-mode (LED, short)

---

## 🔥 One-Liner Summary

> "Nyquist (C=2B×log₂L) for noiseless, Shannon (C=B×log₂(1+SNR)) for noisy; Manchester self-clocking with mid-bit transition; PCM digitizes at 2×fmax; QAM combines amplitude+phase for max efficiency; TDM shares time, FDM shares frequency, CDM shares codes."
