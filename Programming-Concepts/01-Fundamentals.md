# Chapter 1: Fundamentals of Programming
## The Atomic Foundation | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Variables are named memory boxes; Types define box size."**

---

## 1.1 Variables - The Named Memory Containers

### What is a Variable?
A variable is a **named storage location** in memory that holds a value which can be modified during program execution.

**Mental Model:** Think of RAM as a massive hotel. Each variable is a room with:
- A **name** (room number)
- A **type** (room size: single, double, suite)
- A **value** (the guest inside)
- An **address** (physical location)

### Variable Declaration vs Definition

```c
// Declaration: "I will use this variable"
extern int x;

// Definition: "Create this variable now"
int x = 10;

// Initialization: Giving first value
int y = 0;  // Good practice - always initialize!
```

### 🚨 GATE Trap Alert
**Q:** What happens with uninitialized local variables?

```c
int main() {
    int x;
    printf("%d", x);  // Undefined Behavior - GARBAGE VALUE!
    return 0;
}
```
**Answer:** Garbage value (undefined behavior). GATE loves this!

---

## 1.2 Data Types - The Memory Blueprint

### The Type Hierarchy

```
Data Types
├── Primary (Built-in)
│   ├── int      → 4 bytes (typically)
│   ├── char     → 1 byte
│   ├── float    → 4 bytes
│   ├── double   → 8 bytes
│   └── void     → 0 bytes (absence of type)
├── Derived
│   ├── Arrays
│   ├── Pointers
│   ├── Functions
│   └── References (C++)
└── User-Defined
    ├── struct
    ├── union
    ├── enum
    └── typedef
```

### 📊 Size & Range Table (32-bit System)

| Type | Size (bytes) | Range | Format Specifier |
|------|-------------|-------|------------------|
| char | 1 | -128 to 127 | %c |
| unsigned char | 1 | 0 to 255 | %c |
| short | 2 | -32,768 to 32,767 | %hd |
| int | 4 | -2³¹ to 2³¹-1 | %d |
| unsigned int | 4 | 0 to 2³²-1 | %u |
| long | 4 | Same as int (32-bit) | %ld |
| long long | 8 | -2⁶³ to 2⁶³-1 | %lld |
| float | 4 | ±3.4×10³⁸ | %f |
| double | 8 | ±1.7×10³⁰⁸ | %lf |

### 🧮 The Golden Formula
For **n-bit signed integer**:
$$\text{Range} = -2^{n-1} \text{ to } 2^{n-1}-1$$

For **n-bit unsigned integer**:
$$\text{Range} = 0 \text{ to } 2^n - 1$$

### 🎯 GATE 2019 Style Problem
**Q:** What is the output?
```c
char c = 130;
printf("%d", c);
```

