# Chapter 4: Arrays and Strings

## The Singularity | First Principles

> **The Atomic Truth:** "Array = Contiguous memory. String = Character array + null."

---

## 4.1 Arrays | The Foundation

### What is an Array?

An array is a **contiguous block of memory** storing elements of the **same type**.

```c
int arr[5] = {10, 20, 30, 40, 50};
```

**Memory Layout**:
```
Address:   1000   1004   1008   1012   1016
           ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
arr:       │ 10 │ │ 20 │ │ 30 │ │ 40 │ │ 50 │
           └────┘ └────┘ └────┘ └────┘ └────┘
Index:       0      1      2      3      4
```

### The Golden Formula

$$\text{Address of arr}[i] = \text{Base Address} + i \times \text{sizeof(element)}$$

**Example**: For `int arr[]` at base address 1000:
- `arr[3]` is at: $1000 + 3 \times 4 = 1012$

---

## 4.2 Array Declaration and Initialization

### Declaration Methods

```c
int arr[5];                    // Uninitialized (garbage values)
int arr[5] = {1, 2, 3, 4, 5};  // Fully initialized
int arr[5] = {1, 2};           // Partial: {1, 2, 0, 0, 0}
int arr[] = {1, 2, 3};         // Size inferred: 3
int arr[5] = {0};              // All zeros
```

### GATE TRAP: Uninitialized Arrays

```c
int arr[5];  // Local array: GARBAGE values
```

```c
int arr[5];  // Global/static array: All zeros
```

**Rule**: 
- Local (auto) arrays → Garbage
- Global/static arrays → Zero-initialized

---

## 4.3 Array and Pointer Relationship

### Arrays Decay to Pointers

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;  // arr decays to pointer to first element
```

### Equivalence Table

| Expression | Equivalent | Result |
|------------|------------|--------|
| `arr[i]` | `*(arr + i)` | Element at index i |
| `&arr[i]` | `arr + i` | Address of element i |
| `arr` | `&arr[0]` | Address of first element |

### When Array Doesn't Decay

1. **sizeof operator**: `sizeof(arr)` gives total array size
2. **Address-of operator**: `&arr` gives pointer to entire array
3. **String literals in initialization**: `char str[] = "Hello"`

### GATE TRAP: arr vs &arr

```c
int arr[5];
printf("%p\n", arr);       // 1000 (type: int*)
printf("%p\n", &arr);      // 1000 (type: int(*)[5])
printf("%p\n", arr + 1);   // 1004 (moves by sizeof(int))
printf("%p\n", &arr + 1);  // 1020 (moves by sizeof(int[5]))
```

---

## 4.4 Multi-Dimensional Arrays

### 2D Array Declaration

```c
int matrix[3][4];  // 3 rows, 4 columns
```

### Memory Layout (Row-Major Order)

```c
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

**In memory**:
```
Address: 1000 1004 1008 1012 1016 1020
         ┌───┬───┬───┬───┬───┬───┐
         │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │
         └───┴───┴───┴───┴───┴───┘
         └── Row 0 ──┘└── Row 1 ──┘
```

### Address Calculation (Row-Major)

For `arr[R][C]`:
$$\text{Address of arr}[i][j] = \text{Base} + (i \times C + j) \times \text{sizeof(element)}$$

**Example**: `int arr[3][4]` at base 1000, find `arr[1][2]`:
$$1000 + (1 \times 4 + 2) \times 4 = 1000 + 24 = 1024$$

### Column-Major Order (For Reference)

$$\text{Address of arr}[i][j] = \text{Base} + (j \times R + i) \times \text{sizeof(element)}$$

**Note**: C uses **Row-Major**. Column-Major is used in Fortran.

---

## 4.5 Passing Arrays to Functions

### 1D Array

```c
void printArray(int arr[], int n) {
    // arr is actually a pointer here
    for(int i = 0; i < n; i++)
        printf("%d ", arr[i]);
}

// Equivalent declarations:
void printArray(int *arr, int n);
void printArray(int arr[10], int n);  // 10 is ignored!
```

