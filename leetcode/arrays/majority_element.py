'''
169. Majority Element
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m: dict = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        result = max(m, key=m.get)
        print(f'Result: {result}')
        return result
        
        
class Test:
    def test1(self) -> None:
        nums = [3,2,3]
        assert Solution().majorityElement(nums) == 3
        
    def test2(self) -> None:
        nums = [2,2,1,1,1,2,2]
        assert Solution().majorityElement(nums) == 2
        
    def test3(self) -> None:
        nums = [3,3,4]
        assert Solution().majorityElement(nums) == 3
        
        
def main() -> None:
    test = Test()
    test.test1()
    test.test2()
    test.test3()
    print('All tests passed')
    
if __name__ == '__main__':
    main()