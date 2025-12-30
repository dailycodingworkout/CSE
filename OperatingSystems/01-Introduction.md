# Chapter 1: Introduction to Operating Systems

> **"The OS is like a restaurant manager - it doesn't cook food (run programs), but ensures every table (process) gets served efficiently"**

---

## 🎯 What is an Operating System?

An **Operating System (OS)** is system software that acts as an intermediary between users and computer hardware.

### Core Functions (The 4 Pillars)

| Function | Description | Real-World Analogy |
|----------|-------------|-------------------|
| **Resource Manager** | Allocates CPU, memory, I/O devices | Traffic controller at intersection |
| **Process Manager** | Creates, schedules, terminates processes | HR department managing employees |
| **Memory Manager** | Allocates and tracks memory usage | Warehouse manager allocating storage |
| **File Manager** | Organizes and manages files | Librarian organizing books |

---

## 🏗️ OS Structure Types

### 1. Monolithic Structure
```
┌─────────────────────────────────────────┐
│              User Space                  │
├─────────────────────────────────────────┤
│         Single Large Kernel             │
│  (All services in one address space)    │
└─────────────────────────────────────────┘
```

**Characteristics:**
- All OS services run in kernel space
- Fast (no IPC overhead)
- Less reliable (one bug crashes everything)

**Examples:** MS-DOS, early UNIX

**💡 Trick:** Monolithic = "Mono" = One = Everything in one place

---

### 2. Layered Structure
```
┌─────────────────────────────────────┐
│  Layer N: User Interface           │
├─────────────────────────────────────┤
│  Layer N-1: Device Drivers         │
├─────────────────────────────────────┤
│  ...                               │
├─────────────────────────────────────┤
│  Layer 1: Memory Management        │
├─────────────────────────────────────┤
│  Layer 0: Hardware                 │
└─────────────────────────────────────┘
```

**Key Rule:** Layer N can ONLY call Layer N-1 (not N-2 or below)

**Pros:** Easy debugging, modular  
**Cons:** Slow (multiple layer crossings), difficult to define layers

**Example:** THE (Technische Hogeschool Eindhoven) OS

**🧠 Analogy:** Like a corporate hierarchy - you can only talk to your immediate boss

---

### 3. Microkernel Structure
```
┌────────────────────────────────────────────────┐
│            User Space                          │
│  ┌─────────┐  ┌─────────┐  ┌─────────────┐    │
│  │ File    │  │ Device  │  │ Process     │    │
│  │ Server  │  │ Drivers │  │ Server      │    │
│  └────┬────┘  └────┬────┘  └──────┬──────┘    │
├───────┼────────────┼───────────────┼───────────┤
│       └────────────┼───────────────┘           │
│               Microkernel                      │
│   (IPC, Basic Scheduling, Memory Protection)  │
└────────────────────────────────────────────────┘
```

**What stays in kernel?**
- Inter-Process Communication (IPC)
- Basic memory management
- Basic CPU scheduling

**What moves to user space?**
- File systems
- Device drivers
- Network protocols