### 2D Array

```c
// Column size MUST be specified
void print2D(int arr[][4], int rows) {
    // ...
}

// Or using pointer notation
void print2D(int (*arr)[4], int rows) {
    // ...
}
```

**Why column size?** To compute address: `arr[i][j]` needs to know column count.

### The sizeof Trap

```c
void foo(int arr[]) {
    printf("%zu", sizeof(arr));  // Prints 8 (pointer size)!
}

int main() {
    int arr[100];
    printf("%zu", sizeof(arr));  // Prints 400 (100 × 4)
    foo(arr);
    return 0;
}
```

---

## 4.6 Strings | Character Arrays

### String Basics

A string in C is a **character array terminated by null character '\0'**.

```c
char str[] = "Hello";
// Stored as: {'H', 'e', 'l', 'l', 'o', '\0'}
// Size: 6 bytes (including null terminator)
```

### String Initialization

```c
char str1[] = "Hello";           // Size 6 (includes \0)
char str2[10] = "Hello";         // {'H','e','l','l','o','\0','\0','\0','\0','\0'}
char str3[] = {'H', 'e', 'l', 'l', 'o', '\0'};  // Explicit
char str4[] = {'H', 'e', 'l', 'l', 'o'};        // NOT a string! No \0
```

### String Pointer vs Array

```c
char *str1 = "Hello";   // Points to string literal (READ-ONLY!)
char str2[] = "Hello";  // Creates local modifiable copy
```

**GATE TRAP**:
```c
char *str = "Hello";
str[0] = 'J';  // UNDEFINED BEHAVIOR! String literal is in read-only memory
```

```c
char str[] = "Hello";
str[0] = 'J';  // OK! str is a local array
```

---

## 4.7 String Library Functions

### Essential Functions (string.h)

| Function | Purpose | Returns |
|----------|---------|---------|
| `strlen(s)` | Length (excluding \0) | size_t |
| `strcpy(dest, src)` | Copy src to dest | dest |
| `strncpy(dest, src, n)` | Copy at most n chars | dest |
| `strcat(dest, src)` | Concatenate | dest |
| `strncat(dest, src, n)` | Concat at most n chars | dest |
| `strcmp(s1, s2)` | Compare | <0, 0, >0 |
| `strncmp(s1, s2, n)` | Compare n chars | <0, 0, >0 |
| `strchr(s, c)` | Find char | pointer or NULL |
| `strstr(haystack, needle)` | Find substring | pointer or NULL |

### strlen Implementation

```c
size_t strlen(const char *s) {
    size_t len = 0;
    while(s[len] != '\0')
        len++;
    return len;
}
```

### strcmp Return Values

```c
strcmp("abc", "abc")   // 0 (equal)
strcmp("abc", "abd")   // <0 ('c' < 'd')
strcmp("abd", "abc")   // >0 ('d' > 'c')
strcmp("abc", "ab")    // >0 (longer string)
```

**Mnemonic**: Returns the **ASCII difference** of first differing character.

### strcpy Dangers

```c
char dest[5];
strcpy(dest, "Hello World");  // BUFFER OVERFLOW!
```

**Safe Alternative**: Use `strncpy` with size limit.

```c
char dest[10];
strncpy(dest, src, sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';  // Ensure null termination
```

---

## 4.8 String Manipulation Patterns

### Pattern 1: String Reversal

```c
void reverse(char *str) {
    int left = 0, right = strlen(str) - 1;
    while(left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}
```

### Pattern 2: Palindrome Check

```c
int isPalindrome(char *str) {
    int left = 0, right = strlen(str) - 1;
    while(left < right) {
        if(str[left] != str[right])
            return 0;
        left++;
        right--;
    }
    return 1;
}
```

### Pattern 3: Count Character Occurrences

```c
int countChar(char *str, char c) {
    int count = 0;
    while(*str) {
        if(*str == c) count++;
        str++;
    }
    return count;
}
```

