# Chapter 6: Trees

## 🎯 The Atomic Truth
> **"Tree = Hierarchical Data + Parent-Child Relationships"**

---

## 6.1 The Mental Model

### The Analogy 💡
Think of a **family tree**:
- One **ancestor** at the top (root)
- Each person can have **children**
- Siblings share the same parent
- You can trace **lineage** from any person to the root

### Real-World Examples
- File system directories
- Organization hierarchies
- HTML DOM structure
- Decision trees
- Syntax trees in compilers

---

## 6.2 Tree Terminology

```
                    ┌───┐
           Level 0  │ A │ ← Root
                    └─┬─┘
            ┌─────────┼─────────┐
          ┌─┴─┐     ┌─┴─┐     ┌─┴─┐
 Level 1  │ B │     │ C │     │ D │ ← Internal Nodes
          └─┬─┘     └─┬─┘     └───┘
        ┌───┴───┐     │
      ┌─┴─┐   ┌─┴─┐ ┌─┴─┐
Level 2│ E │   │ F │ │ G │ ← Leaves
      └───┘   └───┘ └───┘
```

| Term | Definition |
|------|------------|
| **Root** | Topmost node (no parent) |
| **Parent** | Node with children below it |
| **Child** | Node directly below a parent |
| **Leaf** | Node with no children |
| **Internal Node** | Non-leaf node (has at least one child) |
| **Siblings** | Nodes with same parent |
| **Ancestor** | Any node on path from root to current node |
| **Descendant** | Any node reachable from current node going down |
| **Depth of node** | Length of path from root to node |
| **Height of node** | Length of longest path from node to leaf |
| **Height of tree** | Height of root = max depth |
| **Level** | Set of all nodes at same depth |
| **Degree of node** | Number of children |
| **Degree of tree** | Maximum degree of any node |

---

## 6.3 Binary Tree

### Definition
A **Binary Tree** is a tree where each node has **at most 2 children** (left and right).

### Node Structure

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

```c
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

### Types of Binary Trees

#### 1. Full Binary Tree
Every node has **0 or 2** children (no node has only 1 child).

```
       A
      / \
     B   C
    / \
   D   E

Nodes with 0 children: D, E, C (leaves)
Nodes with 2 children: A, B
```

**Properties**:
- If n = total nodes, leaves L = (n + 1) / 2
- Internal nodes I = (n - 1) / 2
- L = I + 1

#### 2. Complete Binary Tree
All levels filled except possibly last, which is filled left to right.

```
       A              A
      / \            / \
     B   C          B   C
    / \  /         / \
   D  E F         D   E

   Complete       Complete
```

**Properties**:
- Height h = ⌊log₂n⌋
- At level i (0-indexed): max 2ⁱ nodes
- Can be efficiently stored in array

#### 3. Perfect Binary Tree
All internal nodes have 2 children AND all leaves at same level.

```
       A
      / \
     B   C
    /\   /\
   D E  F  G
```

**Properties**:
- Nodes at level i = 2ⁱ
- Total nodes = 2^(h+1) - 1
- Leaves = 2^h
- Internal nodes = 2^h - 1

#### 4. Skewed Binary Tree
All nodes have only one child.

```
Left Skewed:    Right Skewed:
    A                A
   /                  \
  B                    B
 /                      \
C                        C
```

**Height** = n - 1 (worst case for BST)

#### 5. Balanced Binary Tree
Height of left and right subtrees differ by at most 1 for every node.

---

## 6.4 Binary Tree Formulas

### Critical Formulas for GATE

| Property | Formula |
|----------|---------|
| Max nodes at level i | 2ⁱ |
| Max nodes in tree of height h | 2^(h+1) - 1 |
| Min height for n nodes | ⌊log₂n⌋ |
| Max height for n nodes | n - 1 |
| Height of complete BT with n nodes | ⌊log₂n⌋ |
| Number of NULL pointers in BT with n nodes | n + 1 |
| Leaves in full BT with n nodes | (n + 1) / 2 |

### The "AHA" Derivation 💡

**Why n+1 NULL pointers?**

```
Each node has 2 pointer fields = 2n total pointers
Each node (except root) uses 1 pointer from parent = n-1 used
Unused (NULL) pointers = 2n - (n-1) = n + 1
```

---

## 6.5 Tree Traversals

### Visual Example

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

### 1. Inorder Traversal (Left, Root, Right)

**Result**: 4 → 2 → 5 → 1 → 3 → 6

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Iterative version
def inorder_iterative(root):
    stack = []
    current = root
    result = []
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result
```

