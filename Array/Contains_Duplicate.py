# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        # size = len(nums)
        # mySet = set(nums)
        
        return not ( len(nums) == len(set(nums)) )
    
#Other Solution

# class Solution(object):
#     def containsDuplicate(self, nums):
        
#         hashNum = {}
#         for i in nums:
#             if i not in hashNum:
#                 hashNum[i] = 1
#             else:
#                 return True
#         return False