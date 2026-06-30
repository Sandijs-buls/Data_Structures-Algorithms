```python
"""
Problem Number: 1047
Problem Title: Remove All Adjacent Duplicates in String
Summary: Given a string, repeatedly remove adjacent duplicate characters
         until no adjacent duplicates remain, then return the final string.
Approach: Use a stack to track characters. For each character, if the top of
          the stack matches the current character, pop it (removing the pair).
          Otherwise, push the character onto the stack. Join the remaining
          stack elements to form the result.
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
```