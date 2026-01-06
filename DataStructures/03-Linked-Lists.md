# Chapter 3: Linked Lists

## 🎯 The Atomic Truth
> **"Linked List = Nodes + Pointers = Dynamic Sequential Access"**

---

## 3.1 The Mental Model

### The Analogy 💡
Think of a **treasure hunt**:
- Each clue (node) contains a **treasure** (data) and **location of next clue** (pointer)
- You MUST follow the chain - can't jump directly to clue #5
- Adding/removing clues is easy - just update the directions

### Why Linked Lists?

| Array Limitation | Linked List Solution |
|------------------|---------------------|
| Fixed size | Dynamic size |
| Expensive insertion/deletion | O(1) insert/delete at known position |
| Memory must be contiguous | Scattered memory is fine |
| Wasteful pre-allocation | Allocate as needed |

---

## 3.2 Types of Linked Lists

### 1. Singly Linked List

```
┌──────┬───┐    ┌──────┬───┐    ┌──────┬───┐    ┌──────┬────┐
│  10  │ ●─┼───→│  20  │ ●─┼───→│  30  │ ●─┼───→│  40  │NULL│
└──────┴───┘    └──────┴───┘    └──────┴───┘    └──────┴────┘
   HEAD                                              TAIL

Each node: [Data | Next Pointer]
```

**Node Structure**:
```c
struct Node {
    int data;
    struct Node* next;
};
```

### 2. Doubly Linked List

```
       ┌───┬──────┬───┐    ┌───┬──────┬───┐    ┌───┬──────┬───┐
NULL ←─┤ ● │  10  │ ●─┼───→│ ●←┼  20  │ ●─┼───→│ ●←┼  30  │ ● │─→ NULL
       └───┴──────┴───┘    └───┴──────┴───┘    └───┴──────┴───┘
         HEAD                                        TAIL

Each node: [Prev Pointer | Data | Next Pointer]
```

**Node Structure**:
```c
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};
```

### 3. Circular Linked List

**Singly Circular**:
```
┌──────┬───┐    ┌──────┬───┐    ┌──────┬───┐
│  10  │ ●─┼───→│  20  │ ●─┼───→│  30  │ ● │──┐
└──────┴───┘    └──────┴───┘    └──────┴───┘  │
   ↑                                          │
   └──────────────────────────────────────────┘
```

**Doubly Circular**:
```
    ┌──────────────────────────────────────────────────┐
    │  ┌───┬──────┬───┐    ┌───┬──────┬───┐           │
    └─→│ ●←┼  10  │ ●─┼───→│ ●←┼  20  │ ●─┼───────────┘
       └───┴──────┴───┘    └───┴──────┴───┘
```

---

## 3.3 Operations & Complexity

### Singly Linked List

| Operation | Time | Explanation |
|-----------|------|-------------|
| Access by index | O(n) | Must traverse from head |
| Search | O(n) | Linear traversal |
| Insert at head | O(1) | Update head pointer |
| Insert at tail | O(n) or O(1)* | Need to reach tail |
| Insert at position | O(n) | Traverse to position |
| Delete at head | O(1) | Update head pointer |
| Delete at tail | O(n) | Need previous node |
| Delete at position | O(n) | Traverse to position |

*O(1) if tail pointer is maintained

### Doubly Linked List

| Operation | Time | Advantage over SLL |
|-----------|------|-------------------|
| Access by index | O(n) | Same |
| Insert at head | O(1) | Same |
| Insert at tail | O(1) | No traversal needed |
| Delete at tail | O(1) | Direct prev access |
| Reverse traversal | O(n) | Possible! |

---

## 3.4 Implementation: Singly Linked List

### Node Creation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

### Insert at Beginning - O(1)

```python
def insert_at_head(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

**Visual**:
```
Before: HEAD → [20] → [30] → NULL

Insert 10:
Step 1: new_node.next = HEAD (points to 20)
Step 2: HEAD = new_node

After:  HEAD → [10] → [20] → [30] → NULL
```

### Insert at End - O(n)

```python
def insert_at_tail(self, data):
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
        return
    
    current = self.head
    while current.next:
        current = current.next
    
    current.next = new_node
```

### Insert at Position - O(n)

```python
def insert_at_position(self, data, position):
    if position == 0:
        self.insert_at_head(data)
        return
    
    new_node = Node(data)
    current = self.head
    
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of bounds")
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
```

### Delete at Beginning - O(1)

```python
def delete_at_head(self):
    if self.head is None:
        return None
    
    deleted_data = self.head.data
    self.head = self.head.next
    return deleted_data
