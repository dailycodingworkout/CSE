# Chapter 7: Algorithms
## The Problem-Solving Arsenal | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"An algorithm is a recipe; efficiency is the cooking time."**

---

## 7.1 Algorithm Design Paradigms

### The Big Four

| Paradigm | Key Idea | When to Use |
|----------|----------|-------------|
| **Divide & Conquer** | Split → Solve → Merge | Independent subproblems |
| **Greedy** | Local optimal choice | Optimal substructure + greedy choice |
| **Dynamic Programming** | Overlapping subproblems | Optimal substructure + overlapping |
| **Backtracking** | Try all possibilities | Constraint satisfaction |

---

## 7.2 Sorting Algorithms

### Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes |

### Bubble Sort

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = 1;
            }
        }
        if (!swapped) break;  // Optimization: already sorted
    }
}
```

**Passes:** n-1 maximum, **Comparisons:** n(n-1)/2

### Selection Sort

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx])
                minIdx = j;
        swap(&arr[i], &arr[minIdx]);
    }
}
```

**Comparisons (always):** n(n-1)/2, **Swaps:** n-1

### Insertion Sort

```c
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

**Best case:** Already sorted, O(n), **Use case:** Small or nearly sorted arrays

### Merge Sort

```c
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int i = 0; i < n2; i++) R[i] = arr[m + 1 + i];
    
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
```

**Recurrence:** T(n) = 2T(n/2) + O(n) = O(n log n)

### Quick Sort

```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

**Best case:** Balanced partition, O(n log n)
**Worst case:** Already sorted (with first/last pivot), O(n²)

### Heap Sort

```c
void heapSort(int arr[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract elements
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}
```

### Counting Sort

```c
void countingSort(int arr[], int n, int range) {
    int count[range + 1], output[n];
    memset(count, 0, sizeof(count));
    
    for (int i = 0; i < n; i++) count[arr[i]]++;
    for (int i = 1; i <= range; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    for (int i = 0; i < n; i++) arr[i] = output[i];
}
```

---

## 7.3 Searching Algorithms

### Linear Search

```c
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return i;
    return -1;
}
```

**Time:** O(n), **Use when:** Unsorted data

### Binary Search

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) return mid;
        if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

**Time:** O(log n), **Prerequisite:** Sorted array

### 🎯 Binary Search Variations

```c
// Find first occurrence
int firstOccurrence(int arr[], int n, int key) {
    int low = 0, high = n - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            result = mid;
            high = mid - 1;  // Continue searching left
        } else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return result;
}

// Find last occurrence
int lastOccurrence(int arr[], int n, int key) {
    int low = 0, high = n - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            result = mid;
            low = mid + 1;  // Continue searching right
        } else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return result;
}

// Count occurrences
int countOccurrences(int arr[], int n, int key) {
    int first = firstOccurrence(arr, n, key);
    if (first == -1) return 0;
    int last = lastOccurrence(arr, n, key);
    return last - first + 1;
}
```

---

## 7.4 Divide and Conquer

### Template

```c
solution divideAndConquer(problem P) {
    if (P is small enough) {
        return directSolution(P);
    }
    
    // Divide
    subproblems = divide(P);
    
    // Conquer
    for each subproblem S in subproblems:
        solutions.add(divideAndConquer(S));
    
    // Combine
    return combine(solutions);
}
```

### Classic Problems

| Problem | Divide | Conquer | Combine | Time |
|---------|--------|---------|---------|------|
| Merge Sort | Split array | Sort halves | Merge | O(n log n) |
| Quick Sort | Partition | Sort parts | Nothing | O(n log n) |
| Binary Search | Choose half | Search half | Return | O(log n) |
| Max Subarray | Split | Find max in halves | Compare | O(n log n) |
| Closest Pair | Split by x | Find closest in halves | Check strip | O(n log n) |

### Master Theorem

For recurrence: $T(n) = aT(n/b) + f(n)$

