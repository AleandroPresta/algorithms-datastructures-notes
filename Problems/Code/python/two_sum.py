def two_sum(nums, target):
    """
    Finds two numbers in the list 'nums' that add up to 'target'.

    Args:
    - nums (list of int): The list of integers to search.
    - target (int): The target sum of two numbers in 'nums'.

    Returns:
    - list or None: A list containing the indices of the two numbers that add up to 'target',
      or None if no such pair exists.

    Example:
    >>> nums = [2, 7, 11, 15]
    >>> target = 9
    >>> two_sum(nums, target)
    [0, 1]  # Indices of numbers 2 and 7 which add up to 9
    
    Complexity:
    - Time: O(n)
      The function iterates over the list 'nums' once (O(n)), and each dictionary lookup
      or insertion operation in 'num_map' averages O(1). Thus, the overall time complexity
      is O(n).

    - Space: O(n)
      The space complexity is O(n) due to the usage of 'num_map', which can store up to 
      'n' elements in the worst case scenario where no pair is found.
    """
    num_map = {}  # Dictionary (HashMap) to store seen numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement needed to reach 'target'
        if complement in num_map: # Search the complement in num_map
            # If complement exists in num_map, return the indices of the current number and complement
            return [num_map[complement], i]
        num_map[num] = i  # Store the current number and its index in num_map

    return None  # Return None if no such pair is found



def main():
    # Example usage:
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1] (indices of numbers 2 and 7)


if __name__ == "__main__":
    main()
