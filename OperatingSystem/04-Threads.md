# Chapter 4: Threads

## 🎯 The Atomic Truth
> **Thread = Lightweight Process = Shared Memory + Independent Execution**

---

## 🧠 What is a Thread?

### The WHY (First Principles)

**Problem with Processes**:
- Creating process is expensive (copy entire memory)
- Context switch is slow (switch page tables)
- Communication is complex (IPC needed)

**Solution**: Share everything except execution context.

```
PROCESS vs THREAD:

PROCESS (Heavy):                    THREAD (Light):
┌─────────────────────┐             ┌─────────────────────┐
│ Own Memory Space    │             │ Shared Memory       │
│ Own File Handles    │             │ Shared Files        │
│ Own Code            │             │ Shared Code         │
│ Own Resources       │             │ Shared Resources    │
│                     │             │                     │
│ Expensive to create │             │ Own Stack           │
│ Slow to switch      │             │ Own Registers       │
└─────────────────────┘             │ Own Program Counter │
                                    │                     │
                                    │ Cheap to create     │
                                    │ Fast to switch      │
                                    └─────────────────────┘
```

### Analogy: Office Workers

**Processes** = Different companies (separate buildings, own resources)
**Threads** = Employees in same company (share office, resources, but work independently)

---

## 📊 Single vs Multithreaded Process

```
SINGLE-THREADED:                    MULTI-THREADED:

┌──────────────────────┐            ┌──────────────────────────────┐
│      CODE            │            │           CODE               │
├──────────────────────┤            ├──────────────────────────────┤
│      DATA            │            │           DATA               │
├──────────────────────┤            ├──────────────────────────────┤
│      FILES           │            │           FILES              │
├──────────────────────┤            ├────────┬────────┬────────────┤
│                      │            │ Thread1│ Thread2│  Thread3   │
│    REGISTERS         │            │ Regs   │ Regs   │  Regs      │
│                      │            │ Stack  │ Stack  │  Stack     │
│    STACK             │            │ PC     │ PC     │  PC        │
│                      │            │        │        │            │
└──────────────────────┘            └────────┴────────┴────────────┘
   One execution flow                 Multiple execution flows
```

### What's Shared vs Private

| Shared (Per Process) | Private (Per Thread) |
|---------------------|---------------------|
| Code section | Thread ID |
| Data section | Program Counter |
| OS resources (files) | Register set |
| Heap | Stack |
| Global variables | Local variables |

**GATE Trap**: Heap is SHARED among threads. Stack is PRIVATE to each thread.

---

## 🌟 Benefits of Threads

### 1. Responsiveness
```
WEB BROWSER (Multi-threaded):

Thread 1: Handle user input (scrolling, clicking)
Thread 2: Load images
Thread 3: Render page
Thread 4: Network requests

User types while page loads → RESPONSIVE
```

### 2. Resource Sharing
- Threads share memory automatically
- No need for IPC
- Faster communication

### 3. Economy
| Operation | Process | Thread |
|-----------|---------|--------|
| Create | 100× slower | Fast |
| Context Switch | 5× slower | Fast |
| Memory | Own copy | Shared |

### 4. Scalability
- Threads can run on multiple CPUs
- Easy to parallelize

---

## 🔧 Types of Threads

### 1. User-Level Threads (ULT)

**Thread management in user space. Kernel unaware.**

```
┌─────────────────────────────────────────────────────────────┐
│                     USER SPACE                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Application                                         │    │
│  │  ┌────┐ ┌────┐ ┌────┐                                │    │
│  │  │ T1 │ │ T2 │ │ T3 │  ← User-level threads          │    │
│  │  └────┘ └────┘ └────┘                                │    │
│  └──────────────────────────────────────────────────────┘    │
│                         ↓                                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │        THREAD LIBRARY (e.g., pthread)                │    │
│  │        Manages thread creation, scheduling           │    │
│  └─────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                     KERNEL SPACE                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Kernel sees ONE process (doesn't know about T1-T3)  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

**Pros**:
- Fast creation/switching (no kernel mode switch)
- Custom scheduling algorithms possible
- Portable across OSes

**Cons**:
- One thread blocks → Entire process blocks
- Can't use multiple CPUs
- Kernel can't schedule threads

### 2. Kernel-Level Threads (KLT)

**Thread management by kernel. Full OS support.**

```
┌─────────────────────────────────────────────────────────────┐
│                     USER SPACE                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Application                                         │    │
│  └─────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                     KERNEL SPACE                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Kernel manages threads directly                     │    │
│  │  ┌────┐ ┌────┐ ┌────┐                                │    │
│  │  │ T1 │ │ T2 │ │ T3 │  ← Kernel threads               │    │
│  │  └────┘ └────┘ └────┘                                │    │
│  │  Can be scheduled on different CPUs                  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

