# Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing
# subsequence.
# Algorithm: Starting at the end and looping until the end (range(i + 1, len(nums))) to find the LIS for each index
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the array to hold the Longest Increasing Subsequence for each index
        LIS = [1] * len(nums)

        # Start looping through all the values backwards
        for i in range(len(nums) - 1, -1, -1):
            #Another loop that goes from i+1 to the last value in the array
            for j in range(i + 1, len(nums)):
                # Determine if the current value (nums[i]) can be added onto LIS[j] subsequence (since we are working backwards it has to be less than nums[j]). 
                # If it is then set the current LIS to the max of itself and 1 plus LIS[j].
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)