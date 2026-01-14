"""
Date: Jan 14, 2026
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time Complexity: O(n*m) where n is the length of haystack and m is the length of needle
        Space Complexity: O(1)
        """
        needleList=[val for val in needle] 
        if needle in haystack:
            for i,v in enumerate(haystack):
                if needleList[0]==haystack[i]:
                    haystackValu=haystack[i:i+len(needle)]
                    if haystackValu==needle:
                        return i
            return 0
        else:
            return -1
        
# Example usage:
solution = Solution()
print(solution.strStr("hello", "ll"))  # Output: 0