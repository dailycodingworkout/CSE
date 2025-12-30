# Chapter 11: Protection and Security

> **"Protection is like office access cards - controlling WHO can access WHAT within the system. Security is the guard at the building entrance - preventing unauthorized entry."**

---

## 🎯 Protection vs Security

| Aspect | Protection | Security |
|--------|------------|----------|
| **Scope** | Internal mechanisms | External threats |
| **Focus** | Control access to resources | Prevent attacks |
| **Who** | Authenticated users | Attackers, malware |
| **Mechanism** | Access control, domains | Authentication, encryption |

---

## 🔐 Goals of Protection

1. **Prevent unauthorized access** to resources
2. **Ensure confidentiality** of data
3. **Maintain integrity** of system
4. **Provide controlled sharing** of resources
5. **Detect and respond** to violations

---

## 👤 Principles of Protection

### Principle of Least Privilege

**Give each process/user minimum privileges needed to complete task**

```
Good: Editor program gets read/write to document only
Bad:  Editor program gets full system access
```

**Benefits:**
- Limits damage from bugs or attacks
- Easier auditing
- Simpler security analysis

---

### Need-to-Know Principle

**Access information only if needed for the task**

---

### Defense in Depth

**Multiple layers of protection**

```
┌─────────────────────────────────────────┐
│            Physical Security            │
│  ┌───────────────────────────────────┐  │
│  │         Network Security          │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │      OS Protection          │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │  Application Security │  │  │  │
│  │  │  │  ┌─────────────────┐  │  │  │  │
│  │  │  │  │      Data       │  │  │  │  │
│  │  │  │  └─────────────────┘  │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## 🏰 Protection Domains

### Definition

**Domain:** Set of (object, access rights) pairs

```
Domain D1: {(File1, {read}), (Printer, {print})}
Domain D2: {(File1, {read, write}), (File2, {execute})}
```

### Domain Implementation

| Implementation | Description |
|----------------|-------------|
| **User-based** | Each user is a domain |
| **Process-based** | Each process is a domain |
| **Procedure-based** | Each procedure is a domain |

---

### Domain Switching

```
User Mode Domain                  Kernel Mode Domain
┌────────────────────┐           ┌────────────────────┐
│ Limited privileges │──────────►│ Full privileges    │
│ (read own files)   │  syscall  │ (access all)       │
└────────────────────┘           └────────────────────┘
                      ◄──────────
                        return
```

**Examples:**
- System call (user → kernel)
- setuid program execution
- Privilege escalation

---

## 📊 Access Matrix

### Structure

```
              │  File1   │  File2   │ Printer  │ CPU     │
──────────────┼──────────┼──────────┼──────────┼─────────│
Domain 1      │ read     │          │ print    │ execute │
──────────────┼──────────┼──────────┼──────────┼─────────│
Domain 2      │ read     │ read     │          │         │
              │ write    │ write    │          │         │
──────────────┼──────────┼──────────┼──────────┼─────────│
Domain 3      │          │ read     │ print    │ execute │
──────────────┼──────────┼──────────┼──────────┼─────────│
```

**Row:** Domain (subject/process/user)
**Column:** Object (file/device/resource)
**Cell:** Access rights

---

### Domain Switching in Access Matrix

```
              │  File1   │  File2   │  D1      │  D2     │
──────────────┼──────────┼──────────┼──────────┼─────────│
D1            │ read     │          │          │ switch  │
──────────────┼──────────┼──────────┼──────────┼─────────│
D2            │          │ write    │ switch   │         │
──────────────┼──────────┼──────────┼──────────┼─────────│

D1 can switch to D2 (escalate privileges)
D2 can switch to D1 (drop privileges)
```

---

### Access Matrix Modifications

| Right | Meaning | Example |
|-------|---------|---------|
| **Copy** | Copy right to another domain | D1 can give read to D2 |
| **Owner** | Modify rights in column | Owner can grant/revoke |
| **Control** | Modify rights in row | Control over domain |
| **Transfer** | Move right to another | Remove from self, give to other |

---

## 🗂️ Access Matrix Implementation

### 1️⃣ Access Control List (ACL)

**Store by column (with each object):**

```
File1:
  - D1: read, write
  - D2: read
  - D3: execute

File2:
  - D2: read, write
  - D3: read
```

**UNIX Example:**
```
-rwxr-xr-- user group file1
 │├┘├┘├┘
 │ │ │ └── Others: read only
 │ │ └──── Group: read, execute
 │ └────── Owner: read, write, execute
 └──────── Regular file
