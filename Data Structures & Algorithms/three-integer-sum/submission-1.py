class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array first 
        nums.sort()
        res = []

        # loop through the array of nums, 
        # for each num, assign it to variable a
        for i in range (len(nums)): # fix one
            # stop early check
            if nums[i] > 0:
                break
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two-sum the rest
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip dup here 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
        return res


