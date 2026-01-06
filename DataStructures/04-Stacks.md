# Chapter 4: Stacks

## 🎯 The Atomic Truth
> **"Stack = LIFO = Last In, First Out"**

---

## 4.1 The Mental Model

### The Analogy 💡
Think of a **stack of plates** in a cafeteria:
- You can only add a plate on **top** (push)
- You can only remove the **top** plate (pop)
- You can see only the **top** plate (peek)
- You can't access plates in the middle directly

### Real-World Examples
- Browser back button (history stack)
- Undo operation in text editors
- Function call stack in programming
- Expression evaluation in calculators

---

## 4.2 Stack ADT

### Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| push(x) | Add element x to top | O(1) |
| pop() | Remove and return top element | O(1) |
| peek()/top() | Return top element without removing | O(1) |
| isEmpty() | Check if stack is empty | O(1) |
| size() | Return number of elements | O(1) |
| isFull() | Check if stack is full (array) | O(1) |

### Stack Conditions

**Underflow**: Trying to pop from empty stack
**Overflow**: Trying to push to full stack (array implementation)

---

## 4.3 Implementation

### Array-Based Stack

```python
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1  # Empty stack
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self.stack[self.top]
    
    def size(self):
        return self.top + 1
```

### Linked List-Based Stack

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self.top.data
    
    def size(self):
        return self._size
```

### Comparison: Array vs Linked List Stack

| Aspect | Array Stack | Linked Stack |
|--------|-------------|--------------|
| Size | Fixed | Dynamic |
| Memory | Pre-allocated | On-demand |
| Overflow | Possible | Only by memory limit |
| Cache | Better locality | Poor locality |
| Push/Pop | O(1) | O(1) |

---

## 4.4 Applications of Stack

### Application 1: Balanced Parentheses

**Problem**: Check if expression has balanced brackets

```python
def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Time: O(n), Space: O(n)
```

**Test Cases**:
```
"({[]})" → True
"({[}])" → False (wrong nesting)
"((())"  → False (unmatched opening)
"())"    → False (unmatched closing)
```

### Application 2: Infix to Postfix Conversion

**Operator Precedence**:
| Operator | Precedence | Associativity |
|----------|------------|---------------|
| ^ | 3 | Right to Left |
| *, / | 2 | Left to Right |
| +, - | 1 | Left to Right |

```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative = {'^'}
    
    output = []
    stack = []
    
    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and 
                     token not in right_associative))):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Time: O(n), Space: O(n)
```

**Example**:
```
Infix:   A + B * C - D
         ↓
Postfix: A B C * + D -

Step-by-step:
Token | Stack    | Output
A     | []       | A
+     | [+]      | A
B     | [+]      | A B
*     | [+, *]   | A B
C     | [+, *]   | A B C
-     | [-]      | A B C * +
D     | [-]      | A B C * + D
End   | []       | A B C * + D -
```

### Application 3: Postfix Evaluation

```python
def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            elif token == '^':
                stack.append(a ** b)
    
    return stack[0]

# Time: O(n), Space: O(n)
```

**Example**:
```
Postfix: 2 3 4 * +

Stack trace:
Token | Stack
2     | [2]
3     | [2, 3]
4     | [2, 3, 4]
*     | [2, 12]     # 3 * 4 = 12
+     | [14]        # 2 + 12 = 14

Result: 14
```

### Application 4: Infix to Prefix Conversion

**Algorithm**:
1. Reverse the infix expression
2. Replace '(' with ')' and vice versa
3. Apply infix to postfix
4. Reverse the result

```python
def infix_to_prefix(expression):
    # Reverse and swap parentheses
    reversed_expr = []
    for char in reversed(expression):
        if char == '(':
            reversed_expr.append(')')
        elif char == ')':
            reversed_expr.append('(')
        else:
            reversed_expr.append(char)
    
    # Convert to postfix
    postfix = infix_to_postfix(reversed_expr)
    
    # Reverse to get prefix
    return postfix[::-1]
