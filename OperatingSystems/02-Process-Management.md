# Chapter 2: Process Management

> **"A process is a program in execution - like a recipe being cooked, not just a recipe on paper"**

---

## 🎯 Process vs Program

| Aspect | Program | Process |
|--------|---------|---------|
| **Nature** | Passive entity | Active entity |
| **Location** | Stored on disk | Resides in memory |
| **Lifetime** | Permanent | Temporary |
| **Resources** | None | CPU, memory, I/O |
| **State** | None | Has execution state |

**🧠 Analogy:** 
- Program = Recipe book on shelf
- Process = Chef cooking using that recipe

**💡 Key Insight:** One program can spawn multiple processes (e.g., multiple Chrome tabs)

---

## 📦 Process Memory Layout

```
┌─────────────────────────┐ High Address
│        Stack            │ ← Local variables, function calls
│          ↓              │   (grows downward)
├─────────────────────────┤
│                         │
│      Free Space         │
│                         │
├─────────────────────────┤
│          ↑              │
│         Heap            │ ← Dynamic memory (malloc)
│                         │   (grows upward)
├─────────────────────────┤
│         BSS             │ ← Uninitialized global variables
├─────────────────────────┤
│        Data             │ ← Initialized global variables
├─────────────────────────┤
│        Text             │ ← Program code (read-only)
└─────────────────────────┘ Low Address
```

### Memory Sections Explained

| Section | Contents | Characteristics |
|---------|----------|-----------------|
| **Text** | Machine code | Read-only, sharable |
| **Data** | Initialized globals/statics | Read-write |
| **BSS** | Uninitialized globals | Initialized to zero |
| **Heap** | Dynamic allocations | malloc(), new |
| **Stack** | Function frames, locals | LIFO, auto-managed |

**⚠️ GATE Trap:** Stack and Heap grow towards each other. Stack overflow = they collide!

---

## 🔄 Process States

### 5-State Model (Standard)

```
                    admit           dispatch
    ┌─────────┐  ─────────►  ┌─────────┐  ─────────►  ┌─────────┐
    │   NEW   │              │  READY  │              │ RUNNING │
    └─────────┘              └────┬────┘  ◄─────────  └────┬────┘
                                  │       interrupt/       │
                                  │       preemption       │
                             wait │                       │exit
                             for  │                       │
                             I/O  │  ┌─────────┐          ▼
                                  └─►│ WAITING │    ┌─────────┐
                                     │(BLOCKED)│    │TERMINATED│
                                     └────┬────┘    └─────────┘
                                          │
                                          │ I/O complete
                                          ▼
                                     ┌─────────┐
                                     │  READY  │
                                     └─────────┘
```

### State Transitions

| Transition | Cause | Who Initiates |
|------------|-------|---------------|
| New → Ready | Admitted to system | Long-term scheduler |
| Ready → Running | CPU allocated | Short-term scheduler |
| Running → Ready | Preemption/Interrupt | OS/Timer |
| Running → Waiting | I/O request | Process |
| Waiting → Ready | I/O complete | Hardware |
| Running → Terminated | Exit/Abort | Process/OS |

**💡 Memory Trick: "NRWR-T"** = New, Ready, Waiting, Running, Terminated

---

### 7-State Model (With Suspend States)

```
                    ┌────────────────┐
                    │   SUSPENDED    │
                    │     READY      │
                    └───────┬────────┘
                            │ resume
                            ▼
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │   NEW   │───────►│  READY  │───────►│ RUNNING │
    └─────────┘        └────┬────┘        └────┬────┘
                            │                  │
                   suspend  │                  │
                            ▼                  ▼
                    ┌────────────────┐   ┌─────────┐
                    │   SUSPENDED    │   │ WAITING │
                    │    BLOCKED     │   └────┬────┘
                    └────────────────┘        │ suspend
                            ▲─────────────────┘
```