**Pros**:
- One thread blocks → Others continue
- Can use multiple CPUs
- Better scheduling decisions

**Cons**:
- Slower (kernel mode switch for operations)
- More overhead
- Less portable

### Comparison Table (GATE Favorite)

| Aspect | User-Level | Kernel-Level |
|--------|------------|--------------|
| **Managed by** | User library | OS kernel |
| **Kernel awareness** | Unaware | Aware |
| **Switch speed** | Fast | Slower |
| **Blocking** | All threads block | Only one blocks |
| **Multiprocessor** | No | Yes |
| **System call** | No | Yes (for operations) |
| **Example** | POSIX Pthreads (user) | Windows threads |

---

## 🔗 Threading Models

### 1. Many-to-One (M:1)

**Many user threads → One kernel thread**

```
USER SPACE:     T1  T2  T3  T4  T5
                 \   \   |   /   /
                  \   \  |  /   /
KERNEL SPACE:    ┌────────────────┐
                 │  Kernel Thread │
                 └────────────────┘
```

**Properties**:
- User-level threading implementation
- One thread blocks → All block
- Can't use multiple CPUs
- Fast context switch

**Example**: Green threads (early Java)

---

### 2. One-to-One (1:1)

**Each user thread → One kernel thread**

```
USER SPACE:     T1       T2       T3       T4
                 |        |        |        |
                 ↓        ↓        ↓        ↓
KERNEL SPACE:   KT1      KT2      KT3      KT4
```

**Properties**:
- True parallelism on multi-core
- One thread blocks → Others continue
- More overhead (kernel manages all)
- Limited by kernel thread limit

**Example**: Linux, Windows, macOS

---

### 3. Many-to-Many (M:N)

**Many user threads → Many kernel threads (M ≥ N)**

```
USER SPACE:     T1   T2   T3   T4   T5   T6
                 \    \    |    /    |    /
                  \    \   |   /     |   /
KERNEL SPACE:    ┌──────┬──────┬──────┐
                 │  KT1 │  KT2 │  KT3 │
                 └──────┴──────┴──────┘
```

**Properties**:
- Best of both worlds
- Can create unlimited user threads
- Kernel threads = number of CPUs
- Complex implementation

**Example**: Solaris (historical), Go runtime

---

### 4. Two-Level Model

**Combination: M:N + 1:1 for specific threads**

Some threads get dedicated kernel thread (for real-time).
Others share kernel threads.

---

### Model Comparison

| Model | Parallelism | Blocking | Overhead | Flexibility |
|-------|-------------|----------|----------|-------------|
| M:1 | No | All block | Low | Low |
| 1:1 | Yes | Independent | High | Medium |
| M:N | Yes | Independent | Medium | High |

---

## 🛠️ Thread Libraries

### POSIX Threads (Pthreads)

```c
#include <pthread.h>

void* thread_func(void* arg) {
    printf("Hello from thread!\n");
    return NULL;
}

int main() {
    pthread_t tid;
    
    // Create thread
    pthread_create(&tid, NULL, thread_func, NULL);
    
    // Wait for thread to complete
    pthread_join(tid, NULL);
    
    return 0;
}
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `pthread_create()` | Create new thread |
| `pthread_join()` | Wait for thread to finish |
| `pthread_exit()` | Terminate calling thread |
| `pthread_cancel()` | Request thread cancellation |
| `pthread_self()` | Get current thread ID |

---

## 🧮 GATE Numerical: Thread Execution

### Problem
A process creates 3 threads. Each thread prints "GATE".
How many times is "GATE" printed (including main)?

```c
int main() {
    pthread_t t1, t2, t3;
    
    pthread_create(&t1, NULL, print_gate, NULL);
    pthread_create(&t2, NULL, print_gate, NULL);  
    pthread_create(&t3, NULL, print_gate, NULL);
    
    printf("GATE\n");  // Main thread
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);
    
    return 0;
}
```

**Answer**: 4 times (3 threads + 1 main)

---

### Problem: fork() with Threads

**Question**: A process has 3 threads. It calls fork(). How many threads does child have?

**Answer**: Child has ONLY 1 thread.

**Explanation**: fork() duplicates only the calling thread. Other threads are NOT duplicated.

```
BEFORE fork():              AFTER fork():
Parent Process              Parent Process    Child Process
┌───┬───┬───┐              ┌───┬───┬───┐    ┌───┐
│T1 │T2 │T3 │  ────────→   │T1 │T2 │T3 │    │T1'│ (only calling thread)
└───┴───┴───┘              └───┴───┴───┘    └───┘
```

**GATE Trap**: This is different from process fork where child is exact copy.

---

## 🔒 Thread Safety Issues

### Race Condition

When multiple threads access shared data and result depends on execution order.

```c
// UNSAFE: Race condition
int counter = 0;

