```python
"""
Problem Number: 168
Problem Title: Excel Sheet Column Title
Summary: Given an integer columnNumber, return its corresponding column title
         as it appears in an Excel spreadsheet (e.g., 1 -> A, 26 -> Z, 27 -> AA).
Approach: Treat the problem like a base-26 conversion, but since Excel columns
          are 1-indexed (A=1, not 0), decrement columnNumber by 1 before each
          modulo operation to shift the range from 1-26 to 0-25, then map each
          remainder to the corresponding letter using chr() and prepend it to
          the result string. Repeat until columnNumber reaches 0.
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res = chr((columnNumber % 26) + ord("A")) + res
            columnNumber //= 26

        return res
```