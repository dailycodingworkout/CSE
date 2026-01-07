# Chapter 2: Pointers and Memory Management

## The Singularity | First Principles

> **The Atomic Truth:** "Pointer = Address. Dereferencing = Go to that Address."

---

## 2.1 Understanding Pointers | The Foundation

### What is a Pointer?

A pointer is a variable that stores a **memory address**.

```c
int x = 42;      // x is stored at some address, say 1000
int *p = &x;     // p stores 1000 (the address of x)
```

### The Visual Model

```
Memory Address:  1000   1004   1008   1012
                 ┌────┐ ┌────┐ ┌────┐ ┌────┐
                 │ 42 │ │1000│ │    │ │    │
                 └────┘ └────┘ └────┘ └────┘
Variable:          x      p
```

**Analogy**: Think of memory as a hotel:
- Each room (memory location) has a **room number** (address)
- A pointer is like a **note** that tells you which room number to visit
- Dereferencing (`*p`) means actually **going to that room**

---

## 2.2 Pointer Declaration and Initialization

### The Syntax

```c
int *p;       // Pointer to int
char *c;      // Pointer to char
float *f;     // Pointer to float
double *d;    // Pointer to double
void *v;      // Generic pointer (can point to anything)
```

### The Two Operators

| Operator | Name | Meaning |
|----------|------|---------|
| `&` | Address-of | Get the address of a variable |
| `*` | Dereference | Access value at the address |

```c
int x = 10;
int *p = &x;   // p = address of x
int y = *p;    // y = value at address p = 10
*p = 20;       // x is now 20 (modified through pointer)
```

### GATE TRAP: Declaration vs Dereferencing

```c
int *p = &x;   // * here is part of declaration
*p = 10;       // * here is dereference operator
```

---

## 2.3 Pointer Arithmetic | The Exam Goldmine

### The Golden Rule

$$\text{ptr} + n = \text{ptr} + n \times \text{sizeof(*ptr)}$$

**Example**:
```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;     // p points to arr[0], address 1000

p + 1  // Points to arr[1], address 1004 (not 1001!)
p + 2  // Points to arr[2], address 1008
```

### Why?

Because `int` is 4 bytes. When you do `p + 1`, C adds `1 × sizeof(int) = 4` bytes.

**Visual**:
```
Address:  1000  1004  1008  1012  1016
          ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
arr:      │10 │ │20 │ │30 │ │40 │ │50 │
          └───┘ └───┘ └───┘ └───┘ └───┘
          p     p+1   p+2   p+3   p+4
```

### Pointer Subtraction

$$\text{ptr1} - \text{ptr2} = \frac{\text{addr1} - \text{addr2}}{\text{sizeof(*ptr)}}$$

```c
int arr[5];
int *p1 = &arr[4];  // Address 1016
int *p2 = &arr[0];  // Address 1000
int diff = p1 - p2; // = (1016-1000)/4 = 4
```

### Valid Pointer Operations

| Operation | Valid? | Result |
|-----------|--------|--------|
| ptr + integer | ✅ | New pointer |
| ptr - integer | ✅ | New pointer |
| ptr1 - ptr2 | ✅ | Integer (if same array) |
| ptr1 + ptr2 | ❌ | Meaningless |
| ptr * integer | ❌ | Meaningless |
| ptr / integer | ❌ | Meaningless |

---

## 2.4 Pointers and Arrays | The Deep Connection

### The Equivalence

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
```

| Expression | Equivalent To | Value |
|------------|---------------|-------|
| `arr[i]` | `*(arr + i)` | Element at index i |
| `p[i]` | `*(p + i)` | Element at index i |
| `&arr[i]` | `arr + i` | Address of index i |
| `arr` | `&arr[0]` | Address of first element |

### GATE TRAP: arr vs &arr

```c
int arr[5];
printf("%p\n", arr);      // 1000 (address of first element)
printf("%p\n", &arr);     // 1000 (address of entire array)
printf("%p\n", arr + 1);  // 1004 (next int)
printf("%p\n", &arr + 1); // 1020 (next array of 5 ints!)
```

**Key Insight**:
- `arr` has type `int*` (pointer to int)
- `&arr` has type `int(*)[5]` (pointer to array of 5 ints)

---

## 2.5 Pointer to Pointer (Double Pointer)

### The Concept

```c
int x = 10;
int *p = &x;      // p points to x
int **pp = &p;    // pp points to p
```

**Visual**:
```
Address:   1000    1004    1008
           ┌────┐  ┌────┐  ┌────┐
           │ 10 │  │1000│  │1004│
           └────┘  └────┘  └────┘
