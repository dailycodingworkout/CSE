# Chapter 5: Pointers & Memory Management
## The Memory Masters | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"A pointer is a variable that stores an address; Memory is your program's playground."**

---

## 5.1 Pointer Fundamentals

### What is a Pointer?
A **pointer** is a variable that holds the memory address of another variable.

```c
int x = 10;
int *p = &x;  // p stores address of x
```

### Pointer Declaration and Operators

| Symbol | Name | Purpose |
|--------|------|---------|
| `*` | Dereference | Access value at address |
| `&` | Address-of | Get address of variable |
| `*` (in declaration) | Pointer | Declare pointer variable |

```c
int x = 10;
int *p = &x;    // p points to x

printf("%d", x);    // 10 (value of x)
printf("%p", &x);   // Address of x (e.g., 0x7ffd1234)
printf("%p", p);    // Same address (p stores it)
printf("%d", *p);   // 10 (value at address p)
```

### 🧠 Memory Visualization

```
Variable:     x          p
Value:       10      0x1000
Address:   0x1000    0x2000
           ┌─────┐   ┌─────────┐
           │ 10  │←──│ 0x1000  │
           └─────┘   └─────────┘
```

---

## 5.2 Pointer Types

### Basic Pointer Types

```c
int *ip;      // Pointer to int
char *cp;     // Pointer to char
float *fp;    // Pointer to float
double *dp;   // Pointer to double
void *vp;     // Generic pointer (any type)
```

### Size of Pointers

```c
printf("%zu", sizeof(int*));    // 4 (32-bit) or 8 (64-bit)
printf("%zu", sizeof(char*));   // Same as above
printf("%zu", sizeof(void*));   // Same as above
```

**Key Insight:** All pointer sizes are equal (they all store addresses).

### NULL Pointer

```c
int *p = NULL;  // Points to nothing
if (p == NULL) { /* Check before dereferencing */ }
```

**Dereferencing NULL → Segmentation Fault!**

---

## 5.3 Pointer Arithmetic

### The Golden Rules

For pointer `p` of type `T*`:
- `p + 1` moves forward by `sizeof(T)` bytes
- `p - 1` moves backward by `sizeof(T)` bytes
- `p2 - p1` gives number of elements between them

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;

p + 1   // Address of arr[1]
p + 2   // Address of arr[2]
*(p+3)  // Value 40

int *q = &arr[4];
q - p   // 4 (number of elements)
```

### 🎯 GATE Classic

```c
int arr[] = {10, 20, 30};
int *p = arr;
int *q = arr + 2;

printf("%ld", q - p);   // 2 (not bytes!)
printf("%ld", (char*)q - (char*)p);  // 8 (2 × 4 bytes)
```

### Valid vs Invalid Operations

| Operation | Valid? | Example |
|-----------|--------|---------|
| `p + n` | ✓ | Move forward n elements |
| `p - n` | ✓ | Move backward n elements |
| `p1 - p2` | ✓ | Difference in elements |
| `p1 + p2` | ✗ | Adding addresses meaningless |
| `p * n` | ✗ | Multiplication invalid |
| `p / n` | ✗ | Division invalid |

---

## 5.4 Pointers and Arrays

### The Equivalence

```c
int arr[5] = {10, 20, 30, 40, 50};

arr[i] ≡ *(arr + i)
&arr[i] ≡ arr + i
```

### 🚨 Key Difference

```c
int arr[5];
int *p = arr;

arr = p;  // ERROR! arr is constant
p = arr;  // OK, p is variable
```

### Pointer to Array vs Array of Pointers

```c
int (*p)[5];    // Pointer to array of 5 integers
int *p[5];      // Array of 5 pointers to integers
```

**Memory Layout:**

```
int (*p)[5]:          int *p[5]:
p → [arr of 5 ints]   p[0] → int
                      p[1] → int
                      p[2] → int
                      p[3] → int
                      p[4] → int
```

---

## 5.5 Double Pointers (Pointer to Pointer)

```c
int x = 10;
int *p = &x;
int **pp = &p;

printf("%d", x);     // 10
printf("%d", *p);    // 10
printf("%d", **pp);  // 10

printf("%p", &x);    // Address of x
printf("%p", p);     // Same (stored in p)
printf("%p", *pp);   // Same (stored in *pp)
printf("%p", pp);    // Address of p
```

### 🧠 Visualization

```
Variable:    x           p            pp
Value:      10       0x1000        0x2000
Address:  0x1000     0x2000        0x3000
          ┌─────┐    ┌─────────┐   ┌─────────┐
          │ 10  │←───│ 0x1000  │←──│ 0x2000  │
          └─────┘    └─────────┘   └─────────┘