Let $c = \log_b a$

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $f(n) = O(n^{c-\epsilon})$ | $T(n) = \Theta(n^c)$ |
| 2 | $f(n) = \Theta(n^c \log^k n)$ | $T(n) = \Theta(n^c \log^{k+1} n)$ |
| 3 | $f(n) = \Omega(n^{c+\epsilon})$ | $T(n) = \Theta(f(n))$ |

---

## 7.5 Greedy Algorithms

### When Greedy Works

1. **Greedy Choice Property:** Local optimal leads to global optimal
2. **Optimal Substructure:** Optimal solution contains optimal subsolutions

### Activity Selection

```c
struct Activity { int start, end; };

int activitySelection(struct Activity arr[], int n) {
    // Sort by end time
    sort(arr, n);  
    
    int count = 1;
    int lastEnd = arr[0].end;
    
    for (int i = 1; i < n; i++) {
        if (arr[i].start >= lastEnd) {
            count++;
            lastEnd = arr[i].end;
        }
    }
    return count;
}
```

### Fractional Knapsack

```c
struct Item { int weight, value; };

double fractionalKnapsack(struct Item items[], int n, int capacity) {
    // Sort by value/weight ratio
    sortByRatio(items, n);
    
    double totalValue = 0.0;
    for (int i = 0; i < n && capacity > 0; i++) {
        if (items[i].weight <= capacity) {
            totalValue += items[i].value;
            capacity -= items[i].weight;
        } else {
            totalValue += items[i].value * ((double)capacity / items[i].weight);
            capacity = 0;
        }
    }
    return totalValue;
}
```

### Huffman Coding

```c
struct Node { char ch; int freq; Node *left, *right; };

Node* buildHuffmanTree(char chars[], int freqs[], int n) {
    // Create min heap of leaf nodes
    MinHeap *heap = createMinHeap(n);
    for (int i = 0; i < n; i++)
        insert(heap, createNode(chars[i], freqs[i]));
    
    while (heap->size > 1) {
        Node *left = extractMin(heap);
        Node *right = extractMin(heap);
        
        Node *internal = createNode('$', left->freq + right->freq);
        internal->left = left;
        internal->right = right;
        
        insert(heap, internal);
    }
    return extractMin(heap);
}
```

### 🔥 Classic Greedy Problems

| Problem | Greedy Strategy | Time |
|---------|-----------------|------|
| Activity Selection | End time earliest | O(n log n) |
| Fractional Knapsack | Highest value/weight | O(n log n) |
| Job Scheduling | Deadline, penalty | O(n log n) |
| Huffman Coding | Lowest frequency first | O(n log n) |
| Dijkstra's | Nearest unvisited vertex | O(V² or E log V) |
| Prim's MST | Minimum edge weight | O(V² or E log V) |
| Kruskal's MST | Sort edges, union-find | O(E log E) |

---

## 7.6 Dynamic Programming

### When to Use DP

1. **Optimal Substructure:** Solution uses optimal solutions to subproblems
2. **Overlapping Subproblems:** Same subproblems solved multiple times

### Approaches

| Top-Down (Memoization) | Bottom-Up (Tabulation) |
|------------------------|------------------------|
| Start from main problem | Start from base cases |
| Recursion + cache | Iterative, fill table |
| Natural for some problems | Often more efficient |
| May have stack overhead | Uses space for table |

### Fibonacci

