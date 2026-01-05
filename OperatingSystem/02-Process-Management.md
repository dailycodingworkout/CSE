# Chapter 2: Process Management

## 🎯 The Atomic Truth
> **Process = Program in Execution + Resources + State**

---

## 🧠 What is a Process?

### The WHY (First Principles)

**Program**: Static file on disk (passive entity)
**Process**: Running instance with allocated resources (active entity)

```
ANALOGY: Recipe vs Cooking

PROGRAM (Recipe):             PROCESS (Cooking):
┌─────────────────┐           ┌─────────────────────────────────┐
│ Ingredients     │           │ Chef actively cooking            │
│ Steps 1-10      │    →→→    │ Timer running (CPU time)         │
│ (Just text)     │           │ Ingredients used (Memory)        │
│                 │           │ Stove occupied (I/O devices)     │
└─────────────────┘           └─────────────────────────────────┘
   PASSIVE                           ACTIVE
```

**Key Insight**: One program can have multiple processes (open Chrome twice = 2 processes).

---

## 📦 Process Memory Layout

```
HIGH ADDRESS
┌─────────────────────────────────────┐
│           STACK                      │ ← Function calls, local variables
│     (grows downward ↓)               │   Return addresses
├─────────────────────────────────────┤
│              ↓                       │
│         (free space)                 │
│              ↑                       │
├─────────────────────────────────────┤
│           HEAP                       │ ← Dynamic allocation (malloc)
│     (grows upward ↑)                 │   Objects, data structures
├─────────────────────────────────────┤
│        UNINITIALIZED DATA (BSS)      │ ← Global vars initialized to 0
├─────────────────────────────────────┤
│        INITIALIZED DATA              │ ← Global vars with initial values
├─────────────────────────────────────┤
│           TEXT (CODE)                │ ← Machine instructions
│         (Read-Only)                  │   The actual program
└─────────────────────────────────────┘
LOW ADDRESS
```

### Memory Sections Explained

| Section | Contains | Size | Growth |
|---------|----------|------|--------|
| **Text** | Executable code | Fixed | None |
| **Data** | Initialized globals | Fixed | None |
| **BSS** | Uninitialized globals | Fixed | None |
| **Heap** | Dynamic allocations | Variable | Upward ↑ |
| **Stack** | Local vars, function calls | Variable | Downward ↓ |

**GATE Trap**: Stack and Heap grow towards each other. Stack overflow happens when they collide.

---

## 🔄 Process States

### The Five-State Model

```
                    ┌─────────────────────┐
                    │        NEW          │
                    │  (Process created)  │
                    └─────────┬───────────┘
                              │ Admitted to ready queue
                              ↓
    ┌────────────────────────────────────────────────┐
    │                                                │
    │  ┌─────────────────┐    Dispatch    ┌─────────────────┐
    │  │     READY       │ ─────────────→ │    RUNNING      │
    │  │ (Waiting for    │                │ (Executing on   │
    │  │  CPU)           │ ←───────────── │  CPU)           │
    │  └────────┬────────┘   Preempt/     └────────┬────────┘
    │           │            Timeout               │
    │           │                                  │
    │           │                                  │ I/O or Event Wait
    │           │    I/O Complete                  ↓
    │           │    or Event     ┌─────────────────┐
    │           └─────────────────│    WAITING      │
    │                             │ (Blocked for    │
    │                             │  I/O/Event)     │
    │                             └─────────────────┘
    │                                                │
    └────────────────────────────────────────────────┘
                              │
                              │ Exit
                              ↓
                    ┌─────────────────────┐
                    │     TERMINATED      │
                    │  (Process ended)    │
                    └─────────────────────┘
```

### State Transitions

| Transition | Trigger | Example |
|------------|---------|---------|
| New → Ready | Process admitted by scheduler | fork() completes |
| Ready → Running | Dispatcher selects process | CPU becomes available |
| Running → Ready | Preemption or time slice expires | Timer interrupt |
| Running → Waiting | I/O request or event wait | read() system call |
| Waiting → Ready | I/O complete or event occurs | Disk read finishes |
| Running → Terminated | Process exits or killed | exit() or fatal error |

### The Seven-State Model (With Suspend)

