from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.
        """
        # Implementation here
        pass

class Test:
    def test_basic(self):
        assert Solution().reverseWords("the sky is blue") == "blue is sky the"
        assert Solution().reverseWords("  hello world  ") == "world hello"
        assert Solution().reverseWords("a good   example") == "example good a"
        assert Solution().reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
        assert Solution().reverseWords("Alice does not even like bob") == "bob like even not does Alice"

    def test_advanced(self):
        assert Solution().reverseWords("  ") == ""
        assert Solution().reverseWords("a") == "a"
        assert Solution().reverseWords("  a  b  ") == "b a"
        assert Solution().reverseWords("a b c d e f g") == "g f e d c b a"
        assert Solution().reverseWords("  a  b  c  d  e  f  g  ") == "g f e d c b a"

    def test_edge_cases(self):
        assert Solution().reverseWords("") == ""
        assert Solution().reverseWords(" ") == ""
        assert Solution().reverseWords("   ") == ""
        assert Solution().reverseWords("a   ") == "a"
        assert Solution().reverseWords("   a") == "a"

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