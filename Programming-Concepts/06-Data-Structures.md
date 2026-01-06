# Chapter 6: Data Structures
## The Organizational Arsenal | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"Data structures organize data; the right choice transforms O(n) to O(1)."**

---

## 6.1 Introduction to Data Structures

### Classification

```
Data Structures
├── Linear
│   ├── Static
│   │   └── Array
│   └── Dynamic
│       ├── Linked List
│       ├── Stack
│       └── Queue
└── Non-Linear
    ├── Tree
    ├── Graph
    └── Heap
```

### Abstract Data Type (ADT) Concept

An **ADT** specifies:
1. Data stored
2. Operations on data
3. Error conditions

**Example:** Stack ADT
- Data: Collection of elements
- Operations: push, pop, peek, isEmpty
- Errors: Pop from empty stack

---

## 6.2 Linked Lists

### Types of Linked Lists

```
1. Singly Linked List:
   [Data|Next] → [Data|Next] → [Data|Next] → NULL

2. Doubly Linked List:
   NULL ← [Prev|Data|Next] ⟷ [Prev|Data|Next] ⟷ [Prev|Data|Next] → NULL

3. Circular Singly:
   [Data|Next] → [Data|Next] → [Data|Next] ──┐
        ↑__________________________________|

4. Circular Doubly:
   ⟷ [Prev|Data|Next] ⟷ [Prev|Data|Next] ⟷ (connects back)
```

### Singly Linked List Implementation

```c
struct Node {
    int data;
    struct Node *next;
};

// Create node
struct Node* createNode(int data) {
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert at beginning - O(1)
void insertAtHead(struct Node **head, int data) {
    struct Node *newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Insert at end - O(n)
void insertAtTail(struct Node **head, int data) {
    struct Node *newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node *temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

// Delete node - O(n)
void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head, *prev = NULL;
    
    // Head node
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    
    // Find node
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) return;  // Not found
    
    prev->next = temp->next;
    free(temp);
}

// Search - O(n)
struct Node* search(struct Node *head, int key) {
    while (head != NULL) {
        if (head->data == key) return head;
        head = head->next;
    }
    return NULL;
}

// Reverse - O(n)
void reverse(struct Node **head) {
    struct Node *prev = NULL, *curr = *head, *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
}
```

### 🎯 GATE Classic: Find Middle Element

```c
// Using slow-fast pointers - O(n)
struct Node* findMiddle(struct Node *head) {
    struct Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

### Detect Cycle (Floyd's Algorithm)

```c
int hasCycle(struct Node *head) {
    struct Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return 1;  // Cycle exists
    }
    return 0;
}
```

### 📊 Linked List Complexity

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1) if tail ptr |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(1) if tail ptr |
| Delete given node | O(n) | O(1) if node given |

---

## 6.3 Stacks

### Stack ADT
- **LIFO:** Last In, First Out
- Operations: push, pop, peek, isEmpty

### Array Implementation

```c
#define MAX 100

struct Stack {
    int arr[MAX];
    int top;
};

void init(struct Stack *s) { s->top = -1; }

int isEmpty(struct Stack *s) { return s->top == -1; }

int isFull(struct Stack *s) { return s->top == MAX - 1; }

void push(struct Stack *s, int x) {
    if (isFull(s)) { printf("Overflow"); return; }
    s->arr[++s->top] = x;
}

int pop(struct Stack *s) {
    if (isEmpty(s)) { printf("Underflow"); return -1; }
    return s->arr[s->top--];
}

int peek(struct Stack *s) {
    if (isEmpty(s)) return -1;
    return s->arr[s->top];
}
```

### Linked List Implementation

```c
struct Node {
    int data;
    struct Node *next;
};

void push(struct Node **top, int data) {
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *top;
    *top = newNode;
}

int pop(struct Node **top) {
    if (*top == NULL) { printf("Underflow"); return -1; }
    struct Node *temp = *top;
    int data = temp->data;
    *top = (*top)->next;
    free(temp);
    return data;
}
```

### 🔥 Applications of Stack

1. **Function call management** (Call Stack)
2. **Expression evaluation** (Infix, Postfix, Prefix)
3. **Parenthesis matching**
4. **Undo operations**
5. **Browser back button**
6. **DFS traversal**

### Infix to Postfix Conversion

```c
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

