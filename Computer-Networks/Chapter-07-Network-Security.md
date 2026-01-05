# Chapter 7: Network Security

## 🎯 The Atomic Truth
> **"Protecting data confidentiality, integrity, and availability across networks using cryptography and protocols."**

---

## 7.1 Security Fundamentals

### CIA Triad

| Principle | Description | Threat |
|-----------|-------------|--------|
| **Confidentiality** | Data accessible only to authorized | Eavesdropping |
| **Integrity** | Data not modified in transit | Tampering |
| **Availability** | Services accessible when needed | DoS attack |

### Additional Security Goals

| Goal | Description |
|------|-------------|
| **Authentication** | Verify identity of communicating parties |
| **Non-repudiation** | Sender cannot deny sending message |
| **Access Control** | Limit who can access what |

### The "Aha!" Moment 💡
Network security is like a **"secure courier service"**:
- **Encryption** = Sealed envelope (confidentiality)
- **Digital Signature** = Wax seal (integrity + authentication)
- **Certificate** = Courier's ID badge (trust)
- **Firewall** = Security checkpoint (access control)

---

## 7.2 Cryptography Basics ⭐⭐

### 7.2.1 Encryption Types

```
Symmetric (Secret Key)           Asymmetric (Public Key)
┌────────────────────┐           ┌────────────────────┐
│  Same key for      │           │  Different keys:   │
│  encrypt & decrypt │           │  Public + Private  │
│                    │           │                    │
│  ┌────┐   ┌────┐   │           │  ┌────┐   ┌────┐   │
│  │ K  │───│ K  │   │           │  │Pub │───│Priv│   │
│  └────┘   └────┘   │           │  └────┘   └────┘   │
│  Sender   Receiver │           │  Anyone   Owner    │
└────────────────────┘           └────────────────────┘
```

### 7.2.2 Symmetric Key Cryptography ⭐

| Aspect | Details |
|--------|---------|
| Key | Same key for encryption and decryption |
| Speed | Fast |
| Key Distribution | Problem (need secure channel) |
| Key Count | $\frac{n(n-1)}{2}$ for n users |

**Algorithms**:

| Algorithm | Key Size | Block Size | Notes |
|-----------|----------|------------|-------|
| **DES** | 56 bits | 64 bits | Obsolete, insecure |
| **3DES** | 112/168 bits | 64 bits | DES applied 3 times |
| **AES** | 128/192/256 bits | 128 bits | Current standard |
| **Blowfish** | 32-448 bits | 64 bits | Fast, free |
| **RC4** | 40-2048 bits | Stream | Deprecated |

**AES (Advanced Encryption Standard)** ⭐:
- Block cipher, 128-bit blocks
- Rounds: 10 (128-bit key), 12 (192-bit), 14 (256-bit)
- Operations: SubBytes, ShiftRows, MixColumns, AddRoundKey

### 7.2.3 Block Cipher Modes ⭐

| Mode | Name | Properties |
|------|------|------------|
| **ECB** | Electronic Codebook | Parallel, patterns visible |
| **CBC** | Cipher Block Chaining | IV needed, serial encrypt |
| **CFB** | Cipher Feedback | Stream-like from block cipher |
| **OFB** | Output Feedback | Pre-compute keystream |
| **CTR** | Counter | Parallel, random access |
| **GCM** | Galois/Counter Mode | CTR + Authentication |

**CBC Mode** ⭐:
```
P1 ⊕ IV → Encrypt → C1
P2 ⊕ C1 → Encrypt → C2
P3 ⊕ C2 → Encrypt → C3
```

**GATE Trap**: ECB is insecure - identical plaintext blocks produce identical ciphertext blocks (patterns leak).

### 7.2.4 Asymmetric Key Cryptography ⭐⭐

| Aspect | Details |
|--------|---------|
| Keys | Public (shared) + Private (secret) |
| Speed | Slow (1000× slower than symmetric) |
| Key Distribution | Easy (public key can be shared) |
| Key Count | 2n keys for n users |

**Use Cases**:

| Operation | Keys Used |
|-----------|-----------|
| **Encryption** | Encrypt with receiver's public key |
| **Decryption** | Decrypt with receiver's private key |
| **Signing** | Sign with sender's private key |
| **Verification** | Verify with sender's public key |

**Algorithms**:

