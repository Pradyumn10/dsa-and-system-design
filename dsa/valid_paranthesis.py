"""
Date: Jan 10, 2026
Problem: https://leetcode.com/problems/valid-parentheses/description/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N) where N is length of the string
        Space Complexity: O(N) in worst case for stack
        """
        hashmap={')':'(', '}':'{', ']':'['}
        stack=[]
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                if stack==[] or hashmap[char]!=stack.pop():
                    return False
        return True if stack==[] else False


valid=Solution()
print(Solution.isValid(valid, s = "()"))
print(Solution.isValid(valid, s = "([)"))
print(Solution.isValid(valid, s = "[({})]"))