# Chapter 9: Problem Solving Techniques for GATE

## The Singularity | First Principles

> **The Atomic Truth:** "GATE tests pattern recognition + edge case handling + time management."

---

## 9.1 GATE Programming Question Types

### Distribution (Typical)

| Question Type | Marks | Time Allocation |
|---------------|-------|-----------------|
| Output Prediction | 1-2 marks | 1-2 minutes |
| What is the value? | 1-2 marks | 2-3 minutes |
| Time/Space Complexity | 1-2 marks | 1-2 minutes |
| Recurrence Relation | 2 marks | 2-3 minutes |
| Fill in the blank (code) | 2 marks | 3-4 minutes |
| Program Understanding | 2 marks | 3-5 minutes |

### The 60-Second Rule

For 1-mark MCQs: If you can't solve in 60 seconds, mark and move on.

---

## 9.2 Output Prediction | The Systematic Approach

### The TRACE Method

1. **T**able: Create variable tracking table
2. **R**ead: Read code line by line
3. **A**ssign: Update variables in table
4. **C**ompute: Calculate expressions step by step
5. **E**xamine: Check loop/condition boundaries

### Example

```c
int main() {
    int i, j, count = 0;
    for(i = 0; i < 4; i++)
        for(j = i; j < 4; j++)
            count++;
    printf("%d", count);
    return 0;
}
```

**Table Method**:
| i | j values | Iterations |
|---|----------|------------|
| 0 | 0,1,2,3 | 4 |
| 1 | 1,2,3 | 3 |
| 2 | 2,3 | 2 |
| 3 | 3 | 1 |
| **Total** | | **10** |

**Answer**: 10

### The Pattern Recognition

For nested loops `for(i=0; i<n; i++) for(j=i; j<n; j++)`:
$$\text{Count} = \sum_{i=0}^{n-1}(n-i) = n + (n-1) + ... + 1 = \frac{n(n+1)}{2}$$

For n=4: $\frac{4 \times 5}{2} = 10$ ✓

---

## 9.3 Pointer Questions | The Address Method

### Step-by-Step Approach

1. Draw memory boxes with addresses
2. Track pointer values and what they point to
3. Differentiate between `*p`, `p`, `&p`

### Example

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr + 2;
printf("%d %d %d", *p, *(p-1), p[2]);
```

**Visualization**:
```
Index:    0     1     2     3     4
Address: 1000  1004  1008  1012  1016
Value:    10    20    30    40    50
                      ↑
                      p
```

- `*p` = 30 (value at p)
- `*(p-1)` = 20 (value at previous element)
- `p[2]` = *(p+2) = 50 (2 elements ahead)

**Answer**: `30 20 50`

### Common Pointer Patterns

| Pattern | Meaning |
|---------|---------|
| `*p++` | Get value, then increment pointer |
| `(*p)++` | Increment value at pointer |
| `*(p+i)` | Value at p[i] |
| `p - q` | Number of elements between (not bytes) |

---

## 9.4 Recursion Questions | The Tree Method

### Approach

1. Draw the recursion tree
2. Identify base case(s)
3. Trace from leaves to root
4. Count calls or compute return value

### Example

```c
int fun(int n) {
    if(n <= 1) return 1;
    return fun(n-1) + fun(n-2);
}
// What is fun(5)?
```

**Recursion Tree**:
```
                    fun(5)
                   /      \
              fun(4)      fun(3)
             /     \      /    \
         fun(3)  fun(2) fun(2) fun(1)
         /   \    |  \    |  \    |
      fun(2) fun(1) f(1) f(0) f(1) f(0) 1
       |  \    |     |    |    |    |
     f(1) f(0) 1     1    0    1    0
       |    |
       1    0
