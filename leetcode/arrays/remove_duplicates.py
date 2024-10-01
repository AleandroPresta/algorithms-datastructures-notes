from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set = {}
        for num in nums:
            set[num] = 1
            
        nums[:] = list(set.keys())
        return len(nums)

class Test:
    '''
    Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    '''
    def test1(self):
        nums = [1,1,2]
        s = Solution()
        assert s.removeDuplicates(nums) == 2 and nums == [1,2]
        
    def test2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        s = Solution()
        assert s.removeDuplicates(nums) == 5 and nums == [0,1,2,3,4]
        
def main():
    t = Test()
    t.test1()
    t.test2()
    print("All tests passed")
    
if __name__ == "__main__":
    main()