"""
Date: Jan 18, 2026
Problem: https://leetcode.com/problems/single-number/
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        memory=[]
        for i in nums:
            if i in memory:
                memory.remove(i)
            else:
                memory.append(i)
        
        mem=int(''.join(map(str, memory)))
        return mem
