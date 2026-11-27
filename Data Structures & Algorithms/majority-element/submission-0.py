class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        # create freq map
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        # iterate over the map and return the key whose count exceeds the n // 2 threshold
        for num, count in hashMap.items():
            if count > len(nums) // 2:
                return num