class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def hours_needed(k):
            total = 0
            for p in piles:
                # ceil(p / k) using integer math
                total += (p + k - 1) // k
            return total

        while low < high:
            mid = (low + high) // 2
            if hours_needed(mid) <= h:
                high = mid
            else:
                low = mid + 1

        return low