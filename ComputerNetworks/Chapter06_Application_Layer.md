# Chapter 6: Application Layer

## 🎯 GATE/ESE Weightage: 4-6 marks (Conceptual + Protocol Details)

---

## 6.1 Application Layer Overview

The Application Layer is the **interface** between users/applications and the network.

**Key Characteristics**:
- Uses services of Transport layer
- Defines message syntax and semantics
- Implements application-level protocols

### Application Architectures

```
CLIENT-SERVER:                    PEER-TO-PEER (P2P):
    ┌────────┐                        [Peer A]
    │ SERVER │                        ↗  ↕  ↘
    └───┬────┘                    [Peer B] ↔ [Peer C]
   ↙    ↓    ↘                        ↘  ↕  ↗
[C1]  [C2]  [C3]                      [Peer D]

- Server always on                - No always-on server
- Clients contact server          - Peers contact peers
- Server has fixed IP             - Peers have dynamic IP
- Scalability limited             - Self-scaling
```

---

## 6.2 DNS (Domain Name System) (🎯 VERY IMPORTANT)

### Purpose

Translate **domain names** to **IP addresses** (and vice versa).

```
www.google.com → 142.250.192.46

Why not just use IP addresses?
- Hard to remember
- IP can change, name stays same
- Load balancing (one name → multiple IPs)
```

### DNS Hierarchy

```
                    . (Root)
                      │
          ┌───────────┼───────────┐
         com         org         edu
          │           │           │
     ┌────┴────┐     ...      ┌──┴──┐
   google   amazon          mit   stanford
     │         │             │
   www       www           www
```

**Domain Name Structure**:
```
www.example.com.
 │      │    │ │
 │      │    │ └─ Root (often implicit)
 │      │    └─── TLD (Top Level Domain)
 │      └──────── SLD (Second Level Domain)
 └─────────────── Subdomain/Host
```

### DNS Server Types

| Type | Function | Example |
|------|----------|---------|
| **Root** | Points to TLD servers | 13 root server clusters (a.root-servers.net) |
| **TLD** | Handles .com, .org, .edu, etc. | Verisign (.com), PIR (.org) |
| **Authoritative** | Has actual DNS records | google.com's DNS server |
| **Recursive/Local** | Caches and resolves queries | ISP's DNS, 8.8.8.8 |

### DNS Resolution Process

```
User                Local DNS          Root            TLD         Authoritative
 │                     │                │               │               │
 │─1. www.google.com──→│                │               │               │
 │                     │─2. Who has .com?→              │               │
 │                     │←3. Ask a.gtld-servers.net──────│               │
 │                     │─4. Who has google.com?─────────→               │
 │                     │←5. Ask ns1.google.com──────────│               │
 │                     │─6. IP of www.google.com?───────────────────────→
 │                     │←7. 142.250.192.46──────────────────────────────│
 │←8. 142.250.192.46───│                                                │
```

### Iterative vs Recursive Queries

| Type | Description |
|------|-------------|
| **Recursive** | Server does complete resolution (client ↔ local DNS) |
| **Iterative** | Server returns referral, client queries next server |

**Typical**: Client uses recursive, DNS servers use iterative among themselves.

### DNS Record Types (🎯 MEMORIZE)

| Type | Name | Purpose | Example |
|------|------|---------|---------|
| **A** | Address | IPv4 address | www.example.com → 93.184.216.34 |
| **AAAA** | IPv6 Address | IPv6 address | → 2606:2800:220:1:248:1893:25c8:1946 |
| **CNAME** | Canonical Name | Alias | www → example.com |
| **MX** | Mail Exchange | Mail server | → mail.example.com (priority 10) |
| **NS** | Name Server | Authoritative DNS | → ns1.example.com |
| **PTR** | Pointer | Reverse DNS (IP→name) | 34.216.184.93 → example.com |
| **SOA** | Start of Authority | Zone info, serial number | Primary NS, admin email |
| **TXT** | Text | Arbitrary text | SPF records, verification |

### DNS Message Format

```
┌────────────────────────────────────────────────┐
│                   Header (12 bytes)            │
├────────────────────────────────────────────────┤
│                   Question                     │
├────────────────────────────────────────────────┤
│                   Answer (RRs)                 │
├────────────────────────────────────────────────┤
│                   Authority (RRs)              │
├────────────────────────────────────────────────┤
│                   Additional (RRs)             │
└────────────────────────────────────────────────┘
```

### DNS Transport

- **UDP port 53**: Default (response < 512 bytes)
- **TCP port 53**: Zone transfers, large responses

### DNS Caching

- **TTL** (Time To Live): How long to cache
- Reduces load on authoritative servers
- Speeds up resolution

---

## 6.3 HTTP (Hypertext Transfer Protocol) (🎯 IMPORTANT)

### HTTP Versions

