# 🌐 Chapter 6: Application Layer

> **The Atomic Truth:** User-facing protocols that deliver network services.

---

## 🎯 Chapter Overview

| Topic | GATE Weightage | Difficulty |
|-------|----------------|------------|
| DNS | High | Medium |
| HTTP | Medium | Easy |
| SMTP/POP3/IMAP | Low-Medium | Easy |
| FTP | Low | Easy |
| DHCP | Medium | Easy |

---

## 6.1 Application Layer Overview

### Client-Server vs Peer-to-Peer

| Model | Description | Examples |
|-------|-------------|----------|
| **Client-Server** | Dedicated server, clients request | Web, Email, DNS |
| **Peer-to-Peer (P2P)** | All nodes equal | BitTorrent, Blockchain |
| **Hybrid** | Mix of both | Skype, Spotify |

### Application Layer Protocols

| Protocol | Transport | Port | Purpose |
|----------|-----------|------|---------|
| HTTP | TCP | 80 | Web pages |
| HTTPS | TCP | 443 | Secure web |
| FTP | TCP | 20, 21 | File transfer |
| SMTP | TCP | 25 | Send email |
| POP3 | TCP | 110 | Retrieve email |
| IMAP | TCP | 143 | Retrieve email (server-based) |
| DNS | UDP/TCP | 53 | Name resolution |
| DHCP | UDP | 67, 68 | IP address assignment |
| SNMP | UDP | 161 | Network management |
| Telnet | TCP | 23 | Remote terminal |
| SSH | TCP | 22 | Secure remote terminal |

---

## 6.2 DNS (Domain Name System) ⭐⭐

### DNS Purpose

$$\text{Domain Name} \leftrightarrow \text{IP Address}$$

Example: `www.google.com` → `142.250.190.46`

### DNS Hierarchy

```
                    . (Root)
                      │
        ┌─────────────┼─────────────┐
        │             │             │
      .com          .org          .edu
        │             │             │
    ┌───┴───┐        ...          ...
  google  amazon
    │
┌───┴───┐
www    mail
```

### DNS Components

| Component | Function |
|-----------|----------|
| **Resolver** | Client-side, initiates queries |
| **Root Server** | Top of hierarchy, 13 logical servers |
| **TLD Server** | .com, .org, .net, etc. |
| **Authoritative Server** | Has actual records for domain |
| **Caching Server** | Stores recent lookups |

### DNS Query Types

| Type | Description |
|------|-------------|
| **Recursive** | Resolver does all work, returns final answer |
| **Iterative** | Each server returns next server to ask |

### Recursive vs Iterative

```
RECURSIVE QUERY:
Client ─────► Local DNS ─────► Root ─────► TLD ─────► Authoritative
       ◄─────           ◄─────      ◄─────     ◄─────
       Answer         (DNS does     (DNS does   (DNS does
                       the work)    the work)   the work)

ITERATIVE QUERY:
Client ─────► Local DNS
       ◄───── "Ask Root"
       ─────► Root Server
       ◄───── "Ask TLD"
       ─────► TLD Server
       ◄───── "Ask Authoritative"
       ─────► Authoritative
       ◄───── Answer
```

### DNS Record Types ⭐

| Type | Purpose | Example |
|------|---------|---------|
| **A** | IPv4 address | www.example.com → 93.184.216.34 |
| **AAAA** | IPv6 address | www.example.com → 2606:2800:... |
| **CNAME** | Canonical name (alias) | www → webserver.example.com |
| **MX** | Mail exchanger | example.com → mail.example.com |
| **NS** | Name server | example.com → ns1.example.com |
| **PTR** | Reverse lookup | IP → domain |
| **SOA** | Start of Authority | Zone parameters |
| **TXT** | Text record | Verification, SPF |

### DNS Message Format

```
┌─────────────────────────────────────┐
│             Header (12 bytes)       │
├─────────────────────────────────────┤
│             Question Section        │
├─────────────────────────────────────┤
│             Answer Section          │
├─────────────────────────────────────┤
│           Authority Section         │
├─────────────────────────────────────┤
│           Additional Section        │
└─────────────────────────────────────┘
```

### DNS Caching

