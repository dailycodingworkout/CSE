# Chapter 2: Physical Layer

## 🎯 The Atomic Truth
> **"Converting bits to signals across physical media with minimal distortion."**

---

## 2.1 Physical Layer Functions

### Core Responsibilities

| Function | Description |
|----------|-------------|
| **Bit Representation** | Convert bits (0/1) to electrical/optical/radio signals |
| **Bit Synchronization** | Clock synchronization between sender and receiver |
| **Transmission Mode** | Simplex, Half-duplex, Full-duplex |
| **Physical Topology** | How devices are physically connected |
| **Line Configuration** | Point-to-point or Multipoint |

### The "Aha!" Moment 💡
Physical layer is like the **"road infrastructure"** for data:
- **Bits** = Vehicles
- **Signals** = How vehicles move (speed, lanes)
- **Media** = The actual road (asphalt, dirt, water)
- **Encoding** = Traffic rules for vehicle movement

---

## 2.2 Transmission Media

### 2.2.1 Classification

```
                    Transmission Media
                          │
          ┌───────────────┴───────────────┐
      Guided                           Unguided
   (Wired/Bounded)                  (Wireless/Unbounded)
          │                               │
    ┌─────┼─────┐                 ┌───────┼───────┐
    │     │     │                 │       │       │
 Twisted  Coax Fiber          Radio  Microwave Infrared
  Pair                        Waves
```

### 2.2.2 Guided Media (Wired)

#### Twisted Pair Cable

```
     ┌─────────────────────────────────┐
     │  ╭──╮  ╭──╮  ╭──╮  ╭──╮  ╭──╮  │  Wire 1
     │ ╱    ╲╱    ╲╱    ╲╱    ╲╱    ╲ │
     │╱      ╲    ╲    ╲    ╲    ╲   │
     │╲      ╱╲   ╱╲   ╱╲   ╱╲   ╱   │  Wire 2
     │  ╰──╯  ╰──╯  ╰──╯  ╰──╯  ╰──╯ │
     └─────────────────────────────────┘
     Twisting reduces electromagnetic interference (EMI)
```

| Type | Full Form | Shielding | Max Speed | Max Distance | Use Case |
|------|-----------|-----------|-----------|--------------|----------|
| **UTP** | Unshielded Twisted Pair | None | 10 Gbps | 100 m | LAN (Ethernet) |
| **STP** | Shielded Twisted Pair | Metal shield | 10 Gbps | 100 m | Industrial, high EMI |
| **FTP** | Foil Twisted Pair | Foil wrap | 10 Gbps | 100 m | Intermediate protection |

**Categories (GATE Important):**

| Category | Bandwidth | Speed | Standard |
|----------|-----------|-------|----------|
| Cat 3 | 16 MHz | 10 Mbps | 10BASE-T |
| Cat 5 | 100 MHz | 100 Mbps | 100BASE-TX |
| Cat 5e | 100 MHz | 1 Gbps | 1000BASE-T |
| Cat 6 | 250 MHz | 10 Gbps (55m) | 10GBASE-T |
| Cat 6a | 500 MHz | 10 Gbps (100m) | 10GBASE-T |
| Cat 7 | 600 MHz | 10 Gbps | 10GBASE-T |

**Memory Trick**: "**5** for **100**, **5e** for **1G**, **6** for **10G**"

#### Coaxial Cable

```
    ┌────────────────────────────────────────┐
    │  ████████  Outer jacket (plastic)      │
    │  ▓▓▓▓▓▓▓▓  Braided shield (metal)      │
    │  ░░░░░░░░  Insulator (dielectric)      │
    │  ────────  Inner conductor (copper)    │
    └────────────────────────────────────────┘
```

| Type | Impedance | Use |
|------|-----------|-----|
| **50 Ω (Thinnet)** | Baseband | Digital transmission, LAN |
| **75 Ω (Thicknet)** | Broadband | Cable TV, analog |

| Aspect | Details |
|--------|---------|
| Bandwidth | Up to 500 MHz |
| Distance | Up to 500 m (thicknet) |
| Noise Immunity | Better than twisted pair |
| Cost | Higher than twisted pair |

#### Fiber Optic Cable

```
    ┌─────────────────────────────────────────┐
    │  ▓▓▓▓▓▓▓▓▓▓  Outer jacket              │
    │  ░░░░░░░░░░  Cladding (lower RI)       │
    │  ●●●●●●●●●●  Core (higher RI)          │
    │              Light travels here →→→    │
    └─────────────────────────────────────────┘
    Light undergoes Total Internal Reflection (TIR)
```

