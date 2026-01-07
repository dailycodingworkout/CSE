# Chapter 5: Structures and Unions

## The Singularity | First Principles

> **The Atomic Truth:** "Structure = Custom type with named fields. Union = Shared memory for different types."

---

## 5.1 Structures | User-Defined Types

### What is a Structure?

A structure is a **user-defined data type** that groups related variables of **different types** under a single name.

```c
struct Student {
    int id;
    char name[50];
    float gpa;
};
```

### Memory Layout

```
struct Student (size = 60 bytes with padding)
┌────────┬─────────────────────────┬────────┬────────┐
│   id   │         name[50]        │padding │  gpa   │
│ 4 bytes│        50 bytes         │2 bytes │4 bytes │
└────────┴─────────────────────────┴────────┴────────┘
Offset: 0        4                  54       56
```

**Analogy**: A structure is like a **form** with multiple fields. Each field has a name and a type, and together they describe something complex.

---

## 5.2 Structure Declaration and Initialization

### Declaration Methods

```c
// Method 1: Declare type, then variable
struct Point {
    int x;
    int y;
};
struct Point p1;

// Method 2: Declare together
struct Point {
    int x;
    int y;
} p1, p2;

// Method 3: Anonymous structure
struct {
    int x;
    int y;
} p1;  // Can't create more variables of this type

// Method 4: Using typedef
typedef struct {
    int x;
    int y;
} Point;
Point p1;  // No 'struct' keyword needed
```

### Initialization

```c
// Method 1: Ordered initialization
struct Point p1 = {10, 20};

// Method 2: Designated initializers (C99)
struct Point p2 = {.y = 20, .x = 10};

// Method 3: Partial initialization (remaining = 0)
struct Student s = {1};  // id=1, name="", gpa=0.0

// Method 4: Member-by-member
struct Point p3;
p3.x = 10;
p3.y = 20;
```

---

## 5.3 Accessing Structure Members

### Dot Operator (.)

Used with structure variables.

```c
struct Point p = {10, 20};
printf("%d %d", p.x, p.y);  // 10 20
```

### Arrow Operator (->)

Used with structure pointers.

```c
struct Point p = {10, 20};
struct Point *ptr = &p;

printf("%d %d", ptr->x, ptr->y);  // 10 20
// Equivalent to:
printf("%d %d", (*ptr).x, (*ptr).y);  // 10 20
```

### The Mnemonic

- **Dot** (.) = Direct access (when you HAVE the struct)
- **Arrow** (->) = Pointer access (when you have ADDRESS of struct)

---

## 5.4 Structure Memory | Alignment and Padding

### Why Padding?

CPUs access memory more efficiently when data is aligned to its natural boundary.

### Alignment Rules

1. Each member is aligned to its own size (or a smaller alignment)
2. Structure size is a multiple of the largest member's alignment

### Example Analysis

```c
struct Example1 {
    char a;    // 1 byte
    int b;     // 4 bytes
    char c;    // 1 byte
};
```

**Memory Layout**:
```
┌───┬───────┬────────┬───┬───────┐
│ a │padding│   b    │ c │padding│
│ 1 │   3   │   4    │ 1 │   3   │
└───┴───────┴────────┴───┴───────┘
Total: 12 bytes
```

### Optimized Structure

```c
struct Example2 {
    int b;     // 4 bytes
    char a;    // 1 byte
    char c;    // 1 byte
};
```

**Memory Layout**:
```
┌────────┬───┬───┬───────┐
│   b    │ a │ c │padding│
│   4    │ 1 │ 1 │   2   │
└────────┴───┴───┴───────┘
Total: 8 bytes
```

### The Golden Rule

**Order members from largest to smallest to minimize padding.**

### sizeof Structure

```c
struct A {
    char c;
    int i;
    double d;
};

printf("%zu", sizeof(struct A));  // 16 (not 13!)
```

**Calculation**:
- char c: 1 byte at offset 0
- Padding: 3 bytes (to align int)
- int i: 4 bytes at offset 4
- double d: 8 bytes at offset 8
- Total: 16 bytes

---

## 5.5 Structure and Pointers

