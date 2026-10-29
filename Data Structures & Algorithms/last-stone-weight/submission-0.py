import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate to turn min-heap into max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap) # heaviest
            y = -heapq.heappop(heap) # second heaviest
            if x != y:
                heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0