# Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        #Number of ways to reach Step n = Number of ways to reach Step (n-1) + Number of ways to reach Step (n-2).
        prevPrev = 1
        prev = 2
        current = 0
        

        for step in range(3, n+1):
            # Calculate Number of Ways to Reach Current Step
            current = prevPrev + prev
            # Update Pointers for Next Step
            prevPrev = prev
            prev = current

        return current