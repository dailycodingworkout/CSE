# Chapter 2: Control Flow
## The Decision Engine | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Code flows like water; control structures are the dams."**

---

## 2.1 Conditional Statements

### The Decision Hierarchy

```
Control Flow
├── Selection (Decision)
│   ├── if
│   ├── if-else
│   ├── if-else-if ladder
│   ├── nested if
│   └── switch-case
├── Iteration (Loops)
│   ├── for
│   ├── while
│   ├── do-while
│   └── nested loops
└── Jump Statements
    ├── break
    ├── continue
    ├── goto
    └── return
```

---

### 2.1.1 The `if` Statement

```c
if (condition) {
    // Executes if condition is TRUE (non-zero)
}
```

**Key Insight:** In C, `0` is FALSE, everything else is TRUE.

```c
if (5)    // TRUE - any non-zero
if (-1)   // TRUE - negative is non-zero
if (0)    // FALSE
if (NULL) // FALSE - NULL is 0
if ('\0') // FALSE - null character is 0
```

### 🚨 GATE Trap: Assignment vs Comparison

```c
int x = 0;
if (x = 5) {  // ASSIGNMENT, not comparison!
    printf("TRUE");
}
// Output: TRUE (because x becomes 5, which is non-zero)
```

**The Fix:** Use `if (5 == x)` - compiler catches `if (5 = x)` as error.

---

### 2.1.2 The `if-else` Statement

```c
if (condition) {
    // TRUE block
} else {
    // FALSE block
}
```

### 🚨 Dangling Else Problem

```c
if (a)
    if (b)
        printf("1");
else
    printf("2");
```

**Question:** Which `if` does the `else` belong to?

**Answer:** The nearest unmatched `if` → the inner one.

**Equivalent to:**
```c
if (a) {
    if (b)
        printf("1");
    else
        printf("2");
}
```

---

### 2.1.3 The Ternary Operator `?:`

```c
result = (condition) ? value_if_true : value_if_false;
```

**Nesting Ternary (GATE Favorite):**
```c
int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
```

**GATE 2016 Style:**
```c
int x = 1, y = 2, z;
z = x > y ? x : y > z ? y : z;
// Parsing: z = (x > y) ? x : ((y > z) ? y : z);
// But z is uninitialized! Undefined behavior!
```

---

### 2.1.4 The `switch-case` Statement

```c
switch (expression) {
    case constant1:
        // statements
        break;
    case constant2:
        // statements
        break;
    default:
        // default statements
}
```

### Switch Rules

| Rule | Description |
|------|-------------|
| Expression type | Must be integral (int, char, enum) |
| Case labels | Must be compile-time constants |
| Duplicate cases | Not allowed |
| Fall-through | Without break, execution continues to next case |
| default | Optional, can be anywhere (conventionally last) |

### 🔥 Fall-Through Trap

```c
int x = 1;
switch(x) {
    case 1: printf("One ");
    case 2: printf("Two ");
    case 3: printf("Three ");
    default: printf("Default ");
}
// Output: One Two Three Default
```

### 🎯 GATE 2019 Style

```c
int x = 2;
switch(x) {
    default: printf("D ");
    case 1: printf("1 ");
    case 2: printf("2 ");
            break;
    case 3: printf("3 ");
}
// Output: 2
```

**Why?** `switch` jumps to matching case, not sequential check.

---

## 2.2 Iteration Statements (Loops)

### 2.2.1 The `for` Loop

```c
for (initialization; condition; update) {
    // body
}
```

**Execution Order:**
1. Initialization (once)
2. Condition check
3. Body execution
4. Update
5. Back to step 2

### Loop Variations

```c
// Infinite loop
for (;;) { }

// Multiple initializations
for (i = 0, j = 10; i < j; i++, j--) { }

// Empty parts
int i = 0;
for (; i < 10;) { i++; }
```

### 🎯 GATE Classic: Loop Count

```c
int count = 0;
for (int i = 0; i < n; i++)
    for (int j = 0; j < i; j++)
        count++;
```

**Total iterations:** 
$$\sum_{i=0}^{n-1} i = 0 + 1 + 2 + ... + (n-1) = \frac{n(n-1)}{2}$$

---