```

**Computing bottom-up**:
- fun(0) = 1, fun(1) = 1
- fun(2) = 1 + 1 = 2
- fun(3) = 2 + 1 = 3
- fun(4) = 3 + 2 = 5
- fun(5) = 5 + 3 = **8**

### Counting Function Calls

Total calls for fun(n): $2 \times \text{fib}(n+1) - 1$

For fun(5): $2 \times 8 - 1 = 15$ calls

---

## 9.5 Complexity Analysis | Quick Formulas

### Loop Complexity Patterns

| Code Pattern | Complexity |
|--------------|------------|
| `for(i=0; i<n; i++)` | O(n) |
| `for(i=0; i<n; i+=2)` | O(n) |
| `for(i=0; i<n; i*=2)` | O(log n) |
| `for(i=n; i>0; i/=2)` | O(log n) |
| Nested: `for for` (both to n) | O(n²) |
| `for(i=0; i<n; i++) for(j=0; j<i; j++)` | O(n²) |
| `for(i=0; i<n; i++) for(j=0; j<m; j++)` | O(nm) |

### Recurrence Solutions

| Recurrence | Solution |
|------------|----------|
| $T(n) = T(n-1) + c$ | O(n) |
| $T(n) = T(n-1) + n$ | O(n²) |
| $T(n) = T(n/2) + c$ | O(log n) |
| $T(n) = T(n/2) + n$ | O(n) |
| $T(n) = 2T(n/2) + c$ | O(n) |
| $T(n) = 2T(n/2) + n$ | O(n log n) |
| $T(n) = 2T(n-1) + c$ | O(2ⁿ) |
| $T(n) = T(n-1) + T(n-2)$ | O(φⁿ) ≈ O(1.618ⁿ) |

### Master Theorem (Quick Reference)

For $T(n) = aT(n/b) + f(n)$, let $c = \log_b a$:

1. If $f(n) = O(n^{c-\epsilon})$ → $T(n) = \Theta(n^c)$
2. If $f(n) = \Theta(n^c)$ → $T(n) = \Theta(n^c \log n)$
3. If $f(n) = \Omega(n^{c+\epsilon})$ → $T(n) = \Theta(f(n))$

---

## 9.6 Common Traps and Pitfalls

### Trap 1: Operator Precedence

```c
int x = 2;
printf("%d", x+++++x);  // Parsed as (x++) + (++x)
// But behavior is UNDEFINED (multiple modifications)
```

**GATE Rule**: If undefined behavior, it's usually stated. Otherwise, avoid such questions.

### Trap 2: Integer Overflow

```c
int n = 100000;
long long sum = n * (n + 1) / 2;  // n * (n+1) overflows as int!
```

**Fix**: Cast first: `(long long)n * (n + 1) / 2`

### Trap 3: Short-Circuit Evaluation

```c
int a = 0, b = 0;
if(a++ || b++) { }
printf("%d %d", a, b);  // a=1, b=0 or a=1, b=1?
```

**Answer**: `1 1` because `a++` is 0 (false), so `b++` is evaluated.

```c
int a = 1, b = 0;
if(a++ || b++) { }
printf("%d %d", a, b);  // a=2, b=0 (short-circuit)
```

### Trap 4: Array Decay

```c
void foo(int arr[]) {
    printf("%zu", sizeof(arr));  // NOT array size, but pointer size!
}
```

### Trap 5: String Literal Modification

```c
char *s = "Hello";
s[0] = 'J';  // UNDEFINED BEHAVIOR!
```

### Trap 6: Dangling Else

```c
if(a)
    if(b)
        printf("1");
else
    printf("2");  // This else binds to inner if(b), not if(a)
