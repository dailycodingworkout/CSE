# Chapter 5: Process Synchronization

## 🎯 The Atomic Truth
> **Synchronization = Prevent Race Conditions + Ensure Orderly Access**

---

## 🧠 The WHY: Race Conditions

### The Problem

When multiple processes/threads access shared data, the outcome depends on the ORDER of execution.

```c
// SHARED VARIABLE
int counter = 5;

// PROCESS P1                // PROCESS P2
register1 = counter;         register2 = counter;
register1 = register1 + 1;   register2 = register2 - 1;
counter = register1;         counter = register2;
```

**Possible Interleaving**:
| Step | P1 | P2 | register1 | register2 | counter |
|------|----|----|-----------|-----------|---------|
| 1 | r1 = counter | | 5 | | 5 |
| 2 | r1 = r1 + 1 | | 6 | | 5 |
| 3 | | r2 = counter | 6 | 5 | 5 |
| 4 | | r2 = r2 - 1 | 6 | 4 | 5 |
| 5 | counter = r1 | | 6 | 4 | 6 |
| 6 | | counter = r2 | 6 | 4 | **4** ← Wrong! |

**Expected**: 5 + 1 - 1 = 5
**Got**: 4 or 6 (depending on interleaving)

This is a **RACE CONDITION**.

---

## 🔐 The Critical Section Problem

### Definition

**Critical Section**: Code segment accessing shared resources.

```
┌─────────────────────────────────────────────────────────────┐
│  ENTRY SECTION      ← Request permission to enter           │
├─────────────────────────────────────────────────────────────┤
│  CRITICAL SECTION   ← Access shared resource                │
│  (Only ONE process at a time)                                │
├─────────────────────────────────────────────────────────────┤
│  EXIT SECTION       ← Release permission                     │
├─────────────────────────────────────────────────────────────┤
│  REMAINDER SECTION  ← Rest of the code                       │
└─────────────────────────────────────────────────────────────┘
```

### Requirements for Solution

| Requirement | Meaning | Analogy |
|-------------|---------|---------|
| **Mutual Exclusion** | Only one process in CS at a time | One person in bathroom |
| **Progress** | If CS free, selection must happen | No indefinite waiting outside empty bathroom |
| **Bounded Waiting** | Limit on how many times others can enter before a waiting process | Fair queue |

**GATE Trap**: A solution satisfying only mutual exclusion is NOT sufficient!

---

## 🔧 Software Solutions

### Peterson's Solution (2 Processes)

**The Elegant Algorithm for 2 processes.**

```c
// SHARED VARIABLES
int turn;           // Whose turn to enter
bool flag[2];       // flag[i] = true if Pi wants to enter

// PROCESS Pi (i = 0 or 1)
flag[i] = true;           // I want to enter
turn = j;                 // But I'll let you go first
while (flag[j] && turn == j);  // Wait if you want and it's your turn

// CRITICAL SECTION

flag[i] = false;          // I'm done
// REMAINDER SECTION
```

**Why It Works**:

1. **Mutual Exclusion**: Both can't be in CS because:
   - If both want to enter, turn can only be 0 OR 1
   - One will wait in while loop

2. **Progress**: If Pj doesn't want CS (flag[j] = false), Pi enters immediately

3. **Bounded Waiting**: Turn alternates, so max wait = 1 entry by other

**Visualization**:
```
P0 wants to enter:              P1 wants to enter:
flag[0] = true                  flag[1] = true
turn = 1                        turn = 0
                                
If turn = 0:                    If turn = 1:
  P1 waits (turn == 0)            P0 waits (turn == 1)
  P0 enters                       P1 enters
  
If turn = 1 but flag[1] = false:
  P0 enters (no conflict)
```

---

### Bakery Algorithm (n Processes)

**Like taking a number at the bakery.**

```c
// SHARED VARIABLES
bool choosing[n];    // choosing[i] = true while Pi is getting number
int number[n];       // number[i] = Pi's ticket number

// PROCESS Pi
choosing[i] = true;
number[i] = max(number[0], ..., number[n-1]) + 1;
choosing[i] = false;

for (j = 0; j < n; j++) {
    while (choosing[j]);  // Wait if Pj is choosing
    while (number[j] != 0 && 
           (number[j], j) < (number[i], i));  // Wait if Pj has priority
}

// CRITICAL SECTION

number[i] = 0;  // Done
// REMAINDER SECTION
```

