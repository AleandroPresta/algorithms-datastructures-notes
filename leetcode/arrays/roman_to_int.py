'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four
is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

from typing import Dict, List

class Solution:
    mappings: Dict[str, int] = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    
    def romanToInt(self, s: str) -> int:
        l = self.parse(s)
        c = self.count(l)
        return c
        
    def parse(self, s:str) -> List[str]:
        # Input: MCMXCIV, Output: [M, CM, XC ,IV]
        result: List[str] = []
        # One literal string
        if len(s) == 1:
            result.append(s)
            return result
        i = 0
        ub = len(s)-1
        while(i <= ub):
            if (i != ub and s[i] == 'I' and s[i+1] == 'V'):
                result.append('IV')
                i += 2
                continue
            if (i != ub and s[i] == 'I' and s[i+1] == 'X'):
                result.append('IX')
                i += 2
                continue
            if (i != ub and s[i] == 'X' and s[i+1] == 'L'):
                result.append('XL')
                i += 2
                continue
            if (i != ub and s[i] == 'X' and s[i+1] == 'C'):
                result.append('XC')
                i += 2
                continue
            if (i != ub and s[i] == 'C' and s[i+1] == 'D'):
                result.append('CD')
                i += 2
                continue
            if (i != ub and s[i] == 'C' and s[i+1] == 'M'):
                result.append('CM')
                i += 2
                continue
            result.append(s[i])
            i += 1
        return result
    
    def count(self, l: List[str]) -> int:
        # Input: [M, CM, XC ,IV], Output: 1994
        total = 0
        for roman_number in l:
            total += self.mappings[roman_number] 
        return total
    
class Test:
    def test_basic(self):
        assert Solution().romanToInt("I") == 1
        assert Solution().romanToInt("V") == 5
        assert Solution().romanToInt("X") == 10
        assert Solution().romanToInt("XL") == 40
        assert Solution().romanToInt("XC") == 90
        assert Solution().romanToInt("CD") == 400
        assert Solution().romanToInt("CM") == 900
        
    def test_intermediate(self):
        assert Solution().romanToInt("IV") == 4
        assert Solution().romanToInt("IX") == 9
        assert Solution().romanToInt("X") == 10
        assert Solution().romanToInt("L") == 50
        assert Solution().romanToInt("C") == 100
        assert Solution().romanToInt("D") == 500
        assert Solution().romanToInt("M") == 1000
        
    def test_advanced(self):
        assert Solution().romanToInt("MCMXC") == 1990
        assert Solution().romanToInt("MCMXCIV") == 1994
        assert Solution().romanToInt("MMXX") == 2020
        assert Solution().romanToInt("MMMCMXCIX") == 3999
        assert Solution().romanToInt("MMMDCCCLXXXVIII") == 3888
        assert Solution().romanToInt("MMCDXLIV") == 2444
        assert Solution().romanToInt("MDCXCV") == 1695
        

def main() -> None:
    test = Test()
    test.test_basic()
    print('Basic tests passed')
    
    test.test_intermediate()
    print('Intermediate tests passed')
    
    test.test_advanced()
    print('Advanced tests passed')

if __name__ == '__main__':
    main()