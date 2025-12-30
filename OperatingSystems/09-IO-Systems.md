# Chapter 9: I/O Systems

> **"I/O systems are like a restaurant's kitchen communication system - orders (requests) must be efficiently routed between dining room (CPU) and kitchen (devices)"**

---

## 🎯 I/O Hardware Basics

### Device Categories

| Category | Examples | Characteristics |
|----------|----------|-----------------|
| **Block Devices** | Disk, SSD, USB | Fixed-size blocks, random access |
| **Character Devices** | Keyboard, mouse, serial port | Byte stream, sequential |
| **Network Devices** | NIC, WiFi adapter | Packet-based |

---

### Device Controller

```
┌────────────────────────────────────────────────────────┐
│                    Computer                            │
│                                                        │
│   ┌─────────┐      ┌──────────────────┐               │
│   │   CPU   │◄────►│  I/O Controller  │◄───► Device   │
│   └─────────┘      │   - Registers    │               │
│                    │   - Buffer       │               │
│                    │   - Logic        │               │
│                    └──────────────────┘               │
└────────────────────────────────────────────────────────┘
```

**Controller Registers:**
- **Data register:** Data transfer
- **Status register:** Device state (ready, busy, error)
- **Command register:** Instructions to device

---

### I/O Port Addresses

**Port-Mapped I/O:**
```
Special instructions: in/out
Example: 
  out 0x21, al  ; Write to port 0x21
  in al, 0x60   ; Read from port 0x60
```

**Memory-Mapped I/O:**
```
Device registers at memory addresses
Example:
  mov [0xB8000], ax  ; Write to video memory
```

| Aspect | Port-Mapped | Memory-Mapped |
|--------|-------------|---------------|
| Address space | Separate | Shared with RAM |
| Instructions | Special (in/out) | Regular (mov) |
| Protection | Privileged only | Via page tables |

---

## 🔄 I/O Techniques

### 1️⃣ Programmed I/O (Polling)

```
CPU                           Device
 │                              │
 ├──── Check status ───────────►│
 │◄─── Status: busy ────────────┤
 ├──── Check status ───────────►│
 │◄─── Status: busy ────────────┤
 ├──── Check status ───────────►│
 │◄─── Status: ready ───────────┤
 ├──── Send data ──────────────►│
 │                              │
```

```c
while (device_status != READY)
    ;  // Busy wait
device_data = data;
```

**Problem:** CPU wastes cycles polling

**Use Case:** Simple systems, fast devices

---

### 2️⃣ Interrupt-Driven I/O

```
CPU                           Device
 │                              │
 ├──── Start I/O ──────────────►│
 │                              │
 │ (CPU does other work)        │
 │                              │
 │◄──── Interrupt ──────────────┤
 │                              │
 ├──── Handle interrupt ───────►│
 │     (transfer data)          │
```

**Interrupt Handling Steps:**
1. Device raises interrupt
2. CPU finishes current instruction
3. CPU saves context (PC, registers)
4. CPU jumps to interrupt handler
5. Handler services device
6. CPU restores context
7. CPU resumes original task

---

### Interrupt Priority

```
┌────────────────────────────────────────┐
│  High Priority (Non-maskable)          │
│    - Power failure                     │
│    - Memory error                      │
├────────────────────────────────────────┤
│  Medium Priority                       │
│    - Timer                             │
│    - Disk                              │
├────────────────────────────────────────┤
│  Low Priority                          │
│    - Keyboard                          │
│    - Mouse                             │
└────────────────────────────────────────┘
```

**Interrupt Vector Table:**
```
Vector 0:  Divide error handler address
Vector 1:  Debug exception handler
...
Vector 32: Timer interrupt handler
Vector 33: Keyboard interrupt handler
...
```

---

### 3️⃣ Direct Memory Access (DMA)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   ┌─────────┐                           ┌────────────────┐  │
│   │   CPU   │──────────────────────────►│    Memory      │  │
│   └─────────┘                           └────────────────┘  │
│        │                                       ▲            │
│        │ 1. Setup DMA                          │            │
│        ▼                                       │            │
│   ┌─────────────┐                              │            │
│   │    DMA      │──────────────────────────────┘            │
│   │ Controller  │   2. Transfer data                        │
│   └─────────────┘   directly                                │
│        │                                                    │
│        │ 3. Interrupt when done                             │
│        ▼                                                    │
│   ┌─────────────┐                                           │
│   │   Device    │                                           │
│   └─────────────┘                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**DMA Steps:**
1. CPU sets up DMA: source, destination, count
2. DMA controller transfers data
3. DMA sends interrupt when complete
4. CPU gets interrupt, confirms completion

