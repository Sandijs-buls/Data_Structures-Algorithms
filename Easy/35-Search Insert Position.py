```python
"""
Problem Number: 35
Problem Title: Search Insert Position
Difficulty: Easy

Problem Summary:
    Given a sorted array of distinct integers and a target value, return the index
    if the target is found. If not, return the index where it would be inserted
    in order to maintain the sorted order.

Approach:
    Use binary search to efficiently locate the target or its insertion position.
    Narrow the search range by comparing the middle element to the target.
    If the target is not found, the left pointer will naturally settle at the
    correct insertion index once the search range is exhausted.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        idx = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left
```