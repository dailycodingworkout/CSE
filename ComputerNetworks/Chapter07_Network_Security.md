# Chapter 7: Network Security

## 🎯 GATE/ESE Weightage: 4-6 marks (Cryptography + Security Concepts)

---

## 7.1 Security Goals (CIA Triad)

```
                    ┌───────────────────┐
                    │  CONFIDENTIALITY  │
                    │   (Keep secret)   │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
    ┌─────────┴─────────┐     │     ┌─────────┴─────────┐
    │    INTEGRITY      │     │     │   AVAILABILITY    │
    │ (Prevent change)  │◄────┴────►│  (Always access)  │
    └───────────────────┘           └───────────────────┘
```

### Security Properties

| Property | Meaning | Threat | Solution |
|----------|---------|--------|----------|
| **Confidentiality** | Only authorized can read | Eavesdropping | Encryption |
| **Integrity** | Data not modified | Tampering | Hashing, MAC |
| **Availability** | Service accessible | DoS | Redundancy |
| **Authentication** | Verify identity | Impersonation | Certificates |
| **Non-repudiation** | Cannot deny action | Denial | Digital signatures |

---

## 7.2 Network Attacks

### Attack Types

| Attack | Type | Description |
|--------|------|-------------|
| **Eavesdropping** | Passive | Listen to communications |
| **Man-in-the-Middle** | Active | Intercept and modify |
| **Replay** | Active | Capture and resend |
| **DoS/DDoS** | Active | Overwhelm with traffic |
| **IP Spoofing** | Active | Fake source IP |
| **ARP Spoofing** | Active | Fake MAC→IP mapping |
| **DNS Spoofing** | Active | Fake DNS responses |
| **Phishing** | Social | Fake websites/emails |

### Attack Layers

| Layer | Attacks |
|-------|---------|
| Physical | Wire tapping, jamming |
| Data Link | ARP spoofing, MAC flooding |
| Network | IP spoofing, ICMP attacks |
| Transport | SYN flood, session hijacking |
| Application | SQL injection, XSS, phishing |

---

## 7.3 Cryptography Basics

### Encryption Model

```
Plaintext ──→ [Encryption] ──→ Ciphertext ──→ [Decryption] ──→ Plaintext
                   ↑                              ↑
                  Key                            Key
```

### Types of Cryptography

```
Cryptography
├── Symmetric Key
│   ├── Block Ciphers (DES, AES)
│   └── Stream Ciphers (RC4)
│
└── Asymmetric Key (Public Key)
    ├── RSA
    ├── Diffie-Hellman
    └── Elliptic Curve (ECC)
```

---

## 7.4 Symmetric Key Cryptography (🎯 IMPORTANT)

### Characteristics

- **Same key** for encryption and decryption
- **Fast** (suitable for bulk data)
- **Key distribution problem** (how to share key securely?)

### DES (Data Encryption Standard)

| Property | Value |
|----------|-------|
| Block size | 64 bits |
| Key size | 56 bits (effective) |
| Rounds | 16 |
| Structure | Feistel network |
| Status | **Broken** (too short key) |

```
DES Structure (Feistel):

Input (64 bits)
      ↓
Initial Permutation
      ↓
┌──────────────┐
│   L₀  │  R₀  │ (32 bits each)
└───┬───┴───┬──┘
    │   ╲   │
    │    ╲  │
    │  F(Rᵢ,Kᵢ)  ← Round key
    │    ╱  │
    ↓   ╱   ↓
┌───────────────┐
│   L₁  │  R₁  │
└───────────────┘
    (16 rounds)
      ↓
Final Permutation
      ↓
Output (64 bits)
```

### Triple DES (3DES)

```
C = E_K3(D_K2(E_K1(P)))

3 keys: 168 bits effective
2 keys (K1=K3): 112 bits effective

Still secure but slow
```

### AES (Advanced Encryption Standard) (🎯 MODERN STANDARD)

| Property | Value |
|----------|-------|
| Block size | 128 bits |
| Key sizes | 128, 192, or 256 bits |
| Rounds | 10, 12, or 14 (based on key) |
| Structure | Substitution-Permutation Network (not Feistel) |
| Status | **Current standard** |