| Aspect | Single-Mode Fiber (SMF) | Multi-Mode Fiber (MMF) |
|--------|-------------------------|------------------------|
| Core Diameter | 8-10 μm | 50-62.5 μm |
| Light Source | Laser | LED |
| Distance | Up to 100 km | Up to 2 km |
| Bandwidth | Very High (Tbps) | Lower (Gbps) |
| Cost | Higher | Lower |
| Use | Long-haul, WAN | LAN, short distance |
| Dispersion | Less (single path) | More (multiple paths) |

**GATE Formula - Critical Angle:**
$$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)$$

Where $n_1$ = core refractive index, $n_2$ = cladding refractive index, $n_1 > n_2$

**Advantages of Fiber:**
- Immunity to EMI
- Higher bandwidth
- Longer distance
- Lighter weight
- Security (difficult to tap)

### 2.2.3 Unguided Media (Wireless)

| Type | Frequency | Range | Use Case |
|------|-----------|-------|----------|
| **Radio Waves** | 3 kHz - 1 GHz | Long | AM/FM, WiFi, Bluetooth |
| **Microwaves** | 1-300 GHz | Line of sight | Satellite, point-to-point |
| **Infrared** | 300 GHz - 400 THz | Very short | Remote controls, IrDA |

#### Radio Wave Propagation

| Mode | Frequency | Mechanism | Example |
|------|-----------|-----------|---------|
| **Ground Wave** | < 2 MHz | Follows Earth's curvature | AM radio |
| **Sky Wave** | 2-30 MHz | Reflects off ionosphere | Shortwave radio |
| **Line of Sight** | > 30 MHz | Direct path | FM, TV, Microwave |

**Line of Sight Formula:**
$$d = \sqrt{2Rh}$$

Where:
- $d$ = Line of sight distance
- $R$ = Earth's radius (≈ 6378 km)
- $h$ = Antenna height

For two antennas with heights $h_1$ and $h_2$:
$$d = \sqrt{2Rh_1} + \sqrt{2Rh_2}$$

---

## 2.3 Analog vs Digital Transmission

### Key Differences

| Aspect | Analog | Digital |
|--------|--------|---------|
| Signal | Continuous wave | Discrete pulses |
| Values | Infinite | Finite (typically 2) |
| Noise | Amplified with signal | Can be regenerated |
| Example | AM/FM radio | Computer data |
| Quality | Degrades with distance | Maintained with regeneration |

### Signal Parameters

| Parameter | Symbol | Unit | Description |
|-----------|--------|------|-------------|
| Amplitude | A | Volts | Signal strength |
| Frequency | f | Hz | Cycles per second |
| Period | T | Seconds | Time for one cycle, $T = 1/f$ |
| Phase | φ | Degrees/Radians | Position in cycle |
| Wavelength | λ | Meters | Physical length, $λ = v/f$ |

**Relationship:**
$$v = f \times \lambda$$

Where $v$ = velocity of propagation

---

## 2.4 Digital-to-Digital Encoding (Line Coding) ⭐

### 2.4.1 Why Encoding Matters
- Convert digital data to digital signal
- Provide synchronization
- Detect errors
- Optimize bandwidth usage

### 2.4.2 Encoding Schemes

#### Unipolar (NRZ - Non-Return to Zero)

```
Bit:    1    0    1    1    0    0    1
        ┌────┐    ┌────┬────┐         ┌────
Signal: │    │    │    │    │         │
    ────┘    └────┘    │    └────┬────┘
                       │         │
Positive = 1, Zero = 0
```

| Issue | Description |
|-------|-------------|
| DC Component | Average is non-zero |
| Synchronization | Long runs of same bit cause clock drift |
| Baseline Wander | DC component causes signal drift |

#### Polar NRZ-L and NRZ-I

**NRZ-L (Level):**
```
Bit:    1    0    1    1    0    0    1
        ┌────┐    ┌────┬────┐         ┌────
    ────┘    └────┘    │    └────┬────┘
Positive = 1, Negative = 0
```

**NRZ-I (Invert on 1):**
```
Bit:      1      0      1      1      0      0      1
        ──┬────┬────────┬────┬────────┬────────────┬────
Invert on │    │        │    │        │            │
1         └────┘        └────┘        └────────────┘
```