**Priority Rule**: (number[j], j) < (number[i], i) means:
- Smaller ticket number wins
- If tie, smaller process ID wins

---

## ⚙️ Hardware Solutions

### 1. Disabling Interrupts

```c
disable_interrupts();
// CRITICAL SECTION
enable_interrupts();
```

**Problem**: 
- Only works on single CPU
- Dangerous (what if CS hangs?)
- Shouldn't be given to user processes

### 2. Test-and-Set (TAS)

**Atomic instruction that tests and modifies.**

```c
// HARDWARE INSTRUCTION (atomic)
bool test_and_set(bool *target) {
    bool rv = *target;  // Read current value
    *target = true;     // Set to true
    return rv;          // Return old value
}

// SHARED VARIABLE
bool lock = false;

// PROCESS
while (test_and_set(&lock));  // Spin while lock is true
// CRITICAL SECTION
lock = false;  // Release
```

**Why It Works**: The read-modify-write is ATOMIC (uninterruptible).

**Problem**: No bounded waiting (starvation possible).

### 3. Compare-and-Swap (CAS)

```c
// HARDWARE INSTRUCTION (atomic)
int compare_and_swap(int *ptr, int expected, int new_value) {
    int temp = *ptr;
    if (temp == expected)
        *ptr = new_value;
    return temp;
}

// USAGE
while (compare_and_swap(&lock, 0, 1) != 0);  // Wait until lock is 0
// CRITICAL SECTION
lock = 0;  // Release
```

---

## 🚦 Semaphores

### The WHY

Hardware solutions are low-level. We need abstraction.

**Semaphore**: Integer variable with two atomic operations.

### Definition

```
Semaphore S = {
    integer value;
    queue of waiting processes;
}
```

### Operations

```c
// WAIT (P operation) - also called "down" or "acquire"
wait(S) {
    S.value--;
    if (S.value < 0) {
        add process to S.queue;
        block();
    }
}

// SIGNAL (V operation) - also called "up" or "release"
signal(S) {
    S.value++;
    if (S.value <= 0) {
        remove process P from S.queue;
        wakeup(P);
    }
}
```

### Types of Semaphores

| Type | Range | Use |
|------|-------|-----|
| **Binary (Mutex)** | 0 or 1 | Mutual exclusion |
| **Counting** | 0 to N | Resource counting |

### Binary Semaphore Usage

```c
semaphore mutex = 1;  // Binary semaphore initialized to 1

// PROCESS
wait(mutex);         // Enter CS (or wait)
// CRITICAL SECTION
signal(mutex);       // Exit CS
```

### Counting Semaphore Example

```c
// 5 printers available
semaphore printers = 5;

// PROCESS requesting printer
wait(printers);      // Get printer (or wait)
// USE PRINTER
signal(printers);    // Release printer
```

---

## 🏛️ Classical Synchronization Problems

### 1. Producer-Consumer Problem

**Problem**: Producer creates items, Consumer uses them. Buffer has limited size.

```
┌─────────────────────────────────────────────────────────┐
│                                                          │
│  PRODUCER  ──────→  [BUFFER (size N)]  ──────→ CONSUMER │
│                                                          │
│  Constraints:                                            │
│  • Producer waits if buffer full                         │
│  • Consumer waits if buffer empty                        │
│  • Only one accesses buffer at a time                    │
└─────────────────────────────────────────────────────────┘
```

**Solution with Semaphores**:

```c
semaphore mutex = 1;      // Mutual exclusion for buffer
semaphore empty = N;      // Count of empty slots (init to buffer size)
semaphore full = 0;       // Count of filled slots (init to 0)

// PRODUCER
while (true) {
    produce_item();
    
    wait(empty);          // Wait for empty slot
    wait(mutex);          // Enter CS
    
    add_to_buffer();
    
    signal(mutex);        // Exit CS
    signal(full);         // Increment full count
}

// CONSUMER
while (true) {
    wait(full);           // Wait for item
    wait(mutex);          // Enter CS
    
    remove_from_buffer();
    
    signal(mutex);        // Exit CS
    signal(empty);        // Increment empty count
    
    consume_item();
}
```

**GATE Trap**: Order matters!
- Wrong: `wait(mutex); wait(empty);` → Deadlock possible!
- Right: `wait(empty); wait(mutex);`