Variable:    x       p       pp
```

### Dereferencing

| Expression | Value |
|------------|-------|
| `pp` | 1004 (address of p) |
| `*pp` | 1000 (value of p, i.e., address of x) |
| `**pp` | 10 (value of x) |

### Use Case: Dynamic 2D Arrays

```c
int **arr = malloc(rows * sizeof(int*));
for(int i = 0; i < rows; i++)
    arr[i] = malloc(cols * sizeof(int));
```

---

## 2.6 Array of Pointers vs Pointer to Array

### Array of Pointers

```c
int *arr[5];  // Array of 5 pointers to int
```

**Memory Layout**:
```
arr[0] → some int
arr[1] → some int
arr[2] → some int
arr[3] → some int
arr[4] → some int
```

**Use Case**: Array of strings
```c
char *names[] = {"Alice", "Bob", "Charlie"};
```

### Pointer to Array

```c
int (*ptr)[5];  // Pointer to an array of 5 ints
```

```c
int arr[5] = {1, 2, 3, 4, 5};
int (*ptr)[5] = &arr;

printf("%d", (*ptr)[2]);  // 3
```

### The Mnemonic

**"Brackets before Star = Array of Pointers"**
**"Star before Brackets (with parentheses) = Pointer to Array"**

```c
int *arr[5];     // [ ] has higher precedence: array of pointers
int (*arr)[5];   // ( ) forces: pointer to array
```

---

## 2.7 Function Pointers

### Declaration

```c
int (*funcPtr)(int, int);  // Pointer to function taking 2 ints, returning int
```

### Usage

```c
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int main() {
    int (*op)(int, int);
    
    op = add;           // or: op = &add;
    printf("%d", op(5, 3));  // 8
    
    op = sub;
    printf("%d", op(5, 3));  // 2
    
    return 0;
}
```

### GATE Pattern: Array of Function Pointers

```c
int (*operations[])(int, int) = {add, sub, mul, div};
int result = operations[0](10, 5);  // Calls add(10, 5)
```

### Callback Functions

```c
void process(int arr[], int n, int (*callback)(int)) {
    for(int i = 0; i < n; i++)
        arr[i] = callback(arr[i]);
}

int square(int x) { return x * x; }

process(arr, 5, square);  // Squares all elements
```

---

## 2.8 Memory Layout of a C Program

### The Four Segments

```
High Address
┌─────────────────┐
│   Command Line  │
│   Arguments     │
├─────────────────┤
│                 │
│      STACK      │ ← Local variables, function calls
│        ↓        │   (grows downward)
│                 │
├─────────────────┤
│                 │
│        ↑        │
│      HEAP       │ ← Dynamic allocation
│                 │   (grows upward)
├─────────────────┤
│      BSS        │ ← Uninitialized global/static
├─────────────────┤
│      DATA       │ ← Initialized global/static
├─────────────────┤
│      TEXT       │ ← Code (read-only)
└─────────────────┘
Low Address
```

### Segment Characteristics

| Segment | Contents | Initialization | Size |
|---------|----------|----------------|------|
| Text | Code | Read-only | Fixed |
| Data | Initialized globals/statics | Explicit | Fixed |
| BSS | Uninitialized globals/statics | Zero | Fixed |
| Heap | Dynamic allocation | Programmer | Variable |
| Stack | Local variables, returns | Automatic | Variable |

---

## 2.9 Dynamic Memory Allocation

### The Four Functions

```c
#include <stdlib.h>

