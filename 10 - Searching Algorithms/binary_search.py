from typing import List


class BinarySearch:
    def binary_search(a: List[int], target: int) -> int:
        if not a: return -1
        
        left = 0
        right = len(a)-1
        while left <= right:
            middle = left + (right - left) // 2
            if a[middle] == target:
                return middle
            else:
                if target > a[middle]:
                    left = middle + 1
                else:
                    right = middle + 1
        
        return -1
    
    