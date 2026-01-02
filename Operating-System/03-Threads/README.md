# 📖 Chapter 3: Threads

> **The Atomic Truth:** Thread = Lightweight Process (shares address space)

---

## 🎯 GATE Syllabus Coverage
- Thread Concept
- User-Level vs Kernel-Level Threads
- Multithreading Models
- Thread Libraries
- Threading Issues

---

## 3.1 What is a Thread?

### Definition
A **Thread** is the smallest unit of CPU execution. It consists of:
- Thread ID
- Program Counter
- Register Set
- Stack

Threads within the same process **share**:
- Code section
- Data section
- Heap
- Open files
- Signals

### Process vs Thread

```
Single-Threaded Process        Multi-Threaded Process
┌────────────────────┐         ┌────────────────────┐
│     Code           │         │     Code           │
├────────────────────┤         ├────────────────────┤
│     Data           │         │     Data           │
├────────────────────┤         ├────────────────────┤
│     Files          │         │     Files          │
├────────────────────┤         ├────────────────────┤
│   ┌──────────┐     │         │ ┌────┐ ┌────┐ ┌────┐│
│   │ Registers│     │         │ │Reg │ │Reg │ │Reg ││
│   ├──────────┤     │         │ ├────┤ ├────┤ ├────┤│
│   │   Stack  │     │         │ │Stk │ │Stk │ │Stk ││
│   └──────────┘     │         │ └────┘ └────┘ └────┘│
│   One Thread       │         │   Thread1 T2   T3  │
└────────────────────┘         └────────────────────┘
```

### Why Threads?

| Advantage | Explanation |
|-----------|-------------|
| **Responsiveness** | UI stays responsive while computation happens |
| **Resource Sharing** | Threads share memory, no IPC needed |
| **Economy** | Creating thread cheaper than process |
| **Scalability** | Utilize multi-core processors |

### Thread vs Process Comparison

| Feature | Process | Thread |
|---------|---------|--------|
| Address Space | Separate | Shared |
| Creation Time | High (~100ms) | Low (~1ms) |
| Context Switch | Expensive | Cheap |
| Communication | IPC required | Direct memory |
| Crash Impact | Isolated | Affects all threads |
| Memory Overhead | High | Low |

---

## 3.2 Types of Threads

### 3.2.1 User-Level Threads (ULT)

**Concept:** Thread management done entirely in user space by thread library.

