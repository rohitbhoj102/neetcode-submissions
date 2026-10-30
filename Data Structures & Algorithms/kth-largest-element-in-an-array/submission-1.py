import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k # index of kth largest in sorted order

        def partition(left, right):
            # random pivot guards against worst case sorted inputs
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]
            fill = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[fill], nums[i] = nums[i], nums[fill]
                    fill += 1
            nums[fill], nums[right] = nums[right], nums[fill]
            return fill

        left, right = 0, len(nums) - 1
        while left <= right:
            p = partition(left, right)
            if p == target:
                return nums[p]
            elif p > target:
                right = p - 1
            else:
                left = p + 1

        return nums[target]