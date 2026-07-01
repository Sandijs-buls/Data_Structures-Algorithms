```python
"""
Problem Number: 3174
Problem Title: Clear Digits
Summary: Given a string containing letters and digits, repeatedly remove the first
         digit and the closest non-digit character to its left until no digits remain.
         Return the resulting string.
Approach: Use a stack to simulate the process. Iterate through each character -
          if it's a letter, push it onto the stack. If it's a digit, pop the top
          element from the stack (removing the closest left non-digit character).
          Join and return the remaining stack elements as the result.
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        
        string = []

        for char in s:
            if char.isdigit():
                if string:
                    string.pop()

            else:
                string.append(char)
            
        return ''.join(string)
```