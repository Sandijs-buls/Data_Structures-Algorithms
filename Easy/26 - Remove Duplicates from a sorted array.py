'''
26. Remove Duplicates from a Sorted Array - LeetCode
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

My solution:

'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        j = 0 #This is one of the pointers used to keep track of the position of the last unique element in the array.
        for i in range(1, len(nums)): #Goes through the array starting from the second element
            if nums[j] != nums[i]: #If the current element is not the same as the last unique element, then it is a new unique element
                j += 1 #Add to the total of unique elements
                nums[j] = nums[i]  #Make the new sorted list without the duplicates.

        return j + 1 #Returns the total number of unique elements in the array, which is the length of the new sorted list without duplicates.
        