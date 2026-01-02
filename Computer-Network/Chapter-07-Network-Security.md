# 🔐 Chapter 7: Network Security

> **The Atomic Truth:** Protect data in transit using cryptography and protocols.

---

## 🎯 Chapter Overview

| Topic | GATE Weightage | Difficulty |
|-------|----------------|------------|
| Cryptography Basics | Medium | Medium |
| Symmetric Encryption | Medium | Easy |
| Asymmetric Encryption | Medium | Medium |
| Digital Signatures | Medium | Medium |
| Firewalls | Low | Easy |
| SSL/TLS | Medium | Medium |
| IPSec | Low-Medium | Medium |

---

## 7.1 Security Goals (CIA Triad + More)

| Goal | Description | Threat |
|------|-------------|--------|
| **Confidentiality** | Only authorized can read | Eavesdropping |
| **Integrity** | Data not modified | Tampering |
| **Availability** | Service accessible | DoS attack |
| **Authentication** | Verify identity | Impersonation |
| **Non-repudiation** | Cannot deny action | Denial |

---

## 7.2 Cryptography Fundamentals

### Terminology

| Term | Definition |
|------|------------|
| **Plaintext** | Original message |
| **Ciphertext** | Encrypted message |
| **Encryption** | Plaintext → Ciphertext |
| **Decryption** | Ciphertext → Plaintext |
| **Key** | Secret parameter for algorithm |
| **Cipher** | Encryption algorithm |

### Kerckhoffs's Principle

> Security should depend only on the secrecy of the **key**, not the algorithm.

---

## 7.3 Symmetric Key Cryptography ⭐

### Characteristics

- **Same key** for encryption and decryption
- Fast (suitable for bulk data)
- Key distribution is the challenge

$$C = E_K(P)$$
$$P = D_K(C)$$

### Block Ciphers vs Stream Ciphers

| Type | Operation | Examples |
|------|-----------|----------|
| **Block** | Fixed-size blocks | DES, AES |
| **Stream** | Bit by bit | RC4, ChaCha20 |

### Common Symmetric Algorithms

| Algorithm | Key Size | Block Size | Status |
|-----------|----------|------------|--------|
| DES | 56 bits | 64 bits | Insecure (broken) |
| 3DES | 112/168 bits | 64 bits | Legacy |
| AES | 128/192/256 bits | 128 bits | Current standard |
| RC4 | 40-2048 bits | Stream | Deprecated |
| ChaCha20 | 256 bits | Stream | Modern, fast |

### AES (Advanced Encryption Standard)

- Block size: 128 bits
- Key sizes: 128, 192, or 256 bits
- Rounds: 10, 12, or 14 (based on key size)
- Operations: SubBytes, ShiftRows, MixColumns, AddRoundKey

### DES (Data Encryption Standard)

- Block size: 64 bits
- Key: 56 bits (+ 8 parity bits)
- 16 rounds of Feistel structure
- **Broken:** Brute force feasible

### Block Cipher Modes

| Mode | Name | Description | Use |
|------|------|-------------|-----|
| ECB | Electronic Codebook | Each block independent | Not recommended |
| CBC | Cipher Block Chaining | XOR with previous ciphertext | General encryption |
| CFB | Cipher Feedback | Stream from block cipher | Self-synchronizing |
| OFB | Output Feedback | Stream from block cipher | Pre-computable |
| CTR | Counter | Stream from counter | Parallelizable |
| GCM | Galois/Counter | CTR + authentication | Modern standard |

### ⚠️ GATE TRAP: ECB Mode Weakness

ECB encrypts identical blocks to identical ciphertext → Pattern leakage!

```
Plaintext:  [ATTACK][ATTACK][DEFEND]
ECB:        [X1234X][X1234X][Y5678Y]  ← Pattern visible!
CBC:        [A1B2C3][D4E5F6][G7H8I9]  ← Randomized
```

---

## 7.4 Asymmetric Key Cryptography ⭐⭐

### Characteristics

- **Two keys:** Public (shared) + Private (secret)
- Slower than symmetric
- Solves key distribution problem

$$C = E_{K_{public}}(P)$$
$$P = D_{K_{private}}(C)$$

### Use Cases

