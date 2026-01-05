# Module 9: Network Security | The Singularity

> **The Atomic Truth:** *Security = Confidentiality + Integrity + Authentication + Non-repudiation*

---

## 9.1 Security Goals (CIA Triad+)

### **The Four Pillars**

| Goal | Definition | Example Attack |
|------|------------|----------------|
| **Confidentiality** | Only authorized access | Eavesdropping |
| **Integrity** | Data not altered | Man-in-the-middle |
| **Authentication** | Verify identity | Spoofing |
| **Non-repudiation** | Cannot deny action | Digital signature |
| **Availability** | Service accessible | DoS attack |

### **The Analogy 💡**
Think of a **sealed letter with a wax stamp**:
- **Confidentiality:** Envelope hides content
- **Integrity:** Breaking seal shows tampering
- **Authentication:** Unique wax stamp identifies sender
- **Non-repudiation:** Stamp proves sender wrote it

---

## 9.2 Cryptography Fundamentals

### **Terminology**

| Term | Definition |
|------|------------|
| **Plaintext** | Original readable message |
| **Ciphertext** | Encrypted unreadable message |
| **Encryption** | Plaintext → Ciphertext |
| **Decryption** | Ciphertext → Plaintext |
| **Key** | Secret parameter for encryption/decryption |
| **Cipher** | Algorithm for encryption/decryption |

### **Types of Cryptography**

```
                    CRYPTOGRAPHY
                         │
           ┌─────────────┴─────────────┐
           │                           │
     Symmetric Key              Asymmetric Key
     (Secret Key)               (Public Key)
           │                           │
     Same key for                Different keys
     encrypt/decrypt            (public + private)
           │                           │
     DES, 3DES, AES              RSA, ECC, DSA
```

---

## 9.3 Symmetric Key Cryptography

### **The Concept**
$$E_K(P) = C$$
$$D_K(C) = P$$

Same key $K$ for encryption and decryption.

### **Advantages & Disadvantages**

| Pros | Cons |
|------|------|
| Fast (100x faster than asymmetric) | Key distribution problem |
| Efficient for bulk data | Key for each pair: $\frac{n(n-1)}{2}$ |
| Simple implementation | No non-repudiation |

### **Common Symmetric Algorithms**

| Algorithm | Key Size | Block Size | Status |
|-----------|----------|------------|--------|
| **DES** | 56 bits | 64 bits | Broken (insecure) |
| **3DES** | 112/168 bits | 64 bits | Legacy |
| **AES** | 128/192/256 bits | 128 bits | Current standard |
| **RC4** | Variable | Stream | Deprecated |
| **ChaCha20** | 256 bits | Stream | Modern |

### **DES (Data Encryption Standard)**

- 16 rounds of Feistel cipher
- 64-bit block size
- 56-bit effective key (8 parity bits)
- **Broken:** 2^56 keys can be brute-forced

### **AES (Advanced Encryption Standard)**

- Substitution-Permutation Network
- 128-bit block size
- Key sizes: 128 (10 rounds), 192 (12), 256 (14)
- **Current standard** for symmetric encryption

### **Block Cipher Modes**

| Mode | Description | IV? | Parallel? | Use |
|------|-------------|-----|-----------|-----|
| **ECB** | Each block independent | No | Yes | Not recommended |
| **CBC** | Chain blocks with XOR | Yes | No | General purpose |
| **CTR** | Counter as nonce | Yes | Yes | High performance |
| **GCM** | CTR + Authentication | Yes | Yes | Authenticated encryption |

### **GATE Trap Alert ⚠️**

**ECB Mode Weakness:**
- Same plaintext block → Same ciphertext block
- Pattern leakage (visible in images)

**Always use CBC, CTR, or GCM in practice!**

---

## 9.4 Asymmetric Key Cryptography

### **The Concept**

$$E_{K_{public}}(P) = C \quad \text{(Encrypt with public key)}$$
$$D_{K_{private}}(C) = P \quad \text{(Decrypt with private key)}$$

Different keys for encryption (public) and decryption (private).

### **Key Properties**

| Key | Who has it | Used for |
|-----|------------|----------|
| **Public Key** | Everyone | Encrypt, Verify signature |
| **Private Key** | Owner only | Decrypt, Create signature |

### **RSA Algorithm**

**Key Generation:**
1. Choose two large primes: $p$, $q$
2. Compute $n = p \times q$
3. Compute $\phi(n) = (p-1)(q-1)$
4. Choose $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$
5. Compute $d$ such that $e \times d \equiv 1 \pmod{\phi(n)}$

