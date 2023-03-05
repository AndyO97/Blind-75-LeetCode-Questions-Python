#1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order

class Solution(object):
    def twoSum(self, nums, target):
        #initialize dictionary
        values = {}
        #Loop throught the array once
        for idx, value in enumerate(nums):
            #Check if the difference of target and the element in the current iteration exists in the dictionary
            if (target - value in values):
                #if it exists, return the stored value in the dictionary (the index) and the current index
                return [values[target - value],idx]
            else:
                #else store the value in the dictionary
                values[value] = idx