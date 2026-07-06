```python
"""
Problem Number: 205
Problem Title: Isomorphic Strings
Problem Summary: Given two strings s and t, determine if they are isomorphic.
                 Two strings are isomorphic if the characters in s can be replaced
                 to get t, where each character maps to exactly one unique character
                 and no two characters map to the same character.
Approach: Use two hash maps to maintain bidirectional character mappings between
          s and t. For each character pair, verify that existing mappings are
          consistent. If any mapping conflict is found, return False; otherwise,
          return True after processing all characters.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}

        for char1, char2 in zip(s, t):
            if char1 in st:
                if st[char1] != char2:
                    return False
            else:
                st[char1] = char2
            
            if char2 in ts:
                if ts[char2] != char1:
                    return False
            else:
                ts[char2] = char1
        
        return True
```