**Why Suspend?**
- Memory shortage (swapping)
- User request (debugging)
- Timing (periodic process)
- Parent process request

---

## 📋 Process Control Block (PCB)

The PCB is the **data structure** that represents a process in the OS.

```
┌─────────────────────────────────────────┐
│           Process Control Block         │
├─────────────────────────────────────────┤
│ Process ID (PID)                        │
│ Process State (Ready/Running/Waiting)   │
│ Program Counter (PC)                    │
│ CPU Registers                           │
│ CPU Scheduling Info (priority, queues)  │
│ Memory Management Info (page tables)    │
│ Accounting Info (CPU time used)         │
│ I/O Status (open files, devices)        │
│ Parent/Child Process Pointers           │
└─────────────────────────────────────────┘
```

**🧠 Analogy:** PCB is like an employee's HR file - contains all information about them

**💡 GATE Fact:** PCB is stored in kernel memory, not user space

---

## 🔄 Context Switch

### What is Context Switch?
The process of saving the state of current process and loading the state of the next process.

```
Process P1 (Running)              Process P2 (Ready)
      │                                 │
      │ Interrupt/System call           │
      ▼                                 │
┌──────────────┐                        │
│ Save P1's    │                        │
│ context to   │                        │
│ PCB1         │                        │
└──────┬───────┘                        │
       │                                │
       ▼                                ▼
┌──────────────┐                 ┌──────────────┐
│ Load P2's    │────────────────►│ P2 starts    │
│ context from │                 │ running      │
│ PCB2         │                 │              │
└──────────────┘                 └──────────────┘
```

### Context Switch Overhead

**Time Complexity:** Typically 1-1000 microseconds

**What's saved/restored:**
- Program Counter
- CPU Registers
- Memory mappings
- Stack pointer
- Process state

**⚠️ Important:** Context switch time is **pure overhead** - no useful work done

**Factors Affecting Context Switch Time:**
1. Number of registers
2. Memory speed
3. Hardware support (multiple register sets)
4. OS complexity

---

## 🏭 Process Creation

### fork() System Call

```c
#include <unistd.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        // Error occurred
    } else if (pid == 0) {
        // Child process
        printf("I am child, my PID: %d\n", getpid());
    } else {
        // Parent process
        printf("I am parent, child PID: %d\n", pid);
    }
    return 0;
}
```

### fork() Return Values

