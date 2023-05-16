# Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Count number of each different type of letter in board and store it in a dictionary
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1 #Adding one each time the letter is found again

        # Count number of letters in word
        # Use Counter, a subclass of dict that's specially designed for counting hashable objects in Python. 
        # It is a dictionary that stores objects as keys and counts as values.
        wordDic = Counter(word)
        for c in wordDic:
            # Check if board has all the letters in the word and they are at least same count from word
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        # Traverse through board and if word[0] == board[i][j], call the DFS function
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):  
                        return True

        return False

    # k is used to keep track of the index of the word being checked
    def dfs(self, i, j, k, board, word):
        # Recursion will return False if (i,j) is out of bounds 
        # or if board[i][j] != word[k] which is the current letter we need
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or k >= len(word) or word[k] != board[i][j]:
            return False

        # If k is equal to the lengh of the word, it means that we have verified the last letter in the word 
        # Then, we can return True
        if k == len(word) - 1:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:

            # Since we can't use the same letter twice, change current board[i][j] to -1 before traversing further
            tmp = board[i][j]
            board[i][j] = -1
            
            # If dfs returns True, return True for no more dfs
            if self.dfs(i + x, j + y, k + 1, board, word): 
                return True

            #If not true, reset the old value, before trying another route
            board[i][j] = tmp