```

### Delete at End - O(n)

```python
def delete_at_tail(self):
    if self.head is None:
        return None
    
    if self.head.next is None:
        deleted_data = self.head.data
        self.head = None
        return deleted_data
    
    current = self.head
    while current.next.next:
        current = current.next
    
    deleted_data = current.next.data
    current.next = None
    return deleted_data
```

### Search - O(n)

```python
def search(self, key):
    current = self.head
    position = 0
    
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    
    return -1
```

### Traversal - O(n)

```python
def display(self):
    elements = []
    current = self.head
    
    while current:
        elements.append(current.data)
        current = current.next
    
    return elements
```

---

## 3.5 Classic Linked List Problems

### Problem 1: Reverse a Linked List

**Iterative Approach** (Most Important for GATE)

```python
def reverse_iterative(self):
    prev = None
    current = self.head
    
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse link
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    self.head = prev

# Time: O(n), Space: O(1)
```

**Visual Walk-through**:
```
Initial:  NULL   10 → 20 → 30 → NULL
          prev   curr

Step 1:   NULL ← 10   20 → 30 → NULL
                prev  curr

Step 2:   NULL ← 10 ← 20   30 → NULL
                      prev curr

Step 3:   NULL ← 10 ← 20 ← 30   NULL
                           prev curr

Final:    NULL ← 10 ← 20 ← 30
                           HEAD
```

**Recursive Approach**:

```python
def reverse_recursive(self, node):
    if node is None or node.next is None:
        return node
    
    new_head = self.reverse_recursive(node.next)
    node.next.next = node
    node.next = None
    
    return new_head

# Time: O(n), Space: O(n) - recursion stack
```

### Problem 2: Detect Cycle (Floyd's Algorithm)

**The "AHA" Moment** 💡:
> If there's a cycle, a fast runner will eventually lap a slow runner!

```python
def has_cycle(self):
    if self.head is None:
        return False
    
    slow = fast = self.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Time: O(n), Space: O(1)
```

**Why Does This Work?**
- Fast pointer moves 2 steps, slow moves 1 step
- If cycle exists, fast enters cycle first
- Distance between them decreases by 1 each iteration
- They MUST meet within cycle length iterations

### Problem 3: Find Cycle Start Point

```python
def find_cycle_start(self):
    if self.head is None:
        return None
    
    slow = fast = self.head
    
    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find start
    slow = self.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# Time: O(n), Space: O(1)
```

**Mathematical Proof**:
```
Let:
- L = Distance from head to cycle start
- C = Cycle length
- K = Distance from cycle start to meeting point

When they meet:
- Slow traveled: L + K
- Fast traveled: L + K + nC (n complete cycles)

Since fast travels 2x slow:
2(L + K) = L + K + nC
L + K = nC
L = nC - K = (n-1)C + (C - K)

This means: distance from head to cycle start = distance from meeting point to cycle start!
```

### Problem 4: Find Middle Element

**One-Pass Solution**:

```python
def find_middle(self):
    slow = fast = self.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data if slow else None

# Time: O(n), Space: O(1)
```

### Problem 5: Find Nth Node from End

**Two Pointer Technique**:

```python
def nth_from_end(self, n):
    first = second = self.head
    
    # Move first n nodes ahead
    for _ in range(n):
        if first is None:
            return None  # n > list length
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    return second.data

# Time: O(n), Space: O(1)
```

### Problem 6: Merge Two Sorted Lists

```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    
    return dummy.next

# Time: O(n + m), Space: O(1)
```

### Problem 7: Check if Palindrome

```python
def is_palindrome(self):
    if self.head is None or self.head.next is None:
        return True
    
    # Find middle
    slow = fast = self.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = self.reverse_from(slow.next)
    
    # Compare both halves
    first_half = self.head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Time: O(n), Space: O(1)