void infixToPostfix(char *infix, char *postfix) {
    struct Stack s; init(&s);
    int j = 0;
    
    for (int i = 0; infix[i]; i++) {
        char c = infix[i];
        
        if (isalnum(c)) {
            postfix[j++] = c;
        } else if (c == '(') {
            push(&s, c);
        } else if (c == ')') {
            while (!isEmpty(&s) && peek(&s) != '(')
                postfix[j++] = pop(&s);
            pop(&s);  // Remove '('
        } else {
            while (!isEmpty(&s) && precedence(peek(&s)) >= precedence(c))
                postfix[j++] = pop(&s);
            push(&s, c);
        }
    }
    while (!isEmpty(&s))
        postfix[j++] = pop(&s);
    postfix[j] = '\0';
}
```

### Postfix Evaluation

```c
int evaluatePostfix(char *exp) {
    struct Stack s; init(&s);
    
    for (int i = 0; exp[i]; i++) {
        if (isdigit(exp[i])) {
            push(&s, exp[i] - '0');
        } else {
            int b = pop(&s);
            int a = pop(&s);
            switch (exp[i]) {
                case '+': push(&s, a + b); break;
                case '-': push(&s, a - b); break;
                case '*': push(&s, a * b); break;
                case '/': push(&s, a / b); break;
            }
        }
    }
    return pop(&s);
}
```

---

## 6.4 Queues

### Queue ADT
- **FIFO:** First In, First Out
- Operations: enqueue, dequeue, front, isEmpty

### Linear Queue (Array)

```c
#define MAX 100

struct Queue {
    int arr[MAX];
    int front, rear;
};

void init(struct Queue *q) { q->front = q->rear = -1; }

int isEmpty(struct Queue *q) { return q->front == -1; }

int isFull(struct Queue *q) { return q->rear == MAX - 1; }

void enqueue(struct Queue *q, int x) {
    if (isFull(q)) { printf("Overflow"); return; }
    if (isEmpty(q)) q->front = 0;
    q->arr[++q->rear] = x;
}

int dequeue(struct Queue *q) {
    if (isEmpty(q)) { printf("Underflow"); return -1; }
    int data = q->arr[q->front];
    if (q->front == q->rear)
        q->front = q->rear = -1;
    else
        q->front++;
    return data;
}
```

### Circular Queue

```c
void enqueue(struct Queue *q, int x) {
    if ((q->rear + 1) % MAX == q->front) { printf("Full"); return; }
    if (q->front == -1) q->front = 0;
    q->rear = (q->rear + 1) % MAX;
    q->arr[q->rear] = x;
}

int dequeue(struct Queue *q) {
    if (q->front == -1) { printf("Empty"); return -1; }
    int data = q->arr[q->front];
    if (q->front == q->rear)
        q->front = q->rear = -1;
    else
        q->front = (q->front + 1) % MAX;
    return data;
}
```

### 🔥 Applications of Queue

1. **BFS traversal**
2. **CPU scheduling**
3. **Print queue**
4. **Buffering** (I/O buffers)
5. **Producer-Consumer problem**

### Priority Queue (Conceptual)

Elements dequeued based on priority, not arrival order.
Implementation: Heap (most efficient), Array, Linked List

### Deque (Double-Ended Queue)

Insert and delete from both ends.

```
Operations:
- insertFront(), insertRear()
- deleteFront(), deleteRear()
- getFront(), getRear()
```

---

## 6.5 Trees

### Tree Terminology

| Term | Definition |
|------|------------|
| Node | Element in tree |
| Root | Topmost node |
| Parent | Node above |
| Child | Node below |
| Leaf | Node with no children |
| Depth | Distance from root |
| Height | Longest path to leaf |
| Degree | Number of children |

### Binary Tree

Each node has at most 2 children.

```c
struct Node {
    int data;
    struct Node *left, *right;
};

