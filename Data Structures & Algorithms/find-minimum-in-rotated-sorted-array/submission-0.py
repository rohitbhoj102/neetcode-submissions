class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0,len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[end]:
                # min is the right half (rotation point is there)
                start = mid + 1
            else:
                # right half is sorted; min is at the mid or to the left
                end = mid
            
        return nums[start]