```

---

## 3.6 Special Linked List Techniques

### XOR Linked List (Memory Efficient Doubly LL)

**Concept**: Store `prev XOR next` instead of two separate pointers

```
Normal DLL:  [prev | data | next] - 16 bytes for pointers
XOR LL:      [prev⊕next | data]   - 8 bytes for pointer
```

**Properties**:
- `A ⊕ A = 0`
- `A ⊕ 0 = A`
- If we know prev, we can get next: `next = (prev ⊕ next) ⊕ prev`

### Skip List

**Concept**: Multi-level linked list for O(log n) search

```
Level 3: HEAD ─────────────────────────────→ 50 ──→ NULL
Level 2: HEAD ────────→ 20 ───────────────→ 50 ──→ NULL
Level 1: HEAD ───→ 10 → 20 ───→ 30 ───────→ 50 ──→ NULL
Level 0: HEAD → 5 → 10 → 20 → 25 → 30 → 40 → 50 → 60 → NULL
```

**Complexity**: O(log n) average for search, insert, delete

---

## 3.7 Comparison: Types of Linked Lists

| Operation | Singly LL | Doubly LL | Circular LL |
|-----------|-----------|-----------|-------------|
| Memory per node | 1 pointer | 2 pointers | Same as base |
| Insert at head | O(1) | O(1) | O(1) |
| Insert at tail | O(n) or O(1)* | O(1) | O(1) |
| Delete at head | O(1) | O(1) | O(1) |
| Delete at tail | O(n) | O(1) | O(n) |
| Delete given node | O(n)** | O(1) | O(n)** |
| Reverse traversal | O(n²)*** | O(n) | Depends |

*With tail pointer
**Without previous pointer
***Requires multiple passes

---

## 3.8 GATE Exam Patterns & Traps

### Pattern 1: Pointer Manipulation

**Question Type**: What is the output after these operations?

```c
struct Node *p, *q;
p = head;
q = head->next;
p->next = q->next;
q->next = p;
head = q;
```

**Trap**: Track each pointer step-by-step!

### Pattern 2: Cycle Detection Variations

Common questions:
- Does cycle exist?
- Find cycle length
- Find cycle start point
- Remove the cycle

### Pattern 3: Complexity Analysis

**Trap Question**: "Insert at position k in linked list of size n"
- **Wrong Answer**: O(k)
- **Correct Answer**: O(k) but worst case O(n)

### Pattern 4: Edge Cases

| Case | Watch For |
|------|-----------|
| Empty list | head = NULL |
| Single node | head.next = NULL |
| Insert at head | Update head pointer |
| Delete only node | Set head = NULL |
| Cycle includes head | Floyd's still works |

---

## 3.9 Memory Considerations

### Space per Node

| Type | Pointers | Total (32-bit) | Total (64-bit) |
|------|----------|----------------|----------------|
| Singly LL | 1 | 4 bytes | 8 bytes |
| Doubly LL | 2 | 8 bytes | 16 bytes |
| XOR LL | 1 | 4 bytes | 8 bytes |

### Linked List vs Array Memory

For n integers (4 bytes each):

| Structure | 32-bit System | 64-bit System |
|-----------|---------------|---------------|
| Array | 4n bytes | 4n bytes |
| Singly LL | 8n bytes | 12n bytes |
| Doubly LL | 12n bytes | 20n bytes |

---

## 3.10 Advanced: Linked List in Other DS

### Stack using Linked List

```python
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):  # O(1)
        if self.top is None:
            raise Exception("Stack Underflow")
        data = self.top.data
        self.top = self.top.next
        return data
```

### Queue using Linked List

```python
class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, data):  # O(1)
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):  # O(1)
        if self.front is None:
            raise Exception("Queue Empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
```

---

## 📝 GATE Practice Problems

**Q1**: A singly linked list has n nodes. What is the time complexity of inserting a node after a given node?

**Q2**: In a circular linked list, what condition indicates that only one node exists?

**Q3**: Two linked lists of length m and n merge at some point. What is the time complexity to find the merge point using O(1) extra space?

**Q4**: What is the minimum number of pointers needed to reverse a singly linked list iteratively?

**Q5**: In Floyd's cycle detection, if cycle length is C, what is the maximum number of iterations before slow and fast meet?

---

## 🎯 Quick Reference: Problem Patterns

| Problem | Technique | Key Insight |
|---------|-----------|-------------|
| Detect cycle | Floyd's (slow/fast) | Fast laps slow in cycle |
| Find middle | Slow/fast pointers | Fast reaches end, slow at mid |
| Nth from end | Two pointers, n apart | When first reaches end, second at answer |
| Reverse | Three pointers | prev, current, next |
| Merge sorted | Dummy node + tail | Simplifies edge cases |
| Palindrome check | Mid + reverse + compare | O(1) space solution |
| Intersection point | Length difference | Align and walk together |

---

## 🔑 Key Takeaways

1. **Linked lists trade access time for insertion flexibility**
2. **Floyd's algorithm** - memorize it, it's asked every year
3. **Draw the pointers** - visual approach prevents errors
4. **Dummy nodes** simplify many algorithms
5. **Two-pointer technique** solves most LL problems efficiently
6. **Know when to use DLL vs SLL** - based on required operations

---

*Next: [Stacks →](04-Stacks.md)*
