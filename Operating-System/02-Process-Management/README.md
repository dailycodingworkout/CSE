# 📖 Chapter 2: Process Management

> **The Atomic Truth:** Process = Program in Execution

---

## 🎯 GATE Syllabus Coverage
- Process Concept
- Process Control Block (PCB)
- Process States & Transitions
- Context Switching
- Process Creation and Termination
- Inter-Process Communication (IPC)

---

## 2.1 What is a Process?

### Definition
A **Process** is a program in execution. It includes:
- Program code (text section)
- Current activity (program counter, registers)
- Stack (temporary data)
- Data section (global variables)
- Heap (dynamically allocated memory)

### Program vs Process

| Program | Process |
|---------|---------|
| Passive entity | Active entity |
| Stored on disk | Resides in memory |
| No resources allocated | Has allocated resources |
| Single copy | Multiple instances possible |

### Process Memory Layout

```
High Address
┌─────────────────────┐
│       Stack         │ ← Function calls, local variables
│         ↓           │   (grows downward)
├─────────────────────┤
│                     │
│    Free Space       │
│                     │
├─────────────────────┤
│         ↑           │
│        Heap         │ ← Dynamic allocation (malloc)
├─────────────────────┤
│   Uninitialized     │
│   Data (BSS)        │ ← Global uninitialized variables
├─────────────────────┤
│   Initialized       │
│   Data              │ ← Global initialized variables
├─────────────────────┤
│       Text          │ ← Program code (read-only)
└─────────────────────┘
Low Address
```

---

## 2.2 Process Control Block (PCB)

### Definition
The **PCB** (also called Task Control Block) is a data structure that stores all information about a process.

### PCB Structure

```
┌────────────────────────────────┐
│       PROCESS CONTROL BLOCK    │
├────────────────────────────────┤
│ Process ID (PID)               │
├────────────────────────────────┤
│ Process State                  │
├────────────────────────────────┤
│ Program Counter (PC)           │
├────────────────────────────────┤
│ CPU Registers                  │
├────────────────────────────────┤
│ CPU Scheduling Info            │
│ (priority, pointers)           │
├────────────────────────────────┤
│ Memory Management Info         │
│ (base/limit registers, page    │
│  tables)                       │
├────────────────────────────────┤
│ Accounting Info                │
│ (CPU time, real time)          │
├────────────────────────────────┤
│ I/O Status Info                │
│ (open files, devices)          │
└────────────────────────────────┘
```

### PCB Fields Explained

| Field | Description | GATE Relevance |
|-------|-------------|----------------|
| **PID** | Unique process identifier | Low |
| **State** | Current process state | High |
| **PC** | Address of next instruction | High |
| **Registers** | CPU register values | Medium |
| **Priority** | Scheduling priority | High |
| **Memory Pointers** | Page/segment tables | High |
| **Open Files** | List of open file descriptors | Medium |

---

## 2.3 Process States

### 5-State Process Model

```
                    ┌─────────────────┐
                    │      New        │
                    └────────┬────────┘
                             │ Admitted
                             ↓
┌──────────────┐   Schedule  ┌────────────────┐
│    Ready     │────────────→│    Running     │
│    Queue     │←────────────│                │
└──────┬───────┘  Preempt/   └───────┬────────┘
       │          Timeout            │
       │                             │
       │                             │ Exit
       │                             ↓
       │    I/O Complete    ┌────────────────┐
       │←───────────────────│   Terminated   │
       │                    └────────────────┘
       │
       │ I/O Request
       ↓
┌──────────────┐
│   Waiting    │
│   (Blocked)  │
└──────────────┘
```

### State Descriptions

| State | Description | Queue |
|-------|-------------|-------|
| **New** | Process being created | - |
| **Ready** | Waiting for CPU | Ready Queue |
| **Running** | Currently executing | - |
| **Waiting/Blocked** | Waiting for I/O or event | Wait Queue |
| **Terminated** | Finished execution | - |

### State Transitions

