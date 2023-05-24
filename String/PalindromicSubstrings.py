# Palindromic Substrings

# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
		
        palindromes = 0
        for i in range(len(s)):
		    # The idea is to expand around the 'center' of the string, but the center could be odd or even
			# e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
            palindromes += self.expand(s, i, i)
            palindromes += self.expand(s, i, i+ 1)
        return palindromes
    
    def expand(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # count the palindrome and expand outward
            count += 1
            left -= 1
            right += 1
        return count