# Chapter 7: Application Layer
## The User Interface | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Application layer provides services users actually need: web, email, files, names."**

---

## 7.1 Application Layer Overview

### Network Application Architectures

| Architecture | Description | Example |
|--------------|-------------|---------|
| Client-Server | Server always on, clients request | Web, Email |
| Peer-to-Peer (P2P) | Peers both request and serve | BitTorrent, Skype |
| Hybrid | Combination of both | Napster (centralized index) |

### Application Layer Protocols

| Protocol | Port | Transport | Purpose |
|----------|------|-----------|---------|
| HTTP | 80 | TCP | Web pages |
| HTTPS | 443 | TCP | Secure web |
| FTP | 20/21 | TCP | File transfer |
| SMTP | 25 | TCP | Email sending |
| POP3 | 110 | TCP | Email retrieval |
| IMAP | 143 | TCP | Email access |
| DNS | 53 | UDP/TCP | Name resolution |
| DHCP | 67/68 | UDP | IP configuration |
| Telnet | 23 | TCP | Remote terminal |
| SSH | 22 | TCP | Secure remote |
| SNMP | 161/162 | UDP | Network management |

---

## 7.2 DNS (Domain Name System)

### Purpose
Translate human-readable names to IP addresses.

```
www.google.com → 142.250.190.46
```

### DNS Hierarchy

```
                    Root (.)
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
  .com              .org              .edu
    │                 │                 │
  google           wikipedia         mit
    │                 │                 │
  www, mail        www, en          www, web
```

### DNS Record Types

| Type | Purpose | Example |
|------|---------|---------|
| A | IPv4 address | www.example.com → 93.184.216.34 |
| AAAA | IPv6 address | www.example.com → 2606:2800:... |
| CNAME | Canonical name (alias) | blog.example.com → www.example.com |
| MX | Mail exchanger | example.com → mail.example.com |
| NS | Name server | example.com → ns1.example.com |
| PTR | Reverse lookup | IP → domain name |
| SOA | Start of Authority | Zone information |
| TXT | Text record | SPF, DKIM |

### DNS Query Process

```
1. User types www.example.com
2. Check local cache
3. Query local DNS resolver
4. Resolver queries Root server → "Ask .com"
5. Resolver queries .com TLD → "Ask example.com NS"
6. Resolver queries example.com NS → "IP is 93.184.216.34"
7. Resolver caches and returns to user
```

### DNS Query Types

| Type | Description |
|------|-------------|
| Recursive | Resolver does all work |
| Iterative | Client follows referrals |
| Inverse | IP to domain name |

### DNS Message Format

```
┌─────────────────────────────────────┐
│          Header (12 bytes)          │
├─────────────────────────────────────┤
│          Question Section           │
├─────────────────────────────────────┤
│          Answer Section             │
├─────────────────────────────────────┤
│         Authority Section           │
├─────────────────────────────────────┤
│         Additional Section          │
└─────────────────────────────────────┘
```

### 🎯 DNS Key Points

- Uses UDP port 53 (TCP for zone transfers or large responses)
- TTL (Time To Live) for caching
- Distributed database
- Hierarchical namespace

---

## 7.3 HTTP (Hypertext Transfer Protocol)

### HTTP Versions

| Version | Features |
|---------|----------|
| HTTP/1.0 | Non-persistent, one request per connection |
| HTTP/1.1 | Persistent connections, pipelining |
| HTTP/2 | Binary, multiplexing, header compression |
| HTTP/3 | QUIC (UDP-based), faster |

### HTTP Request

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive
```

### HTTP Response

```
HTTP/1.1 200 OK
Date: Mon, 06 Jan 2026 12:00:00 GMT
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

### HTTP Methods

| Method | Purpose | Idempotent |
|--------|---------|------------|
| GET | Retrieve resource | Yes |
| POST | Submit data | No |
| PUT | Update/Create resource | Yes |
| DELETE | Remove resource | Yes |
| HEAD | Get headers only | Yes |
| OPTIONS | Get supported methods | Yes |
| PATCH | Partial update | No |

### HTTP Status Codes

| Code Range | Category | Examples |
|------------|----------|----------|
| 1xx | Informational | 100 Continue |
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved, 304 Not Modified |
| 4xx | Client Error | 400 Bad Request, 404 Not Found |
| 5xx | Server Error | 500 Internal Error, 503 Service Unavailable |