```c
// Naive recursive - O(2^n)
int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

// Memoization (Top-Down) - O(n)
int memo[100] = {-1};
int fibMemo(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fibMemo(n-1) + fibMemo(n-2);
}

// Tabulation (Bottom-Up) - O(n)
int fibTab(int n) {
    int dp[n+1];
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; i++)
        dp[i] = dp[i-1] + dp[i-2];
    return dp[n];
}

// Space Optimized - O(1) space
int fibOpt(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

### 0/1 Knapsack

```c
int knapsack(int W, int wt[], int val[], int n) {
    int dp[n+1][W+1];
    
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i-1] <= w)
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]);
            else
                dp[i][w] = dp[i-1][w];
        }
    }
    return dp[n][W];
}
```

**Recurrence:** 
$$dp[i][w] = \max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])$$

### Longest Common Subsequence (LCS)

```c
int LCS(char *X, char *Y, int m, int n) {
    int dp[m+1][n+1];
    
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (X[i-1] == Y[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[m][n];
}
```

### Longest Increasing Subsequence (LIS)

```c
int LIS(int arr[], int n) {
    int dp[n];
    for (int i = 0; i < n; i++) dp[i] = 1;
    
    for (int i = 1; i < n; i++)
        for (int j = 0; j < i; j++)
            if (arr[i] > arr[j])
                dp[i] = max(dp[i], dp[j] + 1);
    
    int maxLen = 0;
    for (int i = 0; i < n; i++)
        maxLen = max(maxLen, dp[i]);
    
    return maxLen;
}
```

### 🔥 Classic DP Problems

| Problem | State | Time | Space |
|---------|-------|------|-------|
| 0/1 Knapsack | dp[i][w] | O(nW) | O(nW) |
| LCS | dp[i][j] | O(mn) | O(mn) |
| LIS | dp[i] | O(n²) | O(n) |
| Edit Distance | dp[i][j] | O(mn) | O(mn) |
| Coin Change | dp[i] | O(nS) | O(S) |
| Matrix Chain | dp[i][j] | O(n³) | O(n²) |
| Floyd-Warshall | dp[i][j] | O(n³) | O(n²) |

---

## 7.7 Graph Algorithms

### Shortest Path Algorithms

#### Dijkstra's Algorithm

```c
void dijkstra(int graph[V][V], int src) {
    int dist[V];
    int visited[V] = {0};
    
    for (int i = 0; i < V; i++) dist[i] = INT_MAX;
    dist[src] = 0;
    
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, visited);
        visited[u] = 1;
        
        for (int v = 0; v < V; v++)
            if (!visited[v] && graph[u][v] && 
                dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }
}
```

**Time:** O(V²) or O((V+E) log V) with heap
**Limitation:** No negative edges

#### Bellman-Ford Algorithm

```c
void bellmanFord(int graph[E][3], int V, int E, int src) {
    int dist[V];
    for (int i = 0; i < V; i++) dist[i] = INT_MAX;
    dist[src] = 0;
    
    for (int i = 0; i < V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = graph[j][0], v = graph[j][1], w = graph[j][2];
            if (dist[u] != INT_MAX && dist[u] + w < dist[v])
                dist[v] = dist[u] + w;
        }
    }
    
    // Check negative cycle
    for (int j = 0; j < E; j++) {
        int u = graph[j][0], v = graph[j][1], w = graph[j][2];
        if (dist[u] != INT_MAX && dist[u] + w < dist[v])
            printf("Negative cycle exists");
    }
}
```

**Time:** O(VE), **Handles:** Negative edges

#### Floyd-Warshall Algorithm

```c
void floydWarshall(int dist[V][V]) {
    for (int k = 0; k < V; k++)
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
}
```

**Time:** O(V³), **All pairs shortest path**

### Minimum Spanning Tree

#### Prim's Algorithm

```c
void prim(int graph[V][V]) {
    int parent[V], key[V], inMST[V] = {0};
    
    for (int i = 0; i < V; i++) key[i] = INT_MAX;
    key[0] = 0;
    parent[0] = -1;
    
    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, inMST);
        inMST[u] = 1;
        
        for (int v = 0; v < V; v++)
            if (graph[u][v] && !inMST[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
    }
}
```

#### Kruskal's Algorithm

```c
void kruskal(Edge edges[], int V, int E) {
    sortEdgesByWeight(edges, E);
    
    int parent[V];
    for (int i = 0; i < V; i++) parent[i] = i;
    
    int edgeCount = 0, i = 0;
    while (edgeCount < V - 1 && i < E) {
        Edge e = edges[i++];
        int x = find(parent, e.src);
        int y = find(parent, e.dest);
        
        if (x != y) {
            printf("%d -- %d: %d\n", e.src, e.dest, e.weight);
            union(parent, x, y);
            edgeCount++;
        }
    }
}
```

### Topological Sort

```c
void topologicalSort(Graph* g) {
    int inDegree[V] = {0};
    for (int u = 0; u < V; u++)
        for each v in adj[u]
            inDegree[v]++;
    
    Queue q;
    for (int i = 0; i < V; i++)
        if (inDegree[i] == 0) enqueue(&q, i);
    
    while (!isEmpty(&q)) {
        int u = dequeue(&q);
        printf("%d ", u);
        
        for each v in adj[u] {
            inDegree[v]--;
            if (inDegree[v] == 0) enqueue(&q, v);
        }
    }
}
```

---

## 7.8 Backtracking

### Template

```c
void backtrack(state, choices) {
    if (isSolution(state)) {
        processSolution(state);
        return;
    }
    
    for each choice in choices {
        if (isValid(choice)) {
            makeChoice(state, choice);
            backtrack(state, remaining_choices);
            undoChoice(state, choice);  // Backtrack
        }
    }
}
```

### N-Queens Problem

```c
int isSafe(int board[N][N], int row, int col) {
    // Check column
    for (int i = 0; i < row; i++)
        if (board[i][col]) return 0;
    
    // Check upper-left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return 0;
    
    // Check upper-right diagonal
    for (int i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j]) return 0;
    
    return 1;
}

