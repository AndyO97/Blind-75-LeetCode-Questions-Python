# Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#Logical solution
# Most optimized using O(1) space: 
# Use the first row or col to track 0s and at the end go back to update the first row and col with zeroes after we're done replacing the rest of the matrix. 
# The idea is to use the first row and first col of the matrix as a tracker.
# Steps:
#     1. At each row or col, if there is a zero, mark the corresponding first row or first col with a zero.
#     2. Then iterate through the array again to see where the first row and col were marked as zero and set that cell with 0.
#     3. Finally, check the first row and first col if there are any zeroes and if yes, set everything to 0 in the first row or first col.

# Time complexity for all three progression is O(m * n).

# Space: O(1) for modification in place and using the first row and first col to keep track of zeros instead of zeroes_row and zeroes_col

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Iterate through matrix to mark the 0s on the firts row and col
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # Iterate through matrix to update the cells to 0 if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # Update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0