# Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Concept:
# Rotating an image 90 degrees is equal to turning the columns into rows then reversing them

#Could also reverse the entire matrix and then turn the columns into rows. However this approach produces more runtime in Leetcode

# In cartesian coordinates (x, y), rotating by 90 degrees clockwise about the origin will turn the coordinates to (y, -x).


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
		# iterate through matrix
        for i in range(n):
            for j in range(i,n):
			
			    # transpose the matrix, turning rows into columns and vice versa
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			
			# reverse the resulting rows
            matrix[i].reverse()