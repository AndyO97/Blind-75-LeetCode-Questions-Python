# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        
        #if the array is empty return o profit
        if len(prices) == 0:
            return 0
        else:
            #Initialize the max profit to 0 and the min price to the first element
            max_profit = 0
            min_price = prices[0]
            #Loop once throught the array
            for price in prices[1:]:
                profit = price - min_price
                max_profit = max(profit, max_profit)
                min_price = min(min_price, price)

            return max_profit