```

---

## 9.7 Quick Calculation Tricks

### Power of 2 Recognition

| Power | Value | Recognizable Form |
|-------|-------|-------------------|
| 2¹⁰ | 1024 | ≈ 1000 (1K) |
| 2²⁰ | 1,048,576 | ≈ 1 million (1M) |
| 2³⁰ | ~1 billion | ≈ 1G |
| 2³² | 4,294,967,296 | ~4 billion |

### Bit Manipulation Shortcuts

| Task | Expression |
|------|------------|
| Check if power of 2 | `n & (n-1) == 0` |
| Get rightmost set bit | `n & (-n)` |
| Turn off rightmost set bit | `n & (n-1)` |
| Count set bits | Brian Kernighan's: loop `n = n & (n-1)` |
| Check if even | `n & 1 == 0` |

### Sum Formulas

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{i=0}^{n-1} 2^i = 2^n - 1$$

$$\sum_{i=0}^{n-1} a \cdot r^i = a \cdot \frac{r^n - 1}{r - 1}$$

---

## 9.8 NAT (Numerical Answer Type) Strategies

### Precision Requirements

- Integer answers: Exact
- Decimal answers: Usually up to 2-3 decimal places
- Range: Check if answer falls within expected bounds

### Common NAT Patterns

1. **Loop count**: Trace carefully or use formula
2. **Function call count**: Draw recursion tree
3. **Address calculation**: Base + offset × size
4. **sizeof questions**: Remember alignment rules

### Example NAT

```c
int f(int n) {
    if(n <= 1) return 1;
    if(n % 2 == 0) return f(n/2);
    return f(n-1) + f(n-2);
}
```

**Find f(10)**:
- f(10) = f(5) [even]
- f(5) = f(4) + f(3) [odd]
- f(4) = f(2) [even]
- f(2) = f(1) = 1 [even]
- f(3) = f(2) + f(1) = 1 + 1 = 2 [odd]
- f(5) = 1 + 2 = 3
- f(10) = **3**

---

## 9.9 MSQ (Multiple Select Questions) Strategies

### Key Approach

1. Evaluate each option independently
2. Look for "definitely true" vs "possibly true"
3. Check edge cases for each option
4. Partial marking: Only check options you're confident about

### Common MSQ Topics

- Properties of algorithms
- Valid/Invalid statements about pointers
- True statements about OOP
- Complexity bounds

### Example MSQ

Which are true about virtual functions in C++?

A. Virtual functions can be static ❌ (static belongs to class, not object)
B. Virtual functions enable runtime polymorphism ✅
C. Constructors can be virtual ❌ (object must exist first)
D. Destructors should be virtual for polymorphic classes ✅

---

## 9.10 Fill in the Blank Strategies

### Approach

1. Read the entire function to understand purpose
2. Identify the blank's role (return, condition, expression?)
3. Test with examples
4. Check boundary conditions

### Example

```c
// Function to find GCD
int gcd(int a, int b) {
    if(b == 0) return ______;
    return gcd(b, a % b);
}
```

**Logic**: When b=0, GCD is a.
**Answer**: `a`

### Another Example

```c
// Binary search
int binarySearch(int arr[], int l, int r, int x) {
    if(r >= l) {
        int mid = l + (r - l) / 2;
        if(arr[mid] == x) return mid;
        if(arr[mid] > x) return binarySearch(arr, l, ______, x);
        return binarySearch(arr, ______, r, x);
    }
    return -1;
}
```

**Answer**: `mid - 1`, `mid + 1`

---

## 9.11 Time Management Strategies

### Recommended Order

1. **Easy MCQs first** (< 1 minute each)
2. **Numerical answers** (usually straightforward calculation)
3. **Medium difficulty** (2-3 minutes each)
4. **Hard questions** (remaining time)

### Time Allocation (65 questions in 180 minutes)

| Question Type | Count | Time Per | Total Time |
|---------------|-------|----------|------------|
| Easy (1-mark) | ~30 | 1 min | 30 min |
| Medium (1-2 mark) | ~20 | 2.5 min | 50 min |
| Hard (2-mark) | ~15 | 4 min | 60 min |
| Review | - | - | 40 min |

### When Stuck

1. Eliminate obvious wrong answers
2. Use examples to test options
3. Make educated guess (no negative for NAT)
4. Mark for review and move on

---

## 9.12 Common GATE Programming Patterns

### Pattern 1: Two Nested Loops - Count Iterations

```c
for(i = 1; i <= n; i *= 2)
    for(j = 1; j <= i; j++)
        count++;