- **TTL (Time To Live):** How long to cache
- Reduces load on DNS servers
- Faster responses for repeated queries

### ⚠️ GATE TRAP: DNS Transport

- **Usually UDP:** Fast, port 53
- **TCP used when:**
  - Response > 512 bytes
  - Zone transfers (AXFR)
  - DNSSEC validation

#### 🧮 Practice Question

**Q:** What type of DNS record would you query to find the mail server for example.com?

**Answer:** **MX record**

---

## 6.3 HTTP (HyperText Transfer Protocol) ⭐

### HTTP Basics

- **Request-Response** protocol
- **Stateless:** Each request independent
- Default port: **80** (HTTP), **443** (HTTPS)

### HTTP Request Format

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive
<blank line>
[Body for POST/PUT]
```

### HTTP Response Format

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Connection: keep-alive
<blank line>
<html>...
```

### HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| **GET** | Retrieve resource | Yes | Yes |
| **POST** | Submit data | No | No |
| **PUT** | Create/Replace | Yes | No |
| **DELETE** | Remove resource | Yes | No |
| **HEAD** | Get headers only | Yes | Yes |
| **PATCH** | Partial update | No | No |
| **OPTIONS** | Get allowed methods | Yes | Yes |

### HTTP Status Codes

| Code | Category | Examples |
|------|----------|----------|
| 1xx | Informational | 100 Continue |
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved, 304 Not Modified |
| 4xx | Client Error | 400 Bad Request, 404 Not Found, 403 Forbidden |
| 5xx | Server Error | 500 Internal Error, 503 Service Unavailable |

### ⭐ Important Status Codes

| Code | Meaning |
|------|---------|
| **200** | OK (success) |
| **201** | Created |
| **301** | Moved Permanently |
| **302** | Found (temporary redirect) |
| **304** | Not Modified (use cache) |
| **400** | Bad Request |
| **401** | Unauthorized |
| **403** | Forbidden |
| **404** | Not Found |
| **500** | Internal Server Error |
| **503** | Service Unavailable |

### HTTP Versions

| Version | Features |
|---------|----------|
| **HTTP/1.0** | One request per connection |
| **HTTP/1.1** | Persistent connections, pipelining, Host header |
| **HTTP/2** | Binary, multiplexed, header compression, server push |
| **HTTP/3** | QUIC (UDP-based), faster connection setup |

### Persistent vs Non-Persistent Connections

**Non-Persistent (HTTP/1.0):**
- New TCP connection per object
- 2 RTTs per object (1 for TCP handshake, 1 for request/response)

**Persistent (HTTP/1.1+):**
- Reuse TCP connection
- Multiple objects on same connection
- Default behavior

#### 🧮 NAT Practice

**Q:** A webpage has 1 HTML file and 10 images. Calculate total RTTs for:
(a) Non-persistent HTTP
(b) Persistent HTTP without pipelining
(c) Persistent HTTP with pipelining

**Solution:**

(a) **Non-persistent:** 
- 11 objects × 2 RTTs = **22 RTTs**

(b) **Persistent without pipelining:**
- 1 TCP handshake (1 RTT)
- 11 requests × 1 RTT = 11 RTTs
- Total = **12 RTTs**

(c) **Persistent with pipelining:**
- 1 TCP handshake (1 RTT)
- 1 RTT for all requests (sent back-to-back)
- Total = **2 RTTs** (+ transfer time)

### Cookies and Sessions

**Problem:** HTTP is stateless

**Solution:** Cookies

```
Server → Client: Set-Cookie: sessionId=abc123
Client → Server: Cookie: sessionId=abc123
```

**Uses:**
- Session management (login)
- Personalization
- Tracking

### Web Caching (Proxy Server)

**Benefits:**
- Reduce latency
- Reduce bandwidth
- Reduce load on origin server

**Conditional GET:**
```
GET /page.html HTTP/1.1
If-Modified-Since: Wed, 01 Jan 2025 00:00:00 GMT

Response: 304 Not Modified (use cached version)
```

---

## 6.4 Email Protocols

### Email Architecture

