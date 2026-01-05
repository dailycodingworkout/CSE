# Module 8: Application Layer | The Singularity

> **The Atomic Truth:** *Application Layer = User-facing network services*

---

## 8.1 Application Layer Overview

### **Position in Stack**

```
┌───────────────────────────────────────────┐
│            APPLICATION LAYER               │
│                                           │
│   HTTP, HTTPS, FTP, SMTP, DNS, DHCP       │
│   Telnet, SSH, SNMP, POP3, IMAP           │
│                                           │
│   User Interface to Network Services       │
└───────────────────────────────────────────┘
                    ↓
            Transport Layer (TCP/UDP)
```

### **Client-Server Model**

```
    Client                        Server
       │                             │
       │ ────── Request ────────────>│
       │                             │
       │ <───── Response ────────────│
       │                             │
  (Initiates)                   (Always on)
  (Ephemeral port)              (Well-known port)
```

### **Peer-to-Peer Model**

```
    Peer A ←────────────────→ Peer B
       ↑                         ↑
       │                         │
       └─────────→ Peer C ←──────┘
       
  (Each peer is both client and server)
```

---

## 8.2 DNS (Domain Name System) | The Internet's Phonebook

### **Purpose**
Maps domain names to IP addresses and vice versa.

### **DNS Hierarchy**

```
                         . (Root)
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
      .com                .org                .in
        │                   │                   │
    ┌───┴───┐          wikipedia           ┌───┴───┐
  google  amazon                         google  gov
    │                                              │
   www                                           nic
```

### **DNS Record Types**

| Type | Name | Purpose | Example |
|------|------|---------|---------|
| **A** | Address | IPv4 address | www.google.com → 142.250.x.x |
| **AAAA** | IPv6 Address | IPv6 address | |
| **CNAME** | Canonical Name | Alias | www → server1.google.com |
| **MX** | Mail Exchange | Mail server | google.com → smtp.google.com |
| **NS** | Name Server | Authoritative DNS | google.com → ns1.google.com |
| **PTR** | Pointer | Reverse lookup | IP → name |
| **SOA** | Start of Authority | Zone info | Primary NS, admin, timers |
| **TXT** | Text | Arbitrary text | SPF, DKIM records |

### **DNS Resolution Process**

```
Client                Local DNS              Root           TLD         Authoritative
  │                      │                    │              │               │
  │── Query: www.google.com ─>│               │              │               │
  │                      │── Query ─────────>│              │               │
  │                      │<── Refer to .com ─│              │               │
  │                      │── Query ─────────────────────>│               │
  │                      │<── Refer to ns.google.com ────│               │
  │                      │── Query ─────────────────────────────────>│
  │                      │<── IP: 142.250.x.x ───────────────────────│
  │<── IP: 142.250.x.x ──│                    │              │               │
```

### **Iterative vs Recursive Queries**

| Type | Description | Who does work |
|------|-------------|---------------|
| **Recursive** | Resolver does full resolution | Local DNS server |
| **Iterative** | Returns best known answer | Client follows referrals |

### **DNS Caching**
- Each record has **TTL (Time To Live)**
- Cached records reduce load on DNS servers
- Trade-off: Stale data vs performance

### **DNS Transport**
- **UDP port 53** — Normal queries (< 512 bytes)
- **TCP port 53** — Zone transfers, large responses

### **GATE Trap Alert ⚠️**

**DNS uses UDP primarily, but TCP for:**
1. Zone transfers (AXFR)
2. Responses > 512 bytes (with EDNS0, up to 4096 bytes)
3. DNS over TCP/TLS/HTTPS (modern)

---

## 8.3 HTTP (Hypertext Transfer Protocol)

### **HTTP Basics**

| Feature | Value |
|---------|-------|
| Port | TCP 80 |
| Type | Request-Response |
| State | Stateless (HTTP/1.x) |
| Latest | HTTP/3 (over QUIC/UDP) |

### **HTTP Request Structure**

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
Connection: keep-alive

