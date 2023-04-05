# Decode Ways
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)

# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Dynamic Programming can be used to solve this. 
# The idea comes from following thoughts: 
# - Assuming there is a string X(for example, ‘12’) and I knowing the ways to decode it are 2 ([1,2] or [12]). 
# - Lets append one more char (for example, ‘3’).
# - For the new string, the ways to decode it are:
# 2 (by decoding 3 to ‘C’ and geting [1,2,3] or [12,3]) + 1 (by decoding 3 with its previous char ‘2’, and then find the ways to decode the remaining string ‘1’ which is 1) = 3. 

# Concept:
# dp[i] = dp[i-1] + dp[i-2] if( 0 < s[i] + s[i-1] <= 26 )

class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0 or s[0] == '0':
            return 0
        # To make sure dp[i-1] and dp[i-2] are always valid, initiliaze dp=[1,1] and use dp[-1] and dp[-2] instead of dp[i-1] and dp[i-2]. 
        # The values of 1s assume there is always 1 way to decode (if not falling under return 0).
        dp = [1, 1]
        for i in range(1, size):       
            # Let's calculate for a string ending at index i, how many ways to decode it
            ways = 0
            # If s[i] is not 0, and the previous number and the current one are less than or equal to 26 
            # We can add dp[i-2] to the current ways of decoding.
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                ways += dp[-2]
            # If s[i] is not 0, we can add dp[i-1] to the current ways of decoding. Just s[i] will always be less than 26
            if s[i] != '0':
                ways += dp[-1]   
            # if dp[i] is 0, then immediately return 0 which means it’s impossible to decode the whole string.             
            if ways == 0:
                return 0
            # Update the number of ways to decode until the current index
            dp.append(ways)
        return dp[-1]