---

### 2. Readers-Writers Problem

**Problem**: Multiple readers can read simultaneously, but only one writer at a time.

```
┌─────────────────────────────────────────────────────────┐
│  DATABASE                                                │
│                                                          │
│  Readers: Can read simultaneously (no conflict)          │
│  Writers: Exclusive access (no readers or other writers)│
└─────────────────────────────────────────────────────────┘
```

**Solution (First Readers-Writers, Reader Priority)**:

```c
semaphore mutex = 1;      // Protect read_count
semaphore rw_mutex = 1;   // Exclusive access for writers
int read_count = 0;       // Number of current readers

// READER
wait(mutex);              // Enter to update read_count
read_count++;
if (read_count == 1)      // First reader
    wait(rw_mutex);       // Block writers
signal(mutex);

// READ DATA

wait(mutex);
read_count--;
if (read_count == 0)      // Last reader
    signal(rw_mutex);     // Allow writers
signal(mutex);

// WRITER
wait(rw_mutex);           // Exclusive access
// WRITE DATA
signal(rw_mutex);
```

**Problem**: Writers may starve (readers keep coming).

**Second Readers-Writers (Writer Priority)**: Once writer arrives, no new readers start.

---

### 3. Dining Philosophers Problem

**Problem**: 5 philosophers sit at a round table. Each needs two forks to eat. Forks are shared.

```
            P0
       🍴       🍴
    P4     ●     P1
       🍴       🍴
         P3 🍴 P2
```

**Naive Solution (DEADLOCK)**:

```c
semaphore fork[5] = {1, 1, 1, 1, 1};

// PHILOSOPHER i
while (true) {
    think();
    wait(fork[i]);              // Pick left fork
    wait(fork[(i+1) % 5]);      // Pick right fork
    eat();
    signal(fork[(i+1) % 5]);
    signal(fork[i]);
}
```

**Deadlock**: All pick left fork simultaneously → All wait for right fork → DEADLOCK!

**Solutions**:

1. **Allow max 4 philosophers to sit**: Prevents deadlock
   
2. **Odd/Even pickup**: 
   - Odd philosophers: left first
   - Even philosophers: right first

3. **Use mutex for picking both forks atomically**:
```c
wait(mutex);
wait(fork[i]);
wait(fork[(i+1) % 5]);
signal(mutex);
```

4. **Chandy-Misra**: Philosophers request forks from neighbors

---

### 4. Sleeping Barber Problem

```
┌─────────────────────────────────────────────────────────┐
│  BARBER SHOP                                             │
│  ┌─────────┐  ┌─────────────────────────────────────┐   │
│  │ Barber  │  │  Waiting Room (N chairs)            │   │
│  │ Chair   │  │  [C1] [C2] [C3] ... [CN]            │   │
│  └─────────┘  └─────────────────────────────────────┘   │
│                                                          │
│  • If customer arrives and chairs available: wait        │
│  • If no chairs: leave                                   │
│  • If no customers: barber sleeps                        │
│  • Customer wakes barber if sleeping                     │
└─────────────────────────────────────────────────────────┘
```

**Solution**:
```c
semaphore customers = 0;     // Waiting customers
semaphore barber = 0;        // Barber ready?
semaphore mutex = 1;         // Protect waiting count
int waiting = 0;             // Number waiting

// BARBER
while (true) {
    wait(customers);         // Sleep if no customers
    wait(mutex);
    waiting--;
    signal(barber);          // Ready to cut
    signal(mutex);
    cut_hair();
}

// CUSTOMER
wait(mutex);
if (waiting < N) {
    waiting++;
    signal(customers);       // Wake barber
    signal(mutex);
    wait(barber);            // Wait for barber
    get_haircut();
} else {
    signal(mutex);
    leave();                 // No chairs
}
```

---

## 🏢 Monitors

### The WHY

Semaphores are error-prone:
- Forget signal → Deadlock
- Forget wait → Race condition
- Wrong order → Problems

**Monitor**: High-level synchronization construct.

### Definition

```
monitor MonitorName {
    // Shared variables
    
    condition x, y;  // Condition variables
    
    // Procedures (only one executes at a time)
    procedure P1() { ... }
    procedure P2() { ... }
    
    initialization_code() { ... }
}
```

### Properties

