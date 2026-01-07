# Chapter 3: Functions and Recursion

## The Singularity | First Principles

> **The Atomic Truth:** "Function = Reusable code block with own scope."

---

## 3.1 Functions | The Building Blocks

### Anatomy of a Function

```c
return_type function_name(parameter_list) {
    // function body
    return value;  // if not void
}
```

### Function Declaration vs Definition

| Term | What It Does | Example |
|------|--------------|---------|
| Declaration (Prototype) | Tells compiler about signature | `int add(int, int);` |
| Definition | Provides actual implementation | Full function with body |

```c
// Declaration (prototype) - usually in header
int add(int a, int b);

// Definition - usually in source file
int add(int a, int b) {
    return a + b;
}
```

### Why Prototypes?

1. **Forward reference**: Call function before its definition
2. **Type checking**: Compiler validates arguments
3. **Modular design**: Separate interface from implementation

---

## 3.2 Parameter Passing Mechanisms

### Pass by Value (C Default)

```c
void modify(int x) {
    x = 100;  // Only modifies local copy
}

int main() {
    int a = 50;
    modify(a);
    printf("%d", a);  // Still 50!
    return 0;
}
```

**Analogy**: Like giving someone a **photocopy** of your document. They can scribble on it, but your original is safe.

### Simulating Pass by Reference

```c
void modify(int *x) {
    *x = 100;  // Modifies original through pointer
}

int main() {
    int a = 50;
    modify(&a);
    printf("%d", a);  // Now 100!
    return 0;
}
```

**Analogy**: Like giving someone **your home address**. They can go there and rearrange your furniture.

### Arrays are Always Passed by Reference

```c
void modify(int arr[], int n) {
    arr[0] = 999;  // Modifies original array!
}
```

**Why?** Arrays decay to pointers when passed to functions.

---

## 3.3 Return Statement

### Returning a Value

```c
int square(int x) {
    return x * x;  // Copies value to caller
}
```

### Returning a Pointer (CAREFUL!)

```c
// WRONG - Returning local variable address
int* getPointer() {
    int x = 10;
    return &x;  // x dies after function returns!
}

// CORRECT - Return heap memory or static
int* getPointer() {
    static int x = 10;  // Static persists
    return &x;
}

// CORRECT - Return dynamically allocated
int* getPointer() {
    int *p = malloc(sizeof(int));
    *p = 10;
    return p;  // Caller must free!
}
```

### Multiple Returns via Pointers

```c
void getMinMax(int arr[], int n, int *min, int *max) {
    *min = *max = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] < *min) *min = arr[i];
        if(arr[i] > *max) *max = arr[i];
    }
}

int lo, hi;
getMinMax(arr, n, &lo, &hi);
```

---

## 3.4 Scope and Lifetime

### Scope Rules

```c
int global = 10;  // File scope (visible everywhere)

void func() {
    int local = 20;  // Block scope (visible in func only)
    {
        int inner = 30;  // Block scope (visible in this block only)
    }
    // inner not accessible here
}
```

### Variable Shadowing

```c
int x = 10;  // Global

void func() {
    int x = 20;  // Local x shadows global x
    printf("%d", x);  // 20
    {
        int x = 30;  // Inner x shadows local x
        printf("%d", x);  // 30
    }
    printf("%d", x);  // Back to 20
}
```

### Lifetime Summary

| Storage Class | Scope | Lifetime | Default Value |
|--------------|-------|----------|---------------|
| auto (default) | Block | Block execution | Garbage |
| static | Block | Entire program | 0 |
| extern | Global | Entire program | 0 |
| register | Block | Block execution | Garbage |

---

## 3.5 Static Variables | The Persistence Trick

### Static Local Variables

