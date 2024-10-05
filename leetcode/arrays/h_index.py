from typing import Dict, List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        The h-index is defined as the maximum value of h such that the given researcher has 
        published at least h papers that have each been cited at least h times.
        """
        # Edge cases
        if citations == [] or citations == [0]:
            return 0
        
        h = 0
        h_max = max(citations)
        while h < h_max:
            n_h = 0
            for i in range(len(citations)):
                if citations[i] >= h+1:
                    n_h += 1
            if n_h > h:
                h += 1
            else:
                break
        return h

class Test:
    def test_basic(self):
        assert Solution().hIndex([3, 0, 6, 1, 5]) == 3
        assert Solution().hIndex([1, 3, 1]) == 1
        assert Solution().hIndex([0, 1, 3, 5, 6]) == 3
        assert Solution().hIndex([10, 8, 5, 4, 3]) == 4
        assert Solution().hIndex([25, 8, 5, 3, 3]) == 3
        assert Solution().hIndex([0, 0, 0, 0, 0]) == 0
        assert Solution().hIndex([1, 1, 1, 1, 1]) == 1
        assert Solution().hIndex([4, 4, 4, 4, 4]) == 4
        assert Solution().hIndex([0, 1, 2, 3, 4]) == 2
        assert Solution().hIndex([100]) == 1

    def test_advanced(self):
        assert Solution().hIndex([0, 0, 0, 0, 1]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 2]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 3]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 4]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 5]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 6]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 7]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 8]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 9]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 10]) == 1

    def test_edge_cases(self):
        assert Solution().hIndex([]) == 0
        assert Solution().hIndex([0]) == 0
        assert Solution().hIndex([1]) == 1
        assert Solution().hIndex([100, 100, 100, 100, 100]) == 5
        assert Solution().hIndex([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        assert Solution().hIndex([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        assert Solution().hIndex([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        assert Solution().hIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
        assert Solution().hIndex([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        assert Solution().hIndex([0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 1

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