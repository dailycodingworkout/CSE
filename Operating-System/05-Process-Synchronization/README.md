# 📖 Chapter 5: Process Synchronization

> **The Atomic Truth:** Synchronization = Coordinating concurrent access to shared resources

---

## 🎯 GATE Syllabus Coverage
- Critical Section Problem
- Peterson's Solution
- Synchronization Hardware
- Semaphores
- Classic Synchronization Problems
- Monitors
- Deadlock (Intro)

---

## 5.1 The Critical Section Problem

### What is a Critical Section?
A **Critical Section** is a code segment where shared resources are accessed. Only one process should execute in its critical section at a time.

### Process Structure

```c
do {
    // Entry Section
    [Request permission to enter critical section]
    
    // Critical Section
    [Access shared resources]
    
    // Exit Section
    [Release permission]
    
    // Remainder Section
    [Other code]
} while (true);
```

### Requirements for Solution

| Requirement | Description | Analogy |
|-------------|-------------|---------|
| **Mutual Exclusion** | Only one process in CS at a time | Only one person in bathroom |
| **Progress** | Selection of next process must not be delayed indefinitely | If bathroom empty, someone can enter |
| **Bounded Waiting** | Limit on how long a process waits | No one waits forever |

---

## 5.2 Peterson's Solution

### Two-Process Solution

```c
// Shared variables
int turn;           // Whose turn it is
bool flag[2];       // Ready to enter CS

// Process Pi (i = 0 or 1)
void process_i(int i) {
    int j = 1 - i;  // Other process
    
    flag[i] = true;     // I want to enter
    turn = j;           // Give turn to other
    
    while (flag[j] && turn == j);  // Wait
    
    // Critical Section
    
    flag[i] = false;    // I'm done
    
    // Remainder Section
}
```

### Why Peterson's Works

**Mutual Exclusion:**
- If both P0 and P1 in CS, then `flag[0] = flag[1] = true`
- `turn` can only be 0 or 1, not both
- One process must have waited in while loop
- Contradiction! ✓

