# Heap and Trie

## Table of Contents

1. [Heap](#heap)
    - [Operations on a Heap](#operations-on-a-heap)
    - [Complexity of Operations](#complexity-of-operations)
    - [Implementation Details](#implementation-details)
    - [Example Operations on a Max-Heap](#example-operations-on-a-max-heap)
2. [Trie](#trie)
    - [Structure of a Trie](#structure-of-a-trie)
    - [Basic Operations and Their Complexities](#basic-operations-and-their-complexities)
    - [Example of a Trie](#example-of-a-trie)

## Heap

![alt text](image.png)

A heap is a specialized tree-based data structure that satisfies the heap property. This property can be one of two types:

1.  **Max-Heap**: In a max-heap, for any given node `i`, the value of `i` is greater than or equal to the values of its children.
2.  **Min-Heap**: In a min-heap, for any given node `i`, the value of `i` is less than or equal to the values of its children.

### Operations on a Heap

1.  **Insertion**: Adding a new element to the heap.
2.  **Extract-Max/Extract-Min**: Removing the root element (maximum in a max-heap or minimum in a min-heap).
3.  **Peek/Find-Max/Find-Min**: Retrieving the root element without removing it.
4.  **Heapify**: Ensuring the heap property is maintained, typically after insertion or deletion.
5.  **Build-Heap**: Creating a heap from an unsorted array.

### Complexity of Operations

1.  **Insertion**

    -   **Process**:
        1.  Add the element to the end of the heap.
        2.  "Bubble up" (also called "sift up" or "heapify up") the element to restore the heap property.
    -   **Time Complexity**: $O(log n)$ due to the height of the heap (binary heap).

2.  **Extract-Max/Extract-Min**

    -   **Process**:
        1.  Swap the root with the last element.
        2.  Remove the last element (previous root).
        3.  "Bubble down" (also called "sift down" or "heapify down") the new root element to restore the heap property.
    -   **Time Complexity**: $O(log n)$ due to the height of the heap.

3.  **Peek/Find-Max/Find-Min**

    -   **Process**: Directly return the root element of the heap.
    -   **Time Complexity**: $O(1)$ as the root is always accessible.

4.  **Heapify**

    -   **Process**: Adjust the heap to maintain the heap property starting from a given node and moving downwards.
    -   **Time Complexity**: $O(log n)$ for a single node, $O(n)$ for the entire heap when building from an array.

5.  **Build-Heap**

    -   **Process**: Convert an unsorted array into a heap.
    -   **Time Complexity**: $O(n)$. This is often surprising but results from the fact that heapifying subtrees of increasing sizes takes progressively less work overall.

### Implementation Details

-   **Binary Heap**: A common and simple type of heap implemented using an array. For a node at index `i`:
    -   The left child is at index `2i + 1`.
    -   The right child is at index `2i + 2`.
    -   The parent is at index `(i - 1) // 2`.

### Example Operations on a Max-Heap

1.  **Insertion Example**

    -   Heap: [10, 5, 3]
    -   Insert 7:
        1.  Add 7 to the end: [10, 5, 3, 7]
        2.  Bubble up 7: Compare with parent 5 → Swap: [10, 7, 3, 5]

2.  **Extract-Max Example**

    -   Heap: [10, 7, 3, 5]
    -   Extract-Max:
        1.  Swap 10 with last element 5: [5, 7, 3, 10]
        2.  Remove 10: [5, 7, 3]
        3.  Bubble down 5: Compare with children (7 and 3) → Swap with 7: [7, 5, 3]

By maintaining the heap property, heaps are efficient for priority queue operations, providing quick access to the maximum or minimum element.

## Trie

A Trie, also known as a prefix tree, is a tree-like data structure that is used to efficiently store and retrieve keys in a dataset of strings. It is particularly useful for handling large dictionaries of words, like those used in autocompletion features or spell checking.

1.  **Nodes and Edges**:

    -   Each node represents a character of a string.
    -   The root node is empty (does not contain any character).
    -   Edges connect nodes and represent the next character in the string.

2.  **Paths**:

    -   A path from the root to a leaf node represents a complete string (or key).
    -   Intermediate nodes along the path represent prefixes of the string.

3.  **End of Word Marker**:

    -   Nodes can have a flag (or marker) to indicate the end of a valid word.

A Trie, also known as a prefix tree, is a tree-like data structure that is used to efficiently store and retrieve keys in a dataset of strings. It is particularly useful for handling large dictionaries of words, like those used in autocompletion features or spell checking.

### Structure of a Trie

1.  **Nodes and Edges**:

    -   Each node represents a character of a string.
    -   The root node is empty (does not contain any character).
    -   Edges connect nodes and represent the next character in the string.

2.  **Paths**:

    -   A path from the root to a leaf node represents a complete string (or key).
    -   Intermediate nodes along the path represent prefixes of the string.

3.  **End of Word Marker**:

    -   Nodes can have a flag (or marker) to indicate the end of a valid word.

### Basic Operations and Their Complexities

1.  **Insertion**:

    -   **Description**: Insert a word into the Trie.
    -   **Complexity**: $O(L)$, where L is the length of the word being inserted.
    -   **Procedure**:
        -   Start from the root node.
        -   For each character in the word, check if the corresponding child node exists.
        -   If it does not exist, create a new node.
        -   Move to the child node.
        -   Mark the end of the word on the last node.

2.  **Search**:

    -   **Description**: Search for a word in the Trie.
    -   **Complexity**: $O(L)$, where L is the length of the word being searched.
    -   **Procedure**:
        -   Start from the root node.
        -   For each character in the word, move to the corresponding child node.
        -   If a child node does not exist, the word is not present in the Trie.
        -   If all characters are found, check if the last node is marked as the end of the word.

3.  **Prefix Search (StartsWith)**:

    -   **Description**: Check if there is any word in the Trie that starts with a given prefix.
    -   **Complexity**: $O(L)$, where L is the length of the prefix.
    -   **Procedure**:
        -   Start from the root node.
        -   For each character in the prefix, move to the corresponding child node.
        -   If a child node does not exist, no word with the given prefix is present in the Trie.
        -   If all characters are found, return true.

4.  **Deletion**:

    -   **Description**: Delete a word from the Trie.
    -   **Complexity**: $O(L)$, where L is the length of the word being deleted.
    -   **Procedure**:
        -   Perform a search to check if the word exists.
        -   If the word is found, backtrack and remove nodes that are no longer part of any other word.

5.  **Traversal**:

    -   **Description**: Traverse all the words in the Trie.
    -   **Complexity**: $O(N)$, where $N$ is the number of nodes in the Trie.
    -   **Procedure**:
        -   Use Depth-First Search (DFS) or Breadth-First Search (BFS) to visit all nodes.
        -   Collect characters along the path and form words.

### Example of a Trie

Consider inserting the words "cat", "car", "cap", and "dog" into a Trie:

```
       (root)
      /  |    \
    c   d    ...
    |     |
    a     o
    |     |
    t     g
  / | \   |
 r  p ... .
```

-   After inserting "cat", "car", and "cap", they share the common prefix "ca".
-   Inserting "dog" starts a new branch from the root.

### Advantages of Tries

-   Efficient for searching, inserting, and deleting strings.
-   Space-efficient when storing many strings with common prefixes.
-   Supports operations like prefix search and autocomplete efficiently.

### Disadvantages of Tries

-   Can consume a lot of memory if many nodes are sparse.
-   Implementation complexity can be higher compared to simpler data structures like hash tables.
