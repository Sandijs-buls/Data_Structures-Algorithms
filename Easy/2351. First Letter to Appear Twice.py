'''
Easy.2351. First Letter to Appear Twice
Given a string s consisting of lowercase English letters, 
return the first letter to appear twice.

'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        let_map = {} #Dictionary to store the index of the first occurrence of each letter in the string.
        for i, let in enumerate(s): #Go through the string with index and character.
            if let in let_map: #Check if the letter has been seen before.
                return let #If it has, return the letter as it is the first letter to appear twice.
            let_map[let] = i #Store the index of the first occurrence of the letter in the dictionary.