# 📚 PROGRAMMING - Complete A-Z Study Material
## GATE | ESE | PSU | BANK Examinations

---

> **The Atomic Truth:** *Programming = Memory + Logic + Flow Control*

---

# 🔷 TABLE OF CONTENTS

1. [C Programming Fundamentals](#1-c-programming-fundamentals)
2. [Operators & Expressions](#2-operators--expressions)
3. [Control Flow Statements](#3-control-flow-statements)
4. [Functions & Recursion](#4-functions--recursion)
5. [Arrays](#5-arrays)
6. [Strings](#6-strings)
7. [Pointers](#7-pointers)
8. [Dynamic Memory Allocation](#8-dynamic-memory-allocation)
9. [Structures & Unions](#9-structures--unions)
10. [File Handling](#10-file-handling)
11. [Preprocessor Directives](#11-preprocessor-directives)
12. [Storage Classes & Scope](#12-storage-classes--scope)
13. [Bit Manipulation](#13-bit-manipulation)
14. [Parameter Passing Mechanisms](#14-parameter-passing-mechanisms)
15. [Output Prediction Questions](#15-output-prediction-mastery)
16. [GATE PYQ Analysis & Patterns](#16-gate-pyq-analysis--patterns)
17. [Quick Revision Formulas](#17-quick-revision--formulas)

---

# 1. C PROGRAMMING FUNDAMENTALS

## 1.1 Data Types - The Memory Blueprint

### 🎯 The Core Insight
> **Why it matters:** Data types define HOW memory interprets stored bits. Same 32 bits can be `int`, `float`, or garbage—depends on TYPE declaration.

### Size Chart (32-bit vs 64-bit Systems)

| Data Type | 32-bit Size | 64-bit Size | Range |
|-----------|-------------|-------------|-------|
| `char` | 1 byte | 1 byte | **Implementation-defined** signedness: signed char (-128 to 127), unsigned char (0 to 255) |
| `short` | 2 bytes | 2 bytes | -32,768 to 32,767 |
| `int` | 4 bytes | 4 bytes | $-2^{31}$ to $2^{31}-1$ |
| `long` | 4 bytes | **8 bytes** | System dependent |
| `long long` | 8 bytes | 8 bytes | $-2^{63}$ to $2^{63}-1$ |
| `float` | 4 bytes | 4 bytes | ~7 decimal digits precision |
| `double` | 8 bytes | 8 bytes | ~15 decimal digits precision |
| `pointer` | 4 bytes | **8 bytes** | Address space |

### 🔥 GATE TRAP #1: Pointer Size Confusion
```c
// On 64-bit system:
sizeof(int) = 4        // ✓ Same
sizeof(int*) = 8       // ✗ DIFFERENT!
sizeof(char*) = 8      // ALL pointers are 8 bytes on 64-bit
```

**💡 Mnemonic:** "Pointers are addresses, addresses are architecture-dependent"

### 🎯 The Golden Formula for Range Calculation

For n-bit signed integer:
$$\text{Range} = [-2^{n-1}, 2^{n-1} - 1]$$

For n-bit unsigned integer:
$$\text{Range} = [0, 2^n - 1]$$

### Example: Why is `char` range -128 to 127?
- `char` = 8 bits
- Signed: $[-2^7, 2^7-1] = [-128, 127]$
- Total values: $2^8 = 256$ ✓

---

## 1.2 Type Conversion & Casting

### Implicit Type Conversion Hierarchy
```
char → short → int → long → long long → float → double → long double
```

**Rule:** Smaller type ALWAYS promotes to larger type in expressions.

### 🔥 GATE TRAP #2: Integer Division vs Float Division
```c
int a = 5, b = 2;
float c = a/b;        // c = 2.0 (NOT 2.5!)
float d = (float)a/b; // d = 2.5 ✓
float e = a/(float)b; // e = 2.5 ✓
float f = (float)(a/b); // f = 2.0 (Division happened FIRST!)
```

### 🔥 GATE TRAP #3: Signed-Unsigned Comparison
```c
int a = -1;
unsigned int b = 1;
if(a > b) 
    printf("YES");  // Prints YES! 😱
```
**Why?** `-1` in signed = `0xFFFFFFFF` = 4,294,967,295 in unsigned

**💡 Mental Model:** When signed meets unsigned, signed becomes unsigned (preserving bit pattern).

---

## 1.3 Variables & Constants

### Variable Declaration vs Definition
```c
extern int x;    // Declaration (no memory allocated)
int x;           // Definition (memory allocated)
int x = 5;       // Definition + Initialization
```

### Constant Types
```c
const int MAX = 100;        // Read-only variable
#define MAX 100             // Preprocessor macro (text replacement)
enum { MAX = 100 };         // Enumeration constant
```

### 🔥 GATE TRAP #4: const with Pointers
```c
const int *p;      // Pointer to constant int (*p is const)
int const *p;      // Same as above
int *const p;      // Constant pointer to int (p is const)
const int *const p; // Both pointer and value are constant
```

**💡 Read Right-to-Left:** 
- `const int *p` → "p is pointer to int that is const"
- `int *const p` → "p is const pointer to int"

---

# 2. OPERATORS & EXPRESSIONS

## 2.1 Operator Precedence Table (MEMORIZE THIS!)

| Priority | Operators | Associativity |
|----------|-----------|---------------|
| 1 (Highest) | `() [] -> .` | Left to Right |
| 2 | `! ~ ++ -- + - * & (type) sizeof` | **Right to Left** |
| 3 | `* / %` | Left to Right |
| 4 | `+ -` | Left to Right |
| 5 | `<< >>` | Left to Right |
| 6 | `< <= > >=` | Left to Right |
| 7 | `== !=` | Left to Right |
| 8 | `&` (bitwise AND) | Left to Right |
| 9 | `^` (XOR) | Left to Right |
| 10 | `\|` (bitwise OR) | Left to Right |
| 11 | `&&` | Left to Right |
| 12 | `\|\|` | Left to Right |
| 13 | `?:` | **Right to Left** |
| 14 | `= += -= *= /= %= &= ^= \|= <<= >>=` | **Right to Left** |
| 15 (Lowest) | `,` | Left to Right |

### 🎯 Mnemonic: "PUMA REBL AO TC" 
**P**ostfix → **U**nary → **M**ultiplicative → **A**dditive → **R**elational/**E**quality → **B**itwise → **L**ogical → **A**ssignment → **O**ther → **T**ernary → **C**omma

## 2.2 Critical Operator Traps

### 🔥 GATE TRAP #5: Pre/Post Increment in Same Expression
```c
int a = 5;
int b = a++ + ++a;  // UNDEFINED BEHAVIOR! ❌
```
**Rule:** Never modify a variable more than once in a single expression.

### 🔥 GATE TRAP #6: Logical Short-Circuit
```c
int a = 0, b = 5;
if(a && (b = 10))   // b remains 5 (short-circuit)
if(a || (b = 10))   // b becomes 10 (evaluated)
```

### 🔥 GATE TRAP #7: Comma Operator Returns LAST Value
```c
int a = (1, 2, 3);  // a = 3
int b = 1, 2, 3;    // Syntax error!
```

### 🔥 GATE TRAP #8: sizeof is Compile-Time
```c
int arr[10];
printf("%zu", sizeof(arr));     // 40 (10 * 4)
printf("%zu", sizeof(arr[0]));  // 4
printf("%zu", sizeof(arr)/sizeof(arr[0])); // 10 (array length trick)

// BUT with functions:
void foo(int arr[]) {
    printf("%zu", sizeof(arr)); // 8 on 64-bit! (pointer size)
}
```

---

## 2.3 Bitwise Operators - The Power Tools

### The Six Bitwise Operators
| Operator | Symbol | Operation |
|----------|--------|-----------|
| AND | `&` | 1 only if both bits are 1 |
| OR | `\|` | 1 if at least one bit is 1 |
| XOR | `^` | 1 if bits are different |
| NOT | `~` | Flip all bits |
| Left Shift | `<<` | Multiply by $2^n$ (undefined if overflow for signed) |
| Right Shift | `>>` | Divide by $2^n$ (for unsigned; implementation-defined for signed) |

### 🎯 Golden Formulas for Bit Manipulation

```c
// Set bit at position i
n | (1 << i)

// Clear bit at position i
n & ~(1 << i)

// Toggle bit at position i
n ^ (1 << i)

// Check if bit at position i is set
(n >> i) & 1

// Count set bits (Brian Kernighan's Algorithm)
while(n) { count++; n = n & (n-1); }

// Check if power of 2
(n > 0) && ((n & (n-1)) == 0)

// Get rightmost set bit
n & (-n)

// Turn off rightmost set bit
n & (n-1)
```

### 🔥 GATE TRAP #9: Right Shift on Negative Numbers
```c
int a = -8;
printf("%d", a >> 1);  // Implementation-defined behavior in C!
// Result depends on whether implementation uses:
// - Arithmetic shift: -4 (sign bit preserved)
// - Logical shift: large positive number (zeros filled)
```
**Safe Practice:** Use unsigned types for right shifts to ensure defined behavior.

### 🔥 GATE TRAP #10: XOR Swap
```c
a = a ^ b;
b = a ^ b;  // b = original a
a = a ^ b;  // a = original b
// Works, but FAILS if a and b point to same location!
```

---

# 3. CONTROL FLOW STATEMENTS

## 3.1 Conditional Statements

### if-else Ladder Execution
```c
if(condition1) {
    // Executed if condition1 is TRUE (non-zero)
} else if(condition2) {
    // Executed if condition1 is FALSE and condition2 is TRUE
} else {
    // Executed if ALL conditions are FALSE
}
```

### 🔥 GATE TRAP #11: Dangling Else Problem
```c
if(a)
    if(b)
        printf("X");
else
    printf("Y");  // Associates with INNER if!
```
**Rule:** `else` binds to the NEAREST unmatched `if`.

### Switch Statement Mechanics
```c
switch(expression) {  // expression MUST be integral type
    case const1:
        // code
        break;  // Without break, falls through!
    case const2:
    case const3:  // Multiple cases, same action
        // code
        break;
    default:
        // code (optional)
}
```

### 🔥 GATE TRAP #12: Switch Fall-Through
```c
int x = 1;
switch(x) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C");
}
// Output: ABC (no break = fall-through)
```

### 🔥 GATE TRAP #13: Switch Case Must Be Constant
```c
int a = 5;
switch(x) {
    case a:      // ❌ ERROR! Must be compile-time constant
    case 5:      // ✓ OK
    case 2+3:    // ✓ OK (constant expression)
}
```

---

## 3.2 Loops

### Loop Comparison Table
| Feature | `for` | `while` | `do-while` |
|---------|-------|---------|------------|
| Entry check | Yes | Yes | No (post-check) |
| Minimum iterations | 0 | 0 | **1** |
| Best for | Known iterations | Unknown iterations | At least once |
| Syntax | `for(init;cond;update)` | `while(cond)` | `do{...}while(cond);` |

### 🔥 GATE TRAP #14: Infinite Loops
```c
for(;;)         // Infinite
while(1)        // Infinite
do{}while(1);   // Infinite (with semicolon!)
```

### 🔥 GATE TRAP #15: Loop Variable Scope (C99+)
```c
for(int i = 0; i < n; i++) { }
printf("%d", i);  // ❌ ERROR in C99! i is out of scope
```

### 🔥 GATE TRAP #16: Semicolon After Loop
```c
for(i = 0; i < 5; i++);  // Empty loop body!
    printf("%d", i);      // Prints 5 (only once)
```

---

## 3.3 Jump Statements

| Statement | Purpose | Scope |
|-----------|---------|-------|
| `break` | Exit innermost loop/switch | Single level |
| `continue` | Skip to next iteration | Single level |
| `goto` | Jump to labeled statement | Within function |
| `return` | Exit function | Function level |

### 🔥 GATE TRAP #17: break with Nested Loops
```c
for(i = 0; i < 3; i++) {
    for(j = 0; j < 3; j++) {
        if(j == 1) break;  // Only breaks INNER loop
    }
}
// i still iterates fully (0, 1, 2)
```

---

# 4. FUNCTIONS & RECURSION

## 4.1 Function Basics

### Function Declaration vs Definition
```c
int add(int a, int b);        // Declaration (prototype)

int add(int a, int b) {       // Definition
    return a + b;
}
```

### 🎯 The Parameter Passing Truth

> **C uses ONLY Call-by-Value.** Period. What we call "call by reference" is actually passing the VALUE of a pointer.

```c
void swap(int *a, int *b) {   // Receiving VALUES of addresses
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Call:
swap(&x, &y);  // Passing VALUES of &x and &y
```

## 4.2 Recursion - The Self-Reference Machine

### 🎯 The Three Laws of Recursion
1. **Base Case:** Must have a stopping condition
2. **Progress:** Each call must move TOWARD the base case
3. **Trust:** Assume recursive calls work correctly

### Recursion Types

| Type | Definition | Example |
|------|------------|---------|
| **Direct** | Function calls itself | `f() → f()` |
| **Indirect** | Function A calls B, B calls A | `f() → g() → f()` |
| **Tail** | Recursive call is LAST operation | `return f(n-1)` |
| **Non-tail** | Operations after recursive call | `return n * f(n-1)` |

### 🔥 Classic Recursion Formulas

#### Factorial
$$T(n) = T(n-1) + O(1), \quad T(0) = O(1)$$
$$\Rightarrow T(n) = O(n)$$

```c
int factorial(int n) {
    if(n <= 1) return 1;
    return n * factorial(n - 1);
}
```

#### Fibonacci (Naive)
$$T(n) = T(n-1) + T(n-2) + O(1)$$
$$\Rightarrow T(n) = O(2^n)$$ (exponential - BAD!)

```c
int fib(int n) {
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
```

#### Tower of Hanoi
$$T(n) = 2T(n-1) + O(1)$$
$$\Rightarrow T(n) = O(2^n)$$
Moves required: $2^n - 1$

```c
void hanoi(int n, char from, char to, char aux) {
    if(n == 1) {
        printf("Move disk 1 from %c to %c\n", from, to);
        return;
    }
    hanoi(n-1, from, aux, to);
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n-1, aux, to, from);
}
```

### 🔥 GATE TRAP #18: Stack Overflow in Recursion
```c
void infinite() {
    infinite();  // Stack overflow (no base case)
}
```
Each recursive call consumes stack space. Deep recursion → stack overflow.

### 🔥 GATE TRAP #19: Recursion Stack Depth
```c
int f(int n) {
    if(n == 0) return 0;
    return f(n-1);
}
f(1000000);  // May crash! Stack depth = 1,000,000
```

---

## 4.3 Recursion Tree Method for Time Complexity

### 🎯 The Formula
For recurrence $T(n) = aT(n/b) + f(n)$:

**Master Theorem:**
1. If $f(n) = O(n^{\log_b a - \epsilon})$ → $T(n) = \Theta(n^{\log_b a})$
2. If $f(n) = \Theta(n^{\log_b a})$ → $T(n) = \Theta(n^{\log_b a} \log n)$
3. If $f(n) = \Omega(n^{\log_b a + \epsilon})$ → $T(n) = \Theta(f(n))$

### Common Recurrences

| Recurrence | Solution | Example |
|------------|----------|---------|
| $T(n) = T(n-1) + O(1)$ | $O(n)$ | Factorial |
| $T(n) = T(n-1) + O(n)$ | $O(n^2)$ | Selection sort |
| $T(n) = 2T(n-1) + O(1)$ | $O(2^n)$ | Tower of Hanoi |
| $T(n) = 2T(n/2) + O(1)$ | $O(n)$ | Tree traversal |
| $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ | Merge sort |
| $T(n) = T(n/2) + O(1)$ | $O(\log n)$ | Binary search |

---

# 5. ARRAYS

## 5.1 Array Fundamentals

### 🎯 The Core Insight
> **Array = Contiguous memory block with uniform element size**

### Declaration and Initialization
```c
int arr[5];                    // Garbage values
int arr[5] = {1, 2, 3, 4, 5}; // Full initialization
int arr[5] = {1, 2};          // Partial: {1, 2, 0, 0, 0}
int arr[] = {1, 2, 3};        // Size inferred: 3
int arr[5] = {0};             // All zeros
```

### 🎯 Array-Pointer Relationship

```c
int arr[5] = {10, 20, 30, 40, 50};

arr      == &arr[0]           // Both are address of first element
*arr     == arr[0]            // Value at first element
arr + i  == &arr[i]           // Address of i-th element
*(arr+i) == arr[i]            // Value of i-th element
```

### 🔥 GATE TRAP #20: Array Name vs Pointer
```c
int arr[5];
int *ptr = arr;

sizeof(arr)  // 20 (entire array)
sizeof(ptr)  // 8 (pointer size on 64-bit)

arr++;       // ❌ ERROR! Array name is NOT modifiable lvalue
ptr++;       // ✓ OK
```

### 🔥 GATE TRAP #21: Array Indexing Weirdness
```c
int arr[5] = {10, 20, 30, 40, 50};
printf("%d", 2[arr]);  // Prints 30! (2[arr] == arr[2] == *(arr+2) == *(2+arr))
```
**Why?** `a[i]` is defined as `*(a + i)`, and addition is commutative.

---

## 5.2 2D Arrays - Row Major Order

### Memory Layout (Row Major - C Default)
```
int arr[2][3] = {{1,2,3}, {4,5,6}};

Memory: [1][2][3][4][5][6]
        Row 0    Row 1
```

### 🎯 Address Calculation Formula
For `arr[M][N]` with base address B and element size S:
$$\text{Address of } arr[i][j] = B + (i \times N + j) \times S$$

### 🔥 GATE TRAP #22: 2D Array as Function Parameter
```c
void foo(int arr[][3], int rows);  // ✓ Column size REQUIRED
void foo(int arr[][], int rows);   // ❌ ERROR
void foo(int (*arr)[3], int rows); // ✓ Pointer to array of 3 ints
void foo(int **arr, int rows);     // ✗ DIFFERENT! Pointer to pointer
```

### 🔥 GATE TRAP #23: Array of Pointers vs 2D Array
```c
int arr[3][4];        // Contiguous 12 integers (48 bytes)
int *arr[3];          // 3 pointers, each can point anywhere

// Memory layout is COMPLETELY different!
```

---

## 5.3 Array Algorithms - Time Complexities

| Operation | Unsorted Array | Sorted Array |
|-----------|----------------|--------------|
| Access by index | $O(1)$ | $O(1)$ |
| Search | $O(n)$ | $O(\log n)$ (binary) |
| Insert at end (no order maintained) | $O(1)$ | $O(n)$ (must maintain order) |
| Insert at specific position | $O(n)$ | $O(n)$ |
| Delete | $O(n)$ | $O(n)$ |

---

# 6. STRINGS

## 6.1 String Fundamentals

### 🎯 The Core Insight
> **String = Character array + Null terminator (`\0`)**

### Declaration Methods
```c
char str1[] = "Hello";         // Size 6 (includes '\0')
char str2[6] = "Hello";        // Same as above
char str3[] = {'H','e','l','l','o','\0'}; // Explicit
char *str4 = "Hello";          // Pointer to STRING LITERAL (read-only!)
```

### 🔥 GATE TRAP #24: String Literal Modification
```c
char str[] = "Hello";
str[0] = 'J';         // ✓ OK - array in stack

char *str = "Hello";
str[0] = 'J';         // ❌ UNDEFINED BEHAVIOR! String literal in read-only memory
```

### 🔥 GATE TRAP #25: String Comparison
```c
char *s1 = "Hello";
char *s2 = "Hello";

if(s1 == s2)  // May be TRUE (compiler optimization) or FALSE
if(strcmp(s1, s2) == 0)  // ✓ Correct way to compare strings
```

---

## 6.2 Standard Library Functions

| Function | Purpose | Return Value |
|----------|---------|--------------|
| `strlen(s)` | Length (excluding `\0`) | `size_t` |
| `strcpy(dest, src)` | Copy string | `dest` pointer |
| `strncpy(dest, src, n)` | Copy at most n chars | `dest` pointer |
| `strcat(dest, src)` | Concatenate | `dest` pointer |
| `strncat(dest, src, n)` | Concatenate at most n | `dest` pointer |
| `strcmp(s1, s2)` | Compare | `0` if equal, `<0` or `>0` |
| `strncmp(s1, s2, n)` | Compare first n chars | Same as `strcmp` |
| `strchr(s, c)` | Find first occurrence | Pointer or `NULL` |
| `strrchr(s, c)` | Find last occurrence | Pointer or `NULL` |
| `strstr(haystack, needle)` | Find substring | Pointer or `NULL` |

### 🔥 GATE TRAP #26: strlen vs sizeof
```c
char str[] = "Hello";
sizeof(str)   // 6 (includes '\0')
strlen(str)   // 5 (excludes '\0')

char *ptr = "Hello";
sizeof(ptr)   // 8 (pointer size, not string length!)
strlen(ptr)   // 5
```

### 🔥 GATE TRAP #27: strncpy Doesn't Null-Terminate
```c
char src[] = "Hello World";
char dest[5];
strncpy(dest, src, 5);
// dest = {'H','e','l','l','o'} - NO '\0'!
dest[4] = '\0';  // Must add manually if source is longer
```

---

# 7. POINTERS

## 7.1 Pointer Fundamentals

### 🎯 The Core Insight
> **Pointer = Variable storing a memory address**

### Declaration and Usage
```c
int x = 10;
int *p = &x;    // p stores address of x

*p = 20;        // Dereferencing: x becomes 20
p++;            // Pointer arithmetic: moves by sizeof(int)
```

### 🎯 Pointer Arithmetic Rules

| Operation | Result |
|-----------|--------|
| `ptr + n` | Address increases by `n * sizeof(*ptr)` |
| `ptr - n` | Address decreases by `n * sizeof(*ptr)` |
| `ptr1 - ptr2` | Number of elements between them |
| `ptr1 + ptr2` | ❌ INVALID |
| `ptr * n` | ❌ INVALID |
| `ptr / n` | ❌ INVALID |

### 🔥 GATE TRAP #28: Pointer Arithmetic
```c
int arr[] = {10, 20, 30, 40};
int *p = arr;

p + 1         // Address of arr[1] (4 bytes ahead)
*(p + 1)      // Value 20
p++;          // p now points to arr[1]
p - arr       // 1 (number of elements, not bytes)
```

---

## 7.2 Pointer Types

### Void Pointer (`void *`)
```c
void *vp;
int x = 10;
vp = &x;

// Cannot dereference directly:
// *vp = 20;  ❌ ERROR

// Must cast first:
*(int*)vp = 20;  ✓
```

### NULL Pointer
```c
int *p = NULL;    // Points to address 0
if(p == NULL) { } // Safe to check
*p = 10;          // ❌ SEGMENTATION FAULT
```

### 🔥 GATE TRAP #29: Dangling Pointer
```c
int *foo() {
    int x = 10;
    return &x;    // ❌ Returning address of local variable!
}
int *p = foo();   // p is DANGLING - x is destroyed
*p = 20;          // UNDEFINED BEHAVIOR
```

### 🔥 GATE TRAP #30: Wild Pointer
```c
int *p;           // Uninitialized - contains garbage address
*p = 10;          // ❌ UNDEFINED BEHAVIOR
```

---

## 7.3 Complex Pointer Declarations

### 🎯 The Clockwise/Spiral Rule
Read declarations from the identifier, going clockwise (right, then left).

```c
int *p;                  // p is pointer to int
int **p;                 // p is pointer to pointer to int
int *p[10];              // p is array of 10 pointers to int
int (*p)[10];            // p is pointer to array of 10 ints
int *p(int);             // p is function taking int, returning pointer to int
int (*p)(int);           // p is pointer to function taking int, returning int
int (*p[10])(int);       // p is array of 10 pointers to functions
```

### 🔥 GATE TRAP #31: Array of Pointers vs Pointer to Array
```c
int *arr[5];     // 5 pointers, each pointing to int (40 bytes on 64-bit)
int (*arr)[5];   // 1 pointer, pointing to array of 5 ints (8 bytes)

// Usage differs!
int (*p)[5] = &arr2d;
(*p)[2] = 10;    // Access element
```

---

## 7.4 Function Pointers

### Declaration and Usage
```c
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int (*fp)(int, int);    // Function pointer declaration
fp = add;               // Assignment (& is optional)
fp = &add;              // Also valid

int result = fp(5, 3);  // Call through pointer: result = 8
result = (*fp)(5, 3);   // Also valid
```

### 🔥 Callback Pattern
```c
void execute(int a, int b, int (*operation)(int, int)) {
    printf("%d", operation(a, b));
}

execute(10, 5, add);  // Prints 15
execute(10, 5, sub);  // Prints 5
```

---

# 8. DYNAMIC MEMORY ALLOCATION

## 8.1 Memory Layout

```
High Address
┌──────────────────┐
│     Stack        │  ← Local variables, function calls
├──────────────────┤
│        ↓         │
│                  │
│        ↑         │
├──────────────────┤
│      Heap        │  ← malloc, calloc, realloc
├──────────────────┤
│      BSS         │  ← Uninitialized global/static
├──────────────────┤
│      Data        │  ← Initialized global/static
├──────────────────┤
│      Text        │  ← Program code (read-only)
└──────────────────┘
Low Address
```

## 8.2 Allocation Functions

| Function | Syntax | Initializes? | Use Case |
|----------|--------|--------------|----------|
| `malloc` | `malloc(size)` | No (garbage) | General allocation |
| `calloc` | `calloc(n, size)` | Yes (zeros) | Arrays |
| `realloc` | `realloc(ptr, new_size)` | Preserves old | Resize |
| `free` | `free(ptr)` | - | Deallocate |

### Proper Usage
```c
int *arr = (int*)malloc(10 * sizeof(int));
if(arr == NULL) {
    // Handle allocation failure
    exit(1);
}
// Use arr...
free(arr);
arr = NULL;  // Good practice - prevent dangling pointer
```

### 🔥 GATE TRAP #32: Memory Leak
```c
void leak() {
    int *p = malloc(100);
    // Function returns without free(p)
    // Memory is lost forever!
}
```

### 🔥 GATE TRAP #33: Double Free
```c
int *p = malloc(100);
free(p);
free(p);  // ❌ UNDEFINED BEHAVIOR
```

### 🔥 GATE TRAP #34: realloc Behavior
```c
int *p = malloc(10 * sizeof(int));
int *q = realloc(p, 20 * sizeof(int));

// If realloc fails, p is still valid, q is NULL
// If realloc succeeds, p may be invalid (memory may have moved)

// CORRECT pattern:
int *temp = realloc(p, 20 * sizeof(int));
if(temp != NULL) {
    p = temp;  // Update p only on success
}
```

### 🔥 GATE TRAP #35: Heap vs Stack Allocation
```c
int* createArray() {
    int arr[100];           // ❌ Stack - destroyed on return
    return arr;             // DANGLING!
    
    int *arr = malloc(100 * sizeof(int));  // ✓ Heap - persists
    return arr;             // OK (but caller must free)
}
```

---

# 9. STRUCTURES & UNIONS

## 9.1 Structures

### Declaration Styles
```c
// Style 1: Separate declaration and variable
struct Point {
    int x;
    int y;
};
struct Point p1;

// Style 2: Combined
struct Point {
    int x;
    int y;
} p1, p2;

// Style 3: typedef
typedef struct {
    int x;
    int y;
} Point;
Point p1;  // No 'struct' keyword needed
```

### 🔥 GATE TRAP #36: Structure Padding & Alignment

```c
struct Example {
    char a;     // 1 byte + 3 padding
    int b;      // 4 bytes
    char c;     // 1 byte + 3 padding
};
// sizeof = 12 (not 6!)

// Optimized order:
struct Example {
    int b;      // 4 bytes
    char a;     // 1 byte
    char c;     // 1 byte + 2 padding
};
// sizeof = 8
```

### 🎯 Padding Rules
1. Each member aligned to its size (or max member size)
2. Structure size is multiple of largest member alignment
3. Padding added AFTER smaller members

### 🔥 GATE TRAP #37: Structure Assignment
```c
struct Point p1 = {10, 20};
struct Point p2 = p1;  // ✓ OK - memberwise copy

p2.x = 100;            // Does NOT affect p1
```

### 🔥 GATE TRAP #38: Structure with Pointer Member
```c
struct Node {
    int data;
    int *ptr;
};
struct Node n1 = {10, malloc(sizeof(int))};
struct Node n2 = n1;  // SHALLOW COPY!
// n1.ptr and n2.ptr point to SAME memory!
```

---

## 9.2 Unions

### 🎯 The Core Insight
> **Union = Overlay multiple members on SAME memory**

```c
union Data {
    int i;
    float f;
    char c;
};
// sizeof(union Data) = 4 (size of largest member)
```

### 🔥 GATE TRAP #39: Union Member Access
```c
union Data d;
d.i = 1000;
printf("%f", d.f);  // Garbage! (interpreting int bits as float)
```

### Use Case: Type Punning (with care)
```c
union FloatInt {
    float f;
    int i;
};
union FloatInt fi;
fi.f = 3.14;
printf("Bit pattern: 0x%X", fi.i);  // See float's bit representation
```

---

## 9.3 Bit Fields

### Syntax
```c
struct Flags {
    unsigned int flag1 : 1;  // 1 bit
    unsigned int flag2 : 1;  // 1 bit
    unsigned int flag3 : 1;  // 1 bit
    unsigned int value : 5;  // 5 bits (0-31)
};
// Total: 8 bits = 1 byte (plus padding to word boundary)
```

### 🔥 GATE TRAP #40: Cannot Take Address of Bit Field
```c
struct Flags f;
int *p = &f.flag1;  // ❌ ERROR! No address for bit field
```

---

# 10. FILE HANDLING

## 10.1 File Operations

### Opening and Closing
```c
FILE *fp = fopen("file.txt", "r");
if(fp == NULL) {
    perror("Error opening file");
    exit(1);
}
// ... operations ...
fclose(fp);
```

### File Modes
| Mode | Description | If file exists | If file doesn't exist |
|------|-------------|----------------|----------------------|
| `"r"` | Read | Open | Return NULL |
| `"w"` | Write | Truncate | Create |
| `"a"` | Append | Open at end | Create |
| `"r+"` | Read/Write | Open | Return NULL |
| `"w+"` | Read/Write | Truncate | Create |
| `"a+"` | Read/Append | Open at end | Create |

Add `"b"` for binary: `"rb"`, `"wb"`, etc.

## 10.2 File I/O Functions

| Function | Purpose | Return |
|----------|---------|--------|
| `fgetc(fp)` | Read character | char or EOF |
| `fputc(c, fp)` | Write character | char or EOF |
| `fgets(str, n, fp)` | Read line | str or NULL |
| `fputs(str, fp)` | Write string | Non-negative or EOF |
| `fscanf(fp, fmt, ...)` | Formatted read | Items read |
| `fprintf(fp, fmt, ...)` | Formatted write | Chars written |
| `fread(ptr, size, n, fp)` | Binary read | Items read |
| `fwrite(ptr, size, n, fp)` | Binary write | Items written |

### 🔥 GATE TRAP #41: fgets Includes Newline
```c
char line[100];
fgets(line, 100, fp);
// line may contain '\n' before '\0'
```

### 🔥 GATE TRAP #42: EOF Check
```c
int c;
while((c = fgetc(fp)) != EOF) {  // c must be int, not char!
    // process c
}
```
**Why int?** EOF is typically -1. If c is `unsigned char`, it can never equal EOF.

## 10.3 File Positioning

| Function | Purpose |
|----------|---------|
| `fseek(fp, offset, origin)` | Move file pointer |
| `ftell(fp)` | Get current position |
| `rewind(fp)` | Go to beginning |

### fseek Origins
- `SEEK_SET` (0): Beginning of file
- `SEEK_CUR` (1): Current position
- `SEEK_END` (2): End of file

```c
fseek(fp, 0, SEEK_END);   // Go to end
long size = ftell(fp);    // File size in bytes
rewind(fp);               // Back to start
```

---

# 11. PREPROCESSOR DIRECTIVES

## 11.1 Macro Definitions

### Object-like Macros
```c
#define PI 3.14159
#define MAX_SIZE 100
#define DEBUG 1
```

### Function-like Macros
```c
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define SWAP(a, b, type) { type temp = a; a = b; b = temp; }
```

### 🔥 GATE TRAP #43: Macro Side Effects
```c
#define SQUARE(x) x * x
int a = SQUARE(3 + 2);    // 3 + 2 * 3 + 2 = 11, not 25!

#define SQUARE(x) (x) * (x)
int a = SQUARE(3 + 2);    // (3+2) * (3+2) = 25 ✓

#define SQUARE(x) ((x) * (x))
int a = 10 / SQUARE(2);   // 10 / ((2) * (2)) = 2 ✓
```

### 🔥 GATE TRAP #44: Macro with Increment
```c
#define SQUARE(x) ((x) * (x))
int i = 3;
int a = SQUARE(i++);  // ((i++) * (i++)) - i incremented TWICE!
// Result is 3 * 4 = 12 (or 4 * 3, undefined order)
```

### 🔥 GATE TRAP #45: Macro vs Function
| Macro | Function |
|-------|----------|
| Text substitution | Actual call |
| No type checking | Type checking |
| May evaluate args multiple times | Args evaluated once |
| Faster (no call overhead) | Has call overhead |
| Increases code size | One copy of code |

## 11.2 Conditional Compilation

```c
#if defined(DEBUG) || DEBUG_LEVEL > 1
    printf("Debug info\n");
#elif defined(PRODUCTION)
    // Production code
#else
    // Default code
#endif

#ifdef DEBUG    // Same as #if defined(DEBUG)
#endif

#ifndef HEADER_H  // Include guard pattern
#define HEADER_H
// header contents
#endif
```

## 11.3 Stringizing and Token Pasting

```c
// Stringizing: # operator
#define STRINGIFY(x) #x
printf("%s", STRINGIFY(Hello));  // Prints: Hello

// Token pasting: ## operator
#define CONCAT(a, b) a ## b
int xy = 10;
printf("%d", CONCAT(x, y));  // Prints: 10 (variable xy)
```

## 11.4 Predefined Macros

| Macro | Description |
|-------|-------------|
| `__FILE__` | Current source file name |
| `__LINE__` | Current line number |
| `__DATE__` | Compilation date |
| `__TIME__` | Compilation time |
| `__func__` | Current function name (C99) |

---

# 12. STORAGE CLASSES & SCOPE

## 12.1 Storage Classes Summary

| Class | Keyword | Scope | Lifetime | Default Value | Stored In |
|-------|---------|-------|----------|---------------|-----------|
| Automatic | `auto` | Block | Block | Garbage | Stack |
| Register | `register` | Block | Block | Garbage | CPU Register |
| Static (local) | `static` | Block | Program | 0 | Data/BSS |
| Static (global) | `static` | File | Program | 0 | Data/BSS |
| External | `extern` | Program | Program | 0 | Data/BSS |

### 🔥 GATE TRAP #46: Static Local Variable
```c
void counter() {
    static int count = 0;  // Initialized ONCE
    count++;
    printf("%d ", count);
}

counter();  // 1
counter();  // 2
counter();  // 3
```

### 🔥 GATE TRAP #47: Static vs Global
```c
// file1.c
static int x = 10;  // Only visible in file1.c
int y = 20;         // Visible in all files

// file2.c
extern int y;       // Can access y
extern int x;       // ❌ Linker error! x is static
```

### 🔥 GATE TRAP #48: Register Variable
```c
register int i;
int *p = &i;  // ❌ ERROR! Cannot take address of register variable
```

## 12.2 Scope Rules

### Types of Scope
1. **Block Scope:** Variables declared inside `{}`
2. **Function Scope:** Labels (goto targets)
3. **File Scope:** Global variables/functions
4. **Function Prototype Scope:** Parameter names in prototype

### 🔥 GATE TRAP #49: Variable Shadowing
```c
int x = 10;          // Global x
void foo() {
    int x = 20;      // Local x shadows global
    {
        int x = 30;  // Inner x shadows outer
        printf("%d", x);  // 30
    }
    printf("%d", x);      // 20
}
```

## 12.3 Linkage

| Linkage | Meaning | Example |
|---------|---------|---------|
| **None** | Only in block | Local variables |
| **Internal** | Only in file | `static` global |
| **External** | Across files | Global (non-static) |

---

# 13. BIT MANIPULATION

## 13.1 Essential Bit Operations

### Bit Manipulation Cheat Sheet
```c
// 1. Set nth bit
x | (1 << n)

// 2. Clear nth bit
x & ~(1 << n)

// 3. Toggle nth bit
x ^ (1 << n)

// 4. Check nth bit
(x >> n) & 1
// or
(x & (1 << n)) != 0

// 5. Turn off rightmost 1
x & (x - 1)

// 6. Isolate rightmost 1
x & (-x)

// 7. Right propagate rightmost 1
x | (x - 1)

// 8. Check if power of 2
x && !(x & (x - 1))

// 9. Count set bits (Kernighan's)
count = 0;
while (x) { count++; x &= (x - 1); }

// 10. Swap without temp
a ^= b; b ^= a; a ^= b;
```

### 🎯 Important Bit Formulas

| Operation | Formula | Example |
|-----------|---------|---------|
| Multiply by $2^n$ | `x << n` | `5 << 2 = 20` |
| Divide by $2^n$ | `x >> n` | `20 >> 2 = 5` |
| Modulo $2^n$ | `x & (2^n - 1)` | `13 & 7 = 5` |
| Check if even | `!(x & 1)` | `6 & 1 = 0` (even) |
| Make even | `x & ~1` | `7 & ~1 = 6` |

## 13.2 Two's Complement Representation

### 🎯 The Core Formula
For n-bit signed integer:
$$-x = \sim x + 1$$

```c
int x = 5;    // 00000101
int neg = ~x + 1;  // 11111011 = -5
```

### 🔥 GATE TRAP #50: Overflow in Bit Operations
```c
unsigned int x = 0xFFFFFFFF;
x = x << 1;  // x = 0xFFFFFFFE (MSB shifted out, LSB becomes 0)

int x = 0x7FFFFFFF;  // Max positive int
x = x + 1;           // Overflow to -2147483648
```

---

# 14. PARAMETER PASSING MECHANISMS

## 14.1 Call by Value

> **Everything is copied. Original unchanged.**

```c
void increment(int x) {
    x++;  // Changes LOCAL copy only
}

int a = 5;
increment(a);
printf("%d", a);  // Still 5!
```

## 14.2 Call by Reference (Simulated in C)

> **Pass address. Can modify original.**

```c
void increment(int *x) {
    (*x)++;  // Modifies original through pointer
}

int a = 5;
increment(&a);
printf("%d", a);  // Now 6!
```

## 14.3 Call by Value-Result (Copy-In Copy-Out)

> **Copy in at start, copy out at end.**

Not natively in C, but simulated:
```c
void foo(int *x, int *y) {
    int local_x = *x;  // Copy in
    int local_y = *y;
    
    local_x = local_x + local_y;
    local_y = local_x - local_y;
    
    *x = local_x;  // Copy out
    *y = local_y;
}
```

### 🔥 GATE TRAP #51: Call by Reference vs Value-Result

```c
// With call by reference:
void swap(int *a, int *b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}
int x = 5;
swap(&x, &x);  // FAILS! x becomes 0

// With call by value-result:
// Same code would work correctly
```

## 14.4 Call by Name (Lazy Evaluation)

> **Arguments evaluated each time they're used.**

Not in C, but important concept (Algol, Scala):
```
// Pseudo-code
procedure swap(x, y):
    temp = x    // x evaluated
    x = y       // y evaluated, x evaluated
    y = temp    // y evaluated

// With a[i] and i:
swap(a[i], i)
// Every reference to 'a[i]' uses CURRENT value of i!
```

### 🎯 Comparison Table

| Mechanism | When Evaluated | Modifications | Aliasing Issues |
|-----------|----------------|---------------|-----------------|
| By Value | Call time | No effect | None |
| By Reference | Each access | Immediate | Yes |
| By Value-Result | Call & return | At return | Minimal |
| By Name | Each access | Immediate | Complex |

---

# 15. OUTPUT PREDICTION MASTERY

## 15.1 Systematic Approach

### 🎯 The 5-Step Method

1. **Trace Variables:** List all variables and initial values
2. **Track Scope:** Identify which variable is active
3. **Evaluate Expressions:** Follow precedence strictly
4. **Handle Side Effects:** Watch `++`, `--`, assignments
5. **Check Format Specifiers:** Match types carefully

## 15.2 Common Output Traps

### 🔥 GATE TRAP #52: printf Return Value
```c
int x = printf("Hello");  // x = 5 (characters printed)
printf("%d", printf("%d", printf("%d", 43)));
// Innermost: prints 43, returns 2
// Middle: prints 2, returns 1  
// Outer: prints 1
// Output: 4321
```

### 🔥 GATE TRAP #53: Comma in printf
```c
printf("%d", (1, 2, 3));  // Prints 3 (comma operator)
printf("%d %d", 1, 2, 3); // Prints 1 2 (extra arg ignored)
```

### 🔥 GATE TRAP #54: Pointer Printing
```c
int arr[] = {10, 20, 30};
printf("%d", *(arr + 1));     // 20
printf("%d", *arr + 1);       // 11 (10 + 1)
printf("%d", arr[1]);         // 20
printf("%d", 1[arr]);         // 20
```

### 🔥 GATE TRAP #55: String Pointer Arithmetic
```c
char *p = "Hello";
printf("%s", p + 2);    // llo
printf("%c", *p + 1);   // I (H + 1)
printf("%c", *(p + 1)); // e
```

## 15.3 Complex Expression Evaluation

### Example 1: Operator Precedence
```c
int a = 2, b = 3, c = 4;
int x = a + b * c;        // 2 + 12 = 14
int y = (a + b) * c;      // 5 * 4 = 20
int z = a * b + c * a;    // 6 + 8 = 14
```

### Example 2: Logical Operators
```c
int x = 0, y = 1, z;
z = x++ || ++y;
// x++ evaluates x (0), then increments (x = 1)
// Since 0, must check ++y
// ++y increments y to 2, evaluates to 2 (truthy)
// z = 1
// Final: x = 1, y = 2, z = 1
```

### Example 3: Ternary Nesting
```c
int a = 1, b = 2, c = 3;
int x = a > b ? a > c ? a : c : b > c ? b : c;
// a > b is false
// So evaluate: b > c ? b : c
// b > c is false, so x = c = 3
```

---

# 16. GATE PYQ ANALYSIS & PATTERNS

## 16.1 Topic-wise Weightage (Last 10 Years)

| Topic | Average Marks | Question Types |
|-------|---------------|----------------|
| Pointers | 4-6 | Output, Concept |
| Recursion | 4-6 | Output, Time Complexity |
| Arrays & Strings | 2-4 | Output, Addressing |
| Structures | 2-4 | Size, Padding |
| Functions | 2-4 | Parameter Passing |
| Operators | 2-4 | Output, Precedence |
| Storage Classes | 1-2 | Concept |
| File Handling | 0-2 | Concept |

## 16.2 Most Repeated Patterns

### Pattern 1: Pointer Arithmetic
```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;
printf("%d", *(p++));  // 10 (use then increment)
printf("%d", *p);      // 20
```

### Pattern 2: Recursion Tracing
```c
void fun(int n) {
    if(n > 0) {
        fun(n - 1);
        printf("%d ", n);
        fun(n - 1);
    }
}
fun(3);
// Output: 1 2 1 3 1 2 1
```

### Pattern 3: Structure Size
```c
struct X {
    char a;    // 1 + 3 padding
    int b;     // 4
    char c;    // 1 + 3 padding
};
// sizeof = 12
```

### Pattern 4: Pre/Post Increment
```c
int i = 5;
printf("%d %d %d", i, ++i, i++);
// Undefined behavior! Don't predict.
// Why? Variable 'i' is modified multiple times without intervening sequence point.
// Also: Order of evaluation of function arguments is unspecified in C.
// GATE asks: "What is the output OR it is undefined?"
```

### Pattern 5: Macro Evaluation
```c
#define SQR(x) x*x
int a = SQR(2+3);  // 2+3*2+3 = 11
```

## 16.3 High-Frequency GATE Questions

### Q1: What is the output?
```c
int main() {
    int a = 5;
    int b = a++ + ++a;
    printf("%d %d", a, b);
}
```
**Answer:** Undefined Behavior (modifying `a` twice)

### Q2: What is sizeof?
```c
struct test {
    int a;
    char b;
    double c;
    char d;
};
```
**Answer:** 24 bytes (int:4, pad:4, double:8, char:1, pad:7)

### Q3: Recursion output
```c
int f(int n) {
    if(n <= 1) return 1;
    if(n % 2 == 0) return f(n/2);
    return f(n/2) + f(n/2 + 1);
}
printf("%d", f(11));
```
**Trace:**
- f(11) = f(5) + f(6)
- f(5) = f(2) + f(3)
- f(6) = f(3)
- f(3) = f(1) + f(2)
- f(2) = f(1) = 1
- f(3) = 1 + 1 = 2
- f(5) = 1 + 2 = 3
- f(6) = 2
- f(11) = 3 + 2 = **5**

---

# 17. QUICK REVISION & FORMULAS

## 17.1 Data Type Sizes
```
char: 1 byte
short: 2 bytes
int: 4 bytes
long: 4/8 bytes (32/64 bit)
long long: 8 bytes
float: 4 bytes
double: 8 bytes
pointer: 4/8 bytes (32/64 bit)
```

## 17.2 Range Formulas
```
n-bit signed: [-2^(n-1), 2^(n-1) - 1]
n-bit unsigned: [0, 2^n - 1]
```

## 17.3 Array Address Formula (Row Major)
```
arr[i][j] address = Base + (i * COLS + j) * element_size
```

## 17.4 Recursion Complexities
```
T(n) = T(n-1) + c      → O(n)
T(n) = T(n-1) + n      → O(n²)
T(n) = 2T(n-1) + c     → O(2ⁿ)
T(n) = T(n/2) + c      → O(log n)
T(n) = 2T(n/2) + c     → O(n)
T(n) = 2T(n/2) + n     → O(n log n)
```

## 17.5 Bit Operations Quick Reference
```
Set bit i:      n | (1 << i)
Clear bit i:    n & ~(1 << i)
Toggle bit i:   n ^ (1 << i)
Check bit i:    (n >> i) & 1
Count bits:     while(n) { c++; n &= n-1; }
Power of 2:     n && !(n & (n-1))
Multiply 2^k:   n << k
Divide 2^k:     n >> k
Mod 2^k:        n & ((1 << k) - 1)
```

## 17.6 Key Points to Remember

### ✅ Always True
- Array name is NOT a modifiable lvalue
- sizeof is compile-time operator
- Macro arguments may be evaluated multiple times
- String literals are in read-only memory
- All pointers are same size on a given architecture

### ❌ Common Mistakes
- Confusing `=` (assignment) with `==` (comparison)
- Forgetting `break` in switch
- Integer division truncates
- Array decay to pointer in function parameters
- Signed-unsigned comparison issues
- Modifying variable twice in expression (UB)

## 17.7 5-Second Sanity Checks

1. **Pointer question?** Check `*` vs `&` usage
2. **Array question?** Remember arr decays to pointer in functions
3. **Recursion question?** Find base case first
4. **sizeof question?** Consider padding
5. **Operator question?** Check precedence table
6. **String question?** Remember null terminator
7. **Output question?** Watch for undefined behavior

---

## 📝 EXAM DAY STRATEGY

### For MCQ (1 mark)
- Time: 2 minutes max
- If unsure after 1 minute, mark for review
- Eliminate obviously wrong options first

### For MSQ (1-2 marks)
- All correct options needed for marks
- Trace code carefully on rough
- Double-check each option

### For NAT (1-2 marks)
- Show complete calculation on rough
- Be careful with decimal precision
- Verify answer makes sense

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]. Ready for Rank-1 simulation.**

---

## 📚 ADDITIONAL RESOURCES

- Practice on: [GATE Overflow](https://gateoverflow.in/)
- Standard Reference: The C Programming Language (K&R)
- Online Judge: [LeetCode](https://leetcode.com/), [HackerRank](https://hackerrank.com/)

---

*Document Version: 1.0 | Last Updated: January 2026 | For: GATE 2026, ESE, PSU, BANK Exams*