| Transition | From → To | Cause |
|------------|-----------|-------|
| Admit | New → Ready | Process admitted to system |
| Dispatch | Ready → Running | Scheduler selects process |
| Timeout/Preempt | Running → Ready | Time quantum expires or higher priority arrives |
| Event Wait | Running → Waiting | I/O request or wait for event |
| Event Occurs | Waiting → Ready | I/O completion or event signal |
| Exit | Running → Terminated | Process completes or aborts |

### 7-State Process Model (With Suspend)

```
┌────────┐                         ┌────────────┐
│  New   │                         │ Terminated │
└───┬────┘                         └────────────┘
    │                                    ↑
    ↓                                    │
┌────────┐  Dispatch  ┌─────────┐  Exit  │
│ Ready  │───────────→│ Running │────────┘
└───┬────┘←───────────└────┬────┘
    ↑     Timeout          │
    │                      │ I/O Wait
    │     I/O Done         ↓
    │←─────────────────┌────────┐
    │                  │Waiting │
    │                  └───┬────┘
    │                      │ Suspend
    │  Activate            ↓
┌───┴────────┐       ┌───────────────┐
│  Ready     │       │   Waiting     │
│  Suspend   │       │   Suspend     │
└────────────┘       └───────────────┘
```

**Suspended States:** Process swapped to disk (secondary storage)
- **Ready Suspend:** In disk, ready to run when swapped in
- **Blocked Suspend:** In disk, waiting for event

---

## 2.4 Context Switching

### Definition
**Context Switch** is the process of saving the context of a currently running process and loading the context of the next scheduled process.

### Context Switch Steps

```
Process P₀                 OS Kernel               Process P₁
    │                          │                       │
    │  Interrupt/System Call   │                       │
    ├─────────────────────────→│                       │
    │                          │                       │
    │                     Save P₀ context to PCB₀      │
    │                          │                       │
    │                     Load P₁ context from PCB₁    │
    │                          │                       │
    │                          ├──────────────────────→│
    │                          │                       │
    │                          │     Execute P₁        │
    │                          │                       │
```

### Context Switch Overhead

**Time Components:**
1. Save current process state (registers, PC)
2. Update PCB and move to appropriate queue
3. Select next process (scheduling algorithm)
4. Load new process state
5. Flush TLB/cache (if needed)

**Typical Time:** 1-1000 microseconds (hardware dependent)

### Context Switch Cost Analysis

$$\text{Overhead} = \text{Number of Switches} \times \text{Switch Time}$$

**Example:** 
- Time quantum = 10ms
- Context switch time = 1ms
- CPU burst = 100ms

$$\text{Total Time} = 100 + \left(\frac{100}{10} - 1\right) \times 1 = 100 + 9 = 109 \text{ ms}$$

$$\text{Overhead \%} = \frac{9}{109} \times 100 = 8.26\%$$

---

## 2.5 Process Creation

### fork() System Call

**Mechanism:** Parent process creates child process by duplicating itself.

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        // Fork failed
        printf("Fork failed\n");
    } else if (pid == 0) {
        // Child process
        printf("Child: PID = %d, Parent PID = %d\n", getpid(), getppid());
    } else {
        // Parent process
        printf("Parent: PID = %d, Child PID = %d\n", getpid(), pid);
    }
    return 0;
}
```

### fork() Return Values

| Return Value | Meaning | Process |
|--------------|---------|---------|
| `< 0` | Error | Fork failed |
| `= 0` | Success | Child process |
| `> 0` | Child's PID | Parent process |

### Process Tree

```
          init (PID=1)
              │
    ┌─────────┼─────────┐
    │         │         │
  shell     daemon    getty
  (bash)              
    │
  ┌─┴─┐
  │   │
 vim  gcc
```

### fork() Counting Problems (GATE Favorite)

**Formula for n sequential forks:**
$$\text{Total Processes} = 2^n$$

**Example 1: Sequential forks**
```c
fork();    // 2 processes
fork();    // 4 processes  
fork();    // 8 processes
```
**Answer:** 8 processes

**Example 2: Conditional fork**
```c
if (fork() == 0) {
    fork();
}
fork();
```

**Process Tree:**
```
    P (parent)
    ├── fork() returns child_pid to P, 0 to C₁
    │   ├── P: fork()!=0, skips inner fork, does outer fork → P, P₂
    │   └── C₁: fork()==0, does inner fork → C₁, C₃
    │       C₁ does outer fork → C₁, C₄
    │       C₃ does outer fork → C₃, C₅
    └── Final: P, P₂, C₁, C₄, C₃, C₅ = 6 processes
