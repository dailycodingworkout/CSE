# Chapter 5: Queues

## 🎯 The Atomic Truth
> **"Queue = FIFO = First In, First Out"**

---

## 5.1 The Mental Model

### The Analogy 💡
Think of a **line at a ticket counter**:
- First person in line gets served first
- New people join at the **rear** (enqueue)
- Service happens at the **front** (dequeue)
- No cutting in line (no random access)

### Real-World Examples
- Print queue (documents printed in order submitted)
- CPU task scheduling
- BFS traversal in graphs
- Call center waiting line
- Message queues in distributed systems

---

## 5.2 Queue ADT

### Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| enqueue(x) | Add element x at rear | O(1) |
| dequeue() | Remove and return front element | O(1) |
| front()/peek() | Return front element without removing | O(1) |
| isEmpty() | Check if queue is empty | O(1) |
| size() | Return number of elements | O(1) |
| isFull() | Check if queue is full (array) | O(1) |

### Queue Conditions

**Underflow**: Trying to dequeue from empty queue
**Overflow**: Trying to enqueue to full queue (array implementation)

---

## 5.3 Implementation

### Simple Array Queue (Inefficient)

```python
class SimpleQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue Overflow")
        self.rear += 1
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        item = self.queue[self.front]
        self.front += 1
        self.size -= 1
        return item
```

**Problem**: After several operations, front moves right, wasting space!

```
Initial:  [A][B][C][_][_]  front=0, rear=2
After 2 dequeues: [_][_][C][_][_]  front=2, rear=2
Enqueue D, E: [_][_][C][D][E]  front=2, rear=4
Enqueue F: OVERFLOW! But indices 0,1 are empty!
```

### Circular Queue (Efficient)

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue Overflow")
        self.rear = (self.rear + 1) % self.capacity  # Circular wrap
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity  # Circular wrap
        self.size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue Empty")
        return self.queue[self.front]
```

**Visual: Circular Queue**

```
Logical View:           Physical View:
    ┌─────┐
    │  A  │ ←rear      Index: [0][1][2][3][4]
  ┌─┴─────┴─┐          Value: [D][E][_][A][B]
  │         │                     ↑     ↑
  │    ○    │                   rear  front
  │         │
  └─┬─────┬─┘          front=3, rear=1
    │  B  │ ←front     size=4
    └─────┘
```

### Linked List Queue

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue Empty")
        return self.front.data
    
    def size(self):
        return self._size
```

---

## 5.4 Circular Queue Formulas

### Key Formulas

| Operation | Formula |
|-----------|---------|
| Next rear | (rear + 1) % capacity |
| Next front | (front + 1) % capacity |
| Is Empty | size == 0 OR front == -1 |
| Is Full | size == capacity OR (rear + 1) % capacity == front |
| Size (if not tracked) | (rear - front + capacity + 1) % capacity |

### GATE Trap: Empty vs Full Detection

**Problem**: If we only use front and rear pointers, how to distinguish empty from full?

**Solution 1**: Track size separately (shown above)

**Solution 2**: Waste one slot
```
Empty: front == rear (pointing to empty slot)
Full: (rear + 1) % capacity == front

This wastes 1 slot but avoids size variable
Actual capacity = array_size - 1
```

**Solution 3**: Use a boolean flag
```python
self.is_queue_full = False
# Set True when rear catches front after enqueue
# Set False when front moves after dequeue
```

---

## 5.5 Types of Queues

### 1. Simple Queue
- Basic FIFO
- Enqueue at rear, dequeue at front
- Already covered above

### 2. Circular Queue
- Array indices wrap around
- Efficient space utilization
- Covered above

### 3. Double-Ended Queue (Deque)

**Operations**:
- insertFront(x): Insert at front
- insertRear(x): Insert at rear
- deleteFront(): Remove from front
- deleteRear(): Remove from rear

```python
class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = -1
        self.rear = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def insert_front(self, item):
        if self.is_full():
            raise Exception("Deque Full")
        if self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = item
        self.size += 1
    
    def insert_rear(self, item):
        if self.is_full():
            raise Exception("Deque Full")
        if self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = item
        self.size += 1
    
    def delete_front(self):
        if self.is_empty():
            raise Exception("Deque Empty")
        item = self.arr[self.front]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def delete_rear(self):
        if self.is_empty():
            raise Exception("Deque Empty")
        item = self.arr[self.rear]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return item
```