**Advantage:** CPU free during transfer
**Disadvantage:** Memory bus contention (cycle stealing)

---

### DMA Transfer Modes

| Mode | Description |
|------|-------------|
| **Burst** | DMA takes bus until transfer complete |
| **Cycle Stealing** | DMA takes one cycle, releases, repeats |
| **Transparent** | DMA uses bus only when CPU not using |

---

### Comparison

| Technique | CPU Involvement | Speed | Complexity |
|-----------|-----------------|-------|------------|
| Polling | Continuous | Slow | Simple |
| Interrupt | Start + End | Medium | Medium |
| DMA | Setup + End | Fast | Complex |

---

## 🖥️ Kernel I/O Subsystem

### I/O Scheduling

**Goal:** Optimize device access order

```
Disk requests: 98, 183, 37, 122, 14, 124, 65, 67
Current head: 53

Without scheduling: Service in arrival order (inefficient)
With scheduling: Optimize seek time (SSTF, SCAN, etc.)
```

---

### Buffering

**Why Buffer?**
1. Speed mismatch (fast CPU, slow device)
2. Size mismatch (different block sizes)
3. Copy semantics (preserve data during transfer)

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│  User   │◄─►│ User    │◄─►│ Kernel  │◄─►│ Device  │
│ Process │   │ Buffer  │   │ Buffer  │   │         │
└─────────┘   └─────────┘   └─────────┘   └─────────┘
                    Double buffering
```

**Buffer Types:**
- **Single buffer:** One buffer, alternating fill/empty
- **Double buffer:** Two buffers, one filling while other emptying
- **Circular buffer:** Multiple buffers in ring

---

### Caching

**Cache vs Buffer:**

| Aspect | Cache | Buffer |
|--------|-------|--------|
| Purpose | Speed up repeated access | Hold data temporarily |
| Data | May be copy | Only copy |
| Operations | Read mostly | Read and write |

**Buffer cache:** Caches disk blocks in memory

---

### Spooling

**SPOOL:** Simultaneous Peripheral Operations On-Line

```
Process 1 ──►┐
Process 2 ──►├──► Spool Queue ──► Printer
Process 3 ──►┘
```

**Use Case:** Devices that can't be multiplexed (printers)

---

### Error Handling

```
I/O Error Types:
┌────────────────────────────────────────────────┐
│ Transient  │ Retry may succeed (network timeout)│
│ Permanent  │ Retry won't help (disk bad sector) │
│ Protocol   │ Invalid request                    │
└────────────────────────────────────────────────┘
```

**Handling Strategy:**
1. Retry for transient errors
2. Return error code to caller
3. Log for analysis

---

## 🔌 I/O Device Drivers

### Driver Structure

```
┌────────────────────────────────────────────────────────────┐
│                    User Application                        │
├────────────────────────────────────────────────────────────┤
│                    System Call Interface                   │
├────────────────────────────────────────────────────────────┤
│                    I/O Subsystem                          │
├───────────────┬───────────────┬───────────────┬───────────┤
│ Disk Driver   │ Net Driver    │ USB Driver    │ ...       │
├───────────────┼───────────────┼───────────────┼───────────┤
│ Disk          │ Network Card  │ USB Device    │ ...       │
└───────────────┴───────────────┴───────────────┴───────────┘
```

### Driver Functions

```c
// Character device driver operations
struct file_operations {
    int (*open)(struct inode *, struct file *);
    int (*release)(struct inode *, struct file *);
    ssize_t (*read)(struct file *, char __user *, size_t, loff_t *);
    ssize_t (*write)(struct file *, const char __user *, size_t, loff_t *);
    int (*ioctl)(struct inode *, struct file *, unsigned int, unsigned long);
};
```

---

## ⏰ Timer and Clock

### Hardware Timers

```
┌────────────────────────────────────────────────────────────┐
│                    Timer Hardware                          │
│                                                            │
│   Counter ────────► Comparator ────────► Interrupt         │
│                         ▲                                  │
│                         │                                  │
│                    Threshold                               │
└────────────────────────────────────────────────────────────┘
```

**Uses:**
- Time of day
- Process time accounting
- CPU scheduling (preemption)
- Alarm/timeout

---

### Clock Types

| Type | Purpose | Precision |
|------|---------|-----------|
| **Real-Time Clock** | Time of day | Seconds |
| **High-Resolution Timer** | Performance measurement | Nanoseconds |
| **Interval Timer** | Periodic events | Milliseconds |

---

## 🔄 Blocking vs Non-blocking I/O

### Blocking (Synchronous)

```
Process                    Device
   │                          │
   ├──── read() ─────────────►│
   │ (Process sleeps)         │
   │                          │
   │◄──── data ───────────────┤
   │ (Process wakes)          │
   │                          │