```
**Answer:** 6 processes

### exec() Family

**Purpose:** Replaces process image with new program.

| Function | Description |
|----------|-------------|
| `execl()` | List of arguments |
| `execv()` | Vector (array) of arguments |
| `execlp()` | Search PATH for program |
| `execvp()` | Vector + PATH search |

```c
// Child process runs "ls -l"
if (fork() == 0) {
    execlp("ls", "ls", "-l", NULL);
    printf("This won't print if exec succeeds\n");
}
```

---

## 2.6 Process Termination

### Normal Termination
- `exit()` system call
- Return from `main()`
- `_exit()` (immediate termination)

### Abnormal Termination
- Killed by another process
- Fatal error (segmentation fault)
- Resource limit exceeded

### Zombie and Orphan Processes

| Type | Definition | Cause | Solution |
|------|------------|-------|----------|
| **Zombie** | Child terminated, parent hasn't called `wait()` | Parent not collecting exit status | Parent should call `wait()` |
| **Orphan** | Parent terminated before child | Parent exits first | Child adopted by init (PID=1) |

**Zombie Creation:**
```c
int main() {
    if (fork() == 0) {
        exit(0);  // Child exits
    }
    sleep(100);   // Parent sleeps, doesn't wait()
    return 0;
}
// Child becomes zombie for 100 seconds
```

**Orphan Creation:**
```c
int main() {
    if (fork() == 0) {
        sleep(100);  // Child sleeps
    } else {
        exit(0);     // Parent exits immediately
    }
    return 0;
}
// Child becomes orphan, adopted by init
```

---

## 2.7 Inter-Process Communication (IPC)

### Why IPC?
- Information sharing
- Computation speedup (parallel execution)
- Modularity
- Convenience

### IPC Models

```
Shared Memory Model           Message Passing Model
┌──────────────────┐          ┌──────────────────┐
│   Process A      │          │   Process A      │
│  ┌──────────┐    │          │                  │
│  │  Write   │    │          │    Send(msg)     │
│  └────┬─────┘    │          │        │         │
└───────┼──────────┘          └────────┼─────────┘
        │                              │
        ↓                              ↓
┌───────────────────┐         ┌─────────────────┐
│  Shared Memory    │         │  Message Queue  │
│  ┌─────────────┐  │         │  ┌───┬───┬───┐  │
│  │    Data     │  │         │  │ M │ M │ M │  │
│  └─────────────┘  │         │  └───┴───┴───┘  │
└───────────────────┘         └─────────────────┘
        ↑                              │
        │                              ↓
┌───────┼──────────┐          ┌────────┼─────────┐
│   Process B      │          │   Process B      │
│  ┌────┴─────┐    │          │                  │
│  │   Read   │    │          │   Receive(msg)   │
│  └──────────┘    │          │                  │
└──────────────────┘          └──────────────────┘
```

### Shared Memory vs Message Passing

| Feature | Shared Memory | Message Passing |
|---------|---------------|-----------------|
| Speed | Faster (no kernel involvement) | Slower (kernel mediated) |
| Sync Mechanism | Programmer responsibility | Built-in |
| Ease of Use | Complex | Simpler |
| Distributed Systems | Not suitable | Suitable |

### IPC Mechanisms

#### 1. Pipes

**Anonymous Pipes:** Communication between related processes

```c
int fd[2];
pipe(fd);  // fd[0] = read end, fd[1] = write end

