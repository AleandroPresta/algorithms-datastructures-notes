# Searching Algorithm

There are two tecniques using to search a data structure:

1. _Linear Search_: jumping from one node to another to find the searched element (`Time Complexity O(n)`);
2. _Binary Search_: using a sorted data structure we can go to the middle of the structure, if the middle element is `>` than the element we recursively apply the binary search to the left part of the array, if the middle element is `<` than we apply the search on the right side, until we find the searched element (`Time Complexity O(log(n))`).