[Body - for POST/PUT]
```

### **HTTP Methods**

| Method | Purpose | Safe | Idempotent |
|--------|---------|------|------------|
| **GET** | Retrieve resource | Yes | Yes |
| **POST** | Submit data | No | No |
| **PUT** | Replace resource | No | Yes |
| **DELETE** | Remove resource | No | Yes |
| **HEAD** | GET without body | Yes | Yes |
| **PATCH** | Partial update | No | No |
| **OPTIONS** | Supported methods | Yes | Yes |

### **HTTP Response Status Codes**

| Code | Category | Examples |
|------|----------|----------|
| **1xx** | Informational | 100 Continue |
| **2xx** | Success | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| **5xx** | Server Error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

### **The Mnemonic 🧠**
> **"1-Info, 2-Success, 3-Redirect, 4-Client Error, 5-Server Error"**

### **HTTP Versions**

| Version | Features |
|---------|----------|
| **HTTP/1.0** | Non-persistent (1 request/connection) |
| **HTTP/1.1** | Persistent connections, pipelining |
| **HTTP/2** | Multiplexing, binary protocol, header compression |
| **HTTP/3** | Over QUIC (UDP), faster handshake |

### **Persistent vs Non-Persistent**

**Non-persistent (HTTP/1.0):**
$$Time = n \times (2 \times RTT + File\_Time)$$

**Persistent (HTTP/1.1):**
$$Time = 2 \times RTT + n \times File\_Time$$
(assuming pipelining/multiplexing)

### **GATE NAT Favorite: HTTP Timing**

**Problem:** Calculate time to fetch a web page with 1 HTML and 5 images.

**Non-persistent (6 objects):**
$$Time = 6 \times (2 \times RTT) + 6 \times T_{trans}$$

**Persistent without pipelining:**
$$Time = 2 \times RTT + 5 \times RTT + 6 \times T_{trans}$$

**Persistent with pipelining:**
$$Time = 2 \times RTT + RTT + 6 \times T_{trans}$$ (approximately)

---

## 8.4 HTTPS (HTTP Secure)

### **HTTPS = HTTP + TLS/SSL**

| Feature | Value |
|---------|-------|
| Port | TCP 443 |
| Encryption | TLS (Transport Layer Security) |
| Certificate | X.509 |

### **TLS Handshake (Simplified)**

```
Client                                     Server
   │                                          │
   │ ─── ClientHello (versions, ciphers) ────>│
   │                                          │
   │ <── ServerHello, Certificate, Done ──────│
   │                                          │
   │ ─── Key Exchange, Change Cipher ────────>│
   │                                          │
   │ <── Change Cipher, Finished ─────────────│
   │                                          │
   │ ═══════ Encrypted Data ════════════════> │
```

---

## 8.5 FTP (File Transfer Protocol)

### **FTP Characteristics**

| Feature | Value |
|---------|-------|
| Control Port | TCP 21 |
| Data Port | TCP 20 (active) or dynamic (passive) |
| Type | Stateful (maintains session) |
| Authentication | Username/Password |

### **FTP Modes**

#### **Active Mode**
```
Client (Port X) ──────> Server (Port 21)   [Control]
Server (Port 20) ──────> Client (Port X+1) [Data]
```
- Server initiates data connection
- Problem: Client firewall blocks incoming

#### **Passive Mode**
```
Client (Port X) ──────> Server (Port 21)   [Control]
Client (Port Y) ──────> Server (Port Z)    [Data]
```
- Client initiates both connections
- Better for firewalls/NAT

### **FTP Commands**

| Command | Purpose |
|---------|---------|
| USER | Send username |
| PASS | Send password |
| LIST | List files |
| RETR | Download file |
| STOR | Upload file |
| QUIT | Close connection |
| PORT | Specify data port (active) |
| PASV | Request passive mode |

---

## 8.6 Email Protocols

### **Email Architecture**

```
Sender                                              Receiver
   │                                                    │
   │     ┌──────┐         ┌──────┐         ┌──────┐    │
   └────>│ MUA  │──SMTP──>│ MTA  │──SMTP──>│ MTA  │    │
         └──────┘         └──────┘         └──────┘    │
                                               │       │
                                         POP3/IMAP     │
                                               │       │
                                          ┌──────┐     │
                                          │ MUA  │<────┘
                                          └──────┘

