# Chapter 7: Binary Search Trees (BST)

## 🎯 The Atomic Truth
> **"BST = Ordered Binary Tree: Left < Root < Right"**

---

## 7.1 The Mental Model

### The Analogy 💡
Think of a **dictionary**:
- Each page (node) has a word
- Words on left pages come alphabetically before
- Words on right pages come alphabetically after
- Finding a word = follow the ordering

### The BST Property
For every node:
- All nodes in **left subtree** have values **less than** the node
- All nodes in **right subtree** have values **greater than** the node

```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Valid BST: Left subtree of 50 = {20,30,40} - all < 50
           Right subtree of 50 = {60,70,80} - all > 50
```

---

## 7.2 BST Operations

### Search - O(h)

```python
def search(root, key):
    if not root or root.val == key:
        return root
    
    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Iterative version
def search_iterative(root, key):
    while root:
        if key == root.val:
            return root
        elif key < root.val:
            root = root.left
        else:
            root = root.right
    return None
```

### Insert - O(h)

```python
def insert(root, key):
    if not root:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    # If key == root.val, ignore (no duplicates)
    
    return root

# Iterative version
def insert_iterative(root, key):
    new_node = TreeNode(key)
    
    if not root:
        return new_node
    
    parent = None
    current = root
    
    while current:
        parent = current
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            return root  # Duplicate
    
    if key < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node
    
    return root
```

### Delete - O(h)

**Three Cases**:

```
Case 1: Node is leaf         Case 2: One child       Case 3: Two children
        50                          50                       50
       /  \                        /  \                     /  \
      30   70                     30   70                  30   70
       ↑                         /                        / \   / \
    Delete 30                   20                       20 40 60 80
    Just remove            Replace 30 with 20              ↑
                                                       Delete 30
                                                    Replace with 40 (inorder successor)
                                                    or 20 (inorder predecessor)
```

```python
def delete(root, key):
    if not root:
        return root
    
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # Case 1 & 2: No child or one child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Case 3: Two children
        # Find inorder successor (smallest in right subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)
    
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def find_max(node):
    while node.right:
        node = node.right
    return node
```

---

## 7.3 BST Complexity Analysis

| Operation | Average Case | Worst Case (Skewed) |
|-----------|--------------|---------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Find Min/Max | O(log n) | O(n) |
| Inorder Successor | O(log n) | O(n) |

**Why O(n) worst case?**
Inserting sorted sequence creates skewed tree:
```
Insert: 1, 2, 3, 4, 5

    1
     \
      2
       \
        3
         \
          4
           \
            5

Height = n - 1, so all operations are O(n)
```

**Solution**: Self-balancing BSTs (AVL, Red-Black)

---

## 7.4 Important BST Properties

### Inorder Traversal = Sorted Order

```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Inorder: 20, 30, 40, 50, 60, 70, 80 (sorted!)
```

### Inorder Successor

**Definition**: Next node in inorder traversal

**Algorithm**:
1. If right subtree exists: leftmost node in right subtree
2. Otherwise: nearest ancestor where node is in left subtree

```python
def inorder_successor(root, node):
    # Case 1: Right subtree exists
    if node.right:
        return find_min(node.right)
    
    # Case 2: No right subtree
    successor = None
    while root:
        if node.val < root.val:
            successor = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break
    
    return successor
```

### Inorder Predecessor

**Definition**: Previous node in inorder traversal

1. If left subtree exists: rightmost node in left subtree
2. Otherwise: nearest ancestor where node is in right subtree

---

## 7.5 BST Problems

### Problem 1: Validate BST

**Trap**: Just checking node.left.val < node.val < node.right.val is WRONG!

```
        10
       /  \
      5    15
          /  \
         6   20

This is NOT a valid BST (6 < 10, but 6 is in right subtree of 10)
```

