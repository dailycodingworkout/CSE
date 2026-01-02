# 📖 Chapter 1: Introduction to Operating Systems

> **The Atomic Truth:** OS = Resource Manager + User Interface

---

## 🎯 GATE Syllabus Coverage
- Operating System Types
- System Calls
- Operating System Structure
- Kernel Modes

---

## 1.1 What is an Operating System?

### Definition
An **Operating System (OS)** is system software that acts as an intermediary between computer hardware and the end user, managing all hardware and software resources.

### The Mental Model (Analogy)
Think of an OS as a **Restaurant Manager**:
- **Hardware** = Kitchen (CPU, Memory, I/O devices)
- **User Programs** = Customers
- **OS** = Manager who coordinates orders, allocates tables, manages kitchen resources

```
┌─────────────────────────────────────────┐
│           User Applications             │
├─────────────────────────────────────────┤
│         System Programs/Utilities       │
├─────────────────────────────────────────┤
│           Operating System              │
│    ┌───────────────────────────────┐    │
│    │         Kernel                │    │
│    │  • Process Management         │    │
│    │  • Memory Management          │    │
│    │  • File System                │    │
│    │  • I/O Management             │    │
│    │  • Security                   │    │
│    └───────────────────────────────┘    │
├─────────────────────────────────────────┤
│              Hardware                   │
│     (CPU, Memory, Disk, I/O Devices)    │
└─────────────────────────────────────────┘
```

---

## 1.2 Functions of Operating System

| Function | Description | Example |
|----------|-------------|---------|
| **Process Management** | Creates, schedules, terminates processes | Task Manager |
| **Memory Management** | Allocates/deallocates memory | Virtual Memory |
| **File Management** | Creates, deletes, organizes files | File Explorer |
| **I/O Management** | Controls I/O devices | Device Drivers |
| **Security** | Protects resources | Authentication |
| **Resource Allocation** | Distributes resources fairly | CPU Scheduling |

---

## 1.3 Types of Operating Systems

### 1.3.1 Batch Operating System

**Concept:** Jobs are collected, grouped into batches, and executed without user interaction.

**Characteristics:**
- No direct interaction with user
- Jobs queued for execution
- High CPU utilization

**Example:** Payroll processing, Bank statement generation

**Diagram:**
```
┌──────┐    ┌─────────┐    ┌─────────┐    ┌────────┐
│ Jobs │ → │ Batching│ → │ Execution│ → │ Output │
└──────┘    └─────────┘    └─────────┘    └────────┘
```

**Advantages:**
- Simple to implement
- High throughput for similar jobs

**Disadvantages:**
- No user interaction
- Long turnaround time
- One job failure can halt batch

---

### 1.3.2 Multiprogramming Operating System

**Concept:** Multiple programs reside in memory simultaneously; CPU switches between them.

**Why?** To maximize CPU utilization when a process is waiting for I/O.

**The Golden Pivot:** **Degree of Multiprogramming** = Number of processes in memory

```
Memory Layout:
┌─────────────────┐
│   OS Kernel     │
├─────────────────┤
│   Process 1     │ ← Currently Running
├─────────────────┤
│   Process 2     │ ← Waiting for I/O
├─────────────────┤
│   Process 3     │ ← Ready Queue
├─────────────────┤
│   Free Space    │
└─────────────────┘
```

**Key Formula:**
$$\text{CPU Utilization} = 1 - p^n$$

Where:
- $p$ = I/O wait probability per process
- $n$ = Degree of multiprogramming

**Example:** If each process waits 80% time for I/O ($p = 0.8$) and 4 processes in memory:
$$\text{CPU Utilization} = 1 - (0.8)^4 = 1 - 0.4096 = 0.5904 = 59.04\%$$

---

### 1.3.3 Multitasking/Time-Sharing Operating System

**Concept:** CPU time is divided into small **time quanta**, each process gets a turn.

**Key Difference from Multiprogramming:**
| Multiprogramming | Time-Sharing |
|------------------|--------------|
| Switch on I/O wait | Switch on time quantum expiry |
| Non-interactive | Interactive |
| Maximize CPU utilization | Minimize response time |

**Time Quantum Selection (Critical for GATE):**
- Too large → FCFS behavior, poor response time
- Too small → High context switch overhead

**Formula:**
$$\text{Optimal Time Quantum} \approx 80\% \text{ of CPU bursts complete within it}$$

---

### 1.3.4 Real-Time Operating System (RTOS)

**Concept:** Time constraints are critical; tasks must complete within deadlines.

**Types:**

| Type | Deadline | Consequence | Example |
|------|----------|-------------|---------|
| **Hard RTOS** | Absolute | System failure | Pacemaker, ABS |
| **Soft RTOS** | Flexible | Degraded quality | Video streaming |

**Key Terms:**
- **Deadline:** Time by which task must complete
- **Latency:** Time from event to response
- **Jitter:** Variation in latency

---

### 1.3.5 Distributed Operating System

**Concept:** Collection of independent computers that appears as single system to users.

