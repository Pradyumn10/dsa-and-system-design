"""
Date: Jan 9, 2026
Problem: https://leetcode.com/problems/longest-common-prefix/description/
Explanation:
https://leetcode.com/problems/longest-common-prefix/solutions/7480185/please-upvote-by-pradyumn10-9yre/
"""

from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time Complexity: O(N*M^2) where N is number of strings and M is length of the smallest string
        (String slicing i[0:len(min_str)] in the comparison adds an extra M factor)
        Space Complexity: O(1)
        """
        if strs is None or len(strs) == 0:
            return ""
        min_str=min(strs, key=len)
        strs.pop(strs.index(min_str))
        for i in strs:
            while min_str!=i[0:len(min_str)]:
                min_str=min_str[0:len(min_str)-1]
                if min_str=="":
                    return ""
        return min_str

commonPrefix=Solution()
print(commonPrefix.longestCommonPrefix(["flower","flow","flight"]))
print(commonPrefix.longestCommonPrefix(["dog","racecar","car"]))