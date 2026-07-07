```python
"""
Problem Number: 153
Problem Title: Find Minimum in Rotated Sorted Array
Problem Summary: Given a sorted array that has been rotated between 1 and n times,
                 find the minimum element in O(log n) time.
Approach: Use binary search to find the pivot point (minimum element). Compare the
          middle element with the last element to determine which half contains the
          minimum. If nums[mid] <= nums[-1], the minimum is in the left half
          (including mid), so we store mid as a candidate and search left. Otherwise,
          the minimum must be in the right half, so we search right.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[idx]
```