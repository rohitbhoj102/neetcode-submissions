class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                currentCount += 1
                maxCount = max(maxCount, currentCount)
            else:
                currentCount = 0

        return maxCount



        