| Type | Transition | Problem |
|------|------------|---------|
| NRZ-L | Level determines bit | Long 0s or 1s cause sync loss |
| NRZ-I | Transition = 1, No transition = 0 | Long 0s cause sync loss |

#### Manchester Encoding (Self-Clocking) ⭐

```
Bit:       1         0         1         1         0
       ┌────┐    ────┬────    ┌────┐    ┌────┐    ────┬────
       │    │        │        │    │    │    │        │
    ───┘    └────    └────    ┘    └────┘    └────    └────
           ↑              ↑
    Mid-bit transition (ALWAYS)
    
1 = High-to-Low transition (↓) at mid-bit
0 = Low-to-High transition (↑) at mid-bit
```

| Aspect | Details |
|--------|---------|
| Transition | ALWAYS at mid-bit |
| 1 | High → Low |
| 0 | Low → High |
| Synchronization | Excellent (self-clocking) |
| Bandwidth | 2× NRZ (double rate needed) |
| Use | 10BASE-T Ethernet |

**GATE Trap**: Manchester encoding guarantees transition at mid-bit, not at bit boundary!

#### Differential Manchester

```
Bit:       1         0         1         1         0
       ┌────┐    ────┬────    ┌────┐    ────┬────    ────┬────
       │    │        │        │    │        │           │
    ───┘    └────    └────────┘    └────    └───────────┘
       
1 = NO transition at start (only mid-bit transition)
0 = Transition at start AND mid-bit
```

| Aspect | Details |
|--------|---------|
| Mid-bit | ALWAYS transition (clocking) |
| Start of bit | 1 = No transition, 0 = Transition |
| Advantage | More noise immune than Manchester |
| Use | Token Ring |

#### Bipolar AMI (Alternate Mark Inversion)

```
Bit:      1       0       1       0       0       1
        ┌───┐           ┌───┐                   ┌───┐
        │   │           │   │                   │   │
    ────┴───┴───────────┴───┴───────────────────┘   └───
        │               │                       │
    +V  │   0V      -V  │                   +V  │
    (alternating polarity for 1s)
```

| Aspect | Details |
|--------|---------|
| 0 | Zero voltage |
| 1 | Alternating +V and -V |
| DC Component | Zero (balanced) |
| Error Detection | Violation if two consecutive same polarity |
| Issue | Long zeros still cause sync loss |

#### B8ZS and HDB3 (Solutions for Long Zeros)

**B8ZS (Bipolar with 8-Zero Substitution):**
- Used in North America (T1 lines)
- 8 consecutive zeros replaced with: `000VB0VB`
- V = Violation (same polarity as previous), B = Bipolar (alternating)

**HDB3 (High Density Bipolar 3):**
- Used in Europe (E1 lines)
- 4 consecutive zeros replaced based on number of 1s since last substitution

### 2.4.3 Encoding Comparison Table ⭐

| Scheme | Sync | DC Component | Bandwidth | Error Detection |
|--------|------|--------------|-----------|-----------------|
| NRZ-L | Poor | Yes | B | No |
| NRZ-I | Better (for 1s) | Yes | B | No |
| Manchester | Excellent | No | 2B | No |
| Diff Manchester | Excellent | No | 2B | No |
| AMI | Good (for 1s) | No | B | Yes (violation) |
| B8ZS/HDB3 | Excellent | No | B | Yes |

**Bandwidth Relationship:**
- NRZ: $B = \frac{N}{2}$ where N = bit rate
- Manchester: $B = N$ (requires double bandwidth)

---

## 2.5 Analog-to-Digital Conversion ⭐

### 2.5.1 Pulse Code Modulation (PCM)

```
Step 1: Sampling      Step 2: Quantization      Step 3: Encoding
   ╱╲                    ▪  ●                      011 100
  ╱  ╲                   ▪    ●                    101 110
 ╱    ╲                  ▪      ●                  111 101
╱      ╲                 ▪        ●                ...
Continuous → Discrete    Discrete → Levels         Levels → Binary
```

#### Nyquist Theorem (Sampling Rate) ⭐⭐⭐

$$f_s \geq 2 \times f_{max}$$

Where:
- $f_s$ = Sampling frequency
- $f_{max}$ = Maximum frequency in analog signal
- $2 \times f_{max}$ = Nyquist rate

**GATE Trap**: If sampling rate is LESS than Nyquist rate → **Aliasing** (distortion)