1. Only ONE process can be active inside monitor at a time
2. Condition variables for synchronization:
   - `x.wait()`: Suspend calling process
   - `x.signal()`: Wake up one waiting process

### Monitor vs Semaphore

| Aspect | Semaphore | Monitor |
|--------|-----------|---------|
| Level | Low-level | High-level |
| Mutual Exclusion | Programmer ensures | Automatic |
| Error-prone | Yes | Less |
| Language support | OS primitive | Built into language |

---

## 🧮 GATE Numerical Problems

### Problem 1: Semaphore Value

**Initial S = 5. Operations: wait, wait, wait, signal, wait, signal, wait, wait**

**Solution**:
| Operation | S value |
|-----------|---------|
| Initial | 5 |
| wait | 4 |
| wait | 3 |
| wait | 2 |
| signal | 3 |
| wait | 2 |
| signal | 3 |
| wait | 2 |
| wait | 1 |

**Final S = 1**

---

### Problem 2: Maximum Parallelism

**Question**: A system uses binary semaphores. What's the maximum number of processes that can be in CS simultaneously?

**Answer**: 1 (by definition of binary semaphore for mutual exclusion)

---

### Problem 3: Producer-Consumer Buffer

**Question**: Buffer size = 10, initially empty. 15 producers, 10 consumers. If all producers produce once and all consumers consume once, what's the final buffer state?

**Solution**:
- Items produced = 15
- Items consumed = 10
- Final buffer = 15 - 10 = **5 items**

---

## 🎯 GATE Traps and Anti-Solutions

### Trap 1: Semaphore Negative Values
**Question**: Can semaphore be negative?
**Answer**: YES. |S| when negative = number of waiting processes.

### Trap 2: wait() and signal() Order
**Producer**: `wait(empty); wait(mutex);` ✓
**Consumer**: `wait(full); wait(mutex);` ✓
**Wrong**: `wait(mutex); wait(empty);` → Deadlock!

### Trap 3: Peterson's Solution Assumptions
- Works only for 2 processes
- Requires sequential consistency (no instruction reordering)
- Modern CPUs may reorder → may fail

### Trap 4: Binary vs Counting Semaphore
- Binary: 0 or 1
- Counting: Any non-negative value
- **Trap**: Counting semaphore initialized to 1 is NOT same as binary!

---

## 📝 GATE Previous Year Questions

### Q1: (GATE 2018)
**Consider Peterson's solution. If "turn = j" is removed, which property fails?**

(A) Mutual Exclusion ✓  
(B) Progress  
(C) Bounded Waiting  
(D) None

**Explanation**: Without turn, both can set flag[i] = true and enter CS.

---

### Q2: (GATE 2017)
**In producer-consumer, if wait(mutex) comes before wait(empty), what can happen?**

(A) Race condition  
(B) Deadlock ✓  
(C) Starvation  
(D) Nothing

**Explanation**: Producer holds mutex, waits for empty. Consumer needs mutex to signal empty. Deadlock!

---

### Q3: (GATE 2019)
**Binary semaphore initialized to 1. Three processes execute: wait, wait, signal, wait. How many in queue?**

| Op | S | Queue |
|----|---|-------|
| Initial | 1 | 0 |
| wait | 0 | 0 |
| wait | -1 | 1 |
| signal | 0 | 0 |
| wait | -1 | 1 |

**Answer**: 1 process in queue

---

## ⚡ The 5-Second Snap-Check

1. **Semaphore negative?** → |S| = blocked processes count
2. **Deadlock in Producer-Consumer?** → Check mutex order
3. **Dining Philosophers?** → All pick left = deadlock
4. **Peterson's solution?** → Only for 2 processes
5. **Monitor?** → Automatic mutual exclusion

---

## 🏆 Chapter Summary

| Concept | Key Point |
|---------|-----------|
| Race Condition | Outcome depends on execution order |
| Critical Section | Only one process at a time |
| Peterson's | flag[] + turn for 2 processes |
| Semaphore | wait decrements, signal increments |
| Binary Semaphore | Only 0 or 1 |
| Producer-Consumer | empty, full, mutex semaphores |
| Readers-Writers | Multiple readers OR one writer |
| Dining Philosophers | All pick left = deadlock |
| Monitor | Automatic mutual exclusion |

---

*Next Chapter: [Deadlocks →](06-Deadlocks.md)*

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