```

### Use Cases

1. **Modify pointer in function:**
```c
void allocate(int **p) {
    *p = malloc(sizeof(int));
}
```

2. **2D dynamic arrays:**
```c
int **arr = malloc(rows * sizeof(int*));
for (int i = 0; i < rows; i++)
    arr[i] = malloc(cols * sizeof(int));
```

---

## 5.6 Pointers and Functions

### Returning Pointer (DANGER!)

```c
// WRONG - returns address of local variable!
int* getAddress() {
    int x = 10;
    return &x;  // x is destroyed after function returns!
}

// CORRECT - use static or dynamic memory
int* getAddress() {
    static int x = 10;
    return &x;  // x persists
}

int* createInt() {
    int *p = malloc(sizeof(int));
    *p = 10;
    return p;  // Heap memory persists
}
```

### Function Pointers

```c
// Declaration
int (*fp)(int, int);

// Assignment
int add(int a, int b) { return a + b; }
fp = add;  // or fp = &add;

// Call
int result = fp(3, 4);  // or (*fp)(3, 4);
```

### Callback Pattern

```c
void sort(int arr[], int n, int (*compare)(int, int)) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (compare(arr[j], arr[j+1]) > 0) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
}

int ascending(int a, int b) { return a - b; }
int descending(int a, int b) { return b - a; }

sort(arr, n, ascending);   // Sort in ascending order
sort(arr, n, descending);  // Sort in descending order
```

---

## 5.7 const and Pointers

### Four Combinations

```c
int x = 10, y = 20;

// 1. Pointer to constant data (data can't change via pointer)
const int *p1 = &x;
// *p1 = 20;  // ERROR
p1 = &y;      // OK

// 2. Constant pointer to data (pointer can't change)
int *const p2 = &x;
*p2 = 20;     // OK
// p2 = &y;   // ERROR

// 3. Constant pointer to constant data (neither can change)
const int *const p3 = &x;
// *p3 = 20;  // ERROR
// p3 = &y;   // ERROR

// 4. Pointer to non-const data (both can change)
int *p4 = &x;
*p4 = 20;     // OK
p4 = &y;      // OK
```

### Reading Rule: Right to Left

```
const int *p      → p is a pointer to a const int
int *const p      → p is a const pointer to an int
const int *const p → p is a const pointer to a const int
```

---

## 5.8 Dynamic Memory Allocation

### Memory Functions (`#include <stdlib.h>`)

| Function | Purpose | Returns |
|----------|---------|---------|
| `malloc(size)` | Allocate uninitialized memory | `void*` or NULL |
| `calloc(n, size)` | Allocate zero-initialized memory | `void*` or NULL |
| `realloc(ptr, size)` | Resize allocation | `void*` or NULL |
| `free(ptr)` | Release memory | void |

### malloc

```c
int *p = (int*)malloc(5 * sizeof(int));
if (p == NULL) {
    printf("Allocation failed");
    exit(1);
}
// Use p...
free(p);
p = NULL;  // Good practice
```

### calloc

```c
int *p = (int*)calloc(5, sizeof(int));
// All elements initialized to 0
```

### realloc

```c
int *p = malloc(5 * sizeof(int));
p = realloc(p, 10 * sizeof(int));  // Resize to 10
// Old data preserved
```

### 🚨 Memory Pitfalls

1. **Memory Leak:**
```c
void leak() {
    int *p = malloc(100);
    // Forgot to free!
}  // Memory lost forever
```

2. **Dangling Pointer:**
```c
int *p = malloc(sizeof(int));
free(p);
*p = 10;  // UNDEFINED BEHAVIOR!
```

3. **Double Free:**
```c
int *p = malloc(sizeof(int));
free(p);
free(p);  // UNDEFINED BEHAVIOR!
```

4. **Use After Free:**
```c
int *p = malloc(sizeof(int));
free(p);
printf("%d", *p);  // UNDEFINED BEHAVIOR!
```

---

## 5.9 Memory Segments

### Program Memory Layout

```
┌─────────────────────────────────┐ High Address
│           Stack                 │ ← Local variables, function calls
│             ↓                   │    (grows downward)
│                                 │
│             ↑                   │
│           Heap                  │ ← Dynamic allocation (grows upward)
├─────────────────────────────────┤
│     Uninitialized Data (BSS)    │ ← Uninitialized globals, static
├─────────────────────────────────┤
│     Initialized Data            │ ← Initialized globals, static
├─────────────────────────────────┤
│     Text (Code)                 │ ← Program instructions (read-only)
└─────────────────────────────────┘ Low Address
```