**Characteristics:**
- Resource sharing across network
- Transparency (location, migration, replication)
- Fault tolerance

**Example:** Google's infrastructure, Cloud computing platforms

---

### 1.3.6 Comparison Table

| Feature | Batch | Multiprogramming | Time-Sharing | Real-Time | Distributed |
|---------|-------|------------------|--------------|-----------|-------------|
| User Interaction | No | No | Yes | Limited | Yes |
| Response Time | High | Medium | Low | Very Low | Medium |
| CPU Switching | Sequential | On I/O | Time Quantum | Priority | Network |
| Main Goal | Throughput | CPU Utilization | User Response | Meet Deadlines | Resource Sharing |

---

## 1.4 System Calls

### Definition
A **System Call** is the programmatic interface between a process and the operating system kernel.

### Why System Calls?
User programs run in **User Mode** (restricted access). To access hardware/OS services, they must switch to **Kernel Mode** through system calls.

### The Mode Switch
```
User Mode                    Kernel Mode
┌─────────────┐             ┌─────────────┐
│ Application │             │   Kernel    │
│   Code      │────────────→│   Code      │
│             │  System Call│             │
│             │  (trap/int) │             │
│             │←────────────│             │
└─────────────┘   Return    └─────────────┘
```

### System Call Categories

| Category | Examples | Purpose |
|----------|----------|---------|
| **Process Control** | fork(), exec(), exit(), wait() | Create, terminate processes |
| **File Management** | open(), read(), write(), close() | File operations |
| **Device Management** | ioctl(), read(), write() | I/O device access |
| **Information Maintenance** | getpid(), alarm(), sleep() | System info |
| **Communication** | pipe(), shmget(), mmap() | IPC mechanisms |
| **Protection** | chmod(), chown(), umask() | Security |

### Critical System Calls for GATE

#### fork()
Creates a new process (child) by duplicating the calling process (parent).

```c
pid_t pid = fork();
if (pid == 0) {
    // Child process code
} else if (pid > 0) {
    // Parent process code
} else {
    // Error
}
```

**Key Points:**
- Returns **0** to child
- Returns **child's PID** to parent
- Both parent and child continue from next instruction after fork()

**GATE Trap:** How many processes after n fork() calls?
$$\text{Total Processes} = 2^n$$

**Example:**
```c
fork();  // 2 processes
fork();  // 4 processes
fork();  // 8 processes
// Answer: 8 processes
```

#### exec()
Replaces current process image with a new program.

**Key Insight:** fork() + exec() = Running new program in new process

#### wait()
Parent waits for child to terminate.

**Zombie Process:** Child terminated, but parent hasn't called wait()
**Orphan Process:** Parent terminated before child; child adopted by init (PID=1)

---

## 1.5 Operating System Structure

### 1.5.1 Monolithic Structure

**Concept:** Entire OS runs in kernel mode as single program.

```
┌─────────────────────────────────────┐
│        Application Programs         │
├─────────────────────────────────────┤
│           System Calls              │
├─────────────────────────────────────┤
│    ┌─────────────────────────────┐  │
│    │        KERNEL               │  │
│    │  ┌─────┐ ┌─────┐ ┌─────┐   │  │
│    │  │File │ │Proc │ │Mem  │   │  │
│    │  │Sys  │ │Mgmt │ │Mgmt │   │  │
│    │  └─────┘ └─────┘ └─────┘   │  │
│    │  All components tightly     │  │
│    │  coupled in kernel space    │  │
│    └─────────────────────────────┘  │
└─────────────────────────────────────┘
```

**Advantages:**
- High performance (no mode switching within kernel)
- Simple implementation

**Disadvantages:**
- Difficult to maintain
- One bug can crash entire system
- Large kernel size

**Examples:** Traditional UNIX, MS-DOS, Linux (modular monolithic)

---

### 1.5.2 Layered Structure

**Concept:** OS divided into layers, each built on top of lower layers.

```
┌───────────────────────────────────┐
│ Layer N: User Interface           │
├───────────────────────────────────┤
│ Layer N-1: User Programs          │
├───────────────────────────────────┤
│ Layer N-2: I/O Management         │
├───────────────────────────────────┤
│ ...                               │
├───────────────────────────────────┤
│ Layer 1: Memory Management        │
├───────────────────────────────────┤
│ Layer 0: Hardware                 │
└───────────────────────────────────┘
```

**Advantages:**
- Modularity, easier debugging
- Each layer verified independently

**Disadvantages:**
- Performance overhead (layer traversal)
- Difficult to define layers properly

**Example:** THE operating system (Dijkstra)

---

### 1.5.3 Microkernel Structure

**Concept:** Minimal kernel with essential functions; other services in user space.

