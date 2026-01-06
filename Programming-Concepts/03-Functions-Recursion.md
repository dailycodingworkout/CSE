# Chapter 3: Functions & Recursion
## The Modular Powerhouse | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Functions are black boxes; Recursion is a function calling its mirror."**

---

## 3.1 Function Fundamentals

### Function Anatomy

```c
return_type function_name(parameter_list) {
    // function body
    return value;  // if non-void
}
```

### Function Components

| Component | Description | Example |
|-----------|-------------|---------|
| Return type | Data type of returned value | `int`, `void`, `float*` |
| Name | Identifier following naming rules | `calculateSum` |
| Parameters | Input variables (formal parameters) | `(int a, int b)` |
| Body | The actual code | `{ return a + b; }` |
| Return statement | Value sent back to caller | `return result;` |

### Declaration vs Definition

```c
// Declaration (Prototype) - tells compiler function exists
int add(int, int);  // Parameter names optional

// Definition - actual implementation
int add(int a, int b) {
    return a + b;
}
```

**GATE Insight:** Declaration without definition → Linker error, not compiler error.

---

## 3.2 Parameter Passing Mechanisms

### 3.2.1 Pass by Value (C Default)

```c
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(x, y);
    printf("%d %d", x, y);  // Output: 5 10 (NO SWAP!)
    return 0;
}
```

**Why?** `a` and `b` are COPIES. Original variables unchanged.

### 3.2.2 Pass by Reference (Using Pointers)

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(&x, &y);
    printf("%d %d", x, y);  // Output: 10 5 (SWAPPED!)
    return 0;
}
```

### 3.2.3 Array Passing

```c
void modifyArray(int arr[], int size) {
    arr[0] = 100;  // MODIFIES original array!
}

int main() {
    int arr[] = {1, 2, 3};
    modifyArray(arr, 3);
    printf("%d", arr[0]);  // Output: 100
    return 0;
}
```

**Key Insight:** Arrays ALWAYS pass by reference (decay to pointers).

### 🧠 Passing Comparison Table

| What's Passed | Actual Mechanism | Original Changed? |
|---------------|------------------|-------------------|
| Primitive (int, char) | By Value | No |
| Pointer | By Value (pointer copied) | Yes (via pointer) |
| Array | By Reference (decays to pointer) | Yes |
| Struct | By Value | No (unless pointer) |

---

## 3.3 The Call Stack - Function's Memory Model

### Stack Frame (Activation Record)

When a function is called, a **stack frame** is created containing:
1. Return address
2. Parameters
3. Local variables
4. Saved registers

```
┌─────────────────────────────────────┐ High Address
│          main() frame               │
│   - local variables                 │
│   - return address                  │
├─────────────────────────────────────┤
│          func1() frame              │
│   - local variables                 │
│   - parameters                      │
│   - return address                  │
├─────────────────────────────────────┤
│          func2() frame              │  ← Stack Pointer
│   - local variables                 │
│   - parameters                      │
│   - return address                  │
└─────────────────────────────────────┘ Low Address
        Stack grows downward ↓
```

### 🎯 GATE 2020 Style: Stack Trace

```c
void C() { printf("C "); }
void B() { printf("B "); C(); printf("B' "); }
void A() { printf("A "); B(); printf("A' "); }
int main() { A(); return 0; }
```

**Output:** `A B C B' A'`

**Stack Evolution:**
1. main() calls A() → push A
2. A() calls B() → push B
3. B() calls C() → push C
4. C() returns → pop C
5. B() returns → pop B
6. A() returns → pop A

---

## 3.4 Recursion - The Self-Referential Magic

### The Recursion Formula

Every recursive function has:
1. **Base Case(s):** Termination condition
2. **Recursive Case(s):** Function calls itself with smaller input
3. **Progress toward base case:** Ensures termination

### Factorial Example

```c
int factorial(int n) {
    // Base case
    if (n <= 1) return 1;
    
    // Recursive case
    return n * factorial(n - 1);
}
```

**Execution Trace for factorial(4):**
```
factorial(4) = 4 * factorial(3)
             = 4 * (3 * factorial(2))
             = 4 * (3 * (2 * factorial(1)))
             = 4 * (3 * (2 * 1))
             = 4 * (3 * 2)
             = 4 * 6
             = 24
```

### 📊 Stack Frames for Recursion

```
factorial(4)  → Return: 4 * factorial(3)
  factorial(3) → Return: 3 * factorial(2)
    factorial(2) → Return: 2 * factorial(1)
      factorial(1) → Return: 1 (Base case hit!)
    factorial(2) → Returns 2 * 1 = 2
  factorial(3) → Returns 3 * 2 = 6