### Persistent vs Non-Persistent

**Non-Persistent (HTTP/1.0):**
- New TCP connection per object
- Time = 2×RTT + file transfer per object

**Persistent (HTTP/1.1):**
- Single TCP connection for multiple objects
- Time = 1×RTT (connection) + n×(RTT + transfer)

### 🎯 HTTP Response Time Calculation

**Non-persistent, n objects:**
$$\text{Time} = n \times (2 \times RTT + \text{Transmission time})$$

**Persistent without pipelining:**
$$\text{Time} = 2 \times RTT + n \times (RTT + \text{Transmission time})$$

**Persistent with pipelining:**
$$\text{Time} = 2 \times RTT + RTT + \text{Transmission times}$$

---

## 7.4 Email Protocols

### Email Architecture

```
┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
│ User   │    │ Sender │    │Receiver│    │ User   │
│ Agent  │───→│ Mail   │───→│ Mail   │───→│ Agent  │
│ (MUA)  │    │ Server │    │ Server │    │ (MUA)  │
└────────┘    └────────┘    └────────┘    └────────┘
              SMTP ───→    SMTP ───→    POP3/IMAP
```

### SMTP (Simple Mail Transfer Protocol)

- Push protocol (sender initiates)
- Port 25 (587 for submission)
- ASCII text-based

```
HELO mail.sender.com
MAIL FROM:<sender@sender.com>
RCPT TO:<receiver@receiver.com>
DATA
Subject: Hello

This is the body.
.
QUIT
```

### POP3 (Post Office Protocol v3)

- Pull protocol (receiver retrieves)
- Port 110 (995 for SSL)
- Download and delete (typically)
- Simple, limited features

### IMAP (Internet Message Access Protocol)

- Pull protocol
- Port 143 (993 for SSL)
- Server-based storage
- Folders, search, partial fetch

### 🎯 Email Protocol Comparison

| Feature | SMTP | POP3 | IMAP |
|---------|------|------|------|
| Direction | Send | Receive | Receive |
| Connection | Push | Pull | Pull |
| Storage | Transfers | Downloads | Server-side |
| Multi-device | N/A | No | Yes |

---

## 7.5 FTP (File Transfer Protocol)

### Characteristics

- Two connections:
  - Control: Port 21 (commands)
  - Data: Port 20 (file transfer)
- Stateful

### FTP Modes

**Active Mode:**
```
Client sends: PORT (IP, port)
Server connects FROM port 20 TO client's port
```

**Passive Mode:**
```
Client sends: PASV
Server responds with IP and port
Client connects TO server's port
```

### FTP Commands

| Command | Purpose |
|---------|---------|
| USER | Username |
| PASS | Password |
| LIST | Directory listing |
| RETR | Download file |
| STOR | Upload file |
| PWD | Print working directory |
| CWD | Change directory |
| QUIT | Disconnect |

---

## 7.6 DHCP (Dynamic Host Configuration Protocol)

### Purpose
Automatically assign IP addresses and network configuration.

### DHCP Process (DORA)

```
Client                           Server
   │                               │
   │──DHCP Discover (broadcast)──→│
   │                               │
   │←──DHCP Offer────────────────│
   │                               │
   │──DHCP Request (broadcast)───→│
   │                               │
   │←──DHCP Acknowledgment───────│
   │                               │
   │      (Client uses IP)         │
```

### DHCP Message Fields

| Field | Purpose |
|-------|---------|
| Offered IP | IP address for client |
| Subnet Mask | Network mask |
| Default Gateway | Router IP |
| DNS Server | DNS server IP |
| Lease Time | How long IP is valid |

### 🎯 DHCP Lease

- Client must renew before expiry
- T1 (50%): Try to renew with same server
- T2 (87.5%): Try any server
- Expiry: Lose IP address

---

## 7.7 Telnet and SSH

### Telnet

- Port 23
- Remote terminal access
- **Insecure:** Plain text (including passwords)

### SSH (Secure Shell)

- Port 22
- Encrypted remote access
- Key-based authentication
- Tunneling capability

```
SSH provides:
1. Encryption
2. Authentication
3. Integrity
```

---

