'''
Easy.242-Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
In the range a to z     
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Check if the lengths of the strings are different.
            return False    #If they are, return false

        counter = {}  #Hash map / dictionary to store the count of each character in the first string.

        for char in s:  # Count the occurrence of each character in the first string
            counter[char] = counter.get(char, 0) + 1  # Increment the count of the character

        for char in t:  # Check each character in the second string
            if char not in counter or counter[char] == 0:  # If the character is not in the counter or its count is 0
                return False  # Return false
            counter[char] -= 1  # Decrement the count of the character

        return True  # Return true if all characters match
