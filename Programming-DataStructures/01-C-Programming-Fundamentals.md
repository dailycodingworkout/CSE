# Chapter 1: C Programming Fundamentals

## The Singularity | First Principles

> **The Atomic Truth:** "C is memory-addressable machine abstraction."

---

## 1.1 Introduction to C Programming

### Why C for Competitive Exams?

C is the **foundation language** for GATE/ESE because:
1. **Direct Hardware Control**: C operates closest to machine level among high-level languages
2. **Pointer Arithmetic**: Tests true understanding of memory
3. **Manual Memory Management**: No garbage collector = Full control + Full responsibility
4. **Deterministic Behavior**: Output prediction questions are possible

### The Mental Model

**Analogy**: Think of C as a **universal remote control** for your computer's memory. Every button (variable) is directly wired to a specific memory location. Unlike Python/Java where you just give names and the system figures out where to store things.

---

## 1.2 Data Types in C

### The Hierarchy

```
Primary Types
├── Integer Types
│   ├── char      (1 byte)  → -128 to 127 or 0 to 255
│   ├── short     (2 bytes) → -32,768 to 32,767
│   ├── int       (4 bytes) → -2^31 to 2^31 - 1
│   └── long long (8 bytes) → -2^63 to 2^63 - 1
├── Floating Types
│   ├── float     (4 bytes) → 6 decimal precision
│   ├── double    (8 bytes) → 15 decimal precision
│   └── long double (16 bytes)
└── void (0 bytes - represents "nothing")
```

### The Golden Rule of Size

$$\text{sizeof(char)} \leq \text{sizeof(short)} \leq \text{sizeof(int)} \leq \text{sizeof(long)} \leq \text{sizeof(long long)}$$

**GATE TRAP #1**: `sizeof(int)` is NOT always 4 bytes!
- On 16-bit systems: 2 bytes
- On 32-bit systems: 4 bytes
- On 64-bit systems: 4 bytes (usually)

**The Safe Assumption**: Unless specified, assume 32-bit system with 4-byte int.

---

## 1.3 Type Modifiers

### Signed vs Unsigned

| Modifier | Effect on Range |
|----------|-----------------|
| `signed` | Uses 1 bit for sign (default for int) |
| `unsigned` | All bits for magnitude |

**Example:**
```c
unsigned char x = 255;  // Valid: 0 to 255
signed char y = 255;    // Overflow! -128 to 127 range
```

### The Overflow Trap

```c
unsigned int a = 0;
a = a - 1;  // What is a?
```

**Answer**: $a = 2^{32} - 1 = 4294967295$ (wraps around!)

**Mnemonic**: "Unsigned is a **circular track** - go below 0 and you end up at MAX"

---

## 1.4 Variables and Constants

### Variable Declaration vs Definition

| Term | Meaning | Memory Allocated? |
|------|---------|-------------------|
| Declaration | "This variable exists somewhere" | No |
| Definition | "Create this variable here" | Yes |

```c
extern int x;    // Declaration only (x is defined elsewhere)
int x = 10;      // Definition (memory allocated)
```

### Storage Classes | The Four Pillars

```
Storage Class    | Scope     | Lifetime      | Default Value | Storage
-----------------|-----------|---------------|---------------|----------
auto             | Block     | Block         | Garbage       | Stack
register         | Block     | Block         | Garbage       | CPU Register
static           | Block/File| Program       | 0             | Data Segment
extern           | Global    | Program       | 0             | Data Segment
```

### GATE Favorite: Static Variables

```c
void foo() {
    static int count = 0;
    count++;
    printf("%d ", count);
}

int main() {
    foo(); foo(); foo();  // Output: 1 2 3
    return 0;
}
```

**Why?** Static variables are initialized ONCE and retain value across function calls.

**Analogy**: A static variable is like a **permanent marker** - once written, it stays even after you leave the room (function).

---

## 1.5 Operators and Expressions

### Operator Precedence Table (Exam Critical)

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 (Highest)| `()` `[]` `->` `.` | Left to Right |
| 2 | `!` `~` `++` `--` `+` `-` `*` `&` `sizeof` | Right to Left |
| 3 | `*` `/` `%` | Left to Right |
| 4 | `+` `-` | Left to Right |
| 5 | `<<` `>>` | Left to Right |
| 6 | `<` `<=` `>` `>=` | Left to Right |
| 7 | `==` `!=` | Left to Right |
| 8 | `&` (bitwise) | Left to Right |
| 9 | `^` | Left to Right |
| 10 | `\|` | Left to Right |
| 11 | `&&` | Left to Right |
| 12 | `\|\|` | Left to Right |
| 13 | `?:` | Right to Left |
| 14 | `=` `+=` `-=` etc. | Right to Left |
| 15 (Lowest)| `,` | Left to Right |