```
┌─────────────────────────────────────────────┐
│              User Space                     │
│  ┌─────────────────────────────────────┐    │
│  │     Thread Library (e.g., pthreads) │    │
│  │  ┌────┐  ┌────┐  ┌────┐  ┌────┐     │    │
│  │  │ T1 │  │ T2 │  │ T3 │  │ T4 │     │    │
│  │  └────┘  └────┘  └────┘  └────┘     │    │
│  └─────────────────────────────────────┘    │
│              Process                        │
├─────────────────────────────────────────────┤
│              Kernel Space                   │
│  ┌─────────────────────────────────────┐    │
│  │      Kernel sees ONE process        │    │
│  │         (doesn't know about         │    │
│  │          user threads)              │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

**Characteristics:**
- Kernel unaware of threads
- Thread switching in user mode (fast)
- Thread scheduling by user library
- Blocking system call blocks entire process

**Advantages:**
- Fast thread operations (no kernel involvement)
- Can be implemented on any OS
- Customizable scheduling

**Disadvantages:**
- One thread blocks → entire process blocks
- Cannot utilize multiple CPUs
- Page fault in one thread blocks all

---

### 3.2.2 Kernel-Level Threads (KLT)

**Concept:** Thread management done by the operating system kernel.

```
┌─────────────────────────────────────────────┐
│              User Space                     │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐             │
│  │ T1 │  │ T2 │  │ T3 │  │ T4 │             │
│  └──┬─┘  └──┬─┘  └──┬─┘  └──┬─┘             │
│     │       │       │       │               │
│     │       │       │       │               │
├─────┼───────┼───────┼───────┼───────────────┤
│     ↓       ↓       ↓       ↓               │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐             │
│  │KT1 │  │KT2 │  │KT3 │  │KT4 │             │
│  └────┘  └────┘  └────┘  └────┘             │
│     Kernel-Level Threads                    │
│     (Kernel manages each separately)        │
└─────────────────────────────────────────────┘
```

**Characteristics:**
- Kernel aware of and manages all threads
- Thread switching requires mode switch
- Can schedule threads on multiple CPUs
- Blocking one thread doesn't block others

**Advantages:**
- True parallelism on multiprocessors
- One thread blocking doesn't affect others
- Kernel can optimize scheduling

**Disadvantages:**
- Thread operations slower (kernel involvement)
- More overhead per thread
- Limited portability

---

### 3.2.3 Comparison Table

| Feature | User-Level Thread | Kernel-Level Thread |
|---------|------------------|---------------------|
| Management | Thread library | OS Kernel |
| Context Switch | Fast (user mode) | Slow (mode switch) |
| Multiprocessor | ❌ Cannot use | ✅ Can use |
| Blocking Call | Blocks process | Blocks only that thread |
| OS Support | Not required | Required |
| Portability | High | Low |
| Scheduling | User-defined | OS scheduler |

---

## 3.3 Multithreading Models

### 3.3.1 Many-to-One Model

**Concept:** Many user threads mapped to one kernel thread.

```
User Threads         Kernel Thread
┌────┐ ┌────┐ ┌────┐
│ U1 │ │ U2 │ │ U3 │
└──┬─┘ └──┬─┘ └──┬─┘
   │      │      │
   └──────┼──────┘
          ↓
       ┌────┐
       │ K1 │
       └────┘
```

**Characteristics:**
- User threads managed by user library
- One thread blocks → all block
- Cannot use multiple CPUs

**Example:** Solaris Green Threads, GNU Portable Threads

---

### 3.3.2 One-to-One Model

**Concept:** Each user thread mapped to one kernel thread.

```
User Threads         Kernel Threads
┌────┐ ┌────┐ ┌────┐
│ U1 │ │ U2 │ │ U3 │
└──┬─┘ └──┬─┘ └──┬─┘
   │      │      │
   ↓      ↓      ↓
┌────┐ ┌────┐ ┌────┐
│ K1 │ │ K2 │ │ K3 │
└────┘ └────┘ └────┘
```

**Characteristics:**
- True parallelism possible
- One thread blocking doesn't affect others
- Creating user thread = Creating kernel thread (expensive)

**Example:** Windows, Linux (NPTL)

---

### 3.3.3 Many-to-Many Model

**Concept:** Many user threads mapped to smaller or equal number of kernel threads.

```
User Threads              Kernel Threads
┌────┐ ┌────┐ ┌────┐ ┌────┐
│ U1 │ │ U2 │ │ U3 │ │ U4 │
└──┬─┘ └──┬─┘ └──┬─┘ └──┬─┘
   │      │      │      │
   └──────┴──┬───┴──────┘
             │
     ┌───────┼───────┐
     ↓       ↓       ↓
  ┌────┐  ┌────┐  ┌────┐
  │ K1 │  │ K2 │  │ K3 │
  └────┘  └────┘  └────┘
```

**Characteristics:**
- Flexible mapping
- True parallelism
- One blocking doesn't stop all
- Not as limited as one-to-one

**Example:** Solaris prior to version 9, IRIX

---

### 3.3.4 Two-Level Model

**Concept:** Many-to-many with option for one-to-one binding.

```
User Threads              Kernel Threads
┌────┐ ┌────┐ ┌────┐ ┌────┐
│ U1 │ │ U2 │ │ U3 │ │ U4 │ (bound)
└──┬─┘ └──┬─┘ └──┬─┘ └──┬─┘
   │      │      │      │
   └──────┴──┬───┘      │
             │          │
     ┌───────┼──────────┘
     ↓       ↓       
  ┌────┐  ┌────┐  ┌────┐
  │ K1 │  │ K2 │  │ K4 │ (dedicated to U4)
  └────┘  └────┘  └────┘