### Pointer to Structure

```c
struct Point {
    int x, y;
};

struct Point p = {10, 20};
struct Point *ptr = &p;

// Access members
ptr->x = 30;  // or (*ptr).x = 30;
```

### Dynamic Allocation

```c
struct Point *p = (struct Point*)malloc(sizeof(struct Point));
p->x = 10;
p->y = 20;
// ...
free(p);
```

### Array of Structures

```c
struct Student students[100];
students[0].id = 1;
strcpy(students[0].name, "Alice");
```

### Self-Referential Structures

```c
struct Node {
    int data;
    struct Node *next;  // Pointer to same type
};
```

This is the foundation of linked lists, trees, and graphs.

---

## 5.6 Passing Structures to Functions

### Pass by Value

```c
void printPoint(struct Point p) {
    printf("%d %d", p.x, p.y);
}

struct Point p = {10, 20};
printPoint(p);  // Copies entire structure
```

**Issue**: For large structures, copying is expensive.

### Pass by Pointer (Recommended)

```c
void printPoint(struct Point *p) {
    printf("%d %d", p->x, p->y);
}

struct Point p = {10, 20};
printPoint(&p);  // Only passes address (4 or 8 bytes)
```

### Return Structure

```c
struct Point createPoint(int x, int y) {
    struct Point p = {x, y};
    return p;  // Returns copy (valid but may be slow)
}
```

### Return Pointer (Be Careful!)

```c
// WRONG - Returns address of local variable
struct Point* createPoint(int x, int y) {
    struct Point p = {x, y};
    return &p;  // DANGLING POINTER!
}

// CORRECT - Dynamic allocation
struct Point* createPoint(int x, int y) {
    struct Point *p = malloc(sizeof(struct Point));
    p->x = x;
    p->y = y;
    return p;  // Caller must free
}
```

---

## 5.7 Nested Structures

### Definition

```c
struct Date {
    int day, month, year;
};

struct Employee {
    int id;
    char name[50];
    struct Date dob;       // Nested structure
    struct Date joining;
};
```

### Access

```c
struct Employee emp = {
    .id = 1,
    .name = "Alice",
    .dob = {15, 8, 1995},
    .joining = {1, 6, 2020}
};

printf("%d/%d/%d", emp.dob.day, emp.dob.month, emp.dob.year);
// Output: 15/8/1995
```

### With Pointers

```c
struct Employee *ptr = &emp;
printf("%d", ptr->dob.year);  // 1995
```

---

## 5.8 Bit Fields

### Definition

Pack multiple values into a single memory unit.

```c
struct Flags {
    unsigned int bold : 1;      // 1 bit
    unsigned int italic : 1;    // 1 bit
    unsigned int underline : 1; // 1 bit
    unsigned int : 5;           // 5 bits padding (unnamed)
    unsigned int size : 8;      // 8 bits
};
```

### Use Cases

1. Memory-constrained systems
2. Hardware register mapping
3. Network protocols
4. File format parsing

### Limitations

1. Cannot take address of bit field (`&` not allowed)
2. Cannot have arrays of bit fields
3. Portability issues (bit order varies by architecture)

---

## 5.9 Unions | Shared Memory

### What is a Union?

A union is like a structure, but **all members share the same memory location**.

```c
union Data {
    int i;
    float f;
    char str[20];
};
```

### Memory Layout

```
┌──────────────────────────────────────┐
│            20 bytes                  │
│  (can be accessed as i, f, or str)   │
└──────────────────────────────────────┘
Size = max(sizeof(members)) = 20 bytes
```

### Key Difference from Structure

| Aspect | Structure | Union |
|--------|-----------|-------|
| Memory | Each member has own | All share same |
| Size | Sum of all (+ padding) | Max of all |
| Access | All members valid | Only one at a time |
| Use | Group related data | Memory-efficient alternatives |

### Example

```c
union Data d;

d.i = 42;
printf("%d\n", d.i);  // 42

d.f = 3.14;           // Overwrites integer
printf("%f\n", d.f);  // 3.14
printf("%d\n", d.i);  // Garbage (not 42!)
```