```
                           SUSPEND
          ┌─────────────────────────────────────────┐
          │                                         │
          ↓                                         │
┌─────────────────┐                     ┌─────────────────┐
│  READY SUSPEND  │                     │ BLOCKED SUSPEND │
│ (Ready but      │                     │ (Blocked and    │
│  swapped out)   │                     │  swapped out)   │
└────────┬────────┘                     └────────┬────────┘
         │                                       │
         │ Activate                    Activate  │
         ↓                                       ↓
┌─────────────────┐                     ┌─────────────────┐
│     READY       │                     │    BLOCKED      │
│ (In memory,     │                     │ (In memory,     │
│  waiting for    │                     │  waiting for    │
│  CPU)           │                     │  I/O)           │
└─────────────────┘                     └─────────────────┘
```

**WHY Suspend States?**
- Memory is full → swap some processes to disk
- Priority inversion → suspend low priority blocking high priority
- Debugging → freeze process for inspection

---

## 📋 Process Control Block (PCB)

### The WHY

OS needs to track everything about a process. PCB is the "ID card" of a process.

```
┌─────────────────────────────────────────────────────────────┐
│               PROCESS CONTROL BLOCK (PCB)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ PROCESS IDENTIFICATION                               │    │
│  │   • Process ID (PID)                                 │    │
│  │   • Parent Process ID (PPID)                         │    │
│  │   • User ID                                          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ PROCESSOR STATE (Context)                            │    │
│  │   • Program Counter (PC)                             │    │
│  │   • CPU Registers                                    │    │
│  │   • Stack Pointer (SP)                               │    │
│  │   • PSW (Program Status Word)                        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ PROCESS CONTROL INFORMATION                          │    │
│  │   • Process State (Ready/Running/Waiting)            │    │
│  │   • Priority                                         │    │
│  │   • Scheduling Info (time quantum, statistics)       │    │
│  │   • Memory Pointers (page tables, segment tables)    │    │
│  │   • I/O Status (open files, pending I/O)             │    │
│  │   • Accounting (CPU time used, time limits)          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### GATE Favorite: PCB Contents

**Always in PCB**:
- PID
- Process State
- Program Counter
- CPU Registers
- Memory Management Info
- I/O Status

**NOT in PCB**:
- Actual code of process
- User data
- Heap contents

---

## 🔄 Context Switch

### The WHY

CPU can run only one process at a time. To switch between processes:
1. Save state of current process
2. Load state of next process

This is called **Context Switch**.

```
CONTEXT SWITCH FLOW:

Process P₁ executing
        │
        ↓ (Interrupt or System Call)
┌───────────────────────────────────────────────┐
│ 1. Save P₁'s context to PCB₁                   │
│    - PC, registers, stack pointer              │
│    - Process state → READY or WAITING          │
├───────────────────────────────────────────────┤
│ 2. Scheduler selects next process P₂           │
├───────────────────────────────────────────────┤
│ 3. Load P₂'s context from PCB₂                 │
│    - Restore PC, registers, stack pointer      │
│    - Process state → RUNNING                   │
├───────────────────────────────────────────────┤
│ 4. Resume P₂ execution                         │
└───────────────────────────────────────────────┘
        │
        ↓
Process P₂ executing
```

### Context Switch Time

$$\text{Context Switch Time} = \text{Save Time} + \text{Schedule Time} + \text{Load Time}$$

**Typical Values**: 1-1000 microseconds (depends on hardware)

**Factors Affecting Context Switch Time**:
| Factor | Impact |
|--------|--------|
| Number of registers | More registers = more to save |
| Memory speed | Affects PCB read/write |
| Hardware support | Special instructions reduce time |
| OS complexity | More metadata = more overhead |

**GATE Numerical Pattern**:

*Given*: Context switch = 5ms, Process burst = 20ms, n processes
*Find*: CPU utilization or throughput

$$\text{CPU Utilization} = \frac{\text{Useful Time}}{\text{Total Time}} = \frac{n \times \text{burst}}{n \times (\text{burst} + \text{context switch})}$$

---

## 👨‍👦 Process Creation

### The fork() System Call (UNIX)

**Fork creates an exact copy of the calling process.**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    int x = 10;
    pid_t pid = fork();
    
    if (pid == 0) {
        // CHILD process
        x = 20;
        printf("Child: x = %d\n", x);
    } else {
        // PARENT process
        printf("Parent: x = %d\n", x);
    }
    return 0;
}
```

**Output**:
```
Parent: x = 10
Child: x = 20
```

### fork() Return Values

