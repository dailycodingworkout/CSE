# Chapter 2: Physical Layer
## The Bit Highway | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Physical layer moves bits; everything else is just patterns in those bits."**

---

## 2.1 Physical Layer Responsibilities

1. Define physical characteristics (voltage levels, timing)
2. Transmit raw bit streams over medium
3. Line configuration (point-to-point, multipoint)
4. Transmission mode (simplex, duplex)
5. Topology

---

## 2.2 Transmission Media

### Guided (Wired) Media

#### Twisted Pair Cable

```
     ┌─────────┐
    ╱╲ ╲╱ ╲╱ ╲  │ Twisted wires
   ╱  ╲╱  ╲   ╲ │ reduce interference
  ────────────  │
```

| Type | Description | Bandwidth | Distance |
|------|-------------|-----------|----------|
| UTP (Cat 5) | Unshielded | 100 Mbps | 100m |
| UTP (Cat 5e) | Enhanced | 1 Gbps | 100m |
| UTP (Cat 6) | Higher quality | 10 Gbps | 55m |
| STP | Shielded | Higher | Better noise resistance |

**Use:** LAN, Telephone

#### Coaxial Cable

```
┌────────────────────────────┐
│ Outer Jacket               │
│  ├─ Braided Shield        │
│  │   ├─ Insulator         │
│  │   │   ├─ Copper Core   │
└────────────────────────────┘
```

| Type | Impedance | Use |
|------|-----------|-----|
| RG-59 | 75Ω | Cable TV |
| RG-58 | 50Ω | Thin Ethernet |
| RG-11 | 50Ω | Thick Ethernet |

**Use:** Cable TV, Older Ethernet

#### Fiber Optic Cable

```
┌────────────────────────────┐
│ Jacket                     │
│  ├─ Buffer                │
│  │   ├─ Cladding (glass) │
│  │   │   ├─ Core (light) │
└────────────────────────────┘
```

| Type | Core Diameter | Distance | Use |
|------|---------------|----------|-----|
| Single-mode | 8-10 μm | 100+ km | WAN, Long distance |
| Multi-mode | 50-62.5 μm | 2 km | LAN, Short distance |

**Advantages:**
- Higher bandwidth (THz range)
- Lower attenuation
- Immune to EMI
- Secure (hard to tap)

**Disadvantages:**
- Expensive
- Difficult to install
- Fragile

### Unguided (Wireless) Media

| Type | Frequency | Range | Use |
|------|-----------|-------|-----|
| Radio Waves | 3 kHz - 1 GHz | Long | AM/FM Radio, TV |
| Microwave | 1 GHz - 300 GHz | Line of sight | Satellite, Cell towers |
| Infrared | 300 GHz - 400 THz | Short | TV remote, IrDA |

---

## 2.3 Digital Encoding Schemes

### Why Encoding?
Convert digital data to digital signal for transmission.

### Line Coding Schemes

#### 1. Unipolar NRZ (Non-Return to Zero)

```
Data: 1  0  1  1  0
      ┌──┐  ┌──┬──┐
   +V │  │  │     │
      │  └──┘     └──
    0 ────────────────
```
- 1 = High, 0 = Low (or zero)
- **Problem:** DC component, synchronization

#### 2. Polar NRZ-L (Level)

```
Data: 1  0  1  1  0
   +V ┌──┐  ┌──┬──┐
      │  │  │     │
    0 ─┼──┼──┼─────┼──
      │  │  │     │
   -V │  └──┘     └──
```
- 1 = Low voltage, 0 = High voltage (or vice versa)
- **Problem:** No self-clocking

#### 3. Polar NRZ-I (Inversion)

```
Data:    1  0  1  1  0
         │  │  │  │  │
   +V ───┼──┬──┼──┼──┬──
         │  │  │  │  │
   -V ───┘  └──┘  └──┘
         ↑     ↑  ↑
      Transition on 1
```
- Transition at bit start = 1, No transition = 0
- **Better for 1s**, still problem with long 0s

#### 4. Manchester Encoding

```
Data: 1  0  1  1  0
      │  │  │  │  │
   +V ┌┐    ┌┐ ┌┐
      ││    ││ ││
    0 ┼┼────┼┼─┼┼────
      ││    ││ ││
   -V │└──┐ ││ ││┌──┐
         │ └┘ └┘│  │
         └─────────┘
```
- 1 = High-to-Low transition (↓) in middle
- 0 = Low-to-High transition (↑) in middle
- **Self-clocking!** Used in Ethernet (10 Mbps)
- **Disadvantage:** Double the bandwidth required

#### 5. Differential Manchester

