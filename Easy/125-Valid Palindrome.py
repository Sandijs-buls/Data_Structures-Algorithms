```python
"""
Problem Number: 125
Problem Title: Valid Palindrome
Difficulty: Easy

Summary:
    Given a string s, determine if it is a palindrome considering only
    alphanumeric characters and ignoring cases.

Approach:
    First, filter the string to keep only alphanumeric characters and convert
    to lowercase. Then, use a two-pointer technique with one pointer starting
    at the beginning and the other at the end, moving inward while comparing
    characters. If any mismatch is found, return False; otherwise, return True.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
```