| Algorithm | Based On | Use |
|-----------|----------|-----|
| **RSA** | Factoring large primes | Encryption, Signatures |
| **DSA** | Discrete logarithm | Signatures only |
| **ECDSA** | Elliptic curves | Signatures (smaller keys) |
| **Diffie-Hellman** | Discrete logarithm | Key exchange only |

### 7.2.5 RSA Algorithm ⭐⭐

**Key Generation**:
1. Choose two large primes: $p$, $q$
2. Compute $n = p \times q$
3. Compute $\phi(n) = (p-1)(q-1)$
4. Choose $e$ such that $\gcd(e, \phi(n)) = 1$
5. Compute $d = e^{-1} \mod \phi(n)$

**Keys**:
- Public key: $(e, n)$
- Private key: $(d, n)$

**Operations**:
- Encryption: $C = M^e \mod n$
- Decryption: $M = C^d \mod n$

**Example (GATE Style)**:
> p = 3, q = 11, e = 7. Find d and encrypt M = 5.

**Solution**:
- $n = 3 \times 11 = 33$
- $\phi(n) = 2 \times 10 = 20$
- $d \times 7 \equiv 1 \mod 20$ → $d = 3$ (since $3 \times 7 = 21 \equiv 1 \mod 20$)
- $C = 5^7 \mod 33 = 78125 \mod 33 = 14$

**Decryption check**: $14^3 \mod 33 = 2744 \mod 33 = 5$ ✓

### 7.2.6 Diffie-Hellman Key Exchange ⭐⭐

```
                Alice                    Bob
                  │                        │
Public: p, g      │                        │
Private: a        │                        │  Private: b
                  │                        │
Compute: A = g^a mod p                     Compute: B = g^b mod p
                  │                        │
                  │──────── A ────────────►│
                  │                        │
                  │◄──────── B ────────────│
                  │                        │
Compute: s = B^a mod p                     Compute: s = A^b mod p
         = g^(ab) mod p                           = g^(ab) mod p
                  │                        │
                  │    Shared secret: s    │
```

**Security**: Based on Discrete Logarithm Problem.

**Vulnerability**: Man-in-the-Middle (need authentication).

**Example (GATE Style)**:
> p = 23, g = 5, a = 6, b = 15. Find shared key.

**Solution**:
- $A = 5^6 \mod 23 = 15625 \mod 23 = 8$
- $B = 5^{15} \mod 23 = ... = 19$ (use modular exponentiation)
- Alice: $s = 19^6 \mod 23 = 2$
- Bob: $s = 8^{15} \mod 23 = 2$ ✓

---

## 7.3 Hash Functions and MAC ⭐⭐

### 7.3.1 Cryptographic Hash Functions

**Properties**:
1. **One-way**: Cannot reverse to find input
2. **Collision-resistant**: Hard to find two inputs with same hash
3. **Deterministic**: Same input → same output
4. **Avalanche effect**: Small change → completely different hash

**Common Hash Functions**:

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| **MD5** | 128 bits | Broken (collisions) |
| **SHA-1** | 160 bits | Deprecated (collisions) |
| **SHA-256** | 256 bits | Secure (SHA-2 family) |
| **SHA-3** | 256/384/512 bits | Secure (Keccak) |

### 7.3.2 Message Authentication Code (MAC) ⭐

**Purpose**: Integrity + Authentication (but not non-repudiation)

**HMAC (Hash-based MAC)**:
$$\text{HMAC}(K, M) = H((K \oplus opad) || H((K \oplus ipad) || M))$$

| Component | Value |
|-----------|-------|
| K | Secret key |
| ipad | 0x36 repeated |
| opad | 0x5C repeated |
| H | Hash function |

**CMAC**: Cipher-based MAC (uses block cipher like AES)

### 7.3.3 Digital Signatures ⭐⭐

**Purpose**: Integrity + Authentication + Non-repudiation

```
Sender:
    Hash(Message) → Digest
    Encrypt(Digest, PrivateKey) → Signature
    Send: Message + Signature

Receiver:
    Hash(Message) → Digest1
    Decrypt(Signature, PublicKey) → Digest2
    Compare: Digest1 == Digest2 ?
```

**Key Difference from MAC**:
- MAC: Symmetric key (both parties share)
- Signature: Asymmetric (only sender has private key)

---

## 7.4 Key Distribution and PKI ⭐

### 7.4.1 Key Distribution Problem

**Symmetric**: Need secure channel to share key
**Asymmetric**: Need to verify public key belongs to correct party

### 7.4.2 Key Distribution Center (KDC)