**Progress:**
- If only one wants to enter, it enters (other's flag is false)
- If both want, `turn` decides ✓

**Bounded Waiting:**
- Maximum wait = 1 turn (other process executes once) ✓

### Modern Limitation
**Peterson's solution may not work on modern processors** due to:
- Instruction reordering
- Memory visibility issues
- Need memory barriers for correct operation

---

## 5.3 Hardware Synchronization

### 5.3.1 Disabling Interrupts

```c
void enter_critical() {
    disable_interrupts();
}

void exit_critical() {
    enable_interrupts();
}
```

**Problems:**
- Only works on uniprocessor
- Dangerous if process doesn't enable
- Affects system responsiveness

### 5.3.2 Test-and-Set (TAS)

**Atomic instruction** that reads and sets a value in one operation.

```c
// Atomic operation (hardware)
bool test_and_set(bool *target) {
    bool rv = *target;
    *target = true;
    return rv;
}

// Usage
bool lock = false;

void process() {
    while (test_and_set(&lock));  // Busy wait
    
    // Critical Section
    
    lock = false;
}
```

### 5.3.3 Compare-and-Swap (CAS)

```c
// Atomic operation
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected)
        *value = new_value;
    return temp;
}

// Usage
int lock = 0;

void process() {
    while (compare_and_swap(&lock, 0, 1) != 0);  // Busy wait
    
    // Critical Section
    
    lock = 0;
}
```

### 5.3.4 Problems with Busy Waiting

- Wastes CPU cycles
- Priority inversion possible
- Not fair (no bounded waiting guarantee)

---

## 5.4 Semaphores

### Definition
A **Semaphore** is a synchronization variable that is accessed via two atomic operations: `wait()` (P) and `signal()` (V).

### Semaphore Types

| Type | Value Range | Use Case |
|------|-------------|----------|
| **Binary** | 0 or 1 | Mutual exclusion (like lock) |
| **Counting** | 0 to N | Resource counting |

### Operations

```c
// Wait (P, Down, Decrement)
wait(S) {
    while (S <= 0);  // Busy wait
    S--;
}

// Signal (V, Up, Increment)
signal(S) {
    S++;
}
```

### Implementation with Blocking (No Busy Wait)

```c
typedef struct {
    int value;
    struct process *list;  // Waiting queue
} semaphore;

void wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        // Add process to S->list
        block();  // Put process to sleep
    }
}

void signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // Remove process P from S->list
        wakeup(P);
    }
}
```

### Using Semaphores for Mutual Exclusion

```c
semaphore mutex = 1;

void process() {
    wait(&mutex);
    
    // Critical Section
    
    signal(&mutex);
}
```

### Semaphore Value Interpretation

$$S = S_{initial} - \text{num\_waits} + \text{num\_signals}$$

- If $S > 0$: Number of available resources
- If $S = 0$: All resources in use, no waiting
- If $S < 0$: $|S|$ processes waiting

---

## 5.5 Classic Synchronization Problems

### 5.5.1 Producer-Consumer Problem

**Problem:** Producer creates items, Consumer uses them. Bounded buffer between them.

```
Producer                       Consumer
   │                              │
   ↓                              ↓
┌──────┐                      ┌──────┐
│Create│                      │ Use  │
└──┬───┘                      └──┬───┘
   │                              │
   ↓                              ↓
  ┌───────────────────────────────┐
  │  Buffer [0][1][2]...[N-1]    │
  └───────────────────────────────┘
```

**Solution using Semaphores:**

```c
semaphore mutex = 1;      // Binary semaphore for mutual exclusion
semaphore empty = N;      // Counting: empty slots
semaphore full = 0;       // Counting: filled slots

void producer() {
    while (true) {
        item = produce_item();
        
        wait(&empty);     // Wait for empty slot
        wait(&mutex);     // Enter critical section
        
        buffer[in] = item;
        in = (in + 1) % N;
        
        signal(&mutex);   // Exit critical section
        signal(&full);    // Signal item produced
    }
}

void consumer() {
    while (true) {
        wait(&full);      // Wait for item
        wait(&mutex);     // Enter critical section
        
        item = buffer[out];
        out = (out + 1) % N;
        
        signal(&mutex);   // Exit critical section
        signal(&empty);   // Signal slot emptied
        
        consume_item(item);
    }
}
```

**GATE Trap:** Order of wait() matters!
- `wait(empty); wait(mutex);` ✓
- `wait(mutex); wait(empty);` ✗ (Deadlock if buffer full!)

---

### 5.5.2 Readers-Writers Problem

**Problem:** Multiple readers can read simultaneously, but writers need exclusive access.

**First Readers-Writers Problem (Readers Preference):**

```c
semaphore rw_mutex = 1;   // For writers
semaphore mutex = 1;      // For reader count
int read_count = 0;       // Active readers

void writer() {
    wait(&rw_mutex);
    
    // Write data
    
    signal(&rw_mutex);
}

void reader() {
    wait(&mutex);
    read_count++;
    if (read_count == 1)
        wait(&rw_mutex);  // First reader blocks writers
    signal(&mutex);
    
    // Read data
    
    wait(&mutex);
    read_count--;
    if (read_count == 0)
        signal(&rw_mutex);  // Last reader frees writers
    signal(&mutex);
}
```

**Problem:** Writers can starve!

**Second Readers-Writers Problem (Writers Preference):**
- Writers have priority
- New readers wait if writer is waiting

---

### 5.5.3 Dining Philosophers Problem

**Problem:** 5 philosophers around a table with 5 chopsticks. Each needs 2 chopsticks to eat.

```
          P0
       🥢    🥢
     P4  [table]  P1
       🥢    🥢
     P3   🥢   P2
```

**Naive Solution (DEADLOCK!):**

```c
semaphore chopstick[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    while (true) {
        wait(&chopstick[i]);           // Pick left
        wait(&chopstick[(i+1) % 5]);   // Pick right
        
        eat();
        
        signal(&chopstick[i]);
        signal(&chopstick[(i+1) % 5]);
        
        think();
    }
}
// DEADLOCK: All pick left, none can pick right!
```

**Solutions to Prevent Deadlock:**

| Solution | Method | Drawback |
|----------|--------|----------|
| Allow max 4 philosophers | Limit concurrency | Resource underutilization |
| Pick both or none | Atomic pickup | Complex implementation |
| Asymmetric | Odd picks left first, even picks right first | Works but reduces parallelism |
| Resource hierarchy | Always pick lower-numbered first | Simple and effective |

**Resource Hierarchy Solution:**

```c
void philosopher(int i) {
    int first = min(i, (i+1) % 5);
    int second = max(i, (i+1) % 5);
    
    wait(&chopstick[first]);
    wait(&chopstick[second]);
    
    eat();
    
    signal(&chopstick[first]);
    signal(&chopstick[second]);
    
    think();
}
```

---

### 5.5.4 Sleeping Barber Problem

**Setup:** Barber sleeps if no customers, customers wait if barber busy (limited chairs).

```c
semaphore customers = 0;   // Waiting customers
semaphore barber = 0;      // Barber ready
semaphore mutex = 1;       // For waiting count
int waiting = 0;           // Customers waiting
int CHAIRS = N;            // Waiting chairs

void barber_process() {
    while (true) {
        wait(&customers);  // Sleep if no customers
        wait(&mutex);
        waiting--;
        signal(&barber);   // Barber ready
        signal(&mutex);
        
        cut_hair();
    }
}

void customer_process() {
    wait(&mutex);
    if (waiting < CHAIRS) {
        waiting++;
        signal(&customers);  // Wake barber
        signal(&mutex);
        wait(&barber);       // Wait for barber
        get_haircut();
    } else {
        signal(&mutex);      // Leave (no chairs)
    }
}
```

---

## 5.6 Monitors

### Definition
A **Monitor** is a high-level synchronization construct that encapsulates shared data and procedures.

### Monitor Properties
- Only one process can execute monitor procedure at a time
- Automatic mutual exclusion
- Condition variables for synchronization

### Monitor Structure

```
┌───────────────────────────────────┐
│            MONITOR                │
│  ┌─────────────────────────────┐  │
│  │     Shared Data             │  │
│  │  (variables, data structures)│  │
│  └─────────────────────────────┘  │
│                                   │
│  ┌─────────────────────────────┐  │
│  │     Condition Variables     │  │
│  │  condition x, y;            │  │
│  └─────────────────────────────┘  │
│                                   │
│  ┌─────────────────────────────┐  │
│  │     Procedures              │  │
│  │  procedure P1() { ... }     │  │
│  │  procedure P2() { ... }     │  │
│  └─────────────────────────────┘  │
│                                   │
│  ┌─────────────────────────────┐  │
│  │  Initialization Code        │  │
│  └─────────────────────────────┘  │
└───────────────────────────────────┘
```

### Condition Variables

| Operation | Effect |
|-----------|--------|
| `x.wait()` | Suspend calling process, release monitor |
| `x.signal()` | Resume one waiting process |

**Key Difference from Semaphores:**
- `signal()` on condition with no waiters has no effect
- `signal()` on semaphore always increments

### Hoare vs Mesa Monitors

| Aspect | Hoare | Mesa |
|--------|-------|------|
| After signal | Signaler waits, signaled runs | Signaler continues |
| Wait behavior | Condition guaranteed | Must recheck condition |
| Common in | Theory | Practice (Java, C#) |

**Mesa-style usage:**
```java
while (!condition)
    x.wait();
```

---

## 5.7 Common Synchronization Patterns

### Pattern 1: Mutual Exclusion
```c
semaphore mutex = 1;
wait(&mutex);
// Critical Section
signal(&mutex);
```

### Pattern 2: Signaling/Rendezvous
```c
// Process A signals Process B
semaphore s = 0;

// Process A
do_something();
signal(&s);  // Signal B

// Process B
wait(&s);    // Wait for A
do_something_after_A();
```

### Pattern 3: Turnstile
```c
// Let processes through one at a time
wait(&turnstile);
// Pass through
signal(&turnstile);
```

### Pattern 4: Barrier
```c
// All processes wait until everyone arrives
semaphore mutex = 1;
semaphore barrier = 0;
int count = 0;

wait(&mutex);
count++;
if (count == N) {
    signal(&barrier);  // Last one opens barrier
}
signal(&mutex);
wait(&barrier);
signal(&barrier);  // Let next through
```

---

## 5.8 Semaphore Invariants

### Key Theorem
For a semaphore S initialized to $S_0$:

$$S = S_0 + \text{signals} - \text{waits}$$

### Constraints
- $S \geq 0$ for wait to proceed
- $|S| =$ processes blocked (when $S < 0$ in blocking implementation)

---

## 🎯 GATE PYQ Analysis

### Question 1 (GATE 2018)
**Q:** Two processes P1 and P2 use semaphores s1=0, s2=0:

```
P1:             P2:
A1              B1
wait(s1)        wait(s2)
A2              B2
signal(s2)      signal(s1)
```

Which statement is true?
(a) A1 and B1 can execute in any order
(b) A2 will execute before B2
(c) Deadlock will occur
(d) A1, B1, A2, B2 execute sequentially

**Solution:**
- P1: Does A1, then waits on s1 (blocks since s1=0)
- P2: Does B1, then waits on s2 (blocks since s2=0)
- **Deadlock!** Neither can signal the other.

**Answer:** (c)

---

### Question 2 (GATE 2019)
**Q:** In Producer-Consumer, what happens if we swap wait order?

```c
wait(&mutex);     // Instead of wait(&empty);
wait(&empty);     // Instead of wait(&mutex);
```

**Answer:** Deadlock when buffer is full. Producer holds mutex, waits for empty slot, but consumer needs mutex to free a slot.

---

### Question 3 (GATE 2020)
**Q:** Initial semaphore value S=2. Operations: P, V, P, P, V, P. Final value?

**Solution:**
- Start: S = 2
- P (wait): S = 1
- V (signal): S = 2
- P: S = 1
- P: S = 0
- V: S = 1
- P: S = 0

**Answer:** 0

---

## 🧠 Memory Tricks

### Mnemonic: Critical Section "MPB"
- **M**utual Exclusion: One at a time
- **P**rogress: Don't delay unnecessarily
- **B**ounded Waiting: No infinite waiting

### Mnemonic: P and V Operations
- **P** = Proberen (Dutch: test) = wait = **P**ass only if > 0 = Decrement
- **V** = Verhogen (Dutch: increment) = signal = **V**ery nice to increment

### The Mental Slider: Semaphore Value
Imagine a **parking lot counter**:
- Positive: Available spots
- Zero: Lot full
- Negative: Cars waiting (blocking implementation)

### Producer-Consumer Memory Hook
"**EMP-TY** first, then **MU**-tex" for producer:
- **EMP**ty (wait)
- **MU**tex (wait)
- ... work ...
- **MU**tex (signal)
- **FULL** (signal)

---

## ⚠️ Common GATE Traps

### Trap 1: Semaphore Initial Value
**Wrong:** Assuming binary semaphore starts at 0
**Right:** Check problem; mutex usually starts at 1

### Trap 2: wait() Order
**Wrong:** `wait(mutex); wait(resource);`
**Right:** `wait(resource); wait(mutex);` to avoid deadlock

### Trap 3: Monitor signal()
**Wrong:** Treating monitor signal like semaphore signal
**Right:** Monitor signal has no effect if no waiters

### Trap 4: Counting Semaphores
**Wrong:** Thinking value can't go below 0
**Right:** In blocking implementation, $S < 0$ means $|S|$ processes waiting

---

## 📝 Practice Problems

### Problem 1: Semaphore Tracing
Initial: S1=1, S2=0

```
P1:              P2:
wait(S1)         wait(S2)
print("A")       print("C")
signal(S2)       wait(S1)
wait(S2)         print("D")
print("B")       signal(S1)
signal(S1)       signal(S2)
```

What are possible outputs?

### Problem 2: Readers-Writers
Maximum concurrent readers = 5. Design with semaphores.

### Problem 3: Barrier Implementation
3 processes must reach a barrier before any proceeds. Show semaphore solution.

---

## 🔗 Quick Reference

| Concept | Key Point |
|---------|-----------|
| Critical Section | Mutual exclusion required |
| Peterson's | Two-process software solution |
| TAS/CAS | Atomic hardware instructions |
| Semaphore | wait() decrements, signal() increments |
| Binary Semaphore | 0 or 1 (like lock) |
| Counting Semaphore | Track resource count |
| Monitor | Automatic mutual exclusion |
| Condition Variable | wait() and signal() for conditions |

### Classic Problems Summary

| Problem | Key Semaphores |
|---------|----------------|
| Producer-Consumer | mutex, empty, full |
| Readers-Writers | rw_mutex, mutex, read_count |
| Dining Philosophers | chopstick[5], need deadlock prevention |
| Sleeping Barber | customers, barber, mutex |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Next: [Chapter 6 - Deadlocks](../06-Deadlocks/README.md)*
