# Problems

## Table of Contents

-   [Two Sum Problem](#two-sum-problem)
    -   [Example](#example)
    -   [Explanation](#explanation)
    -   [Approach to Solve](#approach-to-solve)
    -   [Complexity](#complexity)
    -   [Edge Cases](#edge-cases)

## Two Sum Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Example

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so the indices are 0 and 1.
```

### Explanation

1. **Input**: You are given an array `nums` and a target integer `target`.
2. **Output**: You need to find two distinct indices `i` and `j` in the array such that `nums[i] + nums[j] = target`.
3. **Assumptions**:
    - Each input would have exactly one solution, meaning there is exactly one pair of indices that satisfies the condition.
    - You cannot use the same element twice (i.e., indices `i` and `j` must be distinct).

### Approach to Solve

The Two Sum problem can be efficiently solved using a hash map (or dictionary) to store elements and their indices as you iterate through the array:

-   **Step-by-step Approach**:
    1. Initialize an empty dictionary to store elements and their indices.
    2. Iterate through each element in the array.
    3. For each element `nums[i]`, calculate `complement = target - nums[i]`.
    4. Check if `complement` exists in the dictionary:
        - If it exists, return the indices `[map[complement], i]`.
        - If it doesn't exist, add the current element and its index to the dictionary.
    5. If no solution is found after iterating through the array, return an appropriate response (based on problem constraints, there should always be a solution).

### Complexity

-   **Time Complexity**: $O(n)$, where n is the number of elements in the array. This is because we traverse the list containing n elements only once, and each lookup and insertion in the hash map takes average $O(1)$ time.
-   **Space Complexity**: $O(n)$, due to the extra space used by the hash map to store elements and their indices.

### Edge Cases

-   Arrays with fewer than two elements (though the problem states there will always be a solution).
-   Arrays with duplicate elements that may confuse the solution.

This problem is commonly used to introduce basic hash map usage and efficient searching techniques in algorithm design and is a good starting point for understanding how to optimize solution finding in data structures.

## Smaller then Current

Given an array `nums`, for each `nums[i]` find the number of elements in the array that are smaller than it. Return the array of counts. The solution can be found combining sorting and searching algorithms.

### Example

```
Input: nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 3]
Explanation: For each element in the array, the number of elements smaller than it are:
- 8: 4 elements (1, 2, 2, 3)
- 1: 0 elements
- 2: 1 element (1)
- 2: 1 element (1)
- 3: 3 elements (1, 2, 2)
```

### Complexity

-   **Time Complexity**: $O(n \log n)$, where n is the number of elements in the array. This is due to the sorting operation.
-   **Space Complexity**: $O(n)$, where n is the number of elements in the array. This is due to the extra space used to store the sorted array and the result array.