**Correct Approach**: Pass valid range to each node

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))
```

**Alternative**: Inorder traversal should give sorted sequence

```python
def is_valid_bst_inorder(root):
    prev = [float('-inf')]
    
    def inorder(node):
        if not node:
            return True
        
        if not inorder(node.left):
            return False
        
        if node.val <= prev[0]:
            return False
        prev[0] = node.val
        
        return inorder(node.right)
    
    return inorder(root)
```

### Problem 2: Kth Smallest Element

```python
def kth_smallest(root, k):
    count = [0]
    result = [None]
    
    def inorder(node):
        if not node or result[0] is not None:
            return
        
        inorder(node.left)
        
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        
        inorder(node.right)
    
    inorder(root)
    return result[0]

# Time: O(H + k), Space: O(H)
```

### Problem 3: Lowest Common Ancestor in BST

```python
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    
    return None

# Time: O(H), Space: O(1)
```

**The "AHA" Moment** 💡:
> LCA is where p and q "split" - one goes left, other goes right

### Problem 4: Convert Sorted Array to Balanced BST

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root

# Time: O(n), Space: O(log n) - recursion
```

### Problem 5: Recover BST (Two Nodes Swapped)

```python
def recover_tree(root):
    first = second = prev = None
    
    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        
        inorder(node.left)
        
        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node
        prev = node
        
        inorder(node.right)
    
    inorder(root)
    first.val, second.val = second.val, first.val
```

---

## 7.6 Self-Balancing BSTs

### Why Balance?

| Tree Type | Height | Operations |
|-----------|--------|------------|
| Skewed BST | O(n) | O(n) |
| Random BST | O(log n) expected | O(log n) expected |
| Balanced BST | O(log n) guaranteed | O(log n) guaranteed |

### AVL Tree

**Property**: For every node, |height(left) - height(right)| ≤ 1

**Balance Factor (BF)** = height(left) - height(right)
- BF ∈ {-1, 0, 1} for valid AVL

**Node Structure**:
```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
```

### AVL Rotations

#### Right Rotation (LL Case)
```
        z                       y
       / \                    /   \
      y   T4     RR(z)       x     z
     / \       -------->    / \   / \
    x   T3                 T1 T2 T3 T4
   / \
  T1  T2
```

```python
def right_rotate(z):
    y = z.left
    T3 = y.right
    
    y.right = z
    z.left = T3
    
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    
    return y
```

#### Left Rotation (RR Case)
```
      z                          y
     / \                       /   \
    T1  y       LR(z)         z     x
       / \    -------->      / \   / \
      T2  x                 T1 T2 T3 T4
         / \
        T3  T4
```

```python
def left_rotate(z):
    y = z.right
    T2 = y.left
    
    y.left = z
    z.right = T2
    
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    
    return y
```

#### LR Case (Left-Right)
```
     z               z               x
    / \            /   \           /   \
   y   T4   LR   x     T4   RR    y     z
  / \       -->  / \         -->  / \   / \
 T1  x          y   T3           T1 T2 T3 T4
    / \        / \
   T2  T3     T1  T2
```

**Solution**: Left rotate y, then right rotate z

#### RL Case (Right-Left)
**Solution**: Right rotate y, then left rotate z

### AVL Insertion

```python
def insert_avl(root, key):
    # Standard BST insert
    if not root:
        return AVLNode(key)
    
    if key < root.val:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)
    
    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    # Get balance factor
    balance = get_balance(root)
    
    # LL Case
    if balance > 1 and key < root.left.val:
        return right_rotate(root)
    
    # RR Case
    if balance < -1 and key > root.right.val:
        return left_rotate(root)
    
    # LR Case
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    # RL Case
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0
```

### AVL vs Red-Black Tree

| Property | AVL | Red-Black |
|----------|-----|-----------|
| Balance strictness | Strict (BF ≤ 1) | Relaxed |
| Height | 1.44 log n | 2 log n |
| Search | Faster | Slower |
| Insert/Delete | More rotations | Fewer rotations |
| Use case | Read-heavy | Write-heavy |
| Used in | Databases | STL map, Java TreeMap |