### 2.2.2 The `while` Loop

```c
while (condition) {
    // body - may execute 0 times
}
```

**Use when:** Number of iterations unknown, condition checked first.

### 2.2.3 The `do-while` Loop

```c
do {
    // body - executes at least once
} while (condition);
```

**Use when:** Body must execute at least once (e.g., menu-driven programs).

### 🧠 Loop Comparison

| Aspect | for | while | do-while |
|--------|-----|-------|----------|
| Entry controlled | Yes | Yes | No |
| Exit controlled | No | No | Yes |
| Minimum iterations | 0 | 0 | 1 |
| Use case | Known count | Unknown count | At least once |
| Semicolon at end | No | No | Yes |

---

## 2.3 Jump Statements

### 2.3.1 `break`

- Exits the **innermost** loop or switch
- Cannot break out of multiple nested loops with single break

```c
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    printf("%d ", i);
}
// Output: 0 1 2 3 4
```

### 2.3.2 `continue`

- Skips remaining body, jumps to next iteration
- In `for`: goes to update expression
- In `while`/`do-while`: goes to condition check

```c
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;
    printf("%d ", i);
}
// Output: 0 1 3 4
```

### 🚨 continue in while vs for

```c
// Potential infinite loop!
int i = 0;
while (i < 5) {
    if (i == 2) {
        continue;  // Skips i++!
    }
    printf("%d ", i);
    i++;
}
// Infinite loop at i = 2!

// Safe version
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;  // Still increments
    printf("%d ", i);
}
```

### 2.3.3 `goto`

```c
goto label;
// ...
label:
    // statements
```

**When to use:** Breaking out of nested loops (rare, but valid use).

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        if (condition) goto done;
    }
}
done:
    printf("Exited all loops");
```

### 2.3.4 `return`

- Exits the function immediately
- Returns value to caller (if non-void)

---

## 2.4 Loop Analysis Patterns

### Pattern 1: Counting Loop Iterations

**Method:** Identify start, end, and step.

$$\text{Iterations} = \left\lfloor \frac{\text{end} - \text{start}}{\text{step}} \right\rfloor + 1$$

```c
for (i = 1; i <= n; i++) { }  // n iterations
for (i = 0; i < n; i++) { }   // n iterations
for (i = 1; i < n; i++) { }   // n-1 iterations
for (i = n; i >= 1; i--) { }  // n iterations
```

### Pattern 2: Logarithmic Loops

```c
for (i = 1; i <= n; i *= 2) { }  // log₂(n) iterations
for (i = n; i >= 1; i /= 2) { }  // log₂(n) iterations
for (i = 1; i <= n; i *= 3) { }  // log₃(n) iterations
```

**General Formula:** For `i *= k`, iterations = $\log_k(n)$

### Pattern 3: Nested Loop Analysis

```c
for (i = 1; i <= n; i++) {      // n times
    for (j = 1; j <= n; j++) {  // n times each
        // O(1) work
    }
}
// Total: O(n²)
```

```c
for (i = 1; i <= n; i++) {      // n times
    for (j = 1; j <= i; j++) {  // 1+2+3+...+n times
        // O(1) work
    }
}
// Total: 1+2+...+n = n(n+1)/2 = O(n²)
```

### Pattern 4: Square Root Loops

```c
for (i = 1; i * i <= n; i++) { }  // √n iterations
for (i = 1; i <= n; i = i + √n) { }  // √n iterations
```

---

## 2.5 Loop Invariants (Theoretical Foundation)

A **loop invariant** is a condition that:
1. Is TRUE before the loop starts
2. Remains TRUE after each iteration
3. Helps prove the loop is correct

**Example:** Finding maximum in array
```c
int max = arr[0];  // Invariant: max is largest in arr[0..i-1]
for (int i = 1; i < n; i++) {
    if (arr[i] > max)
        max = arr[i];
    // Invariant still holds: max is largest in arr[0..i]
}
// After loop: max is largest in arr[0..n-1]
```

---

## 2.6 Output Prediction Techniques

### The Dry Run Table Method

```c
int x = 0, y = 5;
while (y-- > 0) {
    x = x + y;
}
printf("%d", x);
```

| Iteration | y (before check) | Condition | y (after decrement) | x |
|-----------|------------------|-----------|---------------------|---|
| 1 | 5 | 5 > 0 ✓ | 4 | 0+4=4 |
| 2 | 4 | 4 > 0 ✓ | 3 | 4+3=7 |
| 3 | 3 | 3 > 0 ✓ | 2 | 7+2=9 |
| 4 | 2 | 2 > 0 ✓ | 1 | 9+1=10 |
| 5 | 1 | 1 > 0 ✓ | 0 | 10+0=10 |
| 6 | 0 | 0 > 0 ✗ | -1 | - |

**Answer:** `10`

**The Trick:** Note that `y--` is post-decrement in condition!

---

## 2.7 Common GATE Patterns

### Pattern: Comma Operator in Loops

```c
for (int i = 0, j = 10; i < j; i++, j--) {
    printf("%d ", i + j);
}
```
- Iterations: 5 (i goes 0,1,2,3,4 and j goes 10,9,8,7,6)
- Each time: i + j = 10
- **Output:** `10 10 10 10 10`

### Pattern: Empty Loop Bodies

```c
int i = 0;
for (; i < 5; printf("%d ", i++));
// The printf IS the body due to semicolon placement!
// Output: 0 1 2 3 4
```

### Pattern: Nested Ternary in Loops

```c
for (int i = 1; i <= 3; i++)
    for (int j = 1; j <= 3; j++)
        printf("%c ", i == j ? '*' : (i + j == 4 ? '+' : '-'));
