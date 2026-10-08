class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Pick an earlier day to buy, a later day to sell, make sell - buy as large as possible, minimum 0.
        best = 0
        lowest = prices[0]

        for price in prices:
            best = max(best, price - lowest)
            lowest = min(lowest, price)

        return best