**Use Case**: BST gives sorted order

### 2. Preorder Traversal (Root, Left, Right)

**Result**: 1 → 2 → 4 → 5 → 3 → 6

```python
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Iterative version
def preorder_iterative(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

**Use Case**: Copy tree, prefix expression

### 3. Postorder Traversal (Left, Right, Root)

**Result**: 4 → 5 → 2 → 6 → 3 → 1

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Iterative version (using two stacks)
def postorder_iterative(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    return stack2[::-1]
```

**Use Case**: Delete tree, postfix expression

### 4. Level Order Traversal (BFS)

**Result**: 1 → 2 → 3 → 4 → 5 → 6

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

### Traversal Summary

| Traversal | Order | Stack/Queue | Use Case |
|-----------|-------|-------------|----------|
| Inorder | L-Root-R | Stack | Sorted BST values |
| Preorder | Root-L-R | Stack | Copy tree, serialize |
| Postorder | L-R-Root | 2 Stacks | Delete tree, evaluate |
| Level Order | Level by level | Queue | BFS, shortest path |

---

## 6.6 Construct Tree from Traversals

### From Inorder + Preorder

```python
def build_tree(preorder, inorder):
    if not inorder:
        return None
    
    # First element of preorder is root
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    
    # Find root in inorder (divides left and right subtrees)
    mid = inorder.index(root_val)
    
    # Build left and right subtrees
    root.left = build_tree(preorder, inorder[:mid])
    root.right = build_tree(preorder, inorder[mid+1:])
    
    return root
```

**Visual Process**:
```
Preorder: [1, 2, 4, 5, 3, 6]
Inorder:  [4, 2, 5, 1, 3, 6]

Step 1: Root = 1 (first of preorder)
        Inorder split: [4,2,5] | 1 | [3,6]
        
Step 2: Left subtree - Root = 2
        Inorder split: [4] | 2 | [5]
        
Step 3: Continue recursively...
```

### From Inorder + Postorder

```python
def build_tree_post(inorder, postorder):
    if not inorder:
        return None
    
    # Last element of postorder is root
    root_val = postorder.pop()
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    
    # Build right subtree first (postorder processes right before left)
    root.right = build_tree_post(inorder[mid+1:], postorder)
    root.left = build_tree_post(inorder[:mid], postorder)
    
    return root
```

### ⚠️ Important Rules

1. **Inorder is essential** - without it, tree structure is ambiguous
2. **Preorder/Postorder alone** cannot determine unique tree
3. **Inorder + Level Order** - possible but complex

---

## 6.7 Binary Tree Problems

### Problem 1: Height of Binary Tree

```python
def height(root):
    if not root:
        return -1  # or return 0 if counting nodes
    
    return 1 + max(height(root.left), height(root.right))

# Time: O(n), Space: O(h) - recursion stack
```

### Problem 2: Count Nodes

```python
def count_nodes(root):
    if not root:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### Problem 3: Check if Balanced

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        
        left = check(node.left)
        if left == -1:
            return -1
        
        right = check(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    return check(root) != -1

# Time: O(n), Space: O(h)
```

### Problem 4: Diameter of Binary Tree

**Diameter** = longest path between any two nodes (may not pass through root)

```python
def diameter(root):
    result = [0]
    
    def height(node):
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)
        
        # Update diameter (path through current node)
        result[0] = max(result[0], left + right)
        
        return 1 + max(left, right)
    
    height(root)
    return result[0]

# Time: O(n), Space: O(h)
```

### Problem 5: Lowest Common Ancestor (LCA)

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

# Time: O(n), Space: O(h)
```

### Problem 6: Check if Symmetric

```python
def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    
    return is_mirror(root, root)
```

### Problem 7: Path Sum

```python
def has_path_sum(root, target):
    if not root:
        return False
    
    if not root.left and not root.right:  # Leaf
        return root.val == target
    
    remaining = target - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))
```

---

## 6.8 Special Tree Representations

### Array Representation (Complete Binary Tree)

```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Array: [_, 1, 2, 3, 4, 5, 6, 7]
Index:  0  1  2  3  4  5  6  7

