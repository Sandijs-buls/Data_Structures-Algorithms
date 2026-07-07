```python
"""
Problem Number: 34
Problem Title: Find First and Last Position of Element in Sorted Array
Summary: Given a sorted array of integers and a target value, find the starting
         and ending position of the target in the array. If the target is not
         found, return [-1, -1].
Approach: Use binary search twice — once to find the leftmost (first) occurrence
          of the target and once to find the rightmost (last) occurrence.
          When the target is found, instead of returning immediately, the search
          continues in the appropriate direction (left or right) to find the
          boundary index, achieving O(log n) time complexity.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bin_search(nums, target, is_searching_left):

            left, right = 0, len(nums) - 1
            boundary_index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    boundary_index = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return boundary_index

        left = bin_search(nums, target, True)
        right = bin_search(nums, target, False)

        return [left, right]
```