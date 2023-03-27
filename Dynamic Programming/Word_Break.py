# Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# https://leetcode.com/problems/word-break/solutions/43808/Simple-DP-solution-in-Python-with-description/comments/193111/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize array of booleans
        d = [False] * len(s)
        #loop for each element in string S  
        for i in range(len(s)):
            #Try for each word in the dictionary if there is a word that can segment and 
            # d[i-len(w)] was also segemented or the index i minus the length of the word is -1 
            # (the word matches the entire substring considered in the loop)
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]