**Kerberos Model**:
```
Client                 KDC                   Server
   │                    │                      │
   │──Request ticket───►│                      │
   │◄─Ticket (encrypted)│                      │
   │                    │                      │
   │─────────Ticket (encrypted for server)────►│
   │                    │                      │
   │◄────────────Session established──────────│
```

### 7.4.3 Public Key Infrastructure (PKI) ⭐

**Components**:

| Component | Role |
|-----------|------|
| **CA** (Certificate Authority) | Issues and signs certificates |
| **RA** (Registration Authority) | Verifies identity before CA |
| **Certificate** | Binds public key to identity |
| **CRL** (Certificate Revocation List) | List of revoked certificates |
| **OCSP** | Online certificate status check |

### 7.4.4 Digital Certificate (X.509)

```
┌────────────────────────────────────────────┐
│  Version: 3                                │
│  Serial Number: 12345                      │
│  Signature Algorithm: SHA256withRSA        │
│  Issuer: CN=Example CA                     │
│  Validity: 2024-01-01 to 2025-01-01        │
│  Subject: CN=www.example.com               │
│  Subject Public Key: RSA 2048-bit          │
│  Extensions: ...                           │
│  ──────────────────────────────────────────│
│  CA Signature: [bytes]                     │
└────────────────────────────────────────────┘
```

**Certificate Chain**:
```
Root CA (Self-signed, trusted)
    │
    └── Intermediate CA (signed by Root)
            │
            └── End-Entity Certificate (signed by Intermediate)
```

---

## 7.5 Security Protocols ⭐⭐

### 7.5.1 IPSec (IP Security) ⭐

**Operates at**: Network Layer (Layer 3)

**Modes**:

| Mode | Protection | Use Case |
|------|------------|----------|
| **Transport** | Payload only | Host-to-host |
| **Tunnel** | Entire packet (new header) | VPN gateways |

**Protocols**:

| Protocol | Provides |
|----------|----------|
| **AH** (Authentication Header) | Integrity, Authentication (no encryption) |
| **ESP** (Encapsulating Security Payload) | Encryption + Integrity + Authentication |

**IKE (Internet Key Exchange)**: Negotiates security associations.

### 7.5.2 TLS/SSL ⭐⭐

**Operates at**: Between Transport and Application (Session layer concept)

**TLS Handshake** (detailed):

```
Client                                     Server
   │                                         │
   │─── ClientHello ────────────────────────►│
   │    (version, random, ciphers)           │
   │                                         │
   │◄─── ServerHello ────────────────────────│
   │     (version, random, chosen cipher)    │
   │                                         │
   │◄─── Certificate ────────────────────────│
   │                                         │
   │◄─── ServerHelloDone ────────────────────│
   │                                         │
   │─── ClientKeyExchange ──────────────────►│
   │    (pre-master secret encrypted)        │
   │                                         │
   │─── ChangeCipherSpec ───────────────────►│
   │                                         │
   │─── Finished (encrypted) ───────────────►│
   │                                         │
   │◄─── ChangeCipherSpec ───────────────────│
   │                                         │
   │◄─── Finished (encrypted) ───────────────│
   │                                         │
   │         Application Data                │
```

**TLS Versions**:

| Version | Status |
|---------|--------|
| SSL 2.0 | Deprecated, insecure |
| SSL 3.0 | Deprecated (POODLE) |
| TLS 1.0 | Deprecated |
| TLS 1.1 | Deprecated |
| TLS 1.2 | Current (widely used) |
| TLS 1.3 | Latest (faster, more secure) |

### 7.5.3 SSH (Secure Shell)

**Layers**:
1. **Transport**: Encryption, integrity, compression
2. **User Authentication**: Password, public key
3. **Connection**: Channels (shell, forwarding)

---

## 7.6 Firewalls ⭐⭐

### 7.6.1 Firewall Types

| Type | Layer | Filtering Basis |
|------|-------|-----------------|
| **Packet Filter** | 3-4 | IP, Port, Protocol |
| **Stateful Inspection** | 3-4 | Packet + Connection state |
| **Application Gateway** (Proxy) | 7 | Application data |
| **Circuit-level Gateway** | 5 | Session establishment |

### 7.6.2 Packet Filtering Rules

