# Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize array to keep track of minimum amount of coins needed to sum to the amount
        #  Set every index to the amount plus one.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                # Checking which one coin plus the amount required to reach the current value, takes the least amount of coins. 
                # Check that the coin is less than or equal to the amount
                if c <= a:
                    # Find the minimum number of coins to get the actual amount
                    # Set the index in the array to the minimum of:
                    # -If another coin worked previously in the loop, the updated number of coins will be here. 
                        # Otherwise, it will have amount + 1 as the value (As initialized in the array) which will never be the minimum.
                    # -Or the amount of coins it took to get to the current amount minus the actual coin and add a coin of that value 
                        # Will also set to one the number of coins if the curent coin value is equal to the current amount (1 + dp[x - x] = 1).
                    # This will get the minimum amount of coins need to reach the current amount. 
                    
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # After the top loop is finished return that amount of coins it took to reach the amount as long as it isn’t equal to the amount plus 1 (The value with which it was initialized). 
        # If it is equal to that value, return -1 since no combination of coins can reach that value.
        return dp[amount] if dp[amount] != amount + 1 else -1