```
AES Round Operations:
1. SubBytes (S-box substitution)
2. ShiftRows (byte shifting)
3. MixColumns (column mixing)
4. AddRoundKey (XOR with round key)
```

### Block Cipher Modes

| Mode | Name | Parallelizable | Error Propagation |
|------|------|----------------|-------------------|
| **ECB** | Electronic Codebook | Yes | Block only |
| **CBC** | Cipher Block Chaining | Decrypt only | Two blocks |
| **CFB** | Cipher Feedback | Decrypt only | Two blocks |
| **OFB** | Output Feedback | No | Bit only |
| **CTR** | Counter | Yes | Bit only |

```
ECB (insecure for patterns):       CBC (chains blocks):
P₁ ──→ [E] ──→ C₁                  P₁ ⊕ IV ──→ [E] ──→ C₁
P₂ ──→ [E] ──→ C₂                  P₂ ⊕ C₁ ──→ [E] ──→ C₂
(Same plaintext → same ciphertext) (Same plaintext → different ciphertext)
```

**🎯 ECB Problem**: Identical blocks produce identical ciphertext (pattern visible)

### Stream Ciphers

```
Keystream ⊕ Plaintext = Ciphertext
Keystream ⊕ Ciphertext = Plaintext

Example: RC4 (broken), ChaCha20 (modern)
```

---

## 7.5 Asymmetric Key Cryptography (🎯 IMPORTANT)

### Characteristics

- **Two keys**: Public (encrypt) + Private (decrypt)
- **Slow** (for key exchange, signatures)
- **Solves key distribution**

### RSA Algorithm (🎯 MUST KNOW)

#### Key Generation

```
1. Choose two large primes: p, q
2. Compute n = p × q
3. Compute φ(n) = (p-1)(q-1)  [Euler's totient]
4. Choose e such that: 1 < e < φ(n) and gcd(e, φ(n)) = 1
5. Compute d such that: d × e ≡ 1 (mod φ(n))

Public Key: (e, n)
Private Key: (d, n)  [keep d, p, q secret]
```

#### Encryption/Decryption

```
Encryption: C = M^e mod n  (using public key)
Decryption: M = C^d mod n  (using private key)
```

#### Example

```
p = 3, q = 11
n = 3 × 11 = 33
φ(n) = 2 × 10 = 20
e = 7 (gcd(7, 20) = 1)
d = 3 (7 × 3 = 21 ≡ 1 mod 20)

Public Key: (7, 33)
Private Key: (3, 33)

Encrypt M = 2:  C = 2^7 mod 33 = 128 mod 33 = 29
Decrypt C = 29: M = 29^3 mod 33 = 24389 mod 33 = 2 ✓
```

### Diffie-Hellman Key Exchange

```
Public: Prime p, Generator g

Alice                              Bob
  │                                  │
  │ Choose secret a                  │ Choose secret b
  │ Compute A = g^a mod p            │ Compute B = g^b mod p
  │                                  │
  │────────── Send A ───────────────→│
  │←───────── Send B ────────────────│
  │                                  │
  │ Compute K = B^a mod p            │ Compute K = A^b mod p
  │ K = g^(ab) mod p                 │ K = g^(ab) mod p
  │                                  │
        Shared Secret Key K!
```

**Security**: Computing a from g^a mod p is hard (discrete log problem)

**Vulnerability**: Man-in-the-Middle (no authentication)

### RSA vs Diffie-Hellman

| RSA | Diffie-Hellman |
|-----|----------------|
| Encryption + Signatures | Key exchange only |
| Needs PKI for authentication | Vulnerable to MITM alone |
| Based on factoring | Based on discrete log |

---

## 7.6 Hash Functions

### Properties

| Property | Description |
|----------|-------------|
| **Deterministic** | Same input → same output |
| **Fixed output** | Any size input → fixed size output |
| **One-way** | Can't find input from output |
| **Collision-resistant** | Hard to find two inputs with same hash |
| **Avalanche effect** | Small change → completely different hash |

### Common Hash Functions

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| MD5 | 128 bits | **Broken** |
| SHA-1 | 160 bits | **Weak** |
| SHA-256 | 256 bits | **Secure** |
| SHA-3 | 256/512 bits | **Secure** |

