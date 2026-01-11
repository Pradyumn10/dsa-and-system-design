"""
Date: Jan 11, 2026
Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N) where N is number of elements in the array
        Space Complexity: O(1)
        """
        k=0
        for i, v in enumerate(nums):
            if i==0 or nums[i-1]!=v:
                nums[k]=v
                k+=1
        return k    
    

nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]

removeDuplicates=Solution()

k = removeDuplicates.removeDuplicates(nums)

assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

print("All assertions passed!")
