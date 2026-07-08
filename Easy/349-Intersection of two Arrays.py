```python
"""
Problem Number: 349
Problem Title: Intersection of Two Arrays
Summary: Given two integer arrays nums1 and nums2, return an array of their
         intersection, where each element in the result must be unique.
Approach: Convert both arrays to sets to eliminate duplicates, then iterate
          through the first set and check if each element exists in the second
          set. Collect matching elements into a result set and return it as a list.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set()

        for num in set1:
            if num in set2:
                inter.add(num)

        return list(inter)
```