### Hash Applications

1. **Password storage** (store hash, not password)
2. **Data integrity** (checksum)
3. **Digital signatures** (sign hash, not data)
4. **Message authentication** (HMAC)

---

## 7.7 Digital Signatures (🎯 IMPORTANT)

### Purpose

- **Authentication**: Verify sender identity
- **Integrity**: Detect modifications
- **Non-repudiation**: Sender cannot deny

### Digital Signature Process

```
SIGNING:
                    ┌────────────┐
Message ──────────→ │   Hash     │ ──→ Digest ──→ [Encrypt with  ──→ Signature
                    └────────────┘                Private Key]

VERIFICATION:
                    ┌────────────┐
Message ──────────→ │   Hash     │ ──→ Digest₁
                    └────────────┘          ↓
                                        Compare
                                            ↑
Signature ────────→ [Decrypt with  ──→ Digest₂
                     Public Key]

If Digest₁ = Digest₂, signature is valid
```

### Why Hash First?

- RSA is slow for large data
- Hash produces fixed-size digest
- Sign small digest, not large message

### Digital Signature Algorithms

| Algorithm | Based On |
|-----------|----------|
| RSA Signature | RSA |
| DSA | Discrete log |
| ECDSA | Elliptic curves |
| EdDSA | Edwards curves |

---

## 7.8 Public Key Infrastructure (PKI)

### Problem

How do you trust a public key belongs to claimed owner?

### Solution: Certificates

```
┌─────────────────────────────────────────────────────────┐
│                    X.509 Certificate                    │
├─────────────────────────────────────────────────────────┤
│ Version                                                 │
│ Serial Number                                           │
│ Signature Algorithm                                     │
│ Issuer (CA name)                                        │
│ Validity (Not Before, Not After)                        │
│ Subject (Owner name)                                    │
│ Subject Public Key                                      │
│ Extensions                                              │
├─────────────────────────────────────────────────────────┤
│ Digital Signature (CA's signature)                      │
└─────────────────────────────────────────────────────────┘
```

### Certificate Authority (CA) Hierarchy

```
                ┌─────────────┐
                │   Root CA   │ (Self-signed, trusted)
                └──────┬──────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
    ┌─────┴─────┐ ┌────┴────┐ ┌─────┴─────┐
    │Intermediate│ │   ...   │ │Intermediate│
    │    CA     │ │         │ │    CA     │
    └─────┬─────┘ └─────────┘ └─────┬─────┘
          │                         │
    ┌─────┴─────┐             ┌─────┴─────┐
    │  Server   │             │  Server   │
    │Certificate│             │Certificate│
    └───────────┘             └───────────┘
```

### Certificate Verification

```
1. Check signature using CA's public key
2. Check validity period
3. Check revocation (CRL or OCSP)
4. Verify certificate chain to trusted root
```

---

## 7.9 SSL/TLS (🎯 VERY IMPORTANT)

### Purpose

- Secure communication over TCP
- Encryption (confidentiality)
- Authentication (certificates)
- Integrity (MAC)

### TLS Handshake

```
Client                                          Server
   │                                               │
   │──────── ClientHello ─────────────────────────→│
   │         (TLS version, ciphers, random)        │
   │                                               │
   │←─────── ServerHello ─────────────────────────│
   │         (Chosen cipher, random)               │
   │←─────── Certificate ─────────────────────────│
   │←─────── ServerHelloDone ─────────────────────│
   │                                               │
   │──────── ClientKeyExchange ───────────────────→│
   │         (Pre-master secret encrypted)         │
   │──────── ChangeCipherSpec ────────────────────→│
   │──────── Finished ────────────────────────────→│
   │                                               │
   │←─────── ChangeCipherSpec ────────────────────│
   │←─────── Finished ────────────────────────────│
   │                                               │
   │←════════ Application Data ═══════════════════→│
   │         (Encrypted with session key)          │
```

### TLS Versions

| Version | Status |
|---------|--------|
| SSL 2.0 | **Deprecated** |
| SSL 3.0 | **Deprecated** |
| TLS 1.0 | **Deprecated** |
| TLS 1.1 | **Deprecated** |
| TLS 1.2 | Secure |
| TLS 1.3 | **Current** (faster handshake) |