```

**Pros:** Easy to see who can access object
**Cons:** Hard to see what user can access

---

### 2️⃣ Capability List

**Store by row (with each domain/process):**

```
Process P1 (Domain D1):
  - File1: read, write
  - Printer: print
  - CPU: execute

Process P2 (Domain D2):
  - File1: read
  - File2: read, write
```

**Capability:** Unforgeable token granting specific access

```
┌─────────────────────────────────────┐
│ Object ID │ Rights │ Signature      │
│   12345   │  rw-   │ [cryptographic]│
└─────────────────────────────────────┘
```

**Pros:** Easy to see what process can access
**Cons:** Hard to revoke (must find all copies)

---

### ACL vs Capability

| Aspect | ACL | Capability |
|--------|-----|------------|
| Stored with | Object | Subject |
| Question answered | Who can access X? | What can P access? |
| Revocation | Easy | Hard |
| Delegation | Hard | Easy |
| Used by | UNIX, Windows | Research systems |

---

## 🔒 Security Threats

### Types of Security Violations

| Threat | Description |
|--------|-------------|
| **Breach of Confidentiality** | Unauthorized reading |
| **Breach of Integrity** | Unauthorized modification |
| **Breach of Availability** | Denial of Service (DoS) |
| **Theft of Service** | Unauthorized use of resources |

---

### Attack Categories

| Category | Examples |
|----------|----------|
| **Masquerading** | Pretend to be another user |
| **Replay Attack** | Capture and retransmit data |
| **Man-in-the-Middle** | Intercept communication |
| **Session Hijacking** | Take over active session |
| **Privilege Escalation** | Gain higher access |

---

## 🔑 Authentication

### Something You...

| Factor | Example |
|--------|---------|
| **Know** | Password, PIN |
| **Have** | Smart card, token |
| **Are** | Fingerprint, iris |

**Two-Factor:** Combination of two types
**Multi-Factor:** More than two types

---

### Password Security

**Storage:**
```
Plain text:     NEVER!
Encrypted:      Better (but key exposure risk)
Hashed:         Good (one-way function)
Salted hash:    Best (prevents rainbow tables)
```

**Salt + Hash:**
```
Stored: (salt, hash(password + salt))

