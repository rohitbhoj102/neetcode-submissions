class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Algorithm: binary search on a rotated sorted array
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # target is in left sorted part
                else:
                    l = mid + 1 # target is in right unsorted part
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # target is in right sorted part
                else:
                    r = mid - 1 # target is in left unsorted part

        return -1
                