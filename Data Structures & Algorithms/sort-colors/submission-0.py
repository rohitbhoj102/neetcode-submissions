class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  we know nums only contains 0, 1 or 2 -> bucket sort        
        counts = [0, 0, 0]

        # Count the quantity of each val in nums
        for num in nums:
            counts[num] += 1

        # fill each bucket in original array
        i = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1


        