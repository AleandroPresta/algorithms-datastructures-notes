class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge cases
        if (haystack == needle): # this includes the '' == '' case
            return 0
        if (haystack == '' or needle == ''):
            return -1
        
        # If the substring to search is longer then the total string
        if (len(needle) > len(haystack)):
            return -1
        
        # Define the max length to check
        max_len = len(haystack) - len(needle) + 1
        for i in range(max_len):
            # Positive case
            check_str = haystack[i:len(needle)+i]
            if (check_str == needle):
                return i
        
        return -1
        
class Test:
    def test_basic(self):
        assert Solution().strStr('sadbutsad', 'sad') == 0
        assert Solution().strStr('leetcode', 'leeto') == -1
        assert Solution().strStr('hello', 'll') == 2
        assert Solution().strStr('aaaaa', 'bba') == -1

    def test_advanced(self):
        assert Solution().strStr('mississippi', 'issip') == 4
        assert Solution().strStr('abracadabra', 'cad') == 4
        assert Solution().strStr('pineapple', 'apple') == 4
        assert Solution().strStr('a' * 1000 + 'b', 'ab') == 999
        assert Solution().strStr('a' * 1000 + 'b', 'ba') == -1

    def test_edge_cases(self):
        assert Solution().strStr('', 'a') == -1
        assert Solution().strStr('a', '') == 0
        assert Solution().strStr('a', 'a') == 0
        assert Solution().strStr('a', 'b') == -1
        assert Solution().strStr('abc', 'c') == 2
        

def main() -> None:
    tester = Test()
    
    tester.test_basic()
    print('Basic tests passed')
    
    tester.test_advanced()
    print('Advanced tests passed')
    
    tester.test_basic()
    print('Edge case tests passed')
    

if __name__ == '__main__':
    main()