struct Node* createNode(int data) {
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}
```

### Tree Traversals

```c
// Inorder (Left-Root-Right) - For BST: gives sorted order
void inorder(struct Node *root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Preorder (Root-Left-Right) - For copying tree
void preorder(struct Node *root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Postorder (Left-Right-Root) - For deleting tree
void postorder(struct Node *root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

// Level Order (BFS)
void levelOrder(struct Node *root) {
    Queue q; enqueue(&q, root);
    while (!isEmpty(&q)) {
        struct Node *node = dequeue(&q);
        printf("%d ", node->data);
        if (node->left) enqueue(&q, node->left);
        if (node->right) enqueue(&q, node->right);
    }
}
```

### 🎯 GATE Classic: Tree Properties

For a binary tree with n nodes:
- Minimum height: $\lfloor \log_2 n \rfloor$
- Maximum height: $n - 1$ (skewed)
- Nodes at level $i$: at most $2^i$
- Leaves in complete binary tree: $\lceil n/2 \rceil$

**Relation:** If $n_0$ = leaves, $n_2$ = nodes with 2 children: $n_0 = n_2 + 1$

### Binary Search Tree (BST)

Left subtree < Root < Right subtree

```c
// Insert - O(h)
struct Node* insert(struct Node *root, int key) {
    if (root == NULL) return createNode(key);
    if (key < root->data)
        root->left = insert(root->left, key);
    else
        root->right = insert(root->right, key);
    return root;
}

// Search - O(h)
struct Node* search(struct Node *root, int key) {
    if (root == NULL || root->data == key) return root;
    if (key < root->data)
        return search(root->left, key);
    return search(root->right, key);
}

// Find Min
struct Node* findMin(struct Node *root) {
    while (root->left != NULL) root = root->left;
    return root;
}

// Delete - O(h)
struct Node* delete(struct Node *root, int key) {
    if (root == NULL) return NULL;
    
    if (key < root->data)
        root->left = delete(root->left, key);
    else if (key > root->data)
        root->right = delete(root->right, key);
    else {
        // Node found
        if (root->left == NULL) {
            struct Node *temp = root->right;
            free(root);
            return temp;
        }
        if (root->right == NULL) {
            struct Node *temp = root->left;
            free(root);
            return temp;
        }
        // Two children: get inorder successor
        struct Node *temp = findMin(root->right);
        root->data = temp->data;
        root->right = delete(root->right, temp->data);
    }
    return root;
}
```

### AVL Tree (Self-Balancing BST)

**Balance Factor:** height(left) - height(right) ∈ {-1, 0, 1}

**Rotations:**
- Left Rotation (RR imbalance)
- Right Rotation (LL imbalance)
- Left-Right Rotation (LR imbalance)
- Right-Left Rotation (RL imbalance)

---

## 6.6 Heaps

### Heap Properties

**Max-Heap:** Parent ≥ Children
**Min-Heap:** Parent ≤ Children

### Array Representation

For node at index $i$:
- Left child: $2i + 1$
- Right child: $2i + 2$
- Parent: $\lfloor (i-1)/2 \rfloor$

### Heap Operations

```c
// Heapify (Max-Heap) - O(log n)
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;
    
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Build Heap - O(n)
void buildHeap(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}

// Insert - O(log n)
void insert(int arr[], int *n, int key) {
    arr[(*n)++] = key;
    int i = *n - 1;
    while (i > 0 && arr[(i-1)/2] < arr[i]) {
        swap(&arr[i], &arr[(i-1)/2]);
        i = (i-1)/2;
    }
}

// Extract Max - O(log n)
int extractMax(int arr[], int *n) {
    int max = arr[0];
    arr[0] = arr[--(*n)];
    heapify(arr, *n, 0);
    return max;
}
```

### 🔥 Heap Applications

1. **Priority Queue**
2. **Heap Sort**
3. **Kth largest element**
4. **Merge K sorted lists**
5. **Dijkstra's Algorithm**

---

## 6.7 Graphs

### Graph Representation

**Adjacency Matrix:**
```
    0 1 2 3
  ┌─────────
0 │ 0 1 1 0
1 │ 1 0 0 1
2 │ 1 0 0 1
3 │ 0 1 1 0
```
Space: O(V²), Good for dense graphs

**Adjacency List:**
```
0 → [1, 2]
1 → [0, 3]
2 → [0, 3]
3 → [1, 2]
```
Space: O(V + E), Good for sparse graphs

### Graph Implementation

```c
// Adjacency List
struct Node {
    int vertex;
    struct Node *next;
};

struct Graph {
    int numVertices;
    struct Node **adjLists;
    int *visited;
};

void addEdge(struct Graph *g, int src, int dest) {
    struct Node *newNode = createNode(dest);
    newNode->next = g->adjLists[src];
    g->adjLists[src] = newNode;
    
    // For undirected graph
    newNode = createNode(src);
    newNode->next = g->adjLists[dest];
    g->adjLists[dest] = newNode;
}
```

### Graph Traversals

```c
// DFS - O(V + E)
void DFS(struct Graph *g, int v) {
    g->visited[v] = 1;
    printf("%d ", v);
    
    struct Node *temp = g->adjLists[v];
    while (temp) {
        if (!g->visited[temp->vertex])
            DFS(g, temp->vertex);
        temp = temp->next;
    }
}

// BFS - O(V + E)
void BFS(struct Graph *g, int start) {
    Queue q; enqueue(&q, start);
    g->visited[start] = 1;
    
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);
        
        struct Node *temp = g->adjLists[v];
        while (temp) {
            if (!g->visited[temp->vertex]) {
                g->visited[temp->vertex] = 1;
                enqueue(&q, temp->vertex);
            }
            temp = temp->next;
        }
    }
}
```

### 📊 Graph Properties

| Property | Formula/Check |
|----------|---------------|
| Complete graph edges | V(V-1)/2 (undirected) |
| Tree edges | V - 1 |
| Connected (undirected) | DFS/BFS visits all |
| Strongly connected (directed) | All pairs reachable |
| Cycle detection | DFS with back edge |
| Bipartite | BFS 2-coloring |

---

## 6.8 Hashing

### Hash Table

Maps keys to values using a hash function.

### Hash Functions

```c
// Division Method
int hash(int key, int size) {
    return key % size;
}

// Multiplication Method
int hash(int key, int size) {
    double A = 0.6180339887;  // (√5 - 1) / 2
    return (int)(size * fmod(key * A, 1.0));
}
```

### Collision Resolution

**1. Chaining (Separate Chaining):**
```
Index 0: [key1] → [key5] → NULL
Index 1: [key2] → NULL
Index 2: [key3] → [key7] → NULL
```

**2. Open Addressing:**
- Linear Probing: $h(k, i) = (h(k) + i) \mod m$
- Quadratic Probing: $h(k, i) = (h(k) + c_1 i + c_2 i^2) \mod m$
- Double Hashing: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \mod m$

### Load Factor
$$\alpha = \frac{n}{m}$$

Where $n$ = number of elements, $m$ = table size

### 📊 Hash Table Complexity

| Operation | Average | Worst (bad hash) |
|-----------|---------|------------------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

---

## 🎯 Practice Problems

### Problem 1: Stack
**Q:** Stack S is {5, 10, 15, 20} (top = 20). After pop(), pop(), push(25), what's top?
**Answer:** 25

### Problem 2: Queue
**Q:** Circular queue with size 5, front=2, rear=4. Elements count?
**Answer:** 3 elements

### Problem 3: BST
**Q:** Minimum comparisons to search in BST with 1024 nodes?
**Answer:** $\log_2 1024 + 1 = 11$ (worst case for balanced BST)

### Problem 4: Heap
**Q:** Build max-heap from [1, 2, 3, 4, 5]. Result?
**Answer:** [5, 4, 3, 1, 2]

### Problem 5: Graph
**Q:** DFS starting from vertex 0 for adjacency list: 0→[1,2], 1→[0,3], 2→[0,3], 3→[1,2]
**Answer:** 0 1 3 2 (or 0 2 3 1 depending on order)

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Stacks are plates at a buffet (LIFO). Queues are lines at a cinema (FIFO). Trees are family trees (hierarchical). Graphs are social networks (everyone connected)."**

### The Mental Slider
- **Stack:** Elevator going up (last in exits first)
- **Queue:** Tunnel (first in exits first)
- **Tree:** Inverted chandelier (root at top)
- **Heap:** Pyramid (parent always superior)

### The 5-Second Snap-Check
1. **Stack or Queue?** LIFO vs FIFO
2. **Array or Linked List?** Fixed vs dynamic size
3. **BST property?** Left < Root < Right
4. **Heap property?** Parent ≥ or ≤ children
5. **Graph sparse or dense?** List vs Matrix

---

## 📈 Complexity Summary

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Hash Table | - | O(1) | O(1) | O(1) |
| Heap | - | O(n) | O(log n) | O(log n) |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Pointers & Memory](05-Pointers-Memory.md) | [Next: Algorithms →](07-Algorithms.md)
