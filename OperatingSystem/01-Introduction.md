# Chapter 1: Introduction to Operating Systems

## 🎯 The Atomic Truth
> **OS = Resource Manager + Extended Machine**

---

## 🧠 What is an Operating System?

### The WHY (First Principles)

Imagine you're at a restaurant:
- **Hardware** = Kitchen, stoves, ingredients
- **Applications** = Your food order
- **OS** = The restaurant manager

Without the manager:
- Chefs fight over stoves
- Customers wait forever
- Ingredients get wasted
- Chaos ensues

**The OS is the invisible manager that makes everything work efficiently.**

### Formal Definition

$$\text{Operating System} = \text{Hardware Abstraction} + \text{Resource Management}$$

| Role | What it Does | Why it Matters |
|------|-------------|----------------|
| **Abstraction** | Hides hardware complexity | Programmers don't need assembly for every device |
| **Arbitration** | Manages resource conflicts | Multiple programs can run without crashing |
| **Isolation** | Separates processes | One buggy app can't crash the system |

---

## 📊 Computer System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    USER LEVEL                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Browser  │ │  Editor  │ │  Games   │ │ Compiler │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├────────────────────────────────────────────────────────────┤
│                  SYSTEM PROGRAMS                            │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │  Shell   │ │ Compiler │ │  Loader  │                    │
│  └──────────┘ └──────────┘ └──────────┘                    │
├────────────────────────────────────────────────────────────┤
│                 OPERATING SYSTEM                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              KERNEL (Core of OS)                      │  │
│  │  Process | Memory | File | Device | Security         │  │
│  └──────────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────────┤
│                     HARDWARE                                │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │   CPU    │ │  Memory  │ │   Disk   │ │ Devices  │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Types of Operating Systems

### 1. Batch Operating System

**The Problem it Solved**: In 1950s, computers were expensive. Human operators were slow.

**The Solution**: Collect similar jobs, process them in batches.

```
JOB FLOW:
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Job 1   │    │ Job 2   │    │ Job 3   │
│ (FORTRAN)│    │(FORTRAN)│    │(FORTRAN)│
└────┬────┘    └────┬────┘    └────┬────┘
     └──────────────┼──────────────┘
                    ↓
           ┌────────────────┐
           │ BATCH (FORTRAN)│
           │   All Jobs     │
           └────────────────┘
```

| Advantage | Disadvantage |
|-----------|--------------|
| Reduces setup time | No user interaction |
| Efficient for large jobs | Long turnaround time |
| No idle time between jobs | Hard to debug |

**GATE Trap**: Batch OS doesn't mean sequential execution. It means grouped processing.

---

### 2. Time-Sharing (Multitasking) OS

**The Problem**: Users want interactive computing. Batch system = wait for hours.

**The Solution**: Give each user a small time slice. Switch rapidly (illusion of dedicated computer).

```
TIME QUANTUM SWITCHING:
┌────────────────────────────────────────────────────────┐
│ User1 │ User2 │ User3 │ User1 │ User2 │ User3 │ ...   │
└────────────────────────────────────────────────────────┘
   10ms    10ms    10ms    10ms    10ms    10ms
   
Human perception: Each user feels like they have full computer
```

**Key Metric**: Response Time (time to first output)

$$\text{Response Time} = \text{Time to first interaction}$$

**Example**: UNIX, Linux, Windows

---

### 3. Real-Time Operating System (RTOS)

**The Problem**: Some tasks have deadlines. Missing them = disaster.

**The Solution**: Guarantee task completion within time bounds.

| Type | Deadline Miss | Example |
|------|---------------|---------|
| **Hard RTOS** | System failure | Airbag controller, Pacemaker |
| **Soft RTOS** | Quality degradation | Video streaming, Gaming |

**The Mental Model**:
```
Hard RTOS:  Deadline = "I will die if missed"
Soft RTOS:  Deadline = "I will be annoyed if missed"
```

**GATE Favorite Question**: 
> "Which is NOT a hard real-time system?"
> 
> (A) Missile guidance  
> (B) Heart pacemaker  
> (C) Video conferencing ✓  
> (D) Nuclear reactor control

---

### 4. Distributed Operating System

**The Problem**: Single machine has limits (processing, storage, reliability).

**The Solution**: Multiple autonomous computers appear as single system.

```
┌─────────────────────────────────────────────────────────┐
│                   DISTRIBUTED OS                         │
├─────────┬─────────┬─────────┬─────────┬────────────────┤
│ Node 1  │ Node 2  │ Node 3  │ Node 4  │  ... Node N    │
│ (Delhi) │(Mumbai) │(Chennai)│ (Kolkata)│               │
└─────────┴─────────┴─────────┴─────────┴────────────────┘
          Connected via Network (appears as ONE system)
```