void *malloc(size_t size);           // Allocate, uninitialized
void *calloc(size_t n, size_t size); // Allocate, zero-initialized
void *realloc(void *ptr, size_t size); // Resize allocation
void free(void *ptr);                 // Deallocate
```

### malloc vs calloc

| Feature | malloc | calloc |
|---------|--------|--------|
| Syntax | `malloc(n * sizeof(type))` | `calloc(n, sizeof(type))` |
| Initialization | Garbage values | Zero-initialized |
| Speed | Faster | Slightly slower |
| Overflow Safety | Possible overflow in `n * size` | Handles overflow |

### GATE Pattern: What does malloc return?

```c
int *p = (int*)malloc(10 * sizeof(int));
```

- Returns `void*` which can be assigned to any pointer type
- Returns `NULL` if allocation fails
- Cast is optional in C (required in C++)

### Memory Leak

```c
void leak() {
    int *p = malloc(100);
    // Forgot to free!
}  // p goes out of scope, memory still allocated = LEAK
```

**Rule**: Every `malloc` must have a corresponding `free`.

### Dangling Pointer

```c
int *p = malloc(sizeof(int));
*p = 10;
free(p);
*p = 20;  // UNDEFINED BEHAVIOR! p is dangling
```

**Solution**: Set pointer to NULL after freeing
```c
free(p);
p = NULL;
```

### Double Free

```c
int *p = malloc(sizeof(int));
free(p);
free(p);  // UNDEFINED BEHAVIOR!
```

---

## 2.10 Common Pointer Patterns | GATE Favorites

### Pattern 1: Swap using Pointers

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int x = 5, y = 10;
swap(&x, &y);  // x = 10, y = 5
```

**Why pass pointers?** C is pass-by-value. To modify originals, pass addresses.

### Pattern 2: Return Multiple Values

```c
void minmax(int arr[], int n, int *min, int *max) {
    *min = *max = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] < *min) *min = arr[i];
        if(arr[i] > *max) *max = arr[i];
    }
}

int lo, hi;
minmax(arr, n, &lo, &hi);
```

### Pattern 3: Dynamic Array Resize

```c
int *arr = malloc(10 * sizeof(int));
// ... fill arr ...

// Need more space
arr = realloc(arr, 20 * sizeof(int));

// TRAP: If realloc fails, arr becomes NULL but old memory is lost!
// Safe pattern:
int *temp = realloc(arr, 20 * sizeof(int));
if(temp != NULL) arr = temp;
```

---

## 2.11 Pointer Traps and Pitfalls

### Trap 1: Uninitialized Pointer

```c
int *p;
*p = 10;  // CRASH! p points to random address
```

### Trap 2: Returning Local Address

```c
int* getPtr() {
    int x = 10;
    return &x;  // WRONG! x dies after function returns
}
```

### Trap 3: Array Size in Function

```c
void foo(int arr[]) {
    printf("%zu", sizeof(arr));  // Prints 8 (pointer size), NOT array size!
}
```

**Why?** Arrays decay to pointers when passed to functions.

### Trap 4: String Literal Modification

```c
char *str = "Hello";
str[0] = 'J';  // UNDEFINED BEHAVIOR! String literals are in read-only memory
```

```c
char str[] = "Hello";  // This is fine - creates local copy
str[0] = 'J';          // Works!
```

---

## 2.12 Void Pointer | The Universal Type

### Properties

```c
void *ptr;
```

1. Can hold address of any type
2. Cannot be dereferenced directly
3. Cannot do pointer arithmetic (size unknown)

### Usage Pattern

```c
void *ptr = malloc(sizeof(int));
int *ip = (int*)ptr;  // Cast before use
*ip = 42;
```

### Generic Function Example

```c
void printBytes(void *ptr, size_t n) {
    unsigned char *byte = (unsigned char*)ptr;
    for(size_t i = 0; i < n; i++)
        printf("%02x ", byte[i]);
}

int x = 0x12345678;
printBytes(&x, sizeof(x));  // Prints: 78 56 34 12 (little-endian)
```

---

## 2.13 Null Pointer