#### Quantization
- Divide amplitude range into $L$ levels
- $L = 2^n$ where $n$ = number of bits per sample
- **Quantization Error**: $\leq \frac{\Delta}{2}$ where $\Delta = \frac{V_{max} - V_{min}}{L}$

#### PCM Bit Rate Formula ⭐

$$\text{Bit Rate} = f_s \times n = f_s \times \log_2 L$$

**Example**: Telephone audio
- Voice frequency: 0-4 kHz → $f_{max} = 4$ kHz
- Sampling rate: $f_s = 8$ kHz (Nyquist: $2 \times 4 = 8$)
- Quantization levels: $L = 256 = 2^8$ → 8 bits
- **Bit Rate** = $8000 \times 8 = 64$ kbps

### 2.5.2 Delta Modulation (DM)

```
Original signal: ────╱╲╱╲────
                    ╱    ╲
Delta output:     010110101001
(1 = step up, 0 = step down)
```

| Aspect | Details |
|--------|---------|
| Concept | 1 bit per sample (up/down) |
| Bit Rate | Equal to sampling rate |
| Advantage | Simpler than PCM |
| Disadvantage | Slope overload (rapid changes), Granular noise (slow changes) |

**Comparison**: PCM vs DM

| Aspect | PCM | DM |
|--------|-----|-----|
| Bits/sample | n (typically 8) | 1 |
| Complexity | Higher | Lower |
| Quality | Better | Acceptable |
| Bandwidth | Higher | Lower |

---

## 2.6 Digital-to-Analog Modulation ⭐

### 2.6.1 Amplitude Shift Keying (ASK)

```
Bit:    1      0      1      1      0
      ╱╲╱╲╱╲  ────  ╱╲╱╲╱╲╱╲╱╲╱╲  ────
     ╱      ╲      ╱            ╲
    ╱        ╲    ╱              ╲
   
1 = Carrier present, 0 = No carrier (or lower amplitude)
```

| Aspect | Details |
|--------|---------|
| Varies | Amplitude |
| Constant | Frequency, Phase |
| Bandwidth | $B = (1 + d) \times N$ where d = factor (0-1), N = bit rate |
| Minimum BW | $B = N$ (when d = 0) |
| Susceptible to | Noise (amplitude-based) |

### 2.6.2 Frequency Shift Keying (FSK)

```
Bit:     1         0         1         1         0
      ╱╲╱╲╱╲    ╱╲  ╱╲    ╱╲╱╲╱╲    ╱╲╱╲╱╲    ╱╲  ╱╲
     ╱      ╲  ╱  ╲╱  ╲  ╱            ╲  ╱  ╲╱  ╲
    High freq    Low freq    High freq    Low freq
```

| Aspect | Details |
|--------|---------|
| Varies | Frequency |
| Constant | Amplitude |
| Bandwidth | $B = (1 + d) \times N + (f_1 - f_0)$ |
| Less susceptible | To noise than ASK |

### 2.6.3 Phase Shift Keying (PSK)

#### Binary PSK (BPSK)
```
Bit:     1              0              1
      ╱╲╱╲╱╲        ╲╱╲╱╲╱        ╱╲╱╲╱╲
     ╱      ╲      ╱      ╲      ╱      ╲
    (0° phase)    (180° phase)   (0° phase)
```

#### Quadrature PSK (QPSK)
- 4 different phases: 0°, 90°, 180°, 270°
- 2 bits per signal element (symbol)
- Each symbol = dibit (00, 01, 10, 11)

**Constellation Diagram (QPSK):**
```
                90° (01)
                   │
                   │
    180° (11) ─────┼───── 0° (00)
                   │
                   │
               270° (10)
```

### 2.6.4 Quadrature Amplitude Modulation (QAM)

Combines ASK + PSK → Varies both amplitude and phase

**16-QAM**: 16 signal points → 4 bits per symbol
**64-QAM**: 64 signal points → 6 bits per symbol
**256-QAM**: 256 signal points → 8 bits per symbol

### Modulation Comparison ⭐

| Modulation | Bits/Symbol | Bandwidth Efficiency | Noise Immunity | Use |
|------------|-------------|---------------------|----------------|-----|
| ASK | 1 | Low | Poor | Simple systems |
| FSK | 1 | Low | Good | Modems |
| BPSK | 1 | Moderate | Good | Deep space |
| QPSK | 2 | Good | Good | Satellite |
| 8-PSK | 3 | Good | Moderate | Digital radio |
| 16-QAM | 4 | High | Moderate | Cable modems |
| 64-QAM | 6 | Very High | Fair | WiFi, DVB |

