# Chapter 4: Arrays & Strings
## The Contiguous Data Warriors | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Arrays are numbered boxes in a row; Strings are char arrays with a '\0' guard."**

---

## 4.1 Array Fundamentals

### What is an Array?
A **contiguous block of memory** storing elements of the same type, accessible by index.

### Declaration & Initialization

```c
// Declaration
int arr[5];  // 5 integers, garbage values

// Declaration with initialization
int arr[5] = {1, 2, 3, 4, 5};  // All 5 values specified
int arr[5] = {1, 2};           // {1, 2, 0, 0, 0} - rest are 0
int arr[5] = {0};              // All zeros
int arr[] = {1, 2, 3};         // Size inferred = 3

// Designated initializers (C99)
int arr[5] = {[2] = 10, [4] = 20};  // {0, 0, 10, 0, 20}
```

### 🧠 Memory Layout

For `int arr[5] = {10, 20, 30, 40, 50};` at address 1000:

```
Address:  1000    1004    1008    1012    1016
         ┌───────┬───────┬───────┬───────┬───────┐
Values:  │  10   │  20   │  30   │  40   │  50   │
         └───────┴───────┴───────┴───────┴───────┘
Index:      [0]     [1]     [2]     [3]     [4]
```

### The Golden Formula for Address Calculation

$$\text{Address of arr}[i] = \text{Base Address} + i \times \text{sizeof(element)}$$

**Example:** `arr[3] = 1000 + 3 × 4 = 1012`

---

## 4.2 Array and Pointer Relationship

### The Equivalence Rule

```c
arr[i] ≡ *(arr + i)
&arr[i] ≡ (arr + i)
```

### Key Differences

| Aspect | Array Name | Pointer |
|--------|------------|---------|
| Type | `int[5]` | `int*` |
| sizeof | Entire array size | Pointer size (4/8 bytes) |
| Modifiable | No (constant) | Yes |
| Address of | Address of first element | Address of pointer variable |

### 🚨 GATE Trap

```c
int arr[5];
int *p = arr;

printf("%zu\n", sizeof(arr));  // 20 (5 * 4)
printf("%zu\n", sizeof(p));    // 4 or 8 (pointer size)
```

### Array Decay

When passed to functions or assigned to pointers, arrays **decay** to pointers:

```c
void func(int arr[]) {
    // arr is actually a pointer here!
    printf("%zu", sizeof(arr));  // 4 or 8, NOT array size!
}
```

---

## 4.3 Multi-Dimensional Arrays

### 2D Array Declaration

```c
int arr[3][4];  // 3 rows, 4 columns
```

### Memory Layout (Row-Major Order in C)

For `int arr[2][3] = {{1,2,3}, {4,5,6}};`:

```
Logical View:        Memory Layout (Row-Major):
┌───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │  →    │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │
├───┼───┼───┤       └───┴───┴───┴───┴───┴───┘
│ 4 │ 5 │ 6 │       [0][0][0][0][1][1][1][1][2]
└───┴───┴───┘            [0][1][2][0][1][2]
```

### Address Formula for 2D Array (Row-Major)

$$\text{Address of arr}[i][j] = \text{Base} + (i \times \text{cols} + j) \times \text{sizeof(element)}$$

### 🎯 GATE Style Problem

**Q:** For `int arr[4][5]` with base address 2000, find address of `arr[2][3]`.

**Solution:**
- Address = 2000 + (2 × 5 + 3) × 4
- Address = 2000 + 13 × 4
- Address = 2000 + 52 = **2052**

### Column-Major Order (Fortran Style)

$$\text{Address of arr}[i][j] = \text{Base} + (j \times \text{rows} + i) \times \text{sizeof(element)}$$

### 3D Array Address Calculation

For `arr[L][M][N]`:
$$\text{Address of arr}[i][j][k] = \text{Base} + (i \times M \times N + j \times N + k) \times \text{sizeof(element)}$$

---

## 4.4 Passing Arrays to Functions

### Methods

```c
// Method 1: Using unsized array notation
void func(int arr[], int size);

// Method 2: Using pointer notation  
void func(int *arr, int size);

// Method 3: Using sized array (size ignored)
void func(int arr[10], int size);

// For 2D arrays, column size MUST be specified
void func(int arr[][4], int rows);
void func(int (*arr)[4], int rows);  // Pointer to array of 4 ints
```

### 🚨 Common Mistake

```c
void func(int **arr, int rows, int cols);  // WRONG for static 2D array!
```

**Why?** `int**` is pointer to pointer, not pointer to array. Different memory layout!

