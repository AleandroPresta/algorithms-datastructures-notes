from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Edge cases
        if k <= 0 or nums == []:
            return
        
        # Normalize k if k > len(nums)
        while k > len(nums):
            k -= len(nums)
            
        # If k = len(nums) after normalization than the rotate array is the same as the original
        if len(nums) == k:
            return
        
        last_elems = nums[-k:] # save the last k elements of nums
        j = len(nums)-1
        while j > k-1:
            nums[j] = nums[j-k]
            j -= 1
        
        nums[0:k] = last_elems
    

class TestRotate:
    def test_basic(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

        nums = [-1, -100, 3, 99]
        Solution().rotate(nums, 2)
        assert nums == [3, 99, -1, -100]

        nums = [1, 2]
        Solution().rotate(nums, 1)
        assert nums == [2, 1]

        nums = [1, 2, 3]
        Solution().rotate(nums, 2)
        assert nums == [2, 3, 1]

        nums = [1]
        Solution().rotate(nums, 0)
        assert nums == [1]
        
        nums = [1, 2]
        Solution().rotate(nums, 5)
        assert nums == [2, 1]

    def test_advanced(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 10)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 14)
        assert nums == [1, 2, 3, 4, 5, 6, 7]

        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 1)
        assert nums == [7, 1, 2, 3, 4, 5, 6]

        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 6)
        assert nums == [2, 3, 4, 5, 6, 7, 1]

        nums = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(nums, 7)
        assert nums == [1, 2, 3, 4, 5, 6, 7]

    def test_edge_cases(self):
        nums = []
        Solution().rotate(nums, 3)
        assert nums == []
        print('Test 1 passed')
        nums = [1]
        Solution().rotate(nums, 1)
        assert nums == [1]
        print('Test 2 passed')
        nums = [1, 2]
        Solution().rotate(nums, 3)
        assert nums == [2, 1]
        print('Test 3 passed')
        nums = [1, 2, 3]
        Solution().rotate(nums, 0)
        assert nums == [1, 2, 3]
        print('Test 4 passed')
        nums = [1, 2, 3]
        Solution().rotate(nums, 4)
        assert nums == [3, 1, 2]

def main() -> None:
    tester = TestRotate()
    
    tester.test_basic()
    print('Basic tests passed')
    
    tester.test_advanced()
    print('Advanced tests passed')
    
    tester.test_edge_cases()
    print('Edge case tests passed')
    

if __name__ == '__main__':
    main()