### Definition

```c
int *p = NULL;  // or: int *p = 0;
```

`NULL` is typically defined as `((void*)0)`.

### Null Pointer Check

```c
if(p != NULL) {
    *p = 10;
}

// Or more concisely:
if(p) {
    *p = 10;
}
```

### GATE Pattern: What is sizeof(NULL)?

```c
printf("%zu", sizeof(NULL));  // Prints 8 on 64-bit, 4 on 32-bit
```

---

## 2.14 Complex Declarations | Decoding Technique

### The Right-Left Rule

1. Start at identifier
2. Go right until `)` or end
3. Go left until `(` or beginning
4. Repeat

### Examples

```c
int *p;                  // p is pointer to int
int **pp;                // pp is pointer to pointer to int
int *arr[10];            // arr is array of 10 pointers to int
int (*arr)[10];          // arr is pointer to array of 10 ints
int (*fp)(int);          // fp is pointer to function taking int, returning int
int *(*fp)(int);         // fp is pointer to function taking int, returning pointer to int
int (*arr[10])(int);     // arr is array of 10 pointers to functions taking int, returning int
```

### The Declaration Reading Formula

| See | Read As |
|-----|---------|
| `*` | pointer to |
| `[]` | array of |
| `()` | function returning |

---

## 2.15 sizeof with Pointers

### Key Results

```c
int arr[10];
int *p = arr;

sizeof(arr);   // 40 (10 * 4 bytes)
sizeof(p);     // 8 (on 64-bit) or 4 (on 32-bit) - pointer size
sizeof(*p);    // 4 (size of int)
sizeof(&arr);  // 8 (pointer size)
```

### GATE Pattern

```c
char *str = "Hello";
char arr[] = "Hello";

sizeof(str);   // 8 (pointer size)
sizeof(arr);   // 6 (5 chars + null terminator)
strlen(str);   // 5 (doesn't count null)
strlen(arr);   // 5
```

---

## 2.16 Practice Problems

### Q1 (GATE 2019 Style)
```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr + 2;
printf("%d %d %d", p[-1], *p, p[1]);
```

**Answer**: `20 30 40`

**Explanation**:
- `p` points to `arr[2]` (value 30)
- `p[-1]` = `*(p-1)` = `arr[1]` = 20
- `*p` = `arr[2]` = 30
- `p[1]` = `*(p+1)` = `arr[3]` = 40

### Q2 (GATE 2021 Style)
```c
int main() {
    char *p = "GATE";
    printf("%c %c", *(p+1), *p+1);
    return 0;
}
```

**Answer**: `A H`

**Explanation**:
- `*(p+1)` = second character = 'A'
- `*p+1` = 'G' + 1 = 'H' (ASCII arithmetic)

### Q3 (GATE 2017 Style)
```c
int x = 100;
int *p = &x;
int **q = &p;
printf("%d", **q + 1);
```

**Answer**: `101`

**Explanation**: `**q` = value of x = 100, so `**q + 1` = 101

### Q4 (NAT Type)
```c
int arr[4] = {1, 2, 3, 4};
int *p = arr + 3;
printf("%ld", p - arr);
```

**Answer**: `3`

**Explanation**: Pointer difference gives element count, not byte count.

---

## 2.17 Quick Reference

### Memory Functions Summary

| Function | Purpose | Returns |
|----------|---------|---------|
| `malloc(size)` | Allocate bytes | `void*` or `NULL` |
| `calloc(n, size)` | Allocate zeroed | `void*` or `NULL` |
| `realloc(ptr, size)` | Resize | `void*` or `NULL` |
| `free(ptr)` | Deallocate | void |

### Pointer Checklist

- [ ] Always initialize pointers
- [ ] Check for NULL after allocation
- [ ] Never return address of local variable
- [ ] Free all dynamically allocated memory
- [ ] Set pointer to NULL after free
- [ ] Never modify string literals
- [ ] Cast void* before dereferencing

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Intermediate]**

*Next: [Chapter 3: Functions and Recursion →](03-Functions-Recursion.md)*