**Keys:**
- Public key: $(e, n)$
- Private key: $(d, n)$

**Encryption:** $C = M^e \mod n$

**Decryption:** $M = C^d \mod n$

### **RSA Example**

**Given:** $p = 7$, $q = 11$
- $n = 7 \times 11 = 77$
- $\phi(n) = 6 \times 10 = 60$
- Choose $e = 7$ ($\gcd(7, 60) = 1$)
- Find $d$: $7d \equiv 1 \pmod{60}$ → $d = 43$

**Encrypt** $M = 5$:
$C = 5^7 \mod 77 = 78125 \mod 77 = 47$

**Decrypt** $C = 47$:
$M = 47^{43} \mod 77 = 5$ ✓

### **Advantages & Disadvantages**

| Pros | Cons |
|------|------|
| Solves key distribution | Very slow |
| Digital signatures | Computationally intensive |
| Non-repudiation | Key size must be large (2048+ bits) |

### **Common Asymmetric Algorithms**

| Algorithm | Use |
|-----------|-----|
| **RSA** | Encryption, signatures |
| **Diffie-Hellman** | Key exchange only |
| **DSA** | Digital signatures only |
| **ECC** | Modern alternative (smaller keys) |

---

## 9.5 Diffie-Hellman Key Exchange

### **Purpose**
Securely exchange a shared secret over insecure channel.

### **Process**

```
                    Public: p (prime), g (generator)

Alice                                              Bob
  │                                                  │
  │  Choose secret a                Choose secret b  │
  │                                                  │
  │  Compute A = g^a mod p          Compute B = g^b mod p
  │                                                  │
  │ ─────────── Send A ─────────────────────────────>│
  │                                                  │
  │ <────────── Send B ──────────────────────────────│
  │                                                  │
  │  Compute: K = B^a mod p         Compute: K = A^b mod p
  │                                                  │
  │  K = g^(ab) mod p               K = g^(ab) mod p │
  │                                                  │
        Both have same secret K!
```

### **Security**
- Based on Discrete Logarithm Problem
- Vulnerable to Man-in-the-Middle (needs authentication)

---

## 9.6 Hash Functions

### **Purpose**
Create fixed-size fingerprint of any data.

### **Properties**

| Property | Description |
|----------|-------------|
| **Deterministic** | Same input → Same hash |
| **Fixed output** | Any input → Fixed size output |
| **One-way** | Cannot derive input from hash |
| **Collision resistant** | Hard to find two inputs with same hash |
| **Avalanche effect** | Small input change → Big output change |

### **Common Hash Functions**

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| **MD5** | 128 bits | Broken (collisions found) |
| **SHA-1** | 160 bits | Deprecated (collisions found) |
| **SHA-256** | 256 bits | Secure (SHA-2 family) |
| **SHA-3** | Variable | Secure (Keccak) |

### **Uses of Hashing**

1. **Password storage:** Store hash, not password
2. **Message integrity:** Verify data not altered
3. **Digital signatures:** Sign hash, not full document
4. **Blockchain:** Chain of hashes

---

## 9.7 Digital Signatures

### **Purpose**
Prove authenticity and integrity; provide non-repudiation.

### **Process**

```
        SIGNING                          VERIFYING
        
  ┌─────────┐                        ┌─────────┐
  │ Message │                        │ Message │
  └────┬────┘                        └────┬────┘
       │                                  │
       ▼                                  ▼
  ┌─────────┐                        ┌─────────┐
  │  Hash   │                        │  Hash   │
  └────┬────┘                        └────┬────┘
       │                                  │
       ▼                                  │
  ┌─────────────┐                         │
  │ Encrypt with│                    ┌────▼────┐
  │Private Key  │                    │ Compare │───> Valid/Invalid
  └──────┬──────┘                    └────▲────┘
         │                                │
         ▼                           ┌────┴─────────┐
    Signature ────────────────────>  │ Decrypt with │
                                     │ Public Key   │
                                     └──────────────┘
```

### **Signature = Encrypt(Hash(Message), PrivateKey)**

### **Why hash first?**
- Faster (hash is small)
- Works for any size message
- RSA has block size limit

---

## 9.8 Certificates and PKI

### **The Problem**
How to trust a public key belongs to claimed owner?

### **Solution: Digital Certificates**

A certificate is signed by a trusted **Certificate Authority (CA)**:

