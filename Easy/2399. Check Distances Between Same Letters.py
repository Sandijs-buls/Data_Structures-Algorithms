'''
Easy.2399. Check Distances Between Same Letters
Given a 0-indexed string s consisting of only lowercase English letters,
return true if the distance between every two equal letters is equal to the difference 
of their indices, otherwise return false.

'''
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        size = {} #Dictionary to store the index of the first occurrence of each letter in the string.
        for i, let in enumerate(s): # Iterate through the string with index and character.
            if let in size: #Check if the letter has been seen before.
                if distance[ord(let) - ord('a')] != i - size[let] - 1: #Check if the distance between the current index and the index
                                                                       #of the first occurrence of the letter is equal to the value in
                                                                       #the distance array for that letter.
                    return False 
            else:
                size[let] = i #Store the index of the first occurrence of the letter in the dictionary.
        return True
