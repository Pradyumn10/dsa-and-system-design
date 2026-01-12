"""
Date: Jan 12, 2026
Problem: https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """ 
        Time Complextiy: O(n)
        Space Complexity: O(1)
        """
        if x<2:
            return x
        else:
            i=2
            while i*i <=x:
                i+=1
            return i-1