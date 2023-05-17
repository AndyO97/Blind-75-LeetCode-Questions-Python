# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Solution:
# Sliding window
# We use a dictionary to store the character as the key, the last appear index has been seen so far as value.
# seen[character] = index

# move the pointer when you met a repeated character in your window.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}   # dict for storing the characters and the index where they appeared the last time
        l = 0       # left pointer
        output = 0  # variable for storing the current length of the longest substring found until that moment
        for r in range(len(s)): # r is the right pointer
            # If s[r] is not in the dictionary seen, we can keep increasing the window size by moving right pointer
            if s[r] not in seen:
                output = max(output,r-l+1) # Check if the longest substring is the previous historic longest or if the current window has a longest substring
            # There are two cases if s[r] is in seen:
            else:
                # if s[r] is not inside the current window (the index where it appeared the last time is less than the left pointer), we can keep increasing the window
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                # else, if s[r] is inside the current window, we need to change the window by moving the left pointer to seen[s[r]] + 1.
                else:
                    l = seen[s[r]] + 1
            #Finally, update/add the index of the current char to the dict
            seen[s[r]] = r
        return output