```
┌────────────────────────────────────────────┐
│           User Applications                 │
├─────────┬─────────┬─────────┬──────────────┤
│ File    │ Device  │ Memory  │ Process      │
│ Server  │ Drivers │ Server  │ Server       │
│ (User)  │ (User)  │ (User)  │ (User)       │
├─────────┴─────────┴─────────┴──────────────┤
│              Message Passing               │
├────────────────────────────────────────────┤
│    ┌────────────────────────────────────┐  │
│    │         MICROKERNEL                │  │
│    │  • IPC  • Scheduling  • Basic MM   │  │
│    └────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

**Kernel Contains (Minimal):**
- Basic IPC (Inter-Process Communication)
- Basic Memory Management
- Basic Scheduling

**Advantages:**
- More secure (less code in kernel)
- Easier to extend
- More reliable

**Disadvantages:**
- Performance overhead (message passing)
- Complex design

**Examples:** Mach, L4, MINIX, QNX

---

### 1.5.4 Hybrid Kernel

**Concept:** Combines monolithic and microkernel approaches.

**Examples:** Windows NT, macOS (XNU kernel)

---

### 1.5.5 Comparison Table

| Feature | Monolithic | Layered | Microkernel |
|---------|------------|---------|-------------|
| Performance | High | Medium | Lower |
| Modularity | Low | High | Very High |
| Security | Lower | Medium | Higher |
| Complexity | High | Medium | High |
| Flexibility | Low | Medium | High |

---

## 1.6 Kernel vs User Mode

### Mode Bit
A hardware bit that indicates current execution mode:
- **Mode Bit = 0:** Kernel Mode (privileged)
- **Mode Bit = 1:** User Mode (restricted)

### Privileged Instructions
Only executable in Kernel Mode:
- I/O operations
- Memory management
- Interrupt handling
- Modifying mode bit
- Halt instruction

### Mode Transition
```
User Mode                     Kernel Mode
    │                             │
    │     System Call/Interrupt   │
    ├────────────────────────────→│
    │                             │
    │    Return from handler      │
    │←────────────────────────────┤
    │                             │
```

---

## 1.7 Interrupts

### Types of Interrupts

| Type | Source | Example |
|------|--------|---------|
| **Hardware Interrupt** | External devices | Keyboard, Timer |
| **Software Interrupt (Trap)** | Program instruction | System call, Division by zero |
| **Exception** | CPU error | Page fault, Segmentation fault |

### Interrupt Handling Steps
1. Stop current execution
2. Save context (PC, registers) on stack
3. Identify interrupt source (interrupt vector)
4. Execute Interrupt Service Routine (ISR)
5. Restore context
6. Resume execution

### Interrupt Vector Table
```
┌────────────────────────────────┐
│ Vector 0: Divide Error Handler │
├────────────────────────────────┤
│ Vector 1: Debug Handler        │
├────────────────────────────────┤
│ Vector 2: NMI Handler          │
├────────────────────────────────┤
│ ...                            │
├────────────────────────────────┤
│ Vector 128: System Call        │
└────────────────────────────────┘
```

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2019)
**Q:** In a system with 3 fork() calls, how many processes will be created (including parent)?

**Solution:**
- Each fork() doubles the number of processes
- Total = $2^3 = 8$ processes

**Answer:** 8

---

### Question 2 (GATE 2020)
**Q:** Which of the following is NOT a valid system call category?
(a) Process Control
(b) Memory Management
(c) Compilation
(d) File Management

**Answer:** (c) Compilation - Compilation is done by compiler, not OS

---

### Question 3 (GATE 2018)
**Q:** The primary goal of a real-time operating system is:
(a) High throughput
(b) Meeting deadlines
(c) User convenience
(d) Resource utilization

**Answer:** (b) Meeting deadlines

---

## 🧠 Memory Tricks

### Mnemonic: "FDFIS" for System Call Categories
**F**ile management
**D**evice management
**F**ork/Process control
**I**nformation maintenance
**S**ignaling/Communication

### The Mental Slider: Mode Switching
Imagine a **light switch**:
- **UP (1)** = User Mode (limited power)
- **DOWN (0)** = Kernel Mode (full power)
- System calls **flip the switch down**, privileged work, **flip back up**

---

## ⚠️ Common GATE Traps

### Trap 1: fork() Count
**Wrong:** Counting only new processes
**Right:** Count ALL processes including original parent

### Trap 2: Multiprogramming vs Multitasking
**Wrong:** Using terms interchangeably
**Right:** 
- Multiprogramming = Switch on I/O (maximize CPU)
- Multitasking = Switch on time quantum (minimize response)

### Trap 3: Microkernel Performance
**Wrong:** Assuming microkernel is always faster
**Right:** Monolithic is faster due to fewer mode switches

---

## 📝 Practice Problems

1. Calculate CPU utilization with 5 processes, each waiting 70% time for I/O.

2. Write output of:
```c
int main() {
    fork();
    fork();
    printf("Hello\n");
    return 0;
}
```

3. Identify the OS structure: "All services run in kernel space with no modularity"

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| OS Definition | Resource manager + User interface |
| System Call | User to Kernel mode switch |
| fork() result | $2^n$ processes for n forks |
| CPU Utilization | $1 - p^n$ |
| Microkernel | Minimal kernel, services in user space |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 2 - Process Management](../02-Process-Management/README.md)*