**Use Cases**:
- Sliding window maximum/minimum
- Palindrome checking
- Work-stealing algorithms

### 4. Priority Queue

**Concept**: Elements dequeued based on priority, not arrival order

| Operation | Using Array | Using Heap |
|-----------|-------------|------------|
| Insert | O(1) or O(n) | O(log n) |
| Extract-Max/Min | O(n) or O(1) | O(log n) |
| Peek | O(n) or O(1) | O(1) |

*Detailed coverage in Heaps chapter*

### 5. Input-Restricted Deque
- Insert only at rear
- Delete from both ends

### 6. Output-Restricted Deque
- Insert at both ends
- Delete only from front

---

## 5.6 Queue Applications

### Application 1: BFS (Breadth-First Search)

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Time: O(V + E), Space: O(V)
```

### Application 2: Level Order Traversal (Trees)

```python
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Time: O(n), Space: O(w) where w = max width
```

### Application 3: Sliding Window Maximum

```python
from collections import deque

def sliding_window_max(arr, k):
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(arr)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they'll never be max)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Window has k elements
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

# Time: O(n), Space: O(k)
```

**Example**:
```
arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Window [1,3,-1] → max = 3
Window [3,-1,-3] → max = 3
Window [-1,-3,5] → max = 5
Window [-3,5,3] → max = 5
Window [5,3,6] → max = 6
Window [3,6,7] → max = 7

Output: [3, 3, 5, 5, 6, 7]
```

### Application 4: First Non-Repeating Character in Stream

```python
from collections import deque

def first_non_repeating(stream):
    count = {}
    queue = deque()
    result = []
    
    for char in stream:
        count[char] = count.get(char, 0) + 1
        queue.append(char)
        
        # Remove repeating characters from front
        while queue and count[queue[0]] > 1:
            queue.popleft()
        
        if queue:
            result.append(queue[0])
        else:
            result.append('#')  # No non-repeating char
    
    return result

# Time: O(n), Space: O(k) where k = distinct chars
```

### Application 5: Generate Binary Numbers 1 to N

```python
from collections import deque

def generate_binary(n):
    result = []
    queue = deque(['1'])
    
    for _ in range(n):
        front = queue.popleft()
        result.append(front)
        queue.append(front + '0')
        queue.append(front + '1')
    
    return result

# Time: O(n), Space: O(n)
```

**Example**:
```
n = 5
Queue progression:
['1'] → pop '1' → ['10', '11']
['10', '11'] → pop '10' → ['11', '100', '101']
...
Output: ['1', '10', '11', '100', '101']
```

### Application 6: Interleave Queue Halves

```python
from collections import deque

def interleave_queue(queue):
    n = len(queue)
    if n % 2 != 0:
        return queue  # Only works for even size
    
    half = n // 2
    stack = []
    
    # Push first half to stack
    for _ in range(half):
        stack.append(queue.popleft())
    
    # Interleave stack and queue
    while stack:
        queue.append(stack.pop())
        queue.append(queue.popleft())
    
    # Restore order
    for _ in range(half):
        queue.append(queue.popleft())
    
    return queue
```

---

## 5.7 Implementing Queue Using Stacks

### Method 1: Costly Enqueue

```python
class QueueUsingStacks1:
    def __init__(self):
        self.s1 = []  # Main stack
        self.s2 = []  # Helper stack
    
    def enqueue(self, x):  # O(n)
        # Move all from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        
        # Push new element to s1
        self.s1.append(x)
        
        # Move all back to s1
        while self.s2:
            self.s1.append(self.s2.pop())
    
    def dequeue(self):  # O(1)
        if not self.s1:
            raise Exception("Queue Empty")
        return self.s1.pop()
```

### Method 2: Costly Dequeue

```python
class QueueUsingStacks2:
    def __init__(self):
        self.s1 = []  # Enqueue stack
        self.s2 = []  # Dequeue stack
    
    def enqueue(self, x):  # O(1)
        self.s1.append(x)
    
    def dequeue(self):  # Amortized O(1)
        if not self.s2:
            if not self.s1:
                raise Exception("Queue Empty")
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
```

**Why Amortized O(1)?**
- Each element is pushed and popped from each stack exactly once
- Total operations for n elements = 4n (push s1, pop s1, push s2, pop s2)
- Average per element = O(1)

---

## 5.8 Implementing Stack Using Queues

### Method 1: Costly Push

```python
from collections import deque

