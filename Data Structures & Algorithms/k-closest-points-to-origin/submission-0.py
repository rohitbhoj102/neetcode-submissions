import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0] * p[0] + p[1] * p[1]

        def partition(lo, hi):
            # Random pivot to avoid worst-case on adversarial input
            pivot_idx = random.randint(lo, hi)
            points[pivot_idx], points[hi] = points[hi], points[pivot_idx]
            pivot_dist = dist(points[hi])

            store = lo
            for i in range(lo, hi):
                if dist(points[i]) < pivot_dist:
                    points[i], points[store] = points[store], points[i]
                    store += 1
            points[store], points[hi] = points[hi], points[store]
            return store

        lo, hi = 0, len(points) - 1
        while lo < hi:
            p = partition(lo, hi)
            if p == k:          # pivot lands exactly at k
                break
            elif p < k:         # need more points on the right
                lo = p + 1
            else:               # too many, shrink to the left
                hi = p - 1

        return points[:k]  