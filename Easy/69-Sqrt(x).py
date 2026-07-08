```python
"""
Problem Number: 69
Problem Title: Sqrt(x)

Problem Summary:
    Given a non-negative integer x, return the square root of x rounded down
    to the nearest integer. The returned integer should be non-negative as well.
    You may not use any built-in exponent function or operator.

Approach:
    Use binary search between 1 and x // 2 to find the integer square root.
    At each step, compute the square of the midpoint and compare it to x.
    If the square equals x, return mid directly. If the square is less than x,
    search the right half; otherwise, search the left half. When the loop ends,
    'right' holds the floor of the square root.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
```