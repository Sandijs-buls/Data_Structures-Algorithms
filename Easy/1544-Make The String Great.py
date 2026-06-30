```python
"""
Problem Number: 1544
Problem Title: Make The String Great
Problem Summary: Given a string, repeatedly remove adjacent characters that are the
    same letter but different cases (e.g., 'aA' or 'Aa') until no such pairs remain,
    then return the resulting "good" string.
Approach: Use a stack to process each character. For each character, check if the top
    of the stack is the same letter in the opposite case. If so, pop the stack (removing
    the bad pair); otherwise, push the current character. The final stack represents
    the good string.
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
            
        return ''.join(stack)
```