```python
"""
Problem Number: 278
Problem Title: First Bad Version
Summary: Given n versions of a product, find the first bad version where all
         versions after it are also bad. You have access to an API
         isBadVersion(version) that returns whether a version is bad.
Approach: Use binary search between 1 and n. If the middle version is bad,
          search the left half (the first bad version could be earlier).
          If it's not bad, search the right half. The left pointer will
          converge on the first bad version.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
```