**Key Properties**:
- **Transparency**: User doesn't see distribution
- **Fault Tolerance**: Node failure doesn't crash system
- **Scalability**: Add nodes to increase power

---

### 5. Comparison Table (GATE Favorite)

| Feature | Batch | Time-Sharing | Real-Time | Distributed |
|---------|-------|--------------|-----------|-------------|
| User Interaction | None | High | Varies | High |
| Response Time | Hours | Seconds | Milliseconds | Seconds |
| Main Goal | Throughput | Responsiveness | Deadline | Resource Sharing |
| Example | Payroll | UNIX | VxWorks | Google's Borg |

---

## 🔧 Operating System Structure

### 1. Simple/Monolithic Structure

**Everything in one big kernel.**

```
┌─────────────────────────────────────────┐
│              APPLICATION                │
├─────────────────────────────────────────┤
│          MONOLITHIC KERNEL              │
│  ┌─────────────────────────────────┐    │
│  │ Process │ Memory │ File │ I/O   │    │
│  │ Mgmt    │ Mgmt   │ Sys  │ Mgmt  │    │
│  └─────────────────────────────────┘    │
├─────────────────────────────────────────┤
│              HARDWARE                   │
└─────────────────────────────────────────┘
```

| Pros | Cons |
|------|------|
| Fast (no mode switches) | Hard to debug |
| Simple design | One bug crashes all |
| Efficient communication | Hard to maintain |

**Example**: Early UNIX, MS-DOS

---

### 2. Layered Structure

**OS as onion layers. Each layer uses only layer below.**

```
┌─────────────────────────────────────────┐
│  Layer N: User Interface                │
├─────────────────────────────────────────┤
│  Layer N-1: User Programs               │
├─────────────────────────────────────────┤
│  Layer ...                              │
├─────────────────────────────────────────┤
│  Layer 2: Memory Management             │
├─────────────────────────────────────────┤
│  Layer 1: CPU Scheduling                │
├─────────────────────────────────────────┤
│  Layer 0: Hardware                      │
└─────────────────────────────────────────┘
```

| Pros | Cons |
|------|------|
| Easy to debug | Slower (layer traversal) |
| Easy to maintain | Hard to define layers |
| Modularity | Overhead in layer crossing |

**THE Theorem**: Layer N can only use services of Layer 0 to N-1.

**Example**: THE OS by Dijkstra

---

### 3. Microkernel Structure

**Minimal kernel. Everything else in user space.**

```
┌─────────────────────────────────────────────────────────┐
│ USER SPACE                                              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │ File    │ │ Device  │ │ Network │ │ Process │       │
│  │ Server  │ │ Driver  │ │ Stack   │ │ Server  │       │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘       │
├─────────────────────────────────────────────────────────┤
│                   MICROKERNEL                            │
│  ┌─────────────────────────────────────────────────┐    │
│  │   IPC   │   Memory   │   Basic Scheduling       │    │
│  └─────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│                     HARDWARE                             │
└─────────────────────────────────────────────────────────┘
```

| Pros | Cons |
|------|------|
| Fault isolation | Slower (IPC overhead) |
| Easy to extend | Complex design |
| More secure | Performance penalty |

**Example**: Minix, L4, QNX

---

### 4. Modular Structure (Modern Approach)

**Best of both: Monolithic core + Loadable modules.**

```
┌────────────────────────────────────────────────────────┐
│                      KERNEL                             │
│  ┌──────────────────────────────────────────────────┐  │
│  │              CORE KERNEL                          │  │
│  └──────────────────────────────────────────────────┘  │
│     ↑         ↑         ↑         ↑         ↑         │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐        │
│  │Module│ │Module│ │Module│ │Module│ │Module│        │
│  │ USB  │ │ NTFS │ │ GPU  │ │ WiFi │ │ ...  │        │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘        │
└────────────────────────────────────────────────────────┘
         Modules can be loaded/unloaded dynamically
```

**Example**: Linux, Solaris

---

### 5. Hybrid Structure

**Real-world OS = Mix of everything.**

```
WINDOWS NT ARCHITECTURE:
┌─────────────────────────────────────────────────────────┐
│  USER MODE                                              │
│  ┌─────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │ Win32   │ │ POSIX Subsystem │ │ OS/2 Subsystem  │   │
│  │ Apps    │ │                 │ │                 │   │
│  └─────────┘ └─────────────────┘ └─────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  KERNEL MODE                                            │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Executive │ Kernel │ HAL (Hardware Abstraction) │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│                      HARDWARE                           │
└─────────────────────────────────────────────────────────┘
```