### The Mnemonic (PUMA REBL CAT)

**P**arentheses, **U**nary, **M**ultiplicative, **A**dditive, **R**elational, **E**quality, **B**itwise, **L**ogical, **C**onditional, **A**ssignment, **T**erms (comma)

---

## 1.6 Increment and Decrement | The Trap Zone

### Pre vs Post Increment

```c
int a = 5;
int b = ++a;  // Pre: a becomes 6, then b = 6

int c = 5;
int d = c++;  // Post: d = 5, then c becomes 6
```

### GATE TRAP #2: Multiple Side Effects

```c
int a = 5;
int b = a++ + ++a;  // UNDEFINED BEHAVIOR!
```

**Rule**: Never modify a variable more than once in the same expression without a sequence point.

**What is a Sequence Point?**
- End of full expression (`;`)
- `&&`, `||`, `?:`, `,` operators
- Function call (after arguments evaluated)

---

## 1.7 Bitwise Operations | The GATE Gold Mine

### The Six Bitwise Operators

| Operator | Name | Example | Use Case |
|----------|------|---------|----------|
| `&` | AND | `5 & 3 = 1` | Masking bits |
| `\|` | OR | `5 \| 3 = 7` | Setting bits |
| `^` | XOR | `5 ^ 3 = 6` | Toggling bits |
| `~` | NOT | `~5 = -6` | Inverting bits |
| `<<` | Left Shift | `5 << 1 = 10` | Multiply by 2 |
| `>>` | Right Shift | `5 >> 1 = 2` | Divide by 2 |

### The XOR Magic

**Property 1**: $a \oplus a = 0$
**Property 2**: $a \oplus 0 = a$
**Property 3**: $a \oplus b \oplus b = a$

**Application**: Swap without temp variable
```c
a = a ^ b;
b = a ^ b;  // b = (a^b)^b = a
a = a ^ b;  // a = (a^b)^a = b
```

### Bit Manipulation Tricks

| Task | Formula |
|------|---------|
| Check if n is power of 2 | `(n & (n-1)) == 0` |
| Get i-th bit | `(n >> i) & 1` |
| Set i-th bit | `n \| (1 << i)` |
| Clear i-th bit | `n & ~(1 << i)` |
| Toggle i-th bit | `n ^ (1 << i)` |
| Count set bits | Loop with `n & (n-1)` |
| Check if even | `(n & 1) == 0` |
| Multiply by 2^k | `n << k` |
| Divide by 2^k | `n >> k` |

### GATE Pattern: Two's Complement

For n-bit number:
$$\text{Range} = -2^{n-1} \text{ to } 2^{n-1} - 1$$

**To find -x from x**: Invert all bits, add 1
$$-x = \sim x + 1$$

**Example**: Find -5 in 8-bit
```
5  = 00000101
~5 = 11111010
+1 = 11111011  → This is -5
```

---

## 1.8 Control Flow Statements

### The if-else Ladder

```c
if (condition1)
    statement1;
else if (condition2)
    statement2;
else
    statement3;
```

**TRAP**: Dangling else
```c
if (a)
    if (b)
        printf("1");
else
    printf("2");  // This else belongs to inner if!
```

### Switch Statement Rules

1. Expression must be integral type (int, char, enum)
2. Cases must be constant expressions
3. `break` is optional but usually needed
4. `default` is optional but recommended

```c
switch(x) {
    case 1: printf("A");  // Fall-through!
    case 2: printf("B"); break;
    default: printf("C");
}
// If x=1: Output is "AB"
```

---

## 1.9 Loops | The Iteration Trinity

### Loop Types

| Loop | Check Point | Use When |
|------|-------------|----------|
| `while` | Before body | Unknown iterations |
| `do-while` | After body | At least one execution |
| `for` | Before body | Known iterations |

### The For Loop Anatomy

```c
for (init; condition; update) {
    body;
}
```

Execution order: init → condition → body → update → condition → body → update → ...

### GATE Pattern: Loop Output Questions

**Technique**: Trace through with a table
```c
for(int i=0; i<3; i++)
    for(int j=0; j<3; j++)
        printf("%d%d ", i, j);
```

