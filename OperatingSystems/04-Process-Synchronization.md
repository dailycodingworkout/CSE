# Chapter 4: Process Synchronization

> **"Process synchronization is like coordinating dance partners - they must move in harmony to avoid stepping on each other's toes"**

---

## 🎯 Why Process Synchronization?

When multiple processes access **shared data** concurrently, the outcome depends on the order of execution → **Race Condition**

### Race Condition Example

```c
// Shared variable
int counter = 5;

// Process P1: counter++
register1 = counter;    // register1 = 5
register1 = register1 + 1;  // register1 = 6
counter = register1;    // counter = 6

// Process P2: counter--
register2 = counter;    // register2 = 5
register2 = register2 - 1;  // register2 = 4
counter = register2;    // counter = 4
```

**Possible Interleaving:**
```
P1: register1 = counter    (register1 = 5)
P1: register1 = register1 + 1   (register1 = 6)
P2: register2 = counter    (register2 = 5)
P2: register2 = register2 - 1   (register2 = 4)
P1: counter = register1    (counter = 6)
P2: counter = register2    (counter = 4)  ← WRONG! Should be 5
```

**💡 Key Insight:** counter++ and counter-- are NOT atomic operations

---

## 🔒 Critical Section Problem

### Definitions

| Term | Definition |
|------|------------|
| **Critical Section** | Code segment accessing shared data |
| **Entry Section** | Code requesting entry to CS |
| **Exit Section** | Code after leaving CS |
| **Remainder Section** | Non-critical code |

### Process Structure
```c
while (true) {
    // Entry Section
    
    // Critical Section
    // (access shared resources)
    
    // Exit Section
    
    // Remainder Section
}
```

---

### Three Requirements for Valid Solution

| Requirement | Description | Analogy |
|-------------|-------------|---------|
| **Mutual Exclusion** | Only ONE process in CS at a time | One person in bathroom |
| **Progress** | If no process in CS, decision cannot be postponed indefinitely | Door doesn't stay locked forever when empty |
| **Bounded Waiting** | Limit on how many times others can enter before your turn | Queue with max wait time |

**⚠️ GATE Trap:** All three must be satisfied. Most wrong solutions violate Progress or Bounded Waiting.

---

## 🔓 Software Solutions

### Peterson's Solution (2 Processes)

```c
// Shared variables
int turn;           // Whose turn to enter
bool flag[2];       // Ready to enter

// Process Pi (i = 0 or 1, j = 1-i)
flag[i] = true;         // I'm interested
turn = j;               // But you go first
while (flag[j] && turn == j);  // Wait if you're interested AND it's your turn
    // Critical Section
flag[i] = false;        // I'm done
    // Remainder Section
```

**Why it works:**
- **Mutual Exclusion:** Both can't be in CS (one's turn must be j)
- **Progress:** Decision made by turn variable
- **Bounded Waiting:** After you exit, other gets turn

**💡 Memory Trick:** "FLAG + TURN = PETERSON"
- Flag says "I want in"
- Turn says "but you can go first"

---

### Bakery Algorithm (n Processes)

**🧠 Analogy:** Taking a number at a bakery counter

```c
// Shared variables
bool choosing[n];   // Is process taking a number?
int number[n];      // Ticket number

// Process Pi
choosing[i] = true;
number[i] = max(number[0], ..., number[n-1]) + 1;
choosing[i] = false;

for (j = 0; j < n; j++) {
    while (choosing[j]);    // Wait while j is choosing
    while (number[j] != 0 && 
           (number[j], j) < (number[i], i));  // Wait for smaller tickets
}
    // Critical Section
number[i] = 0;
    // Remainder Section
```

**Comparison (a, b) < (c, d):** First compare a vs c, then b vs d as tiebreaker

---

## ⚙️ Hardware Solutions

### Test-and-Set (TAS)

```c
// ATOMIC instruction
bool TestAndSet(bool *target) {
    bool rv = *target;
    *target = true;
    return rv;
}

// Usage
bool lock = false;

// Entry section
while (TestAndSet(&lock));  // Busy wait
    // Critical Section
lock = false;  // Exit section
```

**Problem:** No bounded waiting (starvation possible)

---

### Compare-and-Swap (CAS)

```c
// ATOMIC instruction
int CompareAndSwap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected)
        *value = new_value;
    return temp;
}

// Usage
int lock = 0;

// Entry section
while (CompareAndSwap(&lock, 0, 1) != 0);
    // Critical Section
lock = 0;  // Exit section
```