---

## 📞 System Calls

### The WHY

User programs need OS services (file access, memory allocation, etc.).

**Problem**: Direct hardware access = chaos, security holes.

**Solution**: Controlled interface = System Calls.

```
┌─────────────────────────────────────────────────────────┐
│  USER MODE (Ring 3)                                     │
│  ┌─────────────────────────────────────────────────┐   │
│  │  printf("Hello")                                 │   │
│  │       ↓                                          │   │
│  │  write(1, "Hello", 5)  ← System Call Wrapper     │   │
│  └────────────────────────────┬─────────────────────┘   │
│                               │ TRAP (Software Interrupt)│
├───────────────────────────────┼─────────────────────────┤
│  KERNEL MODE (Ring 0)         ↓                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  sys_write() implementation                      │   │
│  │  → Actual hardware I/O                           │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### The Mode Switch

$$\text{User Mode} \xrightarrow{\text{System Call (TRAP)}} \text{Kernel Mode}$$

**Cost**: Mode switch takes ~1000-2000 CPU cycles (expensive!)

---

### Types of System Calls

| Category | Purpose | UNIX Examples | Windows Examples |
|----------|---------|---------------|------------------|
| **Process Control** | Create, terminate processes | fork(), exec(), exit() | CreateProcess(), ExitProcess() |
| **File Management** | Open, read, write files | open(), read(), write() | CreateFile(), ReadFile() |
| **Device Management** | Request/release devices | ioctl(), read(), write() | SetConsoleMode() |
| **Information Maintenance** | Get/set system info | getpid(), alarm(), time() | GetCurrentProcessId() |
| **Communication** | IPC mechanisms | pipe(), shmget(), mmap() | CreatePipe() |
| **Protection** | Permissions, access control | chmod(), chown() | SetFileSecurity() |

---

### System Call Execution Flow

```
STEP-BY-STEP EXECUTION:
                                                    
1. User calls library function (e.g., printf)
        ↓
2. Library function calls system call wrapper
        ↓
3. Parameters placed in registers/stack
        ↓
4. TRAP instruction executed (mode switch)
        ↓
5. System call handler looks up system call number
        ↓
6. Kernel executes actual system call
        ↓
7. Return value placed in register
        ↓
8. Return to user mode
        ↓