```

**Process blocks until I/O completes**

---

### Non-blocking (Asynchronous)

```
Process                    Device
   │                          │
   ├──── read() ─────────────►│
   │◄──── returns immediately─┤
   │ (with partial or no data)│
   │                          │
   │ (Process continues)      │
   │                          │
   │◄──── callback/signal ────┤
   │      (data ready)        │
```

**Returns immediately, notifies when ready**

---

### I/O Models

| Model | Description | Use Case |
|-------|-------------|----------|
| **Blocking** | Wait for completion | Simple apps |
| **Non-blocking** | Return immediately | Polling apps |
| **I/O Multiplexing** | select()/poll() on multiple fds | Servers |
| **Signal-driven** | Signal on readiness | Event-driven |
| **Asynchronous** | Complete async with callback | High-performance |

---

### select() / poll() / epoll()

```c
// Monitor multiple file descriptors
fd_set readfds;
FD_ZERO(&readfds);
FD_SET(socket_fd, &readfds);
FD_SET(stdin_fd, &readfds);

select(max_fd + 1, &readfds, NULL, NULL, &timeout);

if (FD_ISSET(socket_fd, &readfds)) {
    // Socket has data
}
```

**Comparison:**

| Mechanism | Scalability | Notification |
|-----------|-------------|--------------|
| select() | O(n) | Level-triggered |
| poll() | O(n) | Level-triggered |
| epoll() | O(1) | Level/Edge-triggered |

---

## 🔁 I/O Request Lifecycle

```
1. User issues I/O call (read/write)
         │
         ▼
2. System call → Kernel mode
         │
         ▼
3. I/O subsystem validates request
         │
         ▼
4. Device driver translates to device commands
         │
         ▼
5. Device controller executes operation
         │
         ▼
6. Interrupt signals completion
         │
         ▼
7. Driver handles interrupt
         │
         ▼
8. Data transferred to user buffer
         │
         ▼
9. Process unblocked
         │
         ▼
10. System call returns
```

---

## ⚡ Performance Considerations

### Reducing I/O Latency

1. **Caching:** Keep frequently used data in memory
2. **Buffering:** Batch small I/Os
3. **DMA:** Free CPU during transfers
4. **Asynchronous I/O:** Overlap I/O with computation
5. **Read-ahead:** Prefetch sequential data

---

### I/O Performance Metrics

| Metric | Definition |
|--------|------------|
| **Throughput** | Data transferred per unit time |
| **Latency** | Time for single operation |
| **IOPS** | I/O operations per second |
| **Utilization** | Fraction of time device busy |

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **DMA vs Interrupt vs Polling:** Compare
2. **Interrupt handling:** Steps and timing
3. **I/O scheduling:** (Covered in Disk chapter)
4. **Memory-mapped vs Port I/O:** Differences

### ⚠️ Edge Cases:
1. **DMA uses CPU bus cycles** (cycle stealing)
2. **Interrupt has context switch overhead**
3. **Polling good for fast, predictable devices**
4. **Spooling creates device independence**

---

## 🎯 Quick Revision Points

```
✓ Block device = random access (disk)
✓ Character device = sequential (keyboard)
✓ Polling = CPU continuously checks status
✓ Interrupt = Device notifies CPU
✓ DMA = Device transfers directly to memory
✓ Buffer = Temporary holding area
✓ Cache = Speed up repeated access
✓ Spooling = Queue for non-shareable devices
✓ Blocking I/O = Process waits
✓ Non-blocking I/O = Process continues
```

---

## 📚 Key Concepts

```
Interrupt handling time = 
  Context save + Handler execution + Context restore

DMA transfer time = 
  Setup time + (Data size / Transfer rate) + Interrupt handling

Effective I/O time with buffering:
  Max(CPU processing time, I/O time) per request
  vs. (CPU + I/O) per request without buffering
```

---

[← Previous: File Systems](./08-File-Systems.md) | [Next: Disk Management →](./10-Disk-Management.md)
