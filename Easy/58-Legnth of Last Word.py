```python
"""
Problem Number: 58
Problem Title: Length of Last Word
Difficulty: Easy

Problem Summary:
    Given a string `s` consisting of words and spaces, return the length of the
    last word in the string. A word is defined as a maximal substring consisting
    of non-space characters only.

Approach:
    Split the string using Python's built-in `split()` method, which automatically
    handles multiple spaces and leading/trailing whitespace. Then return the length
    of the last element in the resulting list.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        return len(words[-1])
```