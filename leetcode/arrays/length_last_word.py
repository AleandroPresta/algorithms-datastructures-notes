class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if (s.strip() == ""):
            return 0
        s1 = s.split(sep=' ')
        while('' in s1):
            s1.remove('')
        return len(s1[-1])
        

class Test:
    def test(self):
        assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
        assert Solution().lengthOfLastWord("Hello World") == 5  
        assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
        assert Solution().lengthOfLastWord("") == 0  # Edge case: empty string
        assert Solution().lengthOfLastWord(" ") == 0  # Edge case: string with only spaces
        assert Solution().lengthOfLastWord("a") == 1  # Single character
        assert Solution().lengthOfLastWord("a ") == 1  # Single character with trailing space
        assert Solution().lengthOfLastWord(" a") == 1  # Single character with leading space
        assert Solution().lengthOfLastWord("a b c") == 1  # Multiple single characters
        assert Solution().lengthOfLastWord("   ") == 0  # Edge case: multiple spaces
        assert Solution().lengthOfLastWord("word") == 4  # Single word without spaces
        assert Solution().lengthOfLastWord("word ") == 4  # Single word with trailing space
        assert Solution().lengthOfLastWord(" word") == 4  # Single word with leading space
        assert Solution().lengthOfLastWord("word  ") == 4  # Single word with multiple trailing spaces
        assert Solution().lengthOfLastWord("  word") == 4  # Single word with multiple leading spaces
        assert Solution().lengthOfLastWord("word1 word2 word3") == 5  # Multiple words

def main() -> None:
    test = Test()
    test.test()
    print('All tests passed')
    

if __name__ == '__main__':
    main()