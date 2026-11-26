import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies with hashmap
        countMap = {}
        
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        # can use heap here to find k largest (frequent) elements
        return heapq.nlargest(k, countMap, key=countMap.get)