| i | j | Output |
|---|---|--------|
| 0 | 0,1,2 | 00 01 02 |
| 1 | 0,1,2 | 10 11 12 |
| 2 | 0,1,2 | 20 21 22 |

### Infinite Loops

```c
while(1) { }           // Common
for(;;) { }            // Also valid
do { } while(1);       // Less common
```

---

## 1.10 Type Conversion | The Silent Killer

### Implicit Conversion Rules

**Integer Promotion**: char and short → int before operations

**Arithmetic Conversion Hierarchy**:
```
long double > double > float > unsigned long long > long long > 
unsigned long > long > unsigned int > int
```

**Rule**: Smaller type converts to larger type

### The Sign Extension Trap

```c
char c = -1;              // 0xFF (11111111)
unsigned int u = c;       // What is u?
```

**Answer**: `u = 4294967295` (0xFFFFFFFF)

**Why?** Sign bit extends to fill larger type.

### Explicit Casting

```c
int a = 5, b = 2;
float f = a / b;        // f = 2.0 (integer division first!)
float g = (float)a / b; // g = 2.5 (correct)
```

---

## 1.11 Input/Output Functions

### printf Format Specifiers

| Specifier | Type | Example |
|-----------|------|---------|
| `%d` | int | `printf("%d", 42)` |
| `%u` | unsigned int | `printf("%u", 42)` |
| `%ld` | long | `printf("%ld", 42L)` |
| `%f` | float/double | `printf("%f", 3.14)` |
| `%lf` | double (scanf) | `scanf("%lf", &d)` |
| `%c` | char | `printf("%c", 'A')` |
| `%s` | string | `printf("%s", "Hi")` |
| `%p` | pointer | `printf("%p", &x)` |
| `%x` | hex | `printf("%x", 255)` |
| `%o` | octal | `printf("%o", 8)` |

### Width and Precision

```c
printf("%5d", 42);      // "   42" (right-aligned, width 5)
printf("%-5d", 42);     // "42   " (left-aligned)
printf("%05d", 42);     // "00042" (zero-padded)
printf("%.2f", 3.14159);// "3.14" (2 decimal places)
```

### scanf Gotchas

```c
int a;
char c;
scanf("%d", &a);  // Leaves '\n' in buffer
scanf("%c", &c);  // c gets '\n'!

// Solution:
scanf("%d", &a);
scanf(" %c", &c);  // Space skips whitespace
```

---

## 1.12 Quick Reference | Exam Day Cheatsheet

### Size Reference (32-bit system)
| Type | Size | Range |
|------|------|-------|
| char | 1 | -128 to 127 |
| unsigned char | 1 | 0 to 255 |
| short | 2 | -32768 to 32767 |
| int | 4 | $-2^{31}$ to $2^{31}-1$ |
| unsigned int | 4 | 0 to $2^{32}-1$ |
| float | 4 | 6 digits precision |
| double | 8 | 15 digits precision |
| pointer | 4 | - |

### Common Traps Summary

1. **Integer Overflow**: Wraps around silently
2. **Operator Precedence**: `a + b * c` ≠ `(a + b) * c`
3. **Dangling Else**: Pairs with nearest unmatched if
4. **Fall-through in Switch**: Missing break
5. **Side Effects**: Multiple modifications undefined
6. **Division Truncation**: Integer/Integer = Integer
7. **Sign Extension**: char to int expansion

---

## Practice Questions

### Q1 (GATE 2015 Pattern)
```c
int main() {
    int x = -1;
    unsigned int y = x;
    printf("%u", y);
    return 0;
}
```
**Answer**: 4294967295 (all bits set due to sign extension)

### Q2 (GATE 2018 Pattern)
```c
int main() {
    int a = 5, b = 3;
    printf("%d", a+++b);
    return 0;
}
```
**Answer**: 8 (parsed as `(a++) + b` = 5 + 3)

### Q3 (GATE 2020 Pattern)
```c
int main() {
    int i;
    for(i=0; i<3; i++);
    printf("%d", i);
    return 0;
}
```
**Answer**: 3 (semicolon after for creates empty loop body)

---

## Key Takeaways

1. **C gives you power but demands precision**
2. **Memory model understanding is GATE gold**
3. **Operator precedence kills more answers than logic errors**
4. **When in doubt, trace through step by step**
5. **Undefined behavior is NEVER the answer in GATE**

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Foundation Complete]**

*Next: [Chapter 2: Pointers and Memory Management →](02-Pointers-Memory-Management.md)*
