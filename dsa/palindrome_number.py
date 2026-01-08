"""
Date: Jan 8, 2026
Problem: https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Time Complexity: O(n) where n is the number of digits in the integer.
        Space Complexity: O(n) for storing the reversed string representation of the integer.
        """
        y=str(x)[::-1]
        if str(x)==y:
            return True
        else:
            return False
        
isPalin=Solution()
result=isPalin.isPalindrome(121)
print(result)
result2=isPalin.isPalindrome(-121)
print(result2)