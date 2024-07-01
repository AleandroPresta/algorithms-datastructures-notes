# Arrays
## Introduction
Arrays are data structures used to store multiple values in a single variable. Here are some key points about arrays:

1. **Structure**: Arrays consist of elements, each identified by an index or key. The first element is at index 0 (in most programming languages).

2. **Fixed Size**: In many languages, the size of an array is fixed when it is created, meaning you can't add more elements than the specified size.

3. **Homogeneous Elements**: Typically, arrays store elements of the same data type, such as integers, strings, or objects.

4. **Contiguous Memory Allocation**: Elements of an array are stored in contiguous memory locations, allowing efficient indexing and access.

5. **Accessing Elements**: You can access elements by their index, which allows for quick read and write operations (in $O(1)$). For example, `array[2]` accesses the third element in the array.

6. **Types of Arrays**:
   - **One-dimensional arrays**: A single row of elements.
   - **Multi-dimensional arrays**: Arrays with more than one dimension, like matrices (two-dimensional arrays) or higher-dimensional arrays.

Arrays are fundamental in programming for organizing and managing collections of data efficiently.

### Array Operations

Arrays support several operations. Here are the common ones with their time and space complexity explained:

1. **Accessing an Element**
   - **Description**: Retrieve the value at a specific index.
   - **Time Complexity**: $O(1)$
   - **Space Complexity**: $O(1)$

2. **Updating an Element**
   - **Description**: Change the value at a specific index.
   - **Time Complexity**: $O(1)$
   - **Space Complexity**: $O(1)$

3. **Inserting an Element**
   - **Description**: Add an element at a specific position.
   - **Time Complexity**: $O(n)$
     - Inserting at the end: $O(1)$ (amortized)
     - Inserting at the beginning or middle: $O(n)$ (due to shifting elements)
   - **Space Complexity**: $O(1)$

4. **Deleting an Element**
   - **Description**: Remove an element at a specific position.
   - **Time Complexity**: $O(n)$
     - Deleting from the end: $O(1)$
     - Deleting from the beginning or middle: $O(n)$ (due to shifting elements)
   - **Space Complexity**: $O(1)$

5. **Searching for an Element**
   - **Description**: Find the index of an element with a specific value.
   - **Time Complexity**: $O(n)$
     - Linear Search: $O(n)$
     - Binary Search (only for sorted arrays): $O(log(n))$
   - **Space Complexity**: $O(1)$

6. **Finding the Length**
   - **Description**: Get the number of elements in the array.
   - **Time Complexity**: $O(1)$
   - **Space Complexity**: $O(1)$

7. **Iterating Over Elements**
   - **Description**: Visit each element in the array.
   - **Time Complexity**: $O(n)$
   - **Space Complexity**: $O(1)$

8. **Copying an Array**
   - **Description**: Create a duplicate of the array.
   - **Time Complexity**: $O(n)$
   - **Space Complexity**: $O(n)$

9. **Resizing an Array (Dynamic Arrays)**
   - **Description**: Expand or shrink the array.
   - **Time Complexity**: $O(n)$ (amortized)
   - **Space Complexity**: $O(n)$