Verification:
1. Get salt from storage
2. Compute hash(input + salt)
3. Compare with stored hash
```

---

### Password Attacks

| Attack | Defense |
|--------|---------|
| Dictionary | Use complex passwords |
| Brute force | Limit attempts, lockout |
| Rainbow table | Use salt |
| Keylogger | Two-factor auth |
| Social engineering | User education |

---

## 🛡️ Security Mechanisms

### Encryption

**Symmetric:** Same key for encrypt/decrypt
- Fast, used for bulk data
- Key distribution problem
- Examples: AES, DES

**Asymmetric:** Public/private key pair
- Slow, used for key exchange
- Solves distribution problem
- Examples: RSA, ECC

```
Encryption:   Ciphertext = E(Key, Plaintext)
Decryption:   Plaintext = D(Key, Ciphertext)
```

---

### Digital Signatures

```
Signing:      Signature = Sign(PrivateKey, Hash(Message))
Verifying:    Valid = Verify(PublicKey, Signature, Hash(Message))
```

**Provides:**
- Authentication (who sent)
- Integrity (not modified)
- Non-repudiation (can't deny sending)

---

### Certificates

```
┌─────────────────────────────────────────────┐
│              X.509 Certificate              │
├─────────────────────────────────────────────┤
│ Subject: www.example.com                    │
│ Public Key: [RSA 2048-bit key]             │
│ Issuer: CA Authority                        │
│ Valid From: 2024-01-01                      │
│ Valid To: 2025-01-01                        │
│ Signature: [CA's signature]                 │
└─────────────────────────────────────────────┘
```

---

## 🦠 Malware Types

| Type | Behavior |
|------|----------|
| **Virus** | Attaches to program, needs host to spread |
| **Worm** | Self-replicating, spreads over network |
| **Trojan** | Disguised as legitimate software |
| **Spyware** | Collects user information |
| **Ransomware** | Encrypts data, demands payment |
| **Rootkit** | Hides presence, modifies OS |
| **Keylogger** | Records keystrokes |

---

### Virus Types

| Type | Description |
|------|-------------|
| **File infector** | Attaches to executable files |
| **Boot sector** | Infects boot sector |
| **Macro** | Written in document macros |
| **Polymorphic** | Changes form to avoid detection |
| **Metamorphic** | Rewrites itself completely |
| **Stealth** | Hides from detection |
| **Encrypted** | Encrypted payload, decrypts to run |

---

## 🔍 Security Techniques

### Intrusion Detection

**IDS (Intrusion Detection System):**
- Monitors network/system activity
- Detects suspicious patterns

**Types:**
- **Signature-based:** Matches known attack patterns
- **Anomaly-based:** Detects deviation from normal

---

### Firewall

```
                    ┌──────────────┐
Internet ──────────►│   Firewall   │──────────► Internal
                    │              │           Network
                    │  Rules:      │
                    │  - Allow 80  │
                    │  - Block 23  │
                    │  - Log all   │
                    └──────────────┘
```

**Types:**
- **Packet filter:** Check header (IP, port)
- **Stateful:** Track connections
- **Application:** Inspect content

---

### Sandboxing

**Run untrusted code in isolated environment**

```
┌─────────────────────────────────────────┐
│            Sandbox                      │
│  ┌───────────────────────────────────┐  │
│  │      Untrusted Application        │  │
│  │         (limited access)          │  │
│  └───────────────────────────────────┘  │
│                                         │
│  Restricted: No network, limited FS    │
└─────────────────────────────────────────┘
```

**Examples:** Browser sandbox, Java sandbox, Docker containers

---

## 📊 Buffer Overflow

### The Attack

```c
void vulnerable(char *input) {
    char buffer[100];
    strcpy(buffer, input);  // No bounds check!
}

Stack:
┌─────────────────┐
│ Return Address  │ ← Overwritten with attacker's address
├─────────────────┤
│ Saved EBP       │ ← Overwritten
├─────────────────┤
│ buffer[100]     │ ← Overflow here
├─────────────────┤
│                 │
└─────────────────┘

Attacker sends: [shellcode][padding][new_return_addr]
```

### Defenses

| Defense | How it works |
|---------|--------------|
| **Stack canary** | Random value before return address |
| **ASLR** | Randomize memory layout |
| **DEP/NX** | Mark stack non-executable |
| **Safe functions** | Use strncpy, not strcpy |
| **Bounds checking** | Compiler checks array bounds |

---

## 🔐 Access Control Models

### Discretionary Access Control (DAC)

- **Owner controls access**
- Can grant/revoke permissions
- Example: UNIX file permissions
- Risk: Trojan horse attacks

---

### Mandatory Access Control (MAC)

- **System controls access** (based on policy)
- Users cannot change rules
- Uses security labels

```
Security Levels:
Top Secret > Secret > Confidential > Unclassified

Bell-LaPadula Rules:
- No read up (Simple Security)
- No write down (Star Property)
```

---

### Role-Based Access Control (RBAC)

```
Users ───► Roles ───► Permissions

User1 ───► Admin ───► Full access
User2 ───► Editor ──► Read, Write
User3 ───► Viewer ──► Read only
```

**Benefits:**
- Easier to manage
- Reflects organizational structure
- Separation of duties

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **ACL vs Capability:** Differences
2. **Protection domain:** What can access what
3. **Password hashing:** Why salt
4. **Security properties:** CIA triad
5. **Attack types:** Identify attack

### ⚠️ Edge Cases:
1. **ACL stored with object** (not process)
2. **Capability revocation is hard**
3. **Salting prevents rainbow tables, not brute force**
4. **MAC is stricter than DAC**

---

## 🎯 Quick Revision Points

```
✓ Protection = internal, Security = external
✓ Least Privilege: Minimum necessary access
✓ Access Matrix = Domains × Objects → Rights
✓ ACL = per object, Capability = per subject
✓ Authentication: Know, Have, Are
✓ Hash + Salt = Password storage
✓ Virus needs host, Worm is self-sufficient
✓ DAC = owner controls, MAC = system controls
✓ RBAC = Role-based access
✓ Buffer overflow → Stack canary, ASLR, DEP
```

---

## 📚 Key Concepts

```
CIA Triad:
- Confidentiality: Prevent unauthorized disclosure
- Integrity: Prevent unauthorized modification
- Availability: Ensure authorized access

Bell-LaPadula (Confidentiality):
- Simple Security: No read up
- Star Property: No write down

Biba (Integrity):
- Simple Integrity: No read down
- Star Integrity: No write up
```

---

[← Previous: Disk Management](./10-Disk-Management.md) | [🏠 Back to Index](./README.md)
