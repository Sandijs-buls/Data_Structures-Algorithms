'''
Easy.2460. Apply Operations to an Array
You are given a 0-indexed array nums of size n consisting of non-negative integers. 
You need to apply the following operations to this array: 
if nums[i] == nums[i + 1], then nums[i] is doubled and nums[i + 1] is set to 0.
After performing all the operations, you need to move all the 0's to the end of
    the array while maintaining the relative order of the non-zero elements.

'''

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n -1) :
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        left = 0
    
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left] , nums[right]
                left += 1

        return nums     