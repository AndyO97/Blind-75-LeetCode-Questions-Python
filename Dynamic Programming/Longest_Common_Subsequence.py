class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create an empty 2D array to store the lenght of the longest LCS until that element
        # There is an extra row and column to pad the array so that we 
        # don't run into problems when looking at our neighbouring cells 
        text1Len, text2Len = len(text1), len(text2)
    
        
        lcs_array = [[0 for x in range(text1Len+1)] for y in range(text2Len+1)] 

        for i in range(1, text2Len+1): #Loop for each index in text2 (actually the index is i-1 so starting from 0)
            for j in range(1, text1Len+1): #Loop for each index in text1 (actually the index is j-1 so starting from 0)
                if text1[j-1] == text2[i-1]: #If they match, set the previously found number of characters plus 1
                    lcs_array[i][j] = lcs_array[i-1][j-1] + 1
                else: #else find which previous iteration had the greatest LCS and assign it to array (i-1 or j-1)
                    lcs_array[i][j] = max(lcs_array[i-1][j], lcs_array[i][j-1])
                    
        return lcs_array[text2Len][text1Len]