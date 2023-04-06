# Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Solution:
#  Start from the second last element of the list and move backwards until we reach the first element in the list.
# As we iterate through the list in reverse order, we determine if each position is good or bad. A position is good if it is possible to reach the last index from that position. Else, it is bad.



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        # minStepsRequired stores the minimum number of steps required to reach the most recent position that is considered good.
        minStepsRequired = 0
        # previousGood, on the other hand, stores the index of that position.
        # We initialise previousGood to the index of the last element in nums as we’ll be iterating nums backwards
        previousGood = len(nums)-1
        
        # work backwards and see if can reach final cell
        for i in range(len(nums)-2, -1, -1):
            # We find how many steps are required to jump from i to previousGood
            minStepsRequired = previousGood - i
            # We check if it is possible to jump from index i to previousGood, and if yes, update previousGood
            if nums[i] >= minStepsRequired:
                previousGood = i

        # After the loop, check if we reached index 0
        return previousGood == 0