### Pattern 4: Remove Duplicates

```c
void removeDuplicates(char *str) {
    int seen[256] = {0};
    int write = 0;
    
    for(int read = 0; str[read]; read++) {
        if(!seen[(unsigned char)str[read]]) {
            seen[(unsigned char)str[read]] = 1;
            str[write++] = str[read];
        }
    }
    str[write] = '\0';
}
```

---

## 4.9 Array Algorithms | GATE Favorites

### Pattern 1: Find Maximum/Minimum

```c
int findMax(int arr[], int n) {
    int max = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] > max)
            max = arr[i];
    }
    return max;
}
```

### Pattern 2: Linear Search

```c
int linearSearch(int arr[], int n, int key) {
    for(int i = 0; i < n; i++) {
        if(arr[i] == key)
            return i;
    }
    return -1;
}
```

**Time Complexity**: O(n)

### Pattern 3: Binary Search (Array must be sorted)

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    
    while(low <= high) {
        int mid = low + (high - low) / 2;  // Avoid overflow
        
        if(arr[mid] == key)
            return mid;
        else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

**Time Complexity**: O(log n)

### Pattern 4: Array Rotation

```c
// Left rotate by d positions
void leftRotate(int arr[], int n, int d) {
    d = d % n;  // Handle d > n
    
    reverse(arr, 0, d - 1);
    reverse(arr, d, n - 1);
    reverse(arr, 0, n - 1);
}

void reverse(int arr[], int start, int end) {
    while(start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
```

---

## 4.10 Two-Pointer Technique

### Concept

Use two pointers that move toward each other or in the same direction.

### Pattern 1: Two Sum (Sorted Array)

```c
int twoSum(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while(left < right) {
        int sum = arr[left] + arr[right];
        if(sum == target)
            return 1;  // Found
        else if(sum < target)
            left++;
        else
            right--;
    }
    return 0;  // Not found
}
```

### Pattern 2: Remove Element In-Place

```c
int removeElement(int arr[], int n, int val) {
    int write = 0;
    for(int read = 0; read < n; read++) {
        if(arr[read] != val) {
            arr[write++] = arr[read];
        }
    }
    return write;  // New length
}
```

### Pattern 3: Dutch National Flag (3-Way Partition)

```c
void sort012(int arr[], int n) {
    int low = 0, mid = 0, high = n - 1;
    
    while(mid <= high) {
        switch(arr[mid]) {
            case 0:
                swap(&arr[low], &arr[mid]);
                low++;
                mid++;
                break;
            case 1:
                mid++;
                break;
            case 2:
                swap(&arr[mid], &arr[high]);
                high--;
                break;
        }
    }
}
```

---

## 4.11 Sliding Window Technique

### Concept

Maintain a "window" over a contiguous subarray and slide it.

### Pattern: Maximum Sum Subarray of Size k

```c
int maxSumK(int arr[], int n, int k) {
    // Compute sum of first window
    int windowSum = 0;
    for(int i = 0; i < k; i++)
        windowSum += arr[i];
    
    int maxSum = windowSum;
    
    // Slide the window
    for(int i = k; i < n; i++) {
        windowSum += arr[i] - arr[i - k];  // Add new, remove old
        if(windowSum > maxSum)
            maxSum = windowSum;
    }
    
    return maxSum;
}
```

**Time Complexity**: O(n)

---

## 4.12 Character Array Operations

### Character Classification (ctype.h)

| Function | Purpose |
|----------|---------|
| `isalpha(c)` | Is letter? |
| `isdigit(c)` | Is digit 0-9? |
| `isalnum(c)` | Is alphanumeric? |
| `isspace(c)` | Is whitespace? |
| `islower(c)` | Is lowercase? |
| `isupper(c)` | Is uppercase? |
| `tolower(c)` | Convert to lowercase |
| `toupper(c)` | Convert to uppercase |

### ASCII Tricks

```c
'A' to 'Z': 65 to 90
'a' to 'z': 97 to 122
'0' to '9': 48 to 57
```

**Conversions**:
```c
char upper = 'a' - 32;      // 'A'
char lower = 'A' + 32;      // 'a'
int digit = '5' - '0';      // 5 (as integer)
char ch = 7 + '0';          // '7'
```

---

## 4.13 Common GATE Patterns

### Pattern 1: Output Tracing with Arrays

```c
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;
    printf("%d %d", *(p+2), p[3]);
    return 0;
}
```

**Answer**: `3 4`

### Pattern 2: String Manipulation

```c
int main() {
    char str[] = "GATE";
    printf("%c %c", *(str+2), str[3]);
    return 0;
}
```

**Answer**: `T E`

### Pattern 3: 2D Array Addressing

```c
int arr[3][4];
// Base address = 1000, int = 4 bytes
// Find address of arr[2][1]
```

**Answer**: $1000 + (2 \times 4 + 1) \times 4 = 1000 + 36 = 1036$

### Pattern 4: Pointer Arithmetic with 2D

```c
int arr[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
int *p = &arr[0][0];
printf("%d", *(p + 5));
```

**Answer**: `6` (6th element in row-major order)

---

## 4.14 Edge Cases to Remember

### Arrays

1. **Empty array**: n = 0, handle in algorithms
2. **Single element**: May need special handling
3. **All same elements**: Binary search edge cases
4. **Negative indices**: Undefined behavior in C

### Strings

1. **Empty string**: `""` has length 0, but contains `'\0'`
2. **String with spaces**: May split into multiple tokens
3. **Null pointer**: `strlen(NULL)` crashes!
4. **Buffer overflow**: Always check bounds

---

## 4.15 Practice Problems

### Q1 (GATE Style)
```c
int main() {
    char str[] = "IITG";
    char *p = str;
    printf("%d %d", strlen(str), strlen(p));
    return 0;
}
```

**Answer**: `4 4` (Both give length excluding null)

### Q2 (NAT Type)
```c
int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int *p = arr + 2;
    printf("%d", *(p - 1) + p[1]);
    return 0;
}
```

**Answer**: `2 + 4 = 6`
- `p` points to `arr[2]` = 3
- `*(p-1)` = `arr[1]` = 2
- `p[1]` = `arr[3]` = 4

### Q3 (MSQ Type)
Which are valid array declarations?

A. `int arr[5] = {1, 2, 3, 4, 5, 6};`  ❌ (Too many initializers)
B. `int arr[] = {1, 2, 3};`  ✅
C. `int arr[3] = {0};`  ✅
D. `int n = 5; int arr[n];`  ✅ (VLA in C99)

### Q4 (2D Array Address)
```c
int arr[4][5];
// Base = 2000, int = 4 bytes (row-major)
// Find address of arr[3][2]
```

**Answer**: $2000 + (3 \times 5 + 2) \times 4 = 2000 + 68 = 2068$

---

## 4.16 Quick Reference

### Array vs String

| Aspect | Array | String |
|--------|-------|--------|
| Terminator | None required | '\0' required |
| sizeof | Total bytes | Total bytes (incl. \0) |
| strlen | N/A | Length (excl. \0) |

### Complexity Summary

| Operation | Array | String (as array) |
|-----------|-------|-------------------|
| Access by index | O(1) | O(1) |
| Search (unsorted) | O(n) | O(n) |
| Search (sorted) | O(log n) | N/A |
| Insert at end | O(1)* | O(1)* |
| Insert in middle | O(n) | O(n) |
| Delete | O(n) | O(n) |

*Assuming space available

### Address Formulas

**1D**: $\text{addr}[i] = \text{Base} + i \times \text{size}$

**2D Row-Major**: $\text{addr}[i][j] = \text{Base} + (i \times C + j) \times \text{size}$

**2D Column-Major**: $\text{addr}[i][j] = \text{Base} + (j \times R + i) \times \text{size}$

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Intermediate]**

*Next: [Chapter 5: Structures and Unions →](05-Structures-Unions.md)*