---

### Test-and-Set with Bounded Waiting

```c
bool waiting[n];  // All false initially
bool lock = false;

// Process Pi
waiting[i] = true;
bool key = true;
while (waiting[i] && key)
    key = TestAndSet(&lock);
waiting[i] = false;

    // Critical Section

// Find next waiting process
int j = (i + 1) % n;
while (j != i && !waiting[j])
    j = (j + 1) % n;

if (j == i)
    lock = false;       // No one waiting
else
    waiting[j] = false; // Pass to j
```

---

## 🚦 Semaphores

### Definition
A semaphore S is an integer variable accessed only through:
- **wait(S)** or P(S): Decrement and possibly block
- **signal(S)** or V(S): Increment and possibly wake

### Implementation

```c
// Binary Semaphore (Mutex) - value: 0 or 1
// Counting Semaphore - value: 0 to n

wait(S) {       // Also called P, down, acquire
    while (S <= 0);  // Busy wait
    S--;
}

signal(S) {     // Also called V, up, release
    S++;
}
```

**💡 GATE Trick:** 
- P = Proberen (Dutch for "test") = Down = Wait
- V = Verhogen (Dutch for "increment") = Up = Signal

---

### Blocking Implementation (No Busy Wait)

```c
typedef struct {
    int value;
    struct process *list;  // Waiting queue
} semaphore;

void wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        add this process to S->list;
        block();
    }
}

void signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        remove a process P from S->list;
        wakeup(P);
    }
}
```

**Key Insight:** |S->value| when negative = number of waiting processes

---

### Semaphore Types

| Type | Value Range | Use Case |
|------|-------------|----------|
| **Binary (Mutex)** | 0 or 1 | Mutual exclusion |
| **Counting** | 0 to n | Resource counting |

---

### Using Semaphore for Mutual Exclusion

```c
semaphore mutex = 1;  // Initialize to 1

// Process Pi
wait(mutex);
    // Critical Section
signal(mutex);
    // Remainder Section
```

**Why initialized to 1?** First process can enter; subsequent must wait

---

### Using Semaphore for Synchronization

**Problem:** Ensure S1 in P1 executes before S2 in P2

```c
semaphore sync = 0;  // Initialize to 0

// Process P1            // Process P2
S1;                      wait(sync);
signal(sync);            S2;
```

**Explanation:** P2 blocks until P1 signals

---

## 🔢 Classic Synchronization Problems

### 1️⃣ Producer-Consumer (Bounded Buffer)

**Problem:** Producers add items to buffer, Consumers remove items

```
┌───────────────────────────────────┐
│   Buffer (size n)                 │
│ ┌───┬───┬───┬───┬───┬───┬───┐   │
│ │   │ X │ X │ X │   │   │   │   │
│ └───┴───┴───┴───┴───┴───┴───┘   │
│       ↑               ↑          │
│       Producer adds   Consumer   │
│       here           removes     │
└───────────────────────────────────┘
```

**Semaphores:**
```c
semaphore mutex = 1;    // For critical section
semaphore empty = n;    // Empty slots
semaphore full = 0;     // Full slots
```

**Producer:**
```c
while (true) {
    // Produce item
    wait(empty);        // Wait for empty slot
    wait(mutex);        // Enter CS
    // Add item to buffer
    signal(mutex);      // Exit CS
    signal(full);       // Signal full slot
}
```

**Consumer:**
```c
while (true) {
    wait(full);         // Wait for full slot
    wait(mutex);        // Enter CS
    // Remove item from buffer
    signal(mutex);      // Exit CS
    signal(empty);      // Signal empty slot
    // Consume item
}
```

**⚠️ GATE Trap:** Order matters!
- wait(empty) before wait(mutex) → prevents deadlock
- If reversed: Producer holds mutex, waits for empty; Consumer can't signal empty

---

### 2️⃣ Readers-Writers Problem

**Problem:** Multiple readers can read simultaneously, but writers need exclusive access

**First Readers-Writers (Readers Preference):**
```c
semaphore rw_mutex = 1;   // For writers
semaphore mutex = 1;       // For read_count
int read_count = 0;        // Active readers
```

**Writer:**
```c
wait(rw_mutex);
    // Write
signal(rw_mutex);
```