| Return Value | Means |
|--------------|-------|
| `-1` | Error (fork failed) |
| `0` | In child process |
| `> 0` | In parent process (value = child's PID) |

### fork() Behavior

```
           Parent Process
                 │
          fork() called
                 │
         ┌───────┴───────┐
         │               │
         ▼               ▼
   Parent continues   Child created
   (fork returns      (fork returns 0)
    child's PID)
```

**What's duplicated:**
- Code segment (shared, copy-on-write)
- Data segment (copied)
- Stack (copied)
- Heap (copied)
- File descriptors (copied)
- PCB (new one created)

**What's NOT duplicated:**
- PID (new unique PID assigned)
- Parent PID (set to parent's PID)
- Pending signals (cleared)

---

### 🎯 GATE Favorite: fork() Tree Problems

**How many processes created by n fork() calls?**

```
Total processes = 2^n (including original)
New processes = 2^n - 1
```

**Example:** 
```c
fork();   // 2 processes
fork();   // 4 processes  
fork();   // 8 processes
```

**Visual Tree:**
```
         P0 (Original)
        /  \
       P0   P1
      / \   / \
     P0 P2 P1 P3
    /\  /\ /\ /\
   P0 P4 P2 P5 P1 P6 P3 P7
```

---

### ⚠️ Tricky fork() Patterns

**Pattern 1: fork() in loop**
```c
for(int i = 0; i < 3; i++) {
    fork();
}
// Total processes = 2^3 = 8
```

**Pattern 2: fork() with conditional**
```c
if(fork() == 0) {
    fork();
}
fork();
// Count: Original → fork1 → (parent: fork3) + (child: fork2 → fork3)
// Total = 6 processes
```

**Pattern 3: fork() with OR operator**
```c
fork() || fork();
// If first fork() returns non-zero (parent), second fork() NOT executed
// If first fork() returns 0 (child), second fork() executed
// Total = 3 processes
```

**Pattern 4: fork() with AND operator**
```c
fork() && fork();
// If first fork() returns 0 (child), second fork() NOT executed
// If first fork() returns non-zero (parent), second fork() executed
// Total = 3 processes
```

---

## 🔚 Process Termination

### Normal Termination
- `exit()` system call
- Return from main()
- `_exit()` (immediate, no cleanup)

### Abnormal Termination
- Abort by parent
- Resource limits exceeded
- Segmentation fault
- Kill signal

### Zombie Process
```
Child terminates ──► Parent hasn't called wait() ──► Child becomes zombie
```
- Process finished but entry still in process table
- Uses no resources except PID

**Solution:** Parent calls `wait()` or `waitpid()`

### Orphan Process
```
Parent terminates ──► Child still running ──► Child becomes orphan
```
- Orphan adopted by init process (PID 1)
- Continues execution normally

**💡 GATE Trick:**
- Zombie = Dead but not reaped (parent's fault)
- Orphan = Parent died first (now adopted)

---

## 📬 Inter-Process Communication (IPC)

### Why IPC?
- Information sharing
- Computation speedup
- Modularity
- Convenience

### IPC Mechanisms

```
┌─────────────────────────────────────────────────────────┐
│                    IPC Methods                          │
├───────────────────────┬─────────────────────────────────┤
│    Shared Memory      │      Message Passing            │
│  ┌─────────────────┐  │  ┌───────────────────────────┐  │
│  │ Process A       │  │  │ Process A ───msg──► OS    │  │
│  │      ↑          │  │  │                  │        │  │
│  │      │          │  │  │                  ▼        │  │
│  │  Shared Area    │  │  │          OS ───msg──►     │  │
│  │      │          │  │  │                  │        │  │
│  │      ↓          │  │  │                  ▼        │  │
│  │ Process B       │  │  │              Process B    │  │
│  └─────────────────┘  │  └───────────────────────────┘  │
└───────────────────────┴─────────────────────────────────┘
```

### Comparison

| Aspect | Shared Memory | Message Passing |
|--------|---------------|-----------------|
| **Speed** | Faster (no kernel involvement) | Slower (kernel involved) |
| **Synchronization** | Needed (programmer's job) | Built-in |
| **Data Volume** | Large amounts | Small amounts |
| **Implementation** | Complex | Simple |
| **Use Case** | Same machine | Same or different machines |

---

### Shared Memory Implementation

```c
// Create shared memory
int shmid = shmget(key, size, IPC_CREAT | 0666);

// Attach to shared memory
void *ptr = shmat(shmid, NULL, 0);

// Use shared memory
// ... write/read data ...

// Detach
shmdt(ptr);

// Remove (when done)
shmctl(shmid, IPC_RMID, NULL);
```

---

### Message Passing Implementation

**Direct Communication:**
```
send(P, message)    - Send to process P
receive(Q, message) - Receive from process Q
```

**Indirect Communication (Mailboxes):**
```
send(A, message)    - Send to mailbox A
receive(A, message) - Receive from mailbox A
```

**Synchronization Options:**

| Send | Receive | Type |
|------|---------|------|
| Blocking | Blocking | Synchronous (Rendezvous) |
| Non-blocking | Blocking | Asynchronous |
| Non-blocking | Non-blocking | Asynchronous |

---

### Pipes

**Ordinary Pipes (Unnamed):**
```
┌──────────┐    write    ┌──────┐    read     ┌──────────┐
│ Producer │────────────►│ Pipe │────────────►│ Consumer │
└──────────┘             └──────┘             └──────────┘
```
- Unidirectional
- Parent-child relationship required
- Exist only while processes exist

**Named Pipes (FIFO):**
- Bidirectional (with proper setup)
- No parent-child relationship needed
- Persist beyond process lifetime

```c
// Create named pipe
mkfifo("/tmp/myfifo", 0666);

// Open for writing
int fd = open("/tmp/myfifo", O_WRONLY);
write(fd, buffer, size);

// Open for reading (in another process)
int fd = open("/tmp/myfifo", O_RDONLY);
read(fd, buffer, size);
```

---

## 🧵 Threads

### Process vs Thread

```
Single-threaded Process:        Multi-threaded Process:
┌─────────────────────┐        ┌────────────────────────────┐
│ Code   Data   Files │        │     Code   Data   Files    │
├─────────────────────┤        ├────────┬────────┬──────────┤
│ Registers  Stack    │        │Thread 1│Thread 2│Thread 3  │
│     (Thread)        │        │Reg Stk │Reg Stk │Reg Stk   │
└─────────────────────┘        └────────┴────────┴──────────┘
```

| Aspect | Process | Thread |
|--------|---------|--------|
| **Definition** | Independent execution unit | Lightweight process |
| **Address Space** | Own address space | Shared with other threads |
| **Creation Time** | Slow (heavy) | Fast (light) |
| **Communication** | IPC needed | Shared memory |
| **Context Switch** | Expensive | Cheap |
| **Failure Impact** | Isolated | Can affect other threads |

**💡 Memory Trick:** 
- Process = House (separate everything)
- Thread = Rooms in same house (shared utilities)

---

### What Threads Share vs Don't Share

| Shared | Not Shared (Private) |
|--------|----------------------|
| Code section | Thread ID |
| Data section | Registers |
| Open files | Stack |
| Signals | Program counter |
| Heap | Priority |

---

### Benefits of Multithreading

1. **Responsiveness:** UI stays active while background work
2. **Resource Sharing:** No IPC overhead
3. **Economy:** Thread creation 30x faster than process
4. **Scalability:** Exploit multiple CPUs

---

### Types of Threads

#### User-Level Threads (ULT)
```
┌─────────────────────────────────────┐
│           User Space                │
│  ┌─────────────────────────────┐    │
│  │      Thread Library         │    │
│  │  T1   T2   T3   T4   T5    │    │
│  └─────────────────────────────┘    │
├─────────────────────────────────────┤
│           Kernel Space              │
│         (Sees ONE process)          │
└─────────────────────────────────────┘
```

**Pros:**
- Fast context switch (no kernel involvement)
- Portable (library-based)
- Custom scheduling possible

**Cons:**
- One thread blocks → entire process blocks
- Can't use multiple CPUs

---

#### Kernel-Level Threads (KLT)
```
┌─────────────────────────────────────┐
│           User Space                │
│     T1   T2   T3   T4   T5         │
├─────────────────────────────────────┤
│           Kernel Space              │
│   (Kernel manages each thread)      │
│     T1   T2   T3   T4   T5         │
└─────────────────────────────────────┘
```

**Pros:**
- One thread blocks → others continue
- True parallelism on multiple CPUs

**Cons:**
- Slower (kernel involved in all operations)
- More overhead

---

### Multithreading Models

#### Many-to-One Model
```
User threads:    T1  T2  T3  T4
                  \  |  /  /
                   \ | / /
Kernel thread:      K1
```
- Multiple user threads → One kernel thread
- One blocks → all block
- No parallelism
- **Example:** Green threads (Java)

---

#### One-to-One Model
```
User threads:    T1   T2   T3   T4
                 |    |    |    |
Kernel threads:  K1   K2   K3   K4
```
- Each user thread → One kernel thread
- True parallelism
- Overhead of creating kernel threads
- **Examples:** Linux, Windows

---

#### Many-to-Many Model
```
User threads:    T1  T2  T3  T4  T5  T6
                  \  |  /\   |  /\  /
                   \ | /  \  | /  \/
Kernel threads:     K1      K2    K3
```
- Multiple user threads → Multiple kernel threads
- Best of both worlds
- **Example:** Solaris prior to version 9

---

#### Two-Level Model
```
User threads:    T1  T2  T3  T4  T5  T6
                  \  |  /    |    |
                   \ | /     |    |
Kernel threads:     K1      K2   K3
```
- Many-to-many + allows binding specific thread
- **Examples:** IRIX, HP-UX

---

## 📊 Process Scheduling Queues

### Types of Queues

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Job Queue                                                 │
│   ┌──────────────────────────────────────────┐             │
│   │ All processes in system                  │             │
│   └──────────────────────────────────────────┘             │
│                     │                                       │
│                     ▼                                       │
│   Ready Queue (processes in memory, ready to run)          │
│   ┌──────────────────────────────────────────┐             │
│   │  P1 → P4 → P2 → P7 → head               │────────►CPU │
│   └──────────────────────────────────────────┘             │
│                     │                                       │
│                     ▼                                       │
│   Device Queues (waiting for I/O)                          │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐         │
│   │ Disk queue  │ │ Terminal    │ │ Network     │         │
│   │ P3→P5→P8   │ │ queue: P6   │ │ queue: P9   │         │
│   └─────────────┘ └─────────────┘ └─────────────┘         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⏱️ Types of Schedulers

| Scheduler | Frequency | Function | Queue |
|-----------|-----------|----------|-------|
| **Long-term (Job)** | Rarely (minutes) | Admits jobs to system | Job → Ready |
| **Short-term (CPU)** | Very often (ms) | Selects next process | Ready → Running |
| **Medium-term** | Occasionally | Swapping for memory | Ready ↔ Suspended |

**💡 GATE Trick:**
- Long-term controls **degree of multiprogramming**
- Short-term is the **dispatcher**
- Medium-term handles **swapping**

---

### Process Mix

Long-term scheduler should maintain good mix:
- **CPU-bound:** Long CPU bursts, short I/O bursts
- **I/O-bound:** Short CPU bursts, long I/O bursts

**Ideal:** Mix of both for maximum resource utilization

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **fork() output** - Count processes, print statements
2. **PCB contents** - What's stored where
3. **State transitions** - Valid vs invalid
4. **Thread comparison** - ULT vs KLT
5. **IPC methods** - Which to use when

### ⚠️ Edge Cases & Traps:
1. **fork() returns twice** - Once in parent, once in child
2. **Zombie has no resources** - Only process table entry
3. **exec() replaces process image** - Same PID, new code
4. **Thread stack is private** - Each thread has own stack
5. **Suspended Ready ≠ Blocked** - Can be resumed without I/O

---

## 🎯 Quick Revision Points

```
✓ Process = Program in execution
✓ PCB = Process's identity card
✓ Context switch = CPU switches between processes
✓ fork() returns 0 to child, child's PID to parent
✓ n fork() calls = 2^n processes
✓ Zombie = terminated but not waited
✓ Orphan = parent terminated, adopted by init
✓ Thread shares: code, data, files
✓ Thread private: stack, registers, PC
✓ ULT = fast but no parallelism
✓ KLT = slower but true parallelism
```

---

## 📚 Key Formulas

```
Total processes after n fork() = 2^n
New processes after n fork() = 2^n - 1

Context Switch Overhead = 2 × (save + restore time)

Thread Speedup (Amdahl's Law):
Speedup = 1 / (S + P/N)
where S = serial fraction, P = parallel fraction, N = processors
```

---

[← Previous: Introduction](./01-Introduction.md) | [Next: CPU Scheduling →](./03-CPU-Scheduling.md)
