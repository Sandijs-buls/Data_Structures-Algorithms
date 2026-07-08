```python
"""
Problem Number: 268
Problem Title: Missing Number
Difficulty: Easy

Problem Summary:
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

Approach:
    Convert the list to a set for O(1) lookup, then iterate through all
    numbers from 0 to n (inclusive) and return the first number not found
    in the set.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
```