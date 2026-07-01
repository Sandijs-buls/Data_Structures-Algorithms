```python
"""
Problem Number: 1614
Problem Title: Maximum Nesting Depth of the Parentheses
Summary: Given a valid parentheses string, return the maximum nesting depth
         of the parentheses.
Approach: Use a stack to track open parentheses. Increment a counter for each
          closing parenthesis encountered, and reset when popping from the stack.
          The length of the remaining stack represents the maximum depth.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        longest = 0

        for char in s:
            if char == ')':
                stack.append(char)
                longest += 1
            elif char == '(':
                if stack:
                    stack.pop()
                    longest = 0
            
        return len(stack)
```