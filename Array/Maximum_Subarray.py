# Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        if size == 1:
            return nums[0]
        
        totalSum = nums[0]
        maxSum = nums[0]
        
        #Loop through the list and store the max of the cumulative or the current value
        #Then check if the selected value is bigger than teh previous max sum, and if yes, update the max
        #sum
        for i in range(1, size):
            totalSum = (max(totalSum + nums[i], nums[i]))
            maxSum = max(maxSum, totalSum)
            
        return maxSum