---

## 7.7 Red-Black Tree

### Properties
1. Every node is Red or Black
2. Root is Black
3. Every leaf (NULL) is Black
4. Red node cannot have red child (no two consecutive reds)
5. Every path from node to descendant NULL has same black nodes

```
        B(10)
       /    \
     R(5)   R(15)
     / \     / \
   B(3) B(7) B(12) B(20)
```

### Red-Black Operations

**Insertion**: Insert as Red, then fix violations
**Deletion**: Complex recoloring and rotations

---

## 7.8 GATE Exam Patterns

### Pattern 1: BST Construction

**Q**: Insert 10, 5, 15, 3, 7, 12, 18 into empty BST. Draw the tree.

```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

### Pattern 2: Number of BSTs

**Q**: How many distinct BSTs with n nodes?

**Answer**: Catalan number Cₙ = (2n)! / ((n+1)! × n!)

### Pattern 3: Average Height

**Q**: What is expected height of BST with n random insertions?

**Answer**: O(log n) expected, O(n) worst case

### Pattern 4: AVL Rotations

**Q**: Insert these elements into AVL tree and count rotations.

**Method**: Track balance factors after each insert

### Pattern 5: Min/Max Nodes in AVL

**Q**: Minimum nodes in AVL tree of height h?

**Answer**: N(h) = N(h-1) + N(h-2) + 1

| h | Min Nodes |
|---|-----------|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 7 |
| 4 | 12 |

Formula: N(h) ≈ φ^h where φ = 1.618 (golden ratio)

---

## 7.9 Edge Cases & Traps

### Common Traps ⚠️

**Trap 1**: BST allows duplicates?
- Standard BST: No
- Extended BST: Left subtree ≤ node, Right subtree >

**Trap 2**: Delete node with two children
- Use inorder successor OR predecessor (both valid)
- Copy value, then delete the successor/predecessor

**Trap 3**: AVL after delete
- May require multiple rotations (up to O(log n))
- Insert needs at most 2 rotations

**Trap 4**: Height definition
- Some define: empty tree has height -1, single node has height 0
- Others: empty tree has height 0, single node has height 1
- Read question carefully!

---

## 📝 GATE Practice Problems

**Q1**: A BST has n nodes. What is the minimum and maximum height?

**Q2**: Insert 50, 30, 70, 20, 40, 60, 80, 25 into an AVL tree. How many rotations?

**Q3**: What is the inorder successor of 50 in the BST formed by inserting 50, 30, 70, 40, 60?

**Q4**: Minimum height AVL tree with 100 nodes has approximately how many nodes?

**Q5**: A BST contains n elements. Which traversal gives sorted output?

---

## 🎯 Quick Reference

### BST vs Balanced BST

| Operation | BST (worst) | BST (avg) | AVL/RB |
|-----------|-------------|-----------|--------|
| Search | O(n) | O(log n) | O(log n) |
| Insert | O(n) | O(log n) | O(log n) |
| Delete | O(n) | O(log n) | O(log n) |
| Space | O(n) | O(n) | O(n) |

### AVL Rotation Quick Reference

| Imbalance | BF(node) | BF(child) | Rotation |
|-----------|----------|-----------|----------|
| LL | > 1 | ≥ 0 | Right |
| LR | > 1 | < 0 | Left-Right |
| RR | < -1 | ≤ 0 | Left |
| RL | < -1 | > 0 | Right-Left |

---

## 🔑 Key Takeaways

1. **BST property**: All left < root < all right (not just immediate children)
2. **Inorder of BST = sorted** - this is the most exploited property
3. **Self-balancing** prevents O(n) degradation
4. **AVL trees** guarantee O(log n) with strict balancing
5. **Red-Black trees** are less strict but practically faster for modifications
6. **Validate BST** using range method, not just parent-child comparison

---

*Next: [Heaps & Priority Queues →](08-Heaps.md)*