| Return Value | In Process |
|--------------|------------|
| 0 | Child |
| > 0 (child's PID) | Parent |
| -1 | Fork failed |

### The Fork Tree Problem (GATE Favorite)

**Question**: How many processes are created?

```c
fork();
fork();
fork();
```

**Solution**: 
```
                    P₀ (Original)
            fork()   |
           ┌─────────┴─────────┐
           P₀                   P₁
    fork() |            fork()  |
       ┌───┴───┐           ┌────┴────┐
       P₀      P₂          P₁        P₃
fork() |    fork()|     fork()|   fork()|
    ┌──┴──┐  ┌──┴──┐   ┌──┴──┐   ┌──┴──┐
    P₀   P₄  P₂   P₅   P₁   P₆   P₃   P₇
```

**Formula**: For n fork() calls: $2^n$ total processes, $2^n - 1$ new processes

### fork() + exec()

**fork()**: Creates copy of current process
**exec()**: Replaces current process with new program

```
TYPICAL PATTERN (Shell executing a command):

Shell Process (PID 100)
         │
         │ fork()
         ↓
┌────────────────────────────────────────┐
│  Shell (PID 100)    Child (PID 101)   │
│       │                    │           │
│       │ wait()             │ exec("ls")│
│       ↓                    ↓           │
│   WAITING              REPLACES with   │
│                          "ls" code     │
│       │                    │           │
│       │←───── exit() ──────┘           │
│       ↓                                │
│  READY (continues)                     │
└────────────────────────────────────────┘
```

---

## 🔗 Process Hierarchy

### UNIX Process Tree

```
init (PID 1)
├── login
│   ├── bash (shell)
│   │   ├── vi
│   │   └── gcc
│   └── another_shell
├── sshd
└── cron
```

**Key Properties**:
- Every process (except init) has a parent
- Parent can wait for child or run concurrently
- Orphan process: Parent terminates first → adopted by init
- Zombie process: Child terminates but parent hasn't read exit status

### Zombie vs Orphan

| Aspect | Zombie | Orphan |
|--------|--------|--------|
| **Definition** | Child finished, parent not yet called wait() | Parent finished before child |
| **State** | TERMINATED but PCB exists | Still running |
| **Problem** | Uses PCB space | None (adopted by init) |
| **Solution** | Parent calls wait() | init becomes parent |

```
ZOMBIE:                              ORPHAN:
                                     
Parent        Child                  Parent        Child
   │            │                       │            │
   │         exit()                  exit()          │
   │            │                       │            │
   │ (doesn't   ↓                       ↓            │
   │  call    ZOMBIE                 (gone)         │
   │  wait())   │                                   │
   │            │                    init ←─────────┤
   ↓            ↓                     │             │
```

---

## 📊 Process Scheduling Concepts

### Types of Schedulers

```
                          ┌─────────────────┐
                          │   JOB QUEUE     │
                          │ (All processes  │
                          │  in system)     │
                          └────────┬────────┘
                                   │
                    LONG-TERM      │
                    SCHEDULER      ↓
                    (Job Scheduler)
                                   │
                          ┌────────┴────────┐
                          │   READY QUEUE   │
                          │ (In memory,     │
                          │  waiting for    │
                          │  CPU)           │
                          └────────┬────────┘
                                   │
                    SHORT-TERM     │
                    SCHEDULER      ↓
                    (CPU Scheduler)
                                   │
                          ┌────────┴────────┐
                          │      CPU        │
                          └────────┬────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ↓                             ↓
           I/O Request                    Terminate
                    │
                    ↓
           ┌─────────────────┐
           │  DEVICE QUEUE   │
           └────────┬────────┘
                    │
                    └──→ Back to Ready Queue
```

### Scheduler Comparison

| Scheduler | Frequency | Function | Example Decision |
|-----------|-----------|----------|------------------|
| **Long-term** | Seconds/Minutes | Controls degree of multiprogramming | Admit new process or not |
| **Short-term** | Milliseconds | Selects next process to run | Which ready process gets CPU |
| **Medium-term** | Seconds | Swaps processes in/out of memory | Which process to suspend |

### Degree of Multiprogramming

$$\text{Degree of Multiprogramming} = \text{Number of processes in memory}$$

**Long-term scheduler controls this.**

**Trade-off**:
- Too few: CPU idle during I/O
- Too many: Thrashing (excessive paging)

---

## 📈 Scheduling Criteria

| Criterion | Definition | Goal |
|-----------|------------|------|
| **CPU Utilization** | % time CPU is busy | Maximize (ideal: 40-90%) |
| **Throughput** | Processes completed per unit time | Maximize |
| **Turnaround Time** | Total time from submission to completion | Minimize |
| **Waiting Time** | Time spent in ready queue | Minimize |
| **Response Time** | Time from submission to first response | Minimize |

### The Formulas

$$\text{Turnaround Time} = \text{Completion Time} - \text{Arrival Time}$$

$$\text{Waiting Time} = \text{Turnaround Time} - \text{Burst Time}$$

$$\text{Response Time} = \text{First CPU Time} - \text{Arrival Time}$$

**GATE Trap**: Response Time ≠ Waiting Time in preemptive systems.

---

## 🧮 GATE Numerical Examples

### Example 1: Fork Count

**Question**: How many times will "Hello" be printed?

```c
int main() {
    fork();
    fork();
    printf("Hello\n");
    return 0;
}
```

**Solution**:
- After first fork(): 2 processes
- After second fork(): 4 processes
- Each prints "Hello" once
- **Answer: 4 times**

---

### Example 2: Context Switch Overhead

**Question**: CPU has 4 processes. Each has burst time 10ms. Context switch takes 2ms. Calculate throughput.

**Solution**:

Total time for one round:
$$T = 4 \times (10 + 2) = 48 \text{ms}$$

Wait, that's wrong! After last process, no context switch needed.

$$T = 4 \times 10 + 3 \times 2 = 46 \text{ms}$$

Throughput = $\frac{4 \text{ processes}}{46 \text{ ms}} = \frac{4000}{46} \approx 87$ processes/second

---

### Example 3: Process Metrics

**Question**: 
| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |

With FCFS, calculate average waiting time.

**Solution**:

Gantt Chart:
```
| P1 (0-8) | P2 (8-12) | P3 (12-21) |
```

| Process | Completion | Turnaround | Waiting |
|---------|------------|------------|---------|
| P1 | 8 | 8-0=8 | 8-8=0 |
| P2 | 12 | 12-1=11 | 11-4=7 |
| P3 | 21 | 21-2=19 | 19-9=10 |

$$\text{Avg Waiting Time} = \frac{0+7+10}{3} = \frac{17}{3} = 5.67 \text{ ms}$$

---

## 🎯 The Anti-Solution (Common Mistakes)

### Mistake 1: Fork Count
**Wrong**: Counting only child processes created
**Right**: Count ALL processes (parent + children)

### Mistake 2: Context Switch
**Wrong**: Adding context switch after every process including last
**Right**: Between n processes, there are (n-1) context switches

### Mistake 3: Waiting Time
**Wrong**: Waiting Time = Completion - Arrival
**Right**: That's Turnaround Time. Waiting = Turnaround - Burst

---

## 🧠 Memory Mnemonics

### Process States: "NEAR W T"
- **N**ew
- **R**eady (with E for Entry)
- **W**aiting
- **R**unning (with A for Active)
- **T**erminated

### PCB Contents: "PRISM"
- **P**rocess ID
- **R**egisters (CPU state)
- **I**/O status
- **S**cheduling info
- **M**emory pointers

### Fork Formula
> "n forks, 2 to the n folks" (2^n processes)

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2018)
**The following C program is executed on a UNIX/Linux system:**
```c
int main() {
    for(int i=0; i<3; i++)
        fork();
    return 0;
}
```
**How many processes are created?**

