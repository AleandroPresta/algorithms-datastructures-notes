from typing import List, Dict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge Case
        if strs == []:
            return ""
        
        # Check if all the strings are empty
        if self.all_empty(strs):
            return ""
        
        # Single element list
        if len(strs) == 1:
            return strs[0]
        
        counts: Dict[str, int] = {}
        
        # Add all possible substrings to the dictionary
        for s in strs:
            self.add_substr(counts, s)
        
        max_occurrences = len(strs)
        
        # If there is no common prefix
        if max_occurrences == 1:
            return ""
        
        max_substr = ""
        
        for (key, value) in counts.items():
            if (value == max_occurrences and len(key) >= len(max_substr)):
                max_substr = key
        
        return max_substr
    
    def add_substr(self, counts: Dict[str, int], s: str) -> None:
        for i in range(len(s)):
            substr = s[0:i+1]
            if substr == '':
                continue
            if (substr in counts):
                counts[substr] += 1
            else:
                counts[substr] = 1
                
    def all_empty(self, strs: List[str]):
        all_empty_str = True
        
        for s in strs:
            if s != "":
                all_empty_str = False
                
        return all_empty_str

class TestLongestCommonPrefix:
    def test_common_prefix(self):
        assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
        assert Solution().longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
        assert Solution().longestCommonPrefix(["throne", "throne"]) == "throne"
        assert Solution().longestCommonPrefix(["throne", "throne", "throne"]) == "throne"
        assert Solution().longestCommonPrefix(["reflower","flow","flight"]) == ""

    def test_no_common_prefix(self):
        assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
        assert Solution().longestCommonPrefix(["throne", "dungeon"]) == ""
        assert Solution().longestCommonPrefix(["dog", "cat", "bird"]) == ""
        assert Solution().longestCommonPrefix(["apple", "banana", "cherry"]) == ""

    def test_edge_cases(self):
        assert Solution().longestCommonPrefix([]) == ""  # Edge case: empty list
        assert Solution().longestCommonPrefix([""]) == ""  # Edge case: single empty string
        assert Solution().longestCommonPrefix(["a"]) == "a"  # Single element list
        assert Solution().longestCommonPrefix(["", ""]) == ""  # Multiple empty strings
        assert Solution().longestCommonPrefix(["a", "a", "a"]) == "a"  # All elements are the same single character
        assert Solution().longestCommonPrefix(["ab", "a"]) == "a"  # Common prefix is a single character

def main() -> None:
    test = TestLongestCommonPrefix()
    test.test_common_prefix()
    print('Common prefix tests passed')
    
    test.test_no_common_prefix()
    print('No common prefix tests passed')
    
    test.test_edge_cases()
    print('Edge cases tests passed')

if __name__ == "__main__":
    main()