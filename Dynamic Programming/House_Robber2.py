# House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place 
# are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without 
# alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        #Verify special cases if nums has less than 3 numbers
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums[0], nums[1])
        # Check for three as the loops don't consider this case
        if(len(nums) == 3):
            return max(nums[0], nums[1], nums[2])
        # Initialize the two previous houses max values
        house_minus2 = nums[0]
        house_minus1 = max(nums[0], nums[1])
        house_current = 0
        # loop starting from index 2
        # Don't consider the last element
        for i in range(2, len(nums)-1):
            #Check if the greatest value is obtained by considering or ignoring the current value
            house_current = max((nums[i] + house_minus2),house_minus1)
            #Update the previous 2 houses
            house_minus2 = house_minus1
            house_minus1 = house_current

        house_minus2 = 0
        house_minus1 = nums[1]
        house_current2 = 0
        # Don't consider the first element
        for i in range(2, len(nums)):
            #Check if the greatest value is obtained by considering or ignoring the current value
            house_current2 = max((nums[i] + house_minus2),house_minus1)
            #Update the previous 2 houses
            house_minus2 = house_minus1
            house_minus1 = house_current2
        # Return the biggest solution among the two
        return max( house_current, house_current2 )