**Solution:**
- `char` is signed: range is -128 to 127
- 130 in binary: 10000010
- Interpreted as signed: This is -126 (two's complement)

**Answer:** `-126`

**The Trick:** When value exceeds range, use modular arithmetic:
$$130 - 256 = -126$$

---

## 1.3 Type Modifiers

### The Modifier Matrix

| Modifier | Effect | Example |
|----------|--------|---------|
| `signed` | Can hold negative values (default) | `signed int x` |
| `unsigned` | Only non-negative values | `unsigned int x` |
| `short` | Reduces size | `short int x` |
| `long` | Increases size | `long int x` |
| `const` | Value cannot change | `const int x = 10` |
| `volatile` | Value may change unexpectedly | `volatile int x` |
| `static` | Retains value between function calls | `static int x` |
| `extern` | Variable defined elsewhere | `extern int x` |
| `register` | Store in CPU register (suggestion) | `register int x` |

### Storage Classes Deep Dive

```c
#include <stdio.h>

int global = 100;  // Global: Data segment

void demo() {
    static int persist = 0;  // Static: Data segment, retains value
    int local = 0;           // Auto: Stack, new each call
    persist++;
    local++;
    printf("persist=%d, local=%d\n", persist, local);
}

int main() {
    demo();  // persist=1, local=1
    demo();  // persist=2, local=1
    demo();  // persist=3, local=1
    return 0;
}
```

### 🧠 Memory Segments Mental Map

```
┌─────────────────┐ High Address
│     Stack       │ ← Local variables, function calls
│       ↓         │
│                 │
│       ↑         │
│     Heap        │ ← Dynamic allocation (malloc)
├─────────────────┤
│   BSS Segment   │ ← Uninitialized globals, static
├─────────────────┤
│  Data Segment   │ ← Initialized globals, static
├─────────────────┤
│  Text Segment   │ ← Code (Read-Only)
└─────────────────┘ Low Address
```

---

## 1.4 Operators - The Action Verbs

### Operator Precedence Table (Highest to Lowest)

| Precedence | Operator | Description | Associativity |
|------------|----------|-------------|---------------|
| 1 | `()` `[]` `->` `.` | Function call, array, member | L → R |
| 2 | `++` `--` `!` `~` `*` `&` `sizeof` | Unary operators | R → L |
| 3 | `*` `/` `%` | Multiplication, Division | L → R |
| 4 | `+` `-` | Addition, Subtraction | L → R |
| 5 | `<<` `>>` | Bit shift | L → R |
| 6 | `<` `<=` `>` `>=` | Relational | L → R |
| 7 | `==` `!=` | Equality | L → R |
| 8 | `&` | Bitwise AND | L → R |
| 9 | `^` | Bitwise XOR | L → R |
| 10 | `\|` | Bitwise OR | L → R |
| 11 | `&&` | Logical AND | L → R |
| 12 | `\|\|` | Logical OR | L → R |
| 13 | `?:` | Ternary | R → L |
| 14 | `=` `+=` `-=` etc. | Assignment | R → L |
| 15 | `,` | Comma | L → R |

### 🔥 The Mnemonic
**"Please Excuse My Dear Aunt Sally - But C Has More!"**

Better: **"Pure Unicorns Make Absolutely Safe Reliable Equal Axes, X-raying Opulent Alphabets, Then Commas."**
- **P**ostfix → **U**nary → **M**ultiplicative → **A**dditive → **S**hift → **R**elational → **E**quality → **A**nd (Bitwise) → **X**or → **O**r → **A**nd (Logical) → Then (Ternary) → **C**omma

### Pre-increment vs Post-increment

```c
int a = 5;
int b = a++;  // b = 5, a = 6 (use then increment)
int c = ++a;  // a = 7, c = 7 (increment then use)
```

### 🚨 Undefined Behavior Alert

```c
int i = 5;
int j = i++ + ++i;  // UNDEFINED BEHAVIOR!
// Different compilers give different results
// Never use multiple side effects in one expression
```

---

## 1.5 Bitwise Operators - The Hardware Whisperers

### The Bitwise Toolkit

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | 1 (0101 & 0011 = 0001) |
| `\|` | OR | `5 \| 3` | 7 (0101 \| 0011 = 0111) |
| `^` | XOR | `5 ^ 3` | 6 (0101 ^ 0011 = 0110) |
| `~` | NOT | `~5` | -6 (inverts all bits) |
| `<<` | Left Shift | `5 << 2` | 20 (multiply by 4) |
| `>>` | Right Shift | `20 >> 2` | 5 (divide by 4) |

### 🎯 Golden Formulas

**Left Shift:** $a << n = a \times 2^n$

**Right Shift:** $a >> n = \lfloor a / 2^n \rfloor$

### Bit Manipulation Tricks (GATE Favorites)

```c
// Check if bit at position p is set
(n >> p) & 1

// Set bit at position p
n | (1 << p)

// Clear bit at position p
n & ~(1 << p)

// Toggle bit at position p
n ^ (1 << p)

// Check if power of 2
n > 0 && (n & (n-1)) == 0

// Count set bits (Brian Kernighan's Algorithm)
int count = 0;
while(n) {
    n = n & (n-1);
    count++;
}

// Check if odd or even
n & 1  // 1 = odd, 0 = even

// Swap without temp
a = a ^ b;
b = a ^ b;
a = a ^ b;
```

### 📝 GATE 2017 Style
**Q:** Find value of `(-1 << 1) >> 1` on a machine with 32-bit integers

**Solution:**
- `-1` in binary (2's complement): All 1s (32 bits)
- `-1 << 1`: Shift left, rightmost becomes 0 → `-2`
- For signed right shift, most implementations do arithmetic shift
- `-2 >> 1` = `-1` (sign bit extended)

**Answer:** `-1`

---

## 1.6 Type Casting - The Shape Shifter

### Implicit vs Explicit Casting

```c
// Implicit (Automatic Promotion)
int a = 5;
float b = 2.5;
float c = a + b;  // a promoted to float

// Explicit (Manual Casting)
int x = (int) 3.7;  // x = 3 (truncation)
```

### Type Promotion Rules
1. If either operand is `long double` → both become `long double`
2. Else if either is `double` → both become `double`
3. Else if either is `float` → both become `float`
4. Else integer promotion:
   - `char`, `short` → `int`
   - If either is `unsigned long` → both become `unsigned long`
   - If either is `long` → both become `long`
   - If either is `unsigned int` → both become `unsigned int`

### 🚨 Classic GATE Trap

```c
int main() {
    unsigned int a = 1;
    int b = -1;
    if (a > b)
        printf("a is greater");
    else
        printf("b is greater");
    return 0;
}
```

**Output:** `b is greater`

**Why?** When comparing `unsigned` and `signed`, the signed value is converted to unsigned.
- `-1` as unsigned = `4294967295` (0xFFFFFFFF)
- `4294967295 > 1` → True → Wait, the condition is `a > b`
- So `1 > 4294967295` → False → "b is greater"

---

## 1.7 sizeof Operator - The Memory Measurer

### Key Points
- `sizeof` returns size in bytes
- It's a compile-time operator (mostly)
- Returns type `size_t` (unsigned)

```c
printf("%zu", sizeof(int));       // 4
printf("%zu", sizeof(char));      // 1
printf("%zu", sizeof(int *));     // 4 or 8 (32/64 bit)

int arr[10];
printf("%zu", sizeof(arr));       // 40 (10 * 4)
printf("%zu", sizeof(arr)/sizeof(arr[0]));  // 10 (number of elements)
```

### 🚨 Array vs Pointer Trap

```c
void func(int arr[]) {
    printf("%zu", sizeof(arr));  // 4 or 8 (pointer size!)
}

int main() {
    int arr[10];
    printf("%zu", sizeof(arr));  // 40
    func(arr);
    return 0;
}
```

**Why?** Arrays decay to pointers when passed to functions.

---

## 1.8 Escape Sequences & Special Characters

| Sequence | Meaning |
|----------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\r` | Carriage return |
| `\0` | Null character |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\b` | Backspace |
| `\a` | Alert (beep) |

---

## 🎯 Practice Problems

### Problem 1: Variable Scope (GATE 2018)
```c
int x = 10;
void f() {
    int x = 20;
    {
        int x = 30;
        printf("%d ", x);
    }
    printf("%d ", x);
}
int main() {
    f();
    printf("%d", x);
    return 0;
}
```
**Answer:** `30 20 10`

### Problem 2: sizeof with Arrays
```c
int main() {
    char str[] = "GATE";
    printf("%zu %zu", sizeof(str), strlen(str));
    return 0;
}
```
**Answer:** `5 4` (sizeof includes '\0', strlen doesn't)

### Problem 3: Bitwise Operations
**Q:** What is `(1 << 4) - 1`?
**Answer:** `16 - 1 = 15` (binary: 01111 - all 1s for n positions)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Charlie the Integer lived in a 4-byte house. His pointer friend always knew his address. When Charlie got promoted to float, he got a bigger house but forgot his integer friends."**

### The Mental Slider
Imagine a slider from 0 to 31 (for 32-bit int):
- Slide left = multiply by 2
- Slide right = divide by 2
- Each position is a power of 2

### The 5-Second Snap-Check
- **Overflow?** Check if result fits in type's range
- **Signed/Unsigned mix?** Always convert to unsigned first
- **Pointer vs Array?** In functions, arrays become pointers

---

## 📈 Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Variable access | O(1) | O(1) per variable |
| sizeof | O(1) | - |
| Bitwise ops | O(1) | O(1) |
| Arithmetic | O(1) | O(1) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[Next Chapter: Control Flow →](02-Control-Flow.md)