### TLS 1.3 Improvements

- Faster (1-RTT or 0-RTT handshake)
- Removed weak ciphers
- Forward secrecy mandatory
- Encrypted handshake

---

## 7.10 IPSec

### Purpose

Security at **Network Layer** (IP level)

### IPSec Modes

```
TRANSPORT MODE:                    TUNNEL MODE:
┌─────────────────────────┐       ┌──────────────────────────────┐
│ IP │AH/ESP│ TCP │ Data  │       │NewIP│AH/ESP│OldIP│TCP│ Data │
└─────────────────────────┘       └──────────────────────────────┘
  ↑     ↑                           ↑     ↑
  │     └─ Added header             │     └─ Added header
  └─ Original IP unchanged          └─ New outer IP header

Transport: End-to-end              Tunnel: Gateway-to-gateway (VPN)
```

### IPSec Protocols

| Protocol | Purpose |
|----------|---------|
| **AH** (Authentication Header) | Integrity + Authentication (no encryption) |
| **ESP** (Encapsulating Security Payload) | Confidentiality + Integrity + Authentication |
| **IKE** (Internet Key Exchange) | Key management, SA establishment |

### Security Associations (SA)

- Unidirectional security relationship
- Identified by SPI (Security Parameter Index)
- Contains: Algorithm, keys, sequence number

---

## 7.11 Firewalls

### Types

```
PACKET FILTER (Layer 3-4):
┌─────────────────────────────────────────────────────┐
│ Rule  │ Source IP    │ Dest IP     │ Port │ Action │
├───────┼──────────────┼─────────────┼──────┼────────┤
│   1   │ 192.168.1.0  │ Any         │ 80   │ Allow  │
│   2   │ Any          │ 10.0.0.5    │ 22   │ Allow  │
│   3   │ Any          │ Any         │ Any  │ Deny   │
└─────────────────────────────────────────────────────┘

STATEFUL INSPECTION (Layer 3-4):
- Tracks connection state
- Allows return traffic automatically
- More secure than packet filter

APPLICATION GATEWAY (Layer 7):
- Deep packet inspection
- Application-aware (HTTP, FTP)
- Can detect attacks in payload
```

### Firewall Comparison

| Type | Layer | State | Application Aware |
|------|-------|-------|-------------------|
| Packet Filter | 3-4 | No | No |
| Stateful | 3-4 | Yes | No |
| Application Gateway | 7 | Yes | Yes |
| Next-Gen (NGFW) | 3-7 | Yes | Yes + IPS |

### DMZ (Demilitarized Zone)

```
              ┌─────────────────────────────────────┐
              │            INTERNET                 │
              └────────────────┬────────────────────┘
                               │
                        ┌──────┴──────┐
                        │   Firewall  │
                        └──────┬──────┘
              ┌────────────────┼────────────────┐
              │                │                │
         ┌────┴────┐     ┌─────┴─────┐    ┌─────┴────┐
         │   DMZ   │     │  Firewall  │   │          │
         │ (Web,   │     └─────┬─────┘    │          │
         │  Mail)  │           │          │          │
         └─────────┘     ┌─────┴─────┐    └──────────┘
                         │  Internal  │
                         │  Network   │
                         └───────────┘
```

---

## 7.12 VPN (Virtual Private Network)

### Purpose

Secure communication over public network

### VPN Types

| Type | Description |
|------|-------------|
| **Site-to-Site** | Connect two networks (branch offices) |
| **Remote Access** | User connects to corporate network |
| **SSL VPN** | Browser-based, TLS |
| **IPSec VPN** | Network layer, full tunnel |

```
SITE-TO-SITE VPN:
┌────────────┐      ┌─────────────────────────┐      ┌────────────┐
│  Office A  │──────│   Encrypted Tunnel      │──────│  Office B  │
│  Network   │      │   (over Internet)       │      │  Network   │
└────────────┘      └─────────────────────────┘      └────────────┘
```

---

## 7.13 Authentication Protocols

### Kerberos (🎯 GATE FAVORITE)

