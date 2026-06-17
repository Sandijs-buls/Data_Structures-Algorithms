'''
Docstring for Easy.283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left] , nums[right] # This swaps the elements at the right and left pointers, effectively moving the non-zero element to the left and the zero to the right.
                left += 1

        return nums