**Reader:**
```c
wait(mutex);
read_count++;
if (read_count == 1)
    wait(rw_mutex);        // First reader locks
signal(mutex);

    // Read

wait(mutex);
read_count--;
if (read_count == 0)
    signal(rw_mutex);      // Last reader unlocks
signal(mutex);
```

**Problem with First Solution:** Writers may starve

**Second Readers-Writers (Writers Preference):**
- Add semaphore to give writers priority
- Readers check if writer is waiting

---

### 3️⃣ Dining Philosophers Problem

**Problem:** 5 philosophers, 5 chopsticks, need 2 chopsticks to eat

```
        P0
    C4      C0
  P4          P1
    C3      C1
        P2
        C2
```

**Naive Solution (DEADLOCK!):**
```c
semaphore chopstick[5] = {1, 1, 1, 1, 1};

// Philosopher i
while (true) {
    wait(chopstick[i]);
    wait(chopstick[(i+1) % 5]);
    // Eat
    signal(chopstick[i]);
    signal(chopstick[(i+1) % 5]);
    // Think
}
```

**Problem:** All pick up left chopstick → All wait for right → DEADLOCK

---

**Solutions:**

1. **Allow at most 4 philosophers at table:**
```c
semaphore room = 4;

wait(room);
wait(chopstick[i]);
wait(chopstick[(i+1) % 5]);
// Eat
signal(chopstick[i]);
signal(chopstick[(i+1) % 5]);
signal(room);
```

2. **Asymmetric Solution:**
   - Odd philosophers: pick left first, then right
   - Even philosophers: pick right first, then left

3. **Pick up both or none (atomic):**
```c
wait(mutex);
// Pick up both chopsticks
signal(mutex);
// Eat
wait(mutex);
// Put down both chopsticks
signal(mutex);
```

---

### 4️⃣ Sleeping Barber Problem

**Setup:**
- 1 barber, 1 barber chair, n waiting chairs
- Barber sleeps if no customers
- Customer leaves if all chairs full

```c
semaphore customers = 0;   // Waiting customers
semaphore barber = 0;      // Barber ready?
semaphore mutex = 1;       // For count
int waiting = 0;           // Customers waiting
const int CHAIRS = n;      // Waiting chairs
```

**Barber:**
```c
while (true) {
    wait(customers);       // Sleep until customer
    wait(mutex);
    waiting--;
    signal(barber);        // Barber ready
    signal(mutex);
    // Cut hair
}
```

**Customer:**
```c
wait(mutex);
if (waiting < CHAIRS) {
    waiting++;
    signal(customers);     // Wake barber
    signal(mutex);
    wait(barber);          // Wait for barber
    // Get haircut
} else {
    signal(mutex);         // Leave (no chair)
}
```

---

## 🔒 Monitors

### Why Monitors?
Semaphores are error-prone:
- Forget signal → deadlock
- Forget wait → race condition
- Wrong order → bugs

### Monitor Structure

```c
monitor MonitorName {
    // Shared variables
    
    condition x, y;  // Condition variables
    
    procedure P1(...) {
        // ...
    }
    
    procedure P2(...) {
        // ...
    }
    
    initialization_code(...) {
        // ...
    }
}
```

**Key Properties:**
- Only ONE process active inside monitor at a time
- Mutual exclusion enforced automatically

---

### Condition Variables

**Two operations:**
- **x.wait():** Suspend calling process
- **x.signal():** Resume ONE waiting process (no effect if none waiting)

**⚠️ Different from Semaphore:**
- Semaphore signal: Always increments counter
- Condition signal: Lost if no one waiting

---

### Signal Semantics

| Type | After x.signal() |
|------|------------------|
| **Hoare** | Signaling process waits, awakened process runs immediately |
| **Mesa** | Signaling process continues, awakened process scheduled later |

**Mesa semantics (more common):** Use `while` instead of `if` for waiting

```c
// Mesa semantics
while (condition_not_met)
    x.wait();
```

---

### Dining Philosophers with Monitor

```c
monitor DiningPhilosophers {
    enum {THINKING, HUNGRY, EATING} state[5];
    condition self[5];
    
    void pickup(int i) {
        state[i] = HUNGRY;
        test(i);
        if (state[i] != EATING)
            self[i].wait();
    }
    
    void putdown(int i) {
        state[i] = THINKING;
        test((i + 4) % 5);  // Test left neighbor
        test((i + 1) % 5);  // Test right neighbor
    }
    
    void test(int i) {
        if (state[(i + 4) % 5] != EATING &&
            state[i] == HUNGRY &&
            state[(i + 1) % 5] != EATING) {
            state[i] = EATING;
            self[i].signal();
        }
    }
    
    initialization_code() {
        for (int i = 0; i < 5; i++)
            state[i] = THINKING;
    }
}
```

