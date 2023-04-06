# Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Assumptions:
# There is only one way to reach the left most edge and there is only one way to reach the bottom most edge. 
# So we init the first row and first column of 2D list with 1s:
# 1,1,1,1,1,1,1
# 1,x,x,x,x,x,x
# 1,x,x,x,x,x,x

# The robot can only move either down or right. For each target cell that the robot want to reach, it is either from the cell left from the target or from the cell up from the target. 
# Therefore, we need sum up target’s left cell and up cell to get the total path to reach the target cell. 

# s 1 1  1  1  1  1 
# 1 2 3  4  5  6  7
# 1 3 6 10 15 21 28

# When reach to the bottom-right corner, then number in the bottom-right corner will be the answer.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]