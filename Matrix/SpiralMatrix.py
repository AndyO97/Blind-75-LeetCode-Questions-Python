# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Solution:
# 1. Append the first row, then update the index for beginning row (add 1)
# 2. Append the last column, then update the index for the ending column (decrease 1)
# 3. Append the last row, then update the index for ending row (decrease 1)
# 4. Append the first column, then update the index for the first column (add 1)
# Repeat steps 1 to 4 while the beginning row and column are greater or equal than the ending row and column, respectively 



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        # Get the index of the first row and column
        row_begin = 0
        col_begin = 0
        # Get the index of the last row and column
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            # Append all the elements of the beginning row
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            # Update the next beginning row
            row_begin += 1
            # Append all the elements of the ending column
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            # Update the next ending column (decrease 1)
            col_end -= 1
            # Verify that after the update, the ending row is greater or equal than the starting row
            if (row_begin <= row_end):
                # Append all the elements of the last row, but from end to start
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                # Update the next ending row (decrease 1)
                row_end -= 1
            # Verify that after the update, the ending column is greater or equal than the starting column
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                   # Append all the elements of the first column, but from end to start
                    res.append(matrix[i][col_begin])
                # Update the next starting column
                col_begin += 1
        return res