factorial(4) → Returns 4 * 6 = 24
```

---

## 3.5 Types of Recursion

### 3.5.1 Linear Recursion

One recursive call per function invocation.

```c
int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
```

### 3.5.2 Tail Recursion

Recursive call is the **last** operation.

```c
// Not tail recursive - multiplication after call
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  // multiply AFTER return
}

// Tail recursive version
int factorial_tail(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_tail(n - 1, n * acc);  // No operation after
}
```

**Advantage:** Compiler can optimize tail recursion to iteration (no extra stack frames).

### 3.5.3 Binary Recursion

Two recursive calls per invocation.

```c
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Time Complexity:** $O(2^n)$ - exponential!

### 3.5.4 Mutual Recursion

Functions call each other.

```c
int isEven(int n);  // Forward declaration

int isOdd(int n) {
    if (n == 0) return 0;
    return isEven(n - 1);
}

int isEven(int n) {
    if (n == 0) return 1;
    return isOdd(n - 1);
}
```

### 3.5.5 Nested Recursion

Recursive call as argument to recursive call.

```c
int ackermann(int m, int n) {
    if (m == 0) return n + 1;
    if (n == 0) return ackermann(m - 1, 1);
    return ackermann(m - 1, ackermann(m, n - 1));  // Nested!
}
```

---

## 3.6 Recurrence Relations

### Common Recurrences

| Recurrence | Closed Form | Example |
|------------|-------------|---------|
| $T(n) = T(n-1) + 1$ | $O(n)$ | Linear search |
| $T(n) = T(n-1) + n$ | $O(n^2)$ | Sum of 1 to n |
| $T(n) = 2T(n-1) + 1$ | $O(2^n)$ | Tower of Hanoi |
| $T(n) = T(n/2) + 1$ | $O(\log n)$ | Binary search |
| $T(n) = 2T(n/2) + n$ | $O(n \log n)$ | Merge sort |
| $T(n) = 2T(n/2) + 1$ | $O(n)$ | Binary tree traversal |
| $T(n) = T(n-1) + T(n-2)$ | $O(\phi^n) \approx O(1.618^n)$ | Fibonacci |

### Master Theorem (Quick Reference)

For $T(n) = aT(n/b) + f(n)$:

Let $c = \log_b a$

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $f(n) = O(n^{c-\epsilon})$ | $T(n) = \Theta(n^c)$ |
| 2 | $f(n) = \Theta(n^c \log^k n)$ | $T(n) = \Theta(n^c \log^{k+1} n)$ |
| 3 | $f(n) = \Omega(n^{c+\epsilon})$ | $T(n) = \Theta(f(n))$ |

### 🎯 GATE Recurrence Solving

**Problem:** $T(n) = 2T(n/2) + n$

**Solution using Master Theorem:**
- $a = 2, b = 2, f(n) = n$
- $c = \log_2 2 = 1$
- $f(n) = n = \Theta(n^1) = \Theta(n^c)$
- Case 2 with $k = 0$
- $T(n) = \Theta(n \log n)$

---

## 3.7 Recursion vs Iteration

### Comparison

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Memory | O(n) stack space | O(1) typically |
| Speed | Slower (function call overhead) | Faster |
| Code | Often cleaner, shorter | May be verbose |
| Debugging | Harder (trace calls) | Easier |
| Termination | Base case | Loop condition |
| Use case | Tree/Graph, Divide & Conquer | Simple repetition |

### Converting Recursion to Iteration

**Recursive Factorial:**
```c
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

**Iterative Factorial:**
```c
int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}
```

### The Stack Simulation Technique

For non-tail recursion, simulate the call stack:

```c
// Converting recursive tree traversal to iterative
void inorderIterative(Node* root) {
    Stack* stack = createStack();
    Node* current = root;
    
    while (current != NULL || !isEmpty(stack)) {
        while (current != NULL) {
            push(stack, current);
            current = current->left;
        }
        current = pop(stack);
        printf("%d ", current->data);
        current = current->right;
    }
}
```

---

## 3.8 Classic Recursive Problems

### 3.8.1 Tower of Hanoi

```c
void hanoi(int n, char from, char aux, char to) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", from, to);
        return;
    }
    hanoi(n - 1, from, to, aux);
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n - 1, aux, from, to);
}
```

**Number of moves:** $2^n - 1$

**Recurrence:** $T(n) = 2T(n-1) + 1$

### 3.8.2 Fibonacci Optimization

**Naive (Exponential):**
```c
int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
```

**Memoized (Linear):**
```c
int memo[100] = {0};

int fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
}
```

### 3.8.3 GCD (Euclid's Algorithm)

```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

**Time Complexity:** $O(\log(\min(a, b)))$

