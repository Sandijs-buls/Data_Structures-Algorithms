```python
"""
Problem Number: 20
Problem Title: Valid Parentheses
Problem Summary: Given a string containing only the characters '(', ')', '{', '}', '[', and ']',
                 determine if the input string is valid. A string is valid if every open bracket
                 is closed by the same type of bracket in the correct order.
Approach: Use a stack to track opening brackets. When an opening bracket is encountered, push it
          onto the stack. When a closing bracket is encountered, check if the top of the stack
          holds the matching opening bracket. If not, or if the stack is empty, return False.
          After processing all characters, the string is valid only if the stack is empty.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0
```