## 7.8 SNMP (Simple Network Management Protocol)

### Purpose
Monitor and manage network devices.

### Components

| Component | Description |
|-----------|-------------|
| Manager | Monitoring station |
| Agent | Software on managed device |
| MIB | Management Information Base (data) |

### SNMP Operations

| Operation | Purpose |
|-----------|---------|
| GET | Read single variable |
| GET-NEXT | Read next variable |
| GET-BULK | Read multiple variables |
| SET | Write variable |
| TRAP | Alert from agent |

### Ports
- Agent: UDP 161
- Trap receiver: UDP 162

---

## 7.9 Socket Programming Concepts

### TCP Socket Flow

```
Server:                     Client:
socket()                    socket()
bind()                        │
listen()                      │
   │←── connect() ───────────│
accept()                      │
   │←── recv() ←─ send() ────│
   │─── send() ─→ recv() ───→│
close()                     close()
```

### UDP Socket Flow

```
Server:                     Client:
socket()                    socket()
bind()                        │
   │←── recvfrom() ← sendto()│
   │─── sendto() ─→ recvfrom()│
close()                     close()
```

---

## 🎯 Practice Problems

### Problem 1: DNS
**Q:** User queries www.example.com. DNS cache is empty. How many DNS queries minimum?
**Answer:** 3 (Root → .com TLD → example.com authoritative)

### Problem 2: HTTP
**Q:** 10 objects, non-persistent HTTP, RTT = 100 ms. Find time (ignore transmission).
**Solution:** $10 \times 2 \times 100 = 2000$ ms = **2 seconds**

### Problem 3: HTTP Persistent
**Q:** Base page + 10 embedded objects, persistent pipelining, RTT = 100 ms.
**Solution:**
- Connection: 1 RTT
- Base page: 1 RTT
- 10 objects (pipelined): 1 RTT
- Total: 3 × 100 = **300 ms**

### Problem 4: DHCP
**Q:** Correct order of DHCP messages?
**Answer:** Discover → Offer → Request → Acknowledge (DORA)

### Problem 5: Email
**Q:** Which protocol sends email between mail servers?
**Answer:** SMTP

### Problem 6: Ports
**Q:** Match protocol to port: HTTP, DNS, FTP Control, SSH
**Answer:** HTTP=80, DNS=53, FTP=21, SSH=22

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"DNS Delivers Names, DHCP Delivers IPs"**
**"SMTP Sends, POP3 Pulls, IMAP Is Anywhere"**
**"FTP has Two Tunnels: Control and Data"**

### The Mental Slider
- **DNS:** Phone book (name → number)
- **HTTP:** Waiter taking orders (request → response)
- **SMTP:** Post office (mail delivery)
- **DHCP:** Reception desk (giving room key/IP)

### The 5-Second Snap-Check
1. **DNS port?** 53
2. **HTTP secure?** HTTPS on 443
3. **DHCP order?** DORA
4. **FTP ports?** 20 (data), 21 (control)
5. **Email send?** SMTP, Email receive? POP3/IMAP

---

## 📈 Key Formulas

| Formula | Description |
|---------|-------------|
| HTTP non-persistent: $2 \times RTT \times n$ | Time for n objects |
| HTTP persistent: $RTT + n \times RTT$ | Without pipelining |
| HTTP pipeline: $2 \times RTT + RTT$ | One RTT for all objects |

---

## 📊 Protocol Summary Table

| Protocol | Port | Transport | Layer | Purpose |
|----------|------|-----------|-------|---------|
| DNS | 53 | UDP/TCP | Application | Name resolution |
| HTTP | 80 | TCP | Application | Web |
| HTTPS | 443 | TCP | Application | Secure web |
| FTP | 20,21 | TCP | Application | File transfer |
| SMTP | 25 | TCP | Application | Send email |
| POP3 | 110 | TCP | Application | Receive email |
| IMAP | 143 | TCP | Application | Email access |
| DHCP | 67,68 | UDP | Application | IP config |
| SSH | 22 | TCP | Application | Secure shell |
| Telnet | 23 | TCP | Application | Remote terminal |
| SNMP | 161,162 | UDP | Application | Network management |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Transport Layer](06-Transport-Layer.md) | [Next: Network Security →](08-Network-Security.md)
