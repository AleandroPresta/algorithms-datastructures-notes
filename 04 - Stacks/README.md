# Stack Data Structure

## Introduction
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. The most recently added element is the first one to be removed. Think of it as a collection of items stacked one on top of another, where only the topmost item is accessible.

## Key Characteristics
- **LIFO (Last In, First Out)**: The last element added to the stack is the first one to be removed.
- **Single Access Point**: Elements can only be added or removed from the top of the stack.

## Common Operations and Their Complexities

### Push
Adds an element to the top of the stack.

- **Operation**: `push(element)`
- **Time Complexity**: $O(1)$
- **Space Complexity**: $O(1)$

### Pop
Removes the top element from the stack.

- **Operation**: `pop()`
- **Time Complexity**: $O(1)$
- **Space Complexity**: $O(1)$

### Peek (or Top)
Returns the top element of the stack without removing it.

- **Operation**: `peek()`
- **Time Complexity**: $O(1)$
- **Space Complexity**: $O(1)$

### IsEmpty
Checks if the stack is empty.

- **Operation**: `isEmpty()`
- **Time Complexity**: $O(1)$
- **Space Complexity**: $O(1)$

### Size
Returns the number of elements in the stack.

- **Operation**: `size()`
- **Time Complexity**: $O(1)$
- **Space Complexity**: $O(1)$