### Where Variables Live

```c
int global = 10;           // Initialized Data
int uninit_global;         // BSS
static int static_var = 5; // Initialized Data

int main() {
    int local = 20;        // Stack
    static int s = 3;      // Initialized Data
    int *p = malloc(100);  // p on Stack, allocated memory on Heap
    char *str = "Hello";   // str on Stack, "Hello" in rodata
    return 0;
}
```

---

## 5.10 Complex Pointer Declarations

### Reading Complex Declarations

**Rule:** Start from variable name, go right, then left, alternating.

```c
int *p;                    // p is pointer to int
int *p[10];                // p is array of 10 pointers to int
int (*p)[10];              // p is pointer to array of 10 ints
int *p(void);              // p is function returning pointer to int
int (*p)(void);            // p is pointer to function returning int
int (*p[10])(void);        // p is array of 10 pointers to functions returning int
```

### The Spiral Rule

```
         +---------+
         |  +--+   |
         |  ^  |   |
    int *(*fp[10])(int, char*)
      |   |  ^  |   |
      |   +--+  |   |
      +---------+   
      
Start at fp:
fp → array of 10 → pointers to → functions taking (int, char*) → returning pointer to → int
```

---

## 5.11 Void Pointers

### Generic Pointer

```c
void *vp;

int x = 10;
char c = 'A';

vp = &x;
vp = &c;  // Can point to any type

// Must cast before dereferencing
printf("%d", *(int*)vp);
```

### Use Case: Generic Functions

```c
void swap(void *a, void *b, size_t size) {
    char temp[size];
    memcpy(temp, a, size);
    memcpy(a, b, size);
    memcpy(b, temp, size);
}

int x = 5, y = 10;
swap(&x, &y, sizeof(int));  // Swaps any type!
```

---

## 5.12 Pointer vs Reference (C++ Note)

| Aspect | Pointer | Reference (C++) |
|--------|---------|-----------------|
| Syntax | `int *p = &x` | `int &r = x` |
| NULL | Can be NULL | Cannot be NULL |
| Reassignment | Can point elsewhere | Always refers to same |
| Indirection | Explicit (*p) | Implicit (r) |
| Arithmetic | Supported | Not supported |

---

## 🎯 Practice Problems

### Problem 1: Pointer Output
```c
int arr[] = {10, 20, 30};
int *p = arr;
*p++ = 5;
printf("%d %d", *p, arr[0]);
```
**Answer:** `20 5`

### Problem 2: Double Pointer
```c
int x = 10;
int *p = &x;
int **pp = &p;
**pp = 20;
printf("%d", x);
```
**Answer:** `20`

### Problem 3: Array of Pointers
```c
char *arr[] = {"GATE", "CSE", "2026"};
printf("%c", *arr[1]);
```
**Answer:** `C` (first character of "CSE")

### Problem 4: sizeof Pointer
```c
char *p = "Hello";
printf("%zu %zu", sizeof(p), sizeof("Hello"));
```
**Answer:** `8 6` (64-bit: pointer size vs string size)

### Problem 5: Function Pointer
```c
int f(int x) { return x * x; }
int (*p)(int) = f;
printf("%d", p(5));
```
**Answer:** `25`

### Problem 6: Memory Allocation
```c
int *p = calloc(5, sizeof(int));
printf("%d", p[2]);
```
**Answer:** `0` (calloc initializes to zero)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"A pointer is like a treasure map. The map (pointer) contains coordinates (address). The X marks the spot (dereference) where treasure (value) is buried. Double pointer? A map to find another map!"**

### The Mental Slider
Imagine a parking lot:
- Each spot has an address (memory address)
- The car in the spot is the value
- A pointer is a note saying "Car is in spot A7"
- Pointer arithmetic: Moving to adjacent spots

### The 5-Second Snap-Check
1. **NULL check?** Always before dereferencing
2. **Memory freed?** Set pointer to NULL after free
3. **Returning local address?** Use static or malloc
4. **Array decay?** Remember arrays become pointers in functions
5. **const placement?** Read right-to-left

---

## 📈 Complexity Summary

| Operation | Time | Space |
|-----------|------|-------|
| Dereference | O(1) | O(1) |
| Pointer arithmetic | O(1) | O(1) |
| malloc/calloc | O(1) amortized | O(n) allocated |
| realloc | O(n) worst case | O(new_size) |
| free | O(1) | - |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Arrays & Strings](04-Arrays-Strings.md) | [Next: Data Structures →](06-Data-Structures.md)