```

**Example:** HP-UX, Tru64 UNIX

---

### 3.3.5 Model Comparison

| Model | Parallelism | Blocking | Overhead |
|-------|-------------|----------|----------|
| Many-to-One | ❌ | One blocks all | Low |
| One-to-One | ✅ Max | Independent | High |
| Many-to-Many | ✅ | Flexible | Medium |
| Two-Level | ✅ | Flexible + Bound | Medium |

---

## 3.4 Thread Libraries

### POSIX Threads (pthreads)

**Standard API for thread creation and synchronization.**

```c
#include <pthread.h>
#include <stdio.h>

void *thread_function(void *arg) {
    int *num = (int *)arg;
    printf("Thread received: %d\n", *num);
    return NULL;
}

int main() {
    pthread_t thread;
    int value = 42;
    
    // Create thread
    pthread_create(&thread, NULL, thread_function, &value);
    
    // Wait for thread to complete
    pthread_join(thread, NULL);
    
    return 0;
}
```

### Key pthread Functions

| Function | Purpose |
|----------|---------|
| `pthread_create()` | Create new thread |
| `pthread_exit()` | Terminate calling thread |
| `pthread_join()` | Wait for thread to terminate |
| `pthread_cancel()` | Request thread cancellation |
| `pthread_self()` | Get thread ID |
| `pthread_equal()` | Compare thread IDs |

### Windows Threads

```c
#include <windows.h>

DWORD WINAPI ThreadFunction(LPVOID lpParam) {
    printf("Thread executing\n");
    return 0;
}

int main() {
    HANDLE hThread;
    DWORD threadId;
    
    hThread = CreateThread(
        NULL,           // Security attributes
        0,              // Stack size (default)
        ThreadFunction, // Thread function
        NULL,           // Parameter
        0,              // Creation flags
        &threadId);     // Thread ID
    
    WaitForSingleObject(hThread, INFINITE);
    CloseHandle(hThread);
    return 0;
}
```

---

## 3.5 Threading Issues

### 3.5.1 fork() and exec() Semantics

**Problem:** What happens when a thread calls `fork()`?

| Option | Behavior | Use Case |
|--------|----------|----------|
| Duplicate all threads | All threads copied to child | Child continues same work |
| Duplicate only calling thread | Only caller copied | Child will call exec() |

**UNIX Approach:** Usually only calling thread duplicated.

### 3.5.2 Signal Handling

**Problem:** Which thread should handle a signal?

**Options:**
1. Deliver to thread to which signal applies
2. Deliver to every thread in process
3. Deliver to certain threads only
4. Assign specific thread for all signals

### 3.5.3 Thread Cancellation

**Types:**

| Type | Behavior | Safety |
|------|----------|--------|
| **Asynchronous** | Immediate termination | Dangerous (resource leaks) |
| **Deferred** | Check at cancellation points | Safer |

**Cancellation Points:** Defined points where thread checks for cancellation (e.g., `pthread_testcancel()`)

### 3.5.4 Thread-Local Storage (TLS)

**Problem:** Need per-thread data that persists across function calls.

```c
// Using __thread keyword (GCC)
__thread int thread_local_var;

// Using pthread
pthread_key_t key;
pthread_key_create(&key, NULL);
pthread_setspecific(key, value);
void *val = pthread_getspecific(key);
```

### 3.5.5 Scheduler Activations

**Problem:** Communication between kernel and user-level thread scheduler.

**Solution:** **Lightweight Process (LWP)** - intermediate data structure

```
User Threads      LWP          Kernel Threads
┌────┐ ┌────┐    ┌────┐       ┌────┐
│ U1 │ │ U2 │────│LWP1│───────│ K1 │
└────┘ └────┘    └────┘       └────┘
     ┌────┐      ┌────┐       ┌────┐
     │ U3 │──────│LWP2│───────│ K2 │
     └────┘      └────┘       └────┘