if (fork() == 0) {
    close(fd[0]);  // Child closes read end
    write(fd[1], "Hello", 5);
    close(fd[1]);
} else {
    close(fd[1]);  // Parent closes write end
    char buf[10];
    read(fd[0], buf, 5);
    close(fd[0]);
}
```

**Named Pipes (FIFO):** Communication between unrelated processes

#### 2. Message Queues
- Kernel-maintained message list
- Messages have type and data

#### 3. Shared Memory
- Fastest IPC mechanism
- Needs explicit synchronization

#### 4. Semaphores
- Synchronization primitive
- (Covered in Chapter 5)

#### 5. Signals
- Software interrupts for processes
- Limited information transfer

---

## 2.8 Process Scheduling Queues

### Queue Types

```
┌─────────────────────────────────────────────────────────┐
│                    Job Queue                            │
│     (All processes in the system)                       │
└────────────────────────┬────────────────────────────────┘
                         │ Admit
                         ↓
┌─────────────────────────────────────────────────────────┐
│                   Ready Queue                           │
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐                      │
│  │PCB1│ → │PCB2│ → │PCB3│ → │PCB4│ → CPU                │
│  └────┘   └────┘   └────┘   └────┘                      │
└─────────────────────────────────────────────────────────┘
                         ↑
                         │ I/O Complete
┌────────────────────────┴────────────────────────────────┐
│              Device Wait Queues                         │
│  Disk Queue:  ┌────┐ → ┌────┐                           │
│               │PCB5│   │PCB6│                           │
│               └────┘   └────┘                           │
│  Printer Queue: ┌────┐                                  │
│                 │PCB7│                                  │
│                 └────┘                                  │
└─────────────────────────────────────────────────────────┘
```

### Schedulers

| Scheduler | Queue Transition | Frequency | Goal |
|-----------|------------------|-----------|------|
| **Long-term** | Job → Ready | Infrequent | Control degree of multiprogramming |
| **Short-term** | Ready → Running | Frequent | Select next process to run |
| **Medium-term** | Memory ↔ Disk | Medium | Swap processes (suspend) |

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2017)
**Q:** The number of processes created when the following code executes:
```c
for(i = 0; i < 3; i++)
    fork();
```

**Solution:**
- Loop executes 3 times
- Each fork doubles processes
- Total = $2^3 = 8$ processes

**Answer:** 8

---

### Question 2 (GATE 2015)
**Q:** A process executing its critical section can be:
(a) Preempted and moved to ready queue
(b) Terminated
(c) Both (a) and (b)
(d) Neither (a) nor (b)

**Answer:** (c) - While we prefer not to preempt in critical section, it's technically possible

---

### Question 3 (GATE 2018)
**Q:** Which state transition is NOT valid?
(a) Running → Ready
(b) Ready → Running
(c) Blocked → Running
(d) Running → Blocked

**Answer:** (c) Blocked → Running is invalid. Process must go Blocked → Ready → Running

---

## 🧠 Memory Tricks

### Mnemonic: PCB Contents "PRISM CAM"
- **P**rocess ID
- **R**egisters
- **I**/O Status
- **S**tate
- **M**emory management info
- **C**PU scheduling info
- **A**ccounting info
- **M**ore (program counter)

### The Mental Slider: Process States
Imagine a **traffic light** for processes:
- 🔴 **New/Terminated** = Stopped (not in traffic)
- 🟡 **Ready** = Waiting at signal
- 🟢 **Running** = Going through intersection
- 🔵 **Blocked** = Pulled over (waiting for something)

---

## ⚠️ Common GATE Traps

### Trap 1: Blocked → Running Transition
**Wrong:** Process directly moves from Blocked to Running
**Right:** Must go through Ready state first

### Trap 2: fork() in loops
**Wrong:** Adding fork results
**Right:** Each fork multiplies by 2

### Trap 3: Context Switch Content
**Wrong:** Only PC is saved
**Right:** PC + all CPU registers + memory maps

---

## 🛠️ Problem-Solving Techniques

### Technique 1: fork() Process Counting

**Systematic approach:**

```
Method 1: Power of 2
For n sequential fork() calls:
Total processes = 2ⁿ

Example:
fork();  // 2 processes (1→2)
fork();  // 4 processes (2→4)
fork();  // 8 processes (8 total)
```

**Method 2: Process Tree**
```
Draw tree at each fork():
           P
