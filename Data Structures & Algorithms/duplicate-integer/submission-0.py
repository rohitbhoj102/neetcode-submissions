class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        added = []
        for i in range(0, len(nums)):
            if nums[i] in added:
                return True
            added.append(nums[i])
        return False
        