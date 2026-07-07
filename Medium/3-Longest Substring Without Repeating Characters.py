```python
"""
Problem Number: 3
Problem Title: Longest Substring Without Repeating Characters
Problem Summary: Given a string s, find the length of the longest substring
                 that contains no repeating characters.
Approach: Uses a sliding window technique with two pointers (l and r) and a 
          frequency counter (defaultdict). The right pointer expands the window 
          by adding characters, and when a duplicate is detected (count > 1), 
          the left pointer shrinks the window until the duplicate is removed. 
          The maximum window size seen is tracked and returned as the result.
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        l = 0
        counter = defaultdict(int)
        
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
```