9. Library function returns to user
```

### Parameter Passing Methods

| Method | How it Works | Pros | Cons |
|--------|-------------|------|------|
| **Registers** | Parameters in CPU registers | Fast | Limited by register count |
| **Block/Table** | Parameters in memory, address in register | Unlimited params | Extra memory access |
| **Stack** | Push params to stack | Flexible | Stack management overhead |

---

## 🔐 Dual Mode Operation

### Why Two Modes?

**Problem**: What if a user program executes `HLT` (halt CPU)?

**Solution**: Privileged instructions only in kernel mode.

```
┌─────────────────────────────────────────────────────────┐
│                    CPU                                   │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Mode Bit:  0 = Kernel Mode, 1 = User Mode      │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  User Mode (Mode Bit = 1):                               │
│    - Limited instruction set                             │
│    - Cannot access I/O directly                          │
│    - Cannot disable interrupts                           │
│                                                          │
│  Kernel Mode (Mode Bit = 0):                             │
│    - Full instruction set                                │
│    - Direct hardware access                              │
│    - Can modify mode bit                                 │
└─────────────────────────────────────────────────────────┘
```

### Privileged Instructions (Kernel Only)

| Instruction | Why Privileged |
|-------------|---------------|
| I/O operations | Could access any device |
| Set timer | Could disable preemption |
| Clear memory | Could erase other processes |
| Turn off interrupts | Could monopolize CPU |
| Modify page tables | Could access other processes' memory |
| Switch to kernel mode | Would bypass protection |

**GATE Trap**: 
> "Which is NOT a privileged instruction?"
> - ADD, SUB, LOAD are NOT privileged (regular computation)
> - I/O, interrupt control ARE privileged

---

## ⚡ Interrupts and Traps

### The Difference

| Aspect | Interrupt | Trap (Exception) |
|--------|-----------|------------------|
| **Source** | External (hardware) | Internal (software) |
| **Trigger** | I/O completion, timer | System call, error |
| **Synchronous** | No (can occur anytime) | Yes (predictable) |
| **Example** | Keyboard press | Division by zero |

### Interrupt Handling Flow

```
┌─────────────────────────────────────────────────────────┐
│ 1. Interrupt signal received                            │
│         ↓                                               │
│ 2. CPU completes current instruction                    │
│         ↓                                               │
│ 3. Save state (PC, registers) to stack                  │
│         ↓                                               │
│ 4. Switch to kernel mode                                │
│         ↓                                               │
│ 5. Look up ISR address in Interrupt Vector Table        │
│         ↓                                               │
│ 6. Execute Interrupt Service Routine (ISR)              │
│         ↓                                               │
│ 7. Restore saved state                                  │
│         ↓                                               │
│ 8. Return to interrupted program                        │
└─────────────────────────────────────────────────────────┘
```

### Interrupt Vector Table

```
┌────────────────────────────────────────────────────────┐
│  INTERRUPT VECTOR TABLE                                 │
├─────────┬──────────────────────────────────────────────┤
│ Vector  │ Handler Address                               │
├─────────┼──────────────────────────────────────────────┤
│ 0       │ 0x00001000 (Division by Zero Handler)        │
│ 1       │ 0x00001100 (Debug Exception)                  │
│ ...     │ ...                                           │
│ 32      │ 0x00002000 (Timer Interrupt)                  │
│ 33      │ 0x00002100 (Keyboard Interrupt)               │
│ ...     │ ...                                           │
│ 128     │ 0x00005000 (System Call Handler) - Linux     │
└─────────┴──────────────────────────────────────────────┘
```

---

## 🧮 GATE Numerical: System Call Overhead

### Problem Pattern

**Question**: A system call takes 500 cycles to execute. Mode switch takes 200 cycles. A program makes 1000 system calls. If CPU runs at 2 GHz, what is the total overhead time?

**Solution**:

$$\text{Per system call overhead} = 2 \times \text{mode switch} + \text{execution}$$
$$= 2 \times 200 + 500 = 900 \text{ cycles}$$

$$\text{Total cycles} = 1000 \times 900 = 900,000 \text{ cycles}$$

$$\text{Time} = \frac{900,000}{2 \times 10^9} = 450 \times 10^{-6} \text{ seconds} = 450 \mu s$$

**The Trap**: Don't forget there are TWO mode switches (user→kernel AND kernel→user).

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2017)
**Which of the following is NOT a function of the OS?**

(A) Memory management  
(B) Disk scheduling  
(C) Compiler design ✓  
(D) Process scheduling

**Explanation**: Compiler is a system program, not part of OS.

---

### Q2: (GATE 2015)
**Which of the following is a privileged instruction?**

(A) ADD R1, R2  
(B) LOAD R1, M[1000]  
(C) Set timer value ✓  
(D) STORE R1, M[1000]

**Explanation**: Timer manipulation affects system scheduling.

---

### Q3: (GATE 2019)
**Microkernel architecture puts which of the following in user space?**

(A) Basic scheduling  
(B) IPC  
(C) File system ✓  
(D) Memory management

**Explanation**: Microkernel keeps only essential services (IPC, basic memory) in kernel.

---

## 🎯 Quick Revision: The Mental Slider

### Slider 1: Kernel Size vs Performance

```
MINIMAL KERNEL ◄────────────────────────► MAXIMAL KERNEL
  (Microkernel)                             (Monolithic)
      │                                          │
      ▼                                          ▼
  More Secure                              Faster
  More Stable                              Simpler
  Slower                                   Less Secure
```

### Slider 2: User-Kernel Boundary

```
MORE IN USER SPACE ◄──────────────────► MORE IN KERNEL
      │                                      │
      ▼                                      ▼
  More IPC calls                      Fewer mode switches
  Better isolation                    Better performance
  Example: Minix                      Example: Linux
```

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| OS Definition | Resource manager + Hardware abstraction |
| Batch OS | No interaction, maximize throughput |
| Time-sharing | Illusion of dedicated computer |
| RTOS | Deadlines matter (hard vs soft) |
| Monolithic | Fast but fragile |
| Microkernel | Safe but slow |
| System Call | Controlled OS service access |
| Dual Mode | Protection via privilege levels |
| Interrupts | Async events, hardware-triggered |
| Traps | Sync events, software-triggered |

---

## ⚡ The 5-Second Snap-Check

Before marking an answer about OS structure:

1. **Is it about protection?** → Think mode bits
2. **Is it about performance?** → Think mode switches
3. **Is it about reliability?** → Think kernel size
4. **Is it about I/O?** → Think interrupts

---

*Next Chapter: [Process Management →](02-Process-Management.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
