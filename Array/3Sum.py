# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_n, res = len(nums), []

        if len_n < 3: 
            return []

        nums.sort()

        for i, val in enumerate(nums):
            #Don't include element index 0 and skip repeated values as the solution was already found for those cases
            if i > 0 and val == nums[i - 1]:
                continue

            #Initialize 'l' one element to the right of the base element
            l, r = i + 1, len_n - 1

            while l < r:
                #Get sum of the current value of the outer loop, 'l' and 'r'
                three = val + nums[l] + nums[r]

                #if the sum is less than 0, increase the left pointer
                if three < 0:
                    l += 1
                #if the sum is greater than 0, increase the right pointer
                elif three > 0:
                    r -= 1
                #Otherwise, the sum is 0, and append the three values
                else:
                    res.append([val, nums[l], nums[r]])
                    #Then, increase the left pointer to try to find another solution with the current base element
                    l += 1
                    #Keep going left if the number is the same as the previous number. 
                    # Repeated values need to be skipped as the solution was already found for those cases.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res