```

**Upcall:** Kernel notifies user-level scheduler of events.

---

## 3.6 Multithreading Models Numerical Problems

### Problem Type: Thread Parallelism

**Example:** A process has 4 threads. On a 2-core system:
- Many-to-One: Only 1 thread runs at a time (1 kernel thread)
- One-to-One: 2 threads can run in parallel
- Many-to-Many (2 kernel threads): 2 threads can run in parallel

### Problem Type: Context Switch Cost

**Given:** 
- Thread context switch: 0.5ms
- Process context switch: 5ms
- Task requires 100 context switches

**Calculate time savings using threads:**
- Process: $100 \times 5 = 500$ ms
- Thread: $100 \times 0.5 = 50$ ms
- Savings: 450 ms

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2019)
**Q:** In the many-to-one threading model, if one thread makes a blocking system call:
(a) Only that thread is blocked
(b) All threads in the process are blocked
(c) The entire system is blocked
(d) No thread is blocked

**Answer:** (b) All threads in the process are blocked

**Explanation:** In many-to-one, all user threads map to one kernel thread. When that kernel thread blocks, all user threads block.

---

### Question 2 (GATE 2017)
**Q:** Which is the fastest threading model for thread operations?
(a) One-to-One
(b) Many-to-One
(c) Many-to-Many
(d) All are same

**Answer:** (b) Many-to-One

**Explanation:** No kernel involvement in thread operations - all managed in user space.

---

### Question 3 (GATE 2020)
**Q:** Which data is NOT shared between threads of the same process?
(a) Global variables
(b) Heap memory
(c) Stack
(d) Code section

**Answer:** (c) Stack

**Explanation:** Each thread has its own stack for local variables and function calls.

---

## 🧠 Memory Tricks

### Mnemonic: Thread Shared Resources "CHEF"
- **C**ode section
- **H**eap
- **E**nvironment
- **F**iles (open file descriptors)

**NOT shared:** Stack, Registers, Program Counter (Thread-specific)

### The Mental Slider: Threading Models
Imagine a **funnel**:
- **Many-to-One:** Wide funnel top (many threads) → narrow bottom (one kernel thread)
- **One-to-One:** Straight pipe (each thread gets its pipe)
- **Many-to-Many:** Adjustable funnel (flexible mapping)

### Mnemonic: "PORK" for Thread-Private Data
- **P**rogram Counter
- **O**wn Stack
- **R**egisters
- **K**ernel Stack (for kernel mode)

---

## ⚠️ Common GATE Traps

### Trap 1: Thread vs Process Memory
**Wrong:** Threads have completely separate memory
**Right:** Threads share heap and data section; only stack is separate

### Trap 2: Many-to-One Performance
**Wrong:** Many-to-one utilizes multiple cores
**Right:** Only one thread can run at a time (kernel sees one thread)

### Trap 3: Kernel Thread Overhead
**Wrong:** Kernel threads are always better
**Right:** Kernel threads have more overhead; user threads are faster for operations not requiring kernel services

---

## 📝 Practice Problems

1. **Parallelism Calculation:** A 4-threaded process runs on 8-core machine using one-to-one model. Maximum parallel threads?

2. **Memory Sharing:** Two threads T1 and T2 share variable `int count = 0`. T1 executes `count++` while T2 executes `count--`. What are possible final values?

3. **Model Identification:** An OS creates kernel thread for each user thread. If creating 1000 threads, which model is problematic and why?

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| Thread | Lightweight process, shares address space |
| ULT | User-level, fast, blocks process on system call |
| KLT | Kernel-level, slower, true parallelism |
| Many-to-One | Fast operations, no parallelism |
| One-to-One | True parallelism, expensive creation |
| Many-to-Many | Flexible, balanced |
| Shared | Code, Data, Heap, Files |
| Private | Stack, Registers, PC |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 4 - CPU Scheduling](../04-CPU-Scheduling/README.md)*