MUA = Mail User Agent (client)
MTA = Mail Transfer Agent (server)
```

### **SMTP (Simple Mail Transfer Protocol)**

| Feature | Value |
|---------|-------|
| Port | TCP 25 (587 with auth, 465 with TLS) |
| Function | Sending/relaying mail |
| Model | Push |

**SMTP Commands:**
| Command | Purpose |
|---------|---------|
| HELO/EHLO | Greeting |
| MAIL FROM | Sender address |
| RCPT TO | Recipient address |
| DATA | Start message body |
| QUIT | End session |

### **POP3 (Post Office Protocol v3)**

| Feature | Value |
|---------|-------|
| Port | TCP 110 (995 with TLS) |
| Function | Retrieve mail |
| Model | Download and delete |

**Characteristic:** Downloads mail to local device, typically deletes from server

### **IMAP (Internet Message Access Protocol)**

| Feature | Value |
|---------|-------|
| Port | TCP 143 (993 with TLS) |
| Function | Manage mail on server |
| Model | Keep on server |

**Characteristic:** Keeps mail on server, supports folders, search, multiple devices

### **POP3 vs IMAP**

| Feature | POP3 | IMAP |
|---------|------|------|
| Storage | Local | Server |
| Multiple devices | Difficult | Easy |
| Offline access | After download | Limited |
| Server load | Low | Higher |
| Complexity | Simple | Complex |

---

## 8.7 DHCP (Dynamic Host Configuration Protocol)

### **Purpose**
Automatically assigns IP addresses and network configuration.

### **DHCP Process (DORA)**

```
Client                                          Server
   │                                               │
   │ ─── DISCOVER (broadcast) ────────────────────>│
   │                                               │
   │ <── OFFER (IP, mask, gateway, DNS, lease) ───│
   │                                               │
   │ ─── REQUEST (accept offer) ──────────────────>│
   │                                               │
   │ <── ACKNOWLEDGE (confirmed) ─────────────────│
   │                                               │