---

## 2.7 Multiplexing ⭐⭐

### 2.7.1 What is Multiplexing?

```
Multiple inputs → MUX → Single shared channel → DEMUX → Multiple outputs

  Signal 1 ──┐                                      ┌── Signal 1
  Signal 2 ──┼──► [MUX] ══════════════► [DEMUX] ◄──┼── Signal 2
  Signal 3 ──┘                                      └── Signal 3
```

**Analogy**: Highway with multiple lanes - each lane carries different traffic but shares same road.

### 2.7.2 Frequency Division Multiplexing (FDM)

```
Frequency
    ▲
    │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
    │  │ Ch1 │ │ Ch2 │ │ Ch3 │ │ Ch4 │
    │  └─────┘ └─────┘ └─────┘ └─────┘
    │     │       │       │       │
    │  Guard   Guard   Guard   Guard
    │  Band    Band    Band    Band
    └──────────────────────────────────────► Time
```

| Aspect | Details |
|--------|---------|
| Domain | Frequency |
| Channels | Each gets fixed frequency band |
| Guard Band | Prevents interference between channels |
| Type | Analog multiplexing |
| Example | Radio/TV broadcasting, cable TV |

**GATE Formula:**
$$\text{Total Bandwidth} = n \times B_{channel} + (n-1) \times B_{guard}$$

Or with guard bands on both sides:
$$\text{Total Bandwidth} = n \times (B_{channel} + B_{guard})$$

### 2.7.3 Time Division Multiplexing (TDM)

```
Time →
┌────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ A1 │ B1 │ C1 │ D1 │ A2 │ B2 │ C2 │ D2 │ ...│
└────┴────┴────┴────┴────┴────┴────┴────┴────┘
 ◄────── Frame 1 ──────► ◄────── Frame 2 ──────►
```

#### Synchronous TDM

| Aspect | Details |
|--------|---------|
| Domain | Time |
| Slot Assignment | Fixed slot for each channel |
| Efficiency | May waste slots if channel has no data |
| Frame | Contains one slot from each channel |
| Synchronization | Required between sender/receiver |

**GATE Formulas:**

$$\text{Frame Rate} = \frac{\text{Data Rate of each input}}{\text{Bits per slot}}$$

$$\text{Frame Duration} = \frac{1}{\text{Frame Rate}}$$

$$\text{Link Data Rate} = n \times \text{Input Data Rate}$$

**Example**: 4 channels, each 1 kbps, 1 bit per slot
- Frame Rate = 1000 frames/second
- Frame Duration = 1 ms
- Link Rate = 4 kbps

#### Statistical TDM (Asynchronous TDM)

```
┌──────┬──────┬──────┬──────┐
│ A:D1 │ C:D2 │ A:D2 │ D:D1 │   (Address + Data)
└──────┴──────┴──────┴──────┘
```

| Aspect | Details |
|--------|---------|
| Slot Assignment | On-demand |
| Address | Required in each slot |
| Efficiency | Higher (no empty slots) |
| Overhead | Address field adds overhead |

### 2.7.4 Wavelength Division Multiplexing (WDM)

```
           λ1 ─────┐
           λ2 ─────┼──► [Prism/Combiner] ══fiber══► [Splitter] ──► λ1
           λ3 ─────┤                                           ──► λ2
           λ4 ─────┘                                           ──► λ3
                                                               ──► λ4
```

| Aspect | Details |
|--------|---------|
| Medium | Optical fiber |
| Concept | FDM for light (different wavelengths/colors) |
| DWDM | Dense WDM - many channels, tight spacing |
| CWDM | Coarse WDM - fewer channels, wider spacing |
| Capacity | Tbps possible |

### 2.7.5 Code Division Multiplexing (CDM/CDMA)

Each station gets unique code, all transmit simultaneously at same frequency.

| Aspect | Details |
|--------|---------|
| Code | Unique chip sequence per station |
| Property | Codes are orthogonal |
| Transmission | All stations use same frequency, same time |
| Reception | Receiver uses code to extract intended signal |
| Example | 3G mobile networks |

**Orthogonal Codes**: Inner product = 0 for different codes

---

## 2.8 Channel Capacity Theorems ⭐⭐⭐