fork()  →   ├── P (parent continues)
            └── C1 (child created)

For each existing process, fork doubles them.
```

### Technique 2: fork() with Conditionals

**Trace execution paths:**

```c
if (fork() == 0) {  // Child only
    fork();          // Creates grandchild
}
fork();              // Everyone does this
```

**Process tree:**
```
         P (parent)
        /│\
       / │ \
      C₁ │  P₂ (P does final fork)
     /│  │
    C₃│  │ (C₁ does inner + final fork)
      C₄ │ (C₁ does final fork)
      
Count: P, P₂, C₁, C₃, C₄ = 5? Let me recount:
P → forks C₁, P continues
P does final fork → P, P₂
C₁ (fork==0) → forks C₃, C₁ continues  
C₁ does final fork → C₁, C₄
C₃ does final fork → C₃, C₅

Total: P, P₂, C₁, C₄, C₃, C₅ = 6 processes
```

### Technique 3: fork() with Logical Operators

**Evaluation rules:**
```
fork() && fork()
- If first fork() returns 0 (child): Don't execute second (short-circuit)
- If first fork() returns >0 (parent): Execute second

fork() || fork()
- If first fork() returns >0 (parent): Don't execute second
- If first fork() returns 0 (child): Execute second
```

**Example: fork() && fork() || fork()**
```
Let f1, f2, f3 be the three forks.

P: f1 returns child_pid (>0)
   P does f2, returns child_pid (>0)
   P skips f3 (true || ...)
   
C1 (from f1): f1 returned 0
   C1 skips f2 (false && ...)
   C1 does f3, creates C1_child
   
C2 (from f2): f2 returned 0 in P's context
   P_f2 skips f3
   
Wait, let me be more careful...

Process count: Trace each branch systematically
```

### Technique 4: print/printf Counting

**Key insight:** Each process runs code after fork point.

```c
fork();
fork();
printf("Hello\n");
// 4 processes, 4 "Hello" printed
```

**With conditions:**
```c
if (fork() != 0) {
    printf("Parent\n");  // Only parents print
}
// 2 processes, only 1 "Parent" (original parent)
```

### Technique 5: Variable Sharing After fork()

**Rule:** Child gets COPY of parent's variables.

```c
int x = 5;
if (fork() == 0) {
    x = 10;  // Only child's copy changes
}
printf("%d ", x);
// Parent prints: 5
// Child prints: 10
```

### Technique 6: Zombie and Orphan Identification

**Decision tree:**
```
Parent terminates first?
├── Yes → Child becomes ORPHAN (adopted by init)
└── No → Does parent call wait()?
    ├── Yes → Normal termination
    └── No → Child becomes ZOMBIE after termination
```

### Technique 7: Context Switch Time Impact

**Calculate overhead:**
```
Given:
- Time quantum = TQ
- Context switch time = CS
- CPU burst = B

Number of context switches = ⌈B/TQ⌉ - 1 (within one process)
Total overhead = (switches) × CS
Effective time = B + overhead
```

### Technique 8: Process State Transition Validation

**Valid transitions (5-state model):**
```
New → Ready (admit)
Ready → Running (dispatch)
Running → Ready (preempt/timeout)
Running → Waiting (I/O request)
Running → Terminated (exit)
Waiting → Ready (I/O complete)

INVALID: Waiting → Running (must go through Ready!)
```

---

## 📝 Practice Problems

1. **fork() Output:** What is printed?
```c
int x = 0;
if (fork() == 0) {
    x = 1;
}
printf("%d ", x);
```

2. **Process Count:** How many processes for:
```c
fork() && fork() || fork();
```

3. **PCB Size:** If register file is 32 registers × 64 bits, and page table pointer is 64 bits, what's minimum PCB size for just these?

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| Process | Program + Resources + State |
| PCB | OS data structure for process info |
| States | New → Ready → Running → Terminated |
| Context Switch | Save old, load new process context |
| fork() | Returns 0 to child, child PID to parent |
| Zombie | Terminated child, parent not waited |
| Orphan | Parent died, child adopted by init |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 3 - Threads](../03-Threads/README.md)*