```

### Application 5: Function Call Stack

```
main() calls f1()
f1() calls f2()
f2() calls f3()

Stack:
┌─────────┐
│   f3    │ ← Top (currently executing)
├─────────┤
│   f2    │
├─────────┤
│   f1    │
├─────────┤
│  main   │ ← Bottom
└─────────┘

When f3() returns → pop f3
When f2() returns → pop f2
...and so on
```

### Application 6: Next Greater Element

```python
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # Stack of indices
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result

# Time: O(n), Space: O(n)
```

**Example**:
```
Input:  [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]

For 4: next greater is 5
For 5: next greater is 10
For 2: next greater is 10
For 10: no greater element → -1
For 8: no greater element → -1
```

### Application 7: Stock Span Problem

```python
def stock_span(prices):
    n = len(prices)
    spans = [0] * n
    stack = []  # Stack of indices
    
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        if not stack:
            spans[i] = i + 1
        else:
            spans[i] = i - stack[-1]
        
        stack.append(i)
    
    return spans

# Time: O(n), Space: O(n)
```

**Example**:
```
Prices: [100, 80, 60, 70, 60, 75, 85]
Spans:  [1,   1,  1,  2,  1,  4,  6]

Day 6 (price 85): Span = 6 (85, 75, 60, 70, 60, 80 all ≤ 85)
```

---

## 4.5 Expression Types

### Comparison Table

| Aspect | Infix | Prefix | Postfix |
|--------|-------|--------|---------|
| Operator position | Between operands | Before operands | After operands |
| Example | A + B | + A B | A B + |
| Parentheses needed | Yes | No | No |
| Human readable | Most | Least | Medium |
| Computer evaluation | Hardest | Easy | Easiest |

### Expression Conversions

| From | To | Method |
|------|-----|--------|
| Infix | Postfix | Use operator stack |
| Infix | Prefix | Reverse → Postfix → Reverse |
| Postfix | Infix | Use operand stack |
| Prefix | Infix | Right-to-left + operand stack |
| Prefix | Postfix | Prefix → Infix → Postfix |
| Postfix | Prefix | Postfix → Infix → Prefix |

---

## 4.6 Two Stacks in One Array

### Method 1: Opposite Ends

```python
class TwoStacks:
    def __init__(self, n):
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n
    
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            raise Exception("Overflow")
    
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            raise Exception("Overflow")
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        raise Exception("Underflow")
    
    def pop2(self):
        if self.top2 < len(self.arr):
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        raise Exception("Underflow")
```

**Visual**:
```
Array: [S1 S1 S1 _ _ _ _ S2 S2 S2]
        ↑              ↑
       top1          top2

Stack 1 grows →
Stack 2 grows ←
```

---

## 4.7 Special Stack Variants

### Min Stack (O(1) getMin)

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# All operations: O(1)
```

### Space-Optimized Min Stack

```python
class MinStackOptimized:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
    
    def push(self, x):
        if x <= self.min_val:
            self.stack.append(self.min_val)  # Store previous min
            self.min_val = x
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top == self.min_val:
                self.min_val = self.stack.pop()  # Restore previous min
            return top
    
    def get_min(self):
        return self.min_val
```

---

## 4.8 Recursion and Stack

### Recursion = Implicit Stack

Every recursive function uses the system's call stack.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

**Call Stack for factorial(4)**:
```
┌─────────────────┐
│ factorial(1)=1  │ ← Returns 1
├─────────────────┤
│ factorial(2)    │ ← Returns 2×1=2
├─────────────────┤
│ factorial(3)    │ ← Returns 3×2=6
├─────────────────┤
│ factorial(4)    │ ← Returns 4×6=24
└─────────────────┘
```

### Converting Recursion to Iteration

**Recursive**:
```python
def print_reverse(node):
    if node is None:
        return
    print_reverse(node.next)
    print(node.data)
```

**Iterative (using explicit stack)**:
```python
def print_reverse_iterative(head):
    stack = []
    current = head
    
    while current:
        stack.append(current.data)
        current = current.next
    
    while stack:
        print(stack.pop())
```