---

## 4.5 Pointer Arithmetic with Arrays

### Key Relationships

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;

p + 1      // Points to arr[1]
*(p + 2)   // Value 30
p[3]       // Same as *(p + 3) = 40
p - arr    // 0 (difference in elements)

p++        // p now points to arr[1]
*p++       // Returns 20, then p points to arr[2]
*++p       // p points to arr[3], returns 40
++*p       // Increments arr[3] to 41
```

### 🎯 GATE Classic Output

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr;
printf("%d %d %d", *p++, *p++, *p);
```

**Answer:** Undefined behavior! Order of evaluation of function arguments is unspecified.

---

## 4.6 Strings in C

### String Basics

A string is a **null-terminated character array**.

```c
char str1[] = "Hello";    // 6 chars: H e l l o \0
char str2[6] = "Hello";   // Same as above
char str3[10] = "Hello";  // H e l l o \0 \0 \0 \0 \0
char str4[] = {'H','e','l','l','o','\0'};  // Explicit \0
```

### String vs Character Array

```c
char arr[] = {'H', 'i'};     // NOT a string (no \0)
char str[] = {'H', 'i', '\0'}; // IS a string
char str[] = "Hi";           // IS a string (automatic \0)
```

### String Literal vs Array

```c
char str[] = "Hello";   // Array (modifiable, in stack)
char *ptr = "Hello";    // Pointer to string literal (read-only, in rodata)

str[0] = 'h';  // OK
ptr[0] = 'h';  // UNDEFINED BEHAVIOR! (may crash)
```

---

## 4.7 String Library Functions

### `#include <string.h>`

| Function | Purpose | Return |
|----------|---------|--------|
| `strlen(s)` | Length (excluding \0) | `size_t` |
| `strcpy(dest, src)` | Copy src to dest | `char*` dest |
| `strncpy(dest, src, n)` | Copy at most n chars | `char*` dest |
| `strcat(dest, src)` | Concatenate | `char*` dest |
| `strncat(dest, src, n)` | Concat at most n chars | `char*` dest |
| `strcmp(s1, s2)` | Compare strings | `<0`, `0`, `>0` |
| `strncmp(s1, s2, n)` | Compare first n chars | `<0`, `0`, `>0` |
| `strchr(s, c)` | Find first occurrence of c | `char*` or NULL |
| `strrchr(s, c)` | Find last occurrence of c | `char*` or NULL |
| `strstr(s1, s2)` | Find substring s2 in s1 | `char*` or NULL |

### strlen Implementation

```c
size_t strlen(const char *s) {
    size_t len = 0;
    while (s[len] != '\0') len++;
    return len;
}
```

### 🚨 strcmp Return Values

```c
strcmp("abc", "abc");  // 0 (equal)
strcmp("abc", "abd");  // < 0 (a < d in ASCII)
strcmp("abd", "abc");  // > 0
strcmp("abc", "ab");   // > 0 (longer string after equal prefix)
```

**Common Mistake:**
```c
if (strcmp(s1, s2))  // TRUE if NOT equal!
if (!strcmp(s1, s2)) // TRUE if equal
```

---

## 4.8 String Input/Output

### Input Methods

```c
char str[100];

// Method 1: scanf (stops at whitespace)
scanf("%s", str);  // "Hello World" → only "Hello"

// Method 2: scanf with format (stops at newline)
scanf("%[^\n]", str);

// Method 3: fgets (safe, includes newline)
fgets(str, 100, stdin);  // Reads up to 99 chars + \0

// Method 4: gets (DANGEROUS - no bounds check!)
gets(str);  // NEVER use! Buffer overflow vulnerability
```

### Output Methods

```c
printf("%s", str);
puts(str);  // Adds newline automatically
fputs(str, stdout);  // No newline
```

---

## 4.9 Common String Algorithms

### Reverse a String

```c
void reverse(char *str) {
    int left = 0, right = strlen(str) - 1;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}
```

### Check Palindrome

```c
int isPalindrome(char *str) {
    int left = 0, right = strlen(str) - 1;
    while (left < right) {
        if (str[left] != str[right]) return 0;
        left++;
        right--;
    }
    return 1;
}
```

### Count Words

```c
int countWords(char *str) {
    int count = 0, inWord = 0;
    while (*str) {
        if (*str == ' ' || *str == '\t' || *str == '\n') {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            count++;
        }
        str++;
    }
    return count;
}
```

---

## 4.10 Array Manipulation Algorithms

### Linear Search

```c
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return i;
    return -1;
}
```
**Time:** O(n), **Space:** O(1)