### 2.8.1 Nyquist Formula (Noiseless Channel)

$$C = 2B \log_2 L$$

Where:
- $C$ = Channel capacity (bps)
- $B$ = Bandwidth (Hz)
- $L$ = Number of signal levels

**Maximum bit rate for given bandwidth and signal levels**

**Example**: 3 kHz bandwidth, 4 signal levels
$$C = 2 \times 3000 \times \log_2 4 = 2 \times 3000 \times 2 = 12000 \text{ bps}$$

### 2.8.2 Shannon Capacity (Noisy Channel) ⭐⭐⭐

$$C = B \log_2(1 + SNR)$$

Where:
- $C$ = Channel capacity (bps)
- $B$ = Bandwidth (Hz)
- $SNR$ = Signal-to-Noise Ratio (linear, not dB!)

**Conversion**: If SNR given in dB:
$$SNR_{linear} = 10^{SNR_{dB}/10}$$

**The Golden Insight** 💡:
- Shannon gives **theoretical maximum**
- Practical systems achieve 60-90% of Shannon limit
- Increasing signal levels beyond a point doesn't help (noise limits capacity)

### 2.8.3 Combining Nyquist and Shannon

**Strategy for GATE**:
1. Calculate capacity using both formulas
2. **Take the minimum** as actual capacity
3. Nyquist tells max levels useful, Shannon tells theoretical limit

**Example (GATE Style)**:
> Channel: B = 1 MHz, SNR = 63 (linear). Find max bit rate and signal levels.

**Shannon**: $C = 10^6 \times \log_2(1 + 63) = 10^6 \times \log_2 64 = 6$ Mbps

**For Nyquist to match**:
$6 \times 10^6 = 2 \times 10^6 \times \log_2 L$
$\log_2 L = 3$
$L = 8$ signal levels

---

## 2.9 Transmission Impairments

### 2.9.1 Attenuation

Signal strength decreases with distance.

$$\text{Attenuation (dB)} = 10 \log_{10}\frac{P_1}{P_2}$$

Where $P_1$ = transmitted power, $P_2$ = received power

**Solution**: Amplifiers (analog) or Repeaters (digital)

### 2.9.2 Distortion

Signal shape changes due to different frequency components traveling at different speeds.

| Type | Cause | Effect |
|------|-------|--------|
| Delay Distortion | Frequency-dependent velocity | Signal spreading |
| Amplitude Distortion | Frequency-dependent attenuation | Shape change |

### 2.9.3 Noise

| Type | Cause | Characteristics |
|------|-------|-----------------|
| **Thermal** | Random electron motion | White noise, unavoidable |
| **Induced** | External sources (motors) | Can be shielded |
| **Crosstalk** | Adjacent wires | Twisted pairs help |
| **Impulse** | Lightning, power surges | Spikes, random |

**SNR Calculation:**
$$SNR = \frac{P_{signal}}{P_{noise}}$$

$$SNR_{dB} = 10 \log_{10} SNR = 10 \log_{10}\frac{P_{signal}}{P_{noise}}$$

---

## 2.10 Transmission Calculations ⭐

### Key Formulas

| Parameter | Formula | Units |
|-----------|---------|-------|
| Transmission Time | $T_t = \frac{L}{B}$ | seconds |
| Propagation Time | $T_p = \frac{d}{v}$ | seconds |
| Total Delay | $T_{total} = T_t + T_p$ | seconds |
| Throughput | $\frac{L}{T_{total}}$ | bps |
| Efficiency | $\frac{T_t}{T_t + 2T_p}$ (for stop-and-wait) | ratio |
| Bandwidth-Delay Product | $B \times T_p$ | bits |

### Propagation Velocity by Medium

| Medium | Velocity |
|--------|----------|
| Copper wire | $\approx 2 \times 10^8$ m/s |
| Fiber optic | $\approx 2 \times 10^8$ m/s |
| Air/Vacuum | $3 \times 10^8$ m/s |

### Example Problem (GATE Style)

> A 10 Mbps link is 2000 km long. Frame size is 5000 bits. Propagation velocity is $2 \times 10^8$ m/s.
> Find: (a) Transmission time (b) Propagation time (c) Time to receive first bit (d) Time for complete frame

**Solution:**

(a) $T_t = \frac{5000}{10 \times 10^6} = 500 \mu s = 0.5 ms$

(b) $T_p = \frac{2000 \times 10^3}{2 \times 10^8} = 10 ms$

