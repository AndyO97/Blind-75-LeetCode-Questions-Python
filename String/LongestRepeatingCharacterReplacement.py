# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.

# Solution:
# Use the sliding window technique.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #Count dictionary is maintained to keep count of the number of times a character was present in the window.
        ans = 0
                
        l = 0 # left pointer of the window
        for r in range(len(s)): #iterate through the string and keep updating the count dictionary after encountering every character in the string.
            count[s[r]] = 1 + count.get(s[r], 0) # (The keyname of the item you want to return the value from, and value to return if the specified key does not exist)
                    
            # A window can only have ( (length of window) - (frequency of maximum repeated character) ) number of swaps possible.        
            while (r - l + 1) - max(count.values()) > k: #could also be an if statement
                #Once k is exceeded, decrease by one the counter of the leftmost element, and shrink the window from the left.
                count[s[l]] -= 1
                l += 1

            #The length of the maximum valid substring is updated and stored in ans            
            ans = max(ans, r - l + 1)
                        
        return ans