```
┌─────────────────────────────────────────────────────┐
│                   CERTIFICATE                        │
├─────────────────────────────────────────────────────┤
│  Subject: www.example.com                           │
│  Subject's Public Key: RSA 2048 bits...            │
│  Issuer: DigiCert CA                               │
│  Validity: 2024-01-01 to 2025-01-01                │
│  Serial Number: 12345...                           │
│                                                     │
│  CA's Digital Signature: xxxxxxxxx...              │
└─────────────────────────────────────────────────────┘
```

### **PKI (Public Key Infrastructure)**

```
                    Root CA
                       │
           ┌───────────┼───────────┐
           │           │           │
    Intermediate   Intermediate   Intermediate
         CA           CA           CA
           │           │           │
        End User    End User    End User
        Certs       Certs       Certs
```

### **Certificate Validation**
1. Check signature using CA's public key
2. Verify certificate not expired
3. Check not revoked (CRL or OCSP)
4. Verify chain to trusted root CA

---

## 9.9 TLS/SSL

### **TLS (Transport Layer Security)**

| Feature | Value |
|---------|-------|
| Current Version | TLS 1.3 |
| Purpose | Secure channel for applications |
| Uses | HTTPS, SMTPS, IMAPS, etc. |

### **TLS Handshake (TLS 1.2)**

```
Client                                          Server
   │                                               │
   │── ClientHello (versions, ciphers, random) ───>│
   │                                               │
   │<── ServerHello, Certificate, [KeyExchange] ──│
   │<── ServerHelloDone ──────────────────────────│
   │                                               │
   │── ClientKeyExchange ─────────────────────────>│
   │── ChangeCipherSpec ──────────────────────────>│
   │── Finished (encrypted) ──────────────────────>│
   │                                               │
   │<── ChangeCipherSpec, Finished (encrypted) ───│
   │                                               │
   │══════════ Encrypted Application Data ════════│
```

### **TLS 1.3 Improvements**
- 1-RTT handshake (was 2-RTT)
- 0-RTT resumption
- Removed weak ciphers
- Forward secrecy mandatory

### **Cipher Suite Example**
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS       = Protocol
ECDHE     = Key Exchange (Elliptic Curve DH)
RSA       = Authentication
AES_256   = Bulk Encryption (256-bit AES)
GCM       = Mode (Galois/Counter Mode)
SHA384    = Hash function
```

---

## 9.10 IPSec

### **Purpose**
Secure IP-level communication (VPNs).

### **IPSec Modes**

| Mode | Use | IP Header |
|------|-----|-----------|
| **Transport** | Host-to-host | Original preserved |
| **Tunnel** | Gateway-to-gateway (VPN) | New header added |

### **IPSec Protocols**

| Protocol | Purpose | Protection |
|----------|---------|------------|
| **AH** (Authentication Header) | Integrity, authentication | No encryption |
| **ESP** (Encapsulating Security Payload) | Confidentiality + integrity | Encryption included |
| **IKE** (Internet Key Exchange) | Key negotiation | Uses UDP 500/4500 |

### **IPSec Security Association (SA)**
- One-way relationship between sender and receiver
- Defined by: SPI, IP destination, protocol (AH/ESP)

---

## 9.11 Firewalls

### **Types of Firewalls**

| Type | Layer | Examines | Speed | Security |
|------|-------|----------|-------|----------|
| **Packet Filter** | 3-4 | IP, ports, flags | Fast | Basic |
| **Stateful Inspection** | 3-4 | Connection state | Medium | Good |
| **Application Gateway** | 7 | Full content | Slow | High |
| **Next-Gen (NGFW)** | 3-7 | All + threats | Medium | Highest |

### **Packet Filtering Rules**

```
Action   Protocol   Source IP       Dest IP         Src Port   Dst Port
─────────────────────────────────────────────────────────────────────────
ALLOW    TCP        192.168.1.0/24  ANY             ANY        80,443
ALLOW    TCP        ANY             192.168.1.10    ANY        22
DENY     ICMP       ANY             ANY             ANY        ANY
DENY     ALL        ANY             ANY             ANY        ANY
```

### **DMZ (Demilitarized Zone)**

```
        Internet
            │
      ┌─────┴─────┐
      │ Firewall  │
      └─────┬─────┘
            │
    ┌───────┼───────┐
    │       │       │
 ┌──┴──┐ ┌──┴──┐ ┌──┴──┐
 │ Web │ │Email│ │ DNS │   ← DMZ (Public servers)
 └─────┘ └─────┘ └─────┘
            │
      ┌─────┴─────┐
      │ Firewall  │
      └─────┬─────┘
            │
      Internal Network         ← Private
