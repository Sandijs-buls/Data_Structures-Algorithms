'''
27. Remove Element - LeetCode
Given an integer array nums and an integer val, remove all occurrences of val in the array

My solution:

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k