// Prints a pattern matrix
```

---

## 🎯 Practice Problems

### Problem 1: Loop Output (GATE 2015)
```c
int i;
for (i = 0; i < 10; i++)
    if (i == 5)
        break;
    else
        continue;
printf("%d", i);
```
**Answer:** `5`

### Problem 2: Switch Fall-Through
```c
int x = 3;
switch (x) {
    case 1: x++;
    case 2: x += 2;
    case 3: x += 3;
    default: x += 4;
}
printf("%d", x);
```
**Answer:** `10` (3 + 3 + 4 = 10, fall-through from case 3)

### Problem 3: Nested Loop Count
```c
int count = 0;
for (int i = 1; i <= n; i *= 2)
    for (int j = 1; j <= i; j++)
        count++;
// What is count in terms of n?
```
**Answer:** $2n - 1$ (Geometric series: 1 + 2 + 4 + ... + largest power of 2 ≤ n)

### Problem 4: While with Post-decrement
```c
int x = 5, count = 0;
while (x--) count++;
printf("%d %d", x, count);
```
**Answer:** `-1 5`

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"The IF-ELSE twins lived at a fork in the road. SWITCH was the traffic cop with many lanes. FOR was the marathon runner who knew exactly how many laps. WHILE was the paranoid guard who always checked first. DO-WHILE was the impulsive one who acted first, asked questions later."**

### The Mental Slider
Imagine a water slide with gates:
- **if**: Single gate - pass or stop
- **switch**: Multiple exits at different heights
- **for**: Spiral slide with counter
- **while**: Gate at entrance
- **do-while**: Gate at exit

### The 5-Second Snap-Check
1. **Loop never runs?** Check initial condition
2. **Infinite loop?** Check if update reaches termination
3. **Off-by-one?** Count iterations with small n
4. **Fall-through?** Look for missing `break`
5. **Dangling else?** Find the nearest unmatched `if`

---

## 📈 Time Complexity Summary

| Pattern | Example | Time Complexity |
|---------|---------|-----------------|
| Single loop | `for (i=0; i<n; i++)` | O(n) |
| Nested loop | `for (i=0; i<n; i++) for (j=0; j<n; j++)` | O(n²) |
| Triangular loop | `for (i=0; i<n; i++) for (j=0; j<i; j++)` | O(n²) |
| Logarithmic | `for (i=1; i<n; i*=2)` | O(log n) |
| Log-linear | `for (i=0; i<n; i++) for (j=1; j<n; j*=2)` | O(n log n) |
| Square root | `for (i=1; i*i<=n; i++)` | O(√n) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Fundamentals](01-Fundamentals.md) | [Next: Functions & Recursion →](03-Functions-Recursion.md)