class StackUsingQueues1:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):  # O(n)
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):  # O(1)
        if not self.q1:
            raise Exception("Stack Empty")
        return self.q1.popleft()
```

### Method 2: Costly Pop

```python
from collections import deque

class StackUsingQueues2:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):  # O(1)
        self.q1.append(x)
    
    def pop(self):  # O(n)
        if not self.q1:
            raise Exception("Stack Empty")
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result
```

### Method 3: Single Queue

```python
from collections import deque

class StackUsingSingleQueue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):  # O(n)
        self.q.append(x)
        # Rotate n-1 times
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):  # O(1)
        if not self.q:
            raise Exception("Stack Empty")
        return self.q.popleft()
```

---

## 5.9 GATE Exam Patterns

### Pattern 1: Circular Queue State

**Question Type**: After sequence of operations, what are front, rear, size?

```
Capacity = 5, initial front=0, rear=4
Operations: enqueue(A), enqueue(B), dequeue(), enqueue(C)

Trace:
Initial: [_][_][_][_][_], f=0, r=4, size=0
enqueue(A): [A][_][_][_][_], f=0, r=0, size=1
enqueue(B): [A][B][_][_][_], f=0, r=1, size=2
dequeue(): [_][B][_][_][_], f=1, r=1, size=1
enqueue(C): [_][B][C][_][_], f=1, r=2, size=2
```

### Pattern 2: Queue Permutations

**Question**: Which sequences are possible with a queue?

**Answer**: Only the SAME order as input!
- Push 1,2,3 → Only possible output is 1,2,3
- Queue is FIFO, no flexibility

Compare to stack:
- Push 1,2,3 → Multiple outputs possible (1,2,3), (2,1,3), etc.

### Pattern 3: Double-Ended Queue Operations

**Question**: Deque can implement which data structures?
- Stack (use only one end)
- Queue (use opposite ends)
- Both simultaneously!

### Pattern 4: Time Complexity Questions

| Implementation | Enqueue | Dequeue |
|---------------|---------|---------|
| Array Queue | O(1) | O(1) |
| Circular Array | O(1) | O(1) |
| Linked List | O(1) | O(1) |
| Queue via 2 Stacks | O(1) or O(n) | O(n) or O(1) |

---

## 5.10 Comparison: Stack vs Queue

| Aspect | Stack | Queue |
|--------|-------|-------|
| Order | LIFO | FIFO |
| Operations | push/pop at same end | enqueue/dequeue at different ends |
| Pointer(s) | One (top) | Two (front, rear) |
| Use case | Undo, DFS | Scheduling, BFS |
| Recursion | Natural | Not natural |

---

## 📝 GATE Practice Problems

**Q1**: A circular queue has capacity 5. After enqueue(A, B, C, D, E), dequeue(), dequeue(), enqueue(F, G), what is the state?

**Q2**: Minimum number of queues required to implement a stack?

**Q3**: What is the maximum number of elements in a circular queue of size n using one empty slot to distinguish empty from full?

**Q4**: A priority queue is implemented using a sorted array. What is the complexity of:
- (a) Insert
- (b) Delete-max

**Q5**: Implement a queue that supports enqueue, dequeue, and getMin in O(1) time.

---

## 🎯 Quick Reference

### Queue Implementations Comparison

| Type | Enqueue | Dequeue | Space | Notes |
|------|---------|---------|-------|-------|
| Simple Array | O(1) | O(1) | O(n) | Wastes space |
| Circular Array | O(1) | O(1) | O(n) | Efficient |
| Linked List | O(1) | O(1) | O(n) | Dynamic |
| Two Stacks | O(1)/O(n) | O(n)/O(1) | O(n) | Amortized O(1) |

### Queue vs Deque

| Operation | Queue | Deque |
|-----------|-------|-------|
| Insert front | ✗ | ✓ |
| Insert rear | ✓ | ✓ |
| Delete front | ✓ | ✓ |
| Delete rear | ✗ | ✓ |

---

## 🔑 Key Takeaways

1. **Queue = FIFO** - fundamental principle
2. **Circular queue** solves the space wastage problem
3. **Queue using stacks** achieves amortized O(1) dequeue
4. **BFS and level-order** are classic queue applications
5. **Deque** is the most versatile - can implement both stack and queue
6. **Sliding window maximum** uses deque brilliantly

---

*Next: [Trees →](06-Trees.md)*