```
Data: 1  0  1  1  0
      │  │  │  │  │
Transitions in middle always
1 = No transition at start
0 = Transition at start
```
- Always transition in middle (for clock)
- 0 = Transition at beginning, 1 = No transition at beginning
- **Used in:** Token Ring

#### 6. Bipolar AMI (Alternate Mark Inversion)

```
Data: 1  0  1  0  1  0  0
   +V ┌┐       ┌┐
      ││       ││
    0 ┼┼───────┼┼───────
      ││   ┌┐  ││   
   -V ││   ││  ││   
      ─┘   └┘  └┘
```
- 0 = Zero voltage
- 1 = Alternating +V and -V
- **Advantage:** No DC component, error detection (violation)

### 🎯 Encoding Comparison

| Scheme | Self-clocking | DC Component | Bandwidth |
|--------|---------------|--------------|-----------|
| NRZ-L | No | Yes | B |
| NRZ-I | No | Less | B |
| Manchester | Yes | No | 2B |
| Differential Manchester | Yes | No | 2B |
| AMI | No | No | B |

### Bandwidth Formula

$$\text{Minimum Bandwidth} = \frac{\text{Bit Rate}}{2}$$ (for NRZ)

$$\text{Minimum Bandwidth} = \text{Bit Rate}$$ (for Manchester)

---

## 2.4 Analog-to-Digital Conversion

### Pulse Code Modulation (PCM)

```
Analog Signal → [Sampling] → [Quantization] → [Encoding] → Digital
```

#### Step 1: Sampling

**Nyquist Theorem:**
$$f_s \geq 2 \times f_{max}$$

Where $f_s$ = sampling frequency, $f_{max}$ = maximum signal frequency

**Example:** Audio CD
- $f_{max}$ = 20 kHz (human hearing)
- $f_s$ = 44.1 kHz (> 40 kHz)

#### Step 2: Quantization

Divide amplitude range into levels.

$$\text{Levels} = 2^n$$

Where n = number of bits per sample

**Quantization Error:** Difference between actual and quantized value

#### Step 3: Encoding

Assign binary code to each level.

### PCM Bit Rate

$$\text{Bit Rate} = f_s \times n$$

**Example:** CD Audio
- $f_s$ = 44.1 kHz
- n = 16 bits
- Bit rate = 44,100 × 16 = 705,600 bps per channel
- Stereo = 1.4 Mbps

---

## 2.5 Digital-to-Analog Conversion (Modulation)

### Why Modulation?
- Antenna size proportional to wavelength
- Multiplex different signals
- Bandwidth efficiency

### Amplitude Shift Keying (ASK)

```
Data: 1   0   1   1   0
     ~~~~     ~~~~~~~~
         ~~~~        ~~~~
     Amplitude varies
```
- 1 = Carrier present/high amplitude
- 0 = No carrier/low amplitude
- **Susceptible to noise**

### Frequency Shift Keying (FSK)

```
Data: 1   0   1   1   0
     ~~~~ ∿∿∿ ~~~~~~~~ ∿∿∿
     High  Low  High    Low
     Freq  Freq Freq    Freq
```
- 1 = High frequency
- 0 = Low frequency
- **More immune to noise**

### Phase Shift Keying (PSK)

```
BPSK: 2 phases (0°, 180°)
Data: 1       0
     ~~~~    ~~~~
          (phase shift)
          
QPSK: 4 phases (0°, 90°, 180°, 270°)
- Each symbol represents 2 bits
```

### Quadrature Amplitude Modulation (QAM)

Combines ASK and PSK.

$$\text{QAM-}n: n = 2^{bits/symbol}$$

| Type | Bits/Symbol | Symbols |
|------|-------------|---------|
| QPSK | 2 | 4 |
| 16-QAM | 4 | 16 |
| 64-QAM | 6 | 64 |
| 256-QAM | 8 | 256 |

### Baud Rate vs Bit Rate

$$\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Symbol}$$

**Example:** 
- Baud rate = 1000 symbols/second
- QPSK (2 bits/symbol)
- Bit rate = 1000 × 2 = 2000 bps

---

## 2.6 Multiplexing

### Why Multiplexing?
Combine multiple signals over a single medium.

### Frequency Division Multiplexing (FDM)

```
┌─────────────────────────────────────┐
│ Channel 1 │ Guard │ Channel 2 │ ... │
│  f1-f2    │ Band  │  f3-f4    │     │
└─────────────────────────────────────┘
      Frequency →
```
- Each channel gets a frequency band
- Guard bands prevent interference
- **Used in:** Radio, TV, Cable TV

### Time Division Multiplexing (TDM)

```
Frame:
┌────┬────┬────┬────┬────┬────┬────┐
│ A  │ B  │ C  │ A  │ B  │ C  │... │
└────┴────┴────┴────┴────┴────┴────┘
← Time Slot →
```

