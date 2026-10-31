class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # bucket[i] = list of numbers appearing i times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        # walk from highest freq down
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res