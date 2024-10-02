# Sorting Algorithms

A sorting algorithm is an algorithm that puts elements of a list in a certain order.

## Types of Sorting Algorithms

1. Bubble Sort: Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
2. Selection Sort: The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
3. Insertion Sort: Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
4. Merge Sort: Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
5. Quick Sort: QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
6. Heap Sort: Heap sort is a comparison based sorting technique based on Binary Heap data structure.

## Sorting Algorithms Comparison

| Algorithm      | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity | Stable |
| -------------- | -------------------- | ----------------------- | --------------------- | ---------------- | ------ |
| Bubble Sort    | O(n)                 | O(n^2)                  | O(n^2)                | O(1)             | Yes    |
| Selection Sort | O(n^2)               | O(n^2)                  | O(n^2)                | O(1)             | No     |
| Insertion Sort | O(n)                 | O(n^2)                  | O(n^2)                | O(1)             | Yes    |
| Merge Sort     | O(n log n)           | O(n log n)              | O(n log n)            | O(n)             | Yes    |
| Quick Sort     | O(n log n)           | O(n log n)              | O(n^2)                | O(log n)         | No     |
| Heap Sort      | O(n log n)           | O(n log n)              | O(n log n)            | O(1)             | No     |