void* increment(void* arg) {
    for(int i = 0; i < 1000000; i++) {
        counter++;  // READ-MODIFY-WRITE (not atomic)
    }
    return NULL;
}
```

**Problem**: counter++ is actually:
1. Read counter to register
2. Increment register
3. Write back to counter

If two threads execute simultaneously:
```
Thread 1        Thread 2        counter
READ (0)                        0
                READ (0)        0
INCREMENT                       0
                INCREMENT       0
WRITE (1)                       1
                WRITE (1)       1  ← Should be 2!
```

**Solution**: Synchronization (covered in next chapter)

---

## 📊 Thread vs Process: Complete Comparison

| Aspect | Process | Thread |
|--------|---------|--------|
| **Memory** | Separate | Shared |
| **Creation time** | High (~100ms) | Low (~1ms) |
| **Context switch** | Expensive | Cheap |
| **Communication** | IPC needed | Direct (shared memory) |
| **Crash effect** | Isolated | Can crash process |
| **Resources** | Own | Shared |
| **Overhead** | High | Low |
| **Parallelism** | Yes | Yes |
| **Protection** | Strong | Weak |

---

## 🎯 GATE Previous Year Questions

### Q1: (GATE 2019)
**In a multithreaded process, which is NOT shared among threads?**

(A) Global variables  
(B) Heap  
(C) Stack ✓  
(D) Code

**Explanation**: Each thread has its own stack for local variables and function calls.

---

### Q2: (GATE 2017)
**Which threading model allows a thread's blocking call to block the entire process?**

(A) One-to-One  
(B) Many-to-One ✓  
(C) Many-to-Many  
(D) Two-Level

**Explanation**: M:1 maps all user threads to one kernel thread.

---

### Q3: (GATE 2015)
**Main advantage of user-level threads over kernel-level threads?**

(A) Can run on multiple processors  
(B) Blocking system call doesn't block process  
(C) Thread switch doesn't require kernel intervention ✓  
(D) More secure

**Explanation**: ULT switch is just library call, no mode switch.

---

## 🧠 Memory Mnemonics

### What's Shared: "CORE DATA FILES"
- **CO**de
- **R**esources (OS handles)
- **E**nvironment
- **DATA** (global variables)
- **FILES** (open file handles)
- **Heap** (dynamically allocated)

### What's Private: "REST"
- **RE**gisters
- **S**tack
- **T**hread ID + Program Counter

### Threading Models: "MOM"
- **M**any-to-One (M:1) → All block together
- **O**ne-to-One (1:1) → True parallelism
- **M**any-to-Many (M:N) → Flexible

---

## ⚡ The 5-Second Snap-Check

1. **Thread sharing question?** → Stack is PRIVATE, everything else SHARED
2. **ULT vs KLT?** → ULT fast but blocking, KLT slow but independent
3. **fork() with threads?** → Child gets ONLY calling thread
4. **Model question?** → M:1 blocks, 1:1 parallels, M:N flexible

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Thread | Lightweight process sharing memory |
| ULT | Fast but all block together |
| KLT | Slower but true parallelism |
| M:1 | Many user → One kernel |
| 1:1 | Each user → One kernel (modern OSes) |
| M:N | Flexible mapping |
| Stack | PRIVATE to thread |
| Heap | SHARED among threads |
| fork() | Only calling thread copied |

---

*Next Chapter: [Process Synchronization →](05-Process-Synchronization.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
