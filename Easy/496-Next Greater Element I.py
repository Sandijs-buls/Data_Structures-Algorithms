```python
"""
Problem Number: 496
Problem Title: Next Greater Element I
Summary: Given two arrays nums1 and nums2 (where nums1 is a subset of nums2),
         find the next greater element for each element in nums1 within nums2.
         The next greater element of a value x is the first element to the right
         of x in nums2 that is greater than x. Return -1 if no such element exists.
Approach: Use a monotonic stack to efficiently find the next greater element.
          Iterate through nums2, maintaining a stack of elements that haven't yet
          found their next greater element. When a greater element is found, pop
          elements from the stack and record the result. A hash map is used to
          quickly look up the index of nums1 elements for result placement.
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1idx[val]
                res[idx] = cur
            if cur in nums1:
                stack.append(cur)
            
        return res
```