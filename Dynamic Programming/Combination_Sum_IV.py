#Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.

# Dictionary and recursion are used to solve the problem
# The idea is that target = sum(target - nums[1] , target - nums[2], ..., target - nums[n-1]), as eventually one num should be equal to target
# Therefore, a recursive function can be used: 
# target = search(target - nums[1]) + search(target - nums[2]) + ... + search(target - nums[n-1]) where n is the number of nums
# Or in another words, the number of combinations that add up to target is = combinationsFor(target - nums[1]) + combinationsFor(target - nums[2]) + ... + combinationsFor(target - nums[n-1])
# In some cases if a solution doesn't exist for combinationsFor(target - nums[x]) with the available nums, the function will just return 0.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize dictionary and ways to add up to index 0
        dp = {}
        dp[0] = [1]

        # Sorting and the additional else, add a little runtime, so commented
        # nums = sorted(nums)

        def search(target):
            # If already found the number of combinations for (target - num), return it
            if target in dp:
                return dp[target]
            
            #Initialize the number of combinations to 0
            comb_sum = 0
            # Loop for each number in nums
            for num in nums:
                # Verify that the number in question is smaller than target (it can't be greater as it will not add up to target)
                if num < target:
                    comb_sum += search(target - num)
                # If num is equal to target, a combination was found, therefore, add 1 to the cumulative
                elif target == num:
                    comb_sum += 1
                # else:
                #     break
            
            #Before exiting recursive call, update the number of combinations for current target (to prevent repetitions on future calls)
            dp[target] = comb_sum
            return comb_sum

        return search(target)