```c
void counter() {
    static int count = 0;  // Initialized once
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

**Key Properties**:
1. Initialized only once (at program start)
2. Retains value between function calls
3. Stored in data segment (not stack)

### Static Functions

```c
static void helper() {
    // Only visible in this file
}
```

**Use Case**: Internal implementation functions not meant for external use.

---

## 3.6 Recursion | Functions Calling Themselves

### The Structure of Recursion

Every recursive function needs:
1. **Base Case**: Condition to stop recursion
2. **Recursive Case**: Function calls itself with simpler input
3. **Progress**: Each call moves toward base case

### Classic Example: Factorial

```c
int factorial(int n) {
    // Base case
    if(n <= 1) return 1;
    
    // Recursive case
    return n * factorial(n - 1);
}
```

### Execution Trace (Call Stack)

```
factorial(4)
├── 4 * factorial(3)
│   ├── 3 * factorial(2)
│   │   ├── 2 * factorial(1)
│   │   │   └── returns 1
│   │   └── returns 2 * 1 = 2
│   └── returns 3 * 2 = 6
└── returns 4 * 6 = 24
```

### The Call Stack Visualization

```
Stack grows ↓

┌──────────────┐
│ factorial(1) │  ← Top of stack
├──────────────┤
│ factorial(2) │
├──────────────┤
│ factorial(3) │
├──────────────┤
│ factorial(4) │
├──────────────┤
│    main()    │  ← Bottom
└──────────────┘
```

---

## 3.7 Types of Recursion

### 1. Linear Recursion

One recursive call per function invocation.

```c
int sum(int n) {
    if(n == 0) return 0;
    return n + sum(n - 1);
}
```

### 2. Tail Recursion

Recursive call is the **last operation**.

```c
int factorial_tail(int n, int acc) {
    if(n <= 1) return acc;
    return factorial_tail(n - 1, n * acc);  // Tail call
}

// Usage: factorial_tail(5, 1)
```

**Optimization**: Tail recursion can be optimized to iteration by compiler (no stack growth).

### 3. Binary/Tree Recursion

Multiple recursive calls per invocation.

```c
int fibonacci(int n) {
    if(n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);  // Two calls
}
```

**Time Complexity**: $O(2^n)$ - Exponential!

### 4. Mutual Recursion

Two or more functions call each other.

```c
int isEven(int n);
int isOdd(int n);

int isEven(int n) {
    if(n == 0) return 1;
    return isOdd(n - 1);
}

int isOdd(int n) {
    if(n == 0) return 0;
    return isEven(n - 1);
}
```

---

## 3.8 Recursion vs Iteration

### Comparison

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Memory | O(n) stack space | O(1) |
| Speed | Slower (call overhead) | Faster |
| Code | Often more elegant | May be verbose |
| Risk | Stack overflow | None |
| Use | Tree/graph, divide & conquer | Simple loops |

### Converting Recursion to Iteration

**Factorial - Recursive**:
```c
int fact(int n) {
    if(n <= 1) return 1;
    return n * fact(n - 1);
}
```

**Factorial - Iterative**:
```c
int fact(int n) {
    int result = 1;
    for(int i = 2; i <= n; i++)
        result *= i;
    return result;
}
```

---

## 3.9 Classic Recursive Problems | GATE Favorites

### 1. Fibonacci Series

```c
// Naive - O(2^n)
int fib(int n) {
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

// Optimized with memoization - O(n)
int memo[1000];
int fib_memo(int n) {
    if(n <= 1) return n;
    if(memo[n] != 0) return memo[n];
    return memo[n] = fib_memo(n-1) + fib_memo(n-2);
}
```

### 2. Tower of Hanoi

```c
void hanoi(int n, char from, char aux, char to) {
    if(n == 0) return;
    
    hanoi(n-1, from, to, aux);      // Move n-1 disks to auxiliary
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n-1, aux, from, to);      // Move n-1 disks to destination
}