```
┌────────┬─────────────┬──────────────┬───────┬───────┬────────┐
│ Action │  Source IP  │   Dest IP    │ Proto │ DPort │ SPort  │
├────────┼─────────────┼──────────────┼───────┼───────┼────────┤
│ ALLOW  │  Internal   │     Any      │  TCP  │  80   │  Any   │
│ ALLOW  │    Any      │  WebServer   │  TCP  │  443  │  Any   │
│ DENY   │    Any      │     Any      │  Any  │  Any  │  Any   │
└────────┴─────────────┴──────────────┴───────┴───────┴────────┘
```

**Default Policies**:
- **Default Deny**: Block all, allow specific
- **Default Allow**: Allow all, block specific (less secure)

### 7.6.3 DMZ (Demilitarized Zone)

```
┌──────────────────────────────────────────────────────┐
│                     Internet                         │
└─────────────────────────┬────────────────────────────┘
                          │
                    ┌─────▼─────┐
                    │ Firewall  │
                    └─────┬─────┘
                          │
                    ┌─────▼─────┐
                    │    DMZ    │  ← Web server, Email server
                    └─────┬─────┘
                          │
                    ┌─────▼─────┐
                    │ Firewall  │
                    └─────┬─────┘
                          │
                    ┌─────▼─────┐
                    │ Internal  │  ← Protected network
                    └───────────┘
```

### 7.6.4 NAT as Security

NAT hides internal IPs but is NOT a security feature.
- Obscurity ≠ Security
- Still need proper firewall

---

## 7.7 Network Attacks ⭐⭐

### 7.7.1 Attack Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Passive** | Eavesdrop, monitor | Sniffing, traffic analysis |
| **Active** | Modify, inject | Spoofing, DoS, MITM |

### 7.7.2 Common Attacks ⭐

| Attack | Layer | Description | Prevention |
|--------|-------|-------------|------------|
| **ARP Spoofing** | 2 | Fake ARP replies | Static ARP, DAI |
| **MAC Flooding** | 2 | Overflow switch table | Port security |
| **IP Spoofing** | 3 | Fake source IP | Ingress filtering |
| **ICMP Flood** | 3 | Ping flood | Rate limiting |
| **SYN Flood** | 4 | Half-open connections | SYN cookies |
| **DNS Spoofing** | 7 | Fake DNS responses | DNSSEC |
| **Man-in-the-Middle** | Any | Intercept communication | Encryption, certificates |
| **Phishing** | 7 | Fake websites | User education, 2FA |

### 7.7.3 DoS and DDoS

**DoS (Denial of Service)**: Single attacker overwhelms target.

**DDoS (Distributed DoS)**: Multiple sources (botnet) attack target.

**Types**:
| Type | Target | Example |
|------|--------|---------|
| **Volumetric** | Bandwidth | UDP flood |
| **Protocol** | Network stack | SYN flood |
| **Application** | Application | HTTP flood |

**SYN Flood** ⭐:
```
Attacker ──SYN──► Server
          (never sends ACK)
Server holds half-open connections
Eventually runs out of resources
```

**Defense**: SYN cookies (encode state in response, no memory until ACK)

### 7.7.4 Man-in-the-Middle (MITM)

```
Alice ◄───┐    ┌───► Bob
          │    │
          └─►Eve◄┘
       (intercepts all)
```

**Attacks via MITM**:
- Read encrypted traffic (if keys obtained)
- Modify messages
- Inject malicious content

**Prevention**:
- Certificate verification
- Public key pinning
- End-to-end encryption

---

## 7.8 VPN (Virtual Private Network) ⭐

### 7.8.1 VPN Types

| Type | Use Case |
|------|----------|
| **Site-to-Site** | Connect two networks |
| **Remote Access** | User to corporate network |
| **Client-to-Client** | P2P encrypted |

### 7.8.2 VPN Protocols

| Protocol | Layer | Details |
|----------|-------|---------|
| **IPSec** | 3 | Industry standard, complex |
| **L2TP/IPSec** | 2+3 | L2TP tunnel + IPSec encryption |
| **PPTP** | 2 | Obsolete, insecure |
| **SSL/TLS VPN** | 4-7 | Browser-based, easy |
| **OpenVPN** | 3 | Open source, SSL-based |
| **WireGuard** | 3 | Modern, fast, simple |

### 7.8.3 VPN Tunneling

```
Original Packet: [IP Header | TCP Header | Data]
                            │
                    Encrypt entire packet
                            │
Tunneled:        [New IP Header | VPN Header | Encrypted Original]
```

---

## 7.9 Wireless Security ⭐

### 7.9.1 WiFi Security Protocols