---

## 🔐 Mutex Locks

### Definition
Simplest synchronization tool - protect critical section

```c
acquire() {
    while (!available);  // Busy wait (spinlock)
    available = false;
}

release() {
    available = true;
}

// Usage
acquire(lock);
    // Critical Section
release(lock);
```

### Mutex vs Semaphore

| Aspect | Mutex | Semaphore |
|--------|-------|-----------|
| Value | Binary (0/1) | Any non-negative |
| Ownership | Only owner can release | Any process can signal |
| Use | Mutual exclusion | Sync + resource counting |
| Recursion | May support | Not typically |

---

## 🔄 Deadlock in Synchronization

**When two semaphores cause deadlock:**

```c
// Process P1             // Process P2
wait(S);                  wait(Q);
wait(Q);                  wait(S);
...                       ...
signal(Q);                signal(S);
signal(S);                signal(Q);
```

**Timeline:**
```
P1: wait(S)  → Gets S
P2: wait(Q)  → Gets Q
P1: wait(Q)  → Blocked (Q held by P2)
P2: wait(S)  → Blocked (S held by P1)
DEADLOCK!
```

**Solution:** Always acquire semaphores in same order

---

## 🧮 Priority Inversion

**Problem:** High-priority process blocked by low-priority process

```
Priority: H > M > L

1. L acquires lock, starts CS
2. H arrives, needs lock, blocked
3. M arrives (doesn't need lock), preempts L
4. H waits for L, L waits for M
5. Result: M runs before H (WRONG!)
```

**Solutions:**

1. **Priority Inheritance:**
   - L temporarily gets H's priority
   - L finishes CS, releases lock
   - H runs immediately

2. **Priority Ceiling:**
   - Lock has ceiling priority = max of all who might acquire it
   - Process acquiring lock gets ceiling priority

---

## ⚡ Read-Copy-Update (RCU)

**Modern technique for read-heavy workloads:**
- Readers proceed without locking
- Writers make copy, update, switch pointer
- Old data kept until no readers using it

**Best for:** Linked data structures with rare updates

---

## 📝 GATE PYQ Patterns

### Common Question Types:
1. **Semaphore initialization:** What value to start with?
2. **Deadlock detection:** Will this code deadlock?
3. **Mutual exclusion verification:** Does solution work?
4. **Producer-Consumer variants:** Buffer size, multiple producers
5. **Readers-Writers variants:** Starvation scenarios

### ⚠️ Edge Cases & Traps:
1. **wait before signal in Producer-Consumer** - Order matters!
2. **Semaphore value interpretation** - Negative = waiting processes
3. **Binary semaphore ≠ Mutex** - Ownership difference
4. **Condition variable signal is lost** - If no one waiting
5. **Peterson's needs memory barriers** - On modern hardware

---

## 🎯 Quick Revision Points

```
✓ Race condition = Incorrect result due to uncontrolled access
✓ CS requirements: Mutual Exclusion + Progress + Bounded Waiting
✓ Peterson's: flag[] + turn for 2 processes
✓ Semaphore: P (down/wait) and V (up/signal)
✓ Binary semaphore = 0 or 1, Counting = 0 to n
✓ Producer-Consumer: mutex + empty + full
✓ Readers-Writers: rw_mutex + mutex + read_count
✓ Dining Philosophers: deadlock if all pick left first
✓ Monitor: automatic mutual exclusion
✓ Condition variable: wait + signal (signal lost if none waiting)
✓ Priority Inversion: solved by Priority Inheritance
```

---

## 📚 Key Patterns

```
Mutual Exclusion Pattern:
semaphore mutex = 1;
wait(mutex);
  // Critical Section
signal(mutex);

Synchronization Pattern (S1 before S2):
semaphore sync = 0;
P1: S1; signal(sync);
P2: wait(sync); S2;

Resource Counting:
semaphore resource = n;  // n resources
wait(resource);  // Use one
  // Use resource
signal(resource);  // Release
```

---

[← Previous: CPU Scheduling](./03-CPU-Scheduling.md) | [Next: Deadlocks →](./05-Deadlocks.md)
