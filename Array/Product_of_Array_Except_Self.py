# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        result = 1
        zeros = 0
        for x in nums:
            if(x != 0):
                result = result * x
            else:
                zeros += 1
                if zeros > 1:
                    result = 0
                    break
        #print(result)
        
        if(zeros == 1):
            return [0 if i!= 0 else result for i in nums]
        
        if(zeros > 1):
            return [0 for i in nums]
            
        return [result/i if i!= 0 else 0 for i in nums]
        
        
        