---

## 5.10 Union Applications

### 1. Type Punning (View Memory Differently)

```c
union FloatBits {
    float f;
    unsigned int bits;
};

union FloatBits fb;
fb.f = 3.14;
printf("Bits: 0x%08X\n", fb.bits);  // View float as bits
```

### 2. Variant Types

```c
enum Type { INT, FLOAT, STRING };

struct Variant {
    enum Type type;
    union {
        int i;
        float f;
        char s[20];
    } value;
};

struct Variant v;
v.type = INT;
v.value.i = 42;
```

### 3. Memory-Efficient Storage

```c
union IPAddress {
    unsigned int full;           // 32-bit integer
    unsigned char bytes[4];      // 4 bytes
};

union IPAddress ip;
ip.full = 0xC0A80101;  // 192.168.1.1
printf("%d.%d.%d.%d", ip.bytes[3], ip.bytes[2], 
       ip.bytes[1], ip.bytes[0]);
```

---

## 5.11 Enumeration (enum)

### Definition

Named integer constants.

```c
enum Day {
    SUNDAY,     // 0
    MONDAY,     // 1
    TUESDAY,    // 2
    WEDNESDAY,  // 3
    THURSDAY,   // 4
    FRIDAY,     // 5
    SATURDAY    // 6
};
```

### Custom Values

```c
enum Color {
    RED = 1,
    GREEN = 2,
    BLUE = 4    // Powers of 2 for flags
};
```

### Usage

```c
enum Day today = MONDAY;
printf("%d\n", today);  // 1

// Can use as flags
unsigned int flags = RED | BLUE;
if(flags & RED) printf("Has red\n");
```

### enum vs #define

| Aspect | enum | #define |
|--------|------|---------|
| Type safety | Yes | No |
| Debugging | Shows name | Shows number |
| Scope | Block/file | File |
| Multiple values | Natural | Verbose |

---

## 5.12 typedef | Type Aliases

### Basic Usage

```c
typedef unsigned long ulong;
typedef int* IntPtr;
typedef struct Point Point;  // Common pattern
```

### With Structures

```c
// Without typedef
struct Point {
    int x, y;
};
struct Point p;  // Must use 'struct'

// With typedef
typedef struct {
    int x, y;
} Point;
Point p;  // No 'struct' needed
```

### Complex typedef

```c
// Array type
typedef int IntArray[10];
IntArray arr;  // Same as: int arr[10];

// Function pointer type
typedef int (*Operation)(int, int);
Operation op = add;
```

---

## 5.13 Common GATE Patterns

### Pattern 1: sizeof Structure

```c
struct A {
    char c;
    int i;
};
printf("%zu", sizeof(struct A));
```

**Answer**: 8 (1 char + 3 padding + 4 int)

### Pattern 2: sizeof Union

```c
union B {
    char c;
    int i;
    double d;
};
printf("%zu", sizeof(union B));
```

**Answer**: 8 (size of largest member: double)

### Pattern 3: Structure with Pointer

```c
struct Node {
    int data;
    struct Node *next;
};
printf("%zu", sizeof(struct Node));
```

**Answer**: 16 on 64-bit (4 int + 4 padding + 8 pointer)
         8 on 32-bit (4 int + 4 pointer)

### Pattern 4: Union Access After Assignment

```c
union X {
    int i;
    char c[4];
};
union X x;
x.i = 0x41424344;
printf("%c", x.c[0]);  // Little-endian system
```

**Answer**: 'D' (0x44 is 'D' in ASCII)

On little-endian: LSB first, so c[0] = 0x44 = 'D'

---

## 5.14 Structure Alignment GATE Questions

### Q1: Calculate sizeof

```c
struct X {
    double d;
    int i;
    char c;
};
```

**Answer**: 
- double d: 8 bytes at offset 0
- int i: 4 bytes at offset 8
- char c: 1 byte at offset 12
- Padding: 3 bytes (to make total multiple of 8)
- **Total: 16 bytes**

### Q2: Reorder for Minimum Size

```c
struct Y {
    char a;
    double b;
    int c;
    char d;
};
```