```
                    ┌─────────────────┐
                    │       KDC       │
                    │ ┌─────┬───────┐ │
                    │ │ AS  │  TGS  │ │
                    │ └─────┴───────┘ │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
     ┌────┴────┐        ┌────┴────┐        ┌────┴────┐
     │ Client  │────────│  Server │        │  Server │
     └─────────┘        └─────────┘        └─────────┘
```

**Kerberos Steps**:
1. Client → AS: Request TGT (Ticket Granting Ticket)
2. AS → Client: TGT (encrypted with client's key)
3. Client → TGS: TGT + request for service
4. TGS → Client: Service ticket
5. Client → Server: Service ticket
6. Server → Client: Server authenticator (mutual auth)

**Key Components**:
- **KDC**: Key Distribution Center (AS + TGS)
- **TGT**: Ticket Granting Ticket (allows requesting service tickets)
- **Session Key**: Temporary key for communication

### RADIUS

- **Remote Authentication Dial-In User Service**
- AAA protocol (Authentication, Authorization, Accounting)
- Client-server model
- Used by ISPs, VPNs, Wi-Fi

---

## 7.14 Common Vulnerabilities

### OWASP Top 10 (Web)

1. Injection (SQL, Command)
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

### Network Attack Mitigations

| Attack | Mitigation |
|--------|------------|
| DoS/DDoS | Rate limiting, CDN, scrubbing |
| MITM | TLS, certificate pinning |
| ARP Spoofing | Static ARP, DAI |
| DNS Spoofing | DNSSEC |
| IP Spoofing | Ingress filtering |
| Replay | Timestamps, nonces, sequence numbers |

---

## 7.15 Key Formulas & Numbers

| Concept | Value |
|---------|-------|
| **DES key** | 56 bits |
| **AES block** | 128 bits |
| **AES keys** | 128/192/256 bits |
| **MD5 output** | 128 bits |
| **SHA-1 output** | 160 bits |
| **SHA-256 output** | 256 bits |
| **RSA minimum** | 2048 bits (key) |
| **TLS 1.3** | Current standard |
| **HTTPS port** | 443 |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: RSA Calculation
**Q**: p=5, q=7, e=5. Find d.
**A**: n=35, φ(n)=24, d×5≡1(mod 24), **d=5**

### Pattern 2: Hash Properties
**Q**: What prevents finding input from hash?
**A**: **Pre-image resistance** (one-way property)

### Pattern 3: Digital Signature
**Q**: Which key signs? Which verifies?
**A**: Sign with **private**, verify with **public**

### Pattern 4: Diffie-Hellman
**Q**: g=5, p=23, a=6, b=15. Find shared key.
**A**: A=5^6 mod 23=8, B=5^15 mod 23=19
       K=19^6 mod 23=8^15 mod 23=**2**

### Pattern 5: Protocol Security
**Q**: Which provides non-repudiation?
**A**: **Digital signatures** (not encryption alone)

---

## 📝 Quick Revision Checklist

- [ ] CIA triad: Confidentiality, Integrity, Availability
- [ ] Symmetric: Same key, fast (AES, DES)
- [ ] Asymmetric: Public/Private keys, slow (RSA, DH)
- [ ] RSA: e×d ≡ 1 (mod φ(n)), φ(n)=(p-1)(q-1)
- [ ] Hash: One-way, collision-resistant (SHA-256)
- [ ] Digital Signature: Hash then encrypt with private key
- [ ] Certificate: Public key + identity + CA signature
- [ ] TLS: Secure TCP, handshake, session keys
- [ ] IPSec: AH (integrity), ESP (encryption), tunnel mode for VPN
- [ ] Firewall: Packet filter, stateful, application gateway
- [ ] Kerberos: TGT from AS, service ticket from TGS

---

## 🔥 One-Liner Summary

> "Security ensures CIA (Confidentiality-Integrity-Availability); Symmetric crypto (AES) is fast for data, Asymmetric (RSA) for key exchange; Hash functions provide integrity (SHA-256); Digital signatures = hash + private key encryption provide authentication + non-repudiation; TLS secures transport (HTTPS), IPSec secures network (VPN); firewalls filter traffic, PKI provides trust via certificates."
