```python
"""
Problem Number: 28
Problem Title: Find the Index of the First Occurrence in a String
Difficulty: Easy

Problem Summary:
    Given two strings 'haystack' and 'needle', return the index of the first
    occurrence of 'needle' in 'haystack', or -1 if 'needle' is not part of
    'haystack'.

Approach:
    Iterate through all valid starting positions in 'haystack' where 'needle'
    could fit, and check if the substring of 'haystack' starting at each
    position matches 'needle'. Return the index of the first match found,
    or -1 if no match exists.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1
```