For node at index i:
- Parent: i / 2
- Left child: 2i
- Right child: 2i + 1
```

**Note**: Index 0 is often unused for simpler formulas.

### Threaded Binary Tree

**Problem**: In a binary tree with n nodes, there are n+1 NULL pointers. Can we use them?

**Solution**: Replace NULL pointers with **threads** to inorder predecessor/successor.

**Types**:
1. **Single Threaded**: Only right NULL points to inorder successor
2. **Double Threaded**: Left NULL → predecessor, Right NULL → successor

```
Standard:           Threaded (right):
    1                    1
   / \                  / \
  2   3               2 ─→ 3
 / \                 / \     \
4   5               4 → 5 ────┘
```

**Advantage**: Inorder traversal without stack or recursion

---

## 6.9 Expression Trees

### Concept
Represent mathematical expressions as binary trees.

```
Expression: (a + b) * (c - d)

        *
       / \
      +   -
     / \ / \
    a  b c  d

Inorder:   a + b * c - d (gives infix)
Preorder:  * + a b - c d (gives prefix)
Postorder: a b + c d - * (gives postfix)
```

### Build Expression Tree from Postfix

```python
def build_expression_tree(postfix):
    stack = []
    
    for token in postfix:
        node = TreeNode(token)
        
        if token in '+-*/':
            node.right = stack.pop()
            node.left = stack.pop()
        
        stack.append(node)
    
    return stack[0]
```

### Evaluate Expression Tree

```python
def evaluate(root):
    if not root.left and not root.right:  # Operand
        return int(root.val)
    
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)
    
    if root.val == '+':
        return left_val + right_val
    elif root.val == '-':
        return left_val - right_val
    elif root.val == '*':
        return left_val * right_val
    elif root.val == '/':
        return left_val / right_val
```

---

## 6.10 GATE Exam Patterns

### Pattern 1: Counting Problems

**Q**: How many structurally different binary trees with n nodes?

**Answer**: Catalan Number Cₙ = (2n)! / ((n+1)! × n!)

| n | Trees |
|---|-------|
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 14 |
| 5 | 42 |

### Pattern 2: Traversal Output

**Q**: Given two traversals, find the third or construct tree.

**Trick**: 
- Preorder first = Root
- Postorder last = Root
- Inorder divides left/right subtrees

### Pattern 3: Height/Depth Questions

**Q**: Minimum height binary tree with 15 nodes?

**Answer**: ⌊log₂15⌋ = 3

### Pattern 4: Node Count at Level

**Q**: In a complete binary tree with 100 nodes, how many nodes at last level?

```
Total nodes = 100
Height = ⌊log₂100⌋ = 6
Nodes in complete tree of height 6 = 2^7 - 1 = 127 (max)
Nodes in complete tree of height 5 = 2^6 - 1 = 63 (min for h=6)
Nodes at last level = 100 - 63 = 37
```

---

## 📝 GATE Practice Problems

**Q1**: A binary tree has 10 nodes with 2 children each. How many leaf nodes?

**Q2**: Inorder: D B E A F C, Preorder: A B D E C F. Draw the tree and give postorder.

**Q3**: A complete binary tree has depth 4. What is the minimum and maximum number of nodes?

**Q4**: How many distinct binary trees can be formed with 4 unlabeled nodes?

**Q5**: What is the maximum number of nodes at level 5 of a binary tree?

---

## 🎯 Quick Reference

### Traversal Identification

| Given Output | Look For |
|--------------|----------|
| Inorder | Sorted for BST |
| Preorder | Root at beginning |
| Postorder | Root at end |
| Level Order | BFS pattern |

### Tree Type Identification

| Property | Tree Type |
|----------|-----------|
| Every node: 0 or 2 children | Full |
| All levels full, last level left-filled | Complete |
| All levels completely filled | Perfect |
| Only one child per node | Skewed |

---

## 🔑 Key Takeaways

1. **Inorder + Preorder/Postorder** uniquely determines a binary tree
2. **Complete binary trees** can be efficiently stored in arrays
3. **n+1 NULL pointers** in any binary tree of n nodes
4. **Catalan numbers** count structurally different trees
5. **Threaded trees** utilize NULL pointers for efficient traversal
6. **Height vs Depth**: Height is from bottom up, depth is from top down

---

*Next: [Binary Search Trees →](07-Binary-Search-Trees.md)*
