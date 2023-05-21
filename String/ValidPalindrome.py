# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the 
# same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i starts at beginning of s and j starts at the end         
        i, j = 0, len(s) - 1
        # While i is still before j        
        while i < j:
            # If i is not an alpha-numeric character then advance i            
            if not s[i].isalnum():
                i += 1
            # If j is not an alpha-numeric character then advance i
            elif not s[j].isalnum():
                j -= 1
            # Both i and j are alpha-numeric characters at this point.Therefore, if they do not match return false
            elif s[i].lower() != s[j].lower():
                return False
            # Otherwise characters matched and we should look at the next pair of characters
            else:
                i, j = i + 1, j - 1
        # Finally, the entire string was verified and we return true         
        return True