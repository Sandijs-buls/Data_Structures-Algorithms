```python
"""
Problem Number: 3461
Problem Title: Maximum Sum of Distinct Subarrays
Summary: Given an integer array nums and an integer k, find the maximum sum
         of a subarray of length exactly k where all elements are distinct.
Approach: Use a sliding window of size k with a set to track unique elements.
          Expand the window by adding elements to the right, and shrink from
          the left whenever a duplicate is found or the window exceeds size k.
          Track the maximum sum whenever the window reaches exactly size k.
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        window = set()
        cur_sum = 0

        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while nums[r] in window or r - l + 1 > k:
                window.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = max(res, cur_sum)

            window.add(nums[r])
        return res
```