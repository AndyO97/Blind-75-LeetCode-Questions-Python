# Longest Palindromic Substring

# Given a string s, return the longest palindromic
# substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"




class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        # longestPalindrome() iterates over every pair and individual character of the string (to account for odd and even lengths of the final palindrome).
        # Odd palindromes don't consider the middle value, while even palindromes have pairs with each element.
        for i in range(len(s)):
            # In each iteration, the get_palindrome() function expands for every index until it finds the largest palindrome
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=len)
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # print('Using: ',l,', ',r,' string: ', s[l+1:r])
        return s[l+1:r] # If l+1 >= r, an empty string is returned, 
        #both initial params of the function return an empty string if at least the while loop was not true once
        #l+1 is used to return the previous iteration that was the one that had the correct palindrome, r-1 i not required as the upper limit is reduced by one by default 