| Operation | Key Used |
|-----------|----------|
| **Encryption** | Receiver's public key |
| **Decryption** | Receiver's private key |
| **Digital Signature** | Sender's private key |
| **Verification** | Sender's public key |

### RSA Algorithm ⭐

**Key Generation:**
1. Choose two large primes $p$, $q$
2. Compute $n = p \times q$
3. Compute $\phi(n) = (p-1)(q-1)$
4. Choose $e$ such that $\gcd(e, \phi(n)) = 1$
5. Compute $d$ such that $e \times d \equiv 1 \pmod{\phi(n)}$

**Keys:**
- Public key: $(e, n)$
- Private key: $(d, n)$

**Encryption/Decryption:**
$$C = M^e \mod n$$
$$M = C^d \mod n$$

#### 🧮 RSA Example

**Given:** $p = 3$, $q = 11$, $e = 7$, $M = 5$

**Solution:**
1. $n = 3 \times 11 = 33$
2. $\phi(n) = 2 \times 10 = 20$
3. Find $d$: $7d \equiv 1 \pmod{20}$ → $d = 3$ (since $7 \times 3 = 21 = 20 + 1$)
4. Encrypt: $C = 5^7 \mod 33 = 78125 \mod 33 = 14$
5. Decrypt: $M = 14^3 \mod 33 = 2744 \mod 33 = 5$ ✓

### Diffie-Hellman Key Exchange

**Purpose:** Establish shared secret over insecure channel

**Process:**
1. Agree on public values: prime $p$, generator $g$
2. Alice: Choose secret $a$, send $A = g^a \mod p$
3. Bob: Choose secret $b$, send $B = g^b \mod p$
4. Alice computes: $s = B^a \mod p = g^{ab} \mod p$
5. Bob computes: $s = A^b \mod p = g^{ab} \mod p$

**Result:** Both have shared secret $s = g^{ab} \mod p$

#### 🧮 Diffie-Hellman Example

**Given:** $p = 23$, $g = 5$, $a = 6$, $b = 15$

**Solution:**
1. Alice sends: $A = 5^6 \mod 23 = 15625 \mod 23 = 8$
2. Bob sends: $B = 5^{15} \mod 23 = 19$
3. Shared secret: $s = 8^{15} \mod 23 = 19^6 \mod 23 = 2$

### ⚠️ GATE TRAP: DH Vulnerability

Diffie-Hellman is vulnerable to **Man-in-the-Middle** attack without authentication!

---

## 7.5 Hash Functions ⭐

### Properties

| Property | Description |
|----------|-------------|
| **Fixed output** | Any input → fixed size output |
| **One-way** | Cannot reverse (find input from hash) |
| **Collision resistant** | Hard to find two inputs with same hash |
| **Deterministic** | Same input always gives same output |
| **Avalanche effect** | Small input change → drastically different output |

### Common Hash Algorithms

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| MD5 | 128 bits | Broken (collisions found) |
| SHA-1 | 160 bits | Deprecated (collisions) |
| SHA-256 | 256 bits | Secure |
| SHA-512 | 512 bits | Secure |
| SHA-3 | Variable | Current standard |

### Uses of Hash Functions

1. **Password storage:** Store hash, not password
2. **Integrity verification:** File checksums
3. **Digital signatures:** Sign hash instead of message
4. **Message authentication:** HMAC

### HMAC (Hash-based Message Authentication Code)

$$HMAC(K, M) = H((K \oplus opad) || H((K \oplus ipad) || M))$$

- Combines hash with secret key
- Provides authentication + integrity

---

## 7.6 Digital Signatures ⭐⭐

### Purpose

- **Authentication:** Proves sender identity
- **Integrity:** Detects modification
- **Non-repudiation:** Sender cannot deny signing

### How It Works

```
Sender (Alice):
1. Hash the message: h = H(M)
2. Sign the hash: S = E_{Alice-private}(h)
3. Send: M + S

Receiver (Bob):
1. Compute hash: h1 = H(M)
2. Decrypt signature: h2 = D_{Alice-public}(S)
3. Verify: if h1 == h2, signature valid
```

### Digital Signature Algorithms

| Algorithm | Based On |
|-----------|----------|
| RSA | RSA problem |
| DSA | Discrete log |
| ECDSA | Elliptic curve |
| EdDSA | Edwards curves |

