from typing import List


class BinarySearch:
    '''
        Returns the index of the target element or -1 if the element doesn't exist
    '''
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1