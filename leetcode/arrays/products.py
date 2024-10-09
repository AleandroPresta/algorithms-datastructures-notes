from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass
class Test:
    def test_basic(self):
        assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
        assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
        assert Solution().productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24]
        assert Solution().productExceptSelf([1, 2, 3]) == [6, 3, 2]
        assert Solution().productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_advanced(self):
        assert Solution().productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
        assert Solution().productExceptSelf([5, 4, 3, 2, 1]) == [24, 30, 40, 60, 120]
        assert Solution().productExceptSelf([1, 2, 3, 0, 4]) == [0, 0, 0, 24, 0]
        assert Solution().productExceptSelf([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
        assert Solution().productExceptSelf([1, -1, 1, -1]) == [1, -1, 1, -1]

    def test_edge_cases(self):
        assert Solution().productExceptSelf([1, 0]) == [0, 1]
        assert Solution().productExceptSelf([0, 1]) == [1, 0]
        assert Solution().productExceptSelf([1, 2, 0, 4, 5]) == [0, 0, 40, 0, 0]
        assert Solution().productExceptSelf([1, 2, 3, 4, 0]) == [0, 0, 0, 0, 24]
        assert Solution().productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3628800, 1814400, 1209600, 907200, 725760, 604800, 518400, 453600, 403200, 362880]

def main() -> None:
    tester = Test()
    
    tester.test_basic()
    print('Basic tests passed')
    
    tester.test_advanced()
    print('Advanced tests passed')
    
    tester.test_edge_cases()
    print('Edge case tests passed')
    

if __name__ == '__main__':
    main()