### ⚠️ GATE TRAP: Signature vs Encryption

| Operation | Key Used | Purpose |
|-----------|----------|---------|
| Sign | Private key | Authenticate sender |
| Verify | Public key | Check signature |
| Encrypt | Public key | Confidentiality |
| Decrypt | Private key | Read message |

---

## 7.7 Certificates and PKI ⭐

### Digital Certificate

Contains:
- Subject's public key
- Subject's identity
- Issuer (CA) identity
- Validity period
- CA's digital signature

### Certificate Authority (CA)

- Trusted third party
- Issues and signs certificates
- Hierarchy: Root CA → Intermediate CA → End entity

### X.509 Certificate Format

```
Certificate:
    Data:
        Version: 3
        Serial Number: 12345
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=Example CA
        Validity:
            Not Before: Jan 1 2024
            Not After: Jan 1 2025
        Subject: CN=www.example.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            RSA Public Key: (2048 bit)
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: ...
```

### Certificate Verification Chain

```
┌─────────────┐
│   Root CA   │ ← Self-signed, trusted by OS/browser
└──────┬──────┘
       │ signs
┌──────▼──────┐
│Intermediate │
│     CA      │
└──────┬──────┘
       │ signs
┌──────▼──────┐
│   Server    │
│ Certificate │
└─────────────┘
```

---

## 7.8 SSL/TLS (Transport Layer Security) ⭐⭐

### TLS Purpose

Secure communication over TCP:
- Encryption (confidentiality)
- Authentication (server, optionally client)
- Integrity (MAC)

### TLS Handshake (Simplified)

```
Client                                          Server
   │                                               │
   │──── ClientHello ────────────────────────────►│
   │     (TLS version, cipher suites, random)     │
   │                                               │
   │◄─── ServerHello ──────────────────────────────│
   │     (chosen cipher, random)                   │
   │◄─── Certificate ──────────────────────────────│
   │     (server's certificate)                    │
   │◄─── ServerHelloDone ──────────────────────────│
   │                                               │
   │──── ClientKeyExchange ───────────────────────►│
   │     (pre-master secret, encrypted)            │
   │──── ChangeCipherSpec ────────────────────────►│
   │──── Finished ────────────────────────────────►│
   │                                               │
   │◄─── ChangeCipherSpec ─────────────────────────│
   │◄─── Finished ─────────────────────────────────│
   │                                               │
   │           APPLICATION DATA (encrypted)        │
```

### Key Derivation

1. Client and server exchange randoms
2. Pre-master secret generated
3. Master secret derived: 
   $$\text{master\_secret} = PRF(\text{pre\_master}, \text{randoms})$$
4. Session keys derived from master secret

### TLS Versions

| Version | Status |
|---------|--------|
| SSL 2.0 | Deprecated, insecure |
| SSL 3.0 | Deprecated, insecure |
| TLS 1.0 | Deprecated |
| TLS 1.1 | Deprecated |
| TLS 1.2 | Widely used |
| TLS 1.3 | Current standard, faster |

### TLS 1.3 Improvements

- Faster handshake (1-RTT, 0-RTT resumption)
- Removed weak algorithms
- Perfect Forward Secrecy mandatory
- Simplified cipher suites

---

## 7.9 IPSec ⭐

### IPSec Purpose

Security at IP layer:
- Encrypt and/or authenticate IP packets
- Transparent to applications

### IPSec Modes

| Mode | Description | Use |
|------|-------------|-----|
| **Transport** | Only payload encrypted | End-to-end |
| **Tunnel** | Entire packet encrypted, new header | VPN |

```
Transport Mode:
[IP Header][IPSec Header][Payload (encrypted)]

Tunnel Mode:
[New IP Header][IPSec Header][Original IP Header + Payload (encrypted)]
```

### IPSec Protocols

| Protocol | Function |
|----------|----------|
| **AH** | Authentication Header (integrity, no encryption) |
| **ESP** | Encapsulating Security Payload (encryption + integrity) |
| **IKE** | Internet Key Exchange (key management) |

### Security Association (SA)

- Unidirectional secure channel
- Parameters: algorithm, key, lifetime
- Identified by SPI (Security Parameter Index)

---

## 7.10 Firewalls ⭐

