"""
Date: Jan 13, 2026
Problem: https://leetcode.com/problems/plus-one
"""
from traitlets import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        digits_str="".join(map(str,digits))
        digits_int=int(digits_str)+1
        k=[int(nums) for nums in str(digits_int)]
        return k
    
print(Solution().plusOne([9,9,9]))  # Output: [1,0,0,0]
print(Solution().plusOne([1,2,3]))  # Output: [1,2,4]