---

## 4.9 GATE Exam Patterns

### Pattern 1: Expression Conversion

**Question Type**: Convert `A + B * C - D / E` to postfix/prefix

**Quick Method**:
1. Identify operator precedence
2. Apply left-to-right (or right-to-left for right-associative)
3. Parenthesize based on precedence
4. Convert each pair

### Pattern 2: Stack Sequence Questions

**Question**: Given push sequence 1,2,3,4,5, which pop sequence is NOT possible?

**Method**: Simulate with stack!

```
Can we get: 3,2,1,5,4?
Push 1,2,3 → Pop 3,2,1 → Push 4,5 → Pop 5,4 ✓

Can we get: 3,1,2,5,4?
Push 1,2,3 → Pop 3 → Need 1 but 2 is on top ✗
```

**The Rule**: In a valid pop sequence, if a[i] < a[j] where i < j, then elements between a[i] and a[j] that are in range (a[i], a[j]) must appear in decreasing order before a[j].

### Pattern 3: Number of Stack Permutations

For n distinct elements pushed in order 1, 2, 3, ..., n:
- Number of valid pop sequences = **Catalan Number**

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)! \cdot n!}$$

| n | Catalan Cₙ |
|---|-----------|
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 14 |
| 5 | 42 |

### Pattern 4: Expression Evaluation

**Trap**: Remember operand order for non-commutative operations!

```
Postfix: 6 3 / → 6 / 3 = 2 (NOT 3 / 6)
         First popped = second operand
         Second popped = first operand
```

---

## 4.10 Edge Cases & Traps

### Common Traps ⚠️

**Trap 1**: Empty Stack Operations
```python
# Always check before pop/peek
if not stack.is_empty():
    stack.pop()
```

**Trap 2**: Expression with Right Associative Operators
```
2 ^ 3 ^ 2 = 2 ^ (3 ^ 2) = 2 ^ 9 = 512
NOT: (2 ^ 3) ^ 2 = 8 ^ 2 = 64
```

**Trap 3**: Unary Operators in Expressions
```
-3 + 5 → Need special handling for leading minus
```

**Trap 4**: Multiple Digits in Expression
```
"12+34" → Need tokenization, not char-by-char
```

---

## 📝 GATE Practice Problems

**Q1**: What is the postfix expression for: `a + b * c - d / e * f`?

**Q2**: Evaluate postfix expression: `5 3 2 * + 4 -`

**Q3**: A stack is used to convert infix to postfix. The infix expression is `a+b*c-d`. The stack can hold at most 2 operators. Is conversion possible?

**Q4**: How many different valid pop sequences are possible if we push elements 1, 2, 3, 4 in order?

**Q5**: Design a stack that supports push, pop, and getMax in O(1) time.

---

## 🎯 Quick Reference

### Expression Conversion Formulas

| Infix | Prefix | Postfix |
|-------|--------|---------|
| A + B | + A B | A B + |
| A + B * C | + A * B C | A B C * + |
| (A + B) * C | * + A B C | A B + C * |
| A + B * C - D | - + A * B C D | A B C * + D - |
| A ^ B ^ C | ^ A ^ B C | A B C ^ ^ |

### Stack Applications Cheat Sheet

| Application | Key Insight |
|-------------|-------------|
| Balanced parentheses | Push opening, pop & match for closing |
| Infix to Postfix | Operators wait for lower precedence |
| Postfix evaluation | Pop two operands, apply operator, push result |
| Function calls | LIFO nature of call/return |
| Next greater element | Maintain decreasing stack |
| Browser history | Push on visit, pop on back |

---

## 🔑 Key Takeaways

1. **Stack = LIFO** - this principle drives all applications
2. **O(1) for all basic operations** - push, pop, peek
3. **Expression conversion** is a GATE favorite
4. **Catalan numbers** count valid stack permutations
5. **Two stacks from opposite ends** is space-efficient
6. **Recursion is implicit stack** - can always be converted to iteration

---

*Next: [Queues →](05-Queues.md)*
