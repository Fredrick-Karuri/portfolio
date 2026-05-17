class Solution:
    """
    THE PROBLEM: Find the maximum profit from buying on one day and selling on a future day 

    PATTERN: Two pointers / Greedy tracking

    INSIGHT: To maximize profit you want to buy at the lowest possible price seen so far
    amd sell at the current price. You do not need to check every pair of days; just 
    maintain the global minimum price and calculate potential profit at each step.

    THE PLAN: 
    1. Initializee min_price_so_far to infinity and max_profit to 0
    2. Iterate through each price in the prices array
    3. If the current_price is lower than the min_price_so_far, update min_price_so_far
    4. Otherwise, calculate current_profit (current_price - min_price_so_far)
    5. Update max_profit if current_profit is greater than the global max_profit
    6. Return max_profit

    Example: prices = [7, 1, 5, 3, 6, 4]
    - price = 7: min_price = 7, profit = 0
    - price = 1: min_price = 1, profit = 0
    - price = 5: profit = 5 - 1 = 4 -> max_profit = 4
    - price = 3: profit = 3 - 1 = 2 -> max_profit = 4
    - price = 6: profit = 6 - 1 = 5 -> max_profit = 5
    - price = 4: profit = 4 - 1 = 3 -> max_profit = 5
    Result: 5

    TIME: O(n) - Single pass through array of length n 
    SPACE: O(1) - Only using two variables to track minimum price and maximum profit

    """
    def maxProfit(self, prices: list[int]) -> int:
        min_price_so_far = float('inf')
        max_profit = 0

        for current_price in prices:
            if current_price < min_price_so_far:
                min_price_so_far = current_price
            else:
                current_profit = current_price - min_price_so_far
                max_profit = max(max_profit,current_profit)
        return max_profit