// Usage: hanoi(3, 'A', 'B', 'C');
```

**Number of moves**: $2^n - 1$

### 3. Sum of Digits

```c
int sumDigits(int n) {
    if(n == 0) return 0;
    return (n % 10) + sumDigits(n / 10);
}
```

### 4. Reverse a String

```c
void reverse(char *str, int start, int end) {
    if(start >= end) return;
    
    // Swap
    char temp = str[start];
    str[start] = str[end];
    str[end] = temp;
    
    reverse(str, start + 1, end - 1);
}
```

### 5. Binary Search (Recursive)

```c
int binarySearch(int arr[], int low, int high, int key) {
    if(low > high) return -1;
    
    int mid = low + (high - low) / 2;
    
    if(arr[mid] == key) return mid;
    if(arr[mid] > key) return binarySearch(arr, low, mid - 1, key);
    return binarySearch(arr, mid + 1, high, key);
}
```

### 6. GCD (Euclidean Algorithm)

```c
int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b, a % b);
}
```

**Visualization**:
```
gcd(48, 18)
├── gcd(18, 12)   [48 % 18 = 12]
│   ├── gcd(12, 6)   [18 % 12 = 6]
│   │   ├── gcd(6, 0)    [12 % 6 = 0]
│   │   │   └── returns 6
```

---

## 3.10 Recurrence Relations | GATE Mathematics

### Solving Recurrences for Recursion

| Function Pattern | Recurrence | Solution |
|-----------------|------------|----------|
| Linear | $T(n) = T(n-1) + c$ | $O(n)$ |
| Binary | $T(n) = T(n-1) + T(n-2)$ | $O(2^n)$ |
| Binary Search | $T(n) = T(n/2) + c$ | $O(\log n)$ |
| Merge Sort | $T(n) = 2T(n/2) + n$ | $O(n \log n)$ |

### The Master Theorem (Quick Reference)

For $T(n) = aT(n/b) + f(n)$:

Compare $f(n)$ with $n^{\log_b a}$:

1. If $f(n) = O(n^{\log_b a - \epsilon})$: $T(n) = \Theta(n^{\log_b a})$
2. If $f(n) = \Theta(n^{\log_b a})$: $T(n) = \Theta(n^{\log_b a} \log n)$
3. If $f(n) = \Omega(n^{\log_b a + \epsilon})$: $T(n) = \Theta(f(n))$

---

## 3.11 Stack Overflow | The Recursion Limit

### What Causes It?

```c
void infinite() {
    infinite();  // No base case!
}
```

Each call adds a frame to the stack. Stack is limited (typically 1-8 MB).

### GATE Pattern: Maximum Recursion Depth

**Question**: If stack size is 1 MB and each frame uses 100 bytes, max depth?

$$\text{Max Depth} = \frac{1 \times 1024 \times 1024}{100} = 10485$$

### Preventing Stack Overflow

1. Use iteration for deep recursions
2. Implement tail recursion (compiler may optimize)
3. Use explicit stack data structure

---

## 3.12 Function Call Stack | Detailed View

### Stack Frame Contents

Each function call creates a stack frame containing:
1. Return address
2. Saved registers
3. Local variables
4. Function parameters
5. Previous frame pointer

### Example Analysis

```c
int foo(int x) {
    int y = x + 1;
    return y;
}

int main() {
    int a = 5;
    int b = foo(a);
    return 0;
}
```

**Stack during foo() execution**:
```
┌───────────────────┐ ← Stack Pointer (SP)
│  y = 6            │  Local variable
├───────────────────┤
│  x = 5            │  Parameter
├───────────────────┤
│  Return Address   │  Points to main after foo() call
├───────────────────┤
│  Old Frame Ptr    │
├───────────────────┤
│  a = 5            │  main's local
├───────────────────┤
│  Return Address   │  Points to OS
└───────────────────┘ ← Frame Pointer (FP)
```

---

## 3.13 Inline Functions

### Definition

```c
inline int square(int x) {
    return x * x;
}
```

### How It Works

Compiler replaces function call with function body:

```c
int a = square(5);  // Becomes: int a = 5 * 5;
```

### Pros and Cons

| Pros | Cons |
|------|------|
| No call overhead | Code bloat |
| Better optimization | Compile time increase |
| | Not always inlined (compiler decides) |

---

## 3.14 Variable Length Arguments (varargs)

### Using stdarg.h

```c
#include <stdarg.h>

int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    
    int total = 0;
    for(int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    
    va_end(args);
    return total;
}