### Binary Search

```c
int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Avoids overflow
        if (arr[mid] == key) return mid;
        if (arr[mid] < key) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```
**Time:** O(log n), **Space:** O(1)

### Reverse Array

```c
void reverse(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        int temp = arr[left];
        arr[left++] = arr[right];
        arr[right--] = temp;
    }
}
```

### Rotate Array (Left by d positions)

```c
// Using reversal algorithm
void rotateLeft(int arr[], int n, int d) {
    d = d % n;  // Handle d > n
    reverse(arr, 0, d - 1);
    reverse(arr, d, n - 1);
    reverse(arr, 0, n - 1);
}
```

### Find Maximum and Minimum

```c
void findMinMax(int arr[], int n, int *min, int *max) {
    *min = *max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < *min) *min = arr[i];
        if (arr[i] > *max) *max = arr[i];
    }
}
```

---

## 4.11 Advanced Array Problems

### Find Missing Number (1 to n)

```c
int findMissing(int arr[], int n) {
    int expectedSum = n * (n + 1) / 2;
    int actualSum = 0;
    for (int i = 0; i < n - 1; i++)
        actualSum += arr[i];
    return expectedSum - actualSum;
}
```

### Find Duplicate Element

```c
// Using XOR (when exactly one duplicate exists)
int findDuplicate(int arr[], int n) {
    int result = 0;
    for (int i = 0; i < n; i++)
        result ^= arr[i];
    for (int i = 1; i < n; i++)  // XOR with 1 to n-1
        result ^= i;
    return result;
}
```

### Kadane's Algorithm (Maximum Subarray Sum)

```c
int maxSubarraySum(int arr[], int n) {
    int maxSoFar = arr[0], maxEndingHere = arr[0];
    for (int i = 1; i < n; i++) {
        maxEndingHere = (arr[i] > maxEndingHere + arr[i]) 
                        ? arr[i] : maxEndingHere + arr[i];
        if (maxEndingHere > maxSoFar)
            maxSoFar = maxEndingHere;
    }
    return maxSoFar;
}
```
**Time:** O(n), **Space:** O(1)

---

## 🎯 Practice Problems

### Problem 1: Array Output
```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", 2[arr]);
```
**Answer:** 3 (2[arr] ≡ *(2+arr) ≡ *(arr+2) ≡ arr[2])

### Problem 2: sizeof String
```c
char str[] = "GATE";
printf("%zu %zu", sizeof(str), strlen(str));
```
**Answer:** `5 4`

### Problem 3: String Pointer
```c
char *p = "GATE";
printf("%c %c", *p++, *p);
```
**Answer:** Undefined (order of evaluation). If well-defined: G A

### Problem 4: 2D Array Address
**Q:** For `int arr[3][4]` at base 100, find `&arr[1][2]`.
**Answer:** 100 + (1×4 + 2)×4 = 100 + 24 = 124

### Problem 5: Array Pointer Type
```c
int arr[5];
// What is type of arr + 1?
// What is type of &arr + 1?
```
**Answer:** 
- `arr + 1` is `int*` (points to arr[1])
- `&arr + 1` is `int (*)[5]` (points past entire array)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Arrays are a row of lockers at school. Each locker has a number (index) starting from 0. Strings are special lockers where the last one always has a 'CLOSED' sign (\0) to mark the end. If you forget the sign, you'll keep opening lockers forever!"**

### The Mental Slider
Imagine a train with numbered cars:
- Each car is an element
- The engine (index 0) is at the base address
- To reach car n, walk n × car_length meters
- 2D arrays are trains parked in a rail yard, row by row

### The 5-Second Snap-Check
1. **Array bounds?** Check if index < size
2. **String null-terminator?** Include space for '\0'
3. **sizeof vs strlen?** sizeof includes '\0', strlen doesn't
4. **2D address?** Use formula: Base + (i×cols + j)×size
5. **Decay to pointer?** Arrays become pointers in functions

---

## 📈 Complexity Summary

| Operation | Time | Space |
|-----------|------|-------|
| Access by index | O(1) | O(1) |
| Linear search | O(n) | O(1) |
| Binary search | O(log n) | O(1) |
| Insert at end | O(1) | O(1) |
| Insert at position | O(n) | O(1) |
| Delete from position | O(n) | O(1) |
| strlen | O(n) | O(1) |
| strcpy | O(n) | O(1) |
| strcmp | O(n) | O(1) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Functions & Recursion](03-Functions-Recursion.md) | [Next: Pointers & Memory →](05-Pointers-Memory.md)
