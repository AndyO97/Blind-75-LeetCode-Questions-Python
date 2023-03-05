# Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        numsLen = len(nums)
 
        if numsLen == 1:
            return nums[0]
        
        l = 0
        r = numsLen - 1
        
        while l <= r:
            mid = (l + r) // 2
        
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
        
            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        
        

