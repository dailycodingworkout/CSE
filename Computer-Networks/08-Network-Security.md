# Chapter 8: Network Security
## The Defense Arsenal | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Security = Confidentiality + Integrity + Authentication + Non-repudiation."**

---

## 8.1 Security Goals (CIA Triad + More)

| Goal | Description | Threat |
|------|-------------|--------|
| **Confidentiality** | Only authorized access | Eavesdropping |
| **Integrity** | Data not modified | Tampering |
| **Availability** | Service accessible | DoS attacks |
| **Authentication** | Verify identity | Impersonation |
| **Non-repudiation** | Cannot deny actions | Denial |

---

## 8.2 Cryptography Basics

### Types of Cryptography

```
Cryptography
├── Symmetric Key (Secret Key)
│   ├── Block Ciphers (DES, AES)
│   └── Stream Ciphers (RC4)
└── Asymmetric Key (Public Key)
    ├── RSA
    ├── Diffie-Hellman
    └── ECC
```

### Symmetric Key Cryptography

Same key for encryption and decryption.

```
Plaintext → [Encrypt with Key K] → Ciphertext → [Decrypt with Key K] → Plaintext
```

| Algorithm | Key Size | Block Size | Status |
|-----------|----------|------------|--------|
| DES | 56 bits | 64 bits | Broken |
| 3DES | 168 bits | 64 bits | Legacy |
| AES | 128/192/256 bits | 128 bits | Standard |
| Blowfish | 32-448 bits | 64 bits | Secure |

**Advantages:**
- Fast
- Efficient for large data

**Disadvantages:**
- Key distribution problem
- n users need n(n-1)/2 keys

### Asymmetric Key Cryptography

Different keys for encryption and decryption.

```
Public Key (Kpub): Everyone knows
Private Key (Kpriv): Only owner knows

Encryption: Ciphertext = E(Kpub, Plaintext)
Decryption: Plaintext = D(Kpriv, Ciphertext)
```

**For Confidentiality:**
- Encrypt with receiver's public key
- Only receiver can decrypt with private key

**For Authentication (Digital Signature):**
- Sign with sender's private key
- Anyone can verify with sender's public key

### RSA Algorithm

1. Choose two large primes p, q
2. Compute n = p × q
3. Compute φ(n) = (p-1)(q-1)
4. Choose e such that gcd(e, φ(n)) = 1
5. Compute d such that e × d ≡ 1 (mod φ(n))

**Public Key:** (n, e)
**Private Key:** (n, d)

**Encryption:** $C = M^e \mod n$
**Decryption:** $M = C^d \mod n$

### 🎯 RSA Example

```
p = 3, q = 11
n = 33
φ(n) = 2 × 10 = 20
e = 7 (gcd(7, 20) = 1)
d = 3 (7 × 3 = 21 ≡ 1 mod 20)

Public: (33, 7)
Private: (33, 3)

Encrypt M = 2:
C = 2^7 mod 33 = 128 mod 33 = 29

Decrypt C = 29:
M = 29^3 mod 33 = 24389 mod 33 = 2 ✓
```

### Diffie-Hellman Key Exchange

Securely exchange keys over insecure channel.

```
Public: Prime p, Generator g

Alice:                          Bob:
Choose secret a                 Choose secret b
Compute A = g^a mod p          Compute B = g^b mod p
    │                               │
    └──────── A ──────────────────→│
    │←─────── B ───────────────────┘
    │                               │
Compute K = B^a mod p          Compute K = A^b mod p
         = g^(ab) mod p               = g^(ab) mod p

Both have same K!
```

---

## 8.3 Hash Functions

### Properties

| Property | Description |
|----------|-------------|
| One-way | Can't reverse hash to input |
| Collision-resistant | Hard to find two inputs with same hash |
| Deterministic | Same input → same output |
| Fixed output | Any input → fixed size output |
| Avalanche effect | Small change → completely different hash |

### Common Hash Functions

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| MD5 | 128 bits | Broken (collisions found) |
| SHA-1 | 160 bits | Deprecated |
| SHA-256 | 256 bits | Secure |
| SHA-3 | 224-512 bits | Latest standard |

### Message Authentication Code (MAC)

Hash with key for integrity + authentication.

$$\text{MAC} = H(K || M)$$

**HMAC (Hash-based MAC):**
$$\text{HMAC}(K, M) = H((K \oplus opad) || H((K \oplus ipad) || M))$$

