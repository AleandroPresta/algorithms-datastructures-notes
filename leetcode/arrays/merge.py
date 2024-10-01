from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if (nums2 == []):
            return
        
        nums1_copy = nums1[:]
        i = 0
        j = 0
        k = 0
        while (i < m or j < n):
            if (nums1_copy[i] <= nums2[j] and i < m):
                nums1[k] = nums1_copy[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        
    
class Test:
    def test1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        expected_result = [1,2,2,3,5,6]
        assert nums1 == expected_result
        
    def test2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        expected_result = [1]
        assert nums1 == expected_result
        
    def test3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        expected_result = [1]
        assert nums1 == expected_result
        

def main() -> None:
    test = Test()
    test.test1()
    test.test2()
    test.test3()
    print('All test passed')
    
if __name__ == '__main__':
    main()