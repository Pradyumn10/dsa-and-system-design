"""
Date: Jan 6, 2026
Problem: https://leetcode.com/problems/two-sum/description/
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        * Loop through each element using nested loops.
        * For each pair of elements, check if their sum equals the target.
        * If found, return the indices of the two elements.

        Time Complexity: O(n^2) - because of the nested loops
        Space Complexity: O(1) - no additional space used
        '''
        len_nums=len(nums)
        target_value=[]

        for index1, value1 in enumerate(nums):
            for index2,value2 in enumerate(nums):    
                if len_nums==2 and nums[index1]+nums[index2+1]==target:
                    target_value.append(index1)
                    target_value.append(index2+1)
                    return target_value
                if nums[index1]+nums[index2]==target and index1!=index2:
                    target_value.append(index1)
                    target_value.append(index2)
                    return target_value
    
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        '''
        * Loop through each element while storing the elements in a hash map (dictionary).
        * For each element, calculate the complement (target - current element) and check if it exists in the hash map.
        * If found, return the indices of the two elements.

        Time Complexity: O(n) - single pass through the list
        Space Complexity: O(n) - additional space for the hash map
        '''
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
        return []

two_sum=Solution()
print(two_sum.twoSum([3,2,3],6))  # Output
print(two_sum.twoSum2([3,2,3],6))  # Output

# Additional test cases
#print(two_sum.twoSum([2,7,11,15],9))  # Output
#print(two_sum.twoSum([3,3],6))  # Output
#print(two_sum.twoSum([3,2,4],6))  # Output