| Protocol | Encryption | Key | Status |
|----------|------------|-----|--------|
| **WEP** | RC4 | Static | Broken |
| **WPA** | TKIP (RC4) | Dynamic | Deprecated |
| **WPA2** | AES-CCMP | Dynamic | Current |
| **WPA3** | AES-GCMP, SAE | Dynamic | Latest |

### 7.9.2 WPA2 Authentication

**Personal (PSK)**: Pre-shared key (password)
**Enterprise (802.1X)**: RADIUS server authentication

### 7.9.3 WEP Weaknesses

- 24-bit IV (too short, reuse)
- Static key
- Weak integrity (CRC, not cryptographic)
- RC4 key scheduling attack

---

## 7.10 Email Security

### 7.10.1 Email Threats

| Threat | Description |
|--------|-------------|
| **Spam** | Unsolicited bulk email |
| **Phishing** | Fake emails for credentials |
| **Spoofing** | Fake sender address |
| **Malware** | Attachments with viruses |

### 7.10.2 Email Security Protocols

| Protocol | Purpose |
|----------|---------|
| **SPF** | Sender Policy Framework (authorized senders) |
| **DKIM** | DomainKeys Identified Mail (signature) |
| **DMARC** | Domain-based Message Authentication |
| **S/MIME** | Signed and encrypted email |
| **PGP** | Pretty Good Privacy (end-to-end) |

---

## 7.11 Edge Cases & GATE Traps

### Trap 1: Symmetric vs Asymmetric Speed
- Symmetric: ~1000× faster
- In practice: Use asymmetric to exchange symmetric key, then symmetric for data

### Trap 2: Digital Signature Direction
- Sign with PRIVATE key (sender)
- Verify with PUBLIC key (receiver)
- Opposite of encryption!

### Trap 3: Hash is Not Encryption
- Hash: One-way, fixed output, no key
- Encryption: Two-way, needs key

### Trap 4: AH vs ESP
- AH: No encryption (only authentication + integrity)
- ESP: Encryption + authentication + integrity

### Trap 5: SSL vs TLS
- SSL is deprecated (versions 2.0, 3.0)
- TLS is current (1.2, 1.3)
- People still say "SSL" but mean TLS

### Trap 6: Firewall Layer
- Packet filter: Layer 3-4 (IP, Port)
- Application gateway: Layer 7 (content)

---

## 📝 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| CIA | Confidentiality, Integrity, Availability |
| Symmetric | Same key, fast (AES) |
| Asymmetric | Public/Private, slow (RSA) |
| Hash | One-way, fixed size (SHA-256) |
| MAC | Integrity + Auth (HMAC) |
| Signature | Integrity + Auth + Non-repudiation |
| DH | Key exchange, vulnerable to MITM |
| TLS | Handshake, then encrypted |
| IPSec | AH (auth), ESP (encrypt) |
| Firewall | Packet filter, Stateful, Proxy |
| VPN | Tunnel encrypted traffic |

---

## 🧪 Practice Problems

### Problem 1 (GATE Style)
In RSA, p=5, q=7, e=5. Find d.

<details>
<summary>Solution</summary>

n = 5 × 7 = 35
φ(n) = 4 × 6 = 24
d × 5 ≡ 1 (mod 24)
d = 5 (since 5 × 5 = 25 ≡ 1 mod 24)

**Answer: d = 5**

</details>

### Problem 2 (GATE Style)
Which provides non-repudiation: MAC or Digital Signature?

<details>
<summary>Solution</summary>

**Digital Signature** provides non-repudiation.
MAC uses shared secret key, so either party could have created it.
Digital signature uses sender's private key (only sender has it).

</details>

### Problem 3 (GATE Style)
In Diffie-Hellman, p=11, g=2, a=3, b=5. Find the shared secret.

<details>
<summary>Solution</summary>

A = 2³ mod 11 = 8
B = 2⁵ mod 11 = 32 mod 11 = 10
Shared secret = 10³ mod 11 = 1000 mod 11 = 10
Or: 8⁵ mod 11 = 32768 mod 11 = 10

**Answer: 10**

</details>

### Problem 4 (GATE Style)
Which IPSec protocol provides confidentiality?

<details>
<summary>Solution</summary>

**ESP (Encapsulating Security Payload)**
AH only provides authentication and integrity, not encryption.

</details>

---

**Previous Chapter**: [← Chapter 6: Application Layer](./Chapter-06-Application-Layer.md)

**Next Chapter**: [Chapter 8: Formulas & PYQs →](./Chapter-08-Formulas-and-PYQs.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]*
