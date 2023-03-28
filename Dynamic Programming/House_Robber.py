# House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping 
# you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        #Verify special cases if nums has less than 3 numbers
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums[0], nums[1])
        # Initialize the two previous houses max values
        house_minus2 = nums[0]
        house_minus1 = max(nums[0], nums[1])
        house_current = 0
        # loop starting from index 2
        for i in range(2, len(nums)):
            #Check if the greatest value is obtained by considering or ignoring the current value
            house_current = max((nums[i] + house_minus2),house_minus1)
            #Update the previous 2 houses
            house_minus2 = house_minus1
            house_minus1 = house_current
            
        return house_current