#### Synchronous TDM
- Fixed time slots for each channel
- Empty slots if no data (waste)

#### Statistical TDM
- Dynamic allocation
- More efficient, needs addressing

### Wavelength Division Multiplexing (WDM)

```
λ1 ──┐
λ2 ──┼──[Multiplexer]──Fiber──[Demux]──┼── λ1
λ3 ──┘                                  ├── λ2
                                        └── λ3
```
- FDM for optical fiber
- Each color is a channel
- **DWDM:** Dense WDM (many wavelengths)

---

## 2.7 Channel Capacity

### Nyquist Formula (Noise-free)

$$C = 2 \times B \times \log_2 L$$

Where:
- C = Channel capacity (bps)
- B = Bandwidth (Hz)
- L = Number of signal levels

**Example:** B = 3000 Hz, L = 2
$$C = 2 \times 3000 \times \log_2 2 = 6000 \text{ bps}$$

### Shannon Formula (With Noise)

$$C = B \times \log_2(1 + \text{SNR})$$

Where:
- SNR = Signal-to-Noise Ratio (power ratio)
- SNR(dB) = 10 × log₁₀(SNR)

**Example:** B = 3000 Hz, SNR = 1023
$$C = 3000 \times \log_2(1024) = 3000 \times 10 = 30000 \text{ bps}$$

### 🎯 GATE Classic

**Q:** A channel has B = 4 kHz, SNR = 63. Find max data rate.

**Solution:**
$$C = 4000 \times \log_2(64) = 4000 \times 6 = 24000 \text{ bps} = 24 \text{ Kbps}$$

---

## 2.8 Transmission Impairments

### Attenuation
Signal weakens over distance.
$$\text{Attenuation (dB)} = 10 \log_{10}\frac{P_1}{P_2}$$

### Distortion
Different frequency components travel at different speeds.
- **Solution:** Equalization

### Noise
- **Thermal Noise:** Random electron movement
- **Induced Noise:** External sources (motors)
- **Crosstalk:** Signal from adjacent wire
- **Impulse Noise:** Spikes (lightning)

---

## 🎯 Practice Problems

### Problem 1: Nyquist Rate
**Q:** Maximum frequency of signal is 5 kHz. What's the minimum sampling rate?
**Answer:** $f_s = 2 \times 5000 = 10000$ Hz = 10 kHz

### Problem 2: PCM Bit Rate
**Q:** Audio signal with max frequency 4 kHz, 8 bits per sample. Find bit rate.
**Solution:**
- $f_s = 2 \times 4000 = 8000$ Hz
- Bit rate = $8000 \times 8 = 64000$ bps = **64 Kbps**

### Problem 3: Shannon Capacity
**Q:** Bandwidth = 10 MHz, SNR = 15 dB. Find capacity.
**Solution:**
- $\text{SNR} = 10^{15/10} = 31.62$
- $C = 10 \times 10^6 \times \log_2(32.62) \approx 10 \times 10^6 \times 5.03 \approx 50$ Mbps

### Problem 4: Baud vs Bit Rate
**Q:** 16-QAM at 10,000 baud. Find bit rate.
**Solution:**
- 16-QAM: 4 bits/symbol (since $2^4 = 16$)
- Bit rate = $10000 \times 4 = 40000$ bps = **40 Kbps**

### Problem 5: Manchester Encoding
**Q:** What's the bandwidth needed for 10 Mbps Manchester encoding?
**Answer:** 10 MHz (Manchester needs bandwidth = bit rate)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Never Really Zero - Manchester Makes Clocks"**
- **N**RZ has **N**o clock
- **M**anchester **M**akes clocks (self-clocking)

### The Mental Slider
Imagine radio dial:
- **FDM:** Different stations at different frequencies
- **TDM:** Same frequency, different time slots
- **WDM:** Different colors of light

### The 5-Second Snap-Check
1. **Self-clocking?** Manchester, Differential Manchester
2. **Nyquist rate?** 2 × max frequency
3. **Shannon limit?** B × log₂(1 + SNR)
4. **Fiber types?** Single-mode (long), Multi-mode (short)
5. **QAM bits?** log₂(constellation points)

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| $f_s \geq 2f_{max}$ | Nyquist sampling theorem |
| $\text{Bit Rate} = f_s \times n$ | PCM bit rate |
| $C = 2B\log_2 L$ | Nyquist capacity |
| $C = B\log_2(1+SNR)$ | Shannon capacity |
| $\text{Bit Rate} = \text{Baud} \times \text{bits/symbol}$ | Modulation |
| $\text{Manchester BW} = \text{Bit Rate}$ | Manchester bandwidth |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Introduction](01-Introduction-Models.md) | [Next: Data Link Layer →](03-Data-Link-Layer.md)