| Version | Year | Key Features |
|---------|------|--------------|
| HTTP/0.9 | 1991 | GET only, no headers |
| HTTP/1.0 | 1996 | Headers, status codes, non-persistent |
| HTTP/1.1 | 1997 | Persistent connections, pipelining, Host header |
| HTTP/2 | 2015 | Binary framing, multiplexing, server push |
| HTTP/3 | 2022 | QUIC (UDP-based), reduced latency |

### HTTP/1.0 vs HTTP/1.1

```
HTTP/1.0 (Non-Persistent):         HTTP/1.1 (Persistent):
┌─────────┐    ┌─────────┐         ┌─────────┐    ┌─────────┐
│ Client  │    │ Server  │         │ Client  │    │ Server  │
└────┬────┘    └────┬────┘         └────┬────┘    └────┬────┘
     │              │                   │              │
     │──TCP Connect─→                   │──TCP Connect─→
     │──Request 1───→                   │──Request 1───→
     │←──Response 1──│                  │←──Response 1──│
     │──TCP Close───→                   │──Request 2───→
     │              │                   │←──Response 2──│
     │──TCP Connect─→                   │──Request 3───→
     │──Request 2───→                   │←──Response 3──│
     │←──Response 2──│                  │──TCP Close───→
     │──TCP Close───→                   │              │
```

**HTTP/1.0**: 1 connection per request (2 RTT + transfer each)
**HTTP/1.1**: Multiple requests per connection (persistent)

### HTTP Request Methods

| Method | Purpose | Safe | Idempotent |
|--------|---------|------|------------|
| **GET** | Retrieve resource | Yes | Yes |
| **POST** | Submit data | No | No |
| **PUT** | Update/Create resource | No | Yes |
| **DELETE** | Delete resource | No | Yes |
| **HEAD** | GET without body | Yes | Yes |
| **OPTIONS** | Supported methods | Yes | Yes |
| **PATCH** | Partial update | No | No |

**Safe**: No side effects (read-only)
**Idempotent**: Same result if repeated