int solveNQueens(int board[N][N], int row) {
    if (row >= N) return 1;  // All queens placed
    
    for (int col = 0; col < N; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 1;
            if (solveNQueens(board, row + 1)) return 1;
            board[row][col] = 0;  // Backtrack
        }
    }
    return 0;
}
```

---

## 🎯 Practice Problems

### Problem 1: Sorting Comparisons
**Q:** Minimum comparisons to merge two sorted arrays of size m and n?
**Answer:** m + n - 1 (in worst case)

### Problem 2: Binary Search
**Q:** How many comparisons for binary search in array of 1023 elements?
**Answer:** $\lceil \log_2 1024 \rceil = 10$

### Problem 3: Recurrence
**Q:** Solve $T(n) = 4T(n/2) + n$
**Answer:** Using Master Theorem: $a=4, b=2, c=\log_2 4 = 2$, $f(n) = n = O(n^{2-\epsilon})$. Case 1: $T(n) = \Theta(n^2)$

### Problem 4: LCS
**Q:** LCS of "ABCD" and "AEBD"?
**Answer:** "ABD" with length 3

### Problem 5: Dijkstra
**Q:** Can Dijkstra handle negative edges?
**Answer:** No, may give wrong result. Use Bellman-Ford instead.

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"Greedy grabs the biggest piece immediately. DP builds a table of all possibilities. Divide & Conquer splits the pizza equally. Backtracking tries every topping and removes bad ones."**

### The Mental Slider
- **Sorting:** Visualize cards being arranged
- **DP:** Building a pyramid, each brick needs lower ones
- **Graph:** Metro map, finding shortest route
- **Backtracking:** Maze solving, marking dead ends

### The 5-Second Snap-Check
1. **Overlapping subproblems?** Use DP
2. **Local optimal = Global optimal?** Use Greedy
3. **Independent subproblems?** Use Divide & Conquer
4. **Constraint satisfaction?** Use Backtracking
5. **Negative edges in graph?** Don't use Dijkstra

---

## 📈 Complexity Summary

| Algorithm Type | Best | Average | Worst |
|----------------|------|---------|-------|
| Comparison sorts | O(n log n) | O(n log n) | O(n log n) |
| Non-comparison sorts | O(n + k) | O(n + k) | O(n + k) |
| Binary Search | O(1) | O(log n) | O(log n) |
| BFS/DFS | O(V + E) | O(V + E) | O(V + E) |
| Dijkstra (heap) | O(E log V) | O(E log V) | O(E log V) |
| DP (typical) | - | O(nW) or O(n²) | - |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Data Structures](06-Data-Structures.md) | [Next: Object-Oriented Programming →](08-OOP.md)