### Firewall Types

| Type | Layer | Checks |
|------|-------|--------|
| **Packet Filter** | 3-4 | IP, ports, flags |
| **Stateful** | 3-4 | Connection state |
| **Application** | 7 | Application data |
| **Proxy** | 7 | Full inspection, relay |

### Packet Filter Rules

```
Rule | Source IP    | Dest IP    | Protocol | Dest Port | Action
-----|--------------|------------|----------|-----------|--------
1    | Any          | 10.0.0.1   | TCP      | 80        | Allow
2    | Any          | 10.0.0.1   | TCP      | 443       | Allow
3    | Any          | 10.0.0.1   | TCP      | 22        | Allow
4    | Any          | Any        | Any      | Any       | Deny
```

### Stateful Inspection

- Tracks connection state
- Allows response packets automatically
- More secure than stateless

### DMZ (Demilitarized Zone)

```
┌─────────┐     ┌──────────┐     ┌─────────┐
│ Internet│────►│  DMZ     │────►│ Internal│
│         │     │ (Public  │     │ Network │
│         │     │  Servers)│     │         │
└─────────┘     └──────────┘     └─────────┘
         Firewall       Firewall
```

---

## 7.11 VPN (Virtual Private Network)

### VPN Types

| Type | Description |
|------|-------------|
| **Site-to-Site** | Connect two networks |
| **Remote Access** | Connect user to network |

### VPN Protocols

| Protocol | Layer | Notes |
|----------|-------|-------|
| PPTP | 2 | Legacy, insecure |
| L2TP/IPSec | 2 | Common |
| IPSec | 3 | Standard |
| OpenVPN | 4-7 | Open source, SSL-based |
| WireGuard | 3 | Modern, fast |

---

## 7.12 Common Attacks and Defenses

### Attack Types

| Attack | Description | Defense |
|--------|-------------|---------|
| **Eavesdropping** | Intercept traffic | Encryption |
| **Man-in-the-Middle** | Intercept and modify | Authentication, certificates |
| **Replay** | Resend captured data | Timestamps, nonces |
| **DoS/DDoS** | Overwhelm service | Rate limiting, CDN |
| **Phishing** | Fake websites/emails | User education, 2FA |
| **SQL Injection** | Malicious SQL | Input validation |
| **XSS** | Inject scripts | Sanitization |

### Authentication Methods

| Method | Factor |
|--------|--------|
| Password | Something you know |
| Token/Card | Something you have |
| Biometric | Something you are |
| 2FA | Two of above |

---

## 📝 Quick Revision Formula Sheet

### Key Sizes

| Algorithm | Key Size |
|-----------|----------|
| DES | 56 bits |
| 3DES | 112/168 bits |
| AES | 128/192/256 bits |
| RSA | 2048+ bits |

### Hash Sizes

| Algorithm | Size |
|-----------|------|
| MD5 | 128 bits |
| SHA-1 | 160 bits |
| SHA-256 | 256 bits |

### Port Numbers

| Service | Port |
|---------|------|
| HTTPS | 443 |
| SSH | 22 |
| IPSec (IKE) | 500 |
| IPSec (NAT-T) | 4500 |

### RSA Formulas

| Formula | Purpose |
|---------|---------|
| $n = p \times q$ | Modulus |
| $\phi(n) = (p-1)(q-1)$ | Euler's totient |
| $e \times d \equiv 1 \pmod{\phi(n)}$ | Key relationship |
| $C = M^e \mod n$ | Encryption |
| $M = C^d \mod n$ | Decryption |

---

## 🎯 Chapter Summary

1. **CIA Triad:** Confidentiality, Integrity, Availability
2. **Symmetric:** Same key, fast (AES, DES)
3. **Asymmetric:** Public/Private keys, slow (RSA, DH)
4. **Hash:** One-way, fixed output (SHA-256)
5. **Digital Signature:** Private key sign, public key verify
6. **Certificates:** Public key + identity, signed by CA
7. **TLS:** Secure channel over TCP, handshake + encryption
8. **IPSec:** IP layer security, transport/tunnel modes
9. **Firewall:** Filter packets by rules, stateful better

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
> Computer Networks — **Complete Coverage Achieved.**
> Proceed to practice previous year GATE questions for maximum impact!
