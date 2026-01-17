"""
Date: Jan 17, 2026
Problem: https://leetcode.com/problems/search-insert-position/
"""
from typing_extensions import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if target in nums:
            return nums.index(target)
        else:
            left, right=0, len(nums)-1
            while left <= right:
                mid=left+(right-left)//2
                if nums[right]<target:
                    return right+1
                elif nums[left]>target:
                    return left
                elif nums[mid]>target and nums[mid-1]<target:
                    return mid
                elif nums[mid]<target and nums[mid+1]>target:
                    return mid+1
                else:
                    right=right-1
                    left=left+1

sol=Solution()
#print(sol.searchInsert([1,3,5,6],5))  #2
#print(sol.searchInsert([1,3,5,6],2))  #1 
#print(sol.searchInsert([1,3,5,6],7))  #4
#print(sol.searchInsert([1,3,5,6],0))  #0
#print(sol.searchInsert([1,3],2))  #1
print(sol.searchInsert([3,6,7,8,10],5))  #4