**Original**: 24 bytes
**Optimized** (double, int, char, char): 16 bytes

### Q3: Bit Field sizeof

```c
struct Z {
    unsigned int a : 5;
    unsigned int b : 5;
    unsigned int c : 5;
    unsigned int d : 5;
};
printf("%zu", sizeof(struct Z));
```

**Answer**: 4 bytes (20 bits packed into 1 int)

---

## 5.15 Self-Referential Structures | Linked List Foundation

### Node Definition

```c
struct Node {
    int data;
    struct Node *next;
};
```

### Creating a Linked List

```c
struct Node* createNode(int data) {
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

int main() {
    struct Node *head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    
    // Traverse
    struct Node *curr = head;
    while(curr != NULL) {
        printf("%d ", curr->data);
        curr = curr->next;
    }
    // Output: 1 2 3
    
    return 0;
}
```

### Memory Visualization

```
head
  ↓
┌───────────┐    ┌───────────┐    ┌───────────┐
│ data: 1   │    │ data: 2   │    │ data: 3   │
│ next: ─────────→ next: ─────────→ next: NULL│
└───────────┘    └───────────┘    └───────────┘
```

---

## 5.16 Flexible Array Members (C99)

### Definition

```c
struct Buffer {
    int size;
    char data[];  // Flexible array member (MUST be last)
};
```

### Usage

```c
struct Buffer *buf = malloc(sizeof(struct Buffer) + 100);
buf->size = 100;
strcpy(buf->data, "Hello");
```

### Why Use?

Avoid double indirection:
```c
// Old way
struct OldBuffer {
    int size;
    char *data;  // Requires separate allocation
};

// Flexible array way - single allocation
struct Buffer *buf = malloc(sizeof(struct Buffer) + n);
```

---

## 5.17 Practice Problems

### Q1 (GATE 2019 Style)

```c
struct Point {
    int x, y;
};

int main() {
    struct Point p = {10, 20};
    struct Point *ptr = &p;
    (*ptr).x = 30;
    ptr->y = 40;
    printf("%d %d", p.x, p.y);
    return 0;
}
```

**Answer**: `30 40`

### Q2 (NAT Type)

```c
struct A {
    char c;
    short s;
    int i;
    char d;
};
```

What is sizeof(struct A)?

**Answer**: 12
- c: 1 byte at 0
- padding: 1 byte
- s: 2 bytes at 2
- i: 4 bytes at 4
- d: 1 byte at 8
- padding: 3 bytes
- Total: 12

### Q3 (MSQ Type)

Which statements about unions are TRUE?

A. All members share the same memory location ✅
B. Size equals sum of all member sizes ❌
C. Only one member can be validly accessed at a time ✅
D. Cannot have pointer members ❌

### Q4 (Output)

```c
union U {
    int i;
    float f;
};

int main() {
    union U u;
    u.i = 10;
    printf("%d\n", u.i);
    u.f = 10.0;
    printf("%d\n", u.i);  // What prints?
    return 0;
}
```

**Answer**: 
- First: 10
- Second: 1092616192 (or some large number - float representation of 10.0 interpreted as int)

---

## 5.18 Quick Reference

### Structure vs Union

| Feature | Structure | Union |
|---------|-----------|-------|
| Keyword | `struct` | `union` |
| Memory | Separate for each | Shared |
| Size | Sum + padding | Max member |
| Access | All valid | One at a time |

### sizeof Formulas

**Structure**: Sum of members + alignment padding
**Union**: Max(member sizes) aligned to largest

### Member Access

| Syntax | When to Use |
|--------|-------------|
| `s.member` | Direct access to structure variable |
| `ptr->member` | Access through structure pointer |
| `(*ptr).member` | Same as above (rarely used) |

### Common Patterns

1. **typedef struct**: Cleaner syntax
2. **Self-referential**: Linked structures
3. **Nested structures**: Complex data
4. **Union with enum**: Type-safe variants
5. **Bit fields**: Compact storage

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Intermediate]**

*Next: [Chapter 6: Object-Oriented Programming Concepts →](06-OOP-Concepts.md)*