```

### **The Mnemonic 🧠**
> **"DORA the Explorer"** = Discover, Offer, Request, Acknowledge

### **DHCP Ports**
- **Server:** UDP 67
- **Client:** UDP 68

### **DHCP Lease**
- IP assigned for limited time
- Client must renew (at T1 = 50% of lease)
- Rebind at T2 = 87.5% if renewal fails

### **DHCP Relay Agent**
- Forwards DHCP messages across subnets
- Allows centralized DHCP server

---

## 8.8 Telnet & SSH

### **Telnet**

| Feature | Value |
|---------|-------|
| Port | TCP 23 |
| Security | **None** (plaintext) |
| Use | Legacy remote access |

**Problem:** Passwords and data sent in cleartext!

### **SSH (Secure Shell)**

| Feature | Value |
|---------|-------|
| Port | TCP 22 |
| Security | Encrypted |
| Use | Secure remote access |

**Features:**
- Strong authentication
- Encrypted session
- Port forwarding
- File transfer (SCP, SFTP)

---

## 8.9 SNMP (Simple Network Management Protocol)

### **Purpose**
Network device monitoring and management.

### **SNMP Components**

| Component | Role |
|-----------|------|
| **Manager** | Monitors network |
| **Agent** | Runs on managed device |
| **MIB** | Management Information Base (data structure) |

### **SNMP Operations**

| Operation | Direction | Purpose |
|-----------|-----------|---------|
| GET | Manager → Agent | Retrieve value |
| SET | Manager → Agent | Change value |
| GETNEXT | Manager → Agent | Get next in MIB |
| TRAP | Agent → Manager | Alert/notification |

### **SNMP Ports**
- **Agent:** UDP 161
- **Manager (traps):** UDP 162

---

## 8.10 Other Protocols

### **TFTP (Trivial File Transfer Protocol)**

| Feature | Value |
|---------|-------|
| Port | UDP 69 |
| Use | Simple file transfer (boot images) |
| Authentication | None |
| Features | No directory listing |

### **NTP (Network Time Protocol)**

| Feature | Value |
|---------|-------|
| Port | UDP 123 |
| Use | Time synchronization |
| Accuracy | Milliseconds over internet |

---

## 8.11 Protocol Summary Table

| Protocol | Port | Transport | Purpose |
|----------|------|-----------|---------|
| FTP Data | 20 | TCP | File transfer data |
| FTP Control | 21 | TCP | File transfer commands |
| SSH | 22 | TCP | Secure shell |
| Telnet | 23 | TCP | Remote terminal |
| SMTP | 25 | TCP | Send email |
| DNS | 53 | TCP/UDP | Name resolution |
| DHCP Server | 67 | UDP | IP assignment |
| DHCP Client | 68 | UDP | IP assignment |
| TFTP | 69 | UDP | Simple file transfer |
| HTTP | 80 | TCP | Web |
| POP3 | 110 | TCP | Retrieve email |
| NTP | 123 | UDP | Time sync |
| IMAP | 143 | TCP | Email management |
| SNMP | 161 | UDP | Network management |
| HTTPS | 443 | TCP | Secure web |

---

## 8.12 Solved Examples

### **Example 1: HTTP Timing**

**Problem:** A web page has 1 base HTML (1 KB) and 10 images (1 KB each). RTT = 100 ms, bandwidth = 1 Mbps. Calculate download time for non-persistent HTTP.

**Solution:**

**Per object:**
- Connection setup: 1 RTT = 100 ms
- Request + response: 1 RTT = 100 ms
- Transmission: 1 KB / 1 Mbps = 8 ms

**Total per object:** 208 ms

**11 objects (non-persistent, sequential):**
Total = 11 × 208 ms = **2.288 seconds**

---

### **Example 2: DNS Query Count**

**Problem:** How many DNS queries are needed to resolve www.example.com if local cache is empty?

**Solution:**
Typically with iterative resolution from local DNS:
1. Local DNS → Root (get .com NS)
2. Local DNS → .com TLD (get example.com NS)
3. Local DNS → example.com NS (get www.example.com A)

**Answer: 3 queries** (from local DNS perspective)

---

### **Example 3: DHCP Process**

**Problem:** What messages are exchanged in DHCP?

**Solution:**
1. **DISCOVER:** Client broadcasts to find servers
2. **OFFER:** Server offers configuration
3. **REQUEST:** Client accepts offer
4. **ACKNOWLEDGE:** Server confirms

**Answer: 4 messages (DORA)**

---

## 8.13 Practice Problems

**Q1.** DNS primarily uses which transport protocol?
- (a) TCP
- (b) UDP
- (c) SCTP
- (d) ICMP

<details>
<summary>Answer</summary>
**(b) UDP** — DNS uses UDP for normal queries (TCP for zone transfers and large responses)
</details>

---

**Q2.** FTP uses which ports?
- (a) 20 and 21
- (b) 22 and 23
- (c) 25 and 110
- (d) 80 and 443

<details>
<summary>Answer</summary>
**(a) 20 and 21** — 21 for control, 20 for data (active mode)
</details>

---

**Q3.** HTTP status code 404 means:
- (a) Success
- (b) Redirect
- (c) Not Found
- (d) Server Error

<details>
<summary>Answer</summary>
**(c) Not Found** — 404 is a client error indicating resource not found
</details>

---

**Q4.** [NAT] DHCP server uses which UDP port?

<details>
<summary>Answer</summary>
$\boxed{67}$
</details>

---

**Q5.** Which protocol keeps email on the server?
- (a) POP3
- (b) SMTP
- (c) IMAP
- (d) FTP

<details>
<summary>Answer</summary>
**(c) IMAP** — IMAP manages mail on the server
</details>

---

## 8.14 The 5-Second Snap-Check ✅

1. ☐ DNS: UDP 53, hierarchical, A/AAAA/CNAME/MX records
2. ☐ HTTP: TCP 80, stateless, GET/POST methods
3. ☐ FTP: TCP 21 (control), 20 (data), active vs passive
4. ☐ SMTP: TCP 25 (sending), POP3: 110, IMAP: 143
5. ☐ DHCP: UDP 67/68, DORA process
6. ☐ SSH: TCP 22 (secure), Telnet: TCP 23 (insecure)

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next:** [Module 9: Network Security →](./09-Network-Security.md)
