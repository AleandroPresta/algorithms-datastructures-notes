from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge cases
        if nums == []:
            return 0
    
        if len(nums) == 1:
            return 1
        
        i = 0
        k = 0
        while i < len(nums):            
            j = i+1
            first_occurrence = nums[i]
            
            while j < len(nums):
                second_occurrence = nums[j]
                rest_array = nums[j+1:]
                
                if first_occurrence not in rest_array:
                    break
                    
                # Exit case
                if nums[j:-1] == []:
                    break
                
                # Second element found
                if second_occurrence == first_occurrence:
                    # Remove all the other occurrences
                    while first_occurrence in rest_array:
                        rest_array.remove(first_occurrence)
                    nums[j+1:] = rest_array[:]
                    j += 1
                    break
                else:
                    j +=1
                    
            i += 1
            k += 1
            
        return k
    

class TestRemoveDuplicates:
    def test_basic(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = Solution().removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 1, 2, 2, 3]

        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = Solution().removeDuplicates(nums)
        assert k == 7
        assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]

        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        k = Solution().removeDuplicates(nums)
        assert k == 10
        assert nums[:k] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        k = Solution().removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 1]

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = Solution().removeDuplicates(nums)
        assert k == 10
        assert nums[:k] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_advanced(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        k = Solution().removeDuplicates(nums)
        assert k == 10
        assert nums[:k] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

        nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        k = Solution().removeDuplicates(nums)
        assert k == 8
        assert nums[:k] == [0, 0, 1, 1, 2, 2, 3, 3]

        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        k = Solution().removeDuplicates(nums)
        assert k == 18
        assert nums[:k] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        k = Solution().removeDuplicates(nums)
        assert k == 12
        assert nums[:k] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

        nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
        k = Solution().removeDuplicates(nums)
        assert k == 8
        assert nums[:k] == [1, 1, 2, 2, 3, 3, 4, 4]

    def test_edge_cases(self):
        nums = []
        k = Solution().removeDuplicates(nums)
        assert k == 0
        assert nums[:k] == []

        nums = [1]
        k = Solution().removeDuplicates(nums)
        assert k == 1
        assert nums[:k] == [1]

        nums = [1, 1]
        k = Solution().removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 1]

        nums = [1, 1, 1]
        k = Solution().removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 1]

        nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        k = Solution().removeDuplicates(nums)
        assert k == 9
        assert nums[:k] == [1, 2, 2, 3, 3, 4, 4, 5, 5]

def main() -> None:
    tester = TestRemoveDuplicates()
    
    tester.test_basic()
    print('Basic tests passed')
    
    tester.test_advanced()
    print('Advanced tests passed')
    
    tester.test_edge_cases()
    print('Edge case tests passed')
    

if __name__ == '__main__':
    main()