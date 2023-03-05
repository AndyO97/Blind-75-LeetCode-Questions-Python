# Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        if size == 1:
            return nums[0]
        
        maxProd = nums[0]
        minProd = nums[0]
        largProd = nums[0]
        
        #Loop through the list and store the max of the cumulative, the min of the cumulative
        #or start the subarray with the current value
        #Do the same for the min but for the min val, as the min multiplied by a negative number
        # can turn bigger than the previous max
        #Then check if the current prod is bigger than the previous max prod, and if yes, 
        #update the max prod
        for i in range(1, size):
            temp = maxProd
            maxProd = max(maxProd * nums[i], minProd * nums[i], nums[i])
            minProd = min(temp * nums[i], minProd * nums[i], nums[i])
            largProd = max(maxProd, largProd)
            
        return largProd