```

**Analysis**: i takes values 1, 2, 4, 8, ..., n (log n values)
Inner loop runs: 1 + 2 + 4 + ... + n = 2n - 1 = **O(n)**

### Pattern 2: Recursion with Print

```c
void fun(int n) {
    if(n > 0) {
        printf("%d ", n);
        fun(n - 1);
        fun(n - 1);
    }
}
fun(3);
```

**Output**: `3 2 1 1 2 1 1`

**Technique**: Trace the calls: fun(3) → print 3, fun(2) → print 2, fun(1) → print 1, fun(0), fun(0), fun(1)...

### Pattern 3: Pointer Arithmetic with Strings

```c
char *s = "GATE2026";
printf("%c %c", *s, *(s+4));
```

**Output**: `G 2`

### Pattern 4: Structure Sizeof

```c
struct X {
    int a;
    char b;
    int c;
};
printf("%zu", sizeof(struct X));
```

**Answer**: 12 (4 + 1 + 3 padding + 4)

---

## 9.13 Exam Day Checklist

### Before the Exam

- [ ] Review formula sheet (complexity, recurrences)
- [ ] Practice 5-10 quick output prediction questions
- [ ] Revise pointer arithmetic rules
- [ ] Review operator precedence table
- [ ] Get good sleep

### During the Exam

- [ ] Read questions completely before answering
- [ ] Draw diagrams for pointers and recursion
- [ ] Double-check NAT calculations
- [ ] Use scratch paper for tracing
- [ ] Don't spend too long on one question
- [ ] Review marked questions if time permits

### Red Flags in Questions

- Undefined behavior → May not have a definite answer
- Platform-dependent → Assume 32-bit unless stated
- Ambiguous syntax → Use precedence rules
- Missing includes → Assume they exist

---

## 9.14 Practice Problems (Exam Simulation)

### Q1 (1 mark, 1 minute)

```c
int main() {
    int x = 5;
    printf("%d %d %d", x, x<<1, x>>1);
    return 0;
}
```

**Answer**: `5 10 2`

### Q2 (1 mark, 1 minute)

```c
int main() {
    char *p = "Hello";
    printf("%c %c", *p++, *p);
    return 0;
}
```

**Answer**: `H e` (but actual behavior may vary - undefined due to sequence point)

**Safe answer with clear code**: If sequence points are clear, trace left-to-right for printf arguments.

### Q3 (2 marks, 3 minutes)

```c
int fun(int n) {
    int count = 0;
    while(n > 0) {
        count++;
        n = n & (n - 1);
    }
    return count;
}
```

What does fun(15) return?

**Answer**: 4 (counts set bits: 15 = 1111 in binary = 4 bits)

### Q4 (2 marks, 3 minutes)

```c
void mystery(int n) {
    if(n > 0) {
        mystery(n / 2);
        printf("%d ", n % 2);
    }
}
mystery(13);
```

**Answer**: `1 1 0 1` (binary representation of 13)

### Q5 (NAT, 2 marks)

What is the time complexity of the following?
```c
for(int i = 1; i <= n; i *= 2)
    for(int j = 0; j < i; j++)
        printf("*");
```

**Answer**: O(n) or Θ(n)

Calculation: 1 + 2 + 4 + ... + n = 2n - 1 = O(n)

---

## 9.15 Quick Reference Card

### Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### Key Formulas

| Formula | Use |
|---------|-----|
| $n(n+1)/2$ | Sum 1 to n |
| $2^n - 1$ | Sum of geometric series (r=2) |
| $\log_2 n$ | Binary search iterations |
| $\frac{n!}{r!(n-r)!}$ | Combinations |

### Sizeof Reference (32-bit)

| Type | Size |
|------|------|
| char | 1 |
| short | 2 |
| int | 4 |
| long | 4 |
| long long | 8 |
| float | 4 |
| double | 8 |
| pointer | 4 |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Exam Ready]**

*Next: [Chapter 10: Previous Year Questions Analysis →](10-PYQ-Analysis.md)*