**Pros:** Reliable (crash in user space doesn't crash OS), secure  
**Cons:** Performance overhead due to IPC

**Examples:** Mach, L4, Minix, QNX

**💡 GATE Trick:** Microkernel = Minimal kernel = Only essential services

---

### 4. Modular Structure (Modern Approach)
```
         ┌──────────────┐
         │ Loadable     │
         │ Kernel       │──────┐
         │ Modules      │      │
         └──────────────┘      ▼
              ▲          ┌─────────────┐
              │          │   Core      │
              └──────────│   Kernel    │
                         └─────────────┘
```

**Key Feature:** Modules can be loaded/unloaded dynamically at runtime

**Best of both worlds:**
- Monolithic efficiency (no IPC)
- Microkernel flexibility (modular)

**Examples:** Linux, Solaris

---

### 5. Hybrid Kernel
Combines monolithic and microkernel approaches.

**Examples:** Windows NT, macOS (XNU kernel)

---

## 🔄 System Calls

### What is a System Call?

A **system call** is the programmatic way a program requests a service from the OS kernel.

```
User Program  ──────►  System Call  ──────►  Kernel
              (trap instruction)
```

### Types of System Calls

| Category | Examples | Purpose |
|----------|----------|---------|
| **Process Control** | fork(), exec(), exit(), wait() | Create/manage processes |
| **File Management** | open(), read(), write(), close() | File operations |
| **Device Management** | ioctl(), read(), write() | Device I/O |
| **Information Maintenance** | getpid(), time(), sleep() | System info |
| **Communication** | pipe(), shmget(), mmap() | IPC |
| **Protection** | chmod(), chown(), umask() | Security |

### System Call Execution Flow

```
1. User program calls library function (e.g., printf())
2. Library function sets up system call number and parameters
3. Trap instruction executed (switches to kernel mode)
4. Kernel executes system call handler
5. Result returned to user program
```

**🧠 Analogy:** System call is like pressing a service button in a hotel - you can't go to the kitchen yourself (kernel), but you can request room service (system call).

---

## 🔀 Operating System Operations

### Dual Mode Operation

```
┌────────────────────────────────────────┐
│           USER MODE (Mode bit = 1)     │
│         User programs execute here     │
├────────────────────────────────────────┤
│ ↓↓↓ System Call / Interrupt ↓↓↓        │
├────────────────────────────────────────┤
│          KERNEL MODE (Mode bit = 0)    │
│          Full hardware access          │
└────────────────────────────────────────┘
```

**Why Dual Mode?**
- Protect OS from errant users
- Protect users from each other

**Mode Bit:**
- 0 = Kernel mode (privileged)
- 1 = User mode (restricted)

**Privileged Instructions (Only in Kernel Mode):**
- I/O instructions
- Halt instruction
- Interrupt enable/disable
- Timer management
- Memory management

**⚠️ GATE Trap:** Switching from user to kernel mode happens via:
- System calls (software interrupt/trap)
- Interrupts (hardware)
- Exceptions (errors like divide-by-zero)

---

### Timer & Interrupts

**Timer Purpose:** Prevent infinite loops and resource hogging

```
Timer expires → Interrupt → Control returns to OS
```

**Types of Interrupts:**

| Type | Cause | Example |
|------|-------|---------|
| Hardware Interrupt | External device | Keyboard press |
| Software Interrupt (Trap) | Program instruction | System call |
| Exception | Error condition | Division by zero |

---

## 📊 OS Services vs OS Interface

### Operating System Services (What OS provides)

```
┌───────────────────────────────────────────────────────────┐
│                    User Interface                          │
│                  (CLI, GUI, Batch)                        │
├─────────────┬─────────────┬─────────────┬─────────────────┤
│ Program     │ I/O         │ File System │ Communications  │
│ Execution   │ Operations  │ Manipulation│                 │
├─────────────┴─────────────┴─────────────┴─────────────────┤
│     Error Detection  │  Resource Allocation              │
├──────────────────────┴────────────────────────────────────┤
│         Accounting   │  Protection & Security            │
└───────────────────────────────────────────────────────────┘
```

---

## ⏱️ Types of Operating Systems

### 1. Batch OS
- Jobs submitted in batches
- No user interaction during execution
- **Metric:** Throughput (jobs/time)

### 2. Time-Sharing (Multitasking) OS
- CPU time shared among multiple users
- Quick response time
- Uses time quantum/time slice
- **Metric:** Response time

### 3. Real-Time OS (RTOS)

| Type | Deadline | Example |
|------|----------|---------|
| **Hard Real-Time** | Must meet (failure = system failure) | Flight control, pacemaker |
| **Soft Real-Time** | Should meet (degraded performance OK) | Video streaming, gaming |

**💡 GATE Trick:** 
- Hard = "Hardware-critical" = life/safety critical
- Soft = "Software services" = quality degradation acceptable

### 4. Distributed OS
- Multiple computers appear as single system
- Resource sharing across network

### 5. Embedded OS
- Designed for specific hardware
- Limited resources, optimized

### 6. Network OS
- Provides network services
- Each computer retains its identity

---

## 🖥️ Virtual Machines

### Concept
```
┌─────────────────────────────────────────────┐
│  App A  │  App B  │  App C  │  App D        │
├─────────┼─────────┼─────────┼───────────────┤
│  VM 1   │  VM 2   │  VM 3   │  VM 4         │
│  (Win)  │ (Linux) │ (macOS) │  (BSD)        │
├─────────┴─────────┴─────────┴───────────────┤
│              Hypervisor (VMM)               │
├─────────────────────────────────────────────┤
│            Physical Hardware                │
└─────────────────────────────────────────────┘
```

### Types of Hypervisors

| Type | Name | Location | Examples |
|------|------|----------|----------|
| **Type 1** | Bare-metal | Directly on hardware | VMware ESXi, Xen, Hyper-V |
| **Type 2** | Hosted | On top of host OS | VirtualBox, VMware Workstation |

**Benefits:**
- Isolation (security)
- Multiple OS on one machine
- Testing environments

---

## 🔧 Bootstrap & System Boot

### Boot Process
```
1. Power ON
2. BIOS/UEFI runs (in ROM)
3. POST (Power-On Self-Test)
4. Boot loader loaded from boot sector
5. Boot loader loads kernel
6. Kernel initializes system
7. Init/systemd starts user processes
```

**Bootstrap Program:**
- Stored in ROM/EEPROM
- Initializes CPU registers, memory
- Locates and loads OS kernel

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **System call classification** - Which category does X belong to?
2. **Kernel types comparison** - Microkernel vs Monolithic
3. **Mode switching** - When does mode change occur?
4. **Privileged instructions** - What can only run in kernel mode?

### ⚠️ Edge Cases & Traps:
1. **Timer is a privileged instruction** - Only OS can set it
2. **System call changes mode from user to kernel** (not vice versa)
3. **Interrupt handler runs in kernel mode**
4. **fork() is a system call, not a library function**

---

## 🎯 Quick Revision Points

```
✓ OS = Resource Manager + Extended Machine
✓ Dual Mode = Protection mechanism
✓ Mode bit: 0 = Kernel, 1 = User
✓ System call = User to Kernel transition
✓ Microkernel = Minimal services in kernel
✓ Monolithic = All services in kernel
✓ Type-1 hypervisor = Bare-metal (faster)
✓ Type-2 hypervisor = Hosted (slower)
✓ Hard RT = Deadline mandatory
✓ Soft RT = Deadline preferred
```

---

## 📚 Key Formulas

```
CPU Utilization (with I/O probability p and n processes):
U = 1 - p^n

System Call Overhead:
Total Time = User Time + (n × System Call Time)
where n = number of system calls
```

---

[Next Chapter: Process Management →](./02-Process-Management.md)
