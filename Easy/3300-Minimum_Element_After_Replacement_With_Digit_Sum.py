'''
3300. Minimum Element After Replacement With Digit Sum - LeetCode
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

nums = [1, 15, 6, 3]

My solution:
'''
from python3 import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 37
        for num in nums: #Goes through each element in the array
            dig = 0  #Finds the sum of the digits in the element
            while num > 0: #While there are still digits in the element
                dig += num % 10 #Adds the last digit of the element to the sum - 101 becomes 1 + 0 + 1 = 2
                num //= 10 #Removes the last digit of the element - 101 becomes 10, then 1, then 0
            ans = min(ans, dig)  #Compares the sum of the digits to the current minimum and updates the minimum if necessary
        return ans #Returns the minimum element in the array after all replacements
        
        