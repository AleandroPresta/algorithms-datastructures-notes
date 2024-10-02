# Big O

The purpose of Big O is to define the efficiency of any given algorithm and how their running time or space requirements grow as the input size grows. There are two types of complexity:

1. Time Complexity;
2. Space Complexity.

This efficiency usually refers to the _worst case scenario_. Big O doesn't care about hardware or software cababilities.

### Constant Time

Constant time is indicated with $O(1)$. It is called constant because the running time does not change with the size of the input. **Example**: Accessing an element in an array by index. If we know the index that can be done with a single operation `array[index]`.

### Linear Time

Linear time is indicated with $O(n)$. The running time grows linearly with the input size. This means that if the input size doubles, the running time or space usage also doubles.
**Example**: Iterating through an array. If we need to search an element and we don't know the index we need to iterate through the whole array. If we start from `index = 0` and the element is in the last position (worst case) then we need `n = len(array)` checks or operations to find the element.

### Logarithmic Time

Logarithmic time is indicated with $O(log(n))$.The running time grows logarithmically with the input size. **Example**: Binary search in a sorted array. Because the binary search eliminates 50% of the input for each check/operation.

### Linearithmic Time

Logarithmic time is indicated with $O(n \ log(n))$.
The running time grows in proportion to $n \ log(n)$. This complexity is common in algorithms that divide the problem into smaller subproblems, solve each subproblem independently, and then combine the results. **Example**: Efficient sorting algorithms like mergesort and heapsort.

### Quadratic Time

Quadratic time is indicated with $O(n^2)$.
The running time grows proportionally to the square of the input size. Example: Simple sorting algorithms like bubble sort, insertion sort.

### Cubic Time

Cubic time is indicated with $O(n^3)$.
The running time grows proportionally to the cube of the input size. Example: Certain dynamic programming algorithms.

### Exponential Time

Exponential time is indicated with $O(2^n)$.
The running time doubles with each additional element in the input. Example: Solving the traveling salesman problem using brute-force.

### Factorial Time

Factorial time is indicated with $O(n!)$.
The running time grows factorially with the input size. Example: Generating all permutations of a set.
