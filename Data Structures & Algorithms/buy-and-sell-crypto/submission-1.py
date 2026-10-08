class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Pick an earlier day to buy, a later day to sell, make sell - buy as large as possible, minimum 0.
        best = 0
        lowest = prices[0]

        # "consider each day as a possible SELL day"
        for price in prices: 
            # profit if we sell today = price - lowest
            best = max(best, price - lowest) 
            # then update the best BUY price so far
            lowest = min(lowest, price) 

        return best