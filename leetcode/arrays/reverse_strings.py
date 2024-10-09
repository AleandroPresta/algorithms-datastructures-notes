from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.
        """
        
        # Edge cases
        if s == " " or s == "":
            return ""
        
        if len(s) == 1 or " " not in s:
            return s
        
        s1: str = self.remove_double_spaces(s) # O(n)
        
        if s1 == " " or s1 == "":
            return ""
        
        s1: str = self.remove_initial_spaces(s1)
        s1: str = self.remove_final_spaces(s1)
        words: List[str] = s1.split(sep=" ")
        words_reverse: List[str] = self.reverse_array(words)
        s_result: str = self.concat_array(words_reverse)
        return s_result
    
    def remove_double_spaces(self, s: str) -> str:
        if s == "  ": return " "
        while "  " in s:
            s = s.replace("  ", " ")
        return s
    
    def remove_initial_spaces(self, s: str) -> str:
        while s[0] == " ":
            s = s[1:]
        return s
    
    def remove_final_spaces(self, s: str) -> str:
        while s[-1] == " ":
            s = s[:-1]
        return s
    
    def reverse_array(self, words: List[str]) -> List[str]:
        result = []
        j = len(words)-1
        while j >= 0:
            result.append(words[j])
            j -= 1          
        return result
    
    def concat_array(self, words: List[str]) -> str:
        s_result = ""
        i = 0
        for i in range(len(words)):
            s_result += words[i]
            if i != len(words)-1:
                s_result += " "
        return s_result

class Test:
    def test_basic(self):
        assert Solution().reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
        assert Solution().reverseWords("the sky is blue") == "blue is sky the"
        assert Solution().reverseWords("  hello world  ") == "world hello"
        assert Solution().reverseWords("a good   example") == "example good a"     
        assert Solution().reverseWords("Alice does not even like bob") == "bob like even not does Alice"

    def test_advanced(self):
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