### HTTP Request Format

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
Connection: keep-alive
<blank line>
[Body for POST/PUT]
```

### HTTP Response Format

```
HTTP/1.1 200 OK
Date: Mon, 01 Jan 2024 00:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Connection: keep-alive
<blank line>
<!DOCTYPE html>
<html>...
```

### HTTP Status Codes (🎯 MEMORIZE)

| Code | Category | Examples |
|------|----------|----------|
| **1xx** | Informational | 100 Continue |
| **2xx** | Success | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| **5xx** | Server Error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

### HTTP Caching

```
Cache-Control: max-age=3600    (Cache for 1 hour)
Cache-Control: no-cache        (Revalidate before use)
Cache-Control: no-store        (Don't cache at all)
ETag: "abc123"                 (Resource version)
If-None-Match: "abc123"        (Conditional request)
```

### Cookies

```
Server → Client:  Set-Cookie: session_id=abc123; Path=/; HttpOnly
Client → Server:  Cookie: session_id=abc123

Purpose:
- Session management
- User preferences
- Tracking
```

### HTTPS

- HTTP over TLS/SSL
- **Port 443**
- Encrypts data in transit
- Authenticates server

---

## 6.4 FTP (File Transfer Protocol)

### Characteristics

- **Two connections**: Control (21) + Data (20)
- **Stateful**: Remembers current directory
- **Text-based**: Commands in ASCII

### FTP Connection Model

```
       Client                              Server
         │                                   │
  Control│────────────────────────────────→ │:21
         │       (Commands, responses)       │
         │                                   │
    Data │←────────────────────────────────→ │:20
         │       (File transfers)            │
```

### Active vs Passive FTP

| Mode | Data Connection Initiated By | Firewall Friendly |
|------|------------------------------|-------------------|
| **Active** | Server (to client's port) | No (client needs open port) |
| **Passive** | Client (to server's port) | Yes |

### FTP Commands

| Command | Purpose |
|---------|---------|
| USER | Username |
| PASS | Password |
| LIST | Directory listing |
| RETR | Retrieve (download) |
| STOR | Store (upload) |
| PWD | Print working directory |
| CWD | Change directory |
| QUIT | Disconnect |

---

## 6.5 Email Protocols

### Email System Components

```
         ┌──────────┐        ┌──────────┐
         │  Sender  │        │ Receiver │
         │  (MUA)   │        │  (MUA)   │
         └────┬─────┘        └────┬─────┘
              │                   ↑
         SMTP │              POP3/IMAP
              ↓                   │
         ┌──────────┐        ┌──────────┐
         │ Sender's │  SMTP  │Receiver's│
         │  Mail    ├───────→│  Mail    │
         │  Server  │        │  Server  │
         └──────────┘        └──────────┘

MUA = Mail User Agent (Outlook, Gmail)
MTA = Mail Transfer Agent (sendmail, postfix)
```

### SMTP (Simple Mail Transfer Protocol)

- **Port 25** (or 587 for submission)
- **Push protocol** (sender pushes to server)
- **TCP-based**
- **7-bit ASCII** originally (MIME for attachments)

```
SMTP Conversation:
S: 220 mail.example.com SMTP ready
C: HELO client.example.com
S: 250 Hello client.example.com
C: MAIL FROM:<sender@example.com>
S: 250 OK
C: RCPT TO:<recipient@example.org>
S: 250 OK
C: DATA
S: 354 Start mail input
C: Subject: Hello
C: 
C: This is the body.
C: .
S: 250 OK: Message queued
C: QUIT
S: 221 Bye
```

### POP3 (Post Office Protocol v3)

- **Port 110** (995 for POP3S)
- **Pull protocol** (client pulls from server)
- **Download and delete** (typically)
- Simple, limited features

### IMAP (Internet Message Access Protocol)

- **Port 143** (993 for IMAPS)
- **Pull protocol**
- **Keep on server** (synchronize)
- Folders, search, partial fetch
- More complex than POP3

### POP3 vs IMAP

| Feature | POP3 | IMAP |
|---------|------|------|
| Messages | Downloaded, deleted | Stay on server |
| Folders | No | Yes |
| Search | Client-side | Server-side |
| Multiple devices | Poor | Excellent |
| Offline access | Full | Partial |
| Complexity | Simple | Complex |

### MIME (Multipurpose Internet Mail Extensions)

Extends email for:
- Non-ASCII text
- Attachments
- Multiple parts

```
Content-Type: multipart/mixed; boundary="boundary123"

--boundary123
Content-Type: text/plain

Plain text message.

--boundary123
Content-Type: application/pdf
Content-Disposition: attachment; filename="doc.pdf"
Content-Transfer-Encoding: base64

JVBERi0xLjQKJe...
--boundary123--
```

---

## 6.6 DHCP (Dynamic Host Configuration Protocol)

### Purpose

Automatically configure network settings:
- IP address
- Subnet mask
- Default gateway
- DNS servers
- Lease time

### DHCP Process (DORA)

```
         Client                              Server
            │                                   │
            │──────── DISCOVER ────────────────→│ (Broadcast)
            │         "Need an IP!"             │
            │                                   │
            │←─────── OFFER ───────────────────│ (Unicast/Broadcast)
            │         "Here's 192.168.1.50"    │
            │                                   │
            │──────── REQUEST ─────────────────→│ (Broadcast)
            │         "I'll take 192.168.1.50" │
            │                                   │
            │←─────── ACK ─────────────────────│ (Unicast/Broadcast)
            │         "Confirmed!"             │
            │                                   │
```

### DHCP Messages

| Message | Purpose | Src IP | Dst IP |
|---------|---------|--------|--------|
| DISCOVER | Find DHCP servers | 0.0.0.0 | 255.255.255.255 |
| OFFER | Offer IP address | Server IP | 255.255.255.255 or Client |
| REQUEST | Request offered IP | 0.0.0.0 | 255.255.255.255 |
| ACK | Confirm assignment | Server IP | 255.255.255.255 or Client |
| NAK | Deny request | Server IP | 255.255.255.255 |
| RELEASE | Release IP | Client IP | Server IP |
| INFORM | Request config (has IP) | Client IP | Server IP |

### DHCP Ports

- **Server**: UDP 67
- **Client**: UDP 68

### DHCP Lease

```
Lease Time = T
T1 = 0.5 × T (renewal time, unicast to server)
T2 = 0.875 × T (rebinding time, broadcast)

Example: T = 8 hours
  T1 = 4 hours (try to renew)
  T2 = 7 hours (broadcast if renewal failed)
```

### DHCP Relay

For different subnets:
```
[Client] ─── [Router/Relay] ─── [DHCP Server]
              ↓
       Forwards DHCP to
       configured server
```

---

## 6.7 Telnet and SSH

### Telnet

- **Port 23**
- **Unencrypted** (passwords sent in clear)
- Remote terminal access
- **INSECURE - Don't use over internet!**

### SSH (Secure Shell)

- **Port 22**
- **Encrypted** (TLS-like security)
- Remote terminal access
- File transfer (SCP, SFTP)
- Port forwarding/tunneling

```
SSH provides:
- Confidentiality (encryption)
- Integrity (MAC)
- Authentication (password, public key)
```

---

## 6.8 SNMP (Simple Network Management Protocol)

### Purpose

- Monitor network devices
- Configure network devices
- Collect statistics

### SNMP Components

```
┌─────────────────┐
│     Manager     │ (NMS - Network Management Station)
└───────┬─────────┘
        │ SNMP
        │
┌───────┴─────────┐
│     Agent       │ (Running on managed device)
│  ┌─────────┐    │
│  │   MIB   │    │ (Management Information Base)
│  └─────────┘    │
└─────────────────┘
```

### SNMP Operations

| Operation | Direction | Purpose |
|-----------|-----------|---------|
| GET | Manager → Agent | Read single variable |
| GET-NEXT | Manager → Agent | Read next variable (walk) |
| GET-BULK | Manager → Agent | Read multiple variables |
| SET | Manager → Agent | Modify variable |
| TRAP | Agent → Manager | Asynchronous alert |
| INFORM | Agent → Manager | Acknowledged alert |

### SNMP Ports

- **Agent**: UDP 161
- **Trap receiver**: UDP 162

---

## 6.9 Other Application Protocols

### TFTP (Trivial FTP)

- **UDP port 69**
- Simple, no authentication
- Used for booting diskless devices
- Network device configuration

### NTP (Network Time Protocol)

- **UDP port 123**
- Synchronize clocks
- Stratum levels (0-15)

### RDP (Remote Desktop Protocol)

- **TCP port 3389**
- Microsoft remote desktop
- Full graphical interface

### VNC (Virtual Network Computing)

- **TCP port 5900+**
- Cross-platform remote desktop

---

## 6.10 Application Layer Security

### SSL/TLS

```
Application Data
      ↓
┌───────────────┐
│  SSL/TLS      │ (Encryption, Authentication)
├───────────────┤
│     TCP       │
├───────────────┤
│     IP        │
└───────────────┘

TLS Handshake:
1. Client Hello (supported ciphers)
2. Server Hello (chosen cipher, certificate)
3. Key Exchange (pre-master secret)
4. Change Cipher Spec (switch to encrypted)
5. Finished (verify handshake)
```

### Common Secure Protocols

| Protocol | Port | Security |
|----------|------|----------|
| HTTPS | 443 | HTTP over TLS |
| SMTPS | 465 | SMTP over TLS |
| POP3S | 995 | POP3 over TLS |
| IMAPS | 993 | IMAP over TLS |
| FTPS | 990 | FTP over TLS |
| SFTP | 22 | FTP over SSH |

---

## 6.11 Key Points Summary

| Protocol | Port | Transport | Purpose |
|----------|------|-----------|---------|
| DNS | 53 | UDP/TCP | Name resolution |
| HTTP | 80 | TCP | Web |
| HTTPS | 443 | TCP | Secure web |
| FTP Control | 21 | TCP | File transfer |
| FTP Data | 20 | TCP | File transfer |
| SMTP | 25 | TCP | Send email |
| POP3 | 110 | TCP | Retrieve email |
| IMAP | 143 | TCP | Access email |
| DHCP Server | 67 | UDP | IP configuration |
| DHCP Client | 68 | UDP | IP configuration |
| Telnet | 22 | TCP | Remote terminal (insecure) |
| SSH | 22 | TCP | Secure remote terminal |
| SNMP | 161 | UDP | Network management |
| TFTP | 69 | UDP | Simple file transfer |
| NTP | 123 | UDP | Time synchronization |

---

## 🎯 GATE PYQ Patterns

### Pattern 1: DNS Records
**Q**: Which record maps hostname to IP?
**A**: **A record** (AAAA for IPv6)

### Pattern 2: HTTP Methods
**Q**: Which HTTP method is idempotent?
**A**: GET, PUT, DELETE, HEAD (not POST)

### Pattern 3: Email Protocols
**Q**: Protocol to send email?
**A**: **SMTP** (POP3/IMAP to receive)

### Pattern 4: DHCP
**Q**: First message in DHCP?
**A**: **DISCOVER** (DORA sequence)

### Pattern 5: Ports
**Q**: Which port does FTP control use?
**A**: **21** (20 for data)

---

## 📝 Quick Revision Checklist

- [ ] DNS: Hierarchical, A record for IPv4, UDP/TCP 53
- [ ] DNS resolution: Root → TLD → Authoritative
- [ ] HTTP: 1.1 persistent, status codes (2xx success, 4xx client error, 5xx server error)
- [ ] FTP: Two connections (21 control, 20 data)
- [ ] SMTP: Send email, port 25
- [ ] POP3: Download email, port 110
- [ ] IMAP: Access email on server, port 143
- [ ] DHCP: DORA process, UDP 67/68
- [ ] SSH: Secure remote, port 22
- [ ] SNMP: Network management, UDP 161

---

## 🔥 One-Liner Summary

> "Application layer interfaces with users via protocols: DNS (53) resolves names→IPs hierarchically; HTTP (80/443) transfers web with status codes; FTP uses dual connections (21+20); SMTP (25) sends email, POP3/IMAP retrieves; DHCP (67/68) auto-configures IP via DORA; SSH (22) provides encrypted remote access."