// Usage
int result = sum(4, 10, 20, 30, 40);  // 100
```

### How printf Works

```c
int printf(const char *format, ...);
```

The format string tells printf how many arguments to expect and their types.

---

## 3.15 Common GATE Patterns

### Pattern 1: Recursion Output Tracing

```c
void fun(int n) {
    if(n > 0) {
        printf("%d ", n);
        fun(n - 1);
        printf("%d ", n);
    }
}

fun(3);  // Output: 3 2 1 1 2 3
```

**Technique**: Draw the call tree and trace execution order.

### Pattern 2: Return Value Prediction

```c
int fun(int n) {
    if(n == 0) return 0;
    return n + fun(n - 1);
}

fun(5);  // Returns: 5 + 4 + 3 + 2 + 1 + 0 = 15
```

### Pattern 3: Count Function Calls

```c
int count = 0;
int fib(int n) {
    count++;
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

fib(5);  // count = 15
```

**Formula**: For naive fibonacci, calls = $2 \times fib(n+1) - 1$

### Pattern 4: Stack Space Analysis

```c
int fun(int n) {
    int arr[1000];  // 4000 bytes
    if(n <= 1) return 1;
    return fun(n-1) + fun(n-2);
}
```

**Question**: If n = 5, max stack space?

**Answer**: Maximum depth is 5, each frame uses ~4000+ bytes. Max space ≈ 5 × 4000 = 20000 bytes.

---

## 3.16 Practice Problems

### Q1 (GATE 2018 Style)
```c
int fun(int n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    return fun(n-1) + fun(n-2) + n;
}
```
What is fun(4)?

**Answer**: 
- fun(0) = 0
- fun(1) = 1
- fun(2) = fun(1) + fun(0) + 2 = 1 + 0 + 2 = 3
- fun(3) = fun(2) + fun(1) + 3 = 3 + 1 + 3 = 7
- fun(4) = fun(3) + fun(2) + 4 = 7 + 3 + 4 = **14**

### Q2 (GATE 2020 Style)
```c
int f(int n) {
    static int x = 1;
    if(n > 0) {
        x = x + n;
        f(n - 1);
    }
    return x;
}

int main() {
    printf("%d", f(3));
    return 0;
}
```

**Answer**: 
- x starts at 1
- f(3): x = 1 + 3 = 4, calls f(2)
- f(2): x = 4 + 2 = 6, calls f(1)
- f(1): x = 6 + 1 = 7, calls f(0)
- f(0): returns x = 7
- Output: **7**

### Q3 (NAT Type)
How many times is `fun()` called when `fun(10)` is executed?
```c
int fun(int n) {
    if(n <= 1) return 1;
    return fun(n/2) + fun(n/3);
}
```

**Answer**: Trace the call tree:
- fun(10): calls fun(5), fun(3)
- fun(5): calls fun(2), fun(1)
- fun(3): calls fun(1), fun(1)
- fun(2): calls fun(1), fun(0)
- Total: **9** calls

---

## 3.17 Quick Reference

### Recursion Template

```c
return_type recursive_function(parameters) {
    // 1. Base case(s)
    if(base_condition) {
        return base_value;
    }
    
    // 2. Recursive case(s)
    // 3. Combine results
    return combine(recursive_function(simpler_parameters));
}
```

### Common Recurrences

| Problem | Recurrence | Complexity |
|---------|------------|------------|
| Factorial | $T(n) = T(n-1) + O(1)$ | $O(n)$ |
| Fibonacci (naive) | $T(n) = T(n-1) + T(n-2)$ | $O(2^n)$ |
| Binary Search | $T(n) = T(n/2) + O(1)$ | $O(\log n)$ |
| Tower of Hanoi | $T(n) = 2T(n-1) + O(1)$ | $O(2^n)$ |
| Merge Sort | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |

### Tail Recursion Pattern

```c
// Non-tail (extra work after recursive call)
int factorial(int n) {
    if(n <= 1) return 1;
    return n * factorial(n-1);  // Multiplication after return
}

// Tail (recursive call is last operation)
int factorial_tail(int n, int acc) {
    if(n <= 1) return acc;
    return factorial_tail(n-1, n * acc);  // Only return
}
```

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Intermediate]**

*Next: [Chapter 4: Arrays and Strings →](04-Arrays-Strings.md)*