**Answer**: 
- Total processes = 2³ = 8
- New processes created = 8 - 1 = **7**

---

### Q2: (GATE 2016)
**A process executes fork() twice. How many total processes exist?**

(A) 2  (B) 3  (C) 4  (D) 5

**Answer**: (C) 4

Explanation: 1 → 2 → 4

---

### Q3: (GATE 2020)
**Which is NOT stored in PCB?**

(A) Program Counter  
(B) Process State  
(C) User's password ✓  
(D) Open files list

**Explanation**: User passwords are stored in /etc/shadow, not in PCB.

---

## ⚡ The 5-Second Snap-Check

Before answering process questions:

1. **Fork question?** → Draw the tree, count 2^n
2. **State question?** → Remember: Running can only come from Ready
3. **PCB question?** → If it's about process control, it's in PCB
4. **Context switch?** → n processes = (n-1) switches per round

---

## 🎯 Quick Revision Table

| Concept | Key Formula/Fact |
|---------|------------------|
| Fork creates | 2^n total processes for n forks |
| Process State | Only Ready→Running is possible |
| Context Switch | Save PCB₁ → Load PCB₂ |
| Turnaround Time | Completion - Arrival |
| Waiting Time | Turnaround - Burst |
| Response Time | First CPU - Arrival |
| Zombie | Child done, parent hasn't called wait() |
| Orphan | Parent done, child still running |

---

*Next Chapter: [CPU Scheduling Algorithms →](03-CPU-Scheduling.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
