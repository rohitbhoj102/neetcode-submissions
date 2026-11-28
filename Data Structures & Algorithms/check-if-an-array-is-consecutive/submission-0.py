class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        # sort nums
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return False
        return True