```

---

## 9.12 Network Attacks

### **Common Attack Types**

| Attack | Target | Description |
|--------|--------|-------------|
| **DoS/DDoS** | Availability | Overwhelm with traffic |
| **Man-in-the-Middle** | Confidentiality, Integrity | Intercept communication |
| **ARP Spoofing** | LAN | Fake ARP responses |
| **DNS Spoofing** | Name resolution | Fake DNS responses |
| **IP Spoofing** | Authentication | Forge source IP |
| **Phishing** | Users | Fake websites/emails |
| **SQL Injection** | Databases | Malicious SQL commands |
| **XSS** | Web apps | Inject scripts |

### **DDoS Attack Types**

| Type | Layer | Example |
|------|-------|---------|
| **Volumetric** | 3-4 | UDP flood, ICMP flood |
| **Protocol** | 3-4 | SYN flood, Ping of Death |
| **Application** | 7 | HTTP flood, Slowloris |

---

## 9.13 Formulas Summary

### **RSA**

| Calculation | Formula |
|-------------|---------|
| $n$ | $p \times q$ |
| $\phi(n)$ | $(p-1)(q-1)$ |
| Public key | $(e, n)$ where $\gcd(e, \phi(n)) = 1$ |
| Private key | $(d, n)$ where $ed \equiv 1 \pmod{\phi(n)}$ |
| Encrypt | $C = M^e \mod n$ |
| Decrypt | $M = C^d \mod n$ |

### **Key Distribution**

| System | Keys Needed |
|--------|-------------|
| Symmetric | $\frac{n(n-1)}{2}$ |
| Asymmetric | $2n$ |

---

## 9.14 Solved Examples

### **Example 1: RSA Key Generation**

**Problem:** Given $p = 5$, $q = 7$, $e = 5$. Find $d$.

**Solution:**
- $n = 5 \times 7 = 35$
- $\phi(n) = 4 \times 6 = 24$
- Find $d$: $5d \equiv 1 \pmod{24}$
- $5 \times 5 = 25 \equiv 1 \pmod{24}$
- **$d = 5$**

---

### **Example 2: Keys Required**

**Problem:** A network has 100 users. How many keys are needed for:
(a) Symmetric encryption
(b) Asymmetric encryption

**Solution:**
(a) Symmetric: $\frac{100 \times 99}{2} = 4950$ keys
(b) Asymmetric: $2 \times 100 = 200$ keys (public + private each)

---

### **Example 3: Digital Signature**

**Problem:** How does Alice send a signed message to Bob?

**Solution:**
1. Alice computes hash of message: $H = Hash(M)$
2. Alice encrypts hash with her private key: $S = E_{Alice_{priv}}(H)$
3. Alice sends $(M, S)$ to Bob
4. Bob decrypts signature: $H' = D_{Alice_{pub}}(S)$
5. Bob computes hash of received message: $H'' = Hash(M)$
6. If $H' = H''$, signature is valid

---

## 9.15 Practice Problems

**Q1.** RSA uses which mathematical problem for security?
- (a) Discrete logarithm
- (b) Integer factorization
- (c) Elliptic curve
- (d) Hash collision

<details>
<summary>Answer</summary>
**(b) Integer factorization** — RSA security relies on difficulty of factoring $n = p \times q$
</details>

---

**Q2.** [NAT] If $p = 3$, $q = 11$, calculate $\phi(n)$.

<details>
<summary>Answer</summary>
$\phi(n) = (p-1)(q-1) = 2 \times 10 = \boxed{20}$
</details>

---

**Q3.** Which provides confidentiality in IPSec?
- (a) AH
- (b) ESP
- (c) IKE
- (d) TLS

<details>
<summary>Answer</summary>
**(b) ESP** — Encapsulating Security Payload provides encryption
</details>

---

**Q4.** TLS operates at which layer?
- (a) Network
- (b) Transport
- (c) Session/Transport
- (d) Application

<details>
<summary>Answer</summary>
**(c) Session/Transport** — TLS sits between transport and application
</details>

---

## 9.16 The 5-Second Snap-Check ✅

1. ☐ Symmetric: Same key, fast (AES = current standard)
2. ☐ Asymmetric: Key pair, slow (RSA: $n = pq$, $\phi = (p-1)(q-1)$)
3. ☐ Digital signature = Encrypt(Hash, PrivateKey)
4. ☐ TLS handshake: ClientHello → ServerHello → Key Exchange → Encrypted
5. ☐ IPSec: AH (integrity), ESP (confidentiality)
6. ☐ Firewall types: Packet filter < Stateful < Application gateway

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 10: Formula Sheet & Quick Revision →](./10-Formula-Sheet.md)