---

## 8.4 Digital Signatures

### Purpose
- Authentication (who sent it)
- Integrity (not modified)
- Non-repudiation (sender can't deny)

### Process

```
Sender:
1. Hash message: H = Hash(M)
2. Sign hash: Signature = Encrypt(H, Sender's Private Key)
3. Send: M + Signature

Receiver:
1. Hash received message: H1 = Hash(M)
2. Decrypt signature: H2 = Decrypt(Signature, Sender's Public Key)
3. Verify: If H1 == H2, signature valid
```

### Digital Signature Algorithms

| Algorithm | Based On |
|-----------|----------|
| RSA Signature | RSA |
| DSA | Discrete logarithm |
| ECDSA | Elliptic curves |

---

## 8.5 Digital Certificates & PKI

### X.509 Certificate

```
┌─────────────────────────────────────────┐
│ Version                                 │
│ Serial Number                           │
│ Signature Algorithm                     │
│ Issuer (CA)                            │
│ Validity Period                         │
│ Subject (Owner)                         │
│ Subject's Public Key                    │
│ Extensions                              │
│ CA's Digital Signature                  │
└─────────────────────────────────────────┘
```

### Certificate Authority (CA) Hierarchy

```
Root CA (Self-signed)
    │
    ├── Intermediate CA
    │       │
    │       └── End Entity Certificate
    │
    └── Intermediate CA
            │
            └── End Entity Certificate
```

### Certificate Verification

1. Check signature using CA's public key
2. Check validity period
3. Check revocation status (CRL or OCSP)
4. Verify certificate chain to trusted root

---

## 8.6 Security Protocols

### SSL/TLS (Secure Sockets Layer / Transport Layer Security)

**Location:** Between Application and Transport layer

**TLS Handshake:**
```
Client                              Server
   │                                   │
   │──ClientHello (cipher suites)────→│
   │                                   │
   │←──ServerHello (chosen cipher)────│
   │←──Certificate────────────────────│
   │←──ServerHelloDone────────────────│
   │                                   │
   │──ClientKeyExchange (pre-master)─→│
   │──ChangeCipherSpec────────────────→│
   │──Finished (encrypted)────────────→│
   │                                   │
   │←──ChangeCipherSpec───────────────│
   │←──Finished (encrypted)───────────│
   │                                   │
   │←─────Encrypted Data Exchange────→│
```

### IPSec (IP Security)

**Location:** Network layer

**Modes:**
- **Transport Mode:** Encrypt payload only
- **Tunnel Mode:** Encrypt entire IP packet

**Protocols:**
| Protocol | Purpose |
|----------|---------|
| AH (Authentication Header) | Integrity, authentication |
| ESP (Encapsulating Security Payload) | Confidentiality, integrity |
| IKE (Internet Key Exchange) | Key management |

### SSH (Secure Shell)

**Location:** Application layer

**Features:**
- Encrypted remote login
- Port forwarding
- File transfer (SCP, SFTP)

---

## 8.7 Firewalls

### Types

| Type | Layer | Description |
|------|-------|-------------|
| Packet Filter | Network (3) | Filter by IP, port |
| Stateful | Transport (4) | Track connections |
| Application Gateway | Application (7) | Deep packet inspection |
| Proxy | Application (7) | Intermediary |

### Packet Filter Rules

```
Rule  | Action | Source IP      | Dest IP        | Protocol | Src Port | Dst Port
------|--------|----------------|----------------|----------|----------|----------
1     | Allow  | 192.168.1.0/24 | Any            | TCP      | Any      | 80
2     | Allow  | Any            | 192.168.1.10   | TCP      | Any      | 22
3     | Deny   | Any            | Any            | Any      | Any      | Any
```

### DMZ (Demilitarized Zone)

```
Internet ←→ [Firewall] ←→ DMZ ←→ [Firewall] ←→ Internal Network
                         │
                    Web Server
                    Mail Server
```

---

## 8.8 Network Attacks

### Attack Types

| Attack | Target | Description |
|--------|--------|-------------|
| **Eavesdropping** | Confidentiality | Intercept communication |
| **Man-in-the-Middle** | All | Intercept and modify |
| **Replay** | Authentication | Capture and resend |
| **DoS/DDoS** | Availability | Overwhelm with requests |
| **IP Spoofing** | Authentication | Fake source IP |
| **ARP Spoofing** | Network | Fake MAC address |
| **DNS Spoofing** | Application | Fake DNS response |
| **Phishing** | User | Social engineering |
| **SQL Injection** | Application | Malicious database queries |
| **XSS** | Application | Inject malicious scripts |

### Denial of Service (DoS)

| Type | Method |
|------|--------|
| SYN Flood | Send many SYN, don't complete handshake |
| Ping of Death | Oversized ICMP packet |
| Smurf | Ping broadcast with victim's IP |
| UDP Flood | Send many UDP packets |
| HTTP Flood | Many HTTP requests |

### Prevention Techniques

| Attack | Prevention |
|--------|------------|
| Eavesdropping | Encryption |
| MITM | Certificate verification, TLS |
| Replay | Timestamps, nonces |
| DoS | Rate limiting, filtering |
| IP Spoofing | Ingress filtering |
| ARP Spoofing | Static ARP, VLAN |
| SQL Injection | Parameterized queries |
| XSS | Input sanitization, CSP |

---

## 8.9 VPN (Virtual Private Network)

### Purpose
Secure communication over public network.

### VPN Types

| Type | Description |
|------|-------------|
| Remote Access | User connects to network |
| Site-to-Site | Connect two networks |

### VPN Protocols

| Protocol | Layer | Features |
|----------|-------|----------|
| PPTP | Data Link | Old, weak security |
| L2TP/IPSec | Data Link + Network | Strong security |
| OpenVPN | Application | Flexible, uses SSL |
| WireGuard | Network | Modern, fast |

---

## 8.10 Intrusion Detection Systems (IDS)

### Types

| Type | Method |
|------|--------|
| Signature-based | Match known attack patterns |
| Anomaly-based | Detect deviation from normal |
| Host-based (HIDS) | Monitor single host |
| Network-based (NIDS) | Monitor network traffic |

### IDS vs IPS

| IDS | IPS |
|-----|-----|
| Detects and alerts | Detects and prevents |
| Passive | Active |
| Out-of-band | Inline |

---

## 🎯 Practice Problems

### Problem 1: RSA
**Q:** In RSA, n=33, e=7. Encrypt M=5.
**Solution:** $C = 5^7 \mod 33 = 78125 \mod 33 = 14$

### Problem 2: Diffie-Hellman
**Q:** p=23, g=5, a=6, b=15. Find shared key.
**Solution:**
- A = 5^6 mod 23 = 8
- B = 5^15 mod 23 = 19
- K = 19^6 mod 23 = 8^15 mod 23 = 2

### Problem 3: Digital Signature
**Q:** What ensures non-repudiation in digital signatures?
**Answer:** Sender signs with private key, which only they possess.

### Problem 4: Firewall
**Q:** Which firewall can inspect HTTP content?
**Answer:** Application Gateway / Application Layer Firewall

### Problem 5: TLS
**Q:** What does TLS provide?
**Answer:** Confidentiality (encryption), Integrity (MAC), Authentication (certificates)

### Problem 6: Hash
**Q:** Which property ensures you can't find two inputs with same hash?
**Answer:** Collision resistance

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"CIA Needs Authentication"**
- **C**onfidentiality
- **I**ntegrity
- **A**vailability
- **A**uthentication

**"RSA: Ron Shamir Adleman - Public Key Pioneers"**

### The Mental Slider
- **Symmetric:** Same key, like a regular lock
- **Asymmetric:** Different keys, like a mailbox (anyone deposits, only owner retrieves)
- **Hash:** Fingerprint (unique, can't reverse)
- **Signature:** Seal with private stamp

### The 5-Second Snap-Check
1. **Symmetric vs Asymmetric?** Same key vs different keys
2. **RSA for?** Encryption + Digital signatures
3. **DH for?** Key exchange only
4. **TLS layer?** Between Application and Transport
5. **IPSec layer?** Network layer

---

## 📈 Key Comparison Table

| Aspect | Symmetric | Asymmetric |
|--------|-----------|------------|
| Keys | One shared key | Public + Private pair |
| Speed | Fast | Slow |
| Key distribution | Difficult | Easy (public key) |
| Use case | Bulk encryption | Key exchange, signatures |
| Example | AES, DES | RSA, ECC |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Application Layer](07-Application-Layer.md) | [Next: Practice Problems →](09-Practice-Problems.md)