### 3.8.4 Power Function

```c
// O(n) version
int power(int x, int n) {
    if (n == 0) return 1;
    return x * power(x, n - 1);
}

// O(log n) version - Fast Exponentiation
int power(int x, int n) {
    if (n == 0) return 1;
    int half = power(x, n / 2);
    if (n % 2 == 0)
        return half * half;
    else
        return x * half * half;
}
```

---

## 3.9 Function Pointers

### Declaration and Usage

```c
// Declaration
return_type (*pointer_name)(parameter_types);

// Example
int (*funcPtr)(int, int);

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int main() {
    funcPtr = add;
    printf("%d\n", funcPtr(5, 3));  // Output: 8
    
    funcPtr = sub;
    printf("%d\n", funcPtr(5, 3));  // Output: 2
    
    return 0;
}
```

### Array of Function Pointers

```c
int (*operations[4])(int, int) = {add, sub, mul, div};
int result = operations[0](10, 5);  // Calls add(10, 5)
```

### Callback Functions

```c
void sortArray(int arr[], int n, int (*compare)(int, int)) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (compare(arr[j], arr[j+1]) > 0)
                swap(&arr[j], &arr[j+1]);
}

int ascending(int a, int b) { return a - b; }
int descending(int a, int b) { return b - a; }

// Usage
sortArray(arr, n, ascending);   // Sort ascending
sortArray(arr, n, descending);  // Sort descending
```

---

## 3.10 Variable Arguments (varargs)

```c
#include <stdarg.h>

int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    
    int total = 0;
    for (int i = 0; i < count; i++)
        total += va_arg(args, int);
    
    va_end(args);
    return total;
}

int main() {
    printf("%d\n", sum(3, 10, 20, 30));  // Output: 60
    printf("%d\n", sum(5, 1, 2, 3, 4, 5));  // Output: 15
    return 0;
}
```

---

## 3.11 Static Variables in Functions

```c
void counter() {
    static int count = 0;  // Initialized only once!
    count++;
    printf("%d ", count);
}

int main() {
    counter();  // 1
    counter();  // 2
    counter();  // 3
    return 0;
}
```

**Key Points:**
- Static variables retain value between calls
- Initialized only once (at program start)
- Stored in Data segment, not Stack

---

## 🎯 Practice Problems

### Problem 1: Function Output (GATE 2018)
```c
int fun(int n) {
    if (n == 0) return 1;
    return 2 * fun(n - 1);
}
```
**Q:** What does `fun(4)` return?
**Answer:** $2^4 = 16$

### Problem 2: Recursion Count
```c
int f(int n) {
    if (n <= 1) return 1;
    return f(n - 1) + f(n - 2);
}
```
**Q:** How many times is `f()` called for `f(5)`?
**Answer:** Count recursion tree nodes = 15

### Problem 3: Mystery Function
```c
int mystery(int a, int b) {
    if (b == 0) return 0;
    if (b % 2 == 0)
        return mystery(a + a, b / 2);
    return mystery(a + a, b / 2) + a;
}
```
**Q:** What does `mystery(3, 5)` return?
**Answer:** 15 (It computes a * b!)

### Problem 4: Parameter Passing
```c
void fun(int *p) {
    static int q = 10;
    p = &q;
}

int main() {
    int r = 20;
    int *p = &r;
    fun(p);
    printf("%d", *p);
    return 0;
}
```
**Answer:** 20 (pointer itself is passed by value)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"The recursive rabbit went down the hole to find smaller rabbits, who went down smaller holes, until the tiniest rabbit found a carrot (base case) and passed it up through all the holes, each rabbit adding their bit."**

### The Mental Slider
Imagine a telescope that extends:
- Each recursive call EXTENDS the telescope (push to stack)
- Base case is hitting the wall
- Each return COLLAPSES one segment (pop from stack)
- Final answer emerges from the eyepiece

### The 5-Second Snap-Check
1. **Stack overflow?** Check base case is reachable
2. **Wrong answer?** Verify base case returns correct value
3. **Infinite recursion?** Check progress toward base case
4. **Memory issue?** Consider tail recursion or iteration
5. **Time complexity?** Draw recursion tree

---

## 📈 Complexity Summary

| Function Pattern | Time | Space |
|-----------------|------|-------|
| Linear recursion (1 call) | O(n) | O(n) |
| Tail recursion (optimized) | O(n) | O(1) |
| Binary recursion | O(2^n) | O(n) |
| Divide & Conquer | O(n log n) typical | O(log n) |
| Memoized recursion | O(n) typical | O(n) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Control Flow](02-Control-Flow.md) | [Next: Arrays & Strings →](04-Arrays-Strings.md)