```
┌─────────┐        ┌──────────────┐        ┌─────────┐
│  User   │──SMTP──│   Sender's   │──SMTP──│ Receiver│
│  Agent  │        │  Mail Server │        │  Mail   │
│ (MUA)   │        │    (MTA)     │        │ Server  │
└─────────┘        └──────────────┘        └────┬────┘
                                                 │
                                           POP3/IMAP
                                                 │
                                           ┌─────▼─────┐
                                           │  User     │
                                           │  Agent    │
                                           └───────────┘
```

### SMTP (Simple Mail Transfer Protocol)

- **Port:** 25 (or 587 for submission)
- **Transport:** TCP
- **Push protocol:** Sender initiates

**SMTP Commands:**
| Command | Purpose |
|---------|---------|
| HELO/EHLO | Introduce client |
| MAIL FROM | Sender address |
| RCPT TO | Recipient address |
| DATA | Message body (ends with `.`) |
| QUIT | End session |

**Example Session:**
```
S: 220 mail.server.com SMTP
C: HELO client.com
S: 250 Hello
C: MAIL FROM:<alice@client.com>
S: 250 OK
C: RCPT TO:<bob@server.com>
S: 250 OK
C: DATA
S: 354 Start mail input
C: Subject: Hello
C: 
C: This is the message.
C: .
S: 250 OK
C: QUIT
S: 221 Bye
```

### POP3 (Post Office Protocol v3)

- **Port:** 110
- **Pull protocol:** Client requests mail
- Downloads to local device
- Default: Delete from server after download

**POP3 Commands:**
| Command | Purpose |
|---------|---------|
| USER | Username |
| PASS | Password |
| LIST | List messages |
| RETR | Retrieve message |
| DELE | Delete message |
| QUIT | End session |

### IMAP (Internet Message Access Protocol)

- **Port:** 143
- **Pull protocol:** Client requests mail
- Mail stays on server
- Supports folders, search, partial fetch

**IMAP vs POP3:**
| Feature | POP3 | IMAP |
|---------|------|------|
| Mail storage | Client | Server |
| Multiple devices | Difficult | Easy |
| Folders | No | Yes |
| Partial download | No | Yes |
| Complexity | Simple | Complex |

### MIME (Multipurpose Internet Mail Extensions)

**Problem:** SMTP is 7-bit ASCII only

**Solution:** MIME encoding for:
- Attachments
- Non-ASCII text
- Rich formatting

**MIME Headers:**
```
Content-Type: multipart/mixed
Content-Transfer-Encoding: base64
```

---

## 6.5 FTP (File Transfer Protocol)

### FTP Basics

- **Ports:** 21 (control), 20 (data)
- **Transport:** TCP
- **Two connections:** Control + Data

### FTP Connection Types

**Active Mode:**
```
Client                          Server
  │                               │
  │───── Control (port 21) ──────►│
  │                               │
  │◄───── Data (port 20) ─────────│
          Server initiates
```

**Passive Mode:**
```
Client                          Server
  │                               │
  │───── Control (port 21) ──────►│
  │                               │
  │───── Data (port >1024) ──────►│
          Client initiates
```

**Why Passive?** Firewalls often block incoming connections

### FTP Commands

| Command | Purpose |
|---------|---------|
| USER | Username |
| PASS | Password |
| LIST | List directory |
| RETR | Download file |
| STOR | Upload file |
| CWD | Change directory |
| QUIT | Disconnect |

### FTP vs SFTP vs FTPS

| Protocol | Security | Port |
|----------|----------|------|
| FTP | None | 21 |
| FTPS | SSL/TLS | 990 |
| SFTP | SSH | 22 |

---

## 6.6 DHCP (Dynamic Host Configuration Protocol) ⭐

### DHCP Purpose

Automatically assign:
- IP address
- Subnet mask
- Default gateway
- DNS server

### DHCP Process (DORA)

```
Client                                          Server
   │                                               │
   │──────── DISCOVER (broadcast) ────────────────►│
   │           "Any DHCP servers?"                 │
   │                                               │
   │◄───────── OFFER (unicast/broadcast) ──────────│
   │           "Here's an IP: 192.168.1.100"       │
   │                                               │
   │──────── REQUEST (broadcast) ─────────────────►│
   │           "I'll take 192.168.1.100"           │
   │                                               │
   │◄───────── ACK (unicast/broadcast) ────────────│
   │           "Confirmed, lease for 1 hour"       │
```

