'''
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:   #Negative numbers are not palindromes because of the negative sign
            return False
        
        rev = 0 #Reverse number, starts at 0 and will be built to compare to the original number
        num = x  #Copy of the original number.

        while num != 0:  #While there are still digits in the number.
            rev = rev * 10 + num % 10   #First it takes the last number of the original number and adds it to the reverse number,
                                        #which is multiplied by 10 to shift the digits to the left. For example, if the original number is 123, the reverse number will be 3, then 32, then 321.
            num = num // 10  #Removes the last digit of the original number.
        
        return rev == x  #Compares the reverse number to the original number. If they are the same, then the original number is a palindrome and the function returns true. Otherwise, it returns false.
        