from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            self.rotate_one_step(nums)
            i += 1
            
    def rotate_one_step(self, nums: List[int]):
        last_elem = nums[-1]
        j = len(nums)
        while j > 0:
            nums[j] = nums[j-1]
            j -= 1
            
        nums[0] = last_elem
    

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

        nums = [1]
        Solution().rotate(nums, 1)
        assert nums == [1]

        nums = [1, 2]
        Solution().rotate(nums, 3)
        assert nums == [2, 1]

        nums = [1, 2, 3]
        Solution().rotate(nums, 0)
        assert nums == [1, 2, 3]

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