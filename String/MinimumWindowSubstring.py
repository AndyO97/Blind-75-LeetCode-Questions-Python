#Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t 
# (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Solution:
# Use the sliding window technique.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        # We use two hash maps: 
        # t_dict for keeping count of the frequency of each element in t, 
        # And window for keeping count of the frequency of each element in the substring of s that we are considering.
        t_dict, window = {}, {}
                
        # Set the t_dict dictionary        
        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0) # get (The keyname of the item you want to return the value from, and value to return if the specified key does not exist)
                    
        have, need = 0, len(t_dict) # Have is used to keep track how many characters we already have in the window and need is for the total number needed
        #res will have the l and r pointers and reslen will be used to keep track of the window length
        res, resLen = [-1, -1], float('inf') # float('inf') used to output infinity
        l = 0 # left pointer
                
        for r in range(len(s)):
            # Gradually move the right pointer to its right, until it forms a valid window that contains all the characters of string t.
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the number that we have and need matches, update have by 1        
            if c in t_dict and window[c] == t_dict[c]:
                have += 1
                        
            # If a valid window was obtained, we can now move the left pointer to its right, if we find a smaller window, we update the result with a smaller size.            
            while have == need:
                # update our result
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                            
                # pop from the left of the window
                window[s[l]] -= 1
                #Also verify if popping the leftmost element of the window affects 'have', if yes, update it
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -= 1
                            
                l += 1
                        
        l, r = res
        return s[l:r+1]