(c) First bit received after: $T_t + T_p$? NO! First bit is on wire immediately.
    Time for first bit = $T_p = 10 ms$

(d) Complete frame received = $T_t + T_p = 0.5 + 10 = 10.5 ms$

**The "Aha!" Moment** 💡:
- First bit leaves sender at $t = 0$
- First bit reaches receiver at $t = T_p$
- Last bit leaves sender at $t = T_t$
- Last bit reaches receiver at $t = T_t + T_p$

---

## 2.11 Switching at Physical Layer

### 2.11.1 Circuit Switching
Already covered in Chapter 1. Key points:
- Dedicated path established
- Three phases: Setup, Transfer, Teardown
- Examples: PSTN, ISDN

### 2.11.2 Space-Division vs Time-Division Switching

| Type | Method | Use |
|------|--------|-----|
| Space-Division | Physical crossbar matrix | Traditional telephone exchanges |
| Time-Division | Time slots + memory | Digital switches |

**Crossbar Switch**:
$$\text{Crosspoints} = N \times M$$
For N×N switch: $N^2$ crosspoints

**Multi-stage Switch** (reduces crosspoints):
Example: Clos network reduces from $N^2$ to approximately $4N\sqrt{N}$

---

## 2.12 Edge Cases & GATE Traps

### Trap 1: Bandwidth Units
- **Analog Bandwidth**: Hz (range of frequencies)
- **Digital Bandwidth**: bps (bit rate)
- Don't confuse them!

### Trap 2: SNR in dB vs Linear
Shannon formula uses LINEAR SNR, not dB!

If given SNR = 30 dB:
$$SNR_{linear} = 10^{30/10} = 10^3 = 1000$$

### Trap 3: Nyquist Rate vs Sampling Rate
- **Nyquist Rate** = $2 \times f_{max}$ (minimum required)
- **Actual Sampling Rate** can be higher
- If asked "Nyquist rate" give $2 \times f_{max}$
- If asked "sampling frequency" might be higher

### Trap 4: Manchester Bandwidth
Manchester encoding requires DOUBLE the bandwidth of NRZ.
If NRZ needs B Hz, Manchester needs 2B Hz for same bit rate.

### Trap 5: Frame vs Slot in TDM
- **Frame** = complete cycle containing all channels
- **Slot** = portion of frame for one channel
- Frame Rate ≠ Bit Rate

---

## 📝 Chapter Summary

| Concept | Key Formula/Point |
|---------|-------------------|
| Twisted Pair | Cat5e for 1 Gbps, Cat6 for 10 Gbps |
| Fiber | SMF for long distance, MMF for LAN |
| Manchester | Self-clocking, 2× bandwidth |
| PCM | Bit Rate = $f_s \times \log_2 L$ |
| Nyquist | $C = 2B \log_2 L$ |
| Shannon | $C = B \log_2(1 + SNR)$ |
| FDM | Frequency separation, guard bands |
| TDM | Time slots, synchronous or statistical |
| $T_t$ | $L/B$ |
| $T_p$ | $d/v$ |

---

## 🧪 Practice Problems

### Problem 1 (GATE Style)
A noiseless channel has bandwidth 4 kHz. What is the maximum bit rate if we use 8 signal levels?

<details>
<summary>Solution</summary>

Using Nyquist: $C = 2B \log_2 L = 2 \times 4000 \times \log_2 8 = 8000 \times 3 = 24000$ bps = **24 kbps**

</details>

### Problem 2 (GATE Style)
A channel has bandwidth 20 MHz and SNR of 31. What is the theoretical maximum data rate?

<details>
<summary>Solution</summary>

Using Shannon: $C = B \log_2(1 + SNR) = 20 \times 10^6 \times \log_2(32) = 20 \times 10^6 \times 5 = 100$ Mbps

</details>

### Problem 3 (GATE NAT)
4 voice channels are multiplexed using TDM. Each channel is sampled 8000 times/second with 8 bits per sample. Calculate the output bit rate in kbps.

<details>
<summary>Solution</summary>

Each channel: $8000 \times 8 = 64$ kbps
Total for 4 channels: $4 \times 64 = 256$ kbps

</details>

---

**Previous Chapter**: [← Chapter 1: Introduction](./Chapter-01-Introduction.md)

**Next Chapter**: [Chapter 3: Data Link Layer →](./Chapter-03-Data-Link-Layer.md)

---

*Happy Learning!*