**Mnemonic:** **D**iscover, **O**ffer, **R**equest, **A**ck = **DORA**

### DHCP Message Details

| Message | Source | Destination | Port |
|---------|--------|-------------|------|
| DISCOVER | 0.0.0.0:68 | 255.255.255.255:67 | Broadcast |
| OFFER | Server:67 | Client:68 | Unicast/Broadcast |
| REQUEST | 0.0.0.0:68 | 255.255.255.255:67 | Broadcast |
| ACK | Server:67 | Client:68 | Unicast/Broadcast |

### DHCP Lease

- IP assigned for limited time
- Client must renew before expiry
- At 50% lease time: Unicast REQUEST to original server
- At 87.5% lease time: Broadcast REQUEST

### DHCP Relay Agent

**Problem:** DHCP broadcasts don't cross routers

**Solution:** Relay agent forwards DHCP to server on different subnet

---

## 6.7 Telnet and SSH

### Telnet

- Remote terminal access
- **Port:** 23
- **Security:** None (plaintext!)
- Obsolete for security reasons

### SSH (Secure Shell)

- Encrypted remote access
- **Port:** 22
- Uses public key cryptography
- Supports tunneling (port forwarding)

---

## 6.8 SNMP (Simple Network Management Protocol)

### SNMP Purpose

Monitor and manage network devices

### SNMP Components

| Component | Role |
|-----------|------|
| **Manager** | Monitors, requests data |
| **Agent** | Runs on device, responds |
| **MIB** | Management Information Base (data structure) |

### SNMP Operations

| Operation | Direction | Purpose |
|-----------|-----------|---------|
| GET | Manager → Agent | Request value |
| SET | Manager → Agent | Modify value |
| TRAP | Agent → Manager | Alert/notification |

---

## 6.9 Other Application Protocols

### NTP (Network Time Protocol)

- Synchronize clocks
- **Port:** 123 (UDP)
- Stratum hierarchy (lower = more accurate)

### TFTP (Trivial FTP)

- Simple file transfer
- **Port:** 69 (UDP)
- No authentication
- Used for booting diskless clients

### BitTorrent

- P2P file sharing
- **Tracker:** Coordinates peers
- **Seeders:** Have complete file
- **Leechers:** Downloading

---

## 📝 Quick Revision Formula Sheet

### Port Numbers

| Service | Port |
|---------|------|
| FTP Data | 20 |
| FTP Control | 21 |
| SSH | 22 |
| Telnet | 23 |
| SMTP | 25 |
| DNS | 53 |
| DHCP Server | 67 |
| DHCP Client | 68 |
| TFTP | 69 |
| HTTP | 80 |
| POP3 | 110 |
| IMAP | 143 |
| HTTPS | 443 |

### DNS Records

| Type | Purpose |
|------|---------|
| A | IPv4 |
| AAAA | IPv6 |
| CNAME | Alias |
| MX | Mail server |
| NS | Name server |
| PTR | Reverse lookup |

### HTTP Calculation

| Connection Type | RTTs per Object |
|-----------------|-----------------|
| Non-persistent | 2 |
| Persistent | 1 (first has +1 for TCP) |
| Pipelined | All in 1 (after connection) |

---

## 🎯 Chapter Summary

1. **DNS:** Hierarchical naming, A/AAAA/MX/CNAME records, usually UDP port 53
2. **HTTP:** Request-response, stateless, methods (GET/POST), status codes
3. **HTTP versions:** 1.0 (non-persistent), 1.1 (persistent), 2.0 (multiplexed)
4. **SMTP:** Push email, port 25, text-based commands
5. **POP3:** Pull email, downloads to client, port 110
6. **IMAP:** Pull email, keeps on server, port 143
7. **FTP:** Two connections (control 21, data 20), active/passive modes
8. **DHCP:** DORA process, assigns IP/mask/gateway/DNS, UDP 67/68

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
> Would you like to initiate a